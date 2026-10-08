# YC_NV_08 — MÔ TẢ THIẾT KẾ MÀN HÌNH: HIỆN TRẠNG VÀ MONG MUỐN

> Viết bằng lời nghiệp vụ cho BA, người vẽ Figma và người kiểm thử đọc. Phần kỹ thuật nằm ở mục 10 của
> [dac-ta.md](dac-ta.md). Ảnh mô phỏng: [`input/design/01_panel_nguoi_cung_nhan.svg`](input/design/01_panel_nguoi_cung_nhan.svg).

**Màn hình:** Chi tiết văn bản → panel *Danh sách người/ đơn vị cùng nhận*.
**Đường vào:** mở chi tiết một văn bản từ bất kỳ hộp việc hay màn tra cứu nào, rồi mở panel này. Panel nằm trong chuỗi
các panel thu gọn được của màn chi tiết, sau phần *Chỉ đạo của lãnh đạo*.

---

## 1. Câu chuyện nghiệp vụ, kể bằng một tình huống

Lãnh đạo Sở nhận một văn bản của tỉnh. Lãnh đạo chuyển cho Phòng Kế hoạch chủ trì và một chuyên viên phối hợp, kèm
**hạn xử lý ngày 15/10**. Hôm sau trưởng phòng chuyển tiếp cho UBND huyện Diên Khánh với **hạn 20/10**.

Khi lãnh đạo mở lại văn bản để xem việc đang chạy tới đâu, danh sách người cùng nhận hiện đủ ngày chuyển, người chuyển,
người nhận và ý kiến chỉ đạo, nhưng **không có chỗ nào ghi hạn**. Chính lãnh đạo đã giao hạn mà màn hình không nhắc lại.
Muốn biết ai phải xong khi nào, lãnh đạo phải mở từng hộp việc hoặc hỏi lại văn thư.

Yêu cầu này lấp đúng chỗ đó: thêm một cột hạn xử lý vào danh sách, để một lần mở văn bản là thấy hết hạn của mọi người.

---

## 2. Hiện trạng: danh sách đang có gì

Panel hiện có **tám cột**, theo thứ tự từ trái sang phải:

| # | Cột | Nội dung đang hiện |
|---|---|---|
| 1 | STT | Số thứ tự dòng, đánh lại theo từng trang |
| 2 | Thời gian chuyển | Ngày và giờ phút của lần chuyển |
| 3 | Người chuyển | Họ tên, kèm thông tin liên hệ nếu có |
| 4 | Đơn vị chuyển | Đơn vị của người chuyển |
| 5 | Người nhận | Họ tên người nhận. Dòng chuyển cho đơn vị thì cột này trống |
| 6 | Đơn vị nhận | Đơn vị của người nhận, hoặc đơn vị được nhận |
| 7 | Ý kiến chỉ đạo | Nội dung ý kiến khi chuyển, kèm tệp đính kèm nếu có, có kính lúp xem đầy đủ |
| 8 | Yêu cầu trả lời | Tình trạng yêu cầu trả lời của dòng đó |

Mỗi dòng của danh sách là **một người hoặc một đơn vị được nhận văn bản trong một lần chuyển**. Một văn bản chuyển nhiều
lần thì danh sách có nhiều dòng, và panel chia trang mỗi trang năm dòng.

**Vấn đề:** hạn xử lý đã được lãnh đạo nhập ngay lúc chuyển và hệ thống đã lưu lại cho từng người, nhưng danh sách này
không đọc nó ra. Người xem không có cách nào biết hạn mà không mở thêm màn khác.

---

## 3. Mong muốn: thêm đúng một cột

Panel có **chín cột**. Cột mới tên **Hạn xử lý**, đặt ở **vị trí thứ ba**, ngay sau *Thời gian chuyển* và trước
*Người chuyển*. Bảy cột còn lại giữ nguyên tên, nguyên nội dung, chỉ bị đẩy sang phải một bậc.

**Cột mới hiện gì:**

| Trường hợp | Ô Hạn xử lý hiện |
|---|---|
| Lãnh đạo giao hạn cho người này khi chuyển | Ngày hạn, dạng ngày tháng năm, ví dụ `15/10/2026` |
| Lãnh đạo không giao hạn | **Để trống** |
| Dòng là một đơn vị nhận | Hạn giao cho đơn vị đó, cùng cách hiện như với cá nhân |
| Hai dòng thuộc cùng một lần chuyển | Cùng một hạn, vì lãnh đạo nhập một hạn cho cả lần chuyển |
| Hai dòng thuộc hai lần chuyển khác nhau | Hai hạn khác nhau. Danh sách **không** đồng nhất về một hạn |
| Hạn đã qua so với hôm nay | Vẫn hiện như dòng thường, **không tô đỏ**, không gắn biểu tượng cảnh báo |

**Bốn điều cột này không làm:**

1. Không sửa được hạn tại đây. Cột chỉ để xem. Muốn đổi hạn thì chuyển lại văn bản, đúng như cách làm hiện nay.
2. Không ghi chữ thay thế khi trống. Không có "Không có hạn", không có dấu gạch.
3. Không lấy hạn của sổ văn bản đến để lấp chỗ trống. Hạn trong danh sách là hạn lãnh đạo giao cho từng người, hai thứ
   khác nhau về nghĩa.
4. Không thêm điều kiện phân quyền. Ai mở được danh sách thì thấy cột, dù là lãnh đạo, văn thư hay chuyên viên.

**Áp dụng ở đâu:** mọi đường mở chi tiết văn bản, cho cả **văn bản đến** và **văn bản đã ban hành**. Với văn bản đã ban
hành, các dòng thường không có hạn nên cột sẽ trống gần hết, nhưng cột vẫn hiện chứ không ẩn.

**Trên ứng dụng di động:** mục người cùng nhận trong chi tiết văn bản cũng hiện hạn, theo cùng các quy tắc trên. Phần
giao diện di động đang chờ đội di động chốt, ghi ở mục TBD-01 của đặc tả.

---

## 4. Việc cần vẽ trên Figma

Vẽ lại đúng kiểu bảng đang chạy, **không thiết kế lại panel**. Cần hai khung:

| Khung | Nội dung |
|---|---|
| Khung 1 — Hiện trạng | Panel tám cột, đúng như bản chạy thật, để đối chiếu |
| Khung 2 — Mong muốn | Panel chín cột, có cột Hạn xử lý ở vị trí thứ ba |
| Khung 3 — Trạng thái rỗng | Panel chín cột mà mọi ô hạn đều trống, dùng cho văn bản đã ban hành |

**Quy cách cột mới:**

- Nhãn cột: "Hạn xử lý". Cùng cỡ chữ, cùng kiểu chữ, cùng màu với bảy nhãn cột còn lại.
- Bề rộng: vừa đủ cho một ngày mười ký tự. Không cần rộng bằng cột *Thời gian chuyển* vì không hiện giờ phút.
- Nội dung ô: căn giữa, cùng màu chữ với các cột khác. Không in đậm, không màu riêng.
- Ô trống: để trắng hoàn toàn.
- Màu xanh trong ảnh mô phỏng **chỉ để chỉ chỗ thêm mới**, không được dùng trên sản phẩm.

**Hai điều cần giữ:**

- Bảng không được tràn ngang ở độ rộng màn hình thường dùng. Nếu thiếu chỗ thì thu hẹp *Đơn vị chuyển* và *Đơn vị nhận*,
  vì hai cột này đã có chú thích hiện đủ tên khi trỏ chuột. Không thu hẹp *Ý kiến chỉ đạo*.
- Phân trang của panel giữ nguyên, năm dòng một trang. Cột mới hiện ở mọi trang.

**Dữ liệu mẫu nên dùng trong ảnh** để thấy đủ các trường hợp: một dòng có hạn, một dòng cùng lần chuyển nhưng không có
hạn, một dòng chuyển cho đơn vị với hạn khác, và một dòng đã quá hạn để thấy rõ là không tô màu.

---

## 5. Người kiểm thử nhìn vào đâu

| Nhìn | Đúng khi |
|---|---|
| Thứ tự cột | Hạn xử lý là cột thứ ba, nằm giữa Thời gian chuyển và Người chuyển |
| Giá trị từng dòng | Trùng với hạn mà người chuyển đã nhập ở lần chuyển sinh ra dòng đó |
| Dòng không hạn | Ô trống hẳn, không có ký tự nào |
| Nhiều lần chuyển | Mỗi dòng giữ hạn riêng, không dòng nào bị lấy hạn của dòng khác |
| Dạng ngày | Ngày tháng năm, không có giờ phút |
| Quá hạn | Không đổi màu, không biểu tượng |
| Theo vai trò | Lãnh đạo, văn thư, chuyên viên đều thấy cột |
| Văn bản đã ban hành | Cột vẫn hiện dù mọi ô trống |

Danh sách điều kiện nghiệm thu đầy đủ ở mục 8 của [dac-ta.md](dac-ta.md), mười ba điều kiện từ AC-01 tới AC-13.
