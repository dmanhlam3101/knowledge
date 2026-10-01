# Thuật ngữ — tên trong code ↔ tên nghiệp vụ

Bảng này giải quyết 80% nhầm lẫn khi đọc code VOKhanhHoa. Cột "Trong code" liệt kê tên bảng / class / package thật.

## Văn bản

| Nghiệp vụ | Trong code | Ghi chú |
|---|---|---|
| **Văn bản dự thảo / trình ký** (chưa ban hành) | `TEXT`, `TextEntity`, `textAction`, `TextController` + `DocumentSignController` (gen-1), `TextDAO`, `/api/text-process`; web: màn **Dự thảo** `documentDraft/documentDraft.zul` + `DocumentDraftVM` (menu XỬ LÝ CÔNG VIỆC), `requisition/*`, `RequisitionVM`, `RequisitionViewDetailVM`, `RequisitionBusiness` (sửa 2026-09-30: `documentDraft/*` KHÔNG chết — chỉ các popup con trỏ `vm.admin.requisition.*` là chết; web không gọi `/api/text-draft`). Chi tiết: `xu-ly-cong-viec/nghiep-vu.md` | "Text" là tên cổ của văn bản đang soạn. `requisition` = trình ký. `vbdt` = văn bản dự thảo, `vbtk` = văn bản trình ký, `vbkn` = ký nháy, `vbnx` = nhận xét, `vbkd` = ký duyệt, `vbxd` = xét duyệt (văn thư), `vbbh` = ban hành |
| **Văn bản đã ban hành / văn bản đến** (có số) | `DOCUMENT`, `DocumentAction`, `DocumentController` (gen-1 logic), `DocumentDAO`, `/api/doc`, `/api/doc-in`, `/api/doc-out`; web `document/*`, `DocumentBusiness` | Ban hành = từ `TEXT` sinh bản ghi `DOCUMENT`. Văn bản đến của đơn vị này có thể là văn bản đi của đơn vị khác (liên thông nội bộ) |
| Văn bản đến | `DOCUMENT_IN*`, `DocIn`, `DocumentIn`, `inputDoc`, `DocumentSearchReceive`, `DOCUMENT_IN_STAFF` (ai được giao xử lý) | |
| Văn bản đi | `DocOut`, `documentPublish` (ban hành), `issueDocument` (cấp số), `bookDispatch` | |
| Trích yếu | `title` (TEXT/DOCUMENT) | Không phải "tiêu đề" file |
| Số văn bản / số đi / số đến | `CODE`, `issue number`, `WaitingNumberBookEntity` (chờ cấp số) | Cấp số theo **sổ văn bản** (`TEXT_BOOK`) |
| Sổ văn bản | `TEXT_BOOK`, `textBookAction`, `TextBookManagerController`, web `bookDoc`, `textBook` | Mỗi đơn vị có sổ đến/đi, đánh số theo năm |
| Luồng ký / luồng xử lý | `FLOW*`, `NODE*`, `FlowManager`, `requisitionFlow`, `RequisitionFlow` (cá nhân / đơn vị / tập đoàn) | Cấu hình trong DB, không hard-code |
| Bút phê (lãnh đạo cho ý kiến trên văn bản đến) | `DocLeaderComment`, `document.documentStatus`: *chờ lãnh đạo bút phê / đã phê duyệt / bị từ chối* | |
| Chủ trì / phối hợp / nhận để biết / nắm tình hình | `document.processType`: `main` / `coordinate` / `toKnow`,`receiveToKnow` / `situation`; `document.transfer`: `sendTo` / `carbonCopy` / `toKnow` | Vai trò của đơn vị/người nhận khi được chuyển văn bản |
| Hạn xử lý | `DocumentProcessTerm`, `documentProcessTermConfig`, `document.status`: *sắp đến hạn / quá hạn* | Cấu hình hạn theo loại văn bản |
| Liên thông | `CONNECT_DOCUMENT`, `ConnectDocument`, `VOConnect`, `/api/hook`, `InObject*`, `InternalDoc*` (XML gửi/nhận), `goverment` (VPCP) | Gửi/nhận văn bản với cơ quan ngoài qua trục |
| Công khai văn bản | `document.documentPublish`: *chưa/đã/hủy công khai*; `DocumentPublicStatus` | Khác với "ban hành" |
| Bàn giao văn bản | `DocumentHandover`, `handoverDoc` | Chuyển toàn bộ văn bản khi người xử lý nghỉ/chuyển công tác |

## Ký

| Nghiệp vụ | Trong code |
|---|---|
| Ký nháy (người phụ trách soát trước khi lãnh đạo ký) | `signatureType = 2`, `PENDING_INITIALS(5)`, `vbkn`, `requisitionProcess.type = ky.nhay` |
| Ký duyệt (lãnh đạo ký chính thức) | `signatureType = 3`, `SIGNED(3)`, `vbkd`, `type = ky.duyet` |
| Xét duyệt / trình duyệt (văn thư kiểm tra thể thức trước/sau ký) | `signatureType = 1`, `WAIT_REVIEW/REVIEWED/REJECT_REVIEW`, `vbxd`, `type = xet.duyet` |
| Nhận xét / nhận xét bổ sung (cho ý kiến, không ký) | `vbnx`, `type = nhan.xet / nhan.xet.bo.sung`, `requisitionComment.state` |
| Ký số USB token / CloudCA / ký ảnh | `signUsbToken.zul`, `CloudCAAction`, `P12CertAction`, `ImageSign`, `StaffImageSign`, `AutoDigitalSign` |
| Đóng dấu | `menu.kydientu.van.ban.dong.dau`, `askForSeal` |

## Công việc

| Nghiệp vụ | Trong code | Phân biệt |
|---|---|---|
| **Nhiệm vụ** (mission) | `MISSION*`, `missionAction`, `/api/mission`, web `mission/*` (100 zul) | Của cá nhân/đơn vị, giao từ BGĐ/đơn vị/định hướng/biên bản họp… **Không gắn văn bản** |
| **Công việc** (task) | `TASK*`, `taskAction`, `TaskService`, web `task/*` | Cá nhân, **gắn văn bản** (`OBJECT_TYPE_TASK = 1`), có phiếu giao việc đầu tháng / đánh giá cuối tháng, KI |
| Phiếu trình | `SUBMISSION_FORM`, `submissionForm/*`, `SubmissionFormBusiness`, `/api/submission-manager`, `SubmissionForward` | Trình lãnh đạo phê duyệt một nội dung; có thể đính kèm/được đính kèm vào dự thảo |
| Yêu cầu / kiến nghị đề xuất (khó khăn vướng mắc) | `REQUEST`, `requestAction`, `request.status/action`, `ResovleIssue`, menu KHÓ KHĂN VƯỚNG MẮC | Gửi lên cấp trên giải quyết, có thể sinh nhiệm vụ |
| Nhóm công việc | `WORK_GROUP*`, `workGroupTree` | ❓ nhóm theo dõi nhiệm vụ chung |
| Định hướng | `ORIENTATION`, `orientation/*` | Nguồn sinh nhiệm vụ (`ORIENTATION_MISSION_SOURCE_TYPE`) |
| Nhắc việc (MỚI) | `REMINDER`, `REMINDER_REPLY`, `REMINDER_FOLLOWER`, `REMINDER_DOCUMENT_RELATION`, `REMINDER_HISTORY`, `/reminders`, web `reminder/*` | Lãnh đạo nhắc đơn vị về văn bản/việc; đơn vị trả lời; có theo dõi (follower) |

## Tổ chức & người dùng

| Nghiệp vụ | Trong code |
|---|---|
| Đơn vị | `SYS_ORGANIZATION`, `VHR_ORG` (đồng bộ từ VHR), `ORG_*`; web `ISysOrganization` |
| Người dùng / nhân viên | `SYS_USER`, `STAFF`, `VHR_EMPLOYEE`, `EmployeeEntity`; `employeeId` là id dùng trong JWT (`CoreUtils.getUserId()`) |
| Vai trò | `SYS_ROLE` (id cố định: `SYS_ROLE_VT` văn thư, `SYS_ROLE_LDDV` lãnh đạo đơn vị, `SYS_ROLE_TTDV`, `SYS_ROLE_NV` nhân viên, `SYS_ROLE_TL` trợ lý, `SYS_ROLE_ADMIN`… trong gen-1 `Constants`) |
| Nhóm chuyên viên | `CV_GROUP`, `CvGroupAction` |
| VPS | package `com.viettel.vps` = phân hệ quản trị hệ thống (user, role, menu, resource, operation) |

## Khác

| Từ | Nghĩa |
|---|---|
| `DEL_FLAG` | Xóa mềm: 0 hoạt động, 1 đã xóa. Hầu hết bảng dùng |
| `isSecurity` | Tham số gen-1: request có mã hóa AES/RSA hay không |
| `serviceConnection` | Kết nối web→BE gắn với HttpSession (cookie + JWT) |
| `Delegate.getService(I*.class)` | Lấy facade legacy trong web |
| `LookupUtil.showLookup/showDialog` | Mở popup chọn dữ liệu (ZK) |
| `EventQueues.lookup(...)` | Cơ chế reload giữa các VM ZK (ví dụ `EVENT_QUEUE_HOME_PAGE`) |
| `CODE_MASTER` | Danh mục động (trạng thái, loại) đọc bằng key `code.*` |
| `ToolGen` | Bộ sinh code gen-2 (`voffice-gencode`), comment "Autogen class" |
