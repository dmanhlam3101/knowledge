# Entity ↔ bảng DB

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).

## BE gen-2 (`com.viettel.office.entities`)

| Entity | Bảng | Phân hệ | Repository |
|---|---|---|---|
| `AppMobileEntity` | `APP_MOBILE` | tich-hop | `AppMobileRepositoryJPA` |
| `AreaEntity` | `AREA` | he-thong | `AreaRepositoryJPA` |
| `AreaLanguageEntity` | `AREA_LANGUAGE` | he-thong | `AreaLanguageRepositoryJPA` |
| `AttachEntity` | `ATTACH` | _chung | `AttachRepositoryJPA` |
| `AttachHistoryEntity` | `ATTACH_HISTORY` | _chung | `AttachHistoryRepositoryJPA` |
| `AttachTemplateEntity` | `ATTACH_TEMPLATE` | tai-lieu-mau | `AttachTemplateRepositoryJPA` |
| `BannerEntity` | `BANNER` | he-thong | `BannerRepositoryJPA` |
| `BriefDocumentEntity` | `BRIEF_DOCUMENT` | ho-so-cong-viec | `BriefDocumentRepositoryJPA` |
| `BriefDocumentMapEntity` | `BRIEF_DOCUMENT_MAP` | ho-so-cong-viec | `BriefDocumentMapRepositoryJPA` |
| `BriefEntity` | `BRIEF` | ho-so-cong-viec | `BriefEntityRepositoryJPA` |
| `BriefMultimediaEntity` | `BRIEF_MULTIMEDIA` | ho-so-cong-viec | `BriefMultimediaJPA` |
| `BriefMultimediaFileEntity` | `BRIEF_MULTIMEDIA_FILE` | ho-so-cong-viec | `BriefMultimediaFileJPA` |
| `BriefShareEntity` | `BRIEF_SHARE` | ho-so-cong-viec | `BriefShareEntityRepositoryJPA` |
| `BriefSubmitAttachFileEntity` | `BRIEF_SUBMIT_ATTACH_FILE` | ho-so-cong-viec | `BriefSubmitAttachFileEntityRepositoryJPA` |
| `BriefSubmitDocumentEntity` | `BRIEF_SUBMIT_DOCUMENT` | ho-so-cong-viec | `BriefSubmitDocumentEntityRepositoryJPA` |
| `BriefSubmitRequestEntity` | `BRIEF_SUBMIT_REQUEST` | ho-so-cong-viec | `BriefSubmitRequestEntityRepositoryJPA` |
| `CaSupplierEntity` | `CA_SUPPLIER` | ky-so | `CaSupplierRepositoryJPA` |
| `CatalogingBriefFileEntity` | `CATALOGING_BRIEF_FILE` | ho-so-cong-viec | `CatalogingBriefFileRepositoryJPA` |
| `CategoryCommonEntity` | `CATEGORY_COMMON` | he-thong | `CategoryCommonRepositoryJPA` |
| `CategoryGroupEntity` | `CATEGORY_GROUP` | he-thong | `CategoryGroupRepositoryJPA` |
| `ConfigSmsModuleEntity` | `CONFIG_SMS_MODULE` | he-thong | `ConfigSmsModuleRepositoryJPA` |
| `ConfigSmsOrgEntity` | `CONFIG_SMS_ORG` | he-thong | `ConfigSmsOrgRepositoryJPA` |
| `ConnectDocumentEntity` | `CONNECT_DOCUMENT` | van-ban/lien-thong | `ConnectDocumentRepositoryJPA` |
| `ConnectProcessInEntity` | `CONNECT_PROCESS_IN` | van-ban/lien-thong | `ConnectProcessInRepositoryJPA` |
| `ConnectVhrEntity` | `CONNECT_VHR` | tich-hop | `ConnectVhrRepositoryJPA` |
| `CvGroupEntity` | `CV_GROUP` | he-thong | `CvGroupRepositoryJPA` |
| `CvPriorityEntity` | `CV_PRIORITY` | he-thong | `CvPriorityRepositoryJPA` |
| `CvPriorityLanguageEntity` | `CV_PRIORITY_LANGUAGE` | he-thong | `CvPriorityLanguageRepositoryJPA` |
| `DocDailySummary` | `DOC_DAILY_SUMMARY` | kpi-danh-gia | `DocDailySummaryRepositoryJPA` |
| `DocumentChatEntity` | `DOCUMENT_CHAT` | van-ban/quan-ly-chung | `DocumentChatRepositoryJPA` |
| `DocumentCopyHistory` | `DOCUMENT_COPY_HISTORY` | van-ban/quan-ly-chung | `DocumentCopyHistoryJPA` |
| `DocumentHistoryLogEntity` | `DOCUMENT_HISTORY_LOG` | van-ban/quan-ly-chung | `DocumentHistoryLogJPA` |
| `DocumentInCvGroupEntity` | `DOCUMENT_IN_CV_GROUP` | van-ban/den | `DocumentInCvGroupRepositoryJPA` |
| `DocumentInFileEntity` | `DOCUMENT_IN_FILE` | van-ban/den | `DocumentInFileJPA` |
| `DocumentInGroupEntity` | `DOCUMENT_IN_GROUP` | van-ban/den | `DocumentInGroupRepositoryJPA` |
| `DocumentInListRequestEntity` | `DOCUMENT_IN_LIST_REQUEST` | van-ban/den | `DocumentInListRequestRepositoryJPA` |
| `DocumentInStaffEntity` | `DOCUMENT_IN_STAFF` | van-ban/den | `DocumentInStaffRepositoryJPA` |
| `DocumentInformality` | `DOCUMENT_INFORMALITY` | lich-nhac-viec | `DocumentInformalityRepositoryJPA` |
| `DocumentInformalityAttach` | `DOCUMENT_INFORMALITY_ATTACH` | lich-nhac-viec | `DocumentInformalityAttachRepositoryJPA` |
| `DocumentInformalityGroupEntity` | `DOCUMENTINFORMALITYGROUPENTITY` | lich-nhac-viec | `DocumentInformalityGroupRepositoryJPA` |
| `DocumentInformalityStaff` | `DOCUMENT_INFORMALITY_STAFF` | lich-nhac-viec | `DocumentInformalityStaffRepositoryJPA` |
| `DocumentLeaderCommentEntity` | `DOCUMENT_LEADER_COMMENT` | _chung | `DocumentLeaderCommentRepositoryJPA` |
| `DocumentProcessEntity` | `DOCUMENT_PROCESS` | van-ban/quan-ly-chung | `DocumentProcessRepositoryJPA` |
| `DocumentProposalDetailEntity` | `DOCUMENT_PROPOSAL_DETAIL` | van-ban/quan-ly-chung | `DocumentProposalDetailJpa` |
| `DocumentProposalEntity` | `DOCUMENT_PROPOSAL` | van-ban/quan-ly-chung | `DocumentProposalJpa` |
| `DocumentReceiveMapEntity` | `DOCUMENT_RECEIVE_MAP` | van-ban/den | `DocumentReceiveMapRepositoryJPA` |
| `DocumentScopeEntity` | `DOCUMENT_SCOPE` | van-ban/quan-ly-chung | `DocumentScopeRepository` |
| `DocumentScopeRefEntity` | `DOCUMENT_SCOPE_REF` | van-ban/quan-ly-chung | `DocumentScopeRefRepository` |
| `DocumentTemplateEntity` | `DOCUMENT_TEMPLATE` | tai-lieu-mau | `DocumentTemplateRepositoryJPA` |
| `DocumentTypeEntity` | `DOCUMENT_TYPE` | van-ban/quan-ly-chung | `DocumentTypeRepositoryJPA` |
| `DocumentTypeLanguageEntity` | `DOCUMENT_TYPE_LANGUAGE` | van-ban/quan-ly-chung | `DocumentTypeLanguageRepositoryJPA` |
| `DocumentTypeOrgEntity` | `DOCUMENT_TYPE_ORG` | van-ban/quan-ly-chung | `DocumentTypeOrgRepositoryJPA` |
| `ElasticDocumentPrivate` | `ELASTIC_DOCUMENT_PRIVATE` | tich-hop | `ElasticDocumentPrivateRepositoryJPA` |
| `ElasticDocumentPublic` | `ELASTIC_DOCUMENT_PUBLIC` | tich-hop | `ElasticDocumentPublicRepositoryJPA` |
| `EmpCaDetailEntity` | `EMP_CA_DETAIL` | ky-so | `EmpCaDetailRepositoryJPA` |
| `EmpCaEntity` | `EMP_CA` | ky-so | `EmpCaRepositoryJPA` |
| `EntitySubmissionFormEditHistory` | `SUBMISSION_FORM_EDIT_HISTORY` | phieu-trinh | — |
| `ExtAppApiEntity` | `EXT_APP_API` | tich-hop | `ExtAppApiEntityRepositoryJPA` |
| `ExtAppEntity` | `EXT_APP` | tich-hop | `ExtAppEntityRepositoryJPA` |
| `ExtDocumentAccessLogEntity` | `EXT_DOCUMENT_ACCESS_LOG` | tich-hop | `ExtDocumentAccessLogJPA` |
| `ExtDocumentEntity` | `EXT_DOCUMENT` | tich-hop | `ExtDocumentJPA` |
| `ExtShareConfigEntity` | `EXT_SHARE_CONFIG` | tich-hop | `ExtShareConfigJPA`, `ExtShareConfigRepositoryJPA` |
| `ExtShareScopeEntity` | `EXT_SHARE_SCOPE` | tich-hop | `ExtShareScopeJPA` |
| `FeedbackEntity` | `FEEDBACK` | he-thong | `FeedbackRepositoryJPA` |
| `FeedbackImageEntity` | `FEEDBACK_IMAGE` | _chung | `FeedbackImageRepositoryJPA` |
| `FeedbackLogFileEntity` | `FEEDBACK_LOG_FILE` | he-thong | `FeedbackLogFileRepositoryJPA` |
| `FeedbackProcessEntity` | `FEEDBACK_PROCESS` | he-thong | `FeedbackProcessRepositoryJPA` |
| `FileAttachmentEntity` | `FILE_ATTACHMENT` | _chung | `FileAttachmentJPA` |
| `FileAttachmentMapperEntity` | `FILE_ATTACHMENT_MAPPER` | _chung | `FileAttachmentMapperRepositoryJPA` |
| `FileEcabinetEntity` | `FILE_ECABINET` | hop | `FileEcabinetRepositoryJPA` |
| `FileEncryptMapEntity` | `FILE_ENCRYPT_MAP` | ky-so | `FileEncryptMapJPA` |
| `FileEncryptMapHistoryEntity` | `FILE_ENCRYPT_MAP_HISTORY` | ky-so | `FileEncryptMapHistoryJPA` |
| `FilesAttachmentEntity` | `FILES_ATTACHMENT` | _chung | `FilesAttachmentJPA`, `FilesAttachmentRepositoryJPA` |
| `FilesEntity` | `FILES` | _chung | `FilesRepositoryJPA` |
| `FlowEntity` | `FLOW` | van-ban/luong-xu-ly | `FlowRepositoryJPA` |
| `FlowGroupTypeEntity` | `FLOW_GROUP_TYPE` | van-ban/luong-xu-ly | `FlowGroupTypeRepositoryJPA` |
| `GroupApplyEntity` | `GROUP_APPLY` | he-thong | `GroupApplyRepositoryJPA` |
| `ImageEntity` | `IMAGE` | _chung | `ImageRepositoryJPA` |
| `ImageOrgConfigEntity` | `IMAGE_ORG_CONFIG` | he-thong | `ImageOrgConfigRepositoryJPA` |
| `ImageOrgEntity` | `IMAGE_ORG` | he-thong | `ImageOrgRepositoryJPA` |
| `InObjectDetailEntity` | `IN_OBJECT_DETAIL` | van-ban/lien-thong | `InObjectDetailRepository` |
| `InObjectReceiveXmlEntity` | `IN_OBJECT_RECEIVE_XML` | van-ban/lien-thong | `InObjectReceiveXmlRepository` |
| `InObjectSendXmlEntity` | `IN_OBJECT_SEND_XML` | van-ban/lien-thong | `InObjectSendXmlRepository` |
| `InternalDocDetailEntity` | `INTERNAL_DOC_DETAIL` | van-ban/lien-thong | `InternalDocDetailRepositoryJPA` |
| `InternalDocReceiveEntity` | `INTERNAL_DOC_RECEIVE_XML` | van-ban/lien-thong | `InternalDocReceiveRepositoryJPA` |
| `InternalDocSendXmlEntity` | `INTERNAL_DOC_SEND_XML` | van-ban/lien-thong | `InternalDocSendXmlRepositoryJPA` |
| `KpiPortal` | `KPI` | kpi-danh-gia | `KpiPortalJPA` |
| `LanguageEntity` | `LANGUAGE` | he-thong | `LanguageRepositoryJPA` |
| `LogBackendEntity` | `LOG_BACKEND` | he-thong | `LogBackendJPA` |
| `LogTranstionSignEntity` | `LOG_TRANSTION_SIGN` | he-thong | `LogTranstionSignRepositoryJPA` |
| `MeetingAssistantEntity` | `MEETING_ASSISTANT` | hop | `MeetingAssistantRepositoryJPA` |
| `MeetingConfigEntity` | `MEETING_CONFIG` | hop | `MeetingConfigRepositoryJPA` |
| `MeetingEmailEntity` | `MEETING_EMAIL` | hop | `MeetingEmailRepositoryJPA` |
| `MeetingEntity` | `MEETING` | hop | `MeetingRepositoryJPA` |
| `MeetingFrequencyEntity` | `MEETING_FREQUENCY` | hop | `MeetingFrequencyRepositoryJPA` |
| `MeetingHistoryEntity` | `MEETING_HISTORY` | hop | `MeetingHistoryRepositoryJPA` |
| `MeetingMemberEntity` | `MEETING_MEMBER` | hop | `MeetingMemberRepositoryJPA` |
| `MeetingMemberFilesEntity` | `MEETING_MEMBER_FILES` | hop | `MeetingMemberFilesRepositoryJPA` |
| `MeetingMinuteEntity` | `MEETING_MINUTES` | hop | `MeetingMinuteRepositoryJPA` |
| `MeetingResourceEntity` | `MEETING_RESOURCE` | hop | `MeetingResourceRepositoryJPA` |
| `MeetingResourceManagerEntity` | `MEETING_RESOURCE_MANAGER` | hop | `MeetingResourceManagerRepositoryJPA` |
| `MeetingWeeklyEntity` | `meeting_weekly` | hop | `MeetingWeeklyRepositoryJPA` |
| `MenuEntity` | `MENU` | he-thong | `MenuRepositoryJPA` |
| `MessageEntity` | `MESSAGE` | he-thong | `MessageJPA` |
| `MigratedDocumentEntity` | `MIGRATED_DOCUMENT` | van-ban/lien-thong | `MigratedDocumentRepositoryJPA` |
| `MigratedFilesEntity` | `MIGRATED_FILES` | van-ban/lien-thong | `MigratedFilesRepositoryJPA` |
| `MissionEntity` | `MISSION` | nhiem-vu | `MissionRepositoryJPA` |
| `MissionNormEntity` | `MISSION_NORM` | nhiem-vu | — |
| `MissionProcessEntity` | `MISSION_PROCESS` | nhiem-vu | `MissionProcessRepositoryJPA` |
| `MissionReportResultDetailEntity` | `MISSION_REPORT_RESULT_DETAIL` | nhiem-vu | `MissionReportResultDetailRepositoryJPA` |
| `MissionReportResultEntity` | `MISSION_REPORT_RESULT` | nhiem-vu | `MissionReportResultRepositoryJPA` |
| `MissionStatusEntity` | `MISSION_STATUS` | he-thong | — |
| `MissionTemplateDetailEntity` | `MISSION_TEMPLATE_DETAIL` | nhiem-vu | `MissionTemplateDetailRepositoryJPA` |
| `MissionTemplateEntity` | `MISSION_TEMPLATE` | nhiem-vu | `MissionTemplateRepositoryJPA` |
| `MissionTemplateReceiveDocEntity` | `MISSION_TEMPLATE_RECEIVE_DOC` | nhiem-vu | `MissionTemplateReceiveDocRepositoryJPA` |
| `MissionTemplateScopeDetailEntity` | `MISSION_TEMPLATE_SCOPE_DETAIL` | nhiem-vu | `MissionTemplateScopeDetailRepositoryJPA` |
| `MissionTemplateScopeEntity` | `MISSION_TEMPLATE_SCOPE` | nhiem-vu | `MissionTemplateScopeRepositoryJPA` |
| `MissionTemplateTableEntity` | `MISSION_TEMPLATE_TABLE` | nhiem-vu | `MissionTemplateTableRepositoryJPA` |
| `NodeActionEntity` | `NODE_ACTION` | van-ban/luong-xu-ly | `NodeActionRepositoryJPA` |
| `NodeDeptUserEntity` | `NODE_DEPT_USER` | van-ban/luong-xu-ly | `NodeDeptUserRepositoryJPA` |
| `NodeEntity` | `NODE` | van-ban/luong-xu-ly | `NodeRepositoryJPA` |
| `NodeToNodeActionEntity` | `NODE_TO_NODE_ACTION` | van-ban/luong-xu-ly | `NodeToNodeActionRepositoryJPA` |
| `NodeToNodeEntity` | `NODE_TO_NODE` | van-ban/luong-xu-ly | `NodeToNodeRepositoryJPA` |
| `NotificationEntity` | `NOTIFICATION` | lich-nhac-viec | `NotificationRepositoryJPA` |
| `OrgCombinationMapEntity` | `ORG_COMBINATION_MAP` | he-thong | `OrgCombinationMapRepositoryJPA` |
| `OrgLevelEntity` | `ORG_LEVEL` | he-thong | — |
| `OrgMenuEntity` | `ORG_MENU` | he-thong | — |
| `PermissionBaseEntity` | `PERMISSION_BASE` | nhiem-vu | `PermissionBaseJPA`, `PermissionBaseRepositoryJPA` |
| `PermissionDashboardEntity` | `PERMISSION_DASHBOARD` | nhiem-vu | `PermissionDashboardRepositoryJPA` |
| `PermissionDataEntity` | `PERMISSION_DATA` | nhiem-vu | `PermissionDataRepositoryJPA` |
| `PersonalCategory` | `PERSONAL_CATEGORY` | he-thong | `PersonalCategoryRepositoryJPA` |
| `ReminderDocumentRelationEntity` | `REMINDER_DOCUMENT_RELATIONS` | lich-nhac-viec | `ReminderDocumentRelationRepositoryJPA` |
| `ReminderEntity` | `REMINDER` | lich-nhac-viec | `ReminderRepositoryJPA` |
| `ReminderFollowerEntity` | `REMINDER_FOLLOWERS` | lich-nhac-viec | `ReminderFollowerRepositoryJPA` |
| `ReminderHistoryEntity` | `REMINDER_HISTORY` | lich-nhac-viec | `ReminderHistoryJpa` |
| `ReminderReplyEntity` | `REMINDER_REPLY` | lich-nhac-viec | `ReminderReplyRepositoryJPA` |
| `ReportDailyHistoryEntity` | `REPORT_DAILY_HISTORY` | kpi-danh-gia | `ReportDailyHistoryJPA` |
| `ReportPeriodApproveEntity` | `REPORT_PERIOD_APPROVE` | kpi-danh-gia | `ReportPeriodApproveRepositoryJPA` |
| `ReportPeriodConfigEntity` | `REPORT_PERIOD_CONFIG` | kpi-danh-gia | `ReportPeriodConfigRepositoryJPA` |
| `ReportPeriodHistory` | `REPORT_PERIOD_HISTORY` | kpi-danh-gia | `ReportPeriodHistoryRepositoryJPA` |
| `ReportPeriodIndividualEntity` | `REP_IN` | kpi-danh-gia | `ReportPeriodIndividualRepositoryJPA` |
| `RolePermissionBaseEntity` | `ROLE_PERMISSION_BASE` | nhiem-vu | `RolePermissionBaseRepositoryJPA` |
| `RolePermissionDataEntity` | `ROLE_PERMISSION_DATA` | nhiem-vu | `RolePermissionDataRepositoryJPA` |
| `SecurityTypeEntity` | `SECURITY_TYPE` | he-thong | `SecurityTypeRepositoryJPA` |
| `SecurityTypeLanguageEntity` | `SECURITY_TYPE_LANGUAGE` | he-thong | `SecurityTypeLanguageRepositoryJPA` |
| `SmsBlackListEntity` | `SMS_BLACK_LIST` | lich-nhac-viec | `SmsBlackListRepositoryJPA` |
| `SmsMasterEntity` | `SMS_MASTER` | lich-nhac-viec | `SmsMasterRepositoryJPA` |
| `SourceMapEntity` | `SOURCE_MAP` | he-thong | `DraftMissionLinkRepository`, `SourceMapRepositoryJPA` |
| `StaffImageSignEntity` | `STAFF_IMAGE_SIGN` | ky-so | `StaffImageSignJPA` |
| `StaffInCvGroupEntity` | `STAFF_IN_CV_GROUP` | he-thong | `StaffInCvGroupRepositoryJPA` |
| `StatusEntity` | `STATUS` | he-thong | `StatusRepositoryJPA` |
| `SubmissionFileEntity` | `SUBMISSION_FILE` | phieu-trinh | `SubmissionFileRepositoryJPA` |
| `SubmissionFormEntity` | `SUBMISSION_FORM` | phieu-trinh | `SubmissionFormRepositoryJPA` |
| `SubmissionForwardEntity` | `SUBMISSION_FORWARD` | phieu-trinh | `SubmissionForwardRepositoryJPA` |
| `SubmissionMapEntity` | `SUBMISSION_MAP` | phieu-trinh | `SubmissionMapRepositoryJPA` |
| `SubmissionMapFileEntity` | `SUBMISSION_MAP_FILE` | phieu-trinh | `SubmissionMapFileJPA` |
| `SubmissionProcessEntity` | `SUBMISSION_PROCESS` | phieu-trinh | `SubmissionProcessRepositoryJPA` |
| `SysRoleEntity` | `SYS_ROLE` | he-thong | `SysRoleJPA`, `SysRoleRepositoryJPA` |
| `SysRoleMenuEntity` | `SYS_ROLE_MENU` | he-thong | `SysRoleMenuRepositoryJPA` |
| `SystemDowntimeLog` | `SYSTEM_DOWNTIME_LOG` | he-thong | `SystemDowntimeLogJPA` |
| `SystemParameterEntity` | `SYSTEM_PARAMETER` | he-thong | `SystemParameterRepositoryJPA` |
| `TagDictionaryEntity` | `TAG_DICTIONARY` | tai-lieu-mau | `TagDictionaryJpa` |
| `TextAttachBaseEntity` | `TEXT_ATTACH_BASE` | _chung | `TextAttachBaseRepositoryJPA` |
| `TextAttachEntity` | `TEXT_ATTACH` | _chung | `TextAttachRepositoryJPA` |
| `TextBookEntity` | `TEXT_BOOK` | van-ban/so-van-ban | `TextBookRepositoryJPA` |
| `TextChatEntity` | `TEXT_CHAT` | _chung | `TextChatRepositoryJPA` |
| `TextCheckSpellsEntity` | `TEXT_CHECK_SPELLS` | xu-ly-cong-viec | `TextCheckSpellsRepositoryJPA` |
| `TextDraftEntity` | `TEXT_DRAFT` | xu-ly-cong-viec | `TextDraftRepositoryJPA` |
| `TextDraftFileEntity` | `TEXT_DRAFT_FILE` | xu-ly-cong-viec | `TextDraftFileRepositoryJPA` |
| `TextDraftHistoryEntity` | `TEXT_DRAFT_HISTORY` | xu-ly-cong-viec | `TextDraftHistoryRepositoryJPA` |
| `TextEntity` | `TEXT` | van-ban/di | `DraftMetadataRepository`, `TextRepositoryJPA` |
| `TextProcessEntity` | `TEXT_PROCESS` | van-ban/di | `TextProcessRepositoryJPA` |
| `TextProcessHistoryEntity` | `TEXT_PROCESS_HISTORY` | van-ban/di | `TextProcessRepositoryHistoryJPA` |
| `TextReceiverGroupDetailEntity` | `TEXT_RECEIVER_GROUP_DETAIL` | van-ban/di | — |
| `TimeZoneLocalEntity` | `TIME_ZONE_LOCAL` | he-thong | `TimeZoneLocalJPA`, `TimeZoneLocalRepositoryJPA` |
| `UserDeviceEntity` | `USER_DEVICE` | tich-hop | `UserDeviceJPA` |
| `UserOrgMapEntity` | `USER_ORG_MAP` | he-thong | `UserOrgMapRepositoryJPA` |
| `UserRoleEntity` | `USER_ROLE` | he-thong | `UserRoleJPA`, `UserRoleRepositoryJPA` |
| `UserTableHeaderStateEntity` | `USER_TABLE_HEADER_STATE` | he-thong | `UserTableHeaderStateRepositoryJPA` |
| `UserTokensEntity` | `USER_TOKENS` | he-thong | `UserTokensJPA` |
| `VersionControlEntity` | `VERSION_CONTROL` | he-thong | `VersionControlRepositoryJPA` |
| `VersionControlFileEntity` | `VERSION_CONTROL_FILE` | he-thong | `VersionControlFileJPA` |
| `VideoConferenceGroupEntity` | `VIDEO_CONFERENCE_GROUP` | hop | `VideoConferenceGroupRepositoryJPA` |
| `VoteEntity` | `VOTE` | hop | `VoteRepositoryJPA` |
| `VoteOptionEmployeeEntity` | `VOTE_OPTION_EMPLOYEE` | hop | `VoteOptionEmployeeRepositoryJPA` |
| `VoteOptionEntity` | `VOTE_OPTION` | hop | `VoteOptionRepositoryJPA` |
| `VoteQuestionEntity` | `VOTE_QUESTION` | hop | `VoteQuestionRepositoryJPA` |
| `WaitingNumberBookEntity` | `WAITING_NUMBER_BOOK` | van-ban/di | `WaitingNumberBookRepositoryJPA` |
| `WorkGroupEntity` | `WORK_GROUP` | nhiem-vu | `WorkGroupRepositoryJPA` |
| `WorkGroupItemEntity` | `WORK_GROUP_ITEM` | nhiem-vu | `WorkGroupItemRepositoryJPA` |
| `WorkGroupItemHistory` | `WORK_GROUP_ITEM_HISTORY` | nhiem-vu | `WorkGroupItemHistoryRepositoryJPA` |
| `WorkGroupOrgDetailEntity` | `WORK_GROUP_ORG_DETAIL` | nhiem-vu | `WorkGroupOrgDetailJPA` |

## Web (`com.viettel.voffice.entity`, `com.viettel.vps.entity` — dùng bởi legacy)

| Entity | Bảng | Phân hệ |
|---|---|---|
| `Alert` | `ALERT` | lich-nhac-viec |
| `AlertFeedback` | `ALERT_FEEDBACK` | he-thong |
| `Attach` | `Attach` | he-thong |
| `BChat` | `BCHAT` | _chung |
| `BookDispatch` | `BOOK_DISPATCH` | van-ban/so-van-ban |
| `Boxs` | `BOXS` | ho-so-cong-viec |
| `BriefFilesAttachment` | `BRIEF_FILES_ATTACHMENT` | ho-so-cong-viec |
| `BriefUpdate` | `BRIEF_UPDATE` | ho-so-cong-viec |
| `Category` | `REQUISITION` | he-thong |
| `ChatMessage` | `Chat_Message` | he-thong |
| `CodeMaster` | `CODE_MASTER` | he-thong |
| `Criteria` | `CRITERIA` | kpi-danh-gia |
| `CriteriaGroup` | `CRITERIA_GROUP` | kpi-danh-gia |
| `Document` | `DOCUMENT` | van-ban/quan-ly-chung |
| `DocumentArchive` | `DOCUMENT_ARCHIVE` | van-ban/quan-ly-chung |
| `DocumentFile` | `DOCUMENT_FILE` | van-ban/quan-ly-chung |
| `DocumentHandoverHistory` | `DOCUMENT_HANDOVER_HISTORY` | van-ban/quan-ly-chung |
| `DocumentLibrary` | `DOCUMENT_LIBRARY` | tai-lieu-mau |
| `DocumentLibraryDetail` | `DOCUMENT_LIBRARY_DETAIL` | tai-lieu-mau |
| `DocumentPublicStatus` | `DOCUMENT_PUBLIC_STATUS` | van-ban/quan-ly-chung |
| `EmailConfirm` | `EMAIL_CONFIRM` | he-thong |
| `EmailDetail` | `EMAIL_DETAIL` | _chung |
| `EmailMaster` | `EMAIL_MASTER` | _chung |
| `EmailReceive` | `Email_Receive` | he-thong |
| `EmpRating` | `EMP_RATING` | kpi-danh-gia |
| `EntityActionLogService` | `ACTION_LOG_SERVICE` | he-thong |
| `EvaluationUnit` | `EVALUATION_UNIT` | kpi-danh-gia |
| `FileAttachment` | `FILE_ATTACHMENT` | _chung |
| `FileAttachmentMapper` | `FILE_ATTACHMENT_MAPPER` | _chung |
| `Files` | `FILES` | _chung |
| `GroupDetail` | `GROUP_DETAIL` | he-thong |
| `GroupManager` | `GROUP_MANAGER` | he-thong |
| `ImageOrg` | `IMAGE_ORG` | he-thong |
| `ImageOrgConfig` | `IMAGE_ORG_CONFIG` | he-thong |
| `ImageSignature` | `IMAGE_SIGNATURE` | ky-so |
| `KPIIndex` | `KPI_INDEX` | kpi-danh-gia |
| `KiFormulaConfig` | `KI_FORMULA_CONFIG` | kpi-danh-gia |
| `KiFormulaConfigDetail` | `RATIO_CONFIG_DETAIL` | kpi-danh-gia |
| `KpiPortal` | `KPI` | kpi-danh-gia |
| `LabourContractType` | `LABOUR_CONTRACT_TYPE` | he-thong |
| `LockStatus` | `LOCK_STATUS` | he-thong |
| `LongLeave` | `LONG_LEAVE` | he-thong |
| `MailAction` | `MAIL_ACTION` | _chung |
| `MapConfig` | `MAP_CONFIG` | he-thong |
| `MappingResovle` | `MAPPING_RESOVLE` | he-thong |
| `Meeting` | `MEETING` | hop |
| `MeetingAssistant` | `MEETING_ASSISTANT` | hop |
| `MeetingCommander` | `MEETING_COMMANDER` | hop |
| `MeetingComplementReport` | `M_COMPLEMENT_REPORT` | hop |
| `MeetingComplementReportDetail` | `M_COMPLEMMENT_REPORT_DETAIL` | hop |
| `MeetingEmail` | `MEETING_EMAIL` | hop |
| `MeetingFrequency` | `MEETING_FREQUENCY` | hop |
| `MeetingHistory` | `MEETING_HISTORY` | hop |
| `MeetingLock` | `MEETING_LOCK` | hop |
| `MeetingLockOrg` | `MEETING_LOCK_ORG` | hop |
| `MeetingMember` | `MEETING_MEMBER` | hop |
| `MeetingMinutes` | `MEETING_MINUTES` | hop |
| `MeetingNotification` | `MEETING_NOTIFICATION` | hop |
| `MeetingResource` | `MEETING_RESOURCE` | hop |
| `MeetingResourceManager` | `MEETING_RESOURCE_MANAGER` | hop |
| `MeetingWeekCalendar` | `MEETING_WEEK_CALENDAR` | hop |
| `MeetingWeekCalendarFiles` | `MEETING_WEEK_CALENDAR_FILES` | hop |
| `MigratedDocumentEntity` | `MIGRATED_DOCUMENT` | van-ban/lien-thong |
| `MigratedFilesEntity` | `MIGRATED_FILES` | van-ban/lien-thong |
| `Mission` | `MISSION` | nhiem-vu |
| `MissionDetail` | `MISSION_DETAIL` | nhiem-vu |
| `MissionExtend` | `MISSION_EXTEND` | nhiem-vu |
| `MissionProcess` | `MISSION_PROCESS` | nhiem-vu |
| `MissionRating` | `MISSION_RATING` | nhiem-vu |
| `Notice` | `NOTICE` | lich-nhac-viec |
| `NoticeDetail` | `NOTICE_DETAIL` | lich-nhac-viec |
| `OrgCombinationMap` | `ORG_COMBINATION_MAP` | he-thong |
| `OrgKi` | `ORG_KI` | kpi-danh-gia |
| `OrientOrgMap` | `ORIENT_RECEIVE_ORG` | lich-nhac-viec |
| `Orientation` | `ORIENTATION` | lich-nhac-viec |
| `PageIntroduction` | `PAGE_INTRODUCTION` | he-thong |
| `Permission` | `PERMISSION` | nhiem-vu |
| `Position` | `POSITION` | he-thong |
| `PrimaryVariable` | `PRIMARY_VARIABLE` | he-thong |
| `PrivateShortcut` | `PRIVATE_SHORTCUT` | he-thong |
| `ProposePoint` | `PROPOSE_POINT` | kpi-danh-gia |
| `RatingKi` | `EMP_RATING` | kpi-danh-gia |
| `RatioConfig` | `RATIO_CONFIG` | kpi-danh-gia |
| `RatioConfigDetail` | `RATIO_CONFIG_DETAIL` | kpi-danh-gia |
| `ReadNoticeHistory` | `READ_NOTICE_HISTORY` | lich-nhac-viec |
| `Reminder` | `REMINDER` | lich-nhac-viec |
| `ReminderDocumentRelation` | `REMINDER_DOCUMENT_RELATIONS` | lich-nhac-viec |
| `ReminderReply` | `REMINDER_REPLIES` | lich-nhac-viec |
| `Request` | `REQUEST` | phieu-trinh |
| `RequestEmail` | `REQUEST_EMAIL` | phieu-trinh |
| `Requisition` | `REQUISITION` | xu-ly-cong-viec |
| `RequisitionComment` | `REQUISITION_COMMENT` | xu-ly-cong-viec |
| `RequisitionDoc` | `REQUISITION_DOC` | xu-ly-cong-viec |
| `RequisitionFile` | `REQUISITION_FILE` | ky-so |
| `RequisitionFlow` | `REQUISITION_FLOW` | van-ban/luong-xu-ly |
| `RequisitionFlowDetail` | `REQUISITION_FLOW_DETAIL` | van-ban/luong-xu-ly |
| `RequisitionProcess` | `REQUISITION_PROCESS` | xu-ly-cong-viec |
| `RequisitionReceiver` | `REQUISITION_RECEIVER` | xu-ly-cong-viec |
| `ResovleIssue` | `RESOVLE_ISSUE` | he-thong |
| `RoleMenu` | `ROLE_MENU` | he-thong |
| `RolePermission` | `ROLE_PERMISSION` | nhiem-vu |
| `RoleScopeData` | `ROLE_SCOPE_DATA` | he-thong |
| `ScopeType` | `SCOPE_TYPE` | he-thong |
| `Shelve` | `SHELVE` | ho-so-cong-viec |
| `SmsDetail` | `SMS_DETAIL` | lich-nhac-viec |
| `SmsMaster` | `SMS_MASTER` | lich-nhac-viec |
| `SourceMap` | `SOURCE_MAP` | he-thong |
| `StoreTypeConfig` | `STORE_TYPE_CONFIG` | ho-so-cong-viec |
| `Survey` | `SURVEY` | he-thong |
| `SurveyMap` | `SURVEY_MAP` | he-thong |
| `SyncHistory` | `SYNC_HISTORY` | he-thong |
| `SysCat` | `SYS_CAT` | he-thong |
| `SysCatType` | `SYS_CAT_TYPE` | he-thong |
| `SysMenu` | `SYS_MENU` | he-thong |
| `SysOperation` | `SYS_OPERATION` | he-thong |
| `SysOrganization` | `VHR_ORG` | he-thong |
| `SysParameter` | `SYSTEM_PARAMETER` | he-thong |
| `SysResource` | `SYS_RESOURCE` | he-thong |
| `SysRole` | `SYS_ROLE` | he-thong |
| `SysUser` | `VHR_EMPLOYEE` | he-thong |
| `Task` | `TASK` | cong-viec |
| `TaskApproval` | `TASK_APPROVAL` | cong-viec |
| `TaskFile` | `TASK_FILE` | cong-viec |
| `TaskProcess` | `TASK_PROCESS` | cong-viec |
| `TaskRating` | `TASK_RATING` | cong-viec |
| `TaskReceiver` | `TASK_RECEIVER` | cong-viec |
| `Template` | `TEMPLATE` | tai-lieu-mau |
| `TimeConfig` | `TIME_CONFIG` | lich-nhac-viec |
| `TimeZoneLocal` | `TIME_ZONE_LOCAL` | he-thong |
| `UserOrgMap` | `USER_ORG_MAP` | he-thong |
| `UserRole` | `USER_ROLE` | he-thong |
| `UserRoleSync` | `USER_ROLE` | he-thong |
| `UserScopeData` | `USER_SCOPE_DATA` | he-thong |
| `VHREmployee` | `VHR_EMPLOYEE` | tich-hop |
| `VHROrg` | `VHR_ORG` | tich-hop |
| `VideoConferenceGroup` | `VIDEO_CONFERENCE_GROUP` | hop |
| `WorkingProcess` | `WORK_PROCESS` | he-thong |

## Bảng chạm tới bởi BE gen-1 DAO (ước lượng từ SQL)

| DAO | Bảng |
|---|---|
| `ActionLogMobileDAO` | — |
| `AdOrgDAO` | — |
| `AgreementDAO` | `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `FILE_ATTACHMENT`, `MISSION`, `MISSION_PROCESS`, `ORG_COMBINATION_MAP`, `USER_ROLE`, `VHR_ORG` |
| `AnswerDocumentDAO` | `AREA`, `ATTACH`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_TYPE`, `LSTDOCID`, `MEETING_ASSISTANT`, `MESSAGE`, `SECURITY_TYPE`, `TEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `AttachCommentDAO` | `ATTACH_COMMENT` |
| `AttachDAO` | `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF_DOCUMENT`, `BRIEF_FILES_ATTACHMENT`, `DOCUMENT`, `FILES_ATTACHMENT`, `LOG_TRANSTION_SIGN`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_PROCESS`, `TEXT_SIGN_LOCATION` |
| `AutoDigitalSignDAO` | `AUTO_DIGSIG_RESPOND`, `AUTO_DIGSIG_TRANSACTION`, `EXT_APP`, `MESSAGE`, `STAFF_IN_MESSAGE`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_PROCESS`, `TEXT_PROCESS_CURRENT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `BoxManagementDAO` | `AREA`, `BOXS`, `BRIEF`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `FLOOR`, `SECURITY_TYPE`, `SHELVES`, `STORAGES`, `VHR_ORG` |
| `BriefDetailManagementDAO` | `ATTACH`, `ATTACH_TEMPLATE`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `SECURITY_TYPE`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE` |
| `BriefManagementDAO` | `ATTACH_TEMPLATE`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOG_BRIEF`, `DOCUMENT`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `SECURITY_TYPE`, `SHELVES`, `STORAGES`, `SYS_ROLE`, `TEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `CChartGroupIndicatorDAO` | — |
| `CDepartUnitchartDAO` | — |
| `CIndicatorBaseDAO` | — |
| `CatalogBriefDAO` | `BRIEF`, `CATALOG_BRIEF`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `CertManagementDAO` | `DATABASE`, `P12_CERT`, `STAFF`, `SYSTEM_PARAMETER`, `VHR_EMPLOYEE` |
| `ChartConfigDAO` | — |
| `ChartIndicatorConfigDAO` | — |
| `CiscoMeetingDAO` | `MEETING`, `MEETING_RESOURCE` |
| `CloudDeviceCertDAO` | `CLOUD_DEVICE_CERT` |
| `CommentDAO` | `DOCUMENT`, `DOCUMENT_IN_STAFF`, `FILES`, `MEETING`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `PERSONAL_STOTAGE`, `VHR_EMPLOYEE`, `VOF_COMMENT` |
| `CommonDAO` | `AUTO_DIGSIG_TRANSACTION`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `TEXT`, `VHR_EMPLOYEE` |
| `CommonDataBaseDaoVO1` | — |
| `CommonDataBaseDaoVO2` | — |
| `ConfigParameterDAO` | `CONFIG_USER_DOCUMENT`, `SYSTEM_PARAMETER`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `ConnectDocumentDAO` | `ATTACH_TEMPLATE`, `CONNECT_ATTACHMENT`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_DOC_SEND`, `CONNECT_PROCESS_IN`, `CONNECT_PROCESS_OUT`, `CONNECT_VHR`, `CV_PRIORITY`, `DOCUMENT`, `FILES_ATTACHMENT`, `MESSAGE`, `TEXT`, `VHR_ORG` |
| `ConnectVHRDao` | `CHILD_CNT`, `CONNECT_VHR`, `GROUP_IN_CV_GROUP`, `SYSTEM_PARAMETER`, `VHR_ORG` |
| `CreateChart` | — |
| `CreateChartColumnsAndLines` | — |
| `CvGroupDAO` | `CONNECT_VHR`, `CV_GROUP`, `DUOC`, `GROUP_IN_CV_GROUP`, `GROUP_SIGN`, `LSTROOTEMP`, `ORG_SYS_MENU`, `P12_CERT`, `POSITION`, `ROLE_IN_CV_GROUP`, `STAFF_IN_CV_GROUP`, `SYS_MENU`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DataReportExpenseDAO` | — |
| `DatabaseManagerDAO` | `ALL_TABLES` |
| `DatabaseUtils` | — |
| `DemoDAO` | `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_HISTORY`, `MEETING_MEMBER`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE` |
| `DocOrgRepublishDAO` | `DOCUMENT`, `DOCUMENT_SCOPE_DETAIL`, `DOC_ORG_REPUBLISH`, `TEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentAlternativeDAO` | `DOCUMENT_ALTERNATIVE` |
| `DocumentCommonService` | `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOC_ORG_REPUBLISH`, `TEXT`, `TEXT_MARK` |
| `DocumentConstant` | — |
| `DocumentDAO` | `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `FILES_ATTACHMENT`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentExtendDAO` | `DOCUMENT`, `DOCUMENT_EXTEND`, `TEXT` |
| `DocumentFormalErrorDAO` | `DOCUMENT_FORMAL_ERROR` |
| `DocumentHandoverDAO` | `AGGR`, `AGG_RECEIVERS`, `ALL_RECEIVERS`, `AREA`, `BRIEF`, `BRIEFCODE`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `COMMENT_AGG`, `CV_GROUP`, `CV_PRIORITY`, `DATAS`, `DOCS`, `DOCUMENT`, `DOCUMENT_HANDOVER`, `DOCUMENT_HANDOVER_DETAIL`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST_REPLY`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `FILEATTACHPAGES`, `FILES_ATTACHMENT`, `GROUP_MAPPING`, `HOAN_THANH_AGG`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `NGUOI_HOAN_THANH_RAW`, `RANKED`, `RECEIVEDSAVEDOCUMENTOBJECT`, `RECV_1`, `RECV_2`, `RECV_3`, `ROOTDATA`, `SECURITY_TYPE`, `STAFF`, `TEXT`, `TEXT_BOOK`, `TEXT_PROCESS`, `TRANSFERRECEIVEDDATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentInDAO` | `CV_GROUP`, `DOCUMENT`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE_REF`, `FILES_ATTACHMENT`, `POSITION`, `STAFFGROUP`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentInGroupDAO` | `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_PROCESS`, `DOCUMENT_RECEIVE_MAP`, `FILES_ATTACHMENT`, `STAFFGROUP`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentInStaffDAO` | `ATTACH`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_PROCESS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT_COMMENT`, `MISSION`, `POSITION`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `SYSTIMESTAMP`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentLibraryDAO` | `AREA`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_PUBLISHED`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `SECURITY_TYPE`, `STAFFGROUP`, `TEXT_PROCESS`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentPermissionDAO` | `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `DOCUMENT`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `MEETING`, `MEETING_MEMBER`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `SOURCE_MAP`, `STORE_UNFOLOW`, `TASK`, `TASK_PROCESS`, `TEXT`, `TEXT_TEXT_ATTACH`, `USER_ROLE` |
| `DocumentProposalDAO` | `CV_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_PROPOSAL`, `DOCUMENT_PROPOSAL_DETAIL`, `POSITION`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentPublishDAO` | `AREA`, `DOCUMENT`, `DOCUMENT_ALTERNATIVE`, `DOCUMENT_PUBLISHED`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `SECURITY_TYPE`, `STAFFGROUP` |
| `DocumentPublishedDAO` | `DOCUMENT_ALTERNATIVE`, `DOCUMENT_PUBLISHED` |
| `DocumentPublishedTmpDAO` | `DOCUMENT_PUBLISHED`, `DOCUMENT_PUBLISHED_TMP` |
| `DocumentQueries` | `AREA`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_PROCESS_IN`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `SECURITY_TYPE`, `STAFF`, `TEXT`, `TEXT_BOOK`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentRequestConfigDAO` | `CONFIG_AUTO_SEND_DOCUMENT`, `DOCUMENT_REQUEST_CONFIG`, `DOCUMENT_REQUEST_CONFIG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentScopeDAO` | `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `TEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentSearchInGroupByTextBookService` | `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `SECURITY_TYPE`, `TEXT` |
| `DocumentSearchInService` | `AREA`, `CONNECT_DOCUMENT`, `CONNECT_DOC_IN_INTERNAL`, `CONNECT_PROCESS_IN`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_TYPE`, `SECURITY_TYPE`, `STAFF`, `TEXT`, `TEXT_BOOK`, `TO_DATE`, `VHR_EMPLOYEE` |
| `DocumentSearchOutService` | `AREA`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `CATEGORY_COMMON`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `SECURITY_TYPE`, `TEXT`, `TEXT_BOOK`, `TEXT_MARK`, `TEXT_PROCESS`, `USER_ROLE` |
| `DocumentSendViewInfoDAO` | `DOCUMENT_SEND_VIEW_INFO` |
| `DocumentSignDAO` | `AREA`, `ATTACH`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `CONNECT_DOCUMENT`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `MISSION_NORM`, `ORG_CRITERIA_SOURCE`, `POSITION`, `SECURITY_TYPE`, `STAFF`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_EDIT_HISTORY`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `DocumentToVofMapDAO` | `GOVERMENT_OFFICE_MAP` |
| `DownloadAllFileDAO` | — |
| `DownloadFileCommentDAO` | — |
| `DownloadFileDocumentDAO` | `TEXT_SIGN_LOCATION` |
| `EmpCloudCADAO` | `EMP_CLOUD_CA` |
| `EmployeeDao` | `MISSION`, `MISSION_PROCESS`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `EntityMeetingVideoConference` | — |
| `FavouriteDAO` | `BASE`, `CV_GROUP`, `FAVOURITE`, `STAFF_IN_CV_GROUP`, `TOP_ORG`, `TOP_PERSONAL`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `FileAttachmentDAO` | `BRIEF_FILE_MAP`, `FILES`, `MEETING` |
| `FilesAttachmentDAO` | `ATTACH_TEMPLATE`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `FILES_ATTACHMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `MIGRATED_FILES`, `TEXT_EDIT_HISTORY` |
| `FilesCommentDraffDAO` | `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `TEXT_NOTE` |
| `FinanceDataDAO` | — |
| `GroupInCvGroupDAO` | `GROUP_IN_CV_GROUP` |
| `HistoryChangeSignDAO` | `HISTORY_CHANGE_SIGN` |
| `HomeWidgetDAO` | `HOME_WIDGET` |
| `ImageDAO` | `IMAGE` |
| `ImageOrgDAO` | `BRIEF_MARK`, `IMAGE`, `IMAGE_ORG`, `IMAGE_ORG_CONFIG`, `TEXT_MARK`, `VHR_ORG` |
| `ImageSignDao` | `ATTACH`, `STAFF`, `STAFF_IMAGE_SIGN`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_OTHER`, `TEXT_PROCESS`, `TEXT_SIGN_LOCATION` |
| `LogActionDao` | `ACTION_LOG_SERVICE` |
| `LogTranstionSignDAO` | `LOG_TRANSTION_SIGN` |
| `MappingOrgDAO` | `GROUP_MAPPING`, `STAFF`, `VHR_EMPLOYEE` |
| `MeetingAssistantDAO` | `DOCUMENT_IN_STAFF`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `STAFF`, `SYSTEM_PARAMETER`, `TIME_ZONE_LOCAL`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MeetingConfigAddDAO` | `MEETINGCONFIGADD`, `MEETING_CONFIG_ADD`, `MEETING_MEMBER`, `MEETING_ORG_MEMBER_ADD`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MeetingDAO` | `AREA`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `MAIL_MEETING_HISTORY`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_RESOURCE`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TIME_ZONE_LOCAL`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP` |
| `MeetingFileCommentDAO` | `FILES`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE` |
| `MeetingMinutesDAO` | `MEETING_MINUTES`, `USER_ROLE`, `VHR_EMPLOYEE` |
| `MeetingNativeDAO` | `MEETING`, `MEETING_ASSISTANT`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_REPLATE`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP` |
| `MeetingOrgMemberAddDAO` | `MEETING_CONFIG_ADD`, `MEETING_ORG_MEMBER_ADD`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MeetingResourceDAO` | `FILES`, `MEETING_RESOURCE` |
| `MeetingWeekDAO` | `CV_GROUP`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DUOC`, `FILES`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MISSION`, `PERMISSION_DATA`, `ROLE_PERMISSION_DATA`, `SOURCE_MAP`, `STAFF_IN_CV_GROUP`, `SYS_ROLE`, `TEXT`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP` |
| `MissionChartDAO` | `MISSION`, `VHR_ORG` |
| `MissionDAO` | `AREA`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_TASK`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `FIELD`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `MAPPING_RESOVLE`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `PERFORM_ORG_AREA`, `RESOVLE_ISSUE`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MissionDashboardChartDAO` | `AREA`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `MISSION`, `MISSION_PROCESS`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MissionDashboardReportDAO` | `AREA`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `MISSION`, `MISSION_PROCESS`, `SECURITY_TYPE`, `SOURCE_MAP`, `SYSTEM_PARAMETER`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MissionReportDAO` | `DOCUMENT`, `MISSION`, `MISSION_NORM`, `MISSION_PROCESS`, `SOURCE_MAP`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `MissionSigningDAO` | `MISSION_SIGNING` |
| `NotificationDAO` | `NOTICE`, `NOTIFICATION`, `READ_NOTICE_HISTORY` |
| `ObjectTransferViaAxisDAO` | `MISSION` |
| `OrgCeoDAO` | `ORG_CEO` |
| `OrgCriteriaDAO` | `CONFIG_ORG_RATING`, `ORG_CRITERIA`, `ORG_CRITERIA_CONFIG`, `ORG_CRITERIA_HISTORY`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_SOURCE`, `USER_ORG_MAP`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `OrgCriteriaMapDAO` | `ORG_CRITERIA`, `ORG_CRITERIA_MAP`, `VHR_ORG` |
| `OrgCriteriaRatingDAO` | `ORG_CRITERIA_RATING` |
| `OrgCriteriaRatingTotalDAO` | `ORG_CRITERIA`, `ORG_CRITERIA_MAP`, `ORG_CRITERIA_RATING`, `ORG_CRITERIA_RATING_TOTAL`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `OrgDAO` | `EMPLOYEE_TYPE_PROCESS`, `IMAGE_ORG`, `STAFF_GROUP_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `OrientationDAO` | `AREA`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `ORIENTATION`, `ORIENT_RECEIVE_ORG`, `SOURCE_MAP`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `P12CertDAO` | `P12_CERT`, `STAFF`, `VHR_EMPLOYEE` |
| `PersonTaskDAO` | `ATTACH`, `CODE_MASTER`, `EMP_RATING`, `FILES`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REQUEST`, `REQUEST_PROCESS`, `SOURCE_MAP`, `SYS_ROLE`, `TASK`, `TASK_FILE`, `TASK_PROCESS`, `TEXT_ATTACH`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `PositionDAO` | `POSITION` |
| `ReminderHistoryDAO` | `REMINDER`, `REMINDER_HISTORY`, `REMINDER_REPLY`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `RequestDAO` | `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `MEETING_ASSISTANT`, `MISSION`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `SOURCE_MAP`, `SYS_ROLE`, `TASK`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `RequestEmpConfigDAO` | `REQUEST_EMP_CONFIG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `ShelveManagementDAO` | `BOXS`, `BRIEF`, `SHELVES`, `STORAGES` |
| `SignBriefcaseDAO` | `ATTACH_BRIEFCASE`, `MEETING_ASSISTANT`, `SIGN_BRIEFCASE`, `SIGN_BRIEFCASE_ATTACH`, `SIGN_BRIEFCASE_ATTACH_OTHER`, `SIGN_BRIEFCASE_SIGNER`, `SIGN_BRIEFCASE_STATUS`, `VHR_EMPLOYEE` |
| `SmsDAO` | `CONFIG_SMS_ORG`, `CV_GROUP`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `MEETING_ASSISTANT`, `MESSAGE`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `SmsInterceptDAO` | `CONFIG_SMS_MODULE`, `CONFIG_SMS_ORG`, `SMS_BLACK_LIST` |
| `SourceMapDAO` | `MISSION`, `ORG_COMBINATION_MAP`, `REQUEST_PROCESS`, `SOURCE_MAP`, `SYS_ROLE`, `TASK`, `USER_ROLE` |
| `StaffDAO` | `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `ORG_LEVEL`, `POSITION`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `SYS_MENU`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `StaffImageSignDAO` | `STAFF`, `STAFF_IMAGE_SIGN` |
| `StorageManagementDAO` | `BOXS`, `BRIEF`, `SHELVES`, `STORAGES`, `SYS_ROLE`, `USER_ROLE`, `VHR_ORG` |
| `StoreTypeConfigDAO` | `DOCUMENT_TYPE`, `STORE_DOCUMENT_ROLE`, `STORE_TYPE_CONFIG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `SubmissionFormEditHistoryDAO` | `SUBMISSION_FORM_EDIT_HISTORY` |
| `SyncFavoriteClientDAO` | `GROUP_MAPPING`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `SysRoleDAO` | `PERMISSION_DATA`, `ROLE_PERMISSION_DATA`, `SYS_ROLE`, `USER_ROLE` |
| `SystemManagerDAO` | `ROLE_MENU`, `SYS_MENU` |
| `SystemParameterDAO` | `SYSTEM_PARAMETER` |
| `TaskApprovalDAO` | `TASK_APPROVAL`, `VHR_EMPLOYEE` |
| `TaskCommonDAO` | `FILE_ATTACHMENT`, `SOURCE_MAP` |
| `TaskDAO` | `ATTACH`, `AVERAGE_TASK_RATING`, `CODE_MASTER`, `DOCUMENT`, `DOCUMENT_IN_STAFF`, `EMPLOYEE_TYPE_PROCESS`, `EMP_RATING`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `GENERAL_ITEM`, `MEETING_ASSISTANT`, `MISSION`, `ORG_KI`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `REQUEST`, `REQUEST_PROCESS`, `SOURCE_MAP`, `STAFF`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_FILE`, `TASK_PROCESS`, `TASK_RATING`, `TEXT`, `TEXT_ATTACH`, `TEXT_PROCESS`, `TIME_CONFIG`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `WORK_PROCESS` |
| `TaskDataBaseDao` | `REQUEST`, `REQUEST_PROCESS`, `SOURCE_MAP`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_RECEIVER`, `USER_ROLE`, `VHR_EMPLOYEE` |
| `TaskProcessDAO` | `CODE_MASTER`, `RATIO_CONFIG`, `RATIO_CONFIG_DETAIL`, `TASK_PROCESS`, `VHR_ORG` |
| `TaskRatingDAO` | `AVERAGE_TASK_RATING`, `TASK`, `TASK_APPROVAL`, `TASK_CHECK_DOCUMENT`, `TASK_RATING`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `TemplateDAO` | `AREA`, `DOCUMENT_TYPE`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `TextAssistantDAO` | `TEXT_ASSISTANT_CONFIG` |
| `TextAttachPartnerDAO` | `TEXT_ATTACH_PARTNER` |
| `TextBookDAO` | `DATA_SOURCE`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_TYPE`, `FILTERED_DATA`, `HAS_DEFAULT`, `SYSDATE`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_PROCESS`, `USER_ROLE`, `VHR_ORG`, `WAITING_NUMBER_BOOK` |
| `TextCheckSpellDAO` | `ATTACH`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_OTHER`, `TEXT_CHECK_SPELLS`, `USER_ROLE` |
| `TextCommonDAO` | `DOCUMENT`, `DOCUMENT_PUBLISHED_TMP`, `STAFF`, `STAFF_GROUP_ROLE`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_MANUAL_NUMBER`, `TEXT_MAX_NUMBER`, `TEXT_PROCESS`, `USER_ROLE` |
| `TextDAO` | `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `AUTO_DIGSIG_TRANSACTION`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATEGORY_COMMON`, `CONNECT_DOCUMENT`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `FILES_COMMENT_SIGN`, `IMAGE_ORG`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_MINUTES`, `NODE_ACTION`, `POSITION`, `SECURITY_TYPE`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_CHAIN`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `TextEditHistoryDAO` | `ATTACH`, `ATTACH_TEMPLATE`, `FILES_ATTACHMENT`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_EDIT_HISTORY` |
| `TextFileCommentDAO` | `ATTACH`, `FILES_ATTACHMENT`, `TEXT_ATTACH`, `TEXT_ATTACH_OTHER`, `TEXT_NOTE` |
| `TextMarkSyncDAO` | `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `DOCUMENT`, `DOCUMENT_TYPE`, `STAFF`, `TEXT`, `TEXT_MARK_SYNC`, `TEXT_PROCESS` |
| `TextPartnerDAO` | `TEXT`, `TEXT_ATTACH_PARTNER`, `TEXT_PARTNER`, `VHR_ORG` |
| `TextPartnerLogDAO` | `TEXT_PARTNER_LOG` |
| `TextProcessDAO` | `STAFF`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT` |
| `TextProcessHistoryDAO` | `TEXT_PROCESS_HISTORY` |
| `TextReceiverDAO` | `TEXT_RECEIVER` |
| `TextReceiverGroupDAO` | `CV_GROUP`, `TEXT_RECEIVER_GROUP` |
| `TextReportDAO` | `AREA`, `AUTO_DIGSIG_TRANSACTION`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `SECURITY_TYPE`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `TEXT`, `TEXT_PROCESS`, `TEXT_SIGN_NEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `TextSearchDAO` | `ATTACH`, `ATTACH_TEMPLATE`, `BRIEF`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_PROCESS`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `LOG_TRANSTION_SIGN`, `NODE_ACTION`, `POSITION`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_HISTORY`, `TEXT_SIGN_NEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `TextSignDAO` | `ATTACH`, `ATTACH_HISTORY`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `DOCUMENT_TYPE`, `FILES_ATTACHMENT`, `FILES_COMMENT_SIGN`, `MARK_ATTACH_HISTORY`, `STAFF_GROUP_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_NEXT`, `VHR_EMPLOYEE`, `VHR_ORG` |
| `TimeConfigDAO` | `TIME_CONFIG` |
| `UserActivityLogDAO` | `USER_ACTIVITY_LOG` |
| `UserDAO` | `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `DIRECTOR_CONFIG`, `DOCUMENT`, `EXT_APP`, `GROUP_MAPPING`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_MEMBER`, `P12_CERT`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `TEXT`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG` |
| `UserManuDAO` | `ROLE_MENU`, `SYS_MENU`, `SYS_ROLE`, `TABLE_LOG`, `USER_ROLE`, `VHR_EMPLOYEE` |
| `UserOrgMapDAO` | `USER_ORG_MAP`, `VHR_EMPLOYEE` |
| `UserRoleDAO` | `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_ROLE`, `USER_ROLE` |
| `VContractDAO` | `ATTACH_PARTNER`, `AUTO_DIGSIG_TRANSACTION`, `TEXT_PARTNER`, `TEXT_PROCESS_PARTNER`, `TEXT_SIGN_LOCATION_PARTNER` |
| `VHROrgDAO` | `CONNECT_VHR`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `MEETING_CONFIG`, `STAFF_GROUP_ROLE`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG` |
