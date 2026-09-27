# Văn bản đi — ví dụ mẫu để copy pattern

> Chọn mẫu theo loại việc. Mẫu **gen-2** ưu tiên cho code mới; mẫu **gen-1** chỉ để hiểu/sửa luồng hiện có.

## A. Thêm một hành động mới lên văn bản đang trình ký (kiểu "chuyển cấp số", "thu hồi", "gia hạn") — mẫu gen-2 đã có trong chính phân hệ này

**Chuyển sang cấp số** (`forward-to-assign-number`):

| Tầng | File |
|---|---|
| BE controller | `backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextProcessController.java` → `POST /api/text-process/forward-to-assign-number` (`@RequestBody ForwardToAssignNumberDTO`) |
| BE service | `TextProcessService` / `TextProcessServiceImpl` (`services/impl`) |
| BE repo/entity | `repositories/jpa/*Text*RepositoryJPA`, `entities/TextEntity`, `TextProcessEntity` ❓ tên chính xác — grep `@Table(name = "TEXT_PROCESS")` |
| Web business | `RequisitionBusiness` — hàm gọi `"api.text-process.forward-to-assign-number"` |
| Web VM | `RequisitionVM` — nhánh `viewType == VBKD/VBXD` |

Các hàm cùng nhóm để tham khảo: `rollback-signer/{text-id}` (path variable), `get-next-signers`, `get-next-signers-check-cert`, `get-all-cert-permission`, `validate-update-give-advise`.

**Xin ý kiến / giao người tư vấn trên dự thảo** (`TextDraftController`): `/api/text-draft/get-advise`, `assign-adviser`, `give-advise`, `search-text-draft`, `get-text-draft-history` — mẫu cho thao tác có lịch sử.

## B. Popup nhập lý do rồi đổi trạng thái (mẫu "từ chối ban hành")

| Tầng | File |
|---|---|
| zul | `web-spring/src/main/webapp/view/voffice/requisition/rejectPublish.zul` |
| VM | `com.viettel.voffice.vm.requisition.RejectPublishVM` → `requisitionBusiness.rejectPublishDocument(documentReject)` |
| Business | `RequisitionBusiness.rejectPublishDocument` → gen-1 `textAction.rejectSignDocument` / `DocumentAction.cancelPublish` ❓ (xem ban-do mục 2) |

Dùng làm mẫu cho: thu hồi văn bản, hủy luồng có lý do, trả lại kèm ghi chú.

## C. Cấp số theo sổ

`requisition/requisition_issue_number_view_detail.zul` + `RequisitionViewIssueNumberVM` (`vm/requisition`) → `TextBookBusiness.getNextRegisterNumberByTextBookId` (`textBookAction`, gen-1) + `AnswerDocumentBusiness`. Danh sách sổ theo người/đơn vị/loại: `getAllTextBooksOfUserByOrgForDocOut*`.

## D. Ký số từ web

`requisition/signUsbToken.zul` + `RequisitionSignVM` ❓ (VM thật trong `vm/requisition`) → `RequisitionBusiness` gọi `Sign.SignSoftHashMutiFile` / `Sign.SignCloudCA` / `Sign.SignTextByCASIM` → cập nhật `textAction.updateDatabaseSign`. Chi tiết ở `ky-so/vi-du-mau.md`.

## E. Ban hành & công khai

- Ban hành: `RequisitionVM` (viewType VBBH) → `RequisitionBusiness` `textAction.documentPromulgate` → gen-1 `TextController` → tạo `DOCUMENT` (`DocumentDAO`), gửi người nhận (`TEXT_RECEIVER`), liên thông (`CONNECT_DOCUMENT`).
- Công khai/thay thế: `document/documentPublish/*.zul` + `DocumentPublishVM`, `DocumentPublishReplaceVM`, `DocumentPublishViewDetailVM` → `DocumentPublishBusiness` (`DocumentAction.publish`, `cancelPublish`, `editPublicationInformation`, `DocumentPublishAction.actionSearchDocPublish`, `getListDocAlter`).

## F. Cặp trình ký (gom nhiều văn bản cho lãnh đạo ký một lượt)

`requisition/file/requisitionFile*.zul` + `RequisitionFileVM`, `RequisitionFileUpdateVM`, `RequisitionFileDetailVM`, `RequisitionFileChangeSignerVM` → `RequisitionFileBusiness` → gen-1 `signBriefcaseAction.*` (`SignBriefcaseAction`).

## G. Báo cáo

`requisition/requisitionReport.zul` + `RequisitionReportVM` → `RequisitionBusiness` `TextReportAction.reportRequisiton`, `ReportTextProcessingTime`, `ReportTextRejectionCount`; xuất file qua `com.viettel.util.exporter`.

## H. Tìm kiếm nâng cao văn bản đi

`document/orgFollower/orgFollowerDocOut.zul` + `DocumentSendSearchVM` (`vm/document`) — kết hợp `SearchSolrBusiness` (toàn văn) + `TextBookBusiness` + `AnswerDocumentBusiness`.
