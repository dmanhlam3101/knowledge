# Bản đồ hệ thống — Xử lý công việc – giai đoạn TRƯỚC ban hành: dự thảo → xin ý kiến → trình ký → ký/phê duyệt → trả lại/từ chối (menu XỬ LÝ CÔNG VIỆC)

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 16 màn hình, 6 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `documentDraft/documentDraft.zul` | `vm.documentDraft.DocumentDraftVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CategoryCommonBusiness`, `DocumentPublishBusiness`, `DraftMissionLinkBusiness`, `EnterpriseBusiness`, `HomeBusiness`, `NotificationBusiness`, `ReminderBusiness`, `RequisitionBusiness`, `SearchSolrBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `documentDraft/documentDraftFlowDiagram.zul` | `vm.admin.requisition.FlowChartVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/documentDraftReport.zul` | `vm.admin.requisition.RequisitionReportVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/documentDraft_update_process.zul` | `vm.admin.requisition.RequisitionUpdateProcessVM` | — | — | ☠ VM không tồn tại |
| `documentDraft/documentDraft_viewDetail.zul` | `vm.requisition.RequisitionViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness`, `WOPIBusiness` | `IRequisition`, `ISysOrganization` | BE+LEGACY |
| `documentDraft/transferCommentSigner.zul` | `vm.admin.requisition.TransferCommentSignerVM` | — | — | ☠ VM không tồn tại |
| `requisition/requisition.zul` | `vm.requisition.RequisitionVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `DocumentKpiBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `requisition/requisition_addAppendix.zul` | `vm.requisition.RequisitionAddAppendixVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `SearchSolrBusiness` | `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `requisition/requisition_update_process.zul` | `vm.requisition.RequisitionUpdateProcessVM` | `DocumentBusiness`, `SearchSolrBusiness` | — | BE |
| `requisition/requisition_viewDetail.zul` | `vm.requisition.RequisitionViewDetailVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness`, `WOPIBusiness` | `IRequisition`, `ISysOrganization` | BE+LEGACY |
| `requisition/transferCommentSigner.zul` | `vm.requisition.TransferCommentSignerVM` | — | — | — |
| `requisition/transferGiveAdvice.zul` | `vm.requisition.TransferGiveAdviceVM` | — | — | — |
| `widgets/popupSelectRequisition.zul` | `widget.PopupSelectRequisitionVM` | — | — | — |
| `widgets/requisitionDocumentLookup.zul` | `vm.document.DocumentVM` | `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `widgets/requisitionAssignLookup.zul` | `widget.RequisitionAssignLookupVM` | — | — | — |
| `widgets/template/requisition/templateRequisition_add.zul` | `vm.requisition.RequisitionVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `DocumentKpiBusiness`, `DocumentPublishBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `HomeBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.documentDraft.DocumentDraftFlowLookupVM` | — | `IRequisitionFlow` | LEGACY |
| `vm.documentDraft.DocumentDraftFlowVM` | — | `ICommonVoffice`, `IRequisitionFlow` | LEGACY |
| `vm.documentDraft.DocumentDraftReportVM` | `RequisitionBusiness` | — | BE |
| `vm.documentDraft.DocumentDraftSignVM` | — | `IRequisition` | LEGACY |
| `vm.documentDraft.DocumentDraftUpdateProcessVM` | `DocumentBusiness`, `SearchSolrBusiness` | — | BE |
| `vm.documentDraft.DocumentDraftViewDetailVM` | `DocumentBusiness`, `DraftMissionLinkBusiness`, `EnterpriseBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `WOPIBusiness` | `IRequisition` | BE+LEGACY |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

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
| `Sign.SignSoftAttachMutiFilePosition` | `/Sign/SignSoftAttachMutiFilePosition` | `SignResource.signSoftAttachMutiFilePosition` | gen1 |
| `Sign.SignSoftHashMutiFile` | `/Sign/SignSoftHashMutiFile` | `SignResource.hashMutiFile` | gen1 |
| `Sign.SignSoftHashMutiFileBrief` | `/Sign/SignSoftHashMutiFileBrief` | `SignResource.hashMutiFileBrief` | gen1 |
| `Sign.SignSoftHashMutiFileDoc` | `/Sign/SignSoftHashMutiFileDoc` | `SignResource.hashMutiFileDoc` | gen1 |
| `Sign.SignSoftHashMutiFilePosition` | `/Sign/SignSoftHashMutiFilePosition` | `SignResource.hashMutiFilePosition` | gen1 |
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
| `textAction.rejectSignTextVBBHWaitForNumber` | `/textAction/rejectSignTextVBBHWaitForNumber` | `TextAction.rejectSignTextVBBHWaitForNumber` | gen1 |
| `textAction.restoreDocument` | `/textAction/restoreDocument` | `TextAction.restoreDocument` | gen1 |
| `textAction.returnCreatorTextByVtPromulgate` | `/textAction/returnCreatorTextByVtPromulgate` | `TextAction.returnCreatorTextByVtPromulgate` | gen1 |
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

## 3. BE — Controller → logic / service → DAO / repository → bảng

### DocumentSignService (gen1) — base `/DocumentService`, 19 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentSignService.java`

- Logic (gen-1 `controler/`): `DocumentSignController`, `CommonControler`, `FileControler`, `WOPIController`
- Service: `DocCommentService`, `DocCommentServiceImpl`, `DraftLifecycleEventService`, `DraftLifecycleEventServiceImpl`, `DraftLifecycleMissionClient`, `DraftMissionLinkService`, `DraftMissionLinkServiceImpl`, `ExtShareConfigServiceImpl`, `PdfOcrDocumentService`, `MissionReportResultService`, `MissionReportResultServiceImpl`, `MissionTemplateDetailService`, `MissionTemplateDetailServiceImpl`, `MissionReportResultDetailService`, `MissionReportResultDetailServiceImpl`, `MissionTemplateScopeService`, `MissionTemplateScopeServiceImpl`, `MissionTemplateTableService`, `MissionTemplateTableServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `VhrEmployeeService`, `VhrEmployeeServiceImpl`, `ExtShareConfigService`, `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `SigningFlowUpdateService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AttachDAO`, `AutoDigitalSignDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `ConnectDocumentDAO`, `DocumentDAO`, `DocumentSignDAO`, `TextDAO`, `BriefManagementDAO`, `DownloadAllFileDAO`, `DownloadFileCommentDAO`, `DownloadFileDocumentDAO`, `FilesAttachmentDAO`, `ImageDAO`, `ImageOrgDAO`, `OrgDAO`, `StaffImageSignDAO`, `TaskApprovalDAO`, `TaskDAO`, `TextProcessDAO`, `TextSearchDAO`, `SubmissionFormEditHistoryDAO`, `TextEditHistoryDAO`, `MappingOrgDAO`, `FileAttachmentDAO`, `ReminderHistoryDAO`, `TextCheckSpellDAO`, `TextPartnerDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `HistoryChangeSignDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `TextRepositoryJPA`, `DraftMissionLinkRepository`, `ExtAppEntityRepositoryJPA`, `ExtShareConfigRepositoryJPA`, `ExtShareScopeJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `BriefSubmitAttachFileEntityRepositoryJPA`, `BriefSubmitRequestEntityRepositoryJPA`, `VersionControlRepositoryJPA`, `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `SubmissionFileRepositoryJPA`, `MessageJPA`, `FileEncryptMapJPA`, `MissionReportResultRepositoryJPA`, `MissionProcessRepositoryJPA`, `MissionReportResultDetailRepositoryJPA`, `MissionRepositoryJPA`, `MissionTemplateDetailRepositoryJPA`, `MissionTemplateScopeRepositoryJPA`, `MissionTemplateTableRepositoryJPA`, `MissionTemplateRepositoryJPA`, `MissionTemplateScopeDetailRepositoryJPA`, `ReportDailyHistoryJPA`, `NodeRepositoryJPA`, `NotificationRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `TextProcessRepositoryJPA`, `ExtAppApiEntityRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `PositionRepositoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `SystemParameterRepositoryJPA`, `VhrOrgJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `EXT_APP_API`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_SCOPE_DETAIL`, `MISSION_TEMPLATE_TABLE`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `P12_CERT`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_PROCESS`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_ATTACH_PARTNER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/DocumentService/getListFields` | `getListFields` |
| POST | `/DocumentService/getListDocTypes` | `getListDocTypes` |
| POST | `/DocumentService/getListIndustry` | `getListIndustry` |
| POST | `/DocumentService/getTreeDepartSign` | `getTreeDepartSign` |
| POST | `/DocumentService/getListUserSign` | `getListUserSign` |
| POST | `/DocumentService/addText` | `addText` |
| POST | `/DocumentService/addTextFile` | `addTextFile` |
| POST | `/DocumentService/resignText` | `resignText` |
| POST | `/DocumentService/sendAndSign` | `sendAndSign` |
| POST | `/DocumentService/changeStateSign` | `changeStateSign` |
| POST | `/DocumentService/getPublicDocumentTypeIdConfig` | `getPublicDocumentTypeIdConfig` |
| POST | `/DocumentService/getLitsUserSignWithRole` | `getLitsUserSignWithRole` |
| POST | `/DocumentService/getListMoneyUnit` | `getListMoneyUnit` |
| POST | `/DocumentService/transferMoneyAction` | `transferMoneyAction` |
| POST | `/DocumentService/getListFieldsByArea` | `getListFieldsByArea` |
| POST | `/DocumentService/updateSigningFlow` | `updateSigningFlow` |
| POST | `/DocumentService/checkFinalDocSignAndApproved` | `checkFinalDocSignAndApproved` |
| POST | `/DocumentService/getTextExplanationTypeIdConfig` | `getTextExplanationTypeIdConfig` |
| POST | `/DocumentService/getAllListDocumentTypes` | `getAllListDocumentTypes` |

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
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `SECURITY_TYPE`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_MESSAGE`, `SYSTEM_PARAMETER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

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

**BE gen-2 (`com.viettel.office.entities`)**: `TextCheckSpellsEntity`→`TEXT_CHECK_SPELLS`, `TextDraftEntity`→`TEXT_DRAFT`, `TextDraftFileEntity`→`TEXT_DRAFT_FILE`, `TextDraftHistoryEntity`→`TEXT_DRAFT_HISTORY`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Requisition`→`REQUISITION`, `RequisitionComment`→`REQUISITION_COMMENT`, `RequisitionDoc`→`REQUISITION_DOC`, `RequisitionProcess`→`REQUISITION_PROCESS`, `RequisitionReceiver`→`REQUISITION_RECEIVER`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `EXT_APP_API`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_SCOPE_DETAIL`, `MISSION_TEMPLATE_TABLE`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `P12_CERT`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_PROCESS`, `REQUISITION`, `REQUISITION_COMMENT`, `REQUISITION_DOC`, `REQUISITION_FILE`, `REQUISITION_PROCESS`, `REQUISITION_RECEIVER`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_ATTACH_PARTNER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_FILE`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`
