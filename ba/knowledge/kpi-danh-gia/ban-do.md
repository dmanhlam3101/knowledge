# Bản đồ hệ thống — KPI, tiêu chí, đánh giá, báo cáo định kỳ, thống kê

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 29 màn hình, 3 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `admin/criteriaGroup/criteriaGroup.zul` | `vm.admin.CriteriaGroupVM` | — | `ICriteriaGroup`, `IKPIIndex` | LEGACY |
| `admin/criteriaGroup/criteria_add.zul` | `vm.admin.CriteriaGroupVM` | — | `ICriteriaGroup`, `IKPIIndex` | LEGACY |
| `admin/criteriaGroup/criteria_viewDetail.zul` | `vm.admin.CriteriaGroupVM` | — | `ICriteriaGroup`, `IKPIIndex` | LEGACY |
| `criteriaOrg/configCriteriaOrg/configCriteriaOrg.zul` | `vm.criteria.ConfigCriteriaVM` | `CriteriaOrgBusiness` | — | BE |
| `criteriaOrg/configCriteriaOrg/popUpCriteriaInfo.zul` | `vm.criteria.ConfigCriteriaInfoVM` | — | — | — |
| `criteriaOrg/criteriaOrgMap/criteriaOrgMap.zul` | `vm.criteria.CriteriaOrgMapVM` | `CriteriaOrgBusiness`, `EvaluatedOrgBusiness` | — | BE |
| `criteriaOrg/criteriaOrgMap/popUpCriteriaOrgMapInfo.zul` | `vm.criteria.CriteriaOrgMapInfoVM` | — | — | — |
| `criteriaOrg/criteriaOrgRating/criteriaOrgRating.zul` | `vm.criteria.CriteriaOrgRatingVM` | `CriteriaOrgBusiness`, `DocumentBusiness`, `SearchSolrBusiness` | — | BE |
| `criteriaOrg/evaluatedCriteriaOrg.zul` | `vm.evaluatedOrg.EvaluatedCriteriaOrgVM` | `EvaluatedOrgBusiness`, `MissionBusiness` | `ISysUser` | BE+LEGACY |
| `criteriaOrg/orgCriteriaConfig.zul` | `vm.criteria.OrgCriteriaConfigVM` | `CriteriaOrgBusiness` | — | BE |
| `criteriaOrg/widgets/treeCriteria.zul` | `vm.criteria.CriteriaTreeVM` | — | — | — |
| `kiFormulaConfig/kiFormulaConfig.zul` | `vm.kiFormulaConfig.KiFormulaConfigVM` | — | `IKiFormulaConfig` | LEGACY |
| `kiFormulaConfig/kiFormulaConfig_viewDetail.zul` | `vm.kiFormulaConfig.KiFormulaConfigVM` | — | `IKiFormulaConfig` | LEGACY |
| `kpi/kpi_statistic.zul` | `vm.kpi.KpiStatisticVM` | `AnswerDocumentBusiness`, `KpiStatisticBusiness`, `VhrEmployeeBusiness` | `IVps` | BE+LEGACY |
| `kpiPortal/kpi.zul` | `vm.kpiPortal.KpiPortalVM` | `KpiPortalBusiness` | `ISysMenu` | BE+LEGACY |
| `mission/agreement/chartAgreement.zul` | `vm.mission.ChartAgreementVM` | `AgreementBusiness`, `MissionBusiness` | — | BE |
| `mission/agreement/popupChart.zul` | `vm.mission.ChartDetailVM` | — | — | — |
| `mission/evaluationUnit/evaluationUnit.zul` | `vm.mission.EvaluationUnitVM` | — | `IEvaluationUnit`, `IProposePoint`, `IRatioConfig` | LEGACY |
| `mission/evaluationUnit/evaluationUnitList.zul` | `vm.mission.EvaluationUnitListVM` | — | `IEvaluationUnit` | LEGACY |
| `mission/evaluationUnit/evaluationUnit_viewDetail.zul` | `vm.mission.EvaluationUnitVM` | — | `IEvaluationUnit`, `IProposePoint`, `IRatioConfig` | LEGACY |
| `ratioConfig/ratioConfig.zul` | `vm.ratioConfig.RatioConfigVM` | — | `IRatioConfig` | LEGACY |
| `ratioConfig/ratioConfig_viewDetail.zul` | `vm.ratioConfig.RatioConfigDetailVM` | — | — | — |
| `requisition/requisitionReport.zul` | `vm.requisition.RequisitionReportVM` | `DocHandoverBusiness`, `DocumentBusiness`, `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `summaryUsageReport/summaryUsageReport.zul` | `vm.summaryUsageReport.UsageReportVM` | `StatisticsReportBusiness` | — | BE |
| `task/personalTask/taskGanttChart.zul` | `vm.task.TaskGanttChartVM` | — | — | ☠ VM không tồn tại |
| `widgets/criteriaGroupLookup.zul` | `widget.CriteriaGroupLookupVM` | — | — | — |
| `widgets/criteriaLookup.zul` | `widget.CriteriaLookupVM` | — | — | — |
| `widgets/kpiPortal/add.zul` | `vm.kpiPortal.KpiAddVM` | `KpiPortalBusiness` | — | BE |
| `widgets/kpiPortal/kpi_add_system_downtime_log.zul` | `vm.kpiPortal.systemDowntimeLogVM` | `KpiPortalBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `util.vm.VoTaskEmpRatingUtils` | `TaskBusiness` | `ICommon`, `IRatioConfig` | BE+LEGACY |
| `vm.admin.CriteriaVM` | — | — | — |
| `vm.kpi.KpiStatisticSearchVM` | `AnswerDocumentBusiness`, `KpiStatisticBusiness` | — | BE |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### CriteriaOrgBusiness

`web-spring/src/main/java/com/voffice/service/business/CriteriaOrgBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Org.CreateTextFromOrgCriteriaRatingTotalList` | `/Org/CreateTextFromOrgCriteriaRatingTotalList` | `OrgResource.createTextFromOrgCriteriaRatingTotalList` | gen1 |
| `Org.GetOrgCriteriaDetail` | `/Org/GetOrgCriteriaDetail` | `OrgResource.getOrgCriteriaDetail` | gen1 |
| `Org.GetOrgCriteriaList` | `/Org/GetOrgCriteriaList` | `OrgResource.getOrgCriteriaList` | gen1 |
| `Org.GetOrgCriteriaRatingTotalList` | `/Org/GetOrgCriteriaRatingTotalList` | `OrgResource.getOrgCriteriaRatingTotalList` | gen1 |
| `Org.GetOrgListWhichHaveCriteria` | `/Org/GetOrgListWhichHaveCriteria` | `OrgResource.getOrgListWhichHaveCriteria` | gen1 |
| `Org.UpdateOrgCriteria` | `/Org/UpdateOrgCriteria` | `OrgResource.updateOrgCriteria` | gen1 |
| `Org.UpdateOrgCriteriaMap` | `/Org/UpdateOrgCriteriaMap` | `OrgResource.updateOrgCriteriaMap` | gen1 |
| `Org.getAllOrgCriteria` | `/Org/getAllOrgCriteria` | `OrgResource.getAllOrgCriteria` | gen1 |
| `Org.importOrgCriteria` | `/Org/importOrgCriteria` | `OrgResource.importOrgCriteria` | gen1 |
| `orgCriteria.getDetailOrgCriteriaConfig` | `/orgCriteria/getDetailOrgCriteriaConfig` | `OrgCriteriaAction.getDetailOrgCriteriaConfig` | gen1 |
| `orgCriteria.getListOrgCriteriaConfig` | `/orgCriteria/getListOrgCriteriaConfig` | `OrgCriteriaAction.getListOrgCriteriaConfig` | gen1 |
| `orgCriteria.insertOrgCriteriaConfig` | `/orgCriteria/insertOrgCriteriaConfig` | `OrgCriteriaAction.insertOrgCriteriaConfig` | gen1 |
| `taskAction.getListRatioConfigByOrg` | `/taskAction/getListRatioConfigByOrg` | `TaskAction.getListRatioConfigByOrg` | gen1 |

### EvaluatedOrgBusiness

`web-spring/src/main/java/com/voffice/service/business/EvaluatedOrgBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Org.GetOrgCriteriaList` | `/Org/GetOrgCriteriaList` | `OrgResource.getOrgCriteriaList` | gen1 |
| `Org.UpdateOrgCriteriaRating` | `/Org/UpdateOrgCriteriaRating` | `OrgResource.updateOrgCriteriaRating` | gen1 |
| `Org.getOrgRatingId` | `/Org/getOrgRatingId` | `OrgResource.getOrgRatingId` | gen1 |
| `orgCriteria.getListOrgCriteriaHistory` | `/orgCriteria/getListOrgCriteriaHistory` | `OrgCriteriaAction.getListOrgCriteriaHistory` | gen1 |

### KpiPortalBusiness

`web-spring/src/main/java/com/voffice/service/business/KpiPortalBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.kpi-portal` | `/api/kpi-portal` | `KpiPortalController.search` | gen2 |
| `api.kpi-portal.create` | `/api/kpi-portal/create` | `KpiPortalController.create` | gen2 |
| `api.system-downtime-log` | `/api/system-downtime-log` | `SystemDowntimeLogController.create` | gen2 |

### KpiStatisticBusiness

`web-spring/src/main/java/com/voffice/service/business/KpiStatisticBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.kpi.get-data-bar-chart` | `/api/kpi/get-data-bar-chart` | `KpiManagerController.getDataBarChart` | gen2 |
| `api.kpi.get-kpi-statistic` | `/api/kpi/get-kpi-statistic` | `KpiManagerController.getKpiStatistic` | gen2 |
| `api.kpi.get-list-brief` | `/api/kpi/get-list-brief` | `KpiManagerController.getListBrief` | gen2 |
| `api.kpi.get-list-document` | `/api/kpi/get-list-document` | `KpiManagerController.getListDocument` | gen2 |
| `api.kpi.get-list-submission` | `/api/kpi/get-list-submission` | `KpiManagerController.getListSubmission` | gen2 |
| `api.kpi.get-list-text` | `/api/kpi/get-list-text` | `KpiManagerController.getListText` | gen2 |

### ReportPeriodApproveBusiness

`web-spring/src/main/java/com/voffice/service/business/ReportPeriodApproveBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.report-period-approve.approve` | `/api/report-period-approve/approve` | `ReportPeriodApproveController.approveReportPeriod` | gen2 |
| `api.report-period-approve.get-detail-approve` | `/api/report-period-approve/get-detail-approve` | `ReportPeriodApproveController.getDetailApprove` | gen2 |
| `api.report-period-approve.reject` | `/api/report-period-approve/reject` | `ReportPeriodApproveController.rejectReportPeriod` | gen2 |
| `api.report-period-approve.search-report-period-approve` | `/api/report-period-approve/search-report-period-approve` | `ReportPeriodApproveController.searchReportPeriodApprove` | gen2 |
| `api.report-period-approve.send-leader-approval` | `/api/report-period-approve/send-leader-approval` | `ReportPeriodApproveController.sendLeaderApproval` | gen2 |

### ReportPeriodBusiness

`web-spring/src/main/java/com/voffice/service/business/ReportPeriodBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.report-period-individual.check-valid-approval` | `/api/report-period-individual/check-valid-approval` | `ReportPeriodIndividualController.checkValidApproval` | gen2 |
| `api.report-period-individual.check-valid-send-approval` | `/api/report-period-individual/check-valid-send-approval` | `ReportPeriodIndividualController.checkValidSendApproval` | gen2 |
| `api.report-period-individual.delete-report-period` | `/api/report-period-individual/delete-report-period` | `ReportPeriodIndividualController.removeReportPeriod` | gen2 |
| `api.report-period-individual.do-approval` | `/api/report-period-individual/do-approval` | `ReportPeriodIndividualController.doApproval` | gen2 |
| `api.report-period-individual.exists-report-period` | `/api/report-period-individual/exists-report-period` | `ReportPeriodIndividualController.existsByFields` | gen2 |
| `api.report-period-individual.export-report-period-individual` | `/api/report-period-individual/export-report-period-individual` | `ReportPeriodIndividualController.exportDailyVPTWDDocumentTo` | gen2 |
| `api.report-period-individual.export-report-period-unit` | `/api/report-period-individual/export-report-period-unit` | `ReportPeriodIndividualController.exportDailyVPTWDDocumentToUnit` | gen2 |
| `api.report-period-individual.get-detail` | `/api/report-period-individual/get-detail` | `ReportPeriodIndividualController.existsByFields` | gen2 |
| `api.report-period-individual.get-list-report-by-user` | `/api/report-period-individual/get-list-report-by-user` | `ReportPeriodIndividualController.getListReportByUser` | gen2 |
| `api.report-period-individual.get-list-report-by-user-rating` | `/api/report-period-individual/get-list-report-by-user-rating` | `ReportPeriodIndividualController.getListReportByUserRating` | gen2 |
| `api.report-period-individual.get-report-config-rating` | `/api/report-period-individual/get-report-config-rating` | `ReportPeriodIndividualController.getListReportConfigRating` | gen2 |
| `api.report-period-individual.rating-save` | `/api/report-period-individual/rating-save` | `ReportPeriodIndividualController.addOrEditRating` | gen2 |
| `api.report-period-individual.save` | `/api/report-period-individual/save` | `ReportPeriodIndividualController.addOrEditSelf` | gen2 |

### ReportPeriodConfigBusiness

`web-spring/src/main/java/com/voffice/service/business/ReportPeriodConfigBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.report-period-config.create-or-update-report-period-config` | `/api/report-period-config/create-or-update-report-period-config` | `ReportPeriodConfigController.createOrUpdatereportPeriodConfig` | gen2 |
| `api.report-period-config.delete` | `/api/report-period-config/delete` | `ReportPeriodConfigController.deleteWorkGroup` | gen2 |
| `api.report-period-config.find-by-sys-user-id` | `/api/report-period-config/find-by-sys-user-id` | `ReportPeriodConfigController.findBySysUserId` | gen2 |
| `api.report-period-config.get-detail-report-period-config` | `/api/report-period-config/get-detail-report-period-config` | `ReportPeriodConfigController.getReportPeriodConfigDetail` | gen2 |
| `api.report-period-config.search-report-period-config` | `/api/report-period-config/search-report-period-config` | `ReportPeriodConfigController.searchReportPeriodApprove` | gen2 |

### StatisticsReportBusiness

`web-spring/src/main/java/com/voffice/service/business/StatisticsReportBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.statistics.get-document-in-statistics` | `/api/statistics/get-document-in-statistics` | `StatisticsReportController.getDocumentInStatistics` | gen2 |
| `api.statistics.get-document-out-statistics` | `/api/statistics/get-document-out-statistics` | `StatisticsReportController.getDocumentOutStatistics` | gen2 |
| `api.statistics.get-document-out-statistics-ranking` | `/api/statistics/get-document-out-statistics-ranking` | `StatisticsReportController.getDocumentOutStatisticsRanking` | gen2 |
| `api.statistics.get-meeting-schedule-statistics` | `/api/statistics/get-meeting-schedule-statistics` | `StatisticsReportController.getMeetingScheduleStatistics` | gen2 |
| `api.statistics.get-mission-statistics` | `/api/statistics/get-mission-statistics` | `StatisticsReportController.getMissionStatistics` | gen2 |
| `api.statistics.get-usage-statistics` | `/api/statistics/get-usage-statistics` | `StatisticsReportController.getUsageStatistics` | gen2 |
| `api.vhr-org.get-list-child-all-level` | `/api/vhr-org/get-list-child-all-level` | `VhrOrgController.getListChildAllLevel` | gen2 |
| `api.vhr-org.get-list-direct-child` | `/api/vhr-org/get-list-direct-child` | `VhrOrgController.getListDirectChild` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### OrgCriteriaAction (gen1) — base `/orgCriteria`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/OrgCriteriaAction.java`

- Logic (gen-1 `controler/`): `OrgCriteriaController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `OrgCriteriaDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_ORG_RATING`, `ORG_CRITERIA`, `ORG_CRITERIA_CONFIG`, `ORG_CRITERIA_HISTORY`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_SOURCE`, `USER_ORG_MAP`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/orgCriteria/insertOrgCriteriaConfig` | `insertOrgCriteriaConfig` |
| POST | `/orgCriteria/getDetailOrgCriteriaConfig` | `getDetailOrgCriteriaConfig` |
| POST | `/orgCriteria/getListOrgCriteriaConfig` | `getListOrgCriteriaConfig` |
| POST | `/orgCriteria/getListOrgCriteriaHistory` | `getListOrgCriteriaHistory` |

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

### DraftMetadataController (gen2) — base `/api/document-kpi`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/services/document_kpi/DraftMetadataController.java`

- Logic (gen-1 `controler/`): `TextController`, `CommonControler`, `EmpCloudCAService`
- Service: `DraftMetadataService`, `DraftMetadataServiceImpl`, `CategoryCacheService`, `DocCommentService`, `DocCommentServiceImpl`, `DocumentHistoryLogService`, `DocumentHistoryLogServiceImpl`, `DocumentPermissionCacheService`, `DraftLifecycleEventService`, `DraftLifecycleEventServiceImpl`, `DraftLifecycleMissionClient`, `ElasticDocumentService`, `ElasticDocumentServiceImpl`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ManagerService`, `ManagerServiceImpl`, `OfficePublishedReplacementService`, `OfficePublishedReplacementServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`, `TextDraftService`, `TextDraftServiceImpl`, `TextProcessService`, `TextProcessServiceImpl`, `TextReceiverGroupDetailService`, `TextReceiverGroupDetailServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `TextDAO`, `AnswerDocumentDAO`, `AttachDAO`, `AutoDigitalSignDAO`, `BriefDetailManagementDAO`, `CloudDeviceCertDAO`, `CommonDAO`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `ConfigParameterDAO`, `DocOrgRepublishDAO`, `DocumentDAO`, `DocumentScopeDAO`, `DocumentSignDAO`, `DocumentPublishedTmpDAO`, `DocumentSearchInService`, `EmpCloudCADAO`, `HistoryChangeSignDAO`, `StaffDAO`, `StaffImageSignDAO`, `MeetingWeekDAO`, `MissionDAO`, `MissionSigningDAO`, `OrgDAO`, `ReminderHistoryDAO`, `FilesAttachmentDAO`, `P12CertDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `SysRoleDAO`, `TextBookDAO`, `TextCheckSpellDAO`, `TextCommonDAO`, `TextEditHistoryDAO`, `TextProcessDAO`, `ImageSignDao`, `TextProcessHistoryDAO`, `TextReceiverDAO`, `TextReceiverGroupDAO`, `TextSignDAO`
- Repository (JPA): `DraftMetadataRepository`, `AttachRepositoryJPA`, `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `CategoryCommonRepositoryJPA`, `DocumentHistoryLogJPA`, `DocumentTypeRepositoryJPA`, `TextBookRepositoryJPA`, `VhrOrgJPA`, `DocumentInListRequestRepositoryJPA`, `TextRepositoryJPA`, `ElasticDocumentPrivateRepositoryJPA`, `ElasticDocumentPublicRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `ConfigSmsModuleRepositoryJPA`, `EmpCaDetailRepositoryJPA`, `EmpCaRepositoryJPA`, `FeedbackImageRepositoryJPA`, `FeedbackLogFileRepositoryJPA`, `FeedbackProcessRepositoryJPA`, `FeedbackRepositoryJPA`, `ImageOrgConfigRepositoryJPA`, `ImageOrgRepositoryJPA`, `MenuRepositoryJPA`, `NotificationRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `PositionRepositoryJPA`, `RolePermissionBaseRepositoryJPA`, `RolePermissionDataRepositoryJPA`, `SmsBlackListRepositoryJPA`, `SysMenuRepositoryJPA`, `SysRoleMenuRepositoryJPA`, `SysRoleRepositoryJPA`, `SystemParameterRepositoryJPA`, `UserOrgMapRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `NodeActionRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `SecurityTypeRepositoryJPA`, `StaffImageSignJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `SubmissionMapRepositoryJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextDraftHistoryRepositoryJPA`, `TextDraftRepositoryJPA`, `AttachHistoryRepositoryJPA`, `FileEncryptMapHistoryJPA`, `LogTranstionSignRepositoryJPA`, `MessageJPA`, `NodeRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/document-kpi/draft-metadata/batch` | `getDraftMetadataBatch` |
| POST | `/api/document-kpi/draft-text-detail` | `getDraftTextDetail` |

</details>

### KpiManagerController (gen2) — base `/api/kpi`, 6 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/KpiManagerController.java`

- Service: `KpiManagerService`, `KpiManagerServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/kpi/get-kpi-statistic` | `getKpiStatistic` |
| POST | `/api/kpi/get-data-bar-chart` | `getDataBarChart` |
| POST | `/api/kpi/get-list-text` | `getListText` |
| POST | `/api/kpi/get-list-document` | `getListDocument` |
| POST | `/api/kpi/get-list-submission` | `getListSubmission` |
| POST | `/api/kpi/get-list-brief` | `getListBrief` |

</details>

### KpiPortalController (gen2) — base `/api/kpi-portal`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/KpiPortalController.java`

- Service: `KpiPortalService`, `KpiPortalServiceImpl`
- Repository (JPA): `KpiPortalJPA`, `SystemDowntimeLogJPA`
- Bảng (ước lượng từ SQL/@Table): `KPI`, `SYSTEM_DOWNTIME_LOG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/kpi-portal` | `search` |
| POST | `/api/kpi-portal/create` | `create` |
| POST | `/api/kpi-portal/update/{kpiId}` | `update` |
| GET | `/api/kpi-portal/{kpiId}` | `getDetail` |
| POST | `/api/kpi-portal/delete/{kpiId}` | `delete` |

</details>

### ReportPeriodApproveController (gen2) — base `/api/report-period-approve`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ReportPeriodApproveController.java`

- Service: `ReportPeriodApproveService`, `ReportPeriodApproveServiceImpl`, `ReportPeriodIndividualService`, `ReportPeriodIndividualServiceImpl`, `WorkGroupItemService`, `WorkGroupItemServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `PositionDAO`, `TaskDAO`
- Repository (JPA): `ReportPeriodApproveRepositoryJPA`, `ReportPeriodHistoryRepositoryJPA`, `ReportPeriodIndividualRepositoryJPA`, `VhrOrgJPA`, `VhrOrgRepositoryJPA`, `WorkGroupItemRepositoryJPA`, `CategoryCommonRepositoryJPA`, `WorkGroupItemHistoryRepositoryJPA`, `WorkGroupRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `CATEGORY_COMMON`, `CODE_MASTER`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `GENERAL_ITEM`, `MEETING_ASSISTANT`, `MISSION`, `ORG_KI`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REPORT_PERIOD_APPROVE`, `REPORT_PERIOD_HISTORY`, `REP_IN`, `REQUEST`, `REQUEST_PROCESS`, `SOURCE_MAP`, `STAFF`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ATTACH`, `TEXT_PROCESS`, `TIME_CONFIG`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `WORK_GROUP`, `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/report-period-approve/search-report-period-approve` | `searchReportPeriodApprove` |
| POST | `/api/report-period-approve/send-leader-approval` | `sendLeaderApproval` |
| POST | `/api/report-period-approve/get-detail-approve` | `getDetailApprove` |
| POST | `/api/report-period-approve/approve` | `approveReportPeriod` |
| POST | `/api/report-period-approve/reject` | `rejectReportPeriod` |

</details>

### ReportPeriodConfigController (gen2) — base `/api/report-period-config`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ReportPeriodConfigController.java`

- Service: `ReportPeriodConfigService`, `ReportPeriodConfigServiceImpl`
- Repository (JPA): `ReportPeriodConfigRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `REPORT_PERIOD_CONFIG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/report-period-config/search-report-period-config` | `searchReportPeriodApprove` |
| POST | `/api/report-period-config/create-or-update-report-period-config` | `createOrUpdatereportPeriodConfig` |
| POST | `/api/report-period-config/delete` | `deleteWorkGroup` |
| GET | `/api/report-period-config/get-detail-report-period-config/{reportPeriodConfigId}` | `getReportPeriodConfigDetail` |
| GET | `/api/report-period-config/find-by-sys-user-id/{sysUserId}` | `findBySysUserId` |

</details>

### ReportPeriodIndividualController (gen2) — base `/api/report-period-individual`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ReportPeriodIndividualController.java`

- Service: `ReportPeriodIndividualService`, `ReportPeriodIndividualServiceImpl`, `WorkGroupItemService`, `WorkGroupItemServiceImpl`, `WorkGroupReportService`, `WorkGroupReportServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `PositionDAO`, `TaskDAO`
- Repository (JPA): `ReportPeriodHistoryRepositoryJPA`, `ReportPeriodIndividualRepositoryJPA`, `VhrOrgJPA`, `VhrOrgRepositoryJPA`, `WorkGroupItemRepositoryJPA`, `CategoryCommonRepositoryJPA`, `WorkGroupItemHistoryRepositoryJPA`, `WorkGroupRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `CATEGORY_COMMON`, `CODE_MASTER`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `GENERAL_ITEM`, `MEETING_ASSISTANT`, `MISSION`, `ORG_KI`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REPORT_PERIOD_HISTORY`, `REP_IN`, `REQUEST`, `REQUEST_PROCESS`, `SOURCE_MAP`, `STAFF`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ATTACH`, `TEXT_PROCESS`, `TIME_CONFIG`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `WORK_GROUP`, `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/report-period-individual/get-list-report-by-user` | `getListReportByUser` |
| POST | `/api/report-period-individual/get-list-report-by-user-rating` | `getListReportByUserRating` |
| GET | `/api/report-period-individual/get-report-config-rating` | `getListReportConfigRating` |
| POST | `/api/report-period-individual/save` | `addOrEditSelf` |
| POST | `/api/report-period-individual/rating-save` | `addOrEditRating` |
| POST | `/api/report-period-individual/exists-report-period` | `existsByFields` |
| POST | `/api/report-period-individual/export-report-period-individual` | `exportDailyVPTWDDocumentTo` |
| POST | `/api/report-period-individual/export-report-period-unit` | `exportDailyVPTWDDocumentToUnit` |
| GET | `/api/report-period-individual/get-detail/{reportPeriodId}` | `existsByFields` |
| POST | `/api/report-period-individual/delete-report-period` | `removeReportPeriod` |
| POST | `/api/report-period-individual/check-valid-send-approval` | `checkValidSendApproval` |
| POST | `/api/report-period-individual/check-valid-approval` | `checkValidApproval` |
| POST | `/api/report-period-individual/do-approval` | `doApproval` |

</details>

### StatisticsReportController (gen2) — base `/api/statistics`, 7 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/StatisticsReportController.java`

- Service: `StatisticsReportService`, `StatisticsReportServiceImpl`, `VhrOrgServiceImpl`
- DAO (SQL thuần): `SystemParameterDAO`, `UserRoleDAO`
- Repository (JPA): `DocDailySummaryRepositoryJPA`, `SystemParameterRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `DOC_DAILY_SUMMARY`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ROLE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/statistics/get-usage-statistics` | `getUsageStatistics` |
| POST | `/api/statistics/get-document-in-statistics` | `getDocumentInStatistics` |
| POST | `/api/statistics/get-document-out-statistics` | `getDocumentOutStatistics` |
| POST | `/api/statistics/get-meeting-schedule-statistics` | `getMeetingScheduleStatistics` |
| POST | `/api/statistics/get-mission-statistics` | `getMissionStatistics` |
| GET | `/api/statistics/get-document-out-statistics-ranking` | `getDocumentOutStatisticsRanking` |
| GET | `/api/statistics/get-document-statistics-by-org` | `getDocumentStatisticsByOrg` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `CriteriaGroupFacade` | `ICriteriaGroup` | `CriteriaGroupService`, `ProposePointService` | `CriteriaGroupJpaDao`, `ProposePointJpaDao` | `CriteriaGroup (CRITERIA_GROUP)`, `ProposePoint (PROPOSE_POINT)` |
| `EmpRatingFacade` | `IEmpRating` | `EmpRatingService`, `OrgKiService` | `EmpRatingJpaDao`, `EmpTypeProcessJpaDao`, `OrgKiJpaDao` | `EmpRating (EMP_RATING)`, `OrgKi (ORG_KI)` |
| `EvaluationUnitFacade` | `IEvaluationUnit` | `EvaluationUnitService` | `EvaluationUnitJpaDao` | `EvaluationUnit (EVALUATION_UNIT)` |
| `KPIIndexFacade` | `IKPIIndex` | `KPIIndexService` | `KPIIndexJpaDao` | `KPIIndex (KPI_INDEX)` |
| `KiFormulaConfigFacade` | `IKiFormulaConfig` | `KiFormulaConfigService` | `KiFormulaConfigJpaDao` | `KiFormulaConfig (KI_FORMULA_CONFIG)` |
| `ProposePointFacade` | `IProposePoint` | `ProposePointService` | `ProposePointJpaDao` | `ProposePoint (PROPOSE_POINT)` |
| `RatioConfigDetailFacade` | `IRatioConfigDetail` | `RatioConfigDetailService` | `RatioConfigDetailJpaDao` | `RatioConfigDetail (RATIO_CONFIG_DETAIL)` |
| `RatioConfigFacade` | `IRatioConfig` | `RatioConfigDetailService`, `RatioConfigService` | `RatioConfigDetailJpaDao`, `EmpRatingJpaDao`, `RatioConfigJpaDao` | `EmpRating (EMP_RATING)`, `RatioConfig (RATIO_CONFIG)`, `RatioConfigDetail (RATIO_CONFIG_DETAIL)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `DocDailySummary`→`DOC_DAILY_SUMMARY`, `KpiPortal`→`KPI`, `ReportDailyHistoryEntity`→`REPORT_DAILY_HISTORY`, `ReportPeriodApproveEntity`→`REPORT_PERIOD_APPROVE`, `ReportPeriodConfigEntity`→`REPORT_PERIOD_CONFIG`, `ReportPeriodHistory`→`REPORT_PERIOD_HISTORY`, `ReportPeriodIndividualEntity`→`REP_IN`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Criteria`→`CRITERIA`, `CriteriaGroup`→`CRITERIA_GROUP`, `EmpRating`→`EMP_RATING`, `EvaluationUnit`→`EVALUATION_UNIT`, `KPIIndex`→`KPI_INDEX`, `KiFormulaConfig`→`KI_FORMULA_CONFIG`, `KiFormulaConfigDetail`→`RATIO_CONFIG_DETAIL`, `KpiPortal`→`KPI`, `OrgKi`→`ORG_KI`, `ProposePoint`→`PROPOSE_POINT`, `RatingKi`→`EMP_RATING`, `RatioConfig`→`RATIO_CONFIG`, `RatioConfigDetail`→`RATIO_CONFIG_DETAIL`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CODE_MASTER`, `CONFIG_ORG_RATING`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CRITERIA`, `CRITERIA_GROUP`, `CV_GROUP`, `CV_PRIORITY`, `DATA_SOURCE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_HISTORY_LOG`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_DAILY_SUMMARY`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EMP_RATING`, `EVALUATION_UNIT`, `EXT_APP`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FILE_ENCRYPT_MAP_HISTORY`, `FILTERED_DATA`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HAS_DEFAULT`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `KI_FORMULA_CONFIG`, `KPI`, `KPI_INDEX`, `LOG_TRANSTION_SIGN`, `LSTDOCID`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_SIGNING`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA`, `ORG_CRITERIA_CONFIG`, `ORG_CRITERIA_HISTORY`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `PROPOSE_POINT`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REPORT_PERIOD_APPROVE`, `REPORT_PERIOD_CONFIG`, `REPORT_PERIOD_HISTORY`, `REP_IN`, `REQUEST`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSDATE`, `SYSTEM_DOWNTIME_LOG`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_CHAIN`, `TEXT_CHECK_SPELLS`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MANUAL_NUMBER`, `TEXT_MARK`, `TEXT_MAX_NUMBER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_RECEIVER_GROUP`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WAITING_NUMBER_BOOK`, `WORK_GROUP`, `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`, `WORK_PROCESS`
