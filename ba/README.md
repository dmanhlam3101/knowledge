# AI Analysis/ba — Bộ BA của VOffice Khánh Hòa (mẫu · checklist · tri thức · quy trình)

Bộ tài liệu dành cho BA của dự án **Hệ thống Văn bản và Điều hành tỉnh Khánh Hòa**. BA viết đặc tả **cùng AI**:
BA nói ý muốn và trả lời câu hỏi; AI tra tri thức hệ thống, soạn, kiểm và kiểm lại cho đến khi tài liệu **DEV làm được**.
Đường dẫn trong bộ này tính từ thư mục `AI Analysis/ba/`.

## Cấu trúc

```
AI Analysis/ba/
├── README.md                          ← bạn đang đọc (quy trình từng bước ở dưới)
├── knowledge/                         TRI THỨC HỆ THỐNG (repo git riêng) — BA đọc knowledge/<phân hệ>/tom-tat.md
├── templates/
│   ├── 01-dac-ta-yeu-cau.md           Đặc tả đầy đủ 11 mục (yêu cầu cỡ M/L) — có phiếu ý tưởng + nhãn ai viết mục nào
│   ├── 02-yeu-cau-nho.md              Đặc tả rút gọn 9 mục (yêu cầu cỡ S: đổi giao diện/điều hướng)
│   ├── 03-use-case.md                 Khối use case chi tiết (dùng cho mục 5 của mẫu 01)
│   ├── 04-acceptance-criteria.md      Bảng AC + luật viết + ví dụ tốt/chưa tốt
│   ├── 05-phan-tich-anh-huong.md      Ảnh hưởng GÓC NGHIỆP VỤ (BA tự làm, không cần đọc code)
│   ├── 06-danh-sach-cau-hoi.md        Danh sách câu hỏi gửi khách hàng/nghiệp vụ chốt
│   ├── 07-so-loi-kiem-tra.md          SỔ LỖI của vòng kiểm tra lặp (AI ghi, BA xử lý, giữ mã qua các vòng)
│   └── 08-kich-ban-kiem-thu.xlsx      KHUÔN Excel kịch bản kiểm thử của đội kiểm thử (5 sheet) — skill `kich-ban-kiem-thu`
├── _tools/
│   ├── gen_kich_ban_kiem_thu.py       Sinh file .xlsx kịch bản kiểm thử từ khuôn + spec JSON
│   └── vi-du-kich-ban.json            Spec mẫu, đúng chuẩn viết bước và tiền điều kiện
├── checklist/
│   ├── 01-ra-soat-truoc-khi-gui.md    Tự chấm theo 13 + 12 tiêu chí của /ba-review
│   ├── 02-cau-hoi-lam-ro.md           Ngân hàng câu hỏi 9 nhóm (2.9 = đặc thù Văn phòng số)
│   └── 03-loi-hay-gap.md              Lỗi thật đã gặp khi review (bổ sung dần)
└── yeu-cau/                           NƠI LÀM VIỆC: mỗi yêu cầu một thư mục <YCxx>-<ten-ngan>/
```

## Quy trình từng bước — từ lúc nhận yêu cầu đến lúc DEV làm được

Mỗi yêu cầu có một thư mục `yeu-cau/<YCxx>-<ten-ngan>/` gồm 3 file: `dac-ta.md` (tài liệu chính) · `cau-hoi.md`
(mẫu 06) · `so-loi.md` (mẫu 07). AI tạo giúp ở bước 2. Lệnh gõ trong Claude Code; có thể nói bằng lời thường thay lệnh
("viết đặc tả cho YC20…", "kiểm lại YC20 giúp tôi").

| Bước | BA làm gì | AI làm gì | Xong khi |
|---|---|---|---|
| **1. Ghi ý tưởng** (5–10 phút) | Viết **phiếu ý tưởng** 6 dòng (mục 0 mẫu 01): muốn gì · ai dùng · vì sao · **một tình huống thật** · kết quả mong muốn · kênh web/mobile. Dán vào chat hoặc gửi file | — | Có đủ 6 dòng |
| **2. Gọi AI soạn** | Gõ `/ba-assistant soan YC20` kèm phiếu ý tưởng | Xác định phân hệ + cỡ S/M/L · đọc `tom-tat.md` dựng **hiện trạng** · đối chiếu ý muốn với quy tắc đang có · tạo thư mục làm việc · ghi **câu hỏi vòng 1** vào `cau-hoi.md` (≤ 10 câu, có phương án, câu chặn code lên đầu) | BA nhận được danh sách câu hỏi |
| **3. Trả lời câu hỏi** | Trả lời ngay trong `cau-hoi.md` (chọn phương án). Câu nào cần sếp / khách chốt thì gửi họ, ghi người + hạn | Không làm gì (chờ) | Câu chặn code đã có trả lời hoặc có người chốt + hạn |
| **4. AI viết bản 1** | Báo AI "đã trả lời xong" | Viết `dac-ta.md` theo mẫu 01 (hoặc 02): giữ nguyên lời BA ở mục 🟦, điền mục 🟩 (hiện trạng, mapping, kỹ thuật), soạn mục 🟨 (BR, UC, màn hình, ngoại lệ, AC). Chỗ còn chưa rõ → TBD | Có `dac-ta.md` bản 1.0 |
| **5. BA đọc và sửa** | Đọc các mục 🟦 và 🟨 (không cần đọc mục 🟩). Sửa thẳng vào file chỗ nào không đúng ý | — | BA thấy đúng ý mình |
| **6. AI kiểm (một vòng)** | Gõ `/ba-assistant kiem YC20` | Kiểm **4 lớp** (bảng dưới), ghi lỗi vào `so-loi.md`, chấm điểm, kết luận vòng: **CHƯA ĐẠT / GẦN ĐẠT / ĐẠT** | Có kết luận vòng |
| **7. BA xử lý sổ lỗi** | Với từng lỗi `Mở`: sửa tài liệu rồi ghi `Đã sửa` · hoặc `Không đồng ý: <lý do>` · hoặc `Chuyển câu hỏi` nếu cần người khác chốt | Có thể sửa hộ nếu BA nói "sửa theo đề xuất E-03, E-05" | Không còn lỗi `Mở` BA chưa xử lý |
| **8. Lặp 6 → 7** | — | Từ vòng 2 chỉ kiểm lại **chỗ đã sửa + chỗ bị kéo theo + lỗi còn mở**; lỗi `Đã sửa` thật sự ổn → `Đóng`, chưa ổn → `Mở lại` | Kết luận **ĐẠT — DEV LÀM ĐƯỢC** (điều kiện ở cuối mẫu 07) |
| **9. Bàn giao DEV** | Gửi `dac-ta.md` cho DEV; DEV đọc kèm **danh sách việc + testcase gợi ý** (phần lớp 4 trong `so-loi.md`) và ký mục Phê duyệt | Đổi trạng thái tài liệu `READY_FOR_DEV` | DEV ký duyệt |
| **10. Mở việc** | Báo AI "mở CR" (hoặc chạy `/ba-review` nếu cần chấm chính thức có lưu hồ sơ) | Mở CR (`scripts/new_cr.ps1`), copy đặc tả làm đầu vào; câu trả lời nào làm rõ **hệ thống hiện tại** → cập nhật vào `knowledge/` | CR đã mở |

**Luật dừng:** sau **3 vòng** vẫn còn lỗi CHẶN → AI dừng kiểm, liệt kê các điểm cần **họp chốt** với người quyết định.

### 4 lớp kiểm của mỗi vòng (bước 6)

| Lớp | Câu hỏi lớp đó trả lời | AI kiểm gì | Dựa vào |
|---|---|---|---|
| **L1 · Hình thức** | Viết đúng chuẩn chưa? | Đủ 13 mục A1–A13, 12 tiêu chí B1–B12; mã BR/AC liên tục; từ mơ hồ; thông báo nguyên văn | `docs/rules/ba-spec-rule.md`, `checklist/01`, `checklist/03` |
| **L2 · Đúng nghiệp vụ hiện tại** | Tài liệu có hiểu đúng hệ thống đang chạy không? | Hiện trạng (AS-IS) khớp tri thức; vai trò, trạng thái, menu là **giá trị thật**; BR mới có **mâu thuẫn** quy tắc [Đã xác nhận] không; có đụng câu hỏi còn mở (mục 7.1) không | `knowledge/<phân hệ>/tom-tat.md`, `nghiep-vu.md` |
| **L3 · Làm được trên code** | Code / DB có chỗ để làm không? | Màn / field / nút có thật; bảng / cột có trong DB (thiếu → cần migration); chỗ bị sửa có bao nhiêu nơi khác gọi tới (rủi ro hồi quy); nghiệp vụ có bản sao ở tầng khác (web cũ, BE cũ / mới, mobile) | code `kha_develop` + DB DEV (chỉ đọc) |
| **L4 · Thử làm DEV / Tester** | DEV và Tester có làm được mà **không phải hỏi lại** không? | AI tự lập **danh sách việc DEV** và **danh sách testcase** chỉ từ tài liệu; mỗi chỗ phải đoán = một lỗi | chính tài liệu |

L4 là phép thử quyết định: tài liệu "DEV làm được" khi AI đóng vai DEV/Tester mà không còn câu nào phải hỏi.

### Hai cách dùng khác

- **BA tự viết, chỉ nhờ kiểm:** bỏ bước 2–4, viết thẳng theo mẫu 01/02 rồi bắt đầu từ bước 6.
- **Có sẵn file .docx:** `/ba-assistant viet-lai <file.docx>` → AI chuyển sang mẫu, ghi chỗ thiếu thành câu hỏi → tiếp từ bước 3.
- **Chấm chính thức có lưu hồ sơ** trong `features/<MA>/ba/`: dùng `/ba-review <MA> <BA-id>` (cùng chuẩn chấm, có gate duyệt).
- **Xuất kịch bản kiểm thử cho đội kiểm thử** sau khi đặc tả đạt: `/kich-ban-kiem-thu <MÃ>` → file `.xlsx` theo khuôn
  `templates/08-kich-ban-kiem-thu.xlsx`, lưu ở `yeu-cau/<YC>/testcase/`. Khác `/gen-testcase` (KBKT của pipeline DEV).

## Cách dùng thủ công (không có AI)

```
Nhận yêu cầu
  → Chọn mẫu: cỡ S → templates/02 · cỡ M/L → templates/01
  → Đọc knowledge/<phân hệ>/tom-tat.md (hiện trạng, mục 10 = điều phải ghi rõ)
  → Đi qua checklist/02 (câu hỏi làm rõ) → câu chưa rõ ghi vào templates/06 gửi người chốt
  → Viết tài liệu (UC theo templates/03, AC theo templates/04)
  → Điền templates/05 (ảnh hưởng nghiệp vụ)
  → Tự rà bằng checklist/01 + checklist/03
  → Gửi DEV/Tester hoặc chạy /ba-review (chấm điểm + đánh giá ảnh hưởng code)
  → Lỗi mới phát hiện khi review → thêm vào checklist/03
```

**Chọn cỡ yêu cầu:**

| Cỡ | Dấu hiệu | Mẫu |
|---|---|---|
| S | Đổi giao diện, điều hướng, nhãn, điều kiện hiển thị · không đổi trạng thái · không thêm dữ liệu | `02-yeu-cau-nho.md` |
| M | Thêm/sửa nghiệp vụ trong 1 phân hệ · có đổi trạng thái hoặc dữ liệu | `01-dac-ta-yeu-cau.md` |
| L | Chức năng mới · ảnh hưởng ≥ 2 phân hệ · tích hợp/liên thông · Mobile | `01-dac-ta-yeu-cau.md` đầy đủ + NFR |

## Nguồn của bộ tài liệu

Mọi nội dung đều lấy từ tài liệu **có sẵn trong dự án**, trừ phần NFR tham khảo chuẩn quốc tế.
Mỗi file đều ghi nguồn ở đầu file.

| Nguồn | Dùng cho |
|---|---|
| `features/XULYCONGVIEC/ba/BA-01-yc17-du-thao/input/spec.md` — tài liệu YC17 v2.1, "chuẩn vàng" của dự án | Khung 11 mục, use case, AC, mapping CSDL, TBD |
| `features/XULYCONGVIEC/ba/BA-01-yc17-du-thao/ba-review-report.md` — báo cáo review YC17 | Các cột/mục bổ sung để không bị trừ điểm; checklist 03 |
| `docs/rules/ba-spec-rule.md` — bộ tiêu chí `/ba-review` dùng để chấm | Mã `[A1..A13]` trong mẫu; checklist 01 |
| `knowledge/_chung/thuat-ngu.md`, `knowledge/he-thong/tom-tat.md` | Mã vai trò thật (`VT` / `LDDV` / `TTDV` / `NV`…), mã trạng thái ký, `SEND_TYPE`, `DEL_FLAG` |
| `knowledge/README.md` | Bảng từ khóa → phân hệ; bước đối chiếu tri thức |
| `knowledge/_chung/mau-dau-ra/giai-phap-ba.md` + `knowledge/yeu-cau/2026-09-15-loc-don-vi-nhan-khi-ban-hanh.md` | Mẫu 02 (rút gọn), mẫu 05 (ảnh hưởng) |
| ISO/IEC/IEEE 29148:2018 · Volere Requirements Specification Template | Nhóm yêu cầu phi chức năng (mục 3.3 mẫu 01, nhóm 2.8 checklist 02) |

## Quan hệ với các file khác trong repo

- `docs/rules/ba-spec-rule.md` vẫn là **bộ tiêu chí chấm chính thức** của `/ba-review`. Bộ này không
  thay thế mà giúp BA viết đạt chuẩn đó ngay từ đầu. Sửa rule → cập nhật `checklist/01` cho khớp.
- `docs/templates/ba-review-report.template.md` và `ba-feasibility.template.md` là **đầu ra của
  `/ba-review`**, không phải mẫu cho BA viết.
- Mục NFR (3.3 trong mẫu 01) **chưa được tính điểm** trong `ba-spec-rule.md`.
