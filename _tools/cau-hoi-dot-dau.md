# Câu hỏi cần chủ dự án trả lời — đợt viết lại tri thức 2026-09-29 → 2026-10-02

> **Cách dùng (chốt 2026-10-02):** chủ dự án **không trả lời một lượt** — các câu được làm rõ dần **khi phát triển
> tính năng liên quan**. Khi nhận yêu cầu chạm vào một phân hệ, xem các câu của phân hệ đó ở đây (hoặc mục 7.1 của
> `nghiep-vu.md`) và hỏi lại người giao việc / BA đúng câu liên quan. Trả lời được câu nào thì: gõ ngay sau dòng
> `> **Trả lời:**` (hoặc báo trong chat) → câu được chuyển sang mục 7.2 của phân hệ, sửa BR/NV liên quan, chạy lại
> `_tools/questions.py`; file này sinh lại từ mục 7.1 nên tự bớt dần.
>
> Mỗi câu ghi mã `phân hệ · Qn` và trỏ NV/BR trong bài để tra ngữ cảnh. Phần "Hiện trạng" mô tả hệ thống đang chạy
> thế nào (đã đối chiếu code `kha_develop` + DB DEV).

## Tổng quan

{{BANG_TONG}}

Cộng thêm **5 quyết định chung** ở phần A → tổng cộng {{TONG}} câu theo phân hệ + 5 quyết định.

---

## A. Quyết định chung (ảnh hưởng nhiều phân hệ)

### A1 · Xếp lại thành phần bị phân loại nhầm trong `knowledge/_tools/domains.py`

**Hiện trạng:** `ban-do.md` của mỗi phân hệ do máy sinh theo regex trong `domains.py`. Khi đọc code, các agent thấy
nhiều thành phần bị xếp nhầm phân hệ (thường do regex khớp chuỗi con, vd. `mission` khớp cả `permission`; `brief`
khớp `SignBriefcase`). Danh sách đề xuất (đã gom từ 13 phân hệ):

| # | Thành phần | Đang ở | Nên về |
|---|---|---|---|
| 1 | `request/*`, `admin/request/*`, `RequestVM`, `RequestDetailVM`, `RequestAction`, `ProposalBusiness`, `vm/config/ProposalVM`, `configPersonal/proposal.zul`, entity `Request`, `RequestEmail` (kiến nghị / khó khăn vướng mắc) | `phieu-trinh`, `he-thong` | **phân hệ mới `kien-nghi`** (xem A2) |
| 2 | `Permission*`, `RolePermission*`, `vps/sysRole/rolePermission.zul`, `widgets/permissionLookup.zul` (regex `mission` khớp "permission") | `nhiem-vu` | `he-thong` |
| 3 | `meeting/popup/permissionViewFile.zul`, `widgets/template/calendar/templateCalendar_editor.zul` | `nhiem-vu`, `tai-lieu-mau` | `hop` |
| 4 | `mission/kpi/*`, `mission/proposePoint/*`, `mission/workGroup*`, `mission/report/*`, `workItemApprove/*`, `reportPeriodConfig/*` | `nhiem-vu` | `kpi-danh-gia` |
| 5 | `templateReport/*`, `vm/template/*` (báo cáo đơn vị theo mẫu — BE ở `nhiem-vu`) | `tai-lieu-mau` | `nhiem-vu` |
| 6 | `Alert.java`, `AlertFeedback`, `AlertJpaDao`, `timeConfig/*`, `TimeConfigVM`, `TimeConfigDAO` | `lich-nhac-viec` | `cong-viec` |
| 7 | `orientation/*`, `sourceLookupOrientation` (Định hướng — menu dưới QUẢN LÝ NHIỆM VỤ) | `lich-nhac-viec` | `nhiem-vu` (hoặc giữ) |
| 8 | `SignBriefcaseAction/Controler/DAO` (cặp trình ký), signature core (`http/signature/*`, `ConfirmSignVM`, `CloudCAPopupVM`, `vps/sysImageOrg/*`…) | `ho-so-cong-viec`, `he-thong` | `ky-so` |
| 9 | `ConnectVHR*`, `sysConnectVHR.zul`, `ObjectTransferViaAxisDAO` | `tich-hop` | `van-ban/lien-thong` |
| 10 | `TextSyncController`, `textMarkSync*`, `ShareDocumentController`, `ShareBriefController`, `DocumentSignKNTCService`, `office/editor.zul`, `editHistory.zul`, `vps/integratedSys/*`, `Party*Controller`, `ElasticDocumentService` | `van-ban/*`, `he-thong`, `quan-ly-chung` | `tich-hop` |
| 11 | `VHROrgAction`, `config/appMobile/appMobile.zul`, `CategoryController`, (tùy chọn) `SSOConnector`/`VNeIDConnector` | `tich-hop`, `quan-ly-chung` | `he-thong` |
| 12 | `document_type/*.zul`, `vps/sysOrg/sysOrgMenu.zul` (thể loại văn bản theo đơn vị) | `he-thong` | `van-ban/quan-ly-chung` |
| 13 | `documentHandover/documentBook.zul` + `DocumentBookVM` (báo cáo sổ) | `van-ban/quan-ly-chung` | `van-ban/so-van-ban` |
| 14 | `DocumentProcessTermBusiness` | `van-ban/luong-xu-ly` | `van-ban/chuyen-van-ban` |
| 15 | `requisitionFlowDiagram.zul` + `FlowChartVM`, `select_mission_dialog.zul` + `DraftMissionLinkBusiness`, `DocumentFormalError*`, entity `RequisitionFile`, `DraftMetadataController` | nhiều nơi | `xu-ly-cong-viec` |
| 16 | `DocumentProposal*`, `DocumentCopyHistory`, `smsTask.checkDocumentToSendSms` | `quan-ly-chung`, `cong-viec` | `van-ban/den` |
| 17 | `meeting/popup/approveTaskReason.zul`, `rejectTaskReason.zul`, `VoTaskEmpRatingUtils`, `taskGanttChart.zul` | `hop`, `kpi-danh-gia` | `cong-viec` |
| 18 | widget biên bản họp (`editMeetingMinutesTarget.zul`, `popupViewMeetingMinutesInfo.zul`, `MeetingMinutesFacade`…), `ResovleIssue*`, `ChartAgreementVM` | `hop`, `he-thong`, `kpi-danh-gia` | `nhiem-vu` |
| 19 | `CallbackController` (`/callback/ext-brief`), `financialRecords/*`, `StoreTypeConfig*` | `tich-hop`, `he-thong` | `ho-so-cong-viec` |
| 20 | `InfoHastagDoc`, `popupInfoHastag.zul` (gán tag) | (không xếp) | `tai-lieu-mau` |

Ngoài ra bộ quét có lỗi nhỏ: gắn nhãn "☠ VM không tồn tại" cho lớp tên không kết thúc bằng `VM`
(`SourceLookupSubmission`, `DocumentHandoverVM` bản cũ…), và không nối được `ReminderController` → service.

**Câu hỏi:** (a) đồng ý cả danh sách — mình sửa `domains.py` (kể cả sửa regex `mission`/`brief` cho khớp nguyên từ),
chạy lại `scan.py` + `gen.py`, rồi cập nhật các mục "Module" liên quan; (b) chỉ làm các dòng … (ghi số); (c) để nguyên.

> **Trả lời:** 

### A2 · Tách phân hệ "Kiến nghị / khó khăn vướng mắc"

**Hiện trạng:** nhóm màn `request/*` (kiến nghị, đề xuất, khó khăn vướng mắc; cấu hình cá nhân nhận kiến nghị;
SMS nhóm 600 — đã xóa khỏi danh mục chặn tin) đang bị xếp vào Phiếu trình nhưng không liên quan phiếu trình, và
chưa phân hệ nào mô tả nghiệp vụ của nó.

**Câu hỏi:** (a) tách thành phân hệ riêng `kien-nghi` và viết tri thức như các phân hệ khác; (b) chức năng này không
còn dùng ở Khánh Hòa — chỉ ghi chú "không dùng"; (c) để sau.

> **Trả lời:** 

### A3 · Văn bản mật có đang dùng không?

**Hiện trạng:** trước đây đã xác nhận "nghiệp vụ văn bản mật chưa dùng". Nhưng DB DEV có ~52.900 bản ghi quyền đọc
file mã hóa (`FILE_ENCRYPT_MAP`, phát sinh tới 09/2026) và hơn 121.000 chứng thư mật cá nhân đang hiệu lực
(`P12_CERT`); code chỉ mã hóa file khi văn bản / phiếu trình có độ mật (`ky-so` NV-16, câu Q10).

**Câu hỏi:** (a) văn bản / phiếu trình mật **đang dùng thật** — mình sẽ sửa lại sự thật đã xác nhận ở mọi phân hệ;
(b) chỉ là dữ liệu thử trên DEV, thực tế chưa dùng; (c) cơ chế mã hóa đang dùng cho loại tài liệu khác (ghi rõ).

> **Trả lời:** 

### A4 · Dữ liệu và cấu hình kế thừa Viettel

**Hiện trạng:** rất nhiều chỗ trong code và tham số dùng mã đơn vị / quy tắc của Viettel cũ (148842, 148844, 151233,
"chi nhánh VTT", ban giám đốc tập đoàn, ERP_SAP, FICO, ViettelPay, vContract…), trên DB DEV Khánh Hòa không có các
đơn vị đó nên các nhánh này không bao giờ chạy (`hop` Q1, `kpi-danh-gia`, `tich-hop` Q10, `ky-so` NV-15).

**Câu hỏi:** khi viết tri thức, các nhánh / tích hợp kế thừa Viettel nên ghi là (a) "không áp dụng cho Khánh Hòa"
(gọn, không mô tả sâu); (b) giữ mô tả đầy đủ vì còn triển khai cho khách hàng khác trên cùng mã nguồn.

> **Trả lời:** 

### A5 · Các lỗ hổng bảo mật đã ghi nhận

**Hiện trạng:** đúng phạm vi "chỉ xây tri thức", các lỗi bảo mật chỉ được ghi ở `dac-thu.md` (danh sách tổng hợp
trong báo cáo [`bao-cao-dot-viet-lai-2026-10.md`](bao-cao-dot-viet-lai-2026-10.md) mục 5). Hai lỗi nghiêm trọng nhất: đăng nhập BE cấp token
không kiểm mật khẩu khi SSO trả lỗi; API `/api/app-mobile/*-data-map` chạy câu SQL do client gửi.

**Câu hỏi:** (a) chỉ cần ghi nhận như hiện nay; (b) mình lập thêm một file riêng (chưa có — sẽ tạo `_chung/attt-ghi-nhan.md`)
liệt kê đầy đủ để chuyển cho đội phụ trách; (c) mở CR/BUG theo quy trình repo cho từng lỗi (việc này ngoài phạm vi
tri thức, sẽ làm theo luồng `/bug`).

> **Trả lời:** 

---

## B. Câu hỏi theo phân hệ

