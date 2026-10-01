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
7. **[CẦN XÁC NHẬN]** — gom mọi điểm chưa rõ ý đồ nghiệp vụ ở cuối file (kèm câu hỏi cụ thể cho BA/DEV).

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

## `dac-thu.md`

Bẫy, chỗ web và BE làm khác nhau, code legacy vs mới (gen-1/gen-2), logic trùng lặp giữa các màn (sửa một chỗ phải sửa chỗ nào nữa),
chỗ "đừng đụng", màn chết/VM không tồn tại, các cờ/tham số có hành vi bất ngờ — đều có file:dòng.

## `vi-du-mau.md`

2–4 tính năng THẬT tiêu biểu để copy pattern khi làm mới: đường dẫn đầy đủ zul → VM → Business → endpoint → service → DAO → bảng,
và ghi rõ nên copy phần nào.
