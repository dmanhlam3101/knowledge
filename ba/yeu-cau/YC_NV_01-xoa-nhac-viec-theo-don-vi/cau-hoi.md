# YC_NV_01 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1 — ĐÃ TRẢ LỜI 08/10/2026)

**Yêu cầu:** YC_NV_01 — Xóa nhắc việc theo từng đơn vị xử lý (không xóa lây các đơn vị khác) + xóa nhiều dòng một lần ·
**Gửi tới:** BA / người đề xuất · **Ngày gửi:** 08/10/2026 · **Ngày trả lời:** 08/10/2026

> **Trạng thái:** BA đã trả lời 10 câu (Q05 trả lời "chưa hiểu" → chuyển thành TBD-01 có ví dụ dễ hiểu hơn) → AI đã viết
> `dac-ta.md` bản 1.0. Hai điểm phát sinh sau khi đối chiếu code (Q01 nhiều CT, Q09 di động) ghi ở cuối file.

> **Cách trả lời:** ghi phương án chọn (A / B / C…) vào dòng **Trả lời** của từng câu, thêm ý nếu cần. Câu nào phải
> hỏi người khác thì ghi tên người + hạn. Xong báo AI "đã trả lời xong YC_NV_01" để AI viết `dac-ta.md` bản 1.0.
> Câu **BLOCKING** xếp trước — chưa trả lời thì DEV không code được / Tester không viết được testcase.

## Phiếu ý tưởng (nguyên văn BA)

> Luồng tạo "Nhắc việc" từ 01 VB gửi các Đơn vị -> Khi "Xóa" 1 trong số các đơn vị gửi "Nhắc việc" Các đơn vị khác
> cũng bị xóa theo.
>
> * mô tả: một nhắc việc sẽ có nhiều đơn vị xử lý, bao gồm CT và PH với, mỗi đơn vị xử lý là 1 bản ghi và là cùng 1
>   nhắc việc. Hiện trạng khi xóa 1 bản ghi PH hoặc CT đang xóa all cả các nhắc việc của các đơn vị khác,
> * mong muốn: khi xóa các đơn vị xử lý khác CT thì chỉ xóa nhắc việc của đơn vị xử lý đó thôi, khi xóa CT cũng vậy
>   nhưng có 1 case đặc biệt là nếu nhắc việc đó mà bị xóa hết các đơn vị xử lý CT thì cũng xóa luôn cả cái nhắc việc
>   đó. Thêm option xóa nhiều như ảnh nữa

Ảnh kèm theo: [`input/design/01_xoa-nhieu-nhac-viec.png`](input/design/01_xoa-nhieu-nhac-viec.png) — màn *Theo dõi
nhắc việc*, nhóm *Cần xử lý*, có **cột tick chọn** đầu lưới và nút đỏ **"Xóa 1 nhắc việc"** phía trên lưới (số 1 =
số dòng đang tick).

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | (1) Xóa một dòng đơn vị thì chỉ dòng đó mất; CT bị xóa hết thì cả nhắc việc mất. (2) Tick nhiều dòng xóa một lần |
| Ai dùng | **Một phần** | Phiếu không nói. Hiện trạng chỉ **người tạo nhắc việc** có nút Xóa (LNV BR-08) → xác nhận ở Q02 |
| Vì sao | Có | Xóa nhầm lây sang đơn vị khác: muốn bỏ một đơn vị khỏi nhắc việc nhưng cả nhắc việc biến mất |
| Một tình huống thật | Có | Một văn bản giao cho nhiều đơn vị (1 CT + n PH); người giao bấm Xóa ở dòng một PH → dòng của CT và các PH khác cũng mất |
| Kết quả mong muốn | Có | Xóa đúng dòng; nhắc việc chỉ mất khi không còn CT; có xóa nhiều |
| Kênh web / mobile | **Chưa** | → Q09 |

**Phân hệ:** chính `lich-nhac-viec` (nhắc việc — LNV NV-01 hộp, NV-02 tạo / sửa, NV-08 xóa) · liên quan `van-ban/den`
(cờ "văn bản có nhắc việc" trên hộp văn bản đến bị gỡ khi xóa — LNV NV-08) · không đụng dự thảo / văn bản đi (xóa văn
bản vẫn xóa cả nhắc việc, xem Q07).

**Cỡ: M** → mẫu `templates/01-dac-ta-yeu-cau.md`. Lý do: bổ sung nghiệp vụ trong một phân hệ, đổi cách ghi dữ liệu khi
xóa (từ xóa cả nhắc việc sang xóa từng dòng đơn vị), thêm thao tác xóa nhiều; không thêm trạng thái, không thêm bảng.
**Nâng lên L nếu** BA chọn làm cả ứng dụng di động (Q09).

## Hiện trạng (AI dựng từ tri thức + code)

Nhãn: ✔ = đã xác minh trên code `kha_develop` · ⚠ = suy ra, chưa xác minh.

1. **Một nhắc việc = một "khối" trên form tạo**: một nội dung giao việc, **đúng một** đơn vị xử lý chính (CT), nhiều
   đơn vị phối hợp (PH), hạn riêng từng đơn vị, người theo dõi (LNV NV-02, BR-06; `dac-thu` bẫy 1). Mỗi đơn vị được
   nhắc là **một dòng riêng** trong bảng `REMINDER_REPLY`, cùng trỏ về một dòng `REMINDER` (LNV mục 5.1). ✔ Khớp mô tả
   của BA "mỗi đơn vị xử lý là 1 bản ghi và là cùng 1 nhắc việc".
2. **Lưới *Theo dõi nhắc việc* hiện mỗi dòng = một đơn vị** (một nhắc việc giao 3 đơn vị → 3 dòng), cột *Đơn vị xử
   lý* có nhãn CT / PH (LNV NV-01). ✔ Nhưng dữ liệu lưới gửi về web **chỉ mang mã nhắc việc, chưa mang mã dòng đơn
   vị** (`ReminderRepositoryImpl.java:31-70` chọn `r.REMINDER_ID`, `rr.STATUS`, `rr.ORG_ROLE`, không chọn
   `rr.REMINDER_REPLY_ID`) → DEV phải bổ sung, không ảnh hưởng BA.
3. **Nút Xóa chỉ có trên lưới, chỉ hiện cho người tạo nhắc việc** (web kiểm người tạo; máy chủ kiểm lại) (LNV BR-08;
   `ReminderVM.java:2176-2179`, `ReminderServiceImpl.java:1296-1299`). ✔ Màn chi tiết nhắc việc **không có** nút Xóa
   (`reminder_viewDetail.zul` không có). ✔ Xóa **không cần lý do**, hộp xác nhận dùng câu chung *"Đồng chí có chắc chắn
   muốn xóa?"* (`zk-label.properties:10613`). ✔
4. **Bấm Xóa ở bất kỳ dòng nào → xóa mềm CẢ nhắc việc**: dòng `REMINDER`, **mọi** dòng đơn vị, người theo dõi, liên
   kết văn bản; rồi gỡ cờ "văn bản có nhắc việc" trên luồng văn bản đến của **mọi** đơn vị được nhắc (trừ nhánh còn
   nhắc việc khác) (LNV NV-08; `ReminderServiceImpl.java:1288-1334`, `1336-1398`). ✔ Đây đúng là hiện tượng BA mô tả.
   Xóa được ở **mọi trạng thái** của dòng (kể cả Chờ duyệt / Hoàn thành) — máy chủ không kiểm trạng thái. ✔
5. **Đã có sẵn một cách bỏ một đơn vị khỏi nhắc việc**: người tạo bấm *Sửa* → bỏ đơn vị PH khỏi danh sách → lưu →
   dòng đơn vị đó bị xóa mềm, các dòng khác giữ nguyên (LNV NV-02 bước 4; `ReminderServiceImpl.java:1118-1149`). ✔
   Nhưng: không bỏ được CT (bắt buộc chọn một); nút *Sửa* bị ẩn khi có dòng đã Chờ duyệt / Hoàn thành; và cách này
   **không gỡ cờ "văn bản có nhắc việc"** của đơn vị bị bỏ (chỉ `deleteReminder` mới gỡ). ✔ → BA cân nhắc ở Q03, Q06.
6. **Xóa nhiều: giao diện đã có khung nhưng đang tắt.** Cột tick chọn và ô "chọn tất cả" trên lưới **đang bị comment**
   (`reminder_search.zul:320-322`, `336-338`); mã xử lý tick / bỏ tick vẫn còn trong VM (`ReminderVM.java:1190-1240`);
   hàm web gửi danh sách mã để xóa (`ReminderBusiness.deleteReminders`, `ReminderBusiness.java:384-404`) **không ai gọi**
   và trỏ vào đúng endpoint xóa đơn (máy chủ chỉ nhận một mã) (LNV NV-20, `dac-thu` L7). ✔ Ba nút hàng loạt *Trả lời /
   Hủy trả lời / Duyệt* trên lưới cũng đang ẩn (LNV NV-01). ✔
7. **Xóa văn bản / dự thảo** → nhắc việc giao kèm văn bản đó bị xóa cả (LNV NV-08) — một điểm xóa khác, nằm ở phân hệ
   văn bản. ✔
8. **Dòng "Đã xử lý tạm" (5) là dòng sao** của cùng đơn vị trong cùng nhắc việc (`dac-thu` bẫy 3) → khi xóa "một đơn
   vị" máy chủ phải xóa cả hai dòng của đơn vị đó. ✔ Việc của DEV, không hỏi BA.
9. **Nhắc việc không gửi SMS / thông báo ở bất kỳ bước nào** (LNV BR-22, Q1 còn mở) — xóa cũng không báo cho ai. ✔
10. **Ứng dụng di động:** trong mã nguồn không có nơi nào khác gọi xóa nhắc việc ngoài màn web (grep `/reminders`
    toàn bộ repo chỉ ra 3 lớp của chính nhắc việc). ✔ Tri thức `tich-hop` không nhắc tới nhắc việc trên di động.
    ⚠ Chưa chắc ứng dụng di động có màn nhắc việc hay không → Q09.
11. **Lịch sử:** bảng `REMINDER_HISTORY` chỉ ghi chuyển xử lý (loại 1); xóa nhắc việc **không ghi vết** gì ngoài cột
    `DEL_FLAG` / người xóa / thời điểm trên dòng bị xóa (LNV NV-06, mục 5.1). ✔

**Đối chiếu ý muốn với quy tắc hiện có**

| Ý muốn của BA | Loại | Đụng quy tắc |
|---|---|---|
| Xóa một dòng đơn vị chỉ mất dòng đó | **Sửa** hành vi NV-08 (xóa cả nhắc việc → xóa một dòng) | Không mâu thuẫn quy tắc [Đã xác nhận] nào; BR-08 (chỉ người tạo) giữ nguyên nếu Q02 = A |
| Xóa hết CT thì xóa cả nhắc việc | **Mới** | Mỗi nhắc việc chỉ có **một** CT (BR-06) → "xóa hết CT" = xóa dòng CT duy nhất → **Q01 phải chốt** vì hệ quả là xóa cả các PH còn lại |
| Xóa nhiều dòng một lần | **Mới** (khung giao diện có sẵn, chưa bật) | Chưa có quy tắc; cần chốt phạm vi chọn và cách xử lý dòng không được xóa (Q04, Q05) |

## Câu hỏi

### Q01 · Xóa dòng CT thì các dòng PH còn lại ra sao · BLOCKING

**Hiện trạng:** mỗi nhắc việc chỉ có **một** đơn vị CT (LNV BR-06). Vì vậy "xóa hết các đơn vị CT" trong phiếu ý tưởng
luôn xảy ra ngay lần xóa dòng CT đầu tiên.

**Câu hỏi:** Nhắc việc có 1 CT + 2 PH, người tạo bấm Xóa ở **dòng CT**. Kết quả mong muốn là gì?

- A. Xóa dòng CT **và** cả nhắc việc, tức 2 dòng PH cũng mất (đúng chữ "xóa luôn cả cái nhắc việc" trong phiếu).
  Hộp xác nhận phải nói rõ: *"Đây là đơn vị xử lý chính. Xóa sẽ xóa cả nhắc việc và N đơn vị phối hợp. Đồng chí có
  chắc chắn?"* (câu chữ chốt sau).
- B. Chỉ xóa dòng CT; nhắc việc còn lại 2 PH, không có CT. (Khi đó cần chốt thêm: hệ thống có cho tồn tại nhắc việc
  không có CT không, và màn Sửa đang bắt buộc chọn một CT sẽ xử lý thế nào.)
- C. **Không cho** xóa dòng CT khi còn PH: báo *"Phải xóa các đơn vị phối hợp trước"*; chỉ khi CT là dòng cuối cùng
  thì xóa CT = xóa cả nhắc việc.

**Đề xuất của AI:** **A** — đúng lời phiếu, không sinh nhắc việc mồ côi, DEV làm đơn giản.
**Trả lời:** **A** — kèm lưu ý của BA: *"xóa CT nhưng nhắc việc vẫn còn CT thì chỉ xóa CT đó thôi, chỉ xóa luôn nhắc việc khi mà
không còn CT cho nhắc việc đó nữa"* → ghi thành BR-05 dạng tổng quát (còn CT hoạt động → chỉ xóa dòng; hết CT → xóa cả
nhắc việc). ⚠ Hiện trạng: web chỉ cho chọn **một** CT mỗi nhắc việc (LNV BR-06), máy chủ không chặn nhiều CT
(`ReminderServiceImpl.java:621-636` chỉ chặn trùng đơn vị) → trường hợp "còn CT khác" chỉ xảy ra với dữ liệu tạo ngoài
web; vẫn viết quy tắc tổng quát để DEV không phải đoán.

### Q02 · Ai được xóa · BLOCKING

**Hiện trạng:** chỉ **người tạo nhắc việc** thấy và được bấm Xóa; máy chủ kiểm lại (LNV BR-08). Lãnh đạo / chuyên viên
theo dõi và đơn vị được nhắc không có nút này.

**Câu hỏi:** Sau khi làm yêu cầu này, ai được xóa một dòng đơn vị?

- A. Giữ nguyên: chỉ người tạo nhắc việc (cho cả xóa một dòng lẫn xóa nhiều).
- B. Người tạo **và** lãnh đạo theo dõi của nhắc việc đó.
- C. Khác (ghi rõ).

**Đề xuất của AI:** **A** — không mở rộng quyền trong yêu cầu này.
**Trả lời:** **A** — giữ nguyên hiện trạng (chỉ người tạo).

### Q03 · Xóa được dòng ở trạng thái nào · BLOCKING

**Hiện trạng:** hiện nút Xóa hiện với người tạo ở **mọi trạng thái** dòng (Lưu tạm, Chưa trả lời, Xử lý lại, Chờ
duyệt, Hoàn thành, Đã xử lý tạm); máy chủ không chặn theo trạng thái. Trong khi nút *Sửa* bị ẩn khi dòng đã Chờ duyệt /
Hoàn thành (LNV BR-08).

**Câu hỏi:** Người tạo được xóa dòng của một đơn vị khi dòng đó đang ở trạng thái nào?

- A. Mọi trạng thái, như hiện nay (đơn vị đã trả lời / đã được duyệt vẫn xóa được; nội dung trả lời mất theo).
- B. Chỉ khi đơn vị **chưa trả lời**: Lưu tạm · Chưa trả lời · Xử lý lại. Dòng Chờ duyệt / Hoàn thành / Đã xử lý tạm
  → nút Xóa ẩn (giống nút Sửa), và nếu tick xóa nhiều thì dòng đó bị bỏ qua (xem Q05).
- C. Chỉ khi chưa trả lời, **trừ** trường hợp Q01-A: xóa CT kéo theo cả nhắc việc thì xóa luôn PH đã Hoàn thành.

**Đề xuất của AI:** **B** — xóa một đơn vị đã trả lời / đã được duyệt là mất kết quả xử lý của đơn vị đó; nếu BA muốn
giữ A thì ghi rõ vào tài liệu là chủ ý.
**Trả lời:** *"hiện trạng btn xóa đã có và ta giữ nguyên hiện trạng ẩn hiện của nó, chỉ sửa logic nghiệp vụ khi xóa"* → tức
**phương án A**: xóa được ở mọi trạng thái, điều kiện hiện nút không đổi (BR-03).

### Q04 · Xóa nhiều: tick được những dòng nào, xóa ở nhóm nào · BLOCKING

**Hiện trạng:** ảnh của BA đặt cột tick và nút "Xóa N nhắc việc" ở nhóm *Cần xử lý*. Nhưng *Cần xử lý* là hộp của
**đơn vị được nhắc**, còn người tạo thấy việc mình giao ở nhóm *Giao đi/Theo dõi* (LNV NV-01). Trong ảnh người đang
đăng nhập vừa là người tạo vừa thuộc đơn vị được nhắc nên mới thấy nút xóa ở *Cần xử lý*.

**Câu hỏi:** Cột tick và nút xóa nhiều hiện ở đâu, tick được dòng nào?

- A. Cả hai nhóm *Cần xử lý* và *Giao đi/Theo dõi*; **chỉ dòng có nút Xóa** (người tạo + trạng thái cho phép theo Q03)
  mới có ô tick; dòng khác ô tick bị mờ / không có. "Chọn tất cả" chỉ chọn các dòng tick được **trong trang hiện tại**.
- B. Chỉ nhóm *Giao đi/Theo dõi* (nơi người tạo thường làm việc); *Cần xử lý* giữ như cũ.
- C. Mọi dòng đều tick được; dòng không được xóa thì khi bấm nút sẽ báo và bỏ qua (xem Q05).

**Đề xuất của AI:** **A** — khớp ảnh và tránh người dùng tick rồi bị từ chối.
**Trả lời:** *"xóa được những bản ghi mà đang có btn xóa ấy, theo nghiệp vụ của btn xóa mà hiển thị checkbox cho check"* → tức
**phương án A**: ô tick chỉ hiện ở dòng đang có nút Xóa, ở cả hai nhóm (BR-07).

### Q05 · Xóa nhiều: xử lý khi trong các dòng tick có CT, có dòng không xóa được, hoặc một dòng lỗi · BLOCKING

**Hiện trạng:** chưa có xóa nhiều. Mỗi lần xóa hiện nay là một giao dịch riêng.

**Câu hỏi:** Người tạo tick 5 dòng rồi bấm "Xóa 5 nhắc việc". Hệ thống xử lý thế nào?

- A. **Tất cả hoặc không**: kiểm trước; nếu có dòng không được xóa (không phải người tạo, trạng thái không cho phép theo
  Q03) thì báo *"Có N dòng không thể xóa: …"* và **không xóa dòng nào**. Nếu trong các dòng tick có dòng CT thì hộp xác
  nhận liệt kê rõ *"M nhắc việc sẽ bị xóa hoàn toàn (kèm các đơn vị phối hợp chưa tick)"* theo Q01. Lỗi giữa chừng →
  hoàn tác toàn bộ.
- B. **Xóa phần được, báo phần không**: xóa các dòng hợp lệ, cuối cùng báo *"Đã xóa X dòng, Y dòng không xóa được vì
  …"*.
- C. Khác.

**Đề xuất của AI:** **A** — dễ hiểu với người dùng, dễ kiểm thử; với Q04-A thì trường hợp "dòng không được xóa" gần như
không xảy ra.
**Trả lời:** **"chưa hiểu"** → AI diễn giải lại bằng ví dụ ở **TBD-01** trong `dac-ta.md` mục 11; tài liệu tạm giả định phương án
A (tất cả hoặc không) và ghi rõ hệ quả "tick CT cuối cùng thì PH chưa tick cũng mất" để BA xác nhận.

### Q06 · Hệ quả phía đơn vị bị xóa: cờ "văn bản có nhắc việc" và văn bản trả lời · BLOCKING

**Hiện trạng:** khi giao nhắc việc, hộp văn bản đến của đơn vị được nhắc được đánh dấu "văn bản có nhắc việc" (để đếm
và để chặn / buộc trả lời khi hoàn thành văn bản đến — LNV NV-08, NV-09). Xóa cả nhắc việc hiện **gỡ** dấu này cho mọi
đơn vị. Cách "bỏ đơn vị khi Sửa" hiện **không gỡ** (hiện trạng điểm 5).

**Câu hỏi:** Khi xóa dòng của một đơn vị, phía đơn vị đó cần gì?

- A. Gỡ dấu "văn bản có nhắc việc" **chỉ trên luồng văn bản đến của đơn vị đó** (trừ khi đơn vị đó còn nhắc việc khác
  trên cùng văn bản); dòng trả lời và văn bản trả lời (nếu có) của đơn vị đó bị xóa mềm theo dòng; dòng của các đơn vị
  khác và người theo dõi giữ nguyên. Đơn vị không được báo gì (nhắc việc vốn không gửi thông báo).
- B. Như A nhưng **có** tạo thông báo (chuông) cho đơn vị bị xóa: *"Nhắc việc … đã bị <người tạo> gỡ khỏi đơn vị"*.
  (Mở rộng: nhắc việc hiện chưa có thông báo nào — LNV Q1.)
- C. Như A và **đồng thời sửa luôn** cách "bỏ đơn vị khi Sửa nhắc việc" để cũng gỡ dấu như xóa dòng (hai cách cho cùng
  kết quả).

**Đề xuất của AI:** **A + C** — C làm hai đường cho ra một kết quả, DEV chỉ cần gọi chung một hàm.
**Trả lời:** **A + C** — gỡ cờ theo đơn vị bị xóa; không thông báo; đường *Sửa* bỏ đơn vị cũng gỡ cờ (BR-06, BR-12).

### Q07 · Phạm vi: có đụng "xóa văn bản thì xóa nhắc việc" và xóa từ chi tiết không · NON-BLOCKING

**Hiện trạng:** xóa văn bản / dự thảo → xóa cả nhắc việc giao kèm (LNV NV-08). Màn chi tiết nhắc việc và tab nhắc việc
trong chi tiết văn bản **không có** nút Xóa.

**Câu hỏi:** Đợt này làm những điểm nào?

- A. Chỉ lưới *Theo dõi nhắc việc* (xóa một dòng + xóa nhiều). Xóa theo văn bản giữ nguyên (xóa cả nhắc việc).
- B. Thêm nút Xóa dòng đơn vị trên màn chi tiết nhắc việc (bảng các đơn vị).
- C. Khác.

**Đề xuất của AI:** **A**.
**Trả lời:** **A** — chỉ lưới; xóa theo văn bản giữ nguyên (BR-13).

### Q08 · Nhãn nút, câu xác nhận, câu thông báo · NON-BLOCKING

**Hiện trạng:** nút xóa đơn là icon thùng rác, xác nhận *"Đồng chí có chắc chắn muốn xóa?"*, lỗi *"Xóa nhắc việc thất
bại, vui lòng thử lại!"*; ảnh của BA ghi nút **"Xóa 1 nhắc việc"**.

**Câu hỏi:** Chốt chữ hiển thị:

- A. Nút xóa nhiều: **"Xóa N nhắc việc"** (N = số dòng tick, ẩn nút khi N = 0) như ảnh. Xác nhận xóa một dòng PH:
  *"Xóa nhắc việc của đơn vị <tên đơn vị>?"*; xóa dòng CT (Q01-A): *"<Tên đơn vị> là đơn vị xử lý chính. Xóa sẽ xóa
  toàn bộ nhắc việc này (kể cả N đơn vị phối hợp). Đồng chí có chắc chắn?"*; xóa nhiều: *"Xóa N dòng nhắc việc đã
  chọn?"* (+ dòng cảnh báo CT nếu có). Thành công: *"Đã xóa N nhắc việc"*.
- B. Giữ câu chung *"Đồng chí có chắc chắn muốn xóa?"* cho mọi trường hợp, chỉ đổi nhãn nút theo ảnh.
- C. BA tự ghi câu chữ khác.

**Đề xuất của AI:** **A** — vì khác biệt CT / PH là điểm người dùng dễ nhầm nhất.
**Trả lời:** **B** — giữ câu xác nhận chung *"Đồng chí có chắc chắn muốn xóa?"*, chỉ đổi nhãn nút theo ảnh (BR-10, BR-08).
⚠ Hệ quả đã ghi ở EC-08: xóa dòng CT cuối cùng không được cảnh báo riêng rằng PH chưa tick cũng mất.

### Q09 · Kênh: web hay cả ứng dụng di động · NON-BLOCKING

**Hiện trạng:** trong mã nguồn chỉ màn web gọi xóa nhắc việc; AI chưa xác minh ứng dụng di động có màn nhắc việc không.

**Câu hỏi:** Đợt này làm ở đâu?

- A. Chỉ web.
- B. Web và ứng dụng di động (nếu di động có màn nhắc việc; AI sẽ xác minh thêm và cỡ yêu cầu lên L).

**Đề xuất của AI:** **A**.
**Trả lời:** **B** — web và ứng dụng di động. ⚠ Đối chiếu code: **di động hiện không có màn nhắc việc** (không API di động nào gọi
nhắc việc; `knowledge/tich-hop` không nhắc tới) → "làm cả di động" là xây mới, không phải sửa → **TBD-02** (tài liệu
tạm giả định chỉ web).

### Q10 · Có cần lưu lý do / vết xóa không · NON-BLOCKING

**Hiện trạng:** xóa không cần lý do; chỉ ghi người xóa và thời điểm trên dòng bị xóa; popup "Lý do xóa nhắc nhở" trong
mã cũ không gửi gì lên máy chủ (LNV NV-08, `dac-thu` L14).

**Câu hỏi:**

- A. Không cần lý do; giữ cách ghi vết như hiện nay.
- B. Bắt nhập lý do khi xóa (một dòng hay nhiều dòng) và lưu vào lịch sử nhắc việc để lãnh đạo theo dõi xem được.

**Đề xuất của AI:** **A** (đổi sang B cần thêm cột / loại lịch sử mới).
**Trả lời:** **A** — không lý do, giữ cách ghi vết hiện nay (BR-11).

## Tổng hợp

| Mã | Nhóm | Mức | Đề xuất AI | Trả lời |
|---|---|---|---|---|
| Q01 | Xóa CT → PH còn lại | BLOCKING | A | A (+ lưu ý còn CT khác thì chỉ xóa CT đó) |
| Q02 | Ai được xóa | BLOCKING | A | A |
| Q03 | Trạng thái được xóa | BLOCKING | B | Giữ hiện trạng = A |
| Q04 | Xóa nhiều: ở đâu, tick dòng nào | BLOCKING | A | = A |
| Q05 | Xóa nhiều: dòng CT / dòng không hợp lệ / lỗi | BLOCKING | A | Chưa hiểu → TBD-01 |
| Q06 | Hệ quả phía đơn vị bị xóa | BLOCKING | A + C | A + C |
| Q07 | Phạm vi điểm xóa | NON-BLOCKING | A | A |
| Q08 | Nhãn, câu xác nhận | NON-BLOCKING | A | B |
| Q09 | Web / di động | NON-BLOCKING | A | **B** → TBD-02 |
| Q10 | Lý do / vết xóa | NON-BLOCKING | A | A |

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 10 |
| BLOCKING chưa trả lời | 0 (Q05 chuyển thành TBD-01) |
| Đã chốt | 9 |
| Điểm phát sinh sau khi trả lời | 2 (TBD-01 xóa nhiều · TBD-02 di động) + 2 TBD nhẹ (TBD-03 nút / toast · TBD-04 kỹ thuật) |

## Điểm phát sinh — xem `dac-ta.md` mục 11

| TBD | Nội dung | Ai chốt | Chặn code? |
|---|---|---|---|
| TBD-01 | Xóa nhiều gặp dòng lỗi: không xóa gì (A) hay xóa phần được (B); xác nhận "tick CT cuối cùng thì PH chưa tick cũng mất" | BA | **Có** |
| TBD-02 | Di động hiện không có nhắc việc → YC_NV_01 chỉ web, mở yêu cầu riêng cho di động (A) hay gộp và nâng cỡ L (B) | BA / chủ dự án | **Có** (phần di động) |
| TBD-03 | Nút "Xóa N nhắc việc" khi N = 0 ẩn hay mờ; có toast thành công không | BA | Không |
| TBD-04 | Endpoint mới hay đổi payload endpoint cũ | DEV | Không |

## Ghi chú cho DEV / tri thức (không cần BA làm gì)

- Lưới cần trả thêm **mã dòng đơn vị** (`REMINDER_REPLY_ID`) vì nút Xóa hiện gửi mã nhắc việc
  (`ReminderBusiness.deleteReminder` → `POST /reminders/delete` chỉ nhận `reminderId`).
- Có sẵn: `ReminderReplyRepositoryJPA.deleteByIds` (xóa mềm theo danh sách dòng), `findActiveByReminderId`,
  `DocumentInGroupRepositoryJPA.findActiveReminderRootIds(documentIds, senderOrgId, receiverOrgIds)` nhận **danh sách
  đơn vị nhận** nên gỡ cờ theo từng đơn vị làm được bằng cách truyền một đơn vị.
- Dòng "Đã xử lý tạm" (5) là dòng sao của cùng đơn vị → xóa một đơn vị phải xóa cả hai dòng (`dac-thu` bẫy 3).
- Khung xóa nhiều trên web đã có nhưng tắt: checkbox comment ở `reminder_search.zul:320-322`, `336-338`; lệnh
  `doCheckItem` / `doCheckAll` / `doClearSelection` ở `ReminderVM.java:1196-1240`; `ReminderBusiness.deleteReminders`
  gửi `reminderIds` + `reason` nhưng tới endpoint xóa đơn — cần endpoint mới nhận danh sách mã dòng.
- Khi YC_NV_01 chốt, cập nhật tri thức `knowledge/lich-nhac-viec`: NV-08 (xóa theo dòng), BR mới cho quy tắc CT, mục
  7.1 nếu câu trả lời Q06-B / Q10-B động tới Q1 / Q7 còn mở; L7 (`deleteReminders` hết là code chết).
