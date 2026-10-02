# Văn thư phát hành chuyển VB đi — hướng dẫn MOBILE dùng API

**Phân hệ:** `van-ban/di` · **BE:** gen-2 `com.viettel.office.controller.VhrOrgController` · **Ngày:** 2026-09-16 · Mô tả web/BE chi tiết: `2026-09-16-van-thu-phat-hanh-chuyen-vb-di-web.md`.

> **Cập nhật 2026-10-02 — bỏ điều kiện "ngang cấp":** lấy **mọi đơn vị có mã định danh** (mọi cấp, mọi nhánh) lên cây, không còn xét cùng độ sâu `path`. Ngoài ra **mọi đơn vị cấp 0** luôn chọn được, không xét mã (không phụ thuộc đơn vị ban hành ở cấp nào). **API, request, field response giữ nguyên** — mobile vẫn chỉ hiển thị theo `selectable`/`isLeaf` BE trả; chỉ khác: đơn vị có mã ở nhánh khác giờ có thể `isLeaf = 0` (mở được để thấy đơn vị con **có mã** của nó).

> **Cập nhật 2026-10-02 (2) — phạm vi CÁ NHÂN tách riêng, hẹp hơn đơn vị:** cá nhân chỉ trong **đơn vị ban hành + con cháu**; riêng đơn vị ban hành là **VPUB** (`sysOrganization.id.vpub` = `9133615`) thì thêm cá nhân của **chính đơn vị cha trực tiếp (UBND tỉnh)** — **không** lấy các Sở/đơn vị con khác của UBND. `scope` thêm `userOrgIds`, `userRootOrg`; `org-ids` giờ trả theo phạm vi cá nhân. Chi tiết: `2026-09-16-van-thu-phat-hanh-loc-user-mobile.md`.

## 1. Khi nào áp dụng

Áp dụng **đúng** khi tất cả điều kiện sau đúng (mobile tự xét, BE không xét):

| # | Điều kiện | Mobile lấy từ đâu |
|---|---|---|
| 1 | User có role văn thư | thông tin đăng nhập / role |
| 2 | User là văn thư của **chính đơn vị ban hành** (`document.builtGroupId`) | role "VT" tại đơn vị `builtGroupId` |
| 3 | Chuyển **văn bản đi** (`transferDirection = out`), chuyển **1** văn bản | |
| 4 | Văn bản **đơn vị** (không phải phạm vi "văn bản cá nhân") | web: `orgRangeState != 1` |
| 5 | Màn *Văn bản ban hành*: tab Đã cấp số / Đã ban hành / Tất cả, hoặc *Chờ cấp số* **sau khi cấp số** | web: `viewType ∈ {8, 9, 10}`; sau cấp số coi như tab Đã cấp số |

Không thỏa → dùng cây/tìm kiếm đơn vị như hiện tại của mobile.

## 2. Quy tắc phạm vi (BE đã tính, mobile chỉ hiển thị)

Được chọn: **cấp cha** của đơn vị ban hành + **đơn vị ban hành** + **toàn bộ con cháu** của nó + **mọi đơn vị có mã định danh** (`identifierCode` khác null) — **không xét cấp/độ sâu, không cần cùng cha**.

Ngoài ra **mọi đơn vị cấp 0** (`path` dạng `/1/<id>/`, độ sâu 2) đều chọn được, có mã hay không — áp dụng cho mọi đơn vị ban hành, không cần đơn vị ban hành là cấp 0.

Ở nhánh khác (ngoài nhánh đơn vị ban hành): chỉ đơn vị **có mã** mới chọn được; đơn vị **không có mã** chỉ hiện khi nó là tổ tiên của một đơn vị có mã, và chỉ là node để mở cây (`selectable = false`). Con **không có mã** của một đơn vị có mã ở nhánh khác **không** hiện.

Mobile không cần tự tính — dùng `selectable`/`isLeaf` BE trả.

## 3. API

Cả 3 là `POST`, `Content-Type: application/json`, JWT như các API `/api/**` khác. Cả 3 dùng chung 1 class request `GetDocManagerTransferDTO {builtOrgId, parentOrgId, orgId}`; mỗi API chỉ dùng field của nó (children → `parentOrgId`, org-ids → `orgId`), key giữ nguyên như đã thống nhất. Response bọc chuẩn gen-2:

```json
{ "result": { "mess": { "errorCode": 0, "message": "..." }, "data": <payload>, "status": ..., "timestamp": "..." } }
```
`errorCode = 0` thành công; `data` null/rỗng khi không có dữ liệu (NODATA).

### 3.1 `POST /api/vhr-org/get-doc-manager-transfer-children` — lazy-load 1 cấp cây

Gọi **mỗi lần mở một node** (và 1 lần cho gốc). Chỉ trả con trực tiếp **có liên quan** đến phạm vi.

Request:
```json
{ "builtOrgId": 9133734, "parentOrgId": null }
```
- `builtOrgId` (bắt buộc): `document.builtGroupId`.
- `parentOrgId`: id node đang mở; **null = lấy các node gốc** (độ sâu 1).

Response `data`: mảng `VhrOrgResponseDTO`, các field cần dùng:

| Field | Kiểu | Ý nghĩa |
|---|---|---|
| `sysOrganizationId` | Long | id đơn vị |
| `name`, `abbreviation`, `code` | String | hiển thị |
| `path` | String | `/1/148842/9133734/` |
| `orgParentId` | Long | cha |
| `orderNumber` | Long | đã sort theo `orderNumber, name` |
| `identifierCode` | String | mã định danh (null nếu không có) |
| **`selectable`** | Boolean | `true` = cho tick chọn; `false` = chỉ để mở cây (ẩn/disable ô chọn) |
| **`isLeaf`** | Long 0/1 | `1` = không có con liên quan → không hiện nút mở; `0` = có thể mở (gọi tiếp API với `parentOrgId` = id node). Đơn vị ngoài nhánh đơn vị ban hành: `0` khi còn hậu duệ có mã |

Ví dụ (đơn vị ban hành = Sở A `9133734`, path `/1/148842/9133734/`):

```
POST children {builtOrgId: 9133734, parentOrgId: null}
→ [ {id:1,      name:"Tỉnh Khánh Hòa", selectable:true,  isLeaf:0} ]        // tổ tiên

POST children {builtOrgId: 9133734, parentOrgId: 1}
→ [ {id:148842, name:"UBND tỉnh",      selectable:true,  isLeaf:0},         // tổ tiên
    {id:200001, name:"Tỉnh ủy",        selectable:true,  isLeaf:0},         // có mã → chọn được; mở được vì có Ban có mã
    {id:200500, name:"Khối X",         selectable:false, isLeaf:0} ]        // không mã, chỉ để mở (có con có mã)

POST children {builtOrgId: 9133734, parentOrgId: 148842}
→ [ {id:9133734, name:"Sở A",          selectable:true,  isLeaf:0},         // đơn vị ban hành, mở được → phòng ban
    {id:9133745, name:"Sở B",          selectable:true,  isLeaf:0},         // có mã, có Chi cục có mã → mở được
    {id:9133747, name:"Sở C",          selectable:true,  isLeaf:1} ]        // có mã, không còn con có mã → lá

POST children {builtOrgId: 9133734, parentOrgId: 9133745}
→ [ {id:9139001, name:"Chi cục thuộc Sở B", selectable:true, isLeaf:1} ]   // chỉ con CÓ MÃ; phòng không mã của Sở B không hiện

POST children {builtOrgId: 9133734, parentOrgId: 9133734}
→ [ {id:9134001, name:"Phòng Tổng hợp", selectable:true, isLeaf:1}, ... ]   // con cháu Sở A theo DB, mở tiếp nếu isLeaf=0
```

Gợi ý UI: mở màn → gọi gốc, rồi tự mở lần lượt các node nằm trên `path` của đơn vị ban hành (id trong `path`) để cây dừng ở đơn vị ban hành, giống web. Cache kết quả từng node trong phiên chọn để không gọi lại khi đóng/mở.

### 3.2 `POST /api/vhr-org/get-doc-manager-transfer-org-ids` — id đơn vị trong phạm vi CÁ NHÂN dưới 1 node (lọc danh sách cá nhân)

> Hướng dẫn chi tiết cách gọi API lấy user kèm tập id này: **`2026-09-16-van-thu-phat-hanh-loc-user-mobile.md`**.

Gọi **mỗi khi đổi node đang chọn** trên cây, trước khi lấy danh sách cá nhân của node đó.

Request:
```json
{ "builtOrgId": 9133734, "orgId": 148842 }
```
- `orgId`: id node đang chọn; **null = toàn bộ phạm vi**.

Response `data`: `Long[]` — id các đơn vị trong **phạm vi cá nhân** (đơn vị ban hành + con cháu; VPUB thêm chính UBND tỉnh) nằm dưới node đó. Node ngoài phạm vi cá nhân → `[]`.

Dùng để **ẩn** user ngoài phạm vi (không phải disable): lấy danh sách cá nhân theo đúng tập id này, lọc ở query để phân trang/tổng số vẫn đúng.
- Nếu gọi gen-1 `staffAction.getListUser`: gửi `lstGroupId` = tập id này, **`onlyParentGroup = 1`** và **`user.checkListGroup = true`** (thiếu `checkListGroup` thì BE bỏ qua `lstGroupId`, chỉ lọc `SYS_ORGANIZATION_ID = user.sysOrgId`; thiếu `onlyParentGroup` thì `lstGroupId` là `CONNECT BY` kéo cả con cháu, đưa tổ tiên vào là ra cả tỉnh).
- Lưu ý: với `onlyParentGroup = 1`, BE dùng nhánh `getListUserLongPress` — có thêm ràng buộc `IS_DEFAULT IN (1,2)` và role `LDDV/TTDV/NV` (khi cờ `transferDocOut`), giống ô tìm nhanh trên web.

### 3.3 `POST /api/vhr-org/get-doc-manager-transfer-scope` — tập id để lọc tìm kiếm / validate

Gọi **1 lần** khi mở màn chọn (song song với gọi gốc cây). Chỉ trả id (nhẹ).

Request:
```json
{ "builtOrgId": 9133734 }
```

Response `data`:

| Field | Kiểu | Ý nghĩa |
|---|---|---|
| `builtOrg` | VhrOrgResponseDTO | đơn vị ban hành (`path`, `name`…) |
| `builtOrgDepth` | Integer | độ sâu path đơn vị ban hành (`2` = cấp 0) |
| `selectableOrgIds` | Long[] | tổ tiên + đơn vị ban hành + **mọi đơn vị có mã định danh** + **mọi đơn vị cấp 0** (không xét mã) (**không** gồm con cháu không mã của đơn vị ban hành) |
| `descendantOrgIds` | Long[] | con cháu đơn vị ban hành (còn hiệu lực) |
| `userOrgIds` | Long[] | phạm vi **CÁ NHÂN**: đơn vị ban hành + con cháu (VPUB: thêm id **chính** UBND tỉnh, không có con khác của UBND) |
| `userRootOrg` | VhrOrgResponseDTO | gốc cây cá nhân: đơn vị ban hành; VPUB thì là UBND tỉnh (con duy nhất trong phạm vi là VPUB) |

Tập **đơn vị** hợp lệ = `selectableOrgIds ∪ descendantOrgIds`; tập **cá nhân** hợp lệ = `userOrgIds`. Dùng cho:
- **Ô tìm nhanh đơn vị**: lọc kết quả `sysOrganizationId ∈ tập hợp lệ` (hoặc truyền list id vào API tìm đơn vị đang dùng).
- **Ô tìm nhanh cá nhân**: user hợp lệ khi `user.sysOrganizationId ∈ userOrgIds` (**không** dùng tập đơn vị). Nếu dùng gen-1 `staffAction.getListUser` với `lstGroupId` = `userOrgIds` thì **phải gửi `onlyParentGroup = 1`** và `user.checkListGroup = true`.
- **Validate trước khi bấm Chuyển**: đơn vị đã chọn ∈ tập đơn vị; cá nhân đã chọn có `sysOrganizationId ∈ userOrgIds`.

Kiểm tra nhanh 1 đơn vị bất kỳ có hợp lệ không, không cần list con cháu: `selectableOrgIds.contains(id) || org.path.startsWith(builtOrg.path)`.

## 4. Thứ tự gọi gợi ý

```
mở màn chọn đối tượng (đã thỏa mục 1)
 ├─ scope(builtOrgId)                 → giữ selectableOrgIds, descendantOrgIds, builtOrg.path, userOrgIds, userRootOrg
 ├─ children(builtOrgId, null)        → node gốc
 └─ với mỗi id trong builtOrg.path (trừ chính nó): children(builtOrgId, id) → tự mở đến đơn vị ban hành
user mở node X (isLeaf=0)             → children(builtOrgId, X)   (cache)
màn cá nhân                           → cây riêng, gốc = userRootOrg, lọc con theo userOrgIds (VPUB: UBND tỉnh → chỉ VPUB)
user chọn node X để xem cá nhân       → org-ids(builtOrgId, X) → lấy user theo đúng tập id (ẩn user ngoài phạm vi)
user tick                              → chỉ cho tick node selectable=true
user gõ tìm nhanh                      → đơn vị: tập đơn vị; cá nhân: userOrgIds (mục 3.3)
bấm Chuyển                             → validate theo tập hợp lệ rồi gọi API chuyển như hiện tại
```

## 5. API liên quan (đã có, không đổi)

| API | Dùng khi |
|---|---|
| `GET /api/vhr-org/get-list-org-parent-child-level-once?orgParentId=…` | lấy toàn bộ con trực tiếp (không lọc phạm vi) — không dùng cho cây này |
| `GET /api/vhr-org/get-list-child-all-level?orgParentId=…` | id con cháu — không cần vì scope đã trả `descendantOrgIds` |
| ~~`POST /api/vhr-org/get-list-org-identifier-code`~~ | **đã xóa** (bản đầu, lọc theo `orgLevel` — dữ liệu `orgLevel` sai) |

## 6. Lưu ý

- `selectable`, `isLeaf` chỉ có nghĩa trong ngữ cảnh `builtOrgId` truyền vào; đổi văn bản khác phải gọi lại.
- Node `selectable=false` vẫn cần hiển thị (để mở xuống đơn vị có mã bên dưới), chỉ ẩn/disable ô chọn.
- Đơn vị có mã ở nhánh khác (và đơn vị cấp 0 không mã): `isLeaf=1` khi không còn hậu duệ có mã (dù thực tế có phòng ban không mã) — cố ý, không cho chọn đơn vị không mã ngoài nhánh đơn vị ban hành.
- `selectableOrgIds` giờ chứa toàn bộ đơn vị có mã của hệ thống (có thể nhiều id) — nên dựng `Set` một lần để tra, đừng `List.contains` trong vòng lặp.
- Mọi thứ tính theo `path`; đừng suy luận từ `orgLevel`.
