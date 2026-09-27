# Bản đồ hệ thống — Văn bản đi (dự thảo → trình ký → cấp số → ban hành)

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 47 màn hình, 10 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/documentPublish/document_publish.zul` | `vm.document.DocumentPublishVM` | `DocumentPublishBusiness`, `RequisitionBusiness` | `IDocumentLibrary` | BE+LEGACY |
| `document/documentPublish/document_publish_replace.zul` | `vm.document.DocumentPublishReplaceVM` | `DocumentPublishBusiness` | — | BE |
| `document/documentPublish/popupPublishVB.zul` | `vm.document.DocumentPublishViewDetailVM` | `DocumentPublishBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/documentPublish/popupPublishVBEdit.zul` | `vm.document.DocumentPublishViewDetailVM` | `DocumentPublishBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/issueDocument/issue_document_list.zul` | `vm.requisition.RequisitionViewIssueNumberVM` | `AnswerDocumentBusiness`, `RequisitionBusiness` | — | BE |
| `document/orgFollower/orgFollowerDocOut.zul` | `vm.document.DocumentSendSearchVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `document/submitForConsideration/submitForConsideration.zul` | `vm.document.DocumentProposalVM` | `CVGroupBusiness`, `CommonBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `documentDraft/advancedSearch/advancedSearchDocument.zul` | `vm.document.DocumentSendSearchVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `documentDraft/advancedSearch/advancedSearchDocument_viewDetail.zul` | `vm.admin.requisition.RequisitionViewDetailVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/configDocManager.zul` | `vps.vm.ConfigDocManagerVM` | — | — | — |
| `documentDraft/documentDraft.zul` | `vm.documentDraft.DocumentDraftVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CategoryCommonBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `HomeBusiness`, `NotificationBusiness`, `ReminderBusiness`, `RequisitionBusiness`, `SearchSolrBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `documentDraft/documentDraftFlowDiagram.zul` | `vm.admin.requisition.FlowChartVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/documentDraftReport.zul` | `vm.admin.requisition.RequisitionReportVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/documentDraft_update_process.zul` | `vm.admin.requisition.RequisitionUpdateProcessVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/documentDraft_viewDetail.zul` | `vm.admin.requisition.RequisitionViewDetailVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/file/documentDraftFile.zul` | `vm.admin.requisition.RequisitionFileVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/file/documentDraftFileChangeSigner.zul` | `vm.admin.requisition.RequisitionFileChangeSignerVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/file/documentDraftFileUpdateState.zul` | `vm.admin.requisition.RequisitionFileUpdateVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/file/documentDraftFileViewDetail.zul` | `vm.admin.requisition.RequisitionFileDetailVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/rejectPublish.zul` | `vm.admin.requisition.RejectPublishVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/signUsbToken.zul` | `vm.admin.requisition.RequisitionSignVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/signatureImageSelector.zul` | `vm.admin.requisition.SignatureImageSelectorVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/transferCommentSigner.zul` | `vm.admin.requisition.TransferCommentSignerVM` | — | — | ☠ VM không tồn tại |
| `requisition/configDocManager.zul` | `vps.vm.ConfigDocManagerVM` | — | — | — |
| `requisition/file/requisitionFile.zul` | `vm.requisition.RequisitionFileVM` | `RequisitionFileBusiness` | `ISysOrganization` | BE+LEGACY |
| `requisition/file/requisitionFileChangeSigner.zul` | `vm.requisition.RequisitionFileChangeSignerVM` | — | — | — |
| `requisition/file/requisitionFileUpdateState.zul` | `vm.requisition.RequisitionFileUpdateVM` | `RequisitionFileBusiness`, `SearchSolrBusiness` | — | BE |
| `requisition/file/requisitionFileViewDetail.zul` | `vm.requisition.RequisitionFileDetailVM` | `RequisitionFileBusiness` | — | BE |
| `requisition/rejectPublish.zul` | `vm.requisition.RejectPublishVM` | `RequisitionBusiness` | — | BE |
| `requisition/requisition.zul` | `vm.requisition.RequisitionVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `DocumentKpiBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `requisition/requisitionReport.zul` | `vm.requisition.RequisitionReportVM` | `DocHandoverBusiness`, `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `requisition/requisition_addAppendix.zul` | `vm.requisition.RequisitionAddAppendixVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `SearchSolrBusiness` | `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `requisition/requisition_issue_number_view_detail.zul` | `vm.requisition.RequisitionViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness`, `WOPIBusiness` | `IRequisition`, `ISysOrganization` | BE+LEGACY |
| `requisition/requisition_update_process.zul` | `vm.requisition.RequisitionUpdateProcessVM` | `DocumentBusiness`, `SearchSolrBusiness` | — | BE |
| `requisition/requisition_vbbh.zul` | `vm.requisition.RequisitionVbbhVM` | — | — | — |
| `requisition/requisition_viewDetail.zul` | `vm.requisition.RequisitionViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness`, `WOPIBusiness` | `IRequisition`, `ISysOrganization` | BE+LEGACY |
| `requisition/signUsbToken.zul` | `vm.requisition.RequisitionSignVM` | — | `IRequisition` | LEGACY |
| `requisition/signatureImageSelector.zul` | `vm.requisition.SignatureImageSelectorVM` | — | — | — |
| `requisition/transferCommentSigner.zul` | `vm.requisition.TransferCommentSignerVM` | — | — | — |
| `requisition/transferGiveAdvice.zul` | `vm.requisition.TransferGiveAdviceVM` | — | — | — |
| `submissionForm/confirmSignDocumentDraft.zul` | `vm.submissionForm.ConfirmSignDocumentDraftVM` | — | — | — |
| `task/empRating/popup/signUsbToken.zul` | `vm.task.EmpRatingSignVM` | — | — | ☠ VM không tồn tại |
| `widgets/popupSelectRequisition.zul` | `widget.PopupSelectRequisitionVM` | — | — | — |
| `widgets/popupSelectRequisitionForSubmission.zul` | `widget.PopupSelectRequisitionForSubmissionVM` | — | — | — |
| `widgets/requisitionDocumentLookup.zul` | `vm.document.DocumentVM` | `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `widgets/requisitionAssignLookup.zul` | `widget.RequisitionAssignLookupVM` | — | — | — |
| `widgets/template/requisition/templateRequisition_add.zul` | `vm.requisition.RequisitionVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `DocumentKpiBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.documentDraft.DocumentDraftFileChangeSignerVM` | — | — | — |
| `vm.documentDraft.DocumentDraftFileDetailVM` | `RequisitionFileBusiness` | — | BE |
| `vm.documentDraft.DocumentDraftFileUpdateVM` | `RequisitionFileBusiness`, `SearchSolrBusiness` | — | BE |
| `vm.documentDraft.DocumentDraftFileVM` | `RequisitionFileBusiness` | `ISysOrganization` | BE+LEGACY |
| `vm.documentDraft.DocumentDraftFlowLookupVM` | — | `IRequisitionFlow` | LEGACY |
| `vm.documentDraft.DocumentDraftFlowVM` | — | `ICommonVoffice`, `IRequisitionFlow` | LEGACY |
| `vm.documentDraft.DocumentDraftReportVM` | `RequisitionBusiness` | — | BE |
| `vm.documentDraft.DocumentDraftSignVM` | — | `IRequisition` | LEGACY |
| `vm.documentDraft.DocumentDraftUpdateProcessVM` | `DocumentBusiness`, `SearchSolrBusiness` | — | BE |
| `vm.documentDraft.DocumentDraftViewDetailVM` | `DocumentBusiness`, `EnterpriseBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `WOPIBusiness` | `IRequisition` | BE+LEGACY |

</details>

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

### RequisitionBusiness

`web-spring/src/main/java/com/voffice/service/business/RequisitionBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `CertManagementAction.getCertStateNow` | `/CertManagementAction/getCertStateNow` | `CertManagementAction.getCertStateNow` | gen1 |
| `DocumentAction.actionSearchDocViewLibrary` | `/DocumentAction/actionSearchDocViewLibrary` | `DocumentAction.actionSearchDocViewLibrary` | gen1 |
| `DocumentAction.checkPermissionRollBack` | `/DocumentAction/checkPermissionRollBack` | `DocumentAction.checkPermissionRollBack` | gen1 |
| `DocumentPublishAction.getParentOrgLastSignOrg` | `/DocumentPublishAction/getParentOrgLastSignOrg` | `DocumentPublishAction.getParentOrgLastSignOrg` | gen1 |
| `DocumentService.addText` | `/DocumentService/addText` | `DocumentSignService.addText` | gen1 |
| `DocumentService.addTextFile` | `/DocumentService/addTextFile` | `DocumentSignService.addTextFile` | gen1 |
| `DocumentService.changeStateSign` | `/DocumentService/changeStateSign` | `DocumentSignService.changeStateSign` | gen1 |
| `DocumentService.checkFinalDocSignAndApproved` | `/DocumentService/checkFinalDocSignAndApproved` | `DocumentSignService.checkFinalDocSignAndApproved` | gen1 |
| `DocumentService.getAllListDocumentTypes` | `/DocumentService/getAllListDocumentTypes` | `DocumentSignService.getAllListDocumentTypes` | gen1 |
| `DocumentService.getListFields` | `/DocumentService/getListFields` | `DocumentSignService.getListFields` | gen1 |
| `DocumentService.getListFieldsByArea` | `/DocumentService/getListFieldsByArea` | `DocumentSignService.getListFieldsByArea` | gen1 |
| `DocumentService.getListMoneyUnit` | `/DocumentService/getListMoneyUnit` | `DocumentSignService.getListMoneyUnit` | gen1 |
| `DocumentService.getListUserSign` | `/DocumentService/getListUserSign` | `DocumentSignService.getListUserSign` | gen1 |
| `DocumentService.getLitsUserSignWithRole` | `/DocumentService/getLitsUserSignWithRole` | `DocumentSignService.getLitsUserSignWithRole` | gen1 |
| `DocumentService.getPublicDocumentTypeIdConfig` | `/DocumentService/getPublicDocumentTypeIdConfig` | `DocumentSignService.getPublicDocumentTypeIdConfig` | gen1 |
| `DocumentService.getTextExplanationTypeIdConfig` | `/DocumentService/getTextExplanationTypeIdConfig` | `DocumentSignService.getTextExplanationTypeIdConfig` | gen1 |
| `DocumentService.getTreeDepartSign` | `/DocumentService/getTreeDepartSign` | `DocumentSignService.getTreeDepartSign` | gen1 |
| `DocumentService.resignText` | `/DocumentService/resignText` | `DocumentSignService.resignText` | gen1 |
| `DocumentService.sendAndSign` | `/DocumentService/sendAndSign` | `DocumentSignService.sendAndSign` | gen1 |
| `DocumentService.transferMoneyAction` | `/DocumentService/transferMoneyAction` | `DocumentSignService.transferMoneyAction` | gen1 |
| `DocumentService.updateSigningFlow` | `/DocumentService/updateSigningFlow` | `DocumentSignService.updateSigningFlow` | gen1 |
| `Files.getInfoFile` | `/Files/getInfoFile` | `FileService.getInfoFile` | gen1 |
| `Org.checkSecretaryByGroupId` | `/Org/checkSecretaryByGroupId` | `OrgResource.checkSecretaryByGroupId` | gen1 |
| `P12CertAction.actionCancelRegCertWeb` | `/P12CertAction/actionCancelRegCertWeb` | `P12CertAction.actionCancelRegCertWeb` | gen1 |
| `P12CertAction.search` | `/P12CertAction/search` | `P12CertAction.search` | gen1 |
| `Sign.SignCloudCA` | `/Sign/SignCloudCA` | `SignResource.signCloudCA` | gen1 |
| `Sign.SignSoftAttachMutiFile` | `/Sign/SignSoftAttachMutiFile` | `SignResource.signSoftAttachMutiFile` | gen1 |
| `Sign.SignSoftAttachMutiFileBrief` | `/Sign/SignSoftAttachMutiFileBrief` | `SignResource.signSoftAttachMutiFileBrief` | gen1 |
| `Sign.SignSoftAttachMutiFileDoc` | `/Sign/SignSoftAttachMutiFileDoc` | `SignResource.signSoftAttachMutiFileDoc` | gen1 |
| `Sign.SignSoftHashMutiFile` | `/Sign/SignSoftHashMutiFile` | `SignResource.hashMutiFile` | gen1 |
| `Sign.SignSoftHashMutiFileBrief` | `/Sign/SignSoftHashMutiFileBrief` | `SignResource.hashMutiFileBrief` | gen1 |
| `Sign.SignSoftHashMutiFileDoc` | `/Sign/SignSoftHashMutiFileDoc` | `SignResource.hashMutiFileDoc` | gen1 |
| `Sign.SignTextByCASIM` | `/Sign/SignTextByCASIM` | `SignResource.signTextByCASIM` | gen1 |
| `Sign.updateDatabaseAfterMark` | `/Sign/updateDatabaseAfterMark` | `SignResource.updateDatabaseAfterMark` | gen1 |
| `Sign.updateViewComment` | `/Sign/updateViewComment` | `SignResource.updateViewComment` | gen1 |
| `TextFileCommentAction.getListTextNote` | `/TextFileCommentAction/getListTextNote` | `TextFileCommentAction.getListTextNote` | gen1 |
| `TextFileCommentAction.resetFileCommentDraff` | `/TextFileCommentAction/resetFileCommentDraff` | `TextFileCommentAction.resetFileCommentDraff` | gen1 |
| `TextFileCommentAction.updateTextFileComment` | `/TextFileCommentAction/updateTextFileComment` | `TextFileCommentAction.updateTextFileComment` | gen1 |
| `TextReportAction.ReportTextProcessingTime` | `/TextReportAction/ReportTextProcessingTime` | `TextReportAction.reportTextProcessingTime` | gen1 |
| `TextReportAction.ReportTextRejectionCount` | `/TextReportAction/ReportTextRejectionCount` | `TextReportAction.reportTextRejectionCount` | gen1 |
| `TextReportAction.reportRequisiton` | `/TextReportAction/reportRequisiton` | `TextReportAction.reportRequisiton` | gen1 |
| `TextReportAction.reportTextRejectedDetail` | `/TextReportAction/reportTextRejectedDetail` | `TextReportAction.reportTextRejectedDetail` | gen1 |
| `TextReportAction.reportTextRejectedSumary` | `/TextReportAction/reportTextRejectedSumary` | `TextReportAction.reportTextRejectedSumary` | gen1 |
| `TextReportAction.reportTimeSignText` | `/TextReportAction/reportTimeSignText` | `TextReportAction.reportTimeSignText` | gen1 |
| `VHROrgAction.getOrgCode` | `/VHROrgAction/getOrgCode` | `VHROrgAction.getOrgCode` | gen1 |
| `api.brief-detail.get-list-text` | `/api/brief-detail/get-list-text` | `BriefDetailManagementController.getListText` | gen1 |
| `api.category-common.list-form-type` | `/api/category-common/list-form-type` | `CategoryCommonController.getListFormType` | gen2 |
| `api.category-common.list-sub-type` | `/api/category-common/list-sub-type` | `CategoryCommonController.getListSubType` | gen2 |
| `api.doc-out.add-permission-confidential-file` | `/api/doc-out/add-permission-confidential-file` | `DocOutController.addPermissionConfidentialFile` | gen2 |
| `api.doc-out.get-all-file-encrypt-map-by-fileId` | `/api/doc-out/get-all-file-encrypt-map-by-fileId` | `DocOutController.getAllFileEncryptMap` | gen2 |
| `api.doc-out.get-file-encrypt-map` | `/api/doc-out/get-file-encrypt-map` | `DocOutController.getFileEncryptMap` | gen2 |
| `api.doc-out.get-json-file-encrypt` | `/api/doc-out/get-json-file-encrypt` | `DocOutController.findJsonFileEncryptByTextId` | gen2 |
| `api.doc-out.get-list-document-completes` | `/api/doc-out/get-list-document-completes` | `DocOutController.getlistDocCompletes` | gen2 |
| `api.doc-out.get-list-file-encrypt-map` | `/api/doc-out/get-list-file-encrypt-map` | `DocOutController.findTextFileEncryptByTexId` | gen2 |
| `api.doc-out.get-list-file-encrypt-map-by-text-ids` | `/api/doc-out/get-list-file-encrypt-map-by-text-ids` | `DocOutController.findTextFileEncryptByTexIds` | gen2 |
| `api.doc-out.get-org-json-file-encrypt` | `/api/doc-out/get-org-json-file-encrypt` | `DocOutController.findOrgJsonFileEncryptByTextId` | gen2 |
| `api.doc-out.get-permisison-file-encrypt-map` | `/api/doc-out/get-permisison-file-encrypt-map` | `DocOutController.permissionFileEncryptByTexId` | gen2 |
| `api.flow-manager.doc-out` | ❓ không tìm thấy endpoint | | |
| `api.flow-manager.doc-out.get-leaders` | `/api/flow-manager/doc-out/get-leaders` | `FlowManagerController.getLeaders` | gen2 |
| `api.flow-manager.doc-out.get-users-next-step` | `/api/flow-manager/doc-out/get-users-next-step` | `FlowManagerController.DocOutGetUsersNextStep` | gen2 |
| `api.flow-manager.doc-out.promulgation-units` | `/api/flow-manager/doc-out/promulgation-units` | `FlowManagerController.getAllPromulgationUnits` | gen2 |
| `api.flow-manager.doc-out.signers-switch` | `/api/flow-manager/doc-out/signers-switch` | `FlowManagerController.DocOutSignersSwitch` | gen2 |
| `api.flow-manager.get-list-node` | `/api/flow-manager/get-list-node` | `FlowManagerController.getListNodeByNodeIds` | gen2 |
| `api.report-result.report-daily.find-by-id` | `/api/report-result/report-daily/find-by-id` | `MissionReportResultController.getReportDailyHistoryById` | gen2 |
| `api.report-result.report-daily.find-by-textId` | `/api/report-result/report-daily/find-by-textId` | `MissionReportResultController.getReportDailyHistoryByTextId` | gen2 |
| `api.submission-manager.check-exist-object-id` | `/api/submission-manager/check-exist-object-id` | `SubmissionManagerController.checkExistObjectId` | gen2 |
| `api.text-chat.add` | `/api/text-chat/add` | `TextChatController.addTextChat` | gen2 |
| `api.text-chat.delete` | `/api/text-chat/delete` | `TextChatController.deleteTextChat` | gen2 |
| `api.text-chat.existsNoteByTextId` | `/api/text-chat/existsNoteByTextId` | `TextChatController.deleteTextChat` | gen2 |
| `api.text-process.forward-to-assign-number` | `/api/text-process/forward-to-assign-number` | `TextProcessController.forwardToAssignNumber` | gen2 |
| `api.text-process.get-all-cert-permission` | `/api/text-process/get-all-cert-permission` | `TextProcessController.getAllCertificatePermission` | gen2 |
| `api.text-process.get-all-signer` | `/api/text-process/get-all-signer` | `TextProcessController.getAllSignerForSign` | gen2 |
| `api.text-process.get-cert-user-or-org` | `/api/text-process/get-cert-user-or-org` | `TextProcessController.getCertificateOfUserOrOrg` | gen2 |
| `api.text-process.get-next-signers` | `/api/text-process/get-next-signers` | `TextProcessController.getNextSigners` | gen2 |
| `api.text-process.get-next-signers-check-cert` | `/api/text-process/get-next-signers-check-cert` | `TextProcessController.getNextSignersCheckCert` | gen2 |
| `api.text-process.rollback-signer` | `/api/text-process/rollback-signer` | `TextProcessController.addTextFiles` | gen2 |
| `api.text-process.validate-update-give-advise` | `/api/text-process/validate-update-give-advise` | `TextProcessController.validateUpdateGiveAdvice` | gen2 |
| `api.user-table-header-state.find-user-table-header-state` | `/api/user-table-header-state/find-user-table-header-state` | `UserTableHeaderStateController.findByUserIdViewTypeGroupType` | gen2 |
| `api.user-table-header-state.find-user-table-header-state-by-userId` | `/api/user-table-header-state/find-user-table-header-state-by-userId` | `UserTableHeaderStateController.findByUserId` | gen2 |
| `api.user-table-header-state.save-table-header-state` | `/api/user-table-header-state/save-table-header-state` | `UserTableHeaderStateController.saveTableHeaderState` | gen2 |
| `api.user-table-header-state.save-user-table-header-state` | `/api/user-table-header-state/save-user-table-header-state` | `UserTableHeaderStateController.saveUserTableHeaderState` | gen2 |
| `api.vhr-employee.get-list-certificate` | `/api/vhr-employee/get-list-certificate` | `VhrEmployeeController.getListCertificate` | gen2 |
| `api.vhr-employee.get-list-security-code` | `/api/vhr-employee/get-list-security-code` | `VhrEmployeeController.getListSecurityCode` | gen2 |
| `api.vhr-employee.get-security-cert` | `/api/vhr-employee/get-security-cert` | `VhrEmployeeController.getEmployeeById` | gen2 |
| `api.vhr-employee.update-certificate` | `/api/vhr-employee/update-certificate` | `VhrEmployeeController.updateCertificate` | gen2 |
| `api.vhr-employee.update-security-cert` | `/api/vhr-employee/update-security-cert` | `VhrEmployeeController.updateSecurityCert` | gen2 |
| `configParamAction.getConfigParamMultiSign` | `/configParamAction/getConfigParamMultiSign` | `ConfigParameterAction.getConfigParamMultiSign` | gen1 |
| `imageOrgAction.getOrgMarkList` | `/imageOrgAction/getOrgMarkList` | `ImageOrgAction.getOrgMarkList` | gen1 |
| `imageSignAction.getImageSignByCardId` | `/imageSignAction/getImageSignByCardId` | `ImageSignAction.getImageSignByCardId` | gen1 |
| `imageSignAction.getListLocationByFileDraff` | `/imageSignAction/getListLocationByFileDraff` | `ImageSignAction.getListLocationByFileDraff` | gen1 |
| `missionAction.getMissionCommanderList` | `/missionAction/getMissionCommanderList` | `MissionAction.getMissionCommanderList` | gen1 |
| `staffAction.getListUser` | `/staffAction/getListUser` | `StaffAction.getListUser` | gen1 |
| `staffAction.getListUserMultiTransfer` | `/staffAction/getListUserMultiTransfer` | `StaffAction.getListUserMultiTransfer` | gen1 |
| `staffAction.searchUserRoles` | `/staffAction/searchUserRoles` | `StaffAction.searchUserRoles` | gen1 |
| `text.delete-text-files` | `/text/delete-text-files` | `TextFileController.deleteTextFiles` | gen2 |
| `textAction.CheckTextWaitingForSignOfUser` | `/textAction/CheckTextWaitingForSignOfUser` | `TextAction.checkTextWaitingForSignOfUser` | gen1 |
| `textAction.GetHistoryOfSignerChange` | `/textAction/GetHistoryOfSignerChange` | `TextAction.getHistoryOfSignerChange` | gen1 |
| `textAction.addDocDraftToBrief` | `/textAction/addDocDraftToBrief` | `TextAction.addDocDraftToBrief` | gen1 |
| `textAction.askForSeal` | `/textAction/askForSeal` | `TextAction.askForSeal` | gen1 |
| `textAction.cancelDocumentPublish` | `/textAction/cancelDocumentPublish` | `TextAction.cancelDocumentPublish` | gen1 |
| `textAction.checkImageSign` | `/textAction/checkImageSign` | `IndexController.redirect` | gen2 |
| `textAction.checkShowTransferGiveAdvice` | `/textAction/checkShowTransferGiveAdvice` | `IndexController.redirect` | gen2 |
| `textAction.checkSpellActive` | `/textAction/checkSpellActive` | `TextAction.checkSpellActive` | gen1 |
| `textAction.checkSpellText` | `/textAction/checkSpellText` | `TextAction.checkSpellText` | gen1 |
| `textAction.countDocSendSearch` | `/textAction/countDocSendSearch` | `TextAction.countDocSendSearch` | gen1 |
| `textAction.countMainSigningFilePages` | `/textAction/countMainSigningFilePages` | `TextAction.countMainSigningFilePages` | gen1 |
| `textAction.deleteDocDraftBrief` | `/textAction/deleteDocDraftBrief` | `TextAction.deleteText` | gen1 |
| `textAction.deleteExplanation` | `/textAction/deleteExplanation` | `TextAction.deleteExplanation` | gen1 |
| `textAction.deleteRequisition` | `/textAction/deleteRequisition` | `TextAction.deleteRequisition` | gen1 |
| `textAction.doDeleteRequisition` | `/textAction/doDeleteRequisition` | `TextAction.doDeleteRequisition` | gen1 |
| `textAction.documentPromulgate` | `/textAction/documentPromulgate` | `TextAction.documentPromulgate` | gen1 |
| `textAction.get-reject-history` | `/textAction/get-reject-history` | `IndexController.redirect` | gen2 |
| `textAction.get-text-process` | `/textAction/get-text-process` | `TextAction.getTextProcessByTextIdAndSignType` | gen1 |
| `textAction.getAutoSendText` | `/textAction/getAutoSendText` | `TextAction.getAutoSendText` | gen1 |
| `textAction.getCertificateSynchronization` | `/textAction/getCertificateSynchronization` | `TextAction.getCertificateSynchronization` | gen1 |
| `textAction.getDefaultMarkLocationByTextId` | `/textAction/getDefaultMarkLocationByTextId` | `TextAction.getDefaultMarkLocationByTextId` | gen1 |
| `textAction.getIfUsersExistInProcess` | `/textAction/getIfUsersExistInProcess` | `TextAction.getIfUsersExistInProcess` | gen1 |
| `textAction.getLastSignImageOfText` | `/textAction/getLastSignImageOfText` | `TextAction.getLastSignImageOfText` | gen1 |
| `textAction.getListCloudCertificates` | `/textAction/getListCloudCertificates` | `TextAction.getListCloudCertificates` | gen1 |
| `textAction.getListOrgMark` | `/textAction/getListOrgMark` | `TextAction.getListOrgMark` | gen1 |
| `textAction.getListOrgMultiMarkRequisition` | `/textAction/getListOrgMultiMarkRequisition` | `TextAction.getListOrgMultiMarkRequisition` | gen1 |
| `textAction.getListOrgPermissionMark` | `/textAction/getListOrgPermissionMark` | `TextAction.getListOrgPermissionMark` | gen1 |
| `textAction.getListRegisterNumber` | `/textAction/getListRegisterNumber` | `TextAction.getListRegisterNumber` | gen1 |
| `textAction.getListSigner` | `/textAction/getListSigner` | `TextAction.getListSigner` | gen1 |
| `textAction.getListSignerBySignatureTypeApprovalAndSignFlash` | `/textAction/getListSignerBySignatureTypeApprovalAndSignFlash` | `TextAction.getListSignerBySignatureTypeApprovalAndSignFlash` | gen1 |
| `textAction.getListSubmitterToMark` | `/textAction/getListSubmitterToMark` | `TextAction.getListSubmitterToMark` | gen1 |
| `textAction.getListTextExplanation` | `/textAction/getListTextExplanation` | `TextAction.getListTextExplanation` | gen1 |
| `textAction.getListTextSignNext` | `/textAction/getListTextSignNext` | `TextAction.getListTextSignNext` | gen1 |
| `textAction.getLocationSignature` | `/textAction/getLocationSignature` | `TextAction.getLocationSignature` | gen1 |
| `textAction.getOrgMarkedList` | `/textAction/getOrgMarkedList` | `TextAction.getOrgMarkedList` | gen1 |
| `textAction.getPeopleInApprovalFlow` | `/textAction/getPeopleInApprovalFlow` | `TextAction.getPeopleInApprovalFlow` | gen1 |
| `textAction.getPermissionViewCommentSignatureTypes` | `/textAction/getPermissionViewCommentSignatureTypes` | `TextAction.getPermissionViewCommentSignatureTypes` | gen1 |
| `textAction.getStatusAutoSendText` | `/textAction/getStatusAutoSendText` | `TextAction.getStatusAutoSendText` | gen1 |
| `textAction.getTextDetail` | `/textAction/getTextDetail` | `TextAction.getTextDetail` | gen1 |
| `textAction.getUserMySign` | `/textAction/getUserMySign` | `TextAction.getUserMySign` | gen1 |
| `textAction.getUserSignMethod` | `/textAction/getUserSignMethod` | `TextAction.getUserSignMethod` | gen1 |
| `textAction.lockDocument` | `/textAction/lockDocument` | `TextAction.lockDocument` | gen1 |
| `textAction.markDocumentByOrg` | `/textAction/markDocumentByOrg` | `TextAction.markDocumentByOrg` | gen1 |
| `textAction.markDocumentByOrgForBrief` | `/textAction/markDocumentByOrgForBrief` | `TextAction.markDocumentByOrgForBrief` | gen1 |
| `textAction.markDocumentByOrgForConfirm` | `/textAction/markDocumentByOrgForConfirm` | `TextAction.markDocumentByOrgForConfirm` | gen1 |
| `textAction.rejectMark` | `/textAction/rejectMark` | `TextAction.rejectMark` | gen1 |
| `textAction.rejectSignDocByVTAction` | `/textAction/rejectSignDocByVTAction` | `TextAction.rejectSignDocByVTAction` | gen1 |
| `textAction.rejectSignDocument` | `/textAction/rejectSignDocument` | `TextAction.rejectSignDocument` | gen1 |
| `textAction.rejectSignText` | `/textAction/rejectSignText` | `TextAction.rejectSignText` | gen1 |
| `textAction.restoreDocument` | `/textAction/restoreDocument` | `TextAction.restoreDocument` | gen1 |
| `textAction.rollBackDauDonVi` | `/textAction/rollBackDauDonVi` | `TextAction.rollBackDauDonVi` | gen1 |
| `textAction.saveTextExplanation` | `/textAction/saveTextExplanation` | `TextAction.saveTextExplanation` | gen1 |
| `textAction.searchText` | `/textAction/searchText` | `TextAction.searchText` | gen1 |
| `textAction.searchTextForReminder` | `/textAction/searchTextForReminder` | `TextAction.searchTextForReminder` | gen1 |
| `textAction.searchTextForSubmission` | `/textAction/searchTextForSubmission` | `TextAction.searchTextForSubmission` | gen1 |
| `textAction.softDeleteRejectedDraft` | `/textAction/softDeleteRejectedDraft` | `TextAction.softDeleteRejectedDraft` | gen1 |
| `textAction.synchonizeCertificate` | `/textAction/synchonizeCertificate` | `TextAction.synchonizeCertificate` | gen1 |
| `textAction.tranferProofreadingAsistant` | `/textAction/tranferProofreadingAsistant` | `TextAction.tranferProofreadingAsistant` | gen1 |
| `textAction.transferGiveAdvice` | `/textAction/transferGiveAdvice` | `TextAction.transferGiveAdvice` | gen1 |
| `textAction.transferToPreSigner` | `/textAction/transferToPreSigner` | `TextAction.transferToPreSigner` | gen1 |
| `textAction.unLockDocument` | `/textAction/unLockDocument` | `TextAction.unLockDocument` | gen1 |
| `textAction.updateDatabaseSign` | `/textAction/updateDatabaseSign` | `TextAction.updateDatabaseSign` | gen1 |
| `textAction.updateDefaultCloudCert` | `/textAction/updateDefaultCloudCert` | `TextAction.updateDefaultCloudCert` | gen1 |
| `textAction.updateGiveAdvice` | `/textAction/updateGiveAdvice` | `TextAction.updateGiveAdvice` | gen1 |
| `textAction.updateListSigner` | `/textAction/updateListSigner` | `TextAction.updateListSigner` | gen1 |
| `textAction.updateProofreader` | `/textAction/updateProofreader` | `TextAction.updateProofreader` | gen1 |
| `textAction.updateReadingStatus` | `/textAction/updateReadingStatus` | `TextAction.updateReadingStatus` | gen1 |
| `textAction.updateReadingStatusV2` | `/textAction/updateReadingStatusV2` | `TextAction.updateReadingStatusV2` | gen1 |
| `textAction.updateSignImageBySecrectary` | `/textAction/updateSignImageBySecrectary` | `TextAction.updateSignImageBySecrectary` | gen1 |
| `textAction.updateSigner` | `/textAction/updateSigner` | `TextAction.updateSigner` | gen1 |
| `textAction.updateTextExplanation` | `/textAction/updateTextExplanation` | `TextAction.updateTextExplanation` | gen1 |
| `textAction.updateUnReadingStatusV2` | `/textAction/updateUnReadingStatusV2` | `TextAction.updateUnReadingStatusV2` | gen1 |
| `textAction.updateUserMySign` | `/textAction/updateUserMySign` | `TextAction.updateUserMySign` | gen1 |
| `textAction.updateUserSignMethod` | `/textAction/updateUserSignMethod` | `TextAction.updateUserSignMethod` | gen1 |
| `textMarkSyncAction.addTextMarkSync` | `/textMarkSyncAction/addTextMarkSync` | `TextMarkSyncAction.addTextMarkSync` | gen1 |
| `textMarkSyncAction.getTextMarkSync` | `/textMarkSyncAction/getTextMarkSync` | `TextMarkSyncAction.getTextMarkSync` | gen1 |
| `wopi.generate-online-editor-url` | `/wopi/generate-online-editor-url` | `WOPIAction.generateOnlineEditorUrl` | gen1 |

### RequisitionFileBusiness

`web-spring/src/main/java/com/voffice/service/business/RequisitionFileBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Files.downloadFileSignBriefCase` | `/Files/downloadFileSignBriefCase` | `FileService.downloadFileSignBriefCase` | gen1 |
| `signBriefcaseAction.addOrEditSignBriefcase` | `/signBriefcaseAction/addOrEditSignBriefcase` | `SignBriefcaseAction.addOrEditSignBriefcase` | gen1 |
| `signBriefcaseAction.deleteSignBriefcase` | `/signBriefcaseAction/deleteSignBriefcase` | `SignBriefcaseAction.deleteSignBriefcase` | gen1 |
| `signBriefcaseAction.getBarcode` | `/signBriefcaseAction/getBarcode` | `SignBriefcaseAction.getBarcode` | gen1 |
| `signBriefcaseAction.getLeaderOfAssitant` | `/signBriefcaseAction/getLeaderOfAssitant` | `SignBriefcaseAction.getLeaderOfAssitant` | gen1 |
| `signBriefcaseAction.getListSignBriefcase` | `/signBriefcaseAction/getListSignBriefcase` | `SignBriefcaseAction.getListSignBriefcase` | gen1 |
| `signBriefcaseAction.getListSignBriefcaseStatus` | `/signBriefcaseAction/getListSignBriefcaseStatus` | `SignBriefcaseAction.getListSignBriefcaseStatus` | gen1 |
| `signBriefcaseAction.getSignBriefcaseDetail` | `/signBriefcaseAction/getSignBriefcaseDetail` | `SignBriefcaseAction.getSignBriefcaseDetail` | gen1 |
| `signBriefcaseAction.updateSigner` | `/signBriefcaseAction/updateSigner` | `SignBriefcaseAction.updateSigner` | gen1 |
| `signBriefcaseAction.updateStatusSignBriefcase` | `/signBriefcaseAction/updateStatusSignBriefcase` | `SignBriefcaseAction.updateStatusSignBriefcase` | gen1 |

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

### TextAction (gen1) — base `/textAction`, 95 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TextAction.java`

- Logic (gen-1 `controler/`): `TextController`, `CommonControler`, `EmpCloudCAService`
- Service: `CategoryCacheService`, `DocCommentService`, `DocCommentServiceImpl`, `DocumentHistoryLogService`, `DocumentHistoryLogServiceImpl`, `DocumentPermissionCacheService`, `ElasticDocumentService`, `ElasticDocumentServiceImpl`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ManagerService`, `ManagerServiceImpl`, `OfficePublishedReplacementService`, `OfficePublishedReplacementServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`, `TextDraftService`, `TextDraftServiceImpl`, `TextProcessService`, `TextProcessServiceImpl`, `TextReceiverGroupDetailService`, `TextReceiverGroupDetailServiceImpl`
- DAO (SQL thuần): `AnswerDocumentDAO`, `AttachDAO`, `AutoDigitalSignDAO`, `BriefDetailManagementDAO`, `CloudDeviceCertDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `DocOrgRepublishDAO`, `DocumentDAO`, `DocumentScopeDAO`, `DocumentSignDAO`, `DocumentPublishedTmpDAO`, `DocumentSearchInService`, `EmpCloudCADAO`, `HistoryChangeSignDAO`, `StaffDAO`, `StaffImageSignDAO`, `MeetingWeekDAO`, `MissionDAO`, `MissionSigningDAO`, `OrgDAO`, `ReminderHistoryDAO`, `FilesAttachmentDAO`, `TextDAO`, `P12CertDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `SysRoleDAO`, `TextBookDAO`, `TextCheckSpellDAO`, `TextCommonDAO`, `TextEditHistoryDAO`, `TextProcessDAO`, `ImageSignDao`, `TextProcessHistoryDAO`, `TextReceiverDAO`, `TextReceiverGroupDAO`, `TextSignDAO`
- Repository (JPA): `AttachRepositoryJPA`, `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `CategoryCommonRepositoryJPA`, `DocumentHistoryLogJPA`, `DocumentTypeRepositoryJPA`, `TextBookRepositoryJPA`, `VhrOrgJPA`, `DocumentInListRequestRepositoryJPA`, `ElasticDocumentPrivateRepositoryJPA`, `ElasticDocumentPublicRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `ConfigSmsModuleRepositoryJPA`, `EmpCaDetailRepositoryJPA`, `EmpCaRepositoryJPA`, `FeedbackImageRepositoryJPA`, `FeedbackLogFileRepositoryJPA`, `FeedbackProcessRepositoryJPA`, `FeedbackRepositoryJPA`, `ImageOrgConfigRepositoryJPA`, `ImageOrgRepositoryJPA`, `MenuRepositoryJPA`, `NotificationRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `PositionRepositoryJPA`, `RolePermissionBaseRepositoryJPA`, `RolePermissionDataRepositoryJPA`, `SmsBlackListRepositoryJPA`, `SysMenuRepositoryJPA`, `SysRoleMenuRepositoryJPA`, `SysRoleRepositoryJPA`, `SystemParameterRepositoryJPA`, `UserOrgMapRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `NodeActionRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `SecurityTypeRepositoryJPA`, `StaffImageSignJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextDraftHistoryRepositoryJPA`, `TextDraftRepositoryJPA`, `AttachHistoryRepositoryJPA`, `FileEncryptMapHistoryJPA`, `LogTranstionSignRepositoryJPA`, `MessageJPA`, `NodeRepositoryJPA`
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

### TextReportAction (gen1) — base `/TextReportAction`, 11 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TextReportAction.java`

- Logic (gen-1 `controler/`): `TextReportController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `TextReportDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `AUTO_DIGSIG_TRANSACTION`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `SECURITY_TYPE`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/TextReportAction/getListStaffByRejectSign` | `getListStaffByRejectSign` |
| POST | `/TextReportAction/getLstDeatilDocRejectedByUserLogin` | `getLstDeatilDocRejectedByUserLogin` |
| POST | `/TextReportAction/getStatisticalLineReportReject` | `getStatisticalLineReportReject` |
| POST | `/TextReportAction/getLstDetailDocRejectedOfStaff` | `getLstDetailDocRejectedOfStaff` |
| POST | `/TextReportAction/reportTextRejectedDetail` | `reportTextRejectedDetail` |
| POST | `/TextReportAction/exportReportTextRejectedDetail` | `exportReportTextRejectedDetail` |
| POST | `/TextReportAction/reportTextRejectedSumary` | `reportTextRejectedSumary` |
| POST | `/TextReportAction/reportTimeSignText` | `reportTimeSignText` |
| POST | `/TextReportAction/reportRequisiton` | `reportRequisiton` |
| POST | `/TextReportAction/ReportTextProcessingTime` | `reportTextProcessingTime` |
| POST | `/TextReportAction/ReportTextRejectionCount` | `reportTextRejectionCount` |

</details>

### DocOutController (gen2) — base `/api/doc-out`, 12 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocOutController.java`

- Service: `DocOutService`, `DocOutServiceImpl`
- DAO (SQL thuần): `FilesAttachmentDAO`, `TextDAO`
- Repository (JPA): `AttachRepositoryJPA`, `FileEncryptMapJPA`, `NodeActionRepositoryJPA`, `PositionRepositoryJPA`, `ReportDailyHistoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CONNECT_DOCUMENT`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_MINUTES`, `MIGRATED_FILES`, `NODE_ACTION`, `POSITION`, `REPORT_DAILY_HISTORY`, `SECURITY_TYPE`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

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

### TextDraftController (gen2) — base `/api/text-draft`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextDraftController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `TextDraftService`, `TextDraftServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `SystemParameterRepositoryJPA`, `TextDraftHistoryRepositoryJPA`, `TextDraftRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `GROUP_MAPPING`, `HOME_WIDGET`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `READ_NOTICE_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_NOTE`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/text-draft/get-advise` | `getAdvise` |
| POST | `/api/text-draft/assign-adviser` | `assignAdviser` |
| POST | `/api/text-draft/search-text-draft` | `searchTextDraft` |
| GET | `/api/text-draft/get-text-draft-history` | `getTextDraftHistory` |
| POST | `/api/text-draft/give-advise` | `giveAdvise` |

</details>

### TextFileController (gen2) — base `/text`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextFileController.java`

- Service: `TextFileService`, `TextFileServiceImpl`
- Repository (JPA): `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `TextAttachBaseRepositoryJPA`, `TextAttachRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `ATTACH_TEMPLATE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/text/add-text-files` | `addTextFiles` |
| POST | `/text/delete-text-files` | `deleteTextFiles` |

</details>

### TextProcessController (gen2) — base `/api/text-process`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextProcessController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `TextProcessService`, `TextProcessServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `AutoDigitalSignDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `HistoryChangeSignDAO`, `ImageSignDao`, `TextDAO`, `TextProcessDAO`, `TextProcessHistoryDAO`
- Repository (JPA): `AttachHistoryRepositoryJPA`, `AttachRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `FileEncryptMapHistoryJPA`, `FileEncryptMapJPA`, `LogTranstionSignRepositoryJPA`, `MessageJPA`, `NodeActionRepositoryJPA`, `NodeRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `SECURITY_TYPE`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_MESSAGE`, `SYSTEM_PARAMETER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/text-process/rollback-signer/{text-id}` | `addTextFiles` |
| GET | `/api/text-process/get-next-signers` | `getNextSigners` |
| GET | `/api/text-process/get-all-signer` | `getAllSignerForSign` |
| GET | `/api/text-process/get-next-signers-check-cert` | `getNextSignersCheckCert` |
| POST | `/api/text-process/forward-to-assign-number` | `forwardToAssignNumber` |
| GET | `/api/text-process/get-cert-user-or-org` | `getCertificateOfUserOrOrg` |
| GET | `/api/text-process/get-all-cert-permission` | `getAllCertificatePermission` |
| POST | `/api/text-process/validate-update-give-advise` | `validateUpdateGiveAdvice` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `RequisitionFacade` | `IRequisition` | `RequisitionProcessService`, `RequisitionService` | `RequisitionProcessJpaDao`, `RequisitionCommentJpaDao`, `RequisitionFileJpaDao`, `RequisitionJpaDao`, `UserRoleJpaDao` | `Requisition (REQUISITION)`, `RequisitionComment (REQUISITION_COMMENT)`, `RequisitionFile (REQUISITION_FILE)`, `RequisitionProcess (REQUISITION_PROCESS)`, `UserRole (USER_ROLE)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `TextCheckSpellsEntity`→`TEXT_CHECK_SPELLS`, `TextDraftEntity`→`TEXT_DRAFT`, `TextDraftFileEntity`→`TEXT_DRAFT_FILE`, `TextDraftHistoryEntity`→`TEXT_DRAFT_HISTORY`, `TextEntity`→`TEXT`, `TextProcessEntity`→`TEXT_PROCESS`, `TextProcessHistoryEntity`→`TEXT_PROCESS_HISTORY`, `TextReceiverGroupDetailEntity`→`TEXT_RECEIVER_GROUP_DETAIL`, `WaitingNumberBookEntity`→`WAITING_NUMBER_BOOK`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Requisition`→`REQUISITION`, `RequisitionComment`→`REQUISITION_COMMENT`, `RequisitionDoc`→`REQUISITION_DOC`, `RequisitionFile`→`REQUISITION_FILE`, `RequisitionProcess`→`REQUISITION_PROCESS`, `RequisitionReceiver`→`REQUISITION_RECEIVER`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUISITION`, `REQUISITION_COMMENT`, `REQUISITION_DOC`, `REQUISITION_FILE`, `REQUISITION_PROCESS`, `REQUISITION_RECEIVER`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_FILE`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MARK_SYNC`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_RECEIVER_GROUP_DETAIL`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`
