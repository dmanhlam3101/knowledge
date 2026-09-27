# Bản đồ hệ thống — Ký số, chứng thư, CloudCA, ảnh chữ ký

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 2 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `widgets/imageSignature/insertSignatureImage.zul` | `widget.SignatureImageVM` | — | — | — |
| `widgets/imageSignature/updateSignatureImage.zul` | `widget.SignatureImageVM` | — | — | — |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

_Không có Business riêng — màn hình phân hệ này dùng Business của phân hệ khác (xem cột "Gọi BE qua" ở mục 1)._

## 3. BE — Controller → logic / service → DAO / repository → bảng

### CertManagementAction (gen1) — base `/CertManagementAction`, 22 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CertManagementAction.java`

- Logic (gen-1 `controler/`): `CertManagementController`
- DAO (SQL thuần): `ActionLogMobileDAO`, `CommonDataBaseDaoVO2`, `ImageSignDao`, `P12CertDAO`, `SmsDAO`, `StaffDAO`, `SystemParameterDAO`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `CONFIG_SMS_ORG`, `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `DUOC`, `MEETING_ASSISTANT`, `MESSAGE`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `SMS_BLACK_LIST`, `SMS_MASTER`, `STAFF`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `SYSTEM_PARAMETER`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_OTHER`, `TEXT_PROCESS`, `TEXT_SIGN_LOCATION`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/CertManagementAction/getCertStateNow` | `getCertStateNow` |
| POST | `/CertManagementAction/getListCertPackages` | `getListCertPackages` |
| POST | `/CertManagementAction/cancelWaitingCert` | `cancelWaitingCert` |
| POST | `/CertManagementAction/makeCert` | `makeCert` |
| POST | `/CertManagementAction/confirmTransactionOtp` | `confirmTransactionOtp` |
| POST | `/CertManagementAction/activateCert` | `activateCert` |
| POST | `/CertManagementAction/alterIdentification` | `alterIdentification` |
| POST | `/CertManagementAction/extendCert` | `extendCert` |
| POST | `/CertManagementAction/cancelExtendCert` | `cancelExtendCert` |
| POST | `/CertManagementAction/getExtendCertStatus` | `getExtendCertStatus` |
| POST | `/CertManagementAction/cancelCert` | `cancelCert` |
| POST | `/CertManagementAction/BackupCert` | `backupCert` |
| POST | `/CertManagementAction/DownloadFileInfoUser` | `DownloadFileInfoUser` |
| POST | `/CertManagementAction/DownloadStreamFileInfoUser` | `DownloadStreamFileInfoUser` |
| POST | `/CertManagementAction/DownloadRenewFileInfoUser` | `DownloadRenewFileInfoUser` |
| POST | `/CertManagementAction/DownloadStreamRenewFileInfoUser` | `DownloadStreamRenewFileInfoUser` |
| POST | `/CertManagementAction/signFileExtentCa` | `signFileExtentCa` |
| POST | `/CertManagementAction/signFileRenewCa` | `signFileRenewCa` |
| POST | `/CertManagementAction/cancelRenewCert` | `cancelRenewCert` |
| POST | `/CertManagementAction/getCodeCert` | `getCodeCert` |
| POST | `/CertManagementAction/requestOTPSignUserCAInfo` | `requestOTPSignUserCAInfo` |
| POST | `/CertManagementAction/confirmOTPSignUserCAInfo` | `confirmOTPSignUserCAInfo` |

</details>

### CloudCAAction (gen1) — base `/CloudCAAction`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CloudCAAction.java`

- Logic (gen-1 `controler/`): `CloudCAController`, `EmpCloudCAService`
- DAO (SQL thuần): `CloudDeviceCertDAO`, `CommonDataBaseDaoVO2`, `EmpCloudCADAO`, `SystemParameterDAO`, `TextSignDAO`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CLOUD_DEVICE_CERT`, `DOCUMENT_TYPE`, `EMP_CLOUD_CA`, `FILES_ATTACHMENT`, `FILES_COMMENT_SIGN`, `MARK_ATTACH_HISTORY`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/CloudCAAction/checkUserStatus` | `checkUserStatus` |
| POST | `/CloudCAAction/authenticateUser` | `authenticateUser` |
| POST | `/CloudCAAction/verifyOTPInSigning` | `verifyOTPInSigning` |
| POST | `/CloudCAAction/registerDevice` | `registerDevice` |
| POST | `/CloudCAAction/deleteDevice` | `deleteDevice` |

</details>

### ImageSignAction (gen1) — base `/imageSignAction`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/ImageSignAction.java`

- Logic (gen-1 `controler/`): `ImageSignController`, `WOPIController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ImageSignDao`, `StaffImageSignDAO`, `UserDAO`, `AttachDAO`, `DocumentDAO`, `SubmissionFormEditHistoryDAO`, `SystemParameterDAO`, `TextEditHistoryDAO`
- Repository (JPA): `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `SubmissionFileRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FILES_ATTACHMENT`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `P12_CERT`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_SIGN_LOCATION`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/imageSignAction/addSignImage` | `addSignalImage` |
| POST | `/imageSignAction/editSignImage` | `editSignalImage` |
| POST | `/imageSignAction/search` | `search` |
| POST | `/imageSignAction/reviewFilePdf` | `reviewFilePdf` |
| POST | `/imageSignAction/getImageSignByCardId` | `getImageSignByCardId` |
| POST | `/imageSignAction/getListLocationByTextId` | `getListLocationByTextId` |
| POST | `/imageSignAction/updateListLocation` | `updateListLocation` |
| POST | `/imageSignAction/getListLocationByFileDraff` | `getListLocationByFileDraff` |

</details>

### P12CertAction (gen1) — base `/P12CertAction`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/P12CertAction.java`

- Logic (gen-1 `controler/`): `P12CertControler`, `LogActionControler`, `UserControler`, `EmpCloudCAService`
- Service: `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `CertManagementDAO`, `CommonDataBaseDaoVO2`, `LogActionDao`, `P12CertDAO`, `CloudDeviceCertDAO`, `ConfigParameterDAO`, `DocumentDAO`, `EmpCloudCADAO`, `SystemParameterDAO`, `FavouriteDAO`, `ImageDAO`, `MeetingAssistantDAO`, `MissionDAO`, `OrgDAO`, `StaffDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATABASE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGE_ORG`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `ORG_COMBINATION_MAP`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/P12CertAction/search` | `search` |
| POST | `/P12CertAction/listActiveCerts` | `listActiveCerts` |
| POST | `/P12CertAction/cancelRegCert` | `cancelRegCert` |
| POST | `/P12CertAction/actionCancelRegCertWeb` | `actionCancelRegCertWeb` |

</details>

### SignResource (gen1) — base `/Sign`, 20 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SignResource.java`

- Logic (gen-1 `controler/`): `SignController`, `CommonControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`, `OfficePublishedReplacementService`, `OfficePublishedReplacementServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`
- DAO (SQL thuần): `AttachDAO`, `CloudDeviceCertDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `EmpCloudCADAO`, `LogTranstionSignDAO`, `MissionSigningDAO`, `P12CertDAO`, `FilesAttachmentDAO`, `TextDAO`, `DocumentSignDAO`, `StaffDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `TextSignDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `BriefEntityRepositoryJPA`, `AttachRepositoryJPA`, `FileEncryptMapJPA`, `NodeActionRepositoryJPA`, `PositionRepositoryJPA`, `ReportDailyHistoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `NotificationRepositoryJPA`, `SecurityTypeRepositoryJPA`, `StaffImageSignJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `EMP_CLOUD_CA`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_FILES`, `MISSION_NORM`, `MISSION_SIGNING`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `P12_CERT`, `PHAN`, `POSITION`, `READ_NOTICE_HISTORY`, `REPORT_DAILY_HISTORY`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Sign/CheckSigningStatusForText` | `checkSigningStatusForText` |
| POST | `/Sign/SignByCASIM` | `signByCASIM` |
| POST | `/Sign/SignSoft` | `signSoft` |
| POST | `/Sign/SignSoftHashMutiFile` | `hashMutiFile` |
| POST | `/Sign/SignSoftAttachMutiFile` | `signSoftAttachMutiFile` |
| POST | `/Sign/SignCloudCA` | `signCloudCA` |
| POST | `/Sign/SignTextByCASIM` | `signTextByCASIM` |
| POST | `/Sign/getP12CertInformation` | `getP12CertInformation` |
| POST | `/Sign/RequestResetCertificatePassword` | `requestResetCertificatePassword` |
| POST | `/Sign/ConfirmOTPCodeToResetCertificatePassword` | `confirmOTPCodeToResetCertificatePassword` |
| POST | `/Sign/updatePasswordP12Cert` | `updatePasswordP12Cert` |
| POST | `/Sign/signMultiFileTask` | `signMultiFileTask` |
| POST | `/Sign/SignSoftHashMutiFileBrief` | `hashMutiFileBrief` |
| POST | `/Sign/SignSoftAttachMutiFileBrief` | `signSoftAttachMutiFileBrief` |
| POST | `/Sign/SignSoftHashMutiFileDoc` | `hashMutiFileDoc` |
| POST | `/Sign/SignSoftAttachMutiFileDoc` | `signSoftAttachMutiFileDoc` |
| POST | `/Sign/updateDatabaseAfterMark` | `updateDatabaseAfterMark` |
| POST | `/Sign/updateViewComment` | `updateViewComment` |
| POST | `/Sign/updateDatabaseDocumentAfterMark` | `updateDatabaseDocumentAfterMark` |
| POST | `/Sign/validateTaxCode` | `validateTaxCode` |

</details>

### CaSupplierController (gen2) — base `/api/ca-supplier`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/CaSupplierController.java`

- Service: `CaSupplierService`, `CaSupplierServiceImpl`
- Repository (JPA): `CaSupplierRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `CA_SUPPLIER`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/ca-supplier/get-list-sign-method` | `getListSignMethod` |

</details>

### FileEncryptMapController (gen2) — base `/api/file-encrypt-map`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/FileEncryptMapController.java`

- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/file-encrypt-map/get-list-file-encrypt-by-objectId` | `getListFileEncryptByObjectId` |
| GET | `/api/file-encrypt-map/get-list-file-encrypt-by-rootObjectId` | `getListFileEncryptByRootObjectId` |

</details>

### StaffImageSignController (gen2) — base `/api/staff-image-sign`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/StaffImageSignController.java`

- Logic (gen-1 `controler/`): `FileControler`, `WOPIController`
- Service: `PdfOcrDocumentService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AttachDAO`, `BriefManagementDAO`, `CommonDataBaseDaoVO2`, `ConfigParameterDAO`, `ConnectDocumentDAO`, `DocumentDAO`, `DownloadAllFileDAO`, `DownloadFileCommentDAO`, `DownloadFileDocumentDAO`, `FilesAttachmentDAO`, `ImageDAO`, `ImageOrgDAO`, `OrgDAO`, `SystemParameterDAO`, `StaffImageSignDAO`, `TaskApprovalDAO`, `TaskDAO`, `TextDAO`, `TextProcessDAO`, `TextSearchDAO`, `SubmissionFormEditHistoryDAO`, `TextEditHistoryDAO`
- Repository (JPA): `BriefSubmitAttachFileEntityRepositoryJPA`, `BriefSubmitRequestEntityRepositoryJPA`, `VersionControlRepositoryJPA`, `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `SubmissionFileRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CODE_MASTER`, `CONFIG_USER_DOCUMENT`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `NODE_ACTION`, `ORG_KI`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_PROCESS`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_ORG`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/staff-image-sign/get-staff-image-sign/{staff-image-sign-id}` | `getStaffImageSign` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `SignatureException` | — | — | — | — |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `CaSupplierEntity`→`CA_SUPPLIER`, `EmpCaDetailEntity`→`EMP_CA_DETAIL`, `EmpCaEntity`→`EMP_CA`, `FileEncryptMapEntity`→`FILE_ENCRYPT_MAP`, `FileEncryptMapHistoryEntity`→`FILE_ENCRYPT_MAP_HISTORY`, `StaffImageSignEntity`→`STAFF_IMAGE_SIGN`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `ImageSignature`→`IMAGE_SIGNATURE`

**Tổng hợp bảng chạm tới**: `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CA_SUPPLIER`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATABASE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EMP_RATING`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `IMAGE_SIGNATURE`, `INDEX`, `LOG_TRANSTION_SIGN`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `PHAN`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`
