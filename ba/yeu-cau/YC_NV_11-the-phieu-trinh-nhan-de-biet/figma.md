<!-- Ban rut gon de dua len Figma. Nguon: dac-ta.md v1.0 (07/10/2026).
     Sinh SVG: python "AI Analysis/ba/_tools/md_to_figma_svg.py" figma.md [--theme light]
     ==cam== = thay doi so voi hien tai · !!do!! = luu y / cho chot -->
=== 1900
# YC_NV_11 - THÊM Ô "NHẬN ĐỂ BIẾT" VÀO NHÓM PHIẾU TRÌNH TRÊN TRANG CHỦ
## TỔNG QUAN
- Màn hình: Trang chủ → thẻ "Phiếu trình" (nhóm 5 ô: Chờ xử lý, Đang xử lý, Đã phê duyệt, Tất cả, Xin ý kiến)
- Mục tiêu:
  - ==Thêm ô thứ 6 "Nhận để biết"== ở cuối nhóm, mang số phiếu trình người khác chuyển cho mình để biết
  - Bấm ô → mở thẳng màn "Phiếu trình nhận để biết", ==không phải đi qua menu==
  - Ô ==mặc định bật cho mọi người==, tự bật / tắt được ở "Cấu hình trang chủ"
- Phạm vi: WEB và ==ứng dụng di động==. Phần di động !!chưa đủ điều kiện làm, chờ chốt TBD-01, TBD-02, TBD-03!!
- Giữ nguyên: màn "Phiếu trình nhận để biết", 5 ô phiếu trình hiện có, màn "Cấu hình trang chủ", chuyển tiếp để biết, thông báo / SMS, trạng thái phiếu, cờ đã đọc; không thêm bảng / cột

=== 900
## HIỆN TRẠNG → MONG MUỐN
- Nhóm "Phiếu trình" trên trang chủ đang có 5 ô → ==6 ô, ô "Nhận để biết" ở cuối==
- Phiếu được chuyển để biết hiện chỉ xem được qua menu "Phiếu trình nhận để biết"; biết có phiếu mới qua thông báo và SMS → ==thêm một ô đếm ngoài trang chủ==
- Chế độ trang chủ gọn: nhóm chỉ hiện ô "Chờ xử lý" → ==hiện thêm ô "Nhận để biết", cho mọi vai trò kể cả văn thư==
- Cấu hình trang chủ: 5 dòng dưới nhóm "Phiếu trình" → ==thêm dòng "Nhận để biết", mặc định đã tick==
- Trang chủ ứng dụng di động: không có ô này → ==thêm ô, mặc định bật== !!chờ chốt TBD-01, TBD-02!!
- Không đổi: trạng thái phiếu, cờ đã đọc, dữ liệu nghiệp vụ

## XEM Ô "NHẬN ĐỂ BIẾT" (trang chủ chế độ đầy đủ)
- Hiển thị: ==mọi người dùng đã đăng nhập==, không giới hạn vai trò; mỗi người thấy số của riêng mình
- Vị trí: ô thứ 6, ==sau ô "Xin ý kiến"==; thứ tự 5 ô trước không đổi
- Nhãn trên ô: **"Nhận để biết"**
- Con số = ==tổng số phiếu trình trong hộp "Phiếu trình nhận để biết" của người đăng nhập==
  - Đếm cả phiếu đã đọc và chưa đọc
  - Một phiếu được chuyển cho mình nhiều lần → tính 1
  - Chỉ đếm phiếu có ngày chuyển trong ==365 ngày gần nhất== (bằng khoảng mặc định của bộ lọc màn nhận để biết, để số trên ô khớp số dòng khi bấm vào)
- Không có phiếu nào → ==ô vẫn hiện, ghi số 0==, không ẩn ô
- Phép đếm quá 20 giây → ô hiện 0, trang vẫn tải xong, không báo lỗi (giữ cách nhóm ô này đang xử lý)
- Lỗi khi đếm → ô hiện 0, không làm vỡ 5 ô còn lại
- Ô chỉ đọc: hiển thị và bấm ô ==không đánh dấu đã đọc==, không đổi trạng thái phiếu, không ghi dòng chuyển tiếp mới

--- 1300
## BẤM VÀO Ô
- Nhấn ô "Nhận để biết" → ==mở màn "Phiếu trình nhận để biết"== (như bấm menu)
  - Bộ lọc mặc định của màn: ngày chuyển từ hôm nay trừ 365 ngày đến hôm nay
  - Không lọc tiêu đề, không lọc người gửi, ==không áp thêm bộ lọc chưa đọc==
  - Phiếu chưa đọc vẫn in đậm như hiện nay
- Bấm hai lần liên tiếp → mở màn một lần, không mở trùng tab
- Không thêm tab, không thêm bộ lọc, không thêm cột cho màn nhận để biết

## BẬT / TẮT Ô Ở "CẤU HÌNH TRANG CHỦ"
- Đường vào: khung người dùng góc phải → "Cấu hình trang chủ"
- ==Dòng "Nhận để biết"== nằm dưới nhóm "Phiếu trình", sau dòng "Xin ý kiến"
  - Checkbox, ==mặc định đã tick với mọi người dùng==, kể cả người đã lưu cấu hình riêng trước khi có ô này
  - Không có biểu tượng xóa (chỉ ô người dùng tự tạo mới có)
- Bỏ tick → Lưu → popup xác nhận → OK → toast "Lưu thành công"
  - Mở lại trang chủ: nhóm còn 5 ô, ==không có ô "Nhận để biết"==; 5 ô còn lại giữ nguyên số
  - Tick lại → Lưu → ô hiện lại với số đúng
- Bỏ tick cả 6 ô → nhóm "Phiếu trình" tự tắt (cơ chế sẵn có)
- Tắt cả nhóm → không vẽ ô nào của nhóm, kể cả ô mới
- !!Cấu hình trang chủ của từng người chỉ được giữ tạm, hệ thống khởi động lại là về mặc định nên ô hiện lại - hiện trạng chung của màn này, không xử lý riêng trong YC_NV_11!!
- Màn "Cấu hình trang chủ" không phải sửa: ô mới tự có mặt trong danh sách

## TRANG CHỦ CHẾ ĐỘ GỌN
- Hiện nay nhóm "Phiếu trình" chỉ có ô "Chờ xử lý"
- ==Thêm ô "Nhận để biết"== → nhóm có 2 ô, cho ==mọi người dùng, cả văn thư và người không phải văn thư==
- Ô dạng một dòng: dấu tròn màu bên trái, số trong viên thuốc bên phải
- Ô "Chờ xử lý" dùng dấu tròn đỏ → ô "Nhận để biết" dùng ==dấu tròn xám== (để biết không phải việc phải xử lý)

--- 900
## Ô TRÊN ỨNG DỤNG DI ĐỘNG
- ==Ô "Phiếu trình nhận để biết" có trong danh sách ô trang chủ di động, bật / tắt được, mặc định bật==
- Số đếm dùng ==đúng cách đếm của web== (tổng số phiếu, 365 ngày gần nhất) để hai kênh không lệch số
- !!Chưa đủ điều kiện làm: chờ TBD-01 (di động có màn nhận để biết chưa), TBD-02 (mặc định bật thế nào), TBD-03 (ai phát hành ứng dụng và bao giờ)!!
- !!Chưa chốt thì KHÔNG sửa gì ở trang chủ di động!!

## CẬP NHẬT CSDL
- ==Thêm 1 dòng HOME_WIDGET==: PARENT_CODE = 'PHIEU_TRINH', SIMPLE_MODE = 3 (hiện ở chế độ gọn cho mọi người), CODE mới, ID chưa dùng
- Chỉ SELECT để đếm: SUBMISSION_FORWARD.RECEIVER_ID = người đăng nhập, lọc SUBMISSION_FORWARD.SEND_DATE theo 365 ngày, gộp mỗi phiếu một dòng
- ==Phép đếm dùng lại đúng truy vấn của màn "Phiếu trình nhận để biết"==, không viết truy vấn riêng
- Không ghi, sửa, xóa dòng SUBMISSION_FORWARD nào; không đổi SUBMISSION_FORM.STATUS, không đổi SUBMISSION_FORWARD.IS_READ
- Phần di động (khi làm): ==thêm 1 dòng PERMISSION_DASHBOARD== (TYPE = 1) trỏ tới menu di động; !!có thể phải thêm 1 dòng MENU nếu di động chưa có màn - chờ TBD-01!!
- Cấu hình bật / tắt của từng người: không có bảng, chỉ nằm trong bộ nhớ đệm
- Không thêm bảng / cột, không cần migration dữ liệu nghiệp vụ

## KHÔNG THAY ĐỔI
- Màn "Phiếu trình nhận để biết": lưới, bộ lọc, phân trang, in đậm phiếu chưa đọc, mở chi tiết, chuyển tiếp tiếp
- 5 ô phiếu trình hiện có: số đếm, nhãn, đích điều hướng
- Các nhóm ô khác của trang chủ (Văn bản đến, Văn bản đi, Nhiệm vụ, Lịch họp, Nhắc việc...)
- Màn "Cấu hình trang chủ": bật / tắt ô khác, tạo / xóa ô tự tạo, Lưu, Hủy
- Chuyển tiếp để biết: điều kiện phiếu đã phê duyệt, thông báo và SMS cho người nhận
- Trạng thái phiếu, cờ đã đọc, quyền xem phiếu
- Thời gian tải trang chủ không xấu đi rõ rệt

!!Lưu ý không để ảnh hưởng đến luồng hiện tại!!

## CẦN CHỐT
- !!TBD-01!! Di động đã có màn "Phiếu trình nhận để biết" chưa (mã nguồn chỉ thấy Chờ xử lý, Đang xử lý, Đã phê duyệt, Theo dõi):
  - A. Làm thêm màn đó trên ứng dụng rồi mới thêm ô
  - B. Ô di động mở tạm màn danh sách khác
  - C. Tách phần di động thành yêu cầu riêng, web đi trước (đang đề xuất)
- !!TBD-02!! Trang chủ di động chỉ bật sẵn 5 ô đầu, ô sau mặc định tắt:
  - A. Xếp ô mới vào 5 ô đầu (một ô đang bật bị đẩy ra)
  - B. Nâng số ô bật mặc định lên 6
  - C. Trên di động ô không bật mặc định, người dùng tự bật (đang đề xuất)
- !!TBD-03!! Ứng dụng di động nằm ngoài mã nguồn web: ai làm, phát hành bản nào, bao giờ; người chưa cập nhật ứng dụng vẫn không thấy ô - có chấp nhận không
- TBD-04: Nhãn ô ở các ngôn ngữ khác tiếng Việt - khóa nhãn mới (cần bản dịch) hay dùng lại khóa nhãn "Nhận để biết" của nhóm Văn bản đến (đang đề xuất dùng lại)
- TBD-05: Mã và ID của dòng HOME_WIDGET mới - chốt bằng một câu SELECT trên DB DEV trước khi viết script (script cũ từng cấp ID trùng)
- TBD-06: Phiếu ý tưởng còn thiếu một tình huống thật để làm dữ liệu kiểm thử
- Lựa chọn trình bày (ngoài TBD): ô mới trông ==giống 5 ô cùng nhóm Phiếu trình== hay giống ô "Nhận để biết" của nhóm Văn bản đến - đang đề xuất giống 5 ô cùng nhóm cho đồng bộ
