# Phiếu trình — ví dụ mẫu (gen-2 end-to-end, có ký số và liên kết văn bản)

Gốc: zul `web-spring/src/main/webapp/view/voffice/submissionForm/`, VM `com.viettel.voffice.vm.submissionForm`, BE `com.viettel.office.controller.SubmissionManagerController`.

| Việc | Web | BE |
|---|---|---|
| Danh sách 2 vai (người tạo / người xử lý) dùng chung một VM với tab | `submissionFormList.zul` + `submissionFormProcessList.zul` → `SubmissionFormListVM` | `submission-form/get-list`, `get-list-export` |
| Tạo/sửa có đính kèm dự thảo | `submissionForm_add.zul` (❓ VM: `SubmissionDetailVM`) | `submission-form/create-or-update`, `submit`, `check-submission-attachments-for-submitting`, `submission-form-by-text-id` |
| Ký / trả lại / xin ý kiến | `SubmissionFormSignVM`, `SubmissionFormLeaderVM` (`submissionFormLeader.zul`) | `submission-file/sign`, `reject-sign`, `tranfer-give-advice`, `update-advice` |
| Ký luôn dự thảo đính kèm | `confirmSignDocumentDraft.zul` + `ConfirmSignDocumentDraftVM` | `get-document-draft-after-sign` + luồng ký văn bản (`van-ban/di`) |
| Chuyển tiếp / lịch sử gửi | `transferSubmission.zul` + `TransferSubmissionVM` | `send`, `get-list-submission-forward`, `get-list-sender-history` (`SubmissionForwardService`) |
| Nhận để biết | `submissionFormReceiveToKnow.zul` + `SubmissionFormReceiveToKnowVM` | `get-list` với tab |
| Đưa vào hồ sơ | `SubmissionFormBusiness.addToBrief` | `submission-form/add-to-brief/{briefId}`, `delete-from-brief/{briefId}/{submissionFormId}`, `get-list-for-brief` |
| File mật | | `get-file-encrypt-map`, `get-json-file-encrypt`, `list-file-encrypt-map` |

Mẫu này tốt nhất cho yêu cầu: "thêm một loại tờ trình/phiếu nội bộ mới có ký và luồng".
