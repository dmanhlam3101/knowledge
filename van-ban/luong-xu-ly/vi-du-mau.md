# Luồng xử lý — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| CRUD cấu hình có lịch sử, sao chép, bật/tắt | `FlowManagerController`: `flow/create-or-update`, `flow/copy`, `toggle-active-flow`, `delete-flow`, `get-flow-histories` ← `FlowBusiness` ← `vm/flow/FlowVM` ❓ tên chính xác |
| Lưu đồ thị nút/cạnh từ web | `nodes/save`, `nodes/next-id` (BE cấp id trước cho web vẽ) |
| Hỏi "ai là bước tiếp theo" cho một đối tượng | `doc-in/get-users-next-step-v2` (mới nhất) và bản `-tree-` trả cây đơn vị→người |
| Luồng phụ cho một hành động đặc biệt | `doc-in/consideration/*` (trình xem xét) — copy khi cần luồng riêng cho hành động mới |
| Web chọn người theo luồng | `document/transferDoc/transfer_doc_in_flow.zul` + `TransferDocumentInVM` |
