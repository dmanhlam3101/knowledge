# Bản đồ hệ thống — KPI, tiêu chí, đánh giá, báo cáo định kỳ, thống kê

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 28 màn hình, 3 VM không gắn zul trực tiếp.

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

**Tổng hợp bảng chạm tới**: `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `CATEGORY_COMMON`, `CODE_MASTER`, `CONFIG_ORG_RATING`, `CRITERIA`, `CRITERIA_GROUP`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `DOC_DAILY_SUMMARY`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EVALUATION_UNIT`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `GENERAL_ITEM`, `KI_FORMULA_CONFIG`, `KPI`, `KPI_INDEX`, `MEETING_ASSISTANT`, `MISSION`, `ORG_CRITERIA`, `ORG_CRITERIA_CONFIG`, `ORG_CRITERIA_HISTORY`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `POSITION`, `PROPOSE_POINT`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REPORT_DAILY_HISTORY`, `REPORT_PERIOD_APPROVE`, `REPORT_PERIOD_CONFIG`, `REPORT_PERIOD_HISTORY`, `REP_IN`, `REQUEST`, `REQUEST_PROCESS`, `SOURCE_MAP`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_DOWNTIME_LOG`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ATTACH`, `TEXT_PROCESS`, `TIME_CONFIG`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `WORK_GROUP`, `WORK_GROUP_ITEM`, `WORK_GROUP_ITEM_HISTORY`, `WORK_PROCESS`
