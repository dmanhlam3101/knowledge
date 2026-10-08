# YC_NV_08 — NỘI DUNG DÁN VÀO FIGMA

> Dành cho section **NV_08 — Thêm hạn xử lý ở Danh sách người cùng nhận** trong file
> `VO_KhanhHoa_AT`, trang `🔔Nhắc việc`, nằm trong section cha *Danh sách tính năng Nhắc việc 07/10*.
> Section đã tồn tại và đã có ảnh mô phỏng bên trong. Phần còn thiếu là chữ.
> Trình bày theo mẫu NV_11 cùng section cha: một dòng bảng vàng ở trên, khối *Phân tích nghiệp vụ* ở dưới.

---

## 1. Dòng bảng ở đầu section

| Ô | Nội dung |
|---|---|
| Mã | `NV_08` |
| Nền tảng | `WEB + APP` |
| Tiêu đề | `Thêm hạn xử lý ở Danh sách người cùng nhận (hiện tại hệ thống không hiển thị nếu lãnh đạo giao hạn)` |

---

## 2. Khối "Phân tích nghiệp vụ"

**Hiện trạng**

Panel *Danh sách người/ đơn vị cùng nhận* trong màn chi tiết văn bản đang có 8 cột: STT, Thời gian chuyển,
Người chuyển, Đơn vị chuyển, Người nhận, Đơn vị nhận, Ý kiến chỉ đạo, Yêu cầu trả lời. Không có cột hạn.

Lãnh đạo nhập hạn ngay khi bấm Chuyển văn bản và hệ thống đã lưu hạn đó cho từng người nhận. Màn hình chỉ
chưa đọc nó ra, nên người xem không biết ai phải xử lý xong khi nào.

**Mong muốn**

Thêm đúng một cột **Hạn xử lý**, đặt ở vị trí thứ ba, ngay sau *Thời gian chuyển* và trước *Người chuyển*.
Bảy cột còn lại giữ nguyên, chỉ dịch sang phải một bậc.

**Quy tắc hiển thị**

1. Mỗi dòng hiện hạn của **chính người hoặc đơn vị ở dòng đó**.
2. Hai dòng cùng một lần chuyển thì cùng hạn. Hai lần chuyển khác nhau thì hai hạn khác nhau. Không đồng
   nhất các dòng về một hạn.
3. Lãnh đạo không giao hạn cho người này thì **ô để trống**. Không ghi chữ thay thế, không lấy hạn của sổ
   văn bản đến.
4. Hiện dạng ngày tháng năm, không có giờ phút. Khác cột *Thời gian chuyển* bên cạnh.
5. Dòng đã quá hạn **vẫn hiện như dòng thường**. Không tô đỏ, không biểu tượng cảnh báo.
6. Cột chỉ để xem. Không bấm được, không sửa hạn tại đây. Hệ thống không có chức năng gia hạn.
7. Ai mở được panel thì thấy cột. Không phân biệt lãnh đạo, văn thư hay chuyên viên.
8. Áp dụng cho **văn bản đến và văn bản đã ban hành**. Văn bản đã ban hành phần lớn không có hạn nên ô
   trống, nhưng cột vẫn hiện chứ không ẩn.
9. Dòng của cấp chuyển trước trong chuỗi chuyển cũng theo đúng các quy tắc trên.

**Phạm vi**

Web và ứng dụng di động. Màn chi tiết văn bản là màn dùng chung nên cột hiện ở mọi đường mở: hộp việc, tra
cứu, theo dõi văn bản đơn vị, hồ sơ.

**Dữ liệu**

Hạn đã có sẵn, nằm trên chính dòng nhận: bảng dòng nhận cá nhân và bảng dòng nhận đơn vị, cột hạn xử lý.
Không thêm bảng, không thêm cột, không chuyển đổi dữ liệu cũ.

Lưu ý hệ thống đang có bốn chỗ lưu hạn khác nghĩa nhau: hạn trên bản ghi văn bản, hạn ở sổ văn bản đến, hạn
của người nhận, hạn của đơn vị nhận. Yêu cầu này **chỉ dùng hai chỗ cuối**.

**Điểm cần chốt**

Ứng dụng di động hiện cột ở đâu và từ phiên bản nào. Phần web không còn điểm chặn, làm được ngay.

---

## 3. Ảnh kèm theo

Ảnh mô phỏng hiện trạng và mong muốn đã nằm sẵn trong section, tên lớp
`01_panel_nguoi_cung_nhan-screenshot 1`. Tệp gốc ở
[`input/design/01_panel_nguoi_cung_nhan.svg`](input/design/01_panel_nguoi_cung_nhan.svg), bản xem nhanh bằng
trình duyệt ở [`input/design/01_panel_nguoi_cung_nhan.html`](input/design/01_panel_nguoi_cung_nhan.html).
