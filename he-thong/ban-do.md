# Bản đồ hệ thống — Quản trị hệ thống, danh mục, người dùng, vai trò, tổ chức, cấu hình

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 81 màn hình, 3 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `theme/admin-ex/pages/main.zul` | `vm.requisition.BannerVM` | `StatisticsReportBusiness` | — | BE |
| `changePassword.zul` | `widget.ChangePasswordVM` | — | — | — |
| `forgotPassword.zul` | `widget.ForgotPasswordVM` | — | — | — |
| `help.zul` | `widget.HelpVM` | — | — | — |
| `home.zul` | `common.HomeVM` | `HomeBusiness`, `MeetingBusiness`, `RequisitionBusiness` | `IMeeting`, `ISurvey`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `horizontalMenu.zul` | `cskh.front.common.HorizontalMenuVM` | — | — | ☠ VM không tồn tại |
| `index.zul` | `common.HomeVM` | `HomeBusiness`, `MeetingBusiness`, `RequisitionBusiness` | `IMeeting`, `ISurvey`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `profileInfo.zul` | `widget.ProfileInfoVM` | `ImageOrgBusiness`, `RequisitionBusiness` | — | BE |
| `register.zul` | `widget.RegisterVM` | — | — | — |
| `selectRole.zul` | `widget.SelectRoleVM` | — | `IVps` | LEGACY |
| `survey.zul` | `common.SurveyVM` | — | — | — |
| `admin/importOrganization.zul` | `vm.admin.ImportOrganizationVM` | — | — | — |
| `admin/primaryVariable/primaryVariable.zul` | `vm.admin.PrimaryVariableVM` | — | — | — |
| `admin/sysOrganization/sysOrganization.zul` | `vm.admin.SysOrganizationVM` | `MeetingBusiness`, `PublicMeetingBusiness` | `ISysOrganization` | BE+LEGACY |
| `category/categoryGroup/categoryGroup.zul` | `vm.category.CategoryGroupVM` | `CategoryCommonBusiness`, `CategoryGroupBusiness` | — | BE |
| `code/codeMaster.zul` | `vm.code.CodeMasterVM` | — | `ICodeMaster` | LEGACY |
| `config/configBackList.zul` | `vm.config.ConfigBackListVM` | `ConfigBusiness` | — | BE |
| `config/docProcessTermConfig.zul` | `vm.config.DocumentProcessTermConfigVM` | `DocumentProcessTermBusiness`, `RequisitionBusiness` | — | BE |
| `config/docProcessTermConfigAdd_popup.zul` | `vm.config.DocumentProcessTermConfigPopupVM` | `DocumentProcessTermBusiness`, `RequisitionBusiness` | — | BE |
| `config/notifyToNextSigner.zul` | `vm.config.NotifyToNextSignerVM` | `ConfigBusiness` | — | BE |
| `configPersonal/proposal.zul` | `vm.config.ProposalVM` | `ProposalBusiness` | — | BE |
| `document/reportSendReceiveDoc/reportContentSendReceiveDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/reportSendReceiveDoc/reportSendReceiveDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/transferDoc/transferContentDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `documentDraft/configDocManager.zul` | `vps.vm.ConfigDocManagerVM` | — | — | — |
| `document_type/document_type.zul` | `vm.document.DocumentTypeVM` | `DocumentTypeBusiness` | — | BE |
| `feedback/feedback.zul` | `vm.feedback.FeedbackVM` | `FeedbackBusiness` | — | BE |
| `feedback/feedback_send.zul` | `vm.feedback.PopupSendFeedbackVM` | `FeedbackBusiness` | — | BE |
| `feedback/feedback_update_status.zul` | `vm.feedback.PopupFeedbackUpdateStatusVM` | — | — | — |
| `feedback/feedback_view_detail.zul` | `vm.feedback.PopupFeedbackViewDetailVM` | `FeedbackBusiness` | — | BE |
| `financialRecords/listFianancialRecords/records.zul` | `vm.financialRecordsRoles.FinancialRecordsVM` | `DocumentBusiness`, `StoreTypeConfigBusiness` | — | BE |
| `financialRecords/roles/financialRecordsRoles.zul` | `vm.financialRecordsRoles.FinancialRecordsRolesVM` | `RequisitionBusiness`, `StoreTypeConfigBusiness` | `ISysOrganization` | BE+LEGACY |
| `group/groupDetail.zul` | `vm.group.GroupViewDetailVM` | — | — | — |
| `group/groupDetail_vbd.zul` | `vm.group.GroupViewDetailVM` | — | — | — |
| `group/group_manager.zul` | `vm.group.GroupVM` | — | — | — |
| `group/treegroup/group_org.zul` | `vm.group.OrgGroupSelectVM` | `DocumentBusiness` | — | BE |
| `group/treegroup/group_org_vbd.zul` | `vm.group.OrgGroupSelectVbdVM` | `DocumentBusiness` | — | BE |
| `group/treegroup/group_person.zul` | `vm.group.GroupSelectVM` | `CVGroupBusiness`, `DocumentBusiness` | — | BE |
| `group/treegroup/group_person_vbd.zul` | `vm.group.GroupSelectVbdVM` | `CVGroupBusiness`, `DocumentBusiness` | — | BE |
| `group/treegroup/group_person_vbd_multi.zul` | `vm.group.GroupSelectVbdMultiVM` | `CVGroupBusiness`, `DocumentBusiness` | — | BE |
| `logAuthen/authenHistoryLog.zul` | `vm.logAuthen.AuthenHistoryLogVM` | `FlowBusiness`, `ImageOrgBusiness`, `LogBusiness`, `RequisitionBusiness` | `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `pageIntroduction/pageIntroduction.zul` | `vm.pageIntroduction.PageIntroductionVM` | — | `IPageIntroduction` | LEGACY |
| `pageIntroduction/pageIntroduction_viewDetail.zul` | `vm.pageIntroduction.PageIntroductionVM` | — | `IPageIntroduction` | LEGACY |
| `personalGroup/personalGroup.zul` | `vm.personalGroup.PersonalGroupVM` | `PersonalGroupBusiness`, `SearchSolrBusiness` | `ISysOrganization` | BE+LEGACY |
| `position/popup_position.zul` | `vm.position.PopupPositionVM` | `PositionBusiness` | — | BE |
| `position/position.zul` | `vm.position.PositionVM` | `PositionBusiness` | — | BE |
| `privateShortcut/privateShortcut.zul` | `widget.PrivateShortcutVM` | — | `IPrivateShortcut` | LEGACY |
| `requisition/configDocManager.zul` | `vps.vm.ConfigDocManagerVM` | — | — | — |
| `survey/survey.zul` | `vm.survey.SurveyAdminVM` | — | `ISurvey` | LEGACY |
| `versionControl/versionControl_viewDetail.zul` | `vm.versionControl.VersionControlViewDetailVM` | `BriefBusiness`, `ConnectDocumentBusiness`, `DocumentBusiness`, `DocumentHistoryLogBusiness`, `EnterpriseBusiness`, `FlowBusiness`, `SearchSolrBusiness`, `TagDictionaryBusiness`, `TextBookBusiness`, `WOPIBusiness` | `IRequisition`, `ISysOrganization` | BE+LEGACY |
| `widgets/pageIntroduction_viewDetail.zul` | `vm.pageIntroduction.PageIntroductionVM` | — | `IPageIntroduction` | LEGACY |
| `widgets/popupCategoryGroup.zul` | `widget.PopupCategoryGroupVM` | `CategoryGroupBusiness` | — | BE |
| `widgets/popupCategoryGroupItem.zul` | `widget.PopupCategoryGroupItemVM` | `CategoryCommonBusiness` | — | BE |
| `widgets/popupInfoSelectSysRole.zul` | `widget.InfoSelectSysRoleVM` | `SysRoleBusiness` | — | BE |
| `vps/integratedSys/integratedSys.zul` | `vps.vm.IntegratedSysVM` | `CategoryCommonBusiness`, `SysUserBusiness` | `IPosition`, `ISysOrganization`, `ISysRole`, `ISysUser` | BE+LEGACY |
| `vps/sysCat/sysCat.zul` | `vps.vm.SysCatVM` | — | `ISysCat` | LEGACY |
| `vps/sysCatType/sysCatType.zul` | `vps.vm.SysCatTypeVM` | — | — | — |
| `vps/sysImageOrg/configImageOrg.zul` | `widget.PopupConfigOrgVM` | `ImageOrgBusiness` | `ISysOrganization` | BE+LEGACY |
| `vps/sysImageOrg/insertImageOrg.zul` | `widget.PopupImageOrgVM` | `ImageOrgBusiness` | `ISysOrganization` | BE+LEGACY |
| `vps/sysImageOrg/sysImageOrg.zul` | `vps.vm.SysImageOrgVM` | `ImageOrgBusiness`, `RequisitionBusiness` | `ISysOrganization` | BE+LEGACY |
| `vps/sysMenu/sysMenu.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `vps/sysOperation/sysOperation.zul` | `vps.vm.SysOperationVM` | — | `ISysOperation` | LEGACY |
| `vps/sysOrg/sysOrgMenu.zul` | `widget.SysOrgMenuVM` | `DocumentTypeBusiness` | `ISysOrganization` | BE+LEGACY |
| `vps/sysResource/sysResource.zul` | `vps.vm.SysResourceVM` | — | `ISysResource` | LEGACY |
| `vps/sysRole/roleMenu.zul` | `vps.vm.RoleMenuVM` | — | `ISysMenu`, `ISysRole` | LEGACY |
| `vps/sysRole/roleScopeData.zul` | `vps.vm.RoleScopeDataVM` | — | `ISysRole` | LEGACY |
| `vps/sysRole/sysRole.zul` | `vps.vm.SysRoleVM` | — | `ICommon`, `ISysRole` | LEGACY |
| `vps/sysRole/userRole.zul` | `vps.vm.UserRoleVM` | — | `ISysRole` | LEGACY |
| `vps/sysUser/importUser.zul` | `vps.vm.ImportSysUserVM` | `FlowBusiness`, `RequisitionBusiness` | `IPosition`, `ISysOrganization`, `ISysRole`, `ISysUser` | BE+LEGACY |
| `vps/sysUser/syncSysUser.zul` | `vps.vm.SyncSysUserVM` | — | — | — |
| `vps/sysUser/sysUser.zul` | `vps.vm.SysUserVM` | `DocumentProcessTermBusiness`, `FlowBusiness`, `ImageOrgBusiness`, `RequisitionBusiness` | `ISysUser` | BE+LEGACY |
| `vps/sysUser/userOrgMap.zul` | `vps.vm.UserOrgMapVM` | — | `ISysOrganization`, `ISysUser` | LEGACY |
| `widgets/assignDocumentCategory.zul` | `widget.AssignDocumentCategoryVM` | `PersonalDocCategoryBusiness`, `SavePersonalDocBusiness` | — | BE |
| `widgets/create_home_widget.zul` | `widget.CreateHomeWidgetVM` | — | — | — |
| `widgets/create_home_widget_detail.zul` | `widget.CreateHomeWidgetVM` | — | — | — |
| `widgets/homeSetting.zul` | `vps.vm.HomeSettingVM` | — | — | — |
| `widgets/menubar.zul` | `widget.MenuBarVM` | — | `ISysMenu`, `ISysOrganization`, `ITimeConfig` | LEGACY |
| `widgets/sysOrgWS2Lookup.zul` | `widget.SysOrganizationWS2LookupVM` | `RequisitionBusiness` | — | BE |
| `widgets/sysOrganizationLookup.zul` | `widget.SysOrganizationLookupVM` | — | `ISysOrganization` | LEGACY |
| `widgets/sysUserLookup.zul` | `widget.SysUserLookupVM` | — | — | — |
| `widgets/versionControl.zul` | `vm.versionControl.VersionControlVM` | `VersionControlBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `common.SecurityVM` | `CommonBusiness`, `ConfigBusiness`, `DocumentBusiness`, `EnterpriseBusiness`, `RequisitionBusiness`, `SubmissionFormBusiness` | — | BE |
| `util.vm.VoAdminRequestUtils` | — | — | — |
| `widget.HorizontalMenuVM` | — | — | — |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### CVGroupBusiness

`web-spring/src/main/java/com/voffice/service/business/CVGroupBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `CvGroupAction.checkVisibleGraspSituationMenu` | `/CvGroupAction/checkVisibleGraspSituationMenu` | `CvGroupAction.checkVisibleGraspSituationMenu` | gen1 |
| `CvGroupAction.getListGroup` | `/CvGroupAction/getListGroup` | `CvGroupAction.getListGroup` | gen1 |

### CategoryCommonBusiness

`web-spring/src/main/java/com/voffice/service/business/CategoryCommonBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.category-common.add-or-update-into-group` | `/api/category-common/add-or-update-into-group` | `CategoryCommonController.addOrUpdateIntoGroup` | gen2 |
| `api.category-common.delete-from-group` | `/api/category-common/delete-from-group` | `CategoryCommonController.deleteFromGroup` | gen2 |
| `api.category-common.list-category-by-code` | `/api/category-common/list-category-by-code` | `CategoryCommonController.getListCategoryByCode` | gen2 |
| `api.category-common.list-category-by-code-and-orgs` | `/api/category-common/list-category-by-code-and-orgs` | `CategoryCommonController.getListCategoryByCodeAndOrg` | gen2 |
| `api.category-common.page-category-by-condition` | `/api/category-common/page-category-by-condition` | `CategoryCommonController.getPagingCategoryByCondition` | gen2 |

### CategoryGroupBusiness

`web-spring/src/main/java/com/voffice/service/business/CategoryGroupBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.category-group.add-or-update` | `/api/category-group/add-or-update` | `CategoryGroupController.addOrUpdate` | gen2 |
| `api.category-group.delete` | `/api/category-group/delete` | `CategoryGroupController.delete` | gen2 |
| `api.category-group.get-list-organization` | `/api/category-group/get-list-organization` | `CategoryGroupController.getListOrganization` | gen2 |
| `api.category-group.search` | `/api/category-group/search` | `CategoryGroupController.search` | gen2 |

### ConfigBusiness

`web-spring/src/main/java/com/voffice/service/business/ConfigBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `DocumentService.getLitsUserSignWithRole` | `/DocumentService/getLitsUserSignWithRole` | `DocumentSignService.getLitsUserSignWithRole` | gen1 |
| `SmsInterceptAction.addOrRemoveInterceptByUser` | `/SmsInterceptAction/addOrRemoveInterceptByUser` | `SmsInterceptAction.addOrRemoveInterceptByUser` | gen1 |
| `SmsInterceptAction.getListModulInterceptSmsOfUserId` | `/SmsInterceptAction/getListModulInterceptSmsOfUserId` | `SmsInterceptAction.getListModulInterceptSmsOfUserId` | gen1 |
| `api.smsIntercept.getListModulInterceptSmsOfOrgId` | `/api/smsIntercept/getListModulInterceptSmsOfOrgId` | `SMSInterceptController.getListModulInterceptSmsOfOrg` | gen2 |
| `api.smsIntercept.updateSmsInterceptConfigByOrg` | `/api/smsIntercept/updateSmsInterceptConfigByOrg` | `SMSInterceptController.updateSmsInterceptConfigByOrg` | gen2 |
| `configParamAction.deleteConfigBackList` | `/configParamAction/deleteConfigBackList` | `ConfigParameterAction.deleteConfigBackList` | gen1 |
| `configParamAction.findConfigBackList` | `/configParamAction/findConfigBackList` | `ConfigParameterAction.findConfigBackList` | gen1 |
| `configParamAction.getListConfigBackList` | `/configParamAction/getListConfigBackList` | `ConfigParameterAction.getListConfigBackList` | gen1 |
| `configParamAction.getListConfigBackListByUserIds` | `/configParamAction/getListConfigBackListByUserIds` | `ConfigParameterAction.getListConfigBackListByUserIds` | gen1 |
| `configParamAction.insertConfigBackList` | `/configParamAction/insertConfigBackList` | `ConfigParameterAction.insertConfigBackList` | gen1 |
| `textAction.addOrUpdateLstUserReMessOfSignerLate` | `/textAction/addOrUpdateLstUserReMessOfSignerLate` | `IndexController.redirect` | gen2 |
| `textAction.getLstUserReMessOfSignerLate` | `/textAction/getLstUserReMessOfSignerLate` | `IndexController.redirect` | gen2 |

### FeedbackBusiness

`web-spring/src/main/java/com/voffice/service/business/FeedbackBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.manager.add-feedback` | `/api/manager/add-feedback` | `ManagerController.addFeedback` | gen2 |
| `api.manager.download-feedback-attach` | `/api/manager/download-feedback-attach` | `ManagerController.download` | gen2 |
| `api.manager.get-feedback-by-id` | `/api/manager/get-feedback-by-id` | `ManagerController.getFeedbackById` | gen2 |
| `api.manager.get-list-feedback` | `/api/manager/get-list-feedback` | `ManagerController.getListFeedback` | gen2 |
| `api.manager.get-list-feedback-process-by-feedback-id` | ❓ không tìm thấy endpoint | | |
| `api.manager.update-feedback-process` | `/api/manager/update-feedback-process` | `ManagerController.updateFeedbackProcess` | gen2 |

### HomeBusiness

`web-spring/src/main/java/com/voffice/service/business/HomeBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Authenticate.ChangeLanguageInSession` | `/Authenticate/ChangeLanguageInSession` | `AuthenticateResource.changeLanguageInSession` | gen1 |
| `DocumentAction.countDocument` | `/DocumentAction/countDocument` | `DocumentAction.countDocument` | gen1 |
| `MettingWeek.get3MeetingNearestOnDashboard` | `/MettingWeek/get3MeetingNearestOnDashboard` | `MettingWeek.get3MeetingNearestOnDashboard` | gen1 |
| `commonAction.getHomeWidgets` | `/commonAction/getHomeWidgets` | `CommonAction.getHomeWidgets` | gen1 |
| `missionAction.getCounMission` | `/missionAction/getCounMission` | `MissionAction.getCounMission` | gen1 |
| `textAction.getCountTextDashboard` | `/textAction/getCountTextDashboard` | `TextAction.getCountTextDashboard` | gen1 |

### ImageOrgBusiness

`web-spring/src/main/java/com/voffice/service/business/ImageOrgBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `imageOrgAction.addConfigImage` | `/imageOrgAction/addConfigImage` | `ImageOrgAction.addConfigImage` | gen1 |
| `imageOrgAction.addImageOrg` | `/imageOrgAction/addImageOrg` | `ImageOrgAction.addImageOrg` | gen1 |
| `imageOrgAction.findByConditionImageOrg` | `/imageOrgAction/findByConditionImageOrg` | `ImageOrgAction.findByConditionImageOrg` | gen1 |
| `imageOrgAction.getConfigImage` | `/imageOrgAction/getConfigImage` | `ImageOrgAction.getConfigImage` | gen1 |
| `imageOrgAction.getLstImageOther` | `/imageOrgAction/getLstImageOther` | `ImageOrgAction.getLstImageOther` | gen1 |
| `imageOrgAction.uploadImageOrg` | `/imageOrgAction/uploadImageOrg` | `ImageOrgAction.uploadImageOrg` | gen1 |
| `imageSignAction.editSignImage` | `/imageSignAction/editSignImage` | `ImageSignAction.editSignalImage` | gen1 |

### LogBusiness

`web-spring/src/main/java/com/voffice/service/business/LogBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.logs.advance-search-custom` | `/api/logs/advance-search-custom` | `LogElkController.advancedSearchCustom` | gen2 |
| `logAction.saveLogLogout` | `/logAction/saveLogLogout` | `LogAction.saveLogoutLog` | gen1 |
| `logAction.search-advance-elastic` | `/logAction/search-advance-elastic` | `LogAction.searchAdvanceElastic` | gen1 |

### PersonalGroupBusiness

`web-spring/src/main/java/com/voffice/service/business/PersonalGroupBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `CvGroupAction.addCvGroup` | `/CvGroupAction/addCvGroup` | `CvGroupAction.addCvGroup` | gen1 |
| `CvGroupAction.deleteCvGroup` | `/CvGroupAction/deleteCvGroup` | `CvGroupAction.deleteCvGroup` | gen1 |
| `CvGroupAction.editCvGroup` | `/CvGroupAction/editCvGroup` | `CvGroupAction.editCvGroup` | gen1 |
| `CvGroupAction.search` | `/CvGroupAction/search` | `CvGroupAction.search` | gen1 |
| `VHROrgAction.getVHROrgCvGroup` | `/VHROrgAction/getVHROrgCvGroup` | `IndexController.redirect` | gen2 |

### PositionBusiness

`web-spring/src/main/java/com/voffice/service/business/PositionBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `positionAction.delete` | `/positionAction/delete` | `PositionAction.delete` | gen1 |
| `positionAction.insert` | `/positionAction/insert` | `PositionAction.insertTextBook` | gen1 |
| `positionAction.positions` | `/positionAction/positions` | `PositionAction.search` | gen1 |
| `positionAction.toggleLock` | `/positionAction/toggleLock` | `PositionAction.toggleLock` | gen1 |

### ResovleIssueBusiness

`web-spring/src/main/java/com/voffice/service/business/ResovleIssueBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `missionAction.doUpdatePercentService` | `/missionAction/doUpdatePercentService` | `MissionAction.doUpdatePercentService` | gen1 |
| `missionAction.getMissionResovleIssueList` | `/missionAction/getMissionResovleIssueList` | `MissionAction.getMissionResovleIssueList` | gen1 |

### SysRoleBusiness

`web-spring/src/main/java/com/voffice/service/business/SysRoleBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `VHROrgAction.getSysRole` | `/VHROrgAction/getSysRole` | `VHROrgAction.getSysRole` | gen1 |

### SysUserBusiness

`web-spring/src/main/java/com/voffice/service/business/SysUserBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.vhr-employee.delete-ext-app` | `/api/vhr-employee/delete-ext-app` | `VhrEmployeeController.deleteExtApp` | gen2 |
| `api.vhr-employee.get-emps-by-ids` | `/api/vhr-employee/get-emps-by-ids` | `VhrEmployeeController.getEmployeeById` | gen2 |
| `api.vhr-employee.get-ext-app` | `/api/vhr-employee/get-ext-app` | `VhrEmployeeController.getEmployeeById` | gen2 |
| `api.vhr-employee.insert-or-update-ext-app` | `/api/vhr-employee/insert-or-update-ext-app` | `VhrEmployeeController.insertOrUpdateExtApp` | gen2 |
| `ext-app-config.ext-share-scope` | `/ext-app-config/ext-share-scope` | `IndexController.redirect` | gen2 |
| `staffAction.getListUserConfigAssistant` | `/staffAction/getListUserConfigAssistant` | `StaffAction.getListUserConfigAssistant` | gen1 |
| `staffAction.getUserInfor` | `/staffAction/getUserInfor` | `StaffAction.getUserInfor` | gen1 |

### VersionControlBusiness

`web-spring/src/main/java/com/voffice/service/business/VersionControlBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.version-control.delete-versionControl` | `/api/version-control/delete-versionControl` | `VersionControlController.deleteVersionControl` | gen2 |
| `api.version-control.get-list-file-versionControl` | `/api/version-control/get-list-file-versionControl` | `VersionControlController.getListVersionControlFile` | gen2 |
| `api.version-control.get-list-versionControl` | `/api/version-control/get-list-versionControl` | `VersionControlController.getListVersionControl` | gen2 |
| `api.version-control.get-versionControl-byNo` | ❓ không tìm thấy endpoint | | |
| `api.version-control.save-versionControl` | `/api/version-control/save-versionControl` | `VersionControlController.saveVersionControl` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### AuthenticateResource (gen1) — base `/Authenticate`, 17 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/AuthenticateResource.java`

- Logic (gen-1 `controler/`): `LogController`, `UserControler`, `EmpCloudCAService`, `LogActionControler`, `VContractController`
- Service: `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `ActionLogMobileDAO`, `CommonDataBaseDaoVO2`, `UserActivityLogDAO`, `CloudDeviceCertDAO`, `ConfigParameterDAO`, `DocumentDAO`, `EmpCloudCADAO`, `SystemParameterDAO`, `FavouriteDAO`, `ImageDAO`, `LogActionDao`, `MeetingAssistantDAO`, `MissionDAO`, `OrgDAO`, `StaffDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `AttachDAO`, `TextDAO`, `TextSignDAO`, `VContractDAO`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_PARTNER`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES_ATTACHMENT`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `ORG_COMBINATION_MAP`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ACTIVITY_LOG`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Authenticate/PingNetwork` | `PingNetwork` |
| POST | `/Authenticate/CheckServerStatus` | `checkServerStatus` |
| POST | `/Authenticate/getRsaKeyPublic` | `getRsaKeyPublic` |
| POST | `/Authenticate/login` | `login` |
| POST | `/Authenticate/logOut` | `logOut` |
| POST | `/Authenticate/EncryptAccountSSOForSmartOffice` | `encryptAccountSSOForSmartOffice` |
| POST | `/Authenticate/SyncFavouriteList` | `syncFavouriteList` |
| POST | `/Authenticate/LoginViaPassport` | `loginViaPassport` |
| POST | `/Authenticate/LoginViaVNEID` | `loginViaVNEID` |
| POST | `/Authenticate/checkThresholdPersonLogin` | `checkThresholdPersonLogin` |
| POST | `/Authenticate/checkLockAccountSSO` | `checkLockAccountSSO` |
| POST | `/Authenticate/changePass` | `changePass` |
| POST | `/Authenticate/ChangeLanguageInSession` | `changeLanguageInSession` |
| POST | `/Authenticate/LoginJWT` | `loginJWT` |
| POST | `/Authenticate/getAccessTokenJWT` | `getAccessTokenJWT` |
| POST | `/Authenticate/vofficeSystem` | `vofficeSystem` |
| POST | `/Authenticate/randManager` | `randManager` |

</details>

### ConfigParameterAction (gen1) — base `/configParamAction`, 7 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/ConfigParameterAction.java`

- Logic (gen-1 `controler/`): `ConfigParameterController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ConfigParameterDAO`, `SystemParameterDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_USER_DOCUMENT`, `SYSTEM_PARAMETER`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/configParamAction/getConfigParamMultiSign` | `getConfigParamMultiSign` |
| POST | `/configParamAction/getListConfigBackList` | `getListConfigBackList` |
| POST | `/configParamAction/getListConfigBackListByUserIds` | `getListConfigBackListByUserIds` |
| POST | `/configParamAction/findConfigBackList` | `findConfigBackList` |
| POST | `/configParamAction/deleteConfigBackList` | `deleteConfigBackList` |
| POST | `/configParamAction/insertConfigBackList` | `insertConfigBackList` |
| POST | `/configParamAction/GetAppConfig` | `getAppConfig` |

</details>

### CvGroupAction (gen1) — base `/CvGroupAction`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CvGroupAction.java`

- Logic (gen-1 `controler/`): `CvGroupController`, `CommonControler`
- Service: `FlowManagerService`, `FlowManagerServiceImpl`, `DocInService`, `DocInServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `EntityUserGroupCacheService`, `InternalDocumentService`, `InternalDocumentServiceImpl`, `ReminderService`, `ReminderServiceImpl`, `SigningFlowUpdateService`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ConnectVHRDao`, `CvGroupDAO`, `ConfigParameterDAO`, `CommonDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `DocumentProposalDAO`, `ReminderHistoryDAO`, `HistoryChangeSignDAO`, `StaffDAO`
- Repository (JPA): `ConnectDocumentRepositoryJPA`, `ConnectProcessInRepositoryJPA`, `DocumentInCvGroupRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInListRequestRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentProposalJpa`, `DocumentReceiveMapRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `FileEncryptMapJPA`, `InternalDocDetailRepositoryJPA`, `InternalDocSendXmlRepositoryJPA`, `VhrOrgRepositoryJPA`, `MessageJPA`, `NotificationRepositoryJPA`, `PositionRepositoryJPA`, `ReminderDocumentRelationRepositoryJPA`, `ReminderFollowerRepositoryJPA`, `ReminderHistoryJpa`, `ReminderReplyRepositoryJPA`, `ReminderRepositoryJPA`, `UserRoleJPA`, `VhrEmployeeJPA`, `ReportDailyHistoryJPA`, `UserRoleRepositoryJPA`, `FlowGroupTypeRepositoryJPA`, `FlowRepositoryJPA`, `NodeActionRepositoryJPA`, `NodeDeptUserRepositoryJPA`, `NodeRepositoryJPA`, `NodeToNodeActionRepositoryJPA`, `NodeToNodeRepositoryJPA`, `StaffImageSignJPA`, `SysRoleRepositoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CHILD_CNT`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DUOC`, `EXT_APP`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `GROUP_SIGN`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `LSTROOTEMP`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `MISSION`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_LEVEL`, `ORG_SYS_MENU`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `ROLE_IN_CV_GROUP`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/CvGroupAction/getListGroup` | `getListGroup` |
| POST | `/CvGroupAction/getListGroupV1` | `getListGroupV1` |
| POST | `/CvGroupAction/getListGroupV2` | `getListGroupV2` |
| POST | `/CvGroupAction/getListGroupMultiTransfer` | `getListGroupMultiTransfer` |
| POST | `/CvGroupAction/getListGroups` | `getListGroups` |
| POST | `/CvGroupAction/getCountListGroup` | `getCountListGroup` |
| POST | `/CvGroupAction/getListStaffOfGroup` | `getListStaffOfGroup` |
| POST | `/CvGroupAction/addCvGroup` | `addCvGroup` |
| POST | `/CvGroupAction/search` | `search` |
| POST | `/CvGroupAction/deleteCvGroup` | `deleteCvGroup` |
| POST | `/CvGroupAction/editCvGroup` | `editCvGroup` |
| POST | `/CvGroupAction/getListCvGroupByListId` | `getListCvGroupByListId` |
| POST | `/CvGroupAction/checkVisibleGraspSituationMenu` | `checkVisibleGraspSituationMenu` |

</details>

### FeatureTraceAction (gen1) — base `/api/feature-traces`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/FeatureTraceAction.java`

- Service: `LoggingServiceImpl`, `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `SYS_ROLE`, `TIME_ZONE_LOCAL`, `USER_TOKENS`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/feature-traces/complete` | `complete` |

</details>

### LogAction (gen1) — base `/logAction`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/LogAction.java`

- Logic (gen-1 `controler/`): `LoggingController`
- Service: `LogService`, `KpiConfigService`, `SystemParameterCacheService`, `VipUserService`
- Repository (JPA): `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `DATABASE`, `REDIS`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/logAction/saveLogLogout` | `saveLogoutLog` |
| POST | `/logAction/search-advance-elastic` | `searchAdvanceElastic` |

</details>

### LogResource (gen1) — base `/Log`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/LogResource.java`

- Logic (gen-1 `controler/`): `LogController`
- DAO (SQL thuần): `ActionLogMobileDAO`, `CommonDataBaseDaoVO2`, `UserActivityLogDAO`
- Bảng (ước lượng từ SQL/@Table): `USER_ACTIVITY_LOG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Log/InsertActionLogMobile` | `insertActionLogMobile` |
| POST | `/Log/InsertActionLogMobileBatch` | `insertActionLogMobileBatch` |
| POST | `/Log/InsertUserActivityLog` | `insertUserActivityLog` |
| GET | `/Log/getIPServer` | `getIPServer` |

</details>

### OrgResource (gen1) — base `/Org`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/OrgResource.java`

- Logic (gen-1 `controler/`): `OrgController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `OrgCriteriaDAO`, `OrgCriteriaMapDAO`, `OrgCriteriaRatingDAO`, `OrgCriteriaRatingTotalDAO`, `OrgDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_ORG_RATING`, `EMPLOYEE_TYPE_PROCESS`, `IMAGE_ORG`, `ORG_CRITERIA`, `ORG_CRITERIA_CONFIG`, `ORG_CRITERIA_HISTORY`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_RATING_TOTAL`, `ORG_CRITERIA_SOURCE`, `STAFF_GROUP_ROLE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Org/getListEmployeeOfOrganization` | `getListEmployeeOfOrganization` |
| POST | `/Org/checkSecretaryByGroupId` | `checkSecretaryByGroupId` |
| POST | `/Org/UpdateOrgCriteria` | `updateOrgCriteria` |
| POST | `/Org/GetOrgCriteriaList` | `getOrgCriteriaList` |
| POST | `/Org/GetOrgCriteriaDetail` | `getOrgCriteriaDetail` |
| POST | `/Org/UpdateOrgCriteriaMap` | `updateOrgCriteriaMap` |
| POST | `/Org/GetOrgListWhichHaveCriteria` | `getOrgListWhichHaveCriteria` |
| POST | `/Org/UpdateOrgCriteriaRating` | `updateOrgCriteriaRating` |
| POST | `/Org/GetOrgCriteriaRatingTotalList` | `getOrgCriteriaRatingTotalList` |
| POST | `/Org/CreateTextFromOrgCriteriaRatingTotalList` | `createTextFromOrgCriteriaRatingTotalList` |
| POST | `/Org/getOrgRatingId` | `getOrgRatingId` |
| POST | `/Org/importOrgCriteria` | `importOrgCriteria` |
| POST | `/Org/getAllOrgCriteria` | `getAllOrgCriteria` |

</details>

### PositionAction (gen1) — base `/positionAction`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/PositionAction.java`

- Logic (gen-1 `controler/`): `PositionController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `OrgDAO`, `PositionDAO`
- Bảng (ước lượng từ SQL/@Table): `EMPLOYEE_TYPE_PROCESS`, `IMAGE_ORG`, `POSITION`, `STAFF_GROUP_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/positionAction/insert` | `insertTextBook` |
| POST | `/positionAction/positions` | `search` |
| POST | `/positionAction/delete` | `delete` |
| POST | `/positionAction/toggleLock` | `toggleLock` |

</details>

### StaffAction (gen1) — base `/staffAction`, 12 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/StaffAction.java`

- Logic (gen-1 `controler/`): `UserControler`, `EmpCloudCAService`, `LogActionControler`
- Service: `CommonCacheService`, `EntityUserGroupCacheService`, `UserDetailsCacheService`, `UserTokenCacheService`
- DAO (SQL thuần): `CloudDeviceCertDAO`, `CommonDataBaseDaoVO2`, `ConfigParameterDAO`, `DocumentDAO`, `EmpCloudCADAO`, `SystemParameterDAO`, `FavouriteDAO`, `ImageDAO`, `LogActionDao`, `MeetingAssistantDAO`, `MissionDAO`, `OrgDAO`, `StaffDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `SysRoleJPA`, `TimeZoneLocalRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`, `UserTokensJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CLOUD_DEVICE_CERT`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CLOUD_CA`, `EXT_APP`, `FAVOURITE`, `FIELD`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE`, `IMAGE_ORG`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `ORG_COMBINATION_MAP`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PASS`, `PERFORM_ORG_AREA`, `POSITION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `USER_TOKENS`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/staffAction/getUserInfor` | `getUserInfor` |
| POST | `/staffAction/getListUser` | `getListUser` |
| POST | `/staffAction/getListUserMultiTransfer` | `getListUserMultiTransfer` |
| POST | `/staffAction/getListUserTransfer` | `getListUserTransfer` |
| POST | `/staffAction/searchUserRoles` | `searchUserRoles` |
| POST | `/staffAction/getOrgInfoById` | `getOrgInfoById` |
| POST | `/staffAction/getListUserMutiGroup` | `getListUserMutiGroup` |
| POST | `/staffAction/getLeaderByOrg` | `getLeaderByOrg` |
| POST | `/staffAction/getLstUserVip` | `getLstUserVip` |
| POST | `/staffAction/getListUserConfigAssistant` | `getListUserConfigAssistant` |
| POST | `/staffAction/getEmployeeByOrg` | `getEmployeeByOrg` |
| POST | `/staffAction/get-personal-detail` | `getUserDetail` |

</details>

### SystemManager (gen1) — base `/systemManager`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SystemManager.java`

- Logic (gen-1 `controler/`): `SystemManagerController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `SystemManagerDAO`
- Bảng (ước lượng từ SQL/@Table): `ROLE_MENU`, `SYS_MENU`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/systemManager/getMenuMain` | `getMenuMain` |

</details>

### AdminSystemController (gen2) — base `/adminsystem`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/AdminSystemController.java`

- Service: `AdminSystemService`, `AdminSystemServiceImpl`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/adminsystem/pushTypeWriteLog` | `pushTypeWriteLog` |

</details>

### AuthenticationController (gen2) — base `/Authentication`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/AuthenticationController.java`

- Service: `AuthenticationService`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Authentication/Login` | `Login` |
| POST | `/Authentication/LoginOTP` | `LoginOTP` |
| POST | `/Authentication/LoginVNEID` | `loginVNEID` |
| POST | `/Authentication/LoginEcabinet` | `loginEcabinet` |
| POST | `/Authentication/LoginSSO` | `LoginSSO` |
| POST | `/Authentication/check-username` | `checkUsername` |
| POST | `/Authentication/refresh-token` | `refreshToken` |
| POST | `/Authentication/LoginFromSSO` | `LoginFromSSO` |

</details>

### BaseRolesController (gen2) — base `/api/base-role`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/BaseRolesController.java`

- Service: `BaseRolesService`, `BaseRolesServiceImpl`
- Repository (JPA): `MenuRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `MENU`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/base-role/get-base-roles` | `getListRoleByUser` |
| GET | `/api/base-role/get-menu` | `getMenu` |
| GET | `/api/base-role/get-list-action` | `getListAction` |
| GET | `/api/base-role/get-list-role-by-mission` | `getListRoleByMission` |

</details>

### CacheManagementController (gen2) — base `/api/cache`, 20 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/CacheManagementController.java`

- Service: `CommonCacheService`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/cache/clear-all` | `clearAllCache` |
| POST | `/api/cache/clear/{cacheName}` | `clearCacheByName` |
| POST | `/api/cache/clear-multiple` | `clearMultipleCaches` |
| GET | `/api/cache/list` | `listAllCaches` |
| POST | `/api/cache/clear/user-tokens` | `clearUserTokensCache` |
| POST | `/api/cache/clear/sys-role` | `clearSysRoleCache` |
| POST | `/api/cache/clear/user-public-key` | `clearUserPublicKeyCache` |
| POST | `/api/cache/clear/user-details` | `clearUserDetailsCache` |
| POST | `/api/cache/clear/vhr-org` | `clearVhrOrgCache` |
| POST | `/api/cache/clear/system-parameter` | `clearSystemParameterCache` |
| POST | `/api/cache/clear/document-count` | `clearDocumentCountCache` |
| POST | `/api/cache/clear/org-ceo-all` | `clearAllOrgCeoCache` |
| POST | `/api/cache/clear/vhr-org-all` | `clearAllVHROrgCache` |
| POST | `/api/cache/clear/current-org-and-childs-all` | `clearAllCurrentOrgAndChildsCache` |
| GET | `/api/cache/detail/{cacheName}` | `getCacheDetail` |
| GET | `/api/cache/detail/{cacheName}/user/{userId}` | `getCacheDetailByUserId` |
| GET | `/api/cache/detail/{cacheName}/employee/{employeeCode}` | `getCacheDetailByEmployeeCode` |
| GET | `/api/cache/detail/{cacheName}/all` | `getAllCacheEntries` |
| GET | `/api/cache/methods` | `getAllCacheMethods` |
| GET | `/api/cache/methods/{cacheName}` | `getCacheMethodsByCacheName` |

</details>

### CategoryCommonController (gen2) — base `/api/category-common`, 7 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/CategoryCommonController.java`

- Service: `CategoryCommonService`, `CategoryCommonServiceImpl`, `CategoryCacheService`
- Repository (JPA): `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `CATEGORY_COMMON`, `GROUP_APPLY`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/category-common/list-sub-type` | `getListSubType` |
| GET | `/api/category-common/list-form-type` | `getListFormType` |
| GET | `/api/category-common/list-category-by-code` | `getListCategoryByCode` |
| GET | `/api/category-common/page-category-by-condition` | `getPagingCategoryByCondition` |
| GET | `/api/category-common/list-category-by-code-and-orgs` | `getListCategoryByCodeAndOrg` |
| POST | `/api/category-common/add-or-update-into-group` | `addOrUpdateIntoGroup` |
| POST | `/api/category-common/delete-from-group` | `deleteFromGroup` |

</details>

### CategoryController (gen2) — base `/api/category`, 34 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/CategoryController.java`

- Service: `CategoryService`, `CategoryServiceImpl`
- Repository (JPA): `AreaLanguageRepositoryJPA`, `AreaRepositoryJPA`, `CvPriorityLanguageRepositoryJPA`, `CvPriorityRepositoryJPA`, `DocumentTypeLanguageRepositoryJPA`, `DocumentTypeRepositoryJPA`, `FilesRepositoryJPA`, `LanguageRepositoryJPA`, `MeetingResourceManagerRepositoryJPA`, `MeetingResourceRepositoryJPA`, `MenuRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `SecurityTypeLanguageRepositoryJPA`, `SecurityTypeRepositoryJPA`, `VhrOrgRepositoryJPA`, `VideoConferenceGroupRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `AREA_LANGUAGE`, `CV_PRIORITY`, `CV_PRIORITY_LANGUAGE`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_LANGUAGE`, `FILES`, `LANGUAGE`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `PERMISSION_BASE`, `PERMISSION_DATA`, `SECURITY_TYPE`, `SECURITY_TYPE_LANGUAGE`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/category/get-list-document-information` | `getListDocumentInformation` |
| GET | `/api/category/get-document-information-detail/{type}/{documentInformationId}` | `getDocumentInformationDetail` |
| POST | `/api/category/add-document-information/{type}` | `addDocumentInformation` |
| POST | `/api/category/edit-document-information/{type}/{documentInformationId}` | `editDocumentInformation` |
| POST | `/api/category/delete-document-information/{type}/{documentInformationId}` | `deleteDocumentInformation` |
| GET | `/api/category/get-list-menu` | `getListMenu` |
| GET | `/api/category/get-detail-menu/{menuId}` | `getDetailMenu` |
| POST | `/api/category/add-menu` | `addMenu` |
| GET | `/api/category/find-parent-menu` | `findParentMenus` |
| POST | `/api/category/edit-menu/{menuId}` | `editMenu` |
| POST | `/api/category/lock-menu/{menuId}` | `lockMenu` |
| POST | `/api/category/delete-menu/{menuId}` | `deleteMenu` |
| GET | `/api/category/get-action` | `getActions` |
| POST | `/api/category/add-action` | `addAction` |
| GET | `/api/category/get-action-detail/{permissionBaseId}` | `getActionDetail` |
| POST | `/api/category/edit-action/{permissionBaseId}` | `editAction` |
| POST | `/api/category/delete-action/{permissionBaseId}` | `deleteAction` |
| POST | `/api/category/lock-action/{permissionBaseId}` | `lockAction` |
| GET | `/api/category/get-data` | `getData` |
| POST | `/api/category/add-data` | `addData` |
| GET | `/api/category/get-data-detail/{permissionDataId}` | `getDataDetail` |
| POST | `/api/category/edit-data/{permissionDataId}` | `editData` |
| POST | `/api/category/delete-data/{permissionDataId}` | `deleteData` |
| POST | `/api/category/lock-data/{permissionDataId}` | `lockData` |
| GET | `/api/category/get-list-meeting-resources` | `getListMeetingResource` |
| GET | `/api/category/get-meeting-resources-detail/{meetingResourceId}` | `getDetailMeetingResource` |
| POST | `/api/category/add-meeting-resources` | `addMeetingResource` |
| POST | `/api/category/edit-meeting-resources/{meetingResourceId}` | `editMeetingResource` |
| POST | `/api/category/delete-meeting-resources/{meetingResourceId}` | `deleteMeetingResources` |
| GET | `/api/category/get-list-video-conference-group` | `getListVideoConferenceGroup` |
| GET | `/api/category/get-video-conference-group-detail/{video-conference-group-id}` | `getVideoConferenceGroupDetail` |
| POST | `/api/category/add-video-conference-group` | `addVideoConferenceGroup` |
| POST | `/api/category/delete-video-conference-group/{video-conference-group-id}` | `deleteVideoConferenceGroup` |
| POST | `/api/category/edit-video-conference-group/{video-conference-group-id}` | `editVideoConferenceGroup` |

</details>

### CategoryGroupController (gen2) — base `/api/category-group`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/CategoryGroupController.java`

- Service: `CategoryGroupService`, `CategoryGroupServiceImpl`
- Repository (JPA): `CategoryCommonRepositoryJPA`, `CategoryGroupRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `CATEGORY_COMMON`, `CATEGORY_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/category-group/search` | `search` |
| GET | `/api/category-group/get-list-organization` | `getListOrganization` |
| POST | `/api/category-group/add-or-update` | `addOrUpdate` |
| POST | `/api/category-group/delete` | `delete` |

</details>

### HomeController (gen2) — base `/api/home`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/HomeController.java`

- Service: `BannerService`, `BannerServiceImpl`, `HomeService`, `HomeServiceImpl`, `ConfigDashboardServiceFactory`, `DocumentPermissionCacheService`
- DAO (SQL thuần): `CatalogBriefDAO`, `UserOrgMapDAO`
- Repository (JPA): `BannerRepositoryJPA`, `MenuRepositoryJPA`, `PermissionDashboardRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `BANNER`, `BRIEF`, `CATALOG_BRIEF`, `MENU`, `PERMISSION_DASHBOARD`, `SYS_ROLE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/home/config-user-dashboard` | `configUserDashboard` |
| GET | `/api/home/get-widgets-dashboard` | `getWidgetsDashBoard` |
| GET | `/api/home/get-default-dashboard` | `getDefaultDashboard` |
| GET | `/api/home/get-dashboard` | `getDashboard` |
| GET | `/api/home/get-config-dashboard` | `getConfigDashboard` |
| POST | `/api/home/config-dashboard` | `configDashboard` |
| GET | `/api/home/get-banner` | `getBanner` |
| GET | `/api/home/get-banner-image/{banner-id}` | `getBannerImage` |
| POST | `/api/home/search-all` | `searchAll` |

</details>

### IndexController (gen2) — base `{path:[^.]*}`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/IndexController.java`

- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| REQUEST | `{path:[^.]*}` | `index` |
| REQUEST | `{path:[^.]*}/{path:[^.]*}` | `redirect` |

</details>

### LanguageController (gen2) — base `/api/language`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/LanguageController.java`

- Service: `LanguageService`, `LanguageServiceImpl`
- Repository (JPA): `LanguageRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `LANGUAGE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/language/get-list-language` | `getListLanguage` |

</details>

### LogElkController (gen2) — base `/api/logs`, 12 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/LogElkController.java`

- Service: `KpiConfigService`, `SystemParameterCacheService`, `LogService`, `VipUserService`
- Repository (JPA): `SystemParameterRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `DATABASE`, `REDIS`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/logs/bulk` | `ingestBulk` |
| POST | `/api/logs` | `ingest` |
| GET | `/api/logs` | `search` |
| POST | `/api/logs/advance-search` | `advancedSearch` |
| POST | `/api/logs/feature-dashboard` | `featureDashboard` |
| POST | `/api/logs/feature-dashboard-api-sum` | `featureDashboardApiSum` |
| GET | `/api/logs/vip-users` | `getVipUsers` |
| GET | `/api/logs/kpi-config` | `getKpiConfig` |
| POST | `/api/logs/vip-users/evict-cache` | `evictVipUsersCache` |
| POST | `/api/logs/trace-breakdown` | `traceBreakdown` |
| POST | `/api/logs/export-daily-report` | `exportDailyReport` |
| POST | `/api/logs/advance-search-custom` | `advancedSearchCustom` |

</details>

### ManagerController (gen2) — base `/api/manager`, 56 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ManagerController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `ManagerService`, `ManagerServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `StaffDAO`, `StaffImageSignDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `ConfigSmsModuleRepositoryJPA`, `EmpCaDetailRepositoryJPA`, `EmpCaRepositoryJPA`, `FeedbackImageRepositoryJPA`, `FeedbackLogFileRepositoryJPA`, `FeedbackProcessRepositoryJPA`, `FeedbackRepositoryJPA`, `ImageOrgConfigRepositoryJPA`, `ImageOrgRepositoryJPA`, `MenuRepositoryJPA`, `NotificationRepositoryJPA`, `PermissionBaseRepositoryJPA`, `PermissionDataRepositoryJPA`, `PositionRepositoryJPA`, `RolePermissionBaseRepositoryJPA`, `RolePermissionDataRepositoryJPA`, `SmsBlackListRepositoryJPA`, `SysMenuRepositoryJPA`, `SysRoleMenuRepositoryJPA`, `SysRoleRepositoryJPA`, `SystemParameterRepositoryJPA`, `UserOrgMapRepositoryJPA`, `VhrOrgJPA`
- Bảng (ước lượng từ SQL/@Table): `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EMP_CA`, `EMP_CA_DETAIL`, `EXT_APP`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MENU`, `MESSAGE`, `NOTICE`, `NOTIFICATION`, `ORG_LEVEL`, `P12_CERT`, `PERMISSION_BASE`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `SMS_BLACK_LIST`, `SMS_MASTER`, `STAFF`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `SYSTEM_PARAMETER`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TEXT`, `TEXT_NOTE`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/manager/get-list-role` | `getListRole` |
| GET | `/api/manager/get-group-ceo-members` | `getGroupCeoMembers` |
| GET | `/api/manager/get-group-ceo-ids` | `getGroupCeoIds` |
| GET | `/api/manager/get-list-dept` | `getListDept` |
| GET | `/api/manager/get-dept-detail/{sysOrganizationId}` | `getDeptDetail` |
| GET | `/api/manager/get-list-emp-ca-dept` | `getListEmpCaDept` |
| GET | `/api/manager/get-list-image-org` | `getListImageOrg` |
| POST | `/api/manager/put-notification` | `putNotification` |
| GET | `/api/manager/get-list-user` | `getListUser` |
| GET | `/api/manager/get-list-user-last-sign-submissionform` | `getListUserLastSignSubmisionForm` |
| POST | `/api/manager/add-dept` | `addDept` |
| POST | `/api/manager/delete-emp-ca/{emp-ca-id}` | `deleteEmpCa` |
| GET | `/api/manager/get-user-detail/{employee-id}` | `getUserDetail` |
| POST | `/api/manager/lock-user/{employee-id}/{type}` | `lockUser` |
| POST | `/api/manager/insert-config-group` | `insertConfigGroup` |
| GET | `/api/manager/get-list-mysign/{account}` | `configCa` |
| GET | `/api/manager/get-list-org-config` | `getListOrgConfig` |
| GET | `/api/manager/get-list-emp-ca` | `getListEmpCa` |
| POST | `/api/manager/add-image-org` | `addImageOrg` |
| POST | `/api/manager/edit-image-org` | `editImageOrg` |
| POST | `/api/manager/add-emp-ca` | `addEmpCa` |
| POST | `/api/manager/edit-dept` | `editDept` |
| POST | `/api/manager/delete-dept/{sysOrganizationId}` | `deleteDept` |
| GET | `/api/manager/get-lst-param` | `getListSystemParameter` |
| POST | `/api/manager/add-param` | `addParam` |
| POST | `/api/manager/put-param/{systemParameterId}` | `putParam` |
| POST | `/api/manager/delete-param/{systemParameterId}` | `deleteParam` |
| POST | `/api/manager/add-user` | `addUser` |
| POST | `/api/manager/edit-user/{employee-id}` | `editUser` |
| GET | `/api/manager/get-list-menu` | `getListMenu` |
| GET | `/api/manager/get-list-all-menu/{roleId}` | `getListAllMenu` |
| GET | `/api/manager/get-list-all-action` | `getListAllAction` |
| GET | `/api/manager/get-list-role-action/{roleId}` | `getListMenuWithPermission` |
| GET | `/api/manager/get-list-role-data/{roleId}` | `getListMenuWithPermissionData` |
| GET | `/api/manager/get-list-all-data` | `getListAllDate` |
| POST | `/api/manager/update-role-permissions/{roleId}` | `updateRolePermissions` |
| GET | `/api/manager/get-role-detail/{role-id}` | `getRoleDetail` |
| POST | `/api/manager/add-role` | `addRole` |
| POST | `/api/manager/edit-role/{roleId}` | `editRole` |
| POST | `/api/manager/delete-role/{roleId}` | `deleteMenu` |
| POST | `/api/manager/update-sign-type-default/employee/{employee-id}/sign-type/{main-sign-type}` | `updateSignTypeDefault` |
| POST | `/api/manager/update-sign-type-default/organization/{sys-organization-id}/method-sign/{main-sign-type}` | `updateSignTypeOrgDefault` |
| POST | `/api/manager/update-sign-default/employee/{employee-id}/emp-ca/{emp-ca-id}` | `updateSignEmployeeDefault` |
| POST | `/api/manager/update-sign-default/organization/{sys-organization-id}/emp-ca/{emp-ca-id}` | `updateSignOrganizationDefault` |
| POST | `/api/manager/add-feedback` | `addFeedback` |
| GET | `/api/manager/get-feedback-by-id/{feedback-id}` | `getFeedbackById` |
| GET | `/api/manager/get-list-feedback` | `getListFeedback` |
| POST | `/api/manager/update-feedback-process/{feedbackId}` | `updateFeedbackProcess` |
| GET | `/api/manager/download-feedback-resource` | `downloadFeedbackResource` |
| GET | `/api/manager/download-feedback-attach` | `download` |
| GET | `/api/manager/get-list-position` | `getListPosition` |
| GET | `/api/manager/check-vhrorg-from-systemparameter/{vhr-org-id}` | `checkVhrOrgFromSystemParameter` |
| GET | `/api/manager/get-all-vhrorg-from-systemparameter` | `getAllVhrOrgFromSystemParameter` |
| GET | `/api/manager/get-list-proofreding-in-systemparam` | `getListProofreadingInSystemparam` |
| GET | `/api/manager/check-configuration-proofreading-from-systemparameter` | `checkConfigurationProofreadingFromSystemParameter` |
| GET | `/api/manager/checkConfigurationHomePageMode` | `checkConfigurationHomePageMode` |

</details>

### MenuController (gen2) — base `/api/menu`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MenuController.java`

- Service: `MenuService`, `MenuServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/menu/get-list-all-menu` | `getListAllMenu` |

</details>

### OfficeController (gen2) — base `/`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/OfficeController.java`

- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `UserDAO`
- Repository (JPA): `LogBackendJPA`
- Bảng (ước lượng từ SQL/@Table): `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `DIRECTOR_CONFIG`, `DOCUMENT`, `EXT_APP`, `GROUP_MAPPING`, `LOG_BACKEND`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `P12_CERT`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/login` | `saveTutorial` |
| GET | `/login` | `login` |
| GET | `/query` | `query` |
| POST | `/query` | `query` |
| GET | `/update` | `update` |
| POST | `/update` | `update` |
| GET | `/officesys` | `officesys` |
| POST | `/officesys` | `officesys` |
| POST | `/officesystest` | `officesystest` |

</details>

### PartyCategoryController (gen2) — base `/api/category-common`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/PartyCategoryController.java`

- Service: `PartyMasterDataService`, `PartyMasterDataServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/category-common/party-inherited` | `getInheritedCategories` |

</details>

### PartyOrgController (gen2) — base `/api/party-org`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/PartyOrgController.java`

- Service: `PartyMasterDataService`, `PartyMasterDataServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/party-org/tree` | `getTree` |
| GET | `/api/party-org/effective-tree` | `getEffectiveTree` |
| GET | `/api/party-org/{parentId}/children` | `getChildren` |
| GET | `/api/party-org/{organizationId}/descendant-ids` | `getDescendantIds` |
| GET | `/api/party-org/{organizationId}` | `getOrganization` |

</details>

### PartyPositionController (gen2) — base `/api/position`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/PartyPositionController.java`

- Service: `PartyMasterDataService`, `PartyMasterDataServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/position/party` | `getPartyPositions` |

</details>

### PersonalTreatmentStatusController (gen2) — base `/api/personal-treatment-status`, 3 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/PersonalTreatmentStatusController.java`

- Service: `PersonalTreatmentStatusService`, `PersonalTreatmentStatusServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/personal-treatment-status/get-total-document-kpi` | `getTotalDocumentKpi` |
| POST | `/api/personal-treatment-status/get-document-kpi` | `getDocumentKpi` |
| POST | `/api/personal-treatment-status/get-list-user-id` | `getListUserIdOfOrganization` |

</details>

### SystemDowntimeLogController (gen2) — base `/api/system-downtime-log`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/SystemDowntimeLogController.java`

- Service: `SystemDowntimeLogService`, `SystemDowntimeLogServiceImpl`
- Repository (JPA): `SystemDowntimeLogJPA`
- Bảng (ước lượng từ SQL/@Table): `SYSTEM_DOWNTIME_LOG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/system-downtime-log` | `create` |

</details>

### UserTableHeaderStateController (gen2) — base `/api/user-table-header-state`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/UserTableHeaderStateController.java`

- Service: `UserTableHeaderStateService`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/user-table-header-state/get-all-user-table-header-state` | `getAllUserTableHeaderStates` |
| POST | `/api/user-table-header-state/save-user-table-header-state` | `saveUserTableHeaderState` |
| POST | `/api/user-table-header-state/find-user-table-header-state-by-userId` | `findByUserId` |
| POST | `/api/user-table-header-state/save-table-header-state` | `saveTableHeaderState` |
| POST | `/api/user-table-header-state/find-user-table-header-state` | `findByUserIdViewTypeGroupType` |

</details>

### VersionControlController (gen2) — base `/api/version-control`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/VersionControlController.java`

- Service: `VersionControlService`, `VersionControlServiceImpl`
- DAO (SQL thuần): `TemplateDAO`
- Repository (JPA): `VersionControlFileJPA`, `VersionControlRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `DOCUMENT_TYPE`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `USER_ROLE`, `VERSION_CONTROL`, `VERSION_CONTROL_FILE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/version-control/save-versionControl` | `saveVersionControl` |
| POST | `/api/version-control/get-list-versionControl` | `getListVersionControl` |
| POST | `/api/version-control/get-list-file-versionControl` | `getListVersionControlFile` |
| POST | `/api/version-control/delete-versionControl` | `deleteVersionControl` |

</details>

### VhrOrgController (gen2) — base `/api/vhr-org`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/VhrOrgController.java`

- Service: `VhrOrgService`, `VhrOrgServiceImpl`
- DAO (SQL thuần): `UserRoleDAO`
- Repository (JPA): `SystemParameterRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ROLE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/vhr-org/get-vhrorg` | `getVhrOrg` |
| GET | `/api/vhr-org/get-list-org` | `getListVhrOrg` |
| GET | `/api/vhr-org/get-focus-tree` | `getFocusTree` |
| GET | `/api/vhr-org/get-list-org-parent-child-level-once` | `findByOrgParentId` |
| GET | `/api/vhr-org/get-org-leader` | `getOrgLeader` |
| GET | `/api/vhr-org/get-org-child-leader` | `findOrgChildLeader` |
| GET | `/api/vhr-org/get-org-kpi` | `getOrgKpi` |
| GET | `/api/vhr-org/get-org-info` | `getOrgInfo` |
| GET | `/api/vhr-org/get-list-org-level-one` | `getListOrgLevelOne` |
| GET | `/api/vhr-org/get-list-direct-child` | `getListDirectChild` |
| GET | `/api/vhr-org/get-list-child-all-level` | `getListChildAllLevel` |
| GET | `/api/vhr-org/get-info-org` | `getVhrOrgInfo` |
| POST | `/api/vhr-org/get-list-org-and-child-all-level` | `getListOrgAndChildAllLevel` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `CodeMasterFacade` | `ICodeMaster` | `CodeMasterService` | `CodeMasterJpaDao` | `CodeMaster (CODE_MASTER)` |
| `GroupManagerFacade` | `IGroupManager` | `GroupManagerService` | `GroupManagerJpaDao` | `Document (DOCUMENT)` |
| `LockStatusFacade` | `ILockStatus` | `LockStatusService` | `LockStatusJpaDao` | `LockStatus (LOCK_STATUS)` |
| `MapConfigFacade` | `IMapConfig` | `MapConfigService` | `MapConfigJpaDao` | `MapConfig (MAP_CONFIG)` |
| `PageIntroductionFacade` | `IPageIntroduction` | `PageIntroductionService` | `PageIntroductionJpaDao` | `PageIntroduction (PAGE_INTRODUCTION)` |
| `PrivateShortcutFacade` | `IPrivateShortcut` | `PrivateShortcutService` | `PrivateShortcutJpaDao` | `KiFormulaConfig (KI_FORMULA_CONFIG)` |
| `ResovleIssueFacade` | `IResovleIssue` | `ResovleIssueService` | `MissionJpaDao`, `TaskJpaDao` | `Mission (MISSION)`, `Task (TASK)` |
| `SurveyFacade` | `ISurvey` | `SurveyService` | `SurveyJpaDao` | — |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `AreaEntity`→`AREA`, `AreaLanguageEntity`→`AREA_LANGUAGE`, `BannerEntity`→`BANNER`, `CategoryCommonEntity`→`CATEGORY_COMMON`, `CategoryGroupEntity`→`CATEGORY_GROUP`, `ConfigSmsModuleEntity`→`CONFIG_SMS_MODULE`, `ConfigSmsOrgEntity`→`CONFIG_SMS_ORG`, `CvGroupEntity`→`CV_GROUP`, `CvPriorityEntity`→`CV_PRIORITY`, `CvPriorityLanguageEntity`→`CV_PRIORITY_LANGUAGE`, `FeedbackEntity`→`FEEDBACK`, `FeedbackLogFileEntity`→`FEEDBACK_LOG_FILE`, `FeedbackProcessEntity`→`FEEDBACK_PROCESS`, `GroupApplyEntity`→`GROUP_APPLY`, `ImageOrgConfigEntity`→`IMAGE_ORG_CONFIG`, `ImageOrgEntity`→`IMAGE_ORG`, `LanguageEntity`→`LANGUAGE`, `LogBackendEntity`→`LOG_BACKEND`, `LogTranstionSignEntity`→`LOG_TRANSTION_SIGN`, `MenuEntity`→`MENU`, `MessageEntity`→`MESSAGE`, `MissionStatusEntity`→`MISSION_STATUS`, `OrgCombinationMapEntity`→`ORG_COMBINATION_MAP`, `OrgLevelEntity`→`ORG_LEVEL`, `OrgMenuEntity`→`ORG_MENU`, `PersonalCategory`→`PERSONAL_CATEGORY`, `SecurityTypeEntity`→`SECURITY_TYPE`, `SecurityTypeLanguageEntity`→`SECURITY_TYPE_LANGUAGE`, `SourceMapEntity`→`SOURCE_MAP`, `StaffInCvGroupEntity`→`STAFF_IN_CV_GROUP`, `StatusEntity`→`STATUS`, `SysRoleEntity`→`SYS_ROLE`, `SysRoleMenuEntity`→`SYS_ROLE_MENU`, `SystemDowntimeLog`→`SYSTEM_DOWNTIME_LOG`, `SystemParameterEntity`→`SYSTEM_PARAMETER`, `TimeZoneLocalEntity`→`TIME_ZONE_LOCAL`, `UserOrgMapEntity`→`USER_ORG_MAP`, `UserRoleEntity`→`USER_ROLE`, `UserTableHeaderStateEntity`→`USER_TABLE_HEADER_STATE`, `UserTokensEntity`→`USER_TOKENS`, `VersionControlEntity`→`VERSION_CONTROL`, `VersionControlFileEntity`→`VERSION_CONTROL_FILE`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `AlertFeedback`→`ALERT_FEEDBACK`, `Attach`→`Attach`, `Category`→`REQUISITION`, `ChatMessage`→`Chat_Message`, `CodeMaster`→`CODE_MASTER`, `EmailConfirm`→`EMAIL_CONFIRM`, `EmailReceive`→`Email_Receive`, `EntityActionLogService`→`ACTION_LOG_SERVICE`, `GroupDetail`→`GROUP_DETAIL`, `GroupManager`→`GROUP_MANAGER`, `ImageOrg`→`IMAGE_ORG`, `ImageOrgConfig`→`IMAGE_ORG_CONFIG`, `LabourContractType`→`LABOUR_CONTRACT_TYPE`, `LockStatus`→`LOCK_STATUS`, `LongLeave`→`LONG_LEAVE`, `MapConfig`→`MAP_CONFIG`, `MappingResovle`→`MAPPING_RESOVLE`, `OrgCombinationMap`→`ORG_COMBINATION_MAP`, `PageIntroduction`→`PAGE_INTRODUCTION`, `Position`→`POSITION`, `PrimaryVariable`→`PRIMARY_VARIABLE`, `PrivateShortcut`→`PRIVATE_SHORTCUT`, `ResovleIssue`→`RESOVLE_ISSUE`, `RoleMenu`→`ROLE_MENU`, `RoleScopeData`→`ROLE_SCOPE_DATA`, `ScopeType`→`SCOPE_TYPE`, `SourceMap`→`SOURCE_MAP`, `Survey`→`SURVEY`, `SurveyMap`→`SURVEY_MAP`, `SyncHistory`→`SYNC_HISTORY`, `SysCat`→`SYS_CAT`, `SysCatType`→`SYS_CAT_TYPE`, `SysMenu`→`SYS_MENU`, `SysOperation`→`SYS_OPERATION`, `SysOrganization`→`VHR_ORG`, `SysParameter`→`SYSTEM_PARAMETER`, `SysResource`→`SYS_RESOURCE`, `SysRole`→`SYS_ROLE`, `SysUser`→`VHR_EMPLOYEE`, `TimeZoneLocal`→`TIME_ZONE_LOCAL`, `UserOrgMap`→`USER_ORG_MAP`, `UserRole`→`USER_ROLE`, `UserRoleSync`→`USER_ROLE`, `UserScopeData`→`USER_SCOPE_DATA`, `WorkingProcess`→`WORK_PROCESS`

**Tổng hợp bảng chạm tới**: `ACTION_LOG_SERVICE`, `ALERT_FEEDBACK`, `AREA`, `AREA_LANGUAGE`, `ATTACH`, `ATTACH_HISTORY`, `ATTACH_PARTNER`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `Attach`, `BANNER`, `BASE`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CATEGORY_GROUP`, `CHART_AGREEMENT`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_TASK`, `CHILD_CNT`, `CLOUD_DEVICE_CERT`, `CODE_MASTER`, `CONFIG_ORG_RATING`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_PROCESS_IN`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `CV_PRIORITY_LANGUAGE`, `Chat_Message`, `DATABASE`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_LANGUAGE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMAIL_CONFIRM`, `EMPLOYEE_TYPE_PROCESS`, `EMP_CA`, `EMP_CA_DETAIL`, `EMP_CLOUD_CA`, `EXT_APP`, `Email_Receive`, `FAVOURITE`, `FEEDBACK`, `FEEDBACK_IMAGE`, `FEEDBACK_LOG_FILE`, `FEEDBACK_PROCESS`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `FLOW`, `FLOW_GROUP_TYPE`, `GROUP_APPLY`, `GROUP_DETAIL`, `GROUP_IN_CV_GROUP`, `GROUP_MANAGER`, `GROUP_MAPPING`, `GROUP_SIGN`, `HISTORY_CHANGE_SIGN`, `HOME_WIDGET`, `IMAGE`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `INTERNAL_DOC_DETAIL`, `INTERNAL_DOC_SEND_XML`, `KI_FORMULA_CONFIG`, `LABOUR_CONTRACT_TYPE`, `LANGUAGE`, `LOCK_STATUS`, `LOG_BACKEND`, `LOG_TRANSTION_SIGN`, `LONG_LEAVE`, `LSTROOTEMP`, `MAPPING_RESOVLE`, `MAP_CONFIG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MENU`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE`, `NODE_ACTION`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA`, `ORG_CRITERIA_CONFIG`, `ORG_CRITERIA_HISTORY`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_RATING_TOTAL`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORG_MENU`, `ORG_SYS_MENU`, `ORIENTATION`, `P12_CERT`, `PAGE_INTRODUCTION`, `PASS`, `PERFORM_ORG_AREA`, `PERMISSION_BASE`, `PERMISSION_DASHBOARD`, `PERMISSION_DATA`, `PERSONAL_CATEGORY`, `POSITION`, `PRIMARY_VARIABLE`, `PRIVATE_SHORTCUT`, `READ_NOTICE_HISTORY`, `REDIS`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `REQUISITION`, `RESOVLE_ISSUE`, `ROLE_IN_CV_GROUP`, `ROLE_MENU`, `ROLE_PERMISSION_BASE`, `ROLE_PERMISSION_DATA`, `ROLE_SCOPE_DATA`, `SCOPE_TYPE`, `SECURITY_TYPE`, `SECURITY_TYPE_LANGUAGE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STATUS`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SURVEY`, `SURVEY_MAP`, `SYNC_HISTORY`, `SYSTEM_DOWNTIME_LOG`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_CAT`, `SYS_CAT_TYPE`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_OPERATION`, `SYS_RESOURCE`, `SYS_ROLE`, `SYS_ROLE_MENU`, `TASK`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PARTNER`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TOP_ORG`, `TOP_PERSONAL`, `TO_DATE`, `USER_ACTIVITY_LOG`, `USER_ORG_MAP`, `USER_ROLE`, `USER_SCOPE_DATA`, `USER_TABLE_HEADER_STATE`, `USER_TOKENS`, `VERSION_CONTROL`, `VERSION_CONTROL_FILE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `WORK_PROCESS`
