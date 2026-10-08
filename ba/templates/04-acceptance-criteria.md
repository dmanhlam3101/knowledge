# MẪU ACCEPTANCE CRITERIA

> **Nguồn:** bảng AC (mục 8) của tài liệu mẫu YC17 (đã gỡ khỏi repo)
> + tiêu chí B2, B3, B4, B8 trong `checklist/00-chuan-cham-dac-ta.md` + các lỗi AC mà review YC17 đã chỉ ra.
>
> Dùng để viết **mục 8** của `01-dac-ta-yeu-cau.md` hoặc **mục 9** của `02-yeu-cau-nho.md`.

---

## 1. Bảng AC

| AC ID | BR | Given (tiền điều kiện + dữ liệu cụ thể) | When (một hành động) | Then (kết quả kiểm được) | Ghi chú |
|---|---|---|---|---|---|
| AC-01 | BR-01 | {{…}} | {{…}} | {{…}} | |
| AC-02 | BR-02 | {{…}} | {{…}} | {{…}} | (giả định — chờ TBD-xx) |

## 2. Năm luật viết AC

1. **Mỗi BR có ≥ 1 AC; mỗi AC có cột BR.** Kể cả BR dạng "không ảnh hưởng X" — viết AC kiểm X không đổi.
2. **Given có dữ liệu cụ thể:** số lượng, trạng thái, vai trò. "Có văn bản" → "Văn bản đến có 2 Tài liệu liên quan và 1 File biểu mẫu".
3. **When chỉ một hành động.** Hai hành động → tách thành hai AC.
4. **Then kiểm được bằng mắt hoặc SQL:** con số, tên, trạng thái, thông báo nguyên văn (mã MSG-xx).
5. **AC phụ thuộc TBD chưa chốt → ghi `(giả định — chờ TBD-xx)`** ở cột Ghi chú. Không viết như đã chốt.

## 3. Ví dụ tốt / chưa tốt (lấy từ YC17)

| | Ví dụ | Vì sao |
|---|---|---|
| ✔ Tốt | **AC-01** — Given VB đến có 2 Tài liệu liên quan và 1 File biểu mẫu · When Chuyên viên chọn VB tại Link văn bản đến · Then Dự thảo hiển thị đủ 2 file tại Tài liệu liên quan và 1 file tại File biểu mẫu | Dữ liệu cụ thể, đếm được |
| ✘ Chưa tốt | **AC-09** — Then "Auto-fill vẫn hoạt động theo các BR đã định nghĩa và không nhân đôi file **ngoài chủ đích**" | "Ngoài chủ đích" không đo được. Sửa: "số file trong mỗi nhóm không tăng so với lần tự điền trước" |
| ✘ Chưa tốt | **AC-05** — Given "Dự thảo đã có một file được hệ thống xác định là trùng" | Tiêu chí "trùng" còn ở TBD-01 → phải đánh dấu giả định |

## 4. Nhóm AC nên có

| Nhóm | Câu hỏi | Bắt buộc khi |
|---|---|---|
| Happy path | Luồng chính chạy đúng? | Luôn luôn |
| Không có dữ liệu | Danh sách rỗng, số lượng 0? | Có danh sách/đếm |
| Biên | Tối đa, tối thiểu, đúng ngưỡng, vượt ngưỡng? | Có giới hạn số |
| Phân quyền | Vai trò không có quyền thấy/làm được gì? | Luôn luôn |
| Trạng thái | Thao tác ở trạng thái bị cấm? | Có trạng thái |
| Hủy / làm lại | Hủy giữa chừng, mở lại màn Sửa, bấm 2 lần? | Có form nhập |
| Regression | Chức năng cũ cạnh bên vẫn chạy như cũ? | Luôn luôn |
