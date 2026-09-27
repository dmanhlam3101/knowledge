# Cách làm chuẩn: thêm một tính năng mới (end-to-end)

> Mẫu tham chiếu: **Nhắc việc (reminder)** — tính năng mới nhất, làm hoàn toàn theo cơ chế mới (web → BE gen-2 → JPA → Oracle).
> Khi thêm tính năng mới, **copy pattern từ reminder**, không copy từ `document/*`, `requisition/*` (legacy, lẫn 2 cơ chế).

## 0. Nguyên tắc

1. Logic + truy vấn DB nằm ở **BE gen-2** (`com.viettel.office`). Web chỉ hiển thị và gọi API.
2. Không thêm facade / JPA DAO / entity mới ở web. Không thêm code vào BE gen-1 nếu không phải sửa tính năng cũ.
3. Mỗi màn hình mới cần **4 nơi**: SQL (bảng + menu), BE (controller→service→repo→entity), web `Business`, web `zul + VM`.
4. Làm theo thứ tự **DB → BE → Business → VM/zul**, test API bằng Postman/Swagger trước khi làm màn hình.

## 1. Bản đồ mẫu (reminder) — mở các file này để xem cách viết

| Tầng | File thật | Vai trò |
|---|---|---|
| SQL | `backend2.0/backendvoffice/sql/19062026_create_table_reminder.sql`, `04082026_add_table_reminder_history.sql` | SEQUENCE + TABLE `REMINDER`, `REMINDER_REPLY`, `REMINDER_FOLLOWER`, `REMINDER_DOCUMENT_RELATION`, `REMINDER_HISTORY` |
| Entity | `backend2.0/.../com/viettel/office/entities/ReminderEntity.java` (+ `ReminderReplyEntity`, `ReminderFollowerEntity`, `ReminderDocumentRelationEntity`) | `@Entity @Table`, sequence, `DEL_FLAG`, audit |
| Repository JPA | `.../repositories/jpa/ReminderRepositoryJPA.java` (+ `ReminderReplyRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`) | `@Query` JPQL projection sang DTO, `@Modifying` soft delete |
| Repository SQL tay | `.../repositories/ReminderRepository.java` + `repositories/impl/ReminderRepositoryImpl.java` | Tìm kiếm phân trang nhiều join bằng text block SQL qua `BaseRepositoryImpl` |
| Service | `.../services/ReminderService.java` + `services/impl/ReminderServiceImpl.java` (~1.800 dòng) | Nghiệp vụ: save/reply/approve/delete/remindAgain/history; `@Transactional(rollbackFor = Exception.class)` |
| Controller | `.../controller/ReminderController.java` — `@RequestMapping("/reminders")` | 17 endpoint POST; `getUserId()` từ JWT; `ResponseUtils.getResponseEntity(...)` |
| DTO | `.../dto/request/reminder/*RequestDTO`, `.../dto/response/reminder/*DTO`, `.../projection/ReminderDashboardProjection` | Tách request/response |
| Exception | `.../services/ReminderPromulgationException.java` | Lỗi nghiệp vụ riêng |
| Web Business | `web-spring/.../com/voffice/service/business/ReminderBusiness.java` | Mỗi hàm = 1 endpoint (`"reminders.search"`, `"reminders.insertOrUpdate"`, …), parse Gson |
| Web model | `web-spring/.../com/voffice/service/entity/ReminderEntity.java`, `com/viettel/voffice/dto/reminder/*DTO` | Bản sao DTO phía web |
| Web VM | `web-spring/.../com/viettel/voffice/vm/reminder/ReminderVM.java` (list+add), `ReminderViewDetailVM`, `ReminderReplyVM`, `ReminderActionVM`, `ReminderReportVM`, `ReminderAssigneeLookupVM` | `extends SecurityVM<Reminder>`, `doSearch`, `onDoInsert`→`validateDoSave`→`buildSaveRequest`→`executeSaveToBackend` |
| Web zul | `web-spring/src/main/webapp/view/voffice/reminder/` — `reminder.zul` (list), `reminder_search.zul`, `reminder_add.zul`, `reminder_add_modal.zul`, `reminder_viewDetail.zul`, `reminder_reply.zul`, `reminder_approve.zul`, `reminder_report.zul`, `reminder_draft_card.zul`, `reminderAssigneeLookup.zul` | Tách list / search / add / detail / reply |
| Nhúng vào màn khác | `DocumentViewDetailVM`, `DocumentOutVM`, `DocumentDraftVM` mở `reminder_add_modal.zul`; `ReminderBusiness.getDraftReminderDetail(textId)` / `...ByDocumentId` | Tính năng mới móc vào văn bản qua `TEXT_ID` hoặc `DOCUMENT_ID` |

## 2. Các bước — checklist

### Bước 1. Thiết kế dữ liệu (SQL Oracle)
- [ ] File `backend2.0/backendvoffice/sql/<DDMMYYYY>_<mo_ta>.sql`: `CREATE SEQUENCE SEQ_<TABLE>`, `CREATE TABLE` với `<TABLE>_ID NUMBER(19,0)`, `DEL_FLAG NUMBER(1,0) DEFAULT 0`, `CREATED_AT DATE, CREATED_BY NUMBER(19,0), UPDATED_AT, UPDATED_BY`, `COMMENT ON COLUMN` tiếng Việt.
- [ ] Quan hệ với văn bản: cột `TEXT_ID` (dự thảo) và/hoặc `DOCUMENT_ID` (đã ban hành) — xem `REMINDER_DOCUMENT_RELATION`.
- [ ] Nếu có màn hình mới trong menu: `INSERT INTO SYS_MENU (...)` — mẫu `sql/19122025_add_row_sys_menu.sql` (URL = đường dẫn `.zul`, `PARENT_ID` = menu cha, `PATH` = `/<parent>/<id>/`).
- [ ] Index cho cột lọc chính (`ORG_ID`, `STATUS`, `DEL_FLAG`, ngày).

### Bước 2. BE gen-2
- [ ] `entities/XxxEntity.java` — theo mẫu `ReminderEntity`.
- [ ] `repositories/jpa/XxxRepositoryJPA.java` — CRUD + `@Query` cần thiết. Query phức tạp → `repositories/XxxRepository` + `impl/XxxRepositoryImpl` với `BaseRepositoryImpl`.
- [ ] `dto/request/<domain>/XxxSearchRequestDTO`, `XxxSaveRequestDTO`; `dto/response/<domain>/XxxResponseDTO`.
- [ ] `services/XxxService` + `services/impl/XxxServiceImpl` — validate, quyền (userId từ `getUserId()`, orgId từ user), `@Transactional`.
- [ ] `controller/XxxController` — `@RequestMapping("/api/xxx")`, mỗi thao tác 1 `@PostMapping`, trả `ResponseUtils.getResponseEntity(...)`.
- [ ] Message lỗi: `messages_vi.properties` / exception riêng nếu cần.
- [ ] Test bằng Swagger (`/ServiceMobile_V02/resources/swagger-ui.html`) hoặc Postman (`backend2.0/backendvoffice/postman/`).

### Bước 3. Web — client gọi BE
- [ ] `com/voffice/service/entity/XxxEntity.java` hoặc `com/viettel/voffice/dto/<domain>/XxxDTO.java` — field trùng JSON BE.
- [ ] `com/voffice/service/business/XxxBusiness.java extends Business` — hàm `search(...)`, `save(...)`… gọi `servePostRequest(json, "api.xxx.action")` hoặc `serveProcessing("api.xxx.action", params)`; parse `root.data`/`root.result`. Theo mẫu `ReminderBusiness.getListReminders`, `saveReminders`.

### Bước 4. Web — màn hình
- [ ] `view/voffice/<domain>/xxx.zul` (list, dùng `menuPathLabel.zul` + `toolbarButton.zul`), `xxx_search.zul`, `xxx_add.zul`, `xxx_viewDetail.zul`.
- [ ] `vm/<domain>/XxxVM extends SecurityVM<XxxEntity>` với `@Init(superclass = true) @AfterCompose(superclass = true)`; khởi tạo `new XxxBusiness(serviceConnection)` trong `postViewInitialized()`; `@Command doSearch/onDoInsert/...`.
- [ ] Nhãn: thêm key `voffice.<domain>.label.*` vào `common_voffice_vi.properties` + `_en` (reminder hiện đang hard-code tiếng Việt trong zul — ❓ team chấp nhận hay yêu cầu i18n?).
- [ ] Popup chọn đơn vị/người: dùng lookup có sẵn (`selectMainOrg`, `doSelectSysUser` trong `ReminderVM` là ví dụ).
- [ ] Nếu cần reload màn khác sau khi lưu: `EventQueues.lookup(AppConstants.EVENT_QUEUE.*)`.
- [ ] Nếu nhúng vào chi tiết văn bản: mở modal theo cách `DocumentViewDetailVM` mở `reminder_add_modal.zul`.

### Bước 5. Quyền, menu, thông báo
- [ ] Menu: dòng SYS_MENU (bước 1) + gán vào vai trò (SYS_ROLE ↔ menu) ❓ cách gán — hỏi admin/DBA.
- [ ] Quyền thao tác trong màn hình: `screenName` + `LookupUtil.getPopupPermision` nếu màn hình có nút phân quyền.
- [ ] Thông báo/SMS: `NotificationAction`/`NotificationService`, cấu hình `smsMaster` (xem `lich-nhac-viec/`).

### Bước 6. Cập nhật tri thức
- [ ] `knowledge/<phanhe>/nghiep-vu.md`, `dac-thu.md`; chạy `_tools/scan.py && gen.py`.

## 3. Ước lượng độ lớn (để BA/PM nói chuyện)

| Cỡ | Ví dụ | Việc |
|---|---|---|
| S | Thêm cột/trạng thái, thêm nút hành động trên màn có sẵn | SQL + entity/DTO + 1 endpoint + sửa VM/zul |
| M | Màn hình danh sách + thêm/sửa + chi tiết (kiểu reminder) | 4–6 bảng/endpoint, 4–6 zul, 3–4 VM |
| L | Xuyên phân hệ, đổi luồng ký/xử lý, tích hợp ngoài | Thêm cả sửa gen-1 hoặc luồng FLOW/NODE |
