# Văn thư phát hành chuyển VB đi — mô tả code WEB (+ BE)

**Phân hệ:** `van-ban/di` · **Tầng:** Web (ZK) + BE gen-2 · **Ngày:** 2026-09-16 · **Thay thế** phần "hướng dẫn kỹ thuật" của `2026-09-15-loc-don-vi-nhan-khi-ban-hanh.md` (bản đó còn giả định dùng `orgLevel` và dựng cây ở web — đã bỏ).

## 1. Nghiệp vụ

Văn thư của **đơn vị ban hành** chuyển **văn bản đơn vị** ở màn *Văn bản ban hành* chỉ được chọn:

| Nhóm | Định nghĩa (theo `VHR_ORG.PATH`, **không** dùng `ORG_LEVEL`) |
|---|---|
| Cấp cha | mọi đơn vị nằm trên `PATH` của đơn vị ban hành |
| Đơn vị ban hành | `DOCUMENT.BUILT_GROUP_ID` |
| Con cháu | `PATH LIKE '<path đơn vị ban hành>%'` |
| Ngang cấp có mã | **cùng độ sâu path** (số segment) **và** `IDENTIFIER_CODE IS NOT NULL` — không cần cùng cha |

Không được chọn đơn vị con của cơ quan ngang cấp. Tổ tiên của đơn vị ngang cấp ở nhánh khác chỉ hiện trên cây để mở xuống (node "chỉ điều hướng"), **không** báo lỗi khi click — cây chỉ để lọc; việc chặn nằm ở danh sách bên phải.

Lý do dùng độ sâu path: dữ liệu `ORG_LEVEL` sai (vd `/1/148842/9134381/9135455/9135456/` sâu 5 nhưng `ORG_LEVEL = 2`).

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
 ├─ initSearchScopeOrgIds()  ──► BE scope ──► searchScopeOrgIds (2 ô tìm nhanh)
 └─ doSelectObjectsToTransfer ──► MultiTypeObjectLookupVM (popup Chọn đối tượng)
        └─ getDocManagerTree() [cache 1 lần/popup]
             ├─ BE scope      → orgIds, ancestorAndSelfIds, selectablePathPrefixes, identifierCodeDepth, builtOrgNode
             ├─ BE children(parent=null) → roots
             └─ childrenLoader = parent → BE children(parent.id)
        ├─ tab Đơn vị  → SysOrganizationLookupVM  (cây + danh sách đơn vị)
        └─ tab Cá nhân → UserWSLookupVM           (cây + danh sách user)
```

### 3.1 BE gen-2 (`com.viettel.office`)

| Endpoint | Request | Response | Query |
|---|---|---|---|
| `POST /api/vhr-org/get-doc-manager-transfer-scope` | `GetDocManagerTransferDTO{builtOrgId}` | `GetDocManagerTransferScopeResponseDTO`: `builtOrg`, `builtOrgDepth`, `selectableOrgIds` (tổ tiên + đơn vị ban hành + ngang cấp có mã — **chỉ id**), `descendantOrgIds` (chỉ id) | 3: `findById`, `VhrOrgRepositoryJPA.findOrgIdHasIdentifierCodeByPathDepth`, `findChildrenAllLevel` |
| `POST /api/vhr-org/get-doc-manager-transfer-children` | `GetDocManagerTransferDTO{builtOrgId, parentOrgId}` (`parentOrgId` = nút đang mở, null = gốc) | `List<VhrOrgResponseDTO>` con trực tiếp **có liên quan**, mỗi node có `selectable`, `isLeaf` | 1: `VhrOrgRepositoryImpl.getDocManagerTransferChildren` |
| `POST /api/vhr-org/get-doc-manager-transfer-org-ids` | `GetDocManagerTransferDTO{builtOrgId, orgId}` (`orgId` = nút đang chọn, null = toàn bộ phạm vi) | `List<Long>` id đơn vị **chọn được** nằm dưới node `orgId` (không gồm node "chỉ để mở cây") | 1: `VhrOrgRepositoryImpl.getDocManagerTransferOrgIds` |

Cả 3 endpoint dùng chung **một** DTO request `dto.request.GetDocManagerTransferDTO {builtOrgId, parentOrgId, orgId}` — key giữ nguyên như bản đã bàn giao cho mobile (`children` dùng `parentOrgId`, `org-ids` dùng `orgId`).

Con "có liên quan" của `parentOrgId` (SQL `WHERE org_parent_id = :p AND (a ∨ b ∨ c ∨ d)`):
- (a) trong nhánh đơn vị ban hành → `selectable=true`, `isLeaf` theo DB;
- (b) tổ tiên đơn vị ban hành → `selectable=true`, `isLeaf=0`;
- (c) cùng độ sâu + có mã → `selectable=true`, `isLeaf=1` (không kéo con của ngang cấp);
- (d) có hậu duệ (c) (`EXISTS … d.path LIKE o.path||'%'`) → `selectable=false`, `isLeaf=0` (chỉ để mở).

Service: `VhrOrgServiceImpl.getDocManagerTransferScope / getDocManagerTransferChildren`. Độ sâu = `LENGTH(path) - LENGTH(REPLACE(path,'/','')) - 1`.

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
  - `identifierCodeDepth` = `builtOrgDepth` → `ARG_SELECTABLE_IDENTIFIER_CODE_DEPTH`;
  - `childrenLoader` → `ARG_TREE_CHILDREN_LOADER`; `doc.builtGroupId` → `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` (tab Cá nhân lọc danh sách).
- `prepareForOrgLookup` (tab Đơn vị) nhận `ARG_TREE_ROOT`, `ARG_ORG`, `ARG_ORG_ID`, `ARG_SELECTABLE_PATH_PREFIXES`, `ARG_SELECTABLE_IDENTIFIER_CODE_DEPTH`, `ARG_TREE_CHILDREN_LOADER`; `prepareForUserLookup` (tab Cá nhân) nhận `ARG_TREE_ROOT`, `ARG_ORG`, `ARG_TREE_CHILDREN_LOADER`, `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID`.
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

- Args mới: `ARG_SELECTABLE_PATH_PREFIXES`, `ARG_SELECTABLE_IDENTIFIER_CODE_DEPTH`, `ARG_SELECTABLE_ORG_IDS`, `ARG_TREE_CHILDREN_LOADER`.
- `createSysOrgTree()` cuối: `treeModel.setChildrenLoader(treeChildrenLoader)`.
- `findDataList / countDataList`: `obj.setIncludePathPrefixes(...)`, `obj.setIncludeIdentifierCodeDepth(...)` (transient mới trên `com.viettel.vps.entity.SysOrganization`).
- DAO `SysOrganizationJpaDao.appendInCondition(query, params, "o.sysOrganizationId", "filter", ids, includePathPrefixes, includeIdentifierCodeDepth)` sinh:
  ```sql
  AND ( o.sysOrganizationId IN (:filter0)
        OR o.path LIKE :filterPath0                                   -- '<builtOrgPath>%'
        OR ((LENGTH(o.path) - LENGTH(REPLACE(o.path,'/','')) - 1) = :filterDepth AND o.identifierCode IS NOT NULL) )
  ```
  dùng ở `findByCondition` và `getCountByCondition` (V2 không đổi). Danh sách chỉ hiện đơn vị hợp lệ → không cần disable.
- Click cây: `onClickTreeItem` giữ nguyên (chỉ set `dataSearch.path` rồi `doSearch`).

### 3.6 Web — tab Cá nhân: `UserWSLookupVM`

- Đọc `ARG_TREE_CHILDREN_LOADER`, `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID`; `createSysOrgTree()` set loader.
- **Ẩn hẳn user ngoài phạm vi** (không chỉ disable): `isSelectableScopeMode()` = có `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` → `getPagingCount`/`findDataList` đi nhánh riêng:
  `scopeOrgIds = commonBusiness.getDocManagerTransferOrgIds(builtOrgId, nodeId)` (nodeId = `staffEntity.getSysOrgId()`, cache theo node) rồi gọi `countUserList/getListUser(staffEntity, scopeOrgIds, **true**, …)`.
  `true` = `onlyParentGroup=1` ⇒ gen-1 `StaffDAO.getListUserLongPress`; **phải kèm `staffEntity.setCheckListGroup(true)`** thì mới lọc `u.SYS_ORGANIZATION_ID IN (…)` — không set thì rơi vào `= staff.sysOrgId` (ra đúng user của node đang chọn, kể cả node chỉ để mở cây) (mặc định `lstGroupId` là `CONNECT BY` kéo cả con cháu → không dùng được vì tổ tiên sẽ kéo cả tỉnh). Lọc ở query nên **phân trang/`count` vẫn đúng** (lọc sau khi phân trang thì số trang sẽ lệch).
  ⚠ Hệ quả: ở chế độ này danh sách đi qua `getListUserLongPress` (giống hệt ô tìm nhanh của popup Chuyển) → thêm ràng buộc `u.IS_DEFAULT IN (1,2)` và `r.CODE IN ('LDDV','TTDV','NV')` khi `transferDocOut` — cần QA đối chiếu với danh sách cũ.
- `disableCheckbox` giữ nguyên logic cũ (chỉ kiểm chứng thư mật); lớp disable theo phạm vi đã **bỏ** vì danh sách không còn trả user ngoài phạm vi.

### 3.7 Web — 2 ô tìm nhanh trong popup Chuyển: `TransferDocumentVM`

- `initSearchScopeOrgIds()`: nếu `isDocManagerTransferOut()` → `searchScopeOrgIds = buildDocManagerSearchScopeOrgIds()` = `selectableOrgIds` + builtOrgId + `descendantOrgIds` (từ scope).
- `doSearchOrg` → `findByConditionV2(..., searchScopeOrgIds, ...)` → `id IN`.
- `doSearchReceiver` → `requisitionBusiness.getListUser(..., searchScopeOrgIds, current = … || isDocManagerTransferOut(), ...)`. `current=true` ⇒ `onlyParentGroup=1` ⇒ gen-1 `StaffDAO.getListUserLongPress` lọc `u.SYS_ORGANIZATION_ID IN (…)` **chính xác**. Nếu không ép, `lstGroupId` mặc định là `START WITH … CONNECT BY` kéo cả con cháu của từng id (đưa tổ tiên vào là ra cả tỉnh).

## 4. Đã gỡ

**Bản BE đầu (commit `4fdff173b`)**: endpoint `POST /api/vhr-org/get-list-org-identifier-code` + `VhrOrgService/Repository.getListOrgHasIdentifierCode` + helper `selectOrgHasIdentifierCode` — không còn ai gọi (ngang cấp giờ tính theo độ sâu path).

**Bản web đầu (commit `23bf242ec`)**

- Dựng cây thủ công ở web (`findAncestors`, `buildOrgSubTree`, `cloneOrg`), `CommonBusiness.getListOrgHasIdentifierCode`.
- `findOrgHasIdentifierCode` ở `SysOrganizationJpaDao / Service / Facade / ISysOrganization` (vi phạm "không thêm DAO legacy ở web").
- Chặn click cây + key i18n `voffice.document.transferDoc.invalidOrg`.

## 5. Kiểm thử

1. Văn thư Sở A, tab Đã cấp số, radio *Văn bản đơn vị* → Chuyển → Chọn đơn vị: cây gốc → UBND tỉnh → Sở A (mở sẵn), các Sở khác là lá; Tỉnh ủy (nếu có Ban cùng độ sâu có mã) mở được, click vào danh sách trống; bấm `+` Sở A → phòng ban hiện dần (Network: 1 call `children`/lần mở).
2. Danh sách tab Đơn vị: click UBND tỉnh → có UBND tỉnh, Sở A + phòng, các Sở có mã; **không** có phòng của Sở khác. Tìm nhanh "phòng" của Sở khác → không ra.
3. Tab Cá nhân: click UBND tỉnh → chỉ thấy user của UBND tỉnh, Sở A (+ phòng), các Sở có mã — **không thấy** user phòng của Sở khác (kiểm cả số bản ghi/phân trang); click Sở B → user của Sở B (tick được), không có user phòng dưới Sở B; click phòng dưới Sở A → tick được.
4. Ô "Họ tên, email…" / "Tên đơn vị…" trong popup Chuyển: gõ user/phòng của Sở B → không ra; gõ Sở B, UBND tỉnh, phòng của Sở A → ra.
5. Radio *Văn bản cá nhân* (orgRangeState=1) → hành vi cũ (giới hạn cấp 1). Chờ cấp số → cấp số → chi tiết → Chuyển → áp phạm vi mới.
6. Hồi quy: VB đến, chuyển tự do, chuyển nhiều VB, người không phải văn thư → `getDocManagerTree()` trả null, `treeChildrenLoader` null → tree model đi nhánh DB cũ.
