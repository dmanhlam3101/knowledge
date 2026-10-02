# Nhắc việc, thông báo, SMS — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. **Nhắc việc là tính năng gen-2 mới nhất (2026) — mẫu chính khi làm tính năng mới**: bảng mới + migration SQL, controller mỏng, service `@Transactional`, repository JPA + SQL text block, web `*Business` + VM + zul, và móc vào luồng văn bản cũ. Khi copy, tránh các điểm đã ghi ở `dac-thu.md` (nêu ở cuối từng mẫu).

## Mẫu 1 — Tính năng gen-2 end-to-end: **Nhắc việc** (tạo / sửa / xóa, có kiểm người tạo ở BE)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Migration | `SQL/19062026_create_table_reminder.sql` (4 bảng + sequence + index), `SQL/04082026_add_table_reminder_history.sql` (bảng có `COMMENT ON` từng cột), `SQL/20260808_YC_reminder.sql` (thêm cột vào bảng cũ) | Bảng có `DEL_FLAG` mặc định 0, sequence `SEQ_<BẢNG>`, **comment cột** (bảng lịch sử làm đúng, các bảng đầu thiếu) |
| Entity | `BE2/entities/ReminderEntity.java`, `ReminderReplyEntity.java`, … (`@Table`, `@SequenceGenerator(allocationSize = 1)`) | Khai entity theo sequence có sẵn |
| DTO | `BE2/dto/request/reminder/*` (`ReminderSaveRequestDTO` có hằng trạng thái + `statusName`), `BE2/dto/response/reminder/*` | Gom hằng trạng thái + tên hiển thị một chỗ (`RSRD:11-40`) |
| Controller | `RC:28-154` — mỗi endpoint vài dòng, lấy người dùng bằng `CoreUtils.getUserId()`, trả `ResponseUtils.getResponseEntity` | Endpoint mỏng, không logic |
| Service | `RSI.saveReminders` :101-314 (`@Transactional(rollbackFor = Exception.class)`): sửa thì `findById` + **kiểm người tạo** → `CustomException(ErrorApp.BAD_REQUEST, "Đồng chí không có quyền…")` (:114-122); đồng bộ danh sách con bằng **so tập cũ / mới, xóa mềm phần bỏ, thêm phần mới** (văn bản :146-193, người theo dõi :199-301, đơn vị :1118-1174); `deleteReminder` :1288-1334 (kiểm người tạo, xóa mềm, `setRollbackOnly` khi lỗi khác) | Khung "tìm → kiểm quyền → ghi cha → đồng bộ con theo diff" |
| Repository | JPQL / native trong interface (`RRJ`, `RRRJ`: `@Modifying` update hàng loạt, projection `ReminderDashboardProjection`); SQL động trong `RRI` qua `BaseRepositoryImpl.getListDataNativeQueryPageable` (:202-208), tìm bỏ dấu `handle_vietnamese(...) LIKE :kw ESCAPE '/'` + `FunctionCommon.removeUnsign` (:122-127, :535-537) | SQL động có phân trang, tìm không dấu |
| Web Business | `RB` — mỗi hàm build JSON, `servePostRequest(json, "reminders.xxx")`, parse `result.data` (ví dụ `saveReminders` :305-315, `getListReminders` :157-193) | Khóa `a.b` → URL `/a/b` |
| Web VM / zul | RVM kế thừa `SecurityVM`/`CommonVM` (`insert` / `update` / `delete` override :968-977, :1473-1485; `validateDoSave` :596-734); `ZUL/reminder/reminder.zul` include `reminder_search.zul` + `reminder_add.zul` | Một VM cho danh sách + form theo `viewState` của `CommonVM` |

**Không copy**: `Collectors.toMap` không hàm gộp trên dữ liệu có thể trùng (`dac-thu.md` L3); xóa liên kết theo `OBJECT_ID` mà không lọc loại (L6); truyền nhầm danh sách id (L2); nhãn ghi cứng tiếng Việt trong zul / VM.

## Mẫu 2 — Hộp việc hai nhóm nhiều tab + số đếm một câu SQL + widget trang chủ có link: **Theo dõi nhắc việc**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul tab | `ZUL/reminder/reminder_search.zul:22-56` (hai "nhóm" bằng `div` + `changeGroupType`, tab bằng nút + `doChangeTabStatus`, nhãn `vm.tab*Label`) | Hai cấp lọc (nhóm / tab) trên một lưới |
| VM | `RVM.updateStatusByTab` :543-588 (tab → bộ lọc trạng thái, khóa combobox), `setupListStatus` :2159-2174, `generateMenuCount` :2311-2351 (nhãn tab lấy từ một lần đếm) | Quy đổi tab → tham số BE ở một chỗ |
| BE danh sách | `RRI.searchReminders` :31-209 (điều kiện "của tôi" theo nhóm, mã lọc đặc biệt quá hạn / sắp đến hạn, khoảng ngày mặc định 365 ngày) | — |
| BE đếm | `RRJ.getDashboardCountsV2` :143-268: **một CTE** lấy tập dữ liệu của người dùng rồi `SUM(CASE …)` cho từng ô; service bọc null → 0 (`RSI:1560-1577`) | Đếm mọi ô bằng một câu, nhẹ hơn chạy N truy vấn |
| Widget | `HomeVM.generateNhacViecWidgetDynamic` :4549-4596 (ô con theo `HOME_WIDGET.PARENT_CODE`, chỉ ô `IS_ACTIVE = 1`), `createReminderUrl` :4598-4654 (tham số mã hóa AES, mở menu theo mã `NHACVIEC`); VM đích đọc tham số `homeReminder` (`RVM:2734-2764`) | Widget → mở menu kèm bộ lọc |

**Lưu ý khi copy**: đừng dùng lại số trạng thái làm mã lọc (`dac-thu.md` bẫy 2); điều kiện "của tôi" phải giữ khớp giữa danh sách và câu đếm (bẫy 4).

## Mẫu 3 — Đối tượng con soạn kèm form cha, lưu chung giao dịch của cha và chuyển trạng thái theo vòng đời cha: **Nhắc việc trên dự thảo / văn bản đi**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Card nhúng | `ZUL/reminder/reminder_draft_card.zul` được include trong `ZUL/documentDraft/documentDraft_add.zul:2337`, `ZUL/document/inputDoc/doc_out_add.zul:1082` | Một zul con dùng lại ở nhiều form cha |
| Popup không gọi BE | RVM với `fromDocumentDraft = true` → trả kết quả qua `BindUtils.postGlobalCommand(…, "draftReminderSaved", args)` (`RVM:820-826`); form cha giữ bản nháp trong `dataSelected.reminderDraft` (`DDVM:5349-5415`, `DOVM:2611-2682`) | Soạn trong popup, lưu khi lưu cha |
| Lưu chung giao dịch | gen-1 đọc thêm trường JSON `reminderDraft` / `reminderReplyDrafts` (`DC:351-371`, `452-476`; `DSC:947-954`, `1947-1959`) rồi gọi `RSI.saveDraftReminders` — javadoc "join the transaction opened by addText" (`RSI:566-672`) | Service gen-2 được gọi trong giao dịch gen-1 |
| Chuyển trạng thái theo cha | ban hành → `RSI.promulgateDraftReminders` (`TC:1880-1889`; `RSI:484-564`); chuyển văn bản → `RSI.updateStatusAfterTransferDocument` (`DC:8074-8093`; `RSI:339-482`); xóa cha → `deleteRemindersByDocumentIdOrTextId` (`DC:1028-1031`; `TC:7561`) — lỗi bọc trong `ReminderPromulgationException` để bên gọi bắt riêng (`TC:1930`) | Liên kết theo `TEXT_ID` trước, gán `DOCUMENT_ID` khi ban hành (`RSI:509-513`) |
| Gợi ý điền sẵn ở thao tác của cha | `RSI.getListOrgForTransfer` (`RSI:74-99`; `RRI:211-246`) → popup chuyển văn bản tự thêm đơn vị kèm vai trò (`TDVM:902-904`, `2036-2055`) | Dữ liệu con gợi ý cho thao tác của cha |

**Lưu ý**: ba đường lưu (`insertOrUpdate`, `saveDraftReminders`, `saveDocumentReminders`) đang có quy tắc khác nhau (`dac-thu.md` bẫy 8) — làm mới thì gom về một hàm.

## Mẫu 4 — Thao tác "chuyển xử lý" + bảng lịch sử riêng: **Gán người xử lý nhắc việc**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Popup | `ZUL/reminder/reminderAssigneeLookup.zul` + RALVM (`onSubmit` :145-194: kiểm bắt buộc, build DTO, `postGlobalCommand("refreshReminderDetail")`) | Popup chọn người + ý kiến, làm mới màn cha |
| Service | `RSI.updateNewReplyAssigneeAndFollowers` :1485-1528 (`@Transactional`): cập nhật người xử lý → đồng bộ người theo dõi → **ghi `REMINDER_HISTORY` với `TYPE`** để mở rộng loại lịch sử sau | Bảng lịch sử có cột `TYPE` (comment "có thể mở rộng") |
| Đọc lịch sử | `RC:148-152` → `BE1/database/dao/ReminderHistoryDAO.java:16-57` (lọc theo đơn vị), hiển thị + combobox lọc đơn vị `RVDVM:579-611` | — |

**Lưu ý**: so người theo dõi theo cả loại, không chỉ theo người (`dac-thu.md` L11).

## Mẫu 5 — Gửi SMS + thông báo đúng chuẩn từ một nghiệp vụ (gen-2 gọi DAO gen-1)

Nhắc việc **chưa** gửi tin (NV-02). Mẫu đang dùng tốt: **phiếu trình** — `BE2/services/impl/SubmissionManagerServiceImpl.java:2702-2753` (`sendSMSSubmission` + `addNotification`; xem `../phieu-trinh/vi-du-mau.md`).

| Bước | Vị trí | Copy phần nào |
|---|---|---|
| Loại tin | thêm dòng `CONFIG_SMS_MODULE` (cha + `IS_STYPE`) + hằng `C1:1372-1456`; mẫu script `SQL/20260723_insert_table_sys_mess_and_sys_noti_and_sms_module.sql` (chèn cả mẫu SMS, mẫu SMS mật, mẫu thông báo và loại tin trong một script) | Một script cho cả ba bảng |
| Ghi SMS | `SDAO.addMessToTableMessVof2(người gửi, người nhận, SĐT, nội dung, loại tin, độ mật)` (`SDAO:268-307`) — tự kiểm chặn qua `shouldSendSms` (`SDAO:271`) | **Luôn truyền mã loại tin** để người dùng / đơn vị chặn được (tránh `dac-thu.md` L17) |
| Nội dung | `CC.getStrMessNotificationConfigVn` / mẫu theo `TYPE`, `CATEGORY` (`CC:1584-1636`; `SDAO:71-138`) | Không ghi cứng nội dung |
| Thông báo | `CC.sentNotification(CC.notificationWrapper(...))` (`CC:1249-1272`) hoặc `NotificationEntity.builder()` + đặt `URL` (web điều hướng theo URL — `dac-thu.md` bẫy 13) và `MENU_CODE` qua `NMM` | Bỏ qua khi người gửi = người nhận |

## Mẫu 6 — Cấu hình theo đơn vị nhỏ gọn (gen-2): **Chặn tin nhắn theo đơn vị**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Bảng + menu | `SQL/20250821_create_table_config_sms_org.sql` (bảng, sequence, trigger, **thêm menu** `SYS_MENU` trong cùng script) | Script tạo kèm menu |
| Web | `ZUL/config/sms/smsConfigOrg.zul` + `SmsConfigOrgVM` (cây có tick cha – con :145-189, chỉ gửi dòng đổi :193-227); danh sách đơn vị lọc theo vai trò admin (`BE2/services/impl/VhrOrgServiceImpl.java:420-435`) | — |
| BE | `BE2/controller/SMSInterceptController.java:24-34` → `SISI:33-98` (upsert, bỏ tick thì xóa) → `ConfigSmsOrgRepositoryJPA` | Controller 2 endpoint + service upsert |

**Lưu ý**: dùng `toMap` có hàm gộp và lọc `CONFIG_TYPE` khi đọc (`dac-thu.md` L21).
