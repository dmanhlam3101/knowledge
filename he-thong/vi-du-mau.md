# Hệ thống / quản trị — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-02). Viết tắt như `nghiep-vu.md`. Phần lớn màn quản trị là **legacy VPS** (facade truy vấn thẳng DB từ web) — chỉ để hiểu, **không** dùng làm mẫu cho code mới; mẫu nên copy là các phần gen-2 dưới đây. Khi copy, tránh các điểm ở `dac-thu.md` (nêu cuối từng mẫu).

## Mẫu 1 — Danh mục gen-2 **áp dụng theo đơn vị, kế thừa theo cây**: Danh mục nhóm phân loại

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Migration / menu | `SQL/20250725_insert_menu_category_group.sql:1` (dòng `SYS_MENU` dưới DANH MỤC) | Mẫu chèn menu web — nhớ thêm `ROLE_MENU` (bẫy 6) |
| Web | CGVM (`ZUL/category/categoryGroup/categoryGroup.zul`): quyền nút theo vai trò + đơn vị (`CGVM:200-210`); `BIZ/CategoryGroupBusiness.java`, `BIZ/CategoryCommonBusiness.java` | Kiểm quyền hiển thị bằng `userRoles` + đơn vị của bản ghi |
| Controller | `BE2/controller/CategoryGroupController.java` (4 endpoint), `BE2/controller/CategoryCommonController.java` (7 endpoint) | Endpoint mỏng, trả `ResponseUtils.getResponseEntity` |
| Service | CGS `addOrUpdate` :81-120 (chuẩn hóa mã, kiểm trùng, audit `CoreUtils.getUserId()`), `delete` :122-135 (chặn xóa khi còn con); CCS `addOrUpdateIntoGroup` :278-343 (ghi giá trị + bảng ánh xạ đơn vị `GROUP_APPLY`) | Khung "kiểm trùng → ghi cha → ghi ánh xạ đơn vị" |
| Truy vấn theo đơn vị | CCS `getCategoryByCodeAndOrgIds` :185-275: CTE `CONNECT BY PRIOR org_parent_id = sys_organization_id` từ đơn vị yêu cầu đi lên, chọn đơn vị **gần nhất** có dữ liệu (`ROW_NUMBER() … rn = 1`), cache theo (mã, đơn vị) (:270) | Mẫu "cấu hình theo đơn vị, kế thừa từ cấp trên" |
| Đọc ở phân hệ khác | `BIZ/CategoryCommonBusiness.java` `list-category-by-code` / `list-category-by-code-and-orgs` — ví dụ `DOCUMENT_LEAD_TYPE` (LNV NV-17), `INTEGRATED_SYS_BUSINESS` (`WEB/vps/vm/IntegratedSysVM.java:277`) | Dùng lại thay vì tạo bảng danh mục mới |

**Không copy**: kiểm trùng mã khi sửa với dòng đã xóa (`dac-thu.md` L17); giả định `DEL_FLAG` theo comment DB (bẫy 15); nếu nghiệp vụ cần **cộng dồn** giá trị cấp trên thì phải đổi truy vấn (bẫy 14).

## Mẫu 2 — Thêm màn hình mới vào menu và **giới hạn theo đơn vị**; kiểm "người dùng có menu X" trong code

| Bước | Vị trí | Ghi chú |
|---|---|---|
| Dòng menu web | `SYS_MENU` (`CODE`, `NAME`, `URL` = đường dẫn `.zul`, `PARENT_ID`, `SORT_ORDER`, `STATUS = 1`) — mẫu `SQL/20250725_insert_menu_category_group.sql:1` | URL nằm ở DB, code chỉ dùng mã |
| Cấp cho vai trò | `ROLE_MENU` (`SYS_ROLE_ID`, `SYS_MENU_ID`) — hoặc qua màn "Gán menu" (`RoleMenuVM`, NV-09) | Menu chung cho mọi người: gán vai trò `VAITRO_SUPPORT` (NV-03 BR-12) |
| Giới hạn đơn vị | `ORG_SYS_MENU` (`ORG_ID`, `SYS_MENU_ID`, `DEL_FLAG`) — DDL `SQL/20250804_create_table_org_sys_menu.sql:1-19`; điều kiện đọc `SMD:390-403` | Một dòng là đủ làm menu thành "chỉ đơn vị đã khai" (bẫy 7) |
| Mở màn theo mã từ nơi khác | `MU.processGotoMenu(comp, httpSession, icommon, menuCode, …)` (`MU:1005+`); mẫu dùng thật: mở `NHACVIEC` từ widget (`HVM:2744-2745`) | Không ghi cứng URL |
| Kiểm người dùng có menu | `CM.hasGraspSituation` (`CM:731-750`, duyệt `SessionUtil.getSysMenus`); BE: `CGD:2508-2518` (đơn vị có menu qua `ORG_SYS_MENU`) | Ẩn / hiện tính năng theo menu thay vì theo mã vai trò |
| Bộ menu ứng dụng mới / mobile | `MENU` + `SYS_ROLE_MENU` (`ON_WEB`, `ON_MOBILE`) — mẫu `SQL/20250813_insert_menu_and_sys_role_menu.sql:2-40`; đọc `MRI.getAllowMenus` :222-258 | Độc lập với bộ web ZK (bẫy 6) |

## Mẫu 3 — Đọc **tham số hệ thống** có cấu trúc JSON theo đơn vị: chế độ trang chủ

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| BE gen-2 | `MSI.checkConfigurationHomePageMode` :1420-1470: đọc `SYSTEM_PARAMETER` theo mã + `STATUS = 1` (`getListByCodeAndStatus`), parse JSON `{on, scope: [orgId]}`, so với `USER_ROLE` của người dùng hiện tại (`CoreUtils.getUserId()`) | Tham số bật / tắt tính năng theo đơn vị, có lọc `STATUS` |
| Cache gen-2 | `BE2/services/SystemParameterCacheService.java:40-60` (`@Cacheable("systemParameter")`, `evictSystemParameterCache`) | Đọc tham số có cache, nhớ đường xóa cache (bẫy 16) |
| Web | `BIZ/CommonBusiness.java:348-350` (`api.manager.checkConfigurationHomePageMode`) ← `MC:1222-1245`; đọc nhiều mã cùng lúc: `BIZ/DocumentBusiness.java:4642-4660` (`configParamAction.GetAppConfig`) | Web hỏi BE "bật cho tôi không", không tự đọc giá trị |

**Không copy**: trả nguyên giá trị tham số cho client theo mã client chọn (`dac-thu.md` L12).

## Mẫu 4 — Endpoint gen-2 xác thực bằng JWT và **lấy người dùng từ token**: phản ánh

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Web gửi | `MC:2509-2545` (chụp màn hình, menu đang mở) → `PopupSendFeedbackVM` → `BIZ/FeedbackBusiness.java` (`api.manager.add-feedback`) | Gửi kèm ngữ cảnh màn |
| BE | MGC :630 → `MSI.addFeedback` :1860-1918 (người gửi = `CoreUtils.getUserId()`, trạng thái khởi tạo hằng `Constants.Feedback.Status`), `updateFeedbackProcess` :2111+ ghi lịch sử xử lý `FEEDBACK_PROCESS` và gửi SMS + thông báo cho người gửi (:1913-1915) | Ghi lịch sử từng bước + báo người liên quan |
| Danh sách theo vai trò | `FeedbackVM.java:98-123`: không có vai trò hỗ trợ → lọc theo người gửi = mình; có → theo đơn vị của vai trò | Lọc dữ liệu theo vai trò ở bước dựng điều kiện |
| Xác thực | `JTF:94-126` tự giải mã JWT, nạp `UserDetails`; đường dẫn không cần token khai ở `jwt.ignore-apis` (`BEAPP:433`) | Không nhận `userId` từ client cho thao tác ghi |

**Không copy**: đặt endpoint quản trị mà không có chốt quyền (`dac-thu.md` L10); thêm đường dẫn vào `jwt.ignore-apis` mà quên rằng so khớp là **chứa chuỗi** (L11).

## Tham khảo (chỉ để hiểu, không làm mẫu) — màn quản trị legacy có cây đơn vị: Quản lý người dùng

`VZUL/sysUser/sysUser.zul` → SUVM (cây đơn vị phạm vi quản trị `:489-580`, kiểm form `:583-709`, lưu `:770-845`) → facade `ISysUser` → SUS `insertSysUser` :215-342 (so danh sách con cũ / mới, ghi log thay đổi `ACTION_LOG_SERVICE`) → SUD / URD (JPQL + native trong web). Ý tưởng "so tập cũ / mới, ghi log từng thay đổi" dùng lại được; cách truy cập DB thẳng từ web thì không (kiến trúc tổng thể mục 3).
