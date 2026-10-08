# CHUẨN CHẤM TÀI LIỆU ĐẶC TẢ CỦA BA

> File này định nghĩa **kiểm cái gì** và **chấm thế nào** khi AI kiểm `dac-ta.md` (skill `ba-assistant`, chế độ
> `kiem`). Mục tiêu không phải bắt lỗi BA, mà trả lời một câu: *"tài liệu này đã đủ để DEV code và Tester viết
> testcase mà không phải hỏi lại chưa?"*
>
> Dùng ở vòng kiểm 4 lớp (`../README.md`): **L1 hình thức** = Phần A + B · **L3 làm được trên code** = Phần C ·
> kết luận vòng = Phần D · cách viết sổ lỗi = Phần E. Mã `[A1..A13]` trong mẫu `templates/01-dac-ta-yeu-cau.md` khớp
> Phần A. Bản ô tick để BA tự rà: `01-ra-soat-truoc-khi-gui.md`.

## PHẦN A — CẤU TRÚC (format)

| # | Mục bắt buộc | Đạt khi |
|---|---|---|
| A1 | Lịch sử thay đổi | có bảng phiên bản · ngày · người · nội dung sửa |
| A2 | Phê duyệt / xác nhận | có ô ký cho BA · DEV · Tester (hoặc VTS) |
| A3 | Thông tin chung | mục đích · bối cảnh nghiệp vụ · **phạm vi chức năng bị ảnh hưởng** · thuật ngữ |
| A4 | Phạm vi và vai trò | bảng vai trò + quyền · tiền điều kiện chung |
| A5 | Tổng quan yêu cầu chức năng | danh sách yêu cầu có mã · mapping dữ liệu nguồn → đích |
| A6 | **Business Rules** | bảng `BR-nn` · tên rule · mô tả |
| A7 | **Luồng nghiệp vụ / Use case** | `UC-nn` có actor · tiền điều kiện · luồng chính đánh số · luồng phụ/ngoại lệ |
| A8 | Đặc tả màn hình và trường dữ liệu | bảng field: tên · kiểu · bắt buộc · độ dài · mặc định · quy tắc hiển thị |
| A9 | Xử lý ngoại lệ và trường hợp biên | bảng tình huống → hành vi mong đợi |
| A10 | **Acceptance Criteria** | `AC-nn` dạng **Given / When / Then** |
| A11 | Ma trận kiểm thử và truy vết | ma trận role · **traceability Requirement → BR → AC** · regression tối thiểu |
| A12 | Phạm vi kỹ thuật & mapping CSDL | call-chain · mapping **UI → Code → DTO/API → CSDL** · CRUD & lifecycle · phạm vi KHÔNG đổi |
| A13 | Điểm cần xác nhận (TBD) | mỗi TBD có **mã · câu hỏi cụ thể · người chịu trách nhiệm · ảnh hưởng tới BR nào** |

Thiếu mục → ghi `THIẾU`. Có mục nhưng rỗng/chỉ có tiêu đề → ghi `RỖNG` (nặng ngang thiếu).
Yêu cầu cỡ S (mẫu `02-yeu-cau-nho.md`) được gộp mục theo mẫu đó; chỉ chấm thiếu khi nội dung của mục không có ở đâu.

## PHẦN B — CHẤT LƯỢNG NỘI DUNG (chỗ tài liệu hay hỏng)

| # | Tiêu chí | Cách kiểm |
|---|---|---|
| B1 | **Mọi BR có mã, duy nhất** | grep `BR-\d+`; không trùng, không nhảy số |
| B2 | **Mọi BR có ≥1 AC** | đối chiếu ma trận truy vết; BR không có AC = **không kiểm thử được** |
| B3 | **Mọi AC truy về ≥1 BR** | AC mồ côi = yêu cầu không có cơ sở nghiệp vụ |
| B4 | **AC đúng Given/When/Then** | đủ 3 vế; thiếu Given = không biết tiền điều kiện để dựng test |
| B5 | **Không có từ mơ hồ** | quét: *phù hợp · hợp lý · tương ứng · như hiện tại · linh hoạt · nhanh chóng · thân thiện · nếu cần · tối ưu · v.v.* → phải quy về giá trị/điều kiện đo được |
| B6 | **Số lượng/ngưỡng cụ thể** | "một hoặc nhiều file" phải nói rõ `0..N`; "độ dài phù hợp" phải có số |
| B7 | **Không mâu thuẫn nội bộ** | đối chiếu từng cặp BR và BR↔AC; BR nói "luôn ghi đè" mà AC nói "hỏi xác nhận" = mâu thuẫn |
| B8 | **TBD không được chặn AC** | TBD đang khoá một BR mà BR đó đã có AC "chốt" → AC đang giả định, phải đánh dấu |
| B9 | **Có phạm vi KHÔNG thay đổi** | thiếu thì không khoanh được vùng regression |
| B10 | **Mapping nguồn → đích đủ cột** | nguồn (bảng.cột) · đích (bảng.cột) · quy tắc chuyển đổi · điều kiện áp dụng |
| B11 | **Thông báo người dùng ghi nguyên văn** | "hiển thị thông báo lỗi" chưa đủ — cần chuỗi chính xác để test so khớp |
| B12 | **Ma trận role khớp vai trò thật** | đối chiếu mã vai trò thật trong `knowledge/he-thong/tom-tat.md` §2 và `knowledge/_chung/thuat-ngu.md` |

## PHẦN C — ĐỐI CHIẾU VỚI CODE (lớp L3)

| # | Kiểm | Kết luận có thể |
|---|---|---|
| C1 | Màn hình/field BA nêu có tồn tại trong code | `KHỚP` · `KHÔNG TÌM THẤY` (BA ghi sai tên, hoặc phải làm mới) |
| C2 | Bảng/cột trong mapping CSDL đúng schema thật | `KHỚP` · `SAI TÊN` · `CHƯA TỒN TẠI → cần migration` |
| C3 | Call-chain BA mô tả có khớp code | `KHỚP` · `LỆCH` (nêu call-chain thật) |
| C4 | Mỗi BR: code hiện tại đã có / chưa có / đang làm KHÁC | kèm `file::hàm::dòng` |
| C5 | Hàm/service bị đụng có caller ngoài module không | đếm số caller → mức rủi ro hồi quy |
| C6 | TBD nào **chặn việc code** | `BLOCKING` · `NON-BLOCKING` |
| C7 | Ước lượng thô | số file phải sửa · có cần migration · có đụng bảng dùng chung |

Nguồn đối chiếu: code nhánh `kha_develop` (`web-spring/`, `backend2.0/`); schema lấy từ DB DEV Oracle (chỉ SELECT
`ALL_TAB_COLUMNS` / `ALL_CONSTRAINTS`) hoặc, khi không kết nối được, từ ảnh chụp DB đã ghi trong `knowledge/` kèm
ngày chụp.

**Luật cứng:** mọi kết luận phải trích được bằng chứng (`file::hàm::dòng`, tên bảng/cột từ schema thật). Không tìm
thấy sau khi grep ≥3 cách (tên field, tên hàm, chuỗi thông báo) → ghi `CHƯA RÕ` và hỏi, **không kết luận "BA sai"**.

## PHẦN D — CHẤM ĐIỂM VÀ KẾT LUẬN

Mỗi tiêu chí A và B: `Đạt` = 1, `Thiếu/Sai` = 0.
**Điểm cấu trúc** = số A đạt / 13 · **Điểm nội dung** = số B đạt / 12

| Mức điểm | Điều kiện |
|---|---|
| **ĐỦ ĐỂ CODE** | Cấu trúc ≥ 11/13 · Nội dung ≥ 10/12 · **không có TBD BLOCKING** · không mâu thuẫn (B7) |
| **CẦN BỔ SUNG** | thiếu ≤ 3 tiêu chí · không mâu thuẫn · TBD blocking đã có người và hạn chốt |
| **CHƯA ĐỦ** | thiếu > 3 tiêu chí · hoặc có mâu thuẫn nội bộ · hoặc TBD blocking chưa có người chịu trách nhiệm |

Mức điểm này là **một điều kiện** của kết luận vòng trong sổ lỗi (`templates/07-so-loi-kiem-tra.md`): kết luận
**ĐẠT — DEV LÀM ĐƯỢC** cần mức ĐỦ ĐỂ CODE **và** các điều kiện còn lại cuối mẫu 07 (0 lỗi CHẶN, L4 không còn chỗ phải
đoán...). Kết luận là **khuyến nghị**, quyền quyết vẫn của BA/DEV. Báo cáo phải nêu *thiếu gì và sửa thế nào*, không
chỉ chấm điểm — mỗi điểm trừ kèm **gợi ý câu chữ cụ thể** để BA sửa được ngay.

## PHẦN E — GIỌNG BÁO CÁO

Viết cho BA đọc: mỗi phát hiện gồm **trích nguyên văn chỗ có vấn đề** → **vì sao là vấn đề khi code/test** → **đề
xuất sửa thành gì**. Không dùng từ phán xét, không bắt lỗi chính tả vặt.
Thứ tự ưu tiên: mâu thuẫn > TBD blocking > BR thiếu AC > mơ hồ > thiếu mục.
