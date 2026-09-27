# Nhắc việc & thông báo — đặc thù

- **Nhắc việc = mẫu gen-2 chuẩn nhất** (xem `_chung/cach-lam-chuan/them-tinh-nang-moi.md`): `ReminderController` (`/reminders`, 16 endpoint, không prefix `/api`) → `ReminderServiceImpl` (~1.800 dòng, `@Transactional`) → `ReminderRepositoryJPA` + `ReminderRepositoryImpl` (SQL text block qua `BaseRepositoryImpl`) → `REMINDER*`. Web `vm/reminder/*` (6 VM) + `ReminderBusiness` (18 hàm). Không có gen-1 tương đương. `reminders.cancelReply`, `getReminderReport`, `updateNewReplyAssignee` web gọi nhưng BE không có → ❓ chưa làm hoặc đã bỏ.
- `ReminderServiceImpl` phụ thuộc trực tiếp repo văn bản (`DocumentRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentInGroupRepositoryJPA`, `DocumentProcessRepositoryJPA`, `VhrOrgRepositoryJPA`) — nhắc việc **đọc thẳng bảng văn bản**; đổi schema văn bản ảnh hưởng nhắc việc.
- Nhắc việc được nhúng vào chi tiết văn bản (`DocumentViewDetailVM`, `DocumentOutVM`, `DocumentDraftVM`) qua `reminder_add_modal.zul`, `reminder_draft_card.zul` — sửa giao diện nhắc việc phải test cả màn văn bản.
- Nhãn màn hình nhắc việc **hard-code tiếng Việt** trong zul (không i18n) — nếu team yêu cầu i18n thì đây là nợ.
- Thông báo (`NotificationAction`) và SMS chặn (`SmsInterceptAction`) là gen-1; SMS chặn theo đơn vị mới thêm ở gen-2 (`SMSInterceptController`). `api.smsIntercept.getListModulInterceptSmsOfOrgId.` (dấu chấm cuối) không nối được endpoint ❓ bug tên.
- Nắm tình hình chạy gen-2 `DocumentInformalityController` + `DocumentInformalityGroupController` (`/api/document-informality*`) — web `graspSituation/*` (4 zul) + `vm/graspSituation` (4 VM), nhãn BE. Facade legacy còn dùng: `INotice`, `IOrientation`, `IMultimediaNotification`, `ITimeConfig`.
- Bảng `ALERT` (web entity `Alert`) là cơ chế cảnh báo cũ ❓ còn dùng.
