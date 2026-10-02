# {{MÃ YC}} — SỔ LỖI KIỂM TRA

> **Dùng trong vòng kiểm tra lặp** (README "Quy trình từng bước", bước 6–8). AI ghi lỗi vào đây mỗi vòng; BA xử lý từng
> dòng ngay trong file này. **Mã lỗi giữ nguyên qua các vòng** — không xóa dòng, chỉ đổi trạng thái — để biết vòng sau
> tốt hơn vòng trước bao nhiêu.
>
> **Mức lỗi**
> - **CHẶN** — DEV không code được hoặc sẽ code sai: mâu thuẫn nội bộ; mô tả sai hiện trạng hệ thống; mâu thuẫn với
>   quy tắc đã xác nhận; TBD chặn code chưa có người chốt; field / bảng / màn không tồn tại mà không nói là làm mới;
>   lớp 4 phải đoán ý.
> - **NẶNG** — thiếu mục / tiêu chí của `docs/rules/ba-spec-rule.md`; BR không có AC; AC thiếu vế; thông báo chưa
>   nguyên văn; từ mơ hồ ở BR / AC; thiếu phạm vi KHÔNG đổi.
> - **NHẸ** — câu chữ, định dạng, đánh số, thuật ngữ chưa thống nhất.
>
> **Lớp** (nơi phát hiện): `L1` hình thức · `L2` đúng nghiệp vụ hiện tại · `L3` làm được trên code / DB · `L4` thử làm
> DEV / Tester.
>
> **Trạng thái:** `Mở` (AI ghi) → BA đổi thành `Đã sửa` / `Không đồng ý: <lý do>` / `Chuyển câu hỏi: TBD-xx` → vòng sau
> AI kiểm lại: `Đóng` (đúng là đã ổn) hoặc `Mở lại` (chưa ổn, ghi vì sao).

**Tài liệu:** `{{dac-ta.md}}` · **BA:** {{…}}

## Tổng hợp theo vòng

| Vòng | Ngày | Phiên bản tài liệu | Cấu trúc A | Nội dung B | CHẶN mở | NẶNG mở | NHẸ mở | Kết luận vòng |
|---|---|---|---|---|---|---|---|---|
| 1 | {{dd/mm}} | {{1.0}} | {{x}}/13 | {{x}}/12 | {{n}} | {{n}} | {{n}} | {{CHƯA ĐẠT · GẦN ĐẠT · ĐẠT — DEV LÀM ĐƯỢC}} |

## Lỗi

| Mã | Vòng phát hiện | Mức | Lớp | Vị trí (mục / mã) | Trích nguyên văn | Vì sao là lỗi khi code / test | Đề xuất sửa (câu chữ cụ thể) | Trạng thái | Ghi chú vòng sau |
|---|---|---|---|---|---|---|---|---|---|
| E-01 | 1 | CHẶN | L2 | {{BR-03}} | "{{…}}" | {{Mâu thuẫn `van-ban/den` BR-28 [Đã xác nhận]: Phối hợp được tự hoàn thành}} | {{"…"}} | Mở | |

## Kết quả lớp 4 — thử làm DEV / Tester (vòng gần nhất)

> AI tự lập danh sách việc DEV và danh sách testcase **chỉ từ tài liệu**. Mỗi chỗ phải đoán / phải hỏi đã ghi thành lỗi
> ở bảng trên. Khi tài liệu ĐẠT, hai danh sách này được chuyển cho DEV / Tester làm điểm khởi đầu.

**Việc DEV (dự kiến):**

| # | Việc | Tầng (web / BE / DB / mobile) | Dựa trên (BR / UC / mục) |
|---|---|---|---|

**Testcase gợi ý:**

| # | Tên testcase | AC | Vai trò | Dữ liệu cần chuẩn bị |
|---|---|---|---|---|

## Điều kiện "ĐẠT — DEV LÀM ĐƯỢC" (tất cả phải đúng)

- [ ] 0 lỗi CHẶN ở trạng thái Mở / Mở lại
- [ ] 0 TBD mức BLOCKING chưa có câu trả lời
- [ ] Cấu trúc ≥ 11/13 và nội dung ≥ 10/12 theo `docs/rules/ba-spec-rule.md`; không có mâu thuẫn (B7)
- [ ] Mọi BR có ≥ 1 AC; mọi AC truy về BR
- [ ] Lớp 3: không còn BR nào "CHƯA RÕ" trên code; mapping bảng / cột khớp DB (thiếu cột → đã ghi cần migration)
- [ ] Lớp 4: lập được đủ việc DEV và testcase mà không phải đoán
- [ ] Lỗi NẶNG còn lại (nếu có) đều đã được BA ghi "Không đồng ý" có lý do hoặc chấp nhận rủi ro

> Đạt đủ → AI khuyến nghị **ĐẠT**; quyết định cuối là của DEV (ký mục Phê duyệt). Sau **3 vòng** vẫn còn lỗi CHẶN → AI
> dừng, liệt kê các điểm cần **họp chốt** với người quyết định thay vì kiểm tiếp.
