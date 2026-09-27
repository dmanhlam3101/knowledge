# Quy ước code (rút từ code hiện có — làm theo để code mới "giống" code cũ)

## BE gen-2 (`com.viettel.office`) — chuẩn cho code mới

| Lớp | Package | Đặt tên | Ghi chú |
|---|---|---|---|
| Controller | `controller` | `XxxController`, `@RestController @RequestMapping("/api/xxx-yyy")` (kebab-case) hoặc tên ngắn như `/reminders` | `@RequiredArgsConstructor` + `@FieldDefaults(level = PRIVATE, makeFinal = true)`; method `@PostMapping(value="/action", produces=APPLICATION_JSON_VALUE)`; hầu hết là **POST** kể cả đọc dữ liệu |
| Service | `services/XxxService` (interface) + `services/impl/XxxServiceImpl` | `@Service @RequiredArgsConstructor @Log4j2` | Ghi dữ liệu: `@Transactional(rollbackFor = Exception.class)`; đọc: `@Transactional(readOnly = true)` |
| Repository JPA | `repositories/jpa/XxxRepositoryJPA extends JpaRepository<XxxEntity, Long>` | `@Query` JPQL với `new ...DTO(...)` projection; `@Modifying` cho update | |
| Repository SQL tay | `repositories/XxxRepository` (interface) + `repositories/impl/XxxRepositoryImpl` | `@Repository @RequiredArgsConstructor`, dùng `BaseRepositoryImpl.getListDataAndCount / getListData / getFirstData / executeSqlDatabase` với `HashMap<String,Object> params` và text block SQL | Dùng khi query phức tạp/phân trang nhiều join |
| `getListData` native SQL | `BaseRepositoryImpl.getListData(sql, params, ..., Xxx.class)` | Map **theo tên cột = tên field** (không dùng `@Column`): **không** `SELECT o.*` — cột có `_` (`SYS_ORGANIZATION_ID`, `ORG_PARENT_ID`…) sẽ null; phải alias `o.sys_organization_id AS sysOrganizationId` (mẫu: `VhrOrgRepositoryImpl.findOrganizationFromChildToParent`) | Bẫy đã dính ở `getListOrgHasIdentifierCode` 2026-09 |
| Entity | `entities/XxxEntity` | `@Data @NoArgsConstructor @FieldDefaults(PRIVATE) @Entity @Table(name="XXX")`; id `@GeneratedValue(SEQUENCE)` + `@SequenceGenerator(sequenceName="SEQ_XXX", allocationSize=1)` | Cột UPPER_SNAKE, field camelCase; luôn có `DEL_FLAG`, `CREATED_AT/BY`, `UPDATED_AT/BY` |
| DTO | `dto/request/<domain>/XxxRequestDTO`, `dto/response/<domain>/XxxResponseDTO`, projection interface trong `dto/response/<domain>/projection` | `@Data` | Không trả entity ra ngoài controller |
| Response | `ResponseUtils.getResponseEntity(obj)` → `ResultResponse{ result: BaseResponse{ mess{errorCode,message}, data, status, timestamp } }` | Web đọc `root.data` hoặc `root.result.data` | Lỗi nghiệp vụ: `ResponseUtils.getResponseEntity(ErrorApp, obj)` hoặc throw exception custom (vd `ReminderPromulgationException`) — `GlobalExceptionHandler` xử lý |
| User hiện tại | `CoreUtils.getUserId()` (employeeId từ JWT) | Không nhận userId từ client cho thao tác ghi | |
| SQL migration | `backend2.0/backendvoffice/sql/DDMMYYYY_mo_ta.sql` | Tạo SEQUENCE + TABLE + comment cột; dữ liệu SYS_MENU nếu có màn hình mới | Chưa có Flyway/Liquibase — chạy tay theo môi trường ❓ |

## BE gen-1 (`com.viettel.voffice`) — chỉ khi sửa cái đang có

- Endpoint: `@PostMapping(value="/x", consumes="application/x-www-form-urlencoded", produces="application/json")` nhận `@RequestParam String data, @RequestParam String isSecurity`; ghi log `LogUtils.writeLog(request, ROOT_ACTION, Constants.ACT_START, ...)`; ủy quyền sang `controler/*Controller`.
- Logic trong `controler/*Controller` (`@Service`) tự parse JSON (`CommonFunction.getItemInJson`), tự ghép JSON trả về. Hàm rất dài; khi sửa **thêm hàm mới** thay vì đổi hàm cũ đang được nhiều màn hình dùng.
- DAO: `database/dao/**/XxxDAO` (`@Service`), SQL string + `CommonDataBaseDaoVO2`. Có biến thể `V2` (ví dụ `updateReadingStatusV2`) là bản tối ưu — ưu tiên bản V2 nếu tồn tại.
- Hằng số nghiệp vụ trong `constants/Constants.java` (~3.000 dòng) và enum `TextStateConstants`, `TextProcessStateConstants`.

## Web (`web-spring`)

| Việc | Quy ước |
|---|---|
| Màn hình | `src/main/webapp/view/voffice/<phanhe>/<ten>.zul`; popup/add/search tách file `_add`, `_search`, `_viewDetail`; header dùng `<include src="/view/widgets/menuPathLabel.zul">` + `toolbarButton.zul` |
| ViewModel | `com.viettel.voffice.vm.<phanhe>.XxxVM extends SecurityVM<Entity>`; `@Init(superclass = true) @AfterCompose(superclass = true)`; `@Wire("#id")` cho component; `@Command`/`@NotifyChange` chuẩn ZK MVVM |
| Gọi BE | Tạo `com.voffice.service.business.XxxBusiness extends Business`, mỗi hàm = 1 endpoint, parse JSON bằng Gson; VM khởi tạo `new XxxBusiness(serviceConnection)` (lazy trong `@Init` hoặc getter) |
| Model phía web | `com.voffice.service.entity.XxxEntity` (bản sao DTO của BE) hoặc `com.viettel.voffice.dto.<phanhe>.*DTO` | Không dùng entity JPA của web (`com.viettel.voffice.entity`) cho tính năng mới |
| Nhãn | Key trong `common_voffice_vi.properties` (+ `_en`), dạng `voffice.<phanhe>.label.xxx`; dùng `${labels.voffice...}` trong zul hoặc `CommonResourcesUtil.getLabel(...)` | File là unicode-escape (`\uXXXX`), sửa bằng IDE hỗ trợ hoặc script |
| Thông báo | `NotificationCenter` / `CustomMessageBox` | |
| Popup chọn | `LookupUtil.showLookup(...)`, widget trong `view/widgets/` + `com.viettel.voffice.widget.*` | Có sẵn lookup đơn vị, người dùng, văn bản… — tìm trong `_chung/ban-do.md` trước khi viết mới |
| Reload màn khác | `EventQueues.lookup(AppConstants.EVENT_QUEUE.*)` | |
| Quyền | `screenName` + `LookupUtil.getPopupPermision(screenName, eventName)`; menu & quyền cấu hình trong DB | |

## DB (Oracle)

- **`VHR_ORG.ORG_LEVEL` không tin được** (có bản ghi `ORG_LEVEL = 2` nhưng `PATH` sâu 4–5 cấp). Cấp/độ sâu/quan hệ cha-con luôn suy từ `PATH` (`/1/2/3/`): độ sâu = số `/` − 1, con cháu = `PATH LIKE 'p%'`. Phát hiện 2026-09 khi làm cây chuyển VB đi.

- Bảng/cột UPPER_SNAKE_CASE, `NVARCHAR2` cho tiếng Việt, id `NUMBER(19,0)` từ `SEQ_<TABLE>`.
- Xóa mềm `DEL_FLAG` (0/1). Truy vấn luôn lọc `DEL_FLAG = 0`.
- Audit: `CREATED_AT/CREATED_BY/UPDATED_AT/UPDATED_BY` (gen-2) hoặc `CREATED_DATE/CREATED_BY/UPDATED_DATE/UPDATED_BY` (bảng cũ).
- Quan hệ văn bản ↔ nghiệp vụ khác thường qua bảng `*_RELATION` / `*_DOCUMENT_RELATION` với `TEXT_ID` (dự thảo) **hoặc** `DOCUMENT_ID` (đã ban hành) — một trong hai null.

## Git / build

- Web: Maven, `mvnw`, Java 8, đóng gói WAR/Jar chạy Tomcat nhúng ❓; Jenkinsfile.groovy; Dockerfile.
- BE: Maven, Java 21, Spring Boot 3.5, port dev 8075 / prod 8080, context `/ServiceMobile_V02/resources`; `docker/`, `k8s/`, `postman/` có sẵn collection để thử API.
- Hai repo git riêng; root workspace không phải repo.
