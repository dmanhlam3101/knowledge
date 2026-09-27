# Họp — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Biểu quyết trong họp (gen-2 gọn, tốt để copy) | `VoteController` `/api/vote/insert-vote`, `send-vote`, `answer-vote`, `get-lst-result-vote`, `cancel-vote`, `check-vote` → `VoteService`(Impl) → `Vote*RepositoryJPA` |
| Duyệt / từ chối / hủy lịch có kiểm quyền | gen-1 `MettingWeek.approveCalendar`, `rejectCalendar`, `cancelCalendar`, `checkPermisionCalendar` ← `MeetingBusiness` ← `vm/meeting/*Approve*VM` ❓ |
| Kiểm tra trùng tài nguyên (phòng, cầu truyền hình, thời gian) | `checkConflictTimeUsedRoom`, `getListLocationFree`, `checkDuplicateVideoConference`, gen-2 `ecabinet/check-coincide-location` |
| Điểm danh thủ công/tự động + danh sách vắng | `Meeting.manualRollCallMeeting`, `autoRollCallMeeting`, `getListAbsenceMember`, `permissionRollCall` |
| Biên bản có ký và sinh nhiệm vụ | `Meeting.addOrEditMeetingMinutes`, `requestForSigningMeetingMinutes`, `Files.PreviewMeetingMinutes`, `Meeting.addMission` + `vm/meeting/MeetingMinutes*VM`, `vm/mission/MeetingMinutesVM` |
| Người dự thay (ủy quyền) có phê duyệt | `MeetingAssistantAction.addAssistant`, `approveReplateMember`, `updateMemberReplate` + `meetingAssistant/*.zul` |
| Tài liệu họp có quyền xem theo người | `Meeting.insertMeetingFiles`, `getListUserViewFile`, `removePermissionViewFile`, `getMeetingMemberPermissionFile` |
| Lịch tuần xuất file & duyệt theo cấp | `MettingWeek.getLstMeetingWeek`, `uploadFileMeetingWeek`, `getFileMeetingWeek`, `getListApproveCalendar` |
| Đề xuất họp từ văn bản | `ScheduleToMeetingDocumentBusiness` (`DocumentAction.searchMeetingRequests`, `cancelMeetingRequest`) + `document/requestToScheduleMeetingDoc/` |
