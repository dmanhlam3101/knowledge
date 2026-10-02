# Thư viện, biểu mẫu, tag — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-02). Viết tắt như `nghiep-vu.md`. Phân hệ chủ yếu là code **gen-1 / legacy** — khi làm tính năng mới, ưu tiên mẫu gen-2 ở `lich-nhac-viec/vi-du-mau.md` (nhắc việc); ở đây chỉ lấy những mảnh có ích, và tránh các điểm ghi ở `dac-thu.md` (nêu cuối từng mẫu).

## Mẫu 1 — Danh mục gợi ý / autocomplete gen-2 theo người hoặc đơn vị: **Từ điển tag**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Migration | `SQL/20251012_create_table_tag_dictionary.sql` (bảng + `COMMENT ON` từng cột + sequence + index theo `(ORG_ID, TAG_SCOPE)` và `CREATED_BY` + thêm cột vào bảng cũ) | Khung migration có comment cột đầy đủ |
| Entity | `BE2/entities/TagDictionaryEntity.java:21-64` (`@SequenceGenerator`) | — (thiếu cột `ORG_NAME` — L10) |
| Controller | TDC:27-122 — mỗi endpoint 2–3 dòng, `ResponseUtils.getResponseEntity` | Endpoint mỏng |
| Service | TDSI:32-62 (lấy người dùng bằng `CoreUtils.getUserId()`, xóa mềm `DEL_FLAG` + `DELETED_BY` / `DELETED_DATE`) | Xóa mềm có vết |
| Repository | TDRI:24-66 (`UNION` "của tôi" ∪ "của đơn vị tôi" qua `BaseRepository.getListData` với tham số tên `:orgIds`), :69-87 (điều kiện theo có / không có `orgId`) | Truy vấn gợi ý theo hai phạm vi cá nhân / đơn vị |
| Web Business | TDB:31-57 (`servePostRequest(params, "api.tag-dictionary.get-list-tag-for-searchbox")`, parse `data`) | Khóa `api.a.b` → URL `/api/a/b` |
| Web dùng | ô lọc trên hộp văn bản: `WEB/voffice/vm/document/DocumentPendingProcessingVM.java:12293-12320` (nạp gợi ý, gộp trùng tên bằng `Collectors.toMap(..., (a, b) -> a, LinkedHashMap::new)`, lọc gõ chữ `filterCombobox`) | Combobox gợi ý có lọc khi gõ, không lỗi khi trùng khóa |

Lưu ý dữ liệu: DB DEV ngày 2026-10-02 có ~630 tag còn hiệu lực nhưng 0 văn bản mang tag — kiểm thử phải tự gắn dữ liệu.

**Không copy**: thiếu `DEL_FLAG = 0` ở câu gợi ý (L6); lưu liên kết văn bản – tag bằng **chuỗi tên** thay vì bảng nối (bẫy 6) — tính năng mới nên có bảng nối theo id.

## Mẫu 2 — Popup chọn nhiều giá trị có tạo mới, giới hạn số lượng, trả kết quả về màn cha: **Gán tag văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/widgets/popupInfoHastag.zul` (chosenbox `creatable`), mở bằng `ViewUtil.createLookupHastagDoc` (`WEB/voffice/util/ViewUtil.java:3880-3884`) | Popup lookup chuẩn qua `LookupUtil.showLookup` |
| VM popup | IHD `onSearchHastag` :850-870 (gõ tên mới → thêm vào model + chọn, kiểm tối đa 5 / 40 ký tự), `onSelectHastag` :817-834 (bỏ mục vượt giới hạn), `getInfoTagDoc` :766-792 (trả danh sách qua `Events.postEvent(new SearchEvent(viewComp, null, list))`, kèm phần tử đánh dấu "đã đổi") | Trả kết quả popup bằng `SearchEvent`; chỉ ghi khi có thay đổi |
| Màn cha | DVDVM `doHastagDocument` :7828-7930 (nhận kết quả, nối chuỗi, gọi đúng API theo vai trò / loại văn bản, thông báo, cờ tải lại danh sách) | Một hàm điều phối theo ngữ cảnh |
| BE ghi | DC `editDocumentTag` :14728-14794 (tạo danh mục nếu chưa có, cập nhật cột, cập nhật index `elasticDocumentService.upsertElasticDocument`) | Nhớ cập nhật index sau khi đổi dữ liệu tìm kiếm |

**Không copy**: phần tử giả `"hasChanged"` / id -1 lẫn trong danh sách kết quả (IHD:782-787; DVDVM:7857-7865) — nên trả đối tượng kết quả riêng; điều kiện hiện nút gộp 16 biến (DVDVM:8170-8261).

## Mẫu 3 — CRUD gen-1 có file đính kèm và danh sách đơn vị áp dụng: **Quản lý biểu mẫu**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `WZUL/template/template.zul` (include `template_add.zul` + `template_search.zul`, `toolbarButton`) | Một màn danh sách + form theo `viewState` của `CommonVM` |
| VM | TVM: kiểm nghiệp vụ `validateBusinessDoSave` :195-215; `doSave` hai pha — tải file lên thư mục tạm (`makeUploadFileSession`) rồi lưu trong `onUploadEvent` :217-264; nút Thêm ẩn theo vai trò :140-158; quyền sửa theo người tạo / đơn vị :639-651; trạng thái hiệu lực tính khi hiển thị :611-622 | Luồng "upload trước, lưu sau"; quyền ở tầng nút |
| Business | TB:120-205 (dựng JSON `lstFileAttach`, `lstTempOrg`) | — |
| BE | TC:992-1056 (kiểm bắt buộc rồi gọi DAO); TDAO `addTemplate` :530-605 (lấy id từ sequence trước, **chuyển file từ thư mục tạm sang thư mục chính**, ghi `FILE_ATTACHMENT` + `FILE_ATTACHMENT_MAPPER` với `OBJECT_TYPE`, ghi bảng con, cuối cùng ghi bảng cha); `downloadFile` :1370-1415 (giải mã file khi tải) | Gắn file vào đối tượng bất kỳ qua `FILE_ATTACHMENT_MAPPER.OBJECT_TYPE` |
| Tìm theo cây đơn vị | TDAO:964-986 (`START WITH … CONNECT BY PRIOR` lên và xuống từ đơn vị mặc định), :1423-1452 (đơn vị mặc định = `IS_DEFAULT ∈ {1,2}` hoặc role TL / VT) | Lọc dữ liệu theo cây đơn vị hai chiều |

**Không copy**: ngữ nghĩa "gửi phần thay đổi" khi sửa (bẫy 3); tên hàm controller / DAO đảo ngược (bẫy 5); so `"200"` với kết quả (L5); không có transaction bao các bước ghi của `addTemplate` (mỗi câu `insertOrUpdateDataBase` độc lập — TDAO:540-600).

## Mẫu 4 — Danh sách tra cứu có phân trang trên BE, giới hạn theo cây đơn vị và xuất Excel theo file mẫu: **Thư viện văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/library/documentLibrary.zul` + `documentLibrary_search.zul` (tìm nhanh / nâng cao, lọc trên tiêu đề cột, `vpaging`, popup danh sách file từng dòng) | Lưới có lọc trên header |
| VM | DLVM `findDataList` / `countDataList` :742-752, 877-886 (`isPagingServer = true`); xuất Excel `exportDocumentLibraryReport` :1179-1239 (`DynamicExport` mở mẫu `.xls` trong `APP_CONFIG.TEMPLATE_FOLDER`, `setText` theo ô, kẻ viền `setCellFormat`, tải về `FileUtil.downloadFile`) | Xuất Excel từ file mẫu |
| BE | DLDAO:85-502 (`isCount` dùng chung một câu cho đếm / lấy trang; giới hạn phạm vi theo đơn vị của người dùng và đơn vị cấp trên bằng `connect by … prior org_parent_id` :373-394; nạp file / dữ liệu phụ theo **lô id** một lần cho cả trang :410-496) | Một câu SQL cho cả đếm và trang; nạp quan hệ theo lô |

**Không copy**: nối giá trị tham số hệ thống vào SQL (L15); tham số gửi mà BE không dùng (L3, BR-05); một VM dùng chung cho các zul có id khác nhau (L1).
