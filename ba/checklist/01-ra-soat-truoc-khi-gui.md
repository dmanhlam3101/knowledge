# CHECKLIST 01 — RÀ SOÁT TÀI LIỆU TRƯỚC KHI GỬI

> **Nguồn:** 13 tiêu chí cấu trúc (A1–A13) và 12 tiêu chí nội dung (B1–B12) của
> `docs/rules/ba-spec-rule.md` — chính là bộ tiêu chí `/ba-review` dùng để chấm — viết lại dạng ô
> tick cho BA tự rà. Mục 3 lấy từ quy trình "Cách dùng khi nhận một yêu cầu" trong `knowledge/README.md`.
>
> **Dùng khi:** BA tự rà trước bước 6 của quy trình (README) — AI cũng kiểm đúng các ô này ở lớp L1. Viết xong tài liệu theo `templates/01-dac-ta-yeu-cau.md` (hoặc `02-yeu-cau-nho.md`),
> trước khi gửi DEV/Tester hoặc chạy `/ba-review`.
>
> **Ngưỡng `/ba-review` chấm ĐỦ ĐỂ CODE:** cấu trúc ≥ 11/13 · nội dung ≥ 10/12 · không có TBD
> BLOCKING · không có mâu thuẫn (B7).

**Tài liệu:** {{MÃ YC}} · **Phiên bản:** {{…}} · **Người rà:** {{…}} · **Ngày:** {{dd/mm/yyyy}}

---

## 1. Cấu trúc — đủ mục chưa? (A1–A13)

- [ ] **A1** Bảng lịch sử thay đổi: phiên bản · ngày · nội dung · **tên người** (không chỉ ghi vai trò).
- [ ] **A2** Bảng phê duyệt cho BA · DEV · Tester · Đại diện nghiệp vụ.
- [ ] **A3** Mục đích · bối cảnh · **bảng AS-IS/TO-BE** · phạm vi bị ảnh hưởng · thuật ngữ.
- [ ] **A4** Bảng vai trò **kèm mã vai trò hệ thống** · tiền điều kiện chung.
- [ ] **A5** Danh sách FR-nn có mã · mapping nguồn → đích (hoặc ghi "Không áp dụng").
- [ ] **A6** Bảng BR-nn · tên · mô tả.
- [ ] **A7** Mỗi UC có **Actor** · tiền điều kiện · luồng chính đánh số · luồng thay thế/ngoại lệ **trỏ tới EC-xx**.
- [ ] **A8** Bảng field đủ cột: loại · **bắt buộc · độ dài · mặc định** · quy tắc hiển thị.
- [ ] **A9** Bảng ngoại lệ EC-nn có nội dung.
- [ ] **A10** AC-nn dạng Given / When / Then.
- [ ] **A11** Ma trận role · traceability FR → BR → AC · regression tối thiểu.
- [ ] **A12** Mục kỹ thuật/CSDL có nhãn độ tin cậy (`VERIFIED_*` / `TBD_NOT_CONFIRMED`) + phạm vi KHÔNG đổi.
- [ ] **A13** Bảng TBD có **mã · câu hỏi · ảnh hưởng · mức · AI CHỐT · HẠN**.

**Điểm cấu trúc:** {{…}}/13 *(mục có tiêu đề nhưng để trống = 0 điểm)*

## 2. Nội dung — viết đúng chưa? (B1–B12)

- [ ] **B1** BR-nn liên tục, không trùng, không nhảy số.
- [ ] **B2** Mỗi BR có ≥ 1 AC (kể cả BR dạng "không ảnh hưởng X" → AC kiểm X không đổi).
- [ ] **B3** Mỗi AC có cột BR — không có AC "mồ côi".
- [ ] **B4** Mỗi AC đủ 3 vế, Given có dữ liệu cụ thể (số lượng, trạng thái).
- [ ] **B5** Đã tìm (Ctrl+F) và thay hết từ mơ hồ: *phù hợp · hợp lý · tương ứng · như hiện tại ·
      nhất quán với cơ chế hiện có · linh hoạt · nhanh chóng · thân thiện · nếu cần · tối ưu ·
      ngoài chủ đích · v.v.*
- [ ] **B6** Số lượng/ngưỡng có con số: `0..N`, "tối đa 20 MB", "≤ 3 giây".
- [ ] **B7** Đọc chéo từng cặp BR↔BR, BR↔AC, BR↔UC — không có hai chỗ nói khác nhau.
- [ ] **B8** AC nào phụ thuộc TBD chưa chốt đã đánh dấu `(giả định — chờ TBD-xx)`.
- [ ] **B9** Có danh sách phạm vi **KHÔNG** thay đổi.
- [ ] **B10** Mapping nguồn → đích có đủ: nguồn · đích · quy tắc chuyển · điều kiện.
- [ ] **B11** Mọi thông báo/popup ghi **nguyên văn** (bảng MSG-xx).
- [ ] **B12** Tên vai trò trong tài liệu map được sang mã vai trò thật (`VT`, `LDDV`, `TTDV`, `NV`…)
      (danh sách: `knowledge/_chung/thuat-ngu.md`).

**Điểm nội dung:** {{…}}/12

## 3. Đối chiếu tri thức dự án (không chấm điểm, nhưng hay bị bỏ sót)

- [ ] Đã xác định phân hệ theo bảng "Từ khóa → phân hệ" trong `knowledge/README.md`.
- [ ] Đã đọc `knowledge/<phân hệ>/tom-tat.md` (chi tiết: `nghiep-vu.md` + `dac-thu.md`); AS-IS trong tài liệu
      **khớp** tri thức. Khác → ghi rõ là thay đổi có chủ đích hay tri thức đã cũ. Dựa vào quy tắc [Hiện trạng]
      (chưa xác nhận) → đã nêu rõ hoặc đưa thành TBD.
- [ ] Đã đi hết mục 10 "Khi viết yêu cầu mới…" của `tom-tat.md` phân hệ bị đụng.
- [ ] Đã xem `knowledge/_chung/cau-hoi-mo.md` — có câu hỏi mở nào liên quan đến yêu cầu này không.
- [ ] Đã điền `templates/05-phan-tich-anh-huong.md` — đặc biệt Mobile, liên thông, báo cáo.
- [ ] Đã đi hết các nhóm trong `02-cau-hoi-lam-ro.md`; câu chưa trả lời được đã thành TBD.
- [ ] Đã dò `03-loi-hay-gap.md` — không lặp lại lỗi cũ.

## 4. Kết luận tự rà

- [ ] **Sẵn sàng gửi** — đạt ngưỡng ở trên.
- [ ] **Gửi kèm TBD** — còn TBD BLOCKING nhưng đã có người chốt và hạn.
- [ ] **Chưa gửi** — còn thiếu: {{…}}
