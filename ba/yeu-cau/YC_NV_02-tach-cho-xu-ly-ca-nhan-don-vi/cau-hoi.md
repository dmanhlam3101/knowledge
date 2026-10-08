# YC_NV_02 — DANH SÁCH CÂU HỎI CẦN XÁC NHẬN (vòng 1 — ĐÃ TRẢ LỜI 08/10/2026)

**Yêu cầu:** YC_NV_02 — Tách ô trang chủ *Chờ xử lý* thành **Chờ xử lý cá nhân** và **Chờ xử lý đơn vị**; mặc định trang
chủ chỉ hiện Chờ xử lý cá nhân; văn thư vào *Cấu hình trang chủ* bật thêm Chờ xử lý đơn vị ·
**Gửi tới:** BA / người đề xuất · **Ngày gửi:** 07/10/2026 · **Ngày trả lời:** 08/10/2026

> **Trạng thái:** đã trả lời đủ 10 câu → AI đã viết `dac-ta.md` bản 1.0. Hai điểm trong câu trả lời bị hiện trạng code
> phủ nhận hoặc cần làm rõ thêm, AI chuyển thành TBD trong `dac-ta.md` mục 11 (xem phần **Điểm phát sinh** ở cuối file).

## Phiếu ý tưởng (nguyên văn BA)

> tách chờ xử lý cá nhân và chờ xử lý đơn vị. Mặc định trang chủ sẽ chỉ hiển thị Chờ xử lý cá nhân. Với vai trò văn thư
> vào cấu hình trang chủ hiển thị chờ xử lý đơn vị
>
> * phân tích nghiệp vụ: tách widget CXL đơn vị và CXL cá nhân. Hiện tại văn thư chỉ hiển thị chờ xử lý của đơn vị và ấn
> link tới tab chờ xử lý văn bản đến văn bản đơn vị -, nhớ sửa cả trong cấu hình trang chủ

| Dòng phiếu | Đã có | Ghi chú |
|---|---|---|
| Muốn gì | Có | Một ô *Chờ xử lý* hiện tại → hai ô: *Chờ xử lý cá nhân* và *Chờ xử lý đơn vị*; sửa cả màn *Cấu hình trang chủ* |
| Ai dùng | **Đã chốt (Q01, Q03, Q04)** | Mọi vai trò dùng ô cá nhân; chỉ văn thư có ô đơn vị |
| Vì sao | **Đã chốt (Q01-A)** | Văn thư nhìn ô *Chờ xử lý* chỉ thấy số của đơn vị nên bỏ sót văn bản gửi riêng cho mình |
| Một tình huống thật | **Đã chốt (Q01-A)** | Văn thư đơn vị: văn bản gửi đích danh mình không được ô nào đếm |
| Kết quả mong muốn | **Đã chốt (Q02, Q05)** | Hai ô, mỗi ô mở đúng tab của hộp *Văn bản chờ xử lý* |
| Kênh web / mobile | **Đã chốt (Q10-B)** | Cả web và ứng dụng di động |

**Phân hệ:** chính `he-thong` (cơ chế trang chủ, widget, màn *Cấu hình trang chủ* — HT NV-16) · liên quan
`van-ban/den` (nội dung và số đếm của nhóm ô "Văn bản đến", hộp việc Chờ xử lý, tab *Văn bản đơn vị / Văn bản cá nhân* —
VBĐ 1.3, NV-01, NV-02). **Cỡ: L** — đụng 2 phân hệ, thêm ô trang chủ mới (cần thêm dòng danh mục `HOME_WIDGET`), và sau
Q10-B thì đụng cả trang chủ ứng dụng di động (cơ chế riêng). Không đổi trạng thái văn bản, không thêm bảng nghiệp vụ.

## Hiện trạng (AI dựng từ tri thức + code)

**Trang chủ hiện có một ô "Chờ xử lý" trong nhóm "Văn bản đến"** (nhóm gồm 8 ô: Chờ tiếp nhận, Chờ xử lý, Sắp đến hạn,
Quá hạn, Đề nghị trả lại, Đã xử lý, Đã hoàn thành, Nhận để biết — VBĐ 1.3, DB DEV `HOME_WIDGET` ngày 2026-10-01).

1. **Hộp việc tính theo dòng nhận, không theo văn bản.** Mỗi lần một người hoặc một đơn vị được nhận văn bản là một
   dòng nhận riêng. Người không phải văn thư **chỉ có dòng cá nhân**; văn thư có **cả dòng đơn vị** (của mọi đơn vị mình
   làm văn thư) **lẫn dòng cá nhân** (VBĐ BR-01, BR-02).
2. **Màn *Văn bản chờ xử lý* đã tách sẵn hai tab** *Văn bản đơn vị* / *Văn bản cá nhân*, và **chỉ văn thư thấy hàng tab
   này** (VBĐ NV-01). Với văn thư, tab đơn vị còn đòi văn bản **đã vào sổ** của đơn vị mình (VBĐ NV-02).
3. **Số trên ô *Chờ xử lý* hiện là số theo phạm vi ĐƠN VỊ.** Phía máy chủ đếm hộp "chờ xử lý" với phạm vi *đơn vị*
   (`backend2.0/.../thread/DocumentThread.java:253-258`). Vì người không phải văn thư không có dòng đơn vị, với họ con số
   vẫn ra văn bản của chính mình. ✔ Đã xác minh trên code; BA xác nhận lại ở Q02.
4. **Bấm ô *Chờ xử lý* mở hộp *Văn bản chờ xử lý*** (`HomeWidgetRestController.java:841-843`), và trong màn đó **văn thư
   luôn được đặt sẵn tab *Văn bản đơn vị*** (`DocumentPendingProcessingVM.java:776-778`). ✔ Đã xác minh trên code.
5. **Máy chủ ĐÃ có sẵn số đếm "chờ xử lý cá nhân" riêng** (`DocumentController.java:2605-2610` và `:3005-3006`), hiện chỉ
   dùng cho số trên tab của màn hộp việc, **chưa có ô trang chủ nào dùng**. Cũng đã có sẵn đường mở hộp việc vào **tab
   cá nhân** (`DocumentPendingProcessingVM.java:782-789`, tham số `groupDocType` ở `:11965-11974`).
6. **Màn *Cấu hình trang chủ*** (khung người dùng góc phải): người dùng bật / tắt từng ô, xóa ô tự tạo, tạo ô riêng
   (HT NV-16). Danh sách ô lấy từ danh mục `HOME_WIDGET`; thêm ô mới = thêm dòng danh mục bằng script.
7. **[Hiện trạng] Cấu hình trang chủ của từng người chỉ được giữ TẠM (memcached), không có bảng trong CSDL** — mất khi
   hệ thống khởi động lại, và **có hạn 86.400 giây = 1 ngày** kể từ lần ghi cuối
   (`application.properties:284` → `Memcached.java:285`; HT BR-38). ✔ Đã xác minh trên code — khác với giả định ở câu
   trả lời Q07 ("không có hạn") → chuyển thành TBD-06.
8. **Chế độ trang chủ "đơn giản / đầy đủ".** Ở chế độ **đơn giản**, mỗi ô khai cờ ai được thấy: 1 chỉ văn thư · 2 chỉ
   người không phải văn thư · 3 mọi người (HT BR-39; `HomeWidgetRestController.java:1770-1783`). Ở chế độ **đầy đủ**
   hiện **không có** cơ chế ẩn ô theo vai trò.
9. **Trang chủ ứng dụng di động là cơ chế HOÀN TOÀN KHÁC:** danh sách ô lấy từ bảng `PERMISSION_DASHBOARD` gắn với menu
   gen-2 thiết bị MOBILE, cấu hình của từng người lưu thành **file JSON theo mã nhân viên** + memcached, không dùng
   `HOME_WIDGET` (`HomeServiceImpl.java:106-140, 319-348`). ✔ Đã xác minh trên code → sau Q10-B phát sinh TBD-04, TBD-05.

## Câu hỏi và câu trả lời

### Q01 · Tình huống thật và lý do · BLOCKING

**Câu hỏi:** Cho một tình huống thật: ai, đang làm gì, nhìn thấy số nào, và vì thế bỏ sót việc gì?

- A. Văn thư đơn vị: ô *Chờ xử lý* chỉ ra số của đơn vị, nên văn bản gửi riêng cho mình bị bỏ sót vì không có ô nào đếm.
- B. Người dùng không phân biệt được số nào là việc của mình, số nào của đơn vị.
- C. Khác.

**Đề xuất của AI:** A.
**Trả lời:** **A**

### Q02 · Mỗi ô đếm những văn bản nào · BLOCKING

**Câu hỏi:** Hai ô mới đếm đúng theo cách chia dòng nhận cá nhân / đơn vị sẵn có chứ?

- A. *CXL cá nhân* = văn bản gửi đích danh mình đang chờ mình xử lý · *CXL đơn vị* = văn bản gửi cho đơn vị mình làm văn
  thư, đã vào sổ, đang chờ xử lý. Bằng đúng số của hai tab trong hộp *Văn bản chờ xử lý*.
- B. Như A nhưng *CXL đơn vị* tính cả văn bản chưa vào sổ.
- C. Khác.

**Đề xuất của AI:** A.
**Trả lời:** **A.** Nói rõ thêm hiện trạng: *"Chờ xử lý với user không văn thư đã count cá nhân và chuyển vào màn cá
nhân rồi, chỉ có văn thư là hiển thị count của đơn vị và vào màn đơn vị."* → khớp đúng điểm 3 và 4 phần hiện trạng; với
người không phải văn thư, TO-BE chỉ là **đổi nhãn ô**, hành vi giữ nguyên.

### Q03 · "Mặc định chỉ hiện Chờ xử lý cá nhân" áp cho ai · BLOCKING

**Câu hỏi:** Ngay sau khi triển khai, người dùng mở trang chủ lần đầu thì thấy gì?

- A. Mọi vai trò (kể cả văn thư) chỉ thấy *CXL cá nhân*; *CXL đơn vị* mặc định tắt, văn thư tự bật.
- B. Văn thư thấy sẵn cả hai ô; vai trò khác chỉ thấy *CXL cá nhân*.
- C. Khác.

**Đề xuất của AI:** A.
**Trả lời:** *"A: văn thư mặc định bật hết, k phải Văn thư mặc định bật CXL cá nhân và luôn ẩn CXL đơn vị"*
→ **Nội dung này đúng là phương án B** (văn thư: cả hai ô bật sẵn; không phải văn thư: chỉ ô cá nhân, ô đơn vị **luôn
ẩn**). AI lấy **nguyên văn câu trả lời** làm chuẩn, ghi thành BR-06, BR-07 trong `dac-ta.md`. Lưu ý: điều này **khác lời
phiếu ý tưởng** ("mặc định chỉ hiển thị CXL cá nhân… văn thư vào cấu hình trang chủ bật") — văn thư **không phải vào cấu
hình để bật**, chỉ vào đó nếu muốn **tắt**. Đã ghi chú trong `dac-ta.md` mục 1.2.

### Q04 · Ai được bật ô *CXL đơn vị* trong Cấu hình trang chủ · BLOCKING

**Câu hỏi:** Ô *CXL đơn vị* xuất hiện trong danh sách *Cấu hình trang chủ* của những ai?

- A. Chỉ văn thư thấy ô này; vai trò khác không thấy, không bật được.
- B. Mọi người thấy và bật được; không phải văn thư thì ô hiện số 0.
- C. Mọi người thấy, nhưng không phải văn thư thì bật xong ô không hiện.

**Đề xuất của AI:** A.
**Trả lời:** **A** → nhất quán với Q03 ("luôn ẩn với người không phải văn thư"). Kéo theo: phải **làm mới** cơ chế lọc ô
theo vai trò cho chế độ trang chủ đầy đủ (hiện chỉ có ở chế độ đơn giản — hiện trạng điểm 8).

### Q05 · Bấm vào mỗi ô thì mở đi đâu · BLOCKING

**Câu hỏi:** Hai ô mới mở đi đâu, tab nào đang được chọn?

- A. *CXL cá nhân* → hộp *Văn bản chờ xử lý* tab **Văn bản cá nhân** · *CXL đơn vị* → cùng hộp, tab **Văn bản đơn vị**.
- B. Như A, và với người không phải văn thư (không có hàng tab) thì mở hộp như hiện nay.
- C. Khác.

**Đề xuất của AI:** A + B.
**Trả lời:** **A**

### Q06 · Có tách các ô còn lại trong nhóm "Văn bản đến" không · BLOCKING

**Câu hỏi:** Đợt này tách những ô nào?

- A. Chỉ ô *Chờ xử lý*.
- B. Thêm Sắp đến hạn, Quá hạn.
- C. Toàn bộ 7 ô.

**Đề xuất của AI:** A.
**Trả lời:** **A** → sáu ô còn lại giữ nguyên nhãn, số đếm, điều hướng (BR-15); B và C ghi vào mục "ngoài phạm vi".

### Q07 · Văn thư bật rồi có giữ được lâu dài không · BLOCKING

**Câu hỏi:** Cấu hình cá nhân chỉ nằm trong bộ nhớ tạm — chấp nhận, hay làm luôn phần lưu bền?

- A. Lưu bền vào CSDL (thêm bảng + migration).
- B. Giữ như hiện tại, ghi hạn chế vào tài liệu.
- C. Đặt cứng trong danh mục ô, người dùng không cấu hình.

**Đề xuất của AI:** A nếu chấp nhận thêm khối lượng; B nếu muốn ra nhanh.
**Trả lời:** *"hiện trạng đang lưu vào memcached và lưu là gì thì cứ thế cho đến khi thay đổi thôi, k có hạn"*
→ Hiểu là **phương án B: giữ nguyên cách lưu hiện tại, không thêm bảng** (AI ghi thành BR-14).
⚠ **Một phần câu trả lời không khớp code:** cấu hình **CÓ hạn 1 ngày** (`memcached.expiration.time = 86400` ở
`application.properties:284`, dùng ở `Memcached.java:285`) và mất khi hệ thống khởi động lại. Hệ quả thực tế **nhẹ** vì
mặc định ở Q03 đã đúng ý muốn: sau khi cấu hình hết hạn, văn thư vẫn thấy cả hai ô, người khác vẫn chỉ thấy ô cá nhân.
Chỗ bị ảnh hưởng chỉ là **người đã chủ động TẮT một ô**: trong vòng 1 ngày ô đó sẽ hiện lại. → **TBD-06**, xin BA xác
nhận chấp nhận.

### Q08 · Tên hai ô và thứ tự hiển thị · NON-BLOCKING

**Trả lời:** **A** — "Chờ xử lý cá nhân" rồi "Chờ xử lý đơn vị", đặt đúng vị trí ô *Chờ xử lý* cũ.

### Q09 · Chế độ trang chủ đơn giản · NON-BLOCKING

**Trả lời:** **A** — *CXL cá nhân* hiện cho mọi người (`SIMPLE_MODE = 3`); *CXL đơn vị* chỉ với văn thư
(`SIMPLE_MODE = 1`).

### Q10 · Phạm vi áp dụng · NON-BLOCKING

**Câu hỏi:** Đợt này làm ở đâu?

- A. Chỉ web. · B. Thêm ứng dụng di động. · C. Thêm xử lý cấu hình người dùng cũ.

**Đề xuất của AI:** A.
**Trả lời:** **B** — web **và** ứng dụng di động.
⚠ Kéo theo việc mới: trang chủ di động dùng **cơ chế khác hoàn toàn** (bảng `PERMISSION_DASHBOARD` + menu gen-2 thiết bị
MOBILE + file JSON cấu hình, hiện trạng điểm 9), nên cần thêm dòng danh mục riêng cho di động và **một bản phát hành ứng
dụng mới**. Còn phải xác nhận: trên ứng dụng di động có khái niệm tab *Văn bản đơn vị / Văn bản cá nhân* không, và ai
duyệt lịch phát hành. → **TBD-04, TBD-05**.

## Tổng hợp

| Mã | Nhóm | Mức | Đề xuất AI | Trả lời |
|---|---|---|---|---|
| Q01 | Tình huống thật, lý do | BLOCKING | A | A |
| Q02 | Mỗi ô đếm gì | BLOCKING | A | A (+ xác nhận hiện trạng người không phải văn thư đã đúng) |
| Q03 | "Mặc định" áp cho ai | BLOCKING | A | Nguyên văn = **phương án B**: văn thư bật cả hai, người khác luôn ẩn ô đơn vị |
| Q04 | Ai bật được ô đơn vị | BLOCKING | A | A |
| Q05 | Bấm ô mở đi đâu | BLOCKING | A | A |
| Q06 | Có tách các ô khác không | BLOCKING | A | A |
| Q07 | Cấu hình có giữ lâu dài | BLOCKING | A hoặc B | B (giữ hiện trạng) — kèm sai lệch về hạn 1 ngày → TBD-06 |
| Q08 | Tên ô, thứ tự | NON-BLOCKING | A | A |
| Q09 | Chế độ trang chủ đơn giản | NON-BLOCKING | A | A |
| Q10 | Phạm vi web / mobile | NON-BLOCKING | A | **B** (web + mobile) → TBD-04, TBD-05 |

| | Số lượng |
|---|---|
| Tổng số câu hỏi | 10 |
| BLOCKING chưa trả lời | 0 |
| Đã chốt | 10 |
| Điểm phát sinh sau khi trả lời | 3 (TBD-04, TBD-05 mobile · TBD-06 hạn lưu cấu hình) + 3 TBD kỹ thuật cho DEV (TBD-01 … TBD-03) |

## Điểm phát sinh — xem `dac-ta.md` mục 11

| TBD | Nội dung | Ai chốt | Chặn code? |
|---|---|---|---|
| TBD-01 | Mã `CODE` và `ID` dòng mới trong `HOME_WIDGET`; giữ hay bỏ dòng ô cũ `IN_CHO_XU_LY` | DEV / DBA | Không (có đề xuất) |
| TBD-02 | Số nhắc việc kèm ô: máy chủ có sẵn số nhắc việc theo phạm vi cá nhân chưa | DEV | Không |
| TBD-03 | Cách ẩn ô theo vai trò ở chế độ trang chủ đầy đủ (làm mới) | DEV | Không |
| TBD-04 | Trang chủ di động: ô tương ứng, màn hộp việc di động có tách cá nhân / đơn vị không | BA + DEV mobile | **Có** (phần mobile) |
| TBD-05 | Lịch phát hành ứng dụng di động, cùng đợt với web hay sau | BA / chủ dự án | **Có** (phần mobile) |
| TBD-06 | Chấp nhận cấu hình bật / tắt ô tự trở về mặc định sau ≤ 1 ngày, hay làm lưu bền | BA / chủ dự án | Không |

## Ghi chú cho DEV / tri thức (không cần BA làm gì)

- **Dùng lại được:** số đếm "chờ xử lý cá nhân" đã có ở máy chủ (`DocumentController.java:2605-2610`, `:3005-3006`);
  đường mở hộp việc vào đúng tab bằng tham số `groupDocType` (`DocumentPendingProcessingVM.java:11965-11974`).
- **Phải sửa HAI chỗ dựng trang chủ:** `HomeWidgetRestController.java:773-884` và `HomeVM.java:2985-3045` — cùng một
  nhóm ô "Văn bản đến" được dựng ở hai nơi.
- **Danh sách ô bật mặc định nằm trong code**, không nằm trong `HOME_WIDGET` (`defaultWidgetCodes` —
  `HomeWidgetRestController.java:793-804`); `HomeWidgetDAO.getHomeWidgets` chỉ đọc id, code, key_name, name,
  parent_code, simple_mode.
- **Mẫu script thêm ô:** `backend2.0/backendvoffice/sql/24122025_bi_tu_choi_insert_into_home_widget.sql` (ID lớn nhất
  đang thấy trong script repo là 46 — ID thật phải tra DB DEV).
- Phiên làm việc này **không kết nối được DB DEV** (không có `.env` ở gốc repo) nên mọi con số về bảng đều lấy từ ảnh
  chụp DB DEV ngày 2026-10-01 trong `knowledge/`, hoặc đánh dấu chưa xác minh.
- Khi YC_NV_02 chốt, cập nhật tri thức: `knowledge/he-thong` (NV-16 BR-38 / BR-39, câu hỏi 7.1 Q10 — đã có câu trả lời
  một phần từ Q07) và `knowledge/van-ban/den` (mục 1.3 bảng widget).
