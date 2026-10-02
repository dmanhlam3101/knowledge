# Xử lý công việc — ví dụ mẫu để copy pattern

> Các tính năng THẬT trong code (nhánh `kha_develop`, rà 2026-09-30). Viết tắt đường dẫn như `nghiep-vu.md`.
> Mẫu **gen-2** ưu tiên cho code mới; mẫu gen-1 chỉ để hiểu/sửa luồng hiện có.

## A. Hộp việc nhiều tab + số đếm tab + widget trang chủ (mẫu: hộp "Dự thảo")

| Tầng | File : dòng | Copy phần nào |
|---|---|---|
| zul thanh tab | `web-spring/src/main/webapp/view/voffice/documentDraft/documentDraft_search.zul:6-28` (mỗi tab là `button` có `sclass` theo `vm.tabType`, `onClick doChangeTabStatus(tabType=…)`) | Cách vẽ tab-nút có số |
| VM đổi tab → giá trị lọc | `WEB/voffice/vm/documentDraft/DocumentDraftVM.java:19660-19687` (`doChangeTabStatus`) | Map tab → mã trạng thái gửi BE |
| VM nhãn tab `tiêu đề (số)` | `DocumentDraftVM.java:19749-19823` (`getMenuLabel`: tab đang mở dùng `totalSize`, tab khác dùng map đếm) | Tránh gọi BE đếm lại khi đang ở tab |
| VM nạp map đếm | `DocumentDraftVM.java:19689-19747` (`generateMenuCount` → `XuLyCvTask` → `HomeBusiness`) | |
| Business | `BIZ/RequisitionBusiness.java:2013-2046` (`getRequisitionListDT`), `:8435-8468` (`countRequisitionListWorkProcess`) — tham số map `serveProcessing("textAction.searchText", params)` | Truyền cờ ngữ cảnh (`fromWorkProcessPage`) |
| BE controller | `BE1/controler/TextController.java:523-567` (đọc tham số thứ 33), `:8975-9533` (`getCountXlcvDashboard`: thread pool, mỗi ô 1 `TheadCountTextDashboard`) | Đếm song song nhiều ô |
| BE DAO | `BE1/database/dao/document/TextSearchDAO.java:1617-1885` (`getLstTextAssign`: `state` → mệnh đề `t.state in (…)`), `BE1/thread/TheadCountTextDashboard.java:25-50` | Mẫu mã trạng thái "ảo" (42/43/44) gộp nhiều `TEXT.STATE` |
| Widget | `WEB/voffice/controller/HomeWidgetRestController.java:420-449` (task), `:1889-1898` (`createXuLyCvUrl`), `:1961-2009` (`generateXuLyCvWidget`); điều hướng click `WEB/voffice/common/HomeVM.java:2724-2743`; khai báo `HOME_WIDGET` `SQL/12062026_tach_menu.sql`, `SQL/sql_17072026.sql` | Thêm ô widget con: 1 dòng `HOME_WIDGET` + 1 nhánh `haveShowWidgetChild` + 1 nhánh route |

Lưu ý khi copy: sửa **cả** `HomeVM.generateXuLyCvWidget` (`HomeVM.java:4237-4262,4510`) vì có hai đường render trang chủ (xem `dac-thu.md` bẫy 11).

## B. Hành động mới lên dự thảo đang trình — mẫu gen-2 (thu hồi ký, chuyển cấp số)

**Thu hồi ký** (`rollback-signer`):

| Tầng | File : dòng |
|---|---|
| VM (nút + xác nhận + thông báo theo mã trả về) | `WEB/voffice/vm/requisition/RequisitionViewDetailVM.java:11828-11860` (`doRollbackSigner`); lưới `RequisitionVM.java:17073` |
| Business (POST, path variable ghép bằng dấu chấm) | `BIZ/RequisitionBusiness.java:6939-6949` — `servePostRequest(null, "api.text-process.rollback-signer." + textId)` |
| Controller | `BE2/controller/TextProcessController.java:40-44` (`@PostMapping("/rollback-signer/{text-id}")`, lấy user `CoreUtils.getUserDetails()`) |
| Service | `BE2/services/impl/TextProcessServiceImpl.java:309-620` — trả **mã số** 0..6 cho từng lý do từ chối (mẫu tốt để web hiện thông báo cụ thể) |
| Repository | `TextRepositoryJPA` (`updateSignlevelByTextId`, `updateSignlevelAndStateByTextId`), `TextProcessRepositoryJPA` (`findByTextIdOrderBySignLevelAscSignatureTypeAsc`, `deleteByTextProcessId`), `textProcessHistoryDAO.deleteByTextIdAndTextProcessId` |

**Chuyển cấp số (lưới)** (`forward-to-assign-number`, `@RequestBody ForwardToAssignNumberDTO`): VM `DocumentDraftVM.java:16857-16892` (popup `ViewUtil.createForwardToAssignNumber` trả đơn vị + ý kiến) → `BIZ/RequisitionBusiness.java:7319` → `BE2/controller/TextProcessController.java:64-68` → `TextProcessServiceImpl.java:620-654`.

Copy: chuẩn đầu vào/ra gen-2 (`ResponseEntity<ResultResponse<Integer>>`), kiểm tra trạng thái `TEXT.STATE` ngay đầu service, trả mã số phân biệt lý do. **Nên bổ sung** kiểm tra quyền người gọi (hai mẫu này chưa có — `dac-thu.md` bẫy 5) và ghi `TEXT_PROCESS_HISTORY`.

## C. Popup nhập lý do + chọn người nhận rồi đổi trạng thái (mẫu: "Trả lại")

| Tầng | File : dòng |
|---|---|
| VM mở popup | `RequisitionViewDetailVM.java:5033-5097` (`doReject`: `args` cho `ConfirmInputVM` — bắt buộc, độ dài 3000, tắt đính file khi văn bản mật, `ARG_REQUISITION_SELECTED` để popup hiện danh sách người được trả lại, `checkSendSMS`) |
| Popup dùng chung | `WEB/voffice/util/ViewUtil.java:1640` (`createConfirmInput`) → `web-spring/src/main/webapp/view/widgets/confirmInput.zul` + `WEB/voffice/widget/ConfirmInputVM.java` (trả `List<String>`: lý do, …, id người được trả, id người trả, file, cờ SMS) |
| Rẽ nhánh theo lựa chọn | `RequisitionViewDetailVM.java:5066-5091` (id `"0"` = người tạo → `rejectRequisition`; khác → `rejectSignText`) |
| Business | `BIZ/RequisitionBusiness.java:5333-5368` (`rejectSignText`: file đính kèm tách chuỗi `storage|path|name`) |
| BE | `BE1/controler/TextController.java:6272-6380` (validate, gọi DAO, gửi SMS + thông báo, phát sự kiện Mission) → `BE1/database/dao/text/TextDAO.java:6633-6860` |

Dùng làm mẫu cho: yêu cầu bổ sung, trả lại có chọn người, hủy có lý do.

## D. Khóa thao tác theo trạng thái đối tượng liên kết (mẫu: dự thảo đã đính kèm phiếu trình)

| Tầng | File : dòng |
|---|---|
| Web — ẩn nút trên lưới | `DocumentDraftVM.java:8214-8232` (`checkValidateSubmission` đọc `obj.getSubmissionForms()` có sẵn trong kết quả tìm kiếm) + các `checkView*` `:8238-8398` |
| Web — chặn khi thao tác (chống dữ liệu cũ) | `DocumentDraftVM.java:7487-7491` (trình), `:4336-4340` (xóa) gọi `requisitionBusiness.isSubmissionAttachmentValidForDraft` |
| Business (GET gen-1 trả `ResultResponse`) | `BIZ/RequisitionBusiness.java:8268-8276` (`serveGetRequest("textAction.isSubmissionAttachmentValidForDraft?textId=…")`) |
| BE | `BE1/action/TextAction.java:1197-1201` (`@GetMapping`, trả `ResponseEntity<ResultResponse<Boolean>>`) → `BE1/database/dao/text/TextDAO.java:10721-10734` (`submissionFormService.findSubmissionFormByTextId`) |
| Dữ liệu cho lưới | `TextSearchDAO.java:1641,1673-1676` (join `submission_map`/`submission_form` để trả `submissionFormStatus`, `submissionFormDelFlag` cùng danh sách) |

Copy: kiểm tra 2 lớp — ẩn nút bằng dữ liệu đã có trong danh sách (rẻ) **và** kiểm tra lại ở BE ngay trước khi thực hiện.

## E. Trường cấu hình JSON trong `SYSTEM_PARAMETER` bật/tắt tính năng theo role/đơn vị (mẫu: kiểm tra chính tả)

`BE1/database/dao/text/TextCheckSpellDAO.java:302-345,350-380,431-442` (`CHECK_SPELL_CONFIG`: `active`, `active_roles` "ALL" hoặc danh sách `SYS_ROLE_ID` kiểm qua `USER_ROLE`, danh sách đơn vị `checkUserInOrg`) → endpoint `textAction.checkSpellActive` (`BE1/controler/TextController.java:7250-7260`) → web `DocumentDraftVM.java:995-999` đọc 1 lần khi mở màn. Copy khi cần "bật tính năng cho một số đơn vị/vai trò" mà không thêm bảng mới.
