# Bản đồ hệ thống — Nhiệm vụ (mission) – của cá nhân / đơn vị, không gắn văn bản

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 61 màn hình, 8 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `meeting/popup/permissionViewFile.zul` | `vm.meeting.PermissionViewFileVM` | `MeetingBusiness` | — | BE |
| `mission/agreement/popupExportAgreement.zul` | `vm.mission.ExportAgreementVM` | — | — | — |
| `mission/agreementTask/agreementTask.zul` | `vm.mission.ChartAgreementTaskVM` | `AgreementBusiness`, `MissionBusiness` | — | BE |
| `mission/kpi/kpi.zul` | `vm.mission.KPIIndexVM` | — | `ICriteriaGroup`, `IKPIIndex`, `IProposePoint` | LEGACY |
| `mission/meetingMinutes/meetingMinutes.zul` | `vm.mission.MeetingMinutesVM` | `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `mission/meetingMinutes/meetingMinutes_viewDetail.zul` | `vm.mission.MissionDetailVM` | `AgreementBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness` | `ITask` | BE+LEGACY |
| `mission/meetingMinutes/popupMM.zul` | `vm.mission.PopUpMMVM` | `DocumentBusiness`, `MeetingBusiness` | — | BE |
| `mission/mission/complementMissionInformation.zul` | `vm.mission.ComplementMissionInformationVM` | `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness` | — | BE |
| `mission/mission/mission.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/missionReportSummay.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/mission_add_from_meeting_minutes.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/mission_assign.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/mission_dashboard.zul` | `vm.mission.MissionDashboardVMNew` | `MissionBusiness`, `MissionChartBusiness` | — | BE |
| `mission/mission/mission_extend.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/mission_transfer.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/mission_update_process.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/mission/popUpChooseGroupMission.zul` | `vm.mission.ChooseGroupMissionVm` | `MissionBusiness` | — | BE |
| `mission/mission/popUpListMissionSame.zul` | `vm.mission.MisionViewListSameVm` | `MissionBusiness` | — | BE |
| `mission/missionApprove/missionReportSummay.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionApprove/mission_add_from_meeting_minutes.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionApprove/mission_approve.zul` | `vm.mission.MissionApprovalVM` | `CategoryCommonBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness` | `IMission`, `IProposePoint`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionApprove/mission_assign.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionApprove/mission_extend.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionApprove/mission_transfer.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionApprove/mission_update_process.zul` | `vm.mission.MissionVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `NotificationBusiness`, `SearchSolrBusiness` | `IMission`, `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `mission/missionNorm/missionNorm.zul` | `vm.mission.MissionNormVM` | `MissionBusiness` | — | BE |
| `mission/missionRating/missionRating.zul` | `vm.mission.MissionRatingVM` | `DocumentBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `mission/missionRating/missionRatingApproved.zul` | `vm.mission.MissionRatingVM` | `DocumentBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `mission/missionRating/missionRatingApproved_viewDetail.zul` | `vm.mission.MissionRatingVM` | `DocumentBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `mission/missionRating/missionRating_viewDetail.zul` | `vm.mission.MissionRatingVM` | `DocumentBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `mission/proposePoint/approvedPoint.zul` | `vm.mission.ProposePointVM` | — | `IProposePoint`, `ISysOrganization` | LEGACY |
| `mission/proposePoint/proposePoint.zul` | `vm.mission.ProposePointVM` | — | `IProposePoint`, `ISysOrganization` | LEGACY |
| `mission/report/missionReportViewMeeting.zul` | `vm.mission.MissionReportViewMeetingVM` | — | — | — |
| `mission/report/missionReport_viewTask.zul` | `vm.mission.MissionReportViewTaskVM` | `MissionBusiness` | — | BE |
| `mission/report/mission_report.zul` | `vm.mission.MissionReportVM` | `MeetingBusiness`, `MissionBusiness` | `IMeeting` | BE+LEGACY |
| `mission/report/report_period.zul` | `vm.mission.ReportPeriodIndividualVM` | `OrientationBusiness`, `ReportPeriodApproveBusiness`, `ReportPeriodBusiness`, `WorkGroupBusiness`, `WorkGroupInfoBusiness` | `ISysUser` | BE+LEGACY |
| `mission/report/report_period_detail.zul` | `widget.ReportPeriodIndividualDetailVM` | `ReportPeriodBusiness`, `WorkGroupBusiness`, `WorkGroupInfoBusiness` | — | BE |
| `mission/report/report_period_rating_detail.zul` | `widget.ReportPeriodIndividualDetailVM` | `ReportPeriodBusiness`, `WorkGroupBusiness`, `WorkGroupInfoBusiness` | — | BE |
| `mission/reportPeriodConfig/reportPeriodConfig.zul` | `vm.mission.ReportPeriodConfigVM` | `ReportPeriodConfigBusiness`, `SearchSolrBusiness`, `SysRoleBusiness` | — | BE |
| `mission/resovleIssue/resovle_issue.zul` | `vm.mission.ResovleIssueVM` | `ResovleIssueBusiness` | `IProposePoint`, `IResovleIssue`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `mission/resovleIssue/resovle_issue_difficult.zul` | `vm.mission.ResovleIssueDetailVM` | `ResovleIssueBusiness` | — | BE |
| `mission/widgets/popupMissionProcessDetail.zul` | `vm.mission.PopupMissionProcessDetail` | `DocumentBusiness` | — | BE |
| `mission/workGroup/workGroup.zul` | `vm.mission.WorkGroupVM` | `CategoryCommonBusiness`, `SysRoleBusiness`, `WorkGroupBusiness`, `WorkGroupInfoBusiness` | `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `mission/workGroup/work_group_detail.zul` | `widget.WorkLookupVM` | — | — | — |
| `mission/workGroupExport/workGroupExport.zul` | `vm.mission.ReportPeriodIndividualVM` | `OrientationBusiness`, `ReportPeriodApproveBusiness`, `ReportPeriodBusiness`, `WorkGroupBusiness`, `WorkGroupInfoBusiness` | `ISysUser` | BE+LEGACY |
| `mission/workGroupItem/workGroupItem.zul` | `vm.mission.WorkGroupItemVM` | `CategoryCommonBusiness`, `WorkGroupBusiness`, `WorkGroupInfoBusiness` | — | BE |
| `mission/workItemApprove/work_item_approve.zul` | `vm.mission.WorkItemApproveVM` | `ReportPeriodApproveBusiness`, `SysRoleBusiness` | `ISysOrganization` | BE+LEGACY |
| `mission/workItemApprove/work_item_approve_detail.zul` | `widget.WorkItemApproveDetailVM` | `ReportPeriodApproveBusiness`, `ReportPeriodBusiness` | — | BE |
| `widgets/missionLookup.zul` | `widget.MissionLookupVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness` | `IMission`, `ITask` | BE+LEGACY |
| `widgets/popupAddMission.zul` | `vm.mission.PopupAddMissionVM` | `MeetingBusiness`, `MissionBusiness` | — | BE |
| `widgets/popupCreateMission.zul` | `widget.PopupCreateMissionVM` | — | — | — |
| `widgets/popupMissionDetail.zul` | `vm.mission.MissionDetailVM` | `AgreementBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness` | `ITask` | BE+LEGACY |
| `widgets/proposePointMissionLookup.zul` | `widget.MissionLookupVM` | `AgreementBusiness`, `CategoryCommonBusiness`, `CommentBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness` | `IMission`, `ITask` | BE+LEGACY |
| `vps/sysRole/rolePermission.zul` | `vps.vm.RolePermissionVM` | — | `ISysRole` | LEGACY |
| `widgets/mission/sourceLookupAgreement.zul` | `widget.SourceLookupAgreementVM` | `AgreementBusiness` | — | BE |
| `widgets/mission/sourceLookupAgreementInfo.zul` | `widget.SourceLookupAgreementViewVM` | `AgreementBusiness` | — | BE |
| `widgets/mission/sourceLookupAgreementTaskDetail.zul` | `widget.SourceLookupAgreementTaskInfoVM` | `AgreementBusiness`, `DocumentBusiness` | — | BE |
| `widgets/mission/sourceLookupAgreementTaskInfo.zul` | `widget.SourceLookupAgreementTaskInfoVM` | `AgreementBusiness`, `DocumentBusiness` | — | BE |
| `widgets/permissionLookup.zul` | `widget.PermissionLookupVM` | — | — | — |
| `widgets/workGroupItemAddLookup.zul` | `widget.PopupAddWorkGroupItemVM` | `CategoryCommonBusiness` | — | BE |
| `widgets/workGroupLookup.zul` | `widget.PopupSelectWorkGroupVM` | `CategoryCommonBusiness`, `WorkGroupBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.mission.MissionAddFromDocVM` | `AgreementBusiness`, `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness` | `IMission`, `IProposePoint`, `ISysOrganization`, `IVps` | BE+LEGACY |
| `vm.mission.MissionDashboardVM` | — | — | — |
| `vm.mission.MissionExtendVM` | — | — | — |
| `vm.mission.MissionReportSummary` | — | — | — |
| `vm.mission.WorkGroupRowRenderer` | — | — | — |
| `vm.workGroupTree.IWorkGroupTreeItemEvent` | — | — | — |
| `vm.workGroupTree.WorkGroupTreeItemRender` | — | — | — |
| `vm.workGroupTree.WorkGroupTreeModel` | — | — | — |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### AgreementBusiness

`web-spring/src/main/java/com/voffice/service/business/AgreementBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `agreementAction.exportAgreement` | `/agreementAction/exportAgreement` | `AgreementAction.exportAgreement` | gen1 |
| `agreementAction.findAgreementTaskById` | `/agreementAction/findAgreementTaskById` | `AgreementAction.findAgreementTaskById` | gen1 |
| `agreementAction.findTaskByMissionId` | `/agreementAction/findTaskByMissionId` | `AgreementAction.findTaskByMissionId` | gen1 |
| `agreementAction.getDetailAgreement` | `/agreementAction/getDetailAgreement` | `AgreementAction.getDetailAgreement` | gen1 |
| `agreementAction.getDetailAgreementById` | `/agreementAction/getDetailAgreementById` | `AgreementAction.getDetailAgreementById` | gen1 |
| `agreementAction.getDetailAgreementTask` | `/agreementAction/getDetailAgreementTask` | `AgreementAction.getDetailAgreementTask` | gen1 |
| `agreementAction.getListCharts` | `/agreementAction/getListCharts` | `AgreementAction.getListCharts` | gen1 |
| `agreementAction.getListCustomers` | `/agreementAction/getListCustomers` | `AgreementAction.getListCustomers` | gen1 |
| `agreementAction.listAgreementStatus` | `/agreementAction/listAgreementStatus` | `AgreementAction.listAgreementStatus` | gen1 |
| `agreementAction.listGroupTypes` | `/agreementAction/listGroupTypes` | `AgreementAction.listGroupTypes` | gen1 |
| `agreementAction.listTaskPriority` | `/agreementAction/listTaskPriority` | `AgreementAction.listTaskPriority` | gen1 |

### MissionBusiness

`web-spring/src/main/java/com/voffice/service/business/MissionBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `DocumentService.getListFields` | `/DocumentService/getListFields` | `DocumentSignService.getListFields` | gen1 |
| `Meeting.forwardMission` | `/Meeting/forwardMission` | `MettingResource.forwardMission` | gen1 |
| `Meeting.getListOrgPerformInAdvanceSearch` | `/Meeting/getListOrgPerformInAdvanceSearch` | `MettingResource.getListOrgPerformInAdvanceSearch` | gen1 |
| `Meeting.getListOrganizationExecute` | `/Meeting/getListOrganizationExecute` | `MettingResource.getListOrganizationExecute` | gen1 |
| `Meeting.getListOrganizationsAssign` | `/Meeting/getListOrganizationsAssign` | `MettingResource.getListOrganizationsAssign` | gen1 |
| `MissionReport.findMissionNorm` | `/MissionReport/findMissionNorm` | `MissionReportAction.findMissionNorm` | gen1 |
| `MissionReport.getListEmployee` | `/MissionReport/getListEmployee` | `MissionReportAction.getListEmployee` | gen1 |
| `MissionReport.getListMissionOfGroup` | `/MissionReport/getListMissionOfGroup` | `MissionReportAction.getListMissionOfGroup` | gen1 |
| `MissionReport.getListMissionReport` | `/MissionReport/getListMissionReport` | `MissionReportAction.getListMissionReport` | gen1 |
| `MissionReport.getListOrgMapOfUser` | `/MissionReport/getListOrgMapOfUser` | `MissionReportAction.getListOrgMapOfUser` | gen1 |
| `MissionReport.getListQuarterMissionOfGroup` | `/MissionReport/getListQuarterMissionOfGroup` | `MissionReportAction.getListQuarterMissionOfGroup` | gen1 |
| `MissionReport.getListQuarterMissionReport` | `/MissionReport/getListQuarterMissionReport` | `MissionReportAction.getListQuarterMissionReport` | gen1 |
| `MissionReport.insertMissionNorm` | `/MissionReport/insertMissionNorm` | `MissionReportAction.insertMissionNorm` | gen1 |
| `MissionReport.scoreReport` | `/MissionReport/scoreReport` | `MissionReportAction.scoreReport` | gen1 |
| `MissionReport.scoreReportDetail` | `/MissionReport/scoreReportDetail` | `MissionReportAction.scoreReportDetail` | gen1 |
| `MissionReport.updateMissionNorm` | `/MissionReport/updateMissionNorm` | `MissionReportAction.updateMissionNorm` | gen1 |
| `MissionReport.viewMissionReport` | `/MissionReport/viewMissionReport` | `MissionReportAction.viewMissionReport` | gen1 |
| `MissionReport.viewQuarterMissionReport` | `/MissionReport/viewQuarterMissionReport` | `MissionReportAction.viewQuarterMissionReport` | gen1 |
| `api.mission-template` | `/api/mission-template` | `MissionTemplateController.updateMissionTemplate` | gen2 |
| `api.mission-template.get-list-org-report` | `/api/mission-template/get-list-org-report` | `MissionTemplateController.getListOrgReport` | gen2 |
| `api.mission-template.get-list-receiver-doc` | `/api/mission-template/get-list-receiver-doc` | `MissionTemplateController.getListOrgReport` | gen2 |
| `api.mission-template.lock-report-result` | `/api/mission-template/lock-report-result` | `MissionTemplateController.lockReportResult` | gen2 |
| `api.report-result` | `/api/report-result` | `MissionReportResultController.getReportResult` | gen2 |
| `api.report-result.assign-specialist` | `/api/report-result/assign-specialist` | `MissionReportResultController.assignSpecialist` | gen2 |
| `api.report-result.export` | `/api/report-result/export` | `MissionReportResultController.exportReportResult` | gen2 |
| `api.report-result.get-by-org-id-and-mission-template-id` | `/api/report-result/get-by-org-id-and-mission-template-id` | `MissionReportResultController.getByOrgIdAndMissionTemplateId` | gen2 |
| `api.report-result.get-list-org-perform-specialist` | `/api/report-result/get-list-org-perform-specialist` | `MissionReportResultController.getListOrgPerformSpecialist` | gen2 |
| `api.report-result.report-daily.create-or-update` | `/api/report-result/report-daily/create-or-update` | `MissionReportResultController.createOrUpdateReportDaily` | gen2 |
| `api.report-result.report-daily.get-detail` | `/api/report-result/report-daily/get-detail` | `MissionReportResultController.getReportDailyHistory` | gen2 |
| `api.report-result.report-history.get-detail` | `/api/report-result/report-history/get-detail` | `MissionReportResultController.getListReportHistory` | gen2 |
| `api.report-result.send-confidential-report` | `/api/report-result/send-confidential-report` | `MissionReportResultController.senConfidentialReport` | gen2 |
| `api.report-result.unassign-specialist` | `/api/report-result/unassign-specialist` | `MissionReportResultController.unassignSpecialist` | gen2 |
| `missionAction.CreateTextFromMissionList` | `/missionAction/CreateTextFromMissionList` | `MissionAction.createTextFromMissionList` | gen1 |
| `missionAction.SaveMissionOrder` | `/missionAction/SaveMissionOrder` | `MissionAction.saveMissionOrder` | gen1 |
| `missionAction.addInformationMission` | `/missionAction/addInformationMission` | `MissionAction.addInformationMission` | gen1 |
| `missionAction.addMission` | `/missionAction/addMission` | `MissionAction.addMission` | gen1 |
| `missionAction.approveOrRejectProcess` | `/missionAction/approveOrRejectProcess` | `MissionAction.approveOrRejectProcess` | gen1 |
| `missionAction.approvedMissionByCommander` | `/missionAction/approvedMissionByCommander` | `MissionAction.approvedMissionByCommander` | gen1 |
| `missionAction.checkExtendable` | `/missionAction/checkExtendable` | `MissionAction.checkExtendable` | gen1 |
| `missionAction.closeMission` | `/missionAction/closeMission` | `MissionAction.closeMission` | gen1 |
| `missionAction.deleteMission` | `/missionAction/deleteMission` | `MissionAction.deleteMission` | gen1 |
| `missionAction.editMissionNameCompact` | `/missionAction/editMissionNameCompact` | `MissionAction.editMissionNameCompact` | gen1 |
| `missionAction.editPerformIdMission` | `/missionAction/editPerformIdMission` | `MissionAction.editPerformIdMission` | gen1 |
| `missionAction.findMissionByCondition` | `/missionAction/findMissionByCondition` | `MissionAction.findMissionByCondition` | gen1 |
| `missionAction.getCountMissionNeedCompleted` | `/missionAction/getCountMissionNeedCompleted` | `MissionAction.getCountMissionNeedCompleted` | gen1 |
| `missionAction.getFieldIdFromOrgPerform` | `/missionAction/getFieldIdFromOrgPerform` | `MissionAction.getFieldIdFromOrgPerform` | gen1 |
| `missionAction.getLastMissionProcessOfSubMissions` | `/missionAction/getLastMissionProcessOfSubMissions` | `MissionAction.getLastMissionProcessOfSubMissions` | gen1 |
| `missionAction.getListAddionalMission` | `/missionAction/getListAddionalMission` | `MissionAction.getListAddionalMission` | gen1 |
| `missionAction.getListMissionStatus` | `/missionAction/getListMissionStatus` | `MissionAction.getListMissionStatus` | gen1 |
| `missionAction.getListTransferredMission` | `/missionAction/getListTransferredMission` | `MissionAction.getListTransferredMission` | gen1 |
| `missionAction.getMissionCommanderList` | `/missionAction/getMissionCommanderList` | `MissionAction.getMissionCommanderList` | gen1 |
| `missionAction.getMissionDetail` | `/missionAction/getMissionDetail` | `MissionAction.getMissionDetail` | gen1 |
| `missionAction.getMissionProcessHistory` | `/missionAction/getMissionProcessHistory` | `MissionAction.getMissionProcessHistory` | gen1 |
| `missionAction.getSubMissionNewestToFill` | `/missionAction/getSubMissionNewestToFill` | `MissionAction.getSubMissionNewestToFill` | gen1 |
| `missionAction.getViewSourceMap` | `/missionAction/getViewSourceMap` | `MissionAction.getViewSourceMap` | gen1 |
| `missionAction.rejectMissionByCommander` | `/missionAction/rejectMissionByCommander` | `MissionAction.rejectMissionByCommander` | gen1 |
| `missionAction.updateContentOrResultOfCombinationOrg` | `/missionAction/updateContentOrResultOfCombinationOrg` | `MissionAction.updateContentOrResultOfCombinationOrg` | gen1 |
| `missionAction.updateMission` | `/missionAction/updateMission` | `MissionAction.updateMission` | gen1 |
| `missionAction.updateProcess` | `/missionAction/updateProcess` | `MissionAction.updateProcess` | gen1 |
| `taskAction.getListRatioConfigByOrg` | `/taskAction/getListRatioConfigByOrg` | `TaskAction.getListRatioConfigByOrg` | gen1 |

### MissionChartBusiness

`web-spring/src/main/java/com/voffice/service/business/MissionChartBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Meeting.getListOrgPerformInAdvanceSearch` | `/Meeting/getListOrgPerformInAdvanceSearch` | `MettingResource.getListOrgPerformInAdvanceSearch` | gen1 |
| `api.mission_dashboard.get-assign-mission-charts` | `/api/mission_dashboard/get-assign-mission-charts` | `MissionDashboardController.getAssignMissionCharts` | gen2 |
| `api.mission_dashboard.get-perform-mission-charts` | `/api/mission_dashboard/get-perform-mission-charts` | `MissionDashboardController.getPerformMissionCharts` | gen2 |

### WorkGroupBusiness

`web-spring/src/main/java/com/voffice/service/business/WorkGroupBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.work-group-action.unBlock` | ❓ không tìm thấy endpoint | | |
| `api.work-group.block` | `/api/work-group/block` | `WorkGroupController.block` | gen2 |
| `api.work-group.check-valid-org-apply` | `/api/work-group/check-valid-org-apply` | `WorkGroupController.checkValidToChangeOrgApply` | gen2 |
| `api.work-group.create-or-update-work-group` | `/api/work-group/create-or-update-work-group` | `WorkGroupController.createOrUpdateWorkGroup` | gen2 |
| `api.work-group.delete` | `/api/work-group/delete` | `WorkGroupController.deleteWorkGroup` | gen2 |
| `api.work-group.get-all-work-group` | `/api/work-group/get-all-work-group` | `WorkGroupController.getAllWorkGroup` | gen2 |
| `api.work-group.get-detail-work-group` | `/api/work-group/get-detail-work-group` | `WorkGroupController.getDetailWorkGroup` | gen2 |
| `api.work-group.get-work-group-to-recursive` | `/api/work-group/get-work-group-to-recursive` | `WorkGroupController.getListWorkGroupToRecursive` | gen2 |
| `api.work-group.search-work-group` | `/api/work-group/search-work-group` | `WorkGroupController.searchWorkGroup` | gen2 |

### WorkGroupHistoryBusiness

`web-spring/src/main/java/com/voffice/service/business/WorkGroupHistoryBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.work-group-item-history.save` | `/api/work-group-item-history/save` | `WorkGroupItemHistoryController.save` | gen2 |

### WorkGroupInfoBusiness

`web-spring/src/main/java/com/voffice/service/business/WorkGroupInfoBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.work-group-item.create-or-update-work-group-item` | `/api/work-group-item/create-or-update-work-group-item` | `WorkGroupItemController.createOrUpdateWorkGroupItem` | gen2 |
| `api.work-group-item.delete` | `/api/work-group-item/delete` | `WorkGroupItemController.deleteWorkGroup` | gen2 |
| `api.work-group-item.get-detail` | `/api/work-group-item/get-detail` | `WorkGroupItemController.getDetailWorkGroupItem` | gen2 |
| `api.work-group-item.get-details` | `/api/work-group-item/get-details` | `WorkGroupItemController.getDetailWorkGroupItem` | gen2 |
| `api.work-group-item.get-list-work-group-ids` | `/api/work-group-item/get-list-work-group-ids` | `WorkGroupItemController.getWorkGroupIds` | gen2 |
| `api.work-group-item.get-work-group-items-for-next-week` | `/api/work-group-item/get-work-group-items-for-next-week` | `WorkGroupItemController.getWorkGroupItemsForNextWeek` | gen2 |
| `api.work-group-item.get-work-group-items-from-period` | `/api/work-group-item/get-work-group-items-from-period` | `WorkGroupItemController.getDetailWorkGroupItem` | gen2 |
| `api.work-group-item.search-work-group-item` | `/api/work-group-item/search-work-group-item` | `WorkGroupItemController.searchWorkGroup` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### AgreementAction (gen1) — base `/agreementAction`, 21 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/AgreementAction.java`

- Logic (gen-1 `controler/`): `AgreeChartController`, `LogActionControler`
- DAO (SQL thuần): `AgreementDAO`, `CommonDataBaseDaoVO2`, `LogActionDao`, `MissionDAO`, `UserDAO`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `EXT_APP`, `FIELD`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `GROUP_MAPPING`, `MAPPING_RESOVLE`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SOURCE_MAP`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/agreementAction/getListCharts` | `getListCharts` |
| POST | `/agreementAction/chartAgreementGroupByGroupType` | `chartAgreementGroupByGroupType` |
| POST | `/agreementAction/chartSaleGroupByGroupType` | `chartSaleGroupByGroupType` |
| POST | `/agreementAction/chartRevenueGroupByGroupType` | `chartRevenueGroupByGroupType` |
| POST | `/agreementAction/chartMissionsAndFilterType` | `chartMissionsAndFilterType` |
| POST | `/agreementAction/chartProjectsAndFilterType` | `chartProjectsAndFilterType` |
| POST | `/agreementAction/chartRevenueByGroup` | `chartRevenueByGroup` |
| POST | `/agreementAction/listGroupTypes` | `listGroupTypes` |
| POST | `/agreementAction/listTaskStatus` | `listTaskStatus` |
| POST | `/agreementAction/listTaskType` | `listTaskType` |
| POST | `/agreementAction/listTaskPriority` | `listTaskPriority` |
| POST | `/agreementAction/listAgreementStatus` | `listAgreementStatus` |
| POST | `/agreementAction/getDetailAgreement` | `getDetailAgreement` |
| POST | `/agreementAction/exportAgreement` | `exportAgreement` |
| POST | `/agreementAction/getDetailAgreementTask` | `getDetailAgreementTask` |
| POST | `/agreementAction/getListCustomers` | `getListCustomers` |
| POST | `/agreementAction/findTaskByMissionId` | `findTaskByMissionId` |
| POST | `/agreementAction/getDetailAgreementById` | `getDetailAgreementById` |
| POST | `/agreementAction/findAgreementTaskById` | `findAgreementTaskById` |
| GET | `/agreementAction/vofficeMissions` | `vofficeMissions` |
| GET | `/agreementAction/vofficeMissionProcesses` | `getProcessMission` |

</details>

### MissionAction (gen1) — base `/missionAction`, 55 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MissionAction.java`

- Logic (gen-1 `controler/`): `MeetingController`, `CommonControler`, `LogActionControler`, `MissionControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`, `EcabinetService`, `EcabinetServiceImpl`, `CategoryCommonService`, `CategoryCommonServiceImpl`, `CategoryCacheService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AgreementDAO`, `CiscoMeetingDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `DocumentSignDAO`, `LogActionDao`, `MeetingDAO`, `MeetingMinutesDAO`, `MeetingNativeDAO`, `MeetingWeekDAO`, `MissionDAO`, `ObjectTransferViaAxisDAO`, `OrgDAO`, `RequestDAO`, `SourceMapDAO`, `StaffDAO`, `TextDAO`, `MissionChartDAO`, `TaskCommonDAO`, `UserOrgMapDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`, `MissionRepositoryJPA`, `NotificationRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/missionAction/getListMissionGroup` | `getListMissionGroup` |
| POST | `/missionAction/getListMission` | `getListMission` |
| POST | `/missionAction/getMissionDetail` | `getMissionDetail` |
| POST | `/missionAction/getListFileAttachment` | `getListFileAttachment` |
| POST | `/missionAction/getMissionProcessHistory` | `getMissionProcessHistory` |
| POST | `/missionAction/getLastMissionProcessOfSubMissions` | `getLastMissionProcessOfSubMissions` |
| POST | `/missionAction/getListCombinationOrg` | `getListCombinationOrg` |
| POST | `/missionAction/getListTransferredMission` | `getListTransferredMission` |
| POST | `/missionAction/updateMission` | `updateMission` |
| POST | `/missionAction/getCounMission` | `getCounMission` |
| POST | `/missionAction/getInputForCountMission` | `getInputForCountMission` |
| POST | `/missionAction/deleteMission` | `deleteMission` |
| POST | `/missionAction/updateProcess` | `updateProcess` |
| POST | `/missionAction/approveOrRejectProcess` | `approveOrRejectProcess` |
| POST | `/missionAction/updateContentOrResultOfCombinationOrg` | `updateContentOrResultOfCombinationOrg` |
| POST | `/missionAction/getMissionCommanderList` | `getMissionCommanderList` |
| POST | `/missionAction/approvedMissionByCommander` | `approvedMissionByCommander` |
| POST | `/missionAction/rejectMissionByCommander` | `rejectMissionByCommander` |
| POST | `/missionAction/getListOrg` | `getListOrg` |
| POST | `/missionAction/getMissionResovleIssueList` | `getMissionResovleIssueList` |
| POST | `/missionAction/doUpdatePercentService` | `doUpdatePercentService` |
| POST | `/missionAction/CountMission` | `countMission` |
| POST | `/missionAction/getListMissionLog` | `getListMissionLog` |
| POST | `/missionAction/getCountByOrgPerformSpecialized` | `getCountByOrgPerformSpecialized` |
| POST | `/missionAction/getListOrgSpecialized` | `getListOrgSpecialized` |
| POST | `/missionAction/configSpecializedManagement` | `configSpecializedManagement` |
| POST | `/missionAction/getConfigMissionByUser` | `getConfigMissionByUser` |
| POST | `/missionAction/getCountMissionSpecialized` | `getCountMissionSpecialized` |
| POST | `/missionAction/getListMissionUpcomingDeadline` | `getListMissionUpcomingDeadline` |
| POST | `/missionAction/addInformationMission` | `addInformationMission` |
| POST | `/missionAction/closeMission` | `closeMission` |
| POST | `/missionAction/getListAddionalMission` | `getListAddionalMission` |
| POST | `/missionAction/findMissionByCondition` | `findMissionByCondition` |
| POST | `/missionAction/getSubMissionNewestToFill` | `getSubMissionNewestToFill` |
| POST | `/missionAction/editPerformIdMission` | `editPerformIdMission` |
| POST | `/missionAction/getListSourceMap` | `getListSourceMap` |
| POST | `/missionAction/getListMissionStatus` | `getListMissionStatus` |
| POST | `/missionAction/CreateTextFromMissionList` | `createTextFromMissionList` |
| POST | `/missionAction/ReportMissionProcess` | `reportMissionProcess` |
| POST | `/missionAction/SaveMissionOrder` | `saveMissionOrder` |
| GET | `/missionAction/getListGeneralManager` | `getListGeneralManager` |
| GET | `/missionAction/GetMissionWarning/{assignId}` | `getMissionWarning` |
| GET | `/missionAction/GetMissionWarningByOrg/{orgId}/{type}` | `getMissionWarningByOrg` |
| GET | `/missionAction/getListPerformingOrg` | `getListPerformingOrg` |
| POST | `/missionAction/checkExtendable` | `checkExtendable` |
| POST | `/missionAction/getCountMissionNeedCompleted` | `getCountMissionNeedCompleted` |
| POST | `/missionAction/findDueDateMission` | `findDueDateMission` |
| POST | `/missionAction/getFieldIdFromOrgPerform` | `getFieldIdFromOrgPerform` |
| POST | `/missionAction/getViewSourceMap` | `getViewSourceMap` |
| POST | `/missionAction/addMission` | `addMission` |
| GET | `/missionAction/getListVTSMissions/{apiType}` | `getListVTSMissions` |
| POST | `/missionAction/editMissionNameCompact` | `editMissionNameCompact` |
| POST | `/missionAction/getMissionCharts` | `getMissionCharts` |
| POST | `/missionAction/chartMissionFilterType` | `chartProjectsAndFilterType` |
| POST | `/missionAction/getMissionChartDetail` | `getMissionChartDetail` |

</details>

### MissionReportAction (gen1) — base `/MissionReport`, 23 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MissionReportAction.java`

- Logic (gen-1 `controler/`): `MissionReportController`, `UserControler`, `EmpCloudCAService`, `LogActionControler`
- Service: `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `MissionDashboardReportDAO`, `MissionReportDAO`, `CloudDeviceCertDAO`, `ConfigParameterDAO`, `DocumentDAO`, `EmpCloudCADAO`, `SystemParameterDAO`, `FavouriteDAO`, `ImageDAO`, `LogActionDao`, `MeetingAssistantDAO`, `MissionDAO`, `OrgDAO`, `StaffDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `UserOrgMapDAO`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGE_ORG`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `ORG_COMBINATION_MAP`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/MissionReport/getListEmployee` | `getListEmployee` |
| POST | `/MissionReport/getListCreatBy` | `getListCreatBy` |
| POST | `/MissionReport/getListGroup` | `getListGroup` |
| POST | `/MissionReport/getListGroupPerform` | `getListPerformGroup` |
| POST | `/MissionReport/getListMissionOfGroup` | `getListMissionOfGroup` |
| POST | `/MissionReport/getListQuarterMissionOfGroup` | `getListQuarterMissionOfGroup` |
| POST | `/MissionReport/viewMissionReport` | `viewMissionReport` |
| POST | `/MissionReport/viewQuarterMissionReport` | `viewQuarterMissionReport` |
| POST | `/MissionReport/getListMissionReport` | `getListMissionReport` |
| POST | `/MissionReport/getListQuarterMissionReport` | `getListQuarterMissionReport` |
| POST | `/MissionReport/findMissionNorm` | `findMissionNorm` |
| POST | `/MissionReport/insertMissionNorm` | `insertMissionNorm` |
| POST | `/MissionReport/updateMissionNorm` | `updateMissionNorm` |
| POST | `/MissionReport/viewDetailDashboardReport` | `viewDetailDashboardReport` |
| POST | `/MissionReport/dashboardReport` | `dashboardReport` |
| POST | `/MissionReport/getListOrg` | `getListOrg` |
| POST | `/MissionReport/getMissionReportDashboard` | `getMissionReportDashboard` |
| POST | `/MissionReport/getReportTextOverDate` | `getReportTextOverDate` |
| POST | `/MissionReport/getReportTextReject` | `getReportTextReject` |
| POST | `/MissionReport/scoreReport` | `scoreReport` |
| POST | `/MissionReport/scoreReportDetail` | `scoreReportDetail` |
| POST | `/MissionReport/getListOrgMapOfUser` | `getListOrgMapOfUser` |
| POST | `/MissionReport/getReportTextProcess` | `getReportTextProcess` |

</details>

### MissionController (gen2) — base `/api/mission`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MissionController.java`

- Service: `MissionService`, `MissionServiceImpl`
- DAO (SQL thuần): `MissionDashboardReportDAO`
- Repository (JPA): `MeetingMemberRepositoryJPA`, `MissionRepositoryJPA`, `UserOrgMapRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `MEETING_MEMBER`, `MISSION`, `MISSION_PROCESS`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/mission/{missionId}` | `deleteMission` |
| POST | `/api/mission/get-assign-mission-charts` | `getAssignMissionCharts` |
| POST | `/api/mission/get-perform-mission-charts` | `getPerformMissionCharts` |
| POST | `/api/mission/count-assign-mission` | `countAssignMission` |
| POST | `/api/mission/count-perform-mission` | `countPerformMission` |
| POST | `/api/mission/get-list-org-perform` | `getListOrgPerform` |
| POST | `/api/mission/search-mission` | `searchMission` |
| POST | `/api/mission/sync-mission` | `syncMission` |
| POST | `/api/mission/count-sync-mission` | `countSyncMission` |

</details>

### MissionDashboardController (gen2) — base `/api/mission_dashboard`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MissionDashboardController.java`

- Service: `MissionDashboardService`, `MissionDashboardServiceImpl`
- DAO (SQL thuần): `MissionDashboardChartDAO`
- Repository (JPA): `MeetingMemberRepositoryJPA`, `MissionRepositoryJPA`, `UserOrgMapRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `MEETING_MEMBER`, `MISSION`, `MISSION_PROCESS`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/mission_dashboard/{missionId}` | `deleteMission` |
| POST | `/api/mission_dashboard/get-assign-mission-charts` | `getAssignMissionCharts` |
| POST | `/api/mission_dashboard/get-perform-mission-charts` | `getPerformMissionCharts` |
| POST | `/api/mission_dashboard/count-assign-mission` | `countAssignMission` |
| POST | `/api/mission_dashboard/count-perform-mission` | `countPerformMission` |
| POST | `/api/mission_dashboard/get-list-org-perform` | `getListOrgPerform` |
| POST | `/api/mission_dashboard/search-mission` | `searchMission` |
| POST | `/api/mission_dashboard/sync-mission` | `syncMission` |
| POST | `/api/mission_dashboard/count-sync-mission` | `countSyncMission` |

</details>

### MissionReportResultController (gen2) — base `/api/report-result`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MissionReportResultController.java`

- Service: `MissionReportResultService`, `MissionReportResultServiceImpl`, `MissionTemplateDetailService`, `MissionTemplateDetailServiceImpl`, `MissionReportResultDetailService`, `MissionReportResultDetailServiceImpl`, `MissionTemplateScopeService`, `MissionTemplateScopeServiceImpl`, `MissionTemplateTableService`, `MissionTemplateTableServiceImpl`
- DAO (SQL thuần): `FileAttachmentDAO`
- Repository (JPA): `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `MissionReportResultRepositoryJPA`, `MissionProcessRepositoryJPA`, `MissionReportResultDetailRepositoryJPA`, `MissionRepositoryJPA`, `MissionTemplateDetailRepositoryJPA`, `MissionTemplateScopeRepositoryJPA`, `MissionTemplateTableRepositoryJPA`, `MissionTemplateRepositoryJPA`, `MissionTemplateScopeDetailRepositoryJPA`, `ReportDailyHistoryJPA`, `UserRoleRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `BRIEF_FILE_MAP`, `FILES`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `MEETING`, `MISSION`, `MISSION_PROCESS`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_SCOPE_DETAIL`, `MISSION_TEMPLATE_TABLE`, `REPORT_DAILY_HISTORY`, `USER_ROLE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/report-result` | `updateReportResult` |
| GET | `/api/report-result` | `getReportResult` |
| GET | `/api/report-result/export` | `exportReportResult` |
| POST | `/api/report-result/report-daily/create-or-update` | `createOrUpdateReportDaily` |
| GET | `/api/report-result/report-daily/get-detail` | `getReportDailyHistory` |
| GET | `/api/report-result/report-daily/find-by-id/{id}` | `getReportDailyHistoryById` |
| GET | `/api/report-result/report-daily/find-by-textId/{textId}` | `getReportDailyHistoryByTextId` |
| POST | `/api/report-result/assign-specialist` | `assignSpecialist` |
| POST | `/api/report-result/unassign-specialist` | `unassignSpecialist` |
| POST | `/api/report-result/get-by-org-id-and-mission-template-id` | `getByOrgIdAndMissionTemplateId` |
| GET | `/api/report-result/get-list-org-perform-specialist` | `getListOrgPerformSpecialist` |
| GET | `/api/report-result/report-history/get-detail` | `getListReportHistory` |
| POST | `/api/report-result/send-confidential-report` | `senConfidentialReport` |

</details>

### MissionTemplateController (gen2) — base `/api/mission-template`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MissionTemplateController.java`

- Service: `MissionTemplateService`, `MissionTemplateServiceImpl`, `MissionTemplateDetailService`, `MissionTemplateDetailServiceImpl`, `MissionReportResultDetailService`, `MissionReportResultDetailServiceImpl`, `MissionTemplateScopeService`, `MissionTemplateScopeServiceImpl`, `MissionTemplateTableService`, `MissionTemplateTableServiceImpl`
- Repository (JPA): `MissionReportResultRepositoryJPA`, `MissionProcessRepositoryJPA`, `MissionReportResultDetailRepositoryJPA`, `MissionRepositoryJPA`, `MissionTemplateDetailRepositoryJPA`, `MissionTemplateScopeRepositoryJPA`, `MissionTemplateTableRepositoryJPA`, `MissionTemplateReceiveDocRepositoryJPA`, `MissionTemplateRepositoryJPA`, `ReportDailyHistoryJPA`, `UserRoleRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `MISSION`, `MISSION_PROCESS`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_RECEIVE_DOC`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_TABLE`, `REPORT_DAILY_HISTORY`, `USER_ROLE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/mission-template` | `getMissionTemplateList` |
| GET | `/api/mission-template/daily/org/{orgId}` | `getMissionTemplateListDaily` |
| POST | `/api/mission-template` | `addMissionTemplate` |
| PUT | `/api/mission-template` | `updateMissionTemplate` |
| GET | `/api/mission-template/config-detail` | `getConfigDetail` |
| GET | `/api/mission-template/get-list-org-report` | `getListOrgReport` |
| POST | `/api/mission-template/lock-report-result` | `lockReportResult` |
| GET | `/api/mission-template/get-list-receiver-doc/{textId}` | `getListOrgReport` |

</details>

### WorkGroupController (gen2) — base `/api/work-group`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/WorkGroupController.java`

- Service: `WorkGroupService`, `WorkGroupServiceImpl`
- Repository (JPA): `CategoryCommonRepositoryJPA`, `SysRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `WorkGroupOrgDetailJPA`, `WorkGroupRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `CATEGORY_COMMON`, `SYS_ROLE`, `WORK_GROUP`, `WORK_GROUP_ORG_DETAIL`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/work-group/search-work-group` | `searchWorkGroup` |
| GET | `/api/work-group/get-all-work-group` | `getAllWorkGroup` |
| POST | `/api/work-group/delete` | `deleteWorkGroup` |
| POST | `/api/work-group/block` | `block` |
| POST | `/api/work-group/create-or-update-work-group` | `createOrUpdateWorkGroup` |
| GET | `/api/work-group/get-detail-work-group/{workGroupId}` | `getDetailWorkGroup` |
| POST | `/api/work-group/get-work-group-to-recursive` | `getListWorkGroupToRecursive` |
| POST | `/api/work-group/check-valid-org-apply` | `checkValidToChangeOrgApply` |

</details>

### WorkGroupItemController (gen2) — base `/api/work-group-item`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/WorkGroupItemController.java`

- Service: `WorkGroupItemService`, `WorkGroupItemServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Repository (JPA): `CategoryCommonRepositoryJPA`, `VhrOrgJPA`, `WorkGroupItemHistoryRepositoryJPA`, `WorkGroupItemRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `CATEGORY_COMMON`, `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/work-group-item/create-or-update-work-group-item` | `createOrUpdateWorkGroupItem` |
| POST | `/api/work-group-item/search-work-group-item` | `searchWorkGroup` |
| GET | `/api/work-group-item/get-detail/{workGroupItemId}` | `getDetailWorkGroupItem` |
| GET | `/api/work-group-item/get-details` | `getDetailWorkGroupItem` |
| POST | `/api/work-group-item/delete` | `deleteWorkGroup` |
| POST | `/api/work-group-item/get-work-group-items-from-period` | `getDetailWorkGroupItem` |
| POST | `/api/work-group-item/get-work-group-items-for-next-week` | `getWorkGroupItemsForNextWeek` |
| POST | `/api/work-group-item/get-list-work-group-ids` | `getWorkGroupIds` |

</details>

### WorkGroupItemHistoryController (gen2) — base `/api/work-group-item-history`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/WorkGroupItemHistoryController.java`

- Service: `WorkGroupItemHistoryService`, `WorkGroupItemHistoryServiceImpl`
- Repository (JPA): `WorkGroupItemHistoryRepositoryJPA`, `WorkGroupItemRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/work-group-item-history/save` | `save` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `MissionFacade` | `IMission` | `MissionService` | `MissionJpaDao`, `MissionProcessJpaDao`, `SysUserJpaDao`, `VoMeetingMinutesUtilsJpaDao` | `MeetingMinutes (MEETING_MINUTES)`, `Mission (MISSION)`, `MissionProcess (MISSION_PROCESS)`, `SysUser (VHR_EMPLOYEE)` |
| `MissionRatingFacade` | `IMissionRating` | `MissionRatingService` | `MissionRatingJpaDao` | `MissionRating (MISSION_RATING)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `MissionEntity`→`MISSION`, `MissionNormEntity`→`MISSION_NORM`, `MissionProcessEntity`→`MISSION_PROCESS`, `MissionReportResultDetailEntity`→`MISSION_REPORT_RESULT_DETAIL`, `MissionReportResultEntity`→`MISSION_REPORT_RESULT`, `MissionTemplateDetailEntity`→`MISSION_TEMPLATE_DETAIL`, `MissionTemplateEntity`→`MISSION_TEMPLATE`, `MissionTemplateReceiveDocEntity`→`MISSION_TEMPLATE_RECEIVE_DOC`, `MissionTemplateScopeDetailEntity`→`MISSION_TEMPLATE_SCOPE_DETAIL`, `MissionTemplateScopeEntity`→`MISSION_TEMPLATE_SCOPE`, `MissionTemplateTableEntity`→`MISSION_TEMPLATE_TABLE`, `PermissionBaseEntity`→`PERMISSION_BASE`, `PermissionDashboardEntity`→`PERMISSION_DASHBOARD`, `PermissionDataEntity`→`PERMISSION_DATA`, `RolePermissionBaseEntity`→`ROLE_PERMISSION_BASE`, `RolePermissionDataEntity`→`ROLE_PERMISSION_DATA`, `WorkGroupEntity`→`WORK_GROUP`, `WorkGroupItemEntity`→`WORK_GROUP_ITEM`, `WorkGroupItemHistory`→`WORK_GROUP_ITEM_HISTORY`, `WorkGroupOrgDetailEntity`→`WORK_GROUP_ORG_DETAIL`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Mission`→`MISSION`, `MissionDetail`→`MISSION_DETAIL`, `MissionExtend`→`MISSION_EXTEND`, `MissionProcess`→`MISSION_PROCESS`, `MissionRating`→`MISSION_RATING`, `Permission`→`PERMISSION`, `RolePermission`→`ROLE_PERMISSION`

**Tổng hợp bảng chạm tới**: `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_EXTEND`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_RATING`, `MISSION_REPORT_RESULT`, `MISSION_REPORT_RESULT_DETAIL`, `MISSION_STATUS`, `MISSION_TEMPLATE`, `MISSION_TEMPLATE_DETAIL`, `MISSION_TEMPLATE_RECEIVE_DOC`, `MISSION_TEMPLATE_SCOPE`, `MISSION_TEMPLATE_SCOPE_DETAIL`, `MISSION_TEMPLATE_TABLE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `PERMISSION`, `PERMISSION_BASE`, `PERMISSION_DASHBOARD`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WORK_GROUP`, `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`, `WORK_GROUP_ORG_DETAIL`
