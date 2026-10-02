# Kiến trúc tổng thể VOKhanhHoa

> Đọc file này trước khi làm bất kỳ tính năng nào. Mọi phân hệ đều đi qua các cơ chế mô tả ở đây.

## 1. Hai repo, ba thế hệ code

```
┌──────────────────────────── web-spring (WEB) ────────────────────────────┐
│  ZK 6.5.3 MVVM + Spring Boot, Java 8                                     │
│  .zul (màn hình) → *VM (ViewModel) ─┬─► *Business ──HTTP──► BE           │  ← CƠ CHẾ MỚI
│                                     └─► Delegate.getService(I*) → *Facade│  ← CƠ CHẾ CŨ (legacy)
│                                            → *Service → *JpaDao → Oracle │     query thẳng DB từ web
└──────────────────────────────────────────────────────────────────────────┘
                                   │ POST {voffice.service.url}/a/b  (Bearer JWT + JSESSIONID)
┌──────────────────────── backend2.0/backendvoffice (BE API) ──────────────┐
│  Spring Boot 3.5, Java 21, context-path /ServiceMobile_V02/resources     │
│  gen-1  com.viettel.voffice : action/*Action|*Resource (@RestController) │
│         → controler/*Controller (@Service, logic lớn, port từ EJB cũ)     │
│         → database/dao/*DAO (@Service, SQL thuần qua CommonDataBaseDaoVO2)│
│  gen-2  com.viettel.office  : controller/*Controller (/api/..., /reminders)│
│         → services/*Service(+Impl) → repositories/jpa/*RepositoryJPA      │
│         → entities/*Entity (@Entity/@Table)   ← ToolGen 2024, kiểu Spring │
└──────────────────────────────────────────────────────────────────────────┘
                                   │
                              Oracle DB (sequence SEQ_*, DEL_FLAG, NVARCHAR2; DB DEV gần như không có FK)
                              + Elasticsearch (tìm kiếm + log tập trung; Solr đã bỏ), Redis / memcached (cache)
                              + file trên thư mục đĩa theo khóa storage_* (không có MinIO)
                              + tiến trình NGOÀI repo: gửi SMS, gửi/nhận trục liên thông, đánh chỉ mục ES, đồng bộ hai site
```

(sửa 2026-10-02 theo `tich-hop` NV-10, NV-13 và `lich-nhac-viec` NV-13: bản cũ ghi "Elasticsearch/Solr", "ELS logs".) Chi tiết hạ tầng ngoài: mục 8.

Ngoài ra `backend2.0/voffice-lib` (`voffice-core`, `voffice-gencode`) là lib dùng chung / sinh code cho BE gen-2.

### Số liệu (2026-09-30, nhánh `kha_develop`, từ `_tools/scan.py`)

| | Web | BE |
|---|---|---|
| Màn hình `.zul` có VM | 629 (có nhãn ☠ = trỏ VM không tồn tại, xem `ban-do.md` từng phân hệ) | — |
| ViewModel | 559 | — |
| `*Business` (client gọi BE) | 81 class / 1.164 hàm → 1.153 nối được endpoint | — |
| Facade legacy | 44 | — |
| Controller / endpoint | — | 152 / 1.757 |
| Logic gen-1 / DAO gen-1 | — | 80 / 156 |
| Service gen-2 / Repository / Entity | — | 255 / 200 / 192 |

(sửa 2026-09-30: số cũ "790 hàm / 1.733 endpoint" đã lỗi thời.)

Chi tiết: [`ban-do-tong/thong-ke.md`](ban-do-tong/thong-ke.md).

## 2. Cơ chế MỚI: web gọi BE (dùng cho mọi tính năng mới)

```java
// trong VM (kế thừa SecurityVM<T> → CommonVM<T> → CommonModel)
// CommonModel đã có sẵn: serviceConnection = SessionUtil.getWebServiceConnection(httpSession)
reminderBusiness = new ReminderBusiness(serviceConnection);
List<ReminderEntity> list = reminderBusiness.getListReminders(searchRequest);

// trong com.voffice.service.business.ReminderBusiness extends Business
String response = servePostRequest(json, "reminders.search");     // hoặc serveProcessing("a.b", Map params)
// Business.serveProcessing → ServiceConnection.sendPostRequest:
//   URL = voffice.service.url + "reminders/search"   (dấu "." → "/")
//   header Cookie: JSESSIONID=..., Authorization: Bearer <JWT lấy lúc login>
//   body: application/x-www-form-urlencoded (param "data" = JSON) hoặc JSON tùy Business
```

BE nhận: gen-2 `@RestController @RequestMapping("/reminders")` + `@PostMapping("/search")`; lấy user từ JWT bằng `CoreUtils.getUserId()`; trả `ResponseEntity<ResultResponse<T>>` qua `ResponseUtils.getResponseEntity(...)`. Web parse JSON: `root.data` / `root.result` (xem `ReminderBusiness.getDraftReminderDetail`).

Quy tắc nối tự động: hàm `"a.b"` ở web ↔ endpoint `/a/b` ở BE — bảng đầy đủ tại [`ban-do-tong/web-goi-be.md`](ban-do-tong/web-goi-be.md).

## 3. Cơ chế CŨ: web query thẳng DB (legacy, KHÔNG dùng cho tính năng mới)

```java
IDocument iDocument = Delegate.getService(IDocument.class);   // com.viettel.voffice.remote.IDocument
// → DocumentFacade (@Component implements IDocument) → DocumentService → *JpaDao (EntityManager) → Oracle
```

- 74 VM còn dùng đường này (nhãn **LEGACY** / **BE+LEGACY** trong `ban-do.md`). Hay gặp nhất: `ISysOrganization`, `ISysUser`, `ICommonVoffice` (tra cứu đơn vị/người dùng/danh mục ngay trong web).
- Entity web (`com.viettel.voffice.entity`, `com.viettel.vps.entity`) trùng bảng với entity BE — **hai bộ mapping cho cùng bảng**, sửa schema phải sửa cả hai nếu bảng đó còn được web đọc. Tên entity web khác tên bảng: `SysUser` = `VHR_EMPLOYEE`, `SysOrganization` = `VHR_ORG` (`he-thong/dac-thu.md` bẫy 1).
- **Không chỉ đọc — có nghiệp vụ GHI thẳng DB từ web** (không qua BE), nên sửa nghiệp vụ phải sửa ở web: mọi thao tác ghi **lịch họp** (đặt, sửa, duyệt, từ chối, hủy, xóa, phân công — `hop` 1.1, `hop/dac-thu.md` mục 1; BE có bản ghi riêng cho kênh khác — `hop` NV-17); quản trị **người dùng / vai trò / menu / danh mục động** (`he-thong/dac-thu.md` mục 1); **kiến nghị** `request/*` (PT NV-18); **thông báo chung** `NOTICE` (LNV NV-12); **KPI đơn vị / đề xuất cộng điểm / đánh giá đơn vị** (`kpi-danh-gia` cụm C); web cũng ghi thẳng hàng đợi `SMS_MASTER` (LNV NV-13). (sửa 2026-10-02)
- Nguyên tắc: tính năng mới → không thêm facade/DAO mới ở web; nếu cần dữ liệu, thêm endpoint BE gen-2 rồi thêm hàm vào `*Business`. Xem [`cach-lam-chuan/sua-tinh-nang-cu.md`](cach-lam-chuan/sua-tinh-nang-cu.md).

## 4. BE gen-1 vs gen-2 — chọn cái nào

| | gen-1 `com.viettel.voffice` | gen-2 `com.viettel.office` |
|---|---|---|
| Endpoint | `/textAction/getTextDetail`, `/DocumentAction/...`, `/Meeting/...` (tên tự do, PascalCase lẫn camelCase) | `/api/<kebab-case>/...`, `/reminders/...` |
| Vào/ra | `@RequestParam String data` (JSON trong form-urlencoded) + `isSecurity`, trả `String` JSON tự ghép | `@RequestBody XxxRequestDTO`, trả `ResultResponse<T>` |
| Logic | `controler/*Controller` (@Service) — file rất lớn (TextController hàng nghìn dòng, 20+ DAO) | `services/*ServiceImpl` + `@Transactional(rollbackFor = Exception.class)` |
| Data | `database/dao/*DAO` SQL thuần, `database/entity/*` là POJO/filter (không @Entity) | `repositories/jpa/*RepositoryJPA extends JpaRepository`, `@Query` JPQL/native; `entities/*Entity` @Entity/@Table |
| Ai gọi | Web (đa số hàm `*Business`), mobile | Web (reminder, doc-in mới...), mobile, ứng dụng ngoài (`/ext-*`) |
| Khi nào dùng | **Sửa** tính năng cũ đang ở đó | **Thêm** tính năng/endpoint mới; hoặc khi sửa gen-1 quá rủi ro thì tạo endpoint gen-2 mới và chuyển web sang |

Tính năng mới gần nhất làm hoàn toàn theo gen-2: **Nhắc việc** (`ReminderController` `/reminders` → `ReminderServiceImpl` → `ReminderRepositoryJPA` → `REMINDER*`), web `vm/reminder/*` + `ReminderBusiness`. Đây là mẫu chuẩn: [`cach-lam-chuan/them-tinh-nang-moi.md`](cach-lam-chuan/them-tinh-nang-moi.md). Các phân hệ còn lẫn tầng: gen-1 gọi thẳng service gen-2 (nhắc việc móc vào văn bản — `lich-nhac-viec/dac-thu.md` mục 1); service gen-2 gọi DAO gen-1 (lịch sử nhắc việc). Bảng "tầng nào làm gì" của từng phân hệ: mục 1 `dac-thu.md`.

## 5. Những thứ nằm trong DB chứ không trong code

| Thứ | Ở đâu | Hệ quả |
|---|---|---|
| Menu web | `SYS_MENU` (URL trỏ thẳng tới file `.zul`) + gán cho vai trò `ROLE_MENU` + **danh sách trắng theo đơn vị** `ORG_SYS_MENU` (menu đã có ≥ 1 dòng thì chỉ cây đơn vị khai mới thấy) | Thêm màn = SQL chèn `SYS_MENU` **và** `ROLE_MENU` (mẫu `backend2.0/backendvoffice/sql/19122025_add_row_sys_menu.sql` chỉ chèn `SYS_MENU`). Ứng dụng mới / mobile dùng **bộ menu khác** `MENU` + `SYS_ROLE_MENU` + `ORG_MENU` — `he-thong` NV-03, NV-10, BR-11, `dac-thu.md` bẫy 6–7 (sửa 2026-10-02) |
| Trạng thái/loại văn bản, họp... | `CODE_MASTER` (web đọc qua key `code.doc.status`, `code.doc.state`, `code.meeting.status`… trong `AppConstants`) | Nhiều trạng thái là **dữ liệu**, không phải enum; đối chiếu DB trước khi hard-code |
| Quyền | **menu được cấp** (`ROLE_MENU`, `ORG_SYS_MENU`) + **điều kiện hiện nút trong VM**. Cơ chế thao tác × tài nguyên VPS (`SYS_OPERATION`, `SYS_RESOURCE`, `PERMISSION`) **đã tắt**, RBAC gen-2 `officeCheckPermission()` luôn cho qua (`he-thong` NV-09 BR-25). `LookupUtil.getPopupPermision` **không phải** kiểm quyền — chỉ đếm popup đang mở (`web-spring/src/main/java/com/viettel/zk/common/LookupUtil.java:71-94`) | Nút mới: viết điều kiện hiển thị trong VM + cấp menu; BE không kiểm người gọi (mục 6) (sửa 2026-10-02: bản cũ ghi quyền theo `SYS_OPERATION` + `getPopupPermision`) |
| Tham số hệ thống | `SYSTEM_PARAMETER` (+ `application.properties` cho URL / tài khoản tích hợp) | Bật/tắt tính năng, ngưỡng, URL tích hợp — nhiều khóa chứa địa chỉ / tài khoản: tri thức chỉ ghi tên khóa (`he-thong` NV-14, `tich-hop` 1.6) |
| Luồng ký | bảng `FLOW*`, `NODE*` (gen-2 `FlowEntity`, `NodeEntity`, `NodeToNodeEntity`…) | Luồng là cấu hình, không hard-code bước ký; sửa sơ đồ có hiệu lực ngay với văn bản đang chạy (tham chiếu sống) — `van-ban/luong-xu-ly` NV-09 |
| Widget trang chủ | `HOME_WIDGET` (+ cấu hình cá nhân ở memcached, không có bảng) | `he-thong` NV-16 |

## 6. Đa ngôn ngữ, log, bảo mật

- Nhãn màn hình: `web-spring/src/main/resources/com/viettel/resources/multiLanguage/common_voffice_vi.properties` (unicode-escape, ~10.600 key). Các map `voffice.appConstants.*` ở đây chính là **danh sách trạng thái hiển thị** — nguồn tốt để hiểu nghiệp vụ (đã trích ra `_tools/out/status-maps.txt`).
- BE gen-2 message: `messages_vi.properties`, `core_vi.properties`.
- Log web: `LoggerUtil.writeLog(loggerInfo, ACT_START/ACT_ERROR, ErrorCode, ...)`; BE gen-1: `LogUtils.writeLog(request, ROOT_ACTION, ...)`; gen-2: `@Log4j2`.
- **Đăng nhập** (chi tiết `he-thong` NV-01, NV-02): web `LoginController` (form) + bộ lọc `VNeIDFilter` (`*.zul`) → BE gen-2 `/Authentication/Login`, `LoginSSO`, `LoginVNEID`, `LoginEcabinet`, `LoginOTP`, `LoginFromSSO`, `refresh-token`; BE cấp JWT, lưu phiên `USER_TOKENS`; web giữ JWT trong `serviceConnection` của HttpSession. Mật khẩu form do **dịch vụ SSO** kiểm (một số kênh khác dùng `VHR_EMPLOYEE.PASSWORD` — `he-thong/dac-thu.md` bẫy 2). Bộ `/Authenticate/*` gen-1 là đăng nhập cũ.
- BE auth: JWT stateless (`WebSecurityConfig`, Spring Security 6), mọi endpoint cần token trừ danh sách bỏ qua `jwt.ignore-apis` — so khớp **"chứa chuỗi"** không phân biệt hoa thường (`tich-hop/dac-thu.md` bẫy 6).
- **Quyền**: BE **không kiểm người gọi** có được làm thao tác đó không — quyền nằm ở tầng hiển thị nút trên web + menu (thiết kế chung, đã xác nhận; `_chung/huong-dan-ra-soat-nghiep-vu.md`). Ngoại lệ đáng chú ý: BE gen-1 **nhiệm vụ** có kiểm quyền theo từng nhiệm vụ ở các thao tác ghi chính (`nhiem-vu` mục 1.4; ngoại lệ trong ngoại lệ ở `nhiem-vu/dac-thu.md` L1–L3). (sửa 2026-10-02)
- Tài liệu API: Swagger tại `/ServiceMobile_V02/resources/swagger-ui.html` khi BE chạy.

## 7. Bẫy toàn cục

1. **`Text` ≠ `Document`**: `TEXT`/`TextEntity`/`textAction` = văn bản **đang soạn/trình ký** (chưa ban hành); `DOCUMENT`/`DocumentAction` = văn bản **đã có số** (đến hoặc đi đã ban hành). Ban hành = tạo bản ghi DOCUMENT từ TEXT. Xem `thuat-ngu.md`.
2. **Màn hình chết**: zul trỏ tới VM đã bị xóa (vd các popup con `documentDraft/file/*`, `documentDraft_viewDetail.zul`, `signUsbToken.zul`… trỏ `vm.admin.requisition.*`). Đừng lấy chúng làm mẫu; danh sách có nhãn ☠ trong `ban-do.md` từng phân hệ. (sửa 2026-09-30: màn chính `documentDraft/documentDraft.zul` → `vm.documentDraft.DocumentDraftVM` **còn sống**, là màn Dự thảo của menu XỬ LÝ CÔNG VIỆC — `web-spring/src/main/webapp/view/voffice/documentDraft/documentDraft.zul:7`.)
3. `merge/` ở root workspace là **bản sao mã nguồn** (trùng file với `backend2.0`…), không liên quan migrate dữ liệu — không phải nguồn sự thật, không sửa (sửa chéo 2026-10-02 theo `van-ban/lien-thong` mục 1.5).
4. Tên gọi trùng lặp: `DocumentController` tồn tại ở cả `voffice/controler` (gen-1 logic) và có `DocController`, `DocInController`, `DocumentInController` ở gen-2. Luôn nêu **package đầy đủ** khi hướng dẫn.
5. `controler` (thiếu chữ l) là tên package thật của gen-1 — không phải lỗi gõ khi bạn thấy trong tài liệu.

Bẫy xuyên phân hệ phát hiện trong đợt viết lại 2026-09-29 → 2026-10-02 (chi tiết ở `dac-thu.md` từng phân hệ):

6. **Quyền chỉ ở tầng hiển thị.** BE không kiểm người gọi (thiết kế chung, đã xác nhận) — đừng giả định endpoint tự chặn; điều kiện quyền mới phải đặt ở VM (và cân nhắc BE nếu có kênh mobile / ứng dụng ngoài). Ngoại lệ: BE gen-1 nhiệm vụ có kiểm quyền theo nhiệm vụ (`nhiem-vu` 1.4), nhưng màn "Nhiệm vụ chờ phê duyệt" thì không (`nhiem-vu/dac-thu.md` L1). Khóa tài khoản chỉ chặn ở web, kênh token BE vẫn vào được (`he-thong/dac-thu.md` bẫy 4).
7. **Web ghi thẳng DB qua facade legacy** ở họp, quản trị hệ thống, kiến nghị, `NOTICE`, KPI đơn vị (mục 3) — nhiều nghiệp vụ có **2–3 bản** (web legacy, BE gen-1, BE gen-2) chạy cho các kênh khác nhau; sửa một bản là lệch (vd. `hop` NV-17 "bản thứ ba của cùng nghiệp vụ").
8. **Comment cột DB nhiều chỗ ngược / lệch code** — tin code, không tin comment: `CATEGORY_COMMON.DEL_FLAG` (`he-thong/dac-thu.md` bẫy 15), `BRIEF_TYPE` (`ho-so-cong-viec/dac-thu.md` B6), `TASK_RECEIVER.STATUS` (`cong-viec` mục 3 đầu), `REP_IN.STATUS` (`kpi-danh-gia` mục 3 cụm A), `SMS_MASTER.SMS_TYPE` có giá trị ngoài comment (LNV NV-13). DB DEV gần như **không có FK** — quan hệ ở mục 5 các bài là quan hệ logic từ JOIN / entity.
9. **Mã đơn vị / tham số / quy tắc kế thừa Viettel cũ** (148842, 148844, `VIG` / ban giám đốc tập đoàn, ERP_SAP, ViettelPay, vContract…) ghi cứng trong code hoặc tham số nhưng **không có trên DB Khánh Hòa** → nhánh đó không bao giờ chạy (`hop/dac-thu.md` bẫy 6, `nhiem-vu/dac-thu.md` bẫy 11, `he-thong/dac-thu.md` L23, `cong-viec/dac-thu.md` L25, `van-ban/chuyen-van-ban/dac-thu.md` bẫy 4). Cách ghi tri thức cho các nhánh này đang chờ quyết định (`_chung/cau-hoi-dot-2026-10.md` A4).
10. **Giá trị trạng thái: dùng số thật trong bài, không đoán từ tên hằng.** Hằng trạng thái lệch giữa các bản sao web / BE (`xu-ly-cong-viec/dac-thu.md` bẫy 8); **mã lọc / mã hộp trùng số với trạng thái** (hộp văn bản đến 18…30 ≠ `STATUS` 0…7 — VBĐ NV-01; `replyStatus` 4/5/6 của nhắc việc là mã lọc — `lich-nhac-viec/dac-thu.md` bẫy 2); enum có giá trị không bao giờ được gán (`TEXT.STATE = 5`).
11. **Tên lớp / file gây nhầm**: `solrSearch*` thực chất gọi Elasticsearch; `LookupUtil.getPopupPermision` không phải kiểm quyền; `DocumentProcessTermBusiness` phục vụ **hai** cấu hình khác nhau — hạn xử lý (`DOCUMENT_REQUEST_CONFIG`, HT NV-15) và tự chuyển sau tiếp nhận (CVB NV-06); `documentHandover/documentBook.zul` là báo cáo sổ (SVB NV-11); `SysOrgMenuVM` (tên "menu") là thể loại văn bản theo đơn vị (QLC NV-12); `ReminderReply` web khai `@Table REMINDER_REPLIES` sai tên (LNV mục 6).
12. **Phân loại phân hệ trong `ban-do.md` có chỗ nhầm** (regex `mission` khớp `permission`, `brief` khớp `SignBriefcase`…) — tin mục 1.1 "KHÔNG gồm" của bài; danh sách đề xuất sửa `_tools/domains.py` ở `_chung/cau-hoi-dot-2026-10.md` A1.
13. **Nhiều việc chạy ở tiến trình ngoài repo** (gửi SMS, gửi / nhận trục liên thông, đánh chỉ mục Elasticsearch, đồng bộ hai site, nộp hồ sơ số hóa) — code chỉ ghi bảng hàng đợi / tín hiệu; đừng tìm "chỗ gửi" trong repo (mục 8).
14. **Lỗi bảo mật chỉ ghi nhận ở `dac-thu.md` từng phân hệ** (mục "lỗi hệ thống — ghi nhận"), không chép sang tri thức chung; việc tổng hợp riêng đang chờ quyết định (`_chung/cau-hoi-dot-2026-10.md` A5).

## 8. Hạ tầng và dịch vụ ngoài (tóm tắt — chi tiết ở `tich-hop`)

| Thứ | Hiện trạng | Xem |
|---|---|---|
| Tìm kiếm | **Elasticsearch** (`SYSTEM_PARAMETER` `ELASTICSEARCH_8X` / `ELASTICSEARCH2`): văn bản đã công bố (`documentpublished`), danh sách văn bản, "tìm kiếm tất cả", chọn người / đơn vị, lịch sử luồng; **Solr đã bỏ** (tên `solrSearch` còn). Hệ thống không tự ghi dữ liệu nghiệp vụ vào ES — chỉ ghi **bảng tín hiệu** `ELASTIC_DOCUMENT_PUBLIC` / `_PRIVATE` để dịch vụ ngoài đánh chỉ mục lại | `tich-hop` NV-10, QLC NV-02 |
| Log tập trung | `LogCenter` → chỉ mục `log_center-yyyy.MM.dd` (cũng là nguồn đếm lượt đăng nhập cho báo cáo sử dụng) | `tich-hop` NV-10, `kpi-danh-gia` NV-22 |
| SMS | Code chỉ **ghi hàng đợi** `MESSAGE` (gen-1) / `SMS_MASTER` (gen-1, gen-2 họp, web) sau khi kiểm chặn `shouldSendSms`; **không có code gửi** — cổng SMS ngoài repo đọc bảng; trên DB DEV không có cổng lấy tin đi | LNV NV-13 |
| Thông báo | chuông `NOTIFICATION` (gen-1 `NotificationAction`); đẩy mobile qua thiết bị `USER_DEVICE` (FCM) | LNV NV-11, `tich-hop` NV-11 |
| File | **Không có MinIO / S3**: file lưu trên **thư mục đĩa**, DB giữ đường dẫn tương đối + tên khóa `storage_*` (thư mục gốc lấy từ cấu hình) | `tich-hop` NV-13 |
| Hai site | Khóa `vps.site` = `public` (Internet) / `private` (nội bộ); ký SIM CA chỉ ở site công khai; dải `EXT_DOC_ID`; dữ liệu đồng bộ giữa hai site bằng trigger `VO_SOURCE_*` + cột `VO_VERSION` / `VO_SOURCE` / `VO_LAST_UPDATED` (bảng mới đều có) | `tich-hop` NV-13, KS NV-01 BR-02 |
| Cache | Redis (`spring.data.redis.*` — rate limit, phiên WOPI, OTP…), memcached (cấu hình widget cá nhân, chế độ trang chủ) | `he-thong` NV-14, NV-16 |
| Soạn thảo trực tuyến | WOPI (`/wopi/files`, `ONLINE_EDITOR_CONFIG`) | `tich-hop` NV-09 |
| Đăng nhập ngoài | SSO tỉnh (ticket) và VNeID (OAuth2 + PKCE) — connector | `tich-hop` NV-08, `he-thong` NV-02 |
| Ứng dụng ngoài gọi vào | `/ext-*`, đăng ký ở `EXT_APP` / `EXT_SHARE_CONFIG` (Thư viện điện tử, KNTC…) | `tich-hop` NV-01 … NV-05 |
| Trục liên thông | chỉ ghi gói tin "hộp thư đi"; tiến trình ngoài gửi / nhận | `van-ban/lien-thong` NV-01 |
