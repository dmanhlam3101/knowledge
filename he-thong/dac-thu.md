# Hệ thống / quản trị — đặc thù, bẫy, lỗi hệ thống ghi nhận

> Viết lại từ code `kha_develop` ngày 2026-10-02. Viết tắt đường dẫn / lớp như `nghiep-vu.md` (WEB, ZUL, VZUL, PAGES, BIZ, SC, APP, BE1, BE2, SQL, BEAPP; LC, MC, VNF, SSOC, VNC, WCF, AUC, AUS, UTS, JTF, BSSO, BVNC, VEJ; VF, VS, SUVM, SUS, SUD, URD, UOVM, UOD, SRVM, SRS, SMVM, SMD, PJD, MU, CM, CVM, AC, RPV; SOVM, CB, VOD, PGVM, CGD, CGVM, CGS, CCS, CPD, SPD, UD, MRI, MGC, MSI, HVM).
> **Bảo mật:** mục này chỉ nêu *có* cấu hình / tài khoản bí mật ở đâu, không ghi giá trị.

## 1. Tình trạng kỹ thuật

| Phần | Tầng | Nguồn |
|---|---|---|
| Đăng nhập web (form, SSO, VNeID) | Web ZK composer `LoginController` + bộ lọc `VNeIDFilter` (`*.zul`) → **BE gen-2** `/Authentication/*`; JWT kiểm ở `JwtTokenFilter` | NV-01, NV-02 |
| Đăng nhập cũ `/Authenticate/*` (17 endpoint) | **BE gen-1** `AuthenticateResource` → `UserControler` (còn nhánh passport / SSO cũ); web chỉ gọi `ChangeLanguageInSession` | `he-thong/ban-do.md` mục 3; `BE1/controler/UserControler.java:490`, `909` |
| Phiên web, menu trái | Web `MainController` + `MenuUtil` + **facade legacy** `ISysMenu` (SQL `CONNECT BY` thẳng từ web) | NV-03 |
| Người dùng, vai trò, menu, thao tác, tài nguyên, cấu hình người theo đơn vị, văn thư đơn vị, nhóm cũ, danh mục động, giới thiệu trang, khảo sát | **Legacy web thuần** (`com.viettel.vps.*`, facade `I*` → `*JpaDao` → Oracle); không có endpoint BE tương ứng | NV-06 … NV-10, NV-12, NV-13, NV-15, NV-17 |
| Đơn vị | Web legacy cho đọc cây + **BE gen-1** `commonAction.insertSysOrganization` cho ghi (dữ liệu mã hóa AES) | NV-11 |
| Nhóm cá nhân, chức vụ, tham số (đọc), danh sách không nhận văn bản | **BE gen-1** (`CvGroupAction`, `positionAction`, `configParamAction`) | NV-12 … NV-15 |
| Danh mục nhóm phân loại, cây đơn vị gen-2, phản ánh, lịch sử đăng nhập, phiên bản phát hành, phiên bản mobile | **BE gen-2** | NV-05, NV-11, NV-13, NV-17, NV-18 |
| API quản trị gen-2 (người dùng, vai trò, tham số, menu, quyền chức năng / dữ liệu, cache) | **BE gen-2**, **không có web ZK gọi** — phục vụ ứng dụng mới / mobile / vận hành | NV-09, NV-10, NV-14 |
| Cấu hình widget cá nhân, chế độ trang chủ | **memcached** (không có bảng) | NV-16 |

Quy tắc chọn chỗ sửa: **điều kiện đăng nhập** → `AUS` (mọi kiểu đăng nhập lặp lại đoạn kiểm chặn người dùng thường — sửa đủ 8 chỗ, bẫy 3) **và** `LC` (kiểm `STATUS` chỉ ở web); **ai thấy menu nào** → dữ liệu `ROLE_MENU` / `ORG_SYS_MENU` (không sửa code), câu truy vấn ở `SMD.findByHierMaxLevel`; **ai quản trị được ai** → `SUVM.viewEdit` / `getPermissionOrg` (người dùng), `SOVM.createSysOrgTree` (đơn vị), từng VM riêng (bẫy 9).

## 2. Bẫy

1. **Tên entity khác tên bảng.** `SysUser` = `VHR_EMPLOYEE`, `SysOrganization` = `VHR_ORG` (web); BE gen-2 dùng `VhrEmployeeEntity`, `VhrOrgEntity` cho cùng bảng; gen-1 dùng `EntityVhrOrg`… Đổi cột phải sửa mọi bộ mapping còn đọc bảng đó (kiến trúc tổng thể mục 3).
2. **Hai nguồn mật khẩu.** `/Authentication/Login` dựa vào SSO (`AUS:100-125`), trong khi `LoginOTP` (nhánh SSO trả mã 0 / 2), `LoginFromSSO`, màn đổi mật khẩu, đặt lại mật khẩu, import người dùng dùng `VHR_EMPLOYEE.PASSWORD` SHA-256 (`AUS:335`, `692`; `WEB/voffice/widget/ChangePasswordVM.java:55`, `71`; `SUVM:966-967`; `SUS:233`). Đổi mật khẩu trên VOffice không đổi mật khẩu đăng nhập form.
3. **Đoạn "chặn người dùng thường" lặp 8 lần** trong `AUS` (`AUS:145`, `278`, `366`, `409`, `454`, `496`, `719`, `816`) (`login`, `loginKNTC`, `loginOTP`, `loginVNEID`, `loginEcabinet`, `loginSSO`, `loginFromSSO`, `loginSSOFromExtApp`) — cùng khóa cache `vps_datacache_common_login_prevent` 300 giây. Thêm điều kiện đăng nhập phải sửa đủ.
4. **Khóa tài khoản chỉ có tác dụng ở web.** `VEJ.findUserByEmployeeCode` không xét `STATUS` (`VEJ:21-22`); chỉ `LC:523` chặn. Kênh mobile / eCabinet / ứng dụng ngoài dùng token BE nên người bị khóa vẫn vào được.
5. **Đổi IP / trình duyệt giữa phiên đẩy người đăng nhập bằng form ra trang "không có tài khoản".** `MC:332-345` xóa người dùng khỏi phiên rồi dựng lại từ thuộc tính SSO (`employeeCodePassport`) — với đăng nhập form thuộc tính này rỗng → `SUD:2118-2122` trả null → `error = 1` → `redirectNoAccountPage` (`MC:576-577`).
6. **Hai bộ menu độc lập.** Web ZK: `SYS_MENU` + `ROLE_MENU` + `ORG_SYS_MENU`; ứng dụng mới / mobile: `MENU` + `SYS_ROLE_MENU` (`ON_WEB` / `ON_MOBILE`) + `ORG_MENU` (`MRI:222-258`). Script thêm màn phải chèn đúng bộ (mẫu `SQL/20250725_insert_menu_category_group.sql` cho web, `SQL/20250813_insert_menu_and_sys_role_menu.sql` cho bộ gen-2). Màn mới cho web nhớ chèn **cả `ROLE_MENU`** — script mẫu chỉ chèn `SYS_MENU`.
7. **`ORG_SYS_MENU` là danh sách trắng**: chèn **một** dòng cho một menu là mọi đơn vị khác (không nằm trong cây đơn vị đã khai) **mất** menu đó ngay (`SMD:391-401`). Ngược lại, xóa mềm dòng cuối cùng của một menu thì menu đó **mở cho mọi đơn vị** (trường hợp `SUBMISSION_FOLLOW` trên DB DEV ngày 2026-10-02). Không có màn quản trị bảng này; DB DEV 58 dòng cho 7 menu.
8. **Vai trò `VAITRO_SUPPORT` cộng vào menu của mọi người** (`MC:720-724`) — gán nhầm một menu nhạy cảm cho vai trò này là lộ cho toàn hệ thống. DB DEV ngày 2026-10-02 vai trò này có menu cha 336812 QUẢN TRỊ: menu con không lộ (mỗi dòng phải có `ROLE_MENU` riêng — `SMD:383`) nhưng nút "QUẢN TRỊ" rỗng vẫn được vẽ cho mọi người (`MU:282-290`).
9. **Phạm vi quản trị mỗi màn một kiểu** (kiểm ở VM, không có chỗ chung):

| Màn | Ai thao tác | Phạm vi | Nguồn |
|---|---|---|---|
| Người dùng | `ADMIN`, `ADMIN_LEVEL1` | cây đơn vị nơi có vai trò đó; `ADMIN_LEVEL1` không đụng người có `ADMIN` | `SUVM:547-580`, `1802-1843` |
| Đơn vị | `ADMIN` → cả tỉnh + `DVTHHT`; `ADMIN_LEVEL1` → cây con | — | `SOVM:396-430` |
| Văn thư đơn vị | chỉ `ADMIN` | cây đơn vị nơi có `ADMIN` | `WEB/vps/vm/ConfigDocManagerVM.java:67-103` |
| Không nhận văn bản | `ADMIN`, `ADMIN_LEVEL1` | đơn vị của vai trò | `CPD:92-93` |
| Nhóm phân loại | `ADMIN` tại đơn vị cấp 0 (nhóm); `ADMIN` / `ADMIN_LEVEL1` / `LDDV` / `TTDV` tại đơn vị áp dụng (giá trị) | — | `CGVM:200-210` |
| Quản lý phiên bản | `ADMIN` | toàn hệ thống | `WEB/voffice/vm/versionControl/VersionControlVM.java:132-136` |
| Báo cáo tổng hợp sử dụng | `ADMIN`, `ADMIN_LEVEL1` | cây đơn vị của vai trò | `WEB/voffice/vm/summaryUsageReport/UsageReportVM.java:100-112` |
| Phản ánh | `VAITRO_SUPPORT` | đơn vị của vai trò hỗ trợ | `WEB/voffice/vm/feedback/FeedbackVM.java:102-123` |

10. **Gán menu cho vai trò xóa cứng rồi chèn lại** (`SRS:46-54` → `CommonJpaDao.deleteByParentId` — `WEB/common/dao/CommonJpaDao.java:845-856`): mất dấu `DEL_FLAG` / người tạo của các dòng cũ; dòng `ROLE_MENU.DEL_FLAG = 1` trên DB do script khác ghi và **vẫn cấp menu** (L14).
11. **`USER_ROLE.IS_DEFAULT` đổi nghĩa ngày 2025-09-03**: cột cũ đổi tên thành `IS_ORIGINAL_ORG`, cột `IS_DEFAULT` mới = vai trò mặc định (`SQL/20250903_add_column_is_default_and_rename_column_into_user_role_table.sql:1-5`). Truy vấn cũ còn dùng `IS_DEFAULT` theo nghĩa khác (ví dụ `u.IS_DEFAULT = 6` — `BE1/database/dao/staff/StaffDAO.java:2139-2145`; VHR ghi `IS_DEFAULT = 2` cho kiêm nhiệm — `UD:2472-2500`) — đọc kỹ ngữ cảnh trước khi dùng cột này.
12. **Lưu form người dùng mở khóa ngầm** (`STATUS = 1`, `IS_ACTIVE = 1` — `SUVM:775-776`) và **xóa cứng** dòng vai trò bị bỏ (`SUS:237-249`); đồng bộ VHR đổi đơn vị **xóa cứng toàn bộ** vai trò (`UD:2463-2468`). Không có lịch sử vai trò ngoài `ACTION_LOG_SERVICE` (DB DEV 0 dòng).
13. **Chuyển cha đơn vị không cập nhật cây con** (`VOD:917-964`) — `PATH` / `ORG_LEVEL` con cháu giữ giá trị cũ; truy vấn "con cháu theo `PATH LIKE`" sẽ sai sau khi chuyển. Đây là một nguồn của quy ước "`ORG_LEVEL` không tin được".
14. **Danh mục theo đơn vị thay thế, không cộng dồn** (`CCS:213-262`): thêm một giá trị riêng cho đơn vị con làm đơn vị đó (và cây dưới nó) **mất toàn bộ** giá trị kế thừa của cấp trên.
15. **`CATEGORY_COMMON.DEL_FLAG` ngược comment DB**: code 0 = còn, 1 = xóa (`CCS:291`; `CategoryCommonRepositoryJPA.java:19-31`); comment DB ghi "0 - đã xóa, 1 - chưa xóa".
16. **Tham số có nhiều lớp cache** (BR-35): memcached + cache danh mục 1 giờ (`SPD:201-233`), Spring Cache `systemParameter` (xóa qua `/api/cache/clear/system-parameter`), cache bộ nhớ 300 giây của tham số chặn đăng nhập. Sửa DB xong phải xóa cache hoặc chờ.
17. **Cấu hình trang chủ chỉ ở memcached** (`WEB/voffice/util/PersonalSettingUtil.java:501-534`; `MC:1358-1385`) — đừng tìm bảng DB; muốn lưu lâu dài phải thêm bảng.
18. **Tên lớp / file gây nhầm**: `AuthenticatonServiveImpl` (gõ sai); `VNeIDFilter` xử lý cả SSO lẫn VNeID, còn `WEB/voffice/util/SSOFilter.java` **không được đăng ký** (chỉ `VNeIDFilter` trong `WCF:285-294`); `sysOrgMenu.zul` / `SysOrgMenuVM` là thể loại văn bản theo đơn vị chứ không phải menu; `reportSendReceiveDoc.zul` mượn `SysMenuVM`; `BaseRolesController.java` viết **trên một dòng** (mọi trích dẫn là `:1`); hai menu "Quản lý đơn vị" (338452, 439825) cùng URL.
19. **`ban-do.md` xếp ở đây những thứ thuộc phân hệ khác** (do regex `_tools/domains.py`): `vps/sysImageOrg/*` (`ky-so`), `vps/integratedSys/*` (`tich-hop`), `document_type.zul` + `sysOrgMenu.zul` (`QLC`), `configPersonal/proposal.zul` (`phieu-trinh`), `financialRecords/*` (`ho-so-cong-viec`), `carRegister.zul` (đặt xe), `ResovleIssue*` (`nhiem-vu`), `PersonalTreatmentStatusController` / `summaryUsageReport` (`kpi-danh-gia`), `Party*Controller` (danh mục Đảng). Ngược lại `SyncVHRAction` / `UserDAO` đồng bộ VHR đang ở `tich-hop`.

## 3. Lỗi hệ thống — ghi nhận (không sửa trong phạm vi xây tri thức)

| # | Hiện tượng | Nguồn |
|---|---|---|
| L1 | `/Authentication/Login` **không so mật khẩu** với dữ liệu VOffice (đoạn so đã comment) và cấp token khi tìm được mã nhân viên `IS_ACTIVE = 1`, bất kể kết quả gọi SSO: cờ `sso.service.access.token.flag` tắt → `loginApiSSO` trả null; SSO trả lỗi 4xx có thân → trả đối tượng lỗi; lỗi kết nối → trả null — cả ba trường hợp đều đi tiếp tới cấp token | `AUS:100-125`; `BSSO:151-206` |
| L2 | Khi gọi SSO lỗi, log ghi **mật khẩu thô** của người dùng | `BSSO:188` |
| L3 | Web giữ **mật khẩu thô** trong đối tượng người dùng của phiên (`setAccountPass`) | `LC:554-556` |
| L4 | Ô ẩn `ws2box` (ẩn bằng CSS) quyết định địa chỉ BE mà máy chủ web gửi tên + mật khẩu tới | `LC:448-454`; `PAGES/login.zul:213-216` |
| L5 | Người bị khóa (`STATUS = 2`) vẫn nhận token BE; chỉ web chặn (bẫy 4) | `VEJ:21-22`; `LC:523-534` |
| L6 | Mở khóa màn hình không kiểm mật khẩu | `MC:2304-2318` |
| L7 | So phạm vi quản trị bằng **chuỗi con**: `PATH.contains(orgId.toString())` — id 23 khớp mọi `PATH` chứa "23" (123, 230…); và regex `(.*)ADMIN(.*)` coi mọi mã vai trò chứa "ADMIN" (`DOCUMENT_ADMIN`, `ADMINKH`…) là quản trị | `SUVM:1836`, `263-264`; `WEB/vps/vm/ImportSysUserVM.java:186` |
| L8 | `/api/app-mobile/get-data-map` và `/post-data-map` **thực thi câu SQL do client gửi** (base64) cho mọi người có JWT | `BE2/controller/AppMobileController.java:55-110` |
| L9 | `OfficeController` (`/query`, `/update`, `/officesys`, `/officesystest`) chạy SQL tùy ý / tra vị trí thuê bao cho phiên đăng nhập riêng (quyền theo danh sách mã nhân viên ghi cứng); **tài khoản kết nối hai dịch vụ ngoài khai cứng trong mã nguồn** | `BE2/controller/OfficeController.java:35-56`, `78-170`, `195-226` |
| L10 | API quản trị gen-2 (thêm / sửa người dùng, vai trò, quyền, tham số, đơn vị, cache) không kiểm người gọi là quản trị: `officeCheckPermission()` luôn đúng (TODO), các endpoint `ManagerController` không có chốt — mọi người có JWT gọi được (X1 là thiết kế cho nút web; ghi để biết khi mở API cho kênh khác) | `JTF:114-117`; `BE2/core/config/customsecurity/ProxiesMethodSecurityExpressionRoot.java:15-17`; MGC :189-560 |
| L11 | Danh sách bỏ qua JWT so khớp **chứa chuỗi** trên URL viết thường: mọi đường dẫn có chứa `/public`, `/actuator`, `/index.html`, `/api/connecteoffice`… đều bỏ qua kiểm token | `JTF:151-180`; `BEAPP:433` |
| L12 | `configParamAction.GetAppConfig` trả **bất kỳ mã tham số** client yêu cầu (không danh sách cho phép, không lọc `STATUS`) | `SPD:190-235`; `BE1/controler/ConfigParameterController.java:455-470` |
| L13 | Chuyển cha đơn vị không cập nhật `PATH` / `ORG_LEVEL` cây con (bẫy 13) | `VOD:917-964` |
| L14 | Dựng menu không lọc `ROLE_MENU.DEL_FLAG` — dòng đã xóa mềm vẫn cấp menu (DB DEV 25 dòng) | `SMD:383` |
| L15 | Màn hỏng / chết đang có menu mở hoặc vẫn truy cập được: "Đồng bộ người dùng" (VM comment toàn bộ), "Quản lý giới thiệu trang" (không có bảng), `roleScopeData.zul` / `sysCat` / `sysCatType` (không có bảng), `notifyToNextSigner.zul` (không có endpoint), `view/survey.zul` (VM comment), trang chủ tải khảo sát nhưng không hiển thị | `WEB/vps/vm/SyncSysUserVM.java:113`; `WEB/voffice/common/SurveyVM.java`; `HVM:2237-2256`; NV-20 |
| L16 | Nhãn loại cấu hình người dùng 5 / 6 trỏ khóa i18n không tồn tại (`…orgFollow.document.in/out`) → hiện khóa thô | `AC:6965-6966` |
| L17 | Sửa mã nhóm phân loại kiểm trùng với dòng **`DEL_FLAG = 1`** thay vì 0 → đổi mã sang mã đang dùng không bị chặn | `CGS:106-108` |
| L18 | `GROUP_MANAGER.PRIVATE_TYPE_MAP` dùng khóa 3 / 2 (hằng phạm vi) thay vì 1 / 2 (hằng loại riêng tư) | `AC:5635-5645` |
| L19 | Mở khóa người dùng dùng nhầm hằng `SYS_MENU.ACTIVE` (cùng giá trị 1); lưu form người dùng mở khóa ngầm | `SUVM:939`, `775` |
| L20 | Đặt lại mật khẩu hiện mật khẩu mới trên hộp thoại của quản trị; gửi email đã comment | `SUVM:966-974` |
| L21 | Gán người cho vai trò từ màn vai trò tạo `USER_ROLE` **không có đơn vị**; truy vấn vai trò khi đăng nhập `ORDER BY ur.sysOrganization.orgLevelManage` (JPQL tạo join trong) loại các dòng này khỏi phiên | `SRS:63-77`; `URD:180-186` |
| L22 | `LoginController.createSessionLoginLog` và nhiều đoạn ghi log đăng nhập đã comment thân; `ACTION_LOG_SERVICE` DB DEV 0 dòng | `LC:894-905`; DB DEV 2026-10-01 |
| L23 | Ngoại lệ ghi cứng mã đơn vị hệ cũ `148842` trong dựng menu (không tồn tại ở cây Khánh Hòa) | `MU:152-172` |
| L24 | Dữ liệu cấu hình không khớp code (DB DEV ngày 2026-10-02): `USER_ORG_MAP` loại 4 chỉ cấu hình được cho người có vai trò `TLCDDV` nhưng vai trò này đã xóa; `VHR_ORG.HAVE_DOCUMENT_MANAGER` null ở toàn bộ 2.378 đơn vị; `APP_MOBILE.DEVICE_TYPE` lẫn hoa / thường (`android` / `ANDROID`) | `UOVM:199-215`; `WEB/vps/vm/ConfigDocManagerVM.java:51-52`; `BE2/services/impl/AppMobileServiceImpl.java:43-48` |
