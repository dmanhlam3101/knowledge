# Công việc — đặc thù

- **Gần như toàn bộ gen-1**: `TaskAction` (`/taskAction`) + `TaskService` (`/TaskService`, class annotated @RestController dù tên Service) → `controler/TaskController` ❓ → `TaskDAO`, `TaskRatingDAO`, `KI*DAO`. Không có controller gen-2 riêng → tính năng mới nên tạo `TaskController` gen-2 (`/api/task`) theo `_chung/cach-lam-chuan/them-api-be-gen2.md`.
- Web: `TaskBusiness` 61 hàm, `PersonalTaskBusiness` 8 (PDF phiếu, luồng trình `createPersonalTaskSubmitFlow`); VM `TaskVM`, `TaskNewVM`, `TaskViewDetailVM`, `TaskApprovalVM`, `TaskRating*VM`, `EmpRating*VM`, `TaskAddFromDocVM`. 4 màn ☠ (`EmpRatingSignVM` ×4 zul, `popUpAssignVM`, `TaskGanttChartVM`) — ký phiếu đánh giá & Gantt là màn chết; chức năng ký thật ở `EmpRatingSignAllFiles*VM`.
- Ký phiếu dùng `Sign.signMultiFileTask` (gen-1 `SignResource`) — sửa ký số ảnh hưởng phiếu giao việc/đánh giá.
- `GanttTaskServlet` (web `http/`) phục vụ biểu đồ Gantt cũ.
- Facade legacy `TaskFacade`/`ITask`, `ITaskRating`, `IEmpRating` vẫn tồn tại ở web — kiểm tra `ban-do.md` mục 4 xem VM nào còn dùng.
- Móc với: văn bản đến (`getListTaskFromDocument`, `TaskAddFromDocVM`), trình ký (`updateRequisitionDirect`), KPI/tỷ lệ (`ratioConfig`, `kiFormulaConfig`), SMS (`giao.viec.ca.nhan`, `bao.cao.ket.qua.lanh.dao`).
