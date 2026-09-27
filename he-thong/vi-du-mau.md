# Quản trị hệ thống — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Danh mục chung theo code + theo đơn vị (gen-2) | `CategoryCommonController.list-category-by-code`, `list-category-by-code-and-orgs`, `page-category-by-condition`, `add-or-update-into-group` ← `CategoryCommonBusiness` (nhiều VM dùng cho combobox) |
| Nhóm danh mục theo tổ chức | `CategoryGroupController` ← `CategoryGroupBusiness` ← `vm/group` |
| Tham số hệ thống có UI | `ManagerController.get-lst-param` / `add-param`; gen-1 `configParamAction.GetAppConfig` ← `vm/config` |
| Quyền menu/thao tác gen-2 | `BaseRolesController.get-menu` / `get-list-action`; `CategoryController` phần `permission-base` / `permission-data` |
| Màn quản trị legacy (chỉ để hiểu) | `vps/sysRole/roleMenu.zul` + `RoleMenuVM` → `ISysMenu`, `ISysRole` |
| Trang chủ cấu hình widget theo người dùng (gen-2) | `HomeController.config-user-dashboard`, `get-widgets-dashboard`, `get-default-dashboard` + `HomeSettingVM` |
| Đồng bộ người dùng/đơn vị từ HR | `SyncVHRAction.insertOrUpdateEmpVhrToVoffice`, `updateOrInsertDefaultRoleOnlyUser` ← `SyncVHRBusiness` ← `SyncSysUserVM` |
| Phản ánh người dùng có quy trình xử lý | `ManagerController.add-feedback`, `get-list-feedback-process-by-feedback-id`, `update-feedback-process` ← `FeedbackBusiness` ← `feedback/*.zul` |
| Quản lý phiên bản phát hành + file | `VersionControlController` ← `VersionControlBusiness` ← `versionControl/*.zul` |
