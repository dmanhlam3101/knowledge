# Câu hỏi mở cần người xác nhận

> Sinh bởi `_tools/questions.py`. Trả lời xong: sửa file gốc (xóa ❓), chạy lại script. Đây là danh sách việc cho BA / người biết nghiệp vụ.
Tổng: **121** câu.

## cong-viec/dac-thu.md (1)

- [ ] L3: - **Gần như toàn bộ gen-1**: `TaskAction` (`/taskAction`) + `TaskService` (`/TaskService`, class annotated @RestController dù tên Service) → `controler/TaskController` ❓ → `TaskDAO`, `TaskRatingDAO`, `KI*DAO`. Không có controller gen-2 riêng → tính năng mới nên tạo `TaskController` gen-2 (`/api/task`) theo `_chung/cach-lam-chuan/them-api-be-gen2.md`.

## cong-viec/nghiep-vu.md (4)

- [ ] L34: - QT1. Tổng tỷ trọng công việc trong kỳ = 100% (`updateProportionPersonalTasks`, `checkPointUnit`) ❓.
- [ ] L38: - QT5. Việc sinh từ văn bản giữ liên kết `DOCUMENT_ID`; đóng văn bản không tự đóng việc ❓.
- [ ] L41: 1. "Phiếu giao việc" và "phiếu đánh giá" là file PDF sinh ra (`convertTaskToPDF`, `convertRatingTaskToPDF`) rồi ký số — đúng không? Ký bằng loại chữ ký nào?
- [ ] L42: 2. KI khác KPI thế nào trong hệ thống này?

## he-thong/dac-thu.md (1)

- [ ] L4: - Hai hệ quyền song song: VPS (`SYS_OPERATION`/`SYS_RESOURCE`/`RolePermission`) và gen-2 `PermissionBase`/`PermissionData` — cần chốt ❓ nguồn hiện hành trước khi thêm quyền mới.

## he-thong/nghiep-vu.md (4)

- [ ] L24: - Tham số: `SYSTEM_PARAMETER`/`CONFIG_PARAMETER` (`configParamAction.GetAppConfig`, `getConfigParamMultiSign`; `ManagerController.get-lst-param/add-param`), danh sách đen (`ConfigBackList` — chặn người nhận? ❓), người nhận nhắc ký muộn (`getLstUserReMessOfSignerLate`, `NotifyToNextSignerVM`).
- [ ] L33: 1. Quyền thao tác trong màn hình dùng VPS (`SYS_OPERATION`/`SYS_RESOURCE`) hay `permission-base` gen-2 — cái nào là nguồn hiện hành?
- [ ] L34: 2. SSO đang dùng là Viettel passport hay SSO tỉnh (VNeID)?
- [ ] L35: 3. `ConfigBackList` là gì?

## ho-so-cong-viec/dac-thu.md (1)

- [ ] L5: - `TypeConfigAction.getUserDocRolesByEmpId`, `getUserRolesDetail` được web gọi nhưng không nối được endpoint ❓ (đổi tên?).

## ho-so-cong-viec/nghiep-vu.md (6)

- [ ] L16: - Trạng thái hồ sơ: mở / đang xử lý / đề nghị hoàn thành / hoàn thành / đã nộp lưu / trong kho ❓ mã cụ thể — tra `Brief.getBriefProcessingStats`, `checkHardStatusBrief` (`hardStatus` = trạng thái bản cứng: đang ở kho / đang cho mượn).
- [ ] L19: - Văn bản trong hồ sơ: `BRIEF_DOCUMENT_MAP` ❓ (+ số trang giấy), file `BRIEF_FILES_ATTACHMENT`, đa phương tiện `BRIEF_MULTIMEDIA` (SQL `20250303_add_column_table_brief_multimedia_file.sql`), file danh mục `CATALOGIN_BRIEF_FILE` (`10012026_create_table_catalogin_brief_file.sql`).
- [ ] L21: - Chứng thư SHVB (`get-cert-shvb`) ❓ ký số hồ sơ.
- [ ] L40: 1. Vòng đời trạng thái hồ sơ chính xác và ai được "hoàn thành"?
- [ ] L41: 2. Nộp lưu có theo thời hạn (năm) và tự động không?
- [ ] L42: 3. `get-cert-shvb` phục vụ ký số hồ sơ điện tử theo chuẩn lưu trữ?

## hop/dac-thu.md (1)

- [ ] L5: - `voffice.service.url.meeting` trong `application.properties` — BE họp có thể trỏ **server khác** (10.60.110.21) ❓ còn dùng không.

## hop/nghiep-vu.md (5)

- [ ] L39: - QT4. Đặt lịch bị khóa sau hạn (mở khóa: menu *Mở khóa đặt lịch họp*) ❓ quy tắc khóa.
- [ ] L40: - QT5. Biên bản phải ký (`requestForSigningMeetingMinutes`) trước khi đóng kết luận ❓.
- [ ] L44: 1. eCabinet (phòng họp không giấy) là phân hệ mobile/tablet riêng hay tab trong web?
- [ ] L45: 2. Họp trực tuyến Cisco/cospace còn dùng?
- [ ] L46: 3. "Báo cáo quân số" thuộc họp hay KPI?

## hop/vi-du-mau.md (1)

- [ ] L6: | Duyệt / từ chối / hủy lịch có kiểm quyền | gen-1 `MettingWeek.approveCalendar`, `rejectCalendar`, `cancelCalendar`, `checkPermisionCalendar` ← `MeetingBusiness` ← `vm/meeting/*Approve*VM` ❓ |

## kpi-danh-gia/nghiep-vu.md (5)

- [ ] L19: - `KpiPortalController` (`/api/kpi-portal`): CRUD chỉ số hiển thị cổng KPI (`kpi.status`: đang nháp → chờ phản hồi → chốt đánh giá); `system-downtime-log` (thời gian hệ thống ngừng, trừ vào KPI vận hành ❓).
- [ ] L29: `get-usage-statistics` (mức độ dùng hệ thống), `get-document-in/out-statistics`, `-ranking`, `get-meeting-schedule-statistics`, `get-mission-statistics`, `get-document-statistics-by-org`; cây đơn vị `vhr-org/get-list-child-all-level`. Web `summaryUsageReport/*`, `StatisticsReportBusiness`. Nguồn cho báo cáo lãnh đạo tỉnh ❓.
- [ ] L32: 1. KPI ở đây là KPI vận hành hệ thống (số văn bản, đúng hạn) hay KPI nhân sự? Ai xem cổng KPI?
- [ ] L33: 2. Chấm điểm thi đua theo kỳ nào (tháng/quý/năm) và có liên kết với KI cá nhân?
- [ ] L34: 3. Báo cáo định kỳ cá nhân có thay phiếu đánh giá cuối tháng của `cong-viec` không, hay song song?

## ky-so/nghiep-vu.md (4)

- [ ] L13: | Ký tự động | `AutoDigitalSign` (`AUTO_DIGSIG_TRANSACTION`) | ❓ dùng cho loại văn bản nào |
- [ ] L35: 1. Phương thức nào đang dùng thực tế ở Khánh Hòa (USB token? CloudCA của nhà cung cấp nào?).
- [ ] L36: 2. Ký tự động áp dụng ở đâu?
- [ ] L37: 3. `DocumentSignKNTCService` / `AuthenticationKntcController` (KNTC = khiếu nại tố cáo?) là tích hợp với hệ thống nào?

## ky-so/vi-du-mau.md (2)

- [ ] L6: | Popup ký USB token | `requisition/signUsbToken.zul` + VM ký trong `vm/requisition` (`RequisitionSignVM` ❓) → `RequisitionBusiness` `Sign.SignSoftHashMutiFile` → `textAction.updateDatabaseSign` |
- [ ] L12: | Quản lý chứng thư người dùng | `CertManagementAction.*` + `vm/config` ❓ zul (menu Ký điện tử) |

## lich-nhac-viec/dac-thu.md (3)

- [ ] L3: - **Nhắc việc = mẫu gen-2 chuẩn nhất** (xem `_chung/cach-lam-chuan/them-tinh-nang-moi.md`): `ReminderController` (`/reminders`, 16 endpoint, không prefix `/api`) → `ReminderServiceImpl` (~1.800 dòng, `@Transactional`) → `ReminderRepositoryJPA` + `ReminderRepositoryImpl` (SQL text block qua `BaseRepositoryImpl`) → `REMINDER*`. Web `vm/reminder/*` (6 VM) + `ReminderBusiness` (18 hàm). Không có gen-1 tương đương. `reminders.cancelReply`, `getReminderReport`, `updateNewReplyAssignee` web gọi nhưng BE không có → ❓ chưa làm hoặc đã bỏ.
- [ ] L7: - Thông báo (`NotificationAction`) và SMS chặn (`SmsInterceptAction`) là gen-1; SMS chặn theo đơn vị mới thêm ở gen-2 (`SMSInterceptController`). `api.smsIntercept.getListModulInterceptSmsOfOrgId.` (dấu chấm cuối) không nối được endpoint ❓ bug tên.
- [ ] L9: - Bảng `ALERT` (web entity `Alert`) là cơ chế cảnh báo cũ ❓ còn dùng.

## lich-nhac-viec/nghiep-vu.md (4)

- [ ] L57: Lãnh đạo/trợ lý tạo "văn bản nắm tình hình" (không qua văn thư), gửi cho nhóm lãnh đạo (`get-group-doc-lead-type`, `DOCUMENT_LEAD_TYPE`), có file mật (`get-list-file-encrypt-map`, `get-permission-view-file`), đếm đã đọc (`count-read`, `mark-as-read`), phân quyền nhà cung cấp (`insert-permission-for-supplier`) ❓. Liên quan `document.processType = situation` (Nắm tình hình) trong văn bản đến.
- [ ] L63: 1. Nhắc việc có SMS/thông báo đẩy khi gửi và khi nhắc lại không? Cấu hình ở đâu?
- [ ] L64: 2. `FOLLOWER_TYPE` có những giá trị nào (người tạo / lãnh đạo / theo dõi thêm)?
- [ ] L65: 3. "Nắm tình hình" có phải là tính năng dành riêng cho lãnh đạo tỉnh (Khánh Hòa) không?

## nhiem-vu/dac-thu.md (2)

- [ ] L5: - `MissionController` và `MissionDashboardController` có **cùng bộ endpoint** (`get-assign-mission-charts`, `search-mission`, `sync-mission`…) dưới 2 base — nghi ngờ trùng lặp/di chuyển dở ❓; web gọi `api.mission_dashboard.*`.
- [ ] L6: - `api.work-group-action.unBlock` web gọi nhưng không có endpoint (BE có `api.work-group.block`) ❓.

## nhiem-vu/nghiep-vu.md (6)

- [ ] L54: - QT1. Nhiệm vụ BGĐ giao phải được chỉ huy phê duyệt trước khi chạy (`approvedMissionByCommander`) ❓ áp dụng loại nào.
- [ ] L56: - QT3. Đóng nhiệm vụ cha khi con chưa xong bị chặn ❓.
- [ ] L58: - QT5. Đồng bộ nhiệm vụ với hệ thống khác (`sync-mission`, `count-sync-mission`) ❓ hệ thống nào.
- [ ] L61: 1. `WORK_GROUP` (nhóm công việc) là nhóm theo dõi nhiệm vụ hay nhóm người dùng?
- [ ] L62: 2. "Thỏa thuận hợp tác" (`agreement`) là nghiệp vụ riêng của khách hàng nào? Có còn dùng?
- [ ] L63: 3. Sự khác nhau giữa `/api/mission` và `/api/mission_dashboard` (endpoint trùng tên)?

## nhiem-vu/vi-du-mau.md (1)

- [ ] L5: | Biểu đồ dashboard theo đơn vị/người (gen-2) | `MissionDashboardController.get-assign-mission-charts`, `get-perform-mission-charts`, `count-*` ← `MissionChartBusiness` ← `vm/mission/*Chart*VM` ❓ |

## phieu-trinh/nghiep-vu.md (7)

- [ ] L3: > Phiếu trình = văn bản nội bộ trình lãnh đạo xem xét/phê duyệt một nội dung (đề xuất, xin chủ trương), có luồng ký riêng, **không phải văn bản đi** nhưng liên kết chặt với dự thảo văn bản đi. Bảng `SUBMISSION_FORM`, `SUBMISSION_FORWARD`, `SUBMISSION_MAP` ❓, file ký riêng. Chạy trên **BE gen-2** `SubmissionManagerController` (`/api/submission-manager`, 41 endpoint) — mẫu gen-2 tốt.
- [ ] L45: | Dự thảo **đính kèm phiếu trình đã hoàn thành** | Trong `requisition_add` chọn phiếu trình `completed` | Phiếu trình là sở cứ; kiểm tra `api.brief-detail.check-text-doc-for-submitting` ❓ |
- [ ] L53: - QT4. Đếm trang giấy để thống kê in ấn (`update-num-page`) ❓ mục đích.
- [ ] L58: Khác phiếu trình: là **khó khăn vướng mắc** gửi lên cấp trên (`request.status`: chưa gửi → đã gửi → đang giải quyết → đã giải quyết / đã chuyển cấp trên / đã đóng; `request.action`: giao đơn vị, giao cá nhân, tự giải quyết, gửi lên cấp trên, đóng, từ chối kết quả) và có thể **sinh nhiệm vụ** (`requestProcess.action = tao.cong.viec`). Web `request/*.zul` (12) + `vm/request/*`; cấu hình người nhận kiến nghị `ProposalBusiness` (`requestAction.*RequestEmpConfig`, menu *Cấu hình cá nhân nhận kiến nghị*). ❓ Nếu team coi đây là phân hệ riêng thì tách folder `kien-nghi`.
- [ ] L61: 1. Phiếu trình có nhiều cấp ký cố định (phòng → đơn vị) hay theo luồng `FLOW`?
- [ ] L62: 2. `update-all-submission-7939827832452673672323443432323` là endpoint migrate dữ liệu một lần? Có nên xóa?
- [ ] L63: 3. Phiếu trình "ký luôn dự thảo": chữ ký đặt lên file dự thảo hay chỉ đổi trạng thái?

## phieu-trinh/vi-du-mau.md (1)

- [ ] L8: | Tạo/sửa có đính kèm dự thảo | `submissionForm_add.zul` (❓ VM: `SubmissionDetailVM`) | `submission-form/create-or-update`, `submit`, `check-submission-attachments-for-submitting`, `submission-form-by-text-id` |

## tai-lieu-mau/dac-thu.md (1)

- [ ] L6: - `TemplateFilter` (web `http/`) xử lý URL mẫu ❓.

## tai-lieu-mau/nghiep-vu.md (3)

- [ ] L15: - QT1. Mẫu có thứ tự hiển thị (`updateIndexTemplate`) và thuộc đơn vị/loại ❓.
- [ ] L20: 1. "Cấu hình thư viện" (menu quản trị) cấu hình cây thư mục hay quyền xem?
- [ ] L21: 2. Mẫu văn bản (docx) có tích hợp WOPI để soạn thảo online không (`tich-hop`)?

## tich-hop/nghiep-vu.md (5)

- [ ] L14: | **KNTC** (khiếu nại tố cáo?) | Ký số & đăng nhập cho hệ thống KNTC | `DocumentSignKNTCService`, `AuthenticationKntcController`, `BaseResponseKNTC` ❓ |
- [ ] L20: - QT1. Dữ liệu tổ chức/nhân sự **chỉ nhập từ VHR**; sửa tay trong VOffice sẽ bị đồng bộ ghi đè ❓ (xác nhận).
- [ ] L26: 1. Ở Khánh Hòa, HR nguồn là VHR Viettel hay hệ thống cán bộ công chức tỉnh?
- [ ] L27: 2. Ứng dụng ngoài nào đang dùng `/ext-*`?
- [ ] L28: 3. ViettelPay / VContract / CM còn hoạt động hay là di sản Viettel?

## van-ban/den/dac-thu.md (1)

- [ ] L30: 8. `12032026_yc_16_tacdong.sql` — một yêu cầu (YC16) có "tác động" DB gần đây ❓ nội dung gì; đọc file trước khi đụng bảng liên quan.

## van-ban/den/nghiep-vu.md (4)

- [ ] L80: - QT2. Chỉ **chủ trì** được hoàn thành/đóng; phối hợp và để biết không đóng được (❓ xác nhận trong `updateStatusDocumentInStaff`).
- [ ] L88: 1. Bút phê có bắt buộc với mọi văn bản đến hay tuỳ loại (`documentStatus = van.ban.khong.can.xin.y.kien`)?
- [ ] L89: 2. Ai được "trả lại nơi gửi" và có thông báo ngược qua liên thông không?
- [ ] L90: 4. Trạng thái `needAnswer` do ai đặt: nơi gửi khi ban hành hay lãnh đạo khi bút phê?

## van-ban/den/vi-du-mau.md (2)

- [ ] L29: `DocLeaderCommentController` (`/api/doc-leader-comment/save-doc-leader-comment`, `get-doc-leader-comments`) ← `DocumentBusiness` ← VM chi tiết (`DocumentViewDetailVM`) / popup ❓ zul tên. Mẫu cho: ý kiến chỉ đạo, ghi chú của lãnh đạo lên đối tượng bất kỳ.
- [ ] L37: `document/inputDoc/inputDoc_add.zul`, `doc_in_add.zul`, `inputDocEdit.zul` + VM tương ứng trong `vm/document` (`InputDocument*VM` ❓ tên) → `DocumentBusiness` → gen-1 `DocumentAction.AddDocument`, `AddDocumentAttachment`, `GetRegisterNumberIndex`; gen-2 kiểm tra trùng `api.doc-in.is-duplicated-register-number`, `list-exist-document-by-textbook-and-register`.

## van-ban/di/dac-thu.md (2)

- [ ] L22: 8. `textAction.checkShowTransferGiveAdvice.` (có dấu chấm cuối) và vài key khác không nối được endpoint — có thể là bug tên hàm hoặc endpoint đã bị xóa ❓.
- [ ] L23: 9. Ký đối tác ngoài (`listPartnerSign`, `TextPartnerDAO`) là nhánh riêng, ít dùng ❓.

## van-ban/di/nghiep-vu.md (6)

- [ ] L90: - QT6. Hủy ban hành cần quyền (`checkPermissionRollBack`) và ghi lý do; văn bản đến đã phát sinh ở đơn vị nhận phải được thu hồi ❓ (cần xác nhận cơ chế).
- [ ] L116: 1. Hủy ban hành có tự thu hồi văn bản đến ở đơn vị nhận không, hay chỉ đổi trạng thái?
- [ ] L117: 2. `TYPE_VBDT_V2 = 12` — màn dự thảo bản 2 khác gì bản 1?
- [ ] L118: 3. Ký song song (`STATE_SIGN_PRALLEL`) áp dụng cho bước nào (ký nháy? nhận xét?).
- [ ] L119: 4. "Văn bản phê duyệt" (`VBPD = 7`, menu *Công văn phê duyệt*) là gì so với ký duyệt?
- [ ] L120: 5. Tự động ban hành (`AUTO_PROMULGATE`) cấu hình ở đâu, áp dụng loại văn bản nào?

## van-ban/di/vi-du-mau.md (3)

- [ ] L13: | BE repo/entity | `repositories/jpa/*Text*RepositoryJPA`, `entities/TextEntity`, `TextProcessEntity` ❓ tên chính xác — grep `@Table(name = "TEXT_PROCESS")` |
- [ ] L27: | Business | `RequisitionBusiness.rejectPublishDocument` → gen-1 `textAction.rejectSignDocument` / `DocumentAction.cancelPublish` ❓ (xem ban-do mục 2) |
- [ ] L37: `requisition/signUsbToken.zul` + `RequisitionSignVM` ❓ (VM thật trong `vm/requisition`) → `RequisitionBusiness` gọi `Sign.SignSoftHashMutiFile` / `Sign.SignCloudCA` / `Sign.SignTextByCASIM` → cập nhật `textAction.updateDatabaseSign`. Chi tiết ở `ky-so/vi-du-mau.md`.

## van-ban/lien-thong/dac-thu.md (2)

- [ ] L3: - Điểm vào từ ngoài là **gen-2 webhook** `VOConnectProcessorController` (`/api/hook`: `send-document`, `update-status-document`, `send-mission`, `revoke-document`) → `VOConnectProcessorService`(Impl). Sửa ở đây ảnh hưởng đối tác ngoài — cần test với trục giả lập (`postman/` có collection ❓).
- [ ] L6: - `document/goverment/govermentDocument.zul` + `GovermentDocumentVM`, `TransferGovermentDocumentVM` không gọi Business/facade nào → khả năng là màn chết mềm (VM tồn tại nhưng không còn dữ liệu) ❓.

## van-ban/lien-thong/nghiep-vu.md (6)

- [ ] L12: | Văn bản từ VPCP | `document/goverment/govermentDocument.zul`, `transferGovermentDocument.zul` (VM không gọi dữ liệu — ❓ còn dùng), menu *Văn bản từ VPCP*, *Báo cáo VP CP* | |
- [ ] L20: - QT3. Thu hồi văn bản đã gửi liên thông = `revoke-document` + hủy ban hành ở `van-ban/di` ❓ thứ tự.
- [ ] L21: - QT4. Webhook `/api/hook/*` phải nằm trong `jwtIgnoreConfig` hoặc dùng xác thực riêng ❓ (kiểm tra `WebSecurityConfig`).
- [ ] L24: 1. Trục đang kết nối là trục LGSP tỉnh Khánh Hòa hay trục văn bản quốc gia? Chuẩn edXML phiên bản nào?
- [ ] L25: 2. `goverment/*` (VPCP) còn hoạt động hay là di sản Viettel?
- [ ] L26: 3. `merge/` có liên quan tới migrate dữ liệu không?

## van-ban/luong-xu-ly/dac-thu.md (1)

- [ ] L6: - Bẫy: `api.flow-manager.doc-out` được web gọi nhưng **không có endpoint** (❓ đã bỏ hoặc chưa làm) — xem `_chung/ban-do-tong/web-goi-be.md`.

## van-ban/luong-xu-ly/nghiep-vu.md (5)

- [ ] L10: | Nhóm luồng | `FlowGroupTypeEntity`, `flow-group-type/get-all` | Phân loại: theo loại văn bản, theo đơn vị ❓ |
- [ ] L29: - QT2. Sao chép luồng (`flow/copy`) để tạo luồng mới cho đơn vị khác — không sửa luồng đang dùng nếu văn bản đang chạy trên đó ❓ (cần xác nhận có snapshot hay tham chiếu sống).
- [ ] L31: - QT4. Luồng tập đoàn > đơn vị > cá nhân (`requisitionFlow.requisitionFlowMap`) ❓ thứ tự ưu tiên.
- [ ] L43: 1. Luồng ký văn bản đi có lấy hoàn toàn từ `FLOW/NODE` hay vẫn còn bảng `REQUISITION_FLOW` cũ song song?
- [ ] L44: 2. Khi cấu hình luồng thay đổi, văn bản đang trình có bị ảnh hưởng không?

## van-ban/luong-xu-ly/vi-du-mau.md (1)

- [ ] L5: | CRUD cấu hình có lịch sử, sao chép, bật/tắt | `FlowManagerController`: `flow/create-or-update`, `flow/copy`, `toggle-active-flow`, `delete-flow`, `get-flow-histories` ← `FlowBusiness` ← `vm/flow/FlowVM` ❓ tên chính xác |

## van-ban/quan-ly-chung/dac-thu.md (1)

- [ ] L5: - Tìm kiếm: 2 engine (Solr gen-1 `SolrSearchResource`, Elasticsearch `ElasticDocument*`/`els_query/`) ❓ cái nào đang sản xuất; `application-prod.properties` có `elasticsearch.host`.

## van-ban/quan-ly-chung/nghiep-vu.md (3)

- [ ] L15: | **Lịch sử văn bản** | | gen-2 `document-history-log/search` (`DOCUMENT_HISTORY_LOG`), `getListDocumentHistory`, `ReportdocumentTransferHistory`, `DocumentCopyHistory` (`document-copy/check-permission` — sao y ❓) |
- [ ] L27: - QT2. Loại văn bản có thể riêng đơn vị hoặc dùng chung; xóa loại đang dùng bị chặn ❓.
- [ ] L28: - QT3. Tìm toàn văn phụ thuộc index (Solr/ES) — văn bản mới ban hành phải được index (`indexEmployee` cho người; văn bản qua `ElasticDocument`) ❓ đồng bộ ra sao.

## van-ban/quan-ly-chung/vi-du-mau.md (1)

- [ ] L5: | Danh mục có cấp phát cho đơn vị / chuyển dùng chung (gen-2) | `DocumentTypeController` (`create-doc-type-org`, `granted-doc-type-to-orgs`, `convert-doc-type-to-common`, `get-by-organization`) ← `DocumentTypeBusiness` ← `vm/document` ❓ `DocumentTypeVM` / `document_type/document_type.zul` |

## van-ban/so-van-ban/dac-thu.md (1)

- [ ] L3: - gen-1 `TextBookAction` (`/textBookAction`) → `controler/*` → `TextBookDAO`; gen-2 `TextBookManagerController` (`/api/text-book`) mới, ít hàm ❓ web đã gọi chưa (xem `ban-do.md` mục 2).

## van-ban/so-van-ban/nghiep-vu.md (3)

- [ ] L16: - QT4. Cấp số có hàng chờ (`WaitingNumberBookEntity`, `VBCCS` "chờ cấp số") — tránh trùng khi nhiều người cấp cùng lúc ❓ cơ chế khóa.
- [ ] L20: 1. Đánh số lại đầu năm thực hiện thế nào (tự động theo năm hay tạo sổ mới)?
- [ ] L21: 2. Số văn bản có dạng mẫu (vd. `123/UBND-VP`) sinh từ đâu — sổ hay loại văn bản?

## _chung/kien-truc-tong-the.md (1)

- [ ] L111: 3. `merge/` ở root workspace là bản gộp cũ — không phải nguồn sự thật. ❓ cần xác nhận mục đích.

## _chung/quy-uoc.md (2)

- [ ] L15: | SQL migration | `backend2.0/backendvoffice/sql/DDMMYYYY_mo_ta.sql` | Tạo SEQUENCE + TABLE + comment cột; dữ liệu SYS_MENU nếu có màn hình mới | Chưa có Flyway/Liquibase — chạy tay theo môi trường ❓ |
- [ ] L47: - Web: Maven, `mvnw`, Java 8, đóng gói WAR/Jar chạy Tomcat nhúng ❓; Jenkinsfile.groovy; Dockerfile.

## _chung/thuat-ngu.md (1)

- [ ] L43: | Nhóm công việc | `WORK_GROUP*`, `workGroupTree` | ❓ nhóm theo dõi nhiệm vụ chung |

## _chung/cach-lam-chuan/them-man-hinh-web.md (3)

- [ ] L101: | Gán menu cho vai trò | `SYS_ROLE` ↔ menu ❓ (bảng map — hỏi admin) | |
- [ ] L102: | Nhãn đa ngôn ngữ | `common_voffice_vi.properties` (+ `_en`), key `voffice.<domain>.label.*` | reminder hiện hard-code tiếng Việt ❓ |
- [ ] L113: - `scan.py` thấy zul → VM → Business → endpoint nối đủ (không ❓ trong `ban-do.md`).

## _chung/cach-lam-chuan/them-tinh-nang-moi.md (2)

- [ ] L55: - [ ] Nhãn: thêm key `voffice.<domain>.label.*` vào `common_voffice_vi.properties` + `_en` (reminder hiện đang hard-code tiếng Việt trong zul — ❓ team chấp nhận hay yêu cầu i18n?).
- [ ] L61: - [ ] Menu: dòng SYS_MENU (bước 1) + gán vào vai trò (SYS_ROLE ↔ menu) ❓ cách gán — hỏi admin/DBA.

## _chung/cach-lam-chuan/them-truong-du-lieu.md (2)

- [ ] L16: | 8 | Elasticsearch/Solr | Nếu cột cần tìm kiếm toàn văn: `ElasticDocument*`, `els_query/`, `SolrSearch*` | ❓ quy trình reindex |
- [ ] L33: Pattern sẵn có: `rejectPublish.zul` + `RejectPublishVM` (từ chối ban hành có lý do) → BE `textAction.rejectPublish` ❓ tên hàm — xem `requisition/ban-do`. Làm tương tự: popup nhập lý do → Business → endpoint → lưu vào bảng lịch sử (`TEXT_PROCESS_HISTORY`, `DOCUMENT_HISTORY_LOG`, `REMINDER_HISTORY` là các bảng lịch sử đang có) thay vì cột đơn lẻ, để có lịch sử nhiều lần.
