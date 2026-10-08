# YC_NV_06 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1 — BA đã trả lời đủ 8 câu ngày 08/10/2026)

**Yêu cầu:** YC_NV_06 — Xem được các file đính kèm trả lời "Nhắc việc" của các đơn vị · **Gửi tới:** BA / người đề
xuất · **Ngày gửi:** 08/10/2026 · **Cần phản hồi trước:** {{dd/mm/yyyy}}

> **Cách trả lời:** ghi phương án chọn (A / B / C…) vào dòng **Trả lời** của từng câu, thêm ý nếu cần. Câu nào phải
> hỏi người khác thì ghi tên người + hạn. Xong báo AI "đã trả lời xong YC_NV_06" để AI viết `dac-ta.md` bản 1.0.

## Phiếu ý tưởng (nguyên văn BA)

> Xem được các file đính kèm trả lời "Nhắc việc" của các đơn vị.
>
> Mô tả mong muốn: với văn bản tại sổ VB trả lời người dùng đang phải ấn vào màn chi tiết để xem file -> move file của
> văn bản này ra cột File văn bản ở màn danh sách cho người dùng xem luôn

Ảnh BA gửi (lưu ở `input/design/`):
- `01_luoi-theo-doi-nhac-viec.webp` — lưới *Theo dõi nhắc việc*, khoanh cột **Số VB trả lời**.
- `02_chi-tiet-vb-tra-loi-file-dinh-kem.png` — popup chi tiết văn bản trả lời, khoanh mục **File đính kèm**.
- `03_mau-cot-file-van-ban.png` — mẫu cột **File văn bản** ở màn danh sách văn bản khác (tên file + biểu tượng tải +
  "Xem thêm").

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | Thấy và mở được file của văn bản trả lời ngay trên lưới, không phải vào chi tiết |
| Ai dùng | **Một phần** | "các đơn vị" trả lời → người xem có lẽ là phía giao / theo dõi; chưa rõ có cả phía đơn vị được nhắc không → Q01 |
| Vì sao | Có | Phải bấm từng văn bản trả lời mở chi tiết mới thấy file — tốn thao tác khi duyệt nhiều trả lời |
| Một tình huống thật | **Chưa** | Hỏi ở Q01 |
| Kết quả mong muốn | Một phần | Có cột "File văn bản" giống ảnh 3 — chưa rõ file nào, giữ cột Số VB trả lời không, bấm file làm gì (Q02–Q05) |
| Kênh web / mobile | **Chưa** | Hỏi ở Q08 |

**Phân hệ:** chính `lich-nhac-viec` (màn *Theo dõi nhắc việc* — NV-01; trả lời kèm văn bản trả lời — NV-04) · liên
quan `van-ban/quan-ly-chung` (quyền xem văn bản / file và popup chi tiết dùng chung — QLC NV-06) và `van-ban/di` (văn
bản trả lời là văn bản đi; cách hiện cột "File văn bản" ở danh sách văn bản đi).

**Cỡ: S** → mẫu `templates/02-yeu-cau-nho.md`. Lý do: chỉ thêm **một cột hiển thị** trên một lưới; không đổi trạng
thái nhắc việc, không thêm bảng / cột DB (file đã gắn sẵn với văn bản trả lời). **Nâng lên M nếu** BA chọn làm cả trên
ứng dụng di động (Q08), hoặc chọn cho người chưa được xem văn bản trả lời cũng xem / tải được file (Q06 — đụng quy tắc
quyền xem văn bản dùng chung).

## Hiện trạng (AI dựng từ tri thức)

**Đang chạy như sau:**

1. Menu **VĂN BẢN ĐI > Theo dõi nhắc việc** (mã menu 441265) là một màn cho cả hai phía: nhóm *Cần xử lý* (đơn vị được
   nhắc, lãnh đạo theo dõi chờ duyệt) và nhóm *Giao đi/Theo dõi* (người tạo, người theo dõi). **Mỗi dòng lưới = một đơn
   vị được nhắc** của một nhắc việc (lich-nhac-viec NV-01).
2. Lưới có **9 cột**: Thao tác · Số, Ký hiệu · Trích yếu · Nội dung giao việc · Đơn vị xử lý · Trạng thái · **Số VB trả
   lời** · Hạn xử lý · Ngày tạo. **Chưa có cột file** — khớp đúng điều BA nêu (NV-01; `reminder_search.zul:315-324`).
3. Cột **Số VB trả lời** hiện `[số ký hiệu] trích yếu` của văn bản trả lời mà đơn vị đã chọn khi trả lời; bấm vào thì mở
   **popup chi tiết văn bản trả lời** — file nằm ở mục *File đính kèm* trong popup đó (ảnh 2) (NV-01; `ReminderVM.java:2473-2478`,
   `2897-2922`).
4. **Trả lời nhắc việc không có file đính kèm riêng** — chỉ gồm nội dung trả lời (bắt buộc) và văn bản trả lời (không
   bắt buộc) (NV-04). Vậy "file đính kèm trả lời" = **file của văn bản trả lời**. ⚠ Cần BA xác nhận đúng ý này (Q02).
5. Văn bản trả lời chỉ còn trên dòng **Chờ duyệt** và **Hoàn thành**: khi bị trả lại / hủy trả lời (về *Xử lý lại*) thì
   nội dung và văn bản trả lời bị xóa; dòng *Đã xử lý tạm* (văn bản trả lời chưa phát hành) **không hiện** trên lưới khi
   xem *Tất cả* (NV-04, NV-05 BR-18; NV-01 BR-03). Dòng chưa trả lời / trả lời không kèm văn bản thì cột Số VB trả lời trống.
6. Một lần trả lời **chọn được nhiều văn bản trả lời** (popup trả lời giữ một danh sách văn bản —
   `ReminderReplyVM.java:59`, `209`). ⚠ **Chưa xác minh:** khi đó lưới hiện thế nào — truy vấn danh sách nối văn bản trả
   lời không gộp nên có thể **lặp một dòng đơn vị cho mỗi văn bản** (`ReminderRepositoryImpl.java:63-65`). Sẽ kiểm trên
   DB DEV ở vòng kiểm lớp 3.
7. Mẫu cột **"File văn bản"** đã có ở các màn danh sách văn bản (ảnh 3): hiện **file chính** kèm biểu tượng tải; có
   **"Xem thêm"** khi văn bản có hơn một file, bấm ra popup liệt kê mọi file (bấm tên để xem, biểu tượng để tải); nút
   tải bị ẩn với văn bản không được tải / văn bản mật (`documentOut_search.zul:1222-1313`).
8. Quyền mở một văn bản theo **quy tắc chung**: người tạo, người nhận / người gửi, văn thư – lãnh đạo đơn vị ban hành /
   đơn vị nhận…; riêng đường "xem văn bản trả lời" có ngoại lệ cho xem (QLC NV-06). Văn bản trả lời được chuyển cho
   **đơn vị giao** với vai trò *Nhận để biết* (NV-04) — nên **người theo dõi nhắc việc chưa chắc là người nhận văn bản
   trả lời**. ⚠ Chưa xác minh hiện nay lãnh đạo / chuyên viên theo dõi bấm Số VB trả lời có mở được không (ghi là rủi
   ro, kiểm ở lớp 3).

**Đối chiếu ý muốn với hiện trạng:**

| Ý muốn | Loại | Ghi chú |
|---|---|---|
| Hiện file của văn bản trả lời ngay trên lưới Theo dõi nhắc việc, xem / tải không cần mở chi tiết | **Mới** (chỉ hiển thị) | File đã gắn với văn bản trả lời, không cần thêm dữ liệu |
| — | **Không mâu thuẫn** quy tắc nào đã xác nhận | Không đổi trạng thái nhắc việc, không đổi ai thấy dòng nào. Chỉ cần chốt quyền xem / tải file (Q06) để không vô tình nới quy tắc xem văn bản |

## Câu hỏi

> BLOCKING = chưa trả lời thì DEV không code được / Tester không viết được testcase. BLOCKING xếp trước.

### Q01 · Ai dùng, ở nhóm / tab nào, và một tình huống thật · BLOCKING

**Hiện trạng:** cùng một lưới phục vụ hai phía — *Cần xử lý* (đơn vị được nhắc, lãnh đạo theo dõi thấy trả lời chờ
mình duyệt) và *Giao đi/Theo dõi* (người tạo, người theo dõi) (NV-01).
**Câu hỏi:** Cho một ví dụ thật: ai mở lưới, ở tab nào, đang làm gì thì cần xem file trả lời? Cột mới hiện ở đâu?

- A. Hiện ở **mọi nhóm, mọi tab** — ai thấy dòng thì thấy cột (vd. lãnh đạo theo dõi ở tab *Chờ duyệt* mở file trả
  lời của 6 đơn vị để duyệt nhanh; đơn vị được nhắc xem lại file mình đã trả lời).
- B. Chỉ nhóm **Giao đi/Theo dõi** và tab **Chờ duyệt** của nhóm *Cần xử lý* (nơi phía giao đọc trả lời).
- C. Khác (ghi rõ, kèm ví dụ thật).

**Đề xuất của AI:** A — lưới hiện dùng chung một bộ cột cho mọi tab; ẩn / hiện theo tab là thêm điều kiện và thêm
testcase mà không thêm giá trị rõ rệt.
**Ảnh hưởng:** phạm vi, ma trận testcase theo tab / vai trò. **Ai trả lời:** BA.
**Trả lời:** A

### Q02 · "File đính kèm trả lời" là file nào · BLOCKING

**Hiện trạng:** trả lời nhắc việc **không có file riêng**, chỉ có văn bản trả lời (NV-04). Văn bản trả lời có thể gồm
**file chính** và **file đính kèm khác** (phụ lục, tài liệu kèm) — chi tiết văn bản hiện chung ở mục *File đính kèm*
(ảnh 2).
**Câu hỏi:** Cột mới hiện những file nào?

- A. **Mọi file của văn bản trả lời** — hiện file chính, các file còn lại vào "Xem thêm" (đúng như ảnh 3).
- B. **Chỉ file chính** của văn bản trả lời.
- C. Khác — ví dụ muốn thêm chức năng **đính kèm file trực tiếp khi trả lời** (không qua văn bản trả lời). Đây là tính
  năng mới, phải đổi popup Trả lời và thêm dữ liệu → cỡ M.

**Đề xuất của AI:** A — đúng mẫu đang dùng ở các danh sách văn bản, người dùng đã quen.
**Ảnh hưởng:** nguồn dữ liệu cột, cỡ yêu cầu. **Ai trả lời:** BA.
**Trả lời:** A

### Q03 · "Move" — giữ hay bỏ cột Số VB trả lời · BLOCKING

**Hiện trạng:** cột *Số VB trả lời* hiện số ký hiệu + trích yếu, bấm mở chi tiết văn bản trả lời (hiện trạng 3).
**Câu hỏi:** "Move file ra cột File văn bản" nghĩa là:

- A. **Giữ** cột *Số VB trả lời* như cũ, **thêm** cột mới **"File văn bản"** đứng ngay sau nó.
- B. **Gộp** vào cột *Số VB trả lời*: dòng trên là số ký hiệu / trích yếu, dưới là danh sách file (không thêm cột).
- C. **Thay** cột *Số VB trả lời* bằng cột "File văn bản" (không còn đường mở chi tiết văn bản trả lời từ lưới).

**Đề xuất của AI:** A — giữ đường mở chi tiết cho ai cần xem đầy đủ, đúng nhãn "cột File văn bản" BA nêu.
**Ảnh hưởng:** giao diện, testcase giao diện. **Ai trả lời:** BA.
**Trả lời:** Giữ cột Số VB trả lời như cũ, thêm cột mới "File văn bản" ở cuối bảng

### Q04 · Bấm vào file thì làm gì · BLOCKING

**Hiện trạng:** ở các danh sách văn bản, bấm **tên file** → mở trình xem file ngay trên hệ thống; bấm **biểu tượng tải**
→ tải file gốc về máy (ảnh 3; `documentOut_search.zul:1228-1239`).
**Câu hỏi:** Ở lưới nhắc việc:

- A. Giống danh sách văn bản: bấm tên file = **xem**, biểu tượng = **tải về**.
- B. Chỉ **xem** (không có nút tải trên lưới; muốn tải thì vào chi tiết).
- C. Chỉ **tải về**.

**Đề xuất của AI:** A.
**Ảnh hưởng:** AC, testcase. **Ai trả lời:** BA.
**Trả lời:** A

### Q05 · Một đơn vị trả lời kèm nhiều văn bản trả lời · BLOCKING

**Hiện trạng:** popup Trả lời cho chọn **nhiều** văn bản trả lời (hiện trạng 6). ⚠ Lưới hiện nay xử lý trường hợp này
chưa rõ (có thể lặp dòng).
**Câu hỏi:** Đơn vị X trả lời kèm 2 văn bản (VB1 có 1 file, VB2 có 3 file). Dòng của đơn vị X hiện gì?

- A. **Một dòng**, cột "File văn bản" hiện file của **cả hai văn bản**, nhóm theo từng văn bản (file chính VB1, file
  chính VB2, phần còn lại vào "Xem thêm").
- B. **Mỗi văn bản một dòng** (như lưới có thể đang làm), mỗi dòng hiện file của văn bản đó.
- C. Chỉ hiện file của **một** văn bản (văn bản chọn đầu tiên).

**Đề xuất của AI:** A — một dòng lưới đang được hiểu là "một đơn vị được nhắc"; lặp dòng làm sai số đếm và gây hiểu nhầm
đơn vị trả lời hai lần.
**Ảnh hưởng:** BR, testcase nhiều văn bản. **Ai trả lời:** BA.
**Trả lời:** mỗi dòng chỉ có 1 văn bản đính kèm

### Q06 · Ai được xem / tải file · BLOCKING

**Hiện trạng:** xem / tải file của một văn bản đi theo **quy tắc quyền xem văn bản dùng chung** (QLC NV-06). Văn bản
trả lời được chuyển cho đơn vị giao với vai trò *Nhận để biết*, nên **người theo dõi nhắc việc** (lãnh đạo / chuyên viên
theo dõi) **chưa chắc** là người được xem văn bản đó theo quy tắc chung (hiện trạng 8). Danh sách văn bản đi đang **ẩn
nút tải** với văn bản mật / văn bản không được tải (hiện trạng 7).
**Câu hỏi:** Người thấy dòng trên lưới thì xem / tải file thế nào?

- A. **Ai thấy dòng thì xem và tải được** file văn bản trả lời của dòng đó (người tạo, người theo dõi, đơn vị được
  nhắc) — kể cả khi không phải người nhận văn bản trả lời; văn bản mật thì **chỉ xem, không tải** như danh sách văn bản.
- B. **Theo đúng quy tắc xem văn bản hiện nay**: ai không có quyền xem văn bản trả lời thì vẫn thấy tên file nhưng bấm
  sẽ báo không có quyền.
- C. Chỉ người tạo nhắc việc và lãnh đạo theo dõi được xem / tải; người khác chỉ thấy tên file.

**Đề xuất của AI:** A — người theo dõi cần đọc trả lời để duyệt; đường "xem văn bản trả lời" đã có ngoại lệ cho xem ở
popup chi tiết (QLC NV-06), làm A là áp cùng ngoại lệ đó cho lưới.
**Ảnh hưởng:** quyền, ATTT, cỡ yêu cầu (B, C có thể kéo theo sửa quy tắc dùng chung). **Ai trả lời:** BA (cần lãnh đạo
dự án chốt nếu chọn A với văn bản mật).
**Trả lời:** theo nghiệp vụ hiện tại ai thấy bản ghi thì thấy file thì xem được thôi

### Q07 · Nhãn, vị trí cột và ô trống · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** thứ tự cột: Thao tác · Số, Ký hiệu · Trích yếu · Nội dung giao việc · Đơn vị xử lý · Trạng thái · Số VB
trả lời · Hạn xử lý · Ngày tạo (NV-01). Dòng chưa có văn bản trả lời thì cột Số VB trả lời để trống (hiện trạng 5).
**Câu hỏi:** (a) Nhãn cột? (b) Vị trí? (c) Dòng không có văn bản trả lời / văn bản không có file thì hiện gì?

- A. (a) **"File văn bản"** · (b) ngay **sau "Số VB trả lời"** · (c) **để trống**.
- B. (a) "File trả lời" · (b) như A · (c) như A.
- C. (a) "File văn bản" · (b) **cuối bảng** · (c) hiện chữ "Không có file".

**Đề xuất của AI:** A.
**Ảnh hưởng:** giao diện, testcase giao diện. **Ai trả lời:** BA.
**Trả lời:** cuối cùng của bảng

### Q08 · Kênh web / ứng dụng di động · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** nhắc việc là tính năng mới làm trên web; ⚠ tri thức **chưa ghi** ứng dụng di động có màn nhắc việc hay
không.
**Câu hỏi:** Làm cho kênh nào?

- A. **Chỉ web** đợt này; di động ghi vào phạm vi KHÔNG đổi.
- B. **Web + ứng dụng di động** (nếu di động có màn nhắc việc) → cỡ M, AI kiểm di động ở vòng kiểm.

**Đề xuất của AI:** A.
**Ảnh hưởng:** phạm vi, cỡ yêu cầu. **Ai trả lời:** BA.
**Trả lời:** B

## Tổng hợp

| Mã | Nhóm | Mức | Đề xuất AI | Trả lời |
|---|---|---|---|---|
| Q01 | Ai dùng, nhóm / tab, tình huống thật | BLOCKING | A | A — mọi nhóm, mọi tab |
| Q02 | File nào | BLOCKING | A | A — mọi file, file chính + "Xem thêm" |
| Q03 | Giữ / gộp / thay cột Số VB trả lời | BLOCKING | A | Giữ cột Số VB trả lời, thêm "File văn bản" ở cuối bảng |
| Q04 | Bấm file: xem / tải | BLOCKING | A | A — tên file = xem, biểu tượng = tải |
| Q05 | Nhiều văn bản trả lời | BLOCKING | A | Mỗi dòng chỉ có 1 văn bản → BR-02 (lưu ý lặp dòng → TBD-07) |
| Q06 | Ai được xem / tải file | BLOCKING | A | Ai thấy dòng thì xem được file → BR-07; tải + văn bản mật → TBD-02 |
| Q07 | Nhãn, vị trí, ô trống | NON-BLOCKING | A | Cuối bảng; nhãn + ô trống theo đề xuất → TBD-03 |
| Q08 | Web / di động | NON-BLOCKING | A | B — web + di động (cỡ M, TBD-01) |

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 8 |
| BLOCKING chưa trả lời | 0 |
| Đã chốt | 8 (phần còn mở chuyển sang TBD-01, 02, 03, 07 của `dac-ta.md`) |

## Ghi chú cho DEV / tri thức (không cần BA làm gì)

- **Chỗ sửa dự kiến:** truy vấn danh sách `RRI.searchReminders` (`ReminderRepositoryImpl.java:31-209`) đang chỉ lấy
  `DOCUMENT_ID / CODE / TITLE` của văn bản trả lời, **chưa lấy file** → phải bổ sung danh sách file (theo trang, tránh
  N+1) vào DTO trả về; web thêm cột ở `reminder_search.zul:315-324` + xử lý xem / tải trong `ReminderVM`, có thể dùng lại
  khối cột "File văn bản" của `documentOut_search.zul:1222-1313`. Không cần thêm cột DB.
- **Rủi ro lặp dòng:** `LEFT JOIN REMINDER_DOCUMENT_RELATIONS … OBJECT_TYPE = 2` không gộp (`ReminderRepositoryImpl.java:63-65`)
  — một trả lời có nhiều văn bản sẽ ra nhiều dòng, và số đếm phân trang có thể lệch. Kiểm trên DB DEV ở lớp 3 (đếm
  `REMINDER_REPLY` có > 1 liên kết `OBJECT_TYPE = 2` còn hiệu lực).
- **Quyền xem file:** `doViewDocumentReply` gọi `getDocumentDetail(id, null, null)` — chưa thấy truyền cờ
  `isViewReplyDocument` như popup chi tiết (QLC NV-06; `DDAO:16816`). Xem / tải file từ lưới đi qua kiểm quyền file
  (`SecurityVM.java:4058`, "không có quyền xem file") — cần chốt theo Q06 rồi kiểm ở lớp 3.
- Văn bản trả lời chưa phát hành chỉ có `TEXT_ID` (chưa có `DOCUMENT_ID`) nên hiện nay cột Số VB trả lời trống; các dòng
  đó ở *Đã xử lý tạm* và không hiện khi xem *Tất cả* (NV-01 BR-03); mã lọc 5 trên combobox là "Quá hạn", không phải
  trạng thái 5 (`dac-thu.md` bẫy 2) — nên cột mới không phải xử lý văn bản chưa phát hành.
