# Bản đồ hệ thống — Phiếu trình

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 24 màn hình, 3 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `admin/request/request.zul` | `vm.admin.RequestVM` | — | — | ☠ VM không tồn tại |
| `admin/request/request_popup.zul` | `vm.admin.RequestPopupVM` | — | — | ☠ VM không tồn tại |
| `request/request.zul` | `vm.request.RequestVM` | — | `IMeetingAssistant` | LEGACY |
| `request/request_detail.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/request_history_detail.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/widgets/close_request.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/widgets/reject_confirm_solution_request.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/widgets/request_task_mission_detail.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/widgets/send_to_heigher_solution.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/widgets/sole_myself_solution.zul` | `vm.request.RequestDetailVM` | — | `ISysOrganization` | LEGACY |
| `request/widgets/task_request_view.zul` | `vm.task.TaskViewDetailVM` | `DocumentBusiness`, `TaskBusiness` | `ITask` | BE+LEGACY |
| `submissionForm/confirmSignDocumentDraft.zul` | `vm.submissionForm.ConfirmSignDocumentDraftVM` | — | — | — |
| `submissionForm/submissionFormLeader.zul` | `vm.submissionForm.SubmissionFormLeaderVM` | `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SubmissionFormBusiness` | `ISysUser` | BE+LEGACY |
| `submissionForm/submissionFormList.zul` | `vm.submissionForm.SubmissionFormListVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CommonBusiness`, `DocumentBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `SubmissionFormBusiness`, `VhrEmployeeBusiness` | `ICommon`, `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `submissionForm/submissionFormProcessList.zul` | `vm.submissionForm.SubmissionFormListVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CommonBusiness`, `DocumentBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `SubmissionFormBusiness`, `VhrEmployeeBusiness` | `ICommon`, `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `submissionForm/submissionFormReceiveToKnow.zul` | `vm.submissionForm.SubmissionFormReceiveToKnowVM` | `NotificationBusiness`, `RequisitionBusiness`, `SubmissionFormBusiness` | — | BE |
| `submissionForm/transferSubmission.zul` | `vm.submissionForm.TransferSubmissionVM` | `SearchSolrBusiness`, `SubmissionFormBusiness` | — | BE |
| `widgets/approveSubmissionFormPopup.zul` | `widget.ApproveSubmissionFormPopupVM` | — | — | — |
| `widgets/lookupDocumentSubmission.zul` | `widget.SourceLookupSubmission` | — | — | ☠ VM không tồn tại |
| `widgets/lookupDocumentSubmissionBrief.zul` | `widget.SourceLookupSubmissionBrief` | — | — | ☠ VM không tồn tại |
| `widgets/popupCreateMissionSubmission.zul` | `widget.PopupCreateMissionSubmissionVM` | `MeetingBusiness`, `MissionBusiness` | — | BE |
| `widgets/popupSelectRequisitionForSubmission.zul` | `widget.PopupSelectRequisitionForSubmissionVM` | — | — | — |
| `widgets/previewSubmission.zul` | `widget.PreviewSubmissionVM` | `BriefBusiness`, `WOPIBusiness` | — | BE |
| `widgets/rejectSubmissionFormPopup.zul` | `widget.ApproveSubmissionFormPopupVM` | — | — | — |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.submissionForm.SubmissionDetailVM` | — | — | — |
| `vm.submissionForm.SubmissionFormSignVM` | — | `IRequisition` | LEGACY |
| `vm.submissionForm.SubmissionFormViewDetailVM` | `DocumentBusiness`, `EnterpriseBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `WOPIBusiness` | `IRequisition` | BE+LEGACY |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### ProposalBusiness

`web-spring/src/main/java/com/voffice/service/business/ProposalBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `requestAction.GetListRequestEmpConfig` | `/requestAction/GetListRequestEmpConfig` | `RequestAction.getListRequestEmpConfig` | gen1 |
| `requestAction.UpdateRequestEmpConfig` | `/requestAction/UpdateRequestEmpConfig` | `RequestAction.updateRequestEmpConfig` | gen1 |

### SubmissionFormBusiness

`web-spring/src/main/java/com/voffice/service/business/SubmissionFormBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.file-encrypt-map.get-list-file-encrypt-by-objectId` | `/api/file-encrypt-map/get-list-file-encrypt-by-objectId` | `FileEncryptMapController.getListFileEncryptByObjectId` | gen2 |
| `api.manager.get-list-user-last-sign-submissionform` | `/api/manager/get-list-user-last-sign-submissionform` | `ManagerController.getListUserLastSignSubmisionForm` | gen2 |
| `api.submission-manager.get-file-by-submission-form-id` | `/api/submission-manager/get-file-by-submission-form-id` | `SubmissionManagerController.getFileBySubmissionFormId` | gen2 |
| `api.submission-manager.get-file-encrypt-map` | `/api/submission-manager/get-file-encrypt-map` | `SubmissionManagerController.getFileEncryptMap` | gen2 |
| `api.submission-manager.get-json-file-encrypt` | `/api/submission-manager/get-json-file-encrypt` | `SubmissionManagerController.getJsonFileEncrypt` | gen2 |
| `api.submission-manager.get-org-file-encrypt-map` | `/api/submission-manager/get-org-file-encrypt-map` | `SubmissionManagerController.getOrgFileEncryptMap` | gen2 |
| `api.submission-manager.get-org-json-file-encrypt` | `/api/submission-manager/get-org-json-file-encrypt` | `SubmissionManagerController.getOrgJsonFileEncrypt` | gen2 |
| `api.submission-manager.list-file-encrypt-map` | `/api/submission-manager/list-file-encrypt-map` | `SubmissionManagerController.getFileEncryptMap` | gen2 |
| `api.submission-manager.submission-file.download` | `/api/submission-manager/submission-file/download` | `SubmissionManagerController.generatSubmissionFile` | gen2 |
| `api.submission-manager.submission-file.reject-sign` | `/api/submission-manager/submission-file/reject-sign` | `SubmissionManagerController.rejectSubmission` | gen2 |
| `api.submission-manager.submission-file.sign` | `/api/submission-manager/submission-file/sign` | `SubmissionManagerController.signSubmission` | gen2 |
| `api.submission-manager.submission-form` | `/api/submission-manager/submission-form` | `SubmissionManagerController.submissionGetDetail` | gen2 |
| `api.submission-manager.submission-form-by-text-id` | `/api/submission-manager/submission-form-by-text-id` | `SubmissionManagerController.findSubmissionFormByTextId` | gen2 |
| `api.submission-manager.submission-form.add-to-brief` | `/api/submission-manager/submission-form/add-to-brief` | `SubmissionManagerController.addToBrief` | gen2 |
| `api.submission-manager.submission-form.cancel` | `/api/submission-manager/submission-form/cancel` | `SubmissionManagerController.submissionGetDetail` | gen2 |
| `api.submission-manager.submission-form.check-submission-attachments-for-submitting` | `/api/submission-manager/submission-form/check-submission-attachments-for-submitting` | `SubmissionManagerController.checkSubmissionAttachmentsForSubmitting` | gen2 |
| `api.submission-manager.submission-form.create-or-update` | `/api/submission-manager/submission-form/create-or-update` | `SubmissionManagerController.createOrUpdate` | gen2 |
| `api.submission-manager.submission-form.delete` | `/api/submission-manager/submission-form/delete` | `SubmissionManagerController.submissionGetDetail` | gen2 |
| `api.submission-manager.submission-form.delete-from-brief` | `/api/submission-manager/submission-form/delete-from-brief` | `SubmissionManagerController.deleteFromBrief` | gen2 |
| `api.submission-manager.submission-form.get-list` | `/api/submission-manager/submission-form/get-list` | `SubmissionManagerController.submissionGetList` | gen2 |
| `api.submission-manager.submission-form.get-list-export` | `/api/submission-manager/submission-form/get-list-export` | `SubmissionManagerController.submissionGetListExport` | gen2 |
| `api.submission-manager.submission-form.get-list-for-brief` | `/api/submission-manager/submission-form/get-list-for-brief` | `SubmissionManagerController.submissionGetListForBrief` | gen2 |
| `api.submission-manager.submission-form.get-list-position` | `/api/submission-manager/submission-form/get-list-position` | `SubmissionManagerController.getListPosition` | gen2 |
| `api.submission-manager.submission-form.get-org-submission` | `/api/submission-manager/submission-form/get-org-submission` | `SubmissionManagerController.getListOrgSubmission` | gen2 |
| `api.submission-manager.submission-form.get-total-submission` | `/api/submission-manager/submission-form/get-total-submission` | `SubmissionManagerController.getTotalSubmission` | gen2 |
| `api.submission-manager.submission-form.list-brief-document-id` | `/api/submission-manager/submission-form/list-brief-document-id` | `SubmissionManagerController.getListBriefDocumentId` | gen2 |
| `api.submission-manager.submission-form.submit` | `/api/submission-manager/submission-form/submit` | `SubmissionManagerController.submitForm` | gen2 |
| `api.submission-manager.submission-form.tranfer-give-advice` | `/api/submission-manager/submission-form/tranfer-give-advice` | `SubmissionManagerController.tranferGiveAdvice` | gen2 |
| `api.submission-manager.submission-form.update-advice` | `/api/submission-manager/submission-form/update-advice` | `SubmissionManagerController.updateGiveAdviceState` | gen2 |
| `api.submission-manager.submission-form.update-num-page` | `/api/submission-manager/submission-form/update-num-page` | `SubmissionManagerController.updateNumPage` | gen2 |
| `api.submission-manager.submission-form.update-order` | `/api/submission-manager/submission-form/update-order` | `SubmissionManagerController.submissionGetDetail` | gen2 |
| `api.submission-manager.submission-form.updateFilePageInSubmissionMapFile` | `/api/submission-manager/submission-form/updateFilePageInSubmissionMapFile` | `SubmissionManagerController.updateFilePageInSubmissionMapFile` | gen2 |
| `api.submission-manager.submission-form.updatePaperNumberInSubmissionMap` | `/api/submission-manager/submission-form/updatePaperNumberInSubmissionMap` | `SubmissionManagerController.updatePaperNumberInSubmissionMap` | gen2 |
| `api.submission-manager.submission-forward` | ❓ không tìm thấy endpoint | | |
| `api.submission-manager.submission-forward.get-list-sender-history` | `/api/submission-manager/submission-forward/get-list-sender-history` | `SubmissionManagerController.getListSubmissionForwardHistory` | gen2 |
| `api.submission-manager.submission-forward.get-list-submission-forward` | `/api/submission-manager/submission-forward/get-list-submission-forward` | `SubmissionManagerController.getListSubmissionForwardBySearchCondition` | gen2 |
| `api.submission-manager.submission-forward.get-sent-userIds` | `/api/submission-manager/submission-forward/get-sent-userIds` | `SubmissionManagerController.getSentUserIds` | gen2 |
| `api.submission-manager.submission-forward.get-sub-forward-by-id` | `/api/submission-manager/submission-forward/get-sub-forward-by-id` | `SubmissionManagerController.getSubForWardById` | gen2 |
| `api.submission-manager.submission-forward.send` | `/api/submission-manager/submission-forward/send` | `SubmissionManagerController.submissionForwardCreate` | gen2 |
| `api.submission-manager.submission-forward.update-is-read` | `/api/submission-manager/submission-forward/update-is-read` | `SubmissionManagerController.updateIsRead` | gen2 |
| `api.submission-manager.submission-process` | `/api/submission-manager/submission-process` | `SubmissionManagerController.getSubmisisonProcess` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### RequestAction (gen1) — base `/requestAction`, 15 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/RequestAction.java`

- Logic (gen-1 `controler/`): `RequestController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `MeetingDAO`, `RequestDAO`, `RequestEmpConfigDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `MAIL_MEETING_HISTORY`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_RESOURCE`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TASK`, `TIME_ZONE_LOCAL`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/requestAction/getListRequest` | `getListRequest` |
| POST | `/requestAction/getListRequestAdvance` | `getListRequestAdvance` |
| POST | `/requestAction/getRequestDetail` | `getRequestDetail` |
| POST | `/requestAction/addRequest` | `addRequest` |
| POST | `/requestAction/deleteRequest` | `deleteRequest` |
| POST | `/requestAction/addResolve` | `addResolve` |
| POST | `/requestAction/forwardLevel` | `forwardLevel` |
| POST | `/requestAction/confirmSolutionRequest` | `confirmSolutionRequest` |
| POST | `/requestAction/closeRequest` | `closeRequest` |
| POST | `/requestAction/assignRequest` | `assignRequest` |
| POST | `/requestAction/sendRequest` | `sendRequest` |
| POST | `/requestAction/getRoleRequest` | `getRoleRequest` |
| POST | `/requestAction/getRequestId` | `getRequestId` |
| POST | `/requestAction/UpdateRequestEmpConfig` | `updateRequestEmpConfig` |
| POST | `/requestAction/GetListRequestEmpConfig` | `getListRequestEmpConfig` |

</details>

### SubmissionManagerController (gen2) — base `/api/submission-manager`, 47 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/SubmissionManagerController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `SubmissionForwardService`, `SubmissionForwardServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `TextDAO`, `DocumentDAO`, `FilesAttachmentDAO`, `DocumentSignDAO`, `P12CertDAO`, `StaffDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionForwardRepositoryJPA`, `BriefEntityRepositoryJPA`, `AttachRepositoryJPA`, `FileEncryptMapJPA`, `NodeActionRepositoryJPA`, `PositionRepositoryJPA`, `ReportDailyHistoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `NotificationRepositoryJPA`, `SecurityTypeRepositoryJPA`, `StaffImageSignJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_FORWARD`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/submission-manager/submission-form/get-list` | `submissionGetList` |
| GET | `/api/submission-manager/submission-form/get-list-export` | `submissionGetListExport` |
| GET | `/api/submission-manager/submission-form/get-list-for-brief` | `submissionGetListForBrief` |
| POST | `/api/submission-manager/submission-form/check-submission-attachments-for-submitting` | `checkSubmissionAttachmentsForSubmitting` |
| POST | `/api/submission-manager/submission-form/list-brief-document-id` | `getListBriefDocumentId` |
| POST | `/api/submission-manager/submission-form/add-to-brief/{briefId}` | `addToBrief` |
| POST | `/api/submission-manager/submission-form/delete-from-brief/{briefId}/{submissionFormId}` | `deleteFromBrief` |
| POST | `/api/submission-manager/submission-form/updatePaperNumberInSubmissionMap` | `updatePaperNumberInSubmissionMap` |
| POST | `/api/submission-manager/submission-form/updateFilePageInSubmissionMapFile/{submissionMapId}` | `updateFilePageInSubmissionMapFile` |
| POST | `/api/submission-manager/submission-form/count-home` | `submissionCountHome` |
| GET | `/api/submission-manager/submission-form/{submissionFormId}` | `submissionGetDetail` |
| GET | `/api/submission-manager/submission-process/{submissionFormId}` | `getSubmisisonProcess` |
| POST | `/api/submission-manager/submission-form/create-or-update` | `createOrUpdate` |
| POST | `/api/submission-manager/submission-form/delete/{submissionFormId}` | `deleteSubmissionForm` |
| POST | `/api/submission-manager/submission-form/submit` | `submitForm` |
| POST | `/api/submission-manager/submission-form/update-all-submission-7939827832452673672323443432323` | `updateAllSubmission` |
| POST | `/api/submission-manager/submission-form/mobile/get-file-info` | `generatePathFileForMobile` |
| POST | `/api/submission-manager/submission-form/cancel/{submissionFormId}` | `cancelForm` |
| GET | `/api/submission-manager/submission-form/{submissionFormId}/get-document-draft-after-sign` | `getDocumentDraftsAfterSign` |
| GET | `/api/submission-manager/submission-file/download` | `generatSubmissionFile` |
| POST | `/api/submission-manager/submission-file/sign` | `signSubmission` |
| POST | `/api/submission-manager/submission-file/reject-sign` | `rejectSubmission` |
| GET | `/api/submission-manager/submission-form/get-list-position` | `getListPosition` |
| GET | `/api/submission-manager/submission-process/next-signer/{submissionFormId}` | `getNextSigner` |
| GET | `/api/submission-manager/get-file-encrypt-map/{fileId}` | `getFileEncryptMap` |
| POST | `/api/submission-manager/check-exist-object-id` | `checkExistObjectId` |
| GET | `/api/submission-manager/submission-form/get-total-submission-by-creator` | `getTotalSubmissionByCreator` |
| GET | `/api/submission-manager/submission-form/get-total-submission` | `getTotalSubmission` |
| GET | `/api/submission-manager/submission-form/get-org-submission` | `getListOrgSubmission` |
| POST | `/api/submission-manager/submission-form/tranfer-give-advice` | `tranferGiveAdvice` |
| POST | `/api/submission-manager/submission-form/update-advice` | `updateGiveAdviceState` |
| GET | `/api/submission-manager/get-file-by-submission-form-id/{submissionFormId}` | `getFileBySubmissionFormId` |
| POST | `/api/submission-manager/get-file-by-submission-form-id-and-text-id` | `getFileBySubmissionFormIdAndTextId` |
| GET | `/api/submission-manager/get-org-file-encrypt-map/{fileId}` | `getOrgFileEncryptMap` |
| GET | `/api/submission-manager/submission-form-by-text-id/{textId}` | `findSubmissionFormByTextId` |
| GET | `/api/submission-manager/get-json-file-encrypt/{submissionFormId}` | `getJsonFileEncrypt` |
| POST | `/api/submission-manager/submission-forward/send` | `submissionForwardCreate` |
| GET | `/api/submission-manager/submission-forward/get-list-sender-history` | `getListSubmissionForwardHistory` |
| GET | `/api/submission-manager/submission-forward/get-list-submission-forward` | `getListSubmissionForwardBySearchCondition` |
| POST | `/api/submission-manager/submission-form/update-num-page` | `updateNumPage` |
| POST | `/api/submission-manager/submission-form/update-order/{briefId}` | `changeOrder` |
| POST | `/api/submission-manager/submission-forward/update-is-read` | `updateIsRead` |
| GET | `/api/submission-manager/submission-forward/{submissionFormId}/related-user-ids` | `getUserIdsSentOrReceivedSubmissionForm` |
| GET | `/api/submission-manager/submission-forward/get-sub-forward-by-id/{subId}` | `getSubForWardById` |
| POST | `/api/submission-manager/submission-forward/get-sent-userIds` | `getSentUserIds` |
| POST | `/api/submission-manager/list-file-encrypt-map` | `getFileEncryptMap` |
| GET | `/api/submission-manager/get-org-json-file-encrypt/{submissionFormId}` | `getOrgJsonFileEncrypt` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

_Không có facade legacy riêng._

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `EntitySubmissionFormEditHistory`→`SUBMISSION_FORM_EDIT_HISTORY`, `SubmissionFileEntity`→`SUBMISSION_FILE`, `SubmissionFormEntity`→`SUBMISSION_FORM`, `SubmissionForwardEntity`→`SUBMISSION_FORWARD`, `SubmissionMapEntity`→`SUBMISSION_MAP`, `SubmissionMapFileEntity`→`SUBMISSION_MAP_FILE`, `SubmissionProcessEntity`→`SUBMISSION_PROCESS`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Request`→`REQUEST`, `RequestEmail`→`REQUEST_EMAIL`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_CONFIG`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_RESOURCE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_NORM`, `MISSION_PROCESS`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_FORWARD`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`
