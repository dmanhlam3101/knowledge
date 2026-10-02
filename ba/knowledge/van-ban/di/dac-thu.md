# Văn bản đi (từ cấp số trở đi) — đặc thù, bẫy, tình trạng kỹ thuật

> Viết lại 2026-09-30 từ code nhánh `kha_develop`. Viết tắt đường dẫn giống `nghiep-vu.md` (WEB/, ZUL/, BIZ/, BE1/, BE2/, RVM, RVDVM, VBBHVM, DOVM, DLVM, TC, TDAO, TSDAO, TBDAO).
> Bẫy của giai đoạn trước ban hành (dự thảo, trình ký, ký, trả lại trong luồng, trợ lý ký thay, ký đối tác) xem `xu-ly-cong-viec/dac-thu.md`; kỹ thuật ký/đóng dấu số xem `ky-so/`.

## Tình trạng: BE gen-1 là chính

| Phần | Tầng | Ghi chú |
|---|---|---|
| Hộp Chờ cấp số / Đã trả lại / Từ chối cấp số, hộp Văn bản đóng dấu | gen-1 `textAction.searchText` → TC:539-567 → `TSDAO.getLstTextSign(PUBLISHED_SIGN)` / `getTextMarkList` | SQL ghép chuỗi rất dài; tab phân biệt bằng `state` giả (3/27/15/299) |
| Tab Đã cấp số / Đã ban hành / Tất cả | gen-1 `DocumentAction.searchDocumentOut` → `BE1/database/dao/document/search/DocumentSearchOutService.java` | Tách khỏi `DocumentDAO` (comment "thanhvt-revotech- copy tu ham search") |
| Cấp số, hủy ban hành, trả lại, đóng dấu | gen-1 `TextController` + `TextDAO` (11.000 dòng), `SignUtils` | |
| Kiểm trùng số | **gen-2** `GET /api/doc-out/is-duplicated-register-number` | chỗ duy nhất của màn cấp số dùng gen-2 |
| Công khai | gen-1 `DocumentAction.publish/cancelPublish/...` → `DocumentDAO` (`manuallyPublishV2`) | |

## Bẫy

1. **"Ban hành" có hai nghĩa trong code.** `TEXT.STATE = 4` được đặt ngay khi **cấp số** (`TDAO:2867-2874`, `Constants.TEXT_STATE_PUBLISHED = 4` "Da dc ban hanh"), nhưng tab **"Đã ban hành"** của màn VBBH lại là `DOCUMENT.IS_FORWARD = 1` (đã chuyển đi) — `DocumentSearchOutService.java:262-273`. Văn bản vừa cấp số có `TEXT.STATE = 4` nhưng nằm ở tab **Đã cấp số**. Yêu cầu nào nói "đã ban hành" phải hỏi lại nghĩa nào.
2. **Màn cấp số thật là `ZUL/document/reportSendReceiveDoc/issussDocument.zul` + `DocumentLookUpVM`** (mở từ nút *Cấp số* — `RVDVM:3393`, `ViewConstant.java:337`). `requisition_issue_number_view_detail.zul` chỉ là màn **xem** mở từ danh sách số đã cấp (`RequisitionViewIssueNumberVM:446`); hầu hết nút của nó `visible="false"`. `ban-do.md` hiện **không liệt kê** `issussDocument.zul`/`DocumentLookUpVM`, `documentOut.zul`/`documentOut_dcs_dbh.zul`/`DocumentOutVM` (xếp sai phân hệ — xem báo cáo).
3. **Hủy ban hành ≠ Hủy đóng dấu.** `cancelDocumentPublish` → `TEXT.STATE = 27` (TDAO:4003-4110). `rollBackDauDonVi` + `checkPermissionRollBack` là **hủy đóng dấu**, chỉ trả `TEXT_MARK.STATE = 1`, `TEXT.STATE_MARK = 1` (TDAO:8154-8178). (sửa 2026-09-30: tài liệu cũ gộp hai việc.)
4. **Văn thư trả lại không ra trạng thái 27.** Trả người tạo → `TEXT.STATE = 2` (TDAO:7020-7023); trả người trong luồng → `TEXT.STATE = 1` (TDAO:6672). `27` chỉ đến từ hủy ban hành/từ chối cấp số và xóa văn bản đi.
5. **Cùng một hành động, hai nhãn.** `cancelDocumentPublish` được gọi từ nút chi tiết "Hủy ban hành" (`requisition_viewDetail.zul:4796-4802`) và icon lưới "Từ chối cấp số" (`requisition_search.zul:1331-1336`, `voffice.requisition.button.rejectNumber` trong `WEB-INF/zk-label_vi.properties:7275`); tab chứa kết quả tên "Từ chối cấp số" ở `requisition_vbbh.zul:20` nhưng nút tab trong `requisition_search.zul:73-76` lại mang nhãn "Hủy ban hành".
6. **Hai bộ hằng trạng thái lệch nhau.** Web `AppConstants.REQUISITION.STATE` có `SIGNED = 4`, `PUBLISHER = 8`, `DELETE = 29` (`AppConstants.java:835-850`) — **không** phải giá trị `TEXT.STATE`; màn VBBH dùng `COMBOBOX_MENU.VBBH` {3,4,27} (`AppConstants.java:1080-1105`) và BE `Constants.Text.State` {3 APPROVED, 4 PUBLISHED, 27 CANCEL_PUBLISHED, 15 VTCS_RETURNED, 299 DELETE} (`BE1/constants/Constants.java:788-839`). Web `STATE_CANCEL_REQUISITION.DELETE = 299` nhưng `REQUISITION.STATE.DELETE = 29`. BE còn trùng giá trị `SearchType.PUBLISHED_SIGN = 4 = INITIAL_SIGNED` (`Constants.java:708-711`). Đọc tên, đừng suy từ số.
7. **`VIEW_TYPE.VBCCS = 19` không dùng** (chỉ khai báo — `AppConstants.java:769`, `Constants.java:782, 960`). `WAITING_NUMBER_BOOK` + `/api/text-book-manager/*-waiting-number` (gen-2) **không được web gọi** và thuộc sổ văn bản.
8. **Lỗi nghi vấn ở đóng dấu từ chi tiết màn VBBH:** `RVDVM:10244` `results.get(5) != null ? (Long) results.get(51) : null` — chỉ số 51 (RVM:15105 và DOVM:7581-7582, 9643-9645 dùng `get(5)`). Sửa đóng dấu phải test đường này. **Đã xác nhận (2026-10-01):** lỗi hệ thống, chỉ ghi nhận.
9. **Thiếu kiểm quyền ở BE trả lại:** `returnCreatorTextByVtPromulgate` / `rejectSignTextVBBHWaitForNumber` không gọi `validateGetTextDetail` (so với `cancelDocumentPublish` TC:1977-1981). Nhiều hành động khác chỉ có IDOR (người trong văn bản), **không** kiểm user là văn thư đơn vị ban hành — quyền thực tế nằm ở tầng hiển thị nút (nhất quán với `xu-ly-cong-viec/nghiep-vu.md` Q9).
10. **`validateGetTextDetail` chỉ bật khi `SYSTEM_PARAMETER.VALIDATE_ATTT = 1`** (`BE1/constants/FunctionCommon.java:2369-2371`; DB DEV = 1). Tắt tham số này là bỏ toàn bộ kiểm tra IDOR.
11. **Khôi phục không trọn vẹn:** `restoreDocument` chỉ `DOCUMENT.STATUS_NUMBER = 0` (TDAO:9649-9659), `TEXT` vẫn 27/`DELETED_PROMULGATE = 1`.
12. **Văn bản thay thế khi công khai không được lưu** ở nhánh thủ công: `publishDocument` gọi `manuallyPublishV2` không truyền danh sách thay thế; hàm cũ `manuallyPublish` (có xử lý) bị bỏ gọi (`BE1/database/dao/document/DocumentDAO.java:1652-1658, 1714`). **Đã xác nhận (2026-10-01):** có thể là lỗi — ghi nhận.
13. **`OfficePublishedReplacementService` là "đơn vị ban hành thay thế"** (tham số `DRAFT_APPROVAL_PUBLISH_ORG_REPLACE`), không phải "văn bản thay thế" (`BE2/services/impl/OfficePublishedReplacementServiceImpl.java:24-57`). Đổi tham số này làm văn bản chờ cấp số rơi vào hộp văn thư đơn vị khác.
14. **Tự động ban hành kích hoạt rộng hơn cờ `AUTO_PROMULGATE_TEXT`:** còn khi `TEXT.TEXT_BOOK_ID` đã có (văn thư xét duyệt đã chọn sổ/số) hoặc **đơn vị ban hành không có văn thư** (`BE1/thread/ThreadExcuteAfterSigned.java:754-762`). Không tìm được sổ → lặng lẽ quay về chờ cấp số thủ công (:805-808). Chạy trong thread sau ký → trạng thái cập nhật trễ.
15. **Tự động chuyển chỉ khi tự động ban hành** (`TDAO:3023`): cấp số thủ công không tự chuyển dù `AUTO_SEND_TEXT = 1`; web thay bằng việc mở ngay popup Chuyển (RVDVM:3397-3406).
16. **Bộ đếm số chỉ tăng:** `updateTextBookNumber` chỉ ghi khi số vừa cấp > số hiện tại (TBDAO:1392-1413); **cấp bù (REQ-254)** dựa vào `DOCUMENT.DELETED_DATE` trong **ngày hôm nay** (TBDAO:1172-1218) — số xóa hôm qua không được gợi ý lại. Sổ `NUMBER_TYPE = 1` đếm trong `TEXT_BOOK_NUMBER` theo (sổ, thể loại) và tự tạo dòng khi thiếu (TBDAO:1076-1090).
17. **`TEXT_BOOK.AUTO_PROMULGATE` không còn được code đọc** trong logic cấp số (bộ lọc comment — `BE1/database/dao/text/TextCommonDAO.java:234-260`). Nghĩa nghiệp vụ (xác nhận 2026-10-01) là *tự động cấp số khi đã vào sổ*, và hành vi đó hiện chạy qua nhánh `TEXT_BOOK_ID` đã có (bẫy 14) — đừng nhầm là tính năng đã bỏ.
18. **Request cấp số mã hóa RSA:** `RequisitionBusiness.publishDocument` gọi `connection.sendPostRequest(..., session.getRsaPublicKey())` và đọc `result.data` riêng (`BIZ/RequisitionBusiness.java:2466-2481`), khác `serveProcessing` thông thường; mã `1001` ⇒ web báo trùng số (xác nhận 2026-10-01: BE có thể trả mã này nhưng hiện chưa dùng).
19. **Logic đóng dấu trên `DOCUMENT` bị nhân bản ở ~15 VM** (`rollBackDauDonVi`, `getListOrgMultiMarkRequisition`, `updateDatabaseAfterMark`, `addTextMarkSync`): `ArchiveDocumentVM`, `DocOrgAllVM`, `DocumentOutVM`, `DocumentPendingProcessingVM`, `DocumentPendingReceptionVM`, `DocumentProcessedVM`, `DocumentReceiveToKnowVM`, `DocumentReturnedVM`, `DocumentReturnVM`, `DocumentSearchVM`, `DocumentVM`, `OrgFollowerDocInOrgSearchVM`, `DocumentInVM`… (grep `requisitionBusiness.rollBackDauDonVi` trong `WEB/voffice/vm/document/`). Sửa một chỗ phải sửa đồng loạt. Tương tự `askForSeal` có bản sao ở `DocumentSendSearchVM`, `DocumentTrackSendVM`, `DocumentDraftVM`, `DocumentDraftViewDetailVM`.
20. **Một VM, nhiều màn (giữ từ bản cũ, còn đúng):** `RequisitionVM` (~17.900 dòng) phục vụ mọi `viewType`; VBBH còn rẽ theo `tabTypeStr` (`waitForNumberTab`/`cancelIssueTab`/`returnForNumberTab`) và `tabTypeVBBH` (7/8/15) (RVM:784-801, 1487-1600, 2005-2027). `RequisitionViewDetailVM` (~15.400 dòng) cũng vậy. Sửa nhánh VBBH phải test lại VBTK/VBKD/VBXD/VBDD.
21. **Tìm widget bằng 9 lần `getParent()`** (RVM:814; DOVM:739) và tìm menu bằng `findByParent(SysMenu, "VBBH", "code")` (RVM:805-807; DOVM:734-736) — đổi bố cục `requisition_vbbh.zul` hoặc `SYS_MENU.CODE` sẽ vỡ.
22. **Nhãn radio phạm vi lệch code:** `ORG_RANGE_MAP` ghi {0: "Theo đơn vị và các đơn vị trực thuộc", 1: "Theo đơn vị"} (`AppConstants.java:9526-9536`) nhưng DOVM coi `1` = **phạm vi cá nhân** (DOVM:1596) và BE nhánh `orgRange = 1` là văn bản do mình tạo/ký/quản lý (DocumentSearchOutService:314-342).
23. **Hai nguồn i18n:** nhãn nút màn VBBH (`rejectTextWaitForNumber`, `rejectNumber`, `tu.choi.cap.so`, `da.tra.lai`) nằm ở `web-spring/src/main/webapp/WEB-INF/zk-label_vi.properties`, không phải `common_voffice_vi.properties`.
24. **Hủy ban hành không thu hồi văn bản đến**, chỉ ẩn qua `DOCUMENT.STATUS_NUMBER = 1` ở các truy vấn văn bản đến (`DocumentSearchInService.java:196-199`); SMS cho người đã nhận bị comment (TDAO:4083-4104). Truy vấn mới về văn bản đến/đi **phải** lọc `STATUS_NUMBER`.
25. **File mật khi cấp số:** `FILE_ENCRYPT_MAP` được nhân bản từ `ObjectType.ARRIVE` (gắn text) sang `RECIVE` (gắn document) (TDAO:2833-2865); hủy đóng dấu văn bản mật gọi `rollBackPermissionConfidentialFile` (TC:6976-6982). Chức năng mới tải/xem file sau cấp số phải đi qua quyền này (giữ từ bản cũ: `FileEncryptMap`, `getPermisionReadFileEncryptMap`).
26. **Cấp số đổi tên file vật lý** theo `mã định danh đơn vị_mã sổ_viết tắt thể loại_số_năm` (TDAO:3126-3169) và đóng dấu đổi sang tên "đã đóng dấu" (`SignUtils.renameToDaDongDau`) — tích hợp đọc file theo tên cũ sẽ hỏng.
27. **`documentDraft/*` không chết toàn bộ** (sửa 2026-09-30: bản cũ ghi "documentDraft/* (21 zul) là màn hình chết" là sai): `documentDraft/documentDraft.zul` + `DocumentDraftVM` là màn Dự thảo đang dùng; chỉ các popup trỏ `vm.admin.requisition.*` là chết, trong đó `documentDraft/rejectPublish.zul` (☠, `vm.admin.requisition.RejectPublishVM`) — bản sống là `requisition/rejectPublish.zul`. Chi tiết `xu-ly-cong-viec/dac-thu.md`.

## Quyết định / lịch sử (từ comment code)

- 2018-12 "Pitagon": thêm đóng dấu (`TEXT_MARK`, `askForSeal`, `rejectMark`, `markDocumentByOrg`, VBDD) — comment `// 201812-Pitagon: add` rải khắp TDAO/TC/RVM.
- TungHD: thêm `GROUP_ID` (dấu đơn vị/xác nhận/hồ sơ) cho `TEXT_MARK` (TDAO:6577-6578, 7513-7514); MinhNQ: hủy đóng dấu (`rollBackDauDonVi`, TDAO:8154-8178).
- datdn: thêm tab **Tất cả** (`VIEW_TYPE.ALL = 10`, `documentOut_dcs_dbh.zul`) và `promulIndex` (VBBHVM:50-61; `AppConstants.java:4043-4049`).
- "cap nhat giai phap check VB da cap so / da ban hanh theo document.is_forward" (DocumentSearchOutService:262).
- REQ-254: cấp bù số đến/đi trong ngày (TBDAO:1100-1116, 1133-1218).
- "v5.4 T06": trả lại của văn thư ban hành phát sự kiện Nhiệm vụ (TC:6446-6449, 6526-6537).

## Khi nhận yêu cầu ở phân hệ này

- Sửa hộp việc VBBH/VBDD → sửa SQL ở `TSDAO.getLstTextSign`/`getTextMarkList` hoặc `DocumentSearchOutService`; nhớ bản `isCount` và bản danh sách là **hai nhánh ghép SQL riêng** (TSDAO:3942-4050 vs 4050-…).
- Thêm hành động trên văn bản chờ cấp số → nút ở `requisition_viewDetail.zul` + icon lưới `requisition_search.zul` (hai chỗ), handler ở cả RVDVM và RVM; BE nên thêm endpoint gen-2 (xem `vi-du-mau.md`).
- Đụng tới "ban hành" → xác định là cấp số (`TEXT.STATE = 4`) hay chuyển (`IS_FORWARD`); nếu là chuyển thì sang `van-ban/chuyen-van-ban`.
- Đụng tới đánh số → phối hợp `van-ban/so-van-ban` (`TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`).
