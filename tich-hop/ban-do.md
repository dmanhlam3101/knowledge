# Bản đồ hệ thống — Tích hợp ngoài: VHR, ViettelPay, WOPI, Solr/ES, mobile, chia sẻ ứng dụng ngoài

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 8 màn hình, 2 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `config/appMobile/appMobile.zul` | `vm.config.AppMobileVM` | `AppMobileBusiness` | — | BE |
| `config/extShare/extShareScopePopup.zul` | `vm.config.extShare.ExtShareScopePopupVM` | — | — | — |
| `enterprise/enterprise.zul` | `vm.enterprise.EnterpriseVM` | `EnterpriseBusiness` | — | BE |
| `enterprise/submitToEnterprise.zul` | `vm.enterprise.SubmitToEnterpriseVM` | `EnterpriseBusiness` | — | BE |
| `vps/sysConnectVHR/sysConnectVHR.zul` | `vps.vm.ConnectVHRVM` | `ConnectVHRBusiness` | — | BE |
| `widgets/connecVHRLookup.zul` | `widget.ConnectVHRLookupVM` | `ConnectVHRBusiness` | — | BE |
| `widgets/connecVHRLookupVbd.zul` | `widget.ConnectVHRLookupVbdVM` | `ConnectVHRBusiness` | — | BE |
| `widgets/connectVHRGroupLookUp.zul` | `widget.ConnectVHRLookupVM` | `ConnectVHRBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `widget.ConnectVHRGroupLookUpVM` | `CVGroupBusiness` | — | BE |
| `widget.PopupSelectConnectVHRVM` | — | — | — |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### AppMobileBusiness

`web-spring/src/main/java/com/voffice/service/business/AppMobileBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.app-mobile.create-or-update` | `/api/app-mobile/create-or-update` | `AppMobileController.createOrUpdate` | gen2 |
| `api.app-mobile.get-list` | `/api/app-mobile/get-list` | `AppMobileController.submissionGetList` | gen2 |

### ConnectVHRBusiness

`web-spring/src/main/java/com/voffice/service/business/ConnectVHRBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `connectVHRAction.checkCodeExist` | `/connectVHRAction/checkCodeExist` | `ConnectVHRAction.checkCodeExist` | gen1 |
| `connectVHRAction.createNewConnectVHR` | `/connectVHRAction/createNewConnectVHR` | `ConnectVHRAction.createNewConnectVHR` | gen1 |
| `connectVHRAction.deleteConnectVHR` | `/connectVHRAction/deleteConnectVHR` | `ConnectVHRAction.deleteConnectVHR` | gen1 |
| `connectVHRAction.findByCondition` | `/connectVHRAction/findByCondition` | `ConnectVHRAction.findByCondition` | gen1 |
| `connectVHRAction.findByGroup` | `/connectVHRAction/findByGroup` | `ConnectVHRAction.findByGroup` | gen1 |
| `connectVHRAction.getMaxChildSortOrder` | `/connectVHRAction/getMaxChildSortOrder` | `ConnectVHRAction.getMaxChildSortOrder` | gen1 |
| `connectVHRAction.updateConnectVHR` | `/connectVHRAction/updateConnectVHR` | `ConnectVHRAction.updateConnectVHR` | gen1 |
| `connectVHRAction.updateSyncOrg` | `/connectVHRAction/updateSyncOrg` | `ConnectVHRAction.updateSyncOrg` | gen1 |

### EnterpriseBusiness

`web-spring/src/main/java/com/voffice/service/business/EnterpriseBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `CM.checkPromulgation` | `/CM/checkPromulgation` | `CMResource.checkPromulgation` | gen1 |
| `CM.copyToTmpFolder` | `/CM/copyToTmpFolder` | `CMResource.copyToTmpFolder` | gen1 |
| `CM.createSignDocument` | `/CM/createSignDocument` | `IndexController.redirect` | gen2 |
| `CM.listCompany` | `/CM/listCompany` | `IndexController.redirect` | gen2 |
| `CM.search` | `/CM/search` | `CMResource.search` | gen1 |
| `CM.sendDocument` | `/CM/sendDocument` | `IndexController.redirect` | gen2 |
| `CM.updateStateDocument` | `/CM/updateStateDocument` | `CMResource.updateStateDocument` | gen1 |

### SearchSolrBusiness

`web-spring/src/main/java/com/voffice/service/business/SearchSolrBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `solrSearch.getCountItem` | `/solrSearch/getCountItem` | `SolrSearchResource.getCountItem` | gen1 |
| `solrSearch.getEmployeeCount` | `/solrSearch/getEmployeeCount` | `SolrSearchResource.getEmployeeCount` | gen1 |
| `solrSearch.getEmployeeList` | `/solrSearch/getEmployeeList` | `SolrSearchResource.getEmployeeList` | gen1 |
| `solrSearch.getListItem` | `/solrSearch/getListItem` | `SolrSearchResource.getListItem` | gen1 |
| `solrSearch.getOrgList` | `/solrSearch/getOrgList` | `SolrSearchResource.getOrgList` | gen1 |
| `solrSearch.indexEmployee` | `/solrSearch/indexEmployee` | `SolrSearchResource.indexEmployee` | gen1 |
| `solrSearch.searchTextTitle` | `/solrSearch/searchTextTitle` | `SolrSearchResource.getTextTitles` | gen1 |

### ShareExtDocBusiness

`web-spring/src/main/java/com/voffice/service/business/ShareExtDocBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `ext-doc.add-ext-doc` | `/ext-doc/add-ext-doc` | `ShareDocumentController.addExtDocument` | gen2 |
| `ext-doc.check-authorized-to-share` | `/ext-doc/check-authorized-to-share` | `ShareDocumentController.checkAuthorizedToShareByBuiltGroupIdOfDoc` | gen2 |
| `ext-doc.check-exist` | `/ext-doc/check-exist` | `ShareDocumentController.checkAuthorizedToShareByBuiltGroupIdOfDoc` | gen2 |

### SyncVHRBusiness

`web-spring/src/main/java/com/voffice/service/business/SyncVHRBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `SyncVHRAction.checkUserIsChangeOrgAndRemoveRole` | `/SyncVHRAction/checkUserIsChangeOrgAndRemoveRole` | `SyncVHRAction.checkUserIsChangeOrgAndRemoveRole` | gen1 |
| `SyncVHRAction.insertOrUpdateEmpVhrToVoffice` | `/SyncVHRAction/insertOrUpdateEmpVhrToVoffice` | `SyncVHRAction.insertOrUpdateEmpVhrToVoffice` | gen1 |
| `SyncVHRAction.insertPositionOther` | `/SyncVHRAction/insertPositionOther` | `SyncVHRAction.insertPositionOther` | gen1 |
| `SyncVHRAction.updateDirectorConfig` | `/SyncVHRAction/updateDirectorConfig` | `SyncVHRAction.updateDirectorConfig` | gen1 |
| `SyncVHRAction.updateDirectorConfigToExp` | `/SyncVHRAction/updateDirectorConfigToExp` | `SyncVHRAction.updateDirectorConfigToExp` | gen1 |
| `SyncVHRAction.updateOrInsertDefaultRoleOnlyUser` | `/SyncVHRAction/updateOrInsertDefaultRoleOnlyUser` | `SyncVHRAction.updateOrInsertDefaultRoleOnlyUser` | gen1 |

### VhrEmployeeBusiness

`web-spring/src/main/java/com/voffice/service/business/VhrEmployeeBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.vhr-employee` | `/api/vhr-employee` | `IndexController.redirect` | gen2 |
| `api.vhr-employee.get-VT-in-org` | `/api/vhr-employee/get-VT-in-org` | `VhrEmployeeController.getVhrEmployeeHasRolesInOrg` | gen2 |
| `api.vhr-employee.get-employees-default` | `/api/vhr-employee/get-employees-default` | `VhrEmployeeController.getEmployeesDefaultByOrgId` | gen2 |
| `api.vhr-employee.list` | `/api/vhr-employee/list` | `VhrEmployeeController.getEmployeesByIds` | gen2 |
| `api.vhr-employee.list-leader-by-org-ids` | `/api/vhr-employee/list-leader-by-org-ids` | `VhrEmployeeController.getLeadByListOrgIds` | gen2 |

### WOPIBusiness

`web-spring/src/main/java/com/voffice/service/business/WOPIBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `wopi.convertPdf` | `/wopi/convertPdf` | `WOPIAction.convertToPdf` | gen1 |
| `wopi.deleteAdditionalFile` | `/wopi/deleteAdditionalFile` | `WOPIAction.deleteAdditionalFile` | gen1 |
| `wopi.deleteTextAdditionalFile` | `/wopi/deleteTextAdditionalFile` | `WOPIAction.deleteTextAdditionalFile` | gen1 |
| `wopi.files` | `/wopi/files` | `IndexController.redirect` | gen2 |
| `wopi.getListEditHistories` | `/wopi/getListEditHistories` | `WOPIAction.getListEditHistories` | gen1 |
| `wopi.getListSubmissionFormEditHistories` | `/wopi/getListSubmissionFormEditHistories` | `WOPIAction.getListSubmissionFormEditHistories` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### CMResource (gen1) — base `/CM`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CMResource.java`

- Logic (gen-1 `controler/`): `CMController`, `UserControler`, `EmpCloudCAService`, `LogActionControler`
- Service: `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AutoDigitalSignDAO`, `CommonDataBaseDaoVO2`, `TextPartnerDAO`, `TextPartnerLogDAO`, `CloudDeviceCertDAO`, `ConfigParameterDAO`, `DocumentDAO`, `EmpCloudCADAO`, `SystemParameterDAO`, `FavouriteDAO`, `ImageDAO`, `LogActionDao`, `MeetingAssistantDAO`, `MissionDAO`, `OrgDAO`, `StaffDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGE_ORG`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `ORG_COMBINATION_MAP`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH_PARTNER`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PARTNER`, `TEXT_PARTNER_LOG`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/CM/search` | `search` |
| POST | `/CM/updateStateDocument` | `updateStateDocument` |
| POST | `/CM/copyToTmpFolder` | `copyToTmpFolder` |
| POST | `/CM/checkPromulgation` | `checkPromulgation` |
| POST | `/CM/getListTransactionFailed` | `getListTransactionFailed` |

</details>

### ConnectVHRAction (gen1) — base `/connectVHRAction`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/ConnectVHRAction.java`

- Logic (gen-1 `controler/`): `ConnectVHRController`, `CommonControler`
- Service: `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SigningFlowUpdateService`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ConnectVHRDao`, `ConfigParameterDAO`, `CommonDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`, `HistoryChangeSignDAO`
- Repository (JPA): `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `VhrOrgRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `UserRoleRepositoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CHILD_CNT`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MISSION`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/connectVHRAction/findByCondition` | `findByCondition` |
| POST | `/connectVHRAction/findByGroup` | `findByGroup` |
| POST | `/connectVHRAction/getMaxChildSortOrder` | `getMaxChildSortOrder` |
| POST | `/connectVHRAction/updateConnectVHR` | `updateConnectVHR` |
| POST | `/connectVHRAction/createNewConnectVHR` | `createNewConnectVHR` |
| POST | `/connectVHRAction/checkCodeExist` | `checkCodeExist` |
| POST | `/connectVHRAction/deleteConnectVHR` | `deleteConnectVHR` |
| POST | `/connectVHRAction/updateSyncOrg` | `updateSyncOrg` |

</details>

### SolrSearchResource (gen1) — base `/solrSearch`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SolrSearchResource.java`

- Logic (gen-1 `controler/`): `SolrSearchController`
- Service: `VhrOrgService`, `VhrOrgServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ConfigParameterDAO`, `DocumentDAO`, `OrgDAO`, `UserRoleDAO`
- Repository (JPA): `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `FILES_ATTACHMENT`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/solrSearch/getCountItem` | `getCountItem` |
| POST | `/solrSearch/getListItem` | `getListItem` |
| POST | `/solrSearch/getStatusUser` | `getStatusUser` |
| POST | `/solrSearch/getEmployeeCount` | `getEmployeeCount` |
| POST | `/solrSearch/getEmployeeList` | `getEmployeeList` |
| POST | `/solrSearch/indexEmployee` | `indexEmployee` |
| POST | `/solrSearch/searchTextTitle` | `getTextTitles` |
| POST | `/solrSearch/getOrgList` | `getOrgList` |

</details>

### SyncFavoriteAction (gen1) — base `/syncFavAction`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SyncFavoriteAction.java`

- Logic (gen-1 `controler/`): `SyncFavoriteClientController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `SyncFavoriteClientDAO`
- Bảng (ước lượng từ SQL/@Table): `GROUP_MAPPING`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/syncFavAction/syncEmployeeFav` | `syncEmployeeFav` |
| POST | `/syncFavAction/syncOrganizationFav` | `syncOrganizationFav` |

</details>

### SyncVHRAction (gen1) — base `/SyncVHRAction`, 6 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SyncVHRAction.java`

- Logic (gen-1 `controler/`): `SyncVHRController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `UserDAO`
- Bảng (ước lượng từ SQL/@Table): `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `DIRECTOR_CONFIG`, `DOCUMENT`, `EXT_APP`, `GROUP_MAPPING`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `P12_CERT`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/SyncVHRAction/insertOrUpdateEmpVhrToVoffice` | `insertOrUpdateEmpVhrToVoffice` |
| POST | `/SyncVHRAction/checkUserIsChangeOrgAndRemoveRole` | `checkUserIsChangeOrgAndRemoveRole` |
| POST | `/SyncVHRAction/updateOrInsertDefaultRoleOnlyUser` | `updateOrInsertDefaultRoleOnlyUser` |
| POST | `/SyncVHRAction/insertPositionOther` | `insertPositionOther` |
| POST | `/SyncVHRAction/updateDirectorConfig` | `updateDirectorConfig` |
| POST | `/SyncVHRAction/updateDirectorConfigToExp` | `updateDirectorConfigToExp` |

</details>

### VContractAction (gen1) — base `/vContract`, 3 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/VContractAction.java`

- Logic (gen-1 `controler/`): `VContractController`, `UserControler`, `EmpCloudCAService`, `LogActionControler`
- Service: `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `AttachDAO`, `SystemParameterDAO`, `TextDAO`, `TextSignDAO`, `CloudDeviceCertDAO`, `CommonDataBaseDaoVO2`, `ConfigParameterDAO`, `DocumentDAO`, `EmpCloudCADAO`, `FavouriteDAO`, `ImageDAO`, `LogActionDao`, `MeetingAssistantDAO`, `MissionDAO`, `OrgDAO`, `StaffDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `VContractDAO`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_PARTNER`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES_ATTACHMENT`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `ORG_COMBINATION_MAP`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/vContract/getTextDetail` | `getTextDetail` |
| POST | `/vContract/receiverResult` | `receiverResult` |
| POST | `/vContract/downloadFile` | `downloadFile` |

</details>

### VHROrgAction (gen1) — base `/VHROrgAction`, 12 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/VHROrgAction.java`

- Logic (gen-1 `controler/`): `VHROrgController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `SystemParameterDAO`, `VHROrgDAO`
- Bảng (ước lượng từ SQL/@Table): `CONNECT_VHR`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `MEETING_CONFIG`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/VHROrgAction/getVHROrg` | `getVHROrg` |
| POST | `/VHROrgAction/getSysRole` | `getSysRole` |
| POST | `/VHROrgAction/getVhrLeaderByUserId` | `getVhrLeaderByUserId` |
| POST | `/VHROrgAction/validateAddScheduleLeader` | `validateAddScheduleLeader` |
| POST | `/VHROrgAction/getVhrOrgUserAdminSchedule` | `getVhrOrgUserAdminSchedule` |
| POST | `/VHROrgAction/getListOrgDocumentRequestConfig` | `getListOrgDocumentRequestConfig` |
| POST | `/VHROrgAction/getMeetingManagerVhrOrg` | `getMeetingManagerVhrOrg` |
| POST | `/VHROrgAction/getDocumentManagerVhrOrg` | `getDocumentManagerVhrOrg` |
| POST | `/VHROrgAction/getBriefOrgKCQConfig` | `getBriefOrgKCQConfig` |
| POST | `/VHROrgAction/getOrgCode` | `getOrgCode` |
| POST | `/VHROrgAction/getListVHROrgByScopes` | `getListVHROrgByScopes` |
| POST | `/VHROrgAction/getVHROrgById` | `getVHROrgById` |

</details>

### ViettelPayAction (gen1) — base `/ViettelPay`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/ViettelPayAction.java`

- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/ViettelPay/VerifyDataTrans` | `VerifyDataTrans` |

</details>

### WOPIAction (gen1) — base `/wopi`, 10 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/WOPIAction.java`

- Logic (gen-1 `controler/`): `WOPIController`
- DAO (SQL thuần): `AttachDAO`, `CommonDataBaseDaoVO2`, `DocumentDAO`, `SubmissionFormEditHistoryDAO`, `SystemParameterDAO`, `TextEditHistoryDAO`
- Repository (JPA): `AttachRepositoryJPA`, `AttachTemplateRepositoryJPA`, `SubmissionFileRepositoryJPA`, `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `FILES_ATTACHMENT`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_SIGN_LOCATION`, `TEXT_TEXT_ATTACH`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/wopi/files/{encryptedFileInfo}` | `getFileInfo` |
| GET | `/wopi/files/{encryptedFileInfo}/contents` | `getFileContent` |
| POST | `/wopi/files/{encryptedFileInfo}/contents` | `putFileContent` |
| POST | `/wopi/getListEditHistories` | `getListEditHistories` |
| POST | `/wopi/getListSubmissionFormEditHistories` | `getListSubmissionFormEditHistories` |
| POST | `/wopi/deleteAdditionalFile` | `deleteAdditionalFile` |
| POST | `/wopi/deleteTextAdditionalFile` | `deleteTextAdditionalFile` |
| POST | `/wopi/generate-online-editor-url` | `generateOnlineEditorUrl` |
| POST | `/wopi/convertPdf` | `convertPdf` |
| GET | `/wopi/convertPdf` | `convertToPdf` |

</details>

### AppMobileController (gen2) — base `/api/app-mobile`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/AppMobileController.java`

- Service: `AppMobileService`, `AppMobileServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Repository (JPA): `AppMobileRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `APP_MOBILE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/app-mobile/get-list` | `submissionGetList` |
| POST | `/api/app-mobile/create-or-update` | `createOrUpdate` |
| POST | `/api/app-mobile/get-data-map` | `findByCondition` |
| POST | `/api/app-mobile/post-data-map` | `insertOrUpdateDataBase` |

</details>

### AuthenticationKntcController (gen2) — base `/`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/AuthenticationKntcController.java`

- Service: `AuthenticationService`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/connecteoffice/{employeeCode}` | `LoginKntc` |

</details>

### CallbackController (gen2) — base `/callback`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/CallbackController.java`

- Logic (gen-1 `controler/`): `CommonControler`, `WOPIController`
- Service: `BriefService`, `BriefServiceImpl`, `BriefDetailManagementService`, `BriefDetailManagementServiceImpl`, `CategoryCommonService`, `CategoryCommonServiceImpl`, `CategoryCacheService`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`
- DAO (SQL thuần): `BriefDetailManagementDAO`, `BriefManagementDAO`, `CatalogBriefDAO`, `CommonDataBaseDaoVO2`, `CommonDAO`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `FilesAttachmentDAO`, `TextDAO`, `DocumentSignDAO`, `P12CertDAO`, `StaffDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `AttachDAO`, `DocumentDAO`, `TextEditHistoryDAO`
- Repository (JPA): `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `BriefMultimediaFileJPA`, `BriefMultimediaJPA`, `CatalogingBriefFileRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `SubmissionMapRepositoryJPA`, `BriefShareEntityRepositoryJPA`, `BriefSubmitAttachFileEntityRepositoryJPA`, `BriefSubmitDocumentEntityRepositoryJPA`, `BriefSubmitRequestEntityRepositoryJPA`, `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`, `FilesAttachmentJPA`, `PositionRepositoryJPA`, `SecurityTypeRepositoryJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `AttachRepositoryJPA`, `FileEncryptMapJPA`, `NodeActionRepositoryJPA`, `ReportDailyHistoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `NotificationRepositoryJPA`, `StaffImageSignJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextAttachRepositoryJPA`, `AttachTemplateRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_DOCUMENT`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/callback/ext-brief/submit-result` | `submitResult` |

</details>

### MobilePublishStoreController (gen2) — base `/api/mobile-publish-store`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MobilePublishStoreController.java`

- Service: `MobilePublishStoreService`, `MobilePublishStoreServiceImpl`
- Repository (JPA): `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `SYSTEM_PARAMETER`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/mobile-publish-store/login-required-check` | `loginRequiredCheck` |

</details>

### PublicController (gen2) — base `/public`, 6 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/PublicController.java`

- Service: `AppMobileService`, `AppMobileServiceImpl`
- Repository (JPA): `AppMobileRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `APP_MOBILE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/public/sso-login-flags` | `getSSOLoginFlags` |
| POST | `/public/otps` | `requestOptSSO` |
| POST | `/public/sso-login-flags` | `updateSSOLoginFlags` |
| GET | `/public/check-update` | `checkUpdate` |
| GET | `/public/download` | `downloadInstaller` |
| GET | `/public/download/vofficedoc` | `downloadInstallerVofficeDoc` |

</details>

### ShareBriefController (gen2) — base `/ext-brief`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/extApp/ShareBriefController.java`

- Logic (gen-1 `controler/`): `BriefManagementController`, `CatalogBriefController`
- Service: `ExtBriefService`, `ExtBriefServiceImpl`, `BriefDetailManagementServiceImpl`, `ShareBriefService`, `ShareBriefServiceImpl`
- DAO (SQL thuần): `BriefDetailManagementDAO`, `BriefManagementDAO`, `CatalogBriefDAO`, `CommonDataBaseDaoVO2`, `FileAttachmentDAO`, `OrgDAO`, `VHROrgDAO`
- Repository (JPA): `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `BriefMultimediaFileJPA`, `BriefMultimediaJPA`, `CatalogingBriefFileRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `SubmissionMapRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `ATTACH_TEMPLATE`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CONNECT_VHR`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EMPLOYEE_TYPE_PROCESS`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `IMAGE_ORG`, `MEETING`, `MEETING_CONFIG`, `SECURITY_TYPE`, `SHELVES`, `STAFF_GROUP_ROLE`, `STORAGES`, `SUBMISSION_MAP`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/ext-brief/get-brief-by-sso` | `getBrief` |
| POST | `/ext-brief/brief-multimedia` | `createBriefMultimedia` |

</details>

### ShareDocumentConfigController (gen2) — base `/ext-app-config`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ShareDocumentConfigController.java`

- Service: `ExtShareConfigService`, `ExtShareConfigServiceImpl`
- Repository (JPA): `ExtShareConfigRepositoryJPA`, `ExtShareScopeJPA`
- Bảng (ước lượng từ SQL/@Table): `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/ext-app-config/insert` | `createExtShareConfig` |
| POST | `/ext-app-config/update` | `updateExtShareConfig` |
| POST | `/ext-app-config/delete` | `deleteExtShareConfig` |
| GET | `/ext-app-config/ext-share-scope/{extShareConfigId}` | `getExtShareScopeByExtShareConfigId` |

</details>

### ShareMissionController (gen2) — base `/ext-mission`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/extApp/ShareMissionController.java`

- Logic (gen-1 `controler/`): `MissionControler`, `CommonControler`, `MeetingController`, `LogActionControler`
- Service: `ShareMissionService`, `ShareMissionServiceImpl`, `CategoryCommonService`, `CategoryCommonServiceImpl`, `CategoryCacheService`, `DocCommentService`, `DocCommentServiceImpl`, `EcabinetService`, `EcabinetServiceImpl`
- DAO (SQL thuần): `AgreementDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `ActionLogMobileDAO`, `CiscoMeetingDAO`, `DocumentSignDAO`, `LogActionDao`, `MeetingDAO`, `MeetingMinutesDAO`, `MeetingNativeDAO`, `MeetingWeekDAO`, `MissionDAO`, `ObjectTransferViaAxisDAO`, `OrgDAO`, `RequestDAO`, `SourceMapDAO`, `StaffDAO`, `TextDAO`, `MissionChartDAO`, `TaskCommonDAO`, `UserOrgMapDAO`
- Repository (JPA): `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `MissionRepositoryJPA`, `NotificationRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/ext-mission/get-mission-by-sso` | `getMission` |

</details>

### ShareOrgController (gen2) — base `/ext-app`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/extApp/ShareOrgController.java`

- Service: `ShareOrgService`, `ShareOrgServiceImpl`
- Repository (JPA): `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/ext-app/get-org` | `getOrg` |

</details>

### UserDeviceController (gen2) — base `/api/user-device`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/UserDeviceController.java`

- Service: `UserDeviceService`, `UserDeviceServiceImpl`
- Repository (JPA): `UserDeviceJPA`
- Bảng (ước lượng từ SQL/@Table): `USER_DEVICE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/user-device/save-device` | `saveDevice` |
| POST | `/api/user-device/remove-device` | `getDataBarChart` |

</details>

### VhrEmployeeController (gen2) — base `/api/vhr-employee`, 17 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/VhrEmployeeController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `VhrEmployeeService`, `VhrEmployeeServiceImpl`, `ExtShareConfigService`, `ExtShareConfigServiceImpl`, `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SigningFlowUpdateService`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `DocumentDAO`, `ConfigParameterDAO`, `CommonDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`, `HistoryChangeSignDAO`
- Repository (JPA): `ExtAppApiEntityRepositoryJPA`, `ExtAppEntityRepositoryJPA`, `ExtShareConfigRepositoryJPA`, `ExtShareScopeJPA`, `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `VhrOrgRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `UserRoleRepositoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `SystemParameterRepositoryJPA`, `VhrOrgJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `EXT_APP_API`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/vhr-employee/list` | `getEmployeesByIds` |
| GET | `/api/vhr-employee/{employeeId}` | `getEmployeeById` |
| GET | `/api/vhr-employee/get-employees/{orgId}` | `getEmployeesByOrgId` |
| POST | `/api/vhr-employee/get-employees-default` | `getEmployeesDefaultByOrgId` |
| POST | `/api/vhr-employee/list-leader-by-org-ids` | `getLeadByListOrgIds` |
| POST | `/api/vhr-employee/get-VT-in-org` | `getVhrEmployeeHasRolesInOrg` |
| POST | `/api/vhr-employee/update-security-cert` | `updateSecurityCert` |
| POST | `/api/vhr-employee/get-list-security-code` | `getListSecurityCode` |
| POST | `/api/vhr-employee/get-list-certificate` | `getListCertificate` |
| POST | `/api/vhr-employee/update-certificate` | `updateCertificate` |
| GET | `/api/vhr-employee/get-employees-preside-by-org` | `getVhrEmployeePresideByOrganizationId` |
| GET | `/api/vhr-employee/get-security-cert/{id}` | `getSecurityCert` |
| GET | `/api/vhr-employee/find-nearest-landmark/{startId}` | `findNearestLandmark` |
| GET | `/api/vhr-employee/get-ext-app/{appCode}` | `getExtAppByAppCode` |
| POST | `/api/vhr-employee/insert-or-update-ext-app` | `insertOrUpdateExtApp` |
| POST | `/api/vhr-employee/delete-ext-app` | `deleteExtApp` |
| POST | `/api/vhr-employee/get-org-manager-list-for-consideration` | `getLeadByListOrgIds` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `EnterpriseFacade` | `IEnterprise` | `EnterpriseService` | `EnterpriseJpaDao` | `Meeting (MEETING)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `AppMobileEntity`→`APP_MOBILE`, `ConnectVhrEntity`→`CONNECT_VHR`, `ElasticDocumentPrivate`→`ELASTIC_DOCUMENT_PRIVATE`, `ElasticDocumentPublic`→`ELASTIC_DOCUMENT_PUBLIC`, `ExtAppApiEntity`→`EXT_APP_API`, `ExtAppEntity`→`EXT_APP`, `ExtDocumentAccessLogEntity`→`EXT_DOCUMENT_ACCESS_LOG`, `ExtDocumentEntity`→`EXT_DOCUMENT`, `ExtShareConfigEntity`→`EXT_SHARE_CONFIG`, `ExtShareScopeEntity`→`EXT_SHARE_SCOPE`, `UserDeviceEntity`→`USER_DEVICE`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `VHREmployee`→`VHR_EMPLOYEE`, `VHROrg`→`VHR_ORG`

**Tổng hợp bảng chạm tới**: `ACTION_LOG_SERVICE`, `APP_MOBILE`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_PARTNER`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_DOCUMENT`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CHILD_CNT`, `CLOUD_DEVICE_CERT`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `ELASTIC_DOCUMENT_PRIVATE`, `ELASTIC_DOCUMENT_PUBLIC`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `EXT_APP_API`, `EXT_DOCUMENT`, `EXT_DOCUMENT_ACCESS_LOG`, `EXT_SHARE_CONFIG`, `EXT_SHARE_SCOPE`, `FAVOURITE`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE`, `IMAGE_ORG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LOG_TRANSTION_SIGN`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_DATA`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STAFF_IN_MESSAGE`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_ATTACH_PARTNER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PARTNER`, `TEXT_PARTNER_LOG`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_DEVICE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`
