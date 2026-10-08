# Văn thư phát hành chuyển VB đi — mô tả code WEB (+ BE)

**Phân hệ:** `van-ban/di` · **Tầng:** Web (ZK) + BE gen-2 · **Ngày:** 2026-09-16 · **Thay thế** phần "hướng dẫn kỹ thuật" của `2026-09-15-loc-don-vi-nhan-khi-ban-hanh.md` (bản đó còn giả định dùng `orgLevel` và dựng cây ở web — đã bỏ).

> **Cập nhật 2026-10-02 — bỏ "ngang cấp":** nhóm thứ 4 đổi từ "cùng độ sâu path + có mã" thành **mọi đơn vị có mã định danh** (mọi cấp/nhánh); thêm **mọi đơn vị cấp 0** (`LEVEL_0_PATH_DEPTH = 2`, không xét mã, **không** phụ thuộc cấp của đơn vị ban hành). Endpoint/DTO không đổi.

> ~~**Cập nhật 2026-10-02 (2) — phạm vi CÁ NHÂN tách riêng** (ĐÃ HỦY 2026-10-07, không triển khai):~~ tab Cá nhân + ô tìm cá nhân chỉ trong **đơn vị ban hành + con cháu**; đơn vị ban hành = **VPUB** (`sysOrganization.id.vpub`, BE đọc qua `FuncUtils.environment`) thì thêm cá nhân của **chính đơn vị cha trực tiếp** (UBND tỉnh), không lấy đơn vị con khác của UBND (`VhrOrgServiceImpl.findDocManagerUserParentOrg`). Đơn vị có mã / cấp 0 ngoài nhánh chỉ áp dụng cho tab Đơn vị.

> **Cập nhật 2026-10-07 — BỎ lọc CÁ NHÂN, YC chỉ áp dụng cho ĐƠN VỊ:** phạm vi mới **chỉ** áp dụng cho tab **Đơn vị** và ô tìm nhanh đơn vị. Tab **Cá nhân** + ô tìm nhanh cá nhân **giữ nguyên hành vi như trước khi phát triển YC này** (cây và danh sách đi nhánh cũ `isFreeTransfer` / `checkAutoLimitTransfer`), không ẩn/không lọc user theo đơn vị ban hành. Code web đã gỡ (xem 3.6, 3.7, mục 4). **BE không đụng đến**: endpoint `get-doc-manager-transfer-org-ids` vẫn còn (web không gọi nữa). **LƯU Ý:** 2 field `userOrgIds`/`userRootOrg` và `findDocManagerUserParentOrg` **chưa bao giờ có trong BE hiện tại** — đã bị revert trước đó (web: `fda5937e3`, du thảo: `3e44447b3`); `GetDocManagerTransferScopeResponseDTO` chỉ có `builtOrg`, `builtOrgDepth`, `selectableOrgIds`, `descendantOrgIds`.

## 1. Nghiệp vụ

Văn thư của **đơn vị ban hành** chuyển **văn bản đơn vị** ở màn *Văn bản ban hành* chỉ được chọn:

| Nhóm | Định nghĩa (theo `VHR_ORG.PATH`, **không** dùng `ORG_LEVEL`) |
|---|---|
| Cấp cha | mọi đơn vị nằm trên `PATH` của đơn vị ban hành |
| Đơn vị ban hành | `DOCUMENT.BUILT_GROUP_ID` |
| Con cháu | `PATH LIKE '<path đơn vị ban hành>%'` |
| Đơn vị có mã | `IDENTIFIER_CODE IS NOT NULL` — **mọi độ sâu, mọi nhánh** (trừ nút ảo `1`) |
| Cấp 0 (mọi đơn vị ban hành) | độ sâu `PATH` = 2 (`/1/<id>/`) — mọi đơn vị, **không** xét mã |

Ngoài nhánh đơn vị ban hành, đơn vị **không có mã** không chọn được. Đơn vị không mã là tổ tiên của một đơn vị có mã chỉ hiện trên cây để mở xuống (node "chỉ điều hướng"), **không** báo lỗi khi click — cây chỉ để lọc; việc chặn nằm ở danh sách bên phải.

## 2. Điều kiện kích hoạt

`TransferDocumentVM.isDocManagerTransferOut(isDocManager, isVTOfOrg, transferDirection, isMultipleTransfer, doc, viewType, orgRangeState)` — **một chỗ duy nhất**, `MultiTypeObjectLookupVM` gọi lại.

| Điều kiện | Ý nghĩa | Nguồn |
|---|---|---|
| `isDocManager` | user có role văn thư | `CommonModel` (session) |
| `isVTOfOrg` | là văn thư của **chính** đơn vị ban hành | `TransferDocumentVM.checkHasRoleInOrg(handlingOrg, user, "VT")`, `handlingOrg` = `doc.builtGroupId` |
| `transferDirection == "out"` | chuyển VB đi | |
| `!isMultipleTransfer` | chuyển 1 văn bản | |
| `doc.builtGroupId != null` | | |
| `orgRangeState != 1` | văn bản **đơn vị** (1 = radio "Văn bản cá nhân"); `null` coi như đơn vị | `ARG_ORG_RANGE_STATE` |
| `viewType ∈ {DCS=8, DBH=9, ALL=10}` | `AppConstants.DOCUMENT.VBBH.VIEW_TYPE` | `ARG_VIEW_TYPE` |

Bốn đường vào popup Chuyển đều thỏa:

| Màn | VM truyền args | viewType / orgRangeState |
|---|---|---|
| Tab Đã cấp số / Đã ban hành / Tất cả (list) | `DocumentOutVM` (`doTransferDocument…`, dòng ~3652) | tabType → DCS/DBH/ALL; radio đơn vị/cá nhân |
| Ba tab trên → mở chi tiết → Chuyển | `DocumentViewDetailVM` (~3526) | `tabType`, `doc.getOrgRange()` |
| **Chờ cấp số → sau khi cấp số** → chi tiết → Chuyển | `RequisitionViewIssueNumberVM` → `DocumentViewDetailVM` với `doc.docManagerPromulgate = true` (~3521, 3532) | ép `viewType = DCS`, `orgRangeState = 0`, `ARG_IS_VT_OF_ORG = true` |

Không thỏa → rơi về nhánh cũ (`isFreeTransfer` / `checkAutoLimitTransfer`), không ảnh hưởng màn khác.

## 3. Luồng dữ liệu

```
TransferDocumentVM (popup Chuyển văn bản)
 ├─ initSearchScopeOrgIds()  ──► BE scope ──► searchScopeOrgIds (ô tìm nhanh ĐƠN VỊ)
 │                            └─► searchScopeUserOrgIds (ô tìm nhanh CÁ NHÂN — logic CŨ)
 └─ doSelectObjectsToTransfer ──► MultiTypeObjectLookupVM (popup Chọn đối tượng)
        └─ getDocManagerTree() [cache 1 lần/popup]
             ├─ BE scope      → orgIds, ancestorAndSelfIds, selectablePathPrefixes, identifierCodeDepth, builtOrgNode
             ├─ BE children(parent=null) → roots
             └─ childrenLoader = parent → BE children(parent.id)
        ├─ tab Đơn vị  → SysOrganizationLookupVM  (cây + danh sách đơn vị) ← ÁP phạm vi mới
        └─ tab Cá nhân → UserWSLookupVM           (nhánh CŨ, KHÔNG áp phạm vi)
```

### 3.1 BE gen-2 (`com.viettel.office`)

| Endpoint | Request | Response | Query |
|---|---|---|---|
| `POST /api/vhr-org/get-doc-manager-transfer-scope` | `GetDocManagerTransferDTO{builtOrgId}` | `GetDocManagerTransferScopeResponseDTO`: `builtOrg`, `builtOrgDepth`, `selectableOrgIds` (tổ tiên + đơn vị ban hành + mọi đơn vị có mã — **chỉ id**), `descendantOrgIds` (chỉ id), ~~`userOrgIds` + `userRootOrg`~~ (phạm vi/gốc cây **cá nhân** — BE vẫn trả cho mobile, **web không dùng** từ 2026-10-07) | 3: `findById`, `VhrOrgRepositoryJPA.findOrgIdHasIdentifierCode` + `findOrgIdByPathDepth(2)`, `findChildrenAllLevel` |
| `POST /api/vhr-org/get-doc-manager-transfer-children` | `GetDocManagerTransferDTO{builtOrgId, parentOrgId}` (`parentOrgId` = nút đang mở, null = gốc) | `List<VhrOrgResponseDTO>` con trực tiếp **có liên quan**, mỗi node có `selectable`, `isLeaf` | 1: `VhrOrgRepositoryImpl.getDocManagerTransferChildren` |
| `POST /api/vhr-org/get-doc-manager-transfer-org-ids` **(web không gọi nữa từ 2026-10-07 — chỉ mobile)** | `GetDocManagerTransferDTO{builtOrgId, orgId}` (`orgId` = nút đang chọn, null = toàn bộ phạm vi) | `List<Long>` id đơn vị trong **phạm vi cá nhân** (đơn vị ban hành + con cháu; VPUB thêm chính đơn vị cha) nằm dưới `orgId` | 1: `VhrOrgRepositoryImpl.getDocManagerTransferOrgIds(builtPath, parentOrgId, nodePath)` |

Cả 3 endpoint dùng chung **một** DTO request `dto.request.GetDocManagerTransferDTO {builtOrgId, parentOrgId, orgId}` — key giữ nguyên như bản đã bàn giao cho mobile (`children` dùng `parentOrgId`, `org-ids` dùng `orgId`).

Con "có liên quan" của `parentOrgId` (SQL `WHERE org_parent_id = :p AND (a ∨ b ∨ c ∨ d)`):
- (a) trong nhánh đơn vị ban hành → `selectable=true`, `isLeaf` theo DB;
- (b) tổ tiên đơn vị ban hành → `selectable=true`, `isLeaf=0`;
- (c) có mã, hoặc là đơn vị cấp 0 (`IS_LEVEL_0`) → `selectable=true`, `isLeaf=0` nếu còn hậu duệ có mã, ngược lại `1` (không kéo con không mã);
- (d) không mã nhưng có hậu duệ có mã (`EXISTS … d.path LIKE o.path||'%'`) → `selectable=false`, `isLeaf=0` (chỉ để mở).

`isLeaf` tính trong SQL (`CASE … HAS_CODED_DESCENDANT`), `selectable` tính ở service: `VhrOrgServiceImpl.getDocManagerTransferScope / getDocManagerTransferChildren`.

Bẫy: `BaseRepositoryImpl.getListData` map **tên cột = tên field**, phải alias `sys_organization_id AS sysOrganizationId…` (không `SELECT o.*`). API POST nhận DTO bắt buộc `@RequestBody`.

### 3.2 Web — gọi BE

| File | Hàm | Ghi chú |
|---|---|---|
| `com.voffice.service.business.CommonBusiness` | `getDocManagerTransferScope(builtOrgId)` → `DocManagerTransferScopeDTO`; `getDocManagerTransferChildren(builtOrgId, parentOrgId)` → `List<VhrOrgEntity>` | `servePostRequest` JSON |
| `com.viettel.voffice.dto.DocManagerTransferScopeDTO` | DTO web của scope | |
| `com.voffice.service.entity.VhrOrgEntity` | thêm `identifierCode` | `selectable` BE có trả nhưng web không dùng (danh sách đã lọc bằng SQL) |

### 3.3 Web — `MultiTypeObjectLookupVM` (`com.viettel.voffice.widget`)

- `buildDocManagerTree()` → `DocManagerTree`:
  - `roots` = children(null) convert sang `SysOrganization` (`toTreeNode`: copy id/code/name/abbreviation/path/orgParentId/orderNumber/identifierCode/orgLevel/isLeaf; `onlyCurrentOrg=false`, `listOrgLimitOneLevel=null` để tree model gọi loader);
  - `builtOrgNode` = `scope.builtOrg` → `ARG_ORG` (focus + auto mở cây tới đơn vị ban hành);
  - `ancestorAndSelfIds` = id trong `builtOrg.path` → `ARG_ORG_ID` (filter `id IN` của danh sách — **cố ý không** đưa id ngang cấp vì `SysOrganizationLookupVM` sẽ `findByIds` cả list);
  - `selectablePathPrefixes` = `[builtOrg.path]` → `ARG_SELECTABLE_PATH_PREFIXES`;
  - `hasIdentifierCode` = `TRUE` → `ARG_SELECTABLE_HAS_IDENTIFIER_CODE`;
  - `allPathDepth` = `2` (luôn) → `ARG_SELECTABLE_ALL_PATH_DEPTH`;
  - `childrenLoader` → `ARG_TREE_CHILDREN_LOADER` (chỉ tab Đơn vị). `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` **đã xóa** (2026-10-07).
- `prepareForOrgLookup` (tab Đơn vị) nhận `ARG_TREE_ROOT`, `ARG_ORG`, `ARG_ORG_ID`, `ARG_SELECTABLE_PATH_PREFIXES`, `ARG_SELECTABLE_HAS_IDENTIFIER_CODE`, `ARG_SELECTABLE_ALL_PATH_DEPTH`, `ARG_TREE_CHILDREN_LOADER`; `prepareForUserLookup` (tab Cá nhân) **không nhận arg nào của phạm vi mới** — bỏ hẳn nhánh `docManagerTree`, đi thẳng nhánh cũ (2026-10-07).
- `getDocManagerTree()` cache theo instance vì `sendTabChangeEvent` gọi lại mỗi lần đổi tab.

### 3.4 Web — cây: `SysOrganizationTreeModel`

- Mới: `interface ChildrenLoader { List<SysOrganization> loadChildren(SysOrganization parent); }` + `setChildrenLoader`.
- `getChildren(parent)`: thứ tự nhánh
  1. `parent.listOrgLimitOneLevel` không rỗng → trả (cache);
  2. `parent.onlyCurrentOrg` → rỗng;
  3. **`childrenLoader != null`** → gọi loader; rỗng → `parent.setOnlyCurrentOrg(true)`; có → `parent.setListOrgLimitOneLevel(loaded)` rồi trả.
  4. … nhánh DB cũ (không đụng).
- **Bắt buộc cache** vì `CommonTreeModel.getChild(parent, i)` gọi `getChildren(parent)` cho **từng** index.
- `isLeaf(node)`: `onlyCurrentOrg` → theo cache; else `node.isLeaf == 1` (BE tính) → không gọi loader chỉ để vẽ icon.
- `SysOrgTreeitemRenderer.isExpanded`: node có path là tiền tố path đơn vị ban hành → tự mở → mở popup ≈ (độ sâu − 1) call `children`.

### 3.5 Web — tab Đơn vị: `SysOrganizationLookupVM`

- Args mới: `ARG_SELECTABLE_PATH_PREFIXES`, `ARG_SELECTABLE_HAS_IDENTIFIER_CODE` (Boolean), `ARG_SELECTABLE_ALL_PATH_DEPTH` (Integer), `ARG_SELECTABLE_ORG_IDS`, `ARG_TREE_CHILDREN_LOADER`.
- `createSysOrgTree()` cuối: `treeModel.setChildrenLoader(treeChildrenLoader)`.
- `findDataList / countDataList`: `obj.setIncludePathPrefixes(...)`, `obj.setIncludeHasIdentifierCode(...)`, `obj.setIncludeAllPathDepth(...)` (transient mới trên `com.viettel.vps.entity.SysOrganization`).
- DAO `SysOrganizationJpaDao.appendInCondition(query, params, "o.sysOrganizationId", "filter", ids, includePathPrefixes, includeHasIdentifierCode, includeAllPathDepth)` sinh:
  ```sql
  AND ( o.sysOrganizationId IN (:filter0)
        OR o.path LIKE :filterPath0                                   -- '<builtOrgPath>%'
        OR o.identifierCode IS NOT NULL
        OR (LENGTH(o.path) - LENGTH(REPLACE(o.path,'/','')) - 1) = :filterDepth )   -- mọi đơn vị cấp 0 (:filterDepth = 2)
  ```
  dùng ở `findByCondition` và `getCountByCondition` (V2 không đổi). Danh sách chỉ hiện đơn vị hợp lệ → không cần disable.
- Click cây: `onClickTreeItem` giữ nguyên (chỉ set `dataSearch.path` rồi `doSearch`).

### 3.6 Web — tab Cá nhân: `UserWSLookupVM` — **ĐÃ GỠ (2026-10-07)**

Tab Cá nhân **không áp phạm vi của YC** nữa, cả **cây đơn vị** lẫn **danh sách user** đều về đúng hành vi trước YC:

| Thành phần | Trạng thái hiện tại |
|---|---|
| `MultiTypeObjectLookupVM.prepareForUserLookup` | **bỏ hẳn nhánh `docManagerTree`** — không truyền `ARG_TREE_ROOT = docManagerTree.roots`, `ARG_ORG = builtOrgNode`, `ARG_TREE_CHILDREN_LOADER`, `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID`. Đi thẳng nhánh cũ `isFreeTransfer \|\| (isOutTransfer && checkAutoLimitTransferCustom())` → `getTopMostOrgs(orgVTs)` / `[orgLevelOne]`, hoặc `else` → gốc VIG/`treeRootId` |
| Cây | `treeChildrenLoader` = null → `SysOrganizationTreeModel` mở con theo **DB** như cũ, không gọi BE `children` |
| `UserWSLookupVM.selectableScopeBuiltOrgId` + `getDocManagerTransferOrgIds` | **đã xóa** khỏi web |
| `isSelectableScopeMode()` | chỉ còn `selectableScopeIdentifierCode` — **giữ nguyên**, đó là tính năng KHÁC (màn *Tạo dự thảo*, `DocumentDraftVM`, chỉ user của đơn vị có mã định danh) |
| `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` trong `SysOrganizationLookupVM` | **đã xóa** (không còn ai dùng) |
| `CommonBusiness.getDocManagerTransferOrgIds` | giữ lại nhưng **không còn ai gọi** — endpoint BE vẫn sống cho mobile |

**NGOẠI LỆ DUY NHẤT được giữ cho cá nhân — VPUB "giật lên" đơn vị cha (2026-10-07):**
`handlingOrg` là **VPUB** (`RbParamValue.SYS_ORGANIZATION.ID.VPUB`, param `sysOrganization.id.vpub`) thì văn thư VPUB được chọn thêm **cá nhân của chính đơn vị cha trực tiếp (UBND tỉnh)**, **không** lấy các Sở/đơn vị con khác của UBND.

- Cài ở `MultiTypeObjectLookupVM.addVpubParentOrg(orgVTs)`, gọi trong `prepareForUserLookup` ngay trước khi dựng `ARG_TREE_ROOT`/`ARG_TREE_FILTER_ORG`.
- Cách làm: chỉ **thêm đúng đơn vị cha** vào `orgVTs`. Vì `orgVTs` vừa là nguồn dựng gốc (`getTopMostOrgs`) vừa là **bộ lọc cây** (`ARG_TREE_FILTER_ORG`) nên cây tự giật lên UBND tỉnh (path VPUB bắt đầu bằng path UBND → UBND thành topmost), còn Sở khác không nằm trong `orgVTs` nên bị lọc — **không cần clone/`onlyCurrentOrg`/`listOrgLimitOneLevel`**. `skipIntermediateOrg` vẫn bật nhưng UBND giờ nằm trong `orgFilters` nên không bị coi là cấp trung gian (`SysOrganizationTreeModel.buildIntermediateIndex` dụng index từ `roots` + `orgFilters`).
- Click node UBND tỉnh → ra user của chính UBND: `rootOrganization` trong `UserWSLookupVM` là VIG/`treeRootId` (**không** phải VPUB) nên nhánh "snap về gốc" ở `findDataListSysUser` không kích hoạt.
- **Áp cho cả cây + danh sách tab Cá nhân VÀ ô tìm nhanh "Họ tên, email…" bên ngoài** (2026-10-07, bản sau) — xem 3.7.
- Điều kiện còn lại: chỉ chạy trong nhánh `orgVTs` không rỗng. Với văn thư phát hành thì luôn thỏa (`isVTProcessDepartmentDocument` = true và `findAllOrgVT` luôn thêm `orgLevelOne`).

Hệ quả tích cực: danh sách cá nhân không còn đi qua `StaffDAO.getListUserLongPress` (nhánh `onlyParentGroup=1` + `checkListGroup=true`), nên **mất luôn** ràng buộc phụ `u.IS_DEFAULT IN (1,2)` và `r.CODE IN ('LDDV','TTDV','NV')` mà bản YC vô tình thêm vào — đúng như trước YC.

### 3.7 Web — 2 ô tìm nhanh trong popup Chuyển: `TransferDocumentVM`

Tứ 2026-10-07 **tách làm 2 phạm vi riêng** — đơn vị theo YC, cá nhân theo logic cũ:

| Biến | Dùng cho | Tính thế nào |
|---|---|---|
| `searchScopeOrgIds` | ô "Tên đơn vị…" (`doSearchOrg`) | `isDocManagerTransferOut()` → `buildDocManagerSearchScopeOrgIds()` = `selectableOrgIds` + builtOrgId + `descendantOrgIds`; không thỏa → `buildLegacySearchScopeOrgIds()` (như cũ) |
| `searchScopeUserOrgIds` | ô "Họ tên, email…" (`doSearchReceiver`) | **luôn** `buildLegacySearchScopeOrgIds()` — logic cũ y nguyên: `isFreeTransfer \|\| (out && checkAutoLimitTransfer())` → cấp 1 đổ xuống, ngược lại `findAllChildOrgIds(root)` |

- `doSearchReceiver` trả về dòng trước YC: `isVTProcessDepartmentDocument = isVTOfOrg && (orgRangeState == 0 \|\| tabDoc == 0)` — **bỏ** `\|\| isDocManagerTransferOut()`, nên không còn bị ép `onlyParentGroup=1`.
- **ĐÃ SỬA — ô tìm cá nhân khớp với cây cá nhân** (2026-10-07).

  **Gốc vấn đề:** logic phạm vi cá nhân bị **nhân bản** giữa `MultiTypeObjectLookupVM` (cây) và `TransferDocumentVM` (ô tìm), rồi hai bản trôi khác nhau. Đã đối chiếu từng hàm bằng brace-matching:

  | Helper | Trước khi sửa |
  |---|---|
  | `checkVTProcessDepartmentDocument` | **KHÁC LOGIC** — MultiType: `isVTOfOrg && (orgRangeState==0 \|\| tabDoc==0)` · TransferDoc: `isVTOfOrg && tabDoc==0` |
  | `checkUserRoleLevel0` | **KHÁC** — TransferDoc thiếu chặn `orgLevel != null` (`getOrgLevel()` trả `Long` → unbox → **NPE**), không dedup, add `roots` lặp lại mỗi đơn vị cấp 1 |
  | `collectChildOrgs` | khác cách viết nhưng **tương đương** (MultiType tách `getChildOrgs` có cache + `isValidChildOrg`) |
  | `findAllOrgVT` · `checkAutoLimitTransferCustom` · `getTopMostOrgs` · `addVpubParentOrg` | giống nhau |

  Hệ quả của dòng đầu: văn thư phát hành có `orgRangeState = 0` nhưng `tabDoc != 0` thì cây đi nhánh `orgVTs` (hẹp, có VPUB) còn ô tìm đi nhánh khác → hai phạm vi lệch và luật VPUB không áp cho ô tìm.

  **Cách sửa (giữ 2 bản copy, KHÔNG tách class dùng chung):**

  | Việc | Chi tiết |
  |---|---|
  | `TransferDocumentVM.buildUserSearchScopeOrgIds()` | dựng lại y hệt cách cây tính tập đơn vị, map 1-1 từng nhánh với `prepareForUserLookup` |
  | Điều kiện VT | **cố ý KHÔNG** gọi `checkVTProcessDepartmentDocument()` của chính class đó (bản thiếu `orgRangeState`); viết thẳng biểu thức của cây vào biến `isVTProcessDepartmentDocumentAsTree`, kèm comment giải thích. Nhờ vậy **không đổi hành vi** của `doSelectObjectsToTransfer` đang dùng method cũ |
  | `checkUserRoleLevel0` | đồng bộ theo bản MultiType (chặn null + dedup + add `roots` một lần), thêm `addOrgIfAbsent` |
  | `addVpubParentOrg` | bản sao trong `TransferDocumentVM` |

  Map 1-1 giữa cây và ô tìm:

  | Cây (`prepareForUserLookup`) | Ô tìm (`buildUserSearchScopeOrgIds`) |
  |---|---|
  | `orgVTs` ≠ rỗng → `getTopMostOrgs(orgVTs)` + `ARG_TREE_FILTER_ORG = orgVTs` | id của `orgVTs`, có gọi `addVpubParentOrg` |
  | `orgVTs` rỗng → `ARG_TREE_ROOT = [orgLevelOne]`, không bộ lọc, mở hết cây con theo DB | id `orgLevelOne` + `collectChildOrgs(orgLevelOne)` |
  | không vào nhánh hẹp | `findAllChildOrgIds(root)` |

  ⚠ **NỢ KỸ THUẬT — 3 cặp hàm phải sửa cả hai bên:** `addVpubParentOrg` · `checkUserRoleLevel0` · và tập đơn vị trong `buildUserSearchScopeOrgIds` ↔ `prepareForUserLookup`. Cả 3 chỗ đã ghi comment `SUA MOT BEN THI SUA CA HAI`. Đã thử tách ra `com.viettel.voffice.util.UserLookupScopeUtil` nhưng **bỏ phương án đó** theo quyết định 2026-10-07 (giữ diff nhỏ, không đụng đường dẫn cây đang chạy ổn). Nếu sau này lệch lại lần nữa thì nên tách thật.

- **Tại sao không bị `CONNECT BY` kéo cả tỉnh khi thêm id UBND:** `doSearchReceiver` tính `isVTProcessDepartmentDocument = isVTOfOrg && (orgRangeState == 0 \|\| tabDoc == 0)` — đúng điều kiện mà VPUB được thêm vào (`addVpubParentOrg` chỉ chạy khi `orgVTs` không rỗng, mà nhánh đó cần biểu thức VT = true) ⇒ `current = true` ⇒ `onlyParentGroup=1` ⇒ `StaffDAO.getListUserLongPress` lọc `u.SYS_ORGANIZATION_ID IN (…)` **chính xác**, không dùng `START WITH … CONNECT BY`. **Không sửa `doSearchReceiver`** — nó vốn đã đúng.
- `initSearchScopeOrgIds()` chỉ tính phạm vi đơn vị legacy khi **không** áp phạm vi YC, tránh query thừa.

## 4. Đã gỡ

**Bỏ lọc CÁ NHÂN (2026-10-07)** — YC chỉ còn áp dụng cho tab Đơn vị; web đã gỡ:

| Gỡ gì | Ở đâu |
|---|---|
| Nhánh `docManagerTree` trong `prepareForUserLookup` (cả cây: `ARG_TREE_ROOT`/`ARG_ORG`/`ARG_TREE_CHILDREN_LOADER`, lẫn danh sách: `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID`) | `MultiTypeObjectLookupVM` |
| Field `selectableScopeBuiltOrgId`, nhánh đọc arg, nhánh `getDocManagerTransferOrgIds` trong `getScopeOrgIds()`; `isSelectableScopeMode()` chỉ còn `selectableScopeIdentifierCode` | `UserWSLookupVM` |
| Hằng `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` | `SysOrganizationLookupVM` |
| Ô tìm cá nhân: tách `searchScopeUserOrgIds` (logic cũ) khỏi `searchScopeOrgIds` (YC); bỏ `\|\| isDocManagerTransferOut()` trong `isVTProcessDepartmentDocument` | `TransferDocumentVM` |

Giữ lại: `CommonBusiness.getDocManagerTransferOrgIds` (không ai gọi, đã ghi comment) và **toàn bộ BE** — endpoint `get-doc-manager-transfer-org-ids` vẫn sống.

⚠ **Đính chính mô tả của tài liệu này so với code BE thực tế** (kiểm 2026-10-07): phần "phạm vi CÁ NHÂN" mà các khối *Cập nhật 2026-10-02 (2)* mô tả — `userOrgIds`, `userRootOrg`, `VhrOrgServiceImpl.findDocManagerUserParentOrg`, xử lý VPUB ở BE — **không tồn tại trong backend2.0**, đã bị revert trước khi có yêu cầu bỏ lọc cá nhân (`fda5937e3` ở web, `3e44447b3` cho màn dự thảo). `GetDocManagerTransferScopeResponseDTO` hiện chỉ có `builtOrg`, `builtOrgDepth`, `selectableOrgIds`, `descendantOrgIds`. Endpoint `get-doc-manager-transfer-org-ids` còn, nhưng trả **id đơn vị trong phạm vi dưới 1 node theo `builtOrg.path`**, không phải "phạm vi cá nhân" như bảng ở 3.1 viết.

**Bản BE đầu (commit `4fdff173b`)**: endpoint `POST /api/vhr-org/get-list-org-identifier-code` + `VhrOrgService/Repository.getListOrgHasIdentifierCode` + helper `selectOrgHasIdentifierCode` — không còn ai gọi (ngang cấp giờ tính theo độ sâu path).

**Bản web đầu (commit `23bf242ec`)**

- Dựng cây thủ công ở web (`findAncestors`, `buildOrgSubTree`, `cloneOrg`), `CommonBusiness.getListOrgHasIdentifierCode`.
- `findOrgHasIdentifierCode` ở `SysOrganizationJpaDao / Service / Facade / ISysOrganization` (vi phạm "không thêm DAO legacy ở web").
- Chặn click cây + key i18n `voffice.document.transferDoc.invalidOrg`.

## 5. Kiểm thử

1. Văn thư Sở A, tab Đã cấp số, radio *Văn bản đơn vị* → Chuyển → Chọn đơn vị: cây gốc → UBND tỉnh → Sở A (mở sẵn); Sở khác có mã: lá nếu không còn con có mã, mở được nếu có (chỉ hiện con có mã); đơn vị có mã ở **cấp khác** Sở A (sâu hơn/nông hơn) cũng hiện và chọn được; bấm `+` Sở A → phòng ban hiện dần (Network: 1 call `children`/lần mở).
2. Danh sách tab Đơn vị: click UBND tỉnh → có UBND tỉnh, Sở A + phòng, mọi đơn vị có mã bên dưới; **không** có phòng không mã của Sở khác. Tìm nhanh "phòng" (không mã) của Sở khác → không ra; tìm đơn vị có mã ở cấp khác → ra.
3. **Tab Cá nhân — phải ĐÚNG NHƯ TRƯỚC YC** (2026-10-07): cây **không** có nhánh BE, mở con theo DB; danh sách user **không** bị ẩn theo đơn vị ban hành. Cách kiểm: mở cùng màn trên bản trước YC (hoặc trên màn chuyển VB khác không thuộc YC) rồi so cây + số bản ghi + phân trang — phải trùng. Network: **không** có call `get-doc-manager-transfer-children` / `-org-ids` khi ở tab Cá nhân.
   Kiểm thêm: danh sách cá nhân phải có lại những user mà bản YC đã lọc mất do đi `getListUserLongPress` (`IS_DEFAULT IN (1,2)`, `r.CODE IN ('LDDV','TTDV','NV')`).
4. Ô "Tên đơn vị…" trong popup Chuyển (**vẫn áp YC**): gõ phòng (không mã) của Sở B → không ra; gõ Sở B, UBND tỉnh, đơn vị cấp 0, phòng của Sở A → ra.
   Ô "Họ tên, email…" (**đã đồng bộ với cây**): **phép thử chính** — gõ từng người ra ở ô tìm rồi bấm vào cây: đơn vị của người đó **phải có** trên cây cá nhân. Và ngược lại: gõ người của Sở khác → **không ra**.
5. Radio *Văn bản cá nhân* (orgRangeState=1) → hành vi cũ (giới hạn cấp 1). Chờ cấp số → cấp số → chi tiết → Chuyển → áp phạm vi mới.
6. Hồi quy: VB đến, chuyển tự do, chuyển nhiều VB, người không phải văn thư → `getDocManagerTree()` trả null, `treeChildrenLoader` null → tree model đi nhánh DB cũ.
7. **Văn thư VPUB** (ngoại lệ được giữ): tab Cá nhân → cây phải có **UBND tỉnh → VPUB → phòng của VPUB**; **không** được hiện Sở/đơn vị con khác của UBND. Click **UBND tỉnh** → ra user của chính UBND tỉnh (số bản ghi + phân trang khớp). Click VPUB → user VPUB. Ô tìm nhanh "Họ tên, email…" **cũng phải ra user của UBND tỉnh**, nhưng **không** ra user các Sở con khác của UBND (đây là case dễ vỡ nhất: nếu ra cả Sở tức là BE đang `CONNECT BY` thay vì `IN`).
8. Văn thư đơn vị **không phải VPUB**: tab Cá nhân phải **không** giật lên đơn vị cha — y như trước YC.
9. Hồi quy tính năng KHÁC dùng chung `isSelectableScopeMode()`: màn *Tạo dự thảo* → nơi nhận cá nhân dự kiến (`DocumentDraftVM`, `ARG_SELECTABLE_SCOPE_IDENTIFIER_CODE`) phải **không đổi** — vẫn chỉ ra user của đơn vị có mã định danh.

## 6. Màn TẠO DỰ THẢO — nơi nhận cá nhân dự kiến (2026-10-07)

Màn *Tạo dự thảo* có popup chọn **nơi nhận cá nhân dự kiến** (`DocumentDraftVM.doSelectReceiverList`) và ô tìm nhanh cá nhân (`doSearchReceiver`). Phần này cũng thuộc YC (commit `5ebdcc69d` *feat<text>: check list user auto send*) nên **cũng đưa về code trước YC**, kèm luật UBND.

**Khác màn chuyển văn bản ở MỐC:**

| | Mốc phạm vi cá nhân |
|---|---|
| Màn chuyển VB | **đơn vị ban hành** — `handlingOrg` / `doc.builtGroupId` |
| Màn tạo dự thảo | **đơn vị gốc** — `sysOrg` = `SessionUtil.getSysOrganization(httpSession)`, tức đơn vị của người đang đăng nhập |

### 6.1 Đã gỡ

| Gỡ gì | Ở đâu |
|---|---|
| `buildIdentifierCodeTree()` cho tab Cá nhân + `ARG_SELECTABLE_SCOPE_IDENTIFIER_CODE` | `DocumentDraftVM.doSelectReceiverList` |
| Ô tìm cá nhân dùng `searchScopeOrgIds` (phạm vi mã định danh) + ép `onlyParentGroup = true` | `DocumentDraftVM.doSearchReceiver` — trả về `current = false` như trước YC |
| Toàn bộ cơ chế lọc theo phạm vi: `selectableScopeIdentifierCode`, `isSelectableScopeMode()`, `getScopeOrgIds()`, `scopeOrgIdsCache`, `staffEntity.setCheckListGroup(true)`, 2 nhánh trong `getPagingCount`/`findDataListSysUser` | `UserWSLookupVM` — **không còn ai dùng** sau khi bỏ cả 2 YC (màn chuyển đã gỡ trước đó) |
| Hằng `ARG_SELECTABLE_SCOPE_IDENTIFIER_CODE` | `SysOrganizationLookupVM` |

**GIỮ NGUYÊN phần ĐƠN VỊ:** popup chọn *đơn vị* tự động chuyển VB (`SysOrganizationLookupVM`) và ô tìm nhanh đơn vị vẫn dùng `buildIdentifierCodeTree()` + `getIdentifierCodeOrgIds()` (mọi đơn vị có mã định danh + mọi đơn vị cấp 0). Chỉ phần **cá nhân** bị gỡ.

### 6.2 Luật UBND + hình dạng cây

**Lỗi đã gặp khi làm (ảnh đối chiếu của DEV 2026-10-07):** cùng đơn vị *VĂN PHÒNG ỦY BAN* nhưng hai màn ra cây khác nhau — màn phát hành chỉ hiện `ỦY BAN NHÂN DÂN TỈNH KHÁNH HÒA → VĂN PHÒNG ỦY BAN → các phòng`, còn màn dự thảo bung **toàn bộ Sở con của UBND tỉnh** (Sở Khoa học và Công nghệ, Sở Công Thương, Sở Y tế…). Hai nguyên nhân:

| # | Nguyên nhân | Sửa |
|---|---|---|
| 1 | Màn phát hành có **bộ lọc cây** `ARG_TREE_FILTER_ORG = orgVTs` nên UBND tỉnh chỉ hiện đúng nhánh VPUB. Màn dự thảo chỉ đặt UBND tỉnh làm **gốc, không lọc** → cây mở hết cây con theo DB | Giật lên UBND tỉnh nhưng **treo đúng một nhánh VPUB** bằng `clone()` + `setListOrgLimitOneLevel([VPUB])` — đúng cách `BussinessUtil.getGiveAdviceTreeRootOrgs` đang dùng. Không cần bộ lọc, không cần `findAllOrgVT`/`getTopMostOrgs` |
| 2 | Công thức quy về đơn vị cấp 1 **khác nhau**: màn phát hành `orgLevel > 2` → `pathParts[3]` (ra VPUB); màn dự thảo `orgLevel > 1` → `pathParts[2]` (ra thẳng UBND tỉnh) | Màn dự thảo dùng **cùng công thức** với màn phát hành |

Ba hàm trong `DocumentDraftVM`:

| Hàm | Việc |
|---|---|
| `resolveReceiverBaseOrg()` | `sysOrg` → đơn vị cấp 1 theo path, **cùng công thức** màn phát hành (`orgLevel > 2` → `pathParts[3]`) |
| `resolveReceiverTreeRootOrg()` | gốc cây: mốc là VPUB → trả `clone()` của đơn vị cha (UBND tỉnh) có `listOrgLimitOneLevel = [VPUB]` |
| `initSearchScopeUserOrgIds()` | phạm vi ô tìm: `findAllChildOrgIds(mốc)` (`START WITH … CONNECT BY` nên đã gồm chính mốc) + id đơn vị cha nếu mốc là VPUB |

Cây và ô tìm đều đi từ `resolveReceiverBaseOrg()` nên **không thể lệch phạm vi** — đúng bài học từ màn chuyển văn bản.

⚠ **Thay đổi hành vi cho MỌI người soạn, không riêng VPUB:** đổi công thức từ `pathParts[2]` sang `pathParts[3]` làm mốc **hẹp đi một cấp**. Người soạn thuộc một Sở trước đây thấy cả cây từ đơn vị cấp 0, giờ chỉ thấy Sở của mình đổ xuống. Đây là chủ đích để hai màn khớp nhau, nhưng cần Tester xác nhận với người dùng thật.

**Vì sao vẫn cần luật VPUB dù công thức có vẻ đã đủ:** nhánh quy về cấp 1 chỉ chạy khi `sysOrg.getOrgLevel() > 2`, mà **`ORG_LEVEL` là cột dữ liệu không tin cậy** trong hệ thống này (chính vì vậy endpoint `get-list-org-identifier-code` bản đầu lọc theo `orgLevel` đã bị xóa — xem mục 4). `orgLevel` null hoặc nhỏ thì `baseOrg = sysOrg`; nếu `sysOrg` là VPUB thì vẫn phải giật lên UBND tỉnh. `resolveReceiverTreeRootOrg` chỉ dựa vào id cấu hình `sysOrganization.id.vpub` + `ORG_PARENT_ID`, không phụ thuộc `ORG_LEVEL`.

### 6.3 Kiểm thử

1. Người soạn thuộc **VPUB**, màn Tạo dự thảo → *Chọn cá nhân nhận*: cây phải **giống hệt** tab Cá nhân của popup *Chuyển văn bản* ở màn phát hành — `ỦY BAN NHÂN DÂN TỈNH KHÁNH HÒA → VĂN PHÒNG ỦY BAN → các phòng`. **Không được** hiện Sở Khoa học và Công nghệ, Sở Công Thương, Sở Y tế… hay "Lãnh đạo UBND tỉnh".
2. Click node **UBND tỉnh** → ra user của chính UBND tỉnh. Click VPUB → user VPUB.
3. Ô tìm nhanh cá nhân cùng màn: gõ người của UBND tỉnh → **phải ra**; gõ người của một Sở → **không ra**. Phép thử đối chiếu: gõ ra ai thì bấm vào cây phải thấy đơn vị của người đó.
4. Người soạn **không thuộc VPUB**: cây gốc = đơn vị cấp 1 của chính họ, **không** giật lên đơn vị cha. Đối chiếu với màn phát hành của cùng người đó — phải trùng.
5. Người soạn có `sysOrg` = null → cây về gốc hệ thống (VIG/`treeRootId`).
6. Hồi quy **phần đơn vị**: popup chọn *đơn vị* tự động chuyển VB và ô tìm nhanh đơn vị **không đổi** — vẫn chỉ đơn vị có mã định danh + đơn vị cấp 0.
7. Hồi quy `UserWSLookupVM` ở mọi màn khác dùng popup chọn cá nhân (chuyển VB đến, chuyển tự do, trình ký, xin ý kiến…): phải không đổi, vì cơ chế lọc phạm vi đã gỡ hẳn chứ không chỉ tắt.
