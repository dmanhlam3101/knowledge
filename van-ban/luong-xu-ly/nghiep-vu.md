# Luồng xử lý / luồng ký — nghiệp vụ

> Luồng là **cấu hình trong DB** (bảng `FLOW`, `FLOW_GROUP_TYPE`, `NODE`, `NODE_ACTION`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION`, `NODE_DEPT_USER`) do admin/văn thư đơn vị thiết lập; các phân hệ văn bản đến, văn bản đi, phiếu trình hỏi luồng để biết **người/nhóm bước tiếp theo**. Toàn bộ chạy trên **BE gen-2** `FlowManagerController` (`/api/flow-manager`, 45 endpoint) — mẫu gen-2 tốt.

## 1. Khái niệm

| Khái niệm | Trong code | Ý nghĩa |
|---|---|---|
| Luồng | `FlowEntity` (`FLOW`): code, tên, loại nhóm (`FLOW_GROUP_TYPE`), đơn vị áp dụng, active | Một sơ đồ bước xử lý cho một loại đối tượng (văn bản đến / văn bản đi / phiếu trình…) |
| Nhóm luồng | `FlowGroupTypeEntity`, `flow-group-type/get-all` | Phân loại: theo loại văn bản, theo đơn vị ❓ |
| Nút (bước) | `NodeEntity` (`NODE`), `nodes/next-id`, `nodes/save` | Một bước: ai (đơn vị/vai trò/người — `NODE_DEPT_USER`), làm gì (`NODE_ACTION`: ký nháy, nhận xét, ký duyệt, xét duyệt, chuyển, hoàn thành…) |
| Cạnh | `NodeToNodeEntity`, `NodeToNodeActionEntity` | Bước nào → bước nào, với hành động nào |
| Luồng requisition (web cũ) | `requisitionFlow/*.zul`, `RequisitionFlow` (cá nhân / đơn vị / tập đoàn), `updateSigningFlow` | Bản luồng ký gắn với một dự thảo cụ thể (snapshot của cấu hình khi trình) |
| Lịch sử luồng | `get-flow-histories` | Ai sửa cấu hình khi nào |

## 2. Dùng luồng ở đâu

| Nơi | Endpoint | Ý nghĩa |
|---|---|---|
| Văn bản đến — chuyển xử lý | `doc-in/get-users-next-step*`, `get-groups-next-step*`, `*-tree-*`, `*-multi-transfer*`, `*-while-creating-document`, `get-users-next-step-by-org-id`, `get-users-next-step-show`, `get-leaders` | Danh sách người/nhóm hợp lệ cho bước tiếp theo, theo văn bản + người hiện tại; biến thể `v1/v2` là phiên bản tối ưu |
| Văn bản đến — xem xét (consideration) | `doc-in/consideration/get-users-next-step`, `get-groups-next-step` | Luồng "trình xem xét" (`submitForConsideration`) |
| Văn bản đi — luồng ký | `signing-flow`, `signers-switch`, `promulgation-units` | Người ký theo luồng, đổi người ký, đơn vị ban hành |
| Kiểm tra | `check-flow-code` (mã luồng duy nhất), `check-transfer-free` | |
| Quản trị luồng | web `vm/flow/*` (3 VM), `flow/*.zul` (6) + `FlowBusiness` | Màn hình cấu hình |

## 3. Quy tắc

- QT1. Mã luồng duy nhất (`check-flow-code`); chỉ luồng active được dùng (`toggle-active-flow`).
- QT2. Sao chép luồng (`flow/copy`) để tạo luồng mới cho đơn vị khác — không sửa luồng đang dùng nếu văn bản đang chạy trên đó ❓ (cần xác nhận có snapshot hay tham chiếu sống).
- QT3. Người bước tiếp theo bị lọc thêm bởi: đơn vị (`by-org-id`), vai trò, tự do chuyển (`check-transfer-free`), hạn mức chuyển (`configLimitTransfer.zul`).
- QT4. Luồng tập đoàn > đơn vị > cá nhân (`requisitionFlow.requisitionFlowMap`) ❓ thứ tự ưu tiên.

## 4. Yêu cầu hay gặp → hướng

| Yêu cầu | Hướng |
|---|---|
| Thêm bước / thêm loại người nhận | Cấu hình `NODE`/`NODE_ACTION` — không sửa code; nếu cần loại hành động mới → thêm `NODE_ACTION` + xử lý ở service tương ứng (`TextProcess`, `DocIn`) |
| Lọc người bước tiếp theo theo điều kiện mới | `FlowManagerServiceImpl.getUsersNextStep*` (đã tối ưu — đọc `PERFORMANCE_OPTIMIZATION_FlowManagerServiceImpl.md` trước) |
| Đổi người ký giữa chừng | `signers-switch` + ghi `HISTORY_CHANGE_SIGN` |
| Luồng mới cho đối tượng mới (vd. phiếu trình loại X) | Thêm `FLOW_GROUP_TYPE` + endpoint `get-users-next-step` riêng theo mẫu `doc-in/consideration` |

## ❓
1. Luồng ký văn bản đi có lấy hoàn toàn từ `FLOW/NODE` hay vẫn còn bảng `REQUISITION_FLOW` cũ song song?
2. Khi cấu hình luồng thay đổi, văn bản đang trình có bị ảnh hưởng không?
