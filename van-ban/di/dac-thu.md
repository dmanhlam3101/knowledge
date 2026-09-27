# Văn bản đi — đặc thù, bẫy, tình trạng kỹ thuật

## Tình trạng: BE gen-1 là chính, đang có gen-2 song song

| Phần | Tầng | Ghi chú |
|---|---|---|
| Toàn bộ vòng đời trình ký/ký/cấp số/ban hành | **BE gen-1** `textAction` (77 endpoint) → `com.viettel.voffice.controler.TextController` → `database/dao/text/TextDAO` (+ `TextProcessDAO`, `TextSignDAO`, `TextSearchDAO`, `TextBookDAO`, `TextCommonDAO`, `TextCheckSpellDAO`, `HistoryChangeSignDAO`, `AutoDigitalSignDAO`) | `TextController` là file logic lớn nhất hệ thống; `getTextDetailThread` có biến thể V2 (`TEXT_DETAIL_VARIANT`) |
| Ký số | gen-1 `Sign` (`SignResource`), `CloudCAAction`, `P12CertAction`, `imageSignAction` | xem `ky-so/` |
| Ban hành/công khai/thay thế | gen-1 `DocumentAction.publish/cancelPublish/editPublicationInformation`, `DocumentPublishAction` | tạo `DOCUMENT` |
| Dự thảo, tiến trình, file (mới) | **gen-2** `TextDraftController` (`/api/text-draft`), `TextProcessController` (`/api/text-process`), `TextFileController` (`/text`), `TextSyncController` (`/api/text`), `DocOutController` (`/api/doc-out`), `TextService`, `TextMarkService`, `OfficePublishedReplacementService` | Hướng đi mới; kiểm tra `ban-do.md` mục 2 xem web đã gọi hàm nào |
| Web | `vm/requisition/*` (20 VM; `RequisitionVM` **17.600 dòng**), `RequisitionBusiness` (124 hàm, gọi cả `DocumentService.*`, `Sign.*`, `TextReportAction.*`), `RequisitionFileBusiness` (cặp trình ký `signBriefcaseAction`) | Nhiều VM nhãn **BE+LEGACY** vì tra cứu đơn vị/người qua `ISysOrganization`, `ISysUser`, `ICommonVoffice` |

## Bẫy

1. **`documentDraft/*` (21 zul) là màn hình chết** — trỏ `com.viettel.voffice.vm.admin.requisition.*` không tồn tại. Màn "Văn bản dự thảo" thật là `requisition/requisition.zul` với `viewType = 11 (VBDT)`. Yêu cầu nào nhắc "màn dự thảo" → làm ở `requisition`.
2. **Một VM, nhiều màn**: `RequisitionVM` phục vụ tất cả `VIEW_TYPE` (dự thảo, trình ký, ký nháy, ký duyệt, xét duyệt, ban hành, đóng dấu…) bằng `if (viewType == ...)`. Sửa một nhánh dễ ảnh hưởng nhánh khác — luôn nêu rõ viewType/tabType bị ảnh hưởng và test các màn còn lại.
3. **`TextStateConstants` (gen-1) và `AppConstants.REQUISITION` (web) là hai bản sao hằng số** — thêm trạng thái phải sửa cả hai + i18n `voffice.appConstants.vbtk.*`.
4. **`TYPE_VBKN = 3` và `TYPE_VBKD = 3` trùng giá trị** trong `AppConstants.REQUISITION` (khác với `VIEW_TYPE.VBKN = 4`, `VBKD = 5`) — đừng suy luận nghiệp vụ từ số, đọc tên.
5. **Ban hành = tạo `DOCUMENT`** và đồng thời gửi văn bản đến cho đơn vị nhận + liên thông + index ES. Sửa ban hành phải xem cả `van-ban/den`, `van-ban/lien-thong`, `tich-hop` (Solr/ES).
6. **Mã hóa file mật**: `FileEncryptMap`, `getPermisionReadFileEncryptMap` — thêm chức năng tải/xem file phải đi qua kiểm tra này.
7. **Trợ lý ký thay / ảnh chữ ký**: `updateSignImageBySecrectary`, `SECRETARY_ROLE_ID_KEY` — logic phân quyền đặc biệt, không phải theo SYS_ROLE thông thường.
8. `textAction.checkShowTransferGiveAdvice.` (có dấu chấm cuối) và vài key khác không nối được endpoint — có thể là bug tên hàm hoặc endpoint đã bị xóa ❓.
9. Ký đối tác ngoài (`listPartnerSign`, `TextPartnerDAO`) là nhánh riêng, ít dùng ❓.
10. **Cây đơn vị khi văn thư phát hành chuyển VB đi** (`MultiTypeObjectLookupVM.buildDocManagerTree()`): **lazy-load hoàn toàn từ BE gen-2**, không dựng cây ở web, không kéo subtree/ngang cấp sẵn.
    - `POST /api/vhr-org/get-doc-manager-transfer-scope {builtOrgId}` (`api.vhr-org.get-doc-manager-transfer-scope`) → chỉ **id**: `builtOrg`, `builtOrgDepth` (số segment `PATH`), `selectableOrgIds` (tổ tiên + đơn vị ban hành + ngang cấp có mã), `descendantOrgIds`. 3 query nhẹ (PK, ids ngang cấp `VhrOrgRepositoryJPA.findOrgIdHasIdentifierCodeByPathDepth`, ids con cháu `findChildrenAllLevel`).
    - `POST /api/vhr-org/get-doc-manager-transfer-children {builtOrgId, parentOrgId}` (`parentOrgId` null = gốc, độ sâu 1) → con trực tiếp **có liên quan**: (a) trong nhánh đơn vị ban hành, (b) tổ tiên đơn vị ban hành, (c) cùng độ sâu + có mã (lá, chọn được), (d) có hậu duệ (c) (`EXISTS … path LIKE o.path||'%'`, node chỉ để mở). Mỗi node kèm `selectable`, `isLeaf` do BE tính (`VhrOrgRepositoryImpl.getDocManagerTransferChildren`). Mobile dùng y hệt.
    - Web: `SysOrganizationTreeModel.ChildrenLoader` (arg `ARG_TREE_CHILDREN_LOADER`, cả `SysOrganizationLookupVM` lẫn `UserWSLookupVM`) gọi BE khi mở nút, **cache kết quả vào `parent.listOrgLimitOneLevel`** vì `CommonTreeModel.getChild(i)` gọi `getChildren` cho từng index; rỗng → `onlyCurrentOrg=true`. Renderer tự mở các node trên path đơn vị ban hành → mở popup ≈ (độ sâu − 1) call nhỏ.
    - Danh sách tab Đơn vị: SQL `id IN (tổ tiên + đơn vị ban hành)` (`ARG_ORG_ID` — cố ý **không** đưa id ngang cấp vào vì `SysOrganizationLookupVM` sẽ `findByIds` cả list) `OR path LIKE builtOrgPath%` (`ARG_SELECTABLE_PATH_PREFIXES` → `SysOrganization.includePathPrefixes`) `OR (độ sâu = N AND identifierCode IS NOT NULL)` (`ARG_SELECTABLE_IDENTIFIER_CODE_DEPTH` → `includeIdentifierCodeDepth`) — xem `SysOrganizationJpaDao.appendInCondition`.
    - Tab Cá nhân: **ẩn hẳn** user ngoài phạm vi — `ARG_SELECTABLE_SCOPE_BUILT_ORG_ID` → `UserWSLookupVM` hỏi `POST /api/vhr-org/get-doc-manager-transfer-org-ids {builtOrgId, orgId=node đang chọn}` rồi gọi `countUserList/getListUser(..., scopeOrgIds, onlyParentGroup=true, ...)` (lọc ở query nên phân trang đúng; `onlyParentGroup=1` + `staffEntity.setCheckListGroup(true)` → gen-1 `getListUserLongPress` lọc `SYS_ORGANIZATION_ID IN` — thiếu `checkListGroup` thì BE bỏ qua danh sách id, chỉ lọc `= sysOrgId`, kèm ràng buộc `IS_DEFAULT IN (1,2)` + role `LDDV/TTDV/NV`). (Endpoint `get-list-org-identifier-code` của bản đầu đã xóa.)
    - **Điều kiện áp dụng** = `TransferDocumentVM.isDocManagerTransferOut(...)` (dùng chung 2 VM): văn thư (`isDocManager`) + là văn thư của đơn vị ban hành (`isVTOfOrg`) + chuyển đi 1 văn bản + `orgRangeState != 1` (văn bản đơn vị; null coi như đơn vị) + `viewType` ∈ DCS/DBH/ALL. Bốn đường vào: tab Đã cấp số/Đã ban hành/Tất cả (`DocumentOutVM` truyền `ARG_VIEW_TYPE`, `ARG_ORG_RANGE_STATE`) và **Chờ cấp số sau khi cấp số** (`RequisitionViewIssueNumberVM` → `DocumentViewDetailVM` với `doc.docManagerPromulgate=true` → `viewType=DCS`, `orgRangeState=0`).
    - Hai ô tìm nhanh trong popup Chuyển (`doSearchReceiver`/`doSearchOrg`): `searchScopeOrgIds` = `selectableOrgIds` + `descendantOrgIds` từ scope; tìm cá nhân ép `onlyParentGroup=1` để gen-1 lọc `SYS_ORGANIZATION_ID IN` chính xác (mặc định `lstGroupId` là CONNECT BY kéo cả con cháu).
    - **Không chặn ở click cây** (cây chỉ để lọc). Bản đầu (commit `23bf242ec`) dựng cây thủ công ở web + DAO legacy — đã gỡ.
11. **Tab Cá nhân liệt kê user theo prefix `pathOrg`** (`UserWSLookupVM`), không theo `ARG_ORG_ID` → click tổ tiên vẫn thấy user của mọi đơn vị bên dưới; user ngoài phạm vi chỉ bị **disable** (không ẩn) — chốt với KH 2026-09.
12. **BE gen-2 `@PostMapping` nhận DTO bắt buộc có `@RequestBody`** — web gửi JSON body qua `Business.servePostRequest` → `ServiceConnection.sendPostRestful`; thiếu annotation thì mọi trường DTO = null (đã dính ở `get-list-org-identifier-code`).

## Quyết định / lịch sử (từ comment code)

- 2018-12 "Pitagon": thêm bộ `TYPE_VB*`.
- 2025-03 LongNP: thêm màn "Văn bản dự thảo" (`VBDT = 11`) trong `RequisitionVM` — tức màn dự thảo hiện tại mới được gộp vào requisition từ 2025, trước đó là `documentDraft/*` (nay chết).
- 2025-12 → 2026-03: nhiều SQL tối ưu (`add_confirm_time_table_text_process`, `add_index_table_text_and_document`, `add_deadline_date_table_text`) + tài liệu `PERFORMANCE_OPTIMIZATION_*.md` trong `backend2.0/backendvoffice/` — hiệu năng tìm kiếm văn bản là chủ đề nóng.

## Khi nhận yêu cầu ở phân hệ này

- Sửa luồng ký/bước ký → `van-ban/luong-xu-ly` (gen-2 `flow-manager`) trước, sau đó `TextController`.
- Thêm hành động mới trên văn bản (vd. thu hồi, gia hạn ký) → thêm endpoint gen-2 (`TextProcessController`) + hàm `RequisitionBusiness` + nhánh trong `RequisitionVM` theo `viewType`; ghi lịch sử `TEXT_PROCESS_HISTORY`.
- Thêm trạng thái → việc **L** (xem `_chung/cach-lam-chuan/them-truong-du-lieu.md` §2).
