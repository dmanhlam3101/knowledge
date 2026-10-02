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

| Phân hệ | Thư mục | Số câu |
|---|---|---|
| Xử lý công việc (dự thảo → ký) | `xu-ly-cong-viec` | — (đã trả lời hết) |
| Văn bản đi | `van-ban/di` | — (đã trả lời hết) |
| Chuyển văn bản | `van-ban/chuyen-van-ban` | — (đã trả lời hết) |
| Văn bản đến | `van-ban/den` | — (đã trả lời hết) |
| Phiếu trình | `phieu-trinh` | 1 |
| Nhắc việc / thông báo / SMS / nắm tình hình / định hướng | `lich-nhac-viec` | 10 |
| Luồng xử lý (cấu hình luồng ký) | `van-ban/luong-xu-ly` | 8 |
| Sổ văn bản | `van-ban/so-van-ban` | 10 |
| Liên thông văn bản | `van-ban/lien-thong` | 10 |
| Quản lý chung văn bản | `van-ban/quan-ly-chung` | 9 |
| Nhiệm vụ | `nhiem-vu` | 10 |
| Công việc cá nhân | `cong-viec` | 10 |
| Hồ sơ công việc / lưu trữ | `ho-so-cong-viec` | 10 |
| Họp / lịch | `hop` | 10 |
| Ký số | `ky-so` | 10 |
| Hệ thống / quản trị | `he-thong` | 10 |
| KPI / đánh giá / báo cáo | `kpi-danh-gia` | 10 |
| Tích hợp | `tich-hop` | 10 |
| Tài liệu mẫu / thư viện | `tai-lieu-mau` | 8 |
| **Tổng** | | **136** |

Cộng thêm **5 quyết định chung** ở phần A → tổng cộng 136 câu theo phân hệ + 5 quyết định.

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


## Phiếu trình — `phieu-trinh` (1 câu)

Nguồn: [phieu-trinh/nghiep-vu.md](../phieu-trinh/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### phieu-trinh · Q7

**Hiện trạng:** Bảng phiếu trình trên DB có cột "loại" (`FORM_TYPE`, giá trị 1/2/3 ở khoảng 116 phiếu) nhưng code nhánh hiện tại không đọc / ghi cột này. Cột cùng tên ở văn bản nghĩa là "loại bản" (bản chính / bản gốc / bản sao / dự thảo).

**Câu hỏi:** Cột "loại" của phiếu trình nghĩa là gì (có phải loại bản như văn bản)? Có phải tính năng ở nhánh khác chưa vào `kha_develop`? — (2026-10-01: chủ dự án **chưa rõ** — cần hỏi người làm tính năng / BA; DB DEV: 116 phiếu có giá trị, tạo 2026-02-04 → 2026-04-16)

> **Trả lời:** 


## Nhắc việc / thông báo / SMS / nắm tình hình / định hướng — `lich-nhac-viec` (10 câu)

Nguồn: [lich-nhac-viec/nghiep-vu.md](../lich-nhac-viec/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### lich-nhac-viec · Q1

**Hiện trạng:** Khi giao nhắc việc, khi nhắc lại, khi trả lời hay khi duyệt, hệ thống **không gửi tin nhắn và không tạo thông báo** nào; riêng nút "Nhắc lại" lại báo "Đã gửi thông báo và SMS tới các đơn vị liên quan" nhưng thực tế chỉ ghi lại thời điểm (NV-02, NV-07 BR-22).

**Câu hỏi:** Nhắc việc có cần báo cho người nhận qua tin nhắn / thông báo không? (a) không cần, chỉ xem trên màn hình; (b) cần khi giao và khi nhắc lại; (c) cần ở mọi bước (giao, nhắc lại, trả lời, duyệt).

> **Trả lời:** 

### lich-nhac-viec · Q2

**Hiện trạng:** Ai được **duyệt / trả lại** trả lời: trên màn chi tiết là người giao **và mọi người theo dõi** (cả chuyên viên), nhưng hộp "Cần xử lý" và con số "Chờ duyệt" chỉ đưa trả lời tới **lãnh đạo theo dõi** (NV-05 BR-17, NV-01 BR-02).

**Câu hỏi:** Người duyệt trả lời nhắc việc là ai? (a) chỉ lãnh đạo theo dõi; (b) lãnh đạo theo dõi và người giao; (c) mọi người theo dõi và người giao.

> **Trả lời:** 

### lich-nhac-viec · Q3

**Hiện trạng:** Nhắc việc chỉ thực sự "giao" cho đơn vị khi văn bản được **chuyển** tới đơn vị đó; đơn vị có tên trong nhắc việc mà không được chuyển văn bản thì nhắc việc nằm "Lưu tạm" mãi (NV-03 BR-10).

**Câu hỏi:** Đó có phải ý đồ: nhắc việc chỉ giao cho đơn vị **đã nhận văn bản**? Nếu văn thư quên chuyển cho một đơn vị trong nhắc việc thì (a) chấp nhận nhắc việc không tới đơn vị đó; (b) cần cảnh báo / tự giao.

> **Trả lời:** 

### lich-nhac-viec · Q4

**Hiện trạng:** Khi ban hành dự thảo, nhắc việc soạn kèm bị đổi **đơn vị giao** thành đơn vị ban hành văn bản và **người ký** thành người ký văn bản (NV-03 BR-11).

**Câu hỏi:** Đơn vị giao của nhắc việc luôn phải là đơn vị ban hành văn bản? (a) đúng; (b) không — người soạn được chọn đơn vị giao khác.

> **Trả lời:** 

### lich-nhac-viec · Q5

**Hiện trạng:** Màn "Thông tin phục vụ lãnh đạo": ai có menu thì đều tạo được văn bản không chính thức và thấy văn bản mình tạo / được gửi; chỉ nút "Chuyển nắm tình hình" giới hạn cho lãnh đạo và trợ lý văn bản (NV-17 BR-41, NV-18). Menu là menu cấp 1 riêng.

**Câu hỏi:** Tính năng này dành cho ai? (a) chỉ lãnh đạo và trợ lý của lãnh đạo (phân bằng menu); (b) mọi cán bộ được cấp menu. Và "văn bản không chính thức" là gì trong thực tế (văn bản cấp trên chuyển qua kênh khác, thông tin nắm tình hình địa phương…)?

> **Trả lời:** 

### lich-nhac-viec · Q6

**Hiện trạng:** "Chuyển nắm tình hình" làm văn bản **rời khỏi hộp văn bản đến** của người đó (và lãnh đạo nếu trợ lý chọn "Chuyển cả lãnh đạo") nhưng **không đổi** vai trò xử lý chủ trì / phối hợp và không hoàn thành luồng (NV-18 BR-42).

**Câu hỏi:** Văn bản đã chuyển sang nắm tình hình có còn phải xử lý / hoàn thành như văn bản thường không? (a) không — chỉ để nắm thông tin; (b) vẫn phải xử lý ở nơi khác.

> **Trả lời:** 

### lich-nhac-viec · Q7

**Hiện trạng:** Một trả lời bị **trả lại** hoặc **hủy** đều quay về "Xử lý lại", xóa nội dung và văn bản trả lời; không lưu lịch sử các lần trả lời trước (NV-05 BR-18).

**Câu hỏi:** Có cần giữ lịch sử các lần trả lời / trả lại không? (a) không; (b) có.

> **Trả lời:** 

### lich-nhac-viec · Q8

**Hiện trạng:** Định hướng: menu "Định hướng" đang **khóa**, hai menu danh mục đã xóa; vẫn còn xem được định hướng qua nguồn gốc của nhiệm vụ; trên DB có 295 định hướng còn hiệu lực (NV-19). DB: định hướng cuối cùng tạo / sửa ngày **2021-05-10**.

**Câu hỏi:** Nghiệp vụ Định hướng còn dùng không? (a) đã ngừng, chỉ giữ để xem dữ liệu cũ; (b) tạm khóa, sẽ mở lại.

> **Trả lời:** 

### lich-nhac-viec · Q9

**Hiện trạng:** Chặn tin theo **đơn vị** chỉ do quản trị đơn vị **cấp 1** cấu hình và áp cho toàn bộ cây đơn vị đó; loại tin đơn vị đã chặn thì cá nhân không còn thấy để tự chọn (NV-15 BR-36).

**Câu hỏi:** Có cần chặn ở đơn vị cấp dưới (phòng, ban) không? (a) không, cấp 1 là đủ; (b) có.

> **Trả lời:** 

### lich-nhac-viec · Q10

**Hiện trạng:** Bảng mã loại tin trên DB có các mã không có trong code (109 "cảnh báo chưa ký duyệt", 404–406, 444 "cảnh báo quá hạn", 312–313, 322–325) và code có mã không có trên DB (108, 112 "hủy ban hành", 160 "chuyển xử lý phiếu trình") (mục 5.2).

**Câu hỏi:** Mã 109 và 108 có phải cùng một loại tin ("cảnh báo chưa ký / cảnh báo ban hành")? Mã 444 "cảnh báo quá hạn" dùng cho tin nào (văn bản, nhiệm vụ, phiếu trình…)?

> **Trả lời:** 


## Luồng xử lý (cấu hình luồng ký) — `van-ban/luong-xu-ly` (8 câu)

Nguồn: [van-ban/luong-xu-ly/nghiep-vu.md](../van-ban/luong-xu-ly/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### van-ban/luong-xu-ly · Q1

**Hiện trạng:** Mỗi luồng văn bản đến có thể gắn một "nhóm luồng". Hệ thống dùng nhóm như **bộ điều kiện theo độ mật / loại văn bản / độ khẩn** của văn bản đến: văn bản khớp nhóm nào thì đi luồng của nhóm đó, không khớp thì đi luồng không gán nhóm (NV-08). Trong khi đó ghi chú của cơ sở dữ liệu lại nói nhóm là "Văn bản Đảng / Văn bản Chính quyền", và cả 12 nhóm hiện có đều đánh dấu "Đảng"; hệ thống không dùng dấu "Đảng" này. Trên DB DEV, các nhóm mang tên như "Normal / Luồng bình thường", "Security / Luồng mật" và nhiều nhóm thử ("…Ngoan tạo Thông tư", "…Báo cáo"…), mỗi nhóm đều đặt cả độ mật, loại văn bản và độ khẩn; chỉ nhóm "Normal" đang được 6 luồng dùng (DB DEV `FLOW_GROUP_TYPE`, `FLOW` ngày 2026-10-01).

**Câu hỏi:** Nhóm luồng được hiểu là gì: (a) bộ điều kiện theo thuộc tính văn bản (như hệ thống đang làm); (b) phân loại văn bản Đảng / Chính quyền; (c) cả hai?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q2

**Hiện trạng:** "Đơn vị áp dụng" của luồng hiện **chỉ quyết định quản trị viên nào thấy và sửa được luồng**. Ai dùng được luồng là do người / đơn vị khai trong từng nút; một luồng của đơn vị A có thể khai người của đơn vị B và vẫn có hiệu lực với người đó (NV-01 BR-03).

**Câu hỏi:** "Đơn vị áp dụng" mang ý nghĩa: (a) đơn vị sở hữu / quản trị luồng (như hiện tại); (b) luồng chỉ được áp dụng cho văn bản của đơn vị đó?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q3

**Hiện trạng:** Văn bản đang chạy không giữ bản chụp luồng; mỗi lần chọn người kế, hệ thống đọc **cấu hình hiện tại**. Sửa sơ đồ có hiệu lực ngay với văn bản đang xử lý; xóa một nút mà văn bản đang đứng thì văn bản đó không còn gợi ý người kế theo luồng; khóa / xóa luồng không kiểm có văn bản đang dùng (NV-03 BR-08/09, NV-09 BR-29).

**Câu hỏi:** Cách làm này có đúng ý đồ không: (a) đúng — quản trị tự chịu trách nhiệm khi sửa luồng đang dùng; (b) văn bản đã vào luồng phải đi tiếp theo phiên bản luồng lúc bắt đầu?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q4

**Hiện trạng:** Khi một người trong chuỗi ký là **người được thêm ngoài luồng** (tối đa 5 lãnh đạo / thủ trưởng), bước kế sau người đó được tính theo vị trí của **người ký gốc gần nhất phía trước** — người thêm "đi ké", không làm đổi đường đi của luồng (NV-10, NV-11 BR-41).

**Câu hỏi:** Quy tắc "người ký thêm không làm đổi luồng" có đúng ý đồ không? Giới hạn 5 người và chỉ cho thêm vai trò lãnh đạo đơn vị / thủ trưởng có phải quy định nghiệp vụ?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q5

**Hiện trạng:** Chuyển **một** văn bản đến: hệ thống chọn luồng theo nhóm (độ mật / loại / độ khẩn). Chuyển **nhiều** văn bản cùng lúc: hệ thống chỉ dùng các luồng không gán nhóm (NV-08 BR-27). Cùng một văn bản có thể được gợi ý người nhận khác nhau tùy chuyển lẻ hay chuyển nhiều.

**Câu hỏi:** Khác biệt này là: (a) chủ ý (nhiều văn bản khác thuộc tính nên dùng luồng chung); (b) chuyển nhiều cũng phải theo nhóm của từng văn bản?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q6

**Hiện trạng:** Lịch sử thay đổi chỉ ghi phần **thông tin chung** của luồng (tên, mã, loại, nhóm, đơn vị, trạng thái). Phần ghi thay đổi nút / người theo nút / hành động đang bị tắt có chú thích "tạm thời bỏ qua", trong khi màn lịch sử vẫn có lựa chọn lọc "Thông tin node / Thông tin cấu hình" (NV-07 BR-22).

**Câu hỏi:** Lịch sử thay đổi luồng được thiết kế để theo dõi: (a) chỉ thông tin chung; (b) cả sơ đồ (nút, người theo nút, hành động)?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q7

**Hiện trạng:** Chức năng cũ "luồng trình ký mẫu" (lưu sẵn danh sách người ký theo cá nhân / đơn vị / tập đoàn để chọn lại khi trình) còn mã nhưng **không còn nút / menu nào mở được**, dữ liệu trên DB DEV trống (NV-14).

**Câu hỏi:** Chức năng luồng trình ký mẫu đã (a) bỏ hẳn, thay bằng cấu hình luồng; (b) còn kế hoạch dùng lại?

> **Trả lời:** 

### van-ban/luong-xu-ly · Q8

**Hiện trạng:** Nút kết thúc chỉ được hiểu là "kết thúc và chuyển ban hành" khi đánh dấu **Ban hành**; nút kết thúc không đánh dấu thì hệ thống không gợi ý bước kết thúc và không có đơn vị ban hành (NV-10 BR-33). Ô "Văn thư / Ban hành" bị ẩn với luồng văn bản đến. Trên DB DEV có 44 nút kết thúc: 25 đánh dấu Ban hành, **19 không đánh dấu**; ngoài ra 3 nút xử lý mang dấu Ban hành và 2 nút bắt đầu mang dấu Văn thư — hai trường hợp sau hệ thống gần như không dùng tới (DB DEV `NODE` ngày 2026-10-01).

**Câu hỏi:** Với luồng văn bản đi, nút kết thúc **không** đánh dấu Ban hành mang ý nghĩa nghiệp vụ gì (ví dụ: kết thúc không ban hành), hay mọi nút kết thúc đều phải là nút Ban hành?

> **Trả lời:** 


## Sổ văn bản — `van-ban/so-van-ban` (10 câu)

Nguồn: [van-ban/so-van-ban/nghiep-vu.md](../van-ban/so-van-ban/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### van-ban/so-van-ban · Q1

**Hiện trạng:** Trên form sổ, ô "Số thứ tự" (≥ 1) dùng để sắp xếp sổ trong danh sách. Nhưng cùng ô đó, khi hệ thống **tự chọn sổ** (tự động ban hành, gợi ý sổ khi cấp số) và khi kiểm sổ trùng, lại được hiểu là "**Sổ Đảng**": giá trị 1 = sổ Đảng, 0 = sổ thường; sổ có số thứ tự từ 2 trở lên không bao giờ được hệ thống tự chọn. Màn chi tiết sổ vẫn có ô tick "Sổ văn bản Đảng" (NV-02 BR-05, NV-08 BR-26). Dữ liệu DB DEV: 252 sổ = 0, **3 sổ = 1** (2 sổ đến mật, 1 sổ đi mật — đang bị hệ thống coi là sổ Đảng), **1 sổ = 2** (không bao giờ được tự chọn).

**Câu hỏi:** Hiện còn phân biệt **sổ Đảng** với sổ thường không? (a) không — ô chỉ là số thứ tự, việc tự chọn sổ không cần xét Đảng; (b) có — cần một ô "Sổ Đảng" riêng, tách khỏi số thứ tự.

> **Trả lời:** 

### van-ban/so-van-ban · Q2

**Hiện trạng:** Không có bước "đánh số lại đầu năm". Sổ 1 năm của năm cũ vẫn hiện để văn thư chọn khi cấp số / vào sổ (nếu chưa khóa) và tiếp tục số cũ; còn khi hệ thống tự chọn sổ thì chỉ lấy sổ đúng năm nay (NV-06 BR-21a). Dữ liệu DB DEV: mọi sổ chưa xóa đều là năm 2026 — chưa thấy cách xử lý sổ năm cũ trên dữ liệu.

**Câu hỏi:** Đầu năm mới, số đi / số đến phải bắt đầu lại từ 1 theo cách nào? (a) văn thư tự tạo sổ năm mới và tự khóa sổ năm cũ; (b) hệ thống tự ẩn sổ năm cũ khỏi danh sách chọn; (c) văn thư vẫn được dùng sổ năm cũ trong một thời gian (ví dụ văn bản đến muộn).

> **Trả lời:** 

### van-ban/so-van-ban · Q3

**Hiện trạng:** Khi một đơn vị **chưa có sổ nào** hiệu lực năm nay, hệ thống tự tạo 4 sổ: đi thường, đi mật (đánh số theo thể loại, "ban hành tự động"), đến thường, đến mật. Nếu đơn vị đã tự tạo dù chỉ **một** sổ (ví dụ một sổ đến), bộ 4 sổ không được tạo, các loại còn thiếu cũng không được bổ sung (NV-06 BR-21b). Dữ liệu DB DEV: khoảng 61–63 đơn vị có bộ sổ tự sinh, chỉ 4 sổ tạo tay; có 3 nhóm / 7 sổ trùng cùng loại, năm, độ mật trong một đơn vị.

**Câu hỏi:** (1) Bộ 4 sổ trên có đúng là bộ sổ chuẩn của mọi đơn vị (kể cả phòng, ban)? (2) Đơn vị đã có một vài sổ thì: (a) chấp nhận không sinh thêm; (b) cần sinh bù đúng loại còn thiếu.

> **Trả lời:** 

### van-ban/so-van-ban · Q4

**Hiện trạng:** Sổ có thể được khai "dùng chung" cho đơn vị khác; khi hệ thống tự chọn sổ cho đơn vị nhận, **sổ dùng chung được ưu tiên trước sổ riêng** của đơn vị đó (NV-04 BR-17). Trên DB DEV chưa có sổ dùng chung nào.

**Câu hỏi:** Sổ dùng chung dùng trong trường hợp nào (ví dụ phòng ban dùng chung sổ của cơ quan)? Khi đơn vị vừa có sổ riêng vừa được dùng chung sổ cấp trên thì ưu tiên: (a) sổ dùng chung; (b) sổ riêng.

> **Trả lời:** 

### van-ban/so-van-ban · Q5

**Hiện trạng:** Sổ "5 năm" chỉ được văn thư chọn tay; hệ thống tự chọn sổ (tự động ban hành, gợi ý sổ) không bao giờ lấy sổ 5 năm. Form không kiểm khoảng đúng 5 năm. DB DEV: sổ 5 năm duy nhất đã bị xóa — hiện **không có** sổ 5 năm nào đang dùng (NV-08 BR-26).

**Câu hỏi:** Sổ 5 năm dùng cho loại văn bản nào? Có cần hệ thống tự chọn sổ 5 năm như sổ 1 năm không: (a) không; (b) có.

> **Trả lời:** 

### van-ban/so-van-ban · Q6

**Hiện trạng:** Có chức năng phía máy chủ để "giữ số" (số chờ, kèm tiêu đề) trong một sổ, nhưng màn hình không có chỗ thao tác và khi cấp số hệ thống **không** tránh các số đang giữ (NV-09 BR-28). DB DEV: 8 số chờ còn hiệu lực, tạo gần nhất 2025-04-08 (thử đầu 2025, sau đó không dùng).

**Câu hỏi:** Nghiệp vụ giữ số trước còn cần không? (a) bỏ; (b) cần — giữ số cho trường hợp nào (văn bản ký tay ngoài hệ thống, văn bản sẽ ban hành sau…), và khi cấp số có phải tự bỏ qua số đang giữ không?

> **Trả lời:** 

### van-ban/so-van-ban · Q7

**Hiện trạng:** Sổ chỉ bị chặn xóa khi đã có văn bản đi (hoặc văn bản đến do văn thư tự nhập) mang sổ đó; sổ đến chỉ dùng để **tiếp nhận** văn bản từ đơn vị khác vẫn xóa được (NV-03 BR-14).

**Câu hỏi:** Sổ đến đã có văn bản tiếp nhận vào sổ có được phép xóa không? (a) không — phải khóa; (b) có.

> **Trả lời:** 

### van-ban/so-van-ban · Q8

**Hiện trạng:** Hai menu "Báo cáo văn bản" và "Báo cáo văn bản đi đến" (đều dưới VĂN BẢN ĐẾN) mở cùng một màn. Màn chỉ có báo cáo văn bản **đến** (mục lục, sổ đăng ký, sổ chuyển, báo cáo ngày, xử lý văn bản đến, tổng hợp, tỉ lệ đọc, lịch họp); sổ văn bản **đi** nằm ở màn "Báo cáo văn bản đi". "Mục lục công văn đến" và "Sổ chuyển công văn đến" gộp văn bản của **mọi đơn vị người xuất làm văn thư**, còn "Sổ đăng ký / Sổ chuyển văn bản đến" chỉ lấy **đơn vị đã chọn** (NV-11).

**Câu hỏi:** (1) Hai menu có phải một menu thừa không: (a) giữ cả hai; (b) bỏ một. (2) Khi văn thư của nhiều đơn vị xuất báo cáo cho một đơn vị đã chọn, báo cáo phải chứa: (a) chỉ đơn vị đã chọn; (b) mọi đơn vị mình làm văn thư.

> **Trả lời:** 

### van-ban/so-van-ban · Q9

**Hiện trạng:** Menu "Sổ văn bản đơn vị" mở một danh sách (giao diện giống "Công khai văn bản") nhưng không lấy dữ liệu nên **luôn rỗng** (NV-12).

**Câu hỏi:** Menu này dùng để làm gì? (a) bỏ menu; (b) cần — xem danh sách văn bản đã vào các sổ của đơn vị (giống sổ đăng ký trên màn hình).

> **Trả lời:** 

### van-ban/so-van-ban · Q10

**Hiện trạng:** Ô "Loại cơ quan gửi" (Trung ương / Địa phương) của sổ chỉ được dùng trong "Báo cáo ngày – VP TWĐ" để đếm văn bản đến theo nguồn; loại báo cáo này không còn trên danh sách chọn của màn Báo cáo văn bản (NV-11 BR-34). DB DEV: chỉ 4 sổ có giá trị "Địa phương" hoặc rỗng; cấu hình báo cáo ngày vẫn khai 3 nhóm (Trung ương 2025, tỉnh ủy / thành ủy, công văn đến VPTW) và đơn vị 3189 (NV-11 BR-34a).

**Câu hỏi:** Báo cáo ngày VP TWĐ (và phân loại sổ theo Trung ương / Địa phương) còn dùng không? (a) đã bỏ; (b) còn — cần đưa lại vào danh sách báo cáo.

> **Trả lời:** 


## Liên thông văn bản — `van-ban/lien-thong` (10 câu)

Nguồn: [van-ban/lien-thong/nghiep-vu.md](../van-ban/lien-thong/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### van-ban/lien-thong · Q1

**Hiện trạng:** Hệ thống chỉ ghi văn bản cần gửi vào bảng chờ; việc đưa lên trục và nhận văn bản về do một chương trình khác làm. Đơn vị gửi phải có mã định danh nằm trong "Danh mục đơn vị liên thông" (NV-01, NV-03). Danh mục trên DEV có hơn 123 nghìn cơ quan, lần đồng bộ gần nhất 28/07/2026 — tức được đồng bộ tự động (NV-02).

**Câu hỏi:** Trục liên thông đang kết nối thật là trục nào? (a) trục văn bản quốc gia (VPCP); (b) trục LGSP tỉnh Khánh Hòa; (c) cả hai. Danh mục đơn vị liên thông lấy từ trục đó hay do quản trị nhập tay?

> **Trả lời:** 

### van-ban/lien-thong · Q2

**Hiện trạng:** Kênh "liên thông nội bộ" trao đổi văn bản với đơn vị thuộc **hệ thống khác** cùng nền tảng (mã hệ thống mặc định "VPTWD"; trên DEV mọi đơn vị trong cây tổ chức mang mã này hoặc để trống, chưa có đơn vị nào của hệ thống khác). Bên nhận chỉ nhận văn bản mới, trạng thái và lệnh thu hồi; việc bên gửi **sửa / xóa / khóa / thêm ý kiến chỉ đạo** sau đó không được áp vào bản bên nhận (NV-08, NV-09 BR-28).

**Câu hỏi:** Hệ thống bên kia là hệ thống nào (cấp nào)? Khi bên gửi sửa hoặc xóa văn bản, bên nhận có cần thấy thay đổi không? (a) không cần; (b) cần cập nhật / xóa theo.

> **Trả lời:** 

### van-ban/lien-thong · Q3

**Hiện trạng:** Văn thư hoàn thành văn bản đến tạo từ văn bản liên thông thì **không** tự báo "Đã hoàn thành" cho cơ quan gửi; phải vào màn "Văn bản liên thông" bấm Hoàn thành (NV-06 BR-18).

**Câu hỏi:** Việc báo hoàn thành cho cơ quan gửi là (a) văn thư tự bấm ở màn liên thông khi thấy cần; (b) phải tự động khi văn bản đến được hoàn thành?

> **Trả lời:** 

### van-ban/lien-thong · Q4

**Hiện trạng:** Khi cơ quan ngoài gửi văn bản **cập nhật / thu hồi / thay thế** một văn bản đã gửi trước, hệ thống chỉ hiện nhãn ở cột "Trạng thái VB"; văn bản đến đã vào sổ không bị thu hồi / thay (NV-06 BR-20).

**Câu hỏi:** Khi nhận lệnh thu hồi / thay thế từ cơ quan ngoài: (a) văn thư tự xử lý thủ công; (b) hệ thống phải tự thu hồi / thay văn bản đến đã vào sổ.

> **Trả lời:** 

### van-ban/lien-thong · Q5

**Hiện trạng:** Văn thư đơn vị gốc có nút "Chuyển tiếp nội bộ" văn bản liên thông cho đơn vị khác; bản chuyển hiện ở màn liên thông của đơn vị nhận nhưng **không vào hộp Chờ tiếp nhận**, và việc tiếp nhận / trả lại bản chuyển không được báo về trục (NV-07 BR-22). Trên DEV: 828 bản về thẳng đơn vị nhận (577 đã vào sổ), chỉ 5 bản qua chuyển tiếp nội bộ và chưa bản nào được tiếp nhận.

**Câu hỏi:** Mô hình thực tế ở Khánh Hòa là (a) văn bản liên thông về thẳng đơn vị nhận (không cần đầu mối phân phối); (b) về một đầu mối (văn phòng) rồi phân phối cho đơn vị. Nếu (b), đơn vị nhận bản phân phối có cần báo trạng thái lên trục không?

> **Trả lời:** 

### van-ban/lien-thong · Q6

**Hiện trạng:** Đơn vị liên thông có mã chứa "W00" bị ẩn khi văn thư chọn nơi nhận, chỉ hiện trong màn quản trị danh mục (NV-02 BR-05). Trên DEV có 174 / 123.265 cơ quan mang mã này.

**Câu hỏi:** "W00" là loại đơn vị gì? (a) mã giữ chỗ / đơn vị ảo không nhận văn bản; (b) nhóm đơn vị khác.

> **Trả lời:** 

### van-ban/lien-thong · Q7

**Hiện trạng:** Có cấu hình một số nhánh đơn vị nội bộ nhận **hai bản**: bản nội bộ và bản qua trục; còn đơn vị liên thông nào trùng mã với đơn vị trong hệ thống thì được chuyển nội bộ thay vì qua trục (NV-03 BR-06, BR-07). Trên DEV cấu hình hai nhánh gốc: đơn vị id 3126999 và 3565421.

**Câu hỏi:** Các đơn vị nhận hai bản là đơn vị nào và vì sao (a) đơn vị đang dùng song song một hệ thống khác; (b) yêu cầu lưu vết trên trục; (c) lý do khác?

> **Trả lời:** 

### van-ban/lien-thong · Q8

**Hiện trạng:** "Migrate văn bản": menu hiện tại mở màn trống; màn tra cứu văn bản cũ có sẵn nhưng **không có menu** (đã tra DB); ai mở được thì thấy **toàn bộ** 306 văn bản cũ (NV-12).

**Câu hỏi:** Văn bản migrate còn cần tra cứu không? Nếu cần: (a) mọi người dùng xem tất cả; (b) chỉ văn thư / đơn vị liên quan xem văn bản của mình.

> **Trả lời:** 

### van-ban/lien-thong · Q9

**Hiện trạng:** Menu "Văn bản từ VPCP" vẫn mở nhưng toàn bộ chức năng đã bị gỡ trong code (NV-11).

**Câu hỏi:** Chức năng này (a) đã ngừng hẳn — có thể khóa menu; (b) sẽ làm lại theo trục mới?

> **Trả lời:** 

### van-ban/lien-thong · Q10

**Hiện trạng:** Khi hệ thống khác thu hồi văn bản đã gửi cho đơn vị ở hệ thống này, chỉ bản của **đơn vị** chuyển sang "đã thu hồi"; các bản đơn vị đã chuyển tiếp cho cán bộ vẫn còn (NV-09 BR-29).

**Câu hỏi:** Thu hồi từ hệ thống khác có cần thu hồi luôn các bản đã chuyển tiếp trong đơn vị nhận không? (a) có; (b) không.

> **Trả lời:** 


## Quản lý chung văn bản — `van-ban/quan-ly-chung` (9 câu)

Nguồn: [van-ban/quan-ly-chung/nghiep-vu.md](../van-ban/quan-ly-chung/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### van-ban/quan-ly-chung · Q1

**Hiện trạng:** Văn bản đã công khai **một lần** thì bất kỳ cán bộ nào cũng mở xem được (kể cả khi đã hủy công khai); "phạm vi công khai" chỉ giới hạn danh sách tìm kiếm, không giới hạn người xem (NV-06 BR-13, NV-11). Trên DB DEV kiểm quyền xem đang bật (`VALIDATE_ATTT = 1`) và chưa có văn bản nào đã hủy công khai.

**Câu hỏi:** Công khai văn bản nghĩa là: (a) toàn hệ thống được xem, phạm vi chỉ để biết đơn vị nào cần đọc; (b) chỉ đơn vị trong phạm vi được xem. Khi hủy công khai thì người ngoài luồng nhận (a) vẫn xem được; (b) không còn xem được?

> **Trả lời:** 

### van-ban/quan-ly-chung · Q2

**Hiện trạng:** Tra cứu văn bản hàng năm, mục "Văn bản đi", đang liệt kê văn bản đi mà **mình / đơn vị mình nhận được**, không phải văn bản đi đơn vị mình ban hành; năm chọn chỉ có 2020–2025 (NV-05 BR-11).

**Câu hỏi:** Mục "Văn bản đi" của Tra cứu văn bản hàng năm cần hiện: (a) văn bản đơn vị mình ban hành; (b) văn bản đi mình nhận được; (c) cả hai?

> **Trả lời:** 

### van-ban/quan-ly-chung · Q3

**Hiện trạng:** Màn Theo dõi văn bản đơn vị dùng **một** cấu hình "theo dõi văn bản đi đơn vị" để chọn đơn vị cho cả tab văn bản đi lẫn văn bản đến, trong khi hệ thống có sẵn cấu hình riêng "theo dõi văn bản đến đơn vị" (NV-03 BR-07). DB DEV: cấu hình "theo dõi văn bản đến" đã có 307 dòng hiệu lực (gần bằng 277 dòng "theo dõi văn bản đi"), nhưng màn này không dùng.

**Câu hỏi:** Một người có thể theo dõi văn bản đi của đơn vị A nhưng văn bản đến của đơn vị B không? (a) không — một cấu hình chung là đủ; (b) có — tách riêng.

> **Trả lời:** 

### van-ban/quan-ly-chung · Q4

**Hiện trạng:** Phạm vi có hai loại "Toàn bộ" và "Liền kề"; màn danh mục chỉ cho tạo "Toàn bộ", còn mọi phạm vi hiện có trên DB là "Liền kề"; hệ thống không xử lý khác nhau giữa hai loại (NV-10 BR-24).

**Câu hỏi:** "Toàn bộ" và "Liền kề" khác nhau thế nào trong nghiệp vụ (ví dụ: liền kề = chỉ đơn vị được chọn, toàn bộ = cả đơn vị con)? Có còn cần hai loại không?

> **Trả lời:** 

### van-ban/quan-ly-chung · Q5

**Hiện trạng:** Danh mục thể loại có hai thuộc tính "văn bản pháp luật" (`IS_LAW`) và `IS_PROCESS` với giá trị 0 / 1 / 2 trên DB nhưng màn hình và chức năng không dùng tới (NV-12).

**Câu hỏi:** Hai thuộc tính này dùng để làm gì (ví dụ: lọc văn bản quy phạm pháp luật, văn bản cần xử lý)? Giá trị 2 nghĩa là gì?

> **Trả lời:** 

### van-ban/quan-ly-chung · Q6

**Hiện trạng:** Bàn giao "văn bản nhận được" chỉ lấy văn bản ở các trạng thái của dữ liệu cũ, nên văn bản đang chờ xử lý / đã hoàn thành theo luồng hiện tại **không xuất hiện** (NV-08 BR-20). DB DEV: không có dòng nhận nào ở trạng thái cũ, nên tìm "văn bản nhận được" luôn rỗng; bảng lịch sử bàn giao chưa có dòng nào.

**Câu hỏi:** Khi cán bộ bàn giao, cần bàn giao những văn bản nhận được nào? (a) chỉ văn bản chưa xử lý xong; (b) tất cả văn bản đã nhận (cả đã hoàn thành) để người mới tra cứu.

> **Trả lời:** 

### van-ban/quan-ly-chung · Q7

**Hiện trạng:** Ghi chú trên văn bản: mọi cán bộ có văn bản trong cùng **đơn vị cấp 2** đều đọc được ghi chú của nhau (NV-15 BR-38).

**Câu hỏi:** Ghi chú trên văn bản dành cho ai đọc? (a) chỉ người viết; (b) cùng phòng / đơn vị trực tiếp; (c) toàn đơn vị cấp 2 như hiện nay.

> **Trả lời:** 

### van-ban/quan-ly-chung · Q8

**Hiện trạng:** Menu "Xem luân chuyển văn bản đơn vị" (`VBDV`) đang mở nhưng màn không hiện văn bản (NV-17); menu "Tìm kiếm văn bản" chỉ hiện trang đầu kết quả (NV-02 BR-04).

**Câu hỏi:** Hai chức năng này còn dùng không? (a) ẩn menu; (b) còn cần — mô tả ngắn người dùng mong thấy gì.

> **Trả lời:** 

### van-ban/quan-ly-chung · Q9

**Hiện trạng:** Khi đơn vị tạo thể loại trùng tên với thể loại của đơn vị khác, hệ thống đề nghị **biến thể loại của đơn vị kia thành dùng chung toàn hệ thống** hoặc xin dùng chung thể loại đó (NV-12 BR-30).

**Câu hỏi:** Hướng mong muốn khi trùng: (a) xin cấp thể loại của đơn vị kia; (b) chuyển thành dùng chung toàn hệ thống; (c) cả hai như hiện nay.

> **Trả lời:** 


## Nhiệm vụ — `nhiem-vu` (10 câu)

Nguồn: [nhiem-vu/nghiep-vu.md](../nhiem-vu/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### nhiem-vu · Q1

**Hiện trạng:** Khi **lãnh đạo đơn vị thực hiện** tự báo cáo "hoàn thành / đề xuất đóng / đề xuất gia hạn", trạng thái nhiệm vụ đổi **ngay** sang trạng thái đó trước khi đơn vị giao duyệt; khi trợ lý báo cáo thì phải chờ lãnh đạo đơn vị thực hiện duyệt (NV-03 BR-11).

**Câu hỏi:** Trạng thái nhiệm vụ nên đổi khi nào? (a) ngay khi đơn vị thực hiện (lãnh đạo) báo cáo — như hiện nay; (b) chỉ khi đơn vị giao duyệt.

> **Trả lời:** 

### nhiem-vu · Q2

**Hiện trạng:** Có hai màn duyệt cùng việc: duyệt ngay trên danh sách / chi tiết nhiệm vụ, và màn "Nhiệm vụ chờ phê duyệt". Menu "Phê duyệt của chỉ huy" (đang khóa) và "Nhiệm vụ chờ phê duyệt" mở **cùng một màn** (NV-04).

**Câu hỏi:** "Phê duyệt của chỉ huy" có phải là tên cũ của "Nhiệm vụ chờ phê duyệt" (có thể bỏ)? Hay cần một danh sách riêng cho cấp chỉ huy cao hơn (ví dụ Ban Giám đốc)?

> **Trả lời:** 

### nhiem-vu · Q3

**Hiện trạng:** Từ chối báo cáo ở cấp đơn vị giao luôn đưa nhiệm vụ về "Đang thực hiện" (NV-04 BR-17); đóng nhiệm vụ không cần nhiệm vụ con xong, nhưng xóa thì phải (NV-06 BR-22).

**Câu hỏi:** (a) Đóng nhiệm vụ cha khi còn nhiệm vụ con đang làm có được phép không? (b) Nếu được, nhiệm vụ con có tự đóng theo không?

> **Trả lời:** 

### nhiem-vu · Q4

**Hiện trạng:** Chuyển đơn vị thực hiện: nhiệm vụ đi theo đơn vị mới, đơn vị cũ chỉ còn một bản lưu để xem; đề xuất đóng / gia hạn đang chờ bị coi như từ chối (NV-07 BR-23, BR-24).

**Câu hỏi:** Đơn vị cũ sau khi chuyển có còn trách nhiệm gì (báo cáo phần đã làm, phối hợp) không? (a) không, chỉ xem lịch sử; (b) có.

> **Trả lời:** 

### nhiem-vu · Q5

**Hiện trạng:** Số lần gia hạn tối đa và số ngày sau hạn còn được xin gia hạn là tham số hệ thống (hiện trên DB DEV: tối đa 2 lần; xin được tới 30 ngày sau hạn, riêng nhiệm vụ từ văn bản Quốc phòng / Chính phủ 7 ngày); "số lần gia hạn" có hai con số: số lần xin và số lần được duyệt (NV-05).

**Câu hỏi:** Giới hạn gia hạn tính theo (a) số lần được duyệt; (b) số lần đã xin (kể cả bị từ chối)? Báo cáo "đã gia hạn mấy lần" dùng con số nào?

> **Trả lời:** 

### nhiem-vu · Q6

**Hiện trạng:** Tab "Nhiệm vụ cá nhân" trên trang chủ đếm **công việc cá nhân**, nhưng bấm vào lại mở danh sách **nhiệm vụ giao cho cá nhân chủ trì** (mục 1.3). — (sửa chéo 2026-10-02 theo `cong-viec`): BE `getCountHomeTask` thực chất đếm bảng `MISSION` (`TaskDAO.java:3631` `select count(t.mission_id) from mission t`), nên số đếm **khớp** danh sách mở ra; câu hỏi giữ để xác nhận ý đồ hiển thị.

**Câu hỏi:** Ô "Nhiệm vụ cá nhân" trên trang chủ phải hiển thị gì? (a) công việc cá nhân (phân hệ công việc); (b) nhiệm vụ giao cho cá nhân chủ trì; (c) cả hai.

> **Trả lời:** 

### nhiem-vu · Q7

**Hiện trạng:** Nhiệm vụ đánh dấu không công khai (bí mật) vẫn hiện tên trong danh sách của người cùng phạm vi, chỉ khóa thao tác (NV-01 BR-02).

**Câu hỏi:** Nhiệm vụ bí mật có được hiện tên với người không liên quan trong đơn vị không? (a) có (như hiện nay); (b) phải ẩn hẳn.

> **Trả lời:** 

### nhiem-vu · Q8

**Hiện trạng:** Có những cột nhiệm vụ (tự đăng ký, trạng thái đăng ký, loại nhiệm vụ) không có trong mã nguồn nhưng vẫn được ghi dữ liệu tới 29/09/2026 (NV-20). Có ba kênh cho hệ thống ngoài lấy danh sách nhiệm vụ (`getListVTSMissions` theo ứng dụng, `vofficeMissions` cho TTHT, `sync-mission` không giới hạn đơn vị), và một "dịch vụ Mission" riêng mà web gọi cho dashboard chọn nhiệm vụ khi soạn dự thảo / chuyển văn bản (NV-13).

**Câu hỏi:** Các kênh này phục vụ hệ thống nào (VTS, cổng TTHT, kho dữ liệu, mobile…)? "Dịch vụ Mission" riêng có phải là hệ thống nhiệm vụ mới sẽ thay phần nhiệm vụ trong Văn phòng số không — và có phải nó ghi các cột "tự đăng ký / trạng thái đăng ký" không?

> **Trả lời:** 

### nhiem-vu · Q9

**Hiện trạng:** Menu "Phản ánh từ hệ thống NQ57" (đang khóa) trỏ tới một trang `mission_reflection_nq57.zul` **không có trong mã nguồn**; không có xử lý nào liên quan (NV-20).

**Câu hỏi:** Đây là (a) liên kết sang hệ thống ngoài; (b) tính năng chưa làm; (c) đã bỏ?

> **Trả lời:** 

### nhiem-vu · Q10

**Hiện trạng:** Biên bản họp có hai cách giao nhiệm vụ: giao tay sau khi nhập biên bản (hiệu lực ngay), hoặc soạn danh sách nhiệm vụ trong kết luận rồi trình ký (chỉ hiệu lực khi kết luận được ban hành); trạng thái "Chưa / Đang / Đã thực hiện / Đóng kết luận" của biên bản không bao giờ đổi (NV-10).

**Câu hỏi:** Trạng thái biên bản có cần theo tiến độ các nhiệm vụ sinh ra từ nó không? (a) không cần, chỉ theo trạng thái văn bản kết luận; (b) cần.

> **Trả lời:** 


## Công việc cá nhân — `cong-viec` (10 câu)

Nguồn: [cong-viec/nghiep-vu.md](../cong-viec/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### cong-viec · Q1

**Hiện trạng:** Phiếu giao việc và phiếu đánh giá hiện lập theo **quý hoặc cả năm**; nhưng tên tin nhắn, mẫu tin và một số nhãn vẫn ghi "đầu tháng / cuối tháng", và KI cá nhân lại xếp **hằng tháng** dựa trên điểm phiếu đánh giá (NV-06, NV-07, NV-09 BR-28). Dữ liệu DEV: phiếu từ 2021 đều theo quý, trước đó có kỳ dạng tháng, không có kỳ cả năm; KI cá nhân chỉ có đến 07/2018.

**Câu hỏi:** Kỳ giao việc / đánh giá công việc cá nhân đúng là (a) theo quý (và cả năm); (b) theo tháng; (c) khác? KI cá nhân xếp theo tháng hay theo cùng kỳ với phiếu đánh giá?

> **Trả lời:** 

### cong-viec · Q2

**Hiện trạng:** Có **hai cách** có phiếu giao việc: cán bộ tự chọn việc, tỷ trọng rồi **trình ký như văn bản**; hoặc lãnh đạo mở danh sách cán bộ, duyệt / từ chối từng việc và **ký phiếu trực tiếp** (NV-06 A, B).

**Câu hỏi:** Cả hai cách đều được dùng? Nếu chỉ một cách là chính thức thì (a) cán bộ tự trình; (b) lãnh đạo ký trực tiếp.

> **Trả lời:** 

### cong-viec · Q3

**Hiện trạng:** Công việc **cá nhân tự đề xuất** và công việc **phối hợp** vẫn tạo được (menu thêm mới đang khóa, nhưng form vẫn có chế độ), nhưng **không hiện ở tab nào** của danh sách (NV-01).

**Câu hỏi:** Hai loại này còn dùng không? (a) không — bỏ; (b) có — cần hiện ở danh sách (tab riêng).

> **Trả lời:** 

### cong-viec · Q4

**Hiện trạng:** Cấu hình "ngày chốt / ngày quá hạn chốt" đăng ký và đánh giá **không chặn** thao tác nào trên web; trên DEV chỉ có cấu hình đăng ký (ngày 1 → 31), thiếu cấu hình đánh giá nên màn đánh giá không có dữ liệu (NV-11, NV-07 BR-26).

**Câu hỏi:** Hệ thống có cần giới hạn ngày được đăng ký / đánh giá trong tháng (hoặc kỳ) không? (a) không cần, chỉ giới hạn theo kỳ; (b) cần chặn ngoài khoảng ngày cấu hình.

> **Trả lời:** 

### cong-viec · Q5

**Hiện trạng:** Màn **Đánh giá nhân viên (KI)** lấy danh sách cán bộ từ hệ thống nhân sự; đoạn kết nối đó đang tắt nên danh sách luôn rỗng; trang giám đốc ký KI toàn đơn vị không còn đường vào (NV-09). Dữ liệu DEV: chỉ 35 bản KI cá nhân, mới nhất tháng 07/2018; KI đơn vị đến tháng 01/2022.

**Câu hỏi:** Chức năng KI cá nhân còn dùng trên hệ thống này không? (a) không — KI làm ở hệ thống nhân sự; (b) có — cần lấy danh sách cán bộ (từ đâu: hệ thống nhân sự hay danh sách người dùng của đơn vị?).

> **Trả lời:** 

### cong-viec · Q6

**Hiện trạng:** Màn "Quản lý cấu hình đánh giá công việc" cho chọn một đơn vị rồi tick nhiều đơn vị khác và lưu, nhưng **không chức năng nào dùng** cấu hình này (NV-12).

**Câu hỏi:** Cấu hình này mang ý nghĩa gì: (a) đơn vị A được đánh giá / giao việc cho cán bộ của các đơn vị B; (b) đơn vị A xem thống kê của các đơn vị B; (c) không còn dùng?

> **Trả lời:** 

### cong-viec · Q7

**Hiện trạng:** "Cảnh báo công việc" (người thực hiện gửi cảnh báo cho người giao, có thể leo thang lên cấp trên) đã ẩn nút ở mọi màn và bảng dữ liệu không có trên DEV (NV-13).

**Câu hỏi:** Tính năng này đã ngừng hẳn? (a) đã ngừng; (b) cần khôi phục.

> **Trả lời:** 

### cong-viec · Q8

**Hiện trạng:** Ở màn Phiếu đánh giá, người có vai trò **tổ chức lao động (TCLD)** được nhận ra nhưng không có trang nào hiện (trắng); ở màn KI thì TCLD được coi như lãnh đạo, tính cho toàn đơn vị (NV-07, NV-09).

**Câu hỏi:** Tổ chức lao động cần làm gì với phiếu đánh giá công việc: (a) không tham gia; (b) xem / tổng hợp phiếu của toàn đơn vị; (c) chấm thay lãnh đạo?

> **Trả lời:** 

### cong-viec · Q9

**Hiện trạng:** Cán bộ có thể **lưu lại điểm tự chấm sau khi lãnh đạo đã chấm** (trước khi ký), và khi đó điểm, nhận xét của lãnh đạo bị xóa (NV-07; `dac-thu.md` L17).

**Câu hỏi:** Sau khi lãnh đạo đã chấm, cán bộ còn được sửa điểm tự chấm không? (a) không; (b) được, và lãnh đạo phải chấm lại.

> **Trả lời:** 

### cong-viec · Q10

**Hiện trạng:** Trên DEV, bảng công việc **không có dữ liệu**; dữ liệu phiếu giao / tiến độ dừng ở 12/2024 – 5/2025, phiếu mới nhất của quý 3/2024; không có văn bản phiếu nào và 365 ngày qua không có tin nhắn công việc (ghi chú đầu file).

**Câu hỏi:** Phân hệ công việc cá nhân còn được sử dụng ở Khánh Hòa không? (a) đang dùng (dữ liệu ở môi trường thật); (b) đã ngừng, chỉ giữ để tra cứu; (c) sẽ triển khai lại.

> **Trả lời:** 


## Hồ sơ công việc / lưu trữ — `ho-so-cong-viec` (10 câu)

Nguồn: [ho-so-cong-viec/nghiep-vu.md](../ho-so-cong-viec/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### ho-so-cong-viec · Q1

**Hiện trạng:** Ô "Chế độ sử dụng" trên màn hình hiển thị giá trị 1 = "Sử dụng có điều kiện", 2 = "Công khai", 3 = "Mật"; còn ghi chú trong cơ sở dữ liệu lại ghi 1 = "Công khai", 2 = "Sử dụng có điều kiện". Nút "Mượn" chỉ hiện với hồ sơ giá trị 1, và người khác được xem văn bản trong hồ sơ giá trị 2 mà không cần mượn (NV-01, NV-05).

**Câu hỏi:** Nghĩa đúng là bên nào? (a) như màn hình: 1 = sử dụng có điều kiện (phải mượn), 2 = công khai; (b) như ghi chú DB: 1 = công khai.

> **Trả lời:** 

### ho-so-cong-viec · Q2

**Hiện trạng:** Khi người nhận **tiếp nhận** hồ sơ bàn giao, hồ sơ chuyển hẳn sang họ: người bàn giao không còn thấy hồ sơ trong danh sách của mình (NV-12 BR-32).

**Câu hỏi:** Người bàn giao có cần tiếp tục xem hồ sơ đã bàn giao không? (a) không — bàn giao là chuyển hẳn; (b) có, chỉ xem.

> **Trả lời:** 

### ho-so-cong-viec · Q3

**Hiện trạng:** Hai menu "Hồ sơ duyệt mượn" và "Danh sách mượn" đang khóa, nhưng nút "Mượn", "Cho mượn" và thông báo mượn vẫn hoạt động (NV-17). Dữ liệu DEV: mượn / cho mượn được dùng nhiều đến 2025 (gần 600 yêu cầu), lần cuối 22/01/2026, sau đó không còn phát sinh.

**Câu hỏi:** Nghiệp vụ mượn / cho mượn hồ sơ hiện (a) đã bỏ, (b) tạm khóa sẽ mở lại, hay (c) vẫn dùng (menu khóa nhầm)?

> **Trả lời:** 

### ho-so-cong-viec · Q4

**Hiện trạng:** Mượn **bản mềm** được xem file trong hạn mượn; mượn **bản cứng** đã duyệt thì được xem cả file trên hệ thống cho tới khi chủ hồ sơ xác nhận đã trả, không xét hạn (NV-17 BR-45).

**Câu hỏi:** Người mượn bản cứng có được xem bản điện tử không? (a) có, đến khi trả; (b) có, nhưng chỉ trong hạn mượn; (c) không.

> **Trả lời:** 

### ho-so-cong-viec · Q5

**Hiện trạng:** Có sẵn chức năng gửi tin nhắn cảnh báo hồ sơ **sắp hết thời hạn bảo quản** (trước 30 ngày) và **nhắc trả bản cứng quá hạn**, nhưng không được lịch chạy nào kích hoạt; các loại tin 801–807 của nhóm "Quản lý hồ sơ" cũng đã bị xóa khỏi danh mục chặn tin (NV-20).

**Câu hỏi:** Hai loại cảnh báo này (a) đã bỏ, hay (b) vẫn cần (chưa được bật)?

> **Trả lời:** 

### ho-so-cong-viec · Q6

**Hiện trạng:** Hồ sơ có hai "trạng thái": trạng thái bàn giao (đang thực hiện / chờ tiếp nhận / từ chối / đã tiếp nhận — còn mục "Đã hoàn thành" không bao giờ được dùng) và trạng thái hồ sơ (đang thực hiện / đã đóng). Dữ liệu DEV chỉ còn đúng 1 hồ sơ mang "Đã hoàn thành" (tạo 25/09/2025) và không chức năng nào ghi ra giá trị này.

**Câu hỏi:** "Hoàn thành hồ sơ" bây giờ có phải chính là **Đóng hồ sơ** không? (a) đúng, mục "Đã hoàn thành" cũ không còn ý nghĩa; (b) khác — là bước nào?

> **Trả lời:** 

### ho-so-cong-viec · Q7

**Hiện trạng:** "File biên mục hồ sơ" được xem trên chi tiết và được nộp kèm sang phần mềm số hóa, bị hủy khi mở lại hồ sơ, nhưng trong hệ thống không có chỗ nào tạo ra file này (NV-15). Dữ liệu DEV: khoảng 320 file do khoảng 19 người dùng khác nhau tạo trong 22/01 → 10/04/2026, 130 file không rõ người tạo.

**Câu hỏi:** File biên mục do ai / hệ thống nào tạo và khi nào (ví dụ: phần mềm số hóa trả về sau khi tiếp nhận, hay một công cụ khác)?

> **Trả lời:** 

### ho-so-cong-viec · Q8

**Hiện trạng:** Tài liệu liên quan khác loại 1: màn hình gọi là "Tài liệu", ghi chú DB gọi là "Phim âm bản"; chỉ loại 1 được cộng số trang vào tổng số tờ hồ sơ (NV-08, NV-09 BR-26).

**Câu hỏi:** Loại 1 là (a) tài liệu giấy / điện tử thông thường hay (b) phim âm bản?

> **Trả lời:** 

### ho-so-cong-viec · Q9

**Hiện trạng:** Trên màn chi tiết hồ sơ, khối thao tác cũ (đóng dấu văn bản trong hồ sơ, chuyển văn bản đi xử lý, chuyển văn bản sang hồ sơ khác, yêu cầu bổ sung hồ sơ) đang bị ẩn hoàn toàn, nên các chức năng đó không dùng được dù phía máy chủ vẫn có (NV-13, NV-16, NV-21).

**Câu hỏi:** Các chức năng này (a) đã bỏ, hay (b) cần hiện lại — nếu (b) thì chức năng nào?

> **Trả lời:** 

### ho-so-cong-viec · Q10

**Hiện trạng:** Thư mục hồ sơ gắn với một năm; danh sách hồ sơ chỉ xem được tối đa hai năm thư mục liền nhau; "thư mục khác" tạo khi lập hồ sơ lấy năm hiện tại (NV-01, NV-02). Dữ liệu DEV: 368 thư mục năm 2025 (năm gán hàng loạt cho thư mục cũ), 79 thư mục năm 2026, vài thư mục năm khác.

**Câu hỏi:** Mỗi năm đơn vị (a) lập lại bộ thư mục mới, hay (b) một thư mục dùng qua nhiều năm (năm chỉ để lọc)?

> **Trả lời:** 


## Họp / lịch — `hop` (10 câu)

Nguồn: [hop/nghiep-vu.md](../hop/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### hop · Q1

**Hiện trạng:** Ai duyệt lịch được hệ thống tự tính: đơn vị gần nhất (đi ngược lên cây) có người làm "Quản lý lịch họp"; nhưng trước đó có nhiều quy tắc ưu tiên kế thừa từ đơn vị khác (ban giám đốc tập đoàn, phòng "Crowne", "chi nhánh VTT", Tổng giám đốc) với mã đơn vị cài cứng (NV-02 BR-10). Trên DB DEV các đơn vị cài cứng đó **không tồn tại** (chỉ có id 1 = Tỉnh Khánh Hoà) nên các quy tắc này không áp dụng được; vai trò "Quản lý lịch họp" mới gán cho 7 người.

**Câu hỏi:** Ở Khánh Hòa, lịch họp do ai duyệt? (a) luôn bộ phận quản lý lịch của đơn vị người đặt (hoặc cấp trên gần nhất); (b) của đơn vị quản lý phòng họp; (c) của đơn vị chủ trì. Các quy tắc "ban giám đốc tập đoàn / chi nhánh" có còn ý nghĩa không?

> **Trả lời:** 

### hop · Q2

**Hiện trạng:** Lịch có thành phần thuộc "ban giám đốc" được **chiếm phòng / cầu** của lịch đã duyệt; lịch bị chiếm tự quay về "Chờ duyệt" và người tạo nhận tin "tạm dừng" (NV-03 BR-16).

**Câu hỏi:** Có cần cơ chế ưu tiên này không? Nếu có, "ban giám đốc" ở đây là ai (lãnh đạo UBND tỉnh, lãnh đạo sở…)?

> **Trả lời:** 

### hop · Q3

**Hiện trạng:** Khi duyệt, email mời họp (lịch Outlook) **chỉ tự gửi nếu cuộc họp trong tuần hiện tại**; lịch tuần sau phải chờ người quản lý bấm "Gửi email" (NV-05 BR-20). SMS báo kết quả cho người đặt vẫn gửi ngay.

**Câu hỏi:** Đây có phải quy trình mong muốn (chốt lịch tuần rồi mới mời)? (a) đúng; (b) nên gửi ngay khi duyệt.

> **Trả lời:** 

### hop · Q4

**Hiện trạng:** Có quy tắc "khóa đặt lịch": trong một khung giờ cấu hình, không ai đặt được lịch cho **tuần sau** (trừ đơn vị đang được mở khóa); người quản lý lịch vẫn sửa được (NV-03 BR-14). Trên DB DEV cấu hình có tên nhưng **không có khoảng giờ** nên hiện không khóa gì.

**Câu hỏi:** Khánh Hòa có dùng quy tắc chốt lịch tuần này không? Nếu có, khung giờ khóa là từ thứ mấy, mấy giờ đến khi nào?

> **Trả lời:** 

### hop · Q5

**Hiện trạng:** Lãnh đạo đơn vị là **chủ trì** được tự duyệt lịch chờ duyệt mình chủ trì; với lịch họp ở địa điểm ngoài, **mọi cá nhân chủ trì** đều thấy nút Duyệt (NV-01 BR-03).

**Câu hỏi:** Ý đồ: (a) chủ trì là lãnh đạo thì được tự duyệt; (b) chỉ bộ phận quản lý lịch / trợ lý được duyệt.

> **Trả lời:** 

### hop · Q6

**Hiện trạng:** Màn "Cấu hình duyệt lịch" cho khai người duyệt theo từng ngày trong tuần, nhưng việc ai được bấm Duyệt **không phụ thuộc** cấu hình này và tên người duyệt cấu hình cũng không hiện ở đâu (NV-11 BR-32). Trên DB DEV đã có 616 dòng khai người duyệt — người dùng đang khai cấu hình này.

**Câu hỏi:** Cấu hình này dùng để làm gì? (a) chỉ để biết / in người duyệt trực theo ngày; (b) phải giới hạn: chỉ người được phân công ngày đó mới duyệt được.

> **Trả lời:** 

### hop · Q7

**Hiện trạng:** Thay người dự họp hiện **thay ngay, không cần duyệt**; màn "Phê duyệt thay đổi thành phần" (dành cho trợ lý phê duyệt) không có nơi nào tạo yêu cầu chờ duyệt (NV-07 BR-28). Trên DB DEV vẫn có 87 yêu cầu "chờ duyệt", 188 "đã duyệt", 68 "từ chối" (dữ liệu cũ / nơi khác) bên cạnh 216 lần "thay ngay".

**Câu hỏi:** Việc thay người dự họp (ví dụ lãnh đạo cử người đi thay) có cần ai phê duyệt không? (a) không; (b) có — người nào duyệt?

> **Trả lời:** 

### hop · Q8

**Hiện trạng:** Có sẵn tính năng **điểm danh** (người báo quân số, trong khoảng 30 phút trước đến 30 phút sau cuộc họp), **biểu quyết** và đồng bộ **eCabinet**; trên DB DEV chưa có biểu quyết nào, chưa có lịch nào báo quân số (NV-06, NV-14, NV-15, NV-16). Riêng eCabinet: 459 phòng họp đã có mã phòng bên eCabinet.

**Câu hỏi:** Ở Khánh Hòa đang / sẽ dùng những tính năng nào: điểm danh, biểu quyết, phòng họp không giấy eCabinet, báo cáo quân số?

> **Trả lời:** 

### hop · Q9

**Hiện trạng:** "Giới hạn cuộc họp" chỉ **cảnh báo** khi duyệt / phân công (người duyệt vẫn bấm tiếp được), tính theo số cuộc họp đã duyệt trong tuần (NV-10 BR-31).

**Câu hỏi:** Vượt ngưỡng có cần chặn không? (a) chỉ cảnh báo; (b) chặn duyệt.

> **Trả lời:** 

### hop · Q10

**Hiện trạng:** Lịch tuần cơ quan của đơn vị bật "công khai" xem được qua đường link **không cần đăng nhập** (NV-11). Trên DB DEV có 366 đơn vị đang bật công khai.

**Câu hỏi:** Lịch công khai dành cho ai: (a) mọi người có link (cả người ngoài cơ quan); (b) chỉ nội bộ.

> **Trả lời:** 


## Ký số — `ky-so` (10 câu)

Nguồn: [ky-so/nghiep-vu.md](../ky-so/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### ky-so · Q1

**Hiện trạng:** Màn Thông tin cá nhân cho mỗi người chọn **Ký USB Token** hoặc **Ký Sim CA** (NV-01). Ký qua **MySign / ký từ xa** (CloudCA) có sẵn trong code nhưng phần chọn đang ẩn, nên hiện không ai bật được trên web (NV-06). Dữ liệu DB DEV (2026-10-02): 24 người chọn USB Token, 1 người chọn SIM CA, 368 người để trống (được coi là USB Token), không ai chọn MySign; chưa có giao dịch ký SIM nào; vẫn có 104 chứng thư MySign và hơn 1.000 thiết bị MySign được đồng bộ từ ứng dụng di động.

**Câu hỏi:** Ở Khánh Hòa cán bộ đang ký bằng gì: (a) chỉ USB Token, (b) USB Token và SIM CA, (c) có cả MySign? Hình thức nào chắc chắn không dùng?

> **Trả lời:** 

### ky-so · Q2

**Hiện trạng:** Ảnh chữ ký có 4 loại: màn khai gọi loại 0 là **"Ảnh ký nháy"**, còn ghi chú trên CSDL gọi là **"ảnh in"**; ký nháy dùng loại 0, ký duyệt dùng loại 1 (NV-07 BR-24).

**Câu hỏi:** Loại 0 là (a) ảnh ký nháy (chữ ký tắt) hay (b) ảnh in? Ảnh ký loại 2, loại 3 dùng trong trường hợp nào (ví dụ chữ ký khi ký thay mặt, ký thừa lệnh…)?

> **Trả lời:** 

### ky-so · Q3

**Hiện trạng:** Khi soạn dự thảo, người soạn chọn được loại ảnh ký (1 / 2 / 3) cho từng người ký; nhưng lúc ký thật, hệ thống in ảnh theo ngày hiệu lực và ưu tiên loại 1, không theo lựa chọn đó (NV-08 BR-27).

**Câu hỏi:** Việc chọn loại ảnh khi soạn nhằm mục đích gì: (a) quyết định ảnh sẽ in lên văn bản khi ký, (b) chỉ để xem trước?

> **Trả lời:** 

### ky-so · Q4

**Hiện trạng:** Người chưa khai USB Token nào: lần ký đầu tiên, USB đang cắm được **tự ghi nhận** là USB của người đó; từ đó chỉ USB đã ghi nhận mới ký được. Con dấu đơn vị cũng vậy với USB Token đơn vị (NV-02 BR-07, NV-11). DB DEV (2026-10-02): 160 USB Token cá nhân và 70 USB Token đơn vị đang hiệu lực, vẫn phát sinh mới tới cuối 09/2026.

**Câu hỏi:** Quy định nghiệp vụ là: (a) mỗi người / đơn vị tự đăng ký USB qua lần ký đầu như hiện nay, (b) USB phải được khai trước (cá nhân tự khai hoặc quản trị khai) mới được ký?

> **Trả lời:** 

### ky-so · Q5

**Hiện trạng:** Cặp trình ký theo dõi **bộ hồ sơ giấy** có mã vạch; trợ lý cập nhật tay trạng thái từng lãnh đạo ("Đã vào, chờ ký", "Đã ra…", "Bị trả lại", "Đã trả…"); hệ thống không chặn thứ tự chuyển trạng thái (NV-13). Danh mục trạng thái trên CSDL **có khai bước kế** (0 → 1 → 2 → 5; 3 → 6; "Bị trả lại" 4 → 1) nhưng màn hình chỉ dùng làm gợi ý, vẫn cho chọn tự do. DB DEV (2026-10-02) có 151 cặp, trong đó 118 lượt người ký còn ở "Chưa trình ký".

**Câu hỏi:** Cặp trình ký giấy còn dùng ở Khánh Hòa không? Nếu dùng: "Bị trả lại" (4) khác "Đã ra, bị từ chối ký" (3) thế nào, và trợ lý có được chọn tự do mọi trạng thái hay phải đi theo thứ tự?

> **Trả lời:** 

### ky-so · Q6

**Hiện trạng:** Đóng dấu số hiện chỉ chạy được bằng **USB Token của đơn vị**; đường đóng dấu bằng chữ ký số tổ chức từ xa (tài khoản theo mã số thuế) có trong code nhưng không hoạt động (NV-06 BR-20). DB DEV (2026-10-02): 70 USB Token đơn vị đang hiệu lực.

**Câu hỏi:** Văn thư Khánh Hòa đóng dấu số bằng (a) USB Token đơn vị, (b) chữ ký số tổ chức từ xa, (c) cả hai?

> **Trả lời:** 

### ky-so · Q7

**Hiện trạng:** Ảnh dấu có hai nhóm: **dấu đơn vị** và **dấu xác nhận**; dấu xác nhận được đóng lên văn bản đã ban hành / văn bản đến (NV-10, NV-11). DB DEV (2026-10-02): 105 ảnh dấu xác nhận (66 còn hiệu lực) so với 253 ảnh dấu đơn vị (131 còn hiệu lực).

**Câu hỏi:** Dấu xác nhận dùng trong nghiệp vụ nào (ví dụ "sao y", "đã nhận", xác nhận văn bản đến…)?

> **Trả lời:** 

### ky-so · Q8

**Hiện trạng:** Chức năng "Xác thực chữ ký số" hiển thị thông tin chữ ký, kiểm file có bị sửa và chứng thư còn hạn, nhưng không hỏi nhà cung cấp chứng thư xem chứng thư có bị thu hồi (NV-12 BR-42).

**Câu hỏi:** Mức xác thực mong muốn: (a) như hiện nay là đủ, (b) phải kiểm cả tình trạng thu hồi với nhà cung cấp?

> **Trả lời:** 

### ky-so · Q9

**Hiện trạng:** Tin nhắn loại 111 có tên **"Ký thay"**, nhưng code chỉ gửi khi **đổi người ký** trong luồng; không có chức năng thư ký / trợ lý ký bằng chữ ký của lãnh đạo (NV-14).

**Câu hỏi:** "Ký thay" trong nghiệp vụ là (a) đổi sang người khác ký (người mới nhận tin), (b) người khác ký thay mặt lãnh đạo nhưng vẫn ghi tên lãnh đạo?

> **Trả lời:** 

### ky-so · Q10

**Hiện trạng:** Hệ thống chỉ mã hóa file theo từng người nhận khi văn bản / phiếu trình có **độ mật** (NV-16). Trên DB DEV (2026-10-02) việc mã hóa này vẫn phát sinh đều tới 09/2026 (khoảng 52.900 bản ghi quyền đọc file, hơn 121.000 chứng thư mật cá nhân đang hiệu lực), trong khi trước đây đã xác nhận "văn bản mật chưa dùng".

**Câu hỏi:** Văn bản / phiếu trình mật (mã hóa file theo người nhận) hiện (a) đang dùng thật, (b) chỉ là dữ liệu thử trên môi trường DEV, (c) dùng cho một loại tài liệu khác (nêu rõ)?

> **Trả lời:** 


## Hệ thống / quản trị — `he-thong` (10 câu)

Nguồn: [he-thong/nghiep-vu.md](../he-thong/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### he-thong · Q1

**Hiện trạng:** Khi đăng nhập bằng form, mật khẩu được kiểm qua **hệ thống SSO**; mật khẩu lưu trong VOffice chỉ dùng cho vài kênh phụ, và màn "Đổi mật khẩu" trong VOffice chỉ đổi bản lưu trong VOffice (NV-01 BR-01, NV-04 BR-14).

**Câu hỏi:** Mật khẩu chính thức của cán bộ là: (a) mật khẩu tài khoản SSO tỉnh — VOffice không cần quản mật khẩu riêng; (b) mật khẩu riêng của VOffice; (c) cả hai cùng tồn tại?

> **Trả lời:** 

### he-thong · Q2

**Hiện trạng:** Đăng nhập qua VNeID ghép tài khoản bằng **số định danh trả về từ VNeID = mã nhân viên** trên VOffice; SSO ghép bằng tên đăng nhập SSO = mã nhân viên (NV-02 BR-05).

**Câu hỏi:** Mã nhân viên trên VOffice có phải luôn là (a) số định danh cá nhân / CCCD; (b) tên đăng nhập SSO; (c) mã riêng — cần cột liên kết khác?

> **Trả lời:** 

### he-thong · Q3

**Hiện trạng:** Menu gán cho vai trò "hỗ trợ" (`VAITRO_SUPPORT`) **hiện cho mọi người dùng**; người thực sự giữ vai trò này thì xử lý phản ánh (NV-03 BR-12, NV-18 BR-40). Trên DB DEV vai trò này được cấp menu cha "QUẢN TRỊ" và các menu "Danh sách phản ánh" → mọi cán bộ thấy mục "QUẢN TRỊ" (rỗng nếu không có quyền quản trị) và "DANH SÁCH PHẢN ÁNH".

**Câu hỏi:** Ý đồ là: (a) vai trò hỗ trợ dùng để khai "menu chung cho tất cả" (ví dụ HỖ TRỢ, phản ánh); (b) chỉ người được gán vai trò hỗ trợ mới thấy các menu đó?

> **Trả lời:** 

### he-thong · Q4

**Hiện trạng:** Trên form người dùng, mỗi đơn vị có ô "nhận văn bản đơn vị" với 4 lựa chọn: Không nhận / Chủ trì / Phối hợp / Nhận để biết; khi văn bản chuyển cho đơn vị, hệ thống chỉ tự đưa vào người có lựa chọn "Chủ trì" (NV-06 bảng `USER_ROLE`). Trên DB DEV gần như chưa dùng: 683 / 727 dòng để trống, 39 "Chủ trì", 2 "Phối hợp", 2 "Nhận để biết", 1 "Không nhận".

**Câu hỏi:** Ba lựa chọn Chủ trì / Phối hợp / Nhận để biết nghĩa là gì: người đó tự nhận văn bản chuyển tới đơn vị với **đúng vai trò đó**? Hay chỉ cần "có nhận / không nhận"?

> **Trả lời:** 

### he-thong · Q5

**Hiện trạng:** Người trong danh sách "không nhận văn bản khi chuyển cho đơn vị" bị loại ở **mọi đơn vị** họ thuộc trong phần lớn đường chuyển, nhưng chỉ ở **đơn vị đã cấu hình** khi chuyển theo nhóm đơn vị (NV-15 BR-37). DB DEV đang có 21 người ở 11 đơn vị trong danh sách.

**Câu hỏi:** Danh sách này áp cho: (a) toàn bộ đơn vị người đó thuộc; (b) chỉ đơn vị mà quản trị đã chọn khi cấu hình?

> **Trả lời:** 

### he-thong · Q6

**Hiện trạng:** Ở "Quản lý người dùng", quản trị (`ADMIN` hay `ADMIN_LEVEL1`) chỉ quản lý được người trong cây đơn vị nơi mình được gán vai trò; ở "Quản lý đơn vị", người có `ADMIN` ở bất kỳ đâu thấy và sửa được **cả cây tỉnh** (NV-06 BR-16, NV-11).

**Câu hỏi:** Quản trị hệ thống (`ADMIN`) là: (a) quản trị toàn tỉnh — mọi màn quản trị đều toàn tỉnh; (b) quản trị theo cây đơn vị được gán — màn đơn vị cũng nên giới hạn như màn người dùng?

> **Trả lời:** 

### he-thong · Q7

**Hiện trạng:** Màn "Đồng bộ người dùng" đã tắt; phía máy chủ còn chức năng nhận dữ liệu nhân sự, và khi nhân sự đổi đơn vị thì **xóa toàn bộ vai trò** của người đó (NV-08 BR-23).

**Câu hỏi:** Hiện nay người dùng / đơn vị được cập nhật bằng (a) nhập tay trên VOffice; (b) đồng bộ tự động từ hệ thống nhân sự (hệ thống nào)? Nếu (b): khi đổi đơn vị có đúng là phải gỡ hết vai trò cũ không?

> **Trả lời:** 

### he-thong · Q8

**Hiện trạng:** Có hai loại danh mục: "Danh mục động" (bảng mã dùng chung) và "Danh mục nhóm phân loại" áp theo đơn vị, trong đó đơn vị con khai riêng sẽ **thay hẳn** danh mục cấp trên (NV-13 BR-33).

**Câu hỏi:** Với danh mục theo đơn vị, khi đơn vị con khai thêm giá trị thì mong muốn: (a) thay danh mục của cấp trên (như hiện tại); (b) cộng thêm vào danh mục cấp trên?

> **Trả lời:** 

### he-thong · Q9

**Hiện trạng:** Menu "Quản lý giới thiệu trang" và "Danh sách khảo sát" đang mở nhưng phía người dùng không có chỗ xem giới thiệu / trả lời khảo sát (NV-17).

**Câu hỏi:** Hai tính năng này còn dùng không: (a) ngừng, có thể khóa menu; (b) cần dùng — mong muốn người dùng thấy giới thiệu / khảo sát ở đâu?

> **Trả lời:** 

### he-thong · Q10

**Hiện trạng:** Cấu hình widget trang chủ của từng người và chế độ "đơn giản / đầy đủ" chỉ được giữ tạm, mất khi hệ thống khởi động lại (NV-16 BR-38).

**Câu hỏi:** Cấu hình trang chủ cá nhân cần (a) giữ lâu dài; (b) tạm thời là đủ?

> **Trả lời:** 


## KPI / đánh giá / báo cáo — `kpi-danh-gia` (10 câu)

Nguồn: [kpi-danh-gia/nghiep-vu.md](../kpi-danh-gia/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### kpi-danh-gia · Q1

**Hiện trạng:** Đánh giá công tác tuần (tự chấm, người đánh giá chấm, phê duyệt theo tuần; tổng hợp tháng / quý / năm) chạy riêng, không dùng chung dữ liệu với phiếu đánh giá công việc và KI cá nhân hằng tháng của phân hệ Công việc; menu chỉ mở cho vài đơn vị qua danh sách trắng — và trên DB DEV các đơn vị khai không khớp đơn vị nào nên **không ai thấy menu** (mục 1.3) (NV-04, X9).

**Câu hỏi:** Quan hệ giữa hai cách đánh giá là gì? (a) đánh giá tuần thay cho phiếu đánh giá công việc / KI ở các đơn vị được mở menu; (b) chạy song song, độc lập; (c) điểm tuần sẽ là đầu vào để xếp KI tháng.

> **Trả lời:** 

### kpi-danh-gia · Q2

**Hiện trạng:** Ngưỡng xếp loại "Hoàn thành tốt nhiệm vụ": bảng xếp loại đang có trên DB DEV, Biểu mẫu 2A, chú thích trên màn và đếm loại tháng / quý dùng **từ 70 điểm**; file cài đặt ban đầu và sắp xếp danh sách tuần dùng **từ 75 điểm**. Bảng xếp loại trên DB DEV đang ở trạng thái đã xóa nhưng hệ thống vẫn dùng (mục 3 đầu, NV-08).

**Câu hỏi:** Mức đúng là (a) 70 hay (b) 75?

> **Trả lời:** 

### kpi-danh-gia · Q3

**Hiện trạng:** Mục công việc đã nằm trong phiếu tuần đã được chấm / phê duyệt vẫn sửa, xóa, báo cáo lại được; phiếu tuần không lưu lại nội dung mục công việc (NV-02 BR-10).

**Câu hỏi:** (a) phải khóa mục công việc của tuần đã chấm / duyệt; (b) cho sửa tự do — phiếu đã duyệt chỉ giữ điểm.

> **Trả lời:** 

### kpi-danh-gia · Q4

**Hiện trạng:** Người đánh giá chấm được cả cán bộ **chưa tự đánh giá** tuần đó (hệ thống tự tạo phiếu trống phần tự chấm); khi đó gần như luôn phải nhập giải thích (NV-05 BR-19, BR-20).

**Câu hỏi:** (a) được chấm thay như hiện nay; (b) phải chờ cán bộ tự chấm trước.

> **Trả lời:** 

### kpi-danh-gia · Q5

**Hiện trạng:** Có **hai đường phê duyệt** không đồng bộ: "Phê duyệt đơn vị" duyệt từng người theo người phê duyệt được cấu hình; "Danh sách đánh giá chờ phê duyệt" duyệt cả đơn vị theo lãnh đạo đơn vị cấp trên. Duyệt bên này không đổi trạng thái phiếu bên kia (NV-06, NV-07).

**Câu hỏi:** (a) hai cấp phê duyệt nối tiếp (người phê duyệt rồi lãnh đạo cấp trên); (b) hai cách thay thế nhau — đơn vị chọn một; (c) một cách sẽ bỏ. Nếu (a), bước nào là bước cuối?

> **Trả lời:** 

### kpi-danh-gia · Q6

**Hiện trạng:** Chấm điểm thi đua: trợ lý Ban kế hoạch không nhập được số liệu cho tiêu chí mà đơn vị đánh giá chưa nhập kế hoạch; Ban kế hoạch chỉ rà soát rồi "Gửi tổng hợp" (NV-11 BR-37).

**Câu hỏi:** (a) Ban kế hoạch chỉ chốt, mọi số liệu do đơn vị đánh giá nhập; (b) Ban kế hoạch được nhập thay khi đơn vị đánh giá chưa nhập.

> **Trả lời:** 

### kpi-danh-gia · Q7

**Hiện trạng:** Tiêu chí "chỉ tiêu sản xuất kinh doanh" có mã chỉ tiêu và màn "Đồng bộ danh sách đơn vị" ánh xạ mã đơn vị sang hệ thống số liệu kinh doanh, nhưng việc tự lấy số liệu đang tắt — người dùng nhập tay; dữ liệu chấm điểm thi đua trên DB DEV dừng ở 06/2022 (NV-11, NV-13).

**Câu hỏi:** (a) nhập tay là cách làm hiện hành, màn ánh xạ chỉ còn lưu trữ; (b) vẫn cần hệ thống tự lấy số liệu kinh doanh.

> **Trả lời:** 

### kpi-danh-gia · Q8

**Hiện trạng:** KPI đơn vị: danh sách đơn vị để chấm có cả các phòng ban người dùng đang làm lãnh đạo, nhưng hệ thống chặn không cho chấm KPI cho chính đơn vị mình (NV-15 BR-45).

**Câu hỏi:** (a) chỉ cấp trên chấm cho đơn vị con — phòng ban của mình xuất hiện là thừa; (b) lãnh đạo phòng được tự chấm KPI cho phòng mình.

> **Trả lời:** 

### kpi-danh-gia · Q9

**Hiện trạng:** "Đề xuất cộng điểm", "Phê duyệt đề xuất", "Đánh giá đơn vị" đang khóa menu; bảng đề xuất cộng điểm không có trên DB DEV; KI đơn vị không phát sinh từ 01/2022; KPI đơn vị và đánh giá đơn vị trên DB DEV chỉ có dữ liệu năm 2015. Nếu dùng lại: điểm đề xuất hiện lấy **trung bình** các đề xuất đã duyệt (tối đa 20) trong khi nhãn ghi "tổng" (NV-16, NV-17).

**Câu hỏi:** (a) các màn này đã ngừng, chỉ giữ dữ liệu cũ; (b) sẽ mở lại — khi đó điểm đề xuất là tổng (tối đa 20) hay trung bình?

> **Trả lời:** 

### kpi-danh-gia · Q10

**Hiện trạng:** Cấu hình: hai menu "Quản lý cấu hình KI" và "Quản lý cấu hình tỷ lệ" mở cùng một màn đủ 7 loại; menu "Danh mục nhà cung cấp" thực chất là cấu hình công thức KI, lưu công thức dạng chữ nhưng không nơi nào dùng để tính (NV-18, NV-19).

**Câu hỏi:** (a) một menu cấu hình là đủ, công thức KI đã bỏ; (b) mỗi menu lẽ ra chỉ một nhóm loại (KI: 1, 4, 6; tỷ lệ: 2, 3, 5, 7) và công thức KI vẫn là kế hoạch.

> **Trả lời:** 


## Tích hợp — `tich-hop` (10 câu)

Nguồn: [tich-hop/nghiep-vu.md](../tich-hop/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### tich-hop · Q1

**Hiện trạng:** Nút chia sẻ trên văn bản đi chỉ gửi cho **Thư viện điện tử**; mã hệ thống nhận được ghi cứng trong code, không có màn chọn hệ thống nhận (NV-03 BR-07). Trên DEV đã có khoảng 2.000 lượt văn thư bấm chia sẻ (hầu hết của một đơn vị) nhưng chưa có lần thư viện lấy về. Ngoài ra trên DEV **phần mềm số hóa (`APP_SHVB`)** và hệ thống **`ATTT`** được cấp quyền **tự kéo** văn bản đến / đi theo đơn vị (và theo người dùng) — đó là kéo theo cấu hình, không qua nút của văn thư (NV-04).

**Câu hỏi:** Ngoài Thư viện điện tử, có hệ thống nào khác cần nhận văn bản do văn thư chủ động chia sẻ không? (a) chỉ Thư viện điện tử; (b) sẽ có thêm — cần cho văn thư chọn hệ thống nhận. Thư viện điện tử hiện đã kết nối chạy thật chưa? Và `ATTT` là hệ thống nào, lấy văn bản để làm gì?

> **Trả lời:** 

### tich-hop · Q2

**Hiện trạng:** Văn thư bấm chia sẻ rồi thì không có cách **rút lại**; khi văn bản bị sửa / xóa, hệ thống tự báo cho thư viện bản cập nhật / bản xóa (NV-03 BR-09).

**Câu hỏi:** Văn thư có cần thao tác "thu hồi chia sẻ" (văn bản vẫn còn nhưng không muốn thư viện giữ nữa) không? (a) không cần; (b) cần.

> **Trả lời:** 

### tich-hop · Q3

**Hiện trạng:** Văn bản do hệ thống KNTC đẩy sang luôn được tạo là **công văn, độ khẩn thường, độ mật thường**, chuyển thẳng văn thư cấp số, người ký do KNTC chỉ định (NV-05).

**Câu hỏi:** Mọi văn bản từ KNTC đều là công văn thường? (a) đúng; (b) KNTC cần gửi kèm thể loại / độ khẩn. Và văn thư được KNTC "đại diện" có cần là văn thư của đúng đơn vị ban hành (hiện code kiểm đúng như vậy)?

> **Trả lời:** 

### tich-hop · Q4

**Hiện trạng:** Văn phòng số có sẵn đường nhận đồng bộ nhân viên từ hệ thống nhân sự (VHR — kế thừa Viettel) nhưng không có nơi nào gọi; màn đồng bộ đã tắt, màn "Thông tin nhân viên VHR" không mở được; trên DEV gần như không người dùng nào có dấu đồng bộ (NV-07).

**Câu hỏi:** Ở Khánh Hòa, danh sách cán bộ / đơn vị được (a) quản trị nhập tay / import trong Văn phòng số; (b) đồng bộ tự động từ một hệ thống nhân sự của tỉnh — hệ thống nào? Hai menu "Đồng bộ người dùng" và "Thông tin nhân viên VHR" còn cần không?

> **Trả lời:** 

### tich-hop · Q5

**Hiện trạng:** Mở file để soạn thảo / xem trực tuyến bằng cách mới thì hệ thống **đánh dấu văn bản là đã đọc** cho người mở (và cho đơn vị nếu người đó là văn thư), trong khi ghi chú trong code nói đọc file thì không đánh dấu (NV-09 BR-21). Trên DEV tính năng đã được dùng (khoảng 460 lượt ghi lịch sử sửa).

**Câu hỏi:** Mở file đính kèm trên trình soạn thảo có được tính là "đã đọc văn bản" không? (a) có; (b) không — chỉ tính khi mở chi tiết văn bản.

> **Trả lời:** 

### tich-hop · Q6

**Hiện trạng:** Cấu hình phiên bản app có cờ đăng nhập 0 / 1 trả cho app theo từng phiên bản; ngoài ra có tham số "phiên bản hiện tại" để bật màn đăng nhập riêng khi app đang chờ duyệt trên kho ứng dụng — tham số này chưa khai trên DEV (NV-11).

**Câu hỏi:** Cờ đăng nhập 0 / 1 của từng phiên bản nghĩa là gì: (a) 1 = chỉ cho đăng nhập SSO / VNeID, 0 = cho cả tài khoản; (b) nghĩa khác (mô tả)?

> **Trả lời:** 

### tich-hop · Q7

**Hiện trạng:** Khi đăng ký hệ thống tích hợp mới, hệ thống mặc định **không báo kết quả "đã ký"** cho hệ thống ngoài (lý do ghi trong code: người ký cuối có thể ký lại), chỉ báo từ chối / hủy / ban hành / đóng dấu (NV-01 BR-02).

**Câu hỏi:** Hệ thống ngoài có cần biết thời điểm văn bản **đã ký xong** (trước khi ban hành) không? (a) không, chỉ cần ban hành / hủy / từ chối; (b) cần.

> **Trả lời:** 

### tich-hop · Q8

**Hiện trạng:** Có một bộ API mới đọc **cây tổ chức Đảng** tách khỏi cây chính quyền (khối Đảng / khối chuyên môn) trên cùng danh mục đơn vị, chưa có màn nào dùng; trên DEV **chưa đơn vị nào có thông tin cây Đảng** (cha Đảng, đường dẫn Đảng, "chỉ thuộc Đảng" đều trống) (NV-15).

**Câu hỏi:** Văn phòng số Khánh Hòa có quản lý văn bản / nhiệm vụ theo **tổ chức Đảng** riêng không? (a) có — cây Đảng khác cây chính quyền, sẽ làm màn; (b) chưa dùng.

> **Trả lời:** 

### tich-hop · Q9

**Hiện trạng:** Hệ thống chạy được ở hai chế độ "site công khai (Internet)" và "site nội bộ"; dữ liệu có dấu nguồn / phiên bản để đồng bộ qua lại; ký SIM chỉ ở site công khai (NV-13).

**Câu hỏi:** Ở Khánh Hòa có đúng **hai cụm máy chủ** (Internet và mạng nội bộ) dùng chung dữ liệu đồng bộ qua lại không? (a) có hai cụm; (b) chỉ một cụm.

> **Trả lời:** 

### tich-hop · Q10

**Hiện trạng:** Còn nhiều tích hợp kế thừa từ Viettel: thanh toán ViettelPay khi gia hạn chứng thư, hợp đồng điện tử vContract, "Văn bản ký với đối tác" (menu đã khóa), đồng bộ ERP, các hệ thống trình ký FICO / ERP_SAP / NETLEASE… (NV-06, NV-12).

**Câu hỏi:** Những tích hợp này còn dùng ở Khánh Hòa không? (a) đã ngừng, chỉ giữ dữ liệu cũ; (b) còn dùng — nêu hệ thống nào.

> **Trả lời:** 


## Tài liệu mẫu / thư viện — `tai-lieu-mau` (8 câu)

Nguồn: [tai-lieu-mau/nghiep-vu.md](../tai-lieu-mau/nghiep-vu.md) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.

### tai-lieu-mau · Q1

**Hiện trạng:** Ba menu "Thư viện văn bản" (dưới Văn công khai), "Thư viện cá nhân" (dưới Văn bản đến) và "Thư viện Quy trình - Quy định" đều mở **cùng một danh sách**: các văn bản đang công khai cho phạm vi có đơn vị mình. Không có kho riêng cho cá nhân hay cho quy trình (NV-01 BR-01).

**Câu hỏi:** Ba menu này có phải cố ý trùng nhau? (a) đúng — chỉ là ba lối vào cùng một thư viện; (b) "Thư viện cá nhân" và "Quy trình - Quy định" phải là kho riêng (theo thư mục / theo người).

> **Trả lời:** 

### tai-lieu-mau · Q2

**Hiện trạng:** Có sẵn tính năng dựng **thư mục thư viện** (Quy trình dùng chung / Cá nhân) ở menu quản trị "Cấu hình thư viện" và nút "Chuyển vào thư viện" trên các hộp văn bản, nhưng nút đã bị ẩn ở hầu hết màn và trên DB DEV chưa có thư mục / văn bản nào (NV-03 BR-07).

**Câu hỏi:** Nghiệp vụ thư mục thư viện còn dùng không? (a) đã ngừng, menu "Cấu hình thư viện" là thừa; (b) cần dùng — xếp văn bản vào thư mục kèm mô tả và thời hạn hiệu lực.

> **Trả lời:** 

### tai-lieu-mau · Q3

**Hiện trạng:** Thư viện chỉ cho thấy văn bản công khai cho **đơn vị mình hoặc đơn vị cấp trên** (theo các đơn vị mình là văn thư / quản trị / đơn vị chính); văn bản công khai cho đơn vị cấp dưới không hiện, và ô "Tìm tất cả đơn vị" đã bị ẩn (NV-01 BR-02).

**Câu hỏi:** Phạm vi xem thư viện như vậy có đúng ý đồ? (a) đúng; (b) lãnh đạo / văn thư cấp trên cần thấy cả văn bản công khai cho đơn vị cấp dưới.

> **Trả lời:** 

### tai-lieu-mau · Q4

**Hiện trạng:** Văn thư xóa một tag trong popup "Gán tag văn bản" thì tag bị **xóa khỏi danh mục của đơn vị** (văn bản khác không còn gợi ý tag đó), nhưng tên tag vẫn còn trên các văn bản đã gắn (NV-07 BR-18). Trên DB DEV (2026-10-02) danh mục có ~630 tag còn hiệu lực, 172 tag đã xóa, nhưng chưa văn bản nào đang mang tag.

**Câu hỏi:** Thao tác xóa tag trong popup nghĩa là gì? (a) chỉ bỏ tag khỏi văn bản đang mở; (b) xóa hẳn tag khỏi danh mục đơn vị (như hiện tại) — khi đó tên tag trên các văn bản cũ có cần gỡ theo không?

> **Trả lời:** 

### tai-lieu-mau · Q5

**Hiện trạng:** Biểu mẫu có hai trường chọn: web ghi nhãn "Hình thức" (chọn từ danh mục loại văn bản) và "Ngành" (chọn từ danh mục lĩnh vực); chú thích trên DB lại ghi cột loại là "Id ngành", cột lĩnh vực là "Id lĩnh vực". Dữ liệu DB DEV (2026-10-02) cho thấy trường thứ nhất đúng là **loại văn bản** (Chỉ thị, Báo cáo đột xuất, Chứng từ XNK, Công văn…) — chú thích DB sai; trường thứ hai lưu lĩnh vực nhưng web gọi là "Ngành" (NV-05).

**Câu hỏi:** Trường thứ hai của biểu mẫu nên gọi là gì trên màn hình: (a) "Lĩnh vực" (đúng dữ liệu đang lưu); (b) "Ngành" — khi đó cần danh mục ngành riêng?

> **Trả lời:** 

### tai-lieu-mau · Q6

**Hiện trạng:** Ngoài "Mẫu ý kiến" mới dùng khi chuyển văn bản, hệ thống còn một bộ **ý kiến mẫu cũ** theo người (hai loại: khi ký văn bản, khi chuyển công văn, có sắp thứ tự), có API nhưng web không gọi; bảng dữ liệu của nó **không tồn tại** trên DB DEV (2026-10-02), nên nếu gọi sẽ lỗi (NV-06).

**Câu hỏi:** Bộ ý kiến mẫu cũ còn dùng ở đâu không? (a) không — đã thay bằng mẫu ý kiến mới; (b) còn dùng (ví dụ trên ứng dụng di động).

> **Trả lời:** 

### tai-lieu-mau · Q7

**Hiện trạng:** Danh sách biểu mẫu hiện **cả biểu mẫu chưa đến hoặc đã hết hiệu lực** (chỉ ghi nhãn trạng thái); biểu mẫu áp dụng cho một đơn vị thì cán bộ ở **cả đơn vị cấp trên lẫn cấp dưới** của đơn vị đó đều thấy; biểu mẫu chỉ để xem / tải, không chọn được khi soạn dự thảo (NV-05 BR-12 … BR-14).

**Câu hỏi:** (a) Biểu mẫu hết hiệu lực có nên ẩn khỏi danh sách mặc định không? (b) Biểu mẫu áp dụng cho đơn vị cha thì đơn vị con thấy là đúng; còn đơn vị cha thấy biểu mẫu của đơn vị con có cần không?

> **Trả lời:** 

### tai-lieu-mau · Q8

**Hiện trạng:** Báo cáo ngày (thiết lập mẫu, gửi) chỉ dành cho người có vai trò mã **"REPORT"** tại đơn vị; báo cáo tuần / tháng dành cho lãnh đạo / thủ trưởng / trợ lý và chuyên viên được gán (NV-09 BR-21). DB DEV (2026-10-02): vai trò "Báo cáo" (`REPORT`) đang gán 9 lần.

**Câu hỏi:** Vai trò "REPORT" trong thực tế là ai (chuyên viên tổng hợp, văn thư, thư ký…)? Lãnh đạo đơn vị có cần tự gửi được báo cáo ngày không?

> **Trả lời:** 

