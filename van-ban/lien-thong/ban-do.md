# Bản đồ hệ thống — Liên thông văn bản (trục, VOConnect, cơ quan ngoài)

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 6 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/goverment/connectDocument.zul` | `vm.document.ConnectDocumentVM` | `ConnectDocumentBusiness` | — | BE |
| `document/goverment/connectDocument_detail.zul` | `vm.document.ConnectDocumentVM` | `ConnectDocumentBusiness` | — | BE |
| `document/goverment/govermentDocument.zul` | `vm.document.GovermentDocumentVM` | — | — | — |
| `document/goverment/transferGovermentDocument.zul` | `vm.document.TransferGovermentDocumentVM` | — | — | — |
| `document/migrate/migrated_doc_import.zul` | `vm.document.MigratedDocumentVM` | `CategoryCommonBusiness`, `MigratedDocumentBusiness`, `TextBookBusiness` | — | BE |
| `document/migrate/migrated_document.zul` | `vm.document.MigratedDocumentVM` | `CategoryCommonBusiness`, `MigratedDocumentBusiness`, `TextBookBusiness` | — | BE |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### ConnectDocumentBusiness

`web-spring/src/main/java/com/voffice/service/business/ConnectDocumentBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `connectDocumentAction.addStateConnectDocument` | `/connectDocumentAction/addStateConnectDocument` | `ConnectDocumentAction.addStateConnectDocument` | gen1 |
| `connectDocumentAction.doEvictionDoc` | `/connectDocumentAction/doEvictionDoc` | `ConnectDocumentAction.doEvictionDoc` | gen1 |
| `connectDocumentAction.getListConnectDocOutDetail` | `/connectDocumentAction/getListConnectDocOutDetail` | `ConnectDocumentAction.getListConnectDocOutDetail` | gen1 |
| `connectDocumentAction.getListConnectDocument` | `/connectDocumentAction/getListConnectDocument` | `ConnectDocumentAction.getListConnectDocument` | gen1 |
| `connectDocumentAction.getListInternalOrg` | `/connectDocumentAction/getListInternalOrg` | `ConnectDocumentAction.getListInternalOrg` | gen1 |
| `connectDocumentAction.getOrgConnectDocument` | `/connectDocumentAction/getOrgConnectDocument` | `ConnectDocumentAction.getOrgConnectDocument` | gen1 |
| `connectDocumentAction.transferInternalOrgDoc` | `/connectDocumentAction/transferInternalOrgDoc` | `ConnectDocumentAction.transferInternalOrgDoc` | gen1 |

### MigratedDocumentBusiness

`web-spring/src/main/java/com/voffice/service/business/MigratedDocumentBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.migrated-doc.detail` | ❓ không tìm thấy endpoint | | |
| `api.migrated-doc.search` | `/api/migrated-doc/search` | `MigratedDocController.search` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### ConnectDocumentAction (gen1) — base `/connectDocumentAction`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/ConnectDocumentAction.java`

- Logic (gen-1 `controler/`): `ConnectDocumentController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ConnectDocumentDAO`, `DocumentDAO`, `DocumentInGroupDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_USER_DOCUMENT`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `FILES_ATTACHMENT`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/connectDocumentAction/getListConnectDocument` | `getListConnectDocument` |
| POST | `/connectDocumentAction/getConnectDocumentDetail` | `getConnectDocumentDetail` |
| POST | `/connectDocumentAction/addStateConnectDocument` | `addStateConnectDocument` |
| POST | `/connectDocumentAction/getListConnectDocOutDetail` | `getListConnectDocOutDetail` |
| POST | `/connectDocumentAction/transferInternalOrgDoc` | `transferInternalOrgDoc` |
| POST | `/connectDocumentAction/getListInternalOrg` | `getListInternalOrg` |
| POST | `/connectDocumentAction/doEvictionDoc` | `doEvictionDoc` |
| POST | `/connectDocumentAction/getOrgConnectDocument` | `getOrgConnectDocument` |

</details>

### DocOrgRepublishAction (gen1) — base `/DocOrgRepublish`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocOrgRepublishAction.java`

- Logic (gen-1 `controler/`): `DocOrgRepublishController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `DocOrgRepublishDAO`, `DocumentSignDAO`, `TextDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CONNECT_DOCUMENT`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `FILES_ATTACHMENT`, `FILES_COMMENT_SIGN`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_MINUTES`, `MISSION_NORM`, `NODE_ACTION`, `ORG_CRITERIA_SOURCE`, `POSITION`, `SECURITY_TYPE`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/DocOrgRepublish/getListOrganization` | `getListOrganization` |
| POST | `/DocOrgRepublish/getBaseDocument` | `getBaseDocument` |

</details>

### MigratedDocController (gen2) — base `/api/migrated-doc`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MigratedDocController.java`

- Service: `MigratedDocService`, `MigratedDocServiceImpl`
- Repository (JPA): `MigratedDocumentRepositoryJPA`, `MigratedFilesRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `MIGRATED_DOCUMENT`, `MIGRATED_FILES`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/migrated-doc/search` | `search` |

</details>

### TextSyncController (gen2) — base `/api/text`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextSyncController.java`

- Service: `TextService`, `TextServiceImpl`
- Repository (JPA): `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `TEXT`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/text/sync-text` | `syncText` |
| POST | `/api/text/count-sync-text` | `countSyncText` |

</details>

### VOConnectProcessorController (gen2) — base `/api/hook`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/VOConnectProcessorController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `VOConnectProcessorService`, `VOConnectProcessorServiceImpl`, `DocInService`, `DocInServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`
- DAO (SQL thuần): `AgreementDAO`, `CommentDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`, `DocumentDAO`, `FilesAttachmentDAO`, `MeetingDAO`, `MissionDAO`, `RequestDAO`
- Repository (JPA): `CvPriorityRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `DocumentTypeRepositoryJPA`, `FilesAttachmentRepositoryJPA`, `InternalDocReceiveRepositoryJPA`, `MissionProcessRepositoryJPA`, `MissionRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_RECEIVE_XML`, `INTERNAL_DOC_SEND_XML`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_CONFIG`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `MEETING_RESOURCE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERSONAL_STOTAGE`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `VOF_COMMENT`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/hook/send-document` | `sendDocument` |
| POST | `/api/hook/update-status-document` | `updateStatusDocument` |
| POST | `/api/hook/send-mission` | `sendMission` |
| POST | `/api/hook/revoke-document` | `revokeDocument` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

_Không có facade legacy riêng._

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `ConnectDocumentEntity`→`CONNECT_DOCUMENT`, `ConnectProcessInEntity`→`CONNECT_PROCESS_IN`, `InObjectDetailEntity`→`IN_OBJECT_DETAIL`, `InObjectReceiveXmlEntity`→`IN_OBJECT_RECEIVE_XML`, `InObjectSendXmlEntity`→`IN_OBJECT_SEND_XML`, `InternalDocDetailEntity`→`INTERNAL_DOC_DETAIL`, `InternalDocReceiveEntity`→`INTERNAL_DOC_RECEIVE_XML`, `InternalDocSendXmlEntity`→`INTERNAL_DOC_SEND_XML`, `MigratedDocumentEntity`→`MIGRATED_DOCUMENT`, `MigratedFilesEntity`→`MIGRATED_FILES`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `MigratedDocumentEntity`→`MIGRATED_DOCUMENT`, `MigratedFilesEntity`→`MIGRATED_FILES`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_RECEIVE_XML`, `INTERNAL_DOC_SEND_XML`, `IN_OBJECT_DETAIL`, `IN_OBJECT_RECEIVE_XML`, `IN_OBJECT_SEND_XML`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_CONFIG`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `MEETING_RESOURCE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERSONAL_STOTAGE`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `VOF_COMMENT`
