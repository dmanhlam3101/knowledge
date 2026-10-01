# Bản đồ hệ thống — Văn bản đã ban hành – xem / tìm kiếm / bàn giao / phạm vi / loại văn bản (dùng chung đến & đi)

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 36 màn hình, 1 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/documentHandover/docHandover.zul` | `vm.document.DocumentHandoverVM` | — | — | ☠ VM không tồn tại |
| `document/documentHandover/docHistory.zul` | `vm.document.DocumentHandoverHistoryVM` | — | — | ☠ VM không tồn tại |
| `document/documentTrackSend/documentKpi.zul` | `vm.document.documentKpi.DocumentKpiVM` | `DocumentBusiness`, `TextBookBusiness` | `ISysUser` | BE+LEGACY |
| `document/documentTrackSend/documentTrackSend.zul` | `vm.document.DocumentTrackSendVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `SearchSolrBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `document/documentTrackSend/personalTreatmentStatus/personalTreatmentStatus.zul` | `vm.personalTreatmentStatus.PersonalTreatmentStatusVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `CommonBusiness`, `DocumentKpiBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `SubmissionFormBusiness`, `VhrEmployeeBusiness` | `ICommon`, `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `document/editDoc/editDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/handoverDoc/handoverDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/keyDoc/keyContentDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/keyDoc/keyDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/managerDoc/managerDoc_list.zul` | `vps.vm.DocumentVM` | — | — | ☠ VM không tồn tại |
| `document/managerDoc/managerDoc_list_add.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/office/editHistory.zul` | `widget.EditFileHistoryVM` | `WOPIBusiness` | — | BE |
| `document/office/editor.zul` | `vm.document.OfficeEditorVM` | — | — | — |
| `document/office/insertDocumentTemplate.zul` | `vm.document.SelectDocumentTemplateVM` | `DocumentBusiness` | — | BE |
| `document/office/selectDocumentTemplate.zul` | `vm.document.SelectDocumentTemplateVM` | `DocumentBusiness` | — | BE |
| `document/orgFollower/orgFollower.zul` | `vm.document.OrgFollowerVM` | — | `ISysUser` | LEGACY |
| `document/orgFollower/orgFollowerDocOut.zul` | `vm.document.DocumentSendSearchVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `document/orgFollower/orgFollowerGroup.zul` | `vm.document.DocumentSendSearchVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `document/seachDoc/searchAnnouncedDocument.zul` | `vm.document.SearchAnnouncedDocumentVM` | `SearchSolrBusiness` | — | BE |
| `document/supervisionDoc/supervisionContentDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/supervisionDoc/supervisionDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/transferDoc/viewListHistory.zul` | `vm.document.DocumentLogInfoVM` | `DocumentHistoryLogBusiness` | — | BE |
| `document/viewDoc/listDocReceiver.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/viewRepayDoc/viewRepayContentDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/viewRepayDoc/viewRepayDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `documentDraft/advancedSearch/advancedSearchDocument.zul` | `vm.document.DocumentSendSearchVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `EnterpriseBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `documentDraft/advancedSearch/advancedSearchDocument_viewDetail.zul` | `vm.admin.requisition.RequisitionViewDetailVM` | — | — | ☠ VM không tồn tại |
| `documentHandover/documentBook.zul` | `vm.documentHandover.DocumentBookVM` | `DocHandoverBusiness`, `DocumentBusiness`, `TextBookBusiness` | — | BE |
| `documentHandover/documentHandover.zul` | `vm.documentHandover.DocumentHandoverVM` | `DocHandoverBusiness` | — | BE |
| `documentHandover/documentHandoverHistory.zul` | `vm.documentHandover.DocumentHandoverHistoryVM` | `DocHandoverBusiness` | — | BE |
| `documentHandover/popupDocHandoverHistory.zul` | `vm.documentHandover.PopupHandoverHistoryVM` | `DocHandoverBusiness` | — | BE |
| `documentScope/documentScope.zul` | `vm.documentScope.DocumentScopeVM` | — | — | — |
| `documentScope/documentScope_detail.zul` | `vm.documentScope.DocumentScopeDetailVM` | — | — | — |
| `savePersonalDoc/savePersonalDoc.zul` | `vm.savePersonalDoc.SavePersonalDocVM` | `DocumentBusiness`, `MeetingBusiness`, `PersonalDocCategoryBusiness`, `SavePersonalDocBusiness` | `ICommon`, `IMeeting` | BE+LEGACY |
| `widgets/documentScopeLookup.zul` | `widget.DocumentScopeLookupVM` | — | — | — |
| `widgets/configPersonalDocCategory.zul` | `widget.ConfigPersonalDocCategoryVM` | `PersonalDocCategoryBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.document.DocumentCreateTaskVM` | — | — | — |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### DocHandoverBusiness

`web-spring/src/main/java/com/voffice/service/business/DocHandoverBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `DocumentHandoverAction.exportReportDocument` | `/DocumentHandoverAction/exportReportDocument` | `DocumentHandoverAction.exportReportDocument` | gen1 |
| `DocumentHandoverAction.getDetailDocumentHandover` | `/DocumentHandoverAction/getDetailDocumentHandover` | `DocumentHandoverAction.getDetailDocumentHandover` | gen1 |
| `DocumentHandoverAction.handOverDocument` | `/DocumentHandoverAction/handOverDocument` | `DocumentHandoverAction.handOverDocument` | gen1 |
| `DocumentHandoverAction.historyDocumentHandover` | `/DocumentHandoverAction/historyDocumentHandover` | `DocumentHandoverAction.historyDocumentHandover` | gen1 |
| `DocumentHandoverAction.searchDocumentHandover` | `/DocumentHandoverAction/searchDocumentHandover` | `DocumentHandoverAction.searchDocumentHandover` | gen1 |
| `DocumentHandoverAction.tableOfIncomingDocuments` | `/DocumentHandoverAction/tableOfIncomingDocuments` | `DocumentHandoverAction.exportIndexIncomingDocumentV2` | gen1 |
| `DocumentHandoverAction.tableOfOutgoingDocuments` | `/DocumentHandoverAction/tableOfOutgoingDocuments` | `DocumentHandoverAction.exportIndexOutgoingDocumentV2` | gen1 |
| `api.doc.export-daily-document` | `/api/doc/export-daily-document` | `DocController.generatSubmissionFile` | gen2 |
| `api.doc.export-daily-vptwd-document` | `/api/doc/export-daily-vptwd-document` | `DocController.exportDailyVPTWDDocument` | gen2 |
| `api.doc.export-daily-vptwd-document-to` | `/api/doc/export-daily-vptwd-document-to` | `DocController.exportDailyVPTWDDocumentTo` | gen2 |

### DocumentBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Brief.getListBriefInfo` | `/Brief/getListBriefInfo` | `BriefManagementAction.getListBriefInfo` | gen1 |
| `CvGroupAction.getCountListGroup` | `/CvGroupAction/getCountListGroup` | `CvGroupAction.getCountListGroup` | gen1 |
| `CvGroupAction.getListGroup` | `/CvGroupAction/getListGroup` | `CvGroupAction.getListGroup` | gen1 |
| `CvGroupAction.getListGroupMultiTransfer` | `/CvGroupAction/getListGroupMultiTransfer` | `CvGroupAction.getListGroupMultiTransfer` | gen1 |
| `CvGroupAction.getListGroups` | `/CvGroupAction/getListGroups` | `CvGroupAction.getListGroups` | gen1 |
| `CvGroupAction.getListStaffOfGroup` | `/CvGroupAction/getListStaffOfGroup` | `CvGroupAction.getListStaffOfGroup` | gen1 |
| `DocOrgRepublish.getBaseDocument` | `/DocOrgRepublish/getBaseDocument` | `DocOrgRepublishAction.getBaseDocument` | gen1 |
| `DocumentAction.AddDocument` | `/DocumentAction/AddDocument` | `DocumentAction.addDocument` | gen1 |
| `DocumentAction.AddDocumentAttachment` | `/DocumentAction/AddDocumentAttachment` | `DocumentAction.addDocumentAttachment` | gen1 |
| `DocumentAction.DeleteDocument` | `/DocumentAction/DeleteDocument` | `DocumentAction.deleteDocument` | gen1 |
| `DocumentAction.DeleteDocumentReturned` | `/DocumentAction/DeleteDocumentReturned` | `DocumentAction.deleteDocumentReturned` | gen1 |
| `DocumentAction.EditDocument` | `/DocumentAction/EditDocument` | `DocumentAction.editDocument` | gen1 |
| `DocumentAction.EditDocumentInGroupTag` | `/DocumentAction/EditDocumentInGroupTag` | `DocumentAction.editDocumentInGroupTag` | gen1 |
| `DocumentAction.EditDocumentInStaffTag` | `/DocumentAction/EditDocumentInStaffTag` | `DocumentAction.editDocumentInStaffTag` | gen1 |
| `DocumentAction.EditDocumentTag` | `/DocumentAction/EditDocumentTag` | `DocumentAction.editDocumentTag` | gen1 |
| `DocumentAction.ExtendDocument` | `/DocumentAction/ExtendDocument` | `DocumentAction.extendDocument` | gen1 |
| `DocumentAction.GetRegisterNumberIndex` | `/DocumentAction/GetRegisterNumberIndex` | `DocumentAction.getRegisterNumberIndex` | gen1 |
| `DocumentAction.ReportdocumentTransferHistory` | `/DocumentAction/ReportdocumentTransferHistory` | `DocumentAction.reportdocumentTransferHistory` | gen1 |
| `DocumentAction.SplitDocument` | `/DocumentAction/SplitDocument` | `DocumentAction.splitDocument` | gen1 |
| `DocumentAction.UpdateReadingStatus` | `/DocumentAction/UpdateReadingStatus` | `DocumentAction.updateReadingStatus` | gen1 |
| `DocumentAction.addDocumentMeetingReq` | `/DocumentAction/addDocumentMeetingReq` | `DocumentAction.addDocumentMeetingReq` | gen1 |
| `DocumentAction.addMeetingRequest` | `/DocumentAction/addMeetingRequest` | `DocumentAction.addMeetingRequest` | gen1 |
| `DocumentAction.cancelDocReceiveMap` | `/DocumentAction/cancelDocReceiveMap` | `DocumentAction.cancelDocReceiveMap` | gen1 |
| `DocumentAction.check-permission-export` | `/DocumentAction/check-permission-export` | `DocumentAction.checkPermissionExport` | gen1 |
| `DocumentAction.checkHadInDocCreator` | `/DocumentAction/checkHadInDocCreator` | `IndexController.redirect` | gen2 |
| `DocumentAction.checkIsPublished` | `/DocumentAction/checkIsPublished` | `DocumentAction.checkIsPublished` | gen1 |
| `DocumentAction.checkPermitViewDocument` | `/DocumentAction/checkPermitViewDocument` | `DocumentAction.checkPermitViewDocument` | gen1 |
| `DocumentAction.countDocument` | `/DocumentAction/countDocument` | `DocumentAction.countDocument` | gen1 |
| `DocumentAction.countDocumentByStatus` | `/DocumentAction/countDocumentByStatus` | `DocumentAction.countDocumentByStatus` | gen1 |
| `DocumentAction.countDocumentIn` | `/DocumentAction/countDocumentIn` | `DocumentAction.countDocumentIn` | gen1 |
| `DocumentAction.countDocumentOut` | `/DocumentAction/countDocumentOut` | `DocumentAction.countDocumentOut` | gen1 |
| `DocumentAction.doSubmitForConsideration` | `/DocumentAction/doSubmitForConsideration` | `DocumentAction.doSubmitForConsideration` | gen1 |
| `DocumentAction.docReceivedDocument` | `/DocumentAction/docReceivedDocument` | `DocumentAction.docReceivedDocument` | gen1 |
| `DocumentAction.exportCirculationTree` | `/DocumentAction/exportCirculationTree` | `DocumentAction.exportCirculationTree` | gen1 |
| `DocumentAction.exportDocumentCopy` | `/DocumentAction/exportDocumentCopy` | `DocumentAction.exportDocumentCopy` | gen1 |
| `DocumentAction.exportFinanceText` | `/DocumentAction/exportFinanceText` | `DocumentAction.exportFinanceText` | gen1 |
| `DocumentAction.getAdjacentListByDocumentId` | `/DocumentAction/getAdjacentListByDocumentId` | `DocumentAction.getAdjacentListByDocumentId` | gen1 |
| `DocumentAction.getDocSendInfoByIds` | `/DocumentAction/getDocSendInfoByIds` | `DocumentAction.getDocSendInfoByIds` | gen1 |
| `DocumentAction.getDocumentAdjacentList` | `/DocumentAction/getDocumentAdjacentList` | `DocumentAction.getDocumentAdjacentList` | gen1 |
| `DocumentAction.getDocumentAttach` | `/DocumentAction/getDocumentAttach` | `DocumentAction.getDocumentAttach` | gen1 |
| `DocumentAction.getDocumentByIds` | `/DocumentAction/getDocumentByIds` | `DocumentAction.getDocumentByIds` | gen1 |
| `DocumentAction.getDocumentDetail` | `/DocumentAction/getDocumentDetail` | `DocumentAction.getDocumentDetail` | gen1 |
| `DocumentAction.getDocumentForReminder` | `/DocumentAction/getDocumentForReminder` | `DocumentAction.getDocumentForReminder` | gen1 |
| `DocumentAction.getDocumentListVof2` | `/DocumentAction/getDocumentListVof2` | `DocumentAction.getDocumentListVof2` | gen1 |
| `DocumentAction.getDocumentMeetingReq` | `/DocumentAction/getDocumentMeetingReq` | `DocumentAction.getDocumentMeetingReq` | gen1 |
| `DocumentAction.getDocumentOutIssueNumber` | `/DocumentAction/getDocumentOutIssueNumber` | `DocumentAction.getDocumentOutIssueNumber` | gen1 |
| `DocumentAction.getDocumentStaffEntity` | `/DocumentAction/getDocumentStaffEntity` | `DocumentAction.getDocumentStaffEntity` | gen1 |
| `DocumentAction.getDocumentTypeId` | `/DocumentAction/getDocumentTypeId` | `IndexController.redirect` | gen2 |
| `DocumentAction.getDocumentViewerUserId` | `/DocumentAction/getDocumentViewerUserId` | `DocumentAction.getDocumentViewerUserId` | gen1 |
| `DocumentAction.getInforProposal` | `/DocumentAction/getInforProposal` | `DocumentAction.getInforProposal` | gen1 |
| `DocumentAction.getListAllFileDocAttach` | `/DocumentAction/getListAllFileDocAttach` | `DocumentAction.getListAllFileDocAttach` | gen1 |
| `DocumentAction.getListCommentFromDocument` | `/DocumentAction/getListCommentFromDocument` | `DocumentAction.getListCommentFromDocument` | gen1 |
| `DocumentAction.getListCommentLeaderFromDocument` | `/DocumentAction/getListCommentLeaderFromDocument` | `DocumentAction.getListCommentLeaderFromDocument` | gen1 |
| `DocumentAction.getListDocumentInStaffEntity` | `/DocumentAction/getListDocumentInStaffEntity` | `DocumentAction.getListDocumentInStaffEntity` | gen1 |
| `DocumentAction.getListGroup` | `/DocumentAction/getListGroup` | `DocumentAction.getListGroup` | gen1 |
| `DocumentAction.getListGroupFromDocAndReceive` | `/DocumentAction/getListGroupFromDocAndReceive` | `DocumentAction.getListGroupFromDocAndReceive` | gen1 |
| `DocumentAction.getListGroupMultiTransfer` | `/DocumentAction/getListGroupMultiTransfer` | `DocumentAction.getListGroupMultiTransfer` | gen1 |
| `DocumentAction.getListOfficeOutside` | `/DocumentAction/getListOfficeOutside` | `DocumentAction.getListOfficeOutside` | gen1 |
| `DocumentAction.getListReceivedPersonalGroup` | `/DocumentAction/getListReceivedPersonalGroup` | `DocumentAction.getListReceivedPersonalGroup` | gen1 |
| `DocumentAction.getListReceivedStaffInDepartment` | `/DocumentAction/getListReceivedStaffInDepartment` | `DocumentAction.getListReceivedStaffInDepartment` | gen1 |
| `DocumentAction.getListReceivedStaffInPersonalGroup` | `/DocumentAction/getListReceivedStaffInPersonalGroup` | `DocumentAction.getListReceivedStaffInPersonalGroup` | gen1 |
| `DocumentAction.getListReceiver` | `/DocumentAction/getListReceiver` | `DocumentAction.getListReceiver` | gen1 |
| `DocumentAction.getListReminderForDetail` | `/DocumentAction/getListReminderForDetail` | `DocumentAction.getListReminderForDetail` | gen1 |
| `DocumentAction.getListSignerReminder` | `/DocumentAction/getListSignerReminder` | `DocumentAction.getListSignerReminder` | gen1 |
| `DocumentAction.getListStaffReceiveFromDoc` | `/DocumentAction/getListStaffReceiveFromDoc` | `DocumentAction.getListStaffReceiveFromDoc` | gen1 |
| `DocumentAction.getMeetingAssistantByEmployeeIdAndAssiType` | `/DocumentAction/getMeetingAssistantByEmployeeIdAndAssiType` | `DocumentAction.getMeetingAssistantByEmployeeIdAndAssiType` | gen1 |
| `DocumentAction.getProcessedDetailByUser` | `/DocumentAction/getProcessedDetailByUser` | `DocumentAction.getProcessedDetailByUser` | gen1 |
| `DocumentAction.getProposalDetailDifferent` | `/DocumentAction/getProposalDetailDifferent` | `DocumentAction.getProposalDetailDifferent` | gen1 |
| `DocumentAction.getPublishedStatus` | `/DocumentAction/getPublishedStatus` | `DocumentAction.getPublishedStatus` | gen1 |
| `DocumentAction.getStatusDocumentInGroup` | `/DocumentAction/getStatusDocumentInGroup` | `DocumentAction.getStatusDocumentInGroup` | gen1 |
| `DocumentAction.getStatusDocumentInStaff` | `/DocumentAction/getStatusDocumentInStaff` | `DocumentAction.getStatusDocumentInStaff` | gen1 |
| `DocumentAction.getTextIdByDocId` | `/DocumentAction/getTextIdByDocId` | `DocumentAction.getTextId` | gen1 |
| `DocumentAction.getTextIdByDocumentId` | `/DocumentAction/getTextIdByDocumentId` | `DocumentAction.getTextIdByDocumentId` | gen1 |
| `DocumentAction.isDocumentStamped` | `/DocumentAction/isDocumentStamped` | `DocumentAction.isDocumentStamped` | gen1 |
| `DocumentAction.processConnectDocumentRecipient` | `/DocumentAction/processConnectDocumentRecipient` | `DocumentAction.processConnectDocumentRecipient` | gen1 |
| `DocumentAction.processingTranferBriefDoc` | `/DocumentAction/processingTranferBriefDoc` | `DocumentAction.processingTranferBriefDoc` | gen1 |
| `DocumentAction.retriveInforCreator` | `/DocumentAction/retriveInforCreator` | `DocumentAction.retriveInforCreator` | gen1 |
| `DocumentAction.rollBackDauXacNhan` | `/DocumentAction/rollBackDauXacNhan` | `DocumentAction.rollBackDauXacNhan` | gen1 |
| `DocumentAction.saveDocumentType` | `/DocumentAction/saveDocumentType` | `DocumentAction.saveDocumentType` | gen1 |
| `DocumentAction.saveOrUpdateViewDocSendInfo` | `/DocumentAction/saveOrUpdateViewDocSendInfo` | `DocumentAction.saveOrUpdateViewDocSendInfo` | gen1 |
| `DocumentAction.search` | `/DocumentAction/search` | `DocumentAction.search` | gen1 |
| `DocumentAction.searchDocumentIn` | `/DocumentAction/searchDocumentIn` | `DocumentAction.searchDocumentIn` | gen1 |
| `DocumentAction.searchDocumentInExport` | `/DocumentAction/searchDocumentInExport` | `DocumentAction.searchDocumentInExport` | gen1 |
| `DocumentAction.searchDocumentOut` | `/DocumentAction/searchDocumentOut` | `DocumentAction.searchDocumentOut` | gen1 |
| `DocumentAction.searchDocumentOutExport` | `/DocumentAction/searchDocumentOutExport` | `DocumentAction.searchDocumentOutExport` | gen1 |
| `DocumentAction.searchDocumentOutGroupByTextBook` | `/DocumentAction/searchDocumentOutGroupByTextBook` | `DocumentAction.searchDocumentOutGroupByTextBook` | gen1 |
| `DocumentAction.searchDocumentOutPublished` | `/DocumentAction/searchDocumentOutPublished` | `DocumentAction.searchDocumentOutPublished` | gen1 |
| `DocumentAction.searchDocumentOutPublishedExport` | `/DocumentAction/searchDocumentOutPublishedExport` | `DocumentAction.searchDocumentOutPublishedExport` | gen1 |
| `DocumentAction.searchDocumentScope` | `/DocumentAction/searchDocumentScope` | `DocumentAction.searchDocumentScope` | gen1 |
| `DocumentAction.searchFinancial` | `/DocumentAction/searchFinancial` | `DocumentAction.searchFinancial` | gen1 |
| `DocumentAction.searchReceive` | `/DocumentAction/searchReceive` | `DocumentAction.searchReceive` | gen1 |
| `DocumentAction.searchReceiveExport` | `/DocumentAction/searchReceiveExport` | `DocumentAction.searchReceiveExport` | gen1 |
| `DocumentAction.searchReceiveGroupByTextBook` | `/DocumentAction/searchReceiveGroupByTextBook` | `DocumentAction.searchInGroupByTextBook` | gen1 |
| `DocumentAction.searchReceiveWithProcessingStatsByUser` | `/DocumentAction/searchReceiveWithProcessingStatsByUser` | `DocumentAction.searchReceiveWithProcessingStatsByUser` | gen1 |
| `DocumentAction.sendDocument` | `/DocumentAction/sendDocument` | `DocumentAction.sendDocument` | gen1 |
| `DocumentAction.sendDocumentMultiTransfer` | `/DocumentAction/sendDocumentMultiTransfer` | `DocumentAction.sendDocumentMultiTransfer` | gen1 |
| `DocumentAction.sendFinanceTextToStaff` | `/DocumentAction/sendFinanceTextToStaff` | `DocumentAction.sendFinanceTextToStaff` | gen1 |
| `DocumentAction.tickProcessedDoc` | `/DocumentAction/tickProcessedDoc` | `DocumentAction.tickProcessedDoc` | gen1 |
| `DocumentAction.tranferTextPromulgateOrNotPromulgate` | `/DocumentAction/tranferTextPromulgateOrNotPromulgate` | `DocumentAction.tranferTextPromulgateOrNotPromulgate` | gen1 |
| `DocumentAction.unfollowDocument` | `/DocumentAction/unfollowDocument` | `DocumentAction.unfollowDocument` | gen1 |
| `DocumentAction.updateDocReceiveMap` | `/DocumentAction/updateDocReceiveMap` | `DocumentAction.updateDocReceiveMap` | gen1 |
| `DocumentAction.updateDocumentMeetingReq` | `/DocumentAction/updateDocumentMeetingReq` | `DocumentAction.updateDocumentMeetingReq` | gen1 |
| `DocumentAction.updateDocumentMeetingRequestAfterCreateMeeting` | `/DocumentAction/updateDocumentMeetingRequestAfterCreateMeeting` | `DocumentAction.updateDocumentMeetingRequestAfterCreateMeeting` | gen1 |
| `DocumentAction.updateDocumentProcessing` | `/DocumentAction/updateDocumentProcessing` | `DocumentAction.updateDocumentProcessing` | gen1 |
| `DocumentAction.updateDocumentProposal` | `/DocumentAction/updateDocumentProposal` | `IndexController.redirect` | gen2 |
| `DocumentAction.updateDuplicateReceivedDocument` | `/DocumentAction/updateDuplicateReceivedDocument` | `DocumentAction.updateDuplicateReceivedDocument` | gen1 |
| `DocumentAction.updateIsForwardByDocumentId` | `/DocumentAction/updateIsForwardByDocumentId` | `DocumentAction.updateIsForwardByDocumentId` | gen1 |
| `DocumentAction.updateIsForwardByDocumentIdMultiTransfer` | `/DocumentAction/updateIsForwardByDocumentIdMultiTransfer` | `DocumentAction.updateIsForwardByDocumentIdMultiTransfer` | gen1 |
| `DocumentAction.updateMeetingStatus` | `/DocumentAction/updateMeetingStatus` | `DocumentAction.updateMeetingStatus` | gen1 |
| `DocumentAction.updateReadingStatusV2` | `/DocumentAction/updateReadingStatusV2` | `DocumentAction.updateReadingStatusV2` | gen1 |
| `DocumentAction.updateStatusDocument` | `/DocumentAction/updateStatusDocument` | `DocumentAction.updateStatusDocument` | gen1 |
| `DocumentAction.updateStatusDocumentInStaff` | `/DocumentAction/updateStatusDocumentInStaff` | `DocumentAction.updateStatusDocumentInStaff` | gen1 |
| `DocumentAction.verifyExternalSignature` | `/DocumentAction/verifyExternalSignature` | `DocumentAction.verifyExternalSignature` | gen1 |
| `DocumentAction.verifyExternalSignatureMigratedDoc` | `/DocumentAction/verifyExternalSignatureMigratedDoc` | `DocumentAction.verifyExternalSignatureMigratedDoc` | gen1 |
| `Files.DownloadContentFile` | `/Files/DownloadContentFile` | `FileService.downloadContentFile` | gen1 |
| `Files.DownloadDocumentErrorFile` | `/Files/DownloadDocumentErrorFile` | `FileService.downloadDocumentErrorFile` | gen1 |
| `Files.DownloadStreamMigratedFile` | `/Files/DownloadStreamMigratedFile` | `FileService.downloadStreamMigratedFile` | gen1 |
| `Files.d2SOCRSummarizeDocument` | `/Files/d2SOCRSummarizeDocument` | `FileService.d2SOCRSummarizeDocument` | gen1 |
| `Files.downloadContentFileCommentSign` | `/Files/downloadContentFileCommentSign` | `FileService.downloadContentFileCommentSign` | gen1 |
| `Meeting.getMissionByMeetingId` | `/Meeting/getMissionByMeetingId` | `MettingResource.getMissionByMeetingId` | gen1 |
| `Sign.updateDatabaseDocumentAfterMark` | `/Sign/updateDatabaseDocumentAfterMark` | `SignResource.updateDatabaseDocumentAfterMark` | gen1 |
| `VHROrgAction.getListVHROrgByScopes` | `/VHROrgAction/getListVHROrgByScopes` | `VHROrgAction.getListVHROrgByScopes` | gen1 |
| `VHROrgAction.getVHROrg` | `/VHROrgAction/getVHROrg` | `VHROrgAction.getVHROrg` | gen1 |
| `api.brief-detail.get-list-document-in` | `/api/brief-detail/get-list-document-in` | `BriefDetailManagementController.getListDocumentIn` | gen1 |
| `api.doc-chat` | `/api/doc-chat` | `DocumentChatController.updateDocumentChat` | gen2 |
| `api.doc-chat.delete` | `/api/doc-chat/delete` | `DocumentChatController.deleteDocChat` | gen2 |
| `api.doc-in.check-completion-reminders` | `/api/doc-in/check-completion-reminders` | `DocInController.checkCompletionReminders` | gen2 |
| `api.doc-in.complete-document` | `/api/doc-in/complete-document` | `DocInController.completeDocument` | gen2 |
| `api.doc-in.documents.file-encrypt-map` | `/api/doc-in/documents/file-encrypt-map` | `DocInController.findDocFileEncryptByDocIds` | gen2 |
| `api.doc-in.get-all-file-encrypt-map-by-fileId` | `/api/doc-in/get-all-file-encrypt-map-by-fileId` | `DocInController.getAllFileEncryptMap` | gen2 |
| `api.doc-in.get-file-encrypt-map` | `/api/doc-in/get-file-encrypt-map` | `DocInController.getFileEncryptMap` | gen2 |
| `api.doc-in.get-list-file-encrypt-map` | `/api/doc-in/get-list-file-encrypt-map` | `DocInController.findDocFileEncryptByDocId` | gen2 |
| `api.doc-in.is-duplicated-register-book-number` | `/api/doc-in/is-duplicated-register-book-number` | `DocInController.checkExistRegisterBookNumber` | gen2 |
| `api.doc-in.is-duplicated-register-number` | `/api/doc-in/is-duplicated-register-number` | `DocInController.completeDocument` | gen2 |
| `api.doc-in.is-existing-send-to-preside` | `/api/doc-in/is-existing-send-to-preside` | `DocInController.isExistingSendToPreside` | gen2 |
| `api.doc-in.issued.encrypted-files` | `/api/doc-in/issued/encrypted-files` | `DocInController.getEncryptedFilesForIssuedDoc` | gen2 |
| `api.doc-in.list-exist-document` | `/api/doc-in/list-exist-document` | `DocInController.getListExistDocument` | gen2 |
| `api.doc-in.list-exist-document-by-textbook-and-register` | `/api/doc-in/list-exist-document-by-textbook-and-register` | `DocInController.getListDocumentExistByTextBookAndRegisterNumber` | gen2 |
| `api.doc-in.node-detail2` | `/api/doc-in/node-detail2` | `DocInController.getNodeDetail2` | gen2 |
| `api.doc-in.return-document` | `/api/doc-in/return-document` | `DocInController.returnDocument` | gen2 |
| `api.doc-in.transferred` | `/api/doc-in/transferred` | `DocInController.getTransferredList` | gen2 |
| `api.doc-in.update-exist-connect-document` | `/api/doc-in/update-exist-connect-document` | `DocInController.updateExistConnectDocument` | gen2 |
| `api.doc-in.update-status-dis-proposal` | `/api/doc-in/update-status-dis-proposal` | `DocInController.updateStatusDisWhenAcceptProposal` | gen2 |
| `api.doc-in.update-status-document-in-group` | `/api/doc-in/update-status-document-in-group` | `DocInController.updateStatusDocumentInGroup` | gen2 |
| `api.doc-in.update-status-document-in-staff` | `/api/doc-in/update-status-document-in-staff` | `DocInController.updateStatusDocumentInStaff` | gen2 |
| `api.doc-leader-comment.save-doc-leader-comment` | `/api/doc-leader-comment/save-doc-leader-comment` | `DocLeaderCommentController.saveDocumentLeaderComment` | gen2 |
| `api.doc-out.is-duplicated-register-number` | `/api/doc-out/is-duplicated-register-number` | `DocOutController.checkExistRegisterBookNumber` | gen2 |
| `api.doc.add-document-template` | `/api/doc/add-document-template` | `DocController.addDocumentTemplate` | gen2 |
| `api.doc.get-document-template-default` | `/api/doc/get-document-template-default` | `DocController.getDocumentTemplateDefault` | gen2 |
| `api.doc.get-url-send-document` | `/api/doc/get-url-send-document` | `DocController.getUrlSendDocument` | gen2 |
| `api.doc.search-document-template` | `/api/doc/search-document-template` | `DocController.searchDocumentTemplate` | gen2 |
| `api.document-in.get-documents-processing-stats-by-user` | `/api/document-in/get-documents-processing-stats-by-user` | `DocumentInController.getDocumentsProcessingStatsByUser` | gen1 |
| `api.document-in.get-list-cv-group` | `/api/document-in/get-list-cv-group` | `DocumentInController.getListCvGroup` | gen1 |
| `api.document-in.get-list-receiver-text-transfer` | `/api/document-in/get-list-receiver-text-transfer` | `DocumentInController.getListReceiverTextTransfer` | gen1 |
| `api.document-informality.get-leader-same-receive` | `/api/document-informality/get-leader-same-receive` | `DocumentInformalityController.getLeaderSameReceive` | gen2 |
| `api.document-informality.is-document-assistant` | `/api/document-informality/is-document-assistant` | `DocumentInformalityController.isDocumentAssistant` | gen2 |
| `api.document-informality.update-to-informality` | `/api/document-informality/update-to-informality` | `DocumentInformalityController.updateToInformality` | gen2 |
| `api.flow-manager.doc-in.consideration.get-groups-next-step` | `/api/flow-manager/doc-in/consideration/get-groups-next-step` | `FlowManagerController.getGroupsNextStepConsideration` | gen2 |
| `api.flow-manager.doc-in.consideration.get-users-next-step` | `/api/flow-manager/doc-in/consideration/get-users-next-step` | `FlowManagerController.getUsersNextStepConsideration` | gen2 |
| `api.flow-manager.doc-in.get-groups-next-step` | `/api/flow-manager/doc-in/get-groups-next-step` | `FlowManagerController.DocInGetGroupsNextStep` | gen2 |
| `api.flow-manager.doc-in.get-groups-next-step-multi-transfer` | `/api/flow-manager/doc-in/get-groups-next-step-multi-transfer` | `FlowManagerController.DocInGetGroupsNextStepMultiTransfer` | gen2 |
| `api.flow-manager.doc-in.get-groups-next-step-while-creating-document` | `/api/flow-manager/doc-in/get-groups-next-step-while-creating-document` | `FlowManagerController.DocInGetGroupsNextStep` | gen2 |
| `api.flow-manager.doc-in.get-groups-tree-next-step` | `/api/flow-manager/doc-in/get-groups-tree-next-step` | `FlowManagerController.DocInGetGroupsTreeNextStep` | gen2 |
| `api.flow-manager.doc-in.get-groups-tree-next-step-multi-transfer` | `/api/flow-manager/doc-in/get-groups-tree-next-step-multi-transfer` | `FlowManagerController.DocInGetGroupsTreeNextStepMultiTransfer` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step` | `/api/flow-manager/doc-in/get-users-next-step` | `FlowManagerController.DocInGetUsersNextStep` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-by-org-id` | `/api/flow-manager/doc-in/get-users-next-step-by-org-id` | `FlowManagerController.DocInGetUsersNextStepByOrgId` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-doc-show` | `/api/flow-manager/doc-in/get-users-next-step-doc-show` | `FlowManagerController.DocInGetUsersNextStepDocShow` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-multi-transfer` | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer` | `FlowManagerController.DocInGetUsersNextStepMultiTransfer` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-multi-transfer-by-org-id` | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer-by-org-id` | `FlowManagerController.DocInGetUsersNextStepMultiTransferByOrgId` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-multi-transfer-show` | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer-show` | `FlowManagerController.DocInGetUsersNextStepMultiTransferShow` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-show` | `/api/flow-manager/doc-in/get-users-next-step-show` | `FlowManagerController.DocInGetUsersNextStepShow` | gen2 |
| `api.flow-manager.doc-in.get-users-next-step-while-creating-document` | `/api/flow-manager/doc-in/get-users-next-step-while-creating-document` | `FlowManagerController.DocInGetUsersNextStep` | gen2 |
| `api.flow-manager.doc-in.get-users-tree-next-step` | `/api/flow-manager/doc-in/get-users-tree-next-step` | `FlowManagerController.DocInGetUsersTreeNextStep` | gen2 |
| `api.flow-manager.doc-in.get-users-tree-next-step-multi-transfer` | `/api/flow-manager/doc-in/get-users-tree-next-step-multi-transfer` | `FlowManagerController.DocInGetUsersTreeNextStepMultiTransfer` | gen2 |
| `configParamAction.GetAppConfig` | `/configParamAction/GetAppConfig` | `ConfigParameterAction.getAppConfig` | gen1 |
| `missionAction.getListCombinationOrg` | `/missionAction/getListCombinationOrg` | `MissionAction.getListCombinationOrg` | gen1 |
| `staffAction.getListUserTransfer` | `/staffAction/getListUserTransfer` | `StaffAction.getListUserTransfer` | gen1 |
| `taskAction.getListTaskFromDocument` | `/taskAction/getListTaskFromDocument` | `TaskAction.getListTaskFromDocument` | gen1 |
| `textAction.searchText` | `/textAction/searchText` | `TextAction.searchText` | gen1 |

### DocumentCopyHistoryBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentCopyHistoryBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.document-copy.check-permission` | ❓ không tìm thấy endpoint | | |

### DocumentHistoryLogBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentHistoryLogBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.document-history-log.search` | `/api/document-history-log/search` | `DocumentHistoryLogController.searchWorkGroup` | gen2 |

### DocumentKpiBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentKpiBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.personal-treatment-status.get-document-kpi` | `/api/personal-treatment-status/get-document-kpi` | `PersonalTreatmentStatusController.getDocumentKpi` | gen2 |
| `api.personal-treatment-status.get-list-user-id` | `/api/personal-treatment-status/get-list-user-id` | `PersonalTreatmentStatusController.getListUserIdOfOrganization` | gen2 |
| `api.personal-treatment-status.get-total-document-kpi` | `/api/personal-treatment-status/get-total-document-kpi` | `PersonalTreatmentStatusController.getTotalDocumentKpi` | gen2 |

### DocumentRequestBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentRequestBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `VHROrgAction.getDocumentManagerVhrOrg` | `/VHROrgAction/getDocumentManagerVhrOrg` | `VHROrgAction.getDocumentManagerVhrOrg` | gen1 |
| `answerDocumentAction.deleteRequestedObject` | `/answerDocumentAction/deleteRequestedObject` | `AnswerDocumentAction.deleteRequestedObject` | gen1 |
| `answerDocumentAction.getChair` | `/answerDocumentAction/getChair` | `AnswerDocumentAction.getChair` | gen1 |
| `answerDocumentAction.getRelyRequestPermission` | `/answerDocumentAction/getRelyRequestPermission` | `AnswerDocumentAction.getRelyRequestPermission` | gen1 |
| `answerDocumentAction.getReplyRequestDetail` | `/answerDocumentAction/getReplyRequestDetail` | `AnswerDocumentAction.getReplyRequestDetail` | gen1 |
| `answerDocumentAction.getRequestedObject` | `/answerDocumentAction/getRequestedObject` | `AnswerDocumentAction.getRequestedObject` | gen1 |
| `answerDocumentAction.getReturnList` | `/answerDocumentAction/getReturnList` | `AnswerDocumentAction.getReturnList` | gen1 |
| `answerDocumentAction.replyDocumentUpdate` | `/answerDocumentAction/replyDocumentUpdate` | `AnswerDocumentAction.replyDocumentUpdate` | gen1 |
| `answerDocumentAction.sendDocumentReplyRequest` | `/answerDocumentAction/sendDocumentReplyRequest` | `AnswerDocumentAction.sendDocumentReplyRequest` | gen1 |
| `documentProcessTermConfig.getConfigsByCondition` | `/documentProcessTermConfig/getConfigsByCondition` | `DocumentProcessTermConfigAction.getConfigsByCondition` | gen1 |
| `documentProcessTermConfig.getConfigsByListOrgIds` | `/documentProcessTermConfig/getConfigsByListOrgIds` | `DocumentProcessTermConfigAction.getConfigsByListOrgIds` | gen1 |

### DocumentTypeBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentTypeBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.document-types.convert-doc-type-to-common` | `/api/document-types/convert-doc-type-to-common` | `DocumentTypeController.convertDocTypeToCommon` | gen2 |
| `api.document-types.create` | `/api/document-types/create` | `DocumentTypeController.createDocumentType` | gen2 |
| `api.document-types.create-doc-type-org` | `/api/document-types/create-doc-type-org` | `DocumentTypeController.createDocTypeOrg` | gen2 |
| `api.document-types.delete` | `/api/document-types/delete` | `DocumentTypeController.deleteDocumentType` | gen2 |
| `api.document-types.get-max-order-number` | `/api/document-types/get-max-order-number` | `DocumentTypeController.getMaxOrderNumber` | gen2 |
| `api.document-types.get-orgs-by-doc-type-id` | `/api/document-types/get-orgs-by-doc-type-id` | `DocumentTypeController.getOrganizationIdsByDocTypeId` | gen2 |
| `api.document-types.granted-doc-type-to-orgs` | `/api/document-types/granted-doc-type-to-orgs` | `DocumentTypeController.grantedDocTypeToOrgs` | gen2 |
| `api.document-types.search` | `/api/document-types/search` | `DocumentTypeController.search` | gen2 |

### PersonalDocCategoryBusiness

`web-spring/src/main/java/com/voffice/service/business/PersonalDocCategoryBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.personal-category.check-empty-category` | `/api/personal-category/check-empty-category` | `PersonalCategoryController.checkEmptyCategory` | gen2 |
| `api.personal-category.create` | `/api/personal-category/create` | `PersonalCategoryController.create` | gen2 |
| `api.personal-category.delete` | `/api/personal-category/delete` | `PersonalCategoryController.delete` | gen2 |
| `api.personal-category.get-list` | `/api/personal-category/get-list` | `PersonalCategoryController.getListByEmployeeId` | gen2 |
| `api.personal-category.update` | `/api/personal-category/update` | `PersonalCategoryController.update` | gen2 |

### SavePersonalDocBusiness

`web-spring/src/main/java/com/voffice/service/business/SavePersonalDocBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `commentAction.checkSavedPersonalStorage` | `/commentAction/checkSavedPersonalStorage` | `CommentAction.checkSavedPersonalStorage` | gen1 |
| `commentAction.getPersonalStorageByObjTypeIdUser` | `/commentAction/getPersonalStorageByObjTypeIdUser` | `CommentAction.getPersonalStorageByObjTypeIdUser` | gen1 |
| `commentAction.savePersonalStorage` | `/commentAction/savePersonalStorage` | `CommentAction.savePersonalStorage` | gen1 |
| `commentAction.searchPeronalStorage` | `/commentAction/searchPeronalStorage` | `CommentAction.searchPeronalStorage` | gen1 |
| `commentAction.updateCategoryOfPersonalStorage` | `/commentAction/updateCategoryOfPersonalStorage` | `CommentAction.updateCategoryOfPersonalStorage` | gen1 |

### ScheduleToMeetingDocumentBusiness

`web-spring/src/main/java/com/voffice/service/business/ScheduleToMeetingDocumentBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `DocumentAction.cancelMeetingRequest` | `/DocumentAction/cancelMeetingRequest` | `DocumentAction.cancelMeetingRequest` | gen1 |
| `DocumentAction.searchDocumentScheduleMeeting` | `/DocumentAction/searchDocumentScheduleMeeting` | `DocumentAction.searchDocumentScheduleMeeting` | gen1 |
| `DocumentAction.searchMeetingRequests` | `/DocumentAction/searchMeetingRequests` | `DocumentAction.searchMeetingRequests` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### CorrectDocument (gen1) — base `/CorrectDocument`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CorrectDocument.java`

- Logic (gen-1 `controler/`): `CorrectDocumentControler`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/CorrectDocument/checkCorrectDocument` | `checkCorrectDocument` |

</details>

### DocumentAction (gen1) — base `/DocumentAction`, 133 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentAction.java`

- Logic (gen-1 `controler/`): `DocumentController`, `CommonControler`, `CvGroupController`, `SignatureVerificationController`, `DocumentSearchReceiveController`, `TextController`, `EmpCloudCAService`
- Service: `CategoryCacheService`, `CategoryCommonService`, `CategoryCommonServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SigningFlowUpdateService`, `DocService`, `DocServiceImpl`, `DocumentCopyService`, `DocumentCopyServiceImpl`, `DocumentHistoryLogService`, `DocumentHistoryLogServiceImpl`, `DocumentKpiTransferService`, `DocumentKpiTransferServiceImpl`, `DocumentKpiMissionClient`, `DocumentProposalDetailService`, `DocumentProposalDetailServiceImpl`, `DocumentProposalService`, `DocumentProposalServiceImpl`, `ElasticDocumentService`, `ElasticDocumentServiceImpl`, `ShareDocumentService`, `ShareDocumentServiceImpl`, `ExtShareConfigService`, `ExtShareConfigServiceImpl`, `TagDictionaryService`, `TagDictionaryServiceImpl`, `VhrEmployeeService`, `VhrEmployeeServiceImpl`, `DocLeaderCommentService`, `DocLeaderCommentServiceImpl`, `DocumentPermissionCacheService`, `DraftLifecycleEventService`, `DraftLifecycleEventServiceImpl`, `DraftLifecycleMissionClient`, `ManagerService`, `ManagerServiceImpl`, `OfficePublishedReplacementService`, `OfficePublishedReplacementServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`, `TextDraftService`, `TextDraftServiceImpl`, `TextProcessService`, `TextProcessServiceImpl`, `TextReceiverGroupDetailService`, `TextReceiverGroupDetailServiceImpl`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AnswerDocumentDAO`, `AttachDAO`, `BriefManagementDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `ConnectDocumentDAO`, `ConnectVHRDao`, `CvGroupDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `HistoryChangeSignDAO`, `StaffDAO`, `DocumentHandoverDAO`, `DocumentCommonService`, `DocumentDAO`, `DocumentScopeDAO`, `DocumentSignDAO`, `DocumentLibraryDAO`, `DocumentPublishedDAO`, `DocumentSearchInGroupByTextBookService`, `DocumentSearchInService`, `DocumentSendViewInfoDAO`, `FilesAttachmentDAO`, `MeetingAssistantDAO`, `MeetingDAO`, `SourceMapDAO`, `TextDAO`, `TextSignDAO`, `AutoDigitalSignDAO`, `BriefDetailManagementDAO`, `CloudDeviceCertDAO`, `DocOrgRepublishDAO`, `DocumentPublishedTmpDAO`, `EmpCloudCADAO`, `StaffImageSignDAO`, `MeetingWeekDAO`, `MissionDAO`, `MissionSigningDAO`, `OrgDAO`, `P12CertDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `SysRoleDAO`, `TextBookDAO`, `TextCheckSpellDAO`, `TextCommonDAO`, `TextEditHistoryDAO`, `TextProcessDAO`, `ImageSignDao`, `TextProcessHistoryDAO`, `TextReceiverDAO`, `TextReceiverGroupDAO`
- Repository (JPA): `AttachTemplateRepositoryJPA`, `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReportDailyHistoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `VhrEmployeeJPA`, `SystemParameterRepositoryJPA`, `CvPriorityRepositoryJPA`, `DocumentTemplateRepositoryJPA`, `TextBookRepositoryJPA`, `DocumentCopyHistoryJPA`, `BriefEntityRepositoryJPA`, `DocumentHistoryLogJPA`, `DocumentTypeRepositoryJPA`, `VhrOrgJPA`, `DocumentProposalDetailJpa`, `DocumentScopeRefRepository`, `ElasticDocumentPrivateRepositoryJPA`, `ElasticDocumentPublicRepositoryJPA`, `ExtDocumentAccessLogJPA`, `ExtDocumentJPA`, `ExtShareConfigJPA`, `ExtShareConfigRepositoryJPA`, `ExtShareScopeJPA`, `TagDictionaryJpa`, `UserRoleJPA`, `ExtAppApiEntityRepositoryJPA`, `ExtAppEntityRepositoryJPA`, `AttachRepositoryJPA`, `BriefDocumentMapRepositoryJPA`, `ConfigSmsModuleRepositoryJPA`, `EmpCaDetailRepositoryJPA`, `EmpCaRepositoryJPA`, `FeedbackImageRepositoryJPA`, `FeedbackLogFileRepositoryJPA`, `FeedbackProcessRepositoryJPA`, `FeedbackRepositoryJPA`, `ImageOrgConfigRepositoryJPA`, `ImageOrgRepositoryJPA`, `MenuRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `RolePermissionBaseRepositoryJPA`, `RolePermissionDataRepositoryJPA`, `SmsBlackListRepositoryJPA`, `SysMenuRepositoryJPA`, `SysRoleMenuRepositoryJPA`, `UserOrgMapRepositoryJPA`, `SecurityTypeRepositoryJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextDraftHistoryRepositoryJPA`, `TextDraftRepositoryJPA`, `AttachHistoryRepositoryJPA`, `FileEncryptMapHistoryJPA`, `LogTranstionSignRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AGGR`, `AGG_RECEIVERS`, `ALL_RECEIVERS`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEFCODE`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CHILD_CNT`, `CLOUD_DEVICE_CERT`, `COMMENT_AGG`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATAS`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCS`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_COPY_HISTORY`, `DOCUMENT_HANDOVER`, `DOCUMENT_HANDOVER_DETAIL`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_SEND_VIEW_INFO`, `DOCUMENT_TEMPLATE`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `EXT_APP_API`, `EXT_DOCUMENT`, `EXT_DOCUMENT_ACCESS_LOG`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILEATTACHPAGES`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `GROUP_SIGN`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOAN_THANH_AGG`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `LSTROOTEMP`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NGUOI_HOAN_THANH_RAW`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORG_SYS_MENU`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `RANKED`, `READ_NOTICE_HISTORY`, `RECEIVEDSAVEDOCUMENTOBJECT`, `RECV_1`, `RECV_2`, `RECV_3`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_IN_CV_GROUP`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `ROOTDATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TAG_DICTIONARY`, `TASK`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `TRANSFERRECEIVEDDATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/DocumentAction/AddDocument` | `addDocument` |
| POST | `/DocumentAction/AddDocumentAttachment` | `addDocumentAttachment` |
| POST | `/DocumentAction/EditDocument` | `editDocument` |
| POST | `/DocumentAction/DeleteDocument` | `deleteDocument` |
| POST | `/DocumentAction/processConnectDocumentRecipient` | `processConnectDocumentRecipient` |
| POST | `/DocumentAction/actionSearchDocViewLibrary` | `actionSearchDocViewLibrary` |
| POST | `/DocumentAction/publish` | `publish` |
| POST | `/DocumentAction/publishListDoc` | `publishListDoc` |
| POST | `/DocumentAction/editPublicationInformation` | `editPublicationInformation` |
| POST | `/DocumentAction/editTmpPublicationInformation` | `editTmpPublicationInformation` |
| POST | `/DocumentAction/cancelPublish` | `cancelPublish` |
| POST | `/DocumentAction/countDocument` | `countDocument` |
| POST | `/DocumentAction/search` | `search` |
| POST | `/DocumentAction/searchReceive` | `searchReceive` |
| POST | `/DocumentAction/searchReceiveExport` | `searchReceiveExport` |
| POST | `/DocumentAction/searchReceiveV2` | `searchReceiveV2` |
| POST | `/DocumentAction/searchReceiveWithProcessingStatsByUser` | `searchReceiveWithProcessingStatsByUser` |
| POST | `/DocumentAction/searchReceiveGroupByTextBook` | `searchInGroupByTextBook` |
| POST | `/DocumentAction/searchAll` | `searchAll` |
| POST | `/DocumentAction/getDocumentDetail` | `getDocumentDetail` |
| POST | `/DocumentAction/getDocumentDetailMobile` | `getDocumentDetailMobile` |
| POST | `/DocumentAction/tickProcessedDoc` | `tickProcessedDoc` |
| POST | `/DocumentAction/getListReceiver` | `getListReceiver` |
| POST | `/DocumentAction/getListGroup` | `getListGroup` |
| POST | `/DocumentAction/getListGroupFromDocAndReceive` | `getListGroupFromDocAndReceive` |
| POST | `/DocumentAction/getListGroupMultiTransfer` | `getListGroupMultiTransfer` |
| POST | `/DocumentAction/getDocumentListVof2` | `getDocumentListVof2` |
| POST | `/DocumentAction/sendDocumentToStaff` | `sendDocumentToStaff` |
| POST | `/DocumentAction/sendDocumentToGroup` | `sendDocumentToGroup` |
| POST | `/DocumentAction/sendDocumentToListPersonalGroup` | `sendDocumentToListPersonalGroup` |
| POST | `/DocumentAction/updateDocumentProcessing` | `updateDocumentProcessing` |
| POST | `/DocumentAction/updateStatusDocumentInStaff` | `updateStatusDocumentInStaff` |
| POST | `/DocumentAction/updateStatusDocument` | `updateStatusDocument` |
| POST | `/DocumentAction/getListReceivedStaffInPersonalGroup` | `getListReceivedStaffInPersonalGroup` |
| POST | `/DocumentAction/getListReceivedPersonalGroup` | `getListReceivedPersonalGroup` |
| POST | `/DocumentAction/getListReceivedPersonalGroupMultiTransfer` | `getListReceivedPersonalGroupMultiTransfer` |
| POST | `/DocumentAction/getListReceivedStaffInDepartment` | `getListReceivedStaffInDepartment` |
| POST | `/DocumentAction/addMeetingRequest` | `addMeetingRequest` |
| POST | `/DocumentAction/cancelMeetingRequest` | `cancelMeetingRequest` |
| POST | `/DocumentAction/addDocumentScope` | `addDocumentScope` |
| POST | `/DocumentAction/searchDocumentScope` | `searchDocumentScope` |
| POST | `/DocumentAction/deleteDocumentScope` | `deleteDocumentScope` |
| POST | `/DocumentAction/findDocScopeREFByTextId` | `findDocScopeREFByTextId` |
| POST | `/DocumentAction/getDocScopeLibrary` | `getDocScopeLibrary` |
| POST | `/DocumentAction/tranferTextPromulgateOrNotPromulgate` | `tranferTextPromulgateOrNotPromulgate` |
| POST | `/DocumentAction/checkIsPublished` | `checkIsPublished` |
| POST | `/DocumentAction/getPublishedStatus` | `getPublishedStatus` |
| POST | `/DocumentAction/getAdjacentListByDocumentId` | `getAdjacentListByDocumentId` |
| POST | `/DocumentAction/getDocumentAdjacentList` | `getDocumentAdjacentList` |
| POST | `/DocumentAction/sendDocument` | `sendDocument` |
| POST | `/DocumentAction/sendDocumentMultiTransfer` | `sendDocumentMultiTransfer` |
| POST | `/DocumentAction/sendFinanceTextToStaff` | `sendFinanceTextToStaff` |
| POST | `/DocumentAction/getStatusDocumentInStaff` | `getStatusDocumentInStaff` |
| POST | `/DocumentAction/getStatusDocumentInGroup` | `getStatusDocumentInGroup` |
| POST | `/DocumentAction/exportFinanceText` | `exportFinanceText` |
| POST | `/DocumentAction/saveDocumentType` | `saveDocumentType` |
| POST | `/DocumentAction/getListAllFileDocAttach` | `getListAllFileDocAttach` |
| POST | `/DocumentAction/checkIsOnlyReceiveDoc` | `checkIsOnlyReceiveDoc` |
| POST | `/DocumentAction/getProcessedDetailByUser` | `getProcessedDetailByUser` |
| POST | `/DocumentAction/exportCirculationTree` | `exportCirculationTree` |
| POST | `/DocumentAction/getListFileAttachDocByUserId` | `getListFileAttachDocByUserId` |
| POST | `/DocumentAction/getListStaffReceiveFromDoc` | `getListStaffReceiveFromDoc` |
| POST | `/DocumentAction/SplitDocument` | `splitDocument` |
| POST | `/DocumentAction/getListCommentFromDocument` | `getListCommentFromDocument` |
| POST | `/DocumentAction/GetRegisterNumberIndex` | `getRegisterNumberIndex` |
| POST | `/DocumentAction/ExtendDocument` | `extendDocument` |
| POST | `/DocumentAction/ReportdocumentTransferHistory` | `reportdocumentTransferHistory` |
| POST | `/DocumentAction/UpdateReadingStatus` | `updateReadingStatus` |
| POST | `/DocumentAction/getDocumentAttach` | `getDocumentAttach` |
| POST | `/DocumentAction/checkPermitViewDocument` | `checkPermitViewDocument` |
| POST | `/DocumentAction/getDocumentViewerUserId` | `getDocumentViewerUserId` |
| POST | `/DocumentAction/checkPermissionDoc` | `checkPermissionDoc` |
| POST | `/DocumentAction/getListOfficeOutside` | `getListOfficeOutside` |
| POST | `/DocumentAction/getListCommentLeaderFromDocument` | `getListCommentLeaderFromDocument` |
| POST | `/DocumentAction/getTextIdByDocumentId` | `getTextIdByDocumentId` |
| POST | `/DocumentAction/rollBackDauXacNhan` | `rollBackDauXacNhan` |
| POST | `/DocumentAction/searchFinancial` | `searchFinancial` |
| POST | `/DocumentAction/unfollowDocument` | `unfollowDocument` |
| POST | `/DocumentAction/getDocumentStaffEntity` | `getDocumentStaffEntity` |
| POST | `/DocumentAction/processingTranferBriefDoc` | `processingTranferBriefDoc` |
| POST | `/DocumentAction/getDocumentByIds` | `getDocumentByIds` |
| POST | `/DocumentAction/docReceivedDocument` | `docReceivedDocument` |
| POST | `/DocumentAction/updateDocReceiveMap` | `updateDocReceiveMap` |
| POST | `/DocumentAction/updateDuplicateReceivedDocument` | `updateDuplicateReceivedDocument` |
| POST | `/DocumentAction/searchDocumentOut` | `searchDocumentOut` |
| POST | `/DocumentAction/searchDocumentOutExport` | `searchDocumentOutExport` |
| POST | `/DocumentAction/searchDocumentOutGroupByTextBook` | `searchDocumentOutGroupByTextBook` |
| POST | `/DocumentAction/countDocumentOut` | `countDocumentOut` |
| POST | `/DocumentAction/searchDocumentIn` | `searchDocumentIn` |
| POST | `/DocumentAction/searchDocumentInExport` | `searchDocumentInExport` |
| POST | `/DocumentAction/countDocumentIn` | `countDocumentIn` |
| POST | `/DocumentAction/cancelDocReceiveMap` | `cancelDocReceiveMap` |
| POST | `/DocumentAction/getTextIdByDocId` | `getTextId` |
| POST | `/DocumentAction/updateDocumentMeetingRequestAfterCreateMeeting` | `updateDocumentMeetingRequestAfterCreateMeeting` |
| POST | `/DocumentAction/getDocumentMeetingReq` | `getDocumentMeetingReq` |
| POST | `/DocumentAction/addDocumentMeetingReq` | `addDocumentMeetingReq` |
| POST | `/DocumentAction/updateDocumentMeetingReq` | `updateDocumentMeetingReq` |
| POST | `/DocumentAction/searchDocumentScheduleMeeting` | `searchDocumentScheduleMeeting` |
| POST | `/DocumentAction/searchMeetingRequests` | `searchMeetingRequests` |
| POST | `/DocumentAction/updateMeetingStatus` | `updateMeetingStatus` |
| POST | `/DocumentAction/exportReportDocumentTransferHistory` | `exportReportDocumentTransferHistory` |
| POST | `/DocumentAction/searchMigratedDocument` | `searchMigratedDocument` |
| POST | `/DocumentAction/verifyExternalSignature` | `verifyExternalSignature` |
| POST | `/DocumentAction/verifyExternalSignatureMigratedDoc` | `verifyExternalSignatureMigratedDoc` |
| POST | `/DocumentAction/getListDocumentInStaffEntity` | `getListDocumentInStaffEntity` |
| POST | `/DocumentAction/DeleteDocumentReturned` | `deleteDocumentReturned` |
| POST | `/DocumentAction/updateIsForwardByDocumentId` | `updateIsForwardByDocumentId` |
| POST | `/DocumentAction/updateIsForwardByDocumentIdMultiTransfer` | `updateIsForwardByDocumentIdMultiTransfer` |
| POST | `/DocumentAction/exportDocumentCopy` | `exportDocumentCopy` |
| GET | `/DocumentAction/check-permission-export` | `checkPermissionExport` |
| POST | `/DocumentAction/saveOrUpdateViewDocSendInfo` | `saveOrUpdateViewDocSendInfo` |
| POST | `/DocumentAction/getDocSendInfoByIds` | `getDocSendInfoByIds` |
| POST | `/DocumentAction/searchDocumentOutPublished` | `searchDocumentOutPublished` |
| POST | `/DocumentAction/searchDocumentOutPublishedExport` | `searchDocumentOutPublishedExport` |
| POST | `/DocumentAction/updateReadingStatusV2` | `updateReadingStatusV2` |
| POST | `/DocumentAction/getPublishedDocuments` | `getPublishedDocuments` |
| POST | `/DocumentAction/findDocScopeREFActiveByDocumentId` | `findDocScopeREFActiveByDocumentId` |
| POST | `/DocumentAction/EditDocumentTag` | `editDocumentTag` |
| POST | `/DocumentAction/EditDocumentInGroupTag` | `editDocumentInGroupTag` |
| POST | `/DocumentAction/EditDocumentInStaffTag` | `editDocumentInStaffTag` |
| POST | `/DocumentAction/getInforProposal` | `getInforProposal` |
| POST | `/DocumentAction/checkPermissionRollBack` | `checkPermissionRollBack` |
| POST | `/DocumentAction/getMeetingAssistantByEmployeeIdAndAssiType` | `getMeetingAssistantByEmployeeIdAndAssiType` |
| POST | `/DocumentAction/getProposalDetailDifferent` | `getProposalDetailDifferent` |
| POST | `/DocumentAction/doSubmitForConsideration` | `doSubmitForConsideration` |
| POST | `/DocumentAction/getDocumentOutIssueNumber` | `getDocumentOutIssueNumber` |
| POST | `/DocumentAction/getDocumentForReminder` | `getDocumentForReminder` |
| POST | `/DocumentAction/retriveInforCreator` | `retriveInforCreator` |
| POST | `/DocumentAction/countDocumentByStatus` | `countDocumentByStatus` |
| POST | `/DocumentAction/countDocumentPublishOut` | `countDocumentPublishOut` |
| POST | `/DocumentAction/getListReminderForDetail` | `getListReminderForDetail` |
| POST | `/DocumentAction/getListSignerReminder` | `getListSignerReminder` |
| POST | `/DocumentAction/isDocumentStamped` | `isDocumentStamped` |

</details>

### DocumentHandoverAction (gen1) — base `/DocumentHandoverAction`, 11 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentHandoverAction.java`

- Logic (gen-1 `controler/`): `DocumentHandoverController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `DocumentHandoverDAO`
- Bảng (ước lượng từ SQL/@Table): `AGGR`, `AGG_RECEIVERS`, `ALL_RECEIVERS`, `AREA`, `BRIEF`, `BRIEFCODE`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `COMMENT_AGG`, `CV_GROUP`, `CV_PRIORITY`, `DATAS`, `DOCS`, `DOCUMENT`, `DOCUMENT_HANDOVER`, `DOCUMENT_HANDOVER_DETAIL`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `FILEATTACHPAGES`, `FILES_ATTACHMENT`, `GROUP_MAPPING`, `HOAN_THANH_AGG`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `NGUOI_HOAN_THANH_RAW`, `RANKED`, `RECEIVEDSAVEDOCUMENTOBJECT`, `RECV_1`, `RECV_2`, `RECV_3`, `ROOTDATA`, `SECURITY_TYPE`, `STAFF`, `TEXT`, `TEXT_BOOK`, `TEXT_PROCESS`, `TRANSFERRECEIVEDDATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/DocumentHandoverAction/searchDocumentHandover` | `searchDocumentHandover` |
| POST | `/DocumentHandoverAction/searchDocumentHandoverWeb` | `searchDocumentHandoverWeb` |
| POST | `/DocumentHandoverAction/handOverDocument` | `handOverDocument` |
| POST | `/DocumentHandoverAction/historyDocumentHandover` | `historyDocumentHandover` |
| POST | `/DocumentHandoverAction/exportHistoryDocumentHandover` | `exportHistoryDocumentHandover` |
| POST | `/DocumentHandoverAction/exportReportDocument` | `exportReportDocument` |
| POST | `/DocumentHandoverAction/getDetailDocumentHandover` | `getDetailDocumentHandover` |
| POST | `/DocumentHandoverAction/tableOfIncomingDocumentsBackup` | `exportIndexIncomingDocument` |
| POST | `/DocumentHandoverAction/tableOfIncomingDocuments` | `exportIndexIncomingDocumentV2` |
| POST | `/DocumentHandoverAction/tableOfOutgoingDocumentsBackup` | `exportIndexOutgoingDocument` |
| POST | `/DocumentHandoverAction/tableOfOutgoingDocuments` | `exportIndexOutgoingDocumentV2` |

</details>

### DocumentSignKNTCService (gen1) — base `/`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentSignKNTCService.java`

- Logic (gen-1 `controler/`): `DocumentSignController`, `CommonControler`, `FileControler`, `WOPIController`
- Service: `DocCommentService`, `DocCommentServiceImpl`, `DraftLifecycleEventService`, `DraftLifecycleEventServiceImpl`, `DraftLifecycleMissionClient`, `DraftMissionLinkService`, `DraftMissionLinkServiceImpl`, `ExtShareConfigServiceImpl`, `PdfOcrDocumentService`, `MissionReportResultService`, `MissionReportResultServiceImpl`, `MissionTemplateDetailService`, `MissionTemplateDetailServiceImpl`, `MissionReportResultDetailService`, `MissionReportResultDetailServiceImpl`, `MissionTemplateScopeService`, `MissionTemplateScopeServiceImpl`, `MissionTemplateTableService`, `MissionTemplateTableServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `VhrEmployeeService`, `VhrEmployeeServiceImpl`, `ExtShareConfigService`, `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `SigningFlowUpdateService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AttachDAO`, `AutoDigitalSignDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `ConnectDocumentDAO`, `DocumentDAO`, `DocumentSignDAO`, `TextDAO`, `BriefManagementDAO`, `DownloadAllFileDAO`, `DownloadFileCommentDAO`, `DownloadFileDocumentDAO`, `FilesAttachmentDAO`, `ImageDAO`, `ImageOrgDAO`, `OrgDAO`, `StaffImageSignDAO`, `TaskApprovalDAO`, `TaskDAO`, `TextProcessDAO`, `TextSearchDAO`, `SubmissionFormEditHistoryDAO`, `TextEditHistoryDAO`, `MappingOrgDAO`, `FileAttachmentDAO`, `ReminderHistoryDAO`, `TextCheckSpellDAO`, `TextPartnerDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `HistoryChangeSignDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `TextRepositoryJPA`, `DraftMissionLinkRepository`, `ExtAppEntityRepositoryJPA`, `ExtShareConfigRepositoryJPA`, `ExtShareScopeJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `BriefSubmitAttachFileEntityRepositoryJPA`, `BriefSubmitRequestEntityRepositoryJPA`, `VersionControlRepositoryJPA`, `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `SubmissionFileRepositoryJPA`, `MessageJPA`, `FileEncryptMapJPA`, `MissionReportResultRepositoryJPA`, `MissionProcessRepositoryJPA`, `MissionReportResultDetailRepositoryJPA`, `MissionRepositoryJPA`, `MissionTemplateDetailRepositoryJPA`, `MissionTemplateScopeRepositoryJPA`, `MissionTemplateTableRepositoryJPA`, `MissionTemplateRepositoryJPA`, `MissionTemplateScopeDetailRepositoryJPA`, `ReportDailyHistoryJPA`, `NodeRepositoryJPA`, `NotificationRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `TextProcessRepositoryJPA`, `ExtAppApiEntityRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `PositionRepositoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `SystemParameterRepositoryJPA`, `VhrOrgJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `EXT_APP_API`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FIELD`, `FILE`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_SCOPE_DETAIL`, `MISSION_TEMPLATE_TABLE`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `P12_CERT`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_PROCESS`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_ATTACH_PARTNER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/document/kntc/createdocument` | `addText` |

</details>

### DocController (gen2) — base `/api/doc`, 17 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocController.java`

- Service: `DocService`, `DocServiceImpl`
- DAO (SQL thuần): `DocumentHandoverDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`
- Repository (JPA): `DocumentInStaffRepositoryJPA`, `DocumentRepositoryJPA`, `DocumentTemplateRepositoryJPA`, `TextBookRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AGGR`, `AGG_RECEIVERS`, `ALL_RECEIVERS`, `AREA`, `ATTACH`, `BRIEF`, `BRIEFCODE`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `COMMENT_AGG`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CV_GROUP`, `CV_PRIORITY`, `DATAS`, `DIRECTOR_CONFIG`, `DOCS`, `DOCUMENT`, `DOCUMENT_HANDOVER`, `DOCUMENT_HANDOVER_DETAIL`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_TEMPLATE`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `FILEATTACHPAGES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `GROUP_MAPPING`, `HOAN_THANH_AGG`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `MISSION`, `NGUOI_HOAN_THANH_RAW`, `POSITION`, `RANKED`, `RECEIVEDSAVEDOCUMENTOBJECT`, `RECV_1`, `RECV_2`, `RECV_3`, `ROOTDATA`, `SECURITY_TYPE`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `SYSTIMESTAMP`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TRANSFERRECEIVEDDATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/doc/get-percent-read-doc` | `getPercentReadDoc` |
| POST | `/api/doc/sync-document-in-staff` | `syncDocmentInStaff` |
| POST | `/api/doc/count-sync-document-in-staff` | `countSyncDocmentInStaff` |
| POST | `/api/doc/sync-document` | `syncDocment` |
| POST | `/api/doc/count-sync-document` | `countSyncDocment` |
| GET | `/api/doc/export-report-doc-in` | `exportReportDocIn` |
| GET | `/api/doc/report-doc-in` | `searchReportDocIn` |
| GET | `/api/doc/export-document-out` | `exportDocumentOut` |
| GET | `/api/doc/search-document-out` | `searchDocumentOut` |
| GET | `/api/doc/get-list-user-in-cv-group` | `getListUserInVcGroup` |
| POST | `/api/doc/export-daily-document` | `generatSubmissionFile` |
| POST | `/api/doc/export-daily-vptwd-document` | `exportDailyVPTWDDocument` |
| POST | `/api/doc/export-daily-vptwd-document-to` | `exportDailyVPTWDDocumentTo` |
| POST | `/api/doc/get-url-send-document` | `getUrlSendDocument` |
| POST | `/api/doc/add-document-template` | `addDocumentTemplate` |
| GET | `/api/doc/get-document-template-default` | `getDocumentTemplateDefault` |
| GET | `/api/doc/search-document-template` | `searchDocumentTemplate` |

</details>

### DocumentChatController (gen2) — base `/api/doc-chat`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocumentChatController.java`

- Service: `DocumentChatService`, `DocumentChatServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Repository (JPA): `DocumentChatRepositoryJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `DOCUMENT_CHAT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/doc-chat` | `getAllByDocument` |
| POST | `/api/doc-chat` | `addDocumentChat` |
| POST | `/api/doc-chat/delete` | `deleteDocChat` |
| PUT | `/api/doc-chat` | `updateDocumentChat` |

</details>

### DocumentHistoryLogController (gen2) — base `/api/document-history-log`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocumentHistoryLogController.java`

- Service: `DocumentHistoryLogService`, `DocumentHistoryLogServiceImpl`
- DAO (SQL thuần): `DocumentScopeDAO`, `DocumentSignDAO`
- Repository (JPA): `BriefEntityRepositoryJPA`, `CategoryCommonRepositoryJPA`, `DocumentHistoryLogJPA`, `DocumentTypeRepositoryJPA`, `TextBookRepositoryJPA`, `VhrOrgJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `CATEGORY_COMMON`, `CONNECT_DOCUMENT`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_STAFF`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `MISSION_NORM`, `ORG_CRITERIA_SOURCE`, `POSITION`, `SECURITY_TYPE`, `STAFF`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EDIT_HISTORY`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/document-history-log/get-all-by-document-id/{documentId}` | `getAllByDocument` |
| POST | `/api/document-history-log/search` | `searchWorkGroup` |

</details>

### DocumentKpiController (gen2) — base `/api/document-kpi`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/services/document_kpi/DocumentKpiController.java`

- Service: `DocumentKpiTransferService`, `DocumentKpiTransferServiceImpl`, `DocumentKpiMissionClient`
- DAO (SQL thuần): `DocumentDAO`
- Repository (JPA): `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `FILES_ATTACHMENT`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/document-kpi/catalog-options` | `catalogOptions` |
| POST | `/api/document-kpi/transfer-scope` | `transferScope` |

</details>

### DocumentKpiDraftController (gen2) — base `/api/document-kpi`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/services/document_kpi/DocumentKpiDraftController.java`

- Service: `DraftMissionLinkService`, `DraftMissionLinkServiceImpl`
- Repository (JPA): `DraftMissionLinkRepository`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `SOURCE_MAP`, `TEXT`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/document-kpi/draft-links` | `getDraftLinks` |
| GET | `/api/document-kpi/draft-links/preview` | `previewDraftLinks` |
| POST | `/api/document-kpi/draft-links` | `saveDraftLinks` |
| POST | `/api/document-kpi/draft-links/inherit` | `inheritDraftLinks` |

</details>

### DocumentTypeController (gen2) — base `/api/document-types`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/DocumentTypeController.java`

- Service: `DocumentTypeService`, `DocumentTypeServiceImpl`
- DAO (SQL thuần): `TextBookDAO`
- Repository (JPA): `DocumentRepositoryJPA`, `DocumentTypeOrgRepositoryJPA`, `DocumentTypeRepositoryJPA`, `SysRoleJPA`, `TextRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `DATA_SOURCE`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `FILTERED_DATA`, `HAS_DEFAULT`, `SYSDATE`, `SYS_ROLE`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_PROCESS`, `USER_ROLE`, `VHR_ORG`, `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/document-types/search` | `search` |
| GET | `/api/document-types/document-type/{id}` | `getDocumentType` |
| POST | `/api/document-types/document-type/new-org-doc-type/{id}` | `createOrgDocType` |
| GET | `/api/document-types/get-max-order-number` | `getMaxOrderNumber` |
| GET | `/api/document-types/get-by-organization` | `getDocumentTypeByOrganization` |
| POST | `/api/document-types/create` | `createDocumentType` |
| PUT | `/api/document-types/update/{id}` | `updateDocumentType` |
| PUT | `/api/document-types/lock-unlock/{id}` | `lockDocumentType` |
| POST | `/api/document-types/delete/{id}` | `deleteDocumentType` |
| POST | `/api/document-types/create-doc-type-org` | `createDocTypeOrg` |
| POST | `/api/document-types/granted-doc-type-to-orgs` | `grantedDocTypeToOrgs` |
| POST | `/api/document-types/convert-doc-type-to-common` | `convertDocTypeToCommon` |
| GET | `/api/document-types/get-orgs-by-doc-type-id/{id}` | `getOrganizationIdsByDocTypeId` |

</details>

### PersonalCategoryController (gen2) — base `/api/personal-category`, 6 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/PersonalCategoryController.java`

- Service: `PersonalCategoryService`, `PersonalCategoryServiceImpl`
- Repository (JPA): `PersonalCategoryRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `PERSONAL_CATEGORY`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/personal-category/get-list` | `getListByEmployeeId` |
| GET | `/api/personal-category/get-detail/{categoryId}` | `getById` |
| POST | `/api/personal-category/delete/{categoryId}` | `delete` |
| POST | `/api/personal-category/update/{categoryId}` | `update` |
| POST | `/api/personal-category/create` | `create` |
| POST | `/api/personal-category/check-empty-category` | `checkEmptyCategory` |

</details>

### ShareDocumentController (gen2) — base `/ext-doc`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ShareDocumentController.java`

- Logic (gen-1 `controler/`): `DocumentSearchReceiveController`, `CommonControler`, `SignatureVerificationController`, `TextController`, `EmpCloudCAService`
- Service: `AuthenticationService`, `ShareDocumentFacadeService`, `ShareDocumentFacadeServiceImpl`, `CategoryCacheService`, `CategoryCommonService`, `CategoryCommonServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `DocInService`, `DocInServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `DocLeaderCommentService`, `DocLeaderCommentServiceImpl`, `DocService`, `DocServiceImpl`, `DocumentCopyService`, `DocumentCopyServiceImpl`, `DocumentHistoryLogService`, `DocumentHistoryLogServiceImpl`, `DocumentPermissionCacheService`, `ElasticDocumentService`, `ElasticDocumentServiceImpl`, `TagDictionaryService`, `TagDictionaryServiceImpl`, `ExtShareConfigServiceImpl`, `DraftLifecycleEventService`, `DraftLifecycleEventServiceImpl`, `DraftLifecycleMissionClient`, `ManagerService`, `ManagerServiceImpl`, `OfficePublishedReplacementService`, `OfficePublishedReplacementServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`, `TextDraftService`, `TextDraftServiceImpl`, `TextProcessService`, `TextProcessServiceImpl`, `TextReceiverGroupDetailService`, `TextReceiverGroupDetailServiceImpl`, `ShareDocumentService`, `ShareDocumentServiceImpl`, `ExtShareConfigService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AnswerDocumentDAO`, `AttachDAO`, `BriefManagementDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `ConnectDocumentDAO`, `ConnectVHRDao`, `CvGroupDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`, `DocumentHandoverDAO`, `DocumentCommonService`, `DocumentDAO`, `DocumentScopeDAO`, `DocumentSignDAO`, `DocumentLibraryDAO`, `DocumentPublishedDAO`, `DocumentSearchInService`, `DocumentSendViewInfoDAO`, `FilesAttachmentDAO`, `MeetingDAO`, `SourceMapDAO`, `TextDAO`, `TextSignDAO`, `AutoDigitalSignDAO`, `BriefDetailManagementDAO`, `CloudDeviceCertDAO`, `DocOrgRepublishDAO`, `DocumentPublishedTmpDAO`, `EmpCloudCADAO`, `HistoryChangeSignDAO`, `StaffDAO`, `StaffImageSignDAO`, `MeetingWeekDAO`, `MissionDAO`, `MissionSigningDAO`, `OrgDAO`, `P12CertDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `SysRoleDAO`, `TextBookDAO`, `TextCheckSpellDAO`, `TextCommonDAO`, `TextEditHistoryDAO`, `TextProcessDAO`, `ImageSignDao`, `TextProcessHistoryDAO`, `TextReceiverDAO`, `TextReceiverGroupDAO`
- Repository (JPA): `AttachTemplateRepositoryJPA`, `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `CvPriorityRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `DocumentTemplateRepositoryJPA`, `TextBookRepositoryJPA`, `DocumentCopyHistoryJPA`, `BriefEntityRepositoryJPA`, `DocumentHistoryLogJPA`, `DocumentTypeRepositoryJPA`, `VhrOrgJPA`, `DocumentScopeRefRepository`, `ElasticDocumentPrivateRepositoryJPA`, `ElasticDocumentPublicRepositoryJPA`, `TagDictionaryJpa`, `ExtShareConfigRepositoryJPA`, `ExtShareScopeJPA`, `AttachRepositoryJPA`, `BriefDocumentMapRepositoryJPA`, `TextRepositoryJPA`, `ConfigSmsModuleRepositoryJPA`, `EmpCaDetailRepositoryJPA`, `EmpCaRepositoryJPA`, `FeedbackImageRepositoryJPA`, `FeedbackLogFileRepositoryJPA`, `FeedbackProcessRepositoryJPA`, `FeedbackRepositoryJPA`, `ImageOrgConfigRepositoryJPA`, `ImageOrgRepositoryJPA`, `MenuRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `RolePermissionBaseRepositoryJPA`, `RolePermissionDataRepositoryJPA`, `SmsBlackListRepositoryJPA`, `SysMenuRepositoryJPA`, `SysRoleMenuRepositoryJPA`, `SysRoleRepositoryJPA`, `SystemParameterRepositoryJPA`, `UserOrgMapRepositoryJPA`, `NodeActionRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `SecurityTypeRepositoryJPA`, `StaffImageSignJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextDraftHistoryRepositoryJPA`, `TextDraftRepositoryJPA`, `AttachHistoryRepositoryJPA`, `FileEncryptMapHistoryJPA`, `LogTranstionSignRepositoryJPA`, `NodeRepositoryJPA`, `ExtDocumentAccessLogJPA`, `ExtDocumentJPA`, `ExtShareConfigJPA`
- Bảng (ước lượng từ SQL/@Table): `AGGR`, `AGG_RECEIVERS`, `ALL_RECEIVERS`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEFCODE`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CHILD_CNT`, `CLOUD_DEVICE_CERT`, `COMMENT_AGG`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATAS`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCS`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_COPY_HISTORY`, `DOCUMENT_HANDOVER`, `DOCUMENT_HANDOVER_DETAIL`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_SEND_VIEW_INFO`, `DOCUMENT_TEMPLATE`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `EXT_DOCUMENT`, `EXT_DOCUMENT_ACCESS_LOG`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILEATTACHPAGES`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `GROUP_SIGN`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOAN_THANH_AGG`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `LSTROOTEMP`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NGUOI_HOAN_THANH_RAW`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORG_SYS_MENU`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `RANKED`, `READ_NOTICE_HISTORY`, `RECEIVEDSAVEDOCUMENTOBJECT`, `RECV_1`, `RECV_2`, `RECV_3`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_IN_CV_GROUP`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `ROOTDATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TAG_DICTIONARY`, `TASK`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `TRANSFERRECEIVEDDATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/ext-doc/login-sso-ext-app` | `loginSSOFromExtApp` |
| POST | `/ext-doc/get-document-from-ext-app` | `getShareDocOutIntranet` |
| POST | `/ext-doc/check-exist` | `checkAuthorizedToShareByBuiltGroupIdOfDoc` |
| POST | `/ext-doc/add-ext-doc` | `addExtDocument` |
| POST | `/ext-doc/check-authorized-to-share` | `checkAuthorizedToShareByBuiltGroupIdOfDoc` |
| POST | `/ext-doc/get-document-by-org/out` | `getShareDocumentsOut` |
| POST | `/ext-doc/get-document-by-org/in` | `getShareDocumentsIn` |
| POST | `/ext-doc/get-document-by-sso/in` | `getShareDocumentsIn` |
| POST | `/ext-doc/get-document-by-sso/out` | `getShareDocumentsOut` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `DocumentFacade` | `IDocument` | `DocumentFileService`, `DocumentService` | `DocumentFileJpaDao`, `DocumentJpaDao` | `Document (DOCUMENT)`, `DocumentFile (DOCUMENT_FILE)` |
| `DocumentHandoverHistoryFacade` | `IDocumentHandoverHistory` | — | — | — |
| `DocumentPublicStatusFacade` | `IDocumentPublicStatus` | — | — | — |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `DocumentChatEntity`→`DOCUMENT_CHAT`, `DocumentCopyHistory`→`DOCUMENT_COPY_HISTORY`, `DocumentHistoryLogEntity`→`DOCUMENT_HISTORY_LOG`, `DocumentProcessEntity`→`DOCUMENT_PROCESS`, `DocumentProposalDetailEntity`→`DOCUMENT_PROPOSAL_DETAIL`, `DocumentProposalEntity`→`DOCUMENT_PROPOSAL`, `DocumentScopeEntity`→`DOCUMENT_SCOPE`, `DocumentScopeRefEntity`→`DOCUMENT_SCOPE_REF`, `DocumentTypeEntity`→`DOCUMENT_TYPE`, `DocumentTypeLanguageEntity`→`DOCUMENT_TYPE_LANGUAGE`, `DocumentTypeOrgEntity`→`DOCUMENT_TYPE_ORG`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Document`→`DOCUMENT`, `DocumentArchive`→`DOCUMENT_ARCHIVE`, `DocumentFile`→`DOCUMENT_FILE`, `DocumentHandoverHistory`→`DOCUMENT_HANDOVER_HISTORY`, `DocumentPublicStatus`→`DOCUMENT_PUBLIC_STATUS`

**Tổng hợp bảng chạm tới**: `AGGR`, `AGG_RECEIVERS`, `ALL_RECEIVERS`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEFCODE`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CHILD_CNT`, `CLOUD_DEVICE_CERT`, `CODE_MASTER`, `COMMENT_AGG`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATAS`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCS`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_ARCHIVE`, `DOCUMENT_CHAT`, `DOCUMENT_COPY_HISTORY`, `DOCUMENT_FILE`, `DOCUMENT_HANDOVER`, `DOCUMENT_HANDOVER_DETAIL`, `DOCUMENT_HANDOVER_HISTORY`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLIC_STATUS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_SEND_VIEW_INFO`, `DOCUMENT_TEMPLATE`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_LANGUAGE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EMP_RATING`, `EXT_APP`, `EXT_APP_API`, `EXT_DOCUMENT`, `EXT_DOCUMENT_ACCESS_LOG`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILE`, `FILEATTACHPAGES`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GENERAL_ITEM`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `GROUP_SIGN`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOAN_THANH_AGG`, `HOME_WIDGET`, `IMAGE`, `IMAGES`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INDEX`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `LSTROOTEMP`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_SCOPE_DETAIL`, `MISSION_TEMPLATE_TABLE`, `NGUOI_HOAN_THANH_RAW`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `ORG_LEVEL`, `ORG_SYS_MENU`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `PERSONAL_CATEGORY`, `POSITION`, `RANKED`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `RECEIVEDSAVEDOCUMENTOBJECT`, `RECV_1`, `RECV_2`, `RECV_3`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_IN_CV_GROUP`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `ROOTDATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TAG_DICTIONARY`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_ATTACH_PARTNER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `TRANSFERRECEIVEDDATE`, `USER_ORG_MAP`, `USER_ROLE`, `VERSION_CONTROL`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`, `WORK_PROCESS`
