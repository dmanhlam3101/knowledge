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
                              Oracle DB (sequence SEQ_*, DEL_FLAG, NVARCHAR2)
                              + Elasticsearch/Solr (tìm kiếm văn bản), Redis (cache), ELS logs
```

Ngoài ra `backend2.0/voffice-lib` (`voffice-core`, `voffice-gencode`) là lib dùng chung / sinh code cho BE gen-2.

### Số liệu (2026-09, từ `_tools/scan.py`)

| | Web | BE |
|---|---|---|
| Màn hình `.zul` có VM | 626 (49 ☠ trỏ VM không tồn tại) | — |
| ViewModel | 556 | — |
| `*Business` (client gọi BE) | 79 class / 790 hàm → 748 nối được endpoint | — |
| Facade legacy / JPA DAO / entity web | 44 / 85 / 137 | — |
| Controller / endpoint | — | 145 / 1.733 (gen-1 ≈ 70, gen-2 ≈ 75) |
| Logic gen-1 / DAO gen-1 | — | 80 / 156 |
| Service gen-2 / Repository / Entity | — | 206 / 198 / 192 |

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
- Entity web (`com.viettel.voffice.entity`, `com.viettel.vps.entity`) trùng bảng với entity BE — **hai bộ mapping cho cùng bảng**, sửa schema phải sửa cả hai nếu bảng đó còn được web đọc.
- Nguyên tắc: tính năng mới → không thêm facade/DAO mới ở web; nếu cần dữ liệu, thêm endpoint BE gen-2 rồi thêm hàm vào `*Business`. Xem [`cach-lam-chuan/sua-tinh-nang-cu.md`](cach-lam-chuan/sua-tinh-nang-cu.md).

## 4. BE gen-1 vs gen-2 — chọn cái nào

| | gen-1 `com.viettel.voffice` | gen-2 `com.viettel.office` |
|---|---|---|
| Endpoint | `/textAction/getTextDetail`, `/DocumentAction/...`, `/Meeting/...` (tên tự do, PascalCase lẫn camelCase) | `/api/<kebab-case>/...`, `/reminders/...` |
| Vào/ra | `@RequestParam String data` (JSON trong form-urlencoded) + `isSecurity`, trả `String` JSON tự ghép | `@RequestBody XxxRequestDTO`, trả `ResultResponse<T>` |
| Logic | `controler/*Controller` (@Service) — file rất lớn (TextController hàng nghìn dòng, 20+ DAO) | `services/*ServiceImpl` + `@Transactional(rollbackFor = Exception.class)` |
| Data | `database/dao/*DAO` SQL thuần, `database/entity/*` là POJO/filter (không @Entity) | `repositories/jpa/*RepositoryJPA extends JpaRepository`, `@Query` JPQL/native; `entities/*Entity` @Entity/@Table |
| Ai gọi | Web (đa số 790 hàm), mobile | Web (reminder, doc-in mới...), mobile, ứng dụng ngoài (`/ext-*`) |
| Khi nào dùng | **Sửa** tính năng cũ đang ở đó | **Thêm** tính năng/endpoint mới; hoặc khi sửa gen-1 quá rủi ro thì tạo endpoint gen-2 mới và chuyển web sang |

Tính năng mới gần nhất làm hoàn toàn theo gen-2: **Nhắc việc** (`ReminderController` → `ReminderServiceImpl` → `ReminderRepositoryJPA` → `REMINDER*`), web `vm/reminder/*` + `ReminderBusiness`. Đây là mẫu chuẩn: [`cach-lam-chuan/them-tinh-nang-moi.md`](cach-lam-chuan/them-tinh-nang-moi.md).

## 5. Những thứ nằm trong DB chứ không trong code

| Thứ | Ở đâu | Hệ quả |
|---|---|---|
| Menu web | bảng `SYS_MENU` (URL trỏ thẳng tới file `.zul`, ví dụ `/view/voffice/document/...zul`) | Thêm màn hình mới = thêm dòng SYS_MENU bằng SQL (xem `backend2.0/backendvoffice/sql/19122025_add_row_sys_menu.sql`) |
| Trạng thái/loại văn bản, họp... | `CODE_MASTER` (web đọc qua key `code.doc.status`, `code.doc.state`, `code.meeting.status`… trong `AppConstants`) | Nhiều trạng thái là **dữ liệu**, không phải enum; đối chiếu DB trước khi hard-code |
| Quyền theo màn hình/thao tác | `SYS_ROLE`, `SYS_OPERATION`, `SYS_RESOURCE` (vps) + `LookupUtil.getPopupPermision(screenName, eventName)` | Nút bấm mới có thể cần cấu hình quyền, không chỉ code |
| Tham số hệ thống | `SYSTEM_PARAMETER` / `CONFIG_PARAMETER` | Hạn xử lý, bật/tắt tính năng, URL tích hợp |
| Luồng ký | bảng `FLOW*`, `NODE*` (gen-2 `FlowEntity`, `NodeEntity`, `NodeToNodeEntity`…) | Luồng là cấu hình, không hard-code bước ký |

## 6. Đa ngôn ngữ, log, bảo mật

- Nhãn màn hình: `web-spring/src/main/resources/com/viettel/resources/multiLanguage/common_voffice_vi.properties` (unicode-escape, ~10.600 key). Các map `voffice.appConstants.*` ở đây chính là **danh sách trạng thái hiển thị** — nguồn tốt để hiểu nghiệp vụ (đã trích ra `_tools/out/status-maps.txt`).
- BE gen-2 message: `messages_vi.properties`, `core_vi.properties`.
- Log web: `LoggerUtil.writeLog(loggerInfo, ACT_START/ACT_ERROR, ErrorCode, ...)`; BE gen-1: `LogUtils.writeLog(request, ROOT_ACTION, ...)`; gen-2: `@Log4j2`.
- BE auth: JWT stateless (`WebSecurityConfig`, Spring Security 6), mọi endpoint cần token trừ danh sách ignore (`jwtIgnoreConfig`); login qua `/Authentication/Login|LoginSSO|LoginVNEID|LoginEcabinet`.
- Tài liệu API: Swagger tại `/ServiceMobile_V02/resources/swagger-ui.html` khi BE chạy.

## 7. Bẫy toàn cục

1. **`Text` ≠ `Document`**: `TEXT`/`TextEntity`/`textAction` = văn bản **đang soạn/trình ký** (chưa ban hành); `DOCUMENT`/`DocumentAction` = văn bản **đã có số** (đến hoặc đi đã ban hành). Ban hành = tạo bản ghi DOCUMENT từ TEXT. Xem `thuat-ngu.md`.
2. **49 màn hình chết**: zul trỏ tới VM đã bị xóa (cả bộ `documentDraft/*` trỏ `vm.admin.requisition.*`). Đừng lấy chúng làm mẫu; danh sách có nhãn ☠ trong `ban-do.md` từng phân hệ.
3. `merge/` ở root workspace là bản gộp cũ — không phải nguồn sự thật. ❓ cần xác nhận mục đích.
4. Tên gọi trùng lặp: `DocumentController` tồn tại ở cả `voffice/controler` (gen-1 logic) và có `DocController`, `DocInController`, `DocumentInController` ở gen-2. Luôn nêu **package đầy đủ** khi hướng dẫn.
5. `controler` (thiếu chữ l) là tên package thật của gen-1 — không phải lỗi gõ khi bạn thấy trong tài liệu.
