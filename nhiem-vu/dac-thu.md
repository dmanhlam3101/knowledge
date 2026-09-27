# Nhiệm vụ — đặc thù

- **Lai gen-1/gen-2**: CRUD, phê duyệt, đóng, gia hạn, tiến độ ở gen-1 `missionAction` (`MissionAction` → `controler/MissionController` → `MissionDAO`…); báo cáo/chỉ tiêu/chấm điểm ở gen-1 `MissionReport`; **mẫu báo cáo, kết quả báo cáo (ngày/mật), gán chuyên viên, dashboard biểu đồ, đồng bộ, nhóm công việc** ở gen-2 (`MissionTemplateController`, `MissionReportResultController`, `MissionDashboardController`, `MissionController`, `WorkGroupController`).
- Web: `MissionBusiness` 60 hàm gọi cả `Meeting.*` (nhiệm vụ từ biên bản họp) và `DocumentService.*`; 37 VM trong `vm/mission`; 8 VM không gắn zul (popup).
- `MissionController` và `MissionDashboardController` có **cùng bộ endpoint** (`get-assign-mission-charts`, `search-mission`, `sync-mission`…) dưới 2 base — nghi ngờ trùng lặp/di chuyển dở ❓; web gọi `api.mission_dashboard.*`.
- `api.work-group-action.unBlock` web gọi nhưng không có endpoint (BE có `api.work-group.block`) ❓.
- Nhiệm vụ móc với: họp (`Meeting.getMissionByMeetingId`, `forwardMission`), định hướng (`Orientation`), văn bản (`CreateTextFromMissionList`, `sourceType = theo văn bản`), kiến nghị (`ResovleIssue`), KPI/tiêu chí (`criteriaOrg`), SMS thống kê định kỳ (`smsMaster`).
- Bẫy: "nhiệm vụ" và "công việc" bị dịch lẫn trong i18n (`menu.CONG.VIEC.CA.NHAN = NHIỆM VỤ CÁ NHÂN`, `task.taskType = Nhiệm vụ chức năng…`). Khi đọc nhãn màn hình, xác định bằng package (`mission` vs `task`), không bằng chữ.
