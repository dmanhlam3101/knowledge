# Tích hợp hệ thống ngoài — đặc thù, bẫy, lỗi hệ thống ghi nhận

> Viết lại từ code `kha_develop` ngày 2026-10-02. Viết tắt đường dẫn / lớp như `nghiep-vu.md` (WEB, ZUL, BIZ, BE1, BE2, SQL, RES; SDC, SDS, SDF, SDR, ESU, ESCS, VESI, AUS, ISVM, ISZ, DVDVM, SUB, SEDB, DSC, WA, WC, SVM, C1, C2, AC, APP, JTF, FU, WSC). Chỉ ghi **tên** khóa cấu hình, không ghi giá trị.

## 1. Tình trạng kỹ thuật

| Phần | Tầng | Nguồn |
|---|---|---|
| API cho hệ thống ngoài (`/ext-doc`, `/ext-app`, `/ext-app-config`, `/ext-brief`, `/ext-mission`) | **gen-2** (controller → service → `ShareDocumentRepositoryImpl` SQL chuỗi qua `BaseRepositoryImpl`); bản "theo người dùng" **gọi lại hàm gen-1 cũ** (`documentService.searchReceive`, `MissionControler.findMissionByCondition`) bằng JSON dựng tay | SDF:54-200; `BE2/services/impl/ShareMissionServiceImpl.java:66-90` |
| Quản lý `EXT_APP` | gen-2 nhưng **đặt dưới `/api/vhr-employee`** (`VhrEmployeeController`) | `BE2/controller/VhrEmployeeController.java:121-134` |
| Màn "Quản lý hệ thống tích hợp" | **VM legacy VPS** (`SecurityVM<SysUser>`, facade `ISysUser` ghi thẳng DB từ web) + gọi BE gen-2 cho `EXT_APP` | ISVM:70-160, 521-530 |
| KNTC | đăng nhập gen-2 (`AuthenticationKntcController`) + tạo văn bản **gen-1** (`DocumentSignKNTCService` → `DocumentSignController.addTextKntc` gọi lại `addText`) | DSC:583-840 |
| WOPI, chuyển PDF, Solr/ES tìm kiếm, đồng bộ VHR, ViettelPay, vContract, CM, `textMarkSync` | **gen-1** (`action` → `controler` → DAO SQL) | `ban-do.md` mục 3 |
| Tín hiệu Elasticsearch, log tập trung, mobile, thiết bị, cây Đảng | gen-2 | NV-10, NV-11, NV-15 |

Quy tắc chọn chỗ sửa: **thêm nghiệp vụ gọi vào mới** → hằng `C1:2844-2856` + dòng danh mục `CATEGORY_COMMON` mã `INTEGRATED_INBOUND_BUSINESS` + kiểm `isRegisteredInExtAppAndConfig` trong service + (nếu cần bộ lọc) khối `visibleForm(..., '<MÃ>')` trong ISZ và `ViewConstant.EXT_SHARE_CONFIG` (`WEB/voffice/common/ViewConstant.java:656-674`) — xem `vi-du-mau.md` mẫu 1; **đổi bộ lọc cấu hình** → ESU (và bản sao ở SDF:370-448); **đổi điều kiện chia sẻ văn bản** → SDS.isAuthorizedToShareThisDoc + DVDVM.determineHowToDisplayExtShareButton (hai nơi).

## 2. Bẫy

1. **Ứng dụng ngoài là một "người dùng".** Mọi API `/ext-*` lấy mã ứng dụng từ `CoreUtils.getUserCode()` (= `EMPLOYEE_CODE` của token) hoặc từ claim `extAppCode` (ESU:238-256). Đổi cách sinh tài khoản ở màn đăng ký (ISVM:466) hay đổi `EMPLOYEE_CODE` của tài khoản làm gãy kiểm đăng ký. Tài khoản ứng dụng cũng **đăng nhập web / gọi mọi API thường được** (NV-02 BR-05).
2. **Lưu đăng ký = hai giao dịch.** Tài khoản ghi ở web (facade), `EXT_APP` + `EXT_APP_API` + `EXT_SHARE_CONFIG` ghi ở BE (`@Transactional` riêng — VESI:385-480). BE lỗi thì tài khoản vẫn còn (ISVM:505-517); xóa thì chỉ đặt `EXT_APP.STATUS = 0`, cấu hình cũ còn nguyên (VESI:484-497) — tạo lại cùng mã sẽ dùng lại dòng `EXT_SHARE_CONFIG` cũ (khóa theo `EXT_APP_CODE`).
3. **Mã ứng dụng ghi cứng ở hai nơi** (khác với cấp quyền kéo: trên DEV `APP_SHVB`, `ATTT` được cấp `GET_DOCUMENT_*` qua `EXT_SHARE_CONFIG` mà không cần sửa code). `"APP_TVDT"` ở web (DVDVM:9346-9348) **và** BE (SDS:325-329); `"APP_KNTC_QG"` ở DSC:597-600. Thêm ứng dụng nhận chia sẻ phải sửa cả hai phía và màn chọn.
4. **Hai bộ hằng trùng tên.** `INTEGRATED_INBOUND_BUSINESS`, `EXT_SHARE_CONFIG.MODE`, `EXT_DOC_STATUS` ở **gen-1** `C1:2838-2875` được gen-2 dùng trực tiếp (ví dụ SDR:325, 349-350; ESU dùng cả `com.viettel.voffice.constants.Constants` lẫn `Constants` import — ESU:268, 350); web có bản riêng `AC:8512-8513`, `ViewConstant.EXT_SHARE_CONFIG` (`ViewConstant.java:656-664`). Thêm mã phải sửa cả ba.
5. **`dataRange` và dải `EXT_DOC_ID`.** API kéo văn bản chia sẻ coi `EXT_DOC_ID ≤ 1.000.000.000` là dữ liệu site nội bộ, `> 1 tỉ` là site công khai (`C1:2874`; SDS:110-128; SDR:79-87) — giả định sequence hai site chạy ở hai dải khác nhau. Đổi sequence `EXT_DOCUMENT` trên một site làm lệch phân loại.
6. **Danh sách bỏ qua JWT là "chứa chuỗi".** `jwt.ignore-apis` so khớp `contains` không phân biệt hoa thường (JTF:149-180; WSC:78-102): thêm `/public` thì mọi URL **chứa** `/public` (kể cả `/api/abc/public-x`) đều bỏ qua JWT. Ngược lại `/wopi`, `/callback`, `/vContract`, `/ViettelPay`, `/SyncVHRAction` không có trong giá trị mặc định (APP:433) — bên gọi không có header `Authorization` (WOPI host gửi `access_token` trên URL) **chỉ chạy được nếu môi trường khai thêm** `JWT_IGNORE_API` (NV-02 BR-04, NV-09 BR-23).
7. **Hai kiểu đường dẫn WOPI cùng tồn tại.** Kiểu cũ: `access_token` = JWT người dùng, thông tin file mã hóa AES khóa phiên (SVM:590-597; `WEB/util/CommonUtil.java:1051-1061`, ~38 chỗ gọi); kiểu mới: `wopiToken` có hậu tố `STR_ONLINE_EDITOR`, phiên trong memcached 2 giờ (WC:1150-1221). `OnlineEditorManager` rẽ nhánh theo **hậu tố** của token (`BE1/bean/OnlineEditorManager.java:30-60`). Đổi hằng `STR_ONLINE_EDITOR` hoặc thời hạn cache làm hỏng phiên đang mở.
8. **Lưu file qua WOPI có nhiều tác dụng phụ** (WC:441-587): hủy **mọi vị trí chữ ký đã đặt** trên file đó (`TEXT_SIGN_LOCATION`), ghi lịch sử, đổi đường dẫn nếu đổi đuôi, chạm `ATTACH` để đồng bộ hai site. Mở soạn thảo kiểu mới còn đánh dấu **đã đọc** văn bản (WC:1211-1217).
9. **Bật soạn thảo trực tuyến theo đơn vị ở web, BE chỉ kiểm `active`.** Web kiểm `orgIds` theo `PATH` (SVM:568-588); BE `generateOnlineEditorUrl` / `convertPdf` chỉ kiểm `active = 1` (WC:1165-1168, 1273-1276).
10. **Elasticsearch không do Văn phòng số ghi.** Sửa logic thêm / sửa / chuyển văn bản mà quên gọi `elasticDocumentService.upsertElasticDocument` → văn bản không được đánh chỉ mục lại (16 điểm gọi — NV-10). Bảng tín hiệu tách theo site (`vps.site`).
11. **Bảng mới phải có cột `VO_*` + trigger `VO_SOURCE_<BẢNG>`** (bỏ qua khi phiên là `DBZUSER`) để đồng bộ hai site (19 script trong `SQL/`, ví dụ `SQL/20251218_create_table_elastic_document_.sql`). Cập nhật "giả" (`file_order = file_order`, `dummy_number = dummy_number`) là **cố ý** để kích hoạt đồng bộ — đừng "dọn" đi (`BE1/database/dao/file/AttachDAO.java:1077-1084`; `BE2/repositories/jpa/ElasticDocumentPrivateRepositoryJPA.java:22-23`).
12. **`EXT_APP` có hai cột "nhận hàng loạt"** `ISNHANHANGLOAT` và `IS_NHAN_HANG_LOAT` (`BE2/entities/ExtAppEntity.java:41-45`); DB DEV chỉ `IS_NHAN_HANG_LOAT` có giá trị (3 dòng = 1).
13. **KNTC dùng cả `CoreUtils.getUserCode()` (mã ứng dụng) và `externalUserCode` (mã văn thư)**: giới hạn tần suất theo mã văn thư (AUS:177; DSC:587), giao dịch ký ghi theo mã ứng dụng (DSC:618). Riêng đường dẫn `/api/document/kntc/createdocument` bộ lọc đọc token từ header `x-authentication-token` (FU:138-145) — đổi URL phải sửa cả `FuncUtils`.
14. **`check-update` cần đúng chuỗi phiên bản đang cài** đã khai trong `APP_MOBILE`; thiếu dòng → 404, app không biết có bản mới (AppMobileServiceImpl:43-71). Mã thiết bị lưu không thống nhất hoa / thường (`android` và `ANDROID` — DB DEV), truy vấn so `UPPER(TRIM)` nên hai dòng cùng được tính.
15. **`ban-do.md` xếp ở đây thành phần thuộc phân hệ khác** (do regex "VHR", "share", "enterprise"…): `ConnectVHRAction`, `vps/sysConnectVHR/*`, `widgets/connecVHRLookup*.zul`, `ConnectVHRGroupLookUpVM`, `PopupSelectConnectVHRVM` (`van-ban/lien-thong`); `VHROrgAction` (cây đơn vị — `he-thong`); `enterprise/*.zul` (`van-ban/di` + NV-06); `CallbackController` (`ho-so-cong-viec`); `AppMobileVM` (`he-thong` HT NV-17); `UserDeviceController` để ở đây (NV-11). Ngược lại `IntegratedSysVM` (`vps/integratedSys/*`) đang nằm ở `he-thong` nhưng thuộc phân hệ này.

## 3. Lỗi hệ thống — ghi nhận

| # | Ghi nhận | Nguồn |
|---|---|---|
| L1 | `POST /api/app-mobile/get-data-map` và `post-data-map` **giải mã Base64 rồi chạy nguyên câu SQL** (SELECT, gọi thủ tục, INSERT / UPDATE / DDL, nhiều câu ngăn `;`) cho **bất kỳ người dùng đã đăng nhập**; không có web / app nào trong repo gọi. Nhánh `status = 2` của `post-data-map` lặp theo số câu nhưng mỗi vòng chạy **cả chuỗi** thay vì từng câu | `BE2/controller/AppMobileController.java:55-130` (vòng lặp :106-109) |
| L2 | API kéo văn bản chia sẻ: không gửi `dataRange` → gán mặc định **1.000.000.000** (hằng `INTRANET_MAX_ID`, không phải 1 / 2) → luôn rơi vào lỗi "dải dữ liệu không hợp lệ" | SDS:104-128 |
| L3 | `ExtShareUtil.isValidRequest(List…)` nhánh `INCLUDE` thiếu `return true` sau khi kiểm hợp lệ → rơi xuống `default` ném "cấu hình không hợp lệ": yêu cầu lọc độ khẩn / thể loại / đơn vị ban hành **đúng cấu hình** vẫn bị từ chối | ESU:342-371 |
| L4 | `getDocumentSharedCheckList` **nối thẳng danh sách mã ứng dụng** từ request vào câu SQL (`'…'` trong `SYS.ODCIVARCHAR2LIST`) | SDR:250-258 |
| L5 | `loginKNTC` / `addTextKntc`: không tìm thấy `EXT_APP` (sai mã hoặc `STATUS ≠ 1`) → `NullPointerException` ngay dòng kiểm `RATE_LIMIT`, trả lỗi chung thay vì "không có quyền" | AUS:176-177; DSC:586-587 |
| L6 | Entity `ExtAppEntity` khai cột `@Column(name = "RATE_LIMIT ")` (có dấu cách cuối) | `BE2/entities/ExtAppEntity.java:74` |
| L7 | `SSOConnector.loginApiSSO` ghi log mức INFO **mật khẩu người dùng dạng rõ** khi SSO trả lỗi; cả `SSOConnector` và `VNEIDConnector` dựng HTTP client **tin mọi chứng chỉ TLS** (chú thích "DEV/TEST ONLY") cho môi trường thật | `BE1/utils/SSOConnector.java:188`, `356-395`; `BE1/utils/VNEIDConnector.java:173-210` |
| L8 | `convertPdfWithUserGroup`: file mã hóa → chuyển PDF bản đã giải mã, **rồi** do `file.exists()` lại chuyển PDF bản gốc (đang mã hóa) và ghi đè kết quả | WC:1288-1307 |
| L9 | `generateOnlineEditorUrl` vẫn đánh dấu "đã đọc" ngay dưới chú thích "đọc file thì không đánh dấu là đã đọc văn bản" | WC:1211-1217 |
| L10 | `POST /api/text/sync-text`, `/count-sync-text`: trả **mọi văn bản trình ký của toàn hệ thống** trong khoảng ≤ 90 ngày cho bất kỳ token nào (không kiểm ứng dụng, không lọc đơn vị) | `BE2/controller/TextSyncController.java:40-68`; `BE2/repositories/impl/TextRepositoryImpl.java:48` |
| L11 | `/ViettelPay/VerifyDataTrans` trả chuỗi rỗng (thân comment); `/solrSearch/indexEmployee` luôn trả 0; `IndexDocumentByType.run()` rỗng | `BE1/action/ViettelPayAction.java:28-41`; `BE1/controler/SolrSearchController.java:549-600`; `BE1/elasticsearch/indexdata/IndexDocumentByType.java` |
| L12 | Menu mở dẫn tới zul **không tồn tại**: `EXT-SHARE-CONFIG-ORG` (`config/extShare/extShareConfigOrg.zul`), `VHREMPLOYEE` (`vps/sysUser/vhrEmployee.zul`); web `EnterpriseBusiness` gọi `CM.listCompany` / `createSignDocument` / `sendDocument` đã comment ở BE (menu `VBKDT` đang khóa) | mục 1.2 `nghiep-vu.md`; `BE1/action/CMResource.java:25-91` |
| L13 | Màn đăng ký hệ thống tích hợp: thêm mới thì băm SHA-256 mật khẩu cho `APP_PASS`; **sửa** thì gửi nguyên giá trị ô mật khẩu (không băm) | ISVM:468-472 |
| L14 | `/api/user-device/remove-device` khai tên hàm Java `getDataBarChart` (sao chép); `UserDeviceServiceImpl` mang chú thích "Quản lý phiếu trình" (sinh tự động) | `BE2/controller/UserDeviceController.java`; `BE2/services/impl/UserDeviceServiceImpl.java:26-30` |
| L15 | Comment DB `EXT_DOCUMENT.MODULE_ID` ghi "mặc định là 1 (vb đến)" nhưng code ghi 1 cho **văn bản đi** (`DIGITAL_SIGNATURE = 1L // văn bản đi`); comment `EXT_DOC_STATUS` thiếu giá trị 3 (xóa) | comment DB; AC:9548; `C1:2838-2842` |
| L16 | `SDR.addExtDocument` trả `null`, `SDR.isAuthorizedToShare` không ai gọi (tham số `orgIds` truyền cả tập vào một dấu `?`) | SDR:270-272, 356-372 |
| L17 | `EXT_APP.STATUS = 11` (1 dòng DB DEV — `QLDT_CPDA` "Quản lý Doanh thu - Chi phí dự án") không có trong code | DB DEV `EXT_APP` ngày 2026-10-02 |
| L18 | Dữ liệu trùng mã: `APP_TVDT` có **7 dòng `EXT_APP` cùng `APP_CODE`** (chỉ 1 dòng `STATUS = 1`) — `findByAppCodeAndStatus(code, 1)` trả một dòng nên chạy được, nhưng truy vấn không lọc `STATUS = 1` (ví dụ `SDR.checkRegisteredAndIgnoredExtApp` dùng `MAX`, `getDocumentSharedCheckList` `LEFT JOIN … status <> 0`) phụ thuộc trạng thái các dòng cũ | DB DEV `EXT_APP` ngày 2026-10-02; SDR:225-309; VESI:396-411 |
| L19 | Đơn vị gốc `DVTHHT` không có trên DB DEV (`VHR_ORG.CODE`) → `rootOrganization` null, màn "Quản lý hệ thống tích hợp" lỗi khi mở / thêm (NPE bị nuốt) | ISVM:188-217, 223-224, 277, 287, 301; DB DEV `VHR_ORG` ngày 2026-10-02 |
| L20 | `ONLINE_EDITOR_CONFIG.orgIds` trên DEV = một mã đơn vị không có trong `VHR_ORG` DEV; `MOBILE_CURRENT_VERSION`, `LOGIN_METHOD` chưa khai → `login-required-check` luôn lỗi | DB DEV `SYSTEM_PARAMETER` ngày 2026-10-02; `MobilePublishStoreServiceImpl.java:23-37` |
| L21 | Danh mục `INTEGRATED_INBOUND_BUSINESS` có mã `GET_MEETING_WEEK` (399), `FIND_MEETING_NATIVE` (401) nhưng không có hằng / API nào trong code; cấp cho ứng dụng thì không gọi được | DB DEV `CATEGORY_COMMON` ngày 2026-10-02; `C1:2844-2856` |

## 4. Chỗ "đừng đụng"

- `jwt.ignore-apis` / `JWT_IGNORE_API`: thêm đường dẫn là mở API không cần đăng nhập (so khớp "chứa chuỗi" — bẫy 6).
- Trigger `VO_SOURCE_*` và các câu cập nhật "giả" (bẫy 11).
- Tên khóa `SYSTEM_PARAMETER` `ONLINE_EDITOR_CONFIG`, `ELASTICSEARCH_8X`, `PERMISSION_CALL_API`, `CERT_EXTEND_VTPAY_CONFIG`, `MOBILE_CURRENT_VERSION`, `LOGIN_METHOD` — đọc trực tiếp theo chuỗi, đổi tên làm tắt tích hợp tương ứng.
- Khuôn phản hồi KNTC (`BaseResponseKNTC`) và URL `/api/connecteoffice`, `/api/document/kntc/createdocument` — do bên KNTC thiết kế (chú thích "đơn vị tích hợp khác đang yêu cầu api đăng nhập riêng" — `BE2/controller/AuthenticationKntcController.java:26-27`).
