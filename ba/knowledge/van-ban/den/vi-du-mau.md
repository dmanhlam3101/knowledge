# Văn bản đến — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`.

## Mẫu 1 — Thao tác trên luồng nhận qua popup chọn luồng: **Hoàn thành** (gen-2, mẫu cho thao tác mới kiểu "xin gia hạn", "tạm dừng")

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/document/process/popupCompleteProcess.zul` (bảng luồng nhận :34-130, nội dung ≤ 2000 ký tự :155-156, văn bản trả lời :195-248, nút Lưu :264); cặp anh em `popupReturnProcess.zul`, `popupCommentProcess.zul` | Bảng "luồng đang giữ" có checkbox + cột trạng thái / vai trò / yêu cầu trả lời |
| Mở popup | `ViewUtil.createLookupCompleteDocument` (`WEB/voffice/util/ViewUtil.java:634-639`) đặt `ARG_TYPE = COMPLETE`; zul đăng ký ở `ViewConstant.WIDGETS.COMPLETE_PROCESS_POPUP` (`ViewConstant.java:303`); nơi gọi: DPPVM `doComplete` :3069-3083, `doCompleteMultiple` :3089-3108, DVDVM `doComplete` :3398-3410 | Một VM (`PopupCompleteDocumentVM`) phục vụ nhiều thao tác, phân biệt bằng `ARG_TYPE` (`DOCUMENT_PROCESS_ACTION` — `WEB/util/AppConstants.java:8546-8552`) |
| VM | PCDVM: nạp luồng theo loại (`getPendingDocuments(documentId, type, false, selectType)` :175-186), tự tick khi chỉ 1 luồng (:193-205), gom id luồng được chọn (:481-511), kiểm nghiệp vụ phía web (văn bản trả lời :515-530, nhắc việc :536-538 + :671-718), gọi API (:550), trả kết quả cho màn cha bằng `SearchEvent` (:559) | Pattern "lấy luồng → chọn → gửi `documentInStaffIds` + `documentInGroupIds`" |
| Business | `DB.getPendingDocuments` (:5926, `GET api.doc-in.get-pending-doc-in.{id}?type=…`), `checkCompletionReminders` (:6022), `completeDocument` (:6003-6010, `POST api.doc-in.complete-document` body `ChangeStatusDocumentDTO`) | `servePostRequest` / `serveGetRequest` với key `api.*` |
| Controller | `BE2/controller/DocInController.java:103-113, 133-140` | Endpoint mỏng, `@Valid` DTO, `ResponseUtils.getResponseEntity` |
| Service | `DISI.completeDocument` :214-487 (`@Transactional`); bộ lọc dùng chung với màn chi tiết `filterPendingDocumentsByType` / `filterDocumentsForComplete` :1643-1672, 1748-1767; lan trạng thái theo cây `updateProcessedByDocumentInGroupOrDocumentInStaff` :515-609, `updateCompleteChildrenProcesses` :616-712, `updateCompleteParentProcesses` :741-902 | Kiểm trạng thái hợp lệ bằng danh sách `canUpdateStatuses`; tách nhánh cá nhân / đơn vị (đơn vị kiểm văn thư); dùng `DOCUMENT_PROCESS` để lan lên/xuống |
| Repository / bảng | `DocumentInStaffRepositoryJPA`, `DocumentInGroupRepositoryJPA`, `DocumentProcessRepositoryJPA` (`findChildDocumentProcessesByDocumentIdAndProcessId` :89-91, `findAllSiblingsByDocumentProcessId` :122-123), `FileAttachmentMapperRepositoryJPA` (file theo `OBJECT_TYPE`), `DocumentInListRequestRepositoryJPA` | File đính kèm thao tác → `FILE_ATTACHMENT` + `FILE_ATTACHMENT_MAPPER` với `OBJECT_TYPE` riêng |

Khi copy: **thêm loại lọc mới** trong `filterPendingDocumentsByType` để màn chi tiết tự hiện nút (DDAO:5965-6011 gọi lại bộ lọc này); **báo lỗi bằng exception** (`InvalidInputException`, `VofficeException(ErrorApp.…)`) thay vì bỏ qua im lặng như nhánh đơn vị hiện tại (`dac-thu.md` L7).

## Mẫu 2 — Một hộp việc đầy đủ (menu + tab + widget + đếm): **Văn bản nhận để biết** (hộp mới nhất, mã 27)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Menu / widget | `SYS_MENU 440025 DOCUMENT_RECEIVE_TO_KNOW` → `ZUL/document/reportSendReceiveDoc/document_receive_to_know.zul` (+ `doc_receive_to_know_search.zul`); `HOME_WIDGET 72 IN_NHAN_DE_BIET` (`WEB/util/AppConstants.java:8313`) | Mỗi hộp = 1 zul khung + 1 zul tìm kiếm |
| VM | `DocumentReceiveToKnowVM` `processSearch`: `setDocumentInType(6)`, `setStatus(STATUS_DOCUMENT.VAN_BAN_NHAN_DE_BIET)` (DRKVM:976-977); chi tiết mở `ARG_MENU = NDB` (:1534); chuyển với `ARG_IS_RECEIVE_TO_KNOW` (:2476) | Hằng `STATUS_DOCUMENT` (`WEB/util/AppConstants.java:3050-3060`) |
| Bộ tìm dùng chung | DPOOL nhánh `documentInType == 6` → `getReceivedDocumentByStatus(…, 27, …)` (DPOOL:955-958, 1076-1079) | Thêm nhánh `documentInType` mới |
| Business / endpoint | `DB.getReceivedDocumentByStatus` → `DocumentAction.searchReceive` (DB:440-524; DA:273) | Không cần endpoint mới |
| BE tìm kiếm | DSRC `searchReceive` (:217) + `applyDefaultDateFilters` (1 tháng, chỉ chưa đọc — :796-799, 829-831); DSIS `case RECEIVE_TO_KNOW` (:739-744) và loại trừ `send_type = 3` ở các hộp khác (:654-660) | Thêm `case` mới trong `switch (status)` và hằng `Constants.Document.Status` (`BE1/constants/Constants.java:1625-1652`) |
| Đếm widget | `DC.countDocument` `case RECEIVE_TO_KNOW → setInNhanDeBiet` (:2995-2996); web `HomeWidgetRestController.java:881-883` (`createDocumentUrl("14","1","27")`), mở menu theo `vb=14` (`HomeVM.java:2630-2631`) | Ba chỗ: BE đếm, web dựng ô, web định tuyến `vb` |

## Mẫu 3 — Popup xử lý một/nhiều bản ghi kèm kiểm trùng nhiều tầng: **Tiếp nhận văn bản**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Mở | DPRVM `doReciveDocument` (:3036-3110) / `doReceiveDocuments` (giới hạn 50 — :9823-9895), chuẩn bị dữ liệu `handleReceiveDocuments` (:9897) → `ViewUtil.createLookupReceiveDocument` (`ViewUtil.java:3613`) với `LookupUtil.SINGLE`/`MULTIPLE` | Một popup cho cả một và nhiều bản ghi |
| VM | PRDVM: kiểm bắt buộc + ngày (:1014-1046), kiểm trùng 2 tầng + phát hiện "hai văn thư cùng tiếp nhận" (:1057-1111), đọc lại số tiếp theo ngay lúc lưu và hỏi xác nhận nếu khác (:451-482), nhiều bản ghi: lưu từng cái, gom thành công/thất bại, hiện bảng kết quả (:540-646) | Đọc lại dữ liệu cạnh tranh (số thứ tự) lúc submit; bảng kết quả nhiều bản ghi |
| BE | `DocumentAction.docReceivedDocument` (DA:1183) → `DC.docReceivedDocument` (:11017-11120, kiểm `validateDocumentDetail`) → DDAO `docReceivedDocument` (:17503-17555, chống chèn trùng) + `updateReceivedDocument` (:17563-17590, chỉ đổi dòng `STATUS IS NULL`) | Điều kiện `WHERE … AND STATUS IS NULL` để thao tác lặp không ghi đè |
| Sau khi lưu | Mở ngay popup chuyển (DPRVM:3044-3050); nhiều văn bản → chuyển nhiều (:9862) | Chuỗi thao tác liền mạch |

**Không copy** việc comment kiểm trùng số (PRDVM:675-682, 1048-1051) — xem `dac-thu.md` L9.

## Mẫu 4 — Thao tác có **kiểm quyền thật ở BE** + thông báo văn thư + liên thông nội bộ: **Cho ý kiến**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Web | DVDVM `doComment` (:3430-3450) → `popupCommentProcess.zul` → PCDVM `doComment` (:362-418), bắt mã lỗi 810 (trạng thái) / 403 (không quyền) để hiện thông báo riêng (:405-415) | Bắt `SendRequestException` theo mã |
| Business | `DB.commentDocument` → `api.doc-leader-comment.save-doc-leader-comment` (DB:6281) | |
| BE | `BE2/controller/DocLeaderCommentController.java:37` → DLCS `save` (:87-165): `validateSave` (:167-232 — kiểm người nhận của luồng, trạng thái, vai trò `LDDV/TTDV/VT` hoặc `LEADER_ID`, văn thư đúng đơn vị nhận) → lưu `DOCUMENT_LEADER_COMMENT` mỗi luồng → thông báo + SMS cho văn thư đơn vị (`vhrEmployeeRepository.getEmployeesByOrganizationAndSysRoleIds` :143-154) → `internalDocumentService.handleListGroupInternalConnectSend` (:157-161) | Kiểm quyền ở service (khác thiết kế chung chỉ ẩn nút), ném `VofficeException(ErrorApp.FORBIDDEN)`; móc liên thông nội bộ sau khi lưu |
