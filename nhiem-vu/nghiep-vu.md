# Nhiệm vụ (mission) — nghiệp vụ

> **Nhiệm vụ của cá nhân / đơn vị, KHÔNG gắn văn bản** (khác `cong-viec` = task gắn văn bản). Menu QUẢN LÝ NHIỆM VỤ / NHIỆM VỤ ĐƠN VỊ / NHIỆM VỤ CÁ NHÂN. Bảng `MISSION*`, `MISSION_TEMPLATE*`, `MISSION_REPORT*`, `AGREEMENT*` (thỏa thuận hợp tác), `WORK_GROUP*`, `ORIENTATION`. Web `mission/*` (100 zul, phân hệ có nhiều màn nhất), `vm/mission/*` (37 VM). BE gen-1 `missionAction` (`MissionAction`), `MissionReport` (`MissionReportAction`), `agreementAction`; gen-2 `MissionController`/`MissionDashboardController` (`/api/mission`, `/api/mission_dashboard`), `MissionTemplateController`, `MissionReportResultController` (`/api/report-result`), `WorkGroupController`.

## 1. Actor

| Actor | Làm gì |
|---|---|
| Ban giám đốc / Chỉ huy (`TYPE_TTDV`, `SYS_ROLE_BCQS`) | Giao nhiệm vụ cho đơn vị (`addMission`, loại *Nhiệm vụ BGĐ giao*), phê duyệt (`approvedMissionByCommander`, `approveOrRejectProcess`), duyệt tự chấm điểm (menu *Phê duyệt tự chấm điểm*), phê duyệt đề xuất cộng điểm / gia hạn / đóng |
| Lãnh đạo đơn vị / phòng (`TYPE_LDPB`) | Đăng ký nhiệm vụ đơn vị (*Nhiệm vụ đơn vị đăng ký*), giao đi (*Nhiệm vụ giao đi*), giao cho cá nhân, chuyển (`Meeting.forwardMission`), đóng (`closeMission`), gia hạn (`checkExtendable`), tự chấm điểm (*Tự chấm điểm*), đề xuất cộng điểm |
| Người thực hiện (cá nhân/đơn vị) | Cập nhật tiến độ định kỳ (`frequencyUpdate`: theo ngày/tuần/tháng…), báo cáo (`MissionReport`, báo cáo ngày `report-daily`, báo cáo mật `send-confidential-report`), đề xuất đóng/gia hạn (`apprpveStatus.yeu.cau.dong / yeu.cau.gia.han`), nêu khó khăn (`typeMissionDifficult`, `statusProposeDifficult`) |
| Trợ lý chuyên hướng (`SYS_ROLE_TL`, `TLCT`) | Theo dõi, thống kê nhiệm vụ đơn vị (SMS `thong.ke.nhiem.vu.dv`), chấm điểm hộ (`tu.cham.diem` cho trợ lý), gán chuyên viên theo dõi báo cáo (`assign-specialist`) |
| Admin | Mẫu báo cáo nhiệm vụ (`mission-template`, khóa kết quả `lock-report-result`), chỉ tiêu (`MissionNorm`), nhóm công việc (`work-group`), định hướng (`Orientation`) |

## 2. Phân loại & nguồn

- **Loại** (`mission.typeMission`): Nhiệm vụ BGĐ giao / đơn vị đăng ký / giao đi / phối hợp / thực hiện / tôi tạo.
- **Nguồn** (`mission.sourceType`, `Constants.*_MISSION_SOURCE_TYPE`): theo văn bản (2), theo biên bản họp (3), theo định hướng (5), theo yêu cầu phòng KH (4), theo thỏa thuận hợp tác, theo văn bản Chính phủ/Quốc phòng, theo nhiệm vụ đơn vị, theo khó khăn vướng mắc, khác (1).
- **Định kỳ** (`mission.periodical`), tần suất cập nhật (`frequencyUpdate`), mức quan trọng (`levelImportant`), lĩnh vực (`mission.field`, 40 giá trị), nhóm (`missionGroup`).
- Nhiệm vụ cha–con (`getLastMissionProcessOfSubMissions`, `getListAddionalMission`), thứ tự (`SaveMissionOrder`), sinh văn bản từ danh sách nhiệm vụ (`CreateTextFromMissionList`).

## 3. Trạng thái (`Constants` gen-1 + `mission.status`)

| Mã | Tên | Hiển thị |
|---|---|---|
| 1 | `NOT_EXECUTE` | Chưa thực hiện |
| 2 | `EXECUTING` | Đang thực hiện (+ *Chậm tiến độ*, *Sắp đến hạn* tính theo hạn) |
| 3 | `COMPLETED` | Đã hoàn thành (người thực hiện báo) |
| 4 | `APPROVED` | Đã phê duyệt (chỉ huy xác nhận hoàn thành) |
| 5 | `REQUIRE_CLOSE` | Đề xuất đóng |
| 6 | `CLOSED` | Đã đóng / Đã kết thúc |
| — | | Đề xuất gia hạn → Đã gia hạn; Không thực hiện được; Nhận để biết |

Trạng thái quy trình phê duyệt (`missionProcess.statusApproved`), đánh giá (`missionRating.*`: đã chấm / khóa / đề xuất).

```mermaid
stateDiagram-v2
  [*] --> ChuaThucHien: giao / đăng ký (chờ phê duyệt của chỉ huy nếu cần)
  ChuaThucHien --> DangThucHien
  DangThucHien --> DangThucHien: cập nhật tiến độ định kỳ / báo cáo
  DangThucHien --> DeXuatGiaHan --> DangThucHien: duyệt gia hạn
  DangThucHien --> DaHoanThanh: người thực hiện báo xong
  DaHoanThanh --> DaPheDuyet: chỉ huy phê duyệt
  DangThucHien --> DeXuatDong --> DaDong: chỉ huy duyệt đóng
  DaPheDuyet --> DaDong
```

## 4. Đánh giá & KPI liên quan

Tự chấm điểm đơn vị → phê duyệt tự chấm → đề xuất cộng điểm → tổng hợp (`MissionReport.scoreReport`, `criteriaOrg`), SMS `ky.phieu.danh.gia`, `tu.cham.phe.duyet`. Phần tiêu chí/tỷ lệ nằm ở `kpi-danh-gia`.

## 5. Quy tắc

- QT1. Nhiệm vụ BGĐ giao phải được chỉ huy phê duyệt trước khi chạy (`approvedMissionByCommander`) ❓ áp dụng loại nào.
- QT2. Gia hạn phải qua đề xuất và duyệt; kiểm tra `checkExtendable`.
- QT3. Đóng nhiệm vụ cha khi con chưa xong bị chặn ❓.
- QT4. Báo cáo định kỳ theo mẫu (`mission-template`) và bị khóa sau hạn (`lock-report-result`).
- QT5. Đồng bộ nhiệm vụ với hệ thống khác (`sync-mission`, `count-sync-mission`) ❓ hệ thống nào.

## ❓
1. `WORK_GROUP` (nhóm công việc) là nhóm theo dõi nhiệm vụ hay nhóm người dùng?
2. "Thỏa thuận hợp tác" (`agreement`) là nghiệp vụ riêng của khách hàng nào? Có còn dùng?
3. Sự khác nhau giữa `/api/mission` và `/api/mission_dashboard` (endpoint trùng tên)?
