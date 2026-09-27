# Luồng xử lý — đặc thù

- **Toàn bộ gen-2** (`FlowManagerController` → `FlowManagerService`(Impl) → `FlowRepositoryJPA`, `NodeRepositoryJPA`, `NodeToNode*`, `NodeDeptUser*`). Không có gen-1 tương đương → sửa/thêm ở đây an toàn hơn phân hệ văn bản.
- `FlowManagerServiceImpl` từng là điểm nóng hiệu năng (nhiều endpoint có bản `v1/v2`); tài liệu `backend2.0/backendvoffice/PERFORMANCE_OPTIMIZATION_FlowManagerServiceImpl.md` + `PERFORMANCE_OPTIMIZATION_SLIDE_FlowManagerService.md` mô tả cách tối ưu — đọc trước khi thêm query.
- Web cấu hình luồng: `flow/flow.zul`, `flow_add.zul`, `flow_search.zul`… + `vm/flow/*` (`FlowVM`, …) + `FlowBusiness` (15 hàm). Nhãn BE thuần.
- Bẫy: `api.flow-manager.doc-out` được web gọi nhưng **không có endpoint** (❓ đã bỏ hoặc chưa làm) — xem `_chung/ban-do-tong/web-goi-be.md`.
- Bẫy: tên endpoint có nhiều biến thể gần giống (`get-users-next-step`, `-v1`, `-v2`, `-show`, `-doc-show`, `-by-org-id`, `-multi-transfer`, `-while-creating-document`, `-tree-`) — khi sửa hỏi rõ màn hình nào gọi biến thể nào (tra `ban-do.md` của `van-ban/den` mục 2 `DocumentBusiness`).
