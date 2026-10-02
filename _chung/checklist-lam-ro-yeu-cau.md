# Checklist làm rõ yêu cầu — Văn phòng số (dùng cho BA và AI)

> Bộ câu hỏi rút từ đợt viết lại tri thức 2026-10: đây là những chỗ yêu cầu mới **hay bị bỏ sót** và về sau phải hỏi
> lại DEV. Khi soạn đặc tả (`docs/templates/ba-spec.template.md`), AI duyệt từng nhóm, **chỉ giữ câu liên quan** tới yêu
> cầu, viết lại bằng ngữ cảnh cụ thể rồi đưa vào mục A13 (kèm lựa chọn để BA chọn). Mỗi câu có trỏ tri thức để AI
> tra hiện trạng trước khi hỏi — không hỏi điều tri thức đã trả lời.
>
> Ngoài checklist chung này, luôn xem thêm mục **"10. Khi viết yêu cầu mới…"** trong `tom-tat.md` và mục **7.1** trong
> `nghiep-vu.md` của phân hệ bị đụng.

## 1. Kênh và môi trường

- [ ] Áp dụng cho **web, ứng dụng di động, hay cả hai**? Mobile có phát hành riêng không? (`tich-hop` NV-11)
- [ ] Có ảnh hưởng **site Internet và site nội bộ** không — dữ liệu đồng bộ giữa hai site? (`tich-hop` NV-13)
- [ ] Có đơn vị nào được **bật / tắt riêng** tính năng (danh sách trắng menu theo đơn vị, tham số theo đơn vị)?
  (`he-thong` NV-03)

## 2. Đơn vị và người nhận

- [ ] Áp dụng cho **văn bản đơn vị** (văn thư nhận rồi phân phối) hay **văn bản cá nhân** (gửi thẳng người)?
  (`van-ban/den` NV-01, `van-ban/chuyen-van-ban`)
- [ ] Phạm vi đơn vị: chỉ đơn vị mình / **đơn vị con** (mấy cấp) / **đơn vị cha** / ngang cấp / toàn tỉnh?
- [ ] Vai trò nhận: **Chủ trì / Phối hợp / Nhận để biết / Nắm tình hình** — áp dụng cho vai trò nào? (thuật ngữ
  `SEND_TYPE`, `_chung/thuat-ngu.md`)
- [ ] Người trong danh sách **"không nhận văn bản khi chuyển cho đơn vị"** có bị loại không? (`he-thong` NV-15)
- [ ] **Trợ lý / thư ký lãnh đạo** có nhận thay, có nhận thông báo kèm không? (`hop` NV-08, `van-ban/den` NV-16)
- [ ] Một văn bản **nhiều Chủ trì** thì xử lý thế nào (đã xác nhận: được nhiều Chủ trì)?

## 3. Vai trò và quyền

- [ ] Vai trò nào được thấy **menu**, vai trò nào thấy **nút**, ở **trạng thái** nào? (quyền = menu theo vai trò +
  điều kiện hiện nút; BE không kiểm người gọi — `he-thong` NV-03, NV-09)
- [ ] Văn thư (`VT`), lãnh đạo (`LDDV`), thủ trưởng (`TTDV`), chuyên viên (`NV`), lưu trữ (`LT`), quản lý lịch
  (`QLLH`)… — vai trò nào thật sự liên quan?
- [ ] Quản trị toàn tỉnh (`ADMIN`) hay quản trị đơn vị (`ADMIN_LEVEL1`) được cấu hình? (`he-thong` NV-06)
- [ ] Người được **ủy quyền / ký thay / thay người dự họp** có được làm thay không? (`ky-so` NV-14, `hop` NV-07)

## 4. Vòng đời và trạng thái

- [ ] Áp dụng ở **trạng thái nào** của đối tượng (dự thảo, chờ ký, đã cấp số, đã ban hành, chờ xử lý, đã hoàn
  thành…)? Ghi bằng **tên hiển thị + giá trị số** (`tom-tat.md` §5 của phân hệ).
- [ ] Khi **trả lại / thu hồi / hủy ban hành / hủy luồng / trình ký lại** thì dữ liệu mới xử lý thế nào?
- [ ] Hoàn thành có **lan** lên người chuyển / đơn vị cha không? (`van-ban/den` NV-08)
- [ ] Có thêm **trạng thái mới** không? Nếu có: ai chuyển, điều kiện, chuyển sang đâu, hiện ở hộp / tab nào, widget
  trang chủ có đếm không?

## 5. Liên thông và hệ thống ngoài

- [ ] Văn bản **liên thông** (trục cơ quan ngoài / VOConnect / VPCP) có áp dụng không? (`van-ban/lien-thong`)
- [ ] Có hệ thống ngoài nào **đọc / ghi** dữ liệu này (Thư viện điện tử, phần mềm số hóa, KNTC, eCabinet…)? Cần báo
  kết quả cho họ không? (`tich-hop` NV-01, mục 1.6)
- [ ] Có phải **gửi trạng thái ngược** lên trục (đã nhận, từ chối, hoàn thành) không?

## 6. Hạn xử lý, nhắc việc, thông báo, SMS

- [ ] Có **hạn xử lý** không? Nhập tay hay tự tính? Tính ngày làm việc hay ngày lịch? "Sắp đến hạn" là mấy ngày?
  (`van-ban/den` NV-12)
- [ ] Có tạo **nhắc việc** không (lưu ý: nhắc việc hiện không tự gửi SMS / thông báo — `lich-nhac-viec`)?
- [ ] Gửi **thông báo trong ứng dụng** / **SMS** / **email** cho ai, khi nào, **nội dung nguyên văn**? Dùng **mã loại
  tin** nào — mã đó có trong danh mục chặn tin không (người dùng có tắt được không)? (`lich-nhac-viec` NV-13, mục 5.2)
- [ ] Lãnh đạo trong danh sách **không nhận email / SMS** có bị loại không? (`lich-nhac-viec` NV-16)

## 7. Dữ liệu, file, văn bản mật

- [ ] **Dữ liệu cũ** (tạo trước khi có tính năng) xử lý thế nào: chuyển đổi / để nguyên / ẩn?
- [ ] Thêm trường mới: bắt buộc? độ dài? mặc định cho bản ghi cũ? có hiện ở **tìm kiếm / tra cứu / xuất Excel /
  in** không?
- [ ] File đính kèm: định dạng, dung lượng tối đa, số file `0..N`, có **chặn file lệch đuôi / nội dung** không?
- [ ] Có áp dụng cho **văn bản / phiếu trình mật** (file mã hóa theo người nhận) không? (`ky-so` NV-16 — câu A3 đang
  mở)

## 8. Ký số và đóng dấu

- [ ] Ký bằng **USB Token / SIM CA / ký từ xa** — hình thức nào áp dụng? (`ky-so` NV-01..06)
- [ ] Có **đóng dấu** đơn vị / dấu xác nhận không? Vị trí chữ ký / dấu trên file? (`ky-so` NV-10, NV-11)
- [ ] Sửa file sau khi đã đặt vị trí chữ ký thì sao (soạn thảo trực tuyến hủy vị trí ký — `tich-hop` NV-09)?

## 9. Báo cáo, thống kê, trang chủ

- [ ] Có **ô trang chủ (widget)** nào phải đếm thêm / đổi cách đếm? (mục 1.3 `nghiep-vu.md` từng phân hệ)
- [ ] Báo cáo / thống kê nào bị ảnh hưởng (đúng hạn / quá hạn, KPI, báo cáo sổ, báo cáo tổng hợp sử dụng)?
- [ ] Đã xử lý nhưng **chưa hoàn thành** tính vào đâu trong thống kê? (đã xác nhận ở `van-ban/den` Q7)

## 10. Giao diện và ngoại lệ

- [ ] Màn hình nào, tab nào, vị trí nút? Danh sách **mặc định lọc gì, sắp xếp gì, phân trang** bao nhiêu?
- [ ] **Không có dữ liệu** thì hiện gì? Không có quyền thì hiện gì?
- [ ] Bấm **hai lần / hai người cùng thao tác** thì sao?
- [ ] Mọi **thông báo lỗi / xác nhận** ghi nguyên văn.

## 11. Ranh giới và hồi quy

- [ ] Phân hệ nào khác dùng chung dữ liệu / màn hình này? (`tom-tat.md` §8 "Liên quan phân hệ khác")
- [ ] Nghiệp vụ có **bản sao ở tầng khác** (web legacy ghi thẳng DB, BE gen-1 và gen-2, mobile) — đổi một chỗ hay
  tất cả? (`dac-thu.md` mục 1 của phân hệ)
- [ ] **Phạm vi KHÔNG thay đổi** là gì (để khoanh vùng kiểm thử hồi quy)?
