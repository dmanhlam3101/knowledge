# YC_NV_08 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1 — BA đã trả lời đủ 9 câu ngày 08/10/2026)

**Yêu cầu:** YC_NV_08 — Thêm hạn xử lý ở Danh sách người cùng nhận · **Gửi tới:** BA / người đề xuất ·
**Ngày gửi:** 07/10/2026 · **Cần phản hồi trước:** {{dd/mm/yyyy}}

> **Cách trả lời:** ghi phương án chọn (A / B / C…) vào dòng **Trả lời** của từng câu, thêm ý nếu cần. Câu nào phải
> hỏi người khác thì ghi tên người + hạn. Xong báo AI "đã trả lời xong YC_NV_08" để AI viết `dac-ta.md` bản 1.0.

## Phiếu ý tưởng (nguyên văn BA)

> Thêm hạn xử lý ở Danh sách người cùng nhận (hiện tại hệ thống ko hiển thị nếu lãnh đạo giao hạn)

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | Danh sách người cùng nhận phải hiện **hạn xử lý** của từng dòng |
| Ai dùng | **Chưa** | Chưa rõ ai cần xem (lãnh đạo, văn thư, chuyên viên nhận văn bản?) → Q01 |
| Vì sao | Một phần | Lãnh đạo giao hạn khi chuyển nhưng người xem danh sách không thấy hạn đó → không biết ai phải xong khi nào |
| Một tình huống thật | **Chưa** | Hỏi ở Q01 |
| Kết quả mong muốn | Một phần | Có cột hạn xử lý — chưa rõ hiện hạn của ai, không có hạn thì hiện gì (Q04, Q05) |
| Kênh web / mobile | **Chưa** | Hỏi ở Q09 |

**Phân hệ:** chính `van-ban/quan-ly-chung` (popup chi tiết văn bản dùng chung, nơi đặt panel người cùng nhận — QLC
NV-05 mục "Popup chi tiết `popupVB.zul` — phần dùng chung") · liên quan `van-ban/den` (hạn xử lý, sắp đến hạn / quá hạn
— VBĐ NV-12) và `van-ban/chuyen-van-ban` (hạn nhập khi chuyển — CVB BR-19).

**Cỡ: S** → mẫu `templates/02-yeu-cau-nho.md`. Lý do: chỉ thêm **một cột hiển thị** vào một panel; không đổi trạng
thái, không thêm bảng / cột DB (hạn đã lưu sẵn trên dòng nhận). **Nâng lên M nếu** BA chọn hiển thị cả trên ứng dụng
di động (Q09), hoặc chọn tô màu quá hạn (Q07) vì phải lấy thêm trạng thái xử lý của từng dòng.

## Hiện trạng (AI dựng từ tri thức)

**Đang chạy như sau:**

1. Panel **"Danh sách người/ đơn vị cùng nhận"** nằm trong popup chi tiết văn bản (panel thu gọn được, chỉ hiện khi có
   dữ liệu), gồm **8 cột**: STT · Ngày chuyển · Người chuyển · Đơn vị chuyển · Người nhận · Đơn vị nhận · Ý kiến chỉ đạo
   (kèm file) · Yêu cầu trả lời. **Không có cột hạn xử lý** — khớp đúng điều BA nêu (QLC NV-05; `popupVB.zul:2204-2232`).
   Mỗi dòng của panel = **một lần chuyển tới một người / một đơn vị**.
2. Panel thứ hai trên cùng popup, **"Danh sách đã gửi đi"** (phía người chuyển, có nút thu hồi) gồm: STT · thao tác ·
   đơn vị nhận · ngày chuyển · ý kiến chuyển · yêu cầu trả lời · trạng thái trả lời · trạng thái xử lý · đã đọc —
   **cũng không có hạn xử lý** (QLC NV-05; `popupVB.zul:1319-1420`).
3. **Hạn xử lý luôn do người dùng nhập tay**, có ba đường vào: văn thư nhập khi **tiếp nhận** vào sổ đến · người dùng
   nhập khi **nhập văn bản đến thủ công** · người chuyển nhập trong **popup Chuyển văn bản** (VBĐ NV-12 BR-44).
4. Hạn nhập ở popup Chuyển văn bản là **hạn chung cho cả lần chuyển đó**, được ghi vào từng dòng nhận mới (cá nhân và
   đơn vị) — tức **dữ liệu hạn đã có sẵn trên từng dòng** của danh sách người cùng nhận (CVB BR-19).
   Một văn bản chuyển nhiều lần thì các dòng có thể **có hạn khác nhau**, và có dòng **không có hạn** (người chuyển bỏ
   trống).
5. **Không có chức năng gia hạn** — hạn của một dòng nhận không sửa được sau khi chuyển (VBĐ BR-46).
6. "Sắp đến hạn" / "Quá hạn" ở **hộp việc** tính theo ngày hạn và tham số cảnh báo trước (tính bằng giờ); **thống kê**
   tiến độ dùng công thức khác (hạn + 1 ngày). Hai chỗ đang tính khác nhau và điều này **đã được xác nhận là đúng
   nghiệp vụ** (VBĐ NV-12 BR-45).
7. Chức năng **Cho ý kiến** của lãnh đạo (bút phê) **không có trường hạn** — chỉ có nội dung ý kiến. Nên "lãnh đạo giao
   hạn" trên hệ thống hiện nay **chỉ xảy ra khi lãnh đạo chuyển văn bản** và nhập hạn trong popup chuyển
   (VBĐ NV-07; CVB BR-19). ⚠ Cần BA xác nhận đúng ý này không (Q03).
8. ⚠ **Chưa xác minh:** ứng dụng di động có màn / mục tương đương "người cùng nhận" hay không, và nếu có thì lấy dữ
   liệu từ đâu. Tri thức chưa ghi; sẽ kiểm ở vòng kiểm lớp 3 sau khi BA chốt Q09.

**Đối chiếu ý muốn với hiện trạng:**

| Ý muốn | Loại | Ghi chú |
|---|---|---|
| Hiện hạn xử lý trên từng dòng của Danh sách người cùng nhận | **Mới** (chỉ hiển thị) | Dữ liệu đã có trên dòng nhận, không cần thêm cột DB (CVB BR-19) |
| — | **Không mâu thuẫn** quy tắc nào đã xác nhận | Không đổi cách tính hạn, không đổi trạng thái, không đổi quyền |

## Câu hỏi

> BLOCKING = chưa trả lời thì DEV không code được / Tester không viết được testcase. BLOCKING xếp trước.

### Q01 · Ai dùng và một tình huống thật · BLOCKING

**Hiện trạng:** panel người cùng nhận hiện cho mọi người mở được chi tiết văn bản đó (lãnh đạo, văn thư, chuyên viên),
nội dung giống nhau cho mọi người (QLC NV-05).
**Câu hỏi:** Cho một ví dụ thật: ai mở danh sách này, để làm gì, thiếu cột hạn thì họ gặp khó ra sao? Ai là người dùng
chính?

- A. **Lãnh đạo / văn thư đơn vị** mở chi tiết văn bản để xem đã giao cho ai, hạn từng người là bao giờ, nhắc ai chậm.
- B. **Người cùng nhận** (chuyên viên phối hợp) mở để biết người chủ trì phải xong khi nào mà phối hợp theo.
- C. Cả A và B — cột hạn hiện như nhau cho mọi người thấy panel.
- D. Khác (ghi rõ, kèm ví dụ thật).

**Đề xuất của AI:** C — panel hiện nay không phân biệt người xem, thêm cột cho một nhóm sẽ phải thêm điều kiện mới.
**Ảnh hưởng:** phạm vi vai trò, dữ liệu test. **Ai trả lời:** BA.
**Trả lời:** C

### Q02 · Đúng danh sách nào · BLOCKING

**Hiện trạng:** trên cùng popup chi tiết có **hai** danh sách gần giống nhau: *Danh sách người/ đơn vị cùng nhận* (ai
cũng thấy, 8 cột) và *Danh sách đã gửi đi* (phía người chuyển, có nút thu hồi, có trạng thái xử lý và đã đọc) — cả hai
đều chưa có hạn (QLC NV-05).
**Câu hỏi:** Thêm cột hạn xử lý vào danh sách nào?

- A. Chỉ **Danh sách người/ đơn vị cùng nhận**.
- B. Cả hai danh sách.
- C. Chỉ **Danh sách đã gửi đi**.

**Đề xuất của AI:** A — đúng tên BA nêu, ít ảnh hưởng nhất. Nếu người dùng thật ra đang xem danh sách kia thì chọn C.
**Ảnh hưởng:** phạm vi màn, số testcase. **Ai trả lời:** BA.
**Trả lời:** A

### Q03 · "Lãnh đạo giao hạn" là hạn nào · BLOCKING

**Hiện trạng:** hệ thống có ba chỗ ghi hạn: hạn **sổ đến** (văn thư nhập khi tiếp nhận) · hạn **nhập tay** khi thêm văn
bản đến · hạn **của lần chuyển** (người chuyển nhập trong popup Chuyển văn bản, áp cho mọi người nhận của lần đó).
Chức năng Cho ý kiến của lãnh đạo **không có trường hạn** (VBĐ NV-12 BR-44, NV-07; CVB BR-19).
**Câu hỏi:** Hạn mà BA muốn thấy là hạn nào?

- A. **Hạn của lần chuyển** — lãnh đạo nhập khi bấm Chuyển văn bản, mỗi dòng trong danh sách hiện hạn của lần chuyển
  sinh ra dòng đó.
- B. **Hạn của văn bản / sổ đến** — một giá trị chung cho cả văn bản, mọi dòng hiện cùng một hạn.
- C. Hạn lãnh đạo **viết trong nội dung ý kiến chỉ đạo** (vd. "xử lý trước 10/10") — hệ thống hiện **không có trường
  riêng** cho hạn này, phải thêm trường mới (đổi cỡ yêu cầu sang M).
- D. Khác (ghi rõ).

**Đề xuất của AI:** A — đúng nghĩa "lãnh đạo giao hạn" trên hệ thống hiện nay và dữ liệu đã có sẵn.
**Ảnh hưởng:** nguồn dữ liệu cột mới, cỡ yêu cầu. **Ai trả lời:** BA.
**Trả lời:** hạn xử lý được người chuyển chọn ở popup Chuyển văn bản

### Q04 · Mỗi dòng hiện hạn của ai · BLOCKING

**Hiện trạng:** một văn bản có thể được chuyển nhiều lần, mỗi lần nhập một hạn khác; dòng nhận của **cá nhân** và dòng
nhận của **đơn vị** lưu hạn riêng (CVB BR-19; VBĐ NV-12).
**Câu hỏi:** Ví dụ: lãnh đạo chuyển cho ông A hạn 10/10; hôm sau trưởng phòng chuyển tiếp cho bà B hạn 15/10; và một
dòng chuyển cho **đơn vị X** hạn 20/10. Cột hạn hiện gì trên từng dòng?

- A. **Hạn của chính dòng đó** → A: 10/10 · B: 15/10 · đơn vị X: 20/10 (mỗi dòng một hạn riêng).
- B. **Hạn mới nhất** của văn bản → cả ba dòng hiện 20/10.
- C. **Hạn của văn bản / sổ đến** → cả ba dòng hiện cùng hạn ghi ở sổ đến.

**Đề xuất của AI:** A — đúng dữ liệu đang lưu, và trả lời được câu "ai phải xong khi nào".
**Ảnh hưởng:** BR chính, testcase nhiều lần chuyển. **Ai trả lời:** BA.
**Trả lời:** A mỗi lần chuyển cá nhân hay đơn vị sẽ lưu vào Doc_in_staff và doc in group mà

### Q05 · Dòng không có hạn thì hiện gì · BLOCKING

**Hiện trạng:** hạn khi chuyển là **không bắt buộc** (trừ khi có KPI), nên nhiều dòng nhận không có hạn (CVB BR-19,
NV-04 bước 3).
**Câu hỏi:** Dòng nhận không có hạn thì cột hạn hiện gì?

- A. **Để trống**.
- B. Hiện chữ **"Không có hạn"**.
- C. **Lấy hạn của văn bản / sổ đến** thay thế (và ghi chú là hạn của sổ).

**Đề xuất của AI:** A — đồng nhất với các cột khác của panel (ô không có dữ liệu để trống).
**Ảnh hưởng:** AC, testcase. **Ai trả lời:** BA.
**Trả lời:** A

### Q06 · Áp cho chiều văn bản nào · BLOCKING

**Hiện trạng:** popup chi tiết `popupVB.zul` là **popup dùng chung**, mở từ nhiều màn và cho cả **văn bản đến** lẫn
**văn bản đi** (và từ tra cứu, theo dõi đơn vị, hồ sơ…). Hạn xử lý là khái niệm của **văn bản đến**; văn bản đi sau khi
ban hành thường không có hạn xử lý (QLC NV-05; VBĐ NV-12).
**Câu hỏi:** Cột hạn hiện ở những chiều nào?

- A. Chỉ **văn bản đến**; mở chi tiết văn bản đi thì **không hiện cột**.
- B. Cả **văn bản đến và văn bản đi**; văn bản đi không có hạn thì để trống.
- C. Hiện ở mọi nơi mở popup này (gồm cả tra cứu, theo dõi đơn vị, hồ sơ, phiếu trình).

**Đề xuất của AI:** B — một cột thêm vào panel dùng chung sẽ hiện ở mọi đường mở; làm A phải thêm điều kiện ẩn / hiện
theo chiều văn bản (thêm việc cho DEV và thêm testcase).
**Ảnh hưởng:** phạm vi, ma trận testcase theo màn. **Ai trả lời:** BA.
**Trả lời:** Cả văn bản đến và văn bản đi(văn bản đã ban hành)

### Q07 · Có đánh dấu quá hạn / sắp đến hạn không · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** panel người cùng nhận **không có cột trạng thái xử lý** (không biết dòng đó đã hoàn thành chưa), nên tô
màu "quá hạn" sẽ tô cả dòng đã hoàn thành đúng hạn. Hộp việc và thống kê đang dùng hai công thức quá hạn khác nhau
(VBĐ NV-12 BR-45).
**Câu hỏi:** Cột hạn chỉ hiện ngày, hay có cảnh báo màu?

- A. **Chỉ hiện ngày** (dd/MM/yyyy), không tô màu.
- B. **Tô đỏ** dòng quá hạn — kèm điều kiện: chỉ tô khi dòng đó **chưa hoàn thành**, dùng cách tính của hộp việc
  (hạn < hôm nay).
- C. B + **tô cam** dòng sắp đến hạn theo tham số cảnh báo của hệ thống.

**Đề xuất của AI:** A cho đợt này — B và C phải lấy thêm trạng thái xử lý của từng dòng (nâng cỡ yêu cầu lên M) và phải
chốt dùng công thức quá hạn nào.
**Ảnh hưởng:** cỡ yêu cầu, dữ liệu phải lấy thêm. **Ai trả lời:** BA.
**Trả lời:** A

### Q08 · Nhãn cột, vị trí cột, ai thấy · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** thứ tự cột hiện nay: STT · Ngày chuyển · Người chuyển · Đơn vị chuyển · Người nhận · Đơn vị nhận · Ý
kiến chỉ đạo · Yêu cầu trả lời (QLC NV-05).
**Câu hỏi:** (a) Nhãn cột là gì? (b) Đặt ở đâu? (c) Ai thấy?

- A. (a) **"Hạn xử lý"** · (b) ngay **sau "Ngày chuyển"** (hai cột ngày đi liền nhau) · (c) **mọi người** thấy panel đều
  thấy cột.
- B. (a) "Hạn xử lý" · (b) **cuối bảng**, sau "Yêu cầu trả lời" · (c) như A.
- C. (a) "Hạn xử lý" · (b) như A · (c) **chỉ lãnh đạo và văn thư** thấy cột.

**Đề xuất của AI:** A.
**Ảnh hưởng:** giao diện, testcase giao diện. **Ai trả lời:** BA.
**Trả lời:** ngay sau cột Thời gian chuyển

### Q09 · Kênh web / ứng dụng di động · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** ứng dụng di động gọi thẳng chức năng phía máy chủ nên một thay đổi chỉ làm trên web là không đủ nếu di
động cũng có mục này (VBĐ mục 10). ⚠ Tri thức **chưa ghi** di động có màn tương đương panel người cùng nhận hay không.
**Câu hỏi:** Làm cho kênh nào?

- A. **Chỉ web** đợt này; di động ghi vào phạm vi KHÔNG đổi.
- B. **Web + ứng dụng di động** (nếu di động có mục này thì bổ sung cùng đợt) → cỡ yêu cầu thành M, cần kiểm di động
  trước khi chốt.

**Đề xuất của AI:** A — thay đổi thuần hiển thị trên panel của web; nếu BA cần di động thì AI sẽ kiểm xem di động có
mục này không ở vòng kiểm.
**Ảnh hưởng:** phạm vi, cỡ yêu cầu. **Ai trả lời:** BA.
**Trả lời:** B

## Tổng hợp

| Mã | Nhóm | Mức | Đề xuất AI | Trả lời |
|---|---|---|---|---|
| Q01 | Ai dùng, tình huống thật | BLOCKING | C | C — mọi người thấy panel đều thấy cột. Chưa có ví dụ thật cụ thể, không chặn |
| Q02 | Đúng danh sách nào | BLOCKING | A | A |
| Q03 | "Lãnh đạo giao hạn" là hạn nào | BLOCKING | A | A — hạn người chuyển chọn ở popup Chuyển văn bản |
| Q04 | Mỗi dòng hiện hạn của ai | BLOCKING | A | A — hạn lưu trên chính dòng nhận (cá nhân / đơn vị) |
| Q05 | Dòng không có hạn | BLOCKING | A | A |
| Q06 | Chiều văn bản áp dụng | BLOCKING | B | Cả văn bản đến và văn bản đã ban hành (= B) |
| Q07 | Cảnh báo quá hạn | NON-BLOCKING | A | A |
| Q08 | Nhãn, vị trí cột, ai thấy | NON-BLOCKING | A | Vị trí: ngay sau cột Thời gian chuyển. Nhãn lấy theo đề xuất "Hạn xử lý" (→ TBD-02); ai thấy theo Q01 |
| Q09 | Web / di động | NON-BLOCKING | A | B — web + ứng dụng di động (→ cỡ yêu cầu M, TBD-01) |

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 9 |
| BLOCKING chưa trả lời | 0 |
| Đã chốt | 9 (Q08 chốt phần vị trí; nhãn cột sang TBD-02) |

## Ghi chú cho DEV / tri thức (không cần BA làm gì)

- **Dữ liệu đã có, chỉ thiếu đường mang ra màn.** Mỗi dòng của panel mang theo mã dòng nhận cá nhân / dòng nhận đơn vị
  (`DocCommentEntity.documentInStaffId` / `documentInGroupId` — `web-spring/.../entity/DocCommentEntity.java:9-11`),
  còn hạn nằm ở cột `DEADLINE_DATE` của dòng nhận. Lớp dữ liệu hiện **chưa có trường hạn** nên phải bổ sung trường vào
  DTO và vào truy vấn lấy danh sách — **không cần thêm cột DB, không cần migration**.
- **Hai bản sao cùng logic:** danh sách này được dựng ở hai lớp màn riêng (`DocumentViewDetailVM` cho popup chi tiết và
  `AddAttachFileVM` cho màn thêm file kèm). Sửa một chỗ phải kiểm chỗ kia; sẽ đếm chính xác nơi gọi ở vòng kiểm lớp 3.
- **Chưa xác minh:** ứng dụng di động có đọc cùng danh sách này không (phụ thuộc Q09).
- Hạn **không sửa được sau khi chuyển** (không có gia hạn — VBĐ BR-46), nên cột này là dữ liệu tĩnh; không cần nghĩ tới
  chuyện làm mới khi hạn đổi.
- Nếu Q03 chọn C (hạn viết trong nội dung ý kiến chỉ đạo) thì đây **không còn là yêu cầu hiển thị** mà là thêm trường
  dữ liệu mới cho chức năng Cho ý kiến — phải chuyển sang mẫu đặc tả đầy đủ và mở rộng phạm vi sang `van-ban/den` NV-07.
