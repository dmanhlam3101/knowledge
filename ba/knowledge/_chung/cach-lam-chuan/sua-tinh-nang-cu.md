# Cách làm chuẩn: sửa tính năng đang chạy trên code cũ (BE gen-1 / web legacy)

Phần lớn yêu cầu thực tế rơi vào đây: sửa văn bản đến/đi, trình ký, họp, nhiệm vụ… đang chạy trên `com.viettel.voffice` (gen-1) và VM có nhãn **LEGACY** / **BE+LEGACY**.

## 1. Xác định đúng "tầng nào đang làm việc này"

Mở `knowledge/<phanhe>/ban-do.md`:

1. Tìm màn hình (.zul) → biết VM.
2. Cột "Gọi BE qua" → Business → mục 2 → hàm → endpoint → **controller gen-1 hay gen-2**.
3. Cột "Legacy" → facade nào → mục 4 → service/DAO/entity web.
4. Mục 3: controller → logic (`controler/*Controller`) → DAO → bảng.

Câu hỏi bắt buộc trả lời trước khi sửa: *dữ liệu này đang được đọc/ghi ở web (legacy) hay ở BE?* Nhiều màn hình **đọc bằng legacy nhưng ghi qua BE** (BE+LEGACY) — sửa một bên là lệch.

## 2. Ba kịch bản

### A. Sửa logic trong BE gen-1 (`controler/*Controller` + `database/dao/*DAO`)

- Hàm logic gen-1 rất dài và được nhiều endpoint/màn hình gọi chung (ví dụ `TextController.getTextDetailThread` phục vụ cả xem chi tiết, chờ ký, chờ cấp số). **Trước khi sửa: grep tên hàm trong cả BE và web** để biết ai đang dùng.
- Thay đổi hành vi → thêm hàm mới `xxxV2` / endpoint mới (mẫu: `updateReadingStatusV2`, `getTextDetail` với `TEXT_DETAIL_VARIANT = V2`), giữ hàm cũ cho màn hình khác. Đây là cách dự án đã làm.
- SQL trong DAO là chuỗi ghép tay: thêm điều kiện phải giữ tham số bind (`:param`), không nối chuỗi từ input.
- Trạng thái văn bản dùng hằng số `Constants.TEXT_STATE_*`, `TextStateConstants`, `TextProcessStateConstants` — không dùng số magic. Nhưng **đối chiếu giá trị số trong bài phân hệ**: hằng lệch nhau giữa các bản sao web / BE (`xu-ly-cong-viec/dac-thu.md` bẫy 8), và mã lọc / mã hộp có thể trùng số với trạng thái (kiến trúc tổng thể bẫy 10).
- Sau khi sửa: chạy lại màn hình web tương ứng **và** kiểm tra mobile nếu endpoint đó nằm trong `AppMobile*`/`/ext-*`.

### B. Sửa màn hình web đang dùng facade legacy

- Nếu chỉ sửa hiển thị / thêm cột từ dữ liệu đã có → sửa VM/zul, giữ facade.
- Nếu cần **dữ liệu mới** → không thêm hàm vào facade/DAO web; thêm endpoint gen-2 (`them-api-be-gen2.md`) + hàm Business, VM gọi Business cho phần mới. Màn hình trở thành BE+LEGACY — chấp nhận được, ghi vào `dac-thu.md`.
- Nếu cần **ghi dữ liệu** → bắt buộc qua BE (với tính năng mới). Lưu ý hiện trạng: một số nghiệp vụ **đang ghi thẳng DB từ web** (lịch họp, quản trị hệ thống, kiến nghị, `NOTICE`, KPI đơn vị — kiến trúc tổng thể mục 3) và có bản ghi song song ở BE cho kênh khác; sửa quy tắc nghiệp vụ phải sửa **mọi bản** đang chạy (vd. `hop` NV-17).
- Entity web (`com.viettel.voffice.entity.*`) map cùng bảng với entity BE: thêm cột trong DB thì phải thêm field ở **cả hai** nếu web còn đọc bảng đó qua JPA (xem `them-truong-du-lieu.md`).

### C. Chuyển một màn hình từ legacy sang BE (migration có chủ đích)

Chỉ làm khi được yêu cầu hoặc khi sửa legacy quá rủi ro. Thứ tự: tạo endpoint gen-2 cho từng hàm facade đang dùng → Business → thay từng `Delegate.getService` bằng Business → xóa import remote → chạy `scan.py` để nhãn chuyển thành **BE**.

## 3. Bẫy cụ thể đã thấy trong code

| Bẫy | Chi tiết |
|---|---|
| Màn hình chết | Các zul trỏ VM không tồn tại (☠ trong ban-do — bộ quét có gắn nhầm ☠ cho lớp tên không kết thúc bằng `VM`, xem `_chung/cau-hoi-dot-2026-10.md` A1). Đừng sửa chúng, đừng lấy làm mẫu. Nếu yêu cầu chạm tới màn hình ☠ → tìm màn "sống" cùng chức năng: vd. trong `documentDraft/` chỉ các popup con trỏ `vm.admin.requisition.*` là chết, còn màn chính `documentDraft.zul` + `DocumentDraftVM` (menu XỬ LÝ CÔNG VIỆC › Dự thảo) **đang dùng** (`xu-ly-cong-viec/dac-thu.md` bẫy 1–3) (sửa 2026-10-02: bản cũ ghi "`documentDraft/*` ☠ → thật ra là `requisition/*`"). Menu trỏ zul không tồn tại cũng có (XLCV 1.1 Q16). |
| Hai `DocumentController` | gen-1 logic `com.viettel.voffice.controler.DocumentController` (@Service) ≠ gen-2 `com.viettel.office.controller.DocController`. |
| `TextController.ROOT_ACTION = "textAction"` | Logic gen-1 tự gọi lại endpoint theo tên hàm (`functionName = "textAction.searchText"`) cho log/trace — đổi tên endpoint phải đổi cả chuỗi này. |
| `isSecurity` | Request gen-1 có thể mã hóa AES/RSA (vd. ghi đơn vị — `he-thong/dac-thu.md` mục 1). `backend2.0/backendvoffice/postman/` hiện chỉ có collection quản lý cache, không có mẫu request gen-1 (kiểm 2026-10-02). |
| BE không kiểm quyền người gọi | Quyền nằm ở điều kiện hiện nút trong VM (thiết kế chung, đã xác nhận); sửa điều kiện quyền = sửa VM (cả màn chi tiết lẫn lưới — vd. `van-ban/di/vi-du-mau.md` mục A "hai chỗ"). Ngoại lệ: nhiệm vụ gen-1 (`nhiem-vu` 1.4). |
| Comment cột DB | Có chỗ ngược / lệch code — tin code (kiến trúc tổng thể bẫy 8). |
| Trạng thái từ `CODE_MASTER` | Một số combobox trạng thái đọc DB (`code.doc.status`…), thêm trạng thái mới là **INSERT dữ liệu**, không phải sửa enum. |
| Facade trả entity JPA web | VM legacy giữ entity JPA trong session ZK; đổi entity (thêm quan hệ lazy) có thể gây `LazyInitializationException` ở màn hình. |
| `merge/` | Không sửa; không phải nguồn sự thật. |

## 4. Checklist khi sửa

- [ ] Đã xác định tầng (web legacy / gen-1 / gen-2) và liệt kê mọi màn hình + endpoint dùng chung hàm sắp sửa (đọc mục 1 "Tình trạng kỹ thuật" của `dac-thu.md` phân hệ).
- [ ] Đã kiểm nghiệp vụ có bản sao ở tầng khác không (web legacy ghi thẳng DB / gen-1 / gen-2 / mobile) — sửa đủ các bản.
- [ ] Thay đổi hành vi → hàm/endpoint mới, không phá hàm cũ.
- [ ] DB đổi → SQL migration + entity gen-2 + entity web (nếu còn dùng) + DTO web.
- [ ] Trạng thái → dùng hằng số; nếu là CODE_MASTER thì kèm SQL dữ liệu.
- [ ] Test màn hình web, mobile (nếu chung endpoint), và ứng dụng ngoài (`/ext-*`) nếu chung service.
- [ ] Ghi bẫy mới vào `knowledge/<phanhe>/dac-thu.md`.
