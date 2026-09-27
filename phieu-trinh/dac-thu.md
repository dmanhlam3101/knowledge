# Phiếu trình — đặc thù

- **Toàn bộ BE gen-2** (`SubmissionManagerController` → `SubmissionManagerService`/`SubmissionFormService`/`SubmissionForwardService` (Impl) → `SubmissionForm*RepositoryJPA` → `SUBMISSION_FORM`, `SUBMISSION_FORWARD` (SQL `20012026_add_table_submission_forward.sql`), `SUBMISSION_MAP`). Web `vm/submissionForm/*` (8 VM) + `SubmissionFormBusiness` (41 hàm) — nhãn BE, chỉ tra cứu người/đơn vị qua legacy.
- Endpoint gen-2 dùng **path variable** nhiều (`/{submissionFormId}`, `/{briefId}`, `/{fileId}`) — web ghép chuỗi `"api.submission-manager.submission-form.delete/" + id`; khi thêm endpoint kiểu này nhớ scanner nối theo tiền tố.
- Ký file phiếu trình dùng lại cơ chế ký số (`submission-file/sign`) — sửa ký số phải test cả phiếu trình.
- Có 5 màn ☠ trong `ban-do.md` (`vm.admin.RequestVM`, `RequestPopupVM`, `SourceLookupSubmission*`…) — màn kiến nghị/lookup cũ.
- Điểm móc với văn bản đi: `SubmissionFormBusiness` ↔ `RequisitionVM` (đính kèm), `textAction.searchTextForSubmission`. Sửa quy tắc "ký luôn dự thảo" phải xem cả `TextProcess` (gen-2) và `TextController` (gen-1).
- Nhắc việc / dashboard: `count-home`, `get-total-submission*` cấp số cho trang chủ.
