# Phiếu trình — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phiếu trình là phân hệ **gen-2 thuần** tốt nhất để học cách làm "một đối tượng có luồng xử lý nhiều cấp + file sinh từ mẫu + liên kết đối tượng khác".

## Mẫu 1 — Thao tác đổi trạng thái có khóa đồng thời và kiểm người gọi ở BE: **Hủy luồng phiếu trình** (mẫu cho "tạm dừng", "rút lại")

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | nút trên lưới `ZUL/submissionForm/submmissionForm_search.zul:240-241` (`visible = vm.checkViewCancelSubmissionForm(data)`) | Nút hiện theo hàm `check*` của VM |
| VM | SFLVM `doCancelSubmissionForm` :3953-3997: đọc lại phiếu để chặn trạng thái đã đổi (:3956-3962), hộp xác nhận HTML (:3963-3970), bắt mã lỗi `861` "đang xử lý" (:3978-3981), tải lại danh sách | Đọc lại dữ liệu trước khi thao tác; bắt mã lỗi nghiệp vụ trả về dạng chuỗi |
| Business | `SFB.cancelSubmissionForm` (:311-320) — path variable ghép chuỗi `"api.submission-manager.submission-form.cancel/" + id` | Key `api.*` + path variable |
| Controller | `SMC:210-214` | Endpoint mỏng, `ResponseUtils.getResponseEntity` |
| Service | `SMSI.cancelForm` :1356-1392 (`@Transactional`): khóa `findBySubmissionFormIdForUpdate` (`SubmissionFormRepositoryJPA.java:50-55`, `PESSIMISTIC_WRITE`, timeout 0) → lỗi `ErrorCodeApp.SUBMISSION_ERROR_PROCESS_HANDLING`; kiểm người tạo → `ErrorApp.FORBIDDEN`; kiểm trạng thái → lỗi riêng; đổi trạng thái; kéo theo đối tượng liên kết (`rejectTextAfterRejectOrCancelSubmissionForm` :2163-2188); SMS + thông báo (`sendSMSSubmission`, `addNotification` :2702-2753) | Khung "khóa → kiểm người → kiểm trạng thái → đổi → hệ quả → báo tin" |

## Mẫu 2 — Luồng xử lý nhiều cấp, tuần tự hoặc song song theo nhóm: **Phê duyệt / ký duyệt phiếu trình**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Khai báo luồng | SFLVM `updateProcessList` :2907-3021 (mỗi người một dòng, `SIGN_LEVEL` theo thứ tự), `changeSignMode` :4674-4695 + `adjustSignLevel` :4764-4800 (nhóm song song, người cuối tách nhóm riêng) | Lưu luồng thành bảng dòng xử lý với `SIGN_LEVEL`; song song = nhiều dòng cùng cấp |
| Popup xử lý | `ZUL/widgets/approveSubmissionFormPopup.zul:59-72` (nút Ký duyệt / Phê duyệt theo `vm.signProcess`); ASFPVM :177-318 | Một popup, hai hành động theo cấu hình của dòng |
| Tìm người đang tới lượt | `SPRJ.findCurrentSigner` :43-46 (`sf.status = 1`, `sp.status = 0`, `sp.sign_level = sf.sign_level`, `sp.vhr_employee_id = :user`) | Kiểm "đúng người, đúng lượt" ở BE |
| Chuyển cấp | `SMSI.updateStatusSign` :2016-2161: đếm người cùng cấp còn chờ (`SPRJ:67-69`), hết thì tìm cấp kế, không còn cấp thì hoàn thành, ghi `SEND_DATE` cấp kế, báo tin | Thuật toán chuyển cấp có nhóm song song |
| File kết quả | `SMSI.generatePathFile` :2232-2358 → `BE2/utils/FileUtils.java::generateSubmissionFile` :63-187 (mẫu `<n>_phieu_trinh.docx` qua `ConvertFileAPI`); ký SIM / USB :1615-1774 | Sinh PDF từ mẫu Word + chèn ảnh ký theo vị trí chữ ẩn |

**Không copy**: điều kiện `!= null ||` (dac-thu L1), `findCurrentSigner` không lọc loại dòng (L3), vòng gửi tin chết khi từ chối (L5).

## Mẫu 3 — Hộp việc nhiều tab + widget đếm song song: **Ký duyệt phiếu trình (menu "Trình quyết định")**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Menu / widget | `SYS_MENU 439545 SUBMISSIONFPROCESSLIST` → `submissionFormProcessList.zul?view=1`; `HOME_WIDGET` 35/38/36/39/73 (`HomeWidgetRestController.java:1622-1672`, URL tab :1837-1843) | Ô widget mở menu kèm tham số tab |
| zul | `ZUL/submissionForm/submissionFormProcess_search.zul:6-30` (nút tab, nhãn `vm.tab*Label`) | Tab bằng nút + `changeTab` |
| VM | SFLVM `changeTab` :8924-8994, quy đổi tab → `searchType` / `processingStatus` :1316-1325, nhãn tab `getMenuLabel` :12164-12205 (tab hiện tại lấy tổng thật, tab khác lấy `count-home`) | Một VM nhiều tab, số trên nhãn |
| BE danh sách | `SMRI.submissionGetList` :259-593 (SQL động theo `searchType`), hậu xử lý nhãn / màu trạng thái `postProcessSearch` :595-737 | Trả sẵn nhãn + màu cho lưới |
| BE đếm | `SMSI.submissionCountHome` :162-268 (`CompletableFuture` song song, timeout) + `BE2/dto/SubmissionCountThread.java:53-80` (gọi lại truy vấn danh sách với `size = 1`) | Đếm bằng chính truy vấn danh sách → số luôn khớp danh sách |

## Mẫu 4 — Liên kết đa loại đối tượng qua một bảng map: **Tài liệu kèm theo phiếu trình** (dự thảo / văn bản đến / hồ sơ)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Bảng | `SUBMISSION_MAP (SUBMISSION_FORM_ID, OBJECT_ID, OBJECT_TYPE 1/2/3)` — `BE2/entities/SubmissionMapEntity.java`; hằng `C2:557-563` | Một bảng map + cột loại thay vì nhiều bảng |
| Web chọn | SFLVM `doSelectDocumentDraft` :8689-8718 (popup riêng lọc dự thảo hợp lệ), `doAddDocAttach` :8731-8759, `doAddBrief` :8768-8798; gom lại khi lưu :6080-6083 | Mỗi loại một popup chọn, gộp một danh sách khi gửi |
| BE lưu / đọc | `SMSI.createOrUpdate` :1102-1154 (xóa – chèn lại), `submissionGetDetail` :652-722 (nạp chi tiết từng loại theo `OBJECT_TYPE`) | Đọc gom ID theo loại rồi truy vấn từng bảng một lần |
| Hệ quả lên đối tượng | `SMSI.submitTextAfterCompleteSubmissionForm` :2190-2220, `rejectTextAfterRejectOrCancelSubmissionForm` :2163-2188 | Đổi trạng thái đối tượng liên kết khi đối tượng chính đổi |

Khi copy: cân nhắc **không** xóa – chèn lại toàn bộ (dac-thu bẫy 3, L7) và luôn lọc `OBJECT_TYPE` khi kiểm trùng (L10).
