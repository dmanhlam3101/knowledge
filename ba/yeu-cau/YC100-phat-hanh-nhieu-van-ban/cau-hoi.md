# YC100 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1)

**Yêu cầu:** YC100 — Phát hành nhiều văn bản từ một dự thảo có nhiều file · **Gửi tới:** BA / người đề xuất ·
**Ngày gửi:** 02/10/2026 · **Cần phản hồi trước:** {{dd/mm/yyyy}}

> **Cách trả lời:** ghi phương án chọn (A / B / C…) vào dòng **Trả lời** của từng câu, thêm ý nếu cần. Câu nào phải
> hỏi người khác thì ghi tên người + hạn. Xong báo AI "đã trả lời xong YC100" để AI viết `dac-ta.md` bản 1.0.

## Phiếu ý tưởng (nguyên văn BA)

> Từ 1 vb dự thảo đc lãnh đạo ký duyệt có nhiều file gửi tới văn thư được phát hành cấp số phát hành thành nhiều vb

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | Một dự thảo nhiều file → văn thư cấp số ra nhiều văn bản |
| Ai dùng | Có | Lãnh đạo ký duyệt, văn thư cấp số |
| Vì sao | **Chưa** | Hỏi ở Q01 |
| Một tình huống thật | **Chưa** | Hỏi ở Q01 |
| Kết quả mong muốn | Một phần | Ra nhiều văn bản; chưa rõ số, file, nơi nhận của từng văn bản (Q03 → Q07) |
| Kênh web / mobile | **Chưa** | Hỏi ở Q09 |

**Phân hệ:** chính `van-ban/di` (cấp số) · liên quan `xu-ly-cong-viec` (file dự thảo, ký), `van-ban/so-van-ban`
(số, sổ), `van-ban/chuyen-van-ban` (chuyển sau cấp số), `ky-so` (ký nhiều file). **Cỡ: L** (≥ 2 phân hệ, có thể có
di động) → mẫu `templates/01` đầy đủ.

## Hiện trạng (AI dựng từ tri thức + đọc code)

**Đang chạy như sau:**

1. Người soạn tải được **nhiều file** vào ô *File dự thảo* (bắt buộc, pdf / doc / docx) (`xu-ly-cong-viec` BR-12;
   ô cho chọn nhiều file — `selectDocumentDraftFile.zul:28`). Lãnh đạo ký số được nhiều file một lượt (`ky-so` NV-04).
2. Người ký cuối ký xong → dự thảo *Đã ký duyệt* (giá trị 3) → vào tab *Chờ cấp số* của văn thư đơn vị ban hành;
   hoặc hệ thống tự cấp số nếu đủ điều kiện tự động ban hành (`van-ban/di` NV-01, NV-10).
3. **Một dự thảo cấp số ra đúng một văn bản đi**, một số, một sổ. Mọi file (dự thảo, phụ lục, sở cứ) được chép sang
   văn bản đi đó; file đổi tên theo số (`van-ban/di` NV-02).
4. Cấp số xong, màn *Chuyển văn bản* mở ngay cho văn bản vừa cấp; chỉ ban hành tự động mới tự chuyển tới nơi nhận dự
   kiến [Đã xác nhận] (`van-ban/di` NV-02, BR-36).
5. Hủy ban hành không thu hồi văn bản ở người nhận, không báo cho họ [Đã xác nhận] (`van-ban/di` BR-19).

**AI tìm thấy trong code — tri thức CHƯA ghi** (⚠ chưa xác minh có ai đang dùng, chưa đếm dữ liệu trên DB DEV):

6. **Form Cấp số có sẵn nút "Chia nhỏ văn bản" nhưng đang bị ẩn** (`issussDocument.zul:877-881`, `visible="false"`).
   Phần code đi kèm cho thêm từng "Văn bản con" (số, ký hiệu, trích yếu, chọn file) và kiểm số không trùng nhau, không
   trùng văn bản gốc (`DocumentLookUpVM.java:1344-1390`, `1479-1518`); khi cấp số, hệ thống tạo luôn các văn bản con
   (`TextController.java:1803-1893`).
7. **Sau khi cấp số, văn thư đã có nút "Chia nhỏ văn bản"** ở chi tiết văn bản có hơn 1 file (`popupVB.zul:4406`,
   `popupVB_issue_number.zul:3627`, `popupReplyDocument.zul:2645`, `detailVB_per_storage.zul:1756`), hai cách:
   - *Chia nhỏ tự động*: mỗi file chính thành một văn bản con; số = số tiếp theo sau số gốc; ký hiệu thay phần số;
     trích yếu = trích yếu gốc + "_" + tên file; **mỗi văn bản con kèm toàn bộ phụ lục**;
   - *Chia nhỏ thủ công*: văn thư tự khai từng văn bản con và chọn file.

   Văn bản gốc **vẫn giữ nguyên**, văn bản con gắn với văn bản gốc; bộ đếm số của sổ nhảy tới số lớn nhất đã dùng
   (`DocumentDAO.java:14032-14160`).

**Đối chiếu ý muốn với hiện trạng:**

| Ý muốn | Loại | Ghi chú |
|---|---|---|
| Văn thư cấp số một dự thảo ra nhiều văn bản | **Sửa** — đã có code nửa chừng (mục 6, 7) | Có thể là *mở lại và hoàn thiện* nút đang ẩn, không phải làm mới hoàn toàn — chờ Q02, Q03 |
| Mỗi văn bản có số riêng | **Sửa** quy tắc "1 dự thảo = 1 văn bản đi, 1 số" (`van-ban/di` NV-02) | Chờ Q04 |
| Không mâu thuẫn quy tắc [Đã xác nhận] nào | — | BR-19 (hủy ban hành không thu hồi) và BR-36 (chỉ tự động ban hành mới tự chuyển) vẫn áp dụng, xem Q07, Q08 |

> AI mặc định: nút **"Chia nhỏ văn bản" sau cấp số** (mục 7) **giữ nguyên, không đổi**. Nếu yêu cầu này thay thế nút
> đó thì ghi ở Q03.

## Câu hỏi

> BLOCKING = chưa trả lời thì DEV không code được / Tester không viết được testcase. BLOCKING xếp trước.

### Q01 · Tình huống thật · BLOCKING

**Hiện trạng:** phiếu chưa có ví dụ cụ thể, nên chưa biết các file là "cùng loại cho nhiều người" hay "khác loại".
**Câu hỏi:** Cho một ví dụ thật: loại văn bản gì, khoảng bao nhiêu file, vì sao phải tách thành nhiều văn bản?

- A. Nhiều văn bản **cùng loại, cùng nội dung chung**, mỗi file cho một người / một đơn vị (vd. quyết định nâng lương
  cho từng cán bộ, lãnh đạo ký một lượt).
- B. Nhiều văn bản **khác loại** đi cùng một hồ sơ trình (vd. một tờ trình + một quyết định + một công văn).
- C. Khác (ghi rõ).

**Đề xuất của AI:** A — nhưng cần BA xác nhận vì A và B dẫn tới cách khai thông tin khác nhau (Q05).
**Ảnh hưởng:** toàn bộ BR, AC. **Ai trả lời:** BA / người đề xuất (LĐVP).
**Trả lời:**

### Q02 · Ai quyết định tách, lúc nào · BLOCKING

**Hiện trạng:** dự thảo hiện không có chỗ đánh dấu "phát hành thành nhiều văn bản"; văn thư là người cấp số
(`van-ban/di` NV-02).
**Câu hỏi:** Ai quyết định dự thảo này sẽ ra nhiều văn bản?

- A. **Văn thư** quyết định ngay trên form Cấp số (gần với nút đang ẩn ở mục 6).
- B. **Người soạn** đánh dấu từ lúc soạn; lãnh đạo thấy khi ký; văn thư chỉ cấp số theo đó.
- C. Người soạn đánh dấu gợi ý, văn thư được sửa lại khi cấp số.

**Đề xuất của AI:** A — ít thay đổi nhất, lãnh đạo đã duyệt nội dung từng file khi ký.
**Ảnh hưởng:** màn dự thảo (nếu B / C), form Cấp số, tự động ban hành (Q09). **Ai trả lời:** BA / LĐVP.
**Trả lời:**

### Q03 · Có còn "văn bản gốc" không · BLOCKING

**Hiện trạng:** cơ chế chia nhỏ có sẵn giữ **một văn bản gốc chứa đủ file** và tạo thêm các văn bản con gắn với gốc;
văn bản gốc cũng chiếm một số trong sổ (mục 7).
**Câu hỏi:** Sau khi cấp số, kết quả là gì?

- A. **N văn bản ngang nhau**, mỗi văn bản một số, không có văn bản gốc; hệ thống chỉ ghi nhận chúng cùng xuất phát
  từ một dự thảo.
- B. **1 văn bản gốc + N văn bản con** (như chia nhỏ hiện có) — gốc cũng có số riêng.
- C. File đầu tiên là văn bản chính, các file sau là văn bản con của nó.

**Đề xuất của AI:** A nếu sổ văn bản không được có "số thừa" cho văn bản gốc; B nếu chấp nhận gốc có số (dùng lại
được code có sẵn nhiều nhất). Cần BA / văn thư chốt.
**Ảnh hưởng:** số trong sổ (Q04), chuyển (Q07), hủy (Q08), tra cứu. **Ai trả lời:** BA + văn thư đơn vị.
**Trả lời:**

### Q04 · Số và ký hiệu của từng văn bản · BLOCKING

**Hiện trạng:** cấp số gợi ý số tiếp theo của sổ, chặn số trùng trong sổ; bộ đếm chỉ tăng (`van-ban/di` BR-08,
BR-09). Chia nhỏ tự động hiện lấy số liên tiếp sau số gốc (mục 7).
**Câu hỏi:** Các văn bản được đánh số thế nào?

- A. Cùng một sổ, hệ thống **gợi ý số liên tiếp**, văn thư sửa được từng số; ký hiệu theo số.
- B. Văn thư **nhập tay** từng số.
- C. **Chung một số**, khác nhau ở ký hiệu (vd. 12a, 12b).

**Đề xuất của AI:** A.
**Ảnh hưởng:** form Cấp số, kiểm trùng số, bộ đếm sổ (`van-ban/so-van-ban`). **Ai trả lời:** BA + văn thư đơn vị.
**Trả lời:**

### Q05 · Thông tin khác của từng văn bản · BLOCKING

**Hiện trạng:** form Cấp số bắt buộc sổ, số, ký hiệu, thể loại, độ mật, độ khẩn, ngày văn bản, trích yếu… cho một văn
bản (`van-ban/di` BR-07). Chia nhỏ tự động chép hết từ văn bản gốc, chỉ đổi số, ký hiệu, trích yếu (mục 7).
**Câu hỏi:** Ngoài số, các văn bản khác nhau ở những gì?

- A. Giống hết nhau; chỉ khác số, ký hiệu, file; trích yếu tự ghép = trích yếu chung + tên file.
- B. Như A, nhưng văn thư **sửa được trích yếu** từng văn bản.
- C. Văn thư khai riêng cả thể loại, trích yếu, người ký… cho từng văn bản.

**Đề xuất của AI:** B (nếu Q01 = A); C (nếu Q01 = B).
**Ảnh hưởng:** form Cấp số, BR kiểm bắt buộc. **Ai trả lời:** BA.
**Trả lời:**

### Q06 · File nào thuộc văn bản nào · BLOCKING

**Hiện trạng:** chia nhỏ tự động coi mỗi file chính là một văn bản và gắn **toàn bộ phụ lục** vào mọi văn bản; chia
nhỏ thủ công để văn thư tự chọn (mục 7). Ô *File phụ lục* trên form dự thảo đang ẩn (`xu-ly-cong-viec` NV-04).
**Câu hỏi:** Chia file thế nào?

- A. Mỗi file trong *File dự thảo* = một văn bản; tài liệu sở cứ gắn vào tất cả.
- B. Văn thư tự chọn file cho từng văn bản (một văn bản có thể gồm nhiều file).
- C. A làm mặc định, văn thư sửa lại được.

**Đề xuất của AI:** C.
**Ảnh hưởng:** form Cấp số, đổi tên file sau cấp số. **Ai trả lời:** BA.
**Trả lời:**

### Q07 · Nơi nhận và chuyển văn bản · BLOCKING

**Hiện trạng:** sau cấp số, màn *Chuyển văn bản* mở ngay cho **một** văn bản; nơi nhận dự kiến khai ở dự thảo chỉ tự
chuyển khi ban hành tự động [Đã xác nhận] (`van-ban/di` NV-02, BR-36).
**Câu hỏi:** Các văn bản được gửi đi thế nào?

- A. Tất cả gửi **cùng** nơi nhận dự kiến của dự thảo.
- B. **Mỗi văn bản một nơi nhận riêng**; văn thư chuyển lần lượt từng văn bản.
- C. Văn thư tự chuyển sau, như văn bản thường (không mở màn Chuyển ngay).

**Đề xuất của AI:** B (hợp với Q01 = A: mỗi quyết định cho một người).
**Ảnh hưởng:** `van-ban/chuyen-van-ban`, tab *Đã ban hành*. **Ai trả lời:** BA.
**Trả lời:**

### Q08 · Hủy ban hành, xóa một văn bản trong nhóm · BLOCKING

**Hiện trạng:** hủy ban hành / xóa áp cho từng văn bản đi; dự thảo sang trạng thái 27 (`van-ban/di` NV-05, NV-15).
**Câu hỏi:** Khi một văn bản trong nhóm bị hủy ban hành hoặc xóa?

- A. Chỉ văn bản đó; các văn bản khác giữ nguyên, dự thảo vẫn *Đã ban hành*.
- B. Hủy cả nhóm.
- C. Hủy văn bản gốc thì hủy hết; hủy văn bản con thì chỉ con đó (chỉ khi Q03 = B).

**Đề xuất của AI:** A (hoặc C nếu Q03 = B).
**Ảnh hưởng:** trạng thái dự thảo, số trong sổ (cấp bù số trong ngày — `van-ban/di` BR-09). **Ai trả lời:** BA + văn thư.
**Trả lời:**

### Q09 · Phạm vi áp dụng · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** văn bản mật không có *Cấp số & Đóng dấu*, không tự chuyển (`van-ban/di` BR-12, BR-32); tự động ban
hành cấp số ngầm sau khi ký (NV-10); nghiệp vụ có (hoặc sẽ có) cấp số trên di động (NV-17, Q8).
**Câu hỏi:** Áp dụng cho những trường hợp nào? (chọn nhiều)

- A. Văn bản thường, văn thư cấp số thủ công trên **web**.
- B. Thêm *Cấp số & Đóng dấu*.
- C. Thêm dự thảo bật **tự động ban hành**.
- D. Thêm **văn bản mật**.
- E. Thêm **di động**.

**Đề xuất của AI:** chỉ A ở đợt này; B, C, D, E ghi vào phạm vi KHÔNG đổi.
**Ảnh hưởng:** phạm vi, ma trận testcase. **Ai trả lời:** BA.
**Trả lời:**

### Q10 · Người tạo và lãnh đạo thấy gì · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** cấp số xong người tạo dự thảo nhận một SMS / thông báo "được cấp số" (`van-ban/di` NV-02).
**Câu hỏi:** Sau khi phát hành thành nhiều văn bản?

- A. Dự thảo hiện *Đã ban hành* kèm **danh sách N văn bản** (số, ký hiệu); người tạo nhận **một** tin chung.
- B. Như A nhưng người tạo nhận **mỗi văn bản một** tin.
- C. Không đổi gì ở phía dự thảo.

**Đề xuất của AI:** A.
**Ảnh hưởng:** màn chi tiết dự thảo, SMS. **Ai trả lời:** BA.
**Trả lời:**

## Tổng hợp

| Mã | Nhóm | Mức | Đề xuất AI | Trả lời |
|---|---|---|---|---|
| Q01 | Tình huống | BLOCKING | A | |
| Q02 | Người quyết định | BLOCKING | A | |
| Q03 | Văn bản gốc | BLOCKING | A hoặc B | |
| Q04 | Số, ký hiệu | BLOCKING | A | |
| Q05 | Thông tin từng văn bản | BLOCKING | B / C | |
| Q06 | Chia file | BLOCKING | C | |
| Q07 | Nơi nhận | BLOCKING | B | |
| Q08 | Hủy, xóa | BLOCKING | A | |
| Q09 | Phạm vi | NON-BLOCKING | A | |
| Q10 | Hiển thị, thông báo | NON-BLOCKING | A | |

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 10 |
| BLOCKING chưa trả lời | 8 |
| Đã chốt | 0 |

## Ghi chú cho tri thức (không cần BA làm gì)

Mục 6, 7 (chia nhỏ văn bản lúc cấp số / sau cấp số) **chưa có trong `knowledge/van-ban/di`**. Bổ sung vào tri thức
sau khi YC100 chốt, kèm số liệu trên DB DEV (có văn bản con nào chưa).
