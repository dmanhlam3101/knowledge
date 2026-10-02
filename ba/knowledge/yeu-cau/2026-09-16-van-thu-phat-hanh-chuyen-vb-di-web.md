# Văn thư phát hành chuyển VB đi — mô tả code WEB (+ BE)

**Phân hệ:** `van-ban/di` · **Tầng:** Web (ZK) + BE gen-2 · **Ngày:** 2026-09-16 · **Thay thế** phần "hướng dẫn kỹ thuật" của `2026-09-15-loc-don-vi-nhan-khi-ban-hanh.md` (bản đó còn giả định dùng `orgLevel` và dựng cây ở web — đã bỏ).

> **Cập nhật 2026-10-02 — bỏ "ngang cấp":** nhóm thứ 4 đổi từ "cùng độ sâu path + có mã" thành **mọi đơn vị có mã định danh** (mọi cấp/nhánh); thêm **mọi đơn vị cấp 0** (`LEVEL_0_PATH_DEPTH = 2`, không xét mã, **không** phụ thuộc cấp của đơn vị ban hành). Endpoint/DTO không đổi.

> **Cập nhật 2026-10-02 (2) — phạm vi CÁ NHÂN tách riêng:** tab Cá nhân + ô tìm cá nhân chỉ trong **đơn vị ban hành + con cháu**; đơn vị ban hành = **VPUB** (`sysOrganization.id.vpub`, BE đọc qua `FuncUtils.environment`) thì thêm cá nhân của **chính đơn vị cha trực tiếp** (UBND tỉnh), không lấy đơn vị con khác của UBND (`VhrOrgServiceImpl.findDocManagerUserParentOrg`). Đơn vị có mã / cấp 0 ngoài nhánh chỉ áp dụng cho tab Đơn vị.

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
| `POST /api/vhr-org/get-doc-manager-transfer-scope` | `GetDocManagerTransferDTO{builtOrgId}` | `GetDocManagerTransferScopeResponseDTO`: `builtOrg`, `builtOrgDepth`, `selectableOrgIds` (tổ tiên + đơn vị ban hành + mọi đơn vị có mã — **chỉ id**), `descendantOrgIds` (chỉ id), `userOrgIds` + `userRootOrg` (phạm vi/gốc cây **cá nhân**) | 3: `findById`, `VhrOrgRepositoryJPA.findOrgIdHasIdentifierCode` + `findOrgIdByPathDepth(2)`, `findChildrenAllLevel` |
| `POST /api/vhr-org/get-doc-manager-transfer-children` | `GetDocManagerTransferDTO{builtOrgId, parentOrgId}` (`parentOrgId` = nút đang mở, null = gốc) | `List<VhrOrgResponseDTO>` con trực tiếp **có liên quan**, mỗi node có `selectable`, `isLeaf` | 1: `VhrOrgRepositoryImpl.getDocManagerTransferChildren` |
| `POST /api/vhr-org/get-doc-manager-transfer-org-ids` | `GetDocManagerTransferDTO{builtOrgId, orgId}` (`orgId` = nút đang chọn, null = toàn bộ phạm vi) | `List<Long>` id đơn vị trong **phạm vi cá nhân** (đơn vị ban hành + con cháu; VPUB thêm chính đơn vị cha) nằm dưới `orgId` | 1: `VhrOrgRepositoryImpl.getDocManagerTransferOrgIds(builtPath, parentOrgId, nodePath)` |

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
  - `childrenLoader` → `ARG_TREE_CHILDREN_LOADER`; `doc.builtGroupId` → `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` (tab Cá nhân lọc danh sách).
- `prepareForOrgLookup` (tab Đơn vị) nhận `ARG_TREE_ROOT`, `ARG_ORG`, `ARG_ORG_ID`, `ARG_SELECTABLE_PATH_PREFIXES`, `ARG_SELECTABLE_HAS_IDENTIFIER_CODE`, `ARG_SELECTABLE_ALL_PATH_DEPTH`, `ARG_TREE_CHILDREN_LOADER`; `prepareForUserLookup` (tab Cá nhân) nhận `ARG_TREE_ROOT`, `ARG_ORG`, `ARG_TREE_CHILDREN_LOADER`, `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID`.
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

### 3.6 Web — tab Cá nhân: `UserWSLookupVM`

- **Cây riêng** (sửa 2026-10-02): `MultiTypeObjectLookupVM.prepareForUserLookup` truyền `DocManagerTree.userRoots`, **không** truyền `childrenLoader` (cây mở con theo DB). Thường: gốc = entity đơn vị ban hành. VPUB: gốc = clone đơn vị cha `onlyCurrentOrg = true`, `listOrgLimitOneLevel = [VPUB]` (giống `BussinessUtil.getGiveAdviceTreeRootOrgs`).

- Đọc `ARG_TREE_CHILDREN_LOADER`, `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID`; `createSysOrgTree()` set loader.
- **Ẩn hẳn user ngoài phạm vi** (không chỉ disable): `isSelectableScopeMode()` = có `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` → `getPagingCount`/`findDataList` đi nhánh riêng:
  `scopeOrgIds = commonBusiness.getDocManagerTransferOrgIds(builtOrgId, nodeId)` (nodeId = `staffEntity.getSysOrgId()`, cache theo node) rồi gọi `countUserList/getListUser(staffEntity, scopeOrgIds, **true**, …)`.
  `true` = `onlyParentGroup=1` ⇒ gen-1 `StaffDAO.getListUserLongPress`; **phải kèm `staffEntity.setCheckListGroup(true)`** thì mới lọc `u.SYS_ORGANIZATION_ID IN (…)` — không set thì rơi vào `= staff.sysOrgId` (ra đúng user của node đang chọn, kể cả node chỉ để mở cây) (mặc định `lstGroupId` là `CONNECT BY` kéo cả con cháu → không dùng được vì tổ tiên sẽ kéo cả tỉnh). Lọc ở query nên **phân trang/`count` vẫn đúng** (lọc sau khi phân trang thì số trang sẽ lệch).
  ⚠ Hệ quả: ở chế độ này danh sách đi qua `getListUserLongPress` (giống hệt ô tìm nhanh của popup Chuyển) → thêm ràng buộc `u.IS_DEFAULT IN (1,2)` và `r.CODE IN ('LDDV','TTDV','NV')` khi `transferDocOut` — cần QA đối chiếu với danh sách cũ.
- `disableCheckbox` giữ nguyên logic cũ (chỉ kiểm chứng thư mật); lớp disable theo phạm vi đã **bỏ** vì danh sách không còn trả user ngoài phạm vi.

### 3.7 Web — 2 ô tìm nhanh trong popup Chuyển: `TransferDocumentVM`

- `initSearchScopeOrgIds()`: nếu `isDocManagerTransferOut()` → `searchScopeOrgIds = buildDocManagerSearchScopeOrgIds()` = `selectableOrgIds` + builtOrgId + `descendantOrgIds` (từ scope).
- `doSearchOrg` → `findByConditionV2(..., searchScopeOrgIds, ...)` → `id IN`.
- `doSearchReceiver` → `requisitionBusiness.getListUser(..., searchScopeUserOrgIds (= scope.userOrgIds; fallback searchScopeOrgIds), current = … || isDocManagerTransferOut(), ...)`. `current=true` ⇒ `onlyParentGroup=1` ⇒ gen-1 `StaffDAO.getListUserLongPress` lọc `u.SYS_ORGANIZATION_ID IN (…)` **chính xác**. Nếu không ép, `lstGroupId` mặc định là `START WITH … CONNECT BY` kéo cả con cháu của từng id (đưa tổ tiên vào là ra cả tỉnh).

## 4. Đã gỡ

**Bản BE đầu (commit `4fdff173b`)**: endpoint `POST /api/vhr-org/get-list-org-identifier-code` + `VhrOrgService/Repository.getListOrgHasIdentifierCode` + helper `selectOrgHasIdentifierCode` — không còn ai gọi (ngang cấp giờ tính theo độ sâu path).

**Bản web đầu (commit `23bf242ec`)**

- Dựng cây thủ công ở web (`findAncestors`, `buildOrgSubTree`, `cloneOrg`), `CommonBusiness.getListOrgHasIdentifierCode`.
- `findOrgHasIdentifierCode` ở `SysOrganizationJpaDao / Service / Facade / ISysOrganization` (vi phạm "không thêm DAO legacy ở web").
- Chặn click cây + key i18n `voffice.document.transferDoc.invalidOrg`.

## 5. Kiểm thử

1. Văn thư Sở A, tab Đã cấp số, radio *Văn bản đơn vị* → Chuyển → Chọn đơn vị: cây gốc → UBND tỉnh → Sở A (mở sẵn); Sở khác có mã: lá nếu không còn con có mã, mở được nếu có (chỉ hiện con có mã); đơn vị có mã ở **cấp khác** Sở A (sâu hơn/nông hơn) cũng hiện và chọn được; bấm `+` Sở A → phòng ban hiện dần (Network: 1 call `children`/lần mở).
2. Danh sách tab Đơn vị: click UBND tỉnh → có UBND tỉnh, Sở A + phòng, mọi đơn vị có mã bên dưới; **không** có phòng không mã của Sở khác. Tìm nhanh "phòng" (không mã) của Sở khác → không ra; tìm đơn vị có mã ở cấp khác → ra.
3. Tab Cá nhân: cây chỉ có Sở A + phòng (không có UBND tỉnh, Sở B, cấp 0 khác); click Sở A → user Sở A + phòng; số bản ghi/phân trang khớp. Văn thư **VPUB**: cây = UBND tỉnh (chỉ 1 con VPUB) → VPUB → phòng; click UBND tỉnh → user của chính UBND tỉnh + VPUB (+ phòng), **không** có user các Sở.
4. Ô "Tên đơn vị…" trong popup Chuyển: gõ phòng (không mã) của Sở B → không ra; gõ Sở B, UBND tỉnh, đơn vị cấp 0, phòng của Sở A → ra. Ô "Họ tên, email…": chỉ ra user Sở A + phòng; gõ user Sở B / UBND tỉnh → không ra. VPUB: ra user VPUB + phòng và user của chính UBND tỉnh; gõ user một Sở → không ra.
5. Radio *Văn bản cá nhân* (orgRangeState=1) → hành vi cũ (giới hạn cấp 1). Chờ cấp số → cấp số → chi tiết → Chuyển → áp phạm vi mới.
6. Hồi quy: VB đến, chuyển tự do, chuyển nhiều VB, người không phải văn thư → `getDocManagerTree()` trả null, `treeChildrenLoader` null → tree model đi nhánh DB cũ.
