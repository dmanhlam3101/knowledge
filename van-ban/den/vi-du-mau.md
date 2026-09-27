# Văn bản đến — ví dụ mẫu

Đường dẫn gốc: zul `web-spring/src/main/webapp/view/voffice/document/`, VM `web-spring/src/main/java/com/viettel/voffice/vm/document/`, BE gen-2 `backend2.0/backendvoffice/src/main/java/com/viettel/office/`.

## A. Popup hành động trên văn bản (hoàn thành / trả lại / ghi chú) — **mẫu gen-2, dùng cho hành động mới**

| Tầng | File |
|---|---|
| zul | `document/process/popupCompleteProcess.zul`, `popupReturnProcess.zul`, `popupCommentProcess.zul` |
| VM | `PopupCompleteDocumentVM` (một VM cho 3 popup) |
| Business | `DocumentBusiness` → `api.doc-in.complete-document`, `api.doc-in.return-document`, `api.doc-in.check-completion-reminders` |
| BE | `controller/DocInController` → `services/DocInService`(Impl) → `DocumentInStaffRepositoryJPA`, `DocumentInGroupRepositoryJPA`, `DocumentProcessRepositoryJPA` |

Copy pattern này khi thêm hành động kiểu "tạm dừng xử lý", "chuyển trả lãnh đạo", "xin gia hạn".

## B. Chuyển xử lý theo luồng

| Tầng | File |
|---|---|
| zul | `document/transferDoc/transferDoc.zul` (+ `_flow`, `_multi`, `_flow_multi`, `transfer_doc_in_flow.zul`) |
| VM | `TransferDocumentVM` (đơn), `TransferDocumentMultipleVM` (nhiều văn bản), `TransferDocumentInVM` (theo luồng gen-2) |
| Business | `DocumentBusiness` → gen-2 `api.flow-manager.doc-in.get-users-next-step*`, `get-groups-next-step*` (lấy người/nhóm bước tiếp) → gen-1 `DocumentAction.sendDocument` / `sendDocumentMultiTransfer` (thực hiện chuyển) |
| BE | `FlowManagerController` (`/api/flow-manager/doc-in/...`) → `FlowManagerServiceImpl` (có tài liệu tối ưu `PERFORMANCE_OPTIMIZATION_FlowManagerServiceImpl.md`); gen-1 `DocumentController.sendDocument` |

`TransferDocumentInVM` là bản mới nhất — lấy làm mẫu.

## C. Bút phê lãnh đạo

`DocLeaderCommentController` (`/api/doc-leader-comment/save-doc-leader-comment`, `get-doc-leader-comments`) ← `DocumentBusiness` ← VM chi tiết (`DocumentViewDetailVM`) / popup ❓ zul tên. Mẫu cho: ý kiến chỉ đạo, ghi chú của lãnh đạo lên đối tượng bất kỳ.

## D. Trả lời văn bản (sinh văn bản đi từ văn bản đến)

`document/answerDoc/answerDoc.zul` + `AnswerDocumentVM`; `replyRequestPopup.zul` + `ReplyDocumentVM`; `replyRequestDetail.zul` + `ReplyRequestDetailVM` → `AnswerDocumentBusiness` / `DocumentRequestBusiness` → gen-1 `answerDocumentAction.*`. Liên kết đến–đi: `getRepliedDocumentIds`.

## E. Tiếp nhận / nhập văn bản

`document/inputDoc/inputDoc_add.zul`, `doc_in_add.zul`, `inputDocEdit.zul` + VM tương ứng trong `vm/document` (`InputDocument*VM` ❓ tên) → `DocumentBusiness` → gen-1 `DocumentAction.AddDocument`, `AddDocumentAttachment`, `GetRegisterNumberIndex`; gen-2 kiểm tra trùng `api.doc-in.is-duplicated-register-number`, `list-exist-document-by-textbook-and-register`.

## F. Danh sách + tab trạng thái + thống kê

`document/viewDoc/*`, `seachDoc/*` + `DocumentVM`/`DocumentSendSearchVM` → gen-1 `DocumentAction.searchReceive*`, `countDocumentByStatus`; gen-2 `api.document-in.get-documents-processing-stats-by-user` (thống kê đúng/quá hạn). Mẫu cho dashboard đếm số theo trạng thái.

## G. Xem luồng xử lý (ai nhận, khi nào, trạng thái)

`document/process/viewFlow_v2.zul` + `PopupViewFlowVM`, `popupViewFlowDetail.zul` + `PopupViewFlowDetailVM` → `api.doc-in.node-detail2`, `DocumentAction.exportCirculationTree`. Mẫu cho hiển thị lịch sử/cây luân chuyển.

## H. Hạn xử lý & tự động chuyển

`vm/config/*` (menu *Cấu hình hạn xử lý văn bản*) + `DocumentProcessTermBusiness` → gen-1 `documentProcessTermConfig.*`. Mẫu cho cấu hình theo đơn vị/loại có hiệu lực.

## I. Bàn giao văn bản

`document/documentHandover/*` + `vm/documentHandover/*` → `DocHandoverBusiness` → gen-1 `DocumentHandoverAction.*`, gen-2 `api.doc.export-daily-*`.
