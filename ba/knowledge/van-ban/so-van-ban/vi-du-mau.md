# Sổ văn bản — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phân hệ chủ yếu là **gen-1**; khi làm tính năng mới nên theo mẫu gen-2 của phân hệ khác (nhắc việc — `../../lich-nhac-viec/vi-du-mau.md`), các mẫu dưới đây dùng khi **sửa / mở rộng** chỗ đang có.

## Mẫu 1 — Danh mục CRUD gen-1 một VM (danh sách + form + khóa + xóa có kiểm + popup chi tiết): **Sổ văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/document/textBook/textBook.zul` (khung `borderlayout` + toolbar + include `textBook_search.zul` / `textBook_add.zul`), popup `textBook_detail.zul`, `textBook_inspect.zul` | Một trang, hai include ẩn-hiện theo `vm.isViewSearch` / `isViewInsert || isViewUpdate`; nút thao tác từng dòng ẩn theo `data.permission` (`textBook_search.zul:334-350`) |
| VM | TBVM kế thừa `CommonVM<TextBook>`: phân trang server (`isPagingServer = true` — :123), `findDataList` / `countDataList` (:704-735), `onDoInsert` / `doInsertCallback` / `onDoUpdate` / `onDoSave` / `validateBusinessDoSave` / `insert` / `update` / `validateDoDelete` / `delete` (:248-596), popup chi tiết bằng `ViewUtil.showPopupTextBookDetail` + tham số `ARG_DETAIL_TEXTBOOK` để **cùng VM** chạy chế độ xem (:135-165, 213-235, 819-827) | Dùng các hook của `CommonVM` thay vì tự viết luồng lưu; hộp xác nhận `CustomMessageBox` (:426-428, 755-760) |
| Lưới động | `renderTbNumberGridRows` tạo `Row/Cell/Intbox` bằng Java, đồng bộ ô phụ thuộc trong `onChange` (:279-363) | Khi số dòng phụ thuộc danh mục (mỗi thể loại một ô) |
| Business | `TBB.findListTextBooks` / `getCountListTextBooks` cùng một endpoint, tham số `count = 1` để đếm (:30-69); `insertTextBook(…, insert)` một endpoint cho thêm + sửa (:91-104) | Mẫu danh sách + đếm một endpoint |
| BE | `TBA` (POST `x-www-form-urlencoded`) → `TBC` (`FunctionCommon.getDataFromClient(request, data, keys, cmd)` đọc tham số theo thứ tự `keys`, kiểm phiên — :57-123) → `TBDAO` (SQL + `cmd.insertOrUpdateDataBase`, chèn lô `cmd.insertDataBaseBloc` — :360-401) | Đồng bộ danh sách con bằng **so tập cũ / mới → xóa mềm phần bỏ, chèn phần mới** (`updateTextBookShare` :447-499, `updateTextBookNumber` :501-576) |
| Tìm kiếm | `findListTextBooks` dùng CTE `DATA_SOURCE` (UNION sở hữu + được chia sẻ) → `FILTERED_DATA` → `ROW_NUMBER()` phân trang, đếm con bằng scalar subquery **chỉ cho trang hiện tại** (TBDAO:669-854); tìm bỏ dấu `nlssort(…, 'nls_sort=binary_ai')` (:741-743) | Phân trang + đếm phụ rẻ |

**Không copy**: SQL nối `typeDocId` thẳng vào chuỗi (`TYPE_DOC_ID LIKE '%/" + id + "/%'` — TBDAO:617); BE không kiểm quyền (`dac-thu.md` L1); một truy vấn phụ mỗi dòng trong vòng lặp (`WAITING_NUMBER_BOOK` — TBDAO:868-873); đặt cờ "duy nhất" bằng `UPDATE … = 0` trước khi lưu (L4); dùng một cột cho hai nghĩa (bẫy 1).

## Mẫu 2 — Form cần sổ + số tiếp theo + cấp bù + kiểm trùng: **Tiếp nhận văn bản đến** / **Cấp số văn bản đi**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Danh sách sổ | `TBB.getTextBooksByOrgIdAndDocType(orgId, loại sổ 0/1, textId)` (`TBB:227-250`) — PRDVM:881, DLVM:877-905 | Lấy sổ đơn vị + sổ dùng chung, đã lọc khóa / năm; **chọn sẵn** sổ `IS_DEFAULT = 1` (PRDVM:1819-1838) hoặc `defaultTextBookId` hệ thống gợi ý (DLVM:895-902) |
| Số tiếp theo | `TBB.getNextRegisterNumberDataByTextBookId(textBookId, typeId, isDocOut)` trả `NextRegisterNumberDTO(nextNumber, reusedNumber)` (`TBB:322-351`); đọc lại **ngay lúc lưu** và hỏi xác nhận nếu người dùng sửa khác số tiếp theo (PRDVM:443-482, VBĐ NV-03 bước 3) | Luôn truyền đúng `typeId` (sổ theo thể loại) và `isDocOut` (`dac-thu.md` bẫy 7); hiển thị số bù riêng |
| Kiểm trùng | `GET /api/doc-out/is-duplicated-register-number?regNum&textBookId&typeId&documentId` (`DRI:1905-1950`) / `/api/doc-in/list-exist-document-by-textbook-and-register` (VBĐ BR-11) | Gọi trước khi lưu, loại trừ chính văn bản đang sửa (`documentId`) |
| Ghi bộ đếm | BE gọi `textBookDAO.updateTextBookNumber(document)` sau khi lưu (`TC:1835`, `DDAO:17554`, `17621-17630`) | Không tự `UPDATE CURRENT_NUMBER` ở chỗ mới — gọi hàm chung để giữ quy tắc "chỉ tăng" và quy đổi thể loại gốc |
| Không có form (chạy nền) | `TCDAO.getRegisterNumberByTextBook` + `increaseNumberDocByTextBookIdAndTypeId` (TEAS:800-803; `TaskDAO.java:3846-3862`) | Tự chọn sổ + tăng số trực tiếp; kiểm trùng và thử lại (VBĐi NV-10) |

**Lưu ý khi copy**: gọi `getTextBooksByOrgIdAndDocType` sẽ sinh bộ sổ mặc định nếu đơn vị chưa có sổ năm nay (bẫy 2); số gợi ý không được giữ chỗ (bẫy 6).

## Mẫu 3 — Xuất báo cáo Excel từ file mẫu: **Sổ đăng ký văn bản đến**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/documentHandover/documentBook.zul` — một combobox "loại báo cáo" (`classificationId`), các ô điều kiện `visible` theo mã báo cáo, nút Xuất | Một màn nhiều loại báo cáo |
| VM | RBVM `doExport` (:735-913) rẽ nhánh theo mã → đặt cờ (`setIsReportDocumentInRegister`, `setIsGetIncomingNumber`… :812-823) → gọi Business → `exportIndexDocumentInRegister` (:1365-1440): `new DynamicExport(APP_CONFIG.TEMPLATE_FOLDER + tên mẫu + "_vi.xls", …)`, `setText(..., colIndex++)` từng cột, `Filedownload.save` | Điền mẫu Excel có sẵn tiêu đề; tiêu đề phụ "Từ ngày … đến ngày …" lấy nhãn `LBL:2782-2787` |
| Business | `DHB.searchDocBook` (:314-447): build JSON điều kiện, chọn endpoint theo `isIndex` / `isArrive` | — |
| BE | `DHA` `tableOfIncomingDocuments` → `DHC.exportReportDocumentV2` (đo thời gian, gọi bản V1 — :707-719) → `DHDAO.exportIndexReportDocumentV2` (:77-90, ghi log thời gian từng bước) → `generateSqlReportDocumentInRegisterOrTransfer` (:2281-2548): `WITH rootData AS (UNION hai nguồn)` + các CTE phụ (hồ sơ lưu, nơi nhận bản lưu, ngày chuyển, số trang file) rồi `LEFT JOIN` | Gom dữ liệu phụ bằng CTE thay vì truy vấn từng dòng; tách bản V2 "opt-in" giữ nguyên route cũ |
| Mẫu | `web-spring/src/main/webapp/template/bao_cao_so_dang_ky_vb_den_vi.xls` | — |

**Không copy**: ghép `_en` khi không có file mẫu (`dac-thu.md` L10); lọc đơn vị lẫn lộn đơn vị chọn và mọi đơn vị văn thư (L11); `catch (Exception)` nuốt lỗi rồi vẫn `return true` (RBVM:909-912).

## Mẫu 4 — Endpoint gen-2 CRUD nhỏ có kiểm nghiệp vụ: **Số chờ** (`/api/text-book`)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Controller | `TBMC:28-85` — `@RequestMapping(Constants.REQUEST_MAPPING_PREFIX + "/text-book")`, DTO `@Valid`, trả `ResponseUtils.getResponseEntity` | Endpoint mỏng |
| Service | `TBSI:65-105`: kiểm trùng trong danh sách gửi lên (so `Set` với `List`), trùng với dữ liệu có, trùng với số đã cấp → `throw new VofficeException(ErrorCodeApp.…, tham số)`; người tạo `CoreUtils.getUserId()`; `saveAll`; xóa mềm (:115-128) | Mẫu kiểm trùng nhiều tầng + mã lỗi có tham số |
| Repository | `WaitingNumberBookRepositoryJPA` (derived query `existsByWaitingNumberAndDelFlagAndTextBookId…`, `findByTextBookIdAndDelFlagNotOrderByCreatedDateDesc` + `PageRequest`) | Truy vấn dẫn xuất JPA + phân trang |

**Lưu ý**: tính năng này **chưa có client** và chưa được nối vào bước cấp số (NV-09 BR-28) — copy cấu trúc, không coi là nghiệp vụ đang chạy. Bảng có 13 dòng thử (8 còn hiệu lực, mới nhất 2025-04-08 — DB DEV `WAITING_NUMBER_BOOK` ngày 2026-10-01).
