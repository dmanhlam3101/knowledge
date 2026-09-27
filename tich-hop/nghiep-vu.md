# Tích hợp ngoài — nghiệp vụ

| Hệ thống ngoài | Mục đích | Trong code |
|---|---|---|
| **VHR** (nhân sự Viettel) | Nguồn tổ chức & nhân viên; đồng bộ định kỳ/tay | gen-1 `SyncVHRAction`, `connectVHRAction` (cấu hình kết nối/cây đơn vị, `ConnectVHRVM`), `VHROrgAction` (11 hàm, tra đơn vị theo phạm vi/vai trò); gen-2 `VhrEmployeeController` (`/api/vhr-employee`: danh sách, lãnh đạo theo đơn vị, văn thư `get-VT-in-org`, chứng thư `update-certificate`, mã bảo mật, ứng dụng ngoài `ext-app`), `VhrOrgController` (`/api/vhr-org`: cây đơn vị, lãnh đạo, KPI đơn vị); bảng `VHR_ORG`, `VHR_EMPLOYEE`, `CONNECT_VHR` |
| **SSO** Viettel passport / **VNeID** / eCabinet | Đăng nhập | `AuthenticationController.LoginSSO` / `LoginFromSSO` / `LoginVNEID` / `LoginEcabinet`, web `LoginController`, `sso.ws.url`, `utils/sso`, `PublicController.sso-login-flags` |
| **WOPI** (Office Online / OnlyOffice) | Soạn thảo / xem file online, lịch sử sửa, chuyển PDF | gen-1 `WOPIAction` (`/wopi/{encryptedFileInfo}/contents`, `generate-online-editor-url`, `convertPdf`, `getListEditHistories`, `getListSubmissionFormEditHistories`) ← `WOPIBusiness` ← `AddAttachFileVM` (văn bản), phiếu trình |
| **Solr / Elasticsearch** | Tìm toàn văn văn bản, người | gen-1 `SolrSearchResource` (`/solrSearch`), `ElasticDocument*`, `els_query/`, `LogElkController`; `SearchSolrBusiness` |
| **Mobile app** | API cho app VOffice mobile; cấu hình app; kho phát hành | gen-2 `AppMobileController` (`/api/app-mobile`, `get-data-map`), `MobilePublishStoreController`, `UserDeviceController` (thiết bị/push), `PublicController.check-update` / `download`; web `vm/config/AppMobileVM` |
| **Ứng dụng ngoài dùng chung dữ liệu** (`ext-*`) | Chia sẻ văn bản/hồ sơ/nhiệm vụ/tổ chức cho hệ thống khác (đăng nhập SSO ext-app) | gen-2 `ShareDocumentController` (`/ext-doc`: `login-sso-ext-app`, `get-document-from-ext-app`, `add-ext-doc`, `check-authorized-to-share`, `in` / `out`), `ShareBriefController` (`/ext-brief`), `ShareMissionController` (`/ext-mission`), `ShareOrgController` (`/ext-app`), `ShareDocumentConfigController` (`/ext-app-config`, phạm vi chia sẻ `ext-share-scope`); bảng `EXT_APP*`, `EXT_DOCUMENT*`, `EXT_SHARE_CONFIG` / `EXT_SHARE_SCOPE`, `EXT_DOCUMENT_ACCESS_LOG`; web `vm/config/extShare`, `ShareExtDocBusiness` |
| **ViettelPay** | Xác thực giao dịch chuyển tiền gắn văn bản tài chính | gen-1 `ViettelPayAction.VerifyDataTrans`, `DocumentService.transferMoneyAction`, `document.transferMoney` |
| **VContract / CM** (hợp đồng điện tử, doanh nghiệp) | Nhận kết quả ký hợp đồng, gửi văn bản cho doanh nghiệp | gen-1 `VContractAction` (`getTextDetail`, `receiverResult`, `downloadFile`), `CMResource` (`/CM`: `search`, `sendDocument`, `createSignDocument`, `listCompany`, `updateStateDocument`, `getListTransactionFailed`) ← `EnterpriseBusiness` ← `enterprise/*.zul`, `CallbackController.submit-result` |
| **VOConnect / trục liên thông** | Gửi/nhận văn bản, nhiệm vụ | xem `van-ban/lien-thong` (`/api/hook`) |
| **KNTC** (khiếu nại tố cáo?) | Ký số & đăng nhập cho hệ thống KNTC | `DocumentSignKNTCService`, `AuthenticationKntcController`, `BaseResponseKNTC` ❓ |
| SMS gateway, mail | Gửi SMS/mail | `sms.properties`, `mail/*` (web), xem `lich-nhac-viec` |
| Cisco/cospace, SmartRoom | Họp trực tuyến | xem `hop` |
| Redis, ELK, k8s | Hạ tầng | `RedisController`, `docker/`, `k8s/`, `LogElkController` |

## Quy tắc
- QT1. Dữ liệu tổ chức/nhân sự **chỉ nhập từ VHR**; sửa tay trong VOffice sẽ bị đồng bộ ghi đè ❓ (xác nhận).
- QT2. Endpoint `/ext-*`, `/public/*`, `/callback`, `/api/hook` có cơ chế xác thực riêng (SSO ext-app, `jwtIgnoreConfig`) — không mở thêm endpoint không JWT ngoài các prefix này.
- QT3. Chia sẻ ra ứng dụng ngoài ghi `EXT_DOCUMENT_ACCESS_LOG` (audit).
- QT4. WOPI cần file được mã hóa thông tin (`encryptedFileInfo`) — không truyền path thật.

## ❓
1. Ở Khánh Hòa, HR nguồn là VHR Viettel hay hệ thống cán bộ công chức tỉnh?
2. Ứng dụng ngoài nào đang dùng `/ext-*`?
3. ViettelPay / VContract / CM còn hoạt động hay là di sản Viettel?
