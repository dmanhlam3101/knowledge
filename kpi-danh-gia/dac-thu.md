# KPI & đánh giá — đặc thù

- **Chia đôi rõ**: thi đua tiêu chí/tỷ lệ/công thức = gen-1 (`OrgResource` `/Org`, `OrgCriteriaAction`, `taskAction.getListRatioConfig*`); KPI, cổng KPI, báo cáo định kỳ, thống kê, KPI văn bản cá nhân = **gen-2** (6 controller). Tính năng mới → gen-2.
- Web: 8 Business (`CriteriaOrgBusiness`, `EvaluatedOrgBusiness`, `KpiPortalBusiness`, `KpiStatisticBusiness`, `ReportPeriod*Business` ×3, `StatisticsReportBusiness`, `DocumentKpiBusiness`); **7 facade legacy** còn dùng (`ICriteriaGroup`, `IKPIIndex`, `IKiConfig`, `IKiConfigDetail`, `IKiFormulaConfig`, `IRatioConfig`, `IRatioConfigDetail`, `IEvaluationUnit`) → cấu hình KI/tỷ lệ/tiêu chí **đọc-ghi thẳng DB từ web** (`vm/admin/CriteriaVM`, `CriteriaGroupVM`, `PrimaryVariableVM`, `vm/kiFormulaConfig`, `vm/ratioConfig`). Đây là nhóm màn LEGACY thuần nhiều nhất; sửa cấu hình = sửa entity web `com.viettel.voffice.entity.*Ki*`, `RatioConfig*`, `Criteria*`.
- Biểu đồ: web có `CreateChart`, `CreateChartColumnsAndLines`, `ChartConfigDAO` (gen-1) + gen-2 `get-data-bar-chart` — hai cơ chế vẽ chart.
- Báo cáo PDF: `empRatingReport.pdf`, `orgCriteriaRating.pdf` là "hàm" web gọi không nối endpoint (template báo cáo `com.viettel.report.template`).
- `ReportPeriod*` VM nằm trong `vm/mission` dù nghiệp vụ là báo cáo định kỳ — tìm theo tên class, không theo package.
- Đếm KPI đọc bảng `TEXT`, `DOCUMENT`, `SUBMISSION_FORM`, `BRIEF` trực tiếp (`KpiManagerServiceImpl`) → đổi trạng thái ở các phân hệ đó có thể lệch KPI.
