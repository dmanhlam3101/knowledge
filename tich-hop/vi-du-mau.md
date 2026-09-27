# Tích hợp — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Cho hệ thống ngoài đăng nhập SSO và lấy/đẩy dữ liệu có audit (gen-2) | `ShareDocumentController` (`login-sso-ext-app`, `get-document-from-ext-app`, `add-ext-doc`, `check-authorized-to-share`) + `ShareDocumentConfigController` (cấu hình phạm vi) + bảng `EXT_DOCUMENT_ACCESS_LOG` |
| Chia sẻ thêm loại đối tượng mới ra ngoài | Copy `ShareBriefController` (`/ext-brief`) / `ShareMissionController` (`/ext-mission`) |
| Tra cứu cây đơn vị / lãnh đạo / văn thư (gen-2, dùng cho mọi tính năng mới) | `VhrOrgController.get-focus-tree`, `get-list-child-all-level`, `get-org-leader`; `VhrEmployeeController.list-leader-by-org-ids`, `get-VT-in-org`, `get-employees-preside-by-org` ← `VhrEmployeeBusiness` |
| Webhook nhận kết quả từ đối tác | `CallbackController.submit-result`; `VOConnectProcessorController` (`van-ban/lien-thong`) |
| Đồng bộ dữ liệu từ hệ thống ngoài có xử lý vai trò | `SyncVHRAction.insertOrUpdateEmpVhrToVoffice` + `checkUserIsChangeOrgAndRemoveRole` |
| Mở file Office online + lịch sử sửa | `WOPIAction.generate-online-editor-url`, `getListEditHistories` ← `WOPIBusiness` ← `AddAttachFileVM` |
| API cho mobile với cấu hình động | `AppMobileController.get-data-map` / `post-data-map` + `AppMobileVM` |
| Endpoint công khai có kiểm soát | `PublicController` (`check-update`, `download`, `vofficedoc`) + `jwtIgnoreConfig` |
