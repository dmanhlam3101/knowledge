# YC_NV_08 — CHECKLIST TEST GIAO DIỆN

> Test bằng tay trên màn hình, không cần đọc mã nguồn. Mục tiêu: cột mới hiện đúng, và **các luồng đang chạy không bị
> gãy** vì thêm một cột vào bảng.
> Nghiệp vụ: [thiet-ke-man-hinh.md](thiet-ke-man-hinh.md) · Điều kiện nghiệm thu: mục 8 của [dac-ta.md](dac-ta.md).
> Cách ghi: `Đ` đạt · `K` không đạt, ghi hiện tượng vào cột Ghi chú · `N` chưa chạy được, ghi lý do.

**Màn hình chính cần test:** Chi tiết văn bản → panel *Danh sách người/ đơn vị cùng nhận*.

---

## A. Dữ liệu cần dựng trước khi test

Dựng bằng chính giao diện, không can thiệp cơ sở dữ liệu. Mỗi văn bản chỉ cần nội dung sơ sài.

| Mã | Văn bản cần có | Cách dựng |
|---|---|---|
| VB-1 | Một lần chuyển, **có hạn**, gửi hai cá nhân | Lãnh đạo chuyển cho hai chuyên viên, nhập hạn vài ngày tới |
| VB-2 | Một lần chuyển, **không nhập hạn**, gửi một cá nhân | Chuyển và bỏ trống hạn |
| VB-3 | **Hai lần chuyển, hai hạn khác nhau**, trong đó một lần gửi **đơn vị** | Chuyển lần một cho cá nhân kèm hạn, hôm sau chuyển lần hai cho một đơn vị kèm hạn khác |
| VB-4 | Hạn **đã qua** so với hôm nay | Chuyển kèm hạn là ngày trong quá khứ, hoặc dùng văn bản cũ đã quá hạn |
| VB-5 | Văn bản **đã ban hành** | Lấy một văn bản đi đã cấp số và đã chuyển đi |
| VB-6 | Văn bản **mật** | Văn bản có độ mật khác Thường, đã chuyển cho người có quyền xem mật |
| VB-7 | Văn bản **chưa chuyển cho ai** | Văn bản vừa tiếp nhận, chưa chuyển |
| VB-8 | Văn bản có **trên năm dòng** trong danh sách | Chuyển nhiều lần cho nhiều người, tổng trên năm người nhận |
| VB-9 | Văn bản qua **hai cấp chuyển** | Lãnh đạo chuyển trưởng phòng kèm hạn, trưởng phòng chuyển tiếp chuyên viên kèm hạn khác |

**Tài khoản cần có:** một văn thư, một lãnh đạo đơn vị, hai chuyên viên, và nếu có thì một trợ lý lãnh đạo.

---

## B. Cột mới hiện đúng

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| B1 | Mở VB-1, mở panel người cùng nhận | Bảng có chín cột. Cột **Hạn xử lý** nằm thứ ba, ngay sau *Thời gian chuyển*, trước *Người chuyển* | | |
| B2 | Xem nhãn cột | Nhãn đúng chữ "Hạn xử lý", cùng cỡ chữ và kiểu chữ với các nhãn cột khác | | |
| B3 | Xem hai dòng của VB-1 | Cả hai hiện đúng ngày hạn đã nhập lúc chuyển. Hai dòng cùng một lần chuyển nên cùng hạn | | |
| B4 | Mở VB-2 | Ô Hạn xử lý **trống hẳn**. Không có chữ "Không có hạn", không dấu gạch, không số 0 | | |
| B5 | Mở VB-3 | Dòng cá nhân và dòng đơn vị hiện **hai hạn khác nhau**, đúng từng lần chuyển. Không dòng nào bị lấy hạn của dòng kia | | |
| B6 | Xem dòng chuyển cho đơn vị ở VB-3 | Cột *Người nhận* trống như trước, cột *Đơn vị nhận* có tên đơn vị, cột Hạn xử lý có hạn của đơn vị đó | | |
| B7 | So cột Hạn xử lý với cột Thời gian chuyển ở cùng một dòng | Hạn chỉ có ngày tháng năm. Thời gian chuyển vẫn có cả giờ phút như trước | | |
| B8 | Mở VB-4 | Dòng quá hạn hiện **như dòng thường**: không tô đỏ, không in đậm, không biểu tượng cảnh báo | | |
| B9 | Bấm vào ô Hạn xử lý của một dòng | Không xảy ra gì. Không mở popup, không vào chế độ sửa, không chọn được để gõ | | |
| B10 | Bấm đúp vào ô Hạn xử lý | Vẫn không có gì xảy ra | | |
| B11 | Mở VB-9 | Dòng cấp chuyển trước và dòng của mình đều có hạn riêng, đúng từng cấp | | |
| B12 | Mở VB-5, văn bản đã ban hành | Cột Hạn xử lý **vẫn hiện** dù các ô trống hết. Cột không bị ẩn | | |
| B13 | Mở VB-7, văn bản chưa chuyển cho ai | Panel người cùng nhận không hiện, đúng như trước. Không có bảng rỗng, không lỗi | | |
| B14 | Mở VB-8, chuyển sang trang hai của panel | Cột Hạn xử lý hiện ở trang hai, giá trị đúng theo từng dòng | | |
| B15 | Mở VB-6, văn bản mật, bằng tài khoản có quyền xem mật | Cột Hạn xử lý hiện bình thường. Phần nội dung ý kiến vẫn mã hóa và giải mã được như trước | | |

---

## C. Mở từ các đường vào khác nhau

Cùng một văn bản mở từ nhiều chỗ phải cho cùng kết quả. Đây là chỗ dễ sót nhất vì màn chi tiết dùng chung.

| # | Mở chi tiết văn bản từ | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| C1 | Hộp *Chờ xử lý* | Panel có cột Hạn xử lý, giá trị đúng | | |
| C2 | Hộp *Chờ tiếp nhận*, bằng tài khoản văn thư | Panel có cột, giá trị đúng | | |
| C3 | Hộp *Đã xử lý* | Panel có cột, giá trị đúng | | |
| C4 | Hộp *Văn bản nhận để biết* | Panel có cột, giá trị đúng | | |
| C5 | Hộp *Đề nghị trả lại* hoặc *Đã trả lại* | Panel có cột, giá trị đúng | | |
| C6 | Tab *Văn bản đơn vị*, bằng tài khoản văn thư | Panel có cột, giá trị đúng | | |
| C7 | Màn *Tra cứu văn bản* | Panel có cột, giá trị đúng | | |
| C8 | Màn *Theo dõi văn bản đến đơn vị* | Panel có cột, giá trị đúng | | |
| C9 | Màn hồ sơ công việc, mở văn bản trong hồ sơ | Panel có cột, không lỗi | | |
| C10 | Hộp văn bản đã ban hành hoặc văn bản đi | Panel có cột, các ô trống theo B12 | | |
| C11 | Mở từ thông báo hoặc chuông | Panel có cột, không lỗi | | |

---

## D. Theo vai trò

| # | Đăng nhập bằng | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| D1 | Lãnh đạo đơn vị | Thấy cột Hạn xử lý | | |
| D2 | Văn thư | Thấy cột, kể cả khi mở văn bản của đơn vị | | |
| D3 | Chuyên viên vai trò chủ trì | Thấy cột | | |
| D4 | Chuyên viên vai trò phối hợp | Thấy cột | | |
| D5 | Chuyên viên vai trò nhận để biết | Thấy cột | | |
| D6 | Trợ lý lãnh đạo, nếu có tài khoản | Thấy cột | | |
| D7 | Tài khoản **không liên quan** tới văn bản | Vẫn không mở được văn bản, đúng như trước. Quyền xem không bị mở rộng | | |

---

## E. Các luồng chính không được gãy

Phần quan trọng nhất. Thêm một cột vào bảng có thể làm lệch cả bảng hoặc làm màn khác lỗi, nên phải chạy lại các luồng
quen thuộc.

### E1. Chính panel đó và bảng liền kề

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| E1.1 | Xem toàn bộ chín cột của panel | **Không lệch cột**: tên người ở cột người, tên đơn vị ở cột đơn vị, ý kiến ở cột ý kiến. Không có ô nào nhảy sang cột bên cạnh | | |
| E1.2 | Trỏ chuột vào ô tên đơn vị bị cắt chữ | Chú thích hiện đủ tên như trước | | |
| E1.3 | Bấm kính lúp ở cột *Ý kiến chỉ đạo* | Mở xem đầy đủ nội dung ý kiến như trước | | |
| E1.4 | Bấm tên tệp đính kèm trong cột ý kiến | Mở hoặc tải tệp được như trước | | |
| E1.5 | Thu gọn rồi mở lại panel | Panel đóng mở bình thường, cột vẫn đúng | | |
| E1.6 | Chuyển trang trong panel | Phân trang chạy bình thường, năm dòng một trang | | |
| E1.7 | Xem panel *Danh sách đã gửi đi* trên cùng màn | **Không đổi gì**: số cột, tên cột, dữ liệu, nút thu hồi y như trước | | |
| E1.8 | Xem panel *Chỉ đạo của lãnh đạo* | Không đổi gì | | |
| E1.9 | Cuộn hết màn chi tiết từ trên xuống dưới | Mọi panel khác hiện bình thường: thông tin văn bản, tệp, người ký, nhắc việc, nhiệm vụ, hồ sơ, lịch sử | | |

### E2. Luồng chuyển và thu hồi

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| E2.1 | Chuyển một văn bản cho một cá nhân, **nhập hạn** | Chuyển thành công. Mở lại chi tiết thấy dòng mới với hạn vừa nhập | | |
| E2.2 | Chuyển cho một cá nhân, **bỏ trống hạn** | Chuyển thành công. Dòng mới có ô hạn trống | | |
| E2.3 | Chuyển cho một **đơn vị** kèm hạn | Chuyển thành công. Dòng đơn vị có hạn | | |
| E2.4 | Chuyển cho một **nhóm** | Chuyển thành công như trước, không lỗi | | |
| E2.5 | Chuyển **nhiều văn bản** một lúc | Chạy như trước, không lỗi | | |
| E2.6 | **Thu hồi** một dòng đã chuyển | Thu hồi được. Dòng đó rời khỏi danh sách người cùng nhận như trước | | |
| E2.7 | Chuyển lại cho người đã nhận, có nhập ý kiến | Chạy như trước, danh sách có thêm dòng | | |
| E2.8 | Văn thư chuyển văn bản đã cấp số | Chạy như trước | | |

### E3. Luồng xử lý văn bản

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| E3.1 | Bấm *Hoàn thành* một văn bản | Hoàn thành được như trước, kể cả popup nhập nội dung | | |
| E3.2 | Bấm *Trả lại* một văn bản | Trả lại được như trước | | |
| E3.3 | Lãnh đạo bấm *Cho ý kiến* | Ghi ý kiến được, ý kiến hiện lên đầu danh sách ý kiến như trước | | |
| E3.4 | Văn thư **tiếp nhận** một văn bản gửi đơn vị, có nhập hạn | Tiếp nhận được, hạn lưu đúng như trước | | |
| E3.5 | Đánh dấu đã đọc, rồi đánh dấu chưa đọc | Chạy như trước | | |
| E3.6 | Lưu văn bản vào hồ sơ, ghi chú, gắn thẻ | Chạy như trước | | |
| E3.7 | Mở màn **Thêm file đính kèm** của một văn bản | Màn mở bình thường, không lỗi, không thiếu dữ liệu | | |

### E4. Số đếm và thống kê

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| E4.1 | Xem số trên các hộp việc văn bản đến | Số giữ nguyên, không đổi so với trước khi sửa | | |
| E4.2 | Xem các ô ở trang chủ | Số giữ nguyên | | |
| E4.3 | Xem hộp *Sắp đến hạn* và *Quá hạn* | Danh sách và số giữ nguyên. Yêu cầu này không đụng tới cách tính hạn | | |
| E4.4 | Xem thống kê ở *Theo dõi văn bản đến đơn vị* | Số liệu giữ nguyên | | |

### E5. Giao diện chung

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| E5.1 | Xem bảng ở độ rộng màn hình thường dùng | Bảng **không tràn ngang**, không phải cuộn ngang mới thấy cột cuối | | |
| E5.2 | Thu nhỏ cửa sổ trình duyệt | Bảng co lại gọn, không chồng chữ, không vỡ bố cục | | |
| E5.3 | Bấm Ctrl và dấu trừ, rồi Ctrl và dấu bằng để thu nhỏ phóng to | Bảng hiện đúng ở các mức, không vỡ | | |
| E5.4 | Nhìn độ rộng các cột | Cột hạn vừa đủ cho một ngày. Các cột khác không bị bóp đến mức mất chữ | | |
| E5.5 | Kiểm chính tả nhãn cột | "Hạn xử lý" viết đúng, có dấu đầy đủ | | |
| E5.6 | Đổi ngôn ngữ hiển thị nếu hệ thống cho đổi | Nhãn cột có bản dịch, không hiện mã khóa thô | | |

### E6. Ứng dụng di động

Chạy nếu phần di động làm cùng đợt. Nếu để đợt sau thì ghi `N` và nêu lý do.

| # | Việc cần làm | Kết quả đúng | KQ | Ghi chú |
|---|---|---|---|---|
| E6.1 | Mở chi tiết một văn bản trên ứng dụng di động, bản mới | Mục người cùng nhận hiện hạn đúng từng dòng | | |
| E6.2 | Mở một văn bản không có hạn trên di động | Chỗ hạn để trống, không hiện chữ lạ | | |
| E6.3 | Mở chi tiết văn bản bằng **bản di động cũ** | Vẫn mở bình thường, không lỗi, chỉ là không thấy hạn | | |

---

## F. Kết luận vòng test

| Nhóm | Tổng số case | Đạt | Không đạt | Chưa chạy |
|---|---|---|---|---|
| B. Cột mới hiện đúng | 15 | | | |
| C. Các đường vào | 11 | | | |
| D. Theo vai trò | 7 | | | |
| E1. Panel và bảng liền kề | 9 | | | |
| E2. Chuyển và thu hồi | 8 | | | |
| E3. Xử lý văn bản | 7 | | | |
| E4. Số đếm và thống kê | 4 | | | |
| E5. Giao diện chung | 6 | | | |
| E6. Di động | 3 | | | |
| **Tổng** | **70** | | | |

**Điều kiện kết luận đạt:**

- Nhóm B không còn case nào không đạt.
- Nhóm E1 không còn case nào không đạt. Lệch cột là lỗi nặng nhất của yêu cầu này.
- Nhóm E2, E3, E4 không có case nào thay đổi hành vi so với trước khi sửa.
- Case không đạt còn lại phải có người nhận xử lý và hạn.

**Người test:** ................. · **Môi trường:** ................. · **Ngày:** .................
