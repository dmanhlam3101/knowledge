# Bản đồ hệ thống — Dùng chung: widget, chat, comment, file, common

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 93 màn hình, 12 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `chat/chat.zul` | `vm.chat.ChatVM` | — | — | — |
| `chat/comment.zul` | `vm.chat.CommentVM` | `CommentBusiness` | — | BE |
| `chat/offline_messages.zul` | `org.zkforge.chat.ChatOfflineMessageVM` | — | — | ☠ VM không tồn tại |
| `mail/mail_receive.zul` | `mail.MailReceiveVM` | — | — | ☠ VM không tồn tại |
| `mail/mail_send.zul` | `mail.MailSendVM` | — | — | ☠ VM không tồn tại |
| `search/popupChooseCondition.zul` | `vm.search.ChooseConditionVM` | — | — | — |
| `search/search_all.zul` | `vm.search.SearchAllVM` | `CommonBusiness` | `ISysMenu` | BE+LEGACY |
| `widgets/addInforDocBonus.zul` | `vm.document.AddInforDocBonusVM` | `DocumentBusiness` | — | BE |
| `widgets/changeSignerLookup.zul` | `widget.ChangeSignerVM` | — | — | — |
| `widgets/confirmApproveTaskProgress.zul` | `widget.ConfirmApproveTaskProgressVM` | `TaskBusiness` | `ITaskRating`, `IVps` | BE+LEGACY |
| `widgets/confirmExportGroupDoc.zul` | `widget.ConfirmExportGroupDocVM` | — | — | — |
| `widgets/confirmExportTask.zul` | `widget.ConfirmExportTaskVM` | `TaskBusiness` | `IEmpRating`, `ITask`, `IVps` | BE+LEGACY |
| `widgets/confirmLock.zul` | `widget.ConfirmLockVM` | — | — | — |
| `widgets/confirmRetrieveDocConnect.zul` | `widget.ConfirmRetrieveDocConnectPopupVM` | — | — | — |
| `widgets/confirmSign.zul` | `widget.ConfirmSignVM` | `DocumentBusiness`, `SearchSolrBusiness`, `TextBookBusiness` | `ISysOrganization` | BE+LEGACY |
| `widgets/createGroupSmartOfficeChat.zul` | `widget.CreateGroupSmartOfficeChatLookup` | — | — | ☠ VM không tồn tại |
| `widgets/createNote.zul` | `widget.CreateNoteVM` | `DocumentBusiness` | — | BE |
| `widgets/duplicateDocumentPopup.zul` | `widget.DuplicateDocumentPopupVM` | — | — | — |
| `widgets/editNote.zul` | `widget.EditNoteVM` | `DocumentBusiness` | — | BE |
| `widgets/forwardToAssignNumber.zul` | `widget.ForwardToAssignNumberVM` | `DocumentBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | — | BE |
| `widgets/giveAdvice.zul` | `widget.GiveAdviceVM` | — | — | — |
| `widgets/lookupCopySendText.zul` | `widget.SourceLookupCopySendText` | — | — | ☠ VM không tồn tại |
| `widgets/messageBoxCustom.zul` | `widget.MessageBoxCustomVM` | — | — | — |
| `widgets/multiplePdfViewer.zul` | `widget.MultiplePdfViewerVM` | `RequisitionBusiness` | — | BE |
| `widgets/noteOfProofreader.zul` | `widget.NoteOfProofreaderVM` | `RequisitionBusiness` | — | BE |
| `widgets/organizationSelector.zul` | `widget.OrganizationSelectorVM` | `RequisitionBusiness` | — | BE |
| `widgets/pdfViewer.zul` | `widget.PdfViewerVM` | — | — | — |
| `widgets/pdfViewerFile.zul` | `widget.PdfViewerFileVM` | — | — | — |
| `widgets/popupChooseOrg.zul` | `widget.PopupChosseOrgVM` | — | — | — |
| `widgets/popupCreateTask.zul` | `widget.PopupCreateMissionVM` | — | — | — |
| `widgets/popupDetailEmp.zul` | `vps.vm.SysUserVM` | `DocumentProcessTermBusiness`, `FlowBusiness`, `ImageOrgBusiness`, `RequisitionBusiness` | `ISysUser` | BE+LEGACY |
| `widgets/popupDocumentDirection.zul` | `widget.DocumentDirectionVM` | — | — | — |
| `widgets/popupFileSignList.zul` | `widget.PopupFileSignListVM` | — | — | — |
| `widgets/popupInfoAutoTransDocToLib.zul` | `widget.InfoAutoTransDoctoLibVM` | `DocumentBusiness`, `DocumentPublishBusiness` | `ICommonVoffice` | BE+LEGACY |
| `widgets/popupInfoHastag.zul` | `widget.InfoHastagDoc` | — | — | ☠ VM không tồn tại |
| `widgets/popupInfoSelectBaseDoc.zul` | `widget.InfoSelectBaseDocVM` | `DocumentBusiness` | — | BE |
| `widgets/popupInfoSelectOrgPublishAdjacent.zul` | `widget.InfoSelectOrgPublishAdjacentVM` | — | — | — |
| `widgets/popupListGroupChat.zul` | `widget.ListGroupChatLookupVM` | — | — | — |
| `widgets/popupListSubTask.zul` | `widget.PopupViewListSubTaskVM` | — | — | — |
| `widgets/popupReNameFile.zul` | `widget.PopupRenameFileVM` | — | — | — |
| `widgets/popupRequestResponse.zul` | `widget.RequestResponseVM` | `AnswerDocumentBusiness`, `DocumentRequestBusiness` | — | BE |
| `widgets/popupSelectAnnexFile.zul` | `widget.PopupSelectAnnexFileVM` | — | — | — |
| `widgets/popupSelectFileTransfer.zul` | `widget.PopupSelectFileTransferVM` | — | — | — |
| `widgets/popupSelectOrgMark.zul` | `widget.PopupSelectOrgMarkVM` | `RequisitionBusiness` | — | BE |
| `widgets/popupSelectPartner.zul` | `widget.PopupSelectPartnerVM` | `EnterpriseBusiness` | `IEnterprise` | BE+LEGACY |
| `widgets/popupSignTextByCASim.zul` | `widget.PopupSignTextByCASimVM` | — | — | — |
| `widgets/popupSummarize.zul` | `widget.DocumentSummarizeVM` | — | — | — |
| `widgets/popupTextExplanation.zul` | `widget.PopupTextExplanationVM` | `RequisitionBusiness` | — | BE |
| `widgets/popupTextRejectedList.zul` | `widget.PopupTextRejectedListVM` | — | — | — |
| `widgets/popupTrackingDocument.zul` | `widget.PopupTrackingDocument` | — | — | ☠ VM không tồn tại |
| `widgets/popupViewReport.zul` | `widget.PopupViewReportVM` | — | — | — |
| `widgets/popupWriteReport.zul` | `widget.PopupWriteReportVM` | `RequisitionBusiness` | — | BE |
| `widgets/requestLookup.zul` | `widget.RequestLookupVM` | — | — | — |
| `widgets/securityPdfViewer.zul` | `widget.SecurityPdfViewerVM` | `DocumentBusiness`, `ImageOrgBusiness`, `RequisitionBusiness`, `WOPIBusiness` | `ISysOrganization` | BE+LEGACY |
| `widgets/sourceLookupDocument.zul` | `widget.SourceLookupDocumentVM` | — | — | — |
| `widgets/sourceLookupDocument2.zul` | `widget.SourceLookupDocumentVM2` | — | — | ☠ VM không tồn tại |
| `widgets/sourceLookupDocument3.zul` | `widget.SourceLookupDocumentVM3` | — | — | ☠ VM không tồn tại |
| `widgets/sourceLookupDocumentAll.zul` | `widget.SourceLookupDocumentAllVM` | `AnswerDocumentBusiness`, `DocumentBusiness` | — | BE |
| `widgets/sourceLookupDocumentOut.zul` | `widget.SourceLookupDocumentOut` | — | — | ☠ VM không tồn tại |
| `widgets/sourceLookupTask.zul` | `widget.SourceLookupTaskVM` | `DocumentBusiness`, `MeetingBusiness`, `TaskBusiness` | `ITask` | BE+LEGACY |
| `widgets/sourcePersonalDocument.zul` | `widget.SourcePersonalDocumentVM` | `DocumentBusiness` | — | BE |
| `widgets/spellErrorViewer.zul` | `widget.MultiplePdfViewerVM` | `RequisitionBusiness` | — | BE |
| `widgets/textExplanationDetail.zul` | `widget.TextExplanationDetailVM` | — | — | — |
| `widgets/alertLookup.zul` | `widget.AlertLookupVM` | — | — | — |
| `widgets/changeSignerHistory.zul` | `widget.ChangeSignerHistoryVM` | — | — | — |
| `widgets/cloud_ca_popup.zul` | `widget.CloudCAPopupVM` | `RequisitionBusiness` | — | BE |
| `widgets/commanderLookup.zul` | `widget.CommanderLookupVm` | — | — | ☠ VM không tồn tại |
| `widgets/commonUserLookup.zul` | `widget.UserLookupVM` | `CategoryCommonBusiness` | `ISysUser` | BE+LEGACY |
| `widgets/confirm.zul` | `widget.ConfirmVM` | — | — | — |
| `widgets/confirmApproved.zul` | `widget.ConfirmApprovedVM` | — | `IMission` | LEGACY |
| `widgets/confirmInput.zul` | `widget.ConfirmInputVM` | — | — | — |
| `widgets/confirmSplitDocument.zul` | `widget.ConfirmSplitDocumentVM` | `DocumentBusiness` | — | BE |
| `widgets/confirmSplitManualDocument.zul` | `widget.ConfirmSplitManualDocumentVM` | `DocumentBusiness` | — | BE |
| `widgets/createWorkLookup.zul` | `widget.WorkLookupVM` | — | — | — |
| `widgets/flowHistoryLookup.zul` | `widget.FlowHistoryLookupVM` | `FlowBusiness` | — | BE |
| `widgets/mainMenuTree.zul` | `widget.MainMenuTreeVM` | — | `ISysMenu` | LEGACY |
| `widgets/noteBook.zul` | `widget.NoteBookVM` | `MeetingBusiness` | — | BE |
| `widgets/objectSignLookup2.zul` | `widget.ObjectSignLookupVM2` | — | — | ☠ VM không tồn tại |
| `widgets/popupAddCert.zul` | `widget.PopupAddCertVM` | `RequisitionBusiness` | — | BE |
| `widgets/popupEditPageFile.zul` | `widget.EditPageFileVM` | `BriefBusiness`, `SubmissionFormBusiness` | — | BE |
| `widgets/processGroupWSLookup.zul` | `widget.ProcessGroupWSLookupVM` | `PersonalGroupBusiness` | — | BE |
| `widgets/processingObjectLookup.zul` | `widget.ProcessingObjectVM` | — | — | — |
| `widgets/savePerDoc.zul` | `widget.SavePerDocVM` | `MeetingBusiness`, `PersonalDocCategoryBusiness`, `SavePersonalDocBusiness` | — | BE |
| `widgets/subUserFlowLookup.zul` | `widget.SubUserFlowLookupVM` | `RequisitionBusiness`, `ScheduleConfigBusiness`, `TaskBusiness` | — | BE |
| `widgets/sysCatTypeLookup.zul` | `widget.SysCatTypeLookupVM` | — | — | — |
| `widgets/sysMenuLookup.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `widgets/sysMenuTree.zul` | `widget.MenuTreeVM` | — | — | ☠ VM không tồn tại |
| `widgets/sysOperationLookup.zul` | `widget.SysOperationLookupVM` | — | — | — |
| `widgets/userFlowLookup.zul` | `widget.UserFlowLookupVM` | `RequisitionBusiness`, `ScheduleConfigBusiness`, `TaskBusiness` | — | BE |
| `widgets/userLookup.zul` | `widget.UserLookupVM` | `CategoryCommonBusiness` | `ISysUser` | BE+LEGACY |
| `widgets/userLookupCustomerTask.zul` | `widget.UserLookupCustomerTaskVM` | `TaskBusiness` | `ISysUser` | BE+LEGACY |
| `widgets/userWSLookup.zul` | `widget.UserWSLookupVM` | `RequisitionBusiness`, `ScheduleConfigBusiness`, `TaskBusiness` | — | BE |
| `widgets/work_result.zul` | `widget.WorkGroupResultVM` | `WorkGroupHistoryBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `common.AttachmentVM` | — | — | — |
| `common.CommonLookupVM` | — | — | — |
| `common.CommonTreeVM` | — | — | — |
| `common.CommonVM` | — | `IVps` | LEGACY |
| `common.FileAttachmentVM` | — | — | — |
| `common.SimpleCommonVM` | — | — | — |
| `util.vm.VoChatUtils` | — | — | — |
| `util.vm.VoTaskUtils` | `DocumentBusiness` | `ICommon`, `IEmpRating`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `util.vm.WebServiceUtils` | — | — | — |
| `widget.AttachmentAppendixVM` | — | — | — |
| `widget.CommanderLookupVM` | `RequisitionBusiness`, `ScheduleConfigBusiness` | `IVps` | BE+LEGACY |
| `widget.SelectApproveMethodVM` | — | `IVps` | LEGACY |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### Business

`web-spring/src/main/java/com/voffice/service/business/Business.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|

### CommentBusiness

`web-spring/src/main/java/com/voffice/service/business/CommentBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `commentAction.addComment` | `/commentAction/addComment` | `CommentAction.addComment` | gen1 |
| `commentAction.getListComment` | `/commentAction/getListComment` | `CommentAction.getListComment` | gen1 |
| `commentAction.supportFinacialText` | `/commentAction/supportFinacialText` | `CommentAction.supportFinacialText` | gen1 |
| `commentAction.supportSystem` | `/commentAction/supportSystem` | `CommentAction.supportSystem` | gen1 |

### CommonBusiness

`web-spring/src/main/java/com/voffice/service/business/CommonBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Authenticate.logOut` | `/Authenticate/logOut` | `AuthenticateResource.logOut` | gen1 |
| `api.file-encrypt-map.get-list-file-encrypt-by-objectId` | `/api/file-encrypt-map/get-list-file-encrypt-by-objectId` | `FileEncryptMapController.getListFileEncryptByObjectId` | gen2 |
| `api.file-encrypt-map.get-list-file-encrypt-by-rootObjectId` | `/api/file-encrypt-map/get-list-file-encrypt-by-rootObjectId` | `FileEncryptMapController.getListFileEncryptByRootObjectId` | gen2 |
| `api.home.search-all` | `/api/home/search-all` | `HomeController.searchAll` | gen2 |
| `api.manager.checkConfigurationHomePageMode` | `/api/manager/checkConfigurationHomePageMode` | `ManagerController.checkConfigurationHomePageMode` | gen2 |
| `api.vhr-employee.find-nearest-landmark` | `/api/vhr-employee/find-nearest-landmark` | `VhrEmployeeController.getEmployeeById` | gen2 |
| `api.vhr-employee.get-employees-preside-by-org` | `/api/vhr-employee/get-employees-preside-by-org` | `VhrEmployeeController.getVhrEmployeePresideByOrganizationId` | gen2 |
| `api.vhr-employee.get-org-manager-list` | `/api/vhr-employee/get-org-manager-list` | `VhrEmployeeController.getEmployeeById` | gen2 |
| `api.vhr-employee.get-org-manager-list-for-consideration` | `/api/vhr-employee/get-org-manager-list-for-consideration` | `VhrEmployeeController.getLeadByListOrgIds` | gen2 |
| `api.vhr-org.get-list-org-level-one` | `/api/vhr-org/get-list-org-level-one` | `VhrOrgController.getListOrgLevelOne` | gen2 |
| `api.vhr-org.get-list-org-parent-child-level-once` | `/api/vhr-org/get-list-org-parent-child-level-once` | `VhrOrgController.findByOrgParentId` | gen2 |
| `api.vhr-org.get-org-child-leader` | `/api/vhr-org/get-org-child-leader` | `VhrOrgController.findOrgChildLeader` | gen2 |
| `api.vhr-org.get-org-leader` | `/api/vhr-org/get-org-leader` | `VhrOrgController.getOrgLeader` | gen2 |
| `commonAction.checkSameIdentifierCode` | `/commonAction/checkSameIdentifierCode` | `CommonAction.checkSameIdentifierCode` | gen1 |
| `commonAction.checkValidToConfigSubmitBrief` | `/commonAction/checkValidToConfigSubmitBrief` | `CommonAction.checkValidToConfigSubmitBrief` | gen1 |
| `commonAction.findOrgByCodition` | `/commonAction/findOrgByCodition` | `CommonAction.findOrgByCodition` | gen1 |
| `commonAction.getOrgById` | `/commonAction/getOrgById` | `CommonAction.getOrgById` | gen1 |
| `commonAction.getSysRole` | `/commonAction/getSysRole` | `IndexController.redirect` | gen2 |
| `commonAction.getSystemParameter` | `/commonAction/getSystemParameter` | `CommonAction.getSystemParameter` | gen1 |
| `commonAction.insertSysOrganization` | `/commonAction/insertSysOrganization` | `CommonAction.insertSysOrganization` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### CommentAction (gen1) — base `/commentAction`, 10 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CommentAction.java`

- Logic (gen-1 `controler/`): `CommentController`
- DAO (SQL thuần): `CommentDAO`, `CommonDataBaseDaoVO2`, `DemoDAO`, `DocumentDAO`, `DocumentInStaffDAO`, `MeetingDAO`, `ObjectTransferViaAxisDAO`, `UserDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `MEETING_RESOURCE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `P12_CERT`, `PERSONAL_STOTAGE`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `VOF_COMMENT`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/commentAction/getListComment` | `getListComment` |
| POST | `/commentAction/addComment` | `addComment` |
| POST | `/commentAction/supportFinacialText` | `supportFinacialText` |
| POST | `/commentAction/supportSystem` | `supportSystem` |
| POST | `/commentAction/savePersonalStorage` | `savePersonalStorage` |
| POST | `/commentAction/searchPeronalStorage` | `searchPeronalStorage` |
| POST | `/commentAction/checkSavedPersonalStorage` | `checkSavedPersonalStorage` |
| POST | `/commentAction/getPersonalStorageByObjTypeIdUser` | `getPersonalStorageByObjTypeIdUser` |
| POST | `/commentAction/updateCategoryOfPersonalStorage` | `updateCategoryOfPersonalStorage` |
| POST | `/commentAction/getIsActiveOrStatusNumber` | `getIsActiveOrStatusNumber` |

</details>

### CommonAction (gen1) — base `/commonAction`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CommonAction.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `GROUP_MAPPING`, `HOME_WIDGET`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `READ_NOTICE_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_NOTE`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/commonAction/getSupportCustomerInfo` | `getSupportCustomerInfo` |
| POST | `/commonAction/getSystemParameter` | `getSystemParameter` |
| POST | `/commonAction/getHomeWidgets` | `getHomeWidgets` |
| GET | `/commonAction/getSSOLink` | `getSSOLink` |
| POST | `/commonAction/getOrgById` | `getOrgById` |
| POST | `/commonAction/findOrgByCodition` | `findOrgByCodition` |
| POST | `/commonAction/insertSysOrganization` | `insertSysOrganization` |
| POST | `/commonAction/checkSameIdentifierCode` | `checkSameIdentifierCode` |
| POST | `/commonAction/checkValidToConfigSubmitBrief` | `checkValidToConfigSubmitBrief` |

</details>

### FileService (gen1) — base `/Files`, 47 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/FileService.java`

- Logic (gen-1 `controler/`): `FileControler`, `WOPIController`, `SignBriefcaseControler`, `TemplateController`, `TextMarkSyncControler`
- Service: `PdfOcrDocumentService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AttachDAO`, `BriefManagementDAO`, `CommonDataBaseDaoVO2`, `ConfigParameterDAO`, `ConnectDocumentDAO`, `DocumentDAO`, `DownloadAllFileDAO`, `DownloadFileCommentDAO`, `DownloadFileDocumentDAO`, `FilesAttachmentDAO`, `ImageDAO`, `ImageOrgDAO`, `OrgDAO`, `SystemParameterDAO`, `StaffImageSignDAO`, `TaskApprovalDAO`, `TaskDAO`, `TextDAO`, `TextProcessDAO`, `TextSearchDAO`, `SubmissionFormEditHistoryDAO`, `TextEditHistoryDAO`, `SignBriefcaseDAO`, `TemplateDAO`, `TextMarkSyncDAO`
- Repository (JPA): `BriefSubmitAttachFileEntityRepositoryJPA`, `BriefSubmitRequestEntityRepositoryJPA`, `VersionControlRepositoryJPA`, `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `SubmissionFileRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_BRIEFCASE`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CODE_MASTER`, `CONFIG_USER_DOCUMENT`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `NODE_ACTION`, `ORG_KI`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_PROCESS`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SIGN_BRIEFCASE`, `SIGN_BRIEFCASE_ATTACH`, `SIGN_BRIEFCASE_ATTACH_OTHER`, `SIGN_BRIEFCASE_SIGNER`, `SIGN_BRIEFCASE_STATUS`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_MARK_SYNC`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_ORG`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Files/Download` | `getFile` |
| POST | `/Files/FileSize` | `getFileSize` |
| POST | `/Files/DownloadContentFile` | `downloadContentFile` |
| POST | `/Files/DownloadStreamFile` | `downloadStreamFile` |
| POST | `/Files/DownloadStreamMigratedFile` | `downloadStreamMigratedFile` |
| POST | `/Files/DownloadDocumentErrorFile` | `downloadDocumentErrorFile` |
| POST | `/Files/downloadContentFileCommentSign` | `downloadContentFileCommentSign` |
| POST | `/Files/downloadDocumentReplyAttach` | `downloadDocumentReplyAttach` |
| POST | `/Files/getInfoFile` | `getInfoFile` |
| POST | `/Files/getInfoFileV2` | `getInfoFileV2` |
| POST | `/Files/UploadTmpFile` | `uploadTmpFile` |
| POST | `/Files/downloadTmpFile` | `downloadTmpFile` |
| POST | `/Files/UploadMultiTmpFile` | `UploadMultiTmpFile` |
| GET | `/Files/DownloadStaffImage/{cardId}/{size}` | `downloadStaffImage` |
| GET | `/Files/staff-image/{cardId}/{size}` | `downloadStaffImageBearer` |
| POST | `/Files/downloadTextMarkContentFile` | `downloadTextMarkContentFile` |
| POST | `/Files/printBarCode` | `printBarCode` |
| POST | `/Files/downloadFileSignBriefCase` | `downloadFileSignBriefCase` |
| GET | `/Files/downloadImageIconApp/{imageName}` | `downloadImageIconApp` |
| GET | `/Files/downloadImageReport/{imgName}` | `downloadImageReport` |
| POST | `/Files/updateFilePageFileSize` | `updateFilePageFileSize` |
| POST | `/Files/PreviewMeetingMinutes` | `previewMeetingMinutes` |
| POST | `/Files/PreviewEmpRatingReport` | `previewEmpRatingReport` |
| GET | `/Files/DownloadSignatureImage/{staffImageSignId}` | `downloadSignatureImage` |
| GET | `/Files/downloadSignatureImageViaToken/{staffImageSignId}` | `downloadSignatureImageViaToken` |
| GET | `/Files/downloadImageOrg/{imageOrgId}` | `downloadImageOrg` |
| GET | `/Files/downloadImageOrgViaToken/{imageOrgId}` | `downloadImageOrgViaToken` |
| POST | `/Files/PreviewAppendixChat` | `previewAppendixChat` |
| POST | `/Files/downloadFileTemplate` | `downloadFileTemplate` |
| GET | `/Files/DownloadImage/{imageId}` | `downloadSignatureImage` |
| GET | `/Files/DownloadSignatureImageByCardId/{cardId}/{signedDate}` | `downloadSignatureImageByCardId` |
| GET | `/Files/downloadAllDocumentFilesById/{encryptedDocumentId}/{fileName}` | `downloadAllDocumentFilesById` |
| GET | `/Files/downloadAllBriefFileByBriefDocumentId/{encryptedDocumentId}/{fileName}` | `downloadAllBriefFileByBriefDocumentId` |
| GET | `/Files/downloadAllBriefFileByBriefId/{encryptedDocumentId}/{fileName}` | `downloadAllBriefFileByBriefId` |
| GET | `/Files/downloadAllMigratedDocumentFilesById/{encryptedDocumentId}/{fileName}` | `downloadAllMigratedDocumentFilesById` |
| GET | `/Files/downloadAllOriginMigratedDocumentFilesById/{encryptedDocumentId}/{fileName}` | `downloadAllOriginMigratedDocumentFilesById` |
| GET | `/Files/download-all-file-by-document-id/{documentId}/{fileName}` | `downloadAllDocumentFilesById` |
| GET | `/Files/download-all-original-file-by-document-id/{documentId}/{fileName}` | `downloadAllOriginalDocumentFilesById` |
| GET | `/Files/downloadAllOriginalDocumentFilesById/{encryptedDocumentId}/{fileName}` | `downloadAllOriginalDocumentFilesById` |
| GET | `/Files/download-all-file-by-brief-submit-request-id/{briefSubmitRequestId}` | `downloadAllFilesByBriefSubmitRequestId` |
| POST | `/Files/extractOCRDocument` | `extractOCRDocument` |
| POST | `/Files/d2SOCRExtractDocument` | `d2SOCRExtractDocument` |
| POST | `/Files/d2SOCRSummarizeDocument` | `d2SOCRSummarizeDocument` |
| GET | `/Files/downloadDefaultImage/{type}` | `downloadDefaultImage` |
| POST | `/Files/convertLocalToPdf` | `convertLocalToPdf` |
| POST | `/Files/convertLocalToPdfLibre` | `convertLocalToPdfLibre` |
| GET | `/Files/downloadAllVersionControlFile/{encryptedDocumentId}/{fileName}` | `downloadAllVersionControlFile` |

</details>

### TextChatController (gen2) — base `/api/text-chat`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextChatController.java`

- Service: `TextChatService`, `TextChatServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Repository (JPA): `TextChatRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `TEXT_CHAT`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/text-chat/getAllByTextId` | `getAllByTextId` |
| POST | `/api/text-chat/add` | `addTextChat` |
| POST | `/api/text-chat/delete` | `deleteTextChat` |
| GET | `/api/text-chat/existsNoteByTextId/{textId}` | `deleteTextChat` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `BChatFacade` | `IBChat` | — | — | — |
| `CommonFacade` | `ICommon` | `CommonService` | — | — |
| `CommonVofficeFacade` | `ICommonVoffice` | `CommonVofficeService` | `SysRoleJpaDao`, `UserRoleJpaDao`, `VoMeetingMinutesUtilsJpaDao` | `MeetingMinutes (MEETING_MINUTES)`, `SysRole (SYS_ROLE)`, `UserRole (USER_ROLE)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `AttachEntity`→`ATTACH`, `AttachHistoryEntity`→`ATTACH_HISTORY`, `DocumentLeaderCommentEntity`→`DOCUMENT_LEADER_COMMENT`, `FeedbackImageEntity`→`FEEDBACK_IMAGE`, `FileAttachmentEntity`→`FILE_ATTACHMENT`, `FileAttachmentMapperEntity`→`FILE_ATTACHMENT_MAPPER`, `FilesAttachmentEntity`→`FILES_ATTACHMENT`, `FilesEntity`→`FILES`, `ImageEntity`→`IMAGE`, `TextAttachBaseEntity`→`TEXT_ATTACH_BASE`, `TextAttachEntity`→`TEXT_ATTACH`, `TextChatEntity`→`TEXT_CHAT`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `BChat`→`BCHAT`, `EmailDetail`→`EMAIL_DETAIL`, `EmailMaster`→`EMAIL_MASTER`, `FileAttachment`→`FILE_ATTACHMENT`, `FileAttachmentMapper`→`FILE_ATTACHMENT_MAPPER`, `Files`→`FILES`, `MailAction`→`MAIL_ACTION`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_BRIEFCASE`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BCHAT`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMAIL_DETAIL`, `EMAIL_MASTER`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `FEEDBACK_IMAGE`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `LOG_TRANSTION_SIGN`, `MAIL_ACTION`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `MEETING_RESOURCE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_KI`, `ORIENTATION`, `P12_CERT`, `PERSONAL_STOTAGE`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_PROCESS`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SIGN_BRIEFCASE`, `SIGN_BRIEFCASE_ATTACH`, `SIGN_BRIEFCASE_ATTACH_OTHER`, `SIGN_BRIEFCASE_SIGNER`, `SIGN_BRIEFCASE_STATUS`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_CHAT`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_MARK_SYNC`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `VOF_COMMENT`, `WORK_PROCESS`
