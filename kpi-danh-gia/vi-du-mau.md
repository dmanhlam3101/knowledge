# KPI & đánh giá — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Quy trình lập → gửi duyệt → duyệt/từ chối → xuất (gen-2, gọn) | `ReportPeriodIndividualController` + `ReportPeriodApproveController` + `ReportPeriodConfigController` ← `ReportPeriod*Business` ← `vm/mission/ReportPeriodIndividualVM`, `ReportPeriodConfigVM` |
| Thống kê tổng hợp theo đơn vị nhiều chiều (gen-2) | `StatisticsReportController.get-document-in-statistics` … `get-document-statistics-by-org` + `StatisticsReportBusiness` + `summaryUsageReport/*.zul` |
| Chỉ số KPI đếm từ bảng nghiệp vụ + biểu đồ | `KpiManagerController.get-kpi-statistic`, `get-data-bar-chart`, `get-list-*` ← `KpiStatisticBusiness` ← `vm/kpi` |
| CRUD chỉ số có trạng thái nháp/chờ/chốt | `KpiPortalController` ← `KpiPortalBusiness` ← `vm/kpiPortal` |
| Import Excel danh mục | `Org.importOrgCriteria` (gen-1) + `com.viettel.util.excel` (web) |
| Sinh dự thảo văn bản từ bảng số liệu | `Org.CreateTextFromOrgCriteriaRatingTotalList` (mẫu: tạo `TEXT` từ dữ liệu phân hệ khác) |
| Cấu hình legacy (đọc/ghi DB từ web) — chỉ để hiểu, không copy | `vm/admin/CriteriaVM` → `Delegate.getService(ICriteriaGroup.class)` → `CriteriaGroupFacade` |
