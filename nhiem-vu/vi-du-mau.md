# Nhiệm vụ — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phân hệ chủ yếu là gen-1 cũ; khi làm tính năng **mới** nên theo mẫu gen-2 (mẫu 3, 4) và mẫu nhắc việc ở `../lich-nhac-viec/vi-du-mau.md`. Mẫu gen-1 dưới đây để **hiểu / sửa** code hiện có, kèm các điểm không nên copy.

## Mẫu 1 — Quy trình báo cáo – duyệt hai cấp trên một bảng lịch sử: **Cập nhật tiến độ → duyệt cấp đơn vị thực hiện → duyệt cấp đơn vị giao** (gen-1)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul popup | `ZUL/mission/mission/mission_update_process.zul:44-397` (combobox trạng thái theo `statusListSave`, ô hiện / ẩn theo trạng thái chọn) | Form báo cáo đổi trường theo loại báo cáo |
| VM | MVM `validateUpdatePercent` :7052-7134, `doUpdatePercent` :6981-7050; nút duyệt `doApproveProgess` :7519 / `doApproveMission` :7381 | Kiểm theo loại báo cáo trước khi gửi |
| Business | MB `updateMissionProcess` :333-386, `approveOrRejectProcess` :905-920 | — |
| Controller | MC `updateProcess` :1564-1745 (chặn trạng thái, kiểm quyền qua `checkUserPermissionForMission`, chọn nhánh theo vai), `approveOrRejectProcess` :1765-1951 (chọn dòng chờ theo cấp, rẽ nhánh gia hạn) | Mỗi lần báo cáo một dòng lịch sử + **hai cột duyệt độc lập** (cấp dưới / cấp trên) |
| DAO | `MDAO.updateProcess` :2328-2837, `approveOrRejectProcess` :2974-3126, `approveExtendProcess` :3145-3240; tìm "dòng chờ cấp trên" trong `checkUserPermissionForMission` :1429-1553 | Bảng đối tượng giữ trạng thái **đã được duyệt**, bảng lịch sử giữ mọi lần báo cáo |
| Quyền | `EM.updatePermission` :791-1152 (cờ `approve` / `guide` theo vai và trạng thái dòng chờ) | Tính cờ quyền ở BE một chỗ, trả cho web hiện nút |

**Không copy**: cho một vai (lãnh đạo) đổi trạng thái đối tượng ngay khi báo cáo còn chờ cấp trên (`dac-thu.md` bẫy 8); hai đường duyệt song song (bẫy 3); ghi hàng đợi SMS với nội dung null (L6); SQL nối chuỗi id.

## Mẫu 2 — "Bản sao lịch sử khi đổi chủ thể" + chuyển đối tượng con: **Chuyển đơn vị thực hiện** (gen-1)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul / VM | `ZUL/mission/mission/mission_transfer.zul`; MVM `doTransfer` :7853-7984 (chọn một đơn vị **hoặc** một cá nhân, lý do bắt buộc, xác nhận) | Popup đổi chủ thể có lý do |
| Controller | MTC `forwardMission` :1203-1484 (kiểm trùng, kiểm quyền, chuyển văn bản nguồn, SMS cho bên cũ / bên mới) | Thông báo **cả hai phía** với mẫu tin khác nhau (403 / 401) |
| DAO | `MTDAO.forwardMission` :1717-1992: `INSERT … SELECT` bản sao (`MISSION_ROOT_ID`, cờ đã chuyển, lý do), chép bảng con, cập nhật bản gốc, từ chối đề xuất đang chờ | Giữ id cho chủ thể mới, bản sao làm lịch sử; liệt kê cột tường minh khi `INSERT … SELECT` |
| Lịch sử | `MDAO.getListTransferredMission` :1369-1413 | Truy vấn bản sao theo `MISSION_ROOT_ID` |

**Không copy**: dùng chung `StringBuilder` / danh sách tham số qua vòng lặp, không giao dịch, không kiểm kết quả từng bước chép (L10).

## Mẫu 3 — Dashboard biểu đồ nhiều kỳ tháng / quý (gen-2): **Thống kê tình hình nhiệm vụ**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul + JS | `ZUL/mission/mission/mission_dashboard.zul`; `web-spring/src/main/webapp/theme/admin-ex/js/missionDashboard.js` (Chart.js) | Vẽ biểu đồ ở client từ JSON |
| VM | `WEB/voffice/vm/mission/MissionDashboardVMNew.java` (tab giao đi / thực hiện, chọn tháng / quý :584-608) | — |
| Business | `BIZ/MissionChartBusiness.java` (`api.mission_dashboard.get-assign-mission-charts` / `get-perform-mission-charts`) | — |
| BE | `BE2/controller/MissionDashboardController.java` → `BE2/services/impl/MissionDashboardServiceImpl.java` (kỳ chạy song song bằng thread) → `BE1/database/dao/report/MissionDashboardChartDAO.java` `report` :81-505 | Một câu SQL tham số hóa theo loại biểu đồ |

**Không copy**: biến `static` lưu khoảng ngày trong VM (L14); nhãn dataset JS không khớp tên trường BE (L14); hai controller trùng endpoint (`/api/mission` và `/api/mission_dashboard`).

## Mẫu 4 — Mẫu báo cáo cấu hình được + đơn vị gửi / cấp trên tổng hợp, khóa (gen-2): **Báo cáo đơn vị định kỳ**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| BE mẫu | `BE2/controller/MissionTemplateController.java`; `BE2/services/impl/MissionTemplateServiceImpl.java` (một mẫu / (đơn vị, loại, độ mật) :68-70; xóa mềm cả cây :102-166) | Mẫu dạng cây mục + phạm vi đơn vị từng mục (`MISSION_TEMPLATE_SCOPE`) |
| BE kết quả | `BE2/controller/MissionReportResultController.java`; `BE2/services/impl/MissionReportResultServiceImpl.java:97-191` (validate kỳ, kiểm vai trò, tạo nháp, chặn khi cấp trên đã khóa, gửi → tự khóa) | Hai cấp `REPORT_LEVEL` trên cùng bảng, khóa theo kỳ |
| Tổng hợp từ nhiệm vụ | `BE2/services/impl/MissionReportResultDetailServiceImpl.java:69-129` (ghép kết quả nhiệm vụ gắn `MISSION_TEMPLATE_DETAIL_ID`) | Điền sẵn nội dung báo cáo từ dữ liệu nghiệp vụ |
| Web | `ZUL/templateReport/*` + `WEB/voffice/vm/template/WriteReportVM.java` (phân hệ `tai-lieu-mau`) | — |

**Không copy**: thiếu kiểm quyền ở khóa / gán chuyên viên / xem theo id (L3); hàm trả `null` nhưng web kiểm `"1"` (gán chuyên viên).
