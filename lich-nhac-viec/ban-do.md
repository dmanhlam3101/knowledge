# Bản đồ hệ thống — Nhắc việc (MỚI), thông báo, SMS, định hướng, nắm tình hình

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 19 màn hình, 1 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `config/sms/smsConfigOrg.zul` | `vm.config.sms.SmsConfigOrgVM` | `ConfigBusiness` | — | BE |
| `config/smsController.zul` | `vm.config.SmsControllerVM` | `ConfigBusiness` | — | BE |
| `grasp_situation/graspSituation.zul` | `vm.graspSituation.GraspSituationVM` | `CatalogBriefBusiness`, `CategoryCommonBusiness`, `DocumentBusiness`, `GraspSituationBusiness` | — | BE |
| `grasp_situation/popupUpdateToGraspSituation.zul` | `vm.graspSituation.PopupUpdateToGraspSituationVM` | — | — | — |
| `notice/notice.zul` | `vm.notice.NoticeVM` | — | `INotice` | LEGACY |
| `notice/noticeContentEdit.zul` | `vm.notice.NoticeContentEditVM` | — | — | — |
| `notice/notice_detail.zul` | `vm.notice.NoticeDetailVM` | — | — | — |
| `orientation/orientation.zul` | `vm.orientation.OrientationVM` | `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `OrientationBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `orientation/orientationPP.zul` | `vm.orientation.OrientationVM` | `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `OrientationBusiness` | `ICommonVoffice`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `reminder/reminder.zul` | `vm.reminder.ReminderVM` | `HomeBusiness`, `ReminderBusiness`, `VhrEmployeeBusiness` | — | BE |
| `reminder/reminderAssigneeLookup.zul` | `vm.reminder.ReminderAssigneeLookupVM` | `ReminderBusiness` | — | BE |
| `reminder/reminder_add_modal.zul` | `vm.reminder.ReminderVM` | `HomeBusiness`, `ReminderBusiness`, `VhrEmployeeBusiness` | — | BE |
| `reminder/reminder_approve.zul` | `vm.reminder.ReminderActionVM` | `ReminderBusiness` | — | BE |
| `reminder/reminder_reply.zul` | `vm.reminder.ReminderReplyVM` | `ReminderBusiness`, `VhrEmployeeBusiness` | — | BE |
| `reminder/reminder_report.zul` | `vm.reminder.ReminderReportVM` | `ReminderBusiness` | — | BE |
| `reminder/reminder_viewDetail.zul` | `vm.reminder.ReminderViewDetailVM` | `ReminderBusiness` | — | BE |
| `timeConfig/timeConfig.zul` | `vm.timeConfig.TimeConfigVM` | — | `ITimeConfig` | LEGACY |
| `widgets/popupSelectDocumentForReminder.zul` | `widget.PopupSelectDocumentForReminderVM` | `AnswerDocumentBusiness`, `DocumentBusiness` | — | BE |
| `widgets/sourceLookupOrientation.zul` | `widget.SourceLookupOrientationVM` | — | `IOrientation` | LEGACY |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `util.vm.VoOrientationUtils` | — | — | — |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### GraspSituationBusiness

`web-spring/src/main/java/com/voffice/service/business/GraspSituationBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.document-informality.count-read` | `/api/document-informality/count-read` | `DocumentInformalityController.countReadPost` | gen2 |
| `api.document-informality.create-or-update` | `/api/document-informality/create-or-update` | `DocumentInformalityController.createOrUpdate` | gen2 |
| `api.document-informality.delete` | `/api/document-informality/delete` | `DocumentInformalityController.deleteDocument` | gen2 |
| `api.document-informality.detail` | `/api/document-informality/detail` | `DocumentInformalityController.getDetail` | gen2 |
| `api.document-informality.get-group-doc-lead-type` | `/api/document-informality/get-group-doc-lead-type` | `DocumentInformalityController.getGroupDocumentLeadType` | gen2 |
| `api.document-informality.get-list-file-encrypt-map` | `/api/document-informality/get-list-file-encrypt-map` | `DocumentInformalityController.findDocFileEncryptByDocId` | gen2 |
| `api.document-informality.get-permission-view-file.doc` | `/api/document-informality/get-permission-view-file/doc` | `DocumentInformalityController.getPermissionViewFileByDocIdAndAttachId` | gen2 |
| `api.document-informality.get-permission-view-file.doc-informality` | `/api/document-informality/get-permission-view-file/doc-informality` | `DocumentInformalityController.getPermissionViewFileByDocInformalityIdAndAttachId` | gen2 |
| `api.document-informality.insert-permission-for-supplier` | `/api/document-informality/insert-permission-for-supplier` | `DocumentInformalityController.insertPermissionForSupplier` | gen2 |
| `api.document-informality.mark-as-read` | `/api/document-informality/mark-as-read` | `DocumentInformalityController.markAsRead` | gen2 |
| `api.document-informality.search` | `/api/document-informality/search` | `DocumentInformalityController.search` | gen2 |
| `api.document-informality.send` | `/api/document-informality/send` | `DocumentInformalityController.send` | gen2 |

### NotificationBusiness

`web-spring/src/main/java/com/voffice/service/business/NotificationBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `NotificationAction.countNotificationUnread` | `/NotificationAction/countNotificationUnread` | `NotificationAction.countNotificationUnread` | gen1 |
| `NotificationAction.getNotice` | `/NotificationAction/getNotice` | `NotificationAction.getNotice` | gen1 |
| `NotificationAction.getNotifications` | `/NotificationAction/getNotifications` | `NotificationAction.getNotifications` | gen1 |
| `NotificationAction.searchNotification` | `/NotificationAction/searchNotification` | `NotificationAction.searchNotification` | gen1 |
| `NotificationAction.updateIsRead` | `/NotificationAction/updateIsRead` | `NotificationAction.updateIsRead` | gen1 |
| `NotificationAction.updateIsReadByObjectID` | `/NotificationAction/updateIsReadByObjectID` | `NotificationAction.updateIsReadByObjectID` | gen1 |
| `NotificationAction.updateIsReadListNotification` | `/NotificationAction/updateIsReadListNotification` | `NotificationAction.updateIsReadListNotification` | gen1 |

### OrientationBusiness

`web-spring/src/main/java/com/voffice/service/business/OrientationBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Meeting.getListFileAttachment` | `/Meeting/getListFileAttachment` | `MettingResource.getListFileAttachment` | gen1 |
| `Meeting.getListOrganizationsAssign` | `/Meeting/getListOrganizationsAssign` | `MettingResource.getListOrganizationsAssign` | gen1 |
| `Meeting.getMissionByMeetingId` | `/Meeting/getMissionByMeetingId` | `MettingResource.getMissionByMeetingId` | gen1 |
| `Orientation.addOrEditOrientation` | `/Orientation/addOrEditOrientation` | `OrientationAction.addOrEditOrientation` | gen1 |
| `Orientation.deleteOrientation` | `/Orientation/deleteOrientation` | `OrientationAction.deleteOrientation` | gen1 |
| `Orientation.getListOrientReceiveOrg` | `/Orientation/getListOrientReceiveOrg` | `OrientationAction.getListOrientReceiveOrg` | gen1 |
| `Orientation.getListOrientation` | `/Orientation/getListOrientation` | `OrientationAction.getListOrientation` | gen1 |
| `missionAction.getListSourceMap` | `/missionAction/getListSourceMap` | `MissionAction.getListSourceMap` | gen1 |
| `staffAction.getLeaderByOrg` | `/staffAction/getLeaderByOrg` | `StaffAction.getLeaderByOrg` | gen1 |

### ReminderBusiness

`web-spring/src/main/java/com/voffice/service/business/ReminderBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `reminders.approve` | `/reminders/approve` | `ReminderController.approveReminders` | gen2 |
| `reminders.cancelReply` | `/reminders/cancelReply` | `IndexController.redirect` | gen2 |
| `reminders.countReminderReportByCondition` | `/reminders/countReminderReportByCondition` | `ReminderController.countReminderReportByCondition` | gen2 |
| `reminders.delete` | `/reminders/delete` | `ReminderController.deleteReminder` | gen2 |
| `reminders.findReminderReportByCondition` | `/reminders/findReminderReportByCondition` | `ReminderController.findReminderReportByCondition` | gen2 |
| `reminders.getDetail` | `/reminders/getDetail` | `ReminderController.getReminderDetailInfo` | gen2 |
| `reminders.getDocumentRelationForReminder` | `/reminders/getDocumentRelationForReminder` | `ReminderController.getDocumentRelationForReminder` | gen2 |
| `reminders.getDraftDetail` | `/reminders/getDraftDetail` | `ReminderController.getDraftReminderDetail` | gen2 |
| `reminders.getDraftReplyRemindersByDocumentIds` | `/reminders/getDraftReplyRemindersByDocumentIds` | `ReminderController.getDraftReplyRemindersByDocumentIds` | gen2 |
| `reminders.getListOrgForTransfer` | `/reminders/getListOrgForTransfer` | `ReminderController.getListOrgForTransfer` | gen2 |
| `reminders.getReminderHistory` | `/reminders/getReminderHistory` | `ReminderController.getReminderHistory` | gen2 |
| `reminders.getReminderReport` | `/reminders/getReminderReport` | `IndexController.redirect` | gen2 |
| `reminders.insertOrUpdate` | `/reminders/insertOrUpdate` | `ReminderController.insertOrUpdateReminders` | gen2 |
| `reminders.remindAgain` | `/reminders/remindAgain` | `ReminderController.remindAgain` | gen2 |
| `reminders.reply` | `/reminders/reply` | `ReminderController.replyReminders` | gen2 |
| `reminders.search` | `/reminders/search` | `ReminderController.searchReminders` | gen2 |
| `reminders.updateNewReplyAssignee` | `/reminders/updateNewReplyAssignee` | `IndexController.redirect` | gen2 |
| `reminders.updateNewReplyAssigneeAndFollowers` | `/reminders/updateNewReplyAssigneeAndFollowers` | `ReminderController.updateNewReplyAssignee` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### NotificationAction (gen1) — base `/NotificationAction`, 7 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/NotificationAction.java`

- Logic (gen-1 `controler/`): `NotificationController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `NotificationDAO`
- Repository (JPA): `TextRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `NOTICE`, `NOTIFICATION`, `READ_NOTICE_HISTORY`, `TEXT`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/NotificationAction/getNotifications` | `getNotifications` |
| POST | `/NotificationAction/getNotice` | `getNotice` |
| POST | `/NotificationAction/countNotificationUnread` | `countNotificationUnread` |
| POST | `/NotificationAction/updateIsRead` | `updateIsRead` |
| POST | `/NotificationAction/updateIsReadByObjectID` | `updateIsReadByObjectID` |
| POST | `/NotificationAction/searchNotification` | `searchNotification` |
| POST | `/NotificationAction/updateIsReadListNotification` | `updateIsReadListNotification` |

</details>

### OrientationAction (gen1) — base `/Orientation`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/OrientationAction.java`

- Logic (gen-1 `controler/`): `OrientationController`, `LogActionControler`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `LogActionDao`, `OrientationDAO`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `ORIENTATION`, `ORIENT_RECEIVE_ORG`, `SOURCE_MAP`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Orientation/getListOrientation` | `getListOrientation` |
| POST | `/Orientation/deleteOrientation` | `deleteOrientation` |
| POST | `/Orientation/addOrEditOrientation` | `addOrEditOrientation` |
| POST | `/Orientation/getListOrientReceiveOrg` | `getListOrientReceiveOrg` |

</details>

### SmsInterceptAction (gen1) — base `/SmsInterceptAction`, 3 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SmsInterceptAction.java`

- Logic (gen-1 `controler/`): `SmsInterceptController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `OrgDAO`, `SmsInterceptDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `EMPLOYEE_TYPE_PROCESS`, `IMAGE_ORG`, `SMS_BLACK_LIST`, `STAFF_GROUP_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/SmsInterceptAction/getListModulSms` | `getListModulSms` |
| POST | `/SmsInterceptAction/getListModulInterceptSmsOfUserId` | `getListModulInterceptSmsOfUserId` |
| POST | `/SmsInterceptAction/addOrRemoveInterceptByUser` | `addOrRemoveInterceptByUser` |

</details>

### ReminderController (gen2) — base `/reminders`, 16 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ReminderController.java`

- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/reminders/search` | `searchReminders` |
| POST | `/reminders/getListOrgForTransfer` | `getListOrgForTransfer` |
| POST | `/reminders/insertOrUpdate` | `insertOrUpdateReminders` |
| POST | `/reminders/reply` | `replyReminders` |
| POST | `/reminders/approve` | `approveReminders` |
| POST | `/reminders/delete` | `deleteReminder` |
| POST | `/reminders/findReminderReportByCondition` | `findReminderReportByCondition` |
| POST | `/reminders/countReminderReportByCondition` | `countReminderReportByCondition` |
| POST | `/reminders/getDetail` | `getReminderDetailInfo` |
| POST | `/reminders/getDraftDetail` | `getDraftReminderDetail` |
| POST | `/reminders/updateNewReplyAssigneeAndFollowers` | `updateNewReplyAssignee` |
| POST | `/reminders/getDocumentRelationForReminder` | `getDocumentRelationForReminder` |
| POST | `/reminders/getDraftReplyRemindersByDocumentIds` | `getDraftReplyRemindersByDocumentIds` |
| POST | `/reminders/getCountReminderDashboard` | `getCountReminderDashboard` |
| POST | `/reminders/remindAgain` | `remindAgain` |
| POST | `/reminders/getReminderHistory` | `getReminderHistory` |

</details>

### SMSInterceptController (gen2) — base `/api/smsIntercept`, 2 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/SMSInterceptController.java`

- Service: `SMSInterceptService`, `SMSInterceptServiceImpl`
- Repository (JPA): `ConfigSmsModuleRepositoryJPA`, `ConfigSmsOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/smsIntercept/updateSmsInterceptConfigByOrg` | `updateSmsInterceptConfigByOrg` |
| POST | `/api/smsIntercept/getListModulInterceptSmsOfOrgId/{orgId}` | `getListModulInterceptSmsOfOrg` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `MultimediaNotificationFacade` | `IMultimediaNotification` | `MultimediaNotificationService` | `AlertJpaDao`, `EmailMasterJpaDao`, `SmsMasterJpaDao`, `TaskJpaDao` | `Alert (ALERT)`, `EmailMaster (EMAIL_MASTER)`, `SmsMaster (SMS_MASTER)`, `Task (TASK)` |
| `NoticeFacade` | `INotice` | `NoticeService` | `NoticeJpaDao` | `Notice (NOTICE)` |
| `OrientationFacade` | `IOrientation` | `OrientationService` | `OrientationJpaDao` | — |
| `TimeConfigFacade` | `ITimeConfig` | `TimeConfigService` | `TimeConfigJpaDao` | `TimeConfig (TIME_CONFIG)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `NotificationEntity`→`NOTIFICATION`, `ReminderDocumentRelationEntity`→`REMINDER_DOCUMENT_RELATIONS`, `ReminderEntity`→`REMINDER`, `ReminderFollowerEntity`→`REMINDER_FOLLOWERS`, `ReminderHistoryEntity`→`REMINDER_HISTORY`, `ReminderReplyEntity`→`REMINDER_REPLY`, `SmsBlackListEntity`→`SMS_BLACK_LIST`, `SmsMasterEntity`→`SMS_MASTER`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Alert`→`ALERT`, `Notice`→`NOTICE`, `NoticeDetail`→`NOTICE_DETAIL`, `OrientOrgMap`→`ORIENT_RECEIVE_ORG`, `Orientation`→`ORIENTATION`, `ReadNoticeHistory`→`READ_NOTICE_HISTORY`, `Reminder`→`REMINDER`, `ReminderDocumentRelation`→`REMINDER_DOCUMENT_RELATIONS`, `ReminderReply`→`REMINDER_REPLIES`, `SmsDetail`→`SMS_DETAIL`, `SmsMaster`→`SMS_MASTER`, `TimeConfig`→`TIME_CONFIG`

**Tổng hợp bảng chạm tới**: `ACTION_LOG_SERVICE`, `ALERT`, `AREA`, `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `EMAIL_MASTER`, `EMPLOYEE_TYPE_PROCESS`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `IMAGE_ORG`, `NOTICE`, `NOTICE_DETAIL`, `NOTIFICATION`, `ORIENTATION`, `ORIENT_RECEIVE_ORG`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_FOLLOWERS`, `REMINDER_HISTORY`, `REMINDER_REPLIES`, `REMINDER_REPLY`, `SMS_BLACK_LIST`, `SMS_DETAIL`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF_GROUP_ROLE`, `TASK`, `TEXT`, `TIME_CONFIG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`
