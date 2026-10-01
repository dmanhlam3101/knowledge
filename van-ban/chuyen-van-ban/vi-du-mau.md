# Chuyển văn bản — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`.

## Mẫu 1 — Thêm một lựa chọn gửi kèm mỗi lần chuyển: "Tạo KPI nhiệm vụ" (v5.4, mới nhất, đi đủ web → BE → hook sau commit)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/document/transferDoc/transferDoc_flow.zul:511-538` (checkbox + combobox danh mục, `visible="@load(vm.kpiFeatureVisible)"`), cột "Tạo KPI" ở bảng người nhận :794-796 | Cách ẩn/hiện theo điều kiện VM, thêm cột vào bảng người đã chọn |
| VM | TDVM: điều kiện hiển thị `isKpiFeatureVisible` :4427-4435 (không cho văn bản mật/chuyển trước ban hành, chỉ văn bản đến cá nhân), state `createKpiMission` :298-302, `doToggleCreateKpiMission` :4552, `buildKpiTransfer` :4709, kiểm bắt buộc `validateKpiDeadline` :5509-5516, gọi trong `doTransfer` :4871-4873, 5083, báo kết quả `notifyKpiTransferResult` :4741 | Gom lựa chọn thành 1 DTO (`KpiTransferDTO`) rồi truyền qua `transferDocument(..., kpiTransfer)` |
| Business | `DB.transferDocument` overload thêm tham số cuối, giữ overload cũ gọi với `null` (DB:1671-1683), đẩy params chỉ khi bật (DB:1798-1807) | Giữ tương thích ngược cho mọi nơi gọi cũ — **luôn làm overload, không đổi chữ ký cũ** |
| BE controller | DC `sendDocument`: thêm khóa vào `keys[]` (DC:7609), parse `KpiTransferInput.from(...)` (:7726-7736, null = luồng cũ/mobile không đổi), hook **sau khi** `DISDAO.sendDocument` commit (:8095-8117) có `try/catch` riêng | Tính năng phụ không được làm hỏng lần chuyển: chạy sau commit, lỗi chỉ log |
| Trả về | `sendDocResult.setKpiResult(...)`; trả object khi có KPI hoặc `isSendAndWarning` (DC:8119-8127) | Client mới đọc object, client cũ vẫn nhận số |

## Mẫu 2 — Phạm vi chọn do BE quyết định: tab Cá nhân/Đơn vị "theo luồng" văn bản đến

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Popup chuyển | MTOL `prepareForOrgLookupByFlow` :480-496, `prepareForUserLookupByFlow` :761-795: chỉ truyền cờ `FROM_DOC_IN_TRANSFER_BY_FLOW` + id luồng nguồn (`DOCUMENT_IN_GROUP_ID`/`DOCUMENT_IN_STAFF_ID`) hoặc danh sách văn bản (`ARG_DOC_IN_IDS`) | Popup không tự tính phạm vi, chỉ chuyển "ngữ cảnh" |
| Lookup | UWL: cây = `documentBusiness.getTreeDocInUserFlow(...)` → `allowedOrgIds` → `new SysOrganizationTreeModel(roots, permisionIds, limitOneLevel, allowedOrgIds)` (UWL:1186-1200); danh sách = `searchDocInUserFlow` (UWL:1366-1377). SOL: `createSysOrgTreeAsync` (SOL:448-452), `searchDocInOrgFlow` (SOL:1170-1181) | Tách "cây để điều hướng" và "danh sách để chọn", cả hai lấy từ BE |
| Business | `DB.getTreeDocInUserFlow` :5845, `getListDocInUserFlowByOrg` :5657-5669, `getListOrgFlow` :5763-5773 | `serveGetRequest/servePostRequest` tới `api.flow-manager.doc-in.*` |
| BE gen-2 | `BE2/controller/FlowManagerController.java:203-333` → `FlowManagerService` | Endpoint gen-2 trả `Page<VhrEmployeeDTO>` / `Page<VhrOrgDTO>` |

Bản nâng cấp cùng ý tưởng (cây lazy-load từng cấp, mỗi nút có `selectable`/`isLeaf`, `SysOrganizationTreeModel.ChildrenLoader`) nằm ở nhánh chưa merge `taipd/feature/YC_VT_PH(_fe)` — xem `nghiep-vu.md` mục 7 và `knowledge/yeu-cau/2026-09-16-van-thu-phat-hanh-chuyen-vb-di-web.md`; nên lấy làm mẫu khi cây lớn.

## Mẫu 3 — Cấu hình theo đơn vị điều khiển hành vi chuyển: "Cấu hình chuyển văn bản sau khi tiếp nhận"

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Màn cấu hình | `SYS_MENU 440625` → `ZUL/config/docAutoSendDocumentConfig.zul` → `WEB/voffice/vm/config/DocumentProcessAutoSendConfigVM.java` | Màn CRUD đơn giản theo đơn vị |
| Business / BE | `BIZ/DocumentProcessTermBusiness.java:193-201` → `/documentProcessTermConfig/getListAutoSendConfigs|addOrUpdateAutoSendConfig` (`BE1/action/DocumentProcessTermConfigAction.java:31, 61`) → `BE1/database/dao/DocumentRequestConfigDAO.java:79-82` (insert), :195-216 (đọc còn hiệu lực) | Bảng cấu hình có `EFFECTIVE_FROM/TO`, `DEL_FLAG` |
| Điểm dùng | Nơi mở popup đọc cấu hình rồi truyền `ARG_CONFIG_AUTO_TRANSFER` (`DocumentPendingReceptionVM.java:2969-3025`; DVDVM:3576-3586); TDVM điền sẵn / tự chuyển (TDVM:451-454, 1100-1114, 3991-4115) | Mẫu "popup ẩn + gọi lệnh lưu ngay" (`LookupUtil.INVISIBLE` hoặc `Executions.createComponents` vào `Div` ẩn rồi publish event) |

Lưu ý khi copy: logic đọc cấu hình đang lặp ở ~9 VM nơi gọi (grep `ARG_CONFIG_AUTO_TRANSFER`) — mẫu mới nên đọc cấu hình **một lần trong popup** thay vì ở từng nơi gọi.

## Mẫu 4 — Thao tác lan theo cây luân chuyển: Thu hồi văn bản đã chuyển

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Web | DVDVM `doEvictionDoc/doEvictList` (cá nhân) và `doEvictionOrg/doEvictListOrg` (đơn vị) :6840-7000 — lọc dòng đã thu hồi, văn bản đi chỉ giữ dòng do mình gửi, hỏi xác nhận | Kiểm tra quyền ở web theo thiết kế chung |
| Business | `DB.doEvictionV2` / `doEvictionOrg` → `DocumentAction.updateStatusDocument` (`BIZ/DocumentBusiness.java:3065-3108`) | |
| BE | DC `updateStatusDocument` :5927-6110: dùng `processPath` của từng dòng → cập nhật mọi dòng con cháu (`PROCESS_PATH LIKE path%`), báo liên thông nội bộ, gửi thông báo, đánh lại chỉ mục | Dùng `DOCUMENT_PROCESS.PROCESS_PATH` để thao tác cả nhánh |

**Không copy** cách ghép chuỗi `processPath` vào SQL (DDAO:6746-6751 — `dac-thu.md` L1); dùng tham số bind. Thao tác tương tự trong gen-2 (trả lại → thu hồi nhánh con, đặt "Bị trả lại" cho dòng người gửi) ở `BE2/services/impl/DocInServiceImpl.java:912-1080, 1239-1331` là mẫu sạch hơn (JPA, theo `DOCUMENT_PROCESS`).
