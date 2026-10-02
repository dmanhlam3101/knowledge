# Quản lý hồ sơ — ví dụ mẫu (tính năng thật để copy pattern)

> Viết lại từ code `kha_develop` ngày 2026-10-01. Viết tắt như `nghiep-vu.md`. Ưu tiên copy các mẫu **gen-2** (mẫu 1–4); mẫu 5 là luồng gen-1 cũ — chỉ đọc để hiểu, không copy.

## Mẫu 1 — Thêm một loại nội dung mới vào hồ sơ, BE tự kiểm quyền và trạng thái ("Tài liệu liên quan khác")

| Tầng | Vị trí |
|---|---|
| Màn | tab 4 `ZUL/brief/brief_info.zul:1488-1550` → popup `ZUL/brief/widgets/brief_attach_multimedia.zul` (mở qua `WEB/voffice/util/ViewUtil.java:2890-2896`) |
| VM | `WEB/voffice/vm/brief/BriefAttachMultimediaVM.java` (bắt buộc :420-429, mặc định :182-189, lọc đuôi file theo loại :165-178) |
| Business | `BB` key `api.brief-detail.brief-multimedia` (POST tạo / PUT sửa), `api.brief-detail.upload-brief-multimedia-file`, `delete-brief-multimedia`, `swap-order-brief-multimedia.{briefId}` |
| Controller | `BDC:145-153` (`@Valid @RequestBody CreateBriefMultimediaRequest` / `UpdateBriefMultimediaRequest`), :165, :171, :221 |
| Service | `BDSI.createBriefMultimedia` :494-553 (kiểm hồ sơ chưa đóng + người gọi là chủ / chia sẻ loại 1, thứ tự = max + 1), `updateBriefMultimedia` :560-693, `uploadBriefMultimediaFile` :424-490 (chuyển file tạm → kho), xóa :950-990 |
| Repository | `BE2/repositories/jpa/BriefEntityRepositoryJPA.java:64-102` (`isBriefActive`, `hasAccessToMultimedia`), `BriefMultimediaJPA.java:134-145` (dồn thứ tự khi xóa), `BriefMultimediaFileJPA.java:79-88` |
| Bảng | `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE` (`SQL/20251216_create_table_brief_multimedia*.sql`) |

**Copy:** DTO request có `@Valid` + kiểm quyền / trạng thái **ở BE** trong service (khác hầu hết hồ sơ chỉ ẩn nút); thứ tự lấy `max + 1` (không dùng `count + 1` như `add-document-in-brief` — `dac-thu.md` L13). **Đừng copy:** kiểm quyền ở web lệch với BE (UI chỉ cho sửa tài liệu mình thêm, BE cho mọi người chia sẻ loại 1 — `dac-thu.md` mục 3).

## Mẫu 2 — Chia sẻ một đối tượng cho danh sách người, gom thay đổi thêm / sửa / xóa ("Chia sẻ hồ sơ")

| Tầng | Vị trí |
|---|---|
| Màn | `ZUL/brief/widgets/shareBrief.zul` (chọn cá nhân :11, chức danh :65-70, quyền :88-92) |
| VM | `WEB/voffice/vm/brief/ShareBriefVM.java` — giới hạn chọn người trong đơn vị của đối tượng :116-127; gom thay đổi INSERT = 1 / UPDATE = 2 / DELETE = 3 :50-52, 139-246; gửi :252-281 |
| Business | `BB` `api.brief.update-brief-share-list` (BB:1041-1046), `api.brief.get-list-brief-share` |
| Controller | `BC2:54-61` (`POST /api/brief/update-brief-share-list`) |
| Service | `BSI.updateBriefShareList` :230-317 — kiểm người gọi là chủ (:260-262) và có chức danh tại đơn vị (:266-271); thêm / sửa / xóa mềm (:276-306) |
| Repository / bảng | `BriefShareEntityRepositoryJPA` → `BRIEF_SHARE` (`SQL/20250926_create_table_brief_share.sql`, sequence bước 2) |
| Dùng quyền | danh sách join `BRIEF_SHARE` (BDAO:235); chi tiết `briefShareType` (BIVM:956-966) |

**Copy:** một API nhận cả danh sách thay đổi kèm loại thao tác; lưu chức danh người được chia sẻ tại thời điểm chia sẻ. **Bổ sung khi copy:** đối chiếu `briefShareId` thuộc đúng đối tượng đã kiểm quyền và kiểm quyền cho các API đọc (`dac-thu.md` L11).

## Mẫu 3 — Chuyển trạng thái có điều kiện chặn rõ ràng ở BE ("Đóng / mở lại hồ sơ")

| Tầng | Vị trí |
|---|---|
| Màn | nút "Đóng hồ sơ" `ZUL/brief/brief_info.zul:2321-2326`; icon "Mở lại" `ZUL/brief/brief_search.zul:539-543` |
| VM | BIVM `checkVisibleCloseBrief` :2246-2252, `doCloseBrief` :2255-2287 (kiểm trước ở web :2391-2570, :6245+); BVM `doUnLock` :4208-4233 |
| Business | `BB` `api.brief.close-brief.{id}`, `api.brief.unlock-brief.{id}` (BB:1116, 2105-2109) |
| Controller | `BC2:95-118` |
| Service | `BSI.closeBrief` :1394-1433, `unlockBrief` :1435-1464 (`@Transactional`, ném `CustomException` kèm thông điệp nghiệp vụ tiếng Việt cho từng điều kiện chặn) |
| Bảng | `BRIEF` (`BRIEF_STATUS`, `ACTUAL_COMPLETE_DATE`, `END_TIME`, `YEAR`), `BRIEF_SUBMIT_REQUEST` (chặn mở lại khi đang / đã nộp) |

**Copy:** mỗi điều kiện chặn một thông điệp riêng; web hiển thị nguyên văn chuỗi lỗi BE trả (BIVM:2262-2270). **Bổ sung khi copy:** kiểm người gọi là chủ đối tượng; kiểm trạng thái **trước** khi gán dữ liệu (`dac-thu.md` L16 — `closeBrief` gán `YEAR` trước).

## Mẫu 4 — Đẩy dữ liệu sang hệ thống ngoài qua bảng hàng đợi + callback theo mã giao dịch ("Nộp hồ sơ")

| Tầng | Vị trí |
|---|---|
| Màn / VM | nút `brief_info.zul:2328-2334`; BIVM `checkVisibleSubmit` :2289-2336 (cấu hình theo đơn vị `VHR_ORG.SUBMIT_BRIEF_CONFIG`), `doSubmitBrief` :2371-2389 → `processSubmitBrief` :2572-2694 → `executeSubmitBrief` :2701-2747 |
| Business | `BB` `api.brief.submit-brief`, `api.brief.submit-brief-history`, `api.brief.get-cert-shvb`, `api.brief-detail.check-text-doc-for-submitting` |
| Controller | `BC2:71-93, 120`; callback `BE2/controller/CallbackController.java:16-31` (`POST /callback/ext-brief/submit-result`) |
| Service | `BSI.submitBrief` :366-694 (chặn → gom tài liệu `findAllDocumentsByBriefId` :696+ → gom file :838-1276 → ghi 3 bảng hàng đợi); `submitResult` :1339-1392 (tìm theo `TRANSACTION_ID`, cập nhật kết quả từng tài liệu theo id UUID) |
| Bảng | `BRIEF_SUBMIT_REQUEST`, `BRIEF_SUBMIT_DOCUMENT`, `BRIEF_SUBMIT_ATTACH_FILE` (`SQL/20251127_create_table_for_submit_brief.sql`, `20251217_*`, `20260130_*`, `20260212_*`), `FILE_ENCRYPT_MAP` |

Dữ liệu: DB DEV `VHR_ORG` ngày 2026-10-01 — mới 7 đơn vị bật `SUBMIT_BRIEF_CONFIG = 1` (mẫu bật tính năng theo đơn vị bằng một cột cấu hình trên `VHR_ORG`).

**Copy:** tách "ghi yêu cầu" (đồng bộ, trong transaction) khỏi "gửi" (dịch vụ ngoài đọc hàng đợi, thử lại có giới hạn `NUMBER_RETRY`); id tài liệu là UUID để bên ngoài trả kết quả từng dòng; lưu lịch sử mỗi lần nộp. **Bổ sung khi copy:** xác thực bên gọi callback (hiện chỉ cần JWT bất kỳ) và kiểm người nộp (`dac-thu.md` L2, L16).

## Mẫu 5 (chỉ đọc, không copy) — Luồng gen-1 cũ: bàn giao / tiếp nhận

`ZUL/brief/widgets/process.zul` / `receiveOrRejectBrief.zul` → `ProcessVM` / `ReceiveOrRejectVM` → `BB.processBrief` (BB:413-422, chuỗi tham số theo thứ tự `keys`) → `BMA:252` → `BMC.processBrief` :881-957 (`FunctionCommon.getDataFromClient`) → `BDAO.processBriefs` :2395-2562 (SQL ghép chuỗi, không transaction, SMS + thông báo viết tay trong DAO). Dùng để hiểu dữ liệu `BRIEF_PROCESS` / `STATUS` hiện có (DB DEV `BRIEF_PROCESS` ngày 2026-10-01: loại 3 = 490, 4 = 59, 5 = 284, vẫn phát sinh đến 2026-09); tính năng mới nên làm theo mẫu 3 (gen-2, service có transaction, kiểm điều kiện ở BE). Các lỗi của luồng này: `dac-thu.md` L2–L4.
