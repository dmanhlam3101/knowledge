# Bản đồ hệ thống — Họp, lịch họp, phòng họp không giấy (eCabinet), biểu quyết

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 62 màn hình, 6 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/reportSendReceiveDoc/popupVBScheduleMeeting.zul` | `vm.document.DocumentScheduleMeetingDetailVm` | `DocumentBusiness`, `DocumentRequestBusiness`, `MeetingBusiness`, `ScheduleToMeetingDocumentBusiness`, `WOPIBusiness` | `ICommon`, `IMeeting` | BE+LEGACY |
| `document/requestToScheduleMeetingDoc/docScheduleMeeting.zul` | `vm.document.DocumentScheduleMeetingVM` | `ScheduleToMeetingDocumentBusiness` | — | BE |
| `meeting/calendar/calendar.zul` | `vm.meeting.MeetingVM` | `DocumentBusiness`, `MeetingBusiness`, `SearchSolrBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/calendar/calendar_add.zul` | `vm.meeting.MeetingVM` | `DocumentBusiness`, `MeetingBusiness`, `SearchSolrBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/calendar_editor.zul` | `vm.meeting.MeetingVM` | `DocumentBusiness`, `MeetingBusiness`, `SearchSolrBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/emptyRoomList.zul` | `vm.meeting.MeetingListVM` | — | — | ☠ VM không tồn tại |
| `meeting/importMeeting.zul` | `vps.vm.ImportMeetingVM` | — | `IMeeting`, `ISysOrganization`, `ISysUser` | LEGACY |
| `meeting/list/approveMeetingWeek.zul` | `vm.meeting.MeetingListVM` | — | — | ☠ VM không tồn tại |
| `meeting/list/commander.zul` | `vm.meeting.MeetingListVM` | — | — | ☠ VM không tồn tại |
| `meeting/list/meetingList_search.zul` | `vm.meeting.MeetingListVM` | — | — | ☠ VM không tồn tại |
| `meeting/meetingApprovalExport/meetingApprovalExport.zul` | `vm.meeting.MeetingExportVM` | `MeetingBusiness` | `IMeeting`, `ISysUser` | BE+LEGACY |
| `meeting/meetingApprovalExport/meetingOnDuty.zul` | `vm.meeting.MeetingOnDutyVM` | — | `IMeeting` | LEGACY |
| `meeting/meetingApproverConfig.zul` | `vm.meeting.MeetingApproverConfigVM` | `MeetingBusiness` | `ISysUser` | BE+LEGACY |
| `meeting/meetingComplementReport/meetingComplementReport.zul` | `vm.meeting.MeetingComplementReportVM` | `MeetingBusiness` | — | BE |
| `meeting/meetingComplementReport/meetingComplementReportLookup.zul` | `vm.meeting.MeetingComplementReportLookupVM` | — | `IMeeting`, `IMeetingComplementReport` | LEGACY |
| `meeting/meetingComplementReport/meetingGeneralComplementReportLookup.zul` | `vm.meeting.MeetingGeneralComplementReportLookUpVM` | — | `IMeetingComplementReport` | LEGACY |
| `meeting/meetingComplementReport/meeting_complement_report.zul` | `vm.meeting.MeetingWeekVM` | `DocumentBusiness`, `MeetingBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/meetingFrequency/meetingFrequency.zul` | `vm.meeting.MeetingFrequencyVM` | — | `IMeetingFrequency` | LEGACY |
| `meeting/meetingFrequency/meetingFrequencyAlarm.zul` | `vm.meeting.MeetingFrequencyAlarmVM` | — | — | — |
| `meeting/meetingFrequency/meetingFrequencyReport.zul` | `vm.meeting.MeetingFrequencyReportVM` | `MeetingBusiness` | `IMeeting`, `IMeetingFrequency` | BE+LEGACY |
| `meeting/meetingLock/meetingLock.zul` | `vm.meeting.MeetingLockVM` | — | `ICommonVoffice`, `IMeeting`, `ISysUser` | LEGACY |
| `meeting/meetingMemberConfig.zul` | `vm.meeting.MeetingMemberConfigVM` | `MeetingConfigAddBusiness` | — | BE |
| `meeting/meetingMemberConfig/meetingConfigAdd_detail.zul` | `vm.meeting.MeetingMemberConfigVM` | `MeetingConfigAddBusiness` | — | BE |
| `meeting/meetingResource/meetingResource.zul` | `vm.meeting.MeetingResourceVM` | `MeetingResourceBusiness` | `IMeeting` | BE+LEGACY |
| `meeting/meetingSame/meeting_same.zul` | `vm.meeting.MeetingSameVM` | — | — | — |
| `meeting/meetingWeek.zul` | `vm.meeting.MeetingWeekVM` | `DocumentBusiness`, `MeetingBusiness`, `NotificationBusiness`, `RequisitionBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/meetingWeekManager.zul` | `vm.meeting.MeetingWeekManagerVM` | `MeetingBusiness` | `IMeeting` | BE+LEGACY |
| `meeting/meetingWeekOrganization.zul` | `vm.meeting.MeetingWeekOrganizationVM` | `MeetingBusiness`, `PublicMeetingBusiness` | `IMeeting` | BE+LEGACY |
| `meeting/meeting_add.zul` | `vm.meeting.MeetingVM` | `DocumentBusiness`, `MeetingBusiness`, `SearchSolrBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/meeting_detail.zul` | `vm.meeting.MeetingDetailVM` | `MeetingAssistantBusiness`, `MeetingBusiness`, `MeetingConfigAddBusiness`, `SavePersonalDocBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/meeting_detail_save_per_doc.zul` | `vm.meeting.MeetingDetailVM` | `MeetingAssistantBusiness`, `MeetingBusiness`, `MeetingConfigAddBusiness`, `SavePersonalDocBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/meeting_room_viewdetail.zul` | `vm.meeting.MeetingRoomViewDetailVM` | — | — | — |
| `meeting/popup/addFiles.zul` | `vm.meeting.AddFilesVM` | `MeetingBusiness` | — | BE |
| `meeting/popup/approveTaskReason.zul` | `vm.task.PopupReasonApproveTaskVM` | `TaskBusiness` | — | BE |
| `meeting/popup/commanderPopup.zul` | `vm.meeting.MeetingCommanderLookUpVM` | — | `ICommon` | LEGACY |
| `meeting/popup/meetingReason.zul` | `vm.meeting.MeetingReasonVM` | `MeetingBusiness`, `SysUserBusiness` | `IMeeting` | BE+LEGACY |
| `meeting/popup/meeting_assign.zul` | `vm.meeting.MeetingDetailVM` | `MeetingAssistantBusiness`, `MeetingBusiness`, `MeetingConfigAddBusiness`, `SavePersonalDocBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `meeting/popup/popupMeetingConclustion.zul` | `vm.meeting.MeetingConclustionVM` | `MeetingBusiness` | `ISysUser` | BE+LEGACY |
| `meeting/popup/rejectTaskReason.zul` | `vm.task.PopupReasonRejectTaskVM` | `TaskBusiness` | — | BE |
| `meeting/popup/removeConferenceReason.zul` | `vm.meeting.RemoveVideoConfereneReasonVM` | — | — | — |
| `meeting/popup/roomListPopup.zul` | `widget.VideoConferenceGroupLookupVM` | — | `IMeeting`, `IVideoConferenceGroup` | LEGACY |
| `meeting/popup/room_add.zul` | `widget.MeetingResourceLookupVM` | `MeetingBusiness` | `IMeeting` | BE+LEGACY |
| `meeting/popup/sendSmsMeetingAssign.zul` | `vm.meeting.MeetingSendNotifyAssignVM` | — | `ICommon`, `IMeeting` | LEGACY |
| `meeting/popup/sysOrgLookupMeeting.zul` | `widget.SysOrganizationLookupVM` | — | `ISysOrganization` | LEGACY |
| `meeting/popup/sysOrgLookupMeetingAssign.zul` | `widget.MeetingSysOrganizationLookupVM` | — | `ISysOrganization` | LEGACY |
| `meeting/popup/userLookupMeeting.zul` | `widget.UserLookupVM` | `CategoryCommonBusiness` | `ISysUser` | BE+LEGACY |
| `meeting/popup/viewMeetingChangeHistory.zul` | `widget.MeetingChangeHistoryVM` | — | — | — |
| `meeting/videoConferenceGroup/videoConferenceGroup.zul` | `vm.meeting.VideoConferenceGroupVM` | — | `IMeeting`, `IVideoConferenceGroup` | LEGACY |
| `meetingAssistant/leaderFollowing.zul` | `vm.leaderConfig.LeaderFollowingVM` | `MeetingAssistantBusiness` | — | BE |
| `meetingAssistant/meetingAssistant.zul` | `vm.leaderConfig.MeetingAssistantVM` | `MeetingAssistantBusiness` | — | BE |
| `meetingAssistant/meetingAsssitantChangeMember.zul` | `vm.meeting.MeetingAsssitantChangeMemberVM` | `MeetingAssistantBusiness` | — | BE |
| `meetingAssistant/meetingAsssitantChange_detail.zul` | `vm.meeting.MeetingAsssitantChangeDetailVM` | `MeetingAssistantBusiness` | — | BE |
| `meetingAssistant/scheduleConfig.zul` | `vm.leaderConfig.ScheduleConfigVM` | `ScheduleConfigBusiness` | — | BE |
| `widgets/editMeetingMinutesTarget.zul` | `vm.mission.PopupEditMeetingMinutesTargetVM` | — | — | — |
| `widgets/editVideoConferenceCode.zul` | `widget.EditVideoConferenceCodeVM` | `MeetingBusiness` | `IMeeting` | BE+LEGACY |
| `widgets/popupViewMeetingMinutesInfo.zul` | `vm.mission.MeetingMinutesVM` | `DocumentBusiness`, `MeetingBusiness`, `MissionBusiness`, `SearchSolrBusiness` | — | BE |
| `widgets/sourceLookupMeetingMinutes.zul` | `widget.SourceLookupMeetingMinuteVM` | `MeetingBusiness` | — | BE |
| `widgets/assignDirectorToMeetingLookup.zul` | `widget.AssignDirectorLookupVM` | — | — | ☠ VM không tồn tại |
| `widgets/meetingRoomImage.zul` | `vm.meeting.MeetingRoomImageVM` | — | — | — |
| `widgets/updateInfoCreateMeeting.zul` | `widget.UpdateInfoCreateMeetingVM` | `DocumentBusiness`, `ScheduleToMeetingDocumentBusiness` | — | BE |
| `widgets/videoConferenceGroupLookup.zul` | `widget.VideoConferenceGroupLookupVM` | — | `IMeeting`, `IVideoConferenceGroup` | LEGACY |
| `widgets/videoConferenceRoomLookup.zul` | `widget.VideoConferenceRoomLookupVM` | — | `IMeeting`, `ISysOrganization` | LEGACY |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `util.vm.VoMeetingMinutesUtils` | — | `ICommonVoffice`, `IMeetingMinutes` | LEGACY |
| `vm.meeting.MeetingComparator` | — | — | — |
| `vm.meeting.MeetingGroupingModel` | — | — | — |
| `vm.meeting.MeetingStatusColor` | — | — | — |
| `vm.meeting.MeetingVmUtil` | `MeetingBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `ISysUser` | BE+LEGACY |
| `vm.meeting.PublicMeetingBusiness` | `MeetingBusiness` | `ICommon` | BE+LEGACY |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### MeetingAssistantBusiness

`web-spring/src/main/java/com/voffice/service/business/MeetingAssistantBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Meeting.getMissionByMeetingId` | `/Meeting/getMissionByMeetingId` | `MettingResource.getMissionByMeetingId` | gen1 |
| `MeetingAssistantAction.addAssistant` | `/MeetingAssistantAction/addAssistant` | `MeetingAssistantAction.addAssistant` | gen1 |
| `MeetingAssistantAction.approveReplateMember` | `/MeetingAssistantAction/approveReplateMember` | `MeetingAssistantAction.approveReplateMember` | gen1 |
| `MeetingAssistantAction.deleteAssistant` | `/MeetingAssistantAction/deleteAssistant` | `MeetingAssistantAction.deleteAssistant` | gen1 |
| `MeetingAssistantAction.findMeetingChangeReplate` | `/MeetingAssistantAction/findMeetingChangeReplate` | `MeetingAssistantAction.findMeetingChangeReplate` | gen1 |
| `MeetingAssistantAction.getDetailMeetingAssistant` | `/MeetingAssistantAction/getDetailMeetingAssistant` | `MeetingAssistantAction.getDetailMeetingAssistant` | gen1 |
| `MeetingAssistantAction.getExistAssistantChangeMeetByEmployeeId` | `/MeetingAssistantAction/getExistAssistantChangeMeetByEmployeeId` | `MeetingAssistantAction.getExistAssistantChangeMeetByEmployeeId` | gen1 |
| `MeetingAssistantAction.getLeaderByEmployee` | `/MeetingAssistantAction/getLeaderByEmployee` | `MeetingAssistantAction.getLeaderByEmployee` | gen1 |
| `MeetingAssistantAction.getListAssistant` | `/MeetingAssistantAction/getListAssistant` | `MeetingAssistantAction.getListAssistant` | gen1 |
| `MeetingAssistantAction.getMeetingAssistantList` | `/MeetingAssistantAction/getMeetingAssistantList` | `MeetingAssistantAction.getMeetingAssistantList` | gen1 |
| `MeetingAssistantAction.getMeetingChangeReplate` | `/MeetingAssistantAction/getMeetingChangeReplate` | `MeetingAssistantAction.getMeetingChangeReplate` | gen1 |
| `MeetingAssistantAction.searchAssistant` | `/MeetingAssistantAction/searchAssistant` | `MeetingAssistantAction.searchAssistant` | gen1 |
| `MeetingAssistantAction.searchFollowLeader` | `/MeetingAssistantAction/searchFollowLeader` | `MeetingAssistantAction.searchFollowLeader` | gen1 |
| `taskAction.getListTaskFromDocument` | `/taskAction/getListTaskFromDocument` | `TaskAction.getListTaskFromDocument` | gen1 |

### MeetingBusiness

`web-spring/src/main/java/com/voffice/service/business/MeetingBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `CvGroupAction.getListCvGroupByListId` | `/CvGroupAction/getListCvGroupByListId` | `CvGroupAction.getListCvGroupByListId` | gen1 |
| `Files.PreviewMeetingMinutes` | `/Files/PreviewMeetingMinutes` | `FileService.previewMeetingMinutes` | gen1 |
| `Meeting.GetListSource` | `/Meeting/GetListSource` | `MettingResource.getListSource` | gen1 |
| `Meeting.addOrEditMeetingMinutes` | `/Meeting/addOrEditMeetingMinutes` | `MettingResource.addOrEditMeetingMinutes` | gen1 |
| `Meeting.checkPermissionCreateOnlineRoom` | `/Meeting/checkPermissionCreateOnlineRoom` | `MettingResource.checkPermissionCreateOnlineRoom` | gen1 |
| `Meeting.createOnlineMeetingRoom` | `/Meeting/createOnlineMeetingRoom` | `MettingResource.createOnlineMeetingRoom` | gen1 |
| `Meeting.deleteCospaceInfo` | `/Meeting/deleteCospaceInfo` | `MettingResource.deleteCospaceInfo` | gen1 |
| `Meeting.deleteExpiredCTH` | `/Meeting/deleteExpiredCTH` | `MettingResource.deleteExpiredCTH` | gen1 |
| `Meeting.deleteMeetingMinutes` | `/Meeting/deleteMeetingMinutes` | `MettingResource.deleteMeetingMinutes` | gen1 |
| `Meeting.findMeetingNative` | `/Meeting/findMeetingNative` | `MettingResource.findMeetingNative` | gen1 |
| `Meeting.findMeetingResouresEmpty` | `/Meeting/findMeetingResouresEmpty` | `MettingResource.findMeetingResouresEmpty` | gen1 |
| `Meeting.getConferenceAssignOrder` | `/Meeting/getConferenceAssignOrder` | `MettingResource.getConferenceAssignOrder` | gen1 |
| `Meeting.getCospaceInfo` | `/Meeting/getCospaceInfo` | `MettingResource.getCospaceInfo` | gen1 |
| `Meeting.getDetailMeetingResource` | `/Meeting/getDetailMeetingResource` | `MettingResource.getDetailMeetingResource` | gen1 |
| `Meeting.getDirectorConfig` | `/Meeting/getDirectorConfig` | `MettingResource.getDirectorConfig` | gen1 |
| `Meeting.getListFileAttachment` | `/Meeting/getListFileAttachment` | `MettingResource.getListFileAttachment` | gen1 |
| `Meeting.getListFileMeeting` | `/Meeting/getListFileMeeting` | `MettingResource.getListFileMeeting` | gen1 |
| `Meeting.getListMeetingByMemberIds` | `/Meeting/getListMeetingByMemberIds` | `MettingResource.getListMeetingByMemberIds` | gen1 |
| `Meeting.getListMeetingChangeHistory` | `/Meeting/getListMeetingChangeHistory` | `MettingResource.getListMeetingChangeHistory` | gen1 |
| `Meeting.getListMeetingHasDirector` | `/Meeting/getListMeetingHasDirector` | `MettingResource.getListMeetingHasDirector` | gen1 |
| `Meeting.getListMeetingMinutes` | `/Meeting/getListMeetingMinutes` | `MettingResource.getListMeetingMinutes` | gen1 |
| `Meeting.getListUserMeeting` | `/Meeting/getListUserMeeting` | `MettingResource.getListUserMeeting` | gen1 |
| `Meeting.getListUserViewFile` | `/Meeting/getListUserViewFile` | `MettingResource.getListUserViewFile` | gen1 |
| `Meeting.getManageVideoConferenceIds` | `/Meeting/getManageVideoConferenceIds` | `MettingResource.getManageVideoConferenceIds` | gen1 |
| `Meeting.getMeetingMemberConflict` | `/Meeting/getMeetingMemberConflict` | `MettingResource.getMeetingMemberConflict` | gen1 |
| `Meeting.getMeetingMemberOrderView` | `/Meeting/getMeetingMemberOrderView` | `MettingResource.getMeetingMemberOrderView` | gen1 |
| `Meeting.getMeetingMemberPermissionFile` | `/Meeting/getMeetingMemberPermissionFile` | `MettingResource.getMeetingMemberPermissionFile` | gen1 |
| `Meeting.getMeetingMembers` | `/Meeting/getMeetingMembers` | `MettingResource.getMeetingMembers` | gen1 |
| `Meeting.getMeetingMembersRemoveVideoConfId` | `/Meeting/getMeetingMembersRemoveVideoConfId` | `MettingResource.getMeetingMembersRemoveVideoConfId` | gen1 |
| `Meeting.getMeetingMinutesById` | `/Meeting/getMeetingMinutesById` | `MettingResource.getMeetingMinutesById` | gen1 |
| `Meeting.getMeetingVideoConferenceAssign` | `/Meeting/getMeetingVideoConferenceAssign` | `MettingResource.getMeetingVideoConferenceAssign` | gen1 |
| `Meeting.getMeetingsByDocId` | `/Meeting/getMeetingsByDocId` | `MettingResource.getMeetingsByDocId` | gen1 |
| `Meeting.getMissionByMeetingId` | `/Meeting/getMissionByMeetingId` | `MettingResource.getMissionByMeetingId` | gen1 |
| `Meeting.getOnlineMeetingLink` | `/Meeting/getOnlineMeetingLink` | `MettingResource.getOnlineMeetingLink` | gen1 |
| `Meeting.handleCiscoMeeting` | `/Meeting/handleCiscoMeeting` | `MettingResource.handleCiscoMeeting` | gen1 |
| `Meeting.insertMeetingChangeHistory` | `/Meeting/insertMeetingChangeHistory` | `MettingResource.unLockDocument` | gen1 |
| `Meeting.insertMeetingFiles` | `/Meeting/insertMeetingFiles` | `MettingResource.insertMeetingFiles` | gen1 |
| `Meeting.listRoomIdsUserManageVideoConference` | `/Meeting/listRoomIdsUserManageVideoConference` | `MettingResource.listRoomIdsUserManageVideoConference` | gen1 |
| `Meeting.permissionRollCall` | `/Meeting/permissionRollCall` | `MettingResource.permissionRollCall` | gen1 |
| `Meeting.removeMeetingVideoConference` | `/Meeting/removeMeetingVideoConference` | `MettingResource.removeMeetingVideoConference` | gen1 |
| `Meeting.removePermissionViewFile` | `/Meeting/removePermissionViewFile` | `MettingResource.removePermissionViewFile` | gen1 |
| `Meeting.requestForSigningMeetingMinutes` | `/Meeting/requestForSigningMeetingMinutes` | `MettingResource.requestForSigningMeetingMinutes` | gen1 |
| `Meeting.sendNotification` | `/Meeting/sendNotification` | `MettingResource.sendNotification` | gen1 |
| `Meeting.updateAdditionalMeetingColumn` | `/Meeting/updateAdditionalMeetingColumn` | `MettingResource.updateAdditionalMeetingColumn` | gen1 |
| `Meeting.updateBoardNameSmartRoom` | `/Meeting/updateBoardNameSmartRoom` | `MettingResource.updateBoardNameSmartRoom` | gen1 |
| `Meeting.updateCospaceMeetingInfo` | `/Meeting/updateCospaceMeetingInfo` | `MettingResource.updateCospaceMeetingInfo` | gen1 |
| `Meeting.updateMeetingMinutes` | `/Meeting/updateMeetingMinutes` | `MettingResource.updateMeetingMinutes` | gen1 |
| `Meeting.updateMemberReplate` | `/Meeting/updateMemberReplate` | `MettingResource.updateMemberReplate` | gen1 |
| `Meeting.updateSendMailMemberList` | `/Meeting/updateSendMailMemberList` | `MettingResource.updateSendMailMemberList` | gen1 |
| `Meeting.updateStateFiles` | `/Meeting/updateStateFiles` | `MettingResource.updateStateFiles` | gen1 |
| `MettingWeek.GetMeetingListByText` | `/MettingWeek/GetMeetingListByText` | `MettingWeek.getMeetingListByText` | gen1 |
| `MettingWeek.checkUpdateWithoutConclusions` | `/MettingWeek/checkUpdateWithoutConclusions` | `MettingWeek.checkUpdateWithoutConclusions` | gen1 |
| `MettingWeek.filterMeetingTextByCreator` | `/MettingWeek/filterMeetingTextByCreator` | `MettingWeek.filterMeetingTextByCreator` | gen1 |
| `MettingWeek.getFileMeetingWeek` | `/MettingWeek/getFileMeetingWeek` | `MettingWeek.getFileMeetingWeek` | gen1 |
| `MettingWeek.getLeaderIdForAssistantUser` | `/MettingWeek/getLeaderIdForAssistantUser` | `MettingWeek.getLeaderIdForAssistantUser` | gen1 |
| `MettingWeek.getListCalendarDirectorOrgs` | `/MettingWeek/getListCalendarDirectorOrgs` | `MettingWeek.getListCalendarDirectorOrgs` | gen1 |
| `MettingWeek.getListCalendarWeekOrgs` | `/MettingWeek/getListCalendarWeekOrgs` | `MettingWeek.getListCalendarWeekOrgs` | gen1 |
| `MettingWeek.getListMeetingCommander` | `/MettingWeek/getListMeetingCommander` | `MettingWeek.getListMeetingCommander` | gen1 |
| `MettingWeek.getLstDocumentByLstMeeting` | `/MettingWeek/getLstDocumentByLstMeeting` | `MettingWeek.getLstDocumentByLstMeeting` | gen1 |
| `MettingWeek.getLstMeetingWeek` | `/MettingWeek/getLstMeetingWeek` | `MettingWeek.getLstMeetingWeek` | gen1 |
| `MettingWeek.getLstMissionCreatedByConclusionDocuments` | `/MettingWeek/getLstMissionCreatedByConclusionDocuments` | `MettingWeek.getLstMissionCreatedByConclusionDocuments` | gen1 |
| `MettingWeek.getLstMissionCreatedFromDirectMeetingMinutes` | `/MettingWeek/getLstMissionCreatedFromDirectMeetingMinutes` | `MettingWeek.getLstMissionCreatedFromDirectMeetingMinutes` | gen1 |
| `MettingWeek.getNoteBookDetail` | `/MettingWeek/getNoteBookDetail` | `MettingWeek.getNoteBookDetail` | gen1 |
| `MettingWeek.saveMeetingComander` | `/MettingWeek/saveMeetingComander` | `MettingWeek.saveMeetingComander` | gen1 |
| `MettingWeek.saveMeetingNoteBook` | `/MettingWeek/saveMeetingNoteBook` | `MettingWeek.saveMeetingNoteBook` | gen1 |
| `MettingWeek.updateWithoutConclusions` | `/MettingWeek/updateWithoutConclusions` | `MettingWeek.updateWithoutConclusions` | gen1 |
| `MettingWeek.uploadFileMeetingWeek` | `/MettingWeek/uploadFileMeetingWeek` | `MettingWeek.uploadFileMeetingWeek` | gen1 |
| `VHROrgAction.getVhrOrgByRole` | `/VHROrgAction/getVhrOrgByRole` | `IndexController.redirect` | gen2 |
| `api.ecabinet.check-coincide-location` | `/api/ecabinet/check-coincide-location` | `EcabinetController.checkCoincideLocation` | gen2 |
| `api.meet.cancel-ecabinet-conference` | `/api/meet/cancel-ecabinet-conference` | `MeetController.cancelEcabinetConference` | gen2 |
| `api.meet.get-ecabinet-conference` | `/api/meet/get-ecabinet-conference` | `MeetController.getEcabinetConference` | gen2 |
| `api.meet.save-ecabinet-conference` | `/api/meet/save-ecabinet-conference` | `MeetController.createOrUpdateEcabinetConference` | gen2 |
| `meetingApproverAction.getListMeetingApprover` | `/meetingApproverAction/getListMeetingApprover` | `MeetingApproverAction.getListMeetingApprover` | gen1 |
| `meetingApproverAction.getUserApproval` | `/meetingApproverAction/getUserApproval` | `MeetingApproverAction.getUserApproval` | gen1 |
| `meetingApproverAction.saveMeetingApprover` | `/meetingApproverAction/saveMeetingApprover` | `MeetingApproverAction.saveMeetingApprover` | gen1 |
| `meetingResourceAction.checkExistMapId` | `/meetingResourceAction/checkExistMapId` | `MeetingResourceAction.checkExistMapId` | gen1 |
| `staffAction.getLeaderByOrg` | `/staffAction/getLeaderByOrg` | `StaffAction.getLeaderByOrg` | gen1 |

### MeetingConfigAddBusiness

`web-spring/src/main/java/com/voffice/service/business/MeetingConfigAddBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `MeetingConfigAdd.checkExists` | `/MeetingConfigAdd/checkExists` | `MeetingConfigAddAction.checkExistMeetingConfig` | gen1 |
| `MeetingConfigAdd.delete` | `/MeetingConfigAdd/delete` | `MeetingConfigAddAction.deleteMeetingConfigAdd` | gen1 |
| `MeetingConfigAdd.insert` | `/MeetingConfigAdd/insert` | `MeetingConfigAddAction.insertMeetingConfigAdd` | gen1 |
| `MeetingConfigAdd.listConfiguredMeetingOrgMembers` | `/MeetingConfigAdd/listConfiguredMeetingOrgMembers` | `MeetingConfigAddAction.listConfiguredMeetingOrgMembers` | gen1 |
| `MeetingConfigAdd.search` | `/MeetingConfigAdd/search` | `MeetingConfigAddAction.getListMeetingConfigAdd` | gen1 |
| `MeetingConfigAdd.searchAdvance` | `/MeetingConfigAdd/searchAdvance` | `MeetingConfigAddAction.searchAdvance` | gen1 |
| `MeetingConfigAdd.update` | `/MeetingConfigAdd/update` | `MeetingConfigAddAction.updateMeetingConfigAdd` | gen1 |
| `VHROrgAction.getMeetingManagerVhrOrg` | `/VHROrgAction/getMeetingManagerVhrOrg` | `VHROrgAction.getMeetingManagerVhrOrg` | gen1 |

### MeetingResourceBusiness

`web-spring/src/main/java/com/voffice/service/business/MeetingResourceBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `meetingResourceAction.getFileInforById` | `/meetingResourceAction/getFileInforById` | `MeetingResourceAction.getFileInforById` | gen1 |
| `meetingResourceAction.saveImage` | `/meetingResourceAction/saveImage` | `MeetingResourceAction.saveImage` | gen1 |

### ScheduleConfigBusiness

`web-spring/src/main/java/com/voffice/service/business/ScheduleConfigBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `MeetingAssistantAction.addBlockEmailSms` | `/MeetingAssistantAction/addBlockEmailSms` | `MeetingAssistantAction.addBlockEmailSms` | gen1 |
| `MeetingAssistantAction.deleteAdvancedBlockEmailSms` | `/MeetingAssistantAction/deleteAdvancedBlockEmailSms` | `MeetingAssistantAction.deleteBlockEmailSms` | gen1 |
| `MeetingAssistantAction.editBlockEmailSms` | `/MeetingAssistantAction/editBlockEmailSms` | `MeetingAssistantAction.editBlockEmailSms` | gen1 |
| `MeetingAssistantAction.searchAdvancedBlockEmailSms` | `/MeetingAssistantAction/searchAdvancedBlockEmailSms` | `MeetingAssistantAction.searchAdvancedBlockEmailSms` | gen1 |
| `MeetingAssistantAction.searchBlockEmailSms` | `/MeetingAssistantAction/searchBlockEmailSms` | `MeetingAssistantAction.searchBlockEmailSms` | gen1 |
| `VHROrgAction.getVhrLeaderByUserId` | `/VHROrgAction/getVhrLeaderByUserId` | `VHROrgAction.getVhrLeaderByUserId` | gen1 |
| `VHROrgAction.getVhrOrgUserAdminSchedule` | `/VHROrgAction/getVhrOrgUserAdminSchedule` | `VHROrgAction.getVhrOrgUserAdminSchedule` | gen1 |
| `VHROrgAction.validateAddScheduleLeader` | `/VHROrgAction/validateAddScheduleLeader` | `VHROrgAction.validateAddScheduleLeader` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### MeetingApproverAction (gen1) — base `/meetingApproverAction`, 3 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MeetingApproverAction.java`

- Logic (gen-1 `controler/`): `MeetingWeekController`, `LogActionControler`
- DAO (SQL thuần): `ActionLogMobileDAO`, `CiscoMeetingDAO`, `CommonDataBaseDaoVO2`, `DocumentDAO`, `FileAttachmentDAO`, `LogActionDao`, `MeetingDAO`, `MeetingWeekDAO`, `OrgDAO`, `UserDAO`, `UserRoleDAO`
- Repository (JPA): `MeetingMemberRepositoryJPA`, `MeetingWeeklyRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `P12_CERT`, `PERMISSION_DATA`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `meeting_weekly`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/meetingApproverAction/saveMeetingApprover` | `saveMeetingApprover` |
| POST | `/meetingApproverAction/getListMeetingApprover` | `getListMeetingApprover` |
| POST | `/meetingApproverAction/getUserApproval` | `getUserApproval` |

</details>

### MeetingAssistantAction (gen1) — base `/MeetingAssistantAction`, 18 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MeetingAssistantAction.java`

- Logic (gen-1 `controler/`): `MeetingAssistantController`, `CommonControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `DocumentInGroupDAO`, `DocumentInStaffDAO`, `MeetingAssistantDAO`, `MeetingDAO`, `MeetingWeekDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `P12_CERT`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/MeetingAssistantAction/addAssistant` | `addAssistant` |
| POST | `/MeetingAssistantAction/deleteAssistant` | `deleteAssistant` |
| POST | `/MeetingAssistantAction/searchAssistant` | `searchAssistant` |
| POST | `/MeetingAssistantAction/searchAdvancedAssistant` | `searchAdvancedAssistant` |
| POST | `/MeetingAssistantAction/getDetailMeetingAssistant` | `getDetailMeetingAssistant` |
| POST | `/MeetingAssistantAction/addBlockEmailSms` | `addBlockEmailSms` |
| POST | `/MeetingAssistantAction/searchBlockEmailSms` | `searchBlockEmailSms` |
| POST | `/MeetingAssistantAction/searchAdvancedBlockEmailSms` | `searchAdvancedBlockEmailSms` |
| POST | `/MeetingAssistantAction/deleteAdvancedBlockEmailSms` | `deleteBlockEmailSms` |
| POST | `/MeetingAssistantAction/editBlockEmailSms` | `editBlockEmailSms` |
| POST | `/MeetingAssistantAction/getLeaderByEmployee` | `getLeaderByEmployee` |
| POST | `/MeetingAssistantAction/searchFollowLeader` | `searchFollowLeader` |
| POST | `/MeetingAssistantAction/getMeetingAssistantList` | `getMeetingAssistantList` |
| POST | `/MeetingAssistantAction/findMeetingChangeReplate` | `findMeetingChangeReplate` |
| POST | `/MeetingAssistantAction/getMeetingChangeReplate` | `getMeetingChangeReplate` |
| POST | `/MeetingAssistantAction/approveReplateMember` | `approveReplateMember` |
| POST | `/MeetingAssistantAction/getExistAssistantChangeMeetByEmployeeId` | `getExistAssistantChangeMeetByEmployeeId` |
| POST | `/MeetingAssistantAction/getListAssistant` | `getListAssistant` |

</details>

### MeetingConfigAddAction (gen1) — base `/MeetingConfigAdd`, 7 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MeetingConfigAddAction.java`

- Logic (gen-1 `controler/`): `MeetingConfigAddController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `MeetingConfigAddDAO`
- Bảng (ước lượng từ SQL/@Table): `MEETINGCONFIGADD`, `MEETING_CONFIG_ADD`, `MEETING_MEMBER`, `MEETING_ORG_MEMBER_ADD`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/MeetingConfigAdd/search` | `getListMeetingConfigAdd` |
| POST | `/MeetingConfigAdd/searchAdvance` | `searchAdvance` |
| POST | `/MeetingConfigAdd/checkExists` | `checkExistMeetingConfig` |
| POST | `/MeetingConfigAdd/insert` | `insertMeetingConfigAdd` |
| POST | `/MeetingConfigAdd/update` | `updateMeetingConfigAdd` |
| POST | `/MeetingConfigAdd/delete` | `deleteMeetingConfigAdd` |
| POST | `/MeetingConfigAdd/listConfiguredMeetingOrgMembers` | `listConfiguredMeetingOrgMembers` |

</details>

### MeetingResourceAction (gen1) — base `/meetingResourceAction`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MeetingResourceAction.java`

- Logic (gen-1 `controler/`): `MeetingResourceController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `MeetingResourceDAO`
- Bảng (ước lượng từ SQL/@Table): `FILES`, `MEETING_RESOURCE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/meetingResourceAction/saveImage` | `saveImage` |
| POST | `/meetingResourceAction/getFileInforById` | `getFileInforById` |
| GET | `/meetingResourceAction/DownloadImage/{fileId}` | `downloadSignatureImage` |
| GET | `/meetingResourceAction/downloadImageByMeetingResourceId/{meetingResourceId}` | `downloadImageByMeetingResourceId` |
| POST | `/meetingResourceAction/checkExistMapId` | `checkExistMapId` |

</details>

### MeetingWeekAction (gen1) — base `/MeetingWeekAction`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MeetingWeekAction.java`

- Logic (gen-1 `controler/`): `MeetingController`, `CommonControler`, `LogActionControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`, `EcabinetService`, `EcabinetServiceImpl`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AgreementDAO`, `CiscoMeetingDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `DocumentSignDAO`, `LogActionDao`, `MeetingDAO`, `MeetingMinutesDAO`, `MeetingNativeDAO`, `MeetingWeekDAO`, `MissionDAO`, `ObjectTransferViaAxisDAO`, `OrgDAO`, `RequestDAO`, `SourceMapDAO`, `StaffDAO`, `TextDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/MeetingWeekAction/getMeetingList` | `getMeetingList` |

</details>

### MettingResource (gen1) — base `/Meeting`, 68 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MettingResource.java`

- Logic (gen-1 `controler/`): `MeetingController`, `CommonControler`, `LogActionControler`
- Service: `DocCommentService`, `DocCommentServiceImpl`, `EcabinetService`, `EcabinetServiceImpl`
- DAO (SQL thuần): `ActionLogMobileDAO`, `AgreementDAO`, `CiscoMeetingDAO`, `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `DocumentSignDAO`, `LogActionDao`, `MeetingDAO`, `MeetingMinutesDAO`, `MeetingNativeDAO`, `MeetingWeekDAO`, `MissionDAO`, `ObjectTransferViaAxisDAO`, `OrgDAO`, `RequestDAO`, `SourceMapDAO`, `StaffDAO`, `TextDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Meeting/getListMeetingMinutes` | `getListMeetingMinutes` |
| POST | `/Meeting/getMissionByMeetingId` | `getMissionByMeetingId` |
| POST | `/Meeting/getMeetingMinutesById` | `getMeetingMinutesById` |
| POST | `/Meeting/countListMeetingMinutes` | `countListMeetingMinutes` |
| POST | `/Meeting/countMissionByMeetingId` | `countMissionByMeetingId` |
| POST | `/Meeting/getListFileAttachment` | `getListFileAttachment` |
| POST | `/Meeting/getListOrganizationByUser` | `getListOrganizationByUser` |
| POST | `/Meeting/getListOrganization` | `getListOrganization` |
| POST | `/Meeting/getListOrganizationAssign` | `getListOrganizationAssign` |
| POST | `/Meeting/getListField` | `getListField` |
| POST | `/Meeting/findMeetingResouresEmpty` | `findMeetingResouresEmpty` |
| POST | `/Meeting/addMission` | `addMission` |
| POST | `/Meeting/forwardMission` | `forwardMission` |
| POST | `/Meeting/getSourceMapMission` | `getSourceMapMission` |
| POST | `/Meeting/GetListSource` | `getListSource` |
| POST | `/Meeting/getDetailMeetingResource` | `getDetailMeetingResource` |
| POST | `/Meeting/deleteMeetingMinutes` | `deleteMeetingMinutes` |
| POST | `/Meeting/addOrEditMeetingMinutes` | `addOrEditMeetingMinutes` |
| POST | `/Meeting/getListOrganizationExecute` | `getListOrganizationExecute` |
| POST | `/Meeting/getListOrganizationsAssign` | `getListOrganizationsAssign` |
| POST | `/Meeting/getListOrgPerformInAdvanceSearch` | `getListOrgPerformInAdvanceSearch` |
| POST | `/Meeting/updateMeetingMinutes` | `updateMeetingMinutes` |
| POST | `/Meeting/requestForSigningMeetingMinutes` | `requestForSigningMeetingMinutes` |
| POST | `/Meeting/getMeetingsByDocId` | `getMeetingsByDocId` |
| POST | `/Meeting/getListUserMeeting` | `getListUserMeeting` |
| POST | `/Meeting/manualRollCallMeeting` | `manualRollCallMeeting` |
| POST | `/Meeting/autoRollCallMeeting` | `autoRollCallMeeting` |
| POST | `/Meeting/changeMemberMeeting` | `changeMemberMeeting` |
| POST | `/Meeting/checkAttendMeeting` | `checkAttendMeeting` |
| POST | `/Meeting/updateStateFiles` | `updateStateFiles` |
| POST | `/Meeting/permissionRollCall` | `permissionRollCall` |
| POST | `/Meeting/getContentMeetingMember` | `getContentMeetingMember` |
| POST | `/Meeting/getListAbsenceMember` | `getListAbsenceMember` |
| POST | `/Meeting/getDirectorConfig` | `getDirectorConfig` |
| POST | `/Meeting/updateMemberReplate` | `updateMemberReplate` |
| POST | `/Meeting/getListFileMeeting` | `getListFileMeeting` |
| POST | `/Meeting/insertMeetingFiles` | `insertMeetingFiles` |
| POST | `/Meeting/removePermissionViewFile` | `removePermissionViewFile` |
| POST | `/Meeting/getListUserViewFile` | `getListUserViewFile` |
| POST | `/Meeting/updateBoardNameSmartRoom` | `updateBoardNameSmartRoom` |
| POST | `/Meeting/getMeetingMemberPermissionFile` | `getMeetingMemberPermissionFile` |
| POST | `/Meeting/getDirectorConfigById` | `getDirectorConfigById` |
| POST | `/Meeting/getMeetingMemberOrderView` | `getMeetingMemberOrderView` |
| POST | `/Meeting/findMeetingNative` | `findMeetingNative` |
| POST | `/Meeting/getMeetingMembers` | `getMeetingMembers` |
| POST | `/Meeting/getListMeetingHasDirector` | `getListMeetingHasDirector` |
| POST | `/Meeting/getMeetingMemberConflict` | `getMeetingMemberConflict` |
| POST | `/Meeting/getListMeetingByMemberIds` | `getListMeetingByMemberIds` |
| POST | `/Meeting/getMeetingVideoConferenceAssign` | `getMeetingVideoConferenceAssign` |
| POST | `/Meeting/removeMeetingVideoConference` | `removeMeetingVideoConference` |
| POST | `/Meeting/getManageVideoConferenceIds` | `getManageVideoConferenceIds` |
| POST | `/Meeting/getMeetingMembersRemoveVideoConfId` | `getMeetingMembersRemoveVideoConfId` |
| POST | `/Meeting/updateSendMailMemberList` | `updateSendMailMemberList` |
| POST | `/Meeting/checkPermissionCreateOnlineRoom` | `checkPermissionCreateOnlineRoom` |
| POST | `/Meeting/getOnlineMeetingLink` | `getOnlineMeetingLink` |
| POST | `/Meeting/createOnlineMeetingRoom` | `createOnlineMeetingRoom` |
| POST | `/Meeting/handleCiscoMeeting` | `handleCiscoMeeting` |
| POST | `/Meeting/getCospaceInfo` | `getCospaceInfo` |
| POST | `/Meeting/updateCospaceMeetingInfo` | `updateCospaceMeetingInfo` |
| POST | `/Meeting/listRoomIdsUserManageVideoConference` | `listRoomIdsUserManageVideoConference` |
| POST | `/Meeting/deleteCospaceInfo` | `deleteCospaceInfo` |
| POST | `/Meeting/deleteExpiredCTH` | `deleteExpiredCTH` |
| POST | `/Meeting/getConferenceAssignOrder` | `getConferenceAssignOrder` |
| POST | `/Meeting/updateAdditionalMeetingColumn` | `updateAdditionalMeetingColumn` |
| POST | `/Meeting/insertMeetingChangeHistory` | `unLockDocument` |
| POST | `/Meeting/getListMeetingChangeHistory` | `getListMeetingChangeHistory` |
| POST | `/Meeting/insertMailMeetingHistory` | `insertMailMeetingHistory` |
| POST | `/Meeting/sendNotification` | `sendNotification` |

</details>

### MettingWeek (gen1) — base `/MettingWeek`, 51 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/MettingWeek.java`

- Logic (gen-1 `controler/`): `MeetingFileCommentControler`, `MeetingWeekController`, `LogActionControler`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `MeetingFileCommentDAO`, `TextFileCommentDAO`, `ActionLogMobileDAO`, `CiscoMeetingDAO`, `DocumentDAO`, `FileAttachmentDAO`, `LogActionDao`, `MeetingDAO`, `MeetingWeekDAO`, `OrgDAO`, `UserDAO`, `UserRoleDAO`
- Repository (JPA): `MeetingMemberRepositoryJPA`, `MeetingWeeklyRepositoryJPA`, `VhrEmployeeJPA`, `VhrOrgRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `P12_CERT`, `PERMISSION_DATA`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `meeting_weekly`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/MettingWeek/getLstMeetingWeek` | `getLstMeetingWeek` |
| POST | `/MettingWeek/uploadFileMeetingWeek` | `uploadFileMeetingWeek` |
| POST | `/MettingWeek/getFileMeetingWeek` | `getFileMeetingWeek` |
| POST | `/MettingWeek/getListCalendarDirectorOrgs` | `getListCalendarDirectorOrgs` |
| POST | `/MettingWeek/getListCalendarWeekOrgs` | `getListCalendarWeekOrgs` |
| POST | `/MettingWeek/getMeetingComanderResult` | `getMeetingComanderResult` |
| POST | `/MettingWeek/getWorkMeetingDirector` | `getWorkMeetingDirector` |
| POST | `/MettingWeek/get3MeetingNearestOnDashboard` | `get3MeetingNearestOnDashboard` |
| POST | `/MettingWeek/getMeetingDetail` | `getMeetingDetail` |
| POST | `/MettingWeek/GetListMeeting` | `getListMeeting` |
| POST | `/MettingWeek/getMeetingList` | `getMeetingList` |
| POST | `/MettingWeek/GetMeetingListByText` | `getMeetingListByText` |
| POST | `/MettingWeek/GetMeetingParticipantList` | `getMeetingParticipantList` |
| POST | `/MettingWeek/GetVideoConferencingList` | `getVideoConferencingList` |
| POST | `/MettingWeek/checkLeaderIdForAssistantUserInMemberList` | `checkLeaderIdForAssistantUserInMemberList` |
| POST | `/MettingWeek/getListApproveCalendar` | `getListApproveCalendar` |
| POST | `/MettingWeek/checkPermisionCalendar` | `checkPermisionCalendar` |
| POST | `/MettingWeek/approveCalendar` | `approveCalendar` |
| POST | `/MettingWeek/rejectCalendar` | `rejectCalendar` |
| POST | `/MettingWeek/cancelCalendar` | `cancelCalendar` |
| POST | `/MettingWeek/deleteCalendar` | `deleteCalendar` |
| POST | `/MettingWeek/getListLocationFree` | `getListLocationFree` |
| POST | `/MettingWeek/changeLocation` | `changeLocation` |
| POST | `/MettingWeek/checkConflictTimeUsedRoom` | `checkConflictTimeUsedRoom` |
| POST | `/MettingWeek/checkChangeOrgApproval` | `checkChangeOrgApproval` |
| POST | `/MettingWeek/checkDuplicateParticant` | `checkDuplicateParticant` |
| POST | `/MettingWeek/sendSMSMeetingWeek` | `sendSMSMeetingWeek` |
| POST | `/MettingWeek/sendMail` | `sendMailMeetingWeek` |
| POST | `/MettingWeek/checkDuplicateVideoConferenceRoom` | `checkDuplicateMeetingVideoConference` |
| POST | `/MettingWeek/checkDuplicateVideoConference` | `checkDuplicateVideoConference` |
| POST | `/MettingWeek/checkDuplicateRoomVideoConference` | `checkDuplicateRoomVideoConference` |
| POST | `/MettingWeek/validateSaveMeeting` | `validateSaveMeeting` |
| POST | `/MettingWeek/getMeetingForSmartRoom` | `getMeetingForSmartRoom` |
| POST | `/MettingWeek/updateFileMeetingComment` | `updateFileMeetingComment` |
| POST | `/MettingWeek/resetMeetingAttachComment` | `resetMeetingAttachComment` |
| POST | `/MettingWeek/getListMeetingNote` | `getListMeetingNote` |
| POST | `/MettingWeek/saveMeetingNoteBook` | `saveMeetingNoteBook` |
| POST | `/MettingWeek/updateOrDelMeetingNoteFile` | `updateOrDelMeetingNoteFile` |
| POST | `/MettingWeek/getMeetingRollCall` | `getMeetingRollCall` |
| POST | `/MettingWeek/getNoteBookDetail` | `getNoteBookDetail` |
| POST | `/MettingWeek/getLeaderIdForAssistantUser` | `getLeaderIdForAssistantUser` |
| POST | `/MettingWeek/saveMeetingComander` | `saveMeetingComander` |
| POST | `/MettingWeek/getListMeetingCommander` | `getListMeetingCommander` |
| POST | `/MettingWeek/saveMeetingApprover` | `saveMeetingApprover` |
| POST | `/MettingWeek/getListMeetingApprover` | `getListMeetingApprover` |
| POST | `/MettingWeek/getLstDocumentByLstMeeting` | `getLstDocumentByLstMeeting` |
| POST | `/MettingWeek/getLstMissionCreatedByConclusionDocuments` | `getLstMissionCreatedByConclusionDocuments` |
| POST | `/MettingWeek/getLstMissionCreatedFromDirectMeetingMinutes` | `getLstMissionCreatedFromDirectMeetingMinutes` |
| POST | `/MettingWeek/checkUpdateWithoutConclusions` | `checkUpdateWithoutConclusions` |
| POST | `/MettingWeek/updateWithoutConclusions` | `updateWithoutConclusions` |
| POST | `/MettingWeek/filterMeetingTextByCreator` | `filterMeetingTextByCreator` |

</details>

### EcabinetController (gen2) — base `/api/ecabinet`, 1 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/EcabinetController.java`

- Service: `EcabinetService`, `EcabinetServiceImpl`
- Bảng (ước lượng từ SQL/@Table): —

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/ecabinet/check-coincide-location` | `checkCoincideLocation` |

</details>

### MeetController (gen2) — base `/api/meet`, 10 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/MeetController.java`

- Service: `MeetService`, `MeetServiceImpl`, `EcabinetService`, `EcabinetServiceImpl`
- DAO (SQL thuần): `CiscoMeetingDAO`, `CommonDataBaseDaoVO2`, `DocumentDAO`, `MeetingDAO`, `MeetingWeekDAO`, `SmsDAO`
- Repository (JPA): `FileEcabinetRepositoryJPA`, `FilesRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `MeetingConfigRepositoryJPA`, `MeetingEmailRepositoryJPA`, `MeetingFrequencyRepositoryJPA`, `MeetingHistoryRepositoryJPA`, `MeetingMemberFilesRepositoryJPA`, `MeetingMemberRepositoryJPA`, `MeetingRepositoryJPA`, `MeetingResourceRepositoryJPA`, `NotificationRepositoryJPA`, `SmsMasterRepositoryJPA`, `SystemParameterRepositoryJPA`, `TimeZoneLocalJPA`, `UserRoleRepositoryJPA`, `VhrOrgJPA`, `VhrOrgRepositoryJPA`, `VideoConferenceGroupRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CONFIG_SMS_ORG`, `CONFIG_USER_DOCUMENT`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ECABINET`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `MAIL_MEETING_HISTORY`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_FREQUENCY`, `MEETING_HISTORY`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_PROCESS`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORIENTATION`, `PERMISSION_DATA`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_BOOK`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_PROCESS`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/meet/get-org-meet-detail` | `getOrgMeetDetail` |
| GET | `/api/meet/get-org-meet-member/{meet-id}` | `getOrgMeetMember` |
| GET | `/api/meet/get-meet-internal-participants/{meeting-id}` | `getMeetInternalParticipants` |
| POST | `/api/meet/update-meeting/{meetingId}` | `updateMeeting` |
| POST | `/api/meet/approve-meeting/{meetingId}` | `approveMeeting` |
| POST | `/api/meet/sync-meeting` | `syncMeeting` |
| POST | `/api/meet/count-sync-meeting` | `countSyncMeeting` |
| POST | `/api/meet/save-ecabinet-conference/{meetingId}` | `createOrUpdateEcabinetConference` |
| POST | `/api/meet/cancel-ecabinet-conference/{meetingId}` | `cancelEcabinetConference` |
| GET | `/api/meet/get-ecabinet-conference/{meetingId}` | `getEcabinetConference` |

</details>

### VoteController (gen2) — base `/api/vote`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/VoteController.java`

- Logic (gen-1 `controler/`): `CommonControler`
- Service: `VoteService`, `VoteServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `PermissionDataService`, `PermissionDataServiceImpl`
- DAO (SQL thuần): `CommonDAO`, `CommonDataBaseDaoVO2`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`
- Repository (JPA): `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `DocumentRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `MeetingMemberRepositoryJPA`, `MeetingRepositoryJPA`, `VoteOptionEmployeeRepositoryJPA`, `VoteOptionRepositoryJPA`, `VoteQuestionRepositoryJPA`, `VoteRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AUTO_DIGSIG_TRANSACTION`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_MARK`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_VALUES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_PROCESS`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `EXT_APP`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `GROUP_MAPPING`, `HOME_WIDGET`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MESSAGE`, `NOTICE`, `NOTIFICATION`, `P12_CERT`, `READ_NOTICE_HISTORY`, `SMS_BLACK_LIST`, `SMS_MASTER`, `STAFF`, `STAFF_GROUP_ROLE`, `SYSTEM_PARAMETER`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_NOTE`, `TEXT_PROCESS`, `TIME_ZONE_LOCAL`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VOTE`, `VOTE_OPTION`, `VOTE_OPTION_EMPLOYEE`, `VOTE_QUESTION`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/vote/insert-vote` | `insertVote` |
| POST | `/api/vote/answer-vote` | `answerVote` |
| POST | `/api/vote/get-lst-result-vote` | `getLstResultVote` |
| POST | `/api/vote/send-vote` | `sendVote` |
| POST | `/api/vote/get-lst-vote` | `getLstVote` |
| POST | `/api/vote/cancel-vote` | `cancelVote` |
| POST | `/api/vote/delete-vote` | `deleteVote` |
| POST | `/api/vote/check-vote` | `checkVote` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `MeetingAssistantFacade` | `IMeetingAssistant` | `MeetingAssistantService` | `MeetingAssistantJpaDao` | `MeetingAssistant (MEETING_ASSISTANT)` |
| `MeetingComplementReportFacade` | `IMeetingComplementReport` | `MeetingComplementReportService` | `MeetingComplementReportDetailJpaDao`, `MeetingComplementReportJpaDao` | `MeetingComplementReport (M_COMPLEMENT_REPORT)`, `MeetingComplementReportDetail (M_COMPLEMMENT_REPORT_DETAIL)` |
| `MeetingFacade` | `IMeeting` | `MeetingAssistantService`, `MeetingLockService`, `MeetingResourceService`, `MeetingService`, `SysUserService` | `MeetingAssistantJpaDao`, `MeetingLockJpaDao`, `MeetingResourceJpaDao`, `MeetingResourceManagerJpaDao`, `MeetingCommanderJpaDao`, `MeetingHistoryJpaDao`, `MeetingJpaDao`, `MeetingMemberJpaDao`, `SysOrganizationJpaDao`, `SysUserJpaDao`, `UserOrgMapJpaDao`, `UserRoleJpaDao`, `VHREmployeeJpaDao` | `Meeting (MEETING)`, `MeetingAssistant (MEETING_ASSISTANT)`, `MeetingCommander (MEETING_COMMANDER)`, `MeetingHistory (MEETING_HISTORY)`, `MeetingLock (MEETING_LOCK)`, `MeetingMember (MEETING_MEMBER)`, `MeetingResource (MEETING_RESOURCE)`, `MeetingResourceManager (MEETING_RESOURCE_MANAGER)`, `SysOrganization (VHR_ORG)`, `SysUser (VHR_EMPLOYEE)`, `UserOrgMap (USER_ORG_MAP)`, `UserRole (USER_ROLE)`, `VHREmployee (VHR_EMPLOYEE)` |
| `MeetingFrequencyFacade` | `IMeetingFrequency` | `MeetingFrequencyService` | `MeetingFrequencyJpaDao` | `MeetingFrequency (MEETING_FREQUENCY)` |
| `MeetingLockFacade` | — | — | — | — |
| `MeetingMinutesFacade` | `IMeetingMinutes` | `MeetingMinutesService` | `MeetingMinutesJpaDao`, `VoMeetingMinutesUtilsJpaDao` | `MeetingMinutes (MEETING_MINUTES)` |
| `VideoConferenceGroupFacade` | `IVideoConferenceGroup` | `VideoConferenceGroupService` | `VideoConferenceGroupJpaDao` | `VideoConferenceGroup (VIDEO_CONFERENCE_GROUP)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `FileEcabinetEntity`→`FILE_ECABINET`, `MeetingAssistantEntity`→`MEETING_ASSISTANT`, `MeetingConfigEntity`→`MEETING_CONFIG`, `MeetingEmailEntity`→`MEETING_EMAIL`, `MeetingEntity`→`MEETING`, `MeetingFrequencyEntity`→`MEETING_FREQUENCY`, `MeetingHistoryEntity`→`MEETING_HISTORY`, `MeetingMemberEntity`→`MEETING_MEMBER`, `MeetingMemberFilesEntity`→`MEETING_MEMBER_FILES`, `MeetingMinuteEntity`→`MEETING_MINUTES`, `MeetingResourceEntity`→`MEETING_RESOURCE`, `MeetingResourceManagerEntity`→`MEETING_RESOURCE_MANAGER`, `MeetingWeeklyEntity`→`meeting_weekly`, `VideoConferenceGroupEntity`→`VIDEO_CONFERENCE_GROUP`, `VoteEntity`→`VOTE`, `VoteOptionEmployeeEntity`→`VOTE_OPTION_EMPLOYEE`, `VoteOptionEntity`→`VOTE_OPTION`, `VoteQuestionEntity`→`VOTE_QUESTION`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Meeting`→`MEETING`, `MeetingAssistant`→`MEETING_ASSISTANT`, `MeetingCommander`→`MEETING_COMMANDER`, `MeetingComplementReport`→`M_COMPLEMENT_REPORT`, `MeetingComplementReportDetail`→`M_COMPLEMMENT_REPORT_DETAIL`, `MeetingEmail`→`MEETING_EMAIL`, `MeetingFrequency`→`MEETING_FREQUENCY`, `MeetingHistory`→`MEETING_HISTORY`, `MeetingLock`→`MEETING_LOCK`, `MeetingLockOrg`→`MEETING_LOCK_ORG`, `MeetingMember`→`MEETING_MEMBER`, `MeetingMinutes`→`MEETING_MINUTES`, `MeetingNotification`→`MEETING_NOTIFICATION`, `MeetingResource`→`MEETING_RESOURCE`, `MeetingResourceManager`→`MEETING_RESOURCE_MANAGER`, `MeetingWeekCalendar`→`MEETING_WEEK_CALENDAR`, `MeetingWeekCalendarFiles`→`MEETING_WEEK_CALENDAR_FILES`, `VideoConferenceGroup`→`VIDEO_CONFERENCE_GROUP`

**Tổng hợp bảng chạm tới**: `ACTION_LOG_SERVICE`, `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT`, `CHART_AGREEMENT_CUSTOMER`, `CHART_AGREEMENT_GROUP`, `CHART_AGREEMENT_NUMBER`, `CHART_AGREEMENT_PERMISSION`, `CHART_AGREEMENT_PROCESS`, `CHART_AGREEMENT_REVENUE`, `CHART_AGREEMENT_ROLE`, `CHART_AGREEMENT_TASK`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_DOC_OUT_DETAIL`, `CONNECT_DOC_OUT_FILES`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `DUOC`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FIELD`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ECABINET`, `FLOOR`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `MAIL_MEETING_HISTORY`, `MAPPING_RESOVLE`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETINGCONFIGADD`, `MEETING_APPROVER`, `MEETING_ASSISTANT`, `MEETING_CHANGE_HISTORY`, `MEETING_COMMANDER`, `MEETING_CONFIG`, `MEETING_CONFIG_ADD`, `MEETING_EMAIL`, `MEETING_FILES_COMMENT_DRAFF`, `MEETING_FREQUENCY`, `MEETING_HISTORY`, `MEETING_LOCK`, `MEETING_LOCK_ORG`, `MEETING_MEMBER`, `MEETING_MEMBER_FILES`, `MEETING_MEMBER_REPLATE`, `MEETING_MINUTES`, `MEETING_NOTEBOOK`, `MEETING_NOTE_FILE`, `MEETING_NOTIFICATION`, `MEETING_ORG_MEMBER_ADD`, `MEETING_OTHER`, `MEETING_RESOURCE`, `MEETING_RESOURCE_MANAGER`, `MEETING_WEEK_CALENDAR`, `MEETING_WEEK_CALENDAR_FILES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MISSION`, `MISSION_DETAIL`, `MISSION_LOG`, `MISSION_NORM`, `MISSION_PROCESS`, `MISSION_STATUS`, `MISSION_TEMPLATE_DETAIL`, `M_COMPLEMENT_REPORT`, `M_COMPLEMMENT_REPORT_DETAIL`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_COMBINATION_MAP`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `ORIENTATION`, `P12_CERT`, `PERFORM_ORG_AREA`, `PERMISSION_DATA`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REQUEST`, `REQUEST_EMAIL`, `REQUEST_EMP_CONFIG`, `REQUEST_ORG_CONFIG`, `REQUEST_PROCESS`, `RESOVLE_ISSUE`, `ROLE_PERMISSION_DATA`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FORM`, `SUBMISSION_MAP`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYSTIMESTAMP`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TASK`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `THEM`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`, `VIDEO_CONFERENCE_GROUP`, `VOTE`, `VOTE_OPTION`, `VOTE_OPTION_EMPLOYEE`, `VOTE_QUESTION`, `meeting_weekly`
