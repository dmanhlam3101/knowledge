# NV_11 — CHỮ DÁN VÀO FIGMA (mô tả BA)

> Dán từng khối dưới đây thành từng text layer trong section **`NV_11 — Thẻ Phiếu trình nhận để biết`**
> (id `11036:21492`). Mỗi khối là một layer, tiêu đề in đậm là dòng đầu của layer đó.
> Chữ đã viết theo lời nghiệp vụ, không có mã màu, tên bảng hay tên hàm.
>
> Section hiện có sẵn hai ảnh: một ảnh ngang ở trên bên trái (nhóm ô trang chủ) và một ảnh dọc bên phải.
> Gợi ý đặt chữ: khối 1 đến 4 xếp dọc ở cột trái dưới ảnh ngang; khối 5 và 6 ở cột giữa; khối 7 ở dưới cùng.
> Trong section còn một text layer rời tên `v` ở giữa, nên xóa.

---

## Khối 1 · Tiêu đề và một câu chốt

```
NV_11 — Thêm thẻ "Nhận để biết" vào nhóm Phiếu trình trên trang chủ

Mục đích: từ trang chủ biết ngay mình có bao nhiêu phiếu trình được người khác
chuyển cho để biết, và vào xem bằng một lần bấm.
```

---

## Khối 2 · Hiện trạng

```
HIỆN TRẠNG

Nhóm "Phiếu trình" trên trang chủ đang có 5 ô: Chờ xử lý, Đang xử lý,
Đã phê duyệt, Tất cả, Xin ý kiến.

Phiếu trình được người khác chuyển cho mình để biết thì không có ô nào.
Muốn xem phải vào menu Phiếu trình nhận để biết.

Người nhận chỉ biết có phiếu mới qua thông báo và tin nhắn, hai thứ này
trôi nhanh nên dễ bỏ sót.
```

---

## Khối 3 · Mong muốn

```
MONG MUỐN

Thêm ô thứ 6 tên "Nhận để biết", đặt cuối nhóm, giữ nguyên thứ tự 5 ô đang có.

Ô hiện cho mọi người dùng, không giới hạn vai trò. Mỗi người thấy con số
của riêng mình.

Ô mặc định bật cho mọi người. Ai không cần thì tự tắt ở Cấu hình trang chủ.
```

---

## Khối 4 · Con số trên ô nghĩa là gì

```
CON SỐ TRÊN Ô NGHĨA LÀ GÌ

Đếm cái gì: số phiếu trình mà người khác đã chuyển cho chính tôi để biết.
Không đếm phiếu của người khác.

Trong bao lâu: các phiếu được chuyển trong một năm gần đây. Đúng bằng khoảng
thời gian màn Phiếu trình nhận để biết đang lọc sẵn, nên số trên ô luôn khớp
số dòng nhìn thấy khi bấm vào.

Phiếu đã đọc có còn tính không: có. Ô đếm tất cả, đã đọc hay chưa đọc đều
tính như nhau.

Một phiếu được chuyển nhiều lần: vẫn tính một. Hai người cùng chuyển một
phiếu cho tôi thì ô chỉ tăng 1.

Ví dụ: được chuyển phiếu A đã đọc, phiếu B chưa đọc, phiếu C do hai người
cùng chuyển. Ô hiện số 3.
```

---

## Khối 5 · Bấm vào ô thì đi đâu

```
BẤM VÀO Ô THÌ ĐI ĐÂU

Mở đúng màn Phiếu trình nhận để biết, giống như bấm vào menu, kèm bộ lọc
mặc định sẵn có của màn.

MÀN ĐÓ KHÔNG THAY ĐỔI: danh sách, bộ lọc, cách in đậm phiếu chưa đọc giữ
nguyên. Không thêm tab, không thêm bộ lọc, không thêm cột.

Bấm vào ô không làm phiếu thành đã đọc. Chỉ khi mở chi tiết một phiếu thì
phiếu đó mới tính là đã đọc, như hiện nay.
```

---

## Khối 6 · Tự bật tắt và chế độ trang chủ gọn

```
TỰ BẬT TẮT

Ô mới mặc định bật cho mọi người, kể cả người trước đây đã từng vào tự sửa
cấu hình trang chủ.

Ai không cần thì vào Cấu hình trang chủ, bỏ tick dòng "Nhận để biết", bấm Lưu.
Trang chủ của riêng người đó không còn ô này; 5 ô còn lại không bị ảnh hưởng.

Màn Cấu hình trang chủ không phải làm mới, ô mới tự có mặt trong danh sách.

CHẾ ĐỘ TRANG CHỦ GỌN

Ở cách bày gọn, nhóm Phiếu trình hiện nay chỉ có ô Chờ xử lý. Theo yêu cầu,
ô "Nhận để biết" cũng hiện ở cách gọn, cho mọi người dùng kể cả văn thư.

Ô Chờ xử lý dùng dấu tròn đỏ. Ô Nhận để biết dùng dấu tròn xám, vì để biết
không phải việc phải xử lý nên không cần màu cảnh báo.
```

---

## Khối 7 · Tình huống và điểm chưa chốt

```
TÌNH HUỐNG NGƯỜI DÙNG SẼ GẶP

Chưa từng được chuyển phiếu nào để biết: ô vẫn hiện và ghi số 0. Không ẩn ô,
vì ẩn rồi hiện lại làm người dùng tưởng cấu hình bị đổi.

Tắt ô rồi hệ thống được khởi động lại: ô hiện lại. Cấu hình trang chủ của
từng người hiện chỉ được giữ tạm. Đây là chuyện chung của màn cấu hình,
không riêng ô này.

Tắt cả nhóm Phiếu trình: không còn ô nào của nhóm, kể cả ô mới.

Hệ thống đếm chậm quá thời gian chờ: ô hiện 0 và trang vẫn mở bình thường,
không hiện lỗi. Đây là cách nhóm ô này đang xử lý sẵn, giữ nguyên.

CHƯA CHỐT — PHẦN TRÊN ĐIỆN THOẠI

1. Ứng dụng trên điện thoại có vẻ chưa có màn Phiếu trình nhận để biết. Chưa
   có màn đó thì ô trên điện thoại bấm vào không biết mở gì.
2. Trang chủ trên điện thoại chỉ bật sẵn một số ô đầu tiên, các ô sau người
   dùng phải tự bật. Nên "mặc định hiển thị" chưa chắc đạt được như trên web.
3. Phần ứng dụng do đội làm ứng dụng phát hành riêng, không đi cùng bản web.
   Người chưa cập nhật ứng dụng vẫn sẽ không thấy ô.

Chốt ba điểm này rồi mới thiết kế phần điện thoại.
```

---

## Nhãn nhỏ dán lên ảnh

| Dán ở đâu | Chữ |
|---|---|
| Cạnh ô thứ 6 trên ảnh nhóm ô trang chủ | `MỚI` |
| Dưới ảnh nhóm ô trang chủ | `Ô thứ 6, đứng cuối nhóm, sau ô Xin ý kiến` |
| Chéo lên ảnh màn Phiếu trình nhận để biết | `MÀN NÀY KHÔNG THAY ĐỔI` |
| Cạnh dòng mới trên ảnh Cấu hình trang chủ | `Dòng mới, mặc định đã tick` |
| Dưới ảnh chế độ gọn | `Hiện nay 1 ô · Mong muốn 2 ô` |

---

## Chữ dùng thống nhất

| Chỗ dùng | Chữ đúng | Đừng viết |
|---|---|---|
| Nhãn trên ô trang chủ | **Nhận để biết** | Phiếu trình nhận để biết · Nhận biết · Để biết |
| Tên nhóm ô | **Phiếu trình** | Tờ trình · Trình ký |
| Tên màn đích | **Phiếu trình nhận để biết** | Hộp nhận để biết |
| Tên màn cấu hình | **Cấu hình trang chủ** | Thiết lập trang chủ |
| Hai cách bày trang chủ | **đầy đủ** và **gọn** | simple mode · chế độ đơn giản hoá |
