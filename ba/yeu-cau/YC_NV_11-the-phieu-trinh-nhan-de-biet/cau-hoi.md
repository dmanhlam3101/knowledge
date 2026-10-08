# YC_NV_11 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1 — ĐÃ TRẢ LỜI ĐỦ 07/10/2026)

**Yêu cầu:** YC_NV_11 — Thêm thẻ (ô) "Phiếu trình nhận để biết" ngoài trang chủ; mặc định hiển thị; bật / tắt được ở
*Cấu hình trang chủ* · **Gửi tới:** BA / người đề xuất ({{họ tên}}) · **Ngày gửi:** 07/10/2026 ·
**Cần phản hồi trước:** {{dd/mm/yyyy}}

> **Cách trả lời:** ghi phương án chọn (A / B / C…) vào dòng **Trả lời** của từng câu, thêm ý nếu cần. Câu nào phải
> hỏi người khác thì ghi tên người + hạn. Xong báo AI "đã trả lời xong YC_NV_11" để AI viết `dac-ta.md` bản 1.0.

## Phiếu ý tưởng (nguyên văn BA)

> Thêm thẻ Phiếu trình nhận để biết ngoài trang chủ (mặc định hiển thị và đưa vào on/off ở Cấu hình trang chủ)

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | Thêm một ô đếm "Phiếu trình nhận để biết" vào trang chủ; mặc định bật; người dùng tự bật / tắt được ở *Cấu hình trang chủ* |
| Ai dùng | **Chưa** | Hỏi ở Q01 |
| Vì sao | **Chưa** | Hỏi ở Q01 (AI đoán: hiện phải vào menu mới biết có phiếu mới được chuyển tới — ⚠ chưa xác minh) |
| Một tình huống thật | **Chưa** | Hỏi ở Q01 |
| Kết quả mong muốn | Một phần | "Thẻ hiện ngoài trang chủ" — chưa rõ ô **đếm gì** và **bấm vào mở gì** (Q02, Q04) |
| Kênh web / mobile | **Chưa** | Hỏi ở Q05 |

**Phân hệ:** chính `phieu-trinh` (hộp *Phiếu trình nhận để biết* NV-13; nhóm ô trang chủ "Phiếu trình" 1.2b) · liên
quan `he-thong` (cơ chế trang chủ, *Cấu hình trang chủ*, chế độ đơn giản / đầy đủ — NV-16). **Cỡ: S** (thêm ô hiển
thị + điều hướng, không đổi trạng thái, không thêm dữ liệu nghiệp vụ; chỉ thêm một phép đếm và một dòng khai báo ô)
→ mẫu `templates/02`. Nếu Q05 chọn có mobile thì lên cỡ L (trang chủ mobile dùng bộ riêng).

> Ký hiệu nguồn: `PT` = `knowledge/phieu-trinh`, `HT` = `knowledge/he-thong`, `VBĐ` = `knowledge/van-ban/den`.
> Nhãn quy tắc: [Đã xác nhận] = chủ dự án đã chốt · [Hiện trạng] = đang chạy như vậy, chưa ai xác nhận là ý đồ.

## Hiện trạng (AI dựng từ tri thức)

**Đang chạy như sau:**

1. **Trang chủ đã có nhóm ô "Phiếu trình" gồm 5 ô:** *Chờ xử lý*, *Đang xử lý*, *Đã phê duyệt*, *Tất cả*, *Xin ý
   kiến*. Mỗi ô là một con số, bấm vào mở đúng hộp / tab tương ứng. **Chưa có ô "Nhận để biết"** (PT 1.2b).
   Số đếm tính trong **365 ngày gần nhất**; cả nhóm lấy số bằng một lần gọi chung, quá **20 giây** chưa có kết quả
   thì mọi ô hiện 0 (PT 1.2b; PT `dac-thu` L13) [Hiện trạng].
2. **Hộp "Phiếu trình nhận để biết"** (menu riêng trong nhóm PHIẾU TRÌNH, mã menu 441145): chứa phiếu người khác
   **chuyển tiếp để biết** cho mình; mỗi phiếu một dòng (lần chuyển mới nhất); **phiếu chưa đọc in đậm**; mở chi tiết
   là tính đã đọc. Lọc được theo tiêu đề, người gửi, ngày gửi (PT NV-13). Người nhận để biết **chỉ xem và chuyển tiếp
   tiếp**, không xử lý (PT BR-40 [Đã xác nhận]). Chỉ phiếu *Đã phê duyệt* mới được chuyển để biết (PT BR-39 [Đã xác
   nhận]). Khi được chuyển, người nhận có **thông báo** (bấm mở menu này) và SMS nếu phiếu không mật (PT NV-13).
   ⚠ Chưa xác minh: hộp này có giới hạn thời gian (365 ngày) như các hộp khác hay không.
3. **Mẫu tương tự đã có ở nhóm "Văn bản đến":** ô *Nhận để biết* đếm **toàn bộ** văn bản trong hộp *Văn bản nhận để
   biết* (không chỉ chưa đọc), bấm vào mở menu đó (VBĐ 1.3) [Hiện trạng].
4. **Cấu hình trang chủ** (khung người dùng góc phải → *Cấu hình trang chủ*): danh sách nhóm ô (cha) và từng ô con,
   tick **bật / tắt được tới từng ô con**; tắt hết ô con thì nhóm tự tắt, bật một ô con thì nhóm tự bật; bấm Lưu
   (HT NV-16). Ô mới khai thêm trong hệ thống **tự xuất hiện** trong danh sách này, kể cả với người đã lưu cấu hình
   trước đó (`web-spring/.../PersonalSettingUtil.java:390-421` `syncHomeWidget`) — ⚠ trạng thái bật / tắt mặc định
   của ô mới đối với người đã lưu cấu hình: cần DEV xác nhận ở vòng kiểm (xem Q09).
5. **Cấu hình trang chủ của từng người chỉ lưu tạm** (bộ nhớ đệm máy chủ), **mất khi hệ thống khởi động lại** và trở
   về mặc định (HT BR-38 [Hiện trạng]; câu hỏi mở HT Q10 chưa chốt cần giữ lâu dài hay không). Với yêu cầu này, ô mới
   "mặc định hiển thị" nên sau khởi động lại ô vẫn hiện — không mâu thuẫn, chỉ là rủi ro người đã tắt sẽ thấy lại.
6. **Chế độ trang chủ đơn giản / đầy đủ:** ở chế độ *đơn giản* chỉ ô nào được khai cho chế độ đó mới hiện; trong nhóm
   "Phiếu trình" hiện **chỉ ô *Chờ xử lý*** hiện ở chế độ đơn giản, 4 ô còn lại không (HT BR-39; PT 1.2b) [Hiện trạng].
7. **Trang chủ trên ứng dụng di động** dùng bộ menu / widget **riêng** (máy chủ thế hệ 2), không dùng chung cơ chế ô
   trang chủ web (HT 1.5, NV-10) [Hiện trạng].

**Đối chiếu ý muốn với hiện trạng:**

| Ý muốn | Loại | Ghi chú |
|---|---|---|
| Thêm ô "Phiếu trình nhận để biết" vào trang chủ | **Mới** | Đi theo cơ chế nhóm ô "Phiếu trình" sẵn có (thêm ô thứ 6); có mẫu tương tự ở nhóm Văn bản đến. Không mâu thuẫn quy tắc [Đã xác nhận] nào |
| Mặc định hiển thị | **Mới** (theo mặc định chung) | Các ô phiếu trình hiện có đều mặc định hiện; chỉ 2 ô văn bản đi là mặc định tắt (HT NV-16) |
| Bật / tắt ở *Cấu hình trang chủ* | **Dùng cơ chế sẵn có** | Màn cấu hình đã bật / tắt tới từng ô con; ô mới tự có mặt trong danh sách. Không phải làm màn mới |
| (chưa nói) Ô đếm gì, bấm mở gì, chế độ đơn giản, mobile | **Phải chốt** | Q02 – Q05, Q08 |

**Rủi ro nêu để BA biết (không phải câu hỏi):**
- Số của ô mới đi chung một lần gọi với 5 ô kia → cũng chịu giới hạn 20 giây; thêm phép đếm làm lần gọi lâu hơn
  một chút (PT `dac-thu` L13).
- Cấu hình bật / tắt chỉ lưu tạm (HT BR-38): người tắt ô này sẽ thấy lại sau khi hệ thống khởi động lại. Nếu BA muốn
  giữ lâu dài thì đó là một yêu cầu khác (HT Q10), không gói vào yêu cầu này.

## Câu hỏi

> BLOCKING = chưa trả lời thì DEV không code được / Tester không viết được testcase. BLOCKING xếp trước.

### Q01 · Ai dùng, vì sao cần, một tình huống thật · BLOCKING

**Hiện trạng:** ai cũng có thể được chuyển phiếu để biết (người trình hoặc người đã nhận chọn người nhận tự do — PT
NV-13). Hiện người nhận biết có phiếu mới qua **thông báo** và **SMS**, hoặc tự vào menu *Phiếu trình nhận để biết*.
**Câu hỏi:** Ai là người cần ô này nhất, và vì sao thông báo / SMS hiện nay chưa đủ? Cho một ví dụ thật (ai chuyển
phiếu gì cho ai, người nhận đã bỏ sót thế nào).

- A. **Mọi người dùng** từng được chuyển phiếu để biết (lãnh đạo lẫn chuyên viên) — thông báo trôi nhanh, cần một ô
  ngoài trang chủ để thấy ngay còn bao nhiêu phiếu chưa xem.
- B. Chủ yếu **lãnh đạo** (`TTDV` / `LDDV`) — được chuyển để biết nhiều, cần nhìn tổng quan.
- C. Khác (ghi rõ).

**Đề xuất của AI:** A — ô hiện cho mọi người như các ô phiếu trình khác; ai không cần thì tự tắt ở *Cấu hình trang
chủ*. **Ảnh hưởng:** phạm vi vai trò, dữ liệu test. **Ai trả lời:** BA / người đề xuất.
**Trả lời:** A — mọi người dùng từng được chuyển phiếu để biết; ai không cần thì tự tắt. (BA trả lời 07/10/2026)

### Q02 · Con số trên ô đếm gì · BLOCKING

**Hiện trạng:** hộp *Phiếu trình nhận để biết* phân biệt **chưa đọc** (in đậm) và đã đọc; mỗi phiếu một dòng (PT
NV-13). Ô *Nhận để biết* của nhóm Văn bản đến đếm **toàn bộ** hộp, không tách chưa đọc (VBĐ 1.3). Các ô phiếu trình
khác đếm toàn bộ phiếu trong tab tương ứng (PT 1.2b).
**Câu hỏi:** Con số trên ô là gì?

- A. **Số phiếu chưa đọc** trong hộp nhận để biết (đọc rồi thì số giảm; hết chưa đọc thì ô hiện 0).
- B. **Tổng số phiếu** trong hộp nhận để biết (giống ô Văn bản đến *Nhận để biết*; số chỉ tăng).
- C. Hai số trên cùng ô: tổng và chưa đọc (các ô hiện nay chỉ có một số → phải làm kiểu ô mới).

**Đề xuất của AI:** A — đúng mục đích "để biết có phiếu mới"; B nhất quán với ô văn bản đến nhưng ít giá trị theo dõi.
Lưu ý với A: một phiếu được chuyển cho cùng một người nhiều lần vẫn tính là **một** phiếu (hộp gộp theo phiếu, PT
BR-41). **Ảnh hưởng:** phép đếm, AC, testcase. **Ai trả lời:** BA / người đề xuất.
**Trả lời:** B — **tổng số phiếu** trong hộp nhận để biết (không tách chưa đọc). (BA trả lời 07/10/2026)

### Q03 · Khoảng thời gian đếm · BLOCKING

**Hiện trạng:** 5 ô phiếu trình hiện có đếm trong **365 ngày gần nhất** (PT 1.2b). Hộp nhận để biết: ⚠ chưa xác minh
có giới hạn thời gian hay không.
**Câu hỏi:** Ô mới đếm trong khoảng nào?

- A. **365 ngày gần nhất** tính theo ngày được chuyển — giống 5 ô còn lại trong nhóm.
- B. **Không giới hạn** — đếm đúng những gì hộp nhận để biết đang hiển thị.
- C. Khác (ghi rõ).

**Đề xuất của AI:** A nếu Q02 chọn B (tổng số); nếu Q02 chọn A (chưa đọc) thì B cũng được vì số chưa đọc tự nhỏ. Nên
chọn sao cho **số trên ô = số dòng người dùng thấy khi bấm vào** (Q04), tránh thắc mắc "ô ghi 3 mà mở ra 5".
**Ảnh hưởng:** phép đếm, AC. **Ai trả lời:** BA.
**Trả lời:** A — 365 ngày gần nhất, **giống khoảng mặc định trong bộ lọc nâng cao của màn *Phiếu trình nhận để biết***. (BA trả lời 07/10/2026) · AI đã xác minh: màn đó mặc định lọc từ hôm nay trừ 365 ngày đến hôm nay (`SubmissionFormReceiveToKnowVM.java:103-104`) → khớp.

### Q04 · Bấm vào ô thì mở gì · BLOCKING

**Hiện trạng:** các ô phiếu trình bấm vào mở đúng hộp / tab tương ứng với bộ lọc mặc định (PT 1.2b). Hộp nhận để biết
hiện **chưa có bộ lọc "chưa đọc"**, chỉ lọc theo tiêu đề, người gửi, ngày gửi (PT NV-13).
**Câu hỏi:** Bấm ô mở màn nào, lọc sẵn gì?

- A. Mở menu *Phiếu trình nhận để biết* **như bấm menu** (toàn bộ hộp, chưa đọc in đậm) — không thêm bộ lọc.
- B. Mở hộp đó và **lọc sẵn chỉ phiếu chưa đọc** (phải thêm bộ lọc / tab "Chưa đọc" cho hộp — việc lớn hơn).
- C. Khác (ghi rõ).

**Đề xuất của AI:** A — giống cách thông báo hiện nay mở hộp; nếu Q02 chọn A thì số trên ô là "chưa đọc", mở ra vẫn
thấy đủ hộp, phiếu chưa đọc in đậm đã đủ nhận ra. **Ảnh hưởng:** điều hướng, phạm vi code (B đụng hộp nhận để biết).
**Ai trả lời:** BA.
**Trả lời:** A — mở menu *Phiếu trình nhận để biết* như bấm menu, không áp thêm bộ lọc. (BA trả lời 07/10/2026)

### Q05 · Kênh áp dụng · BLOCKING

**Hiện trạng:** trang chủ web và trang chủ ứng dụng di động dùng **hai cơ chế khác nhau** (HT 1.5) [Hiện trạng].
**Câu hỏi:** Ô mới cần ở đâu?

- A. **Chỉ web** (cỡ S).
- B. Cả web lẫn **ứng dụng di động** (phải làm thêm ở trang chủ mobile — lên cỡ L, nên tách yêu cầu riêng).

**Đề xuất của AI:** A. **Ảnh hưởng:** cỡ yêu cầu, phạm vi. **Ai trả lời:** BA / người đề xuất.
**Trả lời:** B — **cả web lẫn ứng dụng di động**. (BA trả lời 07/10/2026) → yêu cầu lên **cỡ L**; phần mobile còn 3 điểm chưa chốt, xem TBD-01…TBD-03 trong `dac-ta.md`.

### Q06 · Nhãn và vị trí ô · NON-BLOCKING

**Hiện trạng:** trong nhóm "Phiếu trình", nhãn các ô ngắn (*Chờ xử lý*, *Đang xử lý*, *Đã phê duyệt*, *Tất cả*, *Xin
ý kiến*); nhóm Văn bản đến dùng nhãn *Nhận để biết* (PT 1.2b; VBĐ 1.3).
**Câu hỏi:** Nhãn trên ô và vị trí?

- A. Nhãn **"Nhận để biết"**, đứng **cuối nhóm** (ô thứ 6, sau *Xin ý kiến*).
- B. Nhãn **"Phiếu trình nhận để biết"** (đúng tên menu, dài hơn các ô khác).
- C. Vị trí khác (ghi rõ, vd. ngay sau *Chờ xử lý*).

**Đề xuất của AI:** A — tên nhóm đã là "Phiếu trình", lặp lại là thừa; nhất quán với ô văn bản đến. Tên trong *Cấu hình
trang chủ* vẫn là "Nhận để biết" dưới nhóm "Phiếu trình". **Ai trả lời:** BA.
**Trả lời:** A — nhãn **"Nhận để biết"**, đứng cuối nhóm (ô thứ 6, sau *Xin ý kiến*). (BA trả lời 07/10/2026)

### Q07 · Khi không có phiếu nào · NON-BLOCKING

**Hiện trạng:** ô *Xin ý kiến* luôn hiện (kể cả 0); các ô khác trong nhóm **ẩn khi không có số** (chưa đếm xong) và
hiện 0 khi đếm ra 0 (PT 1.2b, code `HomeWidgetRestController.java:1636-1669`) [Hiện trạng].
**Câu hỏi:** Người chưa từng được chuyển phiếu nào thì ô hiện thế nào?

- A. **Vẫn hiện, số 0** — giống ô *Xin ý kiến*.
- B. **Ẩn ô** khi số = 0.

**Đề xuất của AI:** A — ô ẩn / hiện thất thường làm người dùng tưởng cấu hình bị đổi. **Ai trả lời:** BA.
**Trả lời:** A — vẫn hiện, số 0. (BA trả lời 07/10/2026)

### Q08 · Chế độ trang chủ đơn giản · NON-BLOCKING

**Hiện trạng:** ở chế độ *đơn giản*, nhóm "Phiếu trình" chỉ hiện ô *Chờ xử lý* (HT BR-39; PT 1.2b).
**Câu hỏi:** Ô mới có hiện ở chế độ đơn giản không?

- A. **Không** — như 4 ô còn lại của nhóm; chỉ hiện ở chế độ đầy đủ.
- B. **Có, cho mọi người** — coi "có phiếu để biết chưa xem" là việc cần thấy ngay.

**Đề xuất của AI:** A — giữ chế độ đơn giản đúng nghĩa "chỉ việc phải xử lý". **Ai trả lời:** BA.
**Trả lời:** **Khác B:** ô *Nhận để biết* **có hiện ở chế độ trang chủ đơn giản** (BA trả lời 07/10/2026: "thêm 1 trạng thái Nhận để biết ở Chế độ trang chủ đơn giản") → khai ô mới hiện cho mọi người ở chế độ đơn giản, thành ô thứ 2 của nhóm *Phiếu trình* ở chế độ này (hiện chỉ có *Chờ xử lý*).

### Q09 · Người đã tự cấu hình trang chủ trước đó · NON-BLOCKING

**Hiện trạng:** cấu hình cá nhân lưu tạm, ô mới tự được gộp vào danh sách của người đã lưu cấu hình (hiện trạng mục 4,
5). ⚠ Trạng thái bật / tắt mặc định của ô mới với người này chưa xác minh.
**Câu hỏi:** Người đã từng vào *Cấu hình trang chủ* bấm Lưu (có cấu hình riêng) thì ô mới ra sao?

- A. **Tự bật** cho mọi người, kể cả người đã có cấu hình riêng (đúng nghĩa "mặc định hiển thị"); ai không muốn thì tắt.
- B. Chỉ bật cho người **chưa có** cấu hình riêng; người đã có thì ô ở trạng thái tắt, tự vào bật.

**Đề xuất của AI:** A — yêu cầu nói "mặc định hiển thị"; B làm nhiều người không biết có ô mới. **Ai trả lời:** BA.
**Trả lời:** A — tự bật cho mọi người, kể cả người đã lưu cấu hình riêng. (BA trả lời 07/10/2026)

## Tổng hợp

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 9 |
| BLOCKING chưa trả lời | 0 |
| Đã chốt | 9 (BA trả lời 07/10/2026) |

**Không hỏi (tri thức đã trả lời hoặc là việc kỹ thuật):** cách bật / tắt ở *Cấu hình trang chủ* (cơ chế sẵn có tới
từng ô con — HT NV-16); ai được chuyển / nhận để biết (PT NV-13, BR-39, BR-40 [Đã xác nhận]); cấu hình lưu tạm (HT
BR-38, Q10 — nêu rủi ro, không gói vào yêu cầu này).
