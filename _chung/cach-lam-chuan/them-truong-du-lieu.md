# Cách làm chuẩn: thêm trường dữ liệu / trạng thái mới

Yêu cầu kiểu "thêm cột X cho văn bản", "thêm trạng thái Y", "thêm lý do thu hồi".

## 1. Thêm cột

| # | Việc | Ở đâu | Ghi chú |
|---|---|---|---|
| 1 | `ALTER TABLE <T> ADD (<COL> <type>)` + `COMMENT ON COLUMN` | `backend2.0/backendvoffice/sql/<DDMMYYYY>_add_column_<mo_ta>.sql` (mẫu: `06032026_add_deadline_date_table_text.sql`, `04122025_add_column_send_sms.sql`) | Oracle; `NVARCHAR2` cho tiếng Việt, `DATE`, `NUMBER(19,0)`, `NUMBER(1,0)` cho cờ |
| 2 | Entity BE gen-2 | `com.viettel.office.entities.<T>Entity` — thêm `@Column(name="COL") Type col;` | Nếu bảng chưa có entity gen-2 (chỉ gen-1 SQL thuần) thì bỏ qua |
| 3 | DAO/logic BE gen-1 | `database/dao/**/<T>DAO` — thêm cột vào câu SELECT/INSERT/UPDATE tương ứng; `database/entity/<T>*` POJO thêm field | Grep tên bảng trong `database/dao` để tìm mọi SQL đụng bảng |
| 4 | DTO BE | `dto/request|response/...` | |
| 5 | Entity web legacy | `com.viettel.voffice.entity.<T>` / `com.viettel.vps.entity.<T>` nếu tồn tại (137 entity web) | **Bắt buộc** nếu web còn đọc bảng qua JPA — kiểm tra `ban-do.md` mục 4/5 |
| 6 | Model web | `com.voffice.service.entity.<T>Entity` / `dto` | Trùng tên JSON |
| 7 | zul + VM | Thêm ô nhập/hiển thị, validate trong `validateDoSave()` | Nhãn i18n |
| 8 | Elasticsearch/Solr | Nếu cột cần tìm kiếm toàn văn: `ElasticDocument*`, `els_query/`, `SolrSearch*` | ❓ quy trình reindex |
| 9 | Liên thông | Nếu cột phải đi ra ngoài (trục): `InObjectSendXml`, `ConnectDocument` mapping | |

## 2. Thêm trạng thái

Trước hết xác định trạng thái đó thuộc kiểu nào:

| Kiểu | Nhận biết | Cách thêm |
|---|---|---|
| Enum trong code | `TextStateConstants`, `TextProcessStateConstants`, `Constants.TEXT_STATE_*`, `MISSION_STATUS`, `task.state` | Thêm hằng số ở BE gen-1 `constants/` **và** web `AppConstants` (web có bản sao); thêm nhãn `voffice.appConstants.<map>.<key>` trong properties; sửa các `switch`/`if` đọc trạng thái (grep hằng số cũ liền kề) |
| Danh mục động | web đọc `code.doc.status`, `code.meeting.status`… (`AppConstants` dòng ~118–160), bảng `CODE_MASTER` | `INSERT` dữ liệu; code không đổi trừ khi cần xử lý đặc biệt |
| Tab/bộ lọc màn hình | `tabType`, `viewType` trong VM (`ReminderVM.doChangeTabStatus`) | Thêm nhánh trong `updateStatusByTab()` + zul tab + điều kiện query BE |

Máy trạng thái văn bản đi (mã số thật) — xem `knowledge/van-ban/di/nghiep-vu.md`. Thêm trạng thái vào vòng đời văn bản là việc **L**: ảnh hưởng menu "Ký điện tử" (mỗi trạng thái một menu), dashboard đếm số (`HomeController`), mobile, liên thông.

## 3. Thêm lý do / ghi chú hành động (ví dụ "lý do thu hồi")

Pattern sẵn có: `rejectPublish.zul` + `RejectPublishVM` (từ chối ban hành có lý do) → BE `textAction.rejectPublish` ❓ tên hàm — xem `requisition/ban-do`. Làm tương tự: popup nhập lý do → Business → endpoint → lưu vào bảng lịch sử (`TEXT_PROCESS_HISTORY`, `DOCUMENT_HISTORY_LOG`, `REMINDER_HISTORY` là các bảng lịch sử đang có) thay vì cột đơn lẻ, để có lịch sử nhiều lần.
