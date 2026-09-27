# Công việc — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Tạo đối tượng từ văn bản đang xem | `vm/task/TaskAddFromDocVM` + zul trong `task/` ← `DocumentViewDetailVM` mở popup; BE `taskAction.getListTaskFromDocument`, `TaskService.addTask` (gen-1) |
| Phê duyệt/từ chối có lý do (popup) | `PopupReasonApproveTaskVM`, `PopupReasonRejectTaskVM` → `taskAction.ApproveOrRejectTask` |
| Tự đánh giá → cấp trên đánh giá → ký hàng loạt | `TaskRatingSeflVM` → `TaskRatingManagerVM` → `EmpRatingSignAllFilesManagerVM`/`DirectorVM` (`Sign.signMultiFileTask`) |
| Sinh PDF từ dữ liệu rồi ký | `PersonalTaskBusiness.convertTaskToPDF`, `convertRatingTaskToPDF`, `Files.PreviewEmpRatingReport` |
| Lịch sử cập nhật tiến độ | `taskAction.getUpdateTaskHistory`, `getTaskReceiverHistory` |
| Cấu hình tỷ lệ/thang điểm theo đơn vị | `taskAction.getListRatioConfig`, `getListRatioConfigDT`, `updateRatioDetail` + `vm/ratioConfig` |
