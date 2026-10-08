**TÀI LIỆU ĐẶC TẢ YÊU CẦU CHỨC NĂNG**

**YC_NV_01 - XÓA NHẮC VIỆC THEO TỪNG ĐƠN VỊ XỬ LÝ VÀ XÓA NHIỀU DÒNG MỘT LẦN**

**Hệ thống Văn bản và Điều hành tỉnh Khánh Hòa**

| Thuộc tính | Giá trị |
|---|---|
| Mã yêu cầu | YC_NV_01 |
| Chức năng | Theo dõi nhắc việc — thao tác Xóa |
| Phân hệ (knowledge) | `lich-nhac-viec` (chính) · `van-ban/den` (cờ "văn bản có nhắc việc") |
| Loại yêu cầu | Bổ sung nghiệp vụ |
| Loại tài liệu | Đặc tả yêu cầu chức năng (BA/FRD) |
| Phiên bản | 1.0 |
| Trạng thái | DRAFT |
| Ngày cập nhật | 08/10/2026 |

> Nhãn mục: 🟦 BA viết · 🟩 AI điền từ tri thức + code · 🟨 AI soạn từ lời BA, BA đọc và chốt.
> Nguồn hiện trạng: `knowledge/lich-nhac-viec/` (ký hiệu LNV NV-xx / BR-xx) và code nhánh `kha_develop` (`file:dòng`).
> Viết tắt: **RVM** = `web-spring/src/main/java/com/viettel/voffice/vm/reminder/ReminderVM.java` · **RB** =
> `web-spring/src/main/java/com/voffice/service/business/ReminderBusiness.java` · **RC** =
> `backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/ReminderController.java` · **RSI** =
> `backend2.0/backendvoffice/src/main/java/com/viettel/office/services/impl/ReminderServiceImpl.java` · **RRI** =
> `backend2.0/backendvoffice/src/main/java/com/viettel/office/repositories/impl/ReminderRepositoryImpl.java` · **RRRJ** =
> `backend2.0/backendvoffice/src/main/java/com/viettel/office/repositories/jpa/ReminderReplyRepositoryJPA.java` · **ZUL** =
> `web-spring/src/main/webapp/view/voffice/reminder/reminder_search.zul`.

---

# LỊCH SỬ THAY ĐỔI `[A1]` · 🟦

| Phiên bản | Ngày | Nội dung | Người thực hiện |
|---|---|---|---|
| 1.0 | 08/10/2026 | Bản đầu tiên — AI soạn từ phiếu ý tưởng + câu trả lời vòng 1 (`cau-hoi.md`) | BA (chưa ký) · AI |

# PHÊ DUYỆT / XÁC NHẬN `[A2]` · 🟦

| Vai trò | Họ tên | Trạng thái | Ngày | Ghi chú |
|---|---|---|---|---|
| BA phụ trách | | Chưa xác nhận | | |
| DEV phụ trách | | Chưa xác nhận | | |
| Tester phụ trách | | Chưa xác nhận | | |
| Đại diện nghiệp vụ/Khách hàng | | Chưa xác nhận | | |

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

- **Muốn gì:** (nguyên văn) *"một nhắc việc sẽ có nhiều đơn vị xử lý, bao gồm CT và PH, mỗi đơn vị xử lý là 1 bản ghi
  và là cùng 1 nhắc việc. Hiện trạng khi xóa 1 bản ghi PH hoặc CT đang xóa all cả các nhắc việc của các đơn vị khác.
  Mong muốn: khi xóa các đơn vị xử lý khác CT thì chỉ xóa nhắc việc của đơn vị xử lý đó thôi, khi xóa CT cũng vậy
  nhưng có 1 case đặc biệt là nếu nhắc việc đó mà bị xóa hết các đơn vị xử lý CT thì cũng xóa luôn cả cái nhắc việc
  đó. Thêm option xóa nhiều như ảnh nữa."*
- **Ai dùng:** người tạo nhắc việc (giữ nguyên quyền hiện nay — câu trả lời Q02).
- **Vì sao cần:** muốn bỏ một đơn vị khỏi nhắc việc nhưng cả nhắc việc của các đơn vị khác biến mất theo.
- **Một tình huống thật cụ thể:** một văn bản giao nhắc việc cho 1 đơn vị chủ trì + 2 đơn vị phối hợp; người giao bấm
  Xóa ở dòng một đơn vị phối hợp → dòng của đơn vị chủ trì và đơn vị phối hợp còn lại cũng mất.
- **Kết quả mong muốn đo được:** xóa đúng dòng đã bấm; nhắc việc chỉ mất khi không còn đơn vị chủ trì; tick nhiều
  dòng xóa được một lần bằng nút "Xóa N nhắc việc" (ảnh `input/design/01_xoa-nhieu-nhac-viec.png`).
- **Kênh:** BA chọn **cả web và ứng dụng di động** (Q09-B) — xem TBD-02 · **Gấp không:** chưa ghi.

---

# 1. THÔNG TIN CHUNG `[A3]`

## 1.1. Mục đích · 🟦

Khi **người tạo nhắc việc** bấm Xóa ở một dòng trên lưới *Theo dõi nhắc việc*, hệ thống **chỉ xóa dòng đơn vị đó**;
nhắc việc chỉ bị xóa toàn bộ khi sau thao tác **không còn đơn vị xử lý chính** nào. Người tạo cũng **tick nhiều dòng
và xóa một lần** bằng nút "Xóa N nhắc việc".

## 1.2. Bối cảnh nghiệp vụ · 🟦

- Yêu cầu gốc: xem mục 0 (nguyên văn phiếu ý tưởng).
- Chức năng nghiệp vụ chính: Nhắc việc — giao việc kèm văn bản cho đơn vị chủ trì (CT) / phối hợp (PH), đơn vị trả
  lời, bên giao duyệt (LNV mục 1).
- Đường vào chức năng: **VĂN BẢN ĐI → Theo dõi nhắc việc** (menu `NHACVIEC`, id 441265) → nhóm *Cần xử lý* hoặc
  *Giao đi/Theo dõi* → lưới "Danh sách nhắc việc" → cột *Thao tác* (icon thùng rác) và nút "Xóa N nhắc việc".
- Vấn đề hiện tại: nút Xóa trên bất kỳ dòng nào xóa cả nhắc việc (mọi đơn vị). Người giao không có cách nào gỡ một đơn
  vị khỏi nhắc việc ngoài vào *Sửa* (và *Sửa* không bỏ được CT, bị ẩn khi có đơn vị đã trả lời).
- Kết quả mong muốn (đo được): (1) xóa 1 dòng PH của nhắc việc có 1 CT + 2 PH → còn đúng 2 dòng (CT + 1 PH); (2) xóa
  dòng CT duy nhất → cả nhắc việc mất; (3) tick 3 dòng, một lần bấm → 3 dòng mất.

## 1.3. Hiện trạng (AS-IS) và thay đổi (TO-BE) · 🟨 (AS-IS 🟩)

| STT | Nội dung | Hiện tại (AS-IS) | Yêu cầu (TO-BE) | Nguồn AS-IS |
|---|---|---|---|---|
| 1 | Cấu trúc một nhắc việc | Một nhắc việc (`REMINDER`) = một nội dung giao việc + **đúng một** đơn vị CT (web chỉ cho chọn một) + 0..N đơn vị PH; mỗi đơn vị là một dòng `REMINDER_REPLY` có trạng thái riêng. Máy chủ **không** chặn nhiều CT (chỉ chặn trùng đơn vị) | Giữ nguyên | LNV NV-02, BR-06, mục 5.1; `RVM:1950`; `RSI:621-636` |
| 2 | Lưới *Theo dõi nhắc việc* | Mỗi dòng lưới = một đơn vị (một nhắc việc giao 3 đơn vị → 3 dòng), nhãn CT / PH ở cột *Đơn vị xử lý* | Giữ nguyên; thêm cột tick chọn đầu lưới | LNV NV-01; `ZUL:315-346` |
| 3 | Ai thấy nút Xóa | Chỉ **người tạo** nhắc việc, ở **mọi trạng thái** dòng; máy chủ kiểm lại người tạo | **Giữ nguyên** (Q02-A, Q03) | LNV BR-08; `RVM:2446-2448`; `RSI:1296-1299` |
| 4 | Xóa một dòng làm gì | Xóa mềm **cả nhắc việc**: `REMINDER`, mọi `REMINDER_REPLY`, người theo dõi, liên kết văn bản; gỡ cờ "văn bản có nhắc việc" của **mọi** đơn vị được nhắc | Xóa mềm **chỉ dòng đơn vị đã bấm**; nhắc việc chỉ bị xóa toàn bộ khi không còn CT (BR-04, BR-05) | LNV NV-08; `RSI:1288-1334` |
| 5 | Cờ "văn bản có nhắc việc" (`HAS_REMINDER`) | Gỡ cho mọi đơn vị khi xóa nhắc việc; **không gỡ** khi bỏ đơn vị bằng *Sửa* | Gỡ **theo đơn vị bị xóa**; *Sửa* bỏ đơn vị cũng gỡ như xóa dòng (Q06-A+C) | LNV NV-08; `RSI:1336-1398`, `1118-1149` |
| 6 | Xóa nhiều | Chưa có. Cột tick và "chọn tất cả" đang bị comment trong ZUL; lệnh tick / bỏ tick còn trong VM; hàm web gửi nhiều mã không ai gọi và trỏ vào endpoint xóa đơn | Bật cột tick cho dòng có nút Xóa; nút "Xóa N nhắc việc"; endpoint mới nhận danh sách dòng | `ZUL:320-322`, `336-338`; `RVM:1196-1240`; `RB:384-404`; LNV NV-20 |
| 7 | Hộp xác nhận | Câu chung *"Đồng chí có chắc chắn muốn xóa?"* (OK / Hủy) | **Giữ nguyên** câu chung cho cả xóa một dòng và xóa nhiều (Q08-B) | `zk-label.properties:10613`; `CommonVM.java:1455` |
| 8 | Lý do, thông báo | Không cần lý do; không gửi SMS / thông báo; vết = `DEL_FLAG`, `UPDATED_BY`, `UPDATED_AT` trên dòng bị xóa | **Giữ nguyên** (Q10-A, Q06-A) | LNV NV-08, BR-22; `RRRJ:21-22` |
| 9 | Xóa văn bản / dự thảo | Nhắc việc giao kèm văn bản đó bị xóa toàn bộ | **Giữ nguyên** (Q07-A) | LNV NV-08; `RSI:1794-1871` |
| 10 | Ứng dụng di động | Không có màn nhắc việc trên di động (không có API di động nào gọi nhắc việc) | Chưa chốt — TBD-02 | grep `reminder` trong `AppMobileController.java` rỗng; `knowledge/tich-hop` không có nhắc việc |

**Tóm tắt thay đổi:** đổi **đối tượng bị xóa** từ "cả nhắc việc" thành "một dòng đơn vị" (kèm quy tắc CT), thêm **xóa
nhiều**, và cho *Sửa* bỏ đơn vị dùng cùng quy tắc gỡ cờ. Không thêm trạng thái, không thêm bảng / cột; quyền và câu
xác nhận giữ nguyên.

## 1.4. Phạm vi chức năng bị ảnh hưởng · 🟩

| STT | Điểm vào chức năng | Màn hình/Action | Trong phạm vi |
|---|---|---|---|
| 1 | VĂN BẢN ĐI → Theo dõi nhắc việc → lưới, icon thùng rác | Xóa một dòng đơn vị | Có |
| 2 | VĂN BẢN ĐI → Theo dõi nhắc việc → cột tick + nút "Xóa N nhắc việc" | Xóa nhiều dòng | Có (mới) |
| 3 | VĂN BẢN ĐI → Theo dõi nhắc việc → Sửa → bỏ đơn vị PH khỏi danh sách | Gỡ cờ "văn bản có nhắc việc" cho đơn vị bị bỏ | Có (Q06-C) |
| 4 | Hộp văn bản đến của đơn vị bị xóa (số "văn bản có nhắc việc", kiểm khi Hoàn thành văn bản đến) | Không sửa màn; chỉ dữ liệu cờ đổi | Gián tiếp — regression |
| 5 | Xóa văn bản / dự thảo → xóa nhắc việc; tạo / sửa / trả lời / duyệt / nhắc lại / chuyển xử lý / báo cáo nhắc việc; chi tiết nhắc việc; tab nhắc việc trong chi tiết văn bản | Không được mô tả trong YC_NV_01 | Ngoài phạm vi; cần regression |

**Kênh áp dụng:** Web. Ứng dụng di động hiện **không có** màn nhắc việc nên không có hành vi để đổi; BA chọn Q09-B
"web và di động" → phải chốt TBD-02 (làm mới nhắc việc trên di động là một yêu cầu riêng, không thuộc tài liệu này).

## 1.5. Thuật ngữ · 🟨

| Thuật ngữ | Định nghĩa sử dụng trong tài liệu |
|---|---|
| Nhắc việc | Một dòng `REMINDER`: một nội dung giao việc gắn văn bản, do một người tạo |
| Dòng đơn vị | Một dòng `REMINDER_REPLY` thuộc nhắc việc: một đơn vị được nhắc với vai trò CT (`ORG_ROLE = 1`) hoặc PH (`ORG_ROLE = 2`), có trạng thái riêng. Trên lưới mỗi dòng lưới là một dòng đơn vị |
| Dòng sao | Dòng `REMINDER_REPLY` trạng thái *Đã xử lý tạm* (5), cùng nhắc việc, cùng đơn vị, cùng vai trò với dòng gốc (`dac-thu` bẫy 3) |
| Dòng hoạt động | Dòng có `DEL_FLAG = 0` hoặc NULL |
| Xóa | Xóa mềm: đặt `DEL_FLAG = 1`, ghi `UPDATED_BY`, `UPDATED_AT` |
| Người tạo | Người có `REMINDER.CREATED_BY` = mã người đăng nhập |
| Cờ "văn bản có nhắc việc" | `DOCUMENT_IN_GROUP.HAS_REMINDER` / `DOCUMENT_IN_STAFF.HAS_REMINDER` = 1 trên luồng văn bản đến của đơn vị được nhắc (LNV NV-08) |

---

# 2. PHẠM VI VÀ VAI TRÒ `[A4]` · 🟨

## 2.1. Vai trò

Quyền xóa nhắc việc **không theo mã vai trò** mà theo **người tạo** (`CREATED_BY`), kiểm cả web (ẩn / hiện nút) và máy
chủ (LNV BR-08). Người tạo có thể mang bất kỳ vai trò nào có quyền tạo nhắc việc (người có văn bản do mình tạo / trình,
hoặc VT / LDDV / TTDV của đơn vị ban hành — LNV NV-02).

| Vai trò nghiệp vụ | Mã vai trò hệ thống | Được làm gì trong YC_NV_01 | Ghi chú |
|---|---|---|---|
| Người tạo nhắc việc | (bất kỳ — xác định bằng `CREATED_BY`) | Xóa một dòng đơn vị; tick nhiều dòng của **các nhắc việc mình tạo** và xóa một lần; bỏ đơn vị khi Sửa | Vai trò chính |
| Lãnh đạo theo dõi / chuyên viên theo dõi | `LDDV`, `TTDV`, `NV`… | Không có nút Xóa, không có ô tick | Regression: không được mở rộng quyền |
| Đơn vị được nhắc (VT / LDDV / TTDV tại đơn vị) và người được gán | `VT`, `LDDV`, `TTDV`, `NV` | Không có nút Xóa, không có ô tick; sau khi dòng của đơn vị mình bị xóa thì không còn thấy nhắc việc ở *Cần xử lý* | Regression |

**Lưu ý phạm vi role:** không suy diễn lãnh đạo theo dõi hay quản trị có quyền xóa (Q02-A).

## 2.2. Tiền điều kiện chung

- Người dùng đã đăng nhập, có menu *Theo dõi nhắc việc*.
- Có ít nhất một nhắc việc do người đó tạo, đã giao cho ≥ 2 đơn vị (để thấy khác biệt xóa một dòng).
- Không cần cấu hình hệ thống mới.

---

# 3. TỔNG QUAN YÊU CẦU CHỨC NĂNG `[A5]` · 🟦 danh sách FR · 🟩 3.1 · 🟨 3.2–3.3

| ID | Trigger/Action của người dùng | Xử lý mong muốn | BR liên quan |
|---|---|---|---|
| FR-01 | Người tạo bấm icon Xóa ở một dòng **PH** và xác nhận | Chỉ dòng đơn vị đó (và dòng sao của nó) bị xóa mềm; nhắc việc và các dòng khác giữ nguyên; gỡ cờ "văn bản có nhắc việc" của riêng đơn vị đó | BR-01, BR-02, BR-03, BR-04, BR-06, BR-10, BR-11, BR-14 |
| FR-02 | Người tạo bấm icon Xóa ở một dòng **CT** và xác nhận | Nếu sau khi xóa nhắc việc vẫn còn dòng CT hoạt động khác → như FR-01; nếu **không còn CT** → xóa toàn bộ nhắc việc (mọi dòng còn lại, người theo dõi, liên kết văn bản, gỡ cờ mọi đơn vị) | BR-05, BR-06 |
| FR-03 | Người tạo tick ≥ 1 dòng rồi bấm "Xóa N nhắc việc" và xác nhận | Áp quy tắc FR-01 / FR-02 cho từng dòng tick trong một giao dịch; xong tải lại lưới, bỏ tick | BR-07, BR-08, BR-09, BR-10, BR-14 |
| FR-04 | Người tạo vào *Sửa*, bỏ một đơn vị PH khỏi danh sách rồi Lưu | Dòng đơn vị bị bỏ xóa mềm **và** gỡ cờ "văn bản có nhắc việc" của đơn vị đó (cùng quy tắc FR-01) | BR-12 |
| FR-05 | Xóa văn bản / dự thảo đang gắn nhắc việc | Giữ hành vi hiện tại: xóa toàn bộ nhắc việc | BR-13 |

## 3.1. Mapping dữ liệu nguồn → đích

Không áp dụng — yêu cầu không chuyển / sao chép dữ liệu.

## 3.2. Trạng thái và chuyển trạng thái

Không thay đổi trạng thái nghiệp vụ (`REMINDER_REPLY.STATUS` 0 / 1 / 2 / 3 / 4 / 5 giữ nguyên nghĩa). Chỉ cờ xóa mềm
đổi:

| Đối tượng | Hành động | Ai thực hiện | Điều kiện | Cột đổi | BR |
|---|---|---|---|---|---|
| Dòng đơn vị (`REMINDER_REPLY`) | Xóa một dòng / xóa nhiều / bỏ khi Sửa | Người tạo | Dòng hoạt động, thuộc nhắc việc mình tạo | `DEL_FLAG` 0 → 1, `UPDATED_BY`, `UPDATED_AT` | BR-04, BR-12 |
| Nhắc việc (`REMINDER`) + mọi dòng, người theo dõi, liên kết văn bản | Xóa dòng CT khi không còn CT khác | Người tạo | Sau khi xóa không còn dòng CT hoạt động | `DEL_FLAG` 0 → 1 trên tất cả | BR-05 |
| `DOCUMENT_IN_GROUP.HAS_REMINDER`, `DOCUMENT_IN_STAFF.HAS_REMINDER` của đơn vị bị xóa | (kéo theo) | Hệ thống | Đơn vị đó không còn nhắc việc hoạt động khác trên cùng văn bản | 1 → 0 (NULL) | BR-06 |

**Hành động bị cấm:** người không phải người tạo gọi xóa (web ẩn nút; máy chủ từ chối với thông báo hiện có
*"Đồng chí không có quyền thực hiện thao tác này"*).

## 3.3. Yêu cầu phi chức năng (NFR)

| Mã | Nhóm | Yêu cầu (đo được) |
|---|---|---|
| NFR-01 | Toàn vẹn dữ liệu | Xóa nhiều chạy trong **một giao dịch**: lỗi ở bất kỳ dòng nào → không dòng nào bị xóa (giả định — chờ TBD-01) |
| NFR-02 | Hiệu năng | Xóa tối đa một trang lưới (≤ 100 dòng theo cỡ trang hiện có) phản hồi ≤ 5 giây |
| NFR-03 | Nhật ký | Theo chuẩn hiện hành: `DEL_FLAG`, `UPDATED_BY`, `UPDATED_AT` trên dòng bị xóa; không thêm bảng lịch sử (Q10-A) |
| NFR-04 | Thông báo / SMS | Không gửi (Q06-A; nhắc việc hiện không gửi thông báo nào — LNV BR-22) |
| NFR-05 | Tương thích | Web (trình duyệt hiện hành). Di động: TBD-02 |

---

# 4. BUSINESS RULES `[A6]` · 🟨

| Rule ID | Tên rule | Mô tả | Nguồn |
|---|---|---|---|
| BR-01 | Đối tượng xóa là dòng đơn vị | Thao tác Xóa trên lưới tác động lên **một dòng đơn vị** (`REMINDER_REPLY`) được bấm / tick, xác định bằng `REMINDER_REPLY_ID`, không phải lên cả nhắc việc. | Phiếu ý tưởng; Q01 |
| BR-02 | Ai được xóa | Chỉ **người tạo** nhắc việc (`REMINDER.CREATED_BY` = người đăng nhập) thấy icon Xóa, thấy ô tick và được máy chủ chấp nhận; người khác bị từ chối ở cả web và máy chủ. Giữ nguyên hiện trạng. | Q02-A; LNV BR-08 |
| BR-03 | Trạng thái được xóa | Dòng ở **mọi trạng thái** (4 Lưu tạm · 0 Chưa trả lời · 5 Đã xử lý tạm · 1 Chờ duyệt · 2 Xử lý lại · 3 Hoàn thành) đều xóa được; không thêm điều kiện ẩn / hiện nút. Giữ nguyên hiện trạng. | Q03 |
| BR-04 | Xóa dòng PH | Khi dòng bị xóa có `ORG_ROLE = 2`: xóa mềm dòng đó **và** dòng sao (cùng `REMINDER_ID`, `ORG_ID`, `ORG_ROLE`, trạng thái 5) nếu có; xóa mềm liên kết văn bản trả lời (`REMINDER_DOCUMENT_RELATIONS` với `OBJECT_TYPE = 2`, `OBJECT_ID` = mã dòng bị xóa). **Không** đụng `REMINDER`, các dòng đơn vị khác, người theo dõi, liên kết văn bản giao (`OBJECT_TYPE = 1`). Văn bản trả lời (bản ghi `DOCUMENT`) không bị xóa. | Phiếu ý tưởng; Q06-A |
| BR-05 | Xóa dòng CT | Khi dòng bị xóa có `ORG_ROLE = 1`: (a) nếu sau khi xóa, nhắc việc **còn ≥ 1 dòng CT hoạt động** khác → xử lý đúng như BR-04; (b) nếu **không còn dòng CT hoạt động** → xóa toàn bộ nhắc việc như hiện nay: `REMINDER`, **mọi** dòng đơn vị còn lại (kể cả PH chưa được tick), người theo dõi, mọi liên kết văn bản; gỡ cờ theo mọi đơn vị. Vì web hiện chỉ cho một CT, trường hợp (a) chỉ xảy ra với dữ liệu có nhiều CT. | Q01-A + lưu ý của BA |
| BR-06 | Gỡ cờ "văn bản có nhắc việc" theo đơn vị | Sau khi xóa dòng của đơn vị X (BR-04, BR-05a, BR-12): với mỗi văn bản giao của nhắc việc, nếu đơn vị X **không còn** dòng đơn vị hoạt động nào của nhắc việc khác trên cùng văn bản và cùng đơn vị giao, thì gỡ `HAS_REMINDER` trên nhánh luồng văn bản đến bắt đầu từ dòng nhận của đơn vị X (cùng cách gỡ theo nhánh hiện có, trừ nhánh còn nhắc việc khác). Dòng nhận của các đơn vị khác không bị gỡ. Khi xóa toàn bộ (BR-05b): gỡ cho mọi đơn vị như hiện nay. | Q06-A; LNV NV-08 |
| BR-07 | Ô tick | Cột tick ở đầu lưới, hiện ở **cả hai nhóm** *Cần xử lý* và *Giao đi/Theo dõi*. Một dòng có ô tick **khi và chỉ khi** dòng đó đang hiện icon Xóa (BR-02). Dòng không có icon Xóa thì ô tick **không hiện**. Ô "chọn tất cả" ở tiêu đề chỉ tick các dòng có ô tick **trong trang hiện tại**; chuyển trang / tìm kiếm lại / đổi tab thì bỏ hết tick. | Q04 |
| BR-08 | Nút "Xóa N nhắc việc" | Nhãn **"Xóa N nhắc việc"** với N = số dòng đang tick; nút chỉ hiện khi N ≥ 1 (giả định — chờ TBD-03). Vị trí: phía trên lưới, bên trái, như ảnh design. | Ảnh design; Q08-B |
| BR-09 | Xóa nhiều | Bấm nút → một hộp xác nhận chung (BR-10) → máy chủ nhận **danh sách mã dòng** và áp BR-04 / BR-05 / BR-06 cho từng dòng **trong một giao dịch**. Nếu tập dòng tick làm một nhắc việc hết CT (BR-05b) thì nhắc việc đó bị xóa toàn bộ, kể cả dòng PH của nó không được tick. Máy chủ kiểm lại từng dòng: không phải người tạo hoặc dòng không còn hoạt động → **từ chối cả lô**, không xóa dòng nào (giả định — chờ TBD-01). | Q05 (BA chưa hiểu → TBD-01) |
| BR-10 | Câu xác nhận | Cả xóa một dòng lẫn xóa nhiều dùng câu chung hiện có *"Đồng chí có chắc chắn muốn xóa?"*, nút OK / Hủy; Hủy → không làm gì. | Q08-B |
| BR-11 | Không lý do, không thông báo | Không yêu cầu nhập lý do; không tạo thông báo, không gửi SMS cho đơn vị bị xóa hay người theo dõi. Vết chỉ gồm `DEL_FLAG = 1`, `UPDATED_BY`, `UPDATED_AT` trên các dòng bị xóa. | Q10-A; Q06-A |
| BR-12 | Bỏ đơn vị khi Sửa | Khi người tạo Sửa nhắc việc và bỏ một đơn vị PH khỏi danh sách rồi Lưu, dòng đơn vị đó được xử lý **đúng như BR-04 + BR-06** (hiện chỉ xóa mềm dòng, chưa gỡ cờ). Màn Sửa vẫn bắt buộc một CT nên không bỏ được CT qua đường này. | Q06-C |
| BR-13 | Xóa theo văn bản giữ nguyên | Xóa văn bản / dự thảo đang gắn nhắc việc vẫn xóa toàn bộ nhắc việc như hiện nay; không áp quy tắc theo dòng. | Q07-A |
| BR-14 | Sau khi xóa | Lưới tải lại theo bộ lọc hiện tại; số trên nhãn tab và ô trang chủ "Nhắc việc" được tính lại; mọi ô tick trở về không tick. Không có thông báo thành công (giữ hiện trạng xóa đơn — giả định, chờ TBD-03). | Hiện trạng `RVM:1653-1664` |

---

# 5. LUỒNG NGHIỆP VỤ / USE CASE `[A7]` · 🟨

## 5.1. UC-01 - Xóa một dòng đơn vị khỏi nhắc việc

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Gỡ một đơn vị khỏi nhắc việc mà không ảnh hưởng đơn vị khác |
| Actor | Người tạo nhắc việc |
| Tiền điều kiện | Đang ở lưới *Theo dõi nhắc việc*; dòng có icon Xóa (BR-02) |
| Trigger | Bấm icon thùng rác ở cột *Thao tác* của dòng |
| Hậu điều kiện | Dòng (và dòng sao) `DEL_FLAG = 1`; cờ "văn bản có nhắc việc" của đơn vị đó gỡ theo BR-06; hoặc cả nhắc việc bị xóa nếu rơi vào BR-05b |
| Rule liên quan | BR-01 … BR-06, BR-10, BR-11, BR-14 |
| Ngoại lệ liên quan | EC-01, EC-02, EC-03, EC-04, EC-05, EC-06, EC-11 |

**Luồng chính**

1. Người tạo bấm icon Xóa ở dòng đơn vị X.
2. Hệ thống hiện hộp *"Đồng chí có chắc chắn muốn xóa?"* (OK / Hủy).
3. Người tạo bấm OK.
4. Hệ thống gửi mã dòng (`REMINDER_REPLY_ID`) lên máy chủ; máy chủ kiểm người tạo và dòng còn hoạt động.
5. Nếu X là PH, hoặc X là CT mà nhắc việc còn CT khác: máy chủ xóa mềm dòng X + dòng sao + liên kết văn bản trả lời
   của X; gỡ cờ "văn bản có nhắc việc" của X (BR-04, BR-06).
6. Nếu X là CT và sau đó không còn CT: máy chủ xóa toàn bộ nhắc việc (BR-05b).
7. Hệ thống tải lại lưới, tính lại số đếm (BR-14).

**Luồng thay thế**

- 3a. Bấm Hủy → đóng hộp, không thay đổi gì.

**Luồng ngoại lệ**

- 4a. Không phải người tạo / dòng đã bị xóa trước đó → EC-01, EC-03.
- 5a. Lỗi máy chủ → EC-09: hoàn tác, báo *"Xóa nhắc việc thất bại, vui lòng thử lại!"*.

```mermaid
sequenceDiagram
  actor NT as Người tạo
  participant W as Web (lưới nhắc việc)
  participant BE as Máy chủ nhắc việc
  participant DB as CSDL
  NT->>W: Bấm Xóa ở dòng đơn vị X
  W-->>NT: "Đồng chí có chắc chắn muốn xóa?"
  NT->>W: OK
  W->>BE: xóa dòng (reminderReplyId)
  BE->>DB: kiểm người tạo, dòng hoạt động, vai trò X, số CT còn lại
  alt X là PH, hoặc CT nhưng còn CT khác
    BE->>DB: DEL_FLAG=1 dòng X (+ dòng sao), liên kết VB trả lời của X
    BE->>DB: gỡ HAS_REMINDER nhánh của X (nếu X không còn nhắc việc khác)
  else X là CT cuối cùng
    BE->>DB: DEL_FLAG=1 REMINDER + mọi dòng + người theo dõi + liên kết; gỡ cờ mọi đơn vị
  end
  BE-->>W: true
  W->>BE: tìm lại danh sách + số đếm
  W-->>NT: lưới đã cập nhật
```

## 5.2. UC-02 - Xóa nhiều dòng một lần

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Gỡ nhiều đơn vị (có thể thuộc nhiều nhắc việc) bằng một thao tác |
| Actor | Người tạo nhắc việc |
| Tiền điều kiện | Lưới có ≥ 1 dòng có ô tick (BR-07) |
| Trigger | Tick ≥ 1 dòng → bấm "Xóa N nhắc việc" |
| Hậu điều kiện | Mọi dòng tick xử lý theo BR-04 / BR-05 / BR-06 trong một giao dịch; lưới tải lại, bỏ tick |
| Rule liên quan | BR-07, BR-08, BR-09, BR-10, BR-14 |
| Ngoại lệ liên quan | EC-07, EC-08, EC-09, EC-10 |

**Luồng chính**

1. Người tạo tick từng dòng, hoặc tick ô "chọn tất cả" ở tiêu đề (chỉ dòng có ô tick trong trang).
2. Nút "Xóa N nhắc việc" hiện với N = số dòng đang tick.
3. Người tạo bấm nút → hộp *"Đồng chí có chắc chắn muốn xóa?"* → OK.
4. Web gửi danh sách mã dòng; máy chủ kiểm từng dòng (người tạo, còn hoạt động).
5. Máy chủ gom theo nhắc việc: với mỗi nhắc việc, nếu sau khi bỏ các dòng tick không còn CT hoạt động → xóa toàn bộ
   nhắc việc; ngược lại xóa mềm từng dòng tick + dòng sao + liên kết văn bản trả lời; gỡ cờ theo từng đơn vị.
6. Giao dịch thành công → web tải lại lưới, bỏ tick, tính lại số đếm.

**Luồng thay thế**

- 1a. Bỏ tick hết → nút ẩn (BR-08).
- 3a. Hủy → không làm gì, giữ nguyên tick.

**Luồng ngoại lệ**

- 4a. Có dòng không hợp lệ → từ chối cả lô (giả định — chờ TBD-01) → EC-10.
- 5a. Lỗi giữa chừng → hoàn tác toàn bộ → EC-09.

## 5.3. UC-03 - Bỏ đơn vị phối hợp khi Sửa nhắc việc

| Thuộc tính | Nội dung |
|---|---|
| Mục tiêu | Đường "Sửa" cho cùng kết quả với xóa dòng (BR-12) |
| Actor | Người tạo nhắc việc |
| Tiền điều kiện | Nút Sửa hiện (người tạo, dòng chưa Chờ duyệt / Hoàn thành — LNV BR-08) |
| Trigger | Bỏ đơn vị PH khỏi khối → Lưu |
| Hậu điều kiện | Như UC-01 với dòng PH |
| Rule liên quan | BR-12, BR-04, BR-06 |
| Ngoại lệ liên quan | EC-06 |

Luồng chính: giữ luồng Sửa hiện có (LNV NV-02); chỉ bước "đơn vị bị bỏ → xóa mềm" được nối thêm bước gỡ cờ (BR-06).

---

# 6. ĐẶC TẢ MÀN HÌNH VÀ TRƯỜNG DỮ LIỆU `[A8]` · 🟨

## 6.1. Màn hình Theo dõi nhắc việc — lưới "Danh sách nhắc việc"

![Xóa nhiều nhắc việc](input/design/01_xoa-nhieu-nhac-viec.png)

*Hình 1. Ảnh BA gửi: cột tick đầu lưới, nút đỏ "Xóa 1 nhắc việc" phía trên lưới (nhóm Cần xử lý, tab Chưa trả lời).*

| ID | Trường/Control | Loại | Bắt buộc | Độ dài / Giới hạn | Mặc định | Quy tắc hiển thị / Validate | Thay đổi trong YC_NV_01 |
|---|---|---|---|---|---|---|---|
| UI-01 | Ô tick từng dòng (cột đầu lưới) | Checkbox | Không | — | Không tick | Chỉ hiện khi dòng có icon Xóa (BR-07); tick → cập nhật N của UI-03 | **Mới** (bật lại checkbox đang comment) |
| UI-02 | Ô "chọn tất cả" (tiêu đề cột tick) | Checkbox | Không | — | Không tick | Tick → tick mọi UI-01 trong trang; bỏ tick một dòng → UI-02 tự bỏ tick; không có dòng nào tick được → ẩn / vô hiệu | **Mới** |
| UI-03 | Nút "Xóa N nhắc việc" | Nút (đỏ, icon thùng rác) | — | — | Ẩn | N = số dòng đang tick; hiện khi N ≥ 1 (TBD-03); bấm → MSG-01 | **Mới** |
| UI-04 | Icon Xóa ở cột *Thao tác* | Icon `fa-trash-o` | — | — | — | Hiện cho người tạo (BR-02); bấm → MSG-01 → xóa dòng (BR-04 / BR-05) | **Sửa** hành vi (xóa một dòng thay vì cả nhắc việc) |
| UI-05 | Icon Sửa ở cột *Thao tác* | Icon `fa-edit` | — | — | — | Giữ nguyên baseline; đường bỏ đơn vị PH thêm gỡ cờ (BR-12) | Sửa hành vi phía máy chủ |
| UI-06 | Các cột Số ký hiệu · Trích yếu · Nội dung giao việc · Đơn vị xử lý · Trạng thái · Số VB trả lời · Hạn xử lý · Ngày tạo · File văn bản | Cột lưới | — | — | — | Giữ nguyên baseline | Giữ nguyên |
| UI-07 | Tab / nhóm / bộ lọc / phân trang | — | — | — | — | Giữ nguyên baseline; chuyển trang, tab, tìm lại → bỏ tick (BR-07) | Giữ nguyên |

## 6.2. Thông báo người dùng

| Mã | Tình huống | Loại | Nội dung nguyên văn | Nút |
|---|---|---|---|---|
| MSG-01 | Bấm icon Xóa hoặc nút "Xóa N nhắc việc" | Popup xác nhận | "Đồng chí có chắc chắn muốn xóa?" (khóa `app.confirm.delete` hiện có) | OK / Hủy |
| MSG-02 | Máy chủ trả lỗi / từ chối | Toast lỗi | "Xóa nhắc việc thất bại, vui lòng thử lại!" (chuỗi hiện có) | — |
| MSG-03 | Không phải người tạo gọi API (chỉ xảy ra khi gọi ngoài giao diện) | Lỗi máy chủ | "Đồng chí không có quyền thực hiện thao tác này" (chuỗi hiện có) | — |
| MSG-04 | Xóa thành công | Không có thông báo; lưới tải lại (giữ hiện trạng xóa đơn) | — (TBD-03 nếu BA muốn thêm *"Đã xóa N nhắc việc"*) | — |

Lưu ý (rủi ro đã chấp nhận ở Q08-B): hộp xác nhận **không** phân biệt dòng CT và PH; người dùng xóa dòng CT cuối cùng
sẽ không được báo trước rằng các dòng PH chưa tick cũng mất (EC-08).

## 6.3. Điều hướng

Không áp dụng — không đổi điều hướng; sau xóa ở lại đúng nhóm / tab / trang hiện tại.

## 6.4. Quy tắc hiển thị

- UI-01 và UI-04 luôn cùng hiện / cùng ẩn trên một dòng (BR-07).
- UI-03 ở cùng hàng với tiêu đề "Danh sách nhắc việc", căn trái, trước chú giải "Quá hạn / Trong hạn" (ảnh design).
- Nhãn UI-03 cập nhật tức thì khi tick / bỏ tick, không cần tải lại lưới.

---

# 7. XỬ LÝ NGOẠI LỆ VÀ TRƯỜNG HỢP BIÊN `[A9]` · 🟨

| ID | Tình huống | Kết quả mong đợi | UC | Trạng thái |
|---|---|---|---|---|
| EC-01 | Dòng đã bị xóa (bởi chính mình ở tab khác, hoặc nhắc việc đã bị xóa theo văn bản) rồi mới bấm Xóa | Máy chủ trả lỗi; web hiện MSG-02 và tải lại lưới (dòng biến mất) | UC-01 | Đã chốt |
| EC-02 | Bấm OK hai lần nhanh / gửi trùng | Lần sau gặp dòng đã `DEL_FLAG = 1` → như EC-01; không xóa thêm gì | UC-01 | Đã chốt |
| EC-03 | Gọi API xóa với mã dòng của nhắc việc người khác tạo | Từ chối, MSG-03, không thay đổi dữ liệu | UC-01 | Đã chốt |
| EC-04 | Đơn vị bị xóa đang có dòng sao *Đã xử lý tạm* (5) | Cả dòng gốc và dòng sao cùng `DEL_FLAG = 1` (BR-04) | UC-01 | Đã chốt |
| EC-05 | Đơn vị bị xóa đã trả lời kèm văn bản trả lời (Chờ duyệt / Hoàn thành) | Dòng và liên kết văn bản trả lời xóa mềm; văn bản trả lời (`DOCUMENT`) không bị xóa; nhắc việc không đổi trạng thái các đơn vị khác | UC-01 | Đã chốt (Q03 giữ hiện trạng) |
| EC-06 | Đơn vị bị xóa còn một nhắc việc khác hoạt động trên cùng văn bản (cùng đơn vị giao) | Không gỡ cờ "văn bản có nhắc việc" của đơn vị đó (BR-06) | UC-01, UC-03 | Đã chốt |
| EC-07 | Tick ở trang 1, chuyển sang trang 2 rồi bấm nút | Chuyển trang đã bỏ tick → nút ẩn; chỉ xóa được dòng tick trong trang hiện tại (BR-07) | UC-02 | Đã chốt |
| EC-08 | Tick dòng CT (cuối cùng) nhưng không tick các PH cùng nhắc việc | Cả nhắc việc bị xóa, các PH chưa tick cũng mất (BR-05b, BR-09); hộp xác nhận không cảnh báo riêng (Q08-B) | UC-02 | Đã chốt |
| EC-09 | Lỗi CSDL giữa chừng khi xóa nhiều | Hoàn tác toàn bộ, MSG-02, không dòng nào bị xóa | UC-02 | Giả định — TBD-01 |
| EC-10 | Trong lô tick có dòng vừa bị xóa bởi thao tác khác (không còn hoạt động) | Từ chối cả lô, MSG-02, tải lại lưới | UC-02 | Giả định — TBD-01 |
| EC-11 | Dữ liệu có nhắc việc với ≥ 2 dòng CT (tạo ngoài web) | Xóa một CT khi còn CT khác → chỉ xóa dòng đó (BR-05a) | UC-01 | Đã chốt (lưu ý Q01) |
| EC-12 | Dòng ở trạng thái Lưu tạm (4) chỉ hiện khi lọc "Chưa hoàn thành" ở nhóm theo dõi | Vẫn có icon Xóa và ô tick nếu là người tạo; xóa như dòng khác (BR-03) | UC-01, UC-02 | Đã chốt |
| EC-13 | Không có dòng nào tick được trong trang (toàn nhắc việc người khác tạo) | Không có ô tick nào, UI-02 ẩn / vô hiệu, UI-03 ẩn | UC-02 | Đã chốt |

---

# 8. ACCEPTANCE CRITERIA `[A10]` · 🟨

| AC ID | BR | Given | When | Then |
|---|---|---|---|---|
| AC-01 | BR-01, BR-04 | Nhắc việc R1 do A tạo, giao CT = Sở X, PH = Sở Y, Sở Z; A đăng nhập, mở *Giao đi/Theo dõi* | A bấm Xóa ở dòng Sở Y, OK | Lưới còn 2 dòng của R1 (Sở X CT, Sở Z PH); `REMINDER_REPLY` của Sở Y có `DEL_FLAG = 1`; `REMINDER` R1 `DEL_FLAG = 0`; người theo dõi của R1 không đổi |
| AC-02 | BR-05 (b) | R1 như AC-01 (1 CT) | A bấm Xóa ở dòng Sở X (CT), OK | `REMINDER` R1 và cả 3 dòng đơn vị `DEL_FLAG = 1`; người theo dõi, liên kết văn bản của R1 `DEL_FLAG = 1`; lưới không còn dòng nào của R1 |
| AC-03 | BR-05 (a) | Nhắc việc R2 có 2 dòng CT (Sở X, Sở V) + 1 PH (tạo bằng dữ liệu kiểm thử) | A bấm Xóa ở dòng Sở X, OK | Chỉ dòng Sở X `DEL_FLAG = 1`; R2 và dòng Sở V, dòng PH giữ nguyên |
| AC-04 | BR-02 | Người B không phải người tạo R1, là lãnh đạo theo dõi của R1 | B mở lưới | Dòng của R1 không có icon Xóa, không có ô tick; gọi API xóa dòng R1 bằng tài khoản B → MSG-03, dữ liệu không đổi |
| AC-05 | BR-03 | Dòng Sở Z của R1 đang *Hoàn thành* (3) | A bấm Xóa ở dòng Sở Z, OK | Dòng Sở Z `DEL_FLAG = 1`, liên kết văn bản trả lời của dòng đó `DEL_FLAG = 1`; văn bản trả lời vẫn tồn tại |
| AC-06 | BR-04 (dòng sao) | Dòng Sở Y của R1 có thêm dòng sao trạng thái 5 | A xóa dòng Sở Y | Cả hai dòng của Sở Y `DEL_FLAG = 1` |
| AC-07 | BR-06 | Văn bản D giao R1; Sở Y chỉ có R1 trên D; `DOCUMENT_IN_GROUP.HAS_REMINDER = 1` ở dòng nhận của Sở Y và Sở X | A xóa dòng Sở Y | Dòng nhận của Sở Y (và nhánh chuyển tiếp của nó) `HAS_REMINDER` = 0 / NULL; dòng nhận của Sở X vẫn = 1 |
| AC-08 | BR-06 (EC-06) | Sở Y còn nhắc việc R3 hoạt động trên cùng văn bản D, cùng đơn vị giao | A xóa dòng Sở Y của R1 | Dòng nhận của Sở Y vẫn `HAS_REMINDER = 1` |
| AC-09 | BR-07 | Trang hiện tại có 5 dòng: 3 của nhắc việc A tạo, 2 của người khác | A xem lưới | Chỉ 3 dòng có ô tick; tick ô "chọn tất cả" → đúng 3 dòng được tick, nút hiện "Xóa 3 nhắc việc" |
| AC-10 | BR-07 | A đã tick 2 dòng ở trang 1 | A chuyển sang trang 2 | Không dòng nào tick; nút "Xóa N nhắc việc" ẩn |
| AC-11 | BR-08 | A tick 1 dòng rồi bỏ tick | — | Nhãn nút lần lượt "Xóa 1 nhắc việc" rồi nút ẩn |
| AC-12 | BR-09, BR-10 | A tick dòng Sở Y của R1 và dòng PH của nhắc việc R4 (A tạo) | A bấm "Xóa 2 nhắc việc", OK ở "Đồng chí có chắc chắn muốn xóa?" | Hai dòng đó `DEL_FLAG = 1`; R1, R4 và các dòng khác giữ nguyên; lưới tải lại, không còn tick |
| AC-13 | BR-09 (BR-05b) | A tick dòng Sở X (CT duy nhất của R1), không tick Sở Y, Sở Z | A bấm "Xóa 1 nhắc việc", OK | R1 và cả 3 dòng `DEL_FLAG = 1` (Sở Y, Sở Z mất theo) |
| AC-14 | BR-09 (giả định — chờ TBD-01) | A tick 3 dòng; một trong ba vừa bị xóa bởi thao tác khác | A bấm "Xóa 3 nhắc việc", OK | Không dòng nào bị xóa; MSG-02; lưới tải lại |
| AC-15 | BR-10 | A bấm icon Xóa | Hộp xác nhận hiện | Nội dung đúng "Đồng chí có chắc chắn muốn xóa?"; bấm Hủy → không có dòng nào đổi `DEL_FLAG` |
| AC-16 | BR-11 | A xóa dòng Sở Y | — | Không có dòng `NOTIFICATION`, `MESSAGE`, `SMS_MASTER` mới liên quan; dòng Sở Y có `UPDATED_BY` = A, `UPDATED_AT` = thời điểm xóa |
| AC-17 | BR-12 | R1 chưa có đơn vị nào trả lời; Sở Y chỉ có R1 trên văn bản D | A bấm Sửa R1, bỏ Sở Y khỏi đơn vị phối hợp, Lưu | Dòng Sở Y `DEL_FLAG = 1`; `HAS_REMINDER` dòng nhận của Sở Y = 0 / NULL; Sở X, Sở Z không đổi |
| AC-18 | BR-13 | Văn bản D có nhắc việc R1 (3 đơn vị) | Người có quyền xóa văn bản D | R1 và mọi dòng của nó `DEL_FLAG = 1` (như hiện nay) |
| AC-19 | BR-14 | Tab *Chưa hoàn thành* nhóm theo dõi đang đếm 5 | A xóa 1 dòng *Chưa trả lời* | Số trên tab giảm còn 4; ô "Chưa hoàn thành" trên trang chủ cũng 4 sau khi tải lại trang chủ |

---

# 9. MA TRẬN KIỂM THỬ VÀ TRUY VẾT `[A11]` · 🟩

## 9.1. Ma trận role kiểm thử

| Vai trò nghiệp vụ | Mã vai trò hệ thống | Mục tiêu kiểm thử |
|---|---|---|
| Người tạo nhắc việc (chuyên viên ở đơn vị ban hành) | `NV` (tạo bằng văn bản mình trình) | Functional đầy đủ UC-01, UC-02, UC-03 |
| Người tạo là Văn thư / Lãnh đạo đơn vị ban hành | `VT`, `LDDV` | Functional lặp lại AC-01, AC-02, AC-12 |
| Lãnh đạo theo dõi, chuyên viên theo dõi | `LDDV`, `NV` | Regression phân quyền: không có nút / ô tick (AC-04) |
| Văn thư / Lãnh đạo đơn vị được nhắc | `VT`, `LDDV`, `TTDV` | Sau khi dòng bị xóa: không còn thấy ở *Cần xử lý*; số "văn bản có nhắc việc" trên hộp văn bản đến giảm; Hoàn thành văn bản đến không còn bị chặn bởi nhắc việc đã xóa |

## 9.2. Traceability Requirement → Rule → AC

| FR | BR | AC | EC | Ghi chú |
|---|---|---|---|---|
| FR-01 | BR-01, BR-02, BR-03, BR-04, BR-06, BR-10, BR-11, BR-14 | AC-01, AC-04, AC-05, AC-06, AC-07, AC-08, AC-15, AC-16, AC-19 | EC-01 … EC-06, EC-12 | |
| FR-02 | BR-05, BR-06 | AC-02, AC-03 | EC-11 | |
| FR-03 | BR-07, BR-08, BR-09, BR-10, BR-14 | AC-09 … AC-14 | EC-07 … EC-10, EC-13 | AC-14 chờ TBD-01 |
| FR-04 | BR-12 | AC-17 | EC-06 | |
| FR-05 | BR-13 | AC-18 | — | Regression |

## 9.3. Regression tối thiểu

- Tạo / sửa / trả lời / duyệt / trả lại / hủy trả lời / nhắc lại / chuyển xử lý nhắc việc không đổi.
- Nhắc việc soạn trên dự thảo, giao khi chuyển văn bản, đổi đơn vị giao khi ban hành (LNV NV-03) không đổi.
- Hoàn thành văn bản đến: chặn / buộc trả lời / tự duyệt theo nhắc việc còn hoạt động (LNV NV-09); nhắc việc đã xóa
  dòng không còn chặn.
- Số đếm widget trang chủ "Nhắc việc" và báo cáo nhắc việc chỉ đếm dòng hoạt động.
- Quyền xóa không mở rộng cho người theo dõi / đơn vị được nhắc.
- Xóa văn bản / dự thảo vẫn xóa toàn bộ nhắc việc.

---

# 10. PHẠM VI KỸ THUẬT, KIẾN TRÚC VÀ MAPPING CSDL `[A12]` · 🟩

## 10.1. Quy tắc nguồn sự thật

| Thứ tự | Nguồn | Dùng để xác định | Khi mâu thuẫn |
|---|---|---|---|
| 1 | Tài liệu này | WHAT/WHY, phạm vi, BR, AC | Không sửa BR bằng suy luận kỹ thuật |
| 2 | `knowledge/lich-nhac-viec/` | Hành vi cũ, mapping đã kiểm chứng | Dùng làm OLD behavior + regression |
| 3 | Source code `kha_develop` | Control-flow, binding, service, DTO | Trace end-to-end |
| 4 | DB DEV (chỉ SELECT) | Bảng / cột / dữ liệu thật | Phiên này **không kết nối được DB DEV** (không có `.env`) → mọi dòng về DB lấy từ ảnh chụp DB DEV 2026-10-01 trong `knowledge/` hoặc từ entity / SQL migration |

**Quy ước riêng:** "mã dòng" = `REMINDER_REPLY.REMINDER_REPLY_ID`; "mã nhắc việc" = `REMINDER.REMINDER_ID`. Lưới hiện
**chưa trả về mã dòng** (`RRI:31-70` chọn `r.REMINDER_ID`, `rr.STATUS`, `rr.ORG_ROLE`, không chọn `rr.REMINDER_REPLY_ID`).

## 10.2. Call-chain

| Layer | Thành phần | Vai trò với YC_NV_01 | Độ tin cậy |
|---|---|---|---|
| UI/ZK | `ZUL` (`reminder_search.zul:315-346`) | Bật lại checkbox `:320-322`, `:336-338`; thêm nút "Xóa N nhắc việc" (có thể đặt cạnh div 3 nút ẩn `:312-316`); icon Xóa `:344-346` gửi thêm mã dòng | VERIFIED_CODE |
| ViewModel | `RVM` | `checkVisibleDelButton :2446-2448` (giữ); `doCheckItem / doCheckAll / doClearSelection :1196-1240` (có sẵn, dùng lại); `delete :1653-1664` (đổi sang gửi mã dòng); thêm lệnh xóa nhiều gom `selected` → danh sách mã dòng; `reloadReminderList :2147-2155` | VERIFIED_CODE |
| Model web | `web-spring/src/main/java/com/viettel/voffice/entity/Reminder.java` | Thêm trường `reminderReplyId` (cột `selected` đã có) | VERIFIED_CODE (cần sửa) |
| Business web | `RB.deleteReminder :419-432` (đổi payload); `RB.deleteReminders :384-404` (đang trỏ `reminders.delete`, sửa trỏ endpoint mới hoặc gộp) | Gọi BE | VERIFIED_CODE |
| Endpoint BE | `RC:79-88 POST /reminders/delete` (nhận `reminderId`) | Đổi thành nhận `reminderReplyId`, hoặc thêm endpoint mới nhận `reminderReplyIds` (danh sách) dùng cho cả xóa đơn (1 phần tử) và xóa nhiều | VERIFIED_CODE |
| Service BE | `RSI.deleteReminder :1288-1334` (xóa cả nhắc việc — giữ làm nhánh BR-05b); `clearReminderFlagsForBranches :1336-1398` (gỡ cờ theo nhánh — dùng lại với `receiverOrgIds` = 1 đơn vị); `syncReminderReplies :1133-1149` (bỏ đơn vị khi Sửa → gọi thêm gỡ cờ, BR-12) | Logic BR-04 … BR-06, BR-09, BR-12 | VERIFIED_CODE |
| Repository BE | `RRRJ.deleteByIds :21-22`, `findActiveByReminderId :17-18`, `deleteByReminderId :41-42`; `ReminderDocumentRelationRepositoryJPA.deleteByObjectIdAndObjectType` (đã dùng ở `RSI:1127-1130`); `DocumentInGroupRepositoryJPA.findActiveReminderRootIds :348-350` (nhận danh sách đơn vị nhận) | Có sẵn, đủ để làm | VERIFIED_CODE |
| DB | `REMINDER`, `REMINDER_REPLY`, `REMINDER_FOLLOWERS`, `REMINDER_DOCUMENT_RELATIONS`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF`, `DOCUMENT_PROCESS` | Chỉ UPDATE cột có sẵn | VERIFIED_BASELINE (ảnh chụp DB DEV 2026-10-01) |

## 10.3. Bảng/cột liên quan

| Bảng | Mục đích | Cột chính liên quan | Thay đổi | Độ tin cậy |
|---|---|---|---|---|
| `REMINDER` | Nhắc việc | `REMINDER_ID`, `CREATED_BY`, `ORG_ID` (đơn vị giao), `DEL_FLAG`, `UPDATED_BY`, `UPDATED_AT` | Không — chỉ UPDATE khi BR-05b | VERIFIED_BASELINE |
| `REMINDER_REPLY` | Dòng đơn vị | `REMINDER_REPLY_ID`, `REMINDER_ID`, `ORG_ID`, `ORG_ROLE` (1 CT / 2 PH), `STATUS`, `DEL_FLAG`, `UPDATED_BY`, `UPDATED_AT` | Không — UPDATE `DEL_FLAG` | VERIFIED_BASELINE |
| `REMINDER_FOLLOWERS` | Người theo dõi | `REMINDER_ID`, `DEL_FLAG` | Không — chỉ khi BR-05b | VERIFIED_BASELINE |
| `REMINDER_DOCUMENT_RELATIONS` | Liên kết văn bản giao (`OBJECT_TYPE = 1`, `OBJECT_ID` = mã nhắc việc) / văn bản trả lời (`OBJECT_TYPE = 2`, `OBJECT_ID` = mã dòng) | `OBJECT_TYPE`, `OBJECT_ID`, `DOCUMENT_ID`, `DEL_FLAG` | Không — xóa mềm **phải lọc `OBJECT_TYPE`** (tránh lỗi L6 trong `dac-thu`) | VERIFIED_BASELINE |
| `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_STAFF` | Dòng nhận văn bản đến | `HAS_REMINDER`, `SECRETARY_GROUP_ID` | Không — UPDATE `HAS_REMINDER` theo nhánh | VERIFIED_BASELINE |
| `DOCUMENT_PROCESS` | Cây chuyển văn bản (để tìm nhánh gỡ cờ) | `DOCUMENT_PROCESS_ID`, `IN_GROUP_ID`, `IN_STAFF_ID` | Không | VERIFIED_CODE |

**Không cần migration.**

## 10.4. Mapping UI → Code → DTO/API → CSDL

| UI ID | Field UI | ZUL / VM / Command | Payload / API | DB đích | Ghi chú |
|---|---|---|---|---|---|
| UI-01 | Ô tick dòng | `ZUL:336-338` → `data.selected`, `@command('doCheckItem')` | — | — | Bật lại; chỉ render khi `vm.checkVisibleDelButton(data)` |
| UI-02 | Chọn tất cả | `ZUL:320-322` → `vm.selectAll`, `doCheckAll` | — | — | Bật lại; chỉ tick dòng có ô tick |
| UI-03 | Nút "Xóa N nhắc việc" | ZUL mới → lệnh mới trong RVM (gom `selected` → `reminderReplyIds`) → `RB` | `POST /reminders/delete-replies` (đề xuất tên) `{ reminderReplyIds: [...] }` | `REMINDER_REPLY.DEL_FLAG` (+ `REMINDER*` khi BR-05b; `HAS_REMINDER`) | Endpoint mới; `RB.deleteReminders` hiện gửi `reminderIds` + `reason` tới `reminders.delete` — sửa lại |
| UI-04 | Icon Xóa dòng | `ZUL:344-346` → `doDelete` → `RVM.delete :1653` → `RB.deleteReminder :419` | Cùng endpoint UI-03 với 1 phần tử (hoặc `/reminders/delete` đổi payload sang `reminderReplyId`) | như trên | Hộp xác nhận chung của `CommonVM.doDelete :1455` giữ nguyên |
| UI-05 | Sửa → bỏ đơn vị | `RVM.buildSaveRequest :736-806` → `RB.saveReminders` → `POST /reminders/insertOrUpdate` → `RSI.syncReminderReplies :1133-1149` | không đổi payload | `REMINDER_REPLY.DEL_FLAG` + `HAS_REMINDER` | Thêm gọi gỡ cờ sau `replyRepo.deleteByIds` |

## 10.5. CRUD và lifecycle dữ liệu

| Action | Trên giao diện (chưa lưu) | Khi lưu | Khi hủy | Điểm cần xác nhận |
|---|---|---|---|---|
| Tick / bỏ tick | Chỉ trong bộ nhớ trang (`Reminder.selected`) | — | Chuyển trang / tab / tìm lại → mất tick | — |
| Xóa một dòng | Hộp xác nhận | Xóa mềm dòng (+ dòng sao) + liên kết VB trả lời; gỡ cờ; hoặc xóa toàn bộ nhắc việc (BR-05b). Một giao dịch | Không đổi | Xóa mềm (`DEL_FLAG`) — đã chốt |
| Xóa nhiều | Hộp xác nhận | Như trên cho từng dòng, một giao dịch, tất cả hoặc không | Không đổi | TBD-01 |
| Bỏ đơn vị khi Sửa | Danh sách đơn vị trên form | Xóa mềm dòng + gỡ cờ | Đóng form → không đổi | — |

## 10.6. Phạm vi KHÔNG thay đổi và regression bắt buộc

| Hạng mục baseline | Có thay đổi? | Yêu cầu |
|---|---|---|
| Điều kiện hiện icon Xóa / Sửa (`RVM:2446-2452`) | Không | Giữ nguyên |
| Truy vấn lưới `RRI.searchReminders :31-209` | Chỉ thêm cột `rr.REMINDER_REPLY_ID` | Không đổi điều kiện lọc |
| Số đếm `RRJ.getDashboardCountsV2 :143-268` | Không | Đã lọc `DEL_FLAG` — xác nhận lại khi kiểm thử AC-19 |
| `RSI.deleteRemindersByDocumentIdOrTextId :1794-1871` | Không | BR-13 |
| `RSI.saveDraftReminders`, `saveDocumentReminders` | Không | Đường lưu cùng dự thảo / văn bản giữ nguyên |
| Màn chi tiết nhắc việc, tab nhắc việc trong chi tiết văn bản | Không | Không thêm nút Xóa (Q07-A) |

## 10.7. Ràng buộc triển khai

- Không thay đổi schema DB.
- Xóa mềm liên kết văn bản trả lời phải lọc `OBJECT_TYPE = 2` theo mã dòng (không dùng `deleteByObjectId(reminderId)`
  trần — xem `dac-thu` L6).
- Khi xóa toàn bộ nhắc việc (BR-05b) dùng lại đúng nhánh `RSI.deleteReminder` hiện có để không lệch hành vi gỡ cờ.
- Gỡ cờ theo đơn vị: gọi `findActiveReminderRootIds(documentIds, senderOrgId, [orgX])` rồi
  `clearReminderFlagsForBranches` — hàm này đã loại nhánh còn nhắc việc khác (EC-06).
- Xóa nhiều: một `@Transactional`; kiểm toàn bộ trước khi ghi (TBD-01).
- Web: `Reminder` model thêm `reminderReplyId`; lưới phải mang mã dòng về từ `RRI`.

## 10.8. Quy tắc cho AI/DEV khi đọc tài liệu này

| Rule ID | Quy tắc |
|---|---|
| AI-01 | Không suy tên bảng/cột từ tên class, DTO hay nhãn UI. |
| AI-02 | Không tự bịa bảng/cột/API/method/business rule — thiếu bằng chứng ghi `TBD_NOT_CONFIRMED`. |
| AI-03 | Mỗi field phải trace được UI → ZUL → VM → DTO → backend → DAO → DB, kèm `file::hàm::dòng`. |
| AI-04 | Tài liệu và code mâu thuẫn → ghi `CONFLICT` + đề xuất, chờ xác nhận, không tự chọn. |
| AI-05 | "Xóa" trong tài liệu này luôn là **xóa theo dòng đơn vị**; chỉ BR-05b và BR-13 xóa cả nhắc việc. Không dùng `deleteReminder(reminderId)` cho thao tác trên lưới trừ nhánh BR-05b. |

**Quality gate trước khi DEV code:** TBD-01 (cách xử lý lô khi có dòng lỗi) và TBD-02 (phạm vi di động) phải chốt.
Chưa chốt → trạng thái tài liệu = DRAFT_PENDING_CONFIRMATION.

---

# 11. CÁC ĐIỂM CẦN XÁC NHẬN (TBD) `[A13]` · 🟨

| Mã TBD | Câu hỏi cần chốt | Ảnh hưởng BR/AC/EC | Mức | Ai chốt | Hạn | Kết luận |
|---|---|---|---|---|---|---|
| TBD-01 | **Xóa nhiều gặp dòng lỗi thì sao?** (BA trả lời "chưa hiểu" ở Q05 — diễn giải lại bằng ví dụ:) BA tick 3 dòng rồi bấm "Xóa 3 nhắc việc". Giả sử 1 trong 3 dòng **vừa bị xóa bởi người khác** / bị lỗi lúc ghi. Chọn: **A.** không xóa dòng nào cả, báo lỗi, BA tick lại (tài liệu đang giả định A) · **B.** xóa 2 dòng còn lại, báo "1 dòng không xóa được". Ngoài ra khi tick dòng CT cuối cùng mà không tick các PH cùng nhắc việc, tài liệu đang ghi: **cả nhắc việc mất, PH chưa tick cũng mất** (EC-08) — BA xác nhận đúng ý không? | BR-09, NFR-01, AC-13, AC-14, EC-08, EC-09, EC-10 | BLOCKING | BA | | (chưa chốt) |
| TBD-02 | BA chọn Q09-B "web và di động", nhưng mã nguồn cho thấy **ứng dụng di động hiện không có màn nhắc việc** (không API di động nào gọi nhắc việc). "Làm cả di động" nghĩa là **xây mới** nhắc việc trên di động — một yêu cầu riêng, lớn hơn YC_NV_01 nhiều. Chọn: **A.** YC_NV_01 chỉ làm web; nhắc việc trên di động mở yêu cầu khác (tài liệu đang giả định A) · **B.** gộp vào đây và nâng cỡ L (cần thêm đặc tả màn di động) | Mục 1.4, NFR-05 | BLOCKING (phần di động) | BA / chủ dự án | | (chưa chốt) |
| TBD-03 | Nút "Xóa N nhắc việc" khi chưa tick dòng nào: **ẩn** (giả định) hay hiện mờ "Xóa 0 nhắc việc"? Và xóa xong có cần toast *"Đã xóa N nhắc việc"* không (hiện xóa đơn không có toast)? | BR-08, BR-14, UI-03, MSG-04, AC-11 | NON-BLOCKING | BA | | (chưa chốt) |
| TBD-04 | Tên endpoint mới (`/reminders/delete-replies`) hay đổi payload endpoint cũ; có giữ `RB.deleteReminders` hay gộp — quyết định kỹ thuật | 10.2, 10.4 | NON-BLOCKING | DEV | | (chưa chốt) |

**Tiêu chí bàn giao DEV:** chốt TBD-01 và TBD-02; TBD-03, TBD-04 có thể chốt trong lúc code.

---

# KẾT LUẬN

YC_NV_01 đổi thao tác Xóa trên lưới *Theo dõi nhắc việc* từ "xóa cả nhắc việc" thành "xóa một dòng đơn vị", với quy
tắc: xóa PH hay CT đều chỉ mất dòng đó, riêng khi nhắc việc không còn CT thì xóa toàn bộ; thêm cột tick và nút "Xóa N
nhắc việc" để xóa nhiều trong một giao dịch; đường *Sửa* bỏ đơn vị cũng gỡ cờ "văn bản có nhắc việc" như xóa dòng.
Quyền (chỉ người tạo), điều kiện hiện nút, câu xác nhận, không lý do / không thông báo, và xóa theo văn bản đều giữ
nguyên hiện trạng. Không thêm bảng / cột; cần một endpoint nhận danh sách mã dòng và lưới phải trả thêm mã dòng. Còn
hai điểm chặn: cách xử lý lô khi có dòng lỗi (TBD-01) và phạm vi ứng dụng di động (TBD-02). Chốt xong và BA đọc các
mục 🟦 🟨 → gọi `/ba-assistant kiem YC_NV_01`.
