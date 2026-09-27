# Quản trị hệ thống — nghiệp vụ

> Người dùng, vai trò, quyền, menu, tổ chức, danh mục, tham số, đăng nhập, trang chủ, log. Web: **VPS** (`com.viettel.vps.vm.*`, `view/vps/*` — module quản trị gốc của Viettel, **LEGACY thuần**: đọc/ghi thẳng DB qua `ISysUser`, `ISysRole`, `ISysMenu`, `ISysOrganization`, `ISysResource`, `ISysOperation`, `ISysCat`), `vm/admin`, `vm/config`, `vm/group`, `vm/position`, `vm/category`, `admin/*.zul`, `config/*.zul`, `group/*`, `position/*`. BE gen-1 `staffAction`, `Org` (`OrgResource`), `positionAction`, `CvGroupAction`, `imageOrgAction`, `configParamAction`, `logAction`, `SystemManager`, `Authenticate`; gen-2 `AuthenticationController`, `ManagerController` (`/api/manager`), `CategoryController`, `CategoryCommonController`, `CategoryGroupController`, `MenuController`, `BaseRolesController`, `RollPermissionController`, `HomeController`, `LanguageController`, `CacheManagementController`, `LogElkController`, `VersionControlController`, `UserDeviceController`, `SystemDowntimeLogController`.

## 1. Mô hình quyền (VPS)

```
SYS_USER ──UserRole──► SYS_ROLE ──RoleMenu──► SYS_MENU (màn hình .zul)
   │                      ├──RolePermission──► SYS_OPERATION (thao tác) × SYS_RESOURCE (tài nguyên)
   │                      └──RoleScopeData──► phạm vi dữ liệu (đơn vị được thấy)
   └──UserOrgMap──► SYS_ORGANIZATION (nhiều đơn vị/chức vụ: `userOrgMap.type` 5 loại)
```
- Vai trò cố định có id hằng (`SYS_ROLE_VT` văn thư, `LDDV`, `TTDV`, `NV`, `TL` trợ lý, `TLCT`, `ADMIN`, `SUB_ADMIN`, `QLLH` quản lý lịch họp, `LTHS` lưu trữ hồ sơ, `BCQS`, `QLCTH`, `QTHTDV`) — gen-1 `Constants`.
- Quyền động gen-2: `BaseRolesController.get-base-roles/get-menu/get-list-action/get-list-role-by-mission`, `CategoryController` phần `permission-base` (`get-action`, `add-action`) và `permission-data` (`get-data`, `add-data`) → `PermissionBaseService`, `PermissionDataService`.
- Màn hình: `vps/sysRole/sysRole.zul`, `roleMenu.zul`, `rolePermission.zul`, `roleScopeData.zul`; `sysUser/*`, `sysMenu`, `sysOperation`, `sysResource`; `vm/group` (nhóm người dùng, *Cấu hình nhóm*), `personalGroup` (nhóm cá nhân), `CvGroup` (nhóm chuyên viên).

## 2. Tổ chức & người dùng
- Đơn vị `SYS_ORGANIZATION` (`vm/admin/SysOrganizationVM`, `ImportOrganizationVM`, menu *Quản lý đơn vị*) đồng bộ từ **VHR** (`VHR_ORG`, `VHR_EMPLOYEE`, `SyncVHRAction`, `ConnectVHR`, menu *Đồng bộ thông tin người dùng*, *Thông tin nhân viên VHR* — chi tiết `tich-hop`).
- Người dùng: `sysUser/*`, import (`ImportSysUserVM`), đồng bộ (`SyncSysUserVM`), trạng thái (`sysUser.statusMap`), thiết bị mobile (`UserDevice`), VIP (`getLstUserVip`, `VipUserService`), trợ lý của lãnh đạo (`getListUserConfigAssistant`, menu *Cấu hình trợ lý*, `leaderConfig`), văn thư đơn vị (*Cấu hình văn thư đơn vị*, `ConfigDocManagerVM`), chức vụ (`positionAction`, `POSITION`, `insertPositionOther`).
- Đăng nhập: `AuthenticationController` — `Login`, `LoginOTP`, `LoginSSO`/`LoginFromSSO` (SSO Viettel passport `sso.ws.url`), `LoginVNEID` (VNeID), `LoginEcabinet`, `refresh-token`; web `LoginController`, `changePassword.zul`, `forgotPassword.zul`, `selectRole.zul` (chọn vai trò khi có nhiều), `logAuthen` (lịch sử đăng nhập).

## 3. Danh mục & tham số
- Danh mục động `CODE_MASTER` (`ICodeMaster`, `vm/code`, menu *Danh mục động*), danh mục chung gen-2 (`category-common/list-category-by-code`, `category-group`), `SysCat`/`SysCatType` (VPS), thời gian (`timeConfig`), tài nguyên họp, cầu truyền hình.
- Tham số: `SYSTEM_PARAMETER`/`CONFIG_PARAMETER` (`configParamAction.GetAppConfig`, `getConfigParamMultiSign`; `ManagerController.get-lst-param/add-param`), danh sách đen (`ConfigBackList` — chặn người nhận? ❓), người nhận nhắc ký muộn (`getLstUserReMessOfSignerLate`, `NotifyToNextSignerVM`).
- Menu: `SYS_MENU` (`SysMenuVM`, `MenuController.get-list-all-menu`, `SyncMenu`, `SystemManager.getMenuMain`), tách menu (`12062026_tach_menu.sql`), giới thiệu trang (`pageIntroduction`), phím tắt cá nhân (`privateShortcut`), ngôn ngữ (`LanguageController`, `ChangeLanguageInSession`).
- Trang chủ gen-2: `HomeController` (`get-widgets-dashboard`, `config-user-dashboard`, `get-banner`, `search-all`), `HomeBusiness` (đếm văn bản/nhiệm vụ/họp), `HomeSettingVM`, `WebConfigDashboard`/`MobileConfigDashboard`/`TabletConfigDashboard`.

## 4. Vận hành
- Log: `logAction.saveLogLogout`, `search-advance-elastic`, `LogElkController` (`/api/logs`, ELK), `FeatureTraceAction` (`/api/feature-traces` — trace tính năng, header từ `ServiceConnection.applyFeatureTraceHeaders`), `LogResource`, `SystemDowntimeLog` (khai báo thời gian ngừng hệ thống), `AdminSystemController.pushTypeWriteLog`.
- Cache: `CacheManagementController`, Redis (`RedisController`). Phiên bản: `VersionControlController` (`vm/versionControl`, file phát hành). Phản ánh người dùng: `feedback` (`ManagerController.add-feedback`, `update-feedback-process`, `05112025_feed_back_update.sql`). Khảo sát `survey`. Tài liệu hướng dẫn `help.zul`.

## ❓
1. Quyền thao tác trong màn hình dùng VPS (`SYS_OPERATION`/`SYS_RESOURCE`) hay `permission-base` gen-2 — cái nào là nguồn hiện hành?
2. SSO đang dùng là Viettel passport hay SSO tỉnh (VNeID)?
3. `ConfigBackList` là gì?
