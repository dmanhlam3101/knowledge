# Bản đồ hệ thống — Luồng xử lý / luồng ký

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 7 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `flow/flow.zul` | `vm.flow.FlowVM` | `FlowBusiness` | — | BE |
| `flow/flow_config_action.zul` | `vm.flow.FlowConfigActionVM` | `FlowBusiness` | — | BE |
| `flow/flow_config_node.zul` | `vm.flow.FlowConfigNodeVM` | `FlowBusiness` | — | BE |
| `requisition/requisitionFlowDiagram.zul` | `vm.requisition.FlowChartVM` | — | — | — |
| `requisitionFlow/popUpRequisitionFlow.zul` | `vm.requisition.RequisitionFlowVM` | — | `ICommonVoffice`, `IRequisitionFlow` | LEGACY |
| `requisitionFlow/requisitionFlow.zul` | `vm.requisition.RequisitionFlowVM` | — | `ICommonVoffice`, `IRequisitionFlow` | LEGACY |
| `widgets/requisitionFlowLookup.zul` | `vm.requisition.RequisitionFlowLookupVM` | — | `IRequisitionFlow` | LEGACY |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### DocumentProcessTermBusiness

`web-spring/src/main/java/com/voffice/service/business/DocumentProcessTermBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `VHROrgAction.getBriefOrgKCQConfig` | `/VHROrgAction/getBriefOrgKCQConfig` | `VHROrgAction.getBriefOrgKCQConfig` | gen1 |
| `VHROrgAction.getListOrgDocumentRequestConfig` | `/VHROrgAction/getListOrgDocumentRequestConfig` | `VHROrgAction.getListOrgDocumentRequestConfig` | gen1 |
| `documentProcessTermConfig.addOrUpdateAutoSendConfig` | `/documentProcessTermConfig/addOrUpdateAutoSendConfig` | `DocumentProcessTermConfigAction.addOrUpdateAutoSendConfig` | gen1 |
| `documentProcessTermConfig.addOrUpdateConfig` | `/documentProcessTermConfig/addOrUpdateConfig` | `DocumentProcessTermConfigAction.addOrUpdateConfig` | gen1 |
| `documentProcessTermConfig.deleteAutoSendConfig` | `/documentProcessTermConfig/deleteAutoSendConfig` | `DocumentProcessTermConfigAction.deleteAutoSendConfig` | gen1 |
| `documentProcessTermConfig.deleteConfig` | `/documentProcessTermConfig/deleteConfig` | `DocumentProcessTermConfigAction.deleteConfig` | gen1 |
| `documentProcessTermConfig.getAutoSendConfigs` | `/documentProcessTermConfig/getAutoSendConfigs` | `DocumentProcessTermConfigAction.getAutoSendConfigs` | gen1 |
| `documentProcessTermConfig.getConfigDetail` | `/documentProcessTermConfig/getConfigDetail` | `DocumentProcessTermConfigAction.getConfigDetail` | gen1 |
| `documentProcessTermConfig.getConfigs` | `/documentProcessTermConfig/getConfigs` | `DocumentProcessTermConfigAction.getConfigs` | gen1 |
| `documentProcessTermConfig.getEmployeeStatus` | `/documentProcessTermConfig/getEmployeeStatus` | `DocumentProcessTermConfigAction.getEmployeeStatus` | gen1 |
| `documentProcessTermConfig.getListAutoSendConfigs` | `/documentProcessTermConfig/getListAutoSendConfigs` | `DocumentProcessTermConfigAction.getListAutoSendConfigs` | gen1 |
| `documentProcessTermConfig.getOwnerConfigs` | `/documentProcessTermConfig/getOwnerConfigs` | `DocumentProcessTermConfigAction.getOwnerConfigs` | gen1 |
| `documentProcessTermConfig.saveAutoProcessSetting` | `/documentProcessTermConfig/saveAutoProcessSetting` | `DocumentProcessTermConfigAction.saveAutoProcessSetting` | gen1 |

### FlowBusiness

`web-spring/src/main/java/com/voffice/service/business/FlowBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.flow-manager` | `/api/flow-manager` | `IndexController.redirect` | gen2 |
| `api.flow-manager.check-flow-code` | `/api/flow-manager/check-flow-code` | `FlowManagerController.getNextNodeId` | gen2 |
| `api.flow-manager.delete-flow` | `/api/flow-manager/delete-flow` | `FlowManagerController.deleteFlow` | gen2 |
| `api.flow-manager.flow-group-type.get-all` | `/api/flow-manager/flow-group-type/get-all` | `FlowManagerController.getFlowGroupTypes` | gen2 |
| `api.flow-manager.flow.copy` | `/api/flow-manager/flow/copy` | `FlowManagerController.copyFlow` | gen2 |
| `api.flow-manager.flow.create-or-update` | `/api/flow-manager/flow/create-or-update` | `FlowManagerController.createOrUpdateFlow` | gen2 |
| `api.flow-manager.get-flow-histories` | `/api/flow-manager/get-flow-histories` | `FlowManagerController.getFlowHistories` | gen2 |
| `api.flow-manager.get-list-flow` | `/api/flow-manager/get-list-flow` | `FlowManagerController.getListFlow` | gen2 |
| `api.flow-manager.node-action.get-all` | `/api/flow-manager/node-action/get-all` | `FlowManagerController.getNodeActions` | gen2 |
| `api.flow-manager.nodes.next-id` | `/api/flow-manager/nodes/next-id` | `FlowManagerController.getNextNodeId` | gen2 |
| `api.flow-manager.nodes.save` | `/api/flow-manager/nodes/save` | `FlowManagerController.saveNodes` | gen2 |
| `api.flow-manager.toggle-active-flow` | `/api/flow-manager/toggle-active-flow` | `FlowManagerController.toggleActiveFlow` | gen2 |
| `api.manager.check-vhrorg-from-systemparameter` | `/api/manager/check-vhrorg-from-systemparameter` | `ManagerController.checkVhrOrgFromSystemParameter` | gen2 |
| `api.manager.get-all-vhrorg-from-systemparameter` | `/api/manager/get-all-vhrorg-from-systemparameter` | `ManagerController.getAllVhrOrgFromSystemParameter` | gen2 |
| `api.manager.get-list-position` | `/api/manager/get-list-position` | `ManagerController.getListPosition` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### DocumentProcessTermConfigAction (gen1) — base `/documentProcessTermConfig`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentProcessTermConfigAction.java`

- Logic (gen-1 `controler/`): `DocumentProcessTermController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `DocumentRequestConfigDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_AUTO_SEND_DOCUMENT`, `DOCUMENT_REQUEST_CONFIG`, `DOCUMENT_REQUEST_CONFIG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/documentProcessTermConfig/addOrUpdateConfig` | `addOrUpdateConfig` |
| POST | `/documentProcessTermConfig/addOrUpdateAutoSendConfig` | `addOrUpdateAutoSendConfig` |
| POST | `/documentProcessTermConfig/getConfigs` | `getConfigs` |
| POST | `/documentProcessTermConfig/getAutoSendConfigs` | `getAutoSendConfigs` |
| POST | `/documentProcessTermConfig/getListAutoSendConfigs` | `getListAutoSendConfigs` |
| POST | `/documentProcessTermConfig/getOwnerConfigs` | `getOwnerConfigs` |
| POST | `/documentProcessTermConfig/getEmployeeStatus` | `getEmployeeStatus` |
| POST | `/documentProcessTermConfig/getConfigsByCondition` | `getConfigsByCondition` |
| POST | `/documentProcessTermConfig/getConfigsByListOrgIds` | `getConfigsByListOrgIds` |
| POST | `/documentProcessTermConfig/deleteConfig` | `deleteConfig` |
| POST | `/documentProcessTermConfig/saveAutoProcessSetting` | `saveAutoProcessSetting` |
| POST | `/documentProcessTermConfig/deleteAutoSendConfig` | `deleteAutoSendConfig` |
| POST | `/documentProcessTermConfig/getConfigDetail` | `getConfigDetail` |

</details>

### FlowManagerController (gen2) — base `/api/flow-manager`, 42 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/FlowManagerController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SigningFlowUpdateService`
- DAO (SQL thuần): `ConfigParameterDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`, `HistoryChangeSignDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MISSION`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/flow-manager/get-list-flow` | `getListFlow` |
| GET | `/api/flow-manager/get-flow-by-id/{flowId}` | `getFlowById` |
| POST | `/api/flow-manager/flow/create-or-update` | `createOrUpdateFlow` |
| POST | `/api/flow-manager/flow/copy/{flowId}` | `copyFlow` |
| POST | `/api/flow-manager/delete-flow/{flowId}` | `deleteFlow` |
| POST | `/api/flow-manager/toggle-active-flow/{flowId}` | `toggleActiveFlow` |
| GET | `/api/flow-manager/nodes/next-id` | `getNextNodeId` |
| POST | `/api/flow-manager/nodes/save` | `saveNodes` |
| GET | `/api/flow-manager/{flowId}/nodes` | `getNodesByFlowId` |
| GET | `/api/flow-manager/doc-out/get-users-next-step` | `DocOutGetUsersNextStep` |
| GET | `/api/flow-manager/doc-out/get-leaders` | `getLeaders` |
| PUT | `/api/flow-manager/doc-out/{textId}/signing-flow` | `updateSigningFlow` |
| GET | `/api/flow-manager/doc-out/signers-switch` | `DocOutSignersSwitch` |
| GET | `/api/flow-manager/doc-out/promulgation-units` | `getAllPromulgationUnits` |
| GET | `/api/flow-manager/node-dept-users/{nodeId}` | `getNodeDeptUsersByNodeId` |
| GET | `/api/flow-manager/flow-group-type/get-all` | `getFlowGroupTypes` |
| GET | `/api/flow-manager/doc-in/get-users-next-step` | `DocInGetUsersNextStep` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-v1` | `DocInGetUsersNextStepV1` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-v2` | `DocInGetUsersNextStepV2` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-show` | `DocInGetUsersNextStepShow` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-doc-show` | `DocInGetUsersNextStepDocShow` |
| POST | `/api/flow-manager/doc-in/get-users-next-step-by-org-id` | `DocInGetUsersNextStepByOrgId` |
| GET | `/api/flow-manager/doc-in/get-users-tree-next-step` | `DocInGetUsersTreeNextStep` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer` | `DocInGetUsersNextStepMultiTransfer` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer-v1` | `DocInGetUsersNextStepMultiTransferV1` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer-v2` | `DocInGetUsersNextStepMultiTransferV2` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer-show` | `DocInGetUsersNextStepMultiTransferShow` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-while-creating-document` | `DocInGetUsersNextStep` |
| GET | `/api/flow-manager/doc-in/get-groups-next-step` | `DocInGetGroupsNextStep` |
| GET | `/api/flow-manager/doc-in/get-groups-tree-next-step` | `DocInGetGroupsTreeNextStep` |
| GET | `/api/flow-manager/doc-in/get-groups-next-step-multi-transfer` | `DocInGetGroupsNextStepMultiTransfer` |
| GET | `/api/flow-manager/doc-in/get-users-tree-next-step-multi-transfer` | `DocInGetUsersTreeNextStepMultiTransfer` |
| GET | `/api/flow-manager/doc-in/get-users-next-step-multi-transfer-by-org-id` | `DocInGetUsersNextStepMultiTransferByOrgId` |
| GET | `/api/flow-manager/doc-in/get-groups-tree-next-step-multi-transfer` | `DocInGetGroupsTreeNextStepMultiTransfer` |
| GET | `/api/flow-manager/doc-in/get-groups-next-step-while-creating-document` | `DocInGetGroupsNextStep` |
| GET | `/api/flow-manager/node-action/get-all/{type}` | `getNodeActions` |
| GET | `/api/flow-manager/check-flow-code` | `getNextNodeId` |
| GET | `/api/flow-manager/get-list-node/{nodeIds}` | `getListNodeByNodeIds` |
| GET | `/api/flow-manager/check-transfer-free` | `getOrgTransferFreeLevelByOrgId` |
| GET | `/api/flow-manager/get-flow-histories` | `getFlowHistories` |
| GET | `/api/flow-manager/doc-in/consideration/get-users-next-step` | `getUsersNextStepConsideration` |
| GET | `/api/flow-manager/doc-in/consideration/get-groups-next-step` | `getGroupsNextStepConsideration` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `RequisitionFlowFacade` | `IRequisitionFlow` | `RequisitionFlowService` | `RequisitionFlowJpaDao` | `RequisitionFlow (REQUISITION_FLOW)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `FlowEntity`→`FLOW`, `FlowGroupTypeEntity`→`FLOW_GROUP_TYPE`, `NodeActionEntity`→`NODE_ACTION`, `NodeDeptUserEntity`→`NODE_DEPT_USER`, `NodeEntity`→`NODE`, `NodeToNodeActionEntity`→`NODE_TO_NODE_ACTION`, `NodeToNodeEntity`→`NODE_TO_NODE`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `RequisitionFlow`→`REQUISITION_FLOW`, `RequisitionFlowDetail`→`REQUISITION_FLOW_DETAIL`

**Tổng hợp bảng chạm tới**: `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_AUTO_SEND_DOCUMENT`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST_CONFIG`, `DOCUMENT_REQUEST_CONFIG_MAP`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MISSION`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUISITION_FLOW`, `REQUISITION_FLOW_DETAIL`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`
