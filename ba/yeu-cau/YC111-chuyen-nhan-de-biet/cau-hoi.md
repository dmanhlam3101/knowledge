# YC111 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1)

**Yêu cầu:** YC111 — Văn bản đến chờ xử lý nhưng không cần xử lý: chuyển Nhận để biết thì sang Đã xử lý; người nhận
tự chuyển thành Nhận để biết · **Gửi tới:** BA / người đề xuất (anh Long) · **Ngày gửi:** 02/10/2026 ·
**Cần phản hồi trước:** {{dd/mm/yyyy}}

> **Cách trả lời:** ghi phương án chọn (A / B / C…) vào dòng **Trả lời** của từng câu, thêm ý nếu cần. Câu nào phải
> hỏi người khác thì ghi tên người + hạn. Xong báo AI "đã trả lời xong YC111" để AI viết `dac-ta.md` bản 1.0.

## Phiếu ý tưởng (nguyên văn BA)

> Có những văn bản đến chờ xử lý nhưng ko cần xử lý:
> 1. Chuyển cho các cá nhân khác trong phòng để xem để biết, người chuyển chưa sang Đã xử lý => Mong muốn sang đã xử lý
> 2. Cá nhân đó muốn tự chuyển thành Nhận để biết của mình.
>
> A Long note: Nếu chuyển nhận để biết ng nhận để biết đọc hết hết thì kết thúc. còn muốn thì chủ động bấm kết thúc

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | Hai ý: (1) chuyển chỉ Nhận để biết thì văn bản của người chuyển rời *Chờ xử lý*; (2) người nhận tự đổi văn bản của mình thành Nhận để biết |
| Ai dùng | Một phần | "Cá nhân trong phòng" — chưa rõ ai chuyển (lãnh đạo phòng, chuyên viên, văn thư?) → Q01 |
| Vì sao | Có | Văn bản không cần xử lý nhưng cứ nằm ở *Chờ xử lý* (làm số "chờ xử lý" / "quá hạn" sai thực tế) |
| Một tình huống thật | **Chưa** | Hỏi ở Q01 |
| Kết quả mong muốn | Một phần | Sang *Đã xử lý*; đọc hết thì kết thúc — chưa rõ "kết thúc" là ngay hay sau khi đọc (Q02) |
| Kênh web / mobile | **Chưa** | Hỏi ở Q10 |

**Phân hệ:** chính `van-ban/den` (hộp việc, trạng thái luồng nhận, Nhận để biết, hoàn thành) · liên quan
`van-ban/chuyen-van-ban` (chuyển chỉ Nhận để biết đổi luồng người chuyển), `lich-nhac-viec` (điều kiện hoàn thành có
nhắc việc). **Cỡ: L** (2 phân hệ, đổi trạng thái, có thể có di động) → mẫu `templates/01` đầy đủ.

## Hiện trạng (AI dựng từ tri thức)

**Đang chạy như sau:**

1. Khi chuyển văn bản, người chuyển chọn vai trò từng người nhận: *Chủ trì* (1), *Phối hợp* (2), *Nhận để biết* (3)
   (`van-ban/den` mục 5; CVB BR-19).
2. Chuyển có ít nhất một Chủ trì / Phối hợp → văn bản của người chuyển sang *Đã xử lý* (giá trị 4 — "đã chuyển, chưa
   hoàn thành"). **Chuyển chỉ cho Nhận để biết → văn bản của người chuyển vẫn ở *Chờ xử lý*, người chuyển phải tự bấm
   *Hoàn thành*** [Đã xác nhận 2026-10-01] (CVB BR-14; VBĐ BR-41). Riêng chuyển cho **nhóm** thì luôn sang *Đã xử lý*
   (CVB BR-14).
3. Người Nhận để biết: văn bản vào hộp *Văn bản nhận để biết*, **chỉ xem**, không có nút Hoàn thành / Trả lại / Cho ý
   kiến, chỉ được chuyển, lưu hồ sơ, ghi chú [Đã xác nhận Q3, Q9] (VBĐ NV-11, BR-42).
4. "Đã đọc" = mở chi tiết văn bản, **hoặc** bấm *Đánh dấu đã đọc* trên danh sách; có cả nút *Đánh dấu chưa đọc*.
   Đọc **chỉ ghi thời điểm đọc**, không đổi trạng thái, không làm ai hoàn thành (VBĐ NV-06, BR-22, BR-24).
5. Hoàn thành được ở *Chờ xử lý* (3), *Đã xử lý* (4), *Bị trả lại* (7) (VBĐ NV-05). Hoàn thành bị chặn khi có nhắc việc
   chờ duyệt; văn bản có **yêu cầu trả lời** thì phải đính kèm văn bản trả lời (VBĐ BR-31, BR-32).
6. **Chủ trì hoàn thành thì lan lên:** khi mọi Chủ trì cùng cấp xong, văn bản của người giao tự *Đã hoàn thành*, và
   Phối hợp / Nhận để biết cùng cấp cũng tự hoàn thành theo [Đã xác nhận Q2] (VBĐ BR-28, BR-29, BR-42).
7. Thống kê tiến độ coi *Đã xử lý* (4) là **chưa hoàn thành** [Đã xác nhận Q7] (VBĐ BR-45).
8. Người nhận **chưa có** cách tự đổi văn bản của mình thành Nhận để biết trên web. Phía máy chủ có sẵn một chức năng
   "đánh dấu nhận để biết" nhưng web không dùng, và nó đổi vai trò thành **Phối hợp** chứ không phải Nhận để biết
   (VBĐ NV-11; `dac-thu.md` L13).

**Tri thức đã ghi nhận ý đồ gần giống yêu cầu này** (chủ dự án trả lời 2026-10-01, chưa làm):

- VBĐ Q4: nút *Nhận để biết* trong **chi tiết văn bản** → **hoàn thành** văn bản của mình, **đổi loại nhận thành Nhận
  để biết**, văn bản sang menu *Văn bản nhận để biết*. → AI dùng làm căn cứ cho ý 2, không hỏi lại phần này.
- CVB Q8: chuyển mà **tất cả** người nhận là Nhận để biết → khi **tất cả** đã đọc thì văn bản của người chuyển tự hoàn
  thành, **vẫn giữ nút Hoàn thành**. → Khớp ghi chú của anh Long; nhưng câu này nói văn bản **vẫn ở Chờ xử lý** cho tới
  khi đọc hết, còn phiếu YC111 muốn **sang Đã xử lý** → hỏi ở Q02.

**Đối chiếu ý muốn với hiện trạng:**

| Ý muốn | Loại | Ghi chú |
|---|---|---|
| (1) Chuyển chỉ Nhận để biết → văn bản người chuyển sang *Đã xử lý* | **Sửa — đổi quy tắc [Đã xác nhận]** CVB BR-14 / VBĐ BR-41 | BA xác nhận là cố ý đổi quy tắc đã chốt 2026-10-01 (Q02) |
| (1b) Người Nhận để biết đọc hết → văn bản người chuyển tự kết thúc | **Mới** (đã có trong ý đồ CVB Q8, chưa có code) | Cần định nghĩa "đọc hết" (Q03, Q04, Q05) |
| (1c) Người chuyển vẫn được chủ động bấm kết thúc | **Giữ nguyên** | Nút Hoàn thành đã có ở *Chờ xử lý* và *Đã xử lý* |
| (2) Người nhận tự chuyển văn bản của mình thành Nhận để biết | **Mới** (đã có trong ý đồ VBĐ Q4, chưa có trên web) | Cần chốt ai, ở đâu, có lan lên người giao không (Q06, Q07, Q08) |

## Câu hỏi

> BLOCKING = chưa trả lời thì DEV không code được / Tester không viết được testcase. BLOCKING xếp trước.

### Q01 · Tình huống thật, ai dùng · BLOCKING

**Hiện trạng:** phiếu nói "cá nhân trong phòng" nhưng chưa có ví dụ cụ thể; người chuyển có thể là lãnh đạo phòng,
chuyên viên hay văn thư, và mỗi bên giữ văn bản theo cách khác nhau (văn thư giữ cả văn bản của đơn vị).
**Câu hỏi:** Cho một ví dụ thật: văn bản gì, ai nhận đầu tiên, chuyển cho ai, vì sao không cần xử lý? Ai là người dùng
chính của hai ý?

- A. Lãnh đạo phòng / đơn vị nhận văn bản dạng thông báo (vd. thông báo lịch nghỉ lễ), chuyển Nhận để biết cho cả phòng;
  chuyên viên được giao nhầm vai trò xử lý thì tự đổi thành Nhận để biết.
- B. Như A, và văn thư cũng dùng ý 1 khi chuyển văn bản **của đơn vị** chỉ để biết.
- C. Khác (ghi rõ).

**Đề xuất của AI:** A — B kéo theo luồng đơn vị của văn thư (xem Q05).
**Ảnh hưởng:** phạm vi người dùng, dữ liệu test. **Ai trả lời:** BA / anh Long.
**Trả lời:**User chuyển văn bản cá nhân hoặc văn bản đơn vị cho cá nhân/ đơn vị all nắm vai trò Nhận đề biết

### Q02 · Ý 1 — văn bản của người chuyển đi đâu, khi nào · BLOCKING

**Hiện trạng:** chuyển chỉ Nhận để biết thì văn bản người chuyển **ở Chờ xử lý** tới khi tự bấm Hoàn thành [Đã xác
nhận] (CVB BR-14). Ý đồ đã ghi (CVB Q8): đọc hết thì tự hoàn thành, nhưng trong lúc chờ vẫn ở *Chờ xử lý*.
**Câu hỏi:** Khi một lần chuyển chỉ có người Nhận để biết, văn bản của người chuyển đổi thế nào?

- A. **Ngay khi chuyển** → *Đã xử lý* (đã chuyển, chưa hoàn thành). Khi **tất cả** người Nhận để biết đã đọc → tự
  *Đã hoàn thành*. Người chuyển vẫn bấm *Hoàn thành* sớm được.
- B. Ngay khi chuyển → *Đã hoàn thành* luôn, không chờ ai đọc.
- C. Giữ ở *Chờ xử lý*; khi tất cả đã đọc → tự *Đã hoàn thành* (đúng như CVB Q8, không sang Đã xử lý).

**Đề xuất của AI:** A — khớp cả phiếu ("sang đã xử lý") lẫn ghi chú anh Long ("đọc hết thì kết thúc"). Lưu ý: A và B
**đổi quy tắc đã chốt 2026-10-01** (CVB BR-14) — xin BA xác nhận là cố ý. Với A, văn bản vẫn tính "chưa hoàn thành"
trong thống kê tiến độ cho tới khi mọi người đọc (VBĐ BR-45), và vẫn có thể bị tính quá hạn.
**Ảnh hưởng:** trạng thái, hộp *Chờ xử lý* / *Đã xử lý*, ô trang chủ, thống kê *Theo dõi văn bản đến đơn vị*.
**Ai trả lời:** BA / anh Long.
**Trả lời:**A

### Q03 · Ý 1 — thế nào là "đã đọc" · BLOCKING

**Hiện trạng:** hệ thống ghi "đã đọc" khi người nhận mở chi tiết **hoặc** bấm *Đánh dấu đã đọc* trên danh sách (kể cả
đánh dấu hàng loạt không mở văn bản); bấm *Đánh dấu chưa đọc* thì xóa dấu đọc (VBĐ NV-06). Hệ thống không phân biệt hai
cách.
**Câu hỏi:** (a) Cách nào được tính là đã đọc? (b) Văn bản người chuyển đã tự hoàn thành, sau đó một người bấm *Đánh dấu
chưa đọc* thì sao?

- A. (a) Cả hai cách đều tính · (b) Không mở lại — đã hoàn thành là xong.
- B. (a) Chỉ tính khi mở chi tiết văn bản · (b) Không mở lại.
- C. Khác (ghi rõ).

**Đề xuất của AI:** A — hệ thống hiện chỉ ghi một thời điểm đọc chung; B phải ghi thêm dữ liệu mới để phân biệt.
**Ảnh hưởng:** điều kiện tự hoàn thành, testcase. **Ai trả lời:** BA.
**Trả lời:**khi user nhận xem chi tiết văn bản đó, nếu văn bản đó có file thì phải khi xem file dự thảo mới coi là đã đọc và khi đọc sẽ update thời gian vào cột confirm_time ở docinstaff, docingroud

### Q04 · Ý 1 — "tất cả" tính trên những ai · BLOCKING

**Hiện trạng:** người chuyển có thể chuyển một văn bản nhiều lần; người nhận có thể bị thu hồi (CVB NV-10).
**Câu hỏi:** Người chuyển chuyển Nhận để biết cho A, B; hôm sau chuyển thêm Nhận để biết cho C; rồi thu hồi B. "Tất cả
đã đọc" là ai? Và nếu sau đó người chuyển chuyển thêm cho D vai trò **Chủ trì / Phối hợp** thì sao?

- A. Tính trên **mọi người Nhận để biết còn hiệu lực** (chưa bị thu hồi) mà người này đã chuyển văn bản đó, qua mọi lần
  chuyển → ví dụ: A và C. Đã chuyển thêm Chủ trì / Phối hợp thì **bỏ tự hoàn thành**, theo quy tắc cũ (chờ Chủ trì xong).
- B. Tính **theo từng lần chuyển** riêng lẻ: lần chuyển nào có tất cả đã đọc thì hoàn thành.
- C. Khác (ghi rõ).

**Đề xuất của AI:** A. (B có thể làm văn bản tự hoàn thành dù lần chuyển sau còn người chưa đọc.)
**Ảnh hưởng:** điều kiện tự hoàn thành, thu hồi. **Ai trả lời:** BA.
**Trả lời:A**

### Q05 · Ý 1 — người nhận và người chuyển thuộc loại nào · BLOCKING

**Hiện trạng:** chuyển được cho cá nhân, đơn vị, nhóm; đơn vị Nhận để biết thì vào thẳng *Chờ xử lý* của văn thư đơn vị
đó; chuyển cho nhóm thì văn bản người chuyển đã sang *Đã xử lý* sẵn (CVB BR-13, BR-14). Văn thư giữ cả văn bản **của đơn
vị** lẫn văn bản cá nhân (VBĐ BR-02).
**Câu hỏi:** Ý 1 áp dụng khi nào?

- A. Người nhận **chỉ là cá nhân** (đúng "cá nhân trong phòng"); người chuyển chuyển từ văn bản **cá nhân** của mình.
  Có đơn vị hoặc nhóm trong lần chuyển → giữ quy tắc hiện tại.
- B. Như A, thêm người nhận là **đơn vị** (đơn vị tính đã đọc khi văn thư đơn vị đó đã đọc).
- C. Như B, thêm văn thư chuyển từ văn bản **của đơn vị**.

**Đề xuất của AI:** A — đúng tình huống trong phiếu, ít ảnh hưởng nhất.
**Ảnh hưởng:** phạm vi, ma trận testcase. **Ai trả lời:** BA.
**Trả lời: Chuyển được cho cá nhân/đơn vị không tính chuyển nhóm, khi chuyển cho cá nhân thì vào Chờ xử lý của cá nhân, khi chuyển cho đơn vị vào chờ tiếp nhận đơn vị**

### Q06 · Ý 2 — ai được tự chuyển thành Nhận để biết, ở trạng thái nào · BLOCKING

**Hiện trạng:** ý đồ đã chốt (VBĐ Q4): nút *Nhận để biết* trong **chi tiết văn bản** → hoàn thành văn bản của mình, đổi
loại nhận thành Nhận để biết, văn bản sang hộp *Văn bản nhận để biết*. Chưa chốt ai thấy nút.
**Câu hỏi:** Nút *Nhận để biết* hiện cho ai, ở trạng thái nào?

- A. Văn bản **cá nhân**, vai trò **Chủ trì hoặc Phối hợp**, đang **Chờ xử lý** (chưa chuyển cho ai), mở từ hộp *Chờ
  xử lý* hoặc tab *Tất cả*.
- B. Như A, thêm văn bản **đã chuyển tiếp** (*Đã xử lý*) và *Bị trả lại*.
- C. Như A, thêm văn bản **của đơn vị** do văn thư giữ.

**Đề xuất của AI:** A — văn bản đã chuyển tiếp cho người khác thì không còn là "không cần xử lý".
**Ảnh hưởng:** điều kiện hiện nút, testcase theo vai trò. **Ai trả lời:** BA.
**Trả lời:A: user ấn vào màn chi tiết nhấn btn Nhận để biết sẽ hoàn thành và -> vawnbarn về menu văn bản nhận để biết**

### Q07 · Ý 2 — người giao văn bản bị ảnh hưởng thế nào · BLOCKING

**Hiện trạng:** Chủ trì hoàn thành → khi mọi Chủ trì cùng cấp xong thì văn bản của **người giao** tự *Đã hoàn thành*,
và Phối hợp / Nhận để biết cùng cấp cũng tự hoàn thành [Đã xác nhận Q2] (VBĐ BR-28, BR-29, BR-42). Phối hợp hoàn thành
không lan lên.
**Câu hỏi:** Chủ trì (đặc biệt là **Chủ trì duy nhất**) tự đổi thành Nhận để biết thì văn bản của người giao ra sao?

- A. **Như Chủ trì hoàn thành**: lan lên bình thường — nếu là Chủ trì cuối cùng thì người giao và các Phối hợp / Nhận để
  biết cùng cấp cũng *Đã hoàn thành*.
- B. **Không lan lên**: văn bản người giao giữ nguyên *Đã xử lý*, người giao tự quyết (giao lại hoặc tự hoàn thành).
- C. **Không cho** Chủ trì duy nhất đổi thành Nhận để biết (chỉ Phối hợp hoặc khi còn Chủ trì khác).

**Đề xuất của AI:** A — đồng nhất với ý đồ đã chốt "bấm Nhận để biết = hoàn thành" (Q4), không phải làm thêm loại hoàn
thành mới. Rủi ro: một người tự đổi có thể khép cả việc người giao đã giao — nên kèm thông báo cho người giao (Q09).
**Ảnh hưởng:** luồng hoàn thành, hộp của người giao, thống kê. **Ai trả lời:** BA / anh Long.
**Trả lời:A**

### Q08 · Ý 2 — văn bản có nhắc việc / yêu cầu trả lời · BLOCKING

**Hiện trạng:** Hoàn thành bị chặn khi văn bản có nhắc việc đang chờ duyệt hoặc nhắc việc người dùng không có quyền trả
lời; văn bản có **yêu cầu trả lời** thì phải đính kèm văn bản trả lời mới hoàn thành được (VBĐ BR-31, BR-32).
**Câu hỏi:** Văn bản đó có nhắc việc hoặc người gửi yêu cầu trả lời thì nút *Nhận để biết* thế nào?

- A. Kiểm **như Hoàn thành**: bị chặn bằng cùng thông báo; có yêu cầu trả lời thì không đổi được.
- B. **Ẩn nút** khi văn bản có nhắc việc hoặc yêu cầu trả lời.
- C. **Bỏ qua** — Nhận để biết nghĩa là không phải xử lý.

**Đề xuất của AI:** B — người dùng không bấm rồi mới bị chặn; không lách được yêu cầu trả lời.
**Ảnh hưởng:** điều kiện hiện nút, `lich-nhac-viec`. **Ai trả lời:** BA.
**Trả lời:B**

### Q09 · Hiển thị, xác nhận, thông báo · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** hoàn thành có popup nhập nội dung; luân chuyển hiển thị vai trò từng người nhận; chưa có thông báo khi
văn bản tự hoàn thành.
**Câu hỏi:** (a) Bấm *Nhận để biết* có hỏi xác nhận / nhập lý do không? (b) Có **hoàn tác** (đổi lại vai trò cũ) không?
(c) Ai được báo?

- A. (a) Hỏi xác nhận, lý do **không bắt buộc** · (b) Không hoàn tác · (c) Ý 2: báo **người giao** "<tên> đã chuyển văn
  bản thành Nhận để biết"; ý 1: không báo khi tự hoàn thành. Sơ đồ luân chuyển hiện vai trò mới kèm thời điểm đổi.
- B. (a) Bắt buộc lý do · (b), (c) như A.
- C. Không hỏi, không báo.

**Đề xuất của AI:** A.
**Ảnh hưởng:** popup, thông báo, luân chuyển. **Ai trả lời:** BA.
**Trả lời:confirm xác nhận thôi k cần nhập gì**

### Q10 · Phạm vi áp dụng · NON-BLOCKING (mặc định theo đề xuất)

**Hiện trạng:** ứng dụng di động gọi thẳng chức năng phía máy chủ, nên quy tắc chỉ làm trên web là không đủ (VBĐ mục
10; `dac-thu.md` mục 4). Văn bản mật, văn bản liên thông có cách xử lý riêng (CVB BR-46; VBĐ NV-17). Hiện đang có văn bản
nằm *Chờ xử lý* chỉ vì đã chuyển Nhận để biết từ trước.
**Câu hỏi:** Áp dụng cho những trường hợp nào? (chọn nhiều)

- A. Web, văn bản đến thường và văn bản liên thông.
- B. Thêm **văn bản mật**.
- C. Thêm **ứng dụng di động** (giao diện nút ở ý 2; ý 1 tự chạy ở máy chủ nên di động hưởng theo).
- D. Xử lý cả **văn bản cũ** đang nằm Chờ xử lý vì đã chuyển chỉ Nhận để biết trước đây.

**Đề xuất của AI:** A + B (ý 1 chạy ở máy chủ nên di động tự hưởng); giao diện di động cho ý 2 và D để đợt sau, ghi vào
phạm vi KHÔNG đổi.
**Ảnh hưởng:** phạm vi, ma trận testcase. **Ai trả lời:** BA.
**Trả lời:web/mobile**

## Tổng hợp

| Mã | Nhóm | Mức | Đề xuất AI | Trả lời |
|---|---|---|---|---|
| Q01 | Tình huống, ai dùng | BLOCKING | A | Khác: văn bản cá nhân **hoặc đơn vị**, gửi cá nhân / đơn vị, tất cả Nhận để biết — chưa có ví dụ thật (→ TBD-08) |
| Q02 | Ý 1 — trạng thái người chuyển | BLOCKING | A | A |
| Q03 | Ý 1 — "đã đọc" | BLOCKING | A | Khác: mở chi tiết; có file thì phải xem file mới tính (→ TBD-02, TBD-03); (b) chưa trả lời (→ TBD-05) |
| Q04 | Ý 1 — "tất cả" | BLOCKING | A | A |
| Q05 | Ý 1 — loại người nhận / người chuyển | BLOCKING | A | Khác: cá nhân + đơn vị, không nhóm; đơn vị vào Chờ tiếp nhận (→ TBD-01) |
| Q06 | Ý 2 — ai, trạng thái nào | BLOCKING | A | A |
| Q07 | Ý 2 — lan lên người giao | BLOCKING | A | A |
| Q08 | Ý 2 — nhắc việc, yêu cầu trả lời | BLOCKING | B | B |
| Q09 | Hiển thị, thông báo | NON-BLOCKING | A | (a) chỉ xác nhận, không nhập gì; (b)(c) chưa trả lời (→ TBD-05) |
| Q10 | Phạm vi | NON-BLOCKING | A + B | Web + mobile; mật, văn bản cũ chưa trả lời (→ TBD-06) |

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 10 |
| BLOCKING chưa trả lời | 0 (còn 4 điểm chặn phát sinh → `dac-ta.md` mục 11 TBD-01 → TBD-04) |
| Đã chốt | 10 (một phần ở Q01, Q03, Q05, Q09, Q10) |

## Ghi chú cho DEV / tri thức (không cần BA làm gì)

- Phía máy chủ đã có chức năng "đánh dấu nhận để biết" nhưng đổi vai trò sang **Phối hợp** và không hoàn thành — khác ý
  đồ VBĐ Q4 (`dac-thu.md` L13). Khi làm ý 2 phải sửa hoặc thay chức năng này; cần kiểm ứng dụng di động có đang gọi nó
  không trước khi đổi (rủi ro hồi quy).
- Ý 1 (A hoặc B ở Q02) đổi quy tắc đã chốt CVB BR-14 / VBĐ BR-41. Khi YC111 chốt, cập nhật `knowledge/van-ban/den`
  (NV-11 BR-41) và `knowledge/van-ban/chuyen-van-ban` (BR-14, 7.2 Q8).
- Lệch nghiệp vụ đã biết, liên quan gần: người Nhận để biết vẫn bấm được *Trả lại* từ màn Tra cứu (`dac-thu.md` L18) —
  sau ý 2 sẽ có thêm người Nhận để biết, rủi ro này tăng; nêu ở mục rủi ro của đặc tả.
