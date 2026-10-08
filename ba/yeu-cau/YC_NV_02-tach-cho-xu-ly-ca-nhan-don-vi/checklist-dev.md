# YC_NV_02 — CHECKLIST DEV TRƯỚC KHI BÀN GIAO

> Bản tick được trong git. Bản có wireframe và trình bày đầy đủ: `thiet-ke-va-checklist.html` (mở bằng trình duyệt)
> hoặc link artifact đã gửi trong hội thoại. Đặc tả gốc: `dac-ta.md`.
>
> **Luật:** mọi mục chạy **trên con test** bằng tài khoản thật của môi trường test, không phải máy cá nhân.
> Mục chưa có bằng chứng = chưa làm. Mục tiêu: không gãy luồng đang chạy.
>
> Cách dùng: đổi `[ ]` thành `[x]`, ghi đường dẫn bằng chứng vào cột cuối rồi commit cùng code.

| | Tổng |
|---|---|
| Số mục | 34 |
| Môi trường bắt buộc | con test (DEV/UAT) |
| Bằng chứng gom tại | `evidence/YC_NV_02/<mã mục>/` |

## B0. Điều kiện vào — làm trước khi viết dòng code đầu tiên

- [ ] **B0-1** Chốt TBD-01 (mã + ID dòng danh mục ô), TBD-02 (số nhắc việc phạm vi cá nhân), TBD-03 (cách ẩn ô theo vai
      trò) với BA. · *Bằng chứng:* ba dòng kết luận điền vào mục 11 `dac-ta.md`. · Đường dẫn: ______
- [ ] **B0-2** SELECT trên con test lấy ID lớn nhất đang dùng của bảng danh mục ô, chọn ID mới không trùng (script repo
      đang dùng tới 46 — **không đoán**). · *Bằng chứng:* ảnh chụp kết quả SELECT + ngày. · Đường dẫn: ______
- [ ] **B0-3** Ghi mốc mã nguồn: nhánh + commit đang đứng (`git log -1 --oneline` trong `web-spring/` và `backend2.0/`).
      · *Bằng chứng:* hai dòng commit dán vào đây. · ______
- [ ] **B0-4** **Đo số TRƯỚC khi sửa** trên con test: thời gian tải trang chủ + số của 8 ô, với ≥1 văn thư và ≥1 chuyên
      viên. Không có số trước thì không chứng minh được là không gãy. · *Bằng chứng:* bảng số đo, ghi tài khoản + giờ. · ______

## B1. Dữ liệu danh mục trên con test

- [ ] **B1-1** Viết **script tiến** và **script lùi** cho dòng danh mục ô (mẫu:
      `backend2.0/backendvoffice/sql/24122025_bi_tu_choi_insert_into_home_widget.sql`). · *Bằng chứng:* 2 file + thứ tự
      chạy. · ______
- [ ] **B1-2** Chạy script tiến trên con test, SELECT kiểm lại: đúng 2 dòng chờ xử lý trong nhóm Văn bản đến, nhãn đúng
      từng chữ, cờ chế độ đơn giản đúng (cá nhân = mọi người, đơn vị = chỉ văn thư). · *Bằng chứng:* ảnh SELECT. · ______
- [ ] **B1-3** Thử **chạy lùi** rồi chạy lại tiến trên con test; sau khi lùi trang chủ phải về đúng 8 ô như cũ. ·
      *Bằng chứng:* 3 ảnh trang chủ (trước · sau lùi · sau chạy lại). · ______
- [ ] **B1-4** Không chạm dòng danh mục của ô khác / phân hệ khác: đếm số dòng bảng danh mục trước và sau, chỉ lệch đúng
      số dòng mình thêm. · *Bằng chứng:* 2 số đếm. · ______

## B2. Code — ba chỗ dễ làm gãy luồng

- [ ] **B2-1** Sửa đủ **HAI** chỗ dựng nhóm ô trang chủ: `HomeWidgetRestController` **và** `HomeVM`. Sửa một chỗ thì hai
      đường vào trang chủ lệch nhau. · *Bằng chứng:* diff cả hai file. · ______
- [ ] **B2-2** Thêm mã ô mới vào **danh sách ô bật mặc định trong code** (không nằm ở bảng danh mục). Quên bước này thì ô
      mới không hiện với người chưa từng cấu hình. **Nặng nhất với vai trò không phải văn thư:** ô cũ nay là ô đơn vị và bị
      ẩn với họ, nên nếu ô cá nhân không bật mặc định thì họ **mất trắng** ô chờ xử lý trên trang chủ. · *Bằng chứng:* diff + ảnh trang chủ của tài khoản chưa từng mở màn
      cấu hình. · ______
- [ ] **B2-3** Dùng **số đếm cá nhân đã có sẵn** ở máy chủ, không viết truy vấn mới. · *Bằng chứng:* diff + số lượt truy
      vấn khi mở trang chủ trước/sau. · ______
- [ ] **B2-4** Nhãn hai ô lấy từ **file tài nguyên ngôn ngữ**, không viết cứng tiếng Việt trong code. · *Bằng chứng:*
      khóa ngôn ngữ mới trong diff. · ______
- [ ] **B2-5** Điều kiện ẩn ô theo vai trò áp ở **cả trang chủ VÀ màn Cấu hình trang chủ**. · *Bằng chứng:* 2 ảnh bằng
      tài khoản chuyên viên. · ______

## B3. Test theo vai trò trên con test — sáu tài khoản

- [ ] **B3-1** **Văn thư 1 đơn vị:** thấy đủ 2 ô, số đúng, bấm từng ô mở đúng tab. · *Bằng chứng:* 1 ảnh trang chủ + 2
      ảnh hộp việc thấy rõ tab đang chọn. · ______
- [ ] **B3-2** **Văn thư nhiều đơn vị:** số ô đơn vị = **tổng** các đơn vị mình làm văn thư. · *Bằng chứng:* ảnh + phép
      cộng từng đơn vị. · ______
- [ ] **B3-3** **Chuyên viên:** chỉ 1 ô cá nhân, số và hành vi y như trước khi sửa (so với B0-4). Nhóm đông nhất, gãy ở
      đây là gãy to nhất. · *Bằng chứng:* ảnh + so số. · ______
- [ ] **B3-4** **Lãnh đạo / Thủ trưởng:** như chuyên viên; thêm: màn *Theo dõi văn bản đến đơn vị* vẫn mở và vẫn đúng
      số. · *Bằng chứng:* 2 ảnh. · ______
- [ ] **B3-5** **Trợ lý lãnh đạo:** văn bản nhận thay lãnh đạo vẫn nằm trong ô cá nhân của trợ lý. · *Bằng chứng:* ảnh +
      1 mã văn bản cụ thể. · ______
- [ ] **B3-6** **Tài khoản vừa bị gỡ vai trò văn thư:** ô đơn vị biến mất ở cả trang chủ và màn cấu hình, kể cả khi trước
      đó đã bật; không lỗi màn. · *Bằng chứng:* ảnh trước và sau khi gỡ. · ______

## B4. Đối soát số — điều kiện nghiệm thu khắt khe nhất

- [ ] **B4-1** **Số trên ô = số dòng trong danh sách** khi bấm vào, cả 2 ô, với 3 tài khoản khác nhau. Lệch 1 dòng cũng
      là lỗi. · *Bằng chứng:* bảng 3 dòng (tài khoản · số trên ô · số dòng đếm được). · ______
- [ ] **B4-2** Với tài khoản văn thư đã đo ở B0-4: **số ô đơn vị = số ô "Chờ xử lý" cũ**. Khác thì phải truy nguyên
      nhân. · *Bằng chứng:* so sánh trước/sau + kết luận. · ______
- [ ] **B4-3** Văn bản gửi đơn vị **chưa vào sổ** không bị đếm vào ô đơn vị: ô *Chờ tiếp nhận* +1, ô *Chờ xử lý đơn vị*
      không đổi. · *Bằng chứng:* ảnh trước/sau + mã văn bản test. · ______
- [ ] **B4-4** Văn bản **Bị trả lại** vẫn được đếm đúng ô (hộp chờ xử lý vốn gộp nhóm này). · *Bằng chứng:* 1 tình huống
      trả lại trên con test + số trước/sau. · ______
- [ ] **B4-5** **Dọn sạch dữ liệu test** đã tạo (tiền tố thống nhất). Con test là môi trường dùng chung. · *Bằng chứng:*
      danh sách mã đã tạo và đã dọn. · ______

## B5. Regression — phần chống gãy luồng

- [ ] **B5-1** Sáu ô còn lại của nhóm Văn bản đến giữ nguyên nhãn, số, điều hướng (so B0-4, cùng tài khoản, cùng ngày). ·
      *Bằng chứng:* bảng 6 dòng trước/sau. · ______
- [ ] **B5-2** Nhóm ô phân hệ khác vẫn hiện, vẫn đúng số: Văn bản đi, Phiếu trình, Nhiệm vụ, Lịch họp, Nhắc việc, KPI. ·
      *Bằng chứng:* 1 ảnh cả trang chủ. · ______
- [ ] **B5-3** Mở hộp *Văn bản chờ xử lý* **từ menu** vẫn vào tab mặc định như cũ (văn thư = tab Văn bản đơn vị). Chỗ dễ
      gãy nhất vì sửa cùng một chỗ trong code. · *Bằng chứng:* ảnh hộp việc mở từ menu. · ______
- [ ] **B5-4** Đổi tab Văn bản đơn vị ↔ Văn bản cá nhân 3 lần, danh sách đúng phạm vi, không trộn. · *Bằng chứng:* 2
      ảnh. · ______
- [ ] **B5-5** Màn Cấu hình trang chủ: bật, tắt, **tạo ô riêng** của nhóm khác vẫn chạy; lưu rồi mở lại trang chủ. ·
      *Bằng chứng:* ảnh trước/sau khi lưu. · ______
- [ ] **B5-6** Đổi qua lại **chế độ đơn giản ↔ đầy đủ**, với cả văn thư và chuyên viên (4 tổ hợp). · *Bằng chứng:* 4
      ảnh. · ______
- [ ] **B5-7** Trang chủ **ứng dụng di động** vẫn chạy bình thường sau khi đổi danh mục phía web (di động dùng danh mục
      riêng). · *Bằng chứng:* ảnh trang chủ app trỏ con test. · ______
- [ ] **B5-8** Chạy lại **test tự động vùng ảnh hưởng** trước, rồi **bộ đầy đủ**. Báo cáo tách rõ `pass · fail ·
      BLOCKED`. · *Bằng chứng:* log kết quả + giờ chạy + môi trường. · ______

## B6. Cache và khởi động lại

- [ ] **B6-1** Xóa cache cấu hình → mở lại trang chủ: văn thư thấy cả 2 ô, vai trò khác chỉ thấy ô cá nhân. ·
      *Bằng chứng:* ảnh với 2 tài khoản. · ______
- [ ] **B6-2** **Khởi động lại ứng dụng** trên con test → trang chủ về đúng mặc định (không về trạng thái trống). Hạn lưu
      cấu hình là 1 ngày và mất khi khởi động lại. · *Bằng chứng:* ảnh sau khi khởi động lại. · ______
- [ ] **B6-3** Tài khoản có **cấu hình cũ** lưu từ trước khi lên bản mới: không mất ô, không lỗi, không hiện ô trùng. ·
      *Bằng chứng:* ảnh của tài khoản đã cấu hình trước khi cài bản mới. · ______

## B7. Hiệu năng và bảo mật

- [ ] **B7-1** Thời gian tải trang chủ **không tăng quá 10%** so với B0-4 (đo 3 lần, tài khoản văn thư nhiều văn bản,
      lấy trung bình). · *Bằng chứng:* bảng 3 lần đo trước/sau. · ______
- [ ] **B7-2** Người **không phải văn thư** không lấy được số của đơn vị bằng bất kỳ đường nào (thử gọi trực tiếp đường
      lấy số trang chủ bằng phiên chuyên viên). · *Bằng chứng:* kết quả gọi, đã che thông tin phiên. · ______
- [ ] **B7-3** Không có lỗi trên console trình duyệt và không có lỗi mới trong log máy chủ khi: mở trang chủ → bấm 2 ô →
      mở màn cấu hình → lưu. · *Bằng chứng:* đoạn log đúng khoảng thời gian thao tác. · ______

## B8. Hồ sơ bàn giao

- [ ] **B8-1** Danh sách file đã sửa + danh sách script phải chạy **kèm thứ tự** (trước/sau khi khởi động ứng dụng). ·
      *Bằng chứng:* trang hướng dẫn phát hành. · ______
- [ ] **B8-2** **Điều kiện rút lại bản phát hành**: dấu hiệu nào thì rút, các bước rút (gồm script lùi đã thử ở B1-3). ·
      *Bằng chứng:* mục rollback trong hướng dẫn phát hành. · ______
- [ ] **B8-3** Gom toàn bộ ảnh chụp + log về một chỗ, **đặt tên theo mã mục** (B3-2, B4-1…). · *Bằng chứng:* thư mục
      bằng chứng + bảng đối chiếu mã mục. · ______
- [ ] **B8-4** Những gì **chưa làm được** ghi rõ thay vì để trống (ví dụ phần ứng dụng di động nếu TBD-04/TBD-05 còn
      mở). · *Bằng chứng:* mục "ngoài phạm vi đợt này". · ______

## Hai điểm chặn còn mở — không phải việc của DEV

- **Ứng dụng di động:** chờ BA chốt TBD-04 (ô tương ứng trên trang chủ di động, màn đích) và TBD-05 (lịch phát hành app).
  Trang chủ di động dùng **danh mục riêng** và cần bản phát hành ứng dụng mới → không đi cùng bản web nếu còn mở.
- **Hạn lưu cấu hình 1 ngày:** hạn chế sẵn có của hệ thống (TBD-06, BA đang xác nhận). DEV **không tự thêm bảng** để lưu
  bền khi chưa có yêu cầu riêng.

## Ký bàn giao

| Vai trò | Họ tên | Ngày | Kết luận |
|---|---|---|---|
| DEV thực hiện | | | Đã chạy đủ 34 mục trên con test · còn thiếu: ______ |
| Tester nhận bàn giao | | | Nhận / Trả lại vì: ______ |
