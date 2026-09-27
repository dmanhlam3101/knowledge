# KPI, tiêu chí, đánh giá, báo cáo định kỳ, thống kê — nghiệp vụ

> Gom các nghiệp vụ "chấm điểm & báo cáo số liệu": (1) **Chấm điểm thi đua đơn vị theo tiêu chí** (`criteriaOrg`, menu CHẤM ĐIỂM THI ĐUA), (2) **KPI đơn vị / cổng KPI** (`kpi`, `kpiPortal`), (3) **Báo cáo định kỳ cá nhân → duyệt** (`report-period-*`, gen-2), (4) **Cấu hình tỷ lệ / công thức / KI** (`ratioConfig`, `kiFormulaConfig`, KI ở `cong-viec`), (5) **Thống kê sử dụng hệ thống** (`statistics`, `summaryUsageReport`), (6) **KPI xử lý văn bản cá nhân** (`documentKpi`, `personal-treatment-status`). Web `criteriaOrg/*` (15), `kpi/*`, `kpiPortal/*`, `ratioConfig/*`, `kiFormulaConfig/*`, `summaryUsageReport/*`, `evaluatedOrg/*`; `vm/criteria` (7), `vm/kpi`, `vm/kpiPortal`, `vm/ratioConfig`, `vm/evaluatedOrg`. BE gen-1 `Org` (`OrgResource`, phần tiêu chí), `orgCriteria`; gen-2 `KpiManagerController`, `KpiPortalController`, `ReportPeriod{Config,Approve,Individual}Controller`, `StatisticsReportController`, `PersonalTreatmentStatusController`.

## 1. Chấm điểm thi đua đơn vị theo tiêu chí (`criteriaOrg`, gen-1)

| Bước | Ai | Endpoint |
|---|---|---|
| Tạo bộ tiêu chí / tiêu chí (menu DANH MỤC: *Bộ tiêu chí*, *Tiêu chí*; `criteria.criteriaMap`) | Admin/trợ lý | `orgCriteria.insertOrgCriteriaConfig`, `getListOrgCriteriaConfig`, `Org.importOrgCriteria` (import Excel) |
| Gán tiêu chí cho đơn vị | Trợ lý | `Org.UpdateOrgCriteriaMap`, `GetOrgListWhichHaveCriteria` |
| Đơn vị tự chấm | Lãnh đạo đơn vị | `Org.UpdateOrgCriteriaRating`, `getOrgRatingId` (`evaluatedOrg`) |
| Phê duyệt tự chấm / đề xuất cộng điểm | Chỉ huy | menu *Phê duyệt tự chấm điểm*, *Đề xuất cộng điểm* (`ProposePoint`, xem `nhiem-vu`) |
| Tổng hợp, ra văn bản | Trợ lý | `Org.GetOrgCriteriaRatingTotalList`, `CreateTextFromOrgCriteriaRatingTotalList` (sinh dự thảo văn bản đi từ bảng điểm), lịch sử `getListOrgCriteriaHistory`, báo cáo `orgCriteriaRating.pdf` |

Khóa kỳ đánh giá (`evaluation.isLock`, `missionRating.isLock`), loại đánh giá (`evaluation.type`, 6 loại).

## 2. KPI đơn vị & cổng KPI (gen-2)
- `KpiManagerController` (`/api/kpi`): thống kê KPI (`get-kpi-statistic`), biểu đồ (`get-data-bar-chart`), danh sách đối tượng đóng góp: văn bản đi/đến/phiếu trình/hồ sơ (`get-list-text`, `get-list-document`, `get-list-submission`, `get-list-brief`) → KPI tính từ **số lượng & tiến độ xử lý** các đối tượng nghiệp vụ. Bảng `KPI*` (SQL `13032026_create_table_kpi.sql`).
- `KpiPortalController` (`/api/kpi-portal`): CRUD chỉ số hiển thị cổng KPI (`kpi.status`: đang nháp → chờ phản hồi → chốt đánh giá); `system-downtime-log` (thời gian hệ thống ngừng, trừ vào KPI vận hành ❓).
- KPI xử lý văn bản cá nhân: `PersonalTreatmentStatusController` (`get-document-kpi`, `get-total-document-kpi`) — tỷ lệ đúng hạn/quá hạn theo người (`vm/document/documentKpi`).

## 3. Báo cáo định kỳ cá nhân (gen-2 `report-period-*`)
Cấu hình kỳ báo cáo theo người dùng (`report-period-config`: `create-or-update`, `find-by-sys-user-id`) → cá nhân lập báo cáo kỳ (`report-period-individual/save`, `exists-report-period`), tự chấm (`rating-save`, `get-report-config-rating`) → gửi lãnh đạo duyệt (`check-valid-send-approval`, `report-period-approve/send-leader-approval`) → duyệt/từ chối (`approve`, `reject`, `do-approval`) → xuất báo cáo cá nhân/đơn vị (`export-report-period-individual/unit`). Web `vm/mission/ReportPeriodConfigVM`, `ReportPeriodIndividualVM` (nằm trong package mission).

## 4. Cấu hình tỷ lệ, công thức, biến sơ cấp
`ratioConfig` (tỷ lệ điểm theo loại việc/đơn vị, `orientation.ratioConfigType` 11 loại), `kiFormulaConfig` (công thức KI, menu *Quản lý cấu hình công thức động*), `PrimaryVariable` (*Quản lý biến sơ cấp*), `actionFormula`. Dùng bởi `cong-viec` (KI) và `nhiem-vu` (chấm điểm).

## 5. Thống kê sử dụng (gen-2 `StatisticsReportController`)
`get-usage-statistics` (mức độ dùng hệ thống), `get-document-in/out-statistics`, `-ranking`, `get-meeting-schedule-statistics`, `get-mission-statistics`, `get-document-statistics-by-org`; cây đơn vị `vhr-org/get-list-child-all-level`. Web `summaryUsageReport/*`, `StatisticsReportBusiness`. Nguồn cho báo cáo lãnh đạo tỉnh ❓.

## ❓
1. KPI ở đây là KPI vận hành hệ thống (số văn bản, đúng hạn) hay KPI nhân sự? Ai xem cổng KPI?
2. Chấm điểm thi đua theo kỳ nào (tháng/quý/năm) và có liên kết với KI cá nhân?
3. Báo cáo định kỳ cá nhân có thay phiếu đánh giá cuối tháng của `cong-viec` không, hay song song?
