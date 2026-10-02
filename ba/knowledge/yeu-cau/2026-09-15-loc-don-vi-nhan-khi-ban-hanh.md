# Giới hạn đơn vị nhận khi văn thư ban hành văn bản đi

**Phân hệ:** `van-ban/di` (bước ban hành) + `van-ban/lien-thong` (tab đơn vị liên thông) · **Cỡ:** M · **Ngày:** 2026-09-15 · **Người lập:** AI (nháp từ code, chờ BA xác nhận ❓)

---

# PHẦN A — GIẢI PHÁP NGHIỆP VỤ (BA)

## 1. Bối cảnh & mục tiêu
- Yêu cầu gốc: *"VB Đi ⇒ văn thư phát hành không cho chọn đơn vị con của các cơ quan ngang cấp (chỉ cho chọn cấp cha, cấp hiện tại, cấp con của chính đơn vị hiện tại và các đơn vị ngang cấp). Với cơ quan: chuyển toàn cơ quan. Với đơn vị bên ngoài: chỉ chuyển cơ quan và phòng có mã định danh."*
- Vấn đề hiện tại: khi ban hành, tab **Đơn vị** hiển thị **toàn bộ cây tổ chức** từ gốc (`treeRootId`/VIG) → văn thư có thể chọn phòng/ban bên trong cơ quan khác → văn bản đến rơi thẳng vào phòng của cơ quan bạn, bỏ qua văn thư cơ quan đó (sai quy trình văn thư: văn bản gửi cơ quan phải vào văn thư cơ quan để vào sổ và trình lãnh đạo bút phê).
- Mục tiêu: (1) cây chọn đơn vị nội bộ chỉ hiện/cho tick đúng phạm vi; (2) chọn cơ quan = gửi cả cơ quan (văn thư cơ quan nhận); (3) tab liên thông chỉ hiện cơ quan/phòng có mã định danh.

## 2. Phạm vi
- Trong: popup chuyển văn bản **đi** khi ban hành (`transferDirection = "out"`) — tab Đơn vị và tab Đơn vị liên thông (+ Nhóm đơn vị liên thông nếu nhóm chứa đơn vị không có mã định danh ❓).
- Ngoài: chuyển văn bản **đến** trong nội bộ (`"in"`), chuyển tự do (`isFreeTransfer`), chọn người ký/nhận xét khi trình ký, tab Cá nhân/Nhóm.
- Giả định: "cơ quan" = đơn vị cấp 1 dưới gốc tỉnh (`orgLevel` = 1 hoặc đơn vị có văn thư riêng — `isVTOfOrg`); "đơn vị hiện tại" = đơn vị của văn thư đang ban hành (`handlingOrg`).

## 3. Actor & quyền
| Actor | Trong tính năng này |
|---|---|
| Văn thư cơ quan (`SYS_ROLE_VT`, `isVTOfOrg = true`) | Ban hành, chọn nơi nhận trong phạm vi mới |
| Văn thư phòng / người được ủy quyền ban hành (`isVTOfOrg = false`) | Hiện đã bị giới hạn theo cấu hình tự động (`checkAutoLimitTransfer`) — áp dụng cùng quy tắc |
| Văn thư cơ quan nhận | Nhận văn bản "toàn cơ quan" ở *Văn bản chờ tiếp nhận*, vào sổ, chuyển lãnh đạo — không đổi |

## 4. Nghiệp vụ hiện tại (as-is)
1. Ban hành → cấp số → popup "Chuyển văn bản đi" (`TransferDocumentVM`) → nút chọn nơi nhận → `MultiTypeObjectLookupVM`.
2. Tab **Đơn vị** (`prepareForOrgLookup`): cây từ gốc; chỉ khi `isFreeTransfer` hoặc (`out` và `checkAutoLimitTransfer()` = true) mới thu về cây của **cơ quan cấp 1 của người ban hành** (`orgLevelOne` + con + đơn vị người dùng có vai trò cấp 0). Với văn thư cơ quan ở màn *Đã ban hành* / *Chờ cấp số* thông thường → **không giới hạn** → thấy toàn tỉnh, tick được mọi phòng.
3. Tab **Đơn vị liên thông** (`prepareForConnectOrgLookup` → `ConnectVHRLookupVM` → `connectVHRBusiness.getListByCondition(..., isExcludeW00)`): danh sách từ `CONNECT_VHR` (cây cơ quan ngoài, `code` = mã định danh, join `VHR_ORG.IDENTIFIER_CODE`); có cờ loại trừ mã chứa `W00` (mã giữ chỗ ❓). Khi gửi, BE trả `sendConnectStatus = 2` nếu đơn vị không có mã định danh → web báo lỗi *"…empty.identifierCode"* **sau khi** đã bấm gửi (phát hiện muộn).

## 5. Nghiệp vụ đề xuất (to-be)

### 5.1 Quy tắc phạm vi chọn (tab Đơn vị, chiều "out")
Gọi **H** = đơn vị hiện tại của văn thư (`handlingOrg`), **P** = cha của H, **C(x)** = các con trực tiếp và mọi cấp dưới của x, **S** = các đơn vị ngang cấp với H (cùng cha P).

| Nhóm | Hiển thị trên cây | Được tick | Ghi chú |
|---|---|---|---|
| Chuỗi cha của H (P, ông…, đến gốc) | Có | **Có** (cấp cha) | ❓ chỉ P hay toàn bộ chuỗi tổ tiên — đề xuất **toàn bộ chuỗi tổ tiên** (gửi cấp trên bất kỳ) |
| H | Có | Có | |
| C(H) — con/cháu của H | Có | Có | Gửi nội bộ xuống phòng của mình |
| S — ngang cấp với H | Có | Có | **Chọn = gửi toàn cơ quan** |
| C(S) — con của đơn vị ngang cấp | **Ẩn** (hoặc mờ, không tick) | **Không** | Điểm chính của yêu cầu |
| Con của các tổ tiên khác nhánh (cơ quan khác ngang cấp với P, ông…) và con của chúng | ❓ | ❓ | Đề xuất: **các đơn vị ngang cấp với từng tổ tiên được tick (như S), con của chúng không** — để văn thư sở gửi được UBND huyện khác, nhưng không gửi được phòng của huyện đó |

Ô tìm kiếm trong cây chỉ trả về đơn vị thuộc tập được tick.

### 5.2 "Với cơ quan: chuyển toàn cơ quan"
- Khi tick một đơn vị thuộc S (hoặc tổ tiên/ngang cấp tổ tiên), hệ thống ghi nhận người nhận là **cơ quan** (`DOCUMENT_IN_GROUP` với `receiverGroupId = orgId`, `sendType` chủ trì/phối hợp/để biết như hiện nay); văn bản đến xuất hiện ở **Văn bản chờ tiếp nhận** của văn thư cơ quan đó — cơ chế sẵn có, không đổi.
- Không cho chọn đồng thời cơ quan và phòng con của nó (đã có `ARG_SKIP_INTERMEDIATE_ORG`/`limitOneLevel` — tận dụng).

### 5.3 Tab Đơn vị liên thông (đơn vị bên ngoài)
- Chỉ hiển thị **cơ quan** và **phòng** có `code` là mã định danh hợp lệ (khác rỗng, không phải mã giữ chỗ `W00…`) ❓ tiêu chí "hợp lệ" chính xác.
- Phòng không có mã định danh: ẩn (không chỉ chặn lúc gửi). Vẫn giữ kiểm tra ở BE (`sendConnectStatus = 2`) làm hàng rào cuối.
- Nhóm đơn vị liên thông (tab Nhóm liên thông): khi bung nhóm để gửi, loại các thành viên không có mã định danh và cảnh báo trước ❓ (nếu nhóm chỉ còn 0 thành viên → chặn).

### 5.4 Màn hình & thao tác
| Màn hình | Thay đổi |
|---|---|
| Popup Chuyển văn bản đi → tab Đơn vị (`sysOrganizationLookup.zul`) | Cây rút gọn; nút của C(S) không hiển thị/không tick; tooltip "Gửi cơ quan → văn thư cơ quan tiếp nhận" khi trỏ vào S |
| Tab Đơn vị liên thông (`connecVHRLookup.zul`) | Ẩn mục không có mã định danh; hiển thị mã định danh cạnh tên (giúp văn thư đối chiếu) |
| Danh sách nơi nhận đã chọn | Không đổi |

### 5.5 Dữ liệu
Không thêm bảng. Dùng `SYS_ORGANIZATION.PATH`/`ORG_PARENT_ID`/`ORG_LEVEL` (nội bộ) và `CONNECT_VHR.CODE` ↔ `VHR_ORG.IDENTIFIER_CODE` (ngoài). Có thể thêm **tham số cấu hình** bật/tắt quy tắc theo đơn vị (`CONFIG_PARAMETER`, key gợi ý `document.out.limitReceiverScope`) để triển khai dần.

### 5.6 Thông báo
Không đổi. Bỏ tình huống lỗi muộn "thiếu mã định danh" nhờ lọc trước.

## 6. Tác động
- `van-ban/den`: không đổi luồng; giảm văn bản "rơi thẳng vào phòng".
- Chuyển tự do (`isFreeTransfer`) và chuyển văn bản đến nội bộ: **không áp dụng** — cần nói rõ với người dùng.
- Mobile: nếu app mobile có ban hành/chuyển đi (`AppMobile*`) → cần áp cùng quy tắc ở BE ❓.
- Dữ liệu cũ: không migrate.

## 7. Câu hỏi mở ❓
1. "Cấp cha" = chỉ cha trực tiếp hay toàn bộ tổ tiên?
2. Đơn vị ngang cấp với **tổ tiên** (cơ quan khác cùng cấp với cha) có được chọn không? (Đề xuất: có, chỉ cấp cơ quan.)
3. Tiêu chí "có mã định danh" của đơn vị liên thông: `CODE` khác rỗng? loại trừ `W00`? có bảng/cờ riêng?
4. Có áp dụng cho văn thư phòng (không phải văn thư cơ quan) và chuyển tự do không?
5. Cần cấu hình bật/tắt theo đơn vị hay áp toàn hệ thống?

## 8. Tiêu chí nghiệm thu
- [ ] Văn thư Sở A ban hành: cây hiện UBND tỉnh (cha), Sở A, phòng của Sở A, Sở B/C… (ngang cấp); **không** hiện/tick được phòng của Sở B.
- [ ] Tick Sở B → văn bản vào *Chờ tiếp nhận* của văn thư Sở B.
- [ ] Tìm kiếm "Phòng Kế hoạch" chỉ trả về phòng thuộc Sở A (không trả phòng cùng tên của Sở B).
- [ ] Tab liên thông chỉ hiện đơn vị có mã định danh; không còn lỗi "thiếu mã định danh" sau khi gửi.
- [ ] Chuyển văn bản đến nội bộ và chuyển tự do hoạt động như cũ.

---

# PHẦN B — HƯỚNG DẪN KỸ THUẬT

**Tầng chạm tới:** Web (chính) + BE gen-2 (tuỳ chọn) · **Loại việc:** sửa tính năng cũ (web) + có thể thêm 1 API gen-2 · **Cách làm chuẩn:** `_chung/cach-lam-chuan/sua-tinh-nang-cu.md` §B, `them-api-be-gen2.md`

## 1. Hiện trạng kỹ thuật
| Thành phần | Đường dẫn | Nhãn | Ghi chú |
|---|---|---|---|
| Nút Ban hành | `web-spring/src/main/java/com/viettel/voffice/vm/requisition/RequisitionVM.java` `doPromulgate()` (L8109) → `RequisitionViewDetailVM.docCreateTab()` (L3348) | BE+LEGACY | Cấp số rồi gọi `DocumentViewDetailVM.doPopUpTransferDoc(documentEntity, "out")` |
| Popup chuyển văn bản đi | `web-spring/src/main/java/com/viettel/voffice/vm/document/TransferDocumentVM.java` — `doSelectObjectsToTransfer()` (~L1268), `initSearchScopeOrgIds()` (L1207), `checkAutoLimitTransfer()` (L1155), `checkUserRoleLevel0()`, `collectChildOrgs()`, `getTopMostOrgs()` | BE+LEGACY | `handlingOrg`, `isVTOfOrg`, `isFreeTransfer`, `transferDirection` là đầu vào quyết định phạm vi |
| Lookup đa tab | `web-spring/src/main/java/com/viettel/voffice/widget/MultiTypeObjectLookupVM.java` — `prepareForOrgLookup()` (L358), `prepareForConnectOrgLookup()` (~L855), `TAB_DON_VI=0`, `TAB_DON_VI_LIEN_THONG=4` | LEGACY (`iCommon`) | Zul `view/widgets/multiTypeObjectLookup.zul` |
| Cây đơn vị nội bộ | `web-spring/src/main/java/com/viettel/voffice/widget/SysOrganizationLookupVM.java` + `SysOrganizationTreeModel.java` (`LESS/EQUAL/GREATER`, `orgFilters`, `isLimitOneLevel`) | LEGACY | Args sẵn có: `ARG_TREE_ROOT`, `ARG_ORG_ID` (lọc id), `ARG_DIRECTION`, `ARG_SKIP_INTERMEDIATE_ORG`, `ARG_LIMIT_ONE_LEVEL`, `ARG_ONLY_ENABLE_CHECKBOX_IDS`, `ARG_DISABLE_CHECKBOX_IDS` |
| Cây đơn vị liên thông | `web-spring/src/main/java/com/viettel/voffice/widget/ConnectVHRLookupVM.java` (L211 roots, L523 search, L593 autocomplete) → `ConnectVHRBusiness.getListByCondition(..., isExcludeW00)` → gen-1 `connectVHRAction.findByCondition` → `backend2.0/.../database/dao/connectvhr/ConnectVHRDAO.java` (L45–73: `AND cv.CODE NOT LIKE '%W00%'`; L583: `JOIN vhr_org vo ON cv.code = vo.IDENTIFIER_CODE`) | BE gen-1 | |
| Kiểm tra mã định danh khi gửi | gen-1 `com.viettel.voffice.controler.DocumentController` + `DocumentDAO` (`IDENTIFIER_CODE`) → `sendConnectStatus = 2` → web `TransferDocumentVM` L4973/L5516 hiện `voffice.document.transfer.connect.empty.identifierCode` | BE gen-1 | Giữ làm hàng rào cuối |
| Thực thi gửi | `DocumentBusiness.sendDocument` → gen-1 `DocumentAction.sendDocument` → `DocumentController.sendDocument` | | Không đổi |

## 2. Thiết kế thay đổi

### 2.1 Tính tập đơn vị được phép (khuyến nghị: **BE gen-2**, 1 endpoint mới)
Lý do làm ở BE: quy tắc cần chạy cả cho mobile/ứng dụng khác, tránh viết lại bằng `iCommon` legacy trong web; `VhrOrgController` đã có sẵn cây (`get-list-child-all-level`, `get-list-org-parent-child-level-once`).

```
POST /api/vhr-org/get-out-transfer-scope
body: { handlingOrgId }            // userId từ JWT
resp: { allowedOrgIds: [...],      // được tick
        visibleOrgIds: [...],      // hiển thị (allowed + tổ tiên để dựng cây)
        wholeAgencyOrgIds: [...] } // tick = gửi toàn cơ quan (S và ngang cấp tổ tiên)
```
| Bước | File (mới/sửa) | Nội dung |
|---|---|---|
| 1 | `backend2.0/.../com/viettel/office/controller/VhrOrgController.java` (sửa) | thêm `@PostMapping("/get-out-transfer-scope")` |
| 2 | `.../services/VhrOrgService.java` + `services/impl/VhrOrgServiceImpl.java` (sửa) | `getOutTransferScope(handlingOrgId)`: từ `VhrOrgEntity` (`PATH`, `ORG_PARENT_ID`, `ORG_LEVEL`): tổ tiên = tách `PATH`; ngang cấp = `findByOrgParentId(parentId)` cho từng tổ tiên (theo trả lời ❓2); con/cháu của H = `get-list-child-all-level(H)`; **không** lấy con của ngang cấp |
| 3 | `.../dto/response/OutTransferScopeDTO.java` (mới) | 3 danh sách id |
| 4 | Tham số bật/tắt (tuỳ chọn) | `CONFIG_PARAMETER` key `document.out.limitReceiverScope` đọc qua `ManagerController.get-lst-param` / gen-1 `configParamAction.GetAppConfig` |

Phương án nhanh (nếu không muốn thêm API): tính ngay trong web bằng `iCommon.findById` + `iOrganization.findAllChildOrgIds` (đã dùng trong `initSearchScopeOrgIds`) — chấp nhận nợ legacy, ghi vào `dac-thu.md`.

### 2.2 Web — tab Đơn vị
| Bước | File | Nội dung |
|---|---|---|
| 1 | `com/voffice/service/business/VhrEmployeeBusiness.java` hoặc `DocumentBusiness.java` (sửa) | hàm `getOutTransferScope(handlingOrgId)` gọi `"api.vhr-org.get-out-transfer-scope"` |
| 2 | `widget/MultiTypeObjectLookupVM.java#prepareForOrgLookup` (sửa) | Khi `transferDirection == "out"` **và không** `isFreeTransfer`: gọi scope → `args.put(ARG_TREE_ROOT, getTopMostOrgs(visible))`, `args.put(ARG_ORG_ID, visibleOrgIds)`, `args.put(ARG_ONLY_ENABLE_CHECKBOX_IDS, allowedOrgIds)`, `args.put(ARG_SKIP_INTERMEDIATE_ORG, true)`; giữ nguyên nhánh `isFreeTransfer`/`in` |
| 3 | `widget/SysOrganizationLookupVM.java` (sửa nếu cần) | Bảo đảm tìm kiếm (`doSearch`) cũng lọc theo `lstOnlyEnableOrgIds`; ẩn hẳn C(S) thay vì chỉ disable (dùng `ARG_ORG_ID` để không đưa vào `orgFilters`) |
| 4 | `vm/document/TransferDocumentVM.java#initSearchScopeOrgIds` (sửa) | Ô tìm nhanh trong popup (`getListOrgToTransfer` → `documentBusiness.getListOrgFlow`) dùng `searchScopeOrgIds = allowedOrgIds` khi `out` |
| 5 | `TransferDocumentVM` khi lưu (`sendDocument`, ~L4950) | Không đổi; các đơn vị S đã vào `DOCUMENT_IN_GROUP` như hiện nay |
| 6 | `common_voffice_vi.properties` (+ `_en`) | tooltip `voffice.document.transfer.org.wholeAgencyHint` |

### 2.3 Web + BE — tab Đơn vị liên thông
| Bước | File | Nội dung |
|---|---|---|
| 1 | `backend2.0/.../database/dao/connectvhr/ConnectVHRDAO.java#getListByCondition` (sửa) | thêm tham số `onlyHasIdentifier` → `AND cv.CODE IS NOT NULL AND cv.CODE NOT LIKE '%W00%'` (tiêu chí theo ❓3); hoặc join `VHR_ORG.IDENTIFIER_CODE` như L583 |
| 2 | gen-1 `action/ConnectVHRAction.findByCondition` + `controler/ConnectVHRController` ❓ | truyền tham số mới (thêm field JSON, mặc định false để không ảnh hưởng màn khác) |
| 3 | `com/voffice/service/business/ConnectVHRBusiness.java` | thêm tham số |
| 4 | `widget/ConnectVHRLookupVM.java` L211/L523/L593 | truyền `onlyHasIdentifier = true` khi mở từ chuyển "out"; hiển thị `code` cạnh `name` |
| 5 | `MultiTypeObjectLookupVM#prepareForConnectOrgGroupLookup` (nhóm liên thông) | khi bung nhóm, lọc thành viên không có mã và cảnh báo ❓ |

Hợp đồng API mẫu (2.1):
```json
POST /ServiceMobile_V02/resources/api/vhr-org/get-out-transfer-scope
{"handlingOrgId": 337200}
→ {"result":{"data":{"allowedOrgIds":[1,337200,337201,337300],"visibleOrgIds":[1,337200,337201,337300],"wholeAgencyOrgIds":[1,337300]},"status":200}}
```

## 3. Mẫu code để copy
- Thu hẹp cây + chỉ cho tick một tập id: chính `prepareForOrgLookup` nhánh `isAutoLimitTransfer` (đã dùng `ARG_TREE_ROOT` + `ARG_ORG_ID` + `ARG_DIRECTION`), và `ARG_ONLY_ENABLE_CHECKBOX_IDS` đang dùng ở `vm/mission/MissionReportVM.java` L1467 (`args.put(SysOrganizationLookupVM.ARG_ONLY_ENABLE_CHECKBOX_IDS, listOrgIdsMapOfUser)`).
- Endpoint gen-2 trả cây/đơn vị: `VhrOrgController.get-list-org-parent-child-level-once`, `get-list-child-all-level` (`knowledge/tich-hop/vi-du-mau.md`).
- Thêm tham số vào DAO gen-1 không phá màn khác: mẫu `isExcludeW00` trong cùng `ConnectVHRDAO.getListByCondition`.

## 4. Kiểm thử
- Văn thư cơ quan (`isVTOfOrg = true`) ở màn *Đã ban hành* và *Chờ cấp số* → mở popup → tab Đơn vị: kiểm tra 5 tiêu chí nghiệm thu.
- Văn thư phòng (`isVTOfOrg = false`, đang bị `checkAutoLimitTransfer`) → không hồi quy.
- Chuyển tự do (`isFreeTransfer`), chuyển văn bản đến (`"in"`), chuyển nhiều văn bản (`TransferDocumentMultipleVM` — dùng chung `MultiTypeObjectLookupVM`) → không đổi.
- Tab liên thông: đơn vị có/không mã định danh; gửi tới nhóm liên thông có thành viên thiếu mã.
- Mobile (nếu có ban hành) gọi cùng endpoint.

## 5. Rủi ro & lưu ý
- `MultiTypeObjectLookupVM` và `SysOrganizationLookupVM` dùng chung cho **nhiều** màn (chuyển đến, họp, nhiệm vụ…) — chỉ rẽ nhánh theo `transferDirection == "out" && !isFreeTransfer`, không đổi mặc định.
- `TransferDocumentVM` 8.000+ dòng, nhiều biến thể `checkAutoLimitTransfer*` — đừng gộp logic mới vào các hàm đó; thêm hàm riêng `applyOutTransferScope(args)`.
- Cây tổ chức web là legacy (`iCommon`, `SysOrganization`), BE là `VHR_ORG` — cùng bảng gốc nhưng hai entity; id dùng chung `SYS_ORGANIZATION_ID`.
- `treeRootId` trong session (multi-tenant theo cây) phải vẫn là gốc của `visibleOrgIds`.
- Quy tắc "gửi toàn cơ quan" phụ thuộc văn thư cơ quan nhận được cấu hình (*Cấu hình văn thư đơn vị*) — nếu cơ quan chưa có văn thư, văn bản treo ở *Chờ tiếp nhận* ❓ cần thông báo.

## 6. Việc cần người khác
- BA: trả lời ❓1–5 (Phần A §7) trước khi code bước 2.1.
- Admin: nếu dùng tham số bật/tắt → thêm dòng `CONFIG_PARAMETER`.
- Tester: tài khoản văn thư của 2 sở ngang cấp + 1 phòng con mỗi sở; 1 đơn vị liên thông có/không mã định danh.
