# Thư viện, biểu mẫu, từ điển tag — đặc thù, bẫy, lỗi hệ thống ghi nhận

> Viết lại từ code `kha_develop` ngày 2026-10-02. Viết tắt đường dẫn / lớp như `nghiep-vu.md` (WEB, ZUL, WZUL, BIZ, BE1, BE2, SQL; DLVM, DLDVM, RQB, DC, DLDAO, TVM, TB, TA, TC, TDAO, TDB, IHD, DVDVM, TDC, TDSI, TDRI, TDJ, WRVM, ATRVM, AC, C1).

## 1. Tình trạng kỹ thuật

| Phần | Tầng | Nguồn |
|---|---|---|
| Thư viện văn bản (danh sách, chi tiết, xuất Excel) | **gen-1**: `DocumentAction.actionSearchDocViewLibrary` → `DocumentController` → `DocumentLibraryDAO` (SQL ghép chuỗi) | DC:1179-1349; DLDAO:85-502 |
| Thư mục thư viện ("Cấu hình thư viện", "Chuyển vào thư viện", popup chọn thư mục) | **legacy web**: VM ghi thẳng `DOCUMENT_LIBRARY*` qua `iCommon`; đọc cây qua facade `IDocumentLibrary` → `DocumentLibraryJpaDao` | DLVM:227-250; DLDVM:266-300; `WEB/voffice/dao/DocumentLibraryJpaDao.java` |
| Biểu mẫu | **gen-1** `TemplateAction` / `TemplateController` / `TemplateDAO`; facade legacy `ITemplate` còn nhưng không ai dùng | TA; TC; TDAO |
| Ý kiến mẫu cũ (`TEMPLATE_DIRECTING`) | **gen-1**, cùng `TemplateAction` — web không gọi | TA:36-200 |
| Từ điển tag: đọc / xóa | **gen-2** `TagDictionaryController` (`/api/tag-dictionary`) | TDC |
| Từ điển tag: ghi tag lên văn bản | **gen-1** `DocumentAction.EditDocument*Tag` gọi **service gen-2** `TagDictionaryService` + JPA `documentRepositoryJPA` / `documentInGroupRepositoryJPA` / `documentInStaffRepositoryJPA` | DC:14728-14991 |
| Màn báo cáo theo mẫu | web `vm/template/*`; BE gen-2 `mission-template` / `report-result` (phân hệ `nhiem-vu`) | NVu NV-17 |

Quy tắc chọn chỗ sửa: **điều kiện thư viện** → `DLDAO.actionSearchDocViewLibrary` (và hai bản `RQB.getListDocViewLibrary` — bẫy 4); **ai thấy biểu mẫu** → `TDAO.searchTemplate` + `getListOrgDefaultTemplate`; **ai sửa biểu mẫu** → `TVM.permissionEdit` / nút trong `template_search.zul`; **gợi ý / hiển thị tag** → `TDRI`; **ghi tag** → `DC.editDocument*Tag` + `saveNewTagName` (bẫy 7); **nút Gán tag hiện / ẩn** → `DVDVM.isVisibleHastag` (16 điều kiện) và bản riêng ở `WEB/voffice/vm/requisition/RequisitionViewDetailVM.java`.

## 2. Bẫy

0. **Trên DB DEV chưa văn bản nào mang tag** (`TAG_NAME` khác null: 0 dòng ở `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF` — DB DEV ngày 2026-10-02) dù danh mục có ~630 tag còn hiệu lực; muốn thử lọc / hiển thị tag phải tự gắn dữ liệu test.
1. **Ba menu thư viện, một màn.** `TVT` (`library=0`), `TVCN` (`library=1`), `DOCUMENT_LIBRARY` (`library=1`) cùng mở `documentLibrary.zul`; DLVM không đọc `library`. VM duy nhất đọc tham số này (`WEB/voffice/treeLibrary/vm/DocumentLibraryTreeVM.java:89`, `110`) không được zul nào dùng. Muốn tách "cá nhân" / "quy trình" phải dựng lại, không chỉ sửa URL menu.
2. **`DOCUMENT_PUBLIC = 0011L` là số bát phân = 9** (AC:3388). Giá trị lưu ở `DOCUMENT_LIBRARY.USER_LIBRARY` cho thư viện quy trình là **9**, không phải 11. Truy vấn tay theo 11 sẽ không ra.
3. **Sửa biểu mẫu gửi "phần thay đổi", không gửi trạng thái đầy đủ.** Danh sách `lstFileAttach` / `lstTempOrg` khi sửa = mục mới (không id) + mục **bị bỏ** (có id); BE coi mục có id là **cần xóa** (TVM:292-337; TDAO:621-712). Gửi đủ danh sách hiện có (kèm id) sẽ xóa hết file / đơn vị áp dụng.
4. **Hai bản `RQB.getListDocViewLibrary` khác hành vi**: bản `(DocumentEntity, …)` (RQB:184-262, popup chọn văn bản thay thế) không gửi `isNotLimitByOrg` → BE **không giới hạn đơn vị** (DC:1302-1307), không gửi từ khóa; bản `(keyWord, DocumentLibrary, …)` (RQB:265-317, màn thư viện, popup chọn nguồn nhiệm vụ) luôn giới hạn đơn vị. Sửa điều kiện thư viện phải nghĩ tới cả hai nơi dùng.
5. **`/tempAction` trộn hai nghiệp vụ và đặt tên đảo ngược.** Controller `addTemplate` / `editTemplate` / `deleteTemplate` = **ý kiến mẫu cũ** (`TEMPLATE_DIRECTING`) và gọi DAO `insertTemplate` / `updateTemplate`; controller `insertTemplate` / `updateTemplate` / `delete` = **biểu mẫu** (`TEMPLATE`) và gọi DAO `addTemplate` / `editTemplate` / `delete` (TC:129-182, 992-1056; TDAO:110-160, 530-740). Đọc tên hàm rất dễ nhầm bảng.
6. **Tag gắn bằng tên, không bằng id.** Văn bản lưu chuỗi tên nối `,` (`TAG_NAME`); hiển thị "tag đang gắn" = so tên trong chuỗi với danh mục (TDRI:89-196). Đổi / xóa dòng danh mục không đổi văn bản; tên chứa dấu phẩy sẽ bị tách thành nhiều tag; hai tag trùng tên ở hai đơn vị là hai dòng danh mục.
7. **Bốn đường tạo tag với điều kiện "đã có" khác nhau**: `editDocumentTag` / `editDocumentGroupTag` — có tag **đang hoạt động** cùng tên **cùng đơn vị**, không xét phạm vi (DC:14765-14779, 14858-14870; TDJ:17-18); `editDocumentStaffTag` — có tag đang hoạt động cùng tên **do mình tạo**, không xét phạm vi (DC:14953-14966; TDJ:34-35); `saveNewTagName` (thêm / sửa văn bản, vào sổ) — có tag cùng tên **phạm vi 2** cùng đơn vị, **kể cả đã xóa** (DC:14993-15005; TDJ:15). Hai bản `saveNewTagName` (DC và TDSI:146-155) giống nhau, chỉ bản DC được gọi.
8. **Văn bản đã xóa vẫn có thể nằm trong danh sách thư viện**: điều kiện `STATUS_NUMBER ≠ 1` chỉ có trong nhánh lọc theo "loại văn bản + đơn vị" (DLDAO:184-202); không lọc thì văn bản đã xóa vẫn hiện nếu còn dòng công khai, chỉ bị chặn khi bấm mở (DLVM:1057-1069).
9. **Một VM cho ba zul khác nhau**: DLVM được `documentLibrary.zul`, `configlibrary.zul`, `popupLibrary.zul` dùng, nhưng `@Wire` và `findDataList` viết cho `documentLibrary_search.zul` (DLVM:78-108, 742-752) — xem L1. `WRVM` (3.189 dòng) phục vụ bốn menu báo cáo + popup xem báo cáo (`ZUL/widgets/popupViewReport.zul:6`) theo thuộc tính `menuType` / `openFrom` đặt trên include (WRVM:255-289).
10. **Nhãn "Loại văn bản" của thư viện**: hằng `INCOMING = 1` mang nhãn "Văn bản đi", `OUTGOING = 2` mang nhãn "Văn bản đến" (AC:7122-7144) — tên hằng ngược nhãn, nhưng nhãn **khớp** BE (1 = văn bản đi, 2 = văn bản đến — DLDAO:185-194). Đừng "sửa" theo tên hằng.
11. **Comment DB của `TEMPLATE.TYPE_ID` sai** ("Id nganh"): dữ liệu DB DEV 2026-10-02 là id `DOCUMENT_TYPE` (Chỉ thị, Công văn, Báo cáo…); `AREA_ID` = lĩnh vực nhưng nhãn web là "Ngành" — tra cứu theo code (TDAO:1006-1027; `template_add.zul:72-110`).
12. **Mẫu xuất Excel nằm ở `webapp/template/`** và được `TemplateFilter` chặn khi chưa đăng nhập (`WEB/voffice/config/WebConfig.java:318-329`) — thêm mẫu xuất mới đặt vào đây; tên file thường có hậu tố `_vi` / `_en` theo ngôn ngữ (DLVM:1169-1171, 1183).

## 3. Lỗi hệ thống — ghi nhận

| # | Ghi nhận | Nguồn |
|---|---|---|
| L1 | Màn **"Cấu hình thư viện"** (`configlibrary.zul`) dùng DLVM nhưng include `librarySearch.zul` không có các id `vpaging`, `documentLibraryList` mà DLVM `@Wire` (`#includeSearch #vpaging`, `#includeSearch #documentLibraryList`) → `postViewInitialized` lỗi ngay dòng `this.vpaging.getPaging()` và bỏ qua nạp danh mục, tìm kiếm ban đầu, ẩn nút (lỗi bị bắt, chỉ ghi log). `findDataList` / `countDataList` đã bị DLVM thay bằng truy vấn **văn bản công khai**, nên lưới "thư mục" của màn cấu hình không hiển thị thư mục `DOCUMENT_LIBRARY` | DLVM:78-83, 203-224, 742-752; `ZUL/library/librarySearch.zul:146`, `191` |
| L2 | Popup **"Chuyển vào thư viện"** ghi `DOCUMENT_LIBRARY_DETAIL.DOCUMENT_ID = doc.getId()` với `doc = new Document()` không bao giờ được gán → luôn null; văn bản truyền vào (`ARG_SELECTED_DOCUMENT` → `docEntity`) không được dùng khi lưu. `postViewInitialized` đọc `doclib.getLstDocumentFile()` khi popup không truyền `ARG_SELECTED_ITEMS` → lỗi bị bắt, bỏ qua phần sau | DLDVM:56, 83-93, 117-120, 282-283 |
| L3 | Hai hàm đếm / lấy danh sách thư viện không cùng tham số: bản cũ gửi `docType` = `classificationId` khi lấy danh sách nhưng `categoryId` khi đếm (RQB:191 vs 236); tham số `officePublishedId` ("đơn vị công bố", ô chọn `doSelectSysOrg`) được gửi nhưng BE **không dùng** trong câu SQL (DLDAO:86-502 chỉ nhận `publishedGroupId` vào chữ ký); `state` cũng không dùng (BR-05) | RQB:184-262, 265-317; DLDAO:86-93 |
| L4 | Xuất Excel thư viện: cột "phạm vi" luôn trống vì câu SQL không chọn tên phạm vi (`rangePublished`) | DLVM:1198; DLDAO:101-135 |
| L5 | `TB.deleteTemplate` coi thành công khi giá trị trả về là `"200"`, nhưng BE trả `true` → hàm luôn trả false; VM bỏ qua kết quả nên người dùng vẫn thấy xóa thành công | TB:185-205; TC:781-786; TVM:580-585 |
| L6 | Đọc tag **không lọc tag đã xóa**: gợi ý ô lọc (`getTagDictionaryForSearchBox`), "tag đang gắn" của dòng đơn vị / dòng cá nhân (`getTagNamesByDocumentInGroupId`, `getTagNamesByDocumentInStaffId`) không có `DEL_FLAG = 0`; riêng "tag đang gắn" của văn bản đi có lọc | TDRI:49-57, 136-148, 179-191 (so với :98) |
| L7 | Gắn tag cá nhân: kiểm "đã có" theo **người tạo** không xét phạm vi → văn thư đã tạo tag **đơn vị** cùng tên thì tag cá nhân không được tạo, và không hiện trong gợi ý cá nhân (chỉ lấy `TAG_SCOPE = 1`) | DC:14953-14966; TDJ:34-35; TDRI:156-171 |
| L8 | `saveNewTagName` (khi thêm / sửa văn bản, vào sổ) kiểm trùng kể cả tag **đã xóa** → tag đã xóa khỏi danh mục không được tạo lại qua đường này, trong khi gắn qua popup thì tạo lại (bẫy 7) | DC:14993-15005; TDJ:15 |
| L9 | `deleteTag` theo id dùng `findById(...).get()` không kiểm tồn tại → lỗi nếu id không có | TDSI:40-41 |
| L10 | Cột `TAG_DICTIONARY.ORG_NAME` (thêm ở cuối file SQL) không có trong entity; tham số `orgName` của `saveTagDictionary` bị bỏ qua → code `kha_develop` không ghi cột này (DB DEV ngày 2026-10-02 vẫn có 34 dòng có `ORG_NAME`, do nguồn khác ghi); 16 tag đơn vị còn hiệu lực **không có `ORG_ID`** nên không bao giờ hiện trong gợi ý đơn vị | `SQL/20251012_create_table_tag_dictionary.sql:49-50`; TDSI:70-79; `BE2/entities/TagDictionaryEntity.java` |
| L11 | Mở chi tiết và đọc file xử lý văn bản bị khóa khác nhau: `doViewDetail` chặn cả **người đang khóa**, `readAllAttachedFile` cho người đang khóa đọc | DLVM:1050 vs 673-674 |
| L12 | Ô "Quy trình / Cá nhân" khi **tìm** thư mục (`docheckPublicSearch`, `docheckPrivateSearch`) xóa thư mục cha trên `dataSelected` (form thêm) thay vì `dataSearch` | DLVM:363-420 |
| L13 | Comment DB DEV hai cột `ATTACH_TEMPLATE.IS_PUBLISH` và `IS_NOT_PUBLISH` giống hệt nhau ("File gioi han phat hanh, 0: Khong gioi han…, 1: Gioi han…"); comment `TEMPLATE.TYPE_ID` "Id nganh" sai — dữ liệu DB DEV 2026-10-02 khớp `DOCUMENT_TYPE` (bẫy 11) | DB DEV ngày 2026-10-01 |
| L14 | `getListOfTagForOther` có hai bản: JPA native giới hạn 20 dòng (không dùng) và bản SQL không giới hạn (đang dùng) | TDJ:20-31; TDRI:156-171; TDSI:130-132 |
| L15 | Giá trị tham số hệ thống `DOCUMENT_TYPE_ONLY_FOR_ORG` được **nối thẳng vào câu SQL** (`type_id not in ( ` + value + ` )`), không qua tham số bind | DLDAO:95, 397-399 |
| L16 | `TemplateAction` / `TemplateDAO` còn 8 endpoint thao tác `TEMPLATE_DIRECTING`, nhưng **bảng không tồn tại trên DB DEV** (ORA-00942, ngày 2026-10-02) → gọi sẽ lỗi SQL | TA:36-200; TDAO:73-497 |

## 4. Đừng đụng / lưu ý khi sửa

- **Thứ tự / định dạng chuỗi tag** `TAG_NAME` (nối `,`, tách bằng `REGEXP_SUBSTR '[^,]+'`) được dùng ở lọc tìm kiếm văn bản (`BE1/database/dao/document/DocumentDAO.java:3388-3396`, `18250-18258`), hiển thị và index — đổi dấu ngăn cách phải sửa đồng bộ AC:9562, C1:2715, TDRI và các câu lọc.
- **`DOCUMENT_PUBLISHED`, `DOCUMENT_SCOPE_REF`** do phân hệ `van-ban/di` ghi; thư viện chỉ đọc — sửa ý nghĩa `STATUS` (0 / 1 / 2 / 3) phải đối chiếu DLDAO:257-275.
- **`TEMPLATE_MNG_SEQ`** là sequence của `TEMPLATE` (không phải `TEMPLATE_SEQ`) (TDAO:540).
