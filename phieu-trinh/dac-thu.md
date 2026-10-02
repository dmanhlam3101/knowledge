# Phiếu trình — đặc thù, bẫy, lỗi hệ thống ghi nhận

> Viết lại từ code `kha_develop` ngày 2026-10-01. Viết tắt đường dẫn / lớp như `nghiep-vu.md` (WEB, ZUL, BIZ, BE1, BE2, SQL; SFLVM, SFLDVM, SFRKVM, TSVM, CSDDVM, ASFPVM, PSVM, PSRSVM, SLS, DDVM, SFB; SMC, SMSI, SMRI, SFWSI, SFWRI, SPRJ, SMRJ, SFRI, SFSI, C1, C2, DSDAO).

## 1. Tình trạng kỹ thuật

| Phần | Tầng | Nguồn |
|---|---|---|
| Toàn bộ phiếu trình (danh sách, đếm, lưu, trình, ký, từ chối, hủy, xin / cho ý kiến, chuyển tiếp, theo dõi, hồ sơ) | **gen-2** `SubmissionManagerController` → `SubmissionManagerServiceImpl` / `SubmissionForwardServiceImpl` → repository (JPA + SQL thuần qua `BaseRepository`) | SMC:47; `nghiep-vu.md` mục 2 |
| Trình ký dự thảo khi phiếu hoàn thành, "ký luôn dự thảo" | gen-2 gọi thẳng **DAO gen-1** `DocumentSignDAO.sendAndSign` / `sendAndSignLastSigner` | SMSI:2214, 2218 |
| Chọn dự thảo để đính kèm; lưu liên kết dự thảo ↔ phiếu đã phê duyệt | **gen-1** `textAction.searchTextForSubmission` (`TextSearchDAO`), `DocumentSignDAO.addText/editText` | `BE1/action/TextAction.java:127`; DSDAO:990-997, 2735-2753 |
| Web | Một VM khổng lồ **SFLVM** (~12.250 dòng) phục vụ **cả hai menu** (`view=0` người trình, `view=1` người xử lý) + form soạn; phần lớn mã (ký hàng loạt, đóng dấu, `VBXD/VBKD/VBBH`, công bố…) là **bản sao từ màn dự thảo / trình ký** không dùng cho phiếu trình | SFLVM:1251-1279, 2235-2316, 6515-7071 |
| Tìm kiếm chung (Elasticsearch) | Phiếu trình có mẫu truy vấn riêng cho từng hộp (`els_query/phieu_trinh/*.json`) dùng ở trang chủ / tìm kiếm tất cả | `BE1/elasticsearch/search/ElasticHomeSearch.java:159-163`; `C2:683-690`; `WEB/voffice/vm/search/SearchAllVM.java:611-622` |

Quy tắc chọn chỗ sửa: **điều kiện một hộp việc** → `SMRI.submissionGetList` (và các bản lặp — bẫy 6); **thao tác trên phiếu** → `SMSI` (mẫu: `submitForm`, `cancelForm`, `updateStatusSign`); **nút hiện / ẩn** → các hàm `check*` trong SFLVM / SFLDVM / SFRKVM và khởi tạo nút trong PSVM (bẫy 7).

## 2. Bẫy

1. **`SUBMISSION_PROCESS.SIGN_TYPE` hai nghĩa**: trước khi xử lý là *hành động* người trình đặt (0 Phê duyệt / 12 Ký duyệt — SFLVM:9980-9983); sau khi xử lý BE **ghi đè** bằng hình thức ký đã dùng (0 / 1 SIM / 2 USB — SMSI:2024). Mọi logic "người này phải ký số không" (`isSignProcess` — SFLVM:10038-10052, ASFPVM:127-140, SFLDVM:996) đọc giá trị 12; mọi logic "đã ký bằng gì" (gỡ chữ ký khi tải — SMSI:1480-1483) đọc 0/1/2. Khi mở lại phiếu để sửa / sao chép, web chỉ đổi 2 → 12 (SFLVM:9298) — giá trị 1 (đã ký SIM) không được đổi (xem L4).
2. **Hằng trạng thái dùng lẫn giữa phiếu và dòng xử lý**: BE ghi dòng người trình `STATUS = Constants.SubmissionForm.Status.PROCESSED (4)` (SMSI:1317) và `addStrStatusProcess` so trạng thái **dòng xử lý** với hằng `SubmissionForm.Status.REJECTED / PROCESSED / NEW` (SMSI:2664-2685) — đúng giá trị nhờ trùng số 0/2/4 với `SubmissionProcess.Status`. Đổi số của một bên sẽ hỏng bên kia.
3. **Lưu phiếu trạng thái 0 = xóa hết rồi chèn lại** file, liên kết, người xin ý kiến (SMSI:1024-1025, 1103-1104, 1156-1157): mọi `SUBMISSION_FILE_ID`, `SUBMISSION_MAP_ID`, `SUBMISSION_PROCESS_ID` đổi sau mỗi lần lưu; quyền file mật phải dời `OBJECT_ID` (SMSI:1075-1079). Đừng giữ tham chiếu tới các ID này từ bảng khác.
4. **Một bảng `SUBMISSION_MAP` cho hai hướng phiếu ↔ dự thảo** (`nghiep-vu.md` NV-11). Màn dự thảo, khi bỏ chọn phiếu trình đã phê duyệt, xóa **mọi** liên kết `OBJECT_TYPE = 1` của dự thảo (`deleteSubmissionMapsBySubmissionFormId(objectId, objectType)` — DSDAO:2736-2740; SMRJ:44-46), kể cả liên kết do phía phiếu trình tạo. `check-exist-object-id` cũng không phân biệt hướng / trạng thái phiếu (SMSI:2802-2811).
5. **Hộp việc phiếu trình phụ thuộc trạng thái dự thảo**: tab Đang xử lý / Đã phê duyệt / Đã trả lại đọc `TEXT.STATE` của dự thảo kèm theo (SMRI:518-555) và cột trạng thái hiển thị đổi theo dự thảo (SMRI:609-680). Thay đổi giá trị `TEXT.STATE` ở phân hệ dự thảo / văn bản đi ảnh hưởng hộp việc phiếu trình.
6. **Điều kiện 4 tab lặp ở ít nhất 5 chỗ** — sửa một chỗ phải sửa tất cả: `submissionGetList` nhánh cá nhân `-1` (SMRI:414-471), nhánh chung theo `searchType` (:518-562), `submissionGetListByOrgLeaderId` (:155-206), `getTotalSubmissionByCreator` (:1166-1207), `getTotalSubmission` (:1237-1275); thêm mẫu Elasticsearch `els_query/phieu_trinh/*.json`.
7. **Nút trên chi tiết phiếu (PSVM) tính riêng**, không dùng lại hàm `check*` của lưới: "Cho ý kiến" / "Chuyển xin ý kiến" bật trong `postViewInitialized` theo dòng của người xem (PSVM:265-280), "Trình" ẩn khi không phải 0 / không phải người tạo (:246-250), "Chuyển tiếp" theo `checkViewForward` (:172-174). Đổi điều kiện nút phải sửa cả lưới (SFLVM:3758-3896), Theo dõi (SFLDVM:1086-1156, 1422-1429), Nhận để biết (SFRKVM:533-538) và chi tiết.
8. **Điều hướng bằng mã menu**: tab "Tất cả" của hộp ký duyệt đóng tab và mở menu `SUBMISSION_FOLLOW` (SFLVM:8930-8934, 9000-9038); các tab trên màn Theo dõi mở menu `SUBMISSIONFPROCESSLIST` kèm `tabType` (SFLDVM:208-246); nút "Tạo dự thảo" mở menu mã `SIGN` (SFLVM:4075); "Tạo phiếu trình" trên dự thảo mở menu `SUBMISSIONLIST` (DDVM:18838). Đổi `SYS_MENU.CODE` làm hỏng điều hướng.
9. **Khóa đồng thời chỉ ở ký / từ chối / hủy** (`findBySubmissionFormIdForUpdate`, chờ 0 giây — `BE2/repositories/jpa/SubmissionFormRepositoryJPA.java:50-55`; SMSI:1361-1367, 1784-1790, 2590-2596). Trình, lưu, chuyển xin ý kiến, cho ý kiến, chuyển tiếp không khóa.
10. **Số người hiện ảnh ký giới hạn bởi số mẫu Word**: file phiếu chọn mẫu `<n>_phieu_trinh.docx` với n = số dòng có `IMAGE_SIGN = 1` (`BE2/utils/FileUtils.java:73-78`; SMSI:2294-2303); repo chỉ có mẫu 1…20 (`backend2.0/backendvoffice/src/main/resources/report/template/` và `…/one_org_phieu_trinh/`). Không có mẫu tương ứng thì dịch vụ chuyển đổi báo lỗi → hàm trả `null`; lỗi ngoại lệ khác lại trả đường dẫn file chưa tạo (FileUtils.java:179-186; SMSI:2354-2357).
11. **Dòng loại 4 sao từ dòng của người hỏi** (cùng `SIGN_LEVEL`, `SIGN_TYPE`, chức vụ của người hỏi rồi mới ghi đè người được hỏi — PSVM:2381-2408). Truy vấn nào lọc theo `SIGN_LEVEL` mà quên `SIGNATURE_TYPE` sẽ lẫn người được hỏi vào nhóm ký (xem L2, L3).
12. **`SUBMISSION_FORM.SIGN_LEVEL` sau khi hoàn thành = cấp cuối + 1**; truy vấn "người ký cuối phiếu" dùng `s.sign_level = sp.sign_level + 1` (SFRI:35). Truy vấn `next-signer` dùng `sf.signLevel + 1` (SMRI:1131).
13. **Phiếu mật** (`STYPE_ID ≠ 1`) đi nhánh riêng ở gần như mọi thao tác (mã hóa phía trình duyệt, `FILE_ENCRYPT_MAP`, không sinh PDF khi trình) — nghiệp vụ mật chưa dùng; đừng gộp sửa hai nhánh.
14. `ban-do.md` ghi `widgets/lookupDocumentSubmission.zul` (`widget.SourceLookupSubmission`) và `lookupDocumentSubmissionBrief.zul` (`widget.SourceLookupSubmissionBrief`) là "☠ VM không tồn tại" — **sai**: hai lớp có ở `WEB/voffice/widget/SourceLookupSubmission.java`, `SourceLookupSubmissionBrief.java` và đang được DDVM:6694, `ViewUtil.java:1376-1384` dùng (nhãn sai do bộ quét `_tools`, có thể vì tên lớp không kết thúc bằng `VM`). (sửa 2026-10-01: knowledge cũ coi là màn chết)

## 3. Lỗi hệ thống — ghi nhận (không sửa trong phạm vi xây tri thức)

| # | Hiện tượng | Nguồn |
|---|---|---|
| L1 | Kiểm ảnh ký người cuối dùng `x != null \|\| x.getVhrEmployeeId() != null` → khi không tìm thấy dòng nào sẽ ném NullPointerException thay vì báo lỗi nghiệp vụ | SMSI:1168, 1298 |
| L2 | `updateAdvice` cập nhật **mọi** dòng `STATUS = 0` của người gọi trên phiếu, không lọc `SIGNATURE_TYPE = 4` (bản SQL cũ có lọc, nay bị comment) → nếu người đó cũng là người xin ý kiến chính chưa tới lượt, dòng ký của họ cũng thành 4 "Đồng ý" mà không ký | `SPRJ:57-65`; SMRI:1568-1575 |
| L3 | `findCurrentSigner` không lọc `SIGNATURE_TYPE` → người được hỏi ý kiến (loại 4) cùng cấp hiện tại có thể gọi thẳng API ký / từ chối phiếu; `listSigner.get(0)` lấy dòng đầu khi một người có nhiều dòng cùng cấp | `SPRJ:43-46`; SMSI:1802-1804, 2597-2599 |
| L4 | Sao chép / trình ký lại phiếu có người đã ký **SIM CA**: giá trị `SIGN_TYPE = 1` không được đổi về 12 (chỉ đổi 2 → 12) → combobox hành động trống, người đó bị coi là "Phê duyệt" thường | SFLVM:9298, 9980-9983; ASFPVM:127-140 |
| L5 | Khi từ chối, đoạn gửi SMS / thông báo cho người cùng nhóm dùng điều kiện `isEmpty()` rồi mới lặp → **không bao giờ chạy** | SMSI:2103-2112 |
| L6 | Khi từ chối mà cùng cấp không còn ai chờ, `SUBMISSION_FORM.SIGN_LEVEL` vẫn bị tăng lên cấp kế dù phiếu đã trả lại | SMSI:2031-2036, 2060-2061 |
| L7 | Lưu lại phiếu (xóa – chèn `SUBMISSION_MAP`) không xóa `SUBMISSION_MAP_FILE` của liên kết hồ sơ cũ → bản ghi mồ côi trỏ `SUBMISSION_MAP_ID` không còn — **DB xác nhận: 59 dòng `SUBMISSION_MAP_FILE` mồ côi** (DB DEV ngày 2026-10-01) | SMSI:1104, 1138-1150; `SubmissionMapFileJPA` |
| L8 | `listFileEncryptMap` lấy file theo đơn vị nhưng truyền `userId` thay cho danh sách đơn vị (`orgIds`) với loại quyền `GROUP` | SMSI:3054-3058 |
| L9 | `orderBy` từ client nối thẳng vào SQL (`ORDER BY` + chuỗi) ở các truy vấn danh sách | SMRI:230-231, 576-577 |
| L10 | Bộ lọc dự thảo chọn đính kèm: `NOT EXISTS` không lọc `OBJECT_TYPE = 1` và không lọc phiếu đã xóa (`DEL_FLAG`) → dự thảo trùng ID với văn bản đến / hồ sơ đã gắn phiếu bị loại nhầm; dự thảo gắn phiếu đã xóa (0, `DEL_FLAG = 1`) vẫn bị coi là đã gắn | `BE1/database/dao/document/TextSearchDAO.java:1934-1939` |
| L11 | Nút "Chuyển xin ý kiến" bật cho mọi dòng loại 3 `STATUS = 0` của người xem, kể cả người ở **cấp chưa tới lượt** | PSVM:275-278 |
| L12 | Nút "Cho ý kiến" vẫn bật khi phiếu đã hoàn thành / đã hủy / bị trả lại (chỉ loại trừ phiếu 0); BE `updateAdvice` không kiểm trạng thái phiếu — **nghiệp vụ** (Q2, 2026-10-01): phiếu đã duyệt xong thì **không được cho ý kiến nữa** → hành vi hiện tại lệch nghiệp vụ | PSVM:265-274; SMRI:1532-1540 |
| L13 | Ô widget / nhãn tab đếm qua `count-home` mất tới 20 giây chờ; quá hạn thì mọi ô = 0 (ô "Xin ý kiến" không được đặt lại → giữ giá trị khởi tạo) | SMSI:242-261 |
| L14 | Code chết / thân giả trong SFLVM: `doCancelProcess` (kết quả gán cứng 1), `doSubmitSubmissionForm` (gán cứng 1), `doPopUpTransferDoc` (rỗng), `rejectRequisition`; lớp `SubmissionDetailVM` rỗng; `ZUL/submissionForm/signatureImageSelector.zul` trỏ VM không tồn tại (`vm.admin.requisition.SignatureImageSelectorVM`) | SFLVM:3608-3671, 3696-3756, 3821-3829; `SubmissionDetailVM.java`; `signatureImageSelector.zul:4` |
| L15 | Endpoint migrate một lần `update-all-submission-7939827832452673672323443432323` vẫn mở, không kiểm quyền | SMC:193-197; SMSI:2361-2425 |
| L16 | Script `SQL/sql_17072026.sql:5` gán `HOME_WIDGET.ID = 72` cho `SUBMISSION_XIN_Y_KIEN`, DB DEV dùng id 73 (72 đã là `IN_NHAN_DE_BIET`) — script không chạy lại được nguyên trạng | DB DEV `HOME_WIDGET` 2026-10-01 |
| L17 | Mã widget `SUBMISSION_DA_TU_CHOI`, `SUBMISSION_DU_THAO_CHO_KY` có trong code nhưng không có trên DB DEV; BE vẫn chạy phép đếm "đã từ chối" cho mỗi lần tải trang chủ | `WEB/util/AppConstants.java:8326-8327`; SMSI:209-218 |
| L18 | Menu thử nghiệm `MENU_TEST` (440945) trỏ màn phiếu trình, đã `DEL_FLAG = 1` | DB DEV `SYS_MENU` 2026-10-01 |
| L19 | Cột / bảng trên DB không có trong code `kha_develop`: `SUBMISSION_FORM.FORM_TYPE` (116 dòng có giá trị), `SUBMISSION_FILE_CHECKING`, `SUBMISSION_TRACKING_ELK`, `SUBMISSION_NOTE`; `SUBMISSION_PROCESS.STATUS` có 3 dòng = 1 và 45 dòng null ngoài các giá trị code ghi | DB DEV 2026-10-01; `nghiep-vu.md` mục 5 |
| L20 | Typo tên trong code (giữ nguyên khi tìm kiếm): `tranfer-give-advice`, `SubmissionFowardRepositoryImpl`, `getSubmisisonProcess`, `generatSubmissionFile`, `SUMARY`, `IS_PARALLELE_APPROVE`, `OPINION_SUBMITER`, `createLookupApproveSubmissonForm`, mã menu cha `SUMISSIONFORM` | SMC:306, 153, 235; entity; `ViewUtil.java:3683`; DB DEV |

## 4. Yêu cầu hay gặp → hướng

| Yêu cầu | Hướng |
|---|---|
| Thêm điều kiện chặn / cho phép phê duyệt | BE `SMSI.signSubmission` (trước `updateStatusSign`) + `findCurrentSigner`; web ASFPVM (`doApproveSubmissionForm`, `doSignSubmissionForm`) và nút trên lưới / chi tiết (bẫy 7) |
| Thêm tab / hộp việc phiếu trình | `searchType` mới ở `C2:534-555` + nhánh trong `SMRI.submissionGetList` (bẫy 6) + `SubmissionCountThread` + `SMSI.submissionCountHome` + `SubmissionInfoEntity` (web) + nút tab `submissionFormProcess_search.zul` + `SFLVM.changeTab` / `getMenuLabel`; nếu có widget: `HOME_WIDGET` + `HomeWidgetRestController.generateSubmissionWidget` |
| Thêm trường cho phiếu | `SubmissionFormEntity` + DTO + `SMSI.createOrUpdate` (cả nhánh sửa :922-948) + form `submissionForm_add.zul` / SFLVM `validateDoSave` + dữ liệu in `FileUtils.generateSubmissionFile` (:98+) và **mọi mẫu `<n>_phieu_trinh.docx`** |
| Đổi việc gì xảy ra với dự thảo khi phiếu xong / bị trả lại / bị hủy | `SMSI.submitTextAfterCompleteSubmissionForm` (:2190), `rejectTextAfterRejectOrCancelSubmissionForm` (:2163); phía dự thảo `DSDAO.sendAndSign` / `sendAndSignLastSigner`, `XLCV BR-38`, `BR-54/55` |
| Thông báo / SMS mới ở một bước | Mẫu `sendSMSSubmission` + `addNotification` (SMSI:2702-2753) với nhóm tin 15 và loại mới; mã mẫu SMS ở `C1:1436-1440`, cấu hình mẫu → `lich-nhac-viec` |
