# Họp — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phân hệ họp **phần lớn là legacy** (web ghi DB qua facade) — **không copy** cách ghi lịch họp của MVM / MWVM cho tính năng mới; các mẫu dưới đây chọn phần đáng dùng lại.

## Mẫu 1 — Tính năng gen-2 có máy trạng thái và kiểm chặn theo trạng thái: **Biểu quyết** (`/api/vote`)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Controller | `BE2/controller/VoteController.java` (8 endpoint, mỗi endpoint vài dòng, lấy người dùng `CoreUtils.getUserId()`) | Controller mỏng |
| Hằng trạng thái | `C2:131-149` (`Vote.Status` 0 / 1 / 2 / 3 có Javadoc) | Gom trạng thái một chỗ |
| Service | VSI `insertVote` :52-130 (kiểm trùng nội dung phương án, chặn sửa khi đã gửi / đã hủy / đã hết giờ bằng mã lỗi riêng `ErrorApp.VOTE_*`), `sendVote` :291-316, `answerVote` :181-230, `cancelVote` :440-461, `deleteVote` :518-545; trạng thái "kết thúc" tính từ `END_TIME` khi đọc (`isEndedVote` :166-168); nút hiện theo trạng thái trả về cùng dữ liệu (`updateVisibleStatus` :475-497) | Mỗi thao tác: tải → kiểm trạng thái nguồn → `throw new VofficeException(mã lỗi cụ thể)` → ghi |
| Kiểm quyền theo dữ liệu | `checkVote` :584-607 — phân quyền dữ liệu `MEET_ATTENDWEB_DATA` (`PermissionDataService`) hoặc là thành phần | Quyền ở BE theo vai trò / thành phần |
| Repository / bảng | `Vote*RepositoryJPA`; bảng có **FK thật** `VOTE → MEETING`, `VOTE_QUESTION → VOTE`, … (DB DEV) | — |

**Lưu ý**: chưa có màn web gọi; không có code ghi `STATUS = 2` (Hoàn thành) — khi copy phải định nghĩa rõ đường chuyển tới mọi trạng thái đã khai.

## Mẫu 2 — Đồng bộ một bản ghi sang hệ thống ngoài, có tạo / cập nhật / hủy theo trạng thái: **eCabinet**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Web gọi | `MEB.createOrUpdateEcabinetConference` :2467-2469, `cancelEcabinetConference` :2471-2473 (gọi sau mỗi lần lưu / duyệt / phân công — MVM:5034, MWVM:2653, 2788) | Gọi đồng bộ sau thao tác, không chặn luồng chính |
| Controller | MTC `save-ecabinet-conference/{meetingId}`, `cancel-ecabinet-conference/{meetingId}`, `get-ecabinet-conference/{meetingId}` | Endpoint theo id, idempotent |
| Service | MSI `createOrUpdateEcabinetConference` :2887-3039: lấy token (`PerformanceTracker.track("EXT.…")`) → rẽ nhánh theo trạng thái nguồn (chờ duyệt → hủy; không có phòng ánh xạ → hủy; đã duyệt → tạo mới nếu chưa có mã ngoài, cập nhật nếu đã có) → lưu mã ngoài `ID_ECABINET`; tài liệu đẩy kèm quyền xem (`getMeetingFileToCreate` :3041-3120) và lưu ánh xạ `FILE_ECABINET` | Khung "một hàm đồng bộ cho mọi trạng thái" + đo thời gian gọi ngoài |
| Client ngoài | ESI (`@Value("${ecabinet.endpoint}")`, `createConference` :70, `updateConference` :83, `createMedia` :91, `cancelConference` :109) | Cấu hình endpoint qua properties |

**Không copy**: thứ tự `setIdEcabinet(null)` trước `setIdEcabinetBefore(...)` (`dac-thu.md` L10); `disableSslVerification` (ESI :393-415).

## Mẫu 3 — Nút theo trạng thái + vai trò, **tính lại trước khi thực hiện**: `MeetingActionBean`

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Bean quyền | `MeetingActionBean` (viewEdit, viewApproval, viewReject, viewCancel, viewDelete, viewAssign, viewSendEmail, viewSendSMS, viewCopy…) | Một đối tượng quyền cho mỗi dòng |
| Tính quyền | `MVU.viewActionWaitApproval` :3356-3388, `viewActionApproved` :3295-3348, `viewActionReject` :3264-3287, `viewActionCancel` :3251-3256 | Bảng trạng thái × vai trò × "còn hạn" |
| Kiểm lại ngay trước thao tác | `MVU.validateCurrentMeetingState` :3398-3474 (so bean trên màn với bean tính từ dữ liệu mới nhất); dùng ở MWVM :2556-2570, 2763-2772, 2868-2877, 4381-4389 | Chống thao tác trên dữ liệu cũ khi người khác vừa đổi trạng thái |
| zul | `ZUL/meeting/meetingWeek.zul:948-1036` (`visible="@load(each.actionBean.viewX)"`) | Binding nút theo bean |

**Lưu ý khi copy**: tính bean ở **một** chỗ — phân hệ họp đang có ba bản lệch nhau (`dac-thu.md` bẫy 2); quyền chỉ ở web là thiết kế chung (X1).

## Mẫu 4 — Danh mục cấu hình gen-1 đi qua Business (không legacy): **Cấu hình gán thành phần** (`MeetingConfigAdd`)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul / VM | `ZUL/meeting/meetingMemberConfig.zul` (+ `meetingMemberConfig/meetingMemberConfig_add.zul`, `_search.zul`, `meetingConfigAdd_detail.zul`) → `WEB/voffice/vm/meeting/MeetingMemberConfigVM.java` | Danh sách + form thêm / sửa |
| Business | `BIZ/MeetingConfigAddBusiness.java` — `search` :43-72, `searchAdvance` :74-99, `checkExists` :101-120, `insert` :122-134, `update` :136-156, `delete` :158-163 | Mỗi thao tác một khóa `MeetingConfigAdd.x` |
| Action / Controller | `BE1/action/MeetingConfigAddAction.java:17-79` → `BE1/controler/MeetingConfigAddController.java` (`checkExistMeetingConfig` :208, `insertMeetingConfigAdd` :336, `deleteMeetingConfigAdd` :547) | Kiểm trùng cấu hình trước khi thêm |
| DAO | `BE1/database/dao/meeting/MeetingConfigAddDAO.java` (`insert` :372, `deleteMeetingConfigAdd` :486, `checkExistMeetingConfig` :507, 550); con `MeetingOrgMemberAddDAO.java:37` (sequence `MEETING_ORG_MEMBER_ADD_SEQ`) | Cha – con với sequence |
| Dùng cấu hình | `listConfiguredMeetingOrgMembers` (DAO :590-665) → MDVM `setMeetingConfigAdd` :2269-2330 tự điền thành phần khi phân công | Cấu hình được "áp" ở màn nghiệp vụ, đánh dấu dòng tự điền (`isConfig`) |

## Không dùng làm mẫu

| Chỗ | Lý do |
|---|---|
| Lưu lịch họp `MVM.doSave` (:4751-5043) → `iMeeting.insertMeeting` / `updateMeeting` | Ghi DB thẳng từ web, nuốt lỗi, xóa – chèn lại thành phần, logic quyết định đơn vị duyệt chứa id cấu hình cứng (`dac-thu.md` bẫy 3, 6; L4) |
| Gửi SMS / email lịch `MVU.sendNoti*` | Web ghi thẳng `SMS_MASTER` / `MEETING_EMAIL`; với tính năng mới dùng cơ chế dùng chung ở `lich-nhac-viec` (LNV NV-13) |
| `MettingWeek.approveCalendar` và các endpoint ghi BE gen-1 | Không kiểm quyền người gọi (L1); là bản song song với web |
