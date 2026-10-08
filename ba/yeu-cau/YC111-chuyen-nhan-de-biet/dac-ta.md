**TÀI LIỆU ĐẶC TẢ YÊU CẦU CHỨC NĂNG**

**YC111 - VĂN BẢN ĐẾN KHÔNG CẦN XỬ LÝ: CHUYỂN NHẬN ĐỂ BIẾT SANG ĐÃ XỬ LÝ VÀ TỰ CHUYỂN THÀNH NHẬN ĐỂ BIẾT**

**Hệ thống Văn bản và Điều hành tỉnh Khánh Hòa**

| Thuộc tính | Giá trị |
|---|---|
| Mã yêu cầu | YC111 |
| Chức năng | Văn bản đến — chuyển văn bản, Nhận để biết, hoàn thành |
| Phân hệ (knowledge) | `van-ban/den` (chính) · `van-ban/chuyen-van-ban` · `lich-nhac-viec` |
| Loại yêu cầu | Bổ sung nghiệp vụ (đổi trạng thái luồng nhận) |
| Loại tài liệu | Đặc tả yêu cầu chức năng (BA/FRD) |
| Phiên bản | 1.0 |
| Trạng thái | DRAFT |
| Ngày cập nhật | 02/10/2026 |

> Ký hiệu nguồn: `VBĐ` = `knowledge/van-ban/den`, `CVB` = `knowledge/van-ban/chuyen-van-ban`, `Qxx (YC111)` = câu trả lời
> của BA trong `cau-hoi.md`. Nhãn mục: 🟦 BA viết · 🟩 AI điền · 🟨 AI soạn → BA chốt. **BA chỉ cần đọc mục 🟦 và 🟨.**
> Câu ghi *(đề xuất AI)* là chỗ BA chưa nói, AI đề xuất cho trọn luồng — BA đồng ý hoặc sửa.

---

# LỊCH SỬ THAY ĐỔI `[A1]` · 🟦

| Phiên bản | Ngày | Nội dung | Người thực hiện |
|---|---|---|---|
| 1.0 | 02/10/2026 | Bản đầu tiên — AI soạn từ phiếu ý tưởng + trả lời vòng 1 (Q01–Q10) | AI (ba-assistant) · BA phụ trách: {{Họ tên BA}} |

# PHÊ DUYỆT / XÁC NHẬN `[A2]` · 🟦

| Vai trò | Họ tên | Trạng thái | Ngày | Ghi chú |
|---|---|---|---|---|
| BA phụ trách | | Chưa xác nhận | | |
| DEV phụ trách | | Chưa xác nhận | | |
| Tester phụ trách | | Chưa xác nhận | | |
| Đại diện nghiệp vụ/Khách hàng | Anh Long | Chưa xác nhận | | Người đề xuất |

# MỤC LỤC

0. Phiếu ý tưởng
1. Thông tin chung
2. Phạm vi và vai trò
3. Tổng quan yêu cầu chức năng
4. Business Rules
5. Luồng nghiệp vụ / Use Case
6. Đặc tả màn hình và trường dữ liệu
7. Xử lý ngoại lệ và trường hợp biên
8. Acceptance Criteria
9. Ma trận kiểm thử và truy vết
10. Phạm vi kỹ thuật, kiến trúc và mapping CSDL
11. Các điểm cần xác nhận (TBD)

---

# 0. PHIẾU Ý TƯỞNG · 🟦 BA

- **Muốn gì:** Có những văn bản đến chờ xử lý nhưng không cần xử lý. (1) Người giữ văn bản chuyển cho người khác chỉ để
  biết thì văn bản của người chuyển phải sang *Đã xử lý* (hiện vẫn nằm *Chờ xử lý*); người Nhận để biết đọc hết thì kết
  thúc, người chuyển muốn thì chủ động bấm kết thúc. (2) Người nhận được tự chuyển văn bản của mình thành *Nhận để biết*.
- **Ai dùng:** người dùng chuyển văn bản cá nhân hoặc văn bản đơn vị cho cá nhân / đơn vị, tất cả với vai trò Nhận để
  biết (Q01 YC111); người nhận văn bản cá nhân với vai trò Chủ trì / Phối hợp (ý 2).
- **Vì sao cần:** văn bản không cần xử lý vẫn nằm ở *Chờ xử lý*, làm hộp việc và số đếm không đúng thực tế.
- **Một tình huống thật cụ thể:** {{BA bổ sung — Q01 chưa có ví dụ cụ thể}}
- **Kết quả mong muốn đo được:** chuyển chỉ Nhận để biết xong, văn bản rời *Chờ xử lý* ngay; khi mọi người Nhận để biết
  đã đọc, văn bản tự *Đã hoàn thành* mà người chuyển không phải bấm gì; người nhận đổi sang Nhận để biết bằng 1 nút + 1
  xác nhận.
- **Kênh:** Web và Mobile (Q10 YC111) · **Gấp không:** {{BA bổ sung}}

---

# 1. THÔNG TIN CHUNG `[A3]` · 🟦 1.1–1.2 · 🟨 1.3 (AS-IS 🟩) · 🟩 1.4 · 🟨 1.5

## 1.1. Mục đích

- Khi người giữ văn bản đến **chuyển văn bản mà mọi người / đơn vị nhận đều là Nhận để biết**, hệ thống đưa văn bản của
  người chuyển sang *Đã xử lý*; khi **tất cả** người Nhận để biết đã đọc, hệ thống **tự hoàn thành** văn bản của người
  chuyển.
- Khi người nhận văn bản cá nhân (Chủ trì / Phối hợp) bấm nút **Nhận để biết** ở màn chi tiết văn bản, hệ thống hoàn
  thành văn bản của người đó, đổi vai trò nhận thành Nhận để biết và đưa văn bản sang hộp *Văn bản nhận để biết*.

## 1.2. Bối cảnh nghiệp vụ

- Yêu cầu gốc (nguyên văn): "Có những văn bản đến chờ xử lý nhưng ko cần xử lý: 1. Chuyển cho các cá nhân khác trong phòng
  để xem để biết, người chuyển chưa sang Đã xử lý => Mong muốn sang đã xử lý. 2. Cá nhân đó muốn tự chuyển thành Nhận để
  biết của mình." — Ghi chú anh Long: "Nếu chuyển nhận để biết ng nhận để biết đọc hết hết thì két thúc. còn muốn thì chủ
  động bấm két thúc".
- Chức năng nghiệp vụ chính: chuyển văn bản đến; Nhận để biết; hoàn thành văn bản đến.
- Đường vào chức năng:
  - Ý 1: Văn bản đến → *Văn bản chờ xử lý* (hoặc tab *Tất cả*, hộp *Văn bản nhận để biết*) → chọn văn bản → *Chuyển*.
  - Ý 2: Văn bản đến → *Văn bản chờ xử lý* hoặc tab *Tất cả* → mở chi tiết văn bản → nút *Nhận để biết*.
- Vấn đề hiện tại: chuyển chỉ cho Nhận để biết thì người chuyển vẫn giữ văn bản ở *Chờ xử lý* và phải tự bấm Hoàn thành
  (CVB BR-14, VBĐ BR-41); người được giao xử lý nhầm không có cách tự đánh dấu "chỉ để biết" (VBĐ NV-11).
- Kết quả mong muốn: như mục 0.

## 1.3. Hiện trạng (AS-IS) và thay đổi (TO-BE)

> AS-IS lấy theo tri thức `knowledge/` (baseline `kha_develop`). **⚠ CONFLICT:** khi kiểm code trên máy (web-spring,
> backend2.0) AI thấy **đã có một phần** chức năng này mà tri thức chưa ghi — chi tiết và chỗ lệch với tài liệu này ở
> mục 10.9. Tài liệu này là yêu cầu chuẩn; code có sẵn chỉ là điểm xuất phát cho DEV.

| STT | Nội dung | Hiện tại (AS-IS) | Yêu cầu (TO-BE) | Nguồn AS-IS |
|---|---|---|---|---|
| 1 | Văn bản người chuyển khi chuyển chỉ Nhận để biết | Vẫn ở *Chờ xử lý* (3), người chuyển tự bấm Hoàn thành [Đã xác nhận 2026-10-01] | Sang *Đã xử lý* (4) ngay khi chuyển — **đổi quy tắc đã chốt**, BA xác nhận ở Q02 YC111 | CVB BR-14; VBĐ BR-41 |
| 2 | Khi mọi người Nhận để biết đã đọc | Không có gì xảy ra; đọc chỉ ghi thời điểm đọc | Văn bản người chuyển tự *Đã hoàn thành* (5) | VBĐ BR-24; CVB Q8 |
| 3 | Thế nào là "đã đọc" | Mở chi tiết, hoặc bấm *Đánh dấu đã đọc* trên danh sách | Mở chi tiết; văn bản có file chính thì phải mở xem file mới tính (chờ TBD-02, TBD-03) | VBĐ NV-06 |
| 4 | Đơn vị nhận với vai trò Nhận để biết | Vào thẳng *Chờ xử lý* của đơn vị (3), không qua tiếp nhận [Hiện trạng] | Vào *Chờ tiếp nhận* của văn thư đơn vị (chờ TBD-01) | CVB BR-13; VBĐ NV-11 |
| 5 | Người nhận tự đổi thành Nhận để biết | Chưa có trên web; API máy chủ có sẵn lại đổi sang Phối hợp, không ai gọi | Nút *Nhận để biết* ở chi tiết văn bản → hoàn thành + đổi thành Nhận để biết + sang hộp Nhận để biết [ý đồ đã xác nhận VBĐ Q4] | VBĐ NV-11; `dac-thu.md` L13 |
| 6 | Chủ trì hoàn thành | Mọi Chủ trì cùng cấp xong → người giao tự hoàn thành, Phối hợp / Nhận để biết cùng cấp hoàn thành theo [Đã xác nhận Q2] | Giữ nguyên; bấm *Nhận để biết* của Chủ trì được tính như Chủ trì hoàn thành | VBĐ BR-28, BR-29, BR-42 |

**Tóm tắt thay đổi:** đổi trạng thái luồng nguồn của người chuyển khi chuyển chỉ Nhận để biết (3/7 → 4), thêm tự hoàn
thành (4 → 5) theo việc đọc, thêm nút *Nhận để biết* cho người nhận (3 → 5 + vai trò Nhận để biết), đổi nơi vào của đơn vị
Nhận để biết (chờ TBD-01). Không thêm menu, không thêm hộp việc.

## 1.4. Phạm vi chức năng bị ảnh hưởng

| STT | Điểm vào chức năng | Màn hình/Action | Trong phạm vi |
|---|---|---|---|
| 1 | Mọi hộp văn bản đến có nút *Chuyển* | Popup *Chuyển văn bản* (một văn bản) | Có |
| 2 | Hộp *Văn bản chờ xử lý*, tab *Tất cả* | Màn chi tiết văn bản — nút *Nhận để biết* | Có |
| 3 | Mọi hộp văn bản đến, Tra cứu, Theo dõi đơn vị | Mở chi tiết / mở file — ghi "đã đọc" | Có (điểm kích hoạt tự hoàn thành) |
| 4 | Hộp *Văn bản chờ tiếp nhận* của văn thư | Đơn vị nhận Nhận để biết | Có (chờ TBD-01) |
| 5 | Chuyển nhiều văn bản (tối đa 50) | Popup chuyển nhiều | Có — áp dụng như chuyển một văn bản *(đề xuất AI)* |
| 6 | Trang chủ — nhóm ô "Văn bản đến"; màn *Theo dõi văn bản đến đơn vị* | Số đếm | Có — số đổi theo trạng thái mới, không đổi cách đếm |
| 7 | Hoàn thành, Trả lại, Cho ý kiến, Thu hồi, Tiếp nhận | Không được mô tả trong YC111 ngoài các điểm ở mục 4 | Ngoài phạm vi thay đổi; cần regression |
| 8 | Văn bản đi (chuyển văn bản đã cấp số) | Không đổi | Ngoài phạm vi |

**Kênh áp dụng:** Web và Mobile. Mọi quy tắc đặt ở phía máy chủ để ứng dụng di động hưởng cùng hành vi (BR-21). Giao
diện nút *Nhận để biết* trên ứng dụng di động do đội mobile làm (mã nguồn mobile không có trong repo — TBD-07).

## 1.5. Thuật ngữ

| Thuật ngữ | Định nghĩa sử dụng trong tài liệu |
|---|---|
| Luồng nguồn | Dòng nhận văn bản (cá nhân hoặc đơn vị) mà người chuyển đang giữ và dùng để chuyển đi |
| Lần chuyển chỉ Nhận để biết | Một lần bấm *Chuyển* mà **mọi** cá nhân / đơn vị được chọn đều có vai trò Nhận để biết, không có nhóm |
| Tập Nhận để biết của người chuyển | Mọi cá nhân / đơn vị Nhận để biết **còn hiệu lực** (chưa bị thu hồi) mà người chuyển đã chuyển văn bản này từ cùng luồng nguồn, qua mọi lần chuyển (Q04 YC111) |
| Đã đọc | Hệ thống đã ghi thời điểm đọc cho dòng nhận đó theo BR-06 / BR-07 |
| Tự hoàn thành | Hệ thống tự đổi luồng nguồn của người chuyển sang *Đã hoàn thành* (5), không cần người chuyển bấm |
| File chính | File văn bản (loại file chính), không gồm phụ lục / file đính kèm / file chuyển kèm (chờ TBD-02) |

---

# 2. PHẠM VI VÀ VAI TRÒ `[A4]` · 🟨

## 2.1. Vai trò

| Vai trò nghiệp vụ | Mã vai trò hệ thống | Được làm gì trong YC111 | Ghi chú |
|---|---|---|---|
| Người giữ văn bản cá nhân (chuyên viên, lãnh đạo, trợ lý) | `NV` · `LDDV` · `TTDV` · `TL` | Ý 1: chuyển chỉ Nhận để biết từ văn bản cá nhân; ý 2: bấm *Nhận để biết* khi là Chủ trì / Phối hợp | Vai trò chính. Quyền theo nút hiện (không theo mã vai trò) |
| Văn thư đơn vị | `VT` | Ý 1: chuyển chỉ Nhận để biết từ **văn bản đơn vị**; nhận văn bản đơn vị Nhận để biết ở *Chờ tiếp nhận* (chờ TBD-01); ý 2: chỉ trên văn bản cá nhân của mình | Văn bản đơn vị không có nút *Nhận để biết* (BR-15) |
| Người Nhận để biết | mọi vai trò | Đọc văn bản — việc đọc được tính để tự hoàn thành | Không có thao tác mới |
| Người giao (cấp trên của người bấm *Nhận để biết*) | mọi vai trò | Nhận thông báo (BR-20, giả định); văn bản có thể tự hoàn thành theo BR-18 | |
| Hệ thống | — | Tự hoàn thành luồng nguồn khi tập Nhận để biết đã đọc hết | |

**Lưu ý phạm vi role:** không thêm menu, không đổi phân quyền menu. Nút *Nhận để biết* hiện theo điều kiện ở BR-15, BR-16
cho mọi vai trò thỏa điều kiện.

## 2.2. Tiền điều kiện chung

- Người dùng đã đăng nhập, có quyền vào hộp văn bản đến tương ứng theo phân quyền hiện hành.
- Văn bản đến đã có trong hệ thống (đã tiếp nhận / đã chuyển tới người dùng).
- Không cần cấu hình mới.

---

# 3. TỔNG QUAN YÊU CẦU CHỨC NĂNG `[A5]` · 🟦 danh sách FR · 🟩 3.1 mapping · 🟨 3.2–3.3

| ID | Trigger/Action của người dùng | Xử lý mong muốn | BR liên quan |
|---|---|---|---|
| FR-01 | Người giữ văn bản chuyển văn bản mà mọi đối tượng nhận là Nhận để biết | Luồng nguồn của người chuyển sang *Đã xử lý*; người / đơn vị nhận vào đúng hộp | BR-01, BR-02, BR-03, BR-04, BR-05 |
| FR-02 | Người Nhận để biết đọc văn bản | Ghi thời điểm đọc theo định nghĩa mới | BR-06, BR-07 |
| FR-03 | Người cuối cùng trong tập Nhận để biết đọc xong | Luồng nguồn của người chuyển tự *Đã hoàn thành* | BR-08, BR-09, BR-10, BR-12, BR-13 |
| FR-04 | Người chuyển bấm *Hoàn thành* khi văn bản đang *Đã xử lý* | Hoàn thành như hiện tại | BR-11 |
| FR-05 | Người nhận (Chủ trì / Phối hợp) bấm *Nhận để biết* ở chi tiết văn bản | Xác nhận → hoàn thành, đổi vai trò thành Nhận để biết, văn bản sang hộp Nhận để biết; lan lên người giao như Chủ trì hoàn thành | BR-15, BR-16, BR-17, BR-18, BR-19, BR-20 |
| FR-06 | Dùng trên ứng dụng di động | Cùng hành vi FR-01 → FR-05 | BR-14, BR-21 |
| FR-07 | Xem số đếm, thống kê | Số đổi theo trạng thái mới | BR-22 |
| FR-08 | Văn bản mật, liên thông, văn bản cũ | Phạm vi áp dụng | BR-23 |

## 3.1. Mapping dữ liệu nguồn → đích

Không áp dụng — yêu cầu không sao chép dữ liệu giữa đối tượng; chỉ đổi trạng thái / vai trò của dòng nhận (mục 3.2).

## 3.2. Trạng thái và chuyển trạng thái

Mã trạng thái dòng nhận (`DOCUMENT_IN_STAFF.STATUS` / `DOCUMENT_IN_GROUP.STATUS`): trống Chờ tiếp nhận · 3 Chờ xử lý ·
4 Đã xử lý · 5 Đã hoàn thành · 7 Bị trả lại · 0 Đã thu hồi. Vai trò (`SEND_TYPE`): 1 Chủ trì · 2 Phối hợp · 3 Nhận để biết
(VBĐ mục 5).

| Trạng thái hiện tại (tên · mã) | Hành động | Ai thực hiện | Điều kiện | Trạng thái kế tiếp (tên · mã) | BR |
|---|---|---|---|---|---|
| Chờ xử lý · 3 / Bị trả lại · 7 (luồng nguồn) | Chuyển chỉ Nhận để biết | Người giữ văn bản | BR-01, BR-02 | Đã xử lý · 4 | BR-03 |
| — (dòng mới, cá nhân nhận) | Được chuyển Nhận để biết | Hệ thống | — | Chờ xử lý · 3, vai trò 3, hiện ở hộp *Văn bản nhận để biết* | BR-04 |
| — (dòng mới, đơn vị nhận) | Được chuyển Nhận để biết | Hệ thống | — | Chờ tiếp nhận · trống, vai trò 3 (chờ TBD-01) | BR-05 |
| Đã xử lý · 4 (luồng nguồn) | Người cuối cùng trong tập Nhận để biết đọc | Hệ thống | BR-08, BR-10, BR-12 | Đã hoàn thành · 5 | BR-09 |
| Đã xử lý · 4 (luồng nguồn) | Bấm *Hoàn thành* | Người chuyển | Như hiện tại | Đã hoàn thành · 5 | BR-11 |
| Chờ xử lý · 3, vai trò 1 / 2 (luồng cá nhân) | Bấm *Nhận để biết* + xác nhận | Người nhận | BR-15, BR-16 | Đã hoàn thành · 5, vai trò 3 | BR-17 |
| Đã xử lý · 4 (luồng người giao) | Chủ trì cuối cùng cùng cấp bấm *Nhận để biết* | Hệ thống | Như Chủ trì hoàn thành | Đã hoàn thành · 5 | BR-18 |

**Hành động bị cấm:**
- Không hiện nút *Nhận để biết* cho luồng đơn vị, luồng ở trạng thái 4 / 5 / 6 / 7 / 0, luồng đã là Nhận để biết (BR-15).
- Không mở lại (5 → 4) khi người Nhận để biết bấm *Đánh dấu chưa đọc* sau khi đã tự hoàn thành (BR-09, giả định).
- Không hoàn tác *Nhận để biết* (BR-19, giả định).

## 3.3. Yêu cầu phi chức năng (NFR)

| Mã | Nhóm | Yêu cầu (đo được) |
|---|---|---|
| NFR-01 | Nhất quán dữ liệu | Bấm *Nhận để biết*: hoàn thành + đổi vai trò + đưa vào hộp Nhận để biết là **một giao dịch** — lỗi giữa chừng thì không đổi gì (không để văn bản đã hoàn thành mà không vào hộp Nhận để biết) |
| NFR-02 | Đa kênh | Tự hoàn thành (BR-09) chạy ở máy chủ, kích hoạt bởi **mọi** đường ghi "đã đọc" (web, di động, tải file) — không phụ thuộc màn hình |
| NFR-03 | Thao tác lặp | Bấm *Nhận để biết* hai lần liên tiếp / hai thiết bị cùng lúc → chỉ xử lý một lần, lần sau báo MSG-04 |
| NFR-04 | Nhật ký | Sơ đồ luân chuyển hiện vai trò mới "Nhận để biết" và thời điểm đổi của người bấm; tự hoàn thành ghi nội dung hoàn thành MSG-05 |
| NFR-05 | Thông báo | Theo BR-20 (giả định — chờ TBD-05) |
| NFR-06 | Hiệu năng | Ghi "đã đọc" kèm kiểm tự hoàn thành không làm việc mở văn bản chậm thêm quá 1 giây *(đề xuất AI)* |
| NFR-07 | Bảo mật / Văn bản mật | Theo quy tắc chuyển văn bản mật hiện hành (CVB BR-44, BR-46); YC111 không mở rộng quyền xem |

---

# 4. BUSINESS RULES `[A6]` · 🟨

**Ý 1 — chuyển chỉ Nhận để biết**

| Rule ID | Tên rule | Mô tả | Nguồn |
|---|---|---|---|
| BR-01 | Điều kiện "chuyển chỉ Nhận để biết" | Áp dụng khi một lần chuyển văn bản đến có **1..200** đối tượng nhận và **mọi** đối tượng là **cá nhân hoặc đơn vị** có vai trò Nhận để biết (3). Lần chuyển có **nhóm** (nhóm cá nhân, nhóm đơn vị) hoặc có ít nhất một Chủ trì / Phối hợp → **không** áp dụng YC111, giữ quy tắc hiện tại. Người nhận vai trò *Nắm tình hình*: chờ TBD-04 | Q01, Q05 YC111; CVB BR-14 |
| BR-02 | Người chuyển | Áp dụng cho luồng nguồn là **văn bản cá nhân** (người giữ văn bản) và **văn bản đơn vị** (văn thư chuyển từ luồng đơn vị) | Q01 YC111 |
| BR-03 | Luồng nguồn sang Đã xử lý | Chuyển thành công theo BR-01 → luồng nguồn của người chuyển đang 3 hoặc 7 đổi thành **4 Đã xử lý**; văn bản rời hộp *Văn bản chờ xử lý*, hiện ở hộp *Văn bản đã xử lý* lọc *Đã chuyển xử lý*. **Thay quy tắc đã chốt** CVB BR-14 / VBĐ BR-41 | Q02 YC111 |
| BR-04 | Cá nhân nhận Nhận để biết | Dòng nhận của cá nhân: trạng thái 3, vai trò 3, hiện ở hộp *Văn bản nhận để biết* (như hiện tại) (chờ TBD-01a) | Q05 YC111; VBĐ NV-11, Q3 |
| BR-05 | Đơn vị nhận Nhận để biết | Dòng nhận của đơn vị: trạng thái **trống (Chờ tiếp nhận)**, vai trò 3, hiện ở hộp *Văn bản chờ tiếp nhận* của văn thư đơn vị đó — đổi so với hiện tại (vào thẳng 3). Sau khi văn thư tiếp nhận: chờ TBD-01b | Q05 YC111; CVB BR-13 |
| BR-06 | "Đã đọc" của cá nhân | Hệ thống ghi thời điểm đọc (`CONFIRM_TIME`) cho dòng nhận của người đó khi: (a) văn bản **không có file chính** → người đó mở màn chi tiết văn bản; (b) văn bản **có file chính** → người đó mở xem file chính (trình xem file trong màn chi tiết / danh sách) (chờ TBD-02). Nút *Đánh dấu đã đọc* trên danh sách: chờ TBD-03 | Q03 YC111 |
| BR-07 | "Đã đọc" của đơn vị | Dòng nhận của đơn vị được tính đã đọc khi văn thư của đơn vị đó đọc theo đúng cách ở BR-06 (chờ TBD-01b về thời điểm: trước hay sau tiếp nhận) | Q03, Q05 YC111 |
| BR-08 | Tập cần đọc | Xét trên **tập Nhận để biết của người chuyển** (mục 1.5): mọi cá nhân / đơn vị Nhận để biết **chưa bị thu hồi** (trạng thái ≠ 0) mà người chuyển đã chuyển văn bản này từ cùng luồng nguồn, qua **mọi** lần chuyển | Q04 YC111 |
| BR-09 | Tự hoàn thành | Ngay khi mọi đối tượng trong tập BR-08 đã đọc và luồng nguồn đang **4**, hệ thống đổi luồng nguồn thành **5 Đã hoàn thành**, nội dung hoàn thành MSG-05. Văn bản rời lọc *Đã chuyển xử lý*, sang lọc *Đã hoàn thành*. Đã tự hoàn thành thì người Nhận để biết bấm *Đánh dấu chưa đọc* **không** mở lại luồng nguồn (giả định — chờ TBD-05) | Q02 YC111; ghi chú anh Long |
| BR-10 | Không tự hoàn thành khi có người xử lý | Nếu người chuyển đã chuyển văn bản này (cùng luồng nguồn) cho ít nhất một Chủ trì / Phối hợp / nhóm **còn hiệu lực** ở bất kỳ lần nào → không áp dụng BR-09; văn bản chờ theo quy tắc hiện tại (chờ Chủ trì hoàn thành) | Q04 YC111 |
| BR-11 | Người chuyển chủ động kết thúc | Văn bản ở 4 theo BR-03 vẫn có nút *Hoàn thành* như hiện tại; bấm thì hoàn thành theo quy tắc hoàn thành hiện hành (kể cả kiểm nhắc việc, yêu cầu trả lời — VBĐ BR-31, BR-32); dòng Nhận để biết phía dưới chưa xong thì hoàn thành theo như hiện tại | Ghi chú anh Long; CVB Q8 |
| BR-12 | Tự hoàn thành gặp điều kiện chặn | *(đề xuất AI)* Nếu luồng nguồn có điều kiện làm *Hoàn thành* bị chặn (nhắc việc chờ duyệt / phải trả lời nhắc việc — VBĐ BR-31; luồng nguồn có yêu cầu trả lời mà chưa đính kèm văn bản trả lời — VBĐ BR-32) → **không** tự hoàn thành, giữ 4, không báo lỗi; người chuyển tự hoàn thành theo BR-11 | Đề xuất AI — BA xác nhận |
| BR-13 | Thu hồi | *(đề xuất AI)* Người chuyển thu hồi một / nhiều đối tượng Nhận để biết → đối tượng đó ra khỏi tập BR-08; nếu sau thu hồi tập còn **≥ 1** đối tượng và tất cả đã đọc → tự hoàn thành ngay; nếu tập còn **0** đối tượng → giữ 4, không tự hoàn thành | Đề xuất AI — BA xác nhận |
| BR-14 | Kích hoạt ở máy chủ | BR-03, BR-09 chạy ở máy chủ, kích hoạt bởi mọi đường ghi "đã đọc" hợp lệ theo BR-06 (web, di động, tải file chính), không phụ thuộc màn hình mở văn bản | Q10 YC111; VBĐ mục 10 |

**Ý 2 — người nhận tự chuyển thành Nhận để biết**

| Rule ID | Tên rule | Mô tả | Nguồn |
|---|---|---|---|
| BR-15 | Điều kiện hiện nút | Nút *Nhận để biết* hiện ở màn chi tiết văn bản khi **đủ cả**: (a) mở từ hộp *Văn bản chờ xử lý* hoặc tab *Tất cả* (văn bản cá nhân); (b) dòng nhận là **văn bản cá nhân** của người xem; (c) vai trò Chủ trì (1 hoặc trống) hoặc Phối hợp (2); (d) trạng thái **3 Chờ xử lý**. Không hiện ở mọi trường hợp khác (văn bản đơn vị, trạng thái 4 / 5 / 6 / 7, vai trò 3, mở từ Tra cứu / Theo dõi đơn vị / Nhận để biết / Đã xử lý) | Q06 YC111; VBĐ Q4 |
| BR-16 | Ẩn nút khi có ràng buộc | Ẩn nút khi văn bản có nhắc việc làm *Hoàn thành* bị chặn hoặc phải trả lời nhắc việc (VBĐ BR-31), hoặc dòng nhận của người xem có **yêu cầu trả lời** (VBĐ BR-32) | Q08 YC111 |
| BR-17 | Bấm Nhận để biết | Bấm nút → hộp xác nhận MSG-01, **không nhập nội dung**. *Đồng ý* → trong một lần xử lý: (a) dòng nhận của người dùng đổi thành **5 Đã hoàn thành**, nội dung hoàn thành "Nhận để biết"; (b) vai trò nhận của người dùng thành **3 Nhận để biết**; (c) văn bản hiện ở hộp *Văn bản nhận để biết* của người dùng (trạng thái đã đọc), không còn ở *Văn bản chờ xử lý*; báo MSG-02, đóng màn chi tiết, tải lại danh sách. *Hủy* → không đổi gì | Q06, Q09 YC111; VBĐ Q4 |
| BR-18 | Lan lên người giao | Bấm *Nhận để biết* được tính **như hoàn thành** của chính vai trò cũ: vai trò cũ là Chủ trì → áp quy tắc Chủ trì hoàn thành hiện hành (mọi Chủ trì cùng cấp xong thì luồng người giao tự *Đã hoàn thành*, Phối hợp / Nhận để biết cùng cấp hoàn thành theo); vai trò cũ là Phối hợp → không lan lên | Q07 YC111; VBĐ BR-28, BR-29, BR-42 |
| BR-19 | Không hoàn tác | Đã bấm *Nhận để biết* thì không có thao tác đổi lại vai trò cũ (giả định — chờ TBD-05) | Đề xuất Q09 YC111 |
| BR-20 | Thông báo người giao | Bấm *Nhận để biết* thành công → gửi thông báo (chuông) cho người đã chuyển văn bản cho người dùng, nội dung MSG-06. Tự hoàn thành ở ý 1 không gửi thông báo (giả định — chờ TBD-05) | Đề xuất Q09 YC111 |
| BR-21 | Đa kênh | Ý 2 có một chức năng phía máy chủ dùng chung cho web và di động, tự kiểm lại BR-15, BR-16 trước khi xử lý (không tin điều kiện hiện nút phía giao diện) | Q10 YC111 |

**Chung**

| Rule ID | Tên rule | Mô tả | Nguồn |
|---|---|---|---|
| BR-22 | Số đếm, thống kê | Không đổi cách đếm: ô trang chủ *Chờ xử lý* / *Đã xử lý* / *Đã hoàn thành* / *Nhận để biết* và thống kê *Theo dõi văn bản đến đơn vị* đếm theo trạng thái mới. Luồng ở 4 vẫn tính **chưa hoàn thành** trong thống kê tiến độ (VBĐ BR-45) và vẫn có thể quá hạn | VBĐ BR-45, Q6, Q7 |
| BR-23 | Phạm vi văn bản | Áp dụng cho văn bản đến thường, văn bản liên thông, văn bản mật (theo quy tắc chuyển văn bản mật hiện hành). **Không** xử lý ngược văn bản cũ đang nằm *Chờ xử lý* do đã chuyển chỉ Nhận để biết trước khi triển khai (giả định — chờ TBD-06) | Đề xuất Q10 YC111 |

---

# 5. LUỒNG NGHIỆP VỤ / USE CASE `[A7]` · 🟨

## 5.1. UC-01 - Chuyển văn bản chỉ để biết

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Chuyển văn bản cho người / đơn vị chỉ để biết mà văn bản của mình rời *Chờ xử lý* |
| Actor | Người giữ văn bản cá nhân (`NV`, `LDDV`, `TTDV`, `TL`); văn thư đơn vị (`VT`) với văn bản đơn vị |
| Tiền điều kiện | Luồng nguồn của actor đang 3 hoặc 7; actor thấy nút *Chuyển* |
| Trigger | Actor bấm *Chuyển*, chọn đối tượng nhận, bấm *Chuyển* trên popup |
| Hậu điều kiện | Luồng nguồn = 4; cá nhân nhận có dòng vai trò 3 ở hộp Nhận để biết; đơn vị nhận có dòng vai trò 3 ở Chờ tiếp nhận (chờ TBD-01) |
| Rule liên quan | BR-01, BR-02, BR-03, BR-04, BR-05, BR-14, BR-23 |
| Ngoại lệ liên quan | EC-01, EC-02, EC-03, EC-10 |

**Luồng chính**

1. Actor mở *Chuyển văn bản*, chọn luồng nguồn (nếu có nhiều luồng).
2. Actor chọn cá nhân / đơn vị, đặt **tất cả** vai trò *Nhận để biết*, nhập ý kiến (không bắt buộc), bấm *Chuyển*.
3. Hệ thống chuyển như hiện tại (kiểm ngưỡng số người, người đã nhận…).
4. Hệ thống kiểm BR-01: đúng → đổi luồng nguồn thành 4.
5. Hệ thống báo chuyển thành công (thông báo hiện hành), tải lại danh sách: văn bản không còn ở *Văn bản chờ xử lý*.

**Luồng thay thế**

- 2a. Có ít nhất một Chủ trì / Phối hợp → luồng nguồn = 4 theo quy tắc hiện tại; không có tự hoàn thành (BR-10).
- 2b. Có nhóm → giữ quy tắc hiện tại (EC-02).

**Luồng ngoại lệ**

- 3a. Chuyển không thành công cho mọi đối tượng → luồng nguồn giữ nguyên (EC-03).

## 5.2. UC-02 - Tự hoàn thành khi mọi người Nhận để biết đã đọc

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Văn bản của người chuyển tự kết thúc khi mọi người Nhận để biết đã đọc |
| Actor | Hệ thống (kích hoạt bởi người Nhận để biết đọc văn bản) |
| Tiền điều kiện | Luồng nguồn = 4 sau UC-01; không có Chủ trì / Phối hợp / nhóm còn hiệu lực (BR-10) |
| Trigger | Một người / đơn vị trong tập BR-08 được ghi "đã đọc" (BR-06, BR-07); hoặc người chuyển thu hồi (BR-13) |
| Hậu điều kiện | Luồng nguồn = 5, nội dung MSG-05 |
| Rule liên quan | BR-06, BR-07, BR-08, BR-09, BR-10, BR-12, BR-13, BR-14 |
| Ngoại lệ liên quan | EC-04, EC-05, EC-06, EC-07, EC-08 |

**Luồng chính**

1. Người Nhận để biết mở văn bản (không có file chính) hoặc mở xem file chính (có file chính).
2. Hệ thống ghi thời điểm đọc cho dòng nhận của người đó.
3. Hệ thống tìm luồng nguồn của người đã chuyển cho họ; kiểm BR-08, BR-10, BR-12.
4. Nếu mọi đối tượng trong tập đã đọc → đổi luồng nguồn thành 5.

**Luồng thay thế**

- 3a. Còn đối tượng chưa đọc → không làm gì.
- 3b. Gặp điều kiện chặn BR-12 → không làm gì, giữ 4.

**Luồng ngoại lệ**

- 4a. Lỗi khi tự hoàn thành → việc ghi "đã đọc" vẫn thành công, người đọc không thấy lỗi; ghi log (EC-08).

```mermaid
sequenceDiagram
  actor NC as Người chuyển
  actor NB as Người Nhận để biết (A, B)
  participant HT as Hệ thống
  NC->>HT: Chuyển văn bản cho A, B — vai trò Nhận để biết
  HT-->>NC: Văn bản của NC sang Đã xử lý (4)
  NB->>HT: A mở văn bản / mở file chính
  HT-->>HT: Ghi đã đọc A; B chưa đọc → giữ 4
  NB->>HT: B mở văn bản / mở file chính
  HT-->>HT: Ghi đã đọc B; tất cả đã đọc → văn bản NC = Đã hoàn thành (5)
```

## 5.3. UC-03 - Người chuyển chủ động hoàn thành

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Kết thúc văn bản trước khi mọi người đọc |
| Actor | Người chuyển (actor UC-01) |
| Tiền điều kiện | Luồng nguồn = 4 |
| Trigger | Mở văn bản từ hộp *Văn bản đã xử lý*, bấm *Hoàn thành* |
| Hậu điều kiện | Luồng nguồn = 5 |
| Rule liên quan | BR-11 |
| Ngoại lệ liên quan | EC-09 |

**Luồng chính:** như chức năng Hoàn thành hiện hành (VBĐ NV-08). **Luồng thay thế:** không có. **Luồng ngoại lệ:**
bị chặn bởi nhắc việc / yêu cầu trả lời → thông báo hiện hành (EC-09).

## 5.4. UC-04 - Người nhận tự chuyển thành Nhận để biết

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Người được giao xử lý tự đánh dấu văn bản chỉ để biết |
| Actor | Người nhận văn bản cá nhân vai trò Chủ trì / Phối hợp (`NV`, `LDDV`, `TTDV`, `TL`, `VT` trên văn bản cá nhân) |
| Tiền điều kiện | BR-15, BR-16 thỏa |
| Trigger | Mở chi tiết văn bản từ *Văn bản chờ xử lý* / tab *Tất cả*, bấm *Nhận để biết* |
| Hậu điều kiện | Dòng nhận = 5, vai trò 3, văn bản ở hộp *Văn bản nhận để biết*; người giao có thể tự hoàn thành (BR-18) |
| Rule liên quan | BR-15, BR-16, BR-17, BR-18, BR-19, BR-20, BR-21 |
| Ngoại lệ liên quan | EC-11, EC-12, EC-13, EC-14 |

**Luồng chính**

1. Actor bấm *Nhận để biết*.
2. Hệ thống hiện MSG-01.
3. Actor bấm *Đồng ý*.
4. Hệ thống kiểm lại BR-15, BR-16; hoàn thành dòng nhận, đổi vai trò thành 3; áp BR-18; gửi thông báo BR-20.
5. Hệ thống báo MSG-02, đóng chi tiết, tải lại danh sách.

**Luồng thay thế**

- 3a. Actor bấm *Hủy* → đóng hộp xác nhận, không đổi gì.

**Luồng ngoại lệ**

- 4a. Trạng thái đã đổi (người khác thu hồi, đã bấm ở thiết bị khác) → MSG-04, tải lại (EC-12, EC-13).
- 4b. Lỗi hệ thống → MSG-03, không đổi gì (EC-14).

```mermaid
sequenceDiagram
  actor NN as Người nhận (Chủ trì)
  participant HT as Hệ thống
  actor NG as Người giao
  NN->>HT: Bấm Nhận để biết
  HT-->>NN: MSG-01 xác nhận
  NN->>HT: Đồng ý
  HT-->>HT: Dòng của NN = 5, vai trò 3; Chủ trì cuối cùng → luồng NG = 5
  HT-->>NG: Thông báo MSG-06
  HT-->>NN: MSG-02, văn bản sang hộp Nhận để biết
```

---

# 6. ĐẶC TẢ MÀN HÌNH VÀ TRƯỜNG DỮ LIỆU `[A8]` · 🟨

## 6.1. Màn hình chi tiết văn bản đến (thanh nút)

Ảnh: chưa có — {{BA đặt ảnh chụp thanh nút màn chi tiết vào `input/design/01_chi_tiet_nut_nhan_de_biet.png` nếu cần}}.

| ID | Trường/Control | Loại | Bắt buộc | Độ dài / Giới hạn | Mặc định | Quy tắc hiển thị / Validate | Thay đổi trong YC111 |
|---|---|---|---|---|---|---|---|
| UI-01 | Nút *Nhận để biết* | Nút (icon dấu tích), nhãn "Nhận để biết" | — | — | Ẩn | Hiện theo BR-15, BR-16; bị khóa trong lúc đang xử lý (NFR-03) | Mới |
| UI-02 | Hộp xác nhận | Popup xác nhận | — | — | — | Nội dung MSG-01; nút *Đồng ý* / *Hủy*; không có ô nhập | Mới |
| UI-03 | Nút *Hoàn thành*, *Chuyển*, *Trả lại*, *Cho ý kiến* | Nút | — | — | — | Giữ nguyên baseline (VBĐ NV-05) | Giữ nguyên |

## 6.2. Popup Chuyển văn bản (văn bản đến)

| ID | Trường/Control | Loại | Bắt buộc | Độ dài / Giới hạn | Mặc định | Quy tắc hiển thị / Validate | Thay đổi trong YC111 |
|---|---|---|---|---|---|---|---|
| UI-04 | Vai trò từng đối tượng nhận | Combobox | Có | Chủ trì / Phối hợp / Nhận để biết / Nắm tình hình | Giữ nguyên baseline | Giữ nguyên baseline; quyết định BR-01 | Giữ nguyên |
| UI-05 | Ý kiến chuyển | Textarea | Không | ≤ 2000 ký tự | Trống | Giữ nguyên baseline | Giữ nguyên |
| UI-06 | Các trường khác (hạn xử lý, yêu cầu trả lời, file, SMS) | — | — | — | — | Giữ nguyên baseline | Giữ nguyên |

## 6.3. Thông báo người dùng

| Mã | Tình huống | Loại | Nội dung nguyên văn | Nút |
|---|---|---|---|---|
| MSG-01 | Bấm *Nhận để biết* | Popup xác nhận | "Văn bản sẽ được hoàn thành và chuyển sang mục Văn bản nhận để biết. Bạn có chắc chắn?" *(đề xuất AI)* | Đồng ý / Hủy |
| MSG-02 | Nhận để biết thành công | Toast | "Đã nhận văn bản để biết thành công" *(đề xuất AI — code có sẵn đang có hai câu khác nhau giữa hai file ngôn ngữ, xem mục 10.9)* | — |
| MSG-03 | Lỗi hệ thống khi Nhận để biết | Toast cảnh báo | "Nhận để biết văn bản không thành công. Vui lòng thử lại" *(đề xuất AI)* | — |
| MSG-04 | Trạng thái văn bản đã thay đổi | Toast cảnh báo | "Văn bản đã thay đổi trạng thái, vui lòng tải lại danh sách" *(đề xuất AI)* | — |
| MSG-05 | Nội dung hoàn thành khi tự hoàn thành | Nội dung lưu ở lịch sử xử lý | "Tự động hoàn thành: người nhận để biết đã đọc văn bản" *(đề xuất AI)* | — |
| MSG-06 | Thông báo cho người giao | Thông báo (chuông) | "<Họ tên> đã chuyển văn bản <Số ký hiệu> thành Nhận để biết" *(đề xuất AI — chờ TBD-05)* | — |

## 6.4. Điều hướng

| Từ (màn hình · vùng) | Thao tác | Đến (màn hình) | Tab/bộ lọc mặc định | Giữ bộ lọc cũ? |
|---|---|---|---|---|
| Chi tiết văn bản (mở từ *Văn bản chờ xử lý* / *Tất cả*) | *Nhận để biết* → *Đồng ý* thành công | Đóng chi tiết, về danh sách đang mở (đã tải lại) | Không đổi | Có |
| Popup *Chuyển văn bản* | Chuyển chỉ Nhận để biết thành công | Về danh sách đang mở (đã tải lại) | Không đổi | Có |

## 6.5. Quy tắc hiển thị

- UI-01 hiện / ẩn theo BR-15, BR-16; không hiện trên màn chi tiết mở từ hộp *Văn bản nhận để biết*, *Đã xử lý*, *Tra
  cứu*, *Theo dõi văn bản đến đơn vị*.
- Sau BR-17, văn bản trong hộp *Văn bản nhận để biết* hiển thị như văn bản đã đọc (hộp mặc định lọc chưa đọc — VBĐ BR-08 —
  nên người dùng chỉ thấy khi bỏ lọc) *(đề xuất AI)*.

---

# 7. XỬ LÝ NGOẠI LỆ VÀ TRƯỜNG HỢP BIÊN `[A9]` · 🟨

| ID | Tình huống | Kết quả mong đợi | UC | Trạng thái |
|---|---|---|---|---|
| EC-01 | Chuyển cho 2 Nhận để biết + 1 Phối hợp | Luồng nguồn = 4 theo quy tắc hiện tại; không tự hoàn thành | UC-01 | Đã chốt (BR-10) |
| EC-02 | Chuyển cho 1 Nhận để biết + 1 nhóm cá nhân | Giữ quy tắc hiện tại (luồng nguồn = 4 vì có nhóm); không tự hoàn thành | UC-01 | Đã chốt (Q05 YC111) |
| EC-03 | Chuyển chỉ Nhận để biết nhưng mọi đối tượng chuyển không thành công (người đã nhận, bị bỏ qua…) | Luồng nguồn giữ nguyên 3 / 7 | UC-01 | Chờ xác nhận *(đề xuất AI)* |
| EC-04 | Lần 1 chuyển Nhận để biết cho A, B; lần 2 chuyển Nhận để biết cho C; A, B đã đọc, C chưa | Giữ 4; C đọc → 5 | UC-02 | Đã chốt (Q04 YC111) |
| EC-05 | A, B Nhận để biết; người chuyển thu hồi B; A đã đọc | Tự hoàn thành ngay khi thu hồi | UC-02 | Chờ xác nhận (BR-13 đề xuất AI) |
| EC-06 | Đã tự hoàn thành; A bấm *Đánh dấu chưa đọc* | Luồng nguồn giữ 5 | UC-02 | TBD-05 (giả định) |
| EC-07 | Người Nhận để biết chỉ tải file chính về máy (không mở trình xem) | Chờ TBD-02 | UC-02 | TBD-02 |
| EC-08 | Lỗi khi tự hoàn thành | Ghi "đã đọc" vẫn thành công; luồng nguồn giữ 4; ghi log; lần đọc kế tiếp của người khác (hoặc người chuyển bấm Hoàn thành) xử lý tiếp | UC-02 | Chờ xác nhận *(đề xuất AI)* |
| EC-09 | Người chuyển bấm *Hoàn thành* khi văn bản có nhắc việc chờ duyệt | Bị chặn bằng thông báo hiện hành (VBĐ BR-31) | UC-03 | Đã chốt (baseline) |
| EC-10 | Văn bản mật chuyển chỉ Nhận để biết | Áp dụng như văn bản thường, theo quy tắc chuyển văn bản mật hiện hành | UC-01 | TBD-06 (giả định) |
| EC-11 | Chủ trì **duy nhất** bấm *Nhận để biết* | Luồng người giao = 5; Phối hợp / Nhận để biết cùng cấp = 5 | UC-04 | Đã chốt (Q07 YC111) |
| EC-12 | Người nhận mở chi tiết; trong lúc đó người giao thu hồi; người nhận bấm *Nhận để biết* | MSG-04, không đổi gì | UC-04 | Chờ xác nhận *(đề xuất AI)* |
| EC-13 | Bấm *Nhận để biết* đồng thời trên web và di động | Chỉ một lần thành công; lần còn lại MSG-04 | UC-04 | Chờ xác nhận *(đề xuất AI)* |
| EC-14 | Lỗi giữa chừng khi *Nhận để biết* | Không đổi gì (NFR-01); MSG-03 | UC-04 | Chờ xác nhận *(đề xuất AI)* |
| EC-15 | Văn bản có yêu cầu trả lời / nhắc việc chặn | Không hiện nút *Nhận để biết* | UC-04 | Đã chốt (Q08 YC111) |
| EC-16 | Văn bản đơn vị Nhận để biết đang ở *Chờ tiếp nhận*, văn thư mở xem | Chờ TBD-01b | UC-02 | TBD-01 |

---

# 8. ACCEPTANCE CRITERIA `[A10]` · 🟨

> Dữ liệu mẫu: văn bản đến `TEST_VB111` (số 111/TB-TEST, có 1 file chính PDF) ở *Chờ xử lý* của Trưởng phòng P1 (`LDDV`);
> chuyên viên A, B, C thuộc phòng P1 (`NV`); văn thư Phòng P2 (`VT`).

| AC ID | BR | Given | When | Then |
|---|---|---|---|---|
| AC-01 | BR-01, BR-03 | `TEST_VB111` ở *Chờ xử lý* (3) của Trưởng phòng | Trưởng phòng chuyển cho A, B, vai trò Nhận để biết | Văn bản của Trưởng phòng = 4, hiện ở *Văn bản đã xử lý* lọc *Đã chuyển xử lý*, không còn ở *Văn bản chờ xử lý* |
| AC-02 | BR-01 | Như AC-01 | Trưởng phòng chuyển cho A (Nhận để biết) + nhóm cá nhân "TEST_Nhóm P1" | Luồng nguồn = 4 theo quy tắc hiện tại; khi A đọc, luồng nguồn **vẫn** = 4 |
| AC-03 | BR-01, BR-10 | Như AC-01 | Chuyển cho A (Nhận để biết) + B (Phối hợp) | Luồng nguồn = 4; A đọc → vẫn 4 |
| AC-04 | BR-02, BR-03 | Văn thư P1 giữ `TEST_VB111` ở *Chờ xử lý* văn bản đơn vị | Văn thư chuyển cho A, B, vai trò Nhận để biết | Luồng đơn vị của P1 = 4, hiện ở *Đã xử lý* tab *Văn bản đơn vị* |
| AC-05 | BR-03 | `TEST_VB111` ở *Bị trả lại* (7) của Trưởng phòng | Trưởng phòng chuyển chỉ Nhận để biết cho A | Luồng nguồn = 4 |
| AC-06 | BR-04 | AC-01 xong | A mở hộp *Văn bản nhận để biết* | Có `TEST_VB111`, trạng thái 3, vai trò Nhận để biết; không có ở *Văn bản chờ xử lý* của A |
| AC-07 | BR-05 | Trưởng phòng giữ `TEST_VB111` | Chuyển cho Phòng P2, vai trò Nhận để biết | Văn bản ở *Văn bản chờ tiếp nhận* của văn thư P2 (giả định — chờ TBD-01) |
| AC-08 | BR-06 | AC-01 xong; A chưa đọc | A mở chi tiết `TEST_VB111` (có file chính) nhưng không mở file | Dòng của A **chưa** có thời điểm đọc; luồng nguồn = 4 (giả định — chờ TBD-02) |
| AC-09 | BR-06 | Như AC-08 | A mở xem file chính rồi đóng trình xem | Dòng của A có thời điểm đọc |
| AC-10 | BR-06 | Văn bản `TEST_VB111B` không có file chính; chuyển chỉ Nhận để biết cho A | A mở chi tiết | Dòng của A có thời điểm đọc |
| AC-11 | BR-06 | AC-01 xong | A bấm *Đánh dấu đã đọc* trên danh sách, không mở văn bản | Chờ TBD-03 |
| AC-12 | BR-07 | AC-07 xong | Văn thư P2 mở xem file chính | Chờ TBD-01b |
| AC-13 | BR-08, BR-09 | AC-01 xong; A đã đọc | B mở xem file chính | Luồng nguồn = 5, nội dung MSG-05, hiện ở *Văn bản đã xử lý* lọc *Đã hoàn thành* |
| AC-14 | BR-08, BR-09 | AC-01 xong | Chỉ A mở xem file chính | Luồng nguồn vẫn = 4 |
| AC-15 | BR-08 | AC-01 xong; sau đó chuyển thêm Nhận để biết cho C; A, B đã đọc | — | Luồng nguồn = 4; C mở xem file chính → 5 |
| AC-16 | BR-10 | AC-01 xong; sau đó chuyển thêm cho C vai trò Chủ trì | A, B đều đọc | Luồng nguồn = 4 (chờ C hoàn thành theo quy tắc hiện tại) |
| AC-17 | BR-11 | AC-01 xong; chưa ai đọc | Trưởng phòng mở từ *Văn bản đã xử lý*, bấm *Hoàn thành*, lưu | Luồng nguồn = 5; dòng của A, B = 5 |
| AC-18 | BR-12 | AC-01 xong; văn bản có nhắc việc chờ duyệt | A, B đều đọc | Luồng nguồn vẫn = 4, không ai thấy lỗi (giả định — BR-12 đề xuất AI) |
| AC-19 | BR-13 | AC-01 xong; A đã đọc, B chưa | Trưởng phòng thu hồi B | Dòng B = 0; luồng nguồn = 5 (giả định — BR-13 đề xuất AI) |
| AC-20 | BR-09 | AC-13 xong | A bấm *Đánh dấu chưa đọc* | Luồng nguồn vẫn = 5 (giả định — chờ TBD-05) |
| AC-21 | BR-14 | AC-01 xong | A, B mở xem file chính trên **ứng dụng di động** | Luồng nguồn = 5 |
| AC-22 | BR-15 | A nhận `TEST_VB111` vai trò Chủ trì, trạng thái 3 | A mở chi tiết từ *Văn bản chờ xử lý* | Thấy nút *Nhận để biết* |
| AC-23 | BR-15 | A nhận vai trò Chủ trì | A mở chi tiết từ *Tra cứu văn bản* | Không thấy nút *Nhận để biết* |
| AC-24 | BR-15 | A đã chuyển tiếp văn bản (trạng thái 4) / văn bản Bị trả lại (7) / văn thư mở văn bản đơn vị | Mở chi tiết | Không thấy nút *Nhận để biết* |
| AC-25 | BR-16 | A nhận vai trò Chủ trì, người gửi bật *yêu cầu trả lời* | A mở chi tiết từ *Văn bản chờ xử lý* | Không thấy nút *Nhận để biết* |
| AC-26 | BR-17 | AC-22 | A bấm *Nhận để biết* | Hiện MSG-01 với nút *Đồng ý* / *Hủy*, không có ô nhập |
| AC-27 | BR-17 | AC-26 | A bấm *Hủy* | Không đổi gì; văn bản vẫn ở *Văn bản chờ xử lý* |
| AC-28 | BR-17 | AC-26 | A bấm *Đồng ý* | Dòng của A = 5, vai trò 3; MSG-02; văn bản có ở *Văn bản nhận để biết*, không còn ở *Văn bản chờ xử lý* |
| AC-29 | BR-18 | Trưởng phòng chuyển cho A (Chủ trì, duy nhất) và B (Phối hợp); luồng Trưởng phòng = 4 | A bấm *Nhận để biết* → *Đồng ý* | Luồng Trưởng phòng = 5; dòng của B = 5 |
| AC-30 | BR-18 | Như AC-29 nhưng có thêm C Chủ trì chưa hoàn thành | A bấm *Nhận để biết* → *Đồng ý* | Luồng Trưởng phòng vẫn = 4 |
| AC-31 | BR-18 | B (Phối hợp) ở trạng thái 3 | B bấm *Nhận để biết* → *Đồng ý* | Dòng của B = 5, vai trò 3; luồng người giao không đổi |
| AC-32 | BR-19 | AC-28 xong | A mở văn bản từ *Văn bản nhận để biết* | Không có thao tác đổi lại vai trò cũ (giả định — chờ TBD-05) |
| AC-33 | BR-20 | AC-28 xong | — | Trưởng phòng nhận thông báo MSG-06 (giả định — chờ TBD-05) |
| AC-34 | BR-21 | AC-22 | A bấm *Nhận để biết* trên ứng dụng di động | Kết quả như AC-28 (chờ TBD-07 về phiên bản app) |
| AC-35 | BR-22 | AC-01 trước và sau | Xem trang chủ của Trưởng phòng | Ô *Chờ xử lý* giảm 1, ô *Đã xử lý* tăng 1; *Theo dõi văn bản đến đơn vị* tính văn bản là chưa hoàn thành tới khi = 5 |
| AC-36 | BR-23 | Văn bản liên thông đã tiếp nhận ở *Chờ xử lý* của Trưởng phòng | Chuyển chỉ Nhận để biết cho A, B; A, B đọc | Như AC-01, AC-13 |
| AC-37 | BR-23 | Văn bản ở *Chờ xử lý* đã được chuyển chỉ Nhận để biết **trước** khi triển khai | Triển khai YC111 | Văn bản giữ nguyên *Chờ xử lý* (giả định — chờ TBD-06) |

---

# 9. MA TRẬN KIỂM THỬ VÀ TRUY VẾT `[A11]` · 🟩

## 9.1. Ma trận role kiểm thử

| Vai trò nghiệp vụ | Mã vai trò hệ thống | Mục tiêu kiểm thử |
|---|---|---|
| Lãnh đạo phòng | `LDDV` | Functional ý 1 (người chuyển), ý 2 (người giao bị lan lên) |
| Chuyên viên | `NV` | Functional ý 1 (người Nhận để biết đọc), ý 2 (bấm *Nhận để biết*) |
| Văn thư | `VT` | Ý 1 từ văn bản đơn vị; đơn vị nhận Nhận để biết (TBD-01); không thấy nút ý 2 trên văn bản đơn vị |
| Trợ lý | `TL` | Regression: trợ lý cùng nhận không bị đổi hành vi |
| Người dùng ứng dụng di động | mọi vai trò | AC-21, AC-34 |

## 9.2. Traceability Requirement → Rule → AC

| FR | BR | AC | EC | Ghi chú |
|---|---|---|---|---|
| FR-01 | BR-01, BR-02, BR-03, BR-04, BR-05 | AC-01 → AC-07 | EC-01, EC-02, EC-03 | BR-05 chờ TBD-01 |
| FR-02 | BR-06, BR-07 | AC-08 → AC-12 | EC-07, EC-16 | Chờ TBD-01, TBD-02, TBD-03 |
| FR-03 | BR-08, BR-09, BR-10, BR-12, BR-13 | AC-13 → AC-16, AC-18 → AC-20 | EC-04, EC-05, EC-06, EC-08 | BR-12, BR-13 đề xuất AI |
| FR-04 | BR-11 | AC-17 | EC-09 | |
| FR-05 | BR-15 → BR-20 | AC-22 → AC-33 | EC-11 → EC-15 | |
| FR-06 | BR-14, BR-21 | AC-21, AC-34 | EC-13 | Chờ TBD-07 |
| FR-07 | BR-22 | AC-35 | — | |
| FR-08 | BR-23 | AC-36, AC-37 | EC-10 | Chờ TBD-06 |

## 9.3. Regression tối thiểu

- Chuyển có Chủ trì / Phối hợp, chuyển cho nhóm, chuyển văn bản đi: trạng thái người chuyển không đổi so với hiện tại.
- Hoàn thành, Trả lại, Cho ý kiến của Chủ trì / Phối hợp: không đổi (VBĐ NV-08, NV-09, NV-07).
- Chủ trì hoàn thành lan lên người giao và kéo Phối hợp / Nhận để biết cùng cấp: không đổi (VBĐ BR-28, BR-42).
- Hộp *Văn bản nhận để biết*: lọc mặc định chưa đọc, thao tác chuyển / lưu hồ sơ / ghi chú không đổi (VBĐ BR-08, Q9).
- Đánh dấu đã đọc / chưa đọc hàng loạt ở các hộp khác: không đổi (trừ quyết định TBD-03).
- Tiếp nhận văn bản Chủ trì / Phối hợp của văn thư: không đổi.
- Tự chuyển sau tiếp nhận, nắm tình hình, trợ lý cùng nhận: không đổi.
- Ứng dụng di động bản cũ (chưa có nút) vẫn mở / đọc văn bản bình thường.

---

# 10. PHẠM VI KỸ THUẬT, KIẾN TRÚC VÀ MAPPING CSDL `[A12]` · 🟩

> Kiểm code ngày 02/10/2026 trên thư mục làm việc (`web-spring/`, `backend2.0/`), chỉ đọc. DB DEV **chưa** truy vấn —
> các cột ghi `VERIFIED_CODE` (thấy trong SQL / entity), chưa `VERIFIED_DB`. Viết tắt: `WEB/` =
> `web-spring/src/main/java/com/viettel/`, `BIZ/` = `web-spring/src/main/java/com/voffice/service/business/`, `ZUL/` =
> `web-spring/src/main/webapp/view/voffice/`, `BE1/` = `backend2.0/backendvoffice/src/main/java/com/viettel/voffice/`,
> `BE2/` = `backend2.0/backendvoffice/src/main/java/com/viettel/office/`.

## 10.1. Quy tắc nguồn sự thật

| Thứ tự | Nguồn | Dùng để xác định | Khi mâu thuẫn |
|---|---|---|---|
| 1 | Tài liệu này | WHAT/WHY, phạm vi, BR, AC | Không sửa BR bằng suy luận kỹ thuật |
| 2 | `knowledge/van-ban/den`, `knowledge/van-ban/chuyen-van-ban` | Hành vi cũ, quy tắc đã xác nhận | Dùng làm OLD behavior + regression |
| 3 | Source code hiện tại | Control-flow, service, DAO | **Đang mâu thuẫn với nguồn 2** ở BR-14 CVB và L13 VBĐ (mục 10.9) — DEV đối chiếu nhánh thật trước khi code |
| 4 | DB schema + SELECT | Bảng/cột/quan hệ thật | Chưa verify → `TBD_NOT_CONFIRMED` |

**Quy ước riêng của yêu cầu này:** "đã đọc" = cột `CONFIRM_TIME` khác null (Q03 YC111); nút *Nhận để biết* là nút mới
trên màn chi tiết văn bản `popupVB.zul`, **không** dùng API `mark-received-know-doc` hiện có (API đổi sang Phối hợp).

## 10.2. Call-chain

| Layer | Thành phần | Vai trò với YC111 | Độ tin cậy |
|---|---|---|---|
| UI/ZK | `ZUL/document/reportSendReceiveDoc/popupVB.zul` (thanh nút :4224-4290) | Màn chi tiết văn bản — thêm / sửa nút *Nhận để biết* | VERIFIED_CODE |
| ViewModel | `WEB/voffice/vm/document/DocumentViewDetailVM.java` (cờ nút :1213-1248, `NDB` :1901-1909; xem file `readAllAttachedFile` :3030, đánh dấu đọc khi đóng trình xem :3221-3240) | Điều kiện hiện nút; điểm ghi "đã đọc" khi xem file | VERIFIED_CODE |
| ViewModel | `DocumentPendingProcessingVM` :2216, :2599 · `DocumentReceiveToKnowVM` :1574-1588, :8096 · `DocumentPendingReceptionVM` :1649-1653, :9963 · `DocOrgAllVM`, `DocumentProcessedVM`, `DocumentSearchVM`… | Mở văn bản không có file chính thì ghi "đã đọc"; nút đánh dấu đã đọc / chưa đọc hàng loạt | VERIFIED_CODE |
| Business (web) | `BIZ/DocumentBusiness.java` `updateReadingStatus` :5038, :5058-5071; `completeParentDocumentIfAllRead` :5019-5036 | Gọi BE ghi đọc; tự hoàn thành (bản có sẵn, chạy ở web) | VERIFIED_CODE |
| API BE1 | `/DocumentAction/sendDocument`, `/sendDocumentMultiTransfer` → `BE1/controler/DocumentController.java` :7956, :8482 | Chuyển văn bản | VERIFIED_CODE |
| API BE1 | `/DocumentAction/UpdateReadingStatus` → `DocumentController.updateReadingStatus` :9956-9990; `/updateReadingStatusV2` :14667-14693; `/Files/DownloadContentFile`, `/Files/DownloadStreamFile` → `DownloadFileDocumentDAO` :786-791; `/wopi/generate-online-editor-url` → `WOPIController` :1256-1260 | Mọi đường ghi `CONFIRM_TIME` — phải cùng kích hoạt BR-09 (BR-14) | VERIFIED_CODE |
| API BE2 | `/api/doc-in/complete-document` → `BE2/services/impl/DocInServiceImpl.java` `completeDocument` :204-241, `updateProcessedByDocumentInGroupOrDocumentInStaff` :515-609, `updateCompleteParentProcesses` :741-902 | Hoàn thành + lan lên người giao (BR-11, BR-17, BR-18) | VERIFIED_CODE |
| API BE2 | `/api/doc-in/mark-received-know-doc/{doc-id}` → `DocInServiceImpl` :160-165 → `DocumentInStaffRepositoryJPA.updateSendTypeToCC` :71-75 | Có sẵn, **không ai gọi**, đổi `SEND_TYPE` sang 2 — không dùng cho YC111; nên bỏ hoặc sửa để di động không gọi nhầm | VERIFIED_CODE |
| DAO BE1 | `BE1/database/dao/document/DocumentInStaffDAO.java` `sendDocument` :1009, cờ `hasOnlyNBSendType` :1303-1349, gọi `updateProcessedDocument` :1482-1483, :1598-1639 | Đổi luồng nguồn sang 4 (BR-03) | VERIFIED_CODE |
| DAO BE1 | `DocumentDAO.sendDocumentToGroupInternal` :9662, đặt `STATUS = 3` cho đơn vị Nhận để biết :9746-9750 | Phải đổi cho BR-05 (chờ TBD-01) | VERIFIED_CODE |
| DAO BE1 | `DocumentDAO.hasUserReadAllDocument` :7214-7290, `getSenderDocumentInStaffId` :7292 | Bản có sẵn của điều kiện "đọc hết" — **sai phạm vi** so với BR-08 (mục 10.9) | VERIFIED_CODE |
| DAO BE1 | `DocumentDAO.updateStatusDocumentInStaffVof2` :6735-6766, `updateStatusDocumentInGroupVof2` :6567-6597 (thu hồi) | Điểm kích hoạt BR-13 | VERIFIED_CODE |
| DB | `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_GROUP`, `DOCUMENT_PROCESS`, `FILES_ATTACHMENT` | Mục 10.3 | VERIFIED_CODE |

## 10.3. Bảng/cột liên quan

| Bảng | Mục đích | Cột chính liên quan | Thay đổi | Độ tin cậy |
|---|---|---|---|---|
| `DOCUMENT_IN_STAFF` | Dòng nhận cá nhân | `DOCUMENT_IN_STAFFID`, `DOCUMENTID`, `STAFFID_VOF2`, `GROUPID_VOF2`, `STATUS`, `SEND_TYPE`, `CONFIRM_TIME`, `IS_COMPLETE`, `COMPLETE_DATE`, `CHANGE_SEND_TYPE_DATE`, `IS_INFORMALITY` | Không thêm cột (nếu TBD-03 = A) | VERIFIED_CODE |
| `DOCUMENT_IN_GROUP` | Dòng nhận đơn vị | `DOCUMENT_IN_GROUP_ID`, `DOCUMENT_ID`, `GROUP_ID_VOF2`, `STATUS`, `SEND_TYPE`, `CONFIRM_TIME` | Không thêm cột (nếu TBD-03 = A) | VERIFIED_CODE |
| `DOCUMENT_PROCESS` | Quan hệ cha – con của luồng nhận (`PARENT_ID`, `IN_STAFF_ID`, `DEL_FLAG`) | Tìm luồng nguồn của người chuyển và tập Nhận để biết | Không | VERIFIED_CODE |
| `FILES_ATTACHMENT` | File của văn bản; `TYPE` 1 file chính · 2 đính kèm · 3 file gốc · 4 file mã hóa | Xác định "có file chính" (BR-06) | Không | VERIFIED_CODE |
| `DOCUMENT_IN_FILE` | File chuyển kèm khi chuyển | Không tính vào BR-06 (chờ TBD-02) | Không | VERIFIED_CODE |
| (nếu TBD-03 = B) cột / bảng mới ghi "đã đọc nội dung" | Phân biệt đọc thật với *Đánh dấu đã đọc* | — | **Cần migration** | TBD_NOT_CONFIRMED |

## 10.4. Mapping UI → Code → DTO/API → CSDL

| UI ID | Field UI | ZUL / VM / Command | Payload / API | DB đích | Ghi chú |
|---|---|---|---|---|---|
| UI-01 | Nút *Nhận để biết* | `popupVB.zul:4271-4277` `receiveToKnowBtn` / `DocumentViewDetailVM.isVisibleReceiveToKnow` :3518 / `doReceiveToKnow` :3433 | Hiện tại: `/api/doc-in/complete-document` rồi chuyển cho chính mình (2 lần gọi). Cần: **một** API BE mới (BR-21, NFR-01) | `DOCUMENT_IN_STAFF.STATUS = 5`, `SEND_TYPE = 3` | Thiết kế API do DEV quyết |
| UI-02 | Hộp xác nhận | Mới trong `doReceiveToKnow` | — | — | Code có sẵn chưa có xác nhận |
| UI-04 | Vai trò khi chuyển | Popup chuyển (CVB NV-01) | `/DocumentAction/sendDocument` | `SEND_TYPE` | Giữ nguyên |

## 10.5. CRUD và lifecycle dữ liệu

| Action | Trên giao diện (chưa lưu) | Khi lưu | Khi hủy | Điểm cần xác nhận |
|---|---|---|---|---|
| Chuyển chỉ Nhận để biết | Chọn người / đơn vị, vai trò | Tạo dòng nhận; luồng nguồn = 4 | Không đổi | TBD-01 (đơn vị) |
| Ghi "đã đọc" | — | `CONFIRM_TIME = now` (nếu đang null); kiểm BR-09 | — | TBD-02, TBD-03 |
| Tự hoàn thành | — | Luồng nguồn = 5, `IS_COMPLETE`, `COMPLETE_DATE`, nội dung MSG-05 | — | BR-12 |
| Nhận để biết | Hộp xác nhận | Dòng = 5 + `SEND_TYPE = 3` (+ `CHANGE_SEND_TYPE_DATE`) trong một giao dịch; lan lên theo BR-18 | Không đổi | Đổi `SEND_TYPE` trên dòng hiện có hay tạo dòng mới — DEV chọn, nhưng kết quả người dùng thấy phải đúng BR-17 |
| Thu hồi | — | Dòng bị thu hồi = 0; kiểm BR-13 | — | BR-13 |
| Xóa | Không áp dụng | — | — | — |

## 10.6. Phạm vi KHÔNG thay đổi và regression bắt buộc

| Hạng mục baseline | Có thay đổi? | Yêu cầu |
|---|---|---|
| Chuyển có Chủ trì / Phối hợp / nhóm, chuyển văn bản đi | Không | Giữ nguyên `hasToOrCCSendType` và nhánh nhóm |
| Hoàn thành / lan lên (`updateCompleteParentProcesses`) | Không | Dùng lại, không sửa logic lan lên |
| Trả lại, Cho ý kiến, Tiếp nhận văn bản Chủ trì / Phối hợp | Không | Giữ nguyên |
| Nắm tình hình | Chờ TBD-04 | — |
| Đánh dấu đã đọc / chưa đọc hàng loạt | Chờ TBD-03 | — |

## 10.7. Ràng buộc triển khai

- Không đổi schema ngoài kết quả TBD-03.
- Logic BR-03, BR-09, BR-13, BR-17, BR-18 đặt ở **máy chủ**; web chỉ hiện nút và gọi API (ứng dụng di động gọi thẳng máy chủ).
- Mã nguồn ứng dụng di động không có trong repo — phần giao diện di động do đội mobile làm theo API mới (TBD-07).
- Không dùng / bỏ hẳn API `mark-received-know-doc` hiện có để tránh di động gọi nhầm (đổi sang Phối hợp).

## 10.8. Quy tắc cho AI/DEV khi đọc tài liệu này

| Rule ID | Quy tắc |
|---|---|
| AI-01 | Không suy tên bảng/cột từ tên class, DTO hay nhãn UI. |
| AI-02 | Không tự bịa bảng/cột/API/method/business rule — thiếu bằng chứng ghi `TBD_NOT_CONFIRMED`. |
| AI-03 | Mỗi field phải trace được UI → ZUL → VM → DTO → backend → DAO → DB, kèm `file::hàm::dòng`. |
| AI-04 | Tài liệu và code mâu thuẫn → ghi `CONFLICT` + đề xuất, chờ xác nhận, không tự chọn. |
| AI-05 | Code có sẵn (mục 10.9) **không** phải yêu cầu: chỗ nào lệch BR thì sửa theo BR, không sửa BR theo code. |

## 10.9. Code có sẵn liên quan YC111 — CONFLICT với tri thức và lệch với tài liệu này

Code trên máy (cả bản trong `merge/bitbucket/`) **đã có** một phần chức năng; tri thức (`knowledge/`, viết từ
`kha_develop` 2026-10-01) ghi là **chưa có**. DEV xác nhận nhánh nào là chuẩn trước khi code.

| # | Có sẵn trong code | Bằng chứng | So với tài liệu này |
|---|---|---|---|
| K1 | Chuyển chỉ Nhận để biết → luồng nguồn = 4 (cờ `hasOnlyNBSendType`) | `DocumentInStaffDAO.java:1303-1349, 1482-1483` | **Khớp** BR-03 — nhưng tri thức (CVB BR-14) ghi là giữ 3. Riêng: cờ chỉ cần **một** đối tượng Nhận để biết cùng các vai trò khác không phải 1 / 2 (vd. Tham mưu 5) là bật → cần soát lại theo BR-01 |
| K2 | Tự hoàn thành khi "đọc hết" | `DocumentBusiness.completeParentDocumentIfAllRead` :5019-5036; `DocumentDAO.hasUserReadAllDocument` :7214-7290 | **Lệch BR-08:** câu kiểm chỉ xét **các dòng của chính người vừa đọc**, không xét người Nhận để biết khác → người chuyển bị hoàn thành ngay khi **người đầu tiên** đọc. Không loại dòng đã thu hồi; không xét BR-10 (đã có Chủ trì sau) |
| K3 | Tự hoàn thành chạy ở **web** (4 màn: chi tiết, Chờ xử lý, Nhận để biết…) | `DocumentViewDetailVM:3240`, `DocumentPendingProcessingVM:2227, 2609`, `DocumentReceiveToKnowVM:1587` | **Lệch BR-14:** đọc trên di động, tải file, *Đánh dấu đã đọc* hàng loạt không kích hoạt |
| K4 | Người chuyển là văn bản đơn vị | `getSenderDocumentInStaffId` :7292 chỉ trả dòng **cá nhân** của người chuyển | **Lệch BR-02:** luồng đơn vị của văn thư không được tự hoàn thành |
| K5 | "Đã đọc" khi có file chính = khi đóng trình xem file; không có file chính = khi mở chi tiết | `DocumentReceiveToKnowVM:1574-1588`, `DocumentViewDetailVM:3221-3240` | **Khớp** BR-06 (a)(b) ở web |
| K6 | Đơn vị Nhận để biết vào thẳng trạng thái 3 | `DocumentDAO.java:9746-9750` | **Lệch BR-05** (chờ TBD-01) |
| K7 | Nút *Nhận để biết* ở chi tiết văn bản | `popupVB.zul:4271-4277`; `DocumentViewDetailVM.java:3433-3530` | **Lệch:** (a) chỉ hiện khi mở từ hộp *Chờ xử lý* (`CXL`), không có tab *Tất cả* (BR-15a); (b) hiện cả trạng thái 4 / 7 vì dựa vào quyền Hoàn thành (BR-15d); (c) không loại vai trò khác 1 / 2 (BR-15c); (d) **bỏ qua yêu cầu trả lời** (`setIgnoreCheckingRequestReplyStatus(true)` :3461) và không ẩn khi có nhắc việc — trái BR-16; (e) không có hộp xác nhận (BR-17); (f) hai bước riêng (hoàn thành, rồi tự chuyển cho chính mình vai trò 3) — không cùng giao dịch (NFR-01); (g) chỉ có ở web (BR-21); (h) không thông báo người giao (BR-20) |
| K8 | Câu thông báo thành công khác nhau giữa hai file ngôn ngữ tiếng Việt | `zk-label_vi.properties:637` "Chuyển nhận văn bản để biết thành công" · `zk-label.properties:626` "Đã nhận văn bản để biết thành công" | Thống nhất theo MSG-02 |

**Quality gate trước khi DEV code:** chốt TBD-01, TBD-02, TBD-03, TBD-04 (BLOCKING); BA đồng ý hoặc sửa các BR / EC ghi
*(đề xuất AI)* (BR-12, BR-13, EC-03, EC-08, EC-12 → EC-14); DEV xác nhận nhánh chuẩn cho mục 10.9. Chưa đủ → tài liệu
giữ `DRAFT`.

---

# 11. CÁC ĐIỂM CẦN XÁC NHẬN (TBD) `[A13]` · 🟨

| Mã TBD | Câu hỏi cần chốt | Ảnh hưởng BR/AC/EC | Mức | Ai chốt | Hạn | Kết luận |
|---|---|---|---|---|---|---|
| TBD-01 | **Người nhận Nhận để biết vào đâu, đơn vị "đọc" khi nào?** Q05 trả lời "cá nhân vào Chờ xử lý của cá nhân, đơn vị vào Chờ tiếp nhận đơn vị". (a) Cá nhân: **A.** hộp *Văn bản nhận để biết* như hiện tại (trạng thái 3 là "chờ xử lý" về dữ liệu) · **B.** hộp *Văn bản chờ xử lý* (trái quy tắc đã chốt VBĐ Q3). (b) Đơn vị: hiện vào thẳng trạng thái 3, Q05 muốn *Chờ tiếp nhận* — xác nhận đổi? Nếu đổi thì đơn vị tính "đã đọc" khi: **A.** văn thư mở xem văn bản ngay ở *Chờ tiếp nhận* · **B.** văn thư bấm *Tiếp nhận* · **C.** văn thư tiếp nhận rồi mở xem. Sau tiếp nhận văn bản đơn vị Nhận để biết nằm ở hộp nào? Đề xuất AI: (a) A; (b) đổi sang Chờ tiếp nhận, tính đã đọc theo A, sau tiếp nhận vào *Chờ xử lý* văn bản đơn vị như văn bản thường | BR-04, BR-05, BR-07; AC-06, AC-07, AC-12; EC-16 | BLOCKING | BA / anh Long | 09/10/2026 | (chưa chốt) |
| TBD-02 | **"Xem file" là xem file nào, bao nhiêu file?** Q03: "có file thì phải khi xem file dự thảo mới coi là đã đọc". Văn bản đến có file chính, phụ lục / đính kèm, file chuyển kèm. **A.** Mở trình xem **file chính** (hệ thống mở mọi file chính cùng lúc) rồi đóng · **B.** Phải mở **từng** file chính · **C.** Mở bất kỳ file nào. Tải file chính về máy có tính không? Đề xuất AI: A, và tải file chính về cũng tính (hệ thống đang ghi đọc khi tải) | BR-06; AC-08, AC-09; EC-07 | BLOCKING | BA | 09/10/2026 | (chưa chốt) |
| TBD-03 | **Nút *Đánh dấu đã đọc* trên danh sách** (không mở văn bản, kể cả hàng loạt) có được tính là đã đọc để tự hoàn thành không? **A.** Có — cùng một thời điểm đọc, không phân biệt (không cần thêm dữ liệu) · **B.** Không — phải mở thật; cần lưu thêm dữ liệu (migration) hoặc ẩn nút này ở hộp Nhận để biết · **C.** Ẩn nút *Đánh dấu đã đọc* ở hộp *Văn bản nhận để biết*. Đề xuất AI: C (giữ đúng ý "phải xem mới tính", không cần đổi dữ liệu) | BR-06; AC-11; mục 10.3 | BLOCKING | BA | 09/10/2026 | (chưa chốt) |
| TBD-04 | **Người nhận vai trò *Nắm tình hình*** (lưu như Nhận để biết kèm cờ riêng, không hiện ở hộp văn bản đến nào). Lần chuyển gồm Nhận để biết + Nắm tình hình thì sao? **A.** Tính như Nhận để biết: luồng nguồn sang 4, Nắm tình hình cũng phải "đọc" · **B.** Tính như Nhận để biết khi xét "chỉ Nhận để biết" (sang 4), nhưng **không** chờ Nắm tình hình đọc · **C.** Có Nắm tình hình → không áp dụng YC111. Đề xuất AI: B | BR-01, BR-08 | BLOCKING | BA | 09/10/2026 | (chưa chốt) |
| TBD-05 | Q03(b), Q09(b)(c) chưa trả lời — AI dùng đề xuất làm giả định: đã tự hoàn thành thì *Đánh dấu chưa đọc* không mở lại; *Nhận để biết* không hoàn tác; báo người giao (MSG-06), tự hoàn thành không báo. Đồng ý? | BR-09, BR-19, BR-20; AC-20, AC-32, AC-33; EC-06; MSG-06 | NON-BLOCKING | BA | 09/10/2026 | (giả định theo đề xuất) |
| TBD-06 | Q10 chỉ trả lời "web/mobile" — AI giả định: áp dụng cả văn bản mật và liên thông; **không** xử lý văn bản cũ. Đồng ý? | BR-23; AC-36, AC-37; EC-10 | NON-BLOCKING | BA | 09/10/2026 | (giả định theo đề xuất) |
| TBD-07 | Ứng dụng di động: đội mobile làm nút *Nhận để biết* ở phiên bản nào; app bản cũ có đang gọi API `mark-received-know-doc` không (trước khi bỏ / sửa API này)? | BR-21; AC-34; mục 10.7 | NON-BLOCKING | DEV phụ trách + đội mobile | 09/10/2026 | (chưa chốt) |
| TBD-08 | Q01 chưa có **ví dụ thật** (văn bản gì, ai chuyển cho ai) — cần để Tester dựng dữ liệu kiểm thử sát thực tế | Mục 0; mục 8 dữ liệu mẫu | NON-BLOCKING | BA / anh Long | 09/10/2026 | (chưa chốt) |

**Tiêu chí bàn giao DEV:** chỉ estimate / code chính thức khi TBD-01 → TBD-04 đã chốt và BA đã đồng ý các mục *(đề xuất
AI)*.

---

# KẾT LUẬN

YC111 làm hai việc trên văn bản đến: (1) chuyển văn bản mà mọi người / đơn vị nhận đều là Nhận để biết thì văn bản của
người chuyển sang *Đã xử lý* ngay và tự *Đã hoàn thành* khi tất cả đã đọc (người chuyển vẫn tự hoàn thành sớm được);
(2) người nhận Chủ trì / Phối hợp tự chuyển văn bản của mình thành Nhận để biết bằng một nút trong chi tiết văn bản, tính
như hoàn thành. Áp dụng web và di động, logic đặt ở máy chủ. Đã chốt Q02, Q04, Q06, Q07, Q08 và phần lớn Q01, Q03, Q05,
Q09, Q10. Còn **4 TBD chặn code** (nơi vào và cách "đọc" của đơn vị, file nào cần xem, nút đánh dấu đã đọc, Nắm tình
hình) và một số điểm AI đề xuất cần BA đồng ý. Code trên máy đã có một phần chức năng nhưng lệch yêu cầu ở 7 điểm
(mục 10.9) — DEV dùng làm điểm xuất phát, sửa theo BR.
