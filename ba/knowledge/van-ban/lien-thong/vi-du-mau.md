# Liên thông văn bản — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phân hệ này là mẫu cho **trao đổi dữ liệu với hệ thống ngoài theo kiểu "hộp thư đi + webhook"**: hệ thống chỉ ghi gói tin vào bảng, tiến trình ngoài gửi đi; chiều về đi qua webhook có xác thực. Khi copy, tránh các điểm đã ghi ở `dac-thu.md` (nêu cuối từng mẫu).

## Mẫu 1 — Webhook gen-2 nhận dữ liệu từ hệ thống ngoài, idempotent: `POST /api/hook/send-document`

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Controller | `VOC:20-49` — `@RequestMapping(Constants.REQUEST_MAPPING_PREFIX + "/hook")`, mỗi endpoint một dòng gọi service, trả `ResponseUtils.getResponseEntity` | Endpoint mỏng; DTO riêng cho gói nhận (`BE2/dto/request/hook/SendDocumentDTO.java:13-59`: người gửi, danh sách nơi nhận có `tenantCode` + mã định danh + khóa dòng bên gửi `docInId`, file theo đường dẫn) |
| Xác thực | không thêm vào `jwt.ignore-apis` (`APP:433`); nhận diện tài khoản hệ thống bằng mã cấu hình (`FC:2491-2494`) | Webhook vẫn đi qua JWT; tài khoản kỹ thuật riêng |
| Service — kiểm đầu vào | `VOS:68-97`: thiếu nơi nhận / người gửi → `InvalidInputException`; không có nơi nhận thuộc hệ thống này → trả 0 (không lỗi) | Phân biệt "dữ liệu sai" (lỗi) với "không phải của tôi" (bỏ qua) |
| Service — idempotent | `VOS:99-131`: tìm bản ghi theo **khóa ngoài** (`DOCUMENT.DOC_ID`), có thì dùng lại; bỏ các dòng con đã có cùng khóa dòng ngoài (`DOC_IN_ID`) | Hub có thể gửi lại — không tạo trùng |
| Service — ánh xạ danh mục | `VOS:93`, `200-219`: mã định danh → đơn vị (`VORJ:386-392`, lọc hiệu lực); hình thức / độ khẩn khớp **theo tên**, không khớp thì giá trị mặc định | Ánh xạ mềm khi hai hệ thống dùng danh mục khác nhau |
| Service — file | `VOS:236-280`: tạo thư mục đích một lần rồi xử lý song song từng file (đọc → mã hóa DES → ghi kho), file lỗi bỏ qua và ghi log | Chép file theo lô an toàn |
| Ghi nghiệp vụ | dùng lại DAO gen-1 `DDAO.insert`, `DDAO.sendDocumentToGroup` với người gửi ảo (`VOS:133-140`, `232`) | Tái dùng luồng "chuyển văn bản cho đơn vị" thay vì viết lại |

**Không copy**: `Collectors.toMap` không hàm gộp trên mã có thể trùng (`dac-thu.md` L11); tra khóa ngoài ở hai bảng khác nhau giữa các webhook cùng nhóm (L10); không có `@Transactional` bao cả luồng tạo văn bản + dòng nhận (`VOS:68-142`).

## Mẫu 2 — Ghi gói tin "hộp thư đi" cho hệ thống ngoài + migration bảng có đồng bộ: VOConnect `INTERNAL_DOC_*`

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Migration | `SQL/20251009_alter_truc_lien_thong_noi_bo.sql:52-99` (bảng cha gói tin + sequence `INCREMENT BY 2`), `:82-92` / `:135-144` (supplemental log, quyền `VOFFICE_DBZ_ROLE`, trigger `VO_SOURCE_*` đánh dấu nguồn / phiên bản), `:96-99` (thêm cột khóa liên hệ thống vào bảng nghiệp vụ cũ) | Bảng outbox được hub đọc bằng bắt thay đổi; cột `VO_VERSION`, `VO_SOURCE`, `VO_LAST_UPDATED` |
| Migration có comment cột | `SQL/20251105_add_table_internal_communication_axis_mission.sql:27-37`, `77-85`, `122-124` | `COMMENT ON COLUMN` đủ ý nghĩa từng giá trị trạng thái (mẫu tốt hơn bảng `INTERNAL_DOC_*` không có comment) |
| Entity | `BE2/entities/InternalDocSendXmlEntity.java`, `InternalDocDetailEntity.java` (comment ý nghĩa giá trị ngay cạnh trường) | Builder Lombok + comment giá trị |
| Hằng | `C1:2722-2736` (`INTERNAL_DOC_SEND_XML.TYPE`, `DOC_TYPE`) | Gom mã loại gói một chỗ |
| Service | `IDS:43-80` (gói "thêm mới" + một dòng chi tiết mỗi nơi nhận), `88-145` (gói theo sự kiện, nơi nhận lấy từ truy vấn dòng đang hiệu lực — `VORJ:405-445`), `147-186` (gói trạng thái ngược về bên gửi), `188-190` (khóa liên hệ thống) | Một service duy nhất sinh mọi loại gói; điểm gọi chỉ một dòng |
| Chống vòng lặp | `IDS:45-47`, `151-153` (`FC.isHubProcessor`) | Không sinh gói khi thao tác do chính hub gọi vào |
| Điểm gọi | `DDAO:9700-9721`, `DC:785-789`, `1016-1020`, `6087-6091`, `11104-11106`, `DISI:473-476`, `1013-1015` | Gọi **sau** khi ghi nghiệp vụ thành công |

**Không copy**: gói tin ghi trong cùng luồng không bắt lỗi riêng (`dac-thu.md` bẫy 2, `nghiep-vu.md` BR-26); thiếu webhook nhận cho một số loại gói (BR-28) — khi thêm loại gói phải thêm cả phía nhận.

## Mẫu 3 — Màn theo dõi gửi / nhận hai tab + lịch sử trạng thái nhiều dòng (gen-1): **Văn bản liên thông**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/document/goverment/connectDocument.zul:44-52` (hai tab bằng nút + `changeTab`), `:643-670` (nút thao tác theo trạng thái dòng), chi tiết `connectDocument_detail.zul:795-850` (danh sách nơi nhận có chọn nhiều + thu hồi hàng loạt) | Tab đến / đi trên cùng lưới |
| VM | `CDVM:868-900` (đổi tab → đổi tham số + tiêu đề cột), `1555-1641` (chọn nhiều có giữ lựa chọn qua trang), `1804-1881` (quy đổi nhiều cột trạng thái → một nhãn + màu) | Quy đổi trạng thái ở một hàm |
| Business | `CDB:21-103` — `serveProcessing("connectDocumentAction.xxx", params)` | Khóa `a.b` → URL `/a/b` |
| BE | `CDC:43-242` → `CDD.getListConnectDocument` :57-495 (SQL động hai nhánh theo loại), `getListConnectDocOutDetail` :898-1025 (lấy **dòng mới nhất theo cặp** bằng `ROW_NUMBER() OVER (PARTITION BY …)`, đếm tổng một câu), `addStateConnectDocument` :1072-1178 (đổi trạng thái = tắt dòng hiện hành + chèn dòng mới) | Lưu lịch sử trạng thái thay vì UPDATE đè |

**Không copy**: `ORDER BY` ghép chuỗi từ client (`dac-thu.md` L2); trả thành công khi không ghi gì (L3); logic nút nhân bản sang màn khác (bẫy 8) — đặt hàm kiểm vào lớp dùng chung.

## Mẫu 4 — Danh mục dạng cây có CRUD + popup chọn dùng lại ở màn khác: **Danh mục đơn vị liên thông**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `VPS/sysConnectVHR/sysConnectVHR.zul` (cây + include `connectVHR_search.zul` / `connectVHR_add.zul`) | Bố cục cây trái, lưới phải |
| VM | `CVVM:66-117` (ẩn thao tác nếu không phải quản trị, dựng cây gốc ảo `SysConnectVHRTreeModel`), `119-147` (bấm nút cây → lọc lưới), `149-206` (chọn đơn vị cha bằng popup), `208-226` (kiểm mã trùng trước khi lưu), `374-405` (insert / update / delete override) | Cây + lưới trên `SecurityVM` |
| Popup chọn | `CVLVM` (dùng trong popup chuyển văn bản; cờ `ARG_VIEW_FROM_ADMIN_MENU` đổi điều kiện lọc — :540-557) | Một popup phục vụ cả màn quản trị và màn nghiệp vụ |
| BE | `CVA:40-117` → `CVC` → `CVD.getListConnectVHR` :44-292 (tìm không dấu `nlssort binary_ai`, tìm chính xác khi đặt trong ngoặc kép), `deleteConnectVHR` :388-407 (xóa mềm cả nhánh bằng `CONNECT BY`) | Tìm kiếm không dấu / chính xác; xóa mềm theo cây |

**Không copy**: `PATH` / `PATH_NAME` không được tính (`dac-thu.md` L15); kiểm trùng mã chỉ ở web (L1); cờ "đồng bộ" ghi thẳng `SYSTEM_PARAMETER` mà không có nơi đọc trong repo (NV-02). Lưu ý quy mô: DB DEV `CONNECT_VHR` ngày 2026-10-01 có 123.265 dòng (danh mục do tiến trình ngoài đồng bộ) — popup chọn phải phân trang phía server như `CVLVM` (`isPagingServer`), không nạp cả cây.
