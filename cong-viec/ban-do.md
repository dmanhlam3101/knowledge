# Bản đồ hệ thống — Công việc (task) – cá nhân, gắn văn bản

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 30 màn hình, 3 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `asign_taskrating/asign_taskrating.zul` | `vm.task.popUpAssignVM` | — | — | ☠ VM không tồn tại |
| `asign_taskrating/ratingasign.zul` | `vm.task.TaskRatingVM` | — | `ISysOrganization` | LEGACY |
| `configtask/config_task.zul` | `vm.task.TaskConFigVM` | — | `IMapConfig` | LEGACY |
| `task/empRating/empRating.zul` | `vm.task.EmpRatingVM` | — | `ISysOrganization` | LEGACY |
| `task/empRating/empRatingDirector.zul` | `vm.task.EmpRatingDirectorVM` | `TaskBusiness` | `IEmpRating`, `ITask` | BE+LEGACY |
| `task/empRating/empRatingEmployee.zul` | `vm.task.EmpRatingEmployeeVM` | `TaskBusiness` | — | BE |
| `task/empRating/empRatingManager.zul` | `vm.task.EmpRatingManagerVM` | `DocumentBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `StoragesBusiness`, `TaskBusiness` | `IEmpRating`, `IKiFormulaConfig`, `IRatioConfig`, `ISysUser` | BE+LEGACY |
| `task/empRating/popup/showViewEmpPdf.zul` | `vm.task.EmpRatingSignVM` | — | — | ☠ VM không tồn tại |
| `task/empRating/popup/viewFilesDetail.zul` | `vm.task.EmpRatingSignVM` | — | — | ☠ VM không tồn tại |
| `task/empRating/popup/viewFilesSign.zul` | `vm.task.EmpRatingSignVM` | — | — | ☠ VM không tồn tại |
| `task/empRating/signAllFilesDirector.zul` | `vm.task.EmpRatingSignAllFilesDirectorVM` | `TaskBusiness` | `ICommon`, `IEmpRating`, `IRatioConfig` | BE+LEGACY |
| `task/empRating/signAllFilesManager.zul` | `vm.task.EmpRatingSignAllFilesManagerVM` | `TaskBusiness` | `ICommon`, `IEmpRating`, `IRatioConfig` | BE+LEGACY |
| `task/ganttTask/ganttTask.zul` | `vm.task.TaskVM` | `DocumentBusiness`, `SysUserBusiness`, `TaskBusiness` | `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `task/individualTask.zul` | `vm.task.TaskVM` | `DocumentBusiness`, `SysUserBusiness`, `TaskBusiness` | `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `task/personalTask/popupAcceptTask.zul` | `vm.task.TaskRatingAcceptVm` | `TaskBusiness` | — | BE |
| `task/popUpTask.zul` | `vm.task.TaskVM` | `DocumentBusiness`, `SysUserBusiness`, `TaskBusiness` | `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `task/task.zul` | `vm.task.TaskVM` | `DocumentBusiness`, `SysUserBusiness`, `TaskBusiness` | `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `task/taskApproval.zul` | `vm.task.TaskApprovalVM` | `PersonalTaskBusiness`, `SearchSolrBusiness`, `SysUserBusiness`, `TaskBusiness` | `ISysUser`, `ITask` | BE+LEGACY |
| `task/taskEditable/taskEditable.zul` | `vm.task.TaskVM` | `DocumentBusiness`, `SysUserBusiness`, `TaskBusiness` | `ISysOrganization`, `ISysUser`, `ITask`, `IVps` | BE+LEGACY |
| `task/taskRating/popUpRating/popUpRating.zul` | `vm.task.TaskRatingExportVM` | `TaskBusiness` | — | BE |
| `task/taskRating/taskRating.zul` | `vm.task.TaskRatingVM` | — | `ISysOrganization` | LEGACY |
| `task/taskRating/taskRatingManager.zul` | `vm.task.TaskRatingManagerVM` | `PersonalTaskBusiness`, `SearchSolrBusiness`, `TaskBusiness` | `ICommon`, `IRatioConfig`, `ISysUser`, `ITask`, `ITaskRating` | BE+LEGACY |
| `task/taskRating/taskRatingReport.zul` | `vm.task.TaskRatingReportVM` | `TaskBusiness` | `IEmpRating`, `ISysUser`, `ITask`, `ITaskRating` | BE+LEGACY |
| `task/taskRating/taskRatingSelf.zul` | `vm.task.TaskRatingSeflVM` | `TaskBusiness` | — | BE |
| `task/task_transfer.zul` | `vm.task.TaskViewDetailVM` | `DocumentBusiness`, `TaskBusiness` | `ITask` | BE+LEGACY |
| `task/task_updateProcess.zul` | `vm.task.TaskViewDetailVM` | `DocumentBusiness`, `TaskBusiness` | `ITask` | BE+LEGACY |
| `task/task_user_list.zul` | `vm.task.TaskUserListVM` | `TaskBusiness` | — | BE |
| `task/task_viewDetail.zul` | `vm.task.TaskViewDetailVM` | `DocumentBusiness`, `TaskBusiness` | `ITask` | BE+LEGACY |
| `widgets/createdTaskRating.zul` | `widget.CreatedTaskRatingVM` | — | — | — |
| `widgets/empTaskRatingList.zul` | `widget.EmpTaskRatingListVM` | `TaskBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.task.TaskAddFromDocVM` | `DocumentBusiness`, `TaskBusiness` | — | BE |
| `vm.task.TaskComparator` | — | — | — |
| `vm.task.TaskNewVM` | — | `IPageIntroduction` | LEGACY |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### PersonalTaskBusiness

`web-spring/src/main/java/com/voffice/service/business/PersonalTaskBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `taskAction.CancelSignedTaskFileByEmployee` | `/taskAction/CancelSignedTaskFileByEmployee` | `TaskAction.cancelSignedTaskFileByEmployee` | gen1 |
| `taskAction.convertRatingTaskToPDF` | `/taskAction/convertRatingTaskToPDF` | `TaskAction.convertRatingTaskToPDF` | gen1 |
| `taskAction.convertTaskToPDF` | `/taskAction/convertTaskToPDF` | `TaskAction.convertTaskToPDF` | gen1 |
| `taskAction.createPersonalTaskSubmitFlow` | `/taskAction/createPersonalTaskSubmitFlow` | `TaskAction.createPersonalTaskSubmitFlow` | gen1 |
| `taskAction.deleteRatingTaskToPDF` | `/taskAction/deleteRatingTaskToPDF` | `TaskAction.deleteRatingTaskToPDF` | gen1 |
| `taskAction.exportListTaskFile` | `/taskAction/exportListTaskFile` | `TaskAction.exportListTaskFile` | gen1 |
| `taskAction.updateFileAttachmentFromTask` | `/taskAction/updateFileAttachmentFromTask` | `TaskAction.updateFileAttachmentFromTask` | gen1 |
| `taskAction.updateProportionPersonalTasks` | `/taskAction/updateProportionPersonalTasks` | `TaskAction.updateProportionPersonalTasks` | gen1 |

### SmsTaskBusiness

`web-spring/src/main/java/com/voffice/service/business/SmsTaskBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `smsTask.checkDocumentToSendSms` | `/smsTask/checkDocumentToSendSms` | `SmsTaskAction.checkDocumentToSendSms` | gen1 |
| `smsTask.sendSmsMeetingAssistant` | `/smsTask/sendSmsMeetingAssistant` | `SmsTaskAction.sendSmsMeetingAssistant` | gen1 |

### TaskBusiness

`web-spring/src/main/java/com/voffice/service/business/TaskBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Files.DownloadContentFile` | `/Files/DownloadContentFile` | `FileService.downloadContentFile` | gen1 |
| `Files.PreviewEmpRatingReport` | `/Files/PreviewEmpRatingReport` | `FileService.previewEmpRatingReport` | gen1 |
| `Sign.signMultiFileTask` | `/Sign/signMultiFileTask` | `SignResource.signMultiFileTask` | gen1 |
| `Storages.getOrgList` | `/Storages/getOrgList` | `StorageManagementAction.getOrgList` | gen1 |
| `TaskService.addTask` | `/TaskService/addTask` | `TaskService.addTask` | gen1 |
| `TaskService.checkEmpl` | `/TaskService/checkEmpl` | `TaskService.checkEmpl` | gen1 |
| `TaskService.checkKIOrg` | `/TaskService/checkKIOrg` | `TaskService.checkKIOrg` | gen1 |
| `TaskService.checkPointUnit` | `/TaskService/checkPointUnit` | `TaskService.checkPointUnit` | gen1 |
| `TaskService.deleteKIemp` | `/TaskService/deleteKIemp` | `TaskService.deleteKIemp` | gen1 |
| `TaskService.getDetailKIEmployee` | `/TaskService/getDetailKIEmployee` | `TaskService.getDetailKIEmployee` | gen1 |
| `TaskService.getFilesKIToView` | `/TaskService/getFilesKIToView` | `TaskService.getFilesKIToView` | gen1 |
| `TaskService.getKIEmp` | `/TaskService/getKIEmp` | `TaskService.getKIEmp` | gen1 |
| `TaskService.getListCommander` | `/TaskService/getListCommander` | `TaskService.getListCommander` | gen1 |
| `TaskService.getListEmpKI` | `/TaskService/getListEmpKI` | `TaskService.getListEmpKI` | gen1 |
| `TaskService.getListFilesKI` | `/TaskService/getListFilesKI` | `TaskService.getListFilesKI` | gen1 |
| `TaskService.getListRatioPoint` | `/TaskService/getListRatioPoint` | `TaskService.getListRatioPoint` | gen1 |
| `TaskService.getListSysRoleEvaluate` | `/TaskService/getListSysRoleEvaluate` | `TaskService.getListSysRoleEvaluate` | gen1 |
| `TaskService.getTreeEnforcement` | `/TaskService/getTreeEnforcement` | `TaskService.getTreeEnforcement` | gen1 |
| `TaskService.isCheckPermissionSign` | `/TaskService/isCheckPermissionSign` | `TaskService.isCheckPermissionSign` | gen1 |
| `TaskService.isCheckStatusSign` | `/TaskService/isCheckStatusSign` | `TaskService.isCheckStatusSign` | gen1 |
| `TaskService.isLeafOrg` | `/TaskService/isLeafOrg` | `TaskService.isLeafOrg` | gen1 |
| `TaskService.percentKI` | `/TaskService/percentKI` | `TaskService.percentKI` | gen1 |
| `TaskService.signKI` | `/TaskService/signKI` | `TaskService.signKI` | gen1 |
| `TaskService.unResignKIEmp` | `/TaskService/unResignKIEmp` | `TaskService.unResignKIEmp` | gen1 |
| `TaskService.updateKIOrg` | `/TaskService/updateKIOrg` | `TaskService.updateKIOrg` | gen1 |
| `TaskService.updateRequisitionDirect` | `/TaskService/updateRequisitionDirect` | `TaskService.updateRequisitionDirect` | gen1 |
| `taskAction.ApproveOrRejectTask` | `/taskAction/ApproveOrRejectTask` | `TaskAction.approveOrRejectTask` | gen1 |
| `taskAction.GetEmployeeListToAssess` | `/taskAction/GetEmployeeListToAssess` | `TaskAction.getEmployeeListToAssess` | gen1 |
| `taskAction.GetEmployeeListToAssign` | `/taskAction/GetEmployeeListToAssign` | `TaskAction.getEmployeeListToAssign` | gen1 |
| `taskAction.GetListPersonalTasksOfCurrentUser` | `/taskAction/GetListPersonalTasksOfCurrentUser` | `TaskAction.getListPersonalTasksOfCurrentUser` | gen1 |
| `taskAction.GetTaskListToAssessByEmployee` | `/taskAction/GetTaskListToAssessByEmployee` | `TaskAction.getTaskListToAssessByEmployee` | gen1 |
| `taskAction.GetTaskListToAssessByEmployeeEmp` | `/taskAction/GetTaskListToAssessByEmployeeEmp` | `TaskAction.getTaskListToAssessByEmployeeEmp` | gen1 |
| `taskAction.GetTaskListToAssignByEmployee` | `/taskAction/GetTaskListToAssignByEmployee` | `TaskAction.getTaskListToAssignByEmployee` | gen1 |
| `taskAction.approveOrRejectTaskProcess` | `/taskAction/approveOrRejectTaskProcess` | `TaskAction.approveOrRejectTaskProcess` | gen1 |
| `taskAction.checkStatusSignedTaskFileByEmployee` | `/taskAction/checkStatusSignedTaskFileByEmployee` | `TaskAction.checkStatusSignedTaskFileByEmployee` | gen1 |
| `taskAction.closeTask` | `/taskAction/closeTask` | `TaskAction.closeTask` | gen1 |
| `taskAction.deleteTask` | `/taskAction/deleteTask` | `TaskAction.deleteTask` | gen1 |
| `taskAction.exportReportTaskApproved` | `/taskAction/exportReportTaskApproved` | `TaskAction.exportReportTaskApproved` | gen1 |
| `taskAction.getCoordinator` | `/taskAction/getCoordinator` | `TaskAction.getCoordinator` | gen1 |
| `taskAction.getFileAttachmentTask` | `/taskAction/getFileAttachmentTask` | `TaskAction.getFileAttachmentTask` | gen1 |
| `taskAction.getListLeaderIdMission` | `/taskAction/getListLeaderIdMission` | `TaskAction.getListLeaderIdMission` | gen1 |
| `taskAction.getListRank` | `/taskAction/getListRank` | `TaskAction.getListRank` | gen1 |
| `taskAction.getListRatioConfig` | `/taskAction/getListRatioConfig` | `TaskAction.getListRatioConfig` | gen1 |
| `taskAction.getListRatioConfigDT` | `/taskAction/getListRatioConfigDT` | `TaskAction.getListRatioConfigDT` | gen1 |
| `taskAction.getListSubOrTransferredTask` | `/taskAction/getListSubOrTransferredTask` | `TaskAction.getListSubOrTransferredTask` | gen1 |
| `taskAction.getListTask` | `/taskAction/getListTask` | `TaskAction.getListTask` | gen1 |
| `taskAction.getListTaskReportRating` | `/taskAction/getListTaskReportRating` | `TaskAction.getListTaskReportRating` | gen1 |
| `taskAction.getListTaskStatistics` | `/taskAction/getListTaskStatistics` | `TaskAction.getListTaskStatistics` | gen1 |
| `taskAction.getSourceTask` | `/taskAction/getSourceTask` | `TaskAction.getSourceTask` | gen1 |
| `taskAction.getTaskDetail` | `/taskAction/getTaskDetail` | `TaskAction.getTaskDetail` | gen1 |
| `taskAction.getTaskListToAssessByEmployeeEmp` | `/taskAction/getTaskListToAssessByEmployeeEmp` | `TaskAction.getTaskListToAssessByEmployeeEmp` | gen1 |
| `taskAction.getTaskReceiverHistory` | `/taskAction/getTaskReceiverHistory` | `TaskAction.getTaskReceiverHistory` | gen1 |
| `taskAction.getUpdateTaskHistory` | `/taskAction/getUpdateTaskHistory` | `TaskAction.getUpdateTaskHistory` | gen1 |
| `taskAction.receiveTaskStatus` | `/taskAction/receiveTaskStatus` | `TaskAction.receiveTaskStatus` | gen1 |
| `taskAction.saveAverageTask` | `/taskAction/saveAverageTask` | `TaskAction.saveAverageTask` | gen1 |
| `taskAction.saveTaskRating` | `/taskAction/saveTaskRating` | `TaskAction.saveTaskRating` | gen1 |
| `taskAction.saveTaskRatingEmp` | `/taskAction/saveTaskRatingEmp` | `TaskAction.saveTaskRatingEmp` | gen1 |
| `taskAction.subEnforcementTask` | `/taskAction/subEnforcementTask` | `TaskAction.subEnforcementTask` | gen1 |
| `taskAction.transferEnforcementTask` | `/taskAction/transferEnforcementTask` | `TaskAction.transferEnforcementTask` | gen1 |
| `taskAction.updateRatioDetail` | `/taskAction/updateRatioDetail` | `TaskAction.updateRatioDetail` | gen1 |
| `taskAction.updateTaskProcess` | `/taskAction/updateTaskProcess` | `TaskAction.updateTaskProcess` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### SmsTaskAction (gen1) — base `/smsTask`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SmsTaskAction.java`

- Logic (gen-1 `controler/`): `SmsTaskController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `SmsDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_SMS_ORG`, `CV_GROUP`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `MEETING_ASSISTANT`, `MESSAGE`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/smsTask/sendSmsSignAfterMonth` | `sendSmsSignAfterMonth` |
| POST | `/smsTask/sendMulSmsSignAfterMonth` | `sendMulSmsSignAfterMonth` |
| POST | `/smsTask/sendSmsMeetingAssistant` | `sendSmsMeetingAssistant` |
| POST | `/smsTask/checkDocumentToSendSms` | `checkDocumentToSendSms` |

</details>

### TaskAction (gen1) — base `/taskAction`, 52 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TaskAction.java`

- Logic (gen-1 `controler/`): `TaskController`, `CommonControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `OrgDAO`, `StaffDAO`, `TaskDAO`, `TaskDataBaseDao`, `TaskProcessDAO`, `TextDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_KI`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_PROCESS`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TASK_RECEIVER`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/taskAction/getListTask` | `getListTask` |
| POST | `/taskAction/getListTaskFromMission` | `getListTaskFromMission` |
| POST | `/taskAction/getTaskDetail` | `getTaskDetail` |
| POST | `/taskAction/getUpdateTaskHistory` | `getUpdateTaskHistory` |
| POST | `/taskAction/getFileAttachmentTask` | `getFileAttachmentTask` |
| POST | `/taskAction/getRequestList` | `getRequestList` |
| POST | `/taskAction/getSourceTask` | `getSourceTask` |
| POST | `/taskAction/getTaskReceiverHistory` | `getTaskReceiverHistory` |
| POST | `/taskAction/deleteTask` | `deleteTask` |
| POST | `/taskAction/receiveTaskStatus` | `receiveTaskStatus` |
| POST | `/taskAction/closeTask` | `closeTask` |
| POST | `/taskAction/getDetailRequest` | `getDetailRequest` |
| POST | `/taskAction/updateTaskProcess` | `updateTaskProcess` |
| POST | `/taskAction/getListRatioConfig` | `getListRatioConfig` |
| POST | `/taskAction/approveOrRejectTaskProcess` | `approveOrRejectTaskProcess` |
| POST | `/taskAction/getListTaskToAssign` | `getListTaskToSign` |
| POST | `/taskAction/exportListTaskFile` | `exportListTaskFile` |
| POST | `/taskAction/updateCommentRequest` | `updateCommentRequest` |
| POST | `/taskAction/closeRequest` | `closeRequest` |
| POST | `/taskAction/getListTaskToAssess` | `getListTaskToAssess` |
| POST | `/taskAction/getListRatioConfigByOrg` | `getListRatioConfigByOrg` |
| POST | `/taskAction/getListTaskFromDocument` | `getListTaskFromDocument` |
| POST | `/taskAction/getCountHomeTask` | `getCountHomeTask` |
| POST | `/taskAction/convertTaskToPDF` | `convertTaskToPDF` |
| POST | `/taskAction/updateFileAttachmentFromTask` | `updateFileAttachmentFromTask` |
| POST | `/taskAction/convertRatingTaskToPDF` | `convertRatingTaskToPDF` |
| POST | `/taskAction/deleteRatingTaskToPDF` | `deleteRatingTaskToPDF` |
| POST | `/taskAction/GetEmployeeListToAssign` | `getEmployeeListToAssign` |
| POST | `/taskAction/GetTaskListToAssignByEmployee` | `getTaskListToAssignByEmployee` |
| POST | `/taskAction/GetListPersonalTasksOfCurrentUser` | `getListPersonalTasksOfCurrentUser` |
| POST | `/taskAction/GetEmployeeListToAssess` | `getEmployeeListToAssess` |
| POST | `/taskAction/GetTaskListToAssessByEmployee` | `getTaskListToAssessByEmployee` |
| POST | `/taskAction/CancelSignedTaskFileByEmployee` | `cancelSignedTaskFileByEmployee` |
| POST | `/taskAction/getListSubOrTransferredTask` | `getListSubOrTransferredTask` |
| POST | `/taskAction/getCoordinator` | `getCoordinator` |
| POST | `/taskAction/getListTaskReportRating` | `getListTaskReportRating` |
| POST | `/taskAction/getListTaskStatistics` | `getListTaskStatistics` |
| POST | `/taskAction/subEnforcementTask` | `subEnforcementTask` |
| POST | `/taskAction/transferEnforcementTask` | `transferEnforcementTask` |
| POST | `/taskAction/saveTaskRating` | `saveTaskRating` |
| POST | `/taskAction/updateProportionPersonalTasks` | `updateProportionPersonalTasks` |
| POST | `/taskAction/saveAverageTask` | `saveAverageTask` |
| POST | `/taskAction/saveTaskRatingEmp` | `saveTaskRatingEmp` |
| POST | `/taskAction/updateRatioDetail` | `updateRatioDetail` |
| POST | `/taskAction/exportReportTaskApproved` | `exportReportTaskApproved` |
| POST | `/taskAction/getListRatioConfigDT` | `getListRatioConfigDT` |
| POST | `/taskAction/getListRank` | `getListRank` |
| POST | `/taskAction/getTaskListToAssessByEmployeeEmp` | `getTaskListToAssessByEmployeeEmp` |
| POST | `/taskAction/ApproveOrRejectTask` | `approveOrRejectTask` |
| POST | `/taskAction/checkStatusSignedTaskFileByEmployee` | `checkStatusSignedTaskFileByEmployee` |
| POST | `/taskAction/createPersonalTaskSubmitFlow` | `createPersonalTaskSubmitFlow` |
| POST | `/taskAction/getListLeaderIdMission` | `getListLeaderIdMission` |

</details>

### TaskService (gen1) — base `/TaskService`, 25 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TaskService.java`

- Logic (gen-1 `controler/`): `TaskServiceController`, `CommonControler`, `TaskController`
- Service: `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `DocumentSignDAO`, `PersonTaskDAO`, `RequestDAO`, `OrgDAO`, `StaffDAO`, `TaskDAO`, `TaskDataBaseDao`, `TaskProcessDAO`, `TextDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_NORM`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TASK_RECEIVER`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/TaskService/addTask` | `addTask` |
| POST | `/TaskService/getListCommander` | `getListCommander` |
| POST | `/TaskService/getTreeEnforcement` | `getTreeEnforcement` |
| POST | `/TaskService/getListRequest` | `getListRequest` |
| POST | `/TaskService/getListPropose` | `getListPropose` |
| POST | `/TaskService/forwardRequest` | `forwardRequest` |
| POST | `/TaskService/deleteKIemp` | `deleteKIemp` |
| POST | `/TaskService/getKIEmp` | `getKIEmp` |
| POST | `/TaskService/getDetailKIEmployee` | `getDetailKIEmployee` |
| POST | `/TaskService/checkKIOrg` | `checkKIOrg` |
| POST | `/TaskService/checkEmpl` | `checkEmpl` |
| POST | `/TaskService/getListRatioPoint` | `getListRatioPoint` |
| POST | `/TaskService/isCheckPermissionSign` | `isCheckPermissionSign` |
| POST | `/TaskService/isCheckStatusSign` | `isCheckStatusSign` |
| POST | `/TaskService/checkPointUnit` | `checkPointUnit` |
| POST | `/TaskService/updateKIOrg` | `updateKIOrg` |
| POST | `/TaskService/getListEmpKI` | `getListEmpKI` |
| POST | `/TaskService/percentKI` | `percentKI` |
| POST | `/TaskService/isLeafOrg` | `isLeafOrg` |
| POST | `/TaskService/unResignKIEmp` | `unResignKIEmp` |
| POST | `/TaskService/signKI` | `signKI` |
| POST | `/TaskService/getListFilesKI` | `getListFilesKI` |
| POST | `/TaskService/getListSysRoleEvaluate` | `getListSysRoleEvaluate` |
| POST | `/TaskService/updateRequisitionDirect` | `updateRequisitionDirect` |
| POST | `/TaskService/getFilesKIToView` | `getFilesKIToView` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `TaskFacade` | `ITask` | `TaskProcessService`, `TaskRatingService`, `TaskService` | `TaskProcessJpaDao`, `TaskRatingJpaDao`, `TaskJpaDao`, `TaskReceiverJpaDao`, `VoTaskUtilsJpaDao` | `Task (TASK)`, `TaskProcess (TASK_PROCESS)`, `TaskRating (TASK_RATING)` |
| `TaskRatingFacade` | `ITaskRating` | `TaskRatingService` | `TaskRatingJpaDao` | `TaskRating (TASK_RATING)` |

## 5. Entity / bảng DB thuộc phân hệ

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Task`→`TASK`, `TaskApproval`→`TASK_APPROVAL`, `TaskFile`→`TASK_FILE`, `TaskProcess`→`TASK_PROCESS`, `TaskRating`→`TASK_RATING`, `TaskReceiver`→`TASK_RECEIVER`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `AVERAGE_TASK_RATING`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CODE_MASTER`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GENERAL_ITEM`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_NORM`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_KI`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TASK_RECEIVER`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_CONFIG`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `WORK_PROCESS`
