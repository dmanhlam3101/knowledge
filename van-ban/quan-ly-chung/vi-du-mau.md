# Quản lý chung văn bản — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Khi copy, tránh các điểm đã ghi ở `dac-thu.md` (nêu ở cuối từng mẫu).

## Mẫu 1 — Danh mục gen-2 "dùng chung / của đơn vị + cấp cho đơn vị khác", kiểm trùng có mã lỗi để web hỏi tiếp: **Thể loại văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/document_type/document_type.zul` (include `document_type_search.zul` + `document_type_add.zul` — :27, :31) | Một zul gốc include tìm kiếm + form, ẩn hiện theo `viewState` của `CommonVM` |
| VM | DTVM: mặc định khi thêm (`DTVM:153-179`), quyền hiện nút theo vai trò + đường dẫn đơn vị (`DTVM:317-337`), xử lý mã lỗi 863 / 864 bằng hộp xác nhận rồi gọi API phụ (`DTVM:275-311`) | Hỏi người dùng khi BE trả mã nghiệp vụ, thay vì tự quyết ở BE |
| Business | DTB — khóa `api.document-types.*`, đọc mã lỗi trả về để chọn thông báo (`DTB:119-132`) | Khóa `a.b.c` → URL `/a/b/c` |
| Controller | DTCT (`/api/document-types`, mỗi endpoint vài dòng — `DTCT:23-140`) | Endpoint mỏng |
| Service | DTSI: `createDocumentType` `@Transactional` → kiểm vai trò (`validationAccount` :364-376) → kiểm trùng phân nhánh theo phạm vi (`:391-539`) → lưu cha + tự cấp dòng con cho đơn vị tạo (`:69-96`); xóa mềm có kiểm "đang dùng" ở nhiều bảng (`:304-336`, `:548-555`); cấp / gỡ cấp theo tập đơn vị (`:135-210`) | Khung "kiểm quyền → kiểm trùng → lưu → đồng bộ bảng cấp phát" |
| Repository | `DocumentTypeRepositoryJPA`, `DocumentTypeOrgRepositoryJPA`, tìm kiếm động `DocumentTypeRepositoryImpl.searchDocumentTypeByFilter` (`BE2/repositories/impl/DocumentTypeRepositoryImpl.java:60-182`) | SQL động có phân trang + cột ghép tên đơn vị được cấp |
| Mã lỗi / thông báo | `BE2/utils/ErrorCodeApp.java:25-37`; `backend2.0/backendvoffice/src/main/resources/message_vi.properties:44-47` | Mã lỗi nghiệp vụ riêng + thông báo có tham số `{0}` |

**Không copy**: kiểm vai trò chỉ ở thêm / khóa (thiếu ở sửa / xóa / cấp — `dac-thu.md` L8); nhận phạm vi quản lý từ tham số web; ném `RuntimeException` khi người dùng bấm Hủy; quên xóa cache danh sách (`DictionaryCacheService` không `@CacheEvict` — bẫy 8); hai quy tắc lọc khác nhau cho cùng danh mục.

## Mẫu 2 — Nhật ký thay đổi "trước / sau" dạng JSON chỉ các trường đã đổi + panel lịch sử: **Nhật ký thao tác văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Danh sách trường theo dõi | `BE1/constants/Constants.java:2612-2644` (`FIELDS_LOG.ENTITY_DOCUMENT`) | Khai báo tập trường cần ghi ở một chỗ |
| Service ghi | `DHLSI.saveDocHistory` (`DHLSI:92-204`): so cũ / mới theo danh sách trường, đổi id → tên (`:335-488`), thêm danh sách file thêm / bỏ (`:168-194`), không đổi gì thì không ghi (`:155-161`) | So sánh theo whitelist, lưu JSON `before` / `after` |
| Điểm gọi | `DC:509` (thêm), `DC:870-872` (sửa — có đặt người sửa), `DC:11354` (vào sổ) | Gọi sau khi lưu nghiệp vụ thành công |
| Entity / bảng | `BE2/entities/DocumentHistoryLogEntity.java:16-42` (`JSON_BEFORE_EDIT`, `JSON_AFTER_EDIT` CLOB, sequence) | Bảng log chỉ thêm |
| Đọc | `BE2/controller/DocumentHistoryLogController.java:29-33` → `BE2/repositories/impl/DocumentHistoryLogRepositoryImpl.java:20-48`; web `DHLB:21-50` → `DVDVM:7289-7298` (panel), `DVDVM:7306-7320` + `DLIVM:117-222` (popup tách JSON) | Panel lịch sử trên màn chi tiết |

**Không copy**: quên đặt `CREATED_BY` (`DC:509`; `TextController.java:1828` — L12); popup đọc thuộc tính không có khi mở từ màn khác (NPE `DLIVM:107`); tiêu đề ghi cứng không dấu (`ViewUtil.java:3819-3826`).

## Mẫu 3 — Dữ liệu cá nhân gen-2 nhỏ gọn có "mặc định" (CRUD theo người đăng nhập): **Mẫu ý kiến chuyển văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Controller | `BE2/controller/DocController.java:172-186` (`add-document-template`, `get-document-template-default`, `search-document-template`) | Một endpoint "lưu" dùng cho cả thêm / sửa / xóa mềm |
| Service | `BE2/services/impl/DocServiceImpl.java:1354-1404`: gán `USER_ID` từ phiên (`CoreUtils.getUserId()`), xóa mềm bằng `DEL_FLAG = 1` + ngày xóa, đặt mặc định thì bỏ mặc định các mẫu khác của người đó (`updateIsDefaultByUserId`) | Ràng buộc "một bản mặc định / người" bằng một câu update sau khi lưu |
| Web | `WEB/voffice/vm/document/SelectDocumentTemplateVM.java:78-162` (popup chọn / thêm / sửa), điểm dùng `TransferDocumentVM.java:2122-2133` | Popup chọn trả kết quả về form cha qua `LookupUtil` |

**Không copy**: cập nhật theo id mà không kiểm bản ghi thuộc người đăng nhập (L13) — khi sửa / xóa nên tìm theo `(id, USER_ID)`.

## Mẫu 4 — Màn "theo dõi đơn vị" theo cấu hình người – đơn vị, nạp màn con bằng `include` + attribute: **Theo dõi văn bản đơn vị / Theo dõi văn bản đi đơn vị**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Lấy đơn vị theo dõi | `ISysUser.findSysOrgMappedByUser(user, USER_ORG_MAP.TYPE.ORG_FOLLOW)` (`OFLVM:41-47`; `DKVM:99-130` có sắp xếp và chọn mặc định đơn vị của mình) | Cấu hình người – đơn vị ở `USER_ORG_MAP` theo `TYPE` |
| Không có cấu hình | `DKVM:111-114` + thông báo trên zul `documentKpi.zul:94-100` | Hiện hướng dẫn thay vì màn trống (OFLVM chưa làm) |
| Nạp màn con | `OFLVM:107-123`, `DKVM:257-316`: `includeContent.setAttribute("orgId", …)`, `setAttribute("view", -1)`, `setSrc(...)`; màn con đọc `viewComp.getParent().getAttribute(...)` (`DSSVM:647-661`, `766-772`) | Tái dùng VM danh sách có sẵn cho ngữ cảnh mới |
| BE | `TCT:456-463`, `499-507` — tham số `orgId` thay phạm vi đơn vị văn thư | Một tham số ngữ cảnh ở controller, giữ nguyên DAO |

**Lưu ý khi copy**: VM danh sách dùng chung nhiều màn — mọi cờ ngữ cảnh mới phải mặc định "tắt" để màn cũ không đổi hành vi (bẫy 1, 2); tìm nhanh giữa màn cha / con đi qua `EventQueue` (`OFLVM:67-75`) — đặt tên hàng đợi riêng để không lẫn với màn khác.
