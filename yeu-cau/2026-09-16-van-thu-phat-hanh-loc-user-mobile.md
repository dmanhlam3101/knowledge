# MOBILE — lọc danh sách cá nhân theo phạm vi khi văn thư phát hành chuyển VB đi

**Phân hệ:** `van-ban/di` · **Ngày:** 2026-09-16 · Cây đơn vị: `2026-09-16-van-thu-phat-hanh-chuyen-vb-di-mobile.md` · Code web đối chiếu: `2026-09-16-van-thu-phat-hanh-chuyen-vb-di-web.md`

Mục tiêu: **ẩn hẳn** (không phải disable) cá nhân thuộc đơn vị ngoài phạm vi. Lọc ở server để tổng số / phân trang đúng.

---

## 1. Khi nào bật lọc

| # | Điều kiện | Lấy từ đâu (mobile) |
|---|---|---|
| 1 | User có role văn thư | role của user đăng nhập |
| 2 | User là văn thư của **chính đơn vị ban hành** `document.builtGroupId` | kiểm tra user có role "VT" tại đơn vị `builtGroupId` |
| 3 | Chuyển **văn bản đi**, chuyển **1** văn bản | màn đang thao tác |
| 4 | Văn bản **đơn vị** (không phải phạm vi "văn bản cá nhân") | bộ lọc phạm vi của màn (web: `orgRangeState != 1`) |
| 5 | Màn *Văn bản ban hành* tab Đã cấp số / Đã ban hành / Tất cả, **hoặc** *Chờ cấp số* sau khi cấp số | màn đang thao tác |

Đặt kết quả vào 1 biến duy nhất, ví dụ `scopeBuiltOrgId`:

```
scopeBuiltOrgId = (đủ 5 điều kiện) ? document.builtGroupId : null
```

`scopeBuiltOrgId == null` ⇒ **mọi thứ giữ nguyên như hiện tại**, không gọi API mới, không thêm tham số nào.

---

## 2. Luồng gọi API

```
Mở màn chọn người nhận (scopeBuiltOrgId != null)
 ├─(1) POST /api/vhr-org/get-doc-manager-transfer-scope   { builtOrgId }        → cache theo văn bản
 │        dùng cho: Ô TÌM NHANH cá nhân (toàn phạm vi)
 └─(2) POST /api/vhr-org/get-doc-manager-transfer-org-ids { builtOrgId, orgId } → cache theo node
          dùng cho: DANH SÁCH cán bộ khi chọn 1 đơn vị trên cây
                    ↓
     (3) POST staffAction/getListUser  (API cũ mobile đang dùng)
          + lstGroupId = id lấy từ (1) hoặc (2)
          + onlyParentGroup = 1
          + user.checkListGroup = true
```

---

## 3. API (1) — `POST /api/vhr-org/get-doc-manager-transfer-scope`

Gọi **1 lần cho mỗi văn bản**, dùng cho ô tìm nhanh.

### Request
```json
{ "builtOrgId": 9133734 }
```

| Field | Kiểu | Ý nghĩa | Truyền gì |
|---|---|---|---|
| `builtOrgId` | Long | đơn vị ban hành văn bản | `document.builtGroupId` (KHÔNG phải đơn vị của user đăng nhập, KHÔNG phải đơn vị đang chọn trên cây) |

### Response (`result.data`)

| Field | Kiểu | Ý nghĩa | Mobile dùng làm gì |
|---|---|---|---|
| `builtOrg` | object | thông tin đơn vị ban hành (`sysOrganizationId`, `name`, `path`…) | hiển thị / kiểm tra nhanh `path.startsWith` |
| `builtOrgDepth` | Integer | độ sâu path của đơn vị ban hành (số cấp) | chỉ để hiểu quy tắc "ngang cấp", không bắt buộc dùng |
| `selectableOrgIds` | Long[] | tổ tiên + đơn vị ban hành + đơn vị ngang cấp có mã định danh (**không** gồm con cháu) | ghép vào `scopeIds` |
| `descendantOrgIds` | Long[] | toàn bộ con cháu của đơn vị ban hành (còn hiệu lực) | ghép vào `scopeIds` |

### Tính tập id dùng cho ô tìm nhanh
```
scopeIds = distinct( selectableOrgIds + [builtOrgId] + descendantOrgIds )
```

---

## 4. API (2) — `POST /api/vhr-org/get-doc-manager-transfer-org-ids`

Gọi **mỗi khi người dùng chọn/đổi đơn vị trên cây**, dùng cho danh sách cán bộ của đơn vị đó.

### Request
```json
{ "builtOrgId": 9133734, "orgId": 148842 }
```

| Field | Kiểu | Ý nghĩa | Truyền gì |
|---|---|---|---|
| `builtOrgId` | Long | đơn vị ban hành | `document.builtGroupId` (giống API 1) |
| `orgId` | Long | **đơn vị đang chọn trên cây** | id node người dùng vừa bấm; `null` = lấy toàn bộ phạm vi (dùng khi màn không có cây) |

### Response
`result.data` = `Long[]` — id các đơn vị **chọn được** nằm dưới node đó (đã loại node "chỉ để mở cây").

| Trường hợp | Kết quả trả về | Mobile xử lý |
|---|---|---|
| Node là đơn vị ban hành / đơn vị con của nó | id node + con cháu | gọi (3) với list này |
| Node là tổ tiên (vd UBND tỉnh) | id tổ tiên đó + đơn vị ban hành + con cháu + các đơn vị ngang cấp có mã nằm dưới | gọi (3) với list này |
| Node là đơn vị ngang cấp có mã (vd Sở B) | chỉ id của chính nó | chỉ ra cán bộ Sở B |
| Node "chỉ để mở cây" (vd Tỉnh ủy, Sở Xây dựng trong ví dụ) | chỉ id các đơn vị ngang cấp có mã nằm dưới nó | cán bộ của chính node đó **không** xuất hiện |
| Không có đơn vị hợp lệ nào | `[]` hoặc null | **hiển thị danh sách rỗng, KHÔNG gọi (3)** |

---

## 5. API (3) — `staffAction.getListUser` (API cũ, chỉ thêm 3 tham số)

Mobile **giữ nguyên request hiện tại** (kể cả cách đóng gói/mã hoá `data`), chỉ thêm/đặt 3 chỗ đánh dấu ⭐.

### Toàn bộ tham số và ý nghĩa

| Tham số | Kiểu | Ý nghĩa | Truyền gì trong nghiệp vụ này |
|---|---|---|---|
| `user` | object (JSON) | bộ lọc người dùng (xem bảng con) | như hiện tại + ⭐`checkListGroup` |
| ⭐ `lstGroupId` | array | danh sách đơn vị giới hạn, dạng `[{"groupId":"148842"}, …]` (`groupId` là **chuỗi**) | `scopeIds` (API 1) cho ô tìm nhanh, hoặc kết quả API 2 cho danh sách theo node |
| ⭐ `onlyParentGroup` | `"1"` / `"0"` | `1` = lọc **đúng** các đơn vị trong `lstGroupId`; `0`/không gửi = mỗi id kéo theo toàn bộ con cháu (CONNECT BY) | luôn `"1"` |
| `keyword` | String | từ khoá tìm (tên, email, SĐT, mã định danh) | nội dung ô tìm; danh sách theo node thì để rỗng/null |
| `type` | Long | loại danh sách cần lấy (0 = mặc định, 1 = người nhận văn bản thường…) | **giữ nguyên giá trị mobile đang dùng cho màn đó** (web: ô tìm nhanh = `1`) |
| `searchType` | Integer | kiểu tìm (web truyền `1`) | giữ như hiện tại |
| `documentId` | Long | id văn bản — BE dùng để đánh dấu ai đã nhận văn bản | `document.documentId` |
| `startRecord` | Long | bản ghi bắt đầu (offset) | `page * pageSize`; ô gợi ý tìm nhanh web dùng `0` |
| `pageSize` | Long | số bản ghi/trang | danh sách: 15–20; ô gợi ý tìm nhanh web dùng `5` |
| `isCount` | `"1"` | gọi **đếm tổng** thay vì lấy danh sách | chỉ khi cần tổng số để phân trang |
| `getRole` | Integer | tuỳ chọn, lấy kèm vai trò | giữ như hiện tại |

### Object `user` (các field liên quan)

| Field | Kiểu | Ý nghĩa | Truyền gì |
|---|---|---|---|
| `sysOrgId` | Long | đơn vị đang xem | id node đang chọn (giữ như hiện tại). Khi đã có `lstGroupId` + `onlyParentGroup=1` + `checkListGroup=true` thì field này **không** còn quyết định phạm vi |
| ⭐ `checkListGroup` | Boolean | **bật lọc theo `lstGroupId`** | `true` |
| `isTransferDocOut` | Boolean | đang chuyển văn bản **đi** (BE lọc thêm vai trò LDDV/TTDV/NV) | `true` (web gửi vậy cho chiều "out") |
| `getByDefault` | Boolean | lọc theo vai trò mặc định | giữ như hiện tại (web: `true`) |
| `status` | Long | `1` = văn bản mật (lọc người có chứng thư), `0` = thường | theo độ mật văn bản |
| `fullName`, `strEmail`, `mobileNumber`, `strCardNumber`, `sysRoleId` | | tìm nâng cao theo từng trường | như hiện tại |

⚠ Tên field là `isTransferDocOut` (không phải `transferDocOut`), `checkListGroup` viết đúng hoa/thường như trên.

### Body mẫu — danh sách cán bộ của node đang chọn

```json
{
  "user": {
    "sysOrgId": 148842,
    "checkListGroup": true,
    "isTransferDocOut": true,
    "getByDefault": true,
    "status": 0
  },
  "lstGroupId": [ {"groupId":"148842"}, {"groupId":"9133734"}, {"groupId":"9134001"} ],
  "onlyParentGroup": "1",
  "keyword": "",
  "type": 1,
  "searchType": 1,
  "documentId": "123456",
  "startRecord": 0,
  "pageSize": 20
}
```

Đếm tổng: cùng body, thêm `"isCount": "1"`, bỏ `startRecord`/`pageSize`.

### Kết quả
Mảng user như hiện tại (`employeeId`, `fullName`, `position`, `orgName`, `sysOrganizationId`, `pathName`, `email`, `mobilePhone`, `employeeCode`, …). **Không cần lọc lại ở client** — server đã lọc đúng phạm vi.

---

## 6. Ghép lại — luồng cho từng màn

### 6.1 Ô tìm nhanh cá nhân (màn Chuyển văn bản)

```
scopeIds = cache.scope(builtOrgId)              // gọi API 1 nếu chưa có
onDebounce(400ms, keyword):
    if (scopeBuiltOrgId == null) → gọi getListUser như cũ
    else → getListUser(user{checkListGroup:true, isTransferDocOut:true, sysOrgId: builtOrgId},
                       lstGroupId: scopeIds, onlyParentGroup:"1",
                       keyword, type:1, searchType:1, documentId, startRecord:0, pageSize:5)
```

### 6.2 Danh sách cán bộ theo đơn vị trên cây

```
onSelectOrgNode(node):
    if (scopeBuiltOrgId == null) → giữ luồng cũ; return
    ids = cache.orgIds(builtOrgId, node.id)      // gọi API 2 nếu chưa có
    if (ids rỗng) → hiển thị danh sách rỗng; return
    total = getListUser(..., lstGroupId: ids, onlyParentGroup:"1", isCount:"1")
    page0 = getListUser(..., lstGroupId: ids, onlyParentGroup:"1", startRecord:0, pageSize:20)

onLoadMore(page):
    getListUser(..., lstGroupId: ids /*dùng lại, KHÔNG gọi lại API 2*/, startRecord: page*20, pageSize:20)
```

---

## 7. Cache ở mobile — tránh gọi lại DB

| Cache | Key | Giá trị | Vòng đời | Ghi chú |
|---|---|---|---|---|
| `scopeCache` | `builtOrgId` | `selectableOrgIds`, `descendantOrgIds`, `builtOrg.path`, `builtOrgDepth` | phiên chọn người nhận của 1 văn bản; TTL 10–15 phút | dữ liệu đơn vị gần như tĩnh; 1 văn bản chỉ cần gọi 1 lần |
| `orgIdsCache` | `builtOrgId + "#" + nodeId` (`nodeId` null → `0`) | `Long[]` | như trên | quay lại node đã xem → **không gọi lại** (web làm đúng thế này) |
| `treeChildrenCache` | `builtOrgId + "#" + parentOrgId` | danh sách node | như trên | đóng/mở lại nhánh không gọi lại API cây |
| Danh sách user | — | — | **không cache lâu** (≤ 30–60s, hoặc chỉ giữ trong lúc cuộn) | trạng thái "đã nhận văn bản", nhân sự có thể đổi |

Nguyên tắc:
1. **Một văn bản = một `scopeCache`.** Mở lại popup cho cùng văn bản thì dùng lại, đừng gọi lại API 1.
2. **Đổi từ khoá KHÔNG gọi lại API 1/2** — chỉ đổi `keyword`, `lstGroupId` giữ nguyên. Đây là lỗi hay gặp nhất khiến DB bị gọi mỗi lần gõ phím.
3. **Debounce 300–400 ms** cho ô tìm nhanh + huỷ request trước đó (chỉ nhận kết quả của lần gõ cuối).
4. **Phân trang dùng lại `lstGroupId` đã có**, không gọi lại API 2.
5. Khi mở màn: gọi **song song** API 1 và API lấy cây gốc, không gọi nối tiếp.
6. Xoá cache khi: đổi văn bản khác, người dùng kéo refresh, hoặc đăng xuất. Không cần theo dõi thay đổi cây đơn vị (rất hiếm đổi).
7. Nếu `descendantOrgIds` lớn (văn thư UBND tỉnh có thể vài nghìn id): giữ ở dạng mảng để gửi API, kèm `Set` để tra cứu nhanh phía client; vẫn **chỉ tải 1 lần**. Có thể **lười**: chỉ gọi API 1 khi người dùng chạm vào ô tìm nhanh lần đầu, để mở màn nhẹ hơn.

---

## 8. Bẫy (đã dính khi làm web)

1. **Thiếu `user.checkListGroup = true`** → BE **bỏ qua** `lstGroupId` và lọc `SYS_ORGANIZATION_ID = user.sysOrgId` ⇒ vẫn ra cán bộ của đơn vị ngoài phạm vi (đúng triệu chứng đã gặp trên web).
2. **Thiếu `onlyParentGroup = "1"`** → mỗi id trong `lstGroupId` bị hiểu là "id + toàn bộ con cháu" ⇒ truyền id tổ tiên là ra cả tỉnh.
3. **Lọc ở client sau khi phân trang** → tổng số và số trang sai; phải lọc bằng `lstGroupId`.
4. Với `onlyParentGroup = "1"`, BE chạy nhánh `getListUserLongPress`: có thêm `IS_DEFAULT IN (1,2)` và (khi `isTransferDocOut`) vai trò `LDDV/TTDV/NV`. Danh sách có thể khác nhánh cũ vài người — đúng như web hiện tại, không phải bug của tập id.
5. `groupId` trong `lstGroupId` là **chuỗi** (`"148842"`), không phải số.
6. `builtOrgId` luôn là **đơn vị ban hành văn bản**, không phải đơn vị của user đăng nhập — gửi nhầm là sai toàn bộ phạm vi.

---

## 9. Checklist test

1. Văn thư Sở A, màn Văn bản ban hành (Đã cấp số) → chọn người nhận:
   - chọn **UBND tỉnh**: có cán bộ UBND tỉnh + Sở A và phòng của Sở A + các Sở ngang cấp có mã; **không** có cán bộ phòng của Sở khác.
   - chọn **Sở B** (ngang cấp có mã): có cán bộ Sở B, **không** có cán bộ phòng dưới Sở B.
   - chọn node chỉ để mở cây: **không** có cán bộ của chính node đó.
   - tổng số bản ghi + số trang khớp danh sách.
2. Ô tìm nhanh: gõ tên cán bộ phòng thuộc Sở khác → không ra; gõ cán bộ Sở B / UBND tỉnh / phòng của Sở A → ra.
3. Gõ liên tục 10 ký tự → chỉ thấy **1** request `get-doc-manager-transfer-scope` trong log (cache + debounce hoạt động).
4. Mở lại node đã xem → không có request `get-doc-manager-transfer-org-ids` mới.
5. Phạm vi "Văn bản cá nhân" hoặc user không phải văn thư đơn vị ban hành → request `getListUser` **không** có `lstGroupId`/`onlyParentGroup`/`checkListGroup`, hành vi như cũ.
