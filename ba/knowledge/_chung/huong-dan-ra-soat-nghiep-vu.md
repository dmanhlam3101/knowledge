# Hướng dẫn rà soát & viết tri thức nghiệp vụ (dùng cho người và AI)

Áp dụng khi viết lại `nghiep-vu.md` / `dac-thu.md` / `vi-du-mau.md` của một phân hệ từ code thật.
`ban-do.md` luôn do máy sinh (`_tools/scan.py` + `_tools/gen.py`) — KHÔNG sửa tay.
Nhánh code chuẩn: `kha_develop` (cả `web-spring` và `backend2.0`).

## Nguồn

| Tầng | Vị trí |
|---|---|
| Web (ZK) | `web-spring/src/main/webapp/view/**.zul` · ViewModel `web-spring/src/main/java/com/viettel/voffice/vm/**`, widget `com/viettel/voffice/widget/**` · gọi BE qua `com/voffice/service/business/*Business.java` (key `a.b` → URL `/a/b`) · legacy: facade/DAO trong web (`com/viettel/vps/**`, `com/viettel/voffice/{facade,service,dao}/**`) |
| BE gen-1 | `backend2.0/backendvoffice/src/main/java/com/viettel/voffice/**` (action → controler → database/dao SQL thuần) |
| BE gen-2 | `backend2.0/backendvoffice/src/main/java/com/viettel/office/**` (controller → services → repositories JPA/native → entities) |
| Menu / widget | bảng `SYS_MENU`, `HOME_WIDGET` trên DB (không có trong code) — script tham khảo `backend2.0/backendvoffice/sql/*.sql` |
| Hằng số trạng thái | web `com/viettel/util/AppConstants.java`; BE `com/viettel/voffice/constants/*.java`, `com/viettel/office/utils/Constants.java` |
| HDSD cũ (tham khảo, KHÔNG phải nguồn sự thật) | `C:\Users\Admin\Desktop\HDSD\**` (đã chuyển sang md để đọc) — chỉ dùng để hiểu thuật ngữ/luồng người dùng; mọi khẳng định vẫn phải kiểm bằng code |

## Khung `nghiep-vu.md` bắt buộc (đúng thứ tự)

1. **Tổng quan** — phạm vi phân hệ (gồm gì / KHÔNG gồm gì, trỏ sang phân hệ khác), vai trò (actor) + mã role thật.
2. **Module** — bảng thành phần: màn hình (.zul) → VM → Business → endpoint → controller/service → DAO/repository, kèm file:dòng.
3. **Nghiệp vụ** — mỗi nghiệp vụ một mục `### NV-xx. <tên nghiệp vụ>`:
   - Mục đích (ngôn ngữ nghiệp vụ, không phải tên hàm)
   - Actor / vai trò / phân quyền (điều kiện quyền thật trong code)
   - Luồng xử lý: màn hình FE → API → Service → Repository/DB (tên file, class, method, endpoint; file:dòng)
   - Business rule & validation (điều kiện, ràng buộc) — đánh mã `BR-xx`
   - Trạng thái & chuyển trạng thái (nếu có)
   - Bảng dữ liệu liên quan
   - Tích hợp ngoài (job, queue, SMS/thông báo, API bên thứ 3, email, liên thông...)
   - Edge case / xử lý lỗi
4. **Sơ đồ** (Mermaid):
   - `flowchart` tổng quan module
   - `sequenceDiagram` cho mỗi nghiệp vụ chính
   - `stateDiagram-v2` cho mỗi entity có trạng thái
5. **Data model** — `erDiagram` các bảng chính + bảng mô tả cột quan trọng (vai trò nghiệp vụ). Chỉ vẽ quan hệ có bằng chứng trong code (JOIN/FK/entity mapping); quan hệ logic không có FK ghi chú rõ.
6. **Glossary** — thuật ngữ nghiệp vụ ↔ tên trong code (tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh).
7. **[CẦN XÁC NHẬN]** — gom mọi điểm chưa rõ ý đồ nghiệp vụ ở cuối file (kèm câu hỏi cụ thể cho BA/DEV), chia hai mục:
   - **7.1 Còn mở** — bảng `| # | Bối cảnh (hiện trạng code) | Câu hỏi |`, mã `Q1, Q2…`; không còn câu nào thì ghi "(Không còn câu hỏi mở …)".
   - **7.2 Đã xác nhận** — bảng câu đã trả lời (người trả lời, ngày) và sự thật do code / DB xác nhận (`X1, X2…`), cột "Ghi vào" trỏ NV / BR đã sửa theo câu trả lời. Sự thật đã chốt ở phân hệ trước được dùng lại thì liệt kê lại mã (vd. "X1–X6 dùng lại từ module trước").
   Mục 8 trở đi (nếu có) chỉ dành cho phụ lục (vd. thay đổi đang phát triển trên nhánh chưa merge) — không chen trước mục 7.

Đầu bài (blockquote ngay dưới tiêu đề): ngày viết lại + nhánh code; menu / số liệu đối chiếu DB DEV ngày nào, ai tra; bảng viết tắt
đường dẫn / lớp (`WEB/`, `ZUL/`, `BE1/`, `BE2/`, `SQL/`… và tên lớp viết tắt dùng trong bài); dòng "Phân hệ liền kề đã viết" nêu ký
hiệu tham chiếu sang bài khác. Mục 1 nên có thêm: bảng menu thật (DB DEV `SYS_MENU`), widget trang chủ (`HOME_WIDGET`), và
"Sửa so với knowledge cũ" (bảng: nội dung cũ | hiện trạng code | ghi vào) — khi trích lời bài cũ có dấu hỏi thì ghi `(?)`, không chép ký hiệu câu hỏi mở (dấu hỏi đỏ U+2753).

## Quy tắc viết

- Mọi khẳng định phải dẫn nguồn `đường-dẫn/File.java:dòng` (hoặc `File.java::method`), đường dẫn tương đối từ gốc workspace.
- Chỉ mô tả những gì có trong code, KHÔNG bịa, KHÔNG suy diễn. Code không rõ ý đồ nghiệp vụ → ghi `[CẦN XÁC NHẬN]` + câu hỏi cụ thể.
- `[CẦN XÁC NHẬN]` chỉ hỏi về **ý nghĩa / ý đồ nghiệp vụ**, viết bằng ngôn ngữ nghiệp vụ dễ hiểu, kèm bối cảnh ngắn (người trả lời là chủ dự án/BA, không đọc code).
  KHÔNG hỏi "có cần sửa / bổ sung kiểm tra quyền / IDOR không" — mục tiêu là xây tri thức, không sửa lỗi.
  Lỗi nghi vấn, thiếu kiểm tra, code chết, gõ nhầm → ghi vào `dac-thu.md` dạng "lỗi hệ thống — ghi nhận" kèm file:dòng.
  Quyền thao tác của hệ thống nằm ở tầng hiển thị nút trên web (BE không kiểm người gọi là thiết kế chung — đã xác nhận).
- Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh. Không dán code dài; trích điều kiện ngắn khi cần làm bằng chứng.
- Phần knowledge cũ còn đúng thì GIỮ (thêm nguồn); sai thì sửa và ghi `(sửa YYYY-MM-DD: lý do)`.
- Không truy vấn DB (chỉ đọc code). KHÔNG chạy lệnh git ghi. KHÔNG sửa code nguồn. Chỉ ghi file của phân hệ được giao.
- Thành phần bị xếp sai phân hệ trong `ban-do.md`: KHÔNG tự sửa `_tools/domains.py` — ghi vào báo cáo để người điều phối sửa tập trung.
- Mermaid: nhãn có ký tự đặc biệt (dấu ngoặc, dấu hai chấm, dấu /) phải đặt trong ngoặc kép; id node không dấu, không khoảng trắng.

## Quy ước bổ sung (chốt trong đợt viết lại 2026-09-29 → 2026-10-02)

- **Nguồn DB.** Tác giả bài không kết nối DB; số liệu DB do **người điều phối** tra DB DEV (chỉ SELECT) theo danh sách "cần tra DB" của bài. Ghi nguồn dạng
  **"DB DEV `<BẢNG>` ngày YYYY-MM-DD"** (vd. "DB DEV `SYS_MENU` ngày 2026-10-01") ngay cạnh số liệu; đầu bài ghi tổng các bảng đã đối chiếu. Số liệu DB là
  ảnh chụp tại ngày tra (số dòng, phân bố giá trị, comment cột, menu / widget), **không** thay được bằng chứng code. Bảng chưa tra ghi "chưa đối chiếu DB";
  phân hệ khác đã có số liệu thì **trỏ sang** (không tự tra lại).
- **Giá trị trạng thái** luôn ghi **số thật đang lưu** (vd. `SEND_TYPE` 1 / 2 / 3, nắm tình hình = 3 + `IS_INFORMALITY = 1`) kèm tên hằng; phân biệt rõ **mã lọc / mã hộp**
  (tham số tìm kiếm) với **giá trị cột**. Comment cột DB lệch code thì ghi cả hai và theo code.
- **Tham chiếu chéo** sang bài khác: `<ký hiệu> NV-xx` / `<ký hiệu> BR-xx` theo bảng ký hiệu ở `README.md` (`XLCV`, `VBĐi`, `VBĐ`, `CVB`, `LXL`, `SVB`, `LT`,
  `QLC`, `PT`, `LNV`, `NVu`, `CV`, `HSCV`, `KS`, `HT`), hoặc `` `<phân hệ>` NV-xx ``. Trước khi ghi phải mở bài đích kiểm NV đó tồn tại và đúng chủ đề.
  Không tự đặt ký hiệu khác (vd. `NV-nv-xx`, `VBDI`, `NVU`).
- **Sửa theo bài khác.** Sửa một sự thật vì phân hệ khác đã chốt (có trích code rõ hơn) → ghi tag **"(sửa chéo YYYY-MM-DD theo `<phân hệ>`)"** tại chỗ sửa.
  Sửa tri thức cũ của chính bài → "(sửa YYYY-MM-DD: lý do)". Hai bài mâu thuẫn mà không phân xử được bằng code → **không tự chọn**, ghi vào báo cáo cho người điều phối.
- **Ranh giới.** Mỗi nội dung chỉ viết chi tiết ở **một** phân hệ (bảng "KHÔNG gồm" của mục 1.1 chỉ đúng nơi); phân hệ khác chỉ nêu điểm gọi
  ("ở đây chỉ ghi gửi tin loại X khi Y") và trỏ sang.
- **Không ghi giá trị bí mật.** Mật khẩu, khóa (JWT, AES, client secret), token, tài khoản kết nối, **địa chỉ IP / URL máy chủ nội bộ** trong
  `application.properties` / `SYSTEM_PARAMETER`: chỉ ghi **tên khóa**, kèm "(có khai — không ghi giá trị)". Áp dụng cả khi trích lời bài cũ.
- **Lỗi chỉ ghi nhận ở `dac-thu.md`.** Lỗi nghi vấn, lỗ hổng bảo mật, thiếu kiểm tra, code chết, gõ nhầm → bảng "lỗi hệ thống — ghi nhận" (`L1, L2…`, cột nguồn `file:dòng`)
  trong `dac-thu.md`; `nghiep-vu.md` chỉ mô tả hành vi hiện tại (có thể trỏ "ghi nhận `dac-thu.md` Lx"). Không biến lỗi thành câu hỏi, không đề xuất sửa trong tri thức.
- **Câu hỏi chỉ hỏi ý đồ nghiệp vụ**, bằng lời người làm nghiệp vụ hiểu được (bối cảnh = hiện trạng hệ thống đang chạy thế nào, rồi hỏi "ý đồ là (a) … hay (b) …").
  Không hỏi "có cần sửa / thêm kiểm tra không". Câu hỏi đặt trong bảng `Qn` ở mục 7.1; không dùng ký hiệu câu hỏi mở (dấu hỏi đỏ U+2753) ở ngoài mục 7 — công cụ `_tools/questions.py` gom mọi dòng có ký hiệu đó thành danh sách việc (công cụ chưa đọc bảng `Qn` — xem `README.md`).
- **HDSD cũ** (`C:\Users\Admin\Desktop\HDSD\**`) chỉ dùng tham khảo thuật ngữ / tên màn; không phải nguồn sự thật.
- **Nhánh code.** Nếu repo đang checkout nhánh khác `kha_develop`, đọc file của `kha_develop` bằng lệnh git chỉ đọc (`git show kha_develop:<path>`) và ghi rõ ở đầu bài;
  thay đổi trên nhánh chưa merge chỉ ghi ở phụ lục (mục 8), không trộn vào hiện trạng.

## `dac-thu.md`

Bẫy, chỗ web và BE làm khác nhau, code legacy vs mới (gen-1/gen-2), logic trùng lặp giữa các màn (sửa một chỗ phải sửa chỗ nào nữa),
chỗ "đừng đụng", màn chết/VM không tồn tại, các cờ/tham số có hành vi bất ngờ — đều có file:dòng.

## `vi-du-mau.md`

2–4 tính năng THẬT tiêu biểu để copy pattern khi làm mới: đường dẫn đầy đủ zul → VM → Business → endpoint → service → DAO → bảng,
và ghi rõ nên copy phần nào.
