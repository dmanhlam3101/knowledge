# Quản trị hệ thống — đặc thù

- **VPS là legacy thuần**: `com.viettel.vps.vm.*` + `view/vps/*` đọc/ghi DB trực tiếp qua `ISys*` facade → `com.viettel.vps.entity.*` (`SysUser`, `SysRole`, `SysMenu`, `SysOrganization`, `UserRole`…). Sửa quản trị = sửa entity/DAO web, KHÔNG có endpoint BE tương ứng cho nhiều thao tác (vd. gán menu cho vai trò). Muốn chuyển sang BE → tạo gen-2 mới (`ManagerController`, `CategoryController`, `BaseRolesController` là điểm bắt đầu đã có).
- Hai hệ quyền song song: VPS (`SYS_OPERATION`/`SYS_RESOURCE`/`RolePermission`) và gen-2 `PermissionBase`/`PermissionData` — cần chốt ❓ nguồn hiện hành trước khi thêm quyền mới.
- Đăng nhập nằm ở BE gen-2 (`AuthenticationController`, JWT) nhưng session web là HttpSession + cookie; `SessionInfo` giữ cả cookie JSESSIONID lẫn JWT → khi BE đổi cơ chế token phải sửa `ServiceConnection`.
- `HomeBusiness` gọi 6 nguồn khác nhau để vẽ trang chủ (văn bản, họp, nhiệm vụ, text, widget) — trang chủ chậm thường do một trong các đếm này.
- 29 controller BE thuộc phân hệ (nhiều nhất) nhưng phần lớn nhỏ; `ManagerController` (25 endpoint) là "gom lặt vặt": vai trò, phòng ban, chứng thư nhân viên (`emp-ca`), ảnh dấu, thông báo, tham số, feedback — tên không phản ánh hết nội dung.
- Bảng `USER_ORG_MAP` (SQL `20250310_add_row_user_org_map.sql`): một người nhiều đơn vị/vai trò; `checkUserIsChangeOrgAndRemoveRole` khi đồng bộ VHR đổi đơn vị sẽ **gỡ vai trò** — nguồn của lỗi "mất quyền sau đồng bộ".
- i18n: `common_voffice_vi.properties` là unicode-escape; sửa nhãn menu bằng script/IDE; tên menu tiếng Việt cũng nằm trong `SYS_MENU.NAME` (DB) — hai nơi.
