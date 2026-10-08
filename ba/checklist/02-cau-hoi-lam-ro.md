# CHECKLIST 02 — NGÂN HÀNG CÂU HỎI LÀM RÕ YÊU CẦU

> **Nguồn:**
> - Câu hỏi về nghiệp vụ VOffice (vai trò, ký nháy/ký duyệt, chủ trì/phối hợp, liên thông, văn bản mật,
>   ủy quyền): từ `knowledge/_chung/thuat-ngu.md` và bảng "Từ khóa → phân hệ" trong `knowledge/README.md`.
> - Câu hỏi về file, COPY/REFERENCE, đổi/bỏ nguồn, hủy giữa chừng: rút từ 12 TBD (mục 11) của tài liệu mẫu YC17
>   (đã gỡ khỏi repo).
> - Câu hỏi về phạm vi đơn vị, cấp cha/ngang cấp, Mobile: rút từ câu hỏi mở của
>   `knowledge/yeu-cau/2026-09-15-loc-don-vi-nhan-khi-ban-hanh.md`.
> - Nhóm phi chức năng (2.8): theo nhóm NFR của ISO/IEC/IEEE 29148 và Volere.
>
> **Cách dùng:** đi qua từng nhóm. Câu nào **chưa trả lời được từ yêu cầu gốc** → đưa vào mục TBD
> (hoặc `templates/06-danh-sach-cau-hoi.md`) **kèm phương án**. Nhóm không liên quan → bỏ
> qua, nhưng phải *chủ động* bỏ qua chứ không phải quên.

---

## 2.1 Nghiệp vụ & phạm vi

- [ ] Ai yêu cầu, vấn đề thực tế là gì, đo thành công bằng gì?
- [ ] Áp dụng cho **đơn vị nào**: toàn tỉnh, một sở/huyện, hay bật/tắt theo cấu hình đơn vị?
- [ ] Áp dụng cho **dữ liệu cũ** đã tồn tại hay chỉ dữ liệu tạo sau khi triển khai?
- [ ] Có phân biệt **văn bản thường / mật / khẩn** không?
- [ ] Có ngoại lệ theo **loại văn bản, sổ văn bản, lĩnh vực** không?
- [ ] Là **văn bản** (`van-ban/*`) hay **phiếu trình**? Là **nhiệm vụ** (đơn vị giao đơn vị / giao một cá nhân chủ
      trì, duyệt tiến độ hai cấp — `nhiem-vu`), **công việc** (việc của một cá nhân trong kỳ, có phiếu giao việc /
      đánh giá / KI — `cong-viec`) hay **nhắc việc** (giao kèm văn bản cho đơn vị, đơn vị trả lời — `lich-nhac-viec`)?
      Cả ba đều có thể lấy văn bản làm nguồn — "có gắn văn bản" KHÔNG phải tiêu chí phân biệt.

## 2.2 Vai trò & phân quyền

- [ ] Vai trò nào **được thấy**, vai trò nào **được thao tác**? (thấy ≠ thao tác)
- [ ] Một người kiêm nhiều vai trò (VD vừa Văn thư vừa Chuyên viên) thì áp dụng thế nào?
- [ ] **Văn thư cơ quan** và **văn thư phòng** có khác nhau không?
- [ ] Người được **ủy quyền / ký thay / thừa lệnh** có quyền như người gốc không?
- [ ] Đơn vị **phối hợp / nhận để biết / nắm tình hình** có thấy không?
- [ ] Quyền cấu hình trên màn **Phân quyền / Menu** hay gắn cứng theo vai trò?

## 2.3 Trạng thái & luồng xử lý

- [ ] Thao tác được phép ở **những trạng thái nào**? Bị cấm ở trạng thái nào?
- [ ] Sau thao tác, trạng thái chuyển sang gì (tên + mã thật)? Có **quay lui** được không?
- [ ] Có ảnh hưởng **luồng ký** (xét duyệt · ký nháy · ký duyệt) hoặc cấu hình bước ký không?
- [ ] Bản ghi đang ở **giữa luồng** lúc triển khai thì xử lý thế nào?
- [ ] Hai người **cùng thao tác** một bản ghi cùng lúc thì ai thắng?

## 2.4 Giao diện & điều hướng

- [ ] Màn hình nào, tab nào, vị trí nào? Có ảnh design không?
- [ ] Click vào **item** hay cả **khu vực**? Mở trang mới, popup, hay tab mới?
- [ ] Sau điều hướng: **tab mặc định**, **bộ lọc mặc định**, có **giữ bộ lọc cũ** không?
- [ ] **Không có dữ liệu** thì hiển thị gì (ẩn, hiện số 0, câu thông báo)?
- [ ] Danh sách: sắp xếp theo gì, phân trang bao nhiêu, tìm kiếm theo trường nào?
- [ ] Nút mới: nhãn chính xác, có **hỏi xác nhận** không, bấm 2 lần thì sao?
- [ ] Cây đơn vị: hiển thị cấp nào (cha / hiện tại / con / ngang cấp)? Ô tìm kiếm trả về phạm vi nào?

## 2.5 Dữ liệu & file đính kèm

- [ ] Trường mới: kiểu, độ dài, bắt buộc, mặc định, định dạng (ngày, số)?
- [ ] Trường bắt buộc **có điều kiện** (chỉ bắt buộc khi …)?
- [ ] File: giới hạn **dung lượng, số lượng, định dạng**?
- [ ] File trùng xác định theo **tên, mã file hay nội dung**? Trùng thì hỏi, ghi đè hay bỏ qua?
- [ ] Sao chép dữ liệu/file: **COPY** (độc lập) hay **REFERENCE** (dùng chung, nguồn đổi thì đích đổi)?
- [ ] Nguồn dữ liệu nằm ở **bảng/nhóm nào** — đã có người xác nhận chưa?
- [ ] Xóa: **xóa mềm** (`DEL_FLAG`) hay xóa cứng? Xóa ở đích có ảnh hưởng nguồn không?
- [ ] Đổi/bỏ chọn nguồn sau khi đã tự điền: dữ liệu đã điền **giữ hay xóa**?
- [ ] File người dùng **tự upload** trùng với file tự điền: ưu tiên file nào?
- [ ] Hủy giữa chừng (chưa lưu): dữ liệu tạm có bị lưu rác không?

## 2.6 Thông báo, nhắc việc, SMS

- [ ] Có gửi **thông báo / nhắc việc / SMS / email** không? Ai nhận, khi nào?
- [ ] Nội dung **nguyên văn**? Có biến (trích yếu, hạn xử lý) không?
- [ ] Gửi **một lần** hay **lặp lại** đến khi xử lý?

## 2.7 Tích hợp & liên thông

- [ ] Có ảnh hưởng **Mobile app** không? Mobile có làm cùng đợt không?
- [ ] Có ảnh hưởng **liên thông** (trục VPCP, VOConnect) không? Đơn vị ngoài có **mã định danh** chưa?
- [ ] Có ảnh hưởng **ký số** (USB token, CloudCA, ảnh chữ ký, đóng dấu) không?
- [ ] Có ảnh hưởng **báo cáo, thống kê, dashboard, KPI** đang đếm dữ liệu này không?
- [ ] Có ảnh hưởng **tìm kiếm** (Elasticsearch) — dữ liệu mới có cần tìm kiếm được không?
- [ ] Hệ thống ngoài **lỗi/timeout** thì xử lý thế nào, có thử lại không?

## 2.8 Phi chức năng

- [ ] Khối lượng dữ liệu dự kiến? Thời gian phản hồi chấp nhận được?
- [ ] Có cần **ghi nhật ký** (ai, lúc nào, giá trị cũ/mới)?
- [ ] Có yêu cầu **bảo mật** riêng (văn bản mật, che thông tin cá nhân)?
- [ ] Có cần **chuyển đổi dữ liệu cũ** không? Ai chạy, khi nào?
- [ ] Có cần **bật/tắt theo cấu hình** để triển khai dần không?

## 2.9 Đặc thù Văn phòng số (rút từ đợt viết lại tri thức 2026-10)

> Những chỗ yêu cầu mới hay bỏ sót rồi về sau DEV phải hỏi lại. Trước khi hỏi, tra `knowledge/<phân hệ>/tom-tat.md`
> (mục 10 "Khi viết yêu cầu mới…" là checklist riêng của từng phân hệ) — tri thức đã trả lời thì không hỏi.

- [ ] Văn bản **đơn vị** (văn thư nhận rồi phân phối) hay **cá nhân** (gửi thẳng người)? (`van-ban/den` NV-01)
- [ ] Áp dụng cho vai trò nhận nào: **Chủ trì / Phối hợp / Nhận để biết / Nắm tình hình**? Một cấp **nhiều Chủ trì**
      thì chờ tất cả hay một người? Hoàn thành có **lan** lên người giao không? (`van-ban/den` NV-08)
- [ ] Người trong danh sách **"không nhận văn bản khi chuyển cho đơn vị"** có bị loại không? (`he-thong` NV-15)
- [ ] **Trợ lý / thư ký lãnh đạo** nhận thay hay nhận kèm? (`hop` NV-08, `van-ban/den` NV-16)
- [ ] Ai **thấy menu**, ai **thấy nút**, ở **trạng thái** nào? Quản trị toàn tỉnh (`ADMIN`) hay quản trị đơn vị
      (`ADMIN_LEVEL1`) được cấu hình? Có bật **theo danh sách đơn vị** không? (`he-thong` NV-03, NV-06)
- [ ] Trạng thái mới (nếu có): ai chuyển, điều kiện, hiện ở **hộp / tab** nào, **ô trang chủ** có đếm không?
- [ ] Khi **trả lại / thu hồi / hủy ban hành / hủy luồng / trình ký lại** thì dữ liệu mới xử lý thế nào?
- [ ] Văn bản **văn thư tự nhập** (không có người gửi) và văn bản **liên thông** có áp dụng không? Có phải **báo trạng
      thái ngược** lên trục không? (`van-ban/lien-thong`)
- [ ] Có **hệ thống ngoài** nào đọc / ghi dữ liệu này (Thư viện điện tử, phần mềm số hóa, KNTC, eCabinet…)?
      (`tich-hop` mục 1.6)
- [ ] **Hạn xử lý:** nhập tay hay tự tính; "sắp đến hạn" trước bao lâu; "quá hạn" tính theo ngày nào? (`van-ban/den` NV-12)
- [ ] **Nhắc việc** hiện không tự gửi SMS / thông báo — yêu cầu có cần gửi không? (`lich-nhac-viec`)
- [ ] **SMS:** mã loại tin nào; mã đó có trong danh mục chặn tin không (người dùng tắt được không); lãnh đạo trong
      danh sách "không nhận email / SMS" có bị loại không? (`lich-nhac-viec` NV-13, NV-16, mục 5.2)
- [ ] **Ký số:** USB Token / SIM CA / ký từ xa? Có đóng dấu không? Sửa file trên trình soạn thảo trực tuyến sẽ **hủy vị
      trí ký** đã đặt — có ảnh hưởng không? (`ky-so` NV-01, NV-11; `tich-hop` NV-09)
- [ ] **Thống kê:** việc "đã xử lý nhưng chưa hoàn thành" tính vào đâu? (`van-ban/den` Q7 đã xác nhận)
- [ ] Nghiệp vụ có **bản sao ở nhiều tầng** (web ghi thẳng DB, BE cũ và BE mới, ứng dụng di động gọi thẳng BE) — đổi
      một chỗ hay tất cả? Chặn chỉ trên web là chưa đủ. (`dac-thu.md` mục 1 của phân hệ)
- [ ] Có ảnh hưởng **hai site** (Internet / nội bộ) đồng bộ dữ liệu không? (`tich-hop` NV-13)
