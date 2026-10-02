# Thuật ngữ — tên trong code ↔ tên nghiệp vụ

Bảng này giải quyết 80% nhầm lẫn khi đọc code VOKhanhHoa. Cột "Trong code" liệt kê tên bảng / class / package thật.
Mỗi thuật ngữ **một dòng + trỏ sang phân hệ** viết chi tiết (ký hiệu `XLCV`, `VBĐi`, `VBĐ`, `CVB`, `LXL`, `SVB`, `LT`, `QLC`,
`PT`, `LNV`, `NVu`, `CV`, `HSCV`, `KS`, `HT` — xem `README.md`). Giá trị trạng thái ghi **giá trị số thật** đang lưu trong DB.

> (sửa 2026-10-02: rà lại toàn bộ theo 19 bài viết lại 2026-09-29 → 2026-10-02 — sửa các dòng lỗi thời, thêm thuật ngữ
> xuyên phân hệ. Bảng chỉ tóm tắt; chi tiết và nguồn `file:dòng` ở bài của phân hệ.)

## Văn bản

| Nghiệp vụ | Trong code | Ghi chú / xem |
|---|---|---|
| **Text ≠ Document** | `TEXT` = văn bản **đang soạn / trình ký** (chưa có số); `DOCUMENT` = văn bản **đã có bản ghi văn bản** (văn bản đến, hoặc văn bản đi đã cấp số) | Cấp số = sinh bản ghi `DOCUMENT` từ `TEXT` (`TEXT.STATE = 4`) — VBĐi NV-02 |
| **Văn bản dự thảo / trình ký** | `TEXT`, `TextEntity` (gen-2), `EntityText` (gen-1), `Requisition` (web), `textAction`, `TextController` + `DocumentSignController` (gen-1); web màn **Dự thảo** `documentDraft/documentDraft.zul` + `DocumentDraftVM`, hộp ký `requisition/requisition.zul` + `RequisitionVM` | `requisition` = trình ký. Viết tắt `vbdt`/`vbtk`/`vbkn`/`vbkd`/`vbxd`/`vbbh` — XLCV mục 6 |
| Trạng thái dự thảo `TEXT.STATE` | 0 chưa trình · 1 đang trình ký · 2 bị trả lại (về người tạo) · 3 đã ký duyệt, chờ cấp số · 4 đã cấp số / ban hành · 6 hủy luồng · 7 văn bản gốc đã trình lại · 27 hủy ban hành / từ chối cấp số (+ `DELETED_PROMULGATE = 1` = đã xóa) · 28 trình xin ý kiến; 5 "chờ ký nháy" chỉ có trong enum, không được gán | XLCV mục 4.6, VBĐi mục 4.7 |
| Người trong luồng ký `TEXT_PROCESS` | `SIGNATURE_TYPE` 0 trợ lý · 1 văn thư xét duyệt · 3 người xử lý chính (ký nháy / ký duyệt / phê duyệt theo `ACTION_ID` 5 / 2 / 4) · 4 xin ý kiến / cho ý kiến · 5 đọc soát | XLCV NV-02, NV-10 |
| **Văn bản đã ban hành / văn bản đến** (có bản ghi) | `DOCUMENT`, `DocumentAction` + `DocumentController` (gen-1, package `controler`), `DocumentDAO`; gen-2 `/api/doc`, `/api/doc-in`, `/api/doc-out`; web `document/*`, `DocumentBusiness` | Văn bản đến của đơn vị này có thể là văn bản đi của đơn vị khác (chuyển nội bộ) |
| Dòng nhận (luồng nhận) | `DOCUMENT_IN_STAFF` (cá nhân), `DOCUMENT_IN_GROUP` (đơn vị); cây xử lý `DOCUMENT_PROCESS` | Mọi hộp việc / nút văn bản đến tính **theo dòng nhận**, không theo văn bản — VBĐ 1.1 |
| Trạng thái dòng nhận `STATUS` | 3 chờ xử lý · 4 đã xử lý · 5 đã hoàn thành · 6 đã trả lại · 7 bị trả lại · 0 bị thu hồi | VBĐ mục 4.6, CVB mục 4.8 |
| Mã hộp văn bản đến (tham số tìm kiếm, **không phải** trạng thái) | 21 chờ tiếp nhận · 18 chờ xử lý · 19 đã xử lý · 20 đề nghị trả lại · 29 đã trả lại · 27 nhận để biết · 30 tất cả · 22 tra cứu · 23 / 24 sắp đến hạn / quá hạn | VBĐ NV-01, mục 6 |
| **Chủ trì / Phối hợp / Nhận để biết / Nắm tình hình** | Cột `SEND_TYPE` (`DOCUMENT_IN_STAFF`, `DOCUMENT_IN_GROUP`): **1** Chủ trì · **2** Phối hợp · **3** Nhận để biết; nắm tình hình lưu **3 + `IS_INFORMALITY = 1`** (hằng 4 `GRASP_SITUATION` không lưu; 5 Tham mưu chỉ là hằng). BE `Constants.Document.SEND_TYPE.TO/CC/NB/TH/TM`, web `AppConstants.DOCUMENT.SENT_TYPE.SEND_TO/CARBON_COPY/TO_KNOW/GRASP_SITUATION/PROPOSAL`; chuỗi `main`/`coordinate`/`toKnow`/`situation` chỉ là khóa i18n | Một văn bản có thể có **nhiều Chủ trì** (CVB 7.2 Q1). CVB NV-04, VBĐ BR-43, LNV NV-18 |
| Chuyển văn bản | `DocumentAction.sendDocument` / `sendDocumentMultiTransfer` → `DocumentInStaffDAO.sendDocument` (một lõi gen-1 cho mọi biến thể) | CVB 1.1 |
| "Ban hành" (văn bản đi) | = văn thư **chuyển** văn bản đã cấp số: `DOCUMENT.IS_FORWARD = 1` (tab *Đã ban hành*); khác "cấp số" (`TEXT.STATE = 4`, tab *Đã cấp số*) | VBĐi NV-11, CVB NV-08 |
| Tự động ban hành / nơi nhận dự kiến | `AUTO_PROMULGATE_TEXT` (cấp số tự động sau người ký cuối); `AUTO_SEND_TEXT`, `TEXT_RECEIVER(_GROUP)` (tự chuyển tới nơi nhận khai sẵn — chỉ khi ban hành tự động) | VBĐi NV-10, XLCV NV-17, CVB NV-09 |
| Thu hồi văn bản đã chuyển | `doEviction*` → dòng nhận `STATUS = 0` | CVB NV-10 (khác thu hồi văn bản đã gửi trục — LT NV-05; khác thu hồi ký — XLCV NV-12) |
| Trích yếu | `title` (`TEXT` / `DOCUMENT`) | Không phải "tiêu đề" file |
| Số đi / số đến | số đi `DOCUMENT.REGISTER_NUMBER`; số đến `DOCUMENT_RECEIVE_MAP.INCOMING_NUMBER`; số ký hiệu văn thư nhập (tự động ban hành ghép từ `TEXT_DEFAULT` của sổ) | SVB NV-07, mục 6 |
| Sổ văn bản | `TEXT_BOOK` (`TYPE` 0 sổ đi / 1 sổ đến, `YEAR_TYPE` 1 năm / 5 năm, bộ đếm `CURRENT_NUMBER`), `TEXT_BOOK_NUMBER` (đánh số theo thể loại), `TEXT_BOOK_SHARE` (sổ dùng chung); gen-1 `textBookAction`, gen-2 `/api/text-book` | Không có job "reset số" đầu năm — sổ năm mới do văn thư tạo hoặc hệ thống tự sinh bộ 4 sổ mặc định (SVB NV-06) |
| **Số chờ / giữ số** | `WAITING_NUMBER_BOOK`, `WaitingNumberBookEntity`, `/api/text-book/*-waiting-number` — giữ trước một số trong sổ; **không phải** "hàng chờ cấp số", web không gọi | SVB NV-09 (sửa 2026-10-02: bản cũ ghi "chờ cấp số") |
| Chờ cấp số | hộp *Văn bản ban hành* tab *Chờ cấp số* = `TEXT.STATE = 3` (cần phân quyền dữ liệu `REVIEW_PROMULGATE_DATA`) | VBĐi NV-01 |
| Báo cáo / in sổ văn bản | `documentHandover/documentBook.zul` + `DocumentBookVM` (menu `DOCUMENT_BOOK` "Báo cáo văn bản đi đến", `DOCUMENT_REPORT`) — nằm trong package bàn giao nhưng là báo cáo sổ | SVB NV-11 |
| Luồng ký / luồng xử lý | `FLOW` (`FLOW_TYPE` 1 văn bản đi / 2 văn bản đến), `NODE`, `NODE_DEPT_USER`, `NODE_TO_NODE`, `NODE_TO_NODE_ACTION` → `NODE_ACTION`; gen-2 `/api/flow-manager` | Cấu hình trong DB; luồng suy ra từ vị trí người dùng trong nút, không chọn theo tên (LXL NV-09). `REQUISITION_FLOW` là luồng cũ, không còn đường vào (LXL NV-14) |
| Bút phê / ý kiến lãnh đạo (văn bản đến) | `doComment`, `popupCommentProcess.zul`, `save-doc-leader-comment`, `DOCUMENT_LEADER_COMMENT` | VBĐ NV-07 (`DocumentConsultVM` "xin bút phê" là màn cũ không dùng) |
| Hạn xử lý | `DEADLINE_DATE` trên `DOCUMENT_RECEIVE_MAP` / dòng nhận; sắp đến hạn / quá hạn tính theo hạn đó (hộp 23 / 24) | VBĐ NV-12. Cấu hình hạn theo đơn vị và trường thông tin văn bản: menu `DOC_PROCESS_TERM_CONFIG` → `DocumentProcessTermBusiness` → `DOCUMENT_REQUEST_CONFIG(_MAP)` (HT NV-15). Cùng lớp `DocumentProcessTermBusiness` còn phục vụ cấu hình **tự chuyển sau tiếp nhận** (CVB NV-06) |
| Liên thông | kênh A trục cơ quan ngoài `CONNECT_*` (`connectDocumentAction`); kênh B VOConnect (tenant khác) `INTERNAL_DOC_*` + webhook `/api/hook`; kênh C nhiệm vụ qua trục `IN_OBJECT_*`; `goverment/*` (VPCP — code đã chú thích, không chạy) | Hệ thống chỉ ghi gói tin "hộp thư đi", tiến trình ngoài repo gửi — LT NV-01 |
| **Công khai văn bản** | `DOCUMENT_PUBLISHED` (`STATUS` 0 đang công khai / 1 đã hủy; chưa có dòng = chưa công khai) + phạm vi `DOCUMENT_SCOPE_REF`; `DocumentPublishVM`, `DocumentAction.publish/cancelPublish` | Khác "ban hành". Thao tác: VBĐi NV-12; phạm vi / quyền xem: QLC NV-10, NV-11 |
| **Thư viện văn bản** | = danh sách **văn bản đã công khai** mà phạm vi chứa đơn vị người xem (`documentLibrary.zul`, `DocumentLibraryVM`); thư mục thư viện `DOCUMENT_LIBRARY` chưa vận hành (DB DEV 0 dòng) | `tai-lieu-mau` NV-01, NV-03 |
| Bàn giao văn bản | menu `BGVB`, `DocumentHandoverAction`, `DOCUMENT_HANDOVER(_DETAIL)` — chuyển văn bản **mình nhận / mình tạo** sang người khác khi thôi phụ trách | QLC NV-08 (khác **bàn giao hồ sơ** — HSCV NV-12) |
| Quyền xem văn bản | `validateDocumentDetail`, `checkAllPermissionDoc` (xét nhiệm vụ, công việc, lịch họp, hồ sơ mượn, yêu cầu văn bản…) | QLC NV-06 |
| Văn bản mật | `STYPE_ID` / `securityLevel ≠ 1`, `FILE_ENCRYPT_MAP`, chứng thư mật `P12_CERT TYPE 1/2` | Đã xác nhận "nghiệp vụ mật chưa dùng" — đang hỏi lại (`_chung/cau-hoi-dot-2026-10.md` A3); KS NV-16 |

## Ký

| Nghiệp vụ | Trong code | Xem |
|---|---|---|
| Ký nháy / ký duyệt / phê duyệt | Bản ghi `TEXT_PROCESS.SIGNATURE_TYPE = 3` + `ACTION_ID` (= `NODE_ACTION_ID`) 5 ký nháy / 2 ký duyệt / 4 phê duyệt; `NODE_ACTION_CODE` `SIGN_INITIAL` / `SIGN` / `APPROVE`; ký nháy thể hiện ở `TEXT_PROCESS.STATE = 5`, không phải `TEXT.STATE` | XLCV NV-10 (sửa 2026-10-02: bản cũ ghi `signatureType = 2/3`, `PENDING_INITIALS(5)`) |
| Văn thư xét duyệt / trình duyệt | `SIGNATURE_TYPE = 1`, hộp `requisition.zul?view=2` (`VIEW_TYPE.VBXD`) | XLCV NV-10 (ranh giới VBĐi) |
| Xin ý kiến / cho ý kiến (dự thảo) | `SIGNATURE_TYPE = 4`, `TEXT.STATE = 28` khi trình xin ý kiến; không ký | XLCV NV-09 |
| Công cụ ký | USB Token (`makeUsbSignalFileSession`, plugin máy người dùng), SIM CA (`Sign.SignTextByCASIM` — chỉ site công khai), CloudCA / MySign (`Sign.SignCloudCA`); hình thức trên popup `DIGITAL_SIGNATURE.TYPE` 1 USB / 2 SIM / 3 thường / 4 CloudCA / 5 ký nháy / 6 ký nháy SIM | KS NV-01 … NV-06 |
| Ảnh chữ ký / vị trí ký | `STAFF_IMAGE_SIGN`, `TEXT_SIGN_LOCATION` | KS NV-07, NV-08 |
| Con dấu đơn vị / đóng dấu số | ảnh dấu `IMAGE_ORG` (`GROUP_TYPE` 1 đơn vị / 2 xác nhận / 3 hồ sơ); nghiệp vụ xin dấu / đóng dấu `TEXT_MARK`, `TEXT.STATE_MARK` | Cơ chế: KS NV-10, NV-11; nghiệp vụ: VBĐi NV-06 … NV-09 |
| **Cặp trình ký** | `SIGN_BRIEFCASE*`, menu `CTK`, `signBriefcaseAction` — theo dõi **cặp hồ sơ giấy** có mã vạch đưa lãnh đạo ký, trợ lý cập nhật từng người ký; **không** phải ký số, **không** phải hồ sơ | KS NV-13 |
| Giao dịch ký của hệ thống ngoài | `AUTO_DIGSIG_TRANSACTION` / `AUTO_DIGSIG_RESPOND`, `sendAndSign`, `EXT_APP` (KNTC…) | KS NV-15 |

## Công việc, nhắc việc, đánh giá

| Nghiệp vụ | Trong code | Phân biệt / xem |
|---|---|---|
| **Nhiệm vụ** (mission) | `MISSION`, `missionAction` (gen-1, **có** kiểm quyền theo nhiệm vụ), web `mission/*` | Đơn vị giao đơn vị, hoặc giao **một cá nhân chủ trì** (`SPONSOR_ID`); duyệt tiến độ hai cấp; `STATUS` 4 đã kết thúc · 5 đề xuất đóng · 6 đã đóng · 7 đề xuất gia hạn — `nhiem-vu` 1.1, mục 4.6 |
| **Công việc** (task) | `TASK`, `taskAction`, `TaskService`, web `task/*`, menu `TASK_PERSONAL` | Việc của **một cá nhân** theo **kỳ** (`PERIOD` quý / năm), có tỷ trọng, phiếu giao việc đầu kỳ / phiếu đánh giá cuối kỳ — `cong-viec` 1.1 |
| Nguồn gốc nhiệm vụ / công việc | `SOURCE_MAP` (`OBJECT_TYPE` 1 công việc / 2 nhiệm vụ / 4 định hướng; `SOURCE_TYPE` = loại nguồn: văn bản, biên bản họp, kiến nghị, định hướng 5…) | Cả nhiệm vụ lẫn công việc **đều có thể** có văn bản làm nguồn — không phân biệt bằng "gắn văn bản" (sửa 2026-10-02) |
| **Nhắc việc** | `REMINDER`, `REMINDER_REPLY`, `REMINDER_FOLLOWERS`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_HISTORY`, gen-2 `/reminders` (không tiền tố `/api`), web `reminder/*` | Đơn vị phát hành **giao việc kèm văn bản** cho đơn vị chủ trì / phối hợp có hạn; đơn vị được nhắc trả lời, bên giao duyệt; `REMINDER_REPLY.STATUS` 4 lưu tạm · 0 chưa trả lời · 5 đã xử lý tạm · 1 chờ duyệt · 2 xử lý lại · 3 hoàn thành; **không gửi SMS** — LNV NV-01 … NV-10 (sửa 2026-10-02: tên bảng thật có `S`) |
| **Phiếu trình** | `SUBMISSION_FORM` (+ `_PROCESS`, `_FILE`, `_MAP`, `_FORWARD`), gen-2 `/api/submission-manager`, web `submissionForm/*` | Phiếu xin ý kiến nội bộ, **không số, không sổ, không ban hành**; kết quả là PDF có ý kiến + chữ ký; hoàn thành thì dự thảo kèm theo tự trình ký — PT 1.1, NV-09 |
| Kiến nghị / khó khăn vướng mắc | `REQUEST`, `request/*`, `RequestVM`, `RequestAction`, `ProposalBusiness` (web truy vấn thẳng DB) | Chưa có phân hệ riêng — tạm ở PT NV-18. Khác **khó khăn vướng mắc của tiến độ nhiệm vụ** (`MISSION_PROCESS.DIFFICULT`, `RESOVLE_ISSUE`) — NVu NV-11 |
| Định hướng | `ORIENTATION`, `ORIENT_RECEIVE_ORG` | Menu đang khóa; nguồn nhiệm vụ "Theo định hướng" `SOURCE_TYPE = 5` — LNV NV-19 |
| **Nắm tình hình** / thông tin phục vụ lãnh đạo | menu `GRASP_SITUATION`, `DOCUMENT_INFORMALITY*`, gen-2 `/api/document-informality`; văn bản đến "nắm tình hình" = `SEND_TYPE = 3` + `IS_INFORMALITY = 1` | LNV NV-17, NV-18 |
| Thông báo / SMS | chuông `NOTIFICATION`; bảng tin `NOTICE`; SMS ghi hàng đợi `MESSAGE` / `SMS_MASTER` qua `SmsDAO` (+ kiểm chặn `shouldSendSms`), **tiến trình ngoài repo** gửi; chặn tin `SMS_BLACK_LIST` (người) / `CONFIG_SMS_ORG` (đơn vị), loại tin `CONFIG_SMS_MODULE` | LNV NV-11 … NV-15, mục 5.2 |
| Đánh giá công tác tuần | `WORK_GROUP` (cây **nhóm nhiệm vụ** mẫu — không liên kết `MISSION`), `WORK_GROUP_ITEM`, `REP_IN`, gen-2 `/api/work-group*`, `/api/report-period-*` | `kpi-danh-gia` NV-01 … NV-08 (sửa 2026-10-02: bản cũ ghi `WORK_GROUP` "nhóm theo dõi nhiệm vụ chung (?)") |
| **KPI — ba nghĩa khác nhau** | (1) **KPI đơn vị** = điểm nề nếp tháng cấp trên chấm (`KPI_INDEX`, legacy); (2) **Theo dõi KPI** = đúng hạn / quá hạn xử lý văn bản, phiếu trình, hồ sơ (`/api/kpi`); (3) **Cổng KPI** = hiệu năng API hệ thống (`/api/kpi-portal`, bảng `KPI`) | `kpi-danh-gia` NV-15, NV-20, NV-21. "Tạo KPI nhiệm vụ" khi chuyển văn bản là dịch vụ khác (CVB NV-21) |
| KI | **KI cá nhân** hằng tháng `EMP_RATING.KI` (1 A · 2 B · 3 C · 4 D1 · 5 D2), **KI đơn vị** `ORG_KI`; tỷ lệ `RATIO_CONFIG` | CV NV-09; cấu hình: `kpi-danh-gia` NV-18 |
| Chấm điểm thi đua đơn vị | `ORG_CRITERIA*` (gen-1 `/orgCriteria`) — **khác** bộ tiêu chí nề nếp `CRITERIA_GROUP` / `CRITERIA` | `kpi-danh-gia` NV-09 … NV-14 |

## Hồ sơ

| Nghiệp vụ | Trong code | Phân biệt / xem |
|---|---|---|
| Hồ sơ | `BRIEF`, thư mục `CATALOG_BRIEF`, `/Brief`, `/api/brief` | HSCV 1.1 |
| **Bàn giao hồ sơ** | `processBrief` type 3 / 5 / 4, `BRIEF.STATUS` 3 / 5 / 4 (bàn giao / tiếp nhận / từ chối) — chuyển **quyền sở hữu** hồ sơ cho người khác | HSCV NV-12 |
| **Nộp lưu** (nộp hồ sơ) | `submit-brief`, `BRIEF_SUBMIT_*`, `SUBMIT_STATUS` 0 đang thực hiện · 1 đã nộp · 2 đã tiếp nhận · 3 từ chối · 4 thất bại — gửi sang **phần mềm số hóa văn bản** (hệ thống ngoài, `APP_SHVB`), kết quả về qua callback | HSCV NV-15 (khác bàn giao hồ sơ) |

## Tổ chức & người dùng

| Nghiệp vụ | Trong code | Xem |
|---|---|---|
| Đơn vị | `VHR_ORG` (web entity `SysOrganization`, gen-2 `VhrOrgEntity`); cây theo `PATH`, gốc id 1; cấp / độ sâu suy từ `PATH` (`ORG_LEVEL` không tin được) | HT NV-11; đồng bộ VHR đã tắt — quản trị nhập (HT NV-08) |
| Đơn vị cấp 0 / cấp 1 (Khánh Hòa) | cấp 0 = `PATH` `/1/<id>/`; cấp 1 = `/1/<id cấp 0>/<id>/`; tên "cấp 1" trong code có chỗ là cấp 0 nghiệp vụ | CVB mục 6, NV-03 |
| Người dùng / nhân viên | `VHR_EMPLOYEE` (web entity `SysUser`, gen-2 `VhrEmployeeEntity`); tên đăng nhập `EMPLOYEE_CODE`; `employeeId` trong JWT (`CoreUtils.getUserId()`) | HT NV-06 |
| Vai trò tại đơn vị | `SYS_ROLE` + `USER_ROLE` (vai trò của người ở từng đơn vị); mã: `VT` văn thư 336954 · `LDDV` 336952 · `TTDV` 336953 · `NV` 336955 · `TL` 336871 · `ADMIN` 336815 · `ADMIN_LEVEL1` 337591 · `QLLH` quản lý lịch họp · `LT` lưu trữ hồ sơ 336956 | HT 1.4 (id theo DB DEV) |
| Quyền thao tác | = **menu được cấp** (`ROLE_MENU` + danh sách trắng `ORG_SYS_MENU`) + điều kiện hiện nút trong VM; cơ chế thao tác × tài nguyên VPS đã tắt, RBAC gen-2 luôn cho qua | HT NV-03, NV-09 BR-25 |
| Nhóm cá nhân / nhóm dùng chung | `CV_GROUP` (`GROUP_TYPE` 1 cá nhân · 2 vai trò · 5 đơn vị nội bộ · 6 đơn vị liên thông; `IS_PUBLIC`) | HT NV-12, CVB NV-16 |
| Cấu hình người dùng theo đơn vị | `USER_ORG_MAP.TYPE` 1 giao việc · 2 trợ lý chuyên hướng · 3 lãnh đạo chuyên quản · 4 chấm điểm · 5 / 6 theo dõi văn bản | HT NV-07 |
| Trợ lý lãnh đạo | `MEETING_ASSISTANT.ASSI_TYPE` (1 lịch · 2 văn bản · 5 sửa lịch · 6 duyệt lịch · 12 cùng nhận văn bản …) | `hop` NV-08 |
| VPS | package `com.viettel.vps` = quản trị hệ thống legacy trong web (người dùng, vai trò, menu, thao tác, tài nguyên) | HT mục 2 |

## Khác

| Từ | Nghĩa |
|---|---|
| `DEL_FLAG` | Xóa mềm: thường 0 hoạt động, 1 đã xóa — **có bảng comment DB ghi ngược** (vd. `CATEGORY_COMMON`, HT dac-thu bẫy 15); tin code, không tin comment |
| `isSecurity` | Tham số gen-1: request có mã hóa AES/RSA hay không |
| `serviceConnection` | Kết nối web→BE gắn với HttpSession (cookie + JWT) |
| `Delegate.getService(I*.class)` | Lấy facade legacy trong web (web truy vấn thẳng DB) |
| `LookupUtil.showLookup/showDialog` | Mở popup chọn dữ liệu (ZK) |
| `LookupUtil.getPopupPermision` | **Không phải** kiểm quyền: đếm cửa sổ popup đang mở theo `screenName` để không mở trùng (`web-spring/src/main/java/com/viettel/zk/common/LookupUtil.java:71-94`) (sửa 2026-10-02) |
| `EventQueues.lookup(...)` | Cơ chế reload giữa các VM ZK (ví dụ `EVENT_QUEUE_HOME_PAGE`) |
| `CODE_MASTER` | Danh mục động (trạng thái, loại) đọc bằng key `code.*` — HT NV-13 |
| `CATEGORY_GROUP` / `CATEGORY_COMMON` | Danh mục nhóm phân loại + giá trị, áp theo đơn vị (`GROUP_APPLY`) — HT NV-13 |
| `SYSTEM_PARAMETER` | Tham số hệ thống (nhiều khóa chứa địa chỉ / tài khoản — chỉ ghi tên khóa) — HT NV-14 |
| Site công khai / nội bộ | `vps.site` `public` / `private`; hai site đồng bộ dữ liệu qua trigger `VO_SOURCE_*` — `tich-hop` NV-13 |
| `ToolGen` | Bộ sinh code gen-2 (`voffice-gencode`), comment "Autogen class" |
