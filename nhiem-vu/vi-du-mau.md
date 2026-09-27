# Nhiệm vụ — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Biểu đồ dashboard theo đơn vị/người (gen-2) | `MissionDashboardController.get-assign-mission-charts`, `get-perform-mission-charts`, `count-*` ← `MissionChartBusiness` ← `vm/mission/*Chart*VM` ❓ |
| Báo cáo định kỳ theo mẫu, có khóa và lịch sử (gen-2) | `MissionTemplateController` (`mission-template`, `config-detail`, `lock-report-result`) + `MissionReportResultController` (`report-result`, `report-daily/create-or-update`, `report-history/get-detail`, `export`, `send-confidential-report`, `assign-specialist`) |
| Cây tổ chức đệ quy để giao việc | `WorkGroupController.get-work-group-to-recursive`, `check-valid-org-apply`; gen-1 `TaskService.getTreeEnforcement` |
| Phê duyệt / từ chối có quy trình | gen-1 `missionAction.approveOrRejectProcess`, `approvedMissionByCommander`; web popup trong `vm/mission` |
| Đề xuất (gia hạn/đóng/cộng điểm) → duyệt | `missionAction.checkExtendable`, `closeMission`; menu *Phê duyệt đề xuất*, *Đề xuất cộng điểm* (`ProposePoint`) |
| Thống kê nhiều chiều + xuất | gen-1 `MissionReport.viewMissionReport`, `viewQuarterMissionReport`, `scoreReport`, `dashboardReport` |
