# {{MÃ YC}} — {{Tên yêu cầu ngắn gọn}}

> **HƯỚNG DẪN DÙNG MẪU** *(xóa khối này khi hoàn thiện)*
>
> **Nguồn dựng mẫu:** mẫu giải pháp BA của dự án (`knowledge/_chung/mau-dau-ra/giai-phap-ba.md`) +
> yêu cầu đã phân tích thật (`knowledge/yeu-cau/2026-09-15-loc-don-vi-nhan-khi-ban-hanh.md`), bổ sung
> mã BR/AC/TBD để truy vết được giống `01-dac-ta-yeu-cau.md`.
>
> **Dùng khi** yêu cầu **cỡ S**: đổi giao diện, đổi điều hướng, đổi nhãn/thứ tự, thêm/ẩn một trường,
> đổi điều kiện hiển thị — **không** đổi trạng thái, **không** thêm bảng/cột.
> Đụng trạng thái, thêm dữ liệu, hoặc ảnh hưởng ≥ 2 phân hệ → chuyển sang `01-dac-ta-yeu-cau.md`.
>
> Mục không áp dụng ghi "Không áp dụng — lý do: …". Chỗ chưa chắc → mục 8, không đoán.

| Thuộc tính | Giá trị |
|---|---|
| Phân hệ (knowledge) | {{`van-ban/di`}} |
| Cỡ | S |
| Kênh | {{Web · Mobile · Cả hai}} |
| Người lập · Ngày | {{Họ tên}} · {{dd/mm/yyyy}} |
| Phiên bản · Trạng thái | {{1.0}} · {{DRAFT / READY_FOR_DEV}} |

---

## 1. Yêu cầu gốc & mục tiêu

- **Yêu cầu gốc** (trích nguyên văn): "{{…}}"
- **Vấn đề hiện tại:** {{người dùng đang gặp khó gì}}
- **Kết quả mong muốn:** {{đo được — VD: từ Dashboard tới tab Chờ xử lý chỉ cần 1 lần click}}

## 2. Phạm vi

- **Trong phạm vi:** {{màn hình/vùng/thao tác}}
- **Ngoài phạm vi:** {{những gì KHÔNG đổi — ghi rõ để khoanh regression}}

## 3. Vai trò

| Vai trò | Mã hệ thống | Thấy | Thao tác |
|---|---|---|---|
| {{Văn thư}} | `VT` | {{Có}} | {{Có}} |
| {{Chuyên viên}} | `NV` | {{Có}} | {{Không}} |

## 4. Hiện trạng (AS-IS) → Thay đổi (TO-BE)

| STT | Nội dung | Hiện tại | Yêu cầu | Nguồn AS-IS |
|---|---|---|---|---|
| 1 | {{Điều hướng "Chờ phê duyệt"}} | {{Dashboard → Văn thư → Văn bản trình duyệt → tab Chờ xử lý}} | {{Dashboard → Văn bản trình duyệt → tab Chờ xử lý}} | {{`knowledge/…/nghiep-vu.md` / quan sát trên DEV ngày …}} |

**Không thay đổi:** {{dữ liệu · trạng thái văn bản · phân quyền · API}}

## 5. Quy tắc nghiệp vụ

| Mã | Quy tắc |
|---|---|
| BR-01 | {{Khi người dùng click … tại …, hệ thống mở … và chọn sẵn tab …}} |
| BR-02 | {{Chỉ hiển thị … với vai trò …}} |
| BR-03 | {{Khi số lượng = 0: vẫn hiển thị, giá trị 0 / ẩn}} |

## 6. Màn hình, điều hướng & thông báo

| Màn hình · vùng | Thay đổi | Điều kiện hiển thị | Tab/bộ lọc mặc định |
|---|---|---|---|
| {{Dashboard · Xử lý công việc}} | {{…}} | {{…}} | {{…}} |

**Thông báo (nguyên văn):** {{"…" hoặc "Không có thông báo mới"}}

## 7. Tác động

| Hạng mục | Ảnh hưởng? | Ghi chú |
|---|---|---|
| Phân hệ khác | {{Không}} | |
| Mobile | {{Không / Có — …}} | |
| Liên thông · Ký số | {{Không}} | |
| Báo cáo · Dashboard · KPI | {{…}} | |
| Dữ liệu cũ | {{Không cần xử lý}} | |

## 8. Câu hỏi cần chốt

| Mã | Câu hỏi (có phương án) | Ảnh hưởng | Ai chốt | Hạn | Kết luận |
|---|---|---|---|---|---|
| TBD-01 | {{Sau khi điều hướng có giữ bộ lọc cũ không? A. Giữ / B. Về mặc định}} | BR-01 | {{…}} | {{…}} | |

## 9. Tiêu chí nghiệm thu

| Mã | BR | Given | When | Then |
|---|---|---|---|---|
| AC-01 | BR-01 | {{Văn thư có 3 văn bản chờ phê duyệt}} | {{Click "Chờ phê duyệt" trên Dashboard}} | {{Mở màn Văn bản trình duyệt, tab Chờ xử lý đang chọn, hiển thị 3 văn bản}} |
| AC-02 | BR-03 | {{Không có văn bản chờ phê duyệt}} | {{Mở Dashboard}} | {{…}} |
| AC-03 | — | {{Regression}} | {{Vào Văn bản trình duyệt từ menu như cũ}} | {{Hoạt động như hiện tại}} |
