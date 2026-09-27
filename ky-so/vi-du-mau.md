# Ký số — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Thêm luồng ký cho một loại đối tượng mới (vd. "ký biên bản kiểm kê") | Copy cách phiếu trình làm: gen-2 `SubmissionManagerController.submission-file/sign` + `reject-sign` (gọi chung dịch vụ ký gen-1) ← `SubmissionFormBusiness` ← `SubmissionFormSignVM` |
| Popup ký USB token | `requisition/signUsbToken.zul` + VM ký trong `vm/requisition` (`RequisitionSignVM` ❓) → `RequisitionBusiness` `Sign.SignSoftHashMutiFile` → `textAction.updateDatabaseSign` |
| Chọn ảnh chữ ký & vị trí trên PDF | `requisition/signatureImageSelector.zul` + `imageSignAction.getListLocationByTextId`, `updateListLocation`; `textAction.getDefaultMarkLocationByTextId` |
| Ký CloudCA có OTP | `Sign.SignCloudCA` + `CloudCAAction.verifyOTPInSigning`; xử lý lỗi `CLOUD_CA_SIGN_ERROR` trong `Business.serveProcessing` (web) |
| Ký hàng loạt file (phiếu giao việc) | `Sign.signMultiFileTask` ← `TaskBusiness` ← `EmpRatingSignAllFilesManagerVM` |
| Đóng dấu nhiều văn bản | `textAction.markDocumentByOrg`, `getListOrgMultiMarkRequisition`, `MAX_CONCURRENT_SELECTED_DOCUMENTS_MARK` ← `RequisitionVM` (viewType VBDD) |
| Kiểm tra chứng thư trước khi chọn người ký (gen-2) | `TextProcessController.get-next-signers-check-cert`, `get-cert-user-or-org`, `get-all-cert-permission` |
| Quản lý chứng thư người dùng | `CertManagementAction.*` + `vm/config` ❓ zul (menu Ký điện tử) |
