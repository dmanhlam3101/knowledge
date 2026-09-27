# Bản đồ hệ thống — Văn bản đến

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 71 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/answerDoc/answerDoc.zul` | `vm.document.AnswerDocumentVM` | `AnswerDocumentBusiness` | — | BE |
| `document/answerDoc/replyRequestDetail.zul` | `vm.document.ReplyRequestDetailVM` | `DocumentRequestBusiness` | — | BE |
| `document/answerDoc/replyRequestPopup.zul` | `vm.document.ReplyDocumentVM` | `DocumentBusiness`, `DocumentRequestBusiness`, `RequisitionBusiness` | — | BE |
| `document/orgFollower/orgFollowerDocIn.zul` | `vm.document.DocumentSearchVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/orgFollowerDocIn/orgFollowerDocIn.zul` | `vm.document.OrgFollowerDocInVM` | `DocumentBusiness`, `TextBookBusiness` | `ISysUser` | BE+LEGACY |
| `document/orgFollowerDocIn/orgFollowerDocIn_org.zul` | `vm.document.OrgFollowerDocInOrgSearchVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/orgFollowerDocIn/orgFollowerDocIn_person.zul` | `vm.document.OrgFollowerDocInPersonSearchVM` | `DocumentBusiness`, `DocumentProcessTermBusiness`, `TagDictionaryBusiness` | `SysMenuService` | BE+LEGACY |
| `document/process/popupCommentProcess.zul` | `vm.document.PopupCompleteDocumentVM` | `CommonBusiness`, `ReminderBusiness` | — | BE |
| `document/process/popupCompleteProcess.zul` | `vm.document.PopupCompleteDocumentVM` | `CommonBusiness`, `ReminderBusiness` | — | BE |
| `document/process/popupNoteDetail.zul` | `vm.document.PopupNoteDetailVM` | — | — | — |
| `document/process/popupReturnProcess.zul` | `vm.document.PopupCompleteDocumentVM` | `CommonBusiness`, `ReminderBusiness` | — | BE |
| `document/process/popupViewFlowDetail.zul` | `vm.document.PopupViewFlowDetailVM` | `DocumentBusiness` | — | BE |
| `document/process/viewFlow.zul` | `vm.document.PopupViewFlowVM` | — | — | — |
| `document/process/viewFlow_v2.zul` | `vm.document.PopupViewFlowVM` | — | — | — |
| `document/reportSendReceiveDoc/AddAttachFile.zul` | `vm.document.AddAttachFileVM` | `DocumentBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentRequestBusiness`, `SavePersonalDocBusiness`, `WOPIBusiness` | `ICommon`, `ISysOrganization` | BE+LEGACY |
| `document/reportSendReceiveDoc/DocumentReceive.zul` | `vm.document.DocumentReceviceVM` | — | — | ☠ VM không tồn tại |
| `document/reportSendReceiveDoc/archive_document.zul` | `vm.document.ArchiveDocumentVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/assignListMove.zul` | `vm.document.AssignMoveListVM` | — | — | ☠ VM không tồn tại |
| `document/reportSendReceiveDoc/detailVB_per_storage.zul` | `vm.document.DocumentViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CVGroupBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentRequestBusiness`, `FlowBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `ReminderBusiness`, `SavePersonalDocBusiness`, `ShareExtDocBusiness`, `TagDictionaryBusiness`, `WOPIBusiness` | `ICommon`, `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/dispatch_Book_List.zul` | `vm.document.BookDispatchVM` | — | `IBookDispatch` | LEGACY |
| `document/reportSendReceiveDoc/doc_org_all.zul` | `vm.document.DocOrgAllVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentCopyHistoryBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/doc_org_pending_processing_all_doc_manager.zul` | `vm.document.DocOrgAllVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentCopyHistoryBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/document.zul` | `vm.document.DocumentVM` | `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/documentFinance.zul` | `vm.document.DocumentFinanceVM` | `DocumentBusiness` | — | BE |
| `document/reportSendReceiveDoc/documentIn.zul` | `vm.document.DocumentInVM` | `AnswerDocumentBusiness`, `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/documentOut.zul` | `vm.document.DocumentOutVM` | `AnswerDocumentBusiness`, `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `ImageOrgBusiness`, `NotificationBusiness`, `ReminderBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `ISysUser`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/documentOut_dcs_dbh.zul` | `vm.document.DocumentOutVM` | `AnswerDocumentBusiness`, `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `ImageOrgBusiness`, `NotificationBusiness`, `ReminderBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `ISysUser`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/documentViewDetailAdvanced.zul` | `vm.document.DocumentViewDetailAdvancedVM` | `DocumentBusiness`, `MeetingAssistantBusiness` | — | BE |
| `document/reportSendReceiveDoc/document_consult.zul` | `vm.document.DocumentConsultVM` | — | — | — |
| `document/reportSendReceiveDoc/document_lookup.zul` | `vm.document.DocumentSearchVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/document_pending_processing.zul` | `vm.document.DocumentPendingProcessingVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentCopyHistoryBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentTypeBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ICommon`, `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/document_pending_reception.zul` | `vm.document.DocumentPendingReceptionVM` | `CategoryCommonBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/reportSendReceiveDoc/document_processed.zul` | `vm.document.DocumentProcessedVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentTypeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/document_receive_to_know.zul` | `vm.document.DocumentReceiveToKnowVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/document_return.zul` | `vm.document.DocumentReturnVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `HomeBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/document_returned.zul` | `vm.document.DocumentReturnedVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/documentorg.zul` | `vm.document.DocumentSysOrgVM` | `DocumentBusiness` | `IDocument` | BE+LEGACY |
| `document/reportSendReceiveDoc/issussDocument.zul` | `vm.document.DocumentLookUpVM` | `DocumentPublishBusiness`, `ImageOrgBusiness`, `RequisitionBusiness`, `TextBookBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/reportSendReceiveDoc/listDocumentSign.zul` | `vm.document.DocumentVM` | `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/listOrg.zul` | `vm.document.DocumentOrgVM` | — | — | — |
| `document/reportSendReceiveDoc/lookUpDispatchDocument.zul` | `vm.document.BookDispatchVM` | — | `IBookDispatch` | LEGACY |
| `document/reportSendReceiveDoc/popUpMoveList.zul` | `vm.document.DocumentLookUpMoveList` | `DocumentBusiness` | — | BE |
| `document/reportSendReceiveDoc/popupArchiveDocumentDetail.zul` | `vm.document.ArchiveDocumentViewDetailVM` | `DocumentBusiness`, `DocumentRequestBusiness`, `SavePersonalDocBusiness`, `WOPIBusiness` | `ICommon` | BE+LEGACY |
| `document/reportSendReceiveDoc/popupDetailGroupReceived.zul` | `vm.document.DetailGroupReceivedVM` | — | — | — |
| `document/reportSendReceiveDoc/popupExtSign.zul` | `vm.document.ExtSignViewDetailVM` | — | — | — |
| `document/reportSendReceiveDoc/popupGraspSituation.zul` | `vm.graspSituation.PopupGraspSituationVM` | `DocumentBusiness`, `GraspSituationBusiness` | `ICommon` | BE+LEGACY |
| `document/reportSendReceiveDoc/popupListReceived.zul` | `vm.document.DocumentListReceivedVM` | — | — | — |
| `document/reportSendReceiveDoc/popupReceiveDocument.zul` | `widget.PopupReceiveDocVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `DocumentProcessTermBusiness`, `RequisitionBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | — | BE |
| `document/reportSendReceiveDoc/popupReplyDocument.zul` | `vm.document.DocumentViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CVGroupBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentRequestBusiness`, `FlowBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `ReminderBusiness`, `SavePersonalDocBusiness`, `ShareExtDocBusiness`, `TagDictionaryBusiness`, `WOPIBusiness` | `ICommon`, `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/popupTransferGraspSituation.zul` | `vm.graspSituation.PopupTransferGraspSituationVM` | `GraspSituationBusiness` | — | BE |
| `document/reportSendReceiveDoc/popupVB.zul` | `vm.document.DocumentViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CVGroupBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentRequestBusiness`, `FlowBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `ReminderBusiness`, `SavePersonalDocBusiness`, `ShareExtDocBusiness`, `TagDictionaryBusiness`, `WOPIBusiness` | `ICommon`, `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/popupVBScheduleMeeting.zul` | `vm.document.DocumentScheduleMeetingDetailVm` | `DocumentBusiness`, `DocumentRequestBusiness`, `MeetingBusiness`, `ScheduleToMeetingDocumentBusiness`, `WOPIBusiness` | `ICommon`, `IMeeting` | BE+LEGACY |
| `document/reportSendReceiveDoc/popupVB_issue_number.zul` | `vm.document.DocumentViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CVGroupBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentProcessTermBusiness`, `DocumentPublishBusiness`, `DocumentRequestBusiness`, `FlowBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `ReminderBusiness`, `SavePersonalDocBusiness`, `ShareExtDocBusiness`, `TagDictionaryBusiness`, `WOPIBusiness` | `ICommon`, `ISysOrganization`, `SysMenuService` | BE+LEGACY |
| `document/reportSendReceiveDoc/reportContentSendReceiveDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/reportSendReceiveDoc/reportSendReceiveDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/requestToScheduleMeetingDoc/docScheduleMeeting.zul` | `vm.document.DocumentScheduleMeetingVM` | `ScheduleToMeetingDocumentBusiness` | — | BE |
| `document/transferDoc/configLimitTransfer.zul` | `vm.document.ConfigLimitTransferVM` | — | — | — |
| `document/transferDoc/popupTransferError.zul` | `vm.document.PopupTransferErrorVM` | — | — | — |
| `document/transferDoc/transferBriefDoc.zul` | `vm.document.TransferBriefDocVM` | `DocumentBusiness`, `EnterpriseBusiness`, `SearchSolrBusiness` | — | BE |
| `document/transferDoc/transferContentDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/transferDoc/transferDoc.zul` | `vm.document.TransferDocumentVM` | `CVGroupBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferDoc_flow.zul` | `vm.document.TransferDocumentVM` | `CVGroupBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferDoc_flow_multi.zul` | `vm.document.TransferDocumentMultipleVM` | `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `document/transferDoc/transferDoc_multi.zul` | `vm.document.TransferDocumentVM` | `CVGroupBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferFinanceDoc.zul` | `vm.document.TransferFinanceDocumentVM` | `DocumentBusiness` | — | BE |
| `document/transferDoc/transferGroupEditor.zul` | `vm.document.DocumentGroupEditorVM` | `CVGroupBusiness`, `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `document/transferDoc/transferGroupEditor_vbd.zul` | `vm.document.DocumentGroupEditorVM` | `CVGroupBusiness`, `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `document/transferDoc/transfer_doc_in_flow.zul` | `vm.document.TransferDocumentInVM` | `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `SearchSolrBusiness` | — | BE |
| `document/transferDoc/viewListEmployee.zul` | `vm.document.TransferDocViewLstEmployeeVM` | — | — | — |
| `document/transferDoc/viewListHistory.zul` | `vm.document.DocumentLogInfoVM` | `DocumentHistoryLogBusiness` | — | BE |
| `widgets/template/document/templateInputDoc_add.zul` | `vm.document.DocumentVM` | `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### AnswerDocumentBusiness

`web-spring/src/main/java/com/voffice/service/business/AnswerDocumentBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Files.downloadDocumentReplyAttach` | `/Files/downloadDocumentReplyAttach` | `FileService.downloadDocumentReplyAttach` | gen1 |
| `answerDocumentAction.cancelDocumentReply` | `/answerDocumentAction/cancelDocumentReply` | `AnswerDocumentAction.cancelDocumentReply` | gen1 |
| `answerDocumentAction.getListAnswerDocument` | `/answerDocumentAction/getListAnswerDocument` | `AnswerDocumentAction.getListAnswerDocument` | gen1 |
| `answerDocumentAction.getListGroupReceiverRequestResponse` | `/answerDocumentAction/getListGroupReceiverRequestResponse` | `AnswerDocumentAction.getListGroupReceiverRequestResponse` | gen1 |
| `answerDocumentAction.getListReplyDocument` | `/answerDocumentAction/getListReplyDocument` | `AnswerDocumentAction.getListReplyDocument` | gen1 |
| `answerDocumentAction.getRepliedDocumentIds` | `/answerDocumentAction/getRepliedDocumentIds` | `AnswerDocumentAction.getRepliedDocumentIds` | gen1 |
| `answerDocumentAction.getRepliedDocumentsWhenUpdate` | `/answerDocumentAction/getRepliedDocumentsWhenUpdate` | `AnswerDocumentAction.getRepliedDocumentsWhenUpdate` | gen1 |
| `answerDocumentAction.insertDocumentReply` | `/answerDocumentAction/insertDocumentReply` | `AnswerDocumentAction.insertDocumentReply` | gen1 |
| `answerDocumentAction.replyDocument` | `/answerDocumentAction/replyDocument` | `AnswerDocumentAction.replyDocument` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### AnswerDocumentAction (gen1) — base `/answerDocumentAction`, 16 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/AnswerDocumentAction.java`

- Logic (gen-1 `controler/`): `AnswerDocumentController`, `CommonControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `AnswerDocumentDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `LSTDOCID`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/answerDocumentAction/getListGroupReceiverRequestResponse` | `getListGroupReceiverRequestResponse` |
| POST | `/answerDocumentAction/insertDocumentReply` | `insertDocumentReply` |
| POST | `/answerDocumentAction/cancelDocumentReply` | `cancelDocumentReply` |
| POST | `/answerDocumentAction/getListAnswerDocument` | `getListAnswerDocument` |
| POST | `/answerDocumentAction/getListReplyDocument` | `getListReplyDocument` |
| POST | `/answerDocumentAction/getRepliedDocumentIds` | `getRepliedDocumentIds` |
| POST | `/answerDocumentAction/replyDocument` | `replyDocument` |
| POST | `/answerDocumentAction/sendDocumentReplyRequest` | `sendDocumentReplyRequest` |
| POST | `/answerDocumentAction/getChair` | `getChair` |
| POST | `/answerDocumentAction/getRequestedObject` | `getRequestedObject` |
| POST | `/answerDocumentAction/deleteRequestedObject` | `deleteRequestedObject` |
| POST | `/answerDocumentAction/getRelyRequestPermission` | `getRelyRequestPermission` |
| POST | `/answerDocumentAction/replyDocumentUpdate` | `replyDocumentUpdate` |
| POST | `/answerDocumentAction/getReplyRequestDetail` | `getReplyRequestDetail` |
| POST | `/answerDocumentAction/getReturnList` | `getReturnList` |
| POST | `/answerDocumentAction/getRepliedDocumentsWhenUpdate` | `getRepliedDocumentsWhenUpdate` |

</details>

### DocumentInController (gen1) — base `/api/document-in`, 3 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/controler/DocumentInController.java`

- Service: `DocumentInService`, `DocumentInServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `DocumentInDAO`, `DocumentInStaffDAO`
- Repository (JPA): `DocumentRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CV_GROUP`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `MISSION`, `POSITION`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `SYSTIMESTAMP`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/document-in/get-list-receiver-text-transfer` | `getListReceiverTextTransfer` |
| POST | `/api/document-in/get-list-cv-group` | `getListCvGroup` |
| POST | `/api/document-in/get-documents-processing-stats-by-user` | `getDocumentsProcessingStatsByUser` |

</details>

### DocInController (gen2) — base `/api/doc-in`, 28 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocInController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `DocInService`, `DocInServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `GROUP_MAPPING`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MISSION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/doc-in/retrieval-doc-in-group/{doc-in-group-id}` | `retrievalDocInGroup` |
| POST | `/api/doc-in/retrieval-doc-in-cv-group/{doc-in-cv-groupId}` | `retrievalDocumentInCvGroup` |
| POST | `/api/doc-in/mark-received-know-doc/{doc-id}` | `markReceivedKnowDoc` |
| POST | `/api/doc-in/complete-document` | `completeDocument` |
| POST | `/api/doc-in/check-completion-reminders` | `checkCompletionReminders` |
| POST | `/api/doc-in/return-document` | `returnDocument` |
| GET | `/api/doc-in/get-pending-doc-in/{documentId}` | `getPendingDocuments` |
| GET | `/api/doc-in/get-pending-doc-in-reminder-reply-flow/{reminderReplyId}` | `getPendingDocumentsInReminderReplyFlow` |
| GET | `/api/doc-in/get-pending-doc-in-informality/{documentId}` | `getPendingInformalityDocuments` |
| GET | `/api/doc-in/get-doc-in-flows/{documentId}` | `getDocumentFlows` |
| GET | `/api/doc-in/is-duplicated-register-number` | `completeDocument` |
| GET | `/api/doc-in/is-duplicated-register-book-number` | `checkExistRegisterBookNumber` |
| POST | `/api/doc-in/list-exist-document` | `getListExistDocument` |
| POST | `/api/doc-in/list-exist-document-by-textbook-and-register` | `getListDocumentExistByTextBookAndRegisterNumber` |
| POST | `/api/doc-in/update-status-document-in-staff` | `updateStatusDocumentInStaff` |
| POST | `/api/doc-in/update-status-document-in-group` | `updateStatusDocumentInGroup` |
| POST | `/api/doc-in/update-exist-connect-document` | `updateExistConnectDocument` |
| GET | `/api/doc-in/get-doc-transfer-flow/{documentId}` | `getDocTransferFlow` |
| GET | `/api/doc-in/get-file-encrypt-map/{fileId}` | `getFileEncryptMap` |
| GET | `/api/doc-in/get-all-file-encrypt-map-by-fileId/{fileId}` | `getAllFileEncryptMap` |
| GET | `/api/doc-in/get-list-file-encrypt-map/{docId}` | `findDocFileEncryptByDocId` |
| GET | `/api/doc-in/is-existing-send-to-preside` | `isExistingSendToPreside` |
| GET | `/api/doc-in/transferred` | `getTransferredList` |
| GET | `/api/doc-in/node-detail` | `getNodeDetail` |
| GET | `/api/doc-in/node-detail2` | `getNodeDetail2` |
| POST | `/api/doc-in/documents/file-encrypt-map` | `findDocFileEncryptByDocIds` |
| GET | `/api/doc-in/issued/encrypted-files` | `getEncryptedFilesForIssuedDoc` |
| POST | `/api/doc-in/update-status-dis-proposal` | `updateStatusDisWhenAcceptProposal` |

</details>

### DocLeaderCommentController (gen2) — base `/api/doc-leader-comment`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocLeaderCommentController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `DocLeaderCommentService`, `DocLeaderCommentServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `InternalDocumentService`, `InternalDocumentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `GROUP_MAPPING`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `READ_NOTICE_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_NOTE`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/doc-leader-comment/save-doc-leader-comment` | `saveDocumentLeaderComment` |
| GET | `/api/doc-leader-comment/get-doc-leader-comments` | `getDocumentLeaderComments` |

</details>

### DocumentInformalityController (gen2) — base `/api/document-informality`, 16 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocumentInformalityController.java`

- Service: `DocumentInformalityService`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/document-informality/create-or-update` | `createOrUpdate` |
| GET | `/api/document-informality/get-group-doc-lead-type` | `getGroupDocumentLeadType` |
| GET | `/api/document-informality/search` | `search` |
| GET | `/api/document-informality/detail/{documentId}` | `getDetail` |
| POST | `/api/document-informality/send` | `send` |
| POST | `/api/document-informality/delete/{documentId}` | `deleteDocument` |
| POST | `/api/document-informality/mark-as-read/{documentId}` | `markAsRead` |
| GET | `/api/document-informality/count-read` | `countRead` |
| POST | `/api/document-informality/count-read` | `countReadPost` |
| POST | `/api/document-informality/update-to-informality/{documentId}` | `updateToInformality` |
| GET | `/api/document-informality/is-document-assistant` | `isDocumentAssistant` |
| GET | `/api/document-informality/get-leader-same-receive/{documentId}` | `getLeaderSameReceive` |
| GET | `/api/document-informality/get-permission-view-file/doc-informality/{docInformalityId}/{attachId}` | `getPermissionViewFileByDocInformalityIdAndAttachId` |
| GET | `/api/document-informality/get-permission-view-file/doc/{docId}/{attachId}` | `getPermissionViewFileByDocIdAndAttachId` |
| GET | `/api/document-informality/get-list-file-encrypt-map/{docId}` | `findDocFileEncryptByDocId` |
| POST | `/api/document-informality/insert-permission-for-supplier` | `insertPermissionForSupplier` |

</details>

### DocumentInformalityGroupController (gen2) — base `/api/document-informality-group`, 0 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocumentInformalityGroupController.java`

- Service: `DocumentInformalityGroupService`, `DocumentInformalityGroupServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

_Không có facade legacy riêng._

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `DocumentInCvGroupEntity`→`DOCUMENT_IN_CV_GROUP`, `DocumentInFileEntity`→`DOCUMENT_IN_FILE`, `DocumentInGroupEntity`→`DOCUMENT_IN_GROUP`, `DocumentInListRequestEntity`→`DOCUMENT_IN_LIST_REQUEST`, `DocumentInStaffEntity`→`DOCUMENT_IN_STAFF`, `DocumentInformality`→`DOCUMENT_INFORMALITY`, `DocumentInformalityAttach`→`DOCUMENT_INFORMALITY_ATTACH`, `DocumentInformalityGroupEntity`→`DOCUMENTINFORMALITYGROUPENTITY`, `DocumentInformalityStaff`→`DOCUMENT_INFORMALITY_STAFF`, `DocumentReceiveMapEntity`→`DOCUMENT_RECEIVE_MAP`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENTINFORMALITYGROUPENTITY`, `DOCUMENT_INFORMALITY`, `DOCUMENT_INFORMALITY_ATTACH`, `DOCUMENT_INFORMALITY_STAFF`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LSTDOCID`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`
