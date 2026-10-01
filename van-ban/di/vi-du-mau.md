# Văn bản đi (từ cấp số trở đi) — ví dụ mẫu để copy pattern

> Viết lại 2026-09-30. Viết tắt đường dẫn giống `nghiep-vu.md`. Mẫu **gen-2** ưu tiên cho code mới; mẫu **gen-1** để hiểu/sửa luồng hiện có.
> Mẫu của giai đoạn trước ban hành (thêm hành động lên dự thảo kiểu `forward-to-assign-number`, xin ý kiến) xem `xu-ly-cong-viec/vi-du-mau.md`; ký số xem `ky-so/vi-du-mau.md`; mẫu cũ ngoài phạm vi giữ ở mục G.
> (sửa 2026-09-30: bản cũ mục C trỏ `requisition_issue_number_view_detail.zul` + `RequisitionViewIssueNumberVM` là màn cấp số — sai, đó là màn xem danh sách số đã cấp; mục B ghi `rejectPublishDocument` gọi `rejectSignDocument`/`cancelPublish` ❓ — thực tế gọi `textAction.cancelDocumentPublish`; mục E gắn `OfficePublishedReplacementService` vào công khai/thay thế — sai, đó là đơn vị ban hành thay thế.)

## A. Hành động của văn thư trên văn bản chờ cấp số, có popup nhập lý do rồi đổi trạng thái — mẫu "Hủy ban hành / Từ chối cấp số"

| Tầng | File | Copy phần nào |
|---|---|---|
| Nút (chi tiết) | `ZUL/requisition/requisition_viewDetail.zul:4796-4802` (`distroyTab`, `visible="@load(vm.isViewRejectPublish)"`) | Cách gắn nút + cờ hiển thị theo `viewType`/trạng thái |
| Icon (lưới) | `ZUL/requisition/requisition_search.zul:1330-1336` (`checkViewRejectPromulgate(data) and vm.getVisible(data)`) | Nhớ thêm cả ở lưới — hai chỗ |
| Cờ hiển thị | RVDVM `checkPublish` :1896-1912; RVM `checkViewRejectPromulgate` :8193-8204 | Điều kiện theo `COMBOBOX_MENU.VBBH.DKD/DBH` |
| Mở popup | RVDVM `docDestroyTab` :3490-3516 → `ViewUtil.createLookupRejectPublish` (`ViewConstant.java:338`); RVM `doRejectPromulgate` :8311-8324 tái dùng RVDVM | Truyền id qua `args`, nhận kết quả qua `SearchEvent`, refresh `EVENT_QUEUE_HOME_PAGE` + `EVENT_QUEUE_LOOKUP_HIGHLIGHTED` |
| Popup lý do | `ZUL/requisition/rejectPublish.zul` + `WEB/voffice/vm/requisition/RejectPublishVM.java:59-86` | Validate bắt buộc, `CustomMessageBox` xác nhận |
| Business | `BIZ/RequisitionBusiness.java:2417-2435` `rejectPublishDocument` → `serveProcessing("textAction.cancelDocumentPublish", params)` | Đóng gói JSON vào 1 tham số |
| BE | TC `cancelDocumentPublish` :1953-2003 (IDOR + kiểm trạng thái) → `TDAO.cancelDocumentPublish` :4003-4110 | **Luôn** kiểm `validateGetTextDetail` và trạng thái nguồn trước khi đổi |

Popup lý do dạng chung (có file, SMS, chọn người) thì copy `ConfirmInputVM` như `doRejectVBBHWaitForNumber` (RVDVM:5106-5158).

## B. Form cấp số theo sổ (gen-1 + 1 endpoint gen-2)

`RVDVM.docCreateTab` (:3364-3417) → `ZUL/document/reportSendReceiveDoc/issussDocument.zul` + DLVM:
- nạp sổ `TextBookBusiness.getTextBooksByOrgIdAndDocType` (DLVM:877-910) → `/textBookAction/getTextBooksByOrgIdAndDocType` → `TBDAO.getTextBooksByOrgIdAndDocType` :1228;
- số gợi ý `getNextRegisterNumberDataByTextBookId` (DLVM:388-402) → `TBDAO.getNextRegisterNumberByTextBookId` :1064-1124 (trả cả số cấp bù);
- kiểm trùng gen-2 `DocumentBusiness.isDuplicatedRegisterNumberDocOut` (`BIZ/DocumentBusiness.java:6140-6151`, `serveGetRequest("api.doc-out.is-duplicated-register-number?...")`) → `BE2/controller/DocOutController.java:40-47` → `DocOutServiceImpl.checkDuplicateRegisterNumber` :863 → `BE2/repositories/impl/DocumentRepositoryImpl.java:1905-1950`;
- lưu `RequisitionBusiness.publishDocument` → `textAction.documentPromulgate` → TC :1685 → `TDAO.updateDocumentPromulgate` :2671 → `TBDAO.updateTextBookNumber` :1355.

Copy khi: thêm ô/validate vào form cấp số (sửa `validateDoSaves` DLVM:680-772 + `saveDocumentBusiness` :934-1026 + đọc thêm field ở `updateDocumentPromulgate`/`insertDocument`). Kiểm tra mới nên làm theo kiểu endpoint GET gen-2 như `is-duplicated-register-number`.

## C. Hộp việc nhiều tab, lazy-load, mỗi tab một màn con — mẫu `RequisitionVbbhVM`

`ZUL/requisition/requisition_vbbh.zul` (tabbox + `include` + `custom-attributes tabType`) + VBBHVM `loadTabContent` :208-284 (chỉ set `src` khi tab được chọn, truyền `setDynamicProperty("view", "8")`, `pageSize`, `passCbxPaging`), đồng bộ tab qua `EventQueues.lookup("vbbhTabChange")` (:103-145), ghi trace `FeatureCodes.DOCUMENT_OUT_PUBLISH_*` (:294-304). Màn con đọc `tabType` bằng `viewComp.getParent().getAttribute("tabType")` (RVM:784-801; DOVM:690-701).

Copy khi: thêm tab mới vào VBBH (thêm `<tab>` + `<tabpanel>` + biến `tabNSrc` + nhánh `loadTabContent` + `FeatureCodes` + nhánh đọc `tabType` ở VM con + nút tab trong `requisition_search.zul:56-80`).

## D. SQL hộp việc có phân quyền dữ liệu + cấu hình đơn vị — mẫu `TSDAO.getLstTextSign(PUBLISHED_SIGN)`

TSDAO:3164-4100: lấy danh sách đơn vị từ phân quyền dữ liệu `dataPermissionsService.getListOrgByPermissionData("REVIEW_PROMULGATE_DATA", userId)` (:3178-3184), đọc `SYSTEM_PARAMETER` (`TYPE_NOT_PROMULGATE`, `ORG_HAVE_DOC_MANAGER`), dựng bản đếm và bản danh sách riêng, `ROW_NUMBER() OVER (PARTITION BY t.text_id …)` khử trùng lặp do join `TEXT_PROCESS`/`TEXT_MARK`. Mẫu tách service gọn hơn: `BE1/database/dao/document/search/DocumentSearchOutService.java` (text block Java, `UNION` theo phạm vi).

Copy khi: thêm hộp việc/bộ lọc cho văn thư. Code mới nên viết dạng `DocumentSearchOutService` (hoặc gen-2 repository) thay vì chèn tiếp vào `TextSearchDAO`.

## E. Đóng dấu đơn vị (xin dấu → đóng dấu → từ chối/hủy)

- Xin dấu: RVDVM `askForSeal` :10057-10074 → popup `WEB/voffice/widget/PopupAskForSealVM.java` → `textAction.askForSeal` → TC :6146 → `TDAO.askForSeal` :6563.
- Đóng dấu: RVDVM `doApproveMark` :10165-10291 (ConfirmSign → USB token / CloudCA với `VIEW_TYPE.VBDD`) → BE `SignUtils` nhánh `MARK_TYPE` (:2641-2700) → `TDAO.approveMarkDefault` :8402.
- Từ chối: RVDVM `doRejectMark` :10128-10161 → TC :6227 → `TDAO.rejectMark` :6605.
- Hủy: RVDVM `doRollBackDDDV` :11042 → TC `rollBackDauDonVi` :6812.

Copy khi: thêm loại dấu mới (dùng `GROUP_ID`/`GROUP_TYPE`, cấu hình `IMAGE_ORG`) — nhớ bản sao ở ~15 VM văn bản (`dac-thu.md` bẫy 19).

## F. Công khai văn bản

`ZUL/document/documentPublish/document_publish.zul` + `DocumentPublishVM` (danh sách) / `popupPublishVB*.zul` + `DocumentPublishViewDetailVM` → `BIZ/DocumentPublishBusiness.java` (`DocumentPublishAction.actionSearchDocPublish`; `DocumentAction.publish` :465, `editPublicationInformation` :586, `cancelPublish` :608, `editTmpPublicationInformation` :396) → `BE1/controler/DocumentController.java` :1360/:2065/:2306/:1847 → `DocumentDAO.publishDocument` :1594 → `manuallyPublishV2` :1876 / `cancelPublish` :2461 → `DOCUMENT_PUBLISHED`, `DOCUMENT_SCOPE_REF`. Chọn văn bản thay thế: `document_publish_replace.zul` + `DocumentPublishReplaceVM` (lưu ý bẫy 12 — hiện không được lưu).

## G. Mẫu cũ ngoài phạm vi "từ cấp số trở đi" (giữ nguyên từ bản trước, CHƯA rà lại — chờ phân hệ phù hợp nhận)

- **Cặp trình ký** (gom nhiều văn bản cho lãnh đạo ký một lượt): `requisition/file/requisitionFile*.zul` + `RequisitionFileVM`, `RequisitionFileUpdateVM`, `RequisitionFileDetailVM`, `RequisitionFileChangeSignerVM` → `RequisitionFileBusiness` → gen-1 `signBriefcaseAction.*` (`SignBriefcaseAction`).
- **Báo cáo văn bản trình ký**: `requisition/requisitionReport.zul` + `RequisitionReportVM` → `RequisitionBusiness` `TextReportAction.reportRequisiton`, `ReportTextProcessingTime`, `ReportTextRejectionCount`; xuất file qua `com.viettel.util.exporter`.
- **Tìm kiếm nâng cao văn bản đi**: `document/orgFollower/orgFollowerDocOut.zul` + `DocumentSendSearchVM` (`vm/document`) — kết hợp `SearchSolrBusiness` (toàn văn) + `TextBookBusiness` + `AnswerDocumentBusiness`.
