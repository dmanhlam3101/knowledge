# Nhắc việc & thông báo — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| **Tính năng mới end-to-end** (bảng mới, gen-2, web mới, nhúng vào văn bản) | Toàn bộ reminder — bảng liệt kê file trong `_chung/cach-lam-chuan/them-tinh-nang-moi.md` §1 |
| Đối tượng có nhiều "khối" con + nhiều đơn vị nhận mỗi khối | `ReminderSaveRequestDTO` → `ReminderBlockDTO` → `ReminderUnitDTO`; web `ReminderVM.addReminderBlock/copyReminderBlock/mapDraftBlocks` |
| Trả lời → duyệt → trả lại (vòng phê duyệt nhẹ) | `ReminderServiceImpl.replyReminders`, `approveReminders`, `REPLY_STATUS_*` |
| Nhắc lại có lịch sử | `remindAgain` + `ReminderHistoryDAO` + bảng `REMINDER_HISTORY` (SQL `04082026_add_table_reminder_history.sql`) |
| Chặn hành động ở phân hệ khác dựa trên dữ liệu của mình | `DocInController.check-completion-reminders` (văn bản đến hỏi nhắc việc trước khi hoàn thành) |
| Tìm kiếm phân trang nhiều join bằng SQL tay (gen-2) | `ReminderRepositoryImpl.searchReminders` (text block SQL + `BaseRepositoryImpl.getListDataAndCount`) |
| Card tóm tắt nhúng vào màn khác | `reminder_draft_card.zul` + `ReminderBusiness.getDraftReminderDetail(textId)` |
| Đếm cho dashboard | `reminders.getCountReminderDashboard`, `ReminderDashboardProjection` |
| Thông báo đọc/chưa đọc theo đối tượng | gen-1 `NotificationAction.updateIsReadByObjectID`, `countNotificationUnread` |
| Cấu hình chặn theo đơn vị (gen-2) | `SMSInterceptController.updateSmsInterceptConfigByOrg` + `vm/config/sms` |
| Văn bản "ngoài luồng" có nhóm nhận và file mật (gen-2) | `DocumentInformalityController` (`create-or-update`, `send`, `search`, `mark-as-read`, `get-permission-view-file`) + `vm/graspSituation` |
