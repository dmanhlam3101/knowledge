# Công việc cá nhân — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phân hệ **toàn gen-1** — dùng các mẫu dưới đây để hiểu cách làm và móc vào luồng có sẵn; **tính năng mới viết gen-2** (mẫu chuẩn: nhắc việc, `../lich-nhac-viec/vi-du-mau.md` Mẫu 1). Tránh các điểm ghi ở `dac-thu.md` (nêu cuối từng mẫu).

## Mẫu 1 — Ký một "phiếu" sinh từ dữ liệu rồi phát hành thành văn bản nội bộ: **Lãnh đạo ký phiếu giao việc** (NV-06 B)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/task/taskApproval.zul` (danh sách nhóm theo cán bộ, combobox duyệt / từ chối từng việc, biểu tượng ký từng nhóm, nút ký hàng loạt) | Lưới nhóm theo người + thao tác theo nhóm |
| VM — sinh PDF | `TAVM.exportSigningFile` :2031-2142 → `PTB.assignPersonalTask` (`PTB:40-69`, `taskAction.exportListTaskFile`) → `TC:1606-1685` → `BE1/utils/FileUtils.java` `exportListTaskFile` (mẫu → PDF, thư mục `task_export`) | Sinh PDF ở BE từ danh sách bản ghi |
| VM — chọn cách ký | `TAVM.signTaskFile` :2397-2491 (thường / SIM CA / USB / Cloud CA), sự kiện trả về `onSignEvent` :2350-2370, `updateApprovingState` :2616-2682 | Khung chọn phương thức ký dùng chung |
| BE — sau ký | `TB.updateAfterSignTaskApproval` (`TB:2532-2554`, `Sign/signMultiFileTask` `step 2`, `type 1`) → `SignController.java:2047-2397` → `SU.insertRecordAfterSignSuccess` :962-1020 → `insertRecordForTaskAssignmentFlow` :739-805 (FILES, xóa mềm phiếu cũ cùng kỳ, chèn dòng phê duyệt) | Thêm một nhánh `type` mới trong `insertRecordAfterSignSuccess` cho loại phiếu mới |
| BE — phát hành | `TD.updateFileAttachmentFromTask` :3968-4149 (`DOCUMENT` + `TEXT` loại 429, số theo sổ, `DOCUMENT_IN_STAFF` cho người nhận + văn thư, `TASK_CHECK_DOCUMENT`) | Tạo văn bản nội bộ đã ký để lưu vết; bản ghi trạng thái phiếu (`TASK_CHECK_DOCUMENT`) giữ `DOCUMENT_ID` trỏ văn bản (DB DEV `TASK_CHECK_DOCUMENT` ngày 2026-10-01) |
| SMS | `PTD.sendSmsPersionTask` :2743-2860 (mẫu theo `SMS_TEXT_CONFIG`, ghi `SMS_MASTER` với `CONFIG_SMS_MODULE_ID` 502) | Gửi tin sau ký — cơ chế: `lich-nhac-viec` NV-13 |

**Không copy**: trả 1 dù bỏ qua bản ghi lỗi (`dac-thu.md` L16); một đối tượng SMS dùng lại trong vòng lặp, tách kỳ kiểu `yyyyMM` (L12); ánh xạ SIM CA thành "ký thường" (L13); xóa phiếu cũ trước khi ký xong (L20).

## Mẫu 2 — Cho người dùng **trình ký** một phiếu qua luồng văn bản rồi xử lý khi văn bản ký xong: **Cán bộ tự trình phiếu giao việc** (NV-06 A)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| VM | `TAVM.doSubmit` :1266-1296, kiểm `validatePreviewOrSubmit` :1558-1588 (có việc, tổng 100%, có người ký, mỗi người ký có đơn vị, tối đa một ảnh chữ ký); chọn người ký trên màn | Bộ kiểm trước khi trình |
| BE — tạo văn bản trình | `PTB.createPersonalTaskSubmitFlow` (`PTB:251-277`) → `TC:1687-1788` → `TD:10854-11031`: `documentSignDAO.addText` (loại văn bản riêng, ký hiệu tự sinh), `userDAO.createSignerList`, `sendAndSign`, lưu `TEXT_ID` vào bản ghi nghiệp vụ | Dùng lại luồng trình ký văn bản thay vì tự viết luồng ký |
| BE — móc sau ký | `BE1/thread/ThreadExcuteAfterSigned.java:369` → `updateTaskCheckDocument` :1992-2113 (theo `TEXT_ID` tìm bản ghi, ghi trạng thái "đã duyệt") | Điểm móc khi văn bản trình được ký xong |
| Trạng thái "đang trình" | `TD:5093-5106` (`TextDAO.getTextIdSubmitting`, văn bản ở trạng thái 0 / 1 / 5) → khóa thao tác trên màn (`taskApproval.zul:1179-1189`) | Khóa sửa khi đang trình |

Mẫu tương tự cho KI: `ERMVM.doRequisitionDirect` :2967-3100 → `TaskService.updateRequisitionDirect` → `PTD:2888-3050` (PDF bảng tổng hợp + `addText` + ghi `TEXT_ID`). **Không copy**: xóa bản ghi phê duyệt theo id mọi kỳ (L16); không ghi trạng thái nghiệp vụ sau khi ký (L22).

## Mẫu 3 — Hộp danh sách nhiều tab theo vai trò + cờ quyền tính ở BE cho từng dòng: **Quản lý công việc** (NV-01)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/task/task_search.zul:70-85` (tab), `958-1104` (biểu tượng thao tác theo `has*Permission`) | Tab bằng nút + biểu tượng thao tác trên dòng |
| VM | `TVM.doChangeTab` :1704-1730, `findDataList` :4572-4664 / `countDataList` :4716 | — |
| BE | `TD.getListTask` :296-1093 — điều kiện "của tôi" theo tab (`TD:399-499`), mã lọc trạng thái giả "chậm tiến độ" (`TD:502-528`), gắn cờ quyền `updatePermissions` cho từng dòng (`TD:782`) | Tính quyền một lần ở BE, web chỉ đọc cờ |

**Không copy**: biến `static` giữ trạng thái màn (L2); hàm đếm gửi tham số khác hàm danh sách (L10); join cùng bí danh hai lần (L3).

## Mẫu 4 — Popup nhập lý do duyệt / từ chối dùng lại được

`PopupReasonApproveTaskVM.java:58-70` (lý do tùy chọn) / `PopupReasonRejectTaskVM.java:58-74` (lý do bắt buộc, ≤ 2.000) với zul `ZUL/meeting/popup/approveTaskReason.zul`, `rejectTaskReason.zul`, mở từ `TVM:5078-5110` / `TVDVM:2555`, `2588`, trả kết quả cho VM gọi rồi gọi `taskAction.ApproveOrRejectTask` (`TB:165-195`). Copy khung popup + truyền kết quả; **thêm `trim()`** khi kiểm lý do rỗng (bản gốc chỉ `isEmpty()`).
