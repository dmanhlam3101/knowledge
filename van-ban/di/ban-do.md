# Bản đồ hệ thống — Văn bản đi – từ cấp số trở đi: cấp số → ban hành → văn bản ban hành → thu hồi/hủy

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 15 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/documentPublish/document_publish.zul` | `vm.document.DocumentPublishVM` | `DocumentPublishBusiness`, `RequisitionBusiness` | `IDocumentLibrary` | BE+LEGACY |
| `document/documentPublish/document_publish_replace.zul` | `vm.document.DocumentPublishReplaceVM` | `DocumentPublishBusiness` | — | BE |
| `document/documentPublish/popupPublishVB.zul` | `vm.document.DocumentPublishViewDetailVM` | `DocumentPublishBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/documentPublish/popupPublishVBEdit.zul` | `vm.document.DocumentPublishViewDetailVM` | `DocumentPublishBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/issueDocument/issue_document_list.zul` | `vm.requisition.RequisitionViewIssueNumberVM` | `AnswerDocumentBusiness`, `RequisitionBusiness` | — | BE |
| `document/reportSendReceiveDoc/documentOut.zul` | `vm.document.DocumentOutVM` | `AnswerDocumentBusiness`, `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `ImageOrgBusiness`, `NotificationBusiness`, `ReminderBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `ISysUser`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/documentOut_dcs_dbh.zul` | `vm.document.DocumentOutVM` | `AnswerDocumentBusiness`, `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `ImageOrgBusiness`, `NotificationBusiness`, `ReminderBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `ISysUser`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/issussDocument.zul` | `vm.document.DocumentLookUpVM` | `DocumentPublishBusiness`, `ImageOrgBusiness`, `RequisitionBusiness`, `TextBookBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/reportSendReceiveDoc/listDocumentSign.zul` | `vm.document.DocumentVM` | `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/popupVB_issue_number.zul` | `vm.document.DocumentViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CVGroupBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentRequestBusiness`, `FlowBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `ReminderBusiness`, `SavePersonalDocBusiness`, `ShareExtDocBusiness`, `TagDictionaryBusiness`, `WOPIBusiness` | `ICommon`, `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `documentDraft/rejectPublish.zul` | `vm.admin.requisition.RejectPublishVM` | — | — | ☠ VM không tồn tại |
| `requisition/rejectPublish.zul` | `vm.requisition.RejectPublishVM` | `RequisitionBusiness` | — | BE |
| `requisition/requisition_issue_number_view_detail.zul` | `vm.requisition.RequisitionViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness`, `WOPIBusiness` | `IRequisition`, `ISysOrganization` | BE+LEGACY |
| `requisition/requisition_vbbh.zul` | `vm.requisition.RequisitionVbbhVM` | — | — | — |
| `widgets/popupAskForSeal.zul` | `widget.PopupAskForSealVM` | — | — | — |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### DocumentPublishBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentPublishBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `DocumentAction.cancelPublish` | `/DocumentAction/cancelPublish` | `DocumentAction.cancelPublish` | gen1 |
| `DocumentAction.editPublicationInformation` | `/DocumentAction/editPublicationInformation` | `DocumentAction.editPublicationInformation` | gen1 |
| `DocumentAction.editTmpPublicationInformation` | `/DocumentAction/editTmpPublicationInformation` | `DocumentAction.editTmpPublicationInformation` | gen1 |
| `DocumentAction.publish` | `/DocumentAction/publish` | `DocumentAction.publish` | gen1 |
| `DocumentAction.publishListDoc` | `/DocumentAction/publishListDoc` | `DocumentAction.publishListDoc` | gen1 |
| `DocumentPublishAction.actionGetPublishStatusByDocumentId` | `/DocumentPublishAction/actionGetPublishStatusByDocumentId` | `DocumentPublishAction.actionGetPublishStatusByDocumentId` | gen1 |
| `DocumentPublishAction.actionSearchAlterDocAuto` | `/DocumentPublishAction/actionSearchAlterDocAuto` | `DocumentPublishAction.actionSearchAlterDocAuto` | gen1 |
| `DocumentPublishAction.actionSearchDocPublish` | `/DocumentPublishAction/actionSearchDocPublish` | `DocumentPublishAction.actionSearchDocPublish` | gen1 |
| `DocumentPublishAction.getListDocAlter` | `/DocumentPublishAction/getListDocAlter` | `DocumentPublishAction.getListDocAlter` | gen1 |
| `DocumentService.getListFields` | `/DocumentService/getListFields` | `DocumentSignService.getListFields` | gen1 |
| `DocumentService.getListIndustry` | `/DocumentService/getListIndustry` | `DocumentSignService.getListIndustry` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### DocumentPublishAction (gen1) — base `/DocumentPublishAction`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentPublishAction.java`

- Logic (gen-1 `controler/`): `DocumentPublishControler`
- DAO (SQL thuần): `AutoDigitalSignDAO`, `CommonDataBaseDaoVO2`, `DocumentPublishDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_PUBLISHED`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `MESSAGE`, `SECURITY_TYPE`, `STAFFGROUP`, `STAFF_IN_MESSAGE`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/DocumentPublishAction/actionSearchDocPublish` | `actionSearchDocPublish` |
| POST | `/DocumentPublishAction/actionGetPublishStatusByDocumentId` | `actionGetPublishStatusByDocumentId` |
| POST | `/DocumentPublishAction/getListDocAlter` | `getListDocAlter` |
| POST | `/DocumentPublishAction/actionSearchAlterDocAuto` | `actionSearchAlterDocAuto` |
| POST | `/DocumentPublishAction/getParentOrgLastSignOrg` | `getParentOrgLastSignOrg` |

</details>

### TextAction (gen1) — base `/textAction`, 97 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TextAction.java`

- Logic (gen-1 `controler/`): `TextController`, `CommonControler`, `EmpCloudCAService`
- Service: `CategoryCacheService`, `DocCommentService`, `DocCommentServiceImpl`, `DocumentHistoryLogService`, `DocumentHistoryLogServiceImpl`, `DocumentPermissionCacheService`, `DraftLifecycleEventService`, `DraftLifecycleEventServiceImpl`, `DraftLifecycleMissionClient`, `ElasticDocumentService`, `ElasticDocumentServiceImpl`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ManagerService`, `ManagerServiceImpl`, `OfficePublishedReplacementService`, `OfficePublishedReplacementServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`, `TextDraftService`, `TextDraftServiceImpl`, `TextProcessService`, `TextProcessServiceImpl`, `TextReceiverGroupDetailService`, `TextReceiverGroupDetailServiceImpl`
- DAO (SQL thuần): `AnswerDocumentDAO`, `AttachDAO`, `AutoDigitalSignDAO`, `BriefDetailManagementDAO`, `CloudDeviceCertDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `DocOrgRepublishDAO`, `DocumentDAO`, `DocumentScopeDAO`, `DocumentSignDAO`, `DocumentPublishedTmpDAO`, `DocumentSearchInService`, `TextDAO`, `EmpCloudCADAO`, `HistoryChangeSignDAO`, `StaffDAO`, `StaffImageSignDAO`, `MeetingWeekDAO`, `MissionDAO`, `MissionSigningDAO`, `OrgDAO`, `ReminderHistoryDAO`, `FilesAttachmentDAO`, `P12CertDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `SysRoleDAO`, `TextBookDAO`, `TextCheckSpellDAO`, `TextCommonDAO`, `TextEditHistoryDAO`, `TextProcessDAO`, `ImageSignDao`, `TextProcessHistoryDAO`, `TextReceiverDAO`, `TextReceiverGroupDAO`, `TextSignDAO`
- Repository (JPA): `AttachRepositoryJPA`, `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `CategoryCommonRepositoryJPA`, `DocumentHistoryLogJPA`, `DocumentTypeRepositoryJPA`, `TextBookRepositoryJPA`, `VhrOrgJPA`, `DocumentInListRequestRepositoryJPA`, `TextRepositoryJPA`, `ElasticDocumentPrivateRepositoryJPA`, `ElasticDocumentPublicRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `ConfigSmsModuleRepositoryJPA`, `EmpCaDetailRepositoryJPA`, `EmpCaRepositoryJPA`, `FeedbackImageRepositoryJPA`, `FeedbackLogFileRepositoryJPA`, `FeedbackProcessRepositoryJPA`, `FeedbackRepositoryJPA`, `ImageOrgConfigRepositoryJPA`, `ImageOrgRepositoryJPA`, `MenuRepositoryJPA`, `NotificationRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `PositionRepositoryJPA`, `RolePermissionBaseRepositoryJPA`, `RolePermissionDataRepositoryJPA`, `SmsBlackListRepositoryJPA`, `SysMenuRepositoryJPA`, `SysRoleMenuRepositoryJPA`, `SysRoleRepositoryJPA`, `SystemParameterRepositoryJPA`, `UserOrgMapRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `NodeActionRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `SecurityTypeRepositoryJPA`, `StaffImageSignJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextDraftHistoryRepositoryJPA`, `TextDraftRepositoryJPA`, `AttachHistoryRepositoryJPA`, `FileEncryptMapHistoryJPA`, `LogTranstionSignRepositoryJPA`, `MessageJPA`, `NodeRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/textAction/getTextDetail` | `getTextDetail` |
| POST | `/textAction/getTextDetailV2` | `getTextDetailV2` |
| POST | `/textAction/searchText` | `searchText` |
| POST | `/textAction/searchOutgoingTextV2` | `searchOutgoingTextV2` |
| POST | `/textAction/searchTextExport` | `searchTextExport` |
| POST | `/textAction/searchTextForSubmission` | `searchTextForSubmission` |
| POST | `/textAction/searchTextForReminder` | `searchTextForReminder` |
| POST | `/textAction/searchTextAll` | `searchTextAll` |
| POST | `/textAction/rejectSignDocByVTAction` | `rejectSignDocByVTAction` |
| POST | `/textAction/updateReadingStatusV2` | `updateReadingStatusV2` |
| POST | `/textAction/updateUnReadingStatusV2` | `updateUnReadingStatusV2` |
| POST | `/textAction/updateReadingStatus` | `updateReadingStatus` |
| POST | `/textAction/transferToPreSigner` | `transferToPreSigner` |
| POST | `/textAction/transferGiveAdvice` | `transferGiveAdvice` |
| POST | `/textAction/tranferProofreadingAsistant` | `tranferProofreadingAsistant` |
| POST | `/textAction/checkShowTransferGiveAdvice/{textId}` | `checkShowTransferGiveAdvice` |
| POST | `/textAction/updateSigner` | `updateSigner` |
| POST | `/textAction/updateListSigner` | `updateListSigner` |
| POST | `/textAction/documentPromulgate` | `documentPromulgate` |
| POST | `/textAction/cancelDocumentPublish` | `cancelDocumentPublish` |
| POST | `/textAction/updateDatabaseSign` | `updateDatabaseSign` |
| POST | `/textAction/updateGiveAdvice` | `updateGiveAdvice` |
| POST | `/textAction/updateProofreader` | `updateProofreader` |
| POST | `/textAction/updateDatabaseMultiSign` | `updateDatabaseMultiSign` |
| POST | `/textAction/rejectSignDocument` | `rejectSignDocument` |
| POST | `/textAction/getListSigner` | `getListSigner` |
| POST | `/textAction/countTextSignAll` | `countTextSignAll` |
| POST | `/textAction/getCountHome` | `getCountHome` |
| POST | `/textAction/getCountTextDashboard` | `getCountTextDashboard` |
| POST | `/textAction/synchonizeCertificate` | `synchonizeCertificate` |
| POST | `/textAction/getCertificateSynchronization` | `getCertificateSynchronization` |
| POST | `/textAction/getListRegisterNumber` | `getListRegisterNumber` |
| POST | `/textAction/getListSignerNext` | `getListSignerNext` |
| POST | `/textAction/updateSignImageBySecrectary` | `updateSignImageBySecrectary` |
| POST | `/textAction/IdentifyObjectByUser` | `identifyObjectByUser` |
| POST | `/textAction/AddAttachmentForText` | `addAttachmentForText` |
| POST | `/textAction/GetHistoryOfSignerChange` | `getHistoryOfSignerChange` |
| POST | `/textAction/CheckTextWaitingForSignOfUser` | `checkTextWaitingForSignOfUser` |
| POST | `/textAction/getOrgMarkedList` | `getOrgMarkedList` |
| POST | `/textAction/askForSeal` | `askForSeal` |
| POST | `/textAction/rejectMark` | `rejectMark` |
| POST | `/textAction/rejectSignText` | `rejectSignText` |
| POST | `/textAction/returnCreatorTextByVtPromulgate` | `returnCreatorTextByVtPromulgate` |
| POST | `/textAction/rejectSignTextVBBHWaitForNumber` | `rejectSignTextVBBHWaitForNumber` |
| POST | `/textAction/markDocumentByOrg` | `markDocumentByOrg` |
| POST | `/textAction/markDocumentByOrgForConfirm` | `markDocumentByOrgForConfirm` |
| POST | `/textAction/getListOrgPermissionMark` | `getListOrgPermissionMark` |
| POST | `/textAction/getListOrgMark` | `getListOrgMark` |
| POST | `/textAction/getListSubmitterToMark` | `getListSubmitterToMark` |
| POST | `/textAction/markDocumentByOrgForBrief` | `markDocumentByOrgForBrief` |
| POST | `/textAction/rollBackDauDonVi` | `rollBackDauDonVi` |
| POST | `/textAction/rollBackBrief` | `rollBackBrief` |
| POST | `/textAction/getLocationSignature` | `getLocationSignature` |
| POST | `/textAction/getDefaultMarkLocationByTextId` | `getDefaultMarkLocationByTextId` |
| POST | `/textAction/getLastSignImageOfText` | `getLastSignImageOfText` |
| POST | `/textAction/checkSpellText` | `checkSpellText` |
| POST | `/textAction/checkSpellActive` | `checkSpellActive` |
| POST | `/textAction/updateUserSignMethod` | `updateUserSignMethod` |
| POST | `/textAction/getListCloudCertificates` | `getListCloudCertificates` |
| POST | `/textAction/checkHaveCloudCertificates` | `checkHaveCloudCertificates` |
| POST | `/textAction/getUserSignMethod` | `getUserSignMethod` |
| POST | `/textAction/updateDefaultCloudCert` | `updateDefaultCloudCert` |
| POST | `/textAction/getListCloudRegisteredDevices` | `getListCloudRegisteredDevices` |
| POST | `/textAction/checkUserInCloudCAConfig` | `checkUserInCloudCAConfig` |
| POST | `/textAction/getCloudCAClientConfig` | `getCloudCAClientUrl` |
| POST | `/textAction/deleteRequisition` | `deleteRequisition` |
| POST | `/textAction/softDeleteRejectedDraft` | `softDeleteRejectedDraft` |
| POST | `/textAction/deleteDocDraftBrief` | `deleteText` |
| POST | `/textAction/addDocDraftToBrief` | `addDocDraftToBrief` |
| POST | `/textAction/getUserMySign` | `getUserMySign` |
| POST | `/textAction/updateUserMySign` | `updateUserMySign` |
| POST | `/textAction/getPeopleInApprovalFlow` | `getPeopleInApprovalFlow` |
| POST | `/textAction/lockDocument` | `lockDocument` |
| POST | `/textAction/unLockDocument` | `unLockDocument` |
| POST | `/textAction/getListOrgMultiMarkRequisition` | `getListOrgMultiMarkRequisition` |
| POST | `/textAction/updateAutoPromulgateText` | `updateAutoPromulgateText` |
| POST | `/textAction/getListSignerBySignatureTypeApprovalAndSignFlash` | `getListSignerBySignatureTypeApprovalAndSignFlash` |
| POST | `/textAction/getListTextSignNext` | `getListTextSignNext` |
| POST | `/textAction/saveTextExplanation` | `saveTextExplanation` |
| POST | `/textAction/getListTextExplanation` | `getListTextExplanation` |
| POST | `/textAction/deleteExplanation` | `deleteExplanation` |
| POST | `/textAction/updateTextExplanation` | `updateTextExplanation` |
| POST | `/textAction/exportSearchText` | `exportSearchText` |
| POST | `/textAction/getPermissionViewCommentSignatureTypes` | `getPermissionViewCommentSignatureTypes` |
| POST | `/textAction/get-count-docs-by-creator` | `countDocsByCreator` |
| GET | `/textAction/get-reject-history/{textId}` | `getRejectHistory` |
| GET | `/textAction/get-text-process/{textProcessId}` | `getTextProcessById` |
| GET | `/textAction/get-text-process` | `getTextProcessByTextIdAndSignType` |
| POST | `/textAction/doDeleteRequisition` | `doDeleteRequisition` |
| POST | `/textAction/countDocSendSearch` | `countDocSendSearch` |
| POST | `/textAction/getIfUsersExistInProcess` | `getIfUsersExistInProcess` |
| GET | `/textAction/isSubmissionAttachmentValidForDraft` | `isSubmissionAttachmentValidForDraft` |
| POST | `/textAction/getAutoSendText` | `getAutoSendText` |
| POST | `/textAction/getCountXlcvDashboard` | `getCountXlcvDashboard` |
| POST | `/textAction/restoreDocument` | `restoreDocument` |
| POST | `/textAction/getStatusAutoSendText` | `getStatusAutoSendText` |
| POST | `/textAction/countMainSigningFilePages` | `countMainSigningFilePages` |

</details>

### TextFileCommentAction (gen1) — base `/TextFileCommentAction`, 7 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TextFileCommentAction.java`

- Logic (gen-1 `controler/`): `TextFileCommentControler`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `TextFileCommentDAO`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `DUOC`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `TEXT_ATTACH`, `TEXT_ATTACH_OTHER`, `TEXT_NOTE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/TextFileCommentAction/updateTextFileComment` | `updateTextFileComment` |
| POST | `/TextFileCommentAction/updateListTextFileComment` | `updateListTextFileComment` |
| POST | `/TextFileCommentAction/deleteTextNote` | `deleteTextNote` |
| POST | `/TextFileCommentAction/getListTextNote` | `getListTextNote` |
| POST | `/TextFileCommentAction/insertTextNote` | `insertTextNote` |
| POST | `/TextFileCommentAction/resetFileCommentDraff` | `resetFileCommentDraff` |
| POST | `/TextFileCommentAction/resetTextAttachComment` | `resetTextAttachComment` |

</details>

### TextMarkSyncAction (gen1) — base `/textMarkSyncAction`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TextMarkSyncAction.java`

- Logic (gen-1 `controler/`): `TextMarkSyncControler`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `TextMarkSyncDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `DOCUMENT`, `DOCUMENT_TYPE`, `STAFF`, `TEXT`, `TEXT_MARK_SYNC`, `TEXT_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/textMarkSyncAction/addTextMarkSync` | `addTextMarkSync` |
| POST | `/textMarkSyncAction/getTextMarkSync` | `getTextMarkSync` |
| POST | `/textMarkSyncAction/getListDocumentSync` | `getListDocumentSync` |
| POST | `/textMarkSyncAction/getTextDetailSync` | `getTextDetailSync` |

</details>

### DocOutController (gen2) — base `/api/doc-out`, 12 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocOutController.java`

- Service: `DocOutService`, `DocOutServiceImpl`
- DAO (SQL thuần): `DocumentDAO`, `FilesAttachmentDAO`, `TextDAO`
- Repository (JPA): `AttachRepositoryJPA`, `FileEncryptMapJPA`, `NodeActionRepositoryJPA`, `PositionRepositoryJPA`, `ReportDailyHistoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_USER_DOCUMENT`, `CONNECT_DOCUMENT`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `FILES_ATTACHMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `NODE_ACTION`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/doc-out/get-text-process-flow/{textId}` | `getTextProcessFlow` |
| GET | `/api/doc-out/is-duplicated-register-number` | `checkExistRegisterBookNumber` |
| GET | `/api/doc-out/get-file-encrypt-map/{attachId}` | `getFileEncryptMap` |
| GET | `/api/doc-out/get-all-file-encrypt-map-by-fileId/{attachId}` | `getAllFileEncryptMap` |
| GET | `/api/doc-out/get-list-file-encrypt-map/{textId}` | `findTextFileEncryptByTexId` |
| POST | `/api/doc-out/get-list-file-encrypt-map-by-text-ids` | `findTextFileEncryptByTexIds` |
| GET | `/api/doc-out/get-permisison-file-encrypt-map/{textId}` | `permissionFileEncryptByTexId` |
| GET | `/api/doc-out/get-list-file-encrypt-map-by-ids/{strTextIds}` | `findTextFileEncryptByTextIds` |
| GET | `/api/doc-out/get-list-document-completes/{documentId}` | `getlistDocCompletes` |
| POST | `/api/doc-out/add-permission-confidential-file` | `addPermissionConfidentialFile` |
| GET | `/api/doc-out/get-json-file-encrypt/{textId}` | `findJsonFileEncryptByTextId` |
| GET | `/api/doc-out/get-org-json-file-encrypt/{textId}` | `findOrgJsonFileEncryptByTextId` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

_Không có facade legacy riêng._

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `TextEntity`→`TEXT`, `TextProcessEntity`→`TEXT_PROCESS`, `TextProcessHistoryEntity`→`TEXT_PROCESS_HISTORY`, `TextReceiverGroupDetailEntity`→`TEXT_RECEIVER_GROUP_DETAIL`, `WaitingNumberBookEntity`→`WAITING_NUMBER_BOOK`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MARK_SYNC`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_RECEIVER_GROUP_DETAIL`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`
