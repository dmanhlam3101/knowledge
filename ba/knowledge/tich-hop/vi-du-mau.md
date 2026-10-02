# Tích hợp hệ thống ngoài — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-02). Viết tắt như `nghiep-vu.md`. Khi copy, tránh các điểm đã ghi ở `dac-thu.md` (nêu ở cuối từng mẫu).

## Mẫu 1 — API gen-2 cho hệ thống ngoài, có kiểm "ứng dụng đã đăng ký nghiệp vụ": **cấp cây đơn vị** `/ext-app/get-org`

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Hằng nghiệp vụ | `C1:2844-2856` (`INTEGRATED_INBOUND_BUSINESS.GET_ORG`) + dòng `CATEGORY_COMMON` mã `INTEGRATED_INBOUND_BUSINESS` (`VALUE_NAME = GET_ORG`, `CATEGORY_VALUE` 385 trên DB DEV ngày 2026-10-02) | Mỗi nghiệp vụ gọi vào = một mã hằng + một dòng danh mục; quản trị gán cho ứng dụng ở màn NV-01 |
| Controller | `BE2/controller/extApp/ShareOrgController.java:16-27` (`@RequestMapping("/ext-app")`, một hàm `@PostMapping`) | Đặt dưới gói `controller/extApp`, tiền tố `/ext-*` |
| Service | `BE2/services/impl/ShareOrgServiceImpl.java:31-37`: `CoreUtils.getUserCode()` → `shareDocumentRepository.isRegisteredInExtAppAndConfig(appCode, GET_ORG)` → không có thì `CustomException(EXT_DOCUMENT_FETCH_FORBIDDEN)`; kiểm đầu vào bằng mã lỗi riêng (:39-55); phân trang chặn trên 500 (:72-85) | Khung "lấy mã ứng dụng → kiểm đăng ký nghiệp vụ → kiểm đầu vào → truy vấn có trần" |
| Repository | `BE2/repositories/jpa/VhrOrgRepositoryJPA.getAllOrg(voLastUpdated, pageable)` (lọc theo cột vết `VO_LAST_UPDATED` để bên ngoài đồng bộ dần) | Đồng bộ tăng dần theo `VO_LAST_UPDATED` / `VO_VERSION` |
| Phản hồi | `GetShareResponse<T>` (`totalCount`, `pageCount`, `pageSize`, `listResult`) | Khuôn phân trang chung cho API ngoài |

**Biến thể "theo người dùng"** (token cấp qua `login-sso-ext-app`): `ShareMissionServiceImpl.java:47-120` — lấy mã ứng dụng từ claim `ExtShareUtil.getExtAppCodeFromToken(request)` (thiếu → `EXT_DOCUMENT_APP_CODE_NOT_FOUND`), kiểm nghiệp vụ `GET_MISSION_BY_SSO`, rồi gọi lại hàm danh sách gen-1 có sẵn bằng chính token để dữ liệu đúng quyền người dùng.

**Có bộ lọc theo cấu hình**: copy `SDS.getShareDocumentsOutByOrg` (:413-449): đọc `BUSINESS_CONFIG_VALUE` bằng `extShareConfigService.getBusinessConfigValue(appCode, business, CODE, BaseShareConfigDTO.class)`, giới hạn khoảng ngày `ExtShareUtil.applyLimitRange` (30 ngày), áp `applyBaseConfigBeforeFetchData` (:550-584).

**Không copy**: bộ kiểm danh sách `ExtShareUtil.isValidRequest(List…)` hiện thiếu `return true` (L3); nối chuỗi giá trị request vào SQL (L4); ghi cứng mã ứng dụng (bẫy 3). Thêm nghiệp vụ mới nhớ sửa cả ba bộ hằng (bẫy 4).

## Mẫu 2 — Hệ thống ngoài **kéo dữ liệu tăng dần có giao dịch, cho phép lấy lại**: `/ext-doc/get-document-from-ext-app`

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Ghi "hàng đợi chia sẻ" | SDS.addExtDocument :332-408 — mỗi sự kiện (mới / sửa / xóa) **một dòng mới** `EXT_DOCUMENT` với `EXT_DOC_STATUS`; tự gọi khi sửa / xóa văn bản (`BE1/controler/DocumentController.java:874-880`, `1003-1015`) | Nhật ký sự kiện chỉ thêm, bên nhận tự hợp nhất |
| Con trỏ kéo | SDR.getListExtDocIdByLastIndex :68-94 (`EXT_DOC_ID > lastIndex ORDER BY … FETCH FIRST ? ROWS ONLY`) | Phân trang theo khóa tăng dần thay vì `OFFSET` |
| Giao dịch / lấy lại | SDS:76-101 + SDR.isExistTransactionId :33-49, getListExtDocIdByTransactionId :51-66; ghi `EXT_DOCUMENT_ACCESS_LOG` sau khi đọc xong (:169-205) | `transactionId` do bên gọi sinh, dùng lại khi lỗi mạng |
| Đọc song song có hạn chờ | SDS:137-177 (`Executors.newFixedThreadPool(3)`, `awaitTermination` 20 giây) + `BE1/thread/ShareDocumentThread.java` | Ba truy vấn độc lập (chi tiết, file, file mẫu) chạy song song |

**Không copy**: giá trị mặc định `dataRange` sai (L2); ghép file vào văn bản bằng `HashMap` là được, nhưng nhớ `limit` tối đa 100 (SDS:262-274).

## Mẫu 3 — Đăng nhập riêng cho đối tác có **IP whitelist + danh sách người được đại diện + giới hạn tần suất**: KNTC

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Endpoint không qua JWT | `BE2/controller/AuthenticationKntcController.java:40-70` + khai đường dẫn vào `jwt.ignore-apis` (APP:433) | Đường dẫn đăng nhập riêng phải nằm trong danh sách bỏ qua JWT |
| Kiểm truy cập | AUS.loginKNTC :175-246 — `EXT_APP.RATE_LIMIT` (Redis, `FuncUtils.isOverRateLimit`), `EXT_APP.IP` (danh sách / `bypass_all`, IP lấy bằng `FunctionCommon.getClientIpAddressRemote`), `EXT_APP.EMPLOYEE_CODE` | Ba lớp kiểm trên cùng dòng `EXT_APP` |
| Token mang ngữ cảnh ngoài | `userDetails.setExternalUserCode`, `setExternalOrgIdentifier` (AUS:270-271) → bộ lọc JWT nạp lại (JTF:97-111) | Đưa danh tính người dùng phía đối tác vào token ứng dụng |
| Tạo dữ liệu bằng hàm sẵn có | DSC.buildAddTextReqKNTC :718-815 dựng JSON rồi gọi `addText` gen-1; ghi giao dịch `AUTO_DIGSIG_TRANSACTION` (:817-840) để nhận kết quả ký qua cơ chế chung (`KS NV-15`) | Không viết lại luồng tạo văn bản; dựng request và tái dùng |

**Không copy**: NPE khi không có `EXT_APP` (L5); so mật khẩu không băm (BR-14); đọc token từ header riêng bằng so khớp URL trong `FuncUtils.parseJwt` (bẫy 13).

## Mẫu 4 — Mở file trên **trình soạn thảo trực tuyến** (đường dẫn kiểu mới) và phát **tín hiệu đánh chỉ mục**

| Việc | Vị trí | Copy phần nào |
|---|---|---|
| Mở soạn thảo | web `SVM.showEditLocalFile` :5240-5260: dựng `FileInfoRequestEntity` (tên, đường dẫn, storage, `canEdit`, `isEncrypted`) → `requisitionBusiness.generateOnlineEditorUrl` (`BIZ/RequisitionBusiness.java:6752`) → `ViewUtil.popupLibreOffice` với `OfficeEditorVM.WOPI_URL` | Dùng đường dẫn kiểu mới (phiên trong cache, không lộ JWT trên URL); kiểm trước `isActiveOnlineEditor()` (SVM:568-588) |
| BE sinh URL | WC.generateOnlineEditorUrl :1150-1221 | Đặt phiên `OnlineEditorSession` vào cache có TTL |
| Tín hiệu đánh chỉ mục | `elasticDocumentService.upsertElasticDocument(documentId)` sau khi ghi `DOCUMENT` (ví dụ `BE1/controler/DocumentController.java:902`) → `BE2/services/impl/ElasticDocumentServiceImpl.java:18-43` | Mọi thao tác đổi văn bản cần tìm kiếm phải gọi; bảng mới cần cột `VO_*` + trigger (bẫy 11) |

**Không copy**: đánh dấu "đã đọc" khi mở soạn thảo (L9, câu Q5); chuyển PDF hai lần (L8).
