# CHECKLIST 03 — LỖI HAY GẶP TRONG TÀI LIỆU BA

> **Nguồn:** các phát hiện trong báo cáo review thật của tài liệu mẫu YC17 v2.1 (kết luận CHƯA ĐỦ, cấu trúc 10/13,
> nội dung 6/12; tài liệu và báo cáo đã gỡ khỏi repo — cột "Nguồn" ghi YC17 là lỗi rút từ đó) + các vòng kiểm sau này.
>
> **Cách dùng:** rà nhanh trước khi gửi. **Mỗi lần vòng kiểm (`/ba-assistant kiem`) phát hiện lỗi mới đáng nhắc → thêm
> một dòng**, ghi rõ tài liệu nguồn (mã YC). File này lớn dần theo dự án.

| # | Lỗi | Tiêu chí | Ví dụ thực tế | Cách tránh | Nguồn |
|---|---|---|---|---|---|
| 1 | TBD không có người chốt và hạn | A13 | 10 TBD BLOCKING, bảng TBD chỉ có 3 cột → kết luận CHƯA ĐỦ | Dùng bảng TBD của mẫu (có cột Ai chốt · Hạn · Mức) | YC17 |
| 2 | AC viết như đã chốt trong khi TBD còn mở | B8 | AC-05..07 về "file trùng" trong khi tiêu chí trùng (TBD-01) chưa chốt | Đánh dấu `(giả định — chờ TBD-xx)` | YC17 |
| 3 | BR không có AC | B2 | BR-08 (xóa file), BR-11 (không ảnh hưởng file khác) | Rà ma trận truy vết — mọi BR phải có AC | YC17 |
| 4 | Từ mơ hồ | B5 | "tránh bản ghi trùng **ngoài chủ đích**", "**nhất quán với cơ chế hiện có**" | Thay bằng điều kiện đếm được: "số bản ghi không tăng" | YC17 |
| 5 | UC không có Actor, không trỏ tới ngoại lệ | A7 | UC-01..06 | Dùng bảng thuộc tính UC ở `templates/03-use-case.md` | YC17 |
| 6 | Bảng field thiếu cột | A8 | Thiếu Bắt buộc / Độ dài / Mặc định | Ghi "Giữ nguyên baseline" thay vì bỏ cột | YC17 |
| 7 | Tên vai trò không khớp hệ thống | B12 | Chuyên viên / Văn thư / Lãnh đạo không map được sang vai trò thật | Thêm cột "Mã vai trò hệ thống" (`VT`, `LDDV`, `NV`…) | YC17 |
| 8 | Chưa xác định nguồn dữ liệu / COPY hay REFERENCE | B10 | TBD-09, TBD-10 chặn toàn bộ yêu cầu | Hỏi sớm (nhóm 2.5 của `02-cau-hoi-lam-ro.md`) trước khi viết BR chi tiết | YC17 |
| 9 | Thông báo không có nguyên văn | B11 | Nội dung popup file trùng (TBD-03), thông báo lỗi file nguồn (TBD-07) | Bảng MSG-xx, ghi nguyên văn từng chuỗi | YC17 |
