# Chuyển văn bản — đặc thù, bẫy, lỗi hệ thống ghi nhận

> Viết từ code `kha_develop` ngày 2026-10-01. Viết tắt đường dẫn/VM như `nghiep-vu.md` (TDVM, TDMVM, TDIVM, MTOL, UWL, SOL, DVDVM, DOVM, RVDVM, DC, DISDAO, DDAO, DB).

## 1. Tình trạng kỹ thuật

| Phần | Tầng |
|---|---|
| Popup chuyển, chọn đối tượng, tính phạm vi | Web ZK, VM rất lớn (TDVM ~10.300 dòng, TDMVM ~5.400, TDIVM ~4.400); cây đơn vị đọc **thẳng DB từ web** qua facade legacy `ISysOrganization` (`iOrganization.findAllChildOrg`, `findByCondition`) |
| Ghi chuyển (cá nhân, đơn vị, nhóm, trợ lý, ngưỡng, SMS) | **gen-1** `DocumentAction.sendDocument` → `DocumentController` → `DocumentInStaffDAO` → `DocumentDAO` (SQL thuần, xen lẫn vài `*RepositoryJPA` gen-2 như `documentRepositoryJPA.updateIsForwardByDocumentId`, `documentInGroupRepositoryJPA`) |
| Người/đơn vị bước tiếp theo theo luồng | **gen-2** `FlowManagerController /api/flow-manager/doc-in/*` |
| Hoàn thành / trả lại (đổi trạng thái dòng nhận) | **gen-2** `DocInServiceImpl` (thuộc `van-ban/den`) |
| Thu hồi | gen-1 `DocumentAction.updateStatusDocument` |
| Cấu hình chuyển sau tiếp nhận | gen-1 `documentProcessTermConfig.*` → `DocumentRequestConfigDAO` |

Quy tắc chọn tầng khi sửa: **sửa phạm vi chọn** → web (MTOL + SOL/UWL; xem bẫy 3); **sửa cách ghi người nhận** → `DocumentDAO`/`DocumentInStaffDAO` gen-1 (đừng viết lại); **thêm API mới phục vụ phạm vi/cây** → gen-2 (mẫu: nhánh `taipd/feature/YC_VT_PH`, `nghiep-vu.md` mục 7).

## 2. Bẫy

1. **Tên cờ ngược nghĩa `isFreeTransfer`.** Với văn bản **đi**, `isFreeTransfer = true` khi đơn vị bật checkbox **"Giới hạn chuyển văn bản"** (`DOC_OUT_CONFIG_TYPE ∈ {1,3}` — TDVM:1939-1944; `sysOrganization_add.zul:179-182`) và khi đó cây bị **thu hẹp** về đơn vị cấp 1 (MTOL:425-449). Với văn bản **đến**, `isFreeTransfer = true` nghĩa là "Chuyển tự do" (`DOC_IN_CONFIG_TYPE = 2`) — cũng thu hẹp về cấp 1 nhưng bỏ ràng buộc luồng. `isTransferByFlow` chỉ đổi câu thông báo (TDVM:3114), không quyết định phạm vi.
2. **Logic phạm vi nhân bản nhiều nơi — sửa một chỗ phải sửa tất cả:** `checkAutoLimitTransfer` (TDVM:1198-1210 ↔ MTOL:1023-1035), `checkAutoLimitTransferCustom` (TDVM:6642 ↔ MTOL:1037-1053), `checkFreeTransfer/checkFreeTransferMultiLevel` (TDVM:1885-1960 ↔ TDMVM:~4950-5000 ↔ TDIVM), `findAllOrgVT`/`getTopMostOrgs`/`checkUserRoleLevel0` (TDVM:1142-1232 ↔ MTOL:634-720), `initSearchScopeOrgIds` (TDVM:1252-1291 ↔ `DocumentDraftVM.java:20177-20187`). Cùng logic ở BE gen-2 `FlowManagerServiceImpl.getOrgTransferFreeLevel1ByOrgId` (mobile) nhưng **khác**: văn bản đi lần lên tổ tiên cho tới khi gặp 1/3 (không dừng ở 0/-1 như web), trả phần tử thứ 2 của path.
3. **TDVM đặt `ARG_TREE_ROOT`/`ARG_ORG`/`ARG_SKIP_INTERMEDIATE_ORG` nhưng MTOL không đọc** (TDVM:1333-1361; constructor MTOL:146-234 không có các khóa này) — phạm vi thực sự tính lại trong `MTOL.prepareFor*`. Đừng sửa phạm vi ở TDVM.
4. **"Đơn vị cấp 1" tính mỗi nơi một kiểu từ `PATH`** (`/1/148842/A/B/` → mảng `["",1,148842,A,B]`): phần tử [2] (`TDVM.setupOneLevelOrg` :2961-2972, `MTOL.prepareForGroupReceiverLookup*` :823-826, 876-879, `DocumentDraftVM` :8188-8191); phần tử [3] khi `ORG_LEVEL > 2` (TDVM:1270-1276, 1335-1341; MTOL:570-576, 1217-1222); phần tử [3] hoặc [4] nếu cấp huyện = cấp xã (`MTOL.resolveOrgLevelOneId` :1127-1152); BE `FunctionCommon.getFirstOrgIdByPath` cho `FIRST_ORG_ID`. Thêm vào đó dữ liệu `ORG_LEVEL` có bản ghi sai so với `PATH` (yêu cầu 2026-09-16). Quy ước nghiệp vụ (đã xác nhận 2026-10-01): cấp 0 = `/1/<id>/`, cấp 1 = `/1/<id cấp 0>/<id>/` → phần tử [2] là **cấp 0**, phần tử [3] là **cấp 1**; các chỗ code gọi "cấp 1" nhưng lấy [2] thực chất đang lấy cấp 0.
5. **TDVM bỏ qua `ARG_IS_VT_OF_ORG`** mà DVDVM truyền khi văn thư vừa cấp số (DVDVM:3549-3557) — luôn tự tính bằng vai trò `VT` tại `doc.builtGroupId` (TDVM:772).
6. **`STAFF_ID_VOF2`/`GROUP_ID_VOF2` là người gửi**, người nhận ở `RECEIVERID_VOF2`/`RECEIVER_GROUP_ID_VOF2` (DDAO:9566-9569) — kế thừa `van-ban/den/dac-thu.md` bẫy 9, 11, 12; gom "người nhận của một lần chuyển" bằng `DOCUMENT_PROCESS.PARENT_ID`.
7. **Không nhập ý kiến = không chuyển lại cho người/đơn vị đã nhận** (DDAO:7728-7741, 9189-9206) — cả nhánh tự động chuyển (ý kiến rỗng). Ai báo "chuyển rồi mà người kia không nhận" → kiểm họ đã có dòng nhận chưa. Có ý kiến thì BE trả `lstStaffNotSend` rỗng (DISDAO:1526-1528) nên web không hiện danh sách lỗi cá nhân.
8. **Chuyển cho đơn vị sinh thêm dòng cá nhân** cho người có `USER_ROLE.RECEIVE_ORG_DOC ∈ {1,2,3}` (chỉ văn bản thường — DDAO:9153-9155, 9289); đơn vị không có người cấu hình và không có văn thư = "đơn vị trống", không ghi (DDAO:9157-9169). Người trong `CONFIG_USER_DOCUMENT TYPE = 1` bị chặn (DDAO:9023-9081).
9. **Ngưỡng `CONFIG_SEND_DOCUMENT` đếm cá nhân thực nhận**, không đếm đơn vị (DISDAO:1240-1259): chuyển cho 300 đơn vị không cấu hình người nhận sẽ không chạm ngưỡng; câu hỏi web lại nói "cá nhân/đơn vị".
10. **`STATUS_AUTO_SEND_TEXT = 1` không còn nghĩa "đã tự chuyển"** — DC đặt cờ này sau **mọi** lần chuyển thành công văn bản có `TEXT` (DC:8066-8072; DB DEV 305 dòng `AUTO_SEND_TEXT = 0` nhưng cờ = 1).
11. **`autoSendDocument` chạy sau mọi lần chuyển văn bản đi có `TEXT_ID`** (DC:7947-7956) và không kiểm `AUTO_SEND_TEXT` (DDAO:14605-14700) — trái với ghi chú "ban hành thủ công thì không tự động chuyển" ở `TextDAO.java:3023`. Hành vi thực tế phụ thuộc việc `TEXT_RECEIVER*` còn dòng. Ý đồ đã xác nhận (Q2): chỉ tự chuyển khi ban hành tự động → hành vi hiện tại lệch, xem L14.
12. **Văn bản mật — mỗi nơi định nghĩa khác:** web coi mọi `stypeId ≠ 1` là mật (`checkSecretDoc` TDVM:8108-8113); BE `sendDocumentToStaff` và tự chuyển khi ban hành chỉ xét `STYPE_ID = 2` (`DocumentConstant.TEXT_CONFIDENTIAL = 2L`; DDAO:7707; `TextDAO.java:2728-2732`); `sendDocumentToGroupInternal` chỉ sinh người nhận đơn vị khi `stypeId` null hoặc 1 (DDAO:9153).
13. **Popup văn bản đến luôn là `transferDoc_flow.zul`** (`ViewUtil.createLookupTransferDocument` ép `ARG_TRANSFER_BY_FLOW = true` — `ViewUtil.java:578`); `DocumentDraftVM.doPopUpTransferDoc` mở popup này với chiều **`in`** cho dự thảo chưa có số (`DocumentDraftVM.java:8496-8510`) trong khi RVDVM dùng chiều `out` (RVDVM:9090-9106).
14. **DVDVM "fix cứng"**: `isTransferByFlow = true` (DVDVM:654), `transferBeforePublish = false` (DVDVM:658).
15. **Ô tìm nhanh không giới hạn = toàn bộ cây**: nhánh else của `initSearchScopeOrgIds` nạp `findAllChildOrgIds(root)` (TDVM:1287-1290) mỗi lần mở popup — danh sách id rất lớn truyền xuống truy vấn tìm người.
16. **BE không kiểm người nhận có đúng luồng** (DC `sendDocument` :7566-7945) — luồng chỉ ràng buộc ở danh sách chọn trên web/mobile.
17. **Màn trong `ban-do.md` không phải "chuyển văn bản"**: `viewListHistory.zul` (`DocumentLogInfoVM`) là **lịch sử chỉnh sửa file** (`ViewUtil.java:3818-3826`, `api.document-history-log.search`); `transferContentDoc.zul` dùng `SysMenuLookupVM` (chọn menu). Lịch sử/sơ đồ luân chuyển thật ở `PopupViewFlowVM` (`api.doc-in.transferred`).

## 3. Lỗi hệ thống — ghi nhận (không sửa trong phạm vi xây tri thức)

| # | Hiện tượng | Nguồn |
|---|---|---|
| L1 | Thu hồi ghép chuỗi `processPath` do client gửi thẳng vào SQL `PROCESS_PATH LIKE '<processPath>%'` (không dùng tham số) | DDAO:6746-6751 (`updateStatusDocumentInStaffVof2`); tương tự các hàm `*Vof2(listProcessPath…)` gọi ở DC:6067-6084 |
| L2 | Thu hồi văn bản **đến**: web không kiểm người thu hồi có phải người gửi ("giữ logic cũ"); không thấy kiểm ở `DC.updateStatusDocument` | DVDVM:6851-6854, 6874-6880; DC:5927-6110 |
| L3 | Chuyển nhiều văn bản đi: DOVM cảnh báo "không chuyển hàng loạt văn bản mật" nhưng vẫn truyền `selectedItems` (gồm văn bản mật) vào popup | DOVM:3737-3774 (so với `DocOrgAllVM.java:2874` truyền `listNormal`) |
| L4 | Chuyển nhiều: gặp một văn bản có luồng nguồn đã thu hồi thì trả lỗi ngay, các văn bản trước đã chuyển; kết quả trả về là của văn bản cuối; không gọi `autoSendDocument`; luôn `isTransferDocOut = false` | DC:8416-8472, 8555-8561 |
| L5 | `sendSMSSendDocumentToGroupVT` lấy danh sách văn thư rồi `return` — không gửi gì (code chết) | DDAO:9847-9856 |
| L6 | Kiểm "đã có chủ trì" vẫn gọi API nhưng kết quả `sendTypePresideChecked` không được dùng ở zul nào | TDIVM:1230-1245, 2460; TDMVM:1190, 2874; quy tắc gốc bị comment TDVM:4929-4994 |
| L7 | Link "Cấu hình giới hạn chuyển" `visible="false"` và không bao giờ bật | `transferDoc_flow_multi.zul:306-311`; `transfer_doc_in_flow.zul:883-887`; TDIVM:478, 606 |
| L8 | Thiếu key i18n → hiện nguyên key: `voffice.document.transfer.warning.pendingReception`, `voffice.document.transferDoc.autoInsertData`, `voffice.document.transfer.multi.connect.doc.fail` | TDVM:742; `transferDoc.zul:95`; TDMVM:3048, 3090; `common_voffice_vi.properties` (grep không có) |
| L9 | Mọi lỗi trong `DISDAO.sendDocument` bị nuốt, trả `sendResult = 0` — đã ghi một phần (cá nhân) mà lỗi ở bước đơn vị thì không rõ trạng thái giao dịch | DISDAO:1309-1362, 1559-1563 |
| L10 | Kết quả `autoSendDocument` chỉ ghi log; lỗi tự chuyển không báo người dùng | DC:7951-7955 |
| L11 | `checkFreeTransfer`: văn bản bị đóng vào nhánh "văn bản cấp trên chuyển" bằng `assert doc != null` rồi vẫn dùng `doc != null ? … : user.getVhrOrgId()` | TDVM:1914-1918 |
| L12 | Câu xác nhận ngưỡng `allowsend = 0` trả `maxAlert = minalert`, web hiển thị như vượt tối đa | DISDAO:1289-1294 |
| L13 | Code "chuyển trước ban hành" (tạo `DOCUMENT` tạm số "Chưa ban hành") vẫn còn và nút vẫn mở được từ dự thảo/trình ký/phiếu trình, trong khi nghiệp vụ **không có** tình huống này (xác nhận 2026-10-01, Q3) | `nghiep-vu.md` BR-31; DC:7404; DISDAO:706-868 |
| L14 | Tự chuyển tới nơi nhận dự kiến chạy sau **mọi** lần chuyển tay văn bản có dự thảo gốc, trái ý đồ "chỉ tự chuyển khi ban hành tự động" (xác nhận 2026-10-01, Q2) | DC:7947-7956; DDAO:14605-14700 |
| L15 | Tự chuyển khi ban hành tự động chỉ chặn `STYPE_ID = 2`; ý đồ là mọi độ mật khác "Thường" đều không tự chuyển (xác nhận 2026-10-01, Q9) → văn bản mã 3 vẫn bị tự chuyển | `BE1/database/dao/text/TextDAO.java:2728-2732`; `nghiep-vu.md` NV-09 |

## 4. Yêu cầu hay gặp → hướng

| Yêu cầu | Hướng |
|---|---|
| Đổi phạm vi đơn vị/cá nhân được chọn cho một trường hợp | MTOL `prepareFor*` + điều kiện ở `checkAutoLimitTransfer*`; nếu cần cây tính ở BE thì làm theo mẫu nhánh `YC_VT_PH` (API gen-2 lazy-load + `SysOrganizationTreeModel.ChildrenLoader`); nhớ ô tìm nhanh `initSearchScopeOrgIds` và mobile `check-transfer-free` |
| Thêm vai trò nhận mới / đổi cách lưu vai trò | `SENT_TYPE` web + `SEND_TYPE` BE + `DDAO.sendDocumentToStaff` (map TH→NB) + `sendDocumentToGroup*` + `TEXT_RECEIVER` (tự chuyển) + bảng hiển thị trong zul (cột chủ trì/phối hợp/NB/NTH) |
| Thêm điều kiện chặn chuyển | Web `doTransfer` (TDVM, TDMVM, TDIVM, `TransferBriefDocVM`) **và** BE `DC.sendDocument` / `sendDocumentMultiTransfer` (mobile gọi thẳng BE) |
| Thêm thông tin lưu theo mỗi lần chuyển | `DB.transferDocument` params → `DC.sendDocument` `keys[]` (DC:7591-7610) → `DISDAO.sendDocument` → câu INSERT ở DDAO:8032 (staff) và :9538 (group) |
| Đổi điều kiện "đã ban hành" | `DISDAO:1466-1483`, DC:8031-8037, DDAO:14885-14895 (`IS_FORWARD`) |
| Thay đổi tự động chuyển nơi nhận dự kiến | `DDAO.autoSendDocument` + 2 điểm gọi (`TextDAO.java:3023`, DC:7947-7956) + điền sẵn TDVM:988-1008 |
