# Văn bản đến — đặc thù, bẫy

## Tình trạng kỹ thuật: lai gen-1 / gen-2 rõ rệt nhất hệ thống

| Phần | Tầng |
|---|---|
| CRUD, tìm kiếm, chuyển, đếm, xuất | gen-1 `DocumentAction` (104 endpoint) → `controler/DocumentController` → `DocumentDAO`, `DocumentInStaff*`, `AnswerDocumentDAO`… |
| Trả lời văn bản | gen-1 `answerDocumentAction` |
| Bàn giao | gen-1 `DocumentHandoverAction` |
| Hạn xử lý, tự động chuyển | gen-1 `documentProcessTermConfig` |
| **Hoàn thành, trả lại, trùng số, file mã hóa, trạng thái staff/group, node luồng** | **gen-2** `DocInController` (`/api/doc-in`, 28 endpoint) |
| Bút phê | gen-2 `DocLeaderCommentController` |
| Thống kê tiến độ theo user, nhóm CV | gen-2 `DocumentInController` (`/api/document-in`) |
| Người/nhóm bước tiếp theo theo luồng | gen-2 `FlowManagerController` (`/api/flow-manager/doc-in/*`, 17 hàm) |
| Báo cáo ngày, mẫu văn bản, đồng bộ | gen-2 `DocController` (`/api/doc`) |
| Tìm kiếm văn bản nhận (tối ưu) | gen-1 `DocumentSearchReceive*` — có tài liệu `PERFORMANCE_OPTIMIZATION_DOCUMENTATION_DocumentSearchReceive.md` |
| Web | `vm/document/*` (73 VM) — `DocumentBusiness` **178 hàm**, gọi cả gen-1 lẫn gen-2; `DocumentViewDetailVM` là màn chi tiết dùng chung đến/đi, nhúng nhắc việc, công việc, họp |

Quy tắc chọn tầng khi sửa: **hành động mới → gen-2 `DocInController`** (đây là nơi tính năng gần đây được thêm: `complete-document`, `return-document`, `check-completion-reminders`, `update-status-dis-proposal`). Tìm kiếm/danh sách → vẫn gen-1 (đã tối ưu, đừng viết lại).

## Bẫy

1. **`DocumentViewDetailVM` là hub**: sửa chi tiết văn bản ảnh hưởng cả văn bản đi đã ban hành, hồ sơ, nhắc việc, công việc, họp. Grep `DocumentViewDetailVM` trước khi sửa.
2. **Hai bảng giao việc**: `DOCUMENT_IN_STAFF` (cá nhân) và `DOCUMENT_IN_GROUP` (đơn vị/nhóm) — trạng thái phải cập nhật **cả hai** (`update-status-document-in-staff` + `update-status-document-in-group`); lỗi thường gặp là chỉ cập nhật một.
3. **Luồng văn bản đến** không hard-code: người bước tiếp theo lấy từ `flow-manager/doc-in/get-users-next-step*`. Thêm loại người nhận = sửa cấu hình luồng, không sửa VM.
4. Nhiều phiên bản tìm kiếm: `search`, `searchDocumentIn`, `searchReceive`, `searchReceiveGroupByTextBook`, `searchReceiveWithProcessingStatsByUser`, `getDocumentListVof2` — mỗi màn dùng một hàm; đổi cột hiển thị phải sửa đúng hàm màn đó dùng.
5. `getTextIdByDocId` / `getTextIdByDocumentId`: liên kết ngược `DOCUMENT → TEXT` (văn bản đi gốc). Văn bản đến nhập tay không có `TEXT_ID`.
6. Văn bản tài chính (`searchFinancial`, `exportFinanceText`, `sendFinanceTextToStaff`, `FINANCIAL_DOCUMENT_TYPE_ID_KEY`) là nhánh riêng có phân quyền `financialRecordsRoles` (menu HỒ SƠ TÀI CHÍNH).
7. Màn hình ☠ trong phân hệ: xem nhãn trong `ban-do.md` (`DocumentReceviceVM`, `AssignMoveListVM`, `DocumentBookVM`… không tồn tại) — chức năng thật nằm ở VM khác cùng thư mục.
8. `12032026_yc_16_tacdong.sql` — một yêu cầu (YC16) có "tác động" DB gần đây ❓ nội dung gì; đọc file trước khi đụng bảng liên quan.
9. **`STAFFID_VOF2`/`GROUPID_VOF2` (`DOCUMENT_IN_STAFF`) và `STAFF_ID_VOF2`/`GROUP_ID_VOF2` (`DOCUMENT_IN_GROUP`) là NGƯỜI GỬI**, không phải người nhận — cùng lấy từ `userVof2` của người bấm chuyển (`DocumentDAO.sendDocumentToGroup`), nên mọi dòng sinh ra trong một lượt chuyển (cả cá nhân lẫn đơn vị) đều mang cùng cặp giá trị này. Người nhận nằm ở `RECEIVERID_VOF2`/`RECEIVER_GROUPID_VOF2` (staff) và `RECEIVER_GROUP_ID_VOF2` (group). **Đừng dùng cặp cột này để gom người nhận** — xem mục 12.
10. **Đánh dấu đã đọc tách 2 đường**: cá nhân đọc → `DOCUMENT_IN_STAFF.CONFIRM_TIME`; **văn thư** đọc bản gửi đơn vị → `DOCUMENT_IN_GROUP.CONFIRM_TIME` (chỉ chạy khi `listSecretaryVhrOrg` không rỗng — `DocumentController.updateReadingStatus`). Web **không có `documentInStaffId` cho dòng mức đơn vị** (query group select thẳng `null documentInStaffId`; query chi tiết lọc theo `receiverid_vof2` của người đăng nhập, không khớp thì rơi vào `nvl(..., text_id)` trả về **TEXT_ID của bảng khác**) ⇒ mọi logic phía web neo theo `documentInStaffId` sẽ **không chạy khi văn thư là người thao tác**.
11. `DOCUMENT_IN_GROUP.STAFF_ID_VOF2` là **chuỗi** còn `DOCUMENT_IN_STAFF.STAFFID_VOF2` là **số** — so sánh trực tiếp gây implicit `TO_NUMBER` (mất index, `ORA-01722` nếu có dữ liệu không phải số). Dùng `TO_CHAR(...)` ở phía số.
12. **Gom "tất cả người nhận của một lần chuyển" thì dùng `DOCUMENT_PROCESS.PARENT_ID`**, không dùng `STAFFID_VOF2`/`GROUPID_VOF2` (mục 9, 11). Con trực tiếp của dòng cha: cá nhân có `IN_STAFF_ID` (→ `DOCUMENT_IN_STAFF`), đơn vị có `IN_GROUP_ID` (→ `DOCUMENT_IN_GROUP`); cá nhân **bên trong** đơn vị nhận là **cháu** (`PARENT_ID` trỏ dòng đơn vị — `DocumentDAO.java:9817-9820`), nên "đơn vị đã đọc" = `CONFIRM_TIME` của chính dòng `DOCUMENT_IN_GROUP`. Lưu ý: `PARENT_ID` **không tách được các bản ghi nhận trong cùng một lần chuyển** (nhiều người nhận của 1 lần bấm Chuyển đều là con của cùng 1 node cha) — **đây không phải vấn đề khi cần phân biệt các luồng nhận khác nhau của cùng một người**: đã xác nhận bằng code (`DocumentDAO.getDocumentProcessByDocumentInGroupIdOrDocumentInStaffId`, dòng 9752, gọi tại dòng 8208/9619) rằng khi tạo `DOCUMENT_PROCESS` cho lượt chuyển mới, node cha được resolve theo **đúng `documentInStaffId`/`documentInGroupId` nguồn cụ thể** (truyền từ `DocumentBusiness.transferDocument`, `web-spring/.../DocumentBusiness.java:1632`) — một người có 2 luồng nhận (2 đơn vị) sẽ có 2 node cha khác nhau, cây tách biệt hoàn toàn theo luồng. Nhiều luồng không tạo `DOCUMENT_PROCESS` hoặc để `PARENT_ID = NULL` (phát hành cũ, `sendDocumentToStaff`, `AnswerDocumentDAO`) ⇒ logic dựa trên cây process sẽ không chạy ở đó.
13. **Kiểm tra "luồng này đã chuyển giao chủ trì cho ai chưa"** (vd. để ẩn nút Hoàn thành khi đã chuyển tiếp `SEND_TYPE=TO`): dùng `DocInServiceImpl.hasActiveDelegatedLead(documentId, inStaffId, inGroupId)` — đi từ luồng cụ thể qua `findDocumentProcessIdByInStaffId/InGroupId` rồi quét toàn bộ cây con (`findChildDocumentProcessesByDocumentIdAndProcessId`, nhiều cấp) tìm bản ghi `SEND_TYPE=TO` còn ở trạng thái hoạt động (`PENDING/PROCESSED/REJECTED`). Tính on-the-fly, không lưu cờ, nên tự đúng ngay cả với dữ liệu cũ và tự cập nhật khi luồng chủ trì đó bị thu hồi/trả lại. Dùng trong `filterDocumentsForComplete` (ẩn ở danh sách) và đầu `completeDocument` (chặn ở API, không chỉ ẩn UI).

## Yêu cầu hay gặp → hướng

| Yêu cầu | Hướng |
|---|---|
| Thêm điều kiện hoàn thành / chặn hoàn thành | gen-2 `DocInServiceImpl.completeDocument` (mẫu `check-completion-reminders`, `hasActiveDelegatedLead` — xem mục 13) |
| Thêm loại trạng thái theo dõi (vd. "đang chờ ý kiến") | Cột STATUS ở `DOCUMENT_IN_STAFF/GROUP` + `document.status` i18n + tab trong `DocumentVM`/`DocumentSendSearchVM` + điều kiện `DocumentDAO.searchReceive` (gen-1) |
| Thêm thông tin vào chi tiết | `DocumentViewDetailVM` + `getDocumentDetail` (gen-1) hoặc endpoint gen-2 mới |
| Cảnh báo hạn / nhắc | `lich-nhac-viec` (reminder) + `documentProcessTermConfig` |
| Xuất báo cáo mới | gen-2 `DocController.export-*` là mẫu mới nhất |
