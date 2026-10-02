# Báo cáo đợt viết lại tri thức `knowledge/` (2026-09-29 → 2026-10-02)

> Phạm vi: viết lại toàn bộ tri thức nghiệp vụ của Văn phòng số Khánh Hòa từ **code thật** (nhánh `kha_develop` của
> `web-spring` và `backend2.0`) đối chiếu **DB DEV** (Oracle, chỉ SELECT). Mục tiêu: BA / DEV / AI đọc là hiểu hệ
> thống đang chạy thế nào mà không cần mở code. Không sửa code, không sửa DB, không commit.
>
> File câu hỏi cần trả lời: [`cau-hoi-dot-2026-10.md`](cau-hoi-dot-2026-10.md).

## 1. Kết quả tổng

| Phân hệ | Thư mục | Viết lại | Dòng `nghiep-vu` | NV | BR | Sơ đồ | Lỗi ghi nhận | Câu hỏi mở |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Xử lý công việc | `xu-ly-cong-viec` | 2026-09-30 | 770 | 20 | 57 | 8 | — | 1 |
| Văn bản đi | `van-ban/di` | 2026-10-01 | 756 | 17 | 42 | 11 | — | 0 |
| Chuyển văn bản | `van-ban/chuyen-van-ban` | 2026-10-01 | 760 | 22 | 57 | 10 | 15 | 0 |
| Văn bản đến | `van-ban/den` | 2026-10-01 | 838 | 18 | 49 | 10 | 18 | 0 |
| Phiếu trình | `phieu-trinh` | 2026-10-01 | 781 | 19 | 48 | 9 | 20 | 1 |
| Nhắc việc / SMS / nắm tình hình | `lich-nhac-viec` | 2026-10-01 | 990 | 20 | 44 | 12 | 40 | 10 |
| Luồng xử lý | `van-ban/luong-xu-ly` | 2026-10-01 | 602 | 14 | 44 | 7 | 14 | 8 |
| Sổ văn bản | `van-ban/so-van-ban` | 2026-10-01 | 572 | 13 | 35 | 7 | 18 | 10 |
| Liên thông | `van-ban/lien-thong` | 2026-10-01 | 723 | 13 | 32 | 9 | 21 | 10 |
| Quản lý chung văn bản | `van-ban/quan-ly-chung` | 2026-10-01 | 761 | 18 | 40 | 8 | 17 | 9 |
| Nhiệm vụ | `nhiem-vu` | 2026-10-01 | 834 | 20 | 36 | 8 | 28 | 10 |
| Công việc cá nhân | `cong-viec` | 2026-10-01 | 692 | 14 | 33 | 11 | 32 | 10 |
| Hồ sơ công việc | `ho-so-cong-viec` | 2026-10-01 | 860 | 22 | 49 | 9 | 26 | 10 |
| Họp | `hop` | 2026-10-01 | 786 | 18 | 35 | 9 | 17 | 10 |
| Ký số | `ky-so` | 2026-10-02 | 818 | 17 | 46 | 11 | 35 | 10 |
| Hệ thống | `he-thong` | 2026-10-02 | 792 | 20 | 40 | 9 | 24 | 10 |
| KPI / đánh giá | `kpi-danh-gia` | 2026-10-02 | 1059 | 26 | 68 | 12 | 32 | 10 |
| Tích hợp | `tich-hop` | 2026-10-02 | 777 | 16 | 29 | 9 | 21 | 10 |
| Tài liệu mẫu | `tai-lieu-mau` | 2026-10-02 | 482 | 10 | 22 | 7 | 16 | 8 |
| **Tổng (19)** | | | **14653** | **337** | **806** | **176** | **394+** | **137** |

Ghi chú: "Lỗi ghi nhận" = số dòng `L-xx` trong `dac-thu.md` (hai bài đầu dùng khung cũ, lỗi ghi dạng danh sách). Câu hỏi mở của 4 phân hệ đầu đã được trả lời trong đợt; còn lại để trả lời một lượt.

Mỗi phân hệ có 4 file: `nghiep-vu.md` (chính: Tổng quan → Module → NV-xx có BR-xx → sơ đồ Mermaid → data model →
glossary → 7.1 câu hỏi / 7.2 đã xác nhận), `dac-thu.md` (bẫy, chỗ đừng đụng, **lỗi hệ thống ghi nhận** L-xx),
`vi-du-mau.md` (tính năng thật để copy pattern), `ban-do.md` (máy sinh). Mọi khẳng định có trích `file:dòng`; mọi
số liệu DB ghi nguồn "DB DEV `<BẢNG>` ngày …".

## 2. Cách làm

1. Với mỗi phân hệ: tra sẵn DB DEV (menu `SYS_MENU`, widget `HOME_WIDGET`, bảng thuộc phân hệ, số dòng thật,
   comment cột, phân bố giá trị trạng thái) → giao một agent đọc code và viết bài theo khung chuẩn → mình tự kiểm 3–5
   khẳng định then chốt trong code → chạy thêm các truy vấn DB agent cần → agent bổ sung → sang phân hệ kế.
2. Câu hỏi chỉ hỏi **ý đồ nghiệp vụ**, bằng lời thường; lỗi / thiếu kiểm quyền / code chết chỉ **ghi nhận** ở
   `dac-thu.md` (theo yêu cầu "nhiệm vụ là xây kiến thức, không phải fix bug").
3. Sửa chéo: phân hệ sau phát hiện phân hệ trước ghi sai → sửa tại chỗ, gắn tag
   "(sửa chéo 2026-10-02 theo `<phân hệ>`)" — 12 chỗ ở lượt viết + các chỗ sửa ở lượt rà soát.
4. Lượt rà soát cuối: README, thuật ngữ, kiến trúc, tham chiếu chéo, lộ bí mật (mục 6).
5. Thông tin đăng nhập DB chỉ nằm trong biến môi trường của từng lệnh, không ghi vào file nào; giá trị bí mật trong
   tham số hệ thống (mật khẩu, secret, token) không ghi vào tri thức — đã quét lại toàn bộ `knowledge/`.

## 3. Phát hiện lớn theo phân hệ (bản cũ sai / thiếu)

| Phân hệ | Điểm chính |
|---|---|
| Văn bản đến | Phối hợp tự hoàn thành được; Nhận để biết chỉ xem; trả lại có hiệu lực ngay; nút "Nhận để biết" mới chưa có trên web `kha_develop` |
| Phiếu trình | Trạng thái 0/1/2/3/5/7; trình ký lại = lập phiếu mới; người trình tự chọn người xin ý kiến (tuần tự / song song); phiếu xong tự trình ký dự thảo |
| Nhắc việc / SMS | Nhắc việc **không gửi SMS / thông báo**; trạng thái 4/5 là chờ văn bản được chuyển; repo chỉ ghi hàng đợi SMS, việc gửi ở dịch vụ ngoài; nhiều mã tin thật không chặn được |
| Luồng xử lý | `NODE.TYPE` comment DB ngược code; nhóm luồng = bộ điều kiện độ mật / loại / độ khẩn; cấu hình là tham chiếu sống (sửa luồng ảnh hưởng ngay văn bản đang chạy) |
| Sổ văn bản | Cột `COMMUNIST_PARTY` hai nghĩa (số thứ tự / sổ Đảng); không có reset đầu năm; sổ tự sinh khi mở danh sách; 3 nhóm sổ trùng trên DEV |
| Liên thông | 3 kênh tách biệt (trục cơ quan ngoài / VOConnect / nhiệm vụ qua trục); repo không tự gửi — chỉ ghi bảng chờ; "Văn bản từ VPCP" chết hoàn toàn |
| Quản lý chung | Quyền xem chung ở `validateDocumentDetail`; văn bản từng công khai → ai cũng xem; tìm kiếm ES đếm luôn 0; bàn giao lọc trạng thái cũ nên không lấy được văn bản |
| Nhiệm vụ | Không có bước duyệt nhiệm vụ mới (tạo là "Đang thực hiện"); "chờ phê duyệt" là duyệt báo cáo; BE gen-1 nhiệm vụ **có** kiểm quyền; duyệt tiến độ hai cấp |
| Công việc | Kỳ theo quý / năm (KI vẫn tháng); bảng `TASK` trên DEV 0 dòng; KI cá nhân gần như không chạy; số trang chủ thực ra đếm `MISSION` |
| Hồ sơ | Hai cột trạng thái (bàn giao / đóng); tiếp nhận bàn giao = đổi chủ; nộp lưu = đẩy sang phần mềm số hóa; mượn vẫn chạy dù menu khóa |
| Họp | Web ghi thẳng DB qua facade legacy (BE chỉ cho app khác); đơn vị duyệt dựa trên quy tắc Viettel cài cứng; email chỉ tự gửi trong tuần hiện tại |
| Ký số | Cặp trình ký = theo dõi hồ sơ giấy; `SIGN_TYPE` hai cách mã hóa; đóng dấu CloudCA tổ chức không hoạt động; "ký tự động" là giao dịch hệ thống ngoài |
| Hệ thống | Hai hệ quyền thao tác đều vô hiệu (chỉ menu theo vai trò có tác dụng); đăng nhập không so mật khẩu khi SSO lỗi; `VAITRO_SUPPORT` cộng menu cho mọi người |
| KPI | `report-period` = đánh giá công tác tuần; 3 thứ cùng tên "KPI"; ngưỡng xếp loại 70 vs 75; cụm đánh giá tuần ẩn trên DEV vì mã đơn vị không khớp |
| Tích hợp | Mỗi hệ thống ngoài = một tài khoản + `EXT_APP`; chia sẻ chủ động chỉ cho Thư viện điện tử, APP_SHVB / ATTT kéo theo cấu hình; không có MinIO; cơ chế hai site công khai / nội bộ |
| Tài liệu mẫu | 3 menu thư viện mở cùng một danh sách văn bản công khai; thư mục thư viện chưa vận hành; tag lưu chuỗi trên văn bản (DEV 0 văn bản có tag) |

## 4. Phát hiện xuyên phân hệ

- **Quyền ở tầng hiển thị** (đã xác nhận là thiết kế) — BE phần lớn không kiểm người gọi; ngoại lệ có kiểm: ký / từ
  chối phiếu trình, nhiệm vụ gen-1, chia sẻ hồ sơ.
- **Comment cột DB nhiều chỗ ngược / lệch code** (`NODE.TYPE`, `BRIEF_TYPE`, `TEMPLATE.TYPE_ID`, `REP_IN.STATUS`,
  ảnh chữ ký loại 0, `RECEIVER` công việc…) — tri thức luôn ghi theo code, nêu cả hai.
- **Nhiều dữ liệu / cấu hình kế thừa Viettel** không khớp DB Khánh Hòa → các nhánh đó không chạy (câu A4).
- **Nhiều menu đang mở trỏ zul không tồn tại hoặc VM bị comment** (VHR, NQ57, HELP_TASK, BCVBTK, VP CP, đồng bộ người
  dùng…) — liệt kê ở `dac-thu.md` từng phân hệ.
- **Tiến trình ngoài repo** ghi dữ liệu: gửi SMS, đánh chỉ mục Elasticsearch, `DOC_DAILY_SUMMARY`, các cột lạ trên
  `MISSION`, file biên mục hồ sơ, trục liên thông.

## 5. Lỗi bảo mật đã ghi nhận (chỉ ghi nhận, chưa sửa)

Mức nghiêm trọng do mình đánh giá từ code; chi tiết và `file:dòng` ở `dac-thu.md` của phân hệ.

| # | Lỗi | Phân hệ | Mức |
|---|---|---|---|
| 1 | **Đăng nhập BE cấp token không kiểm mật khẩu**: đoạn kiểm kết quả SSO bị comment, chỉ cần mã nhân viên đang hoạt động (`AuthenticatonServiveImpl.java:100-125` — mình đã tự kiểm); tài khoản bị khóa vẫn được cấp token; log ghi mật khẩu thô khi SSO lỗi | `he-thong` | **Rất cao** |
| 2 | **API chạy câu SQL do client gửi** (`/api/app-mobile/get-data-map`, `post-data-map` — đọc, ghi, gọi thủ tục; `AppMobileController.java:55-130` — đã tự kiểm). Ghép với lỗi 1 ⇒ ai biết một mã nhân viên là đọc / sửa được toàn DB | `he-thong`, `tich-hop` | **Rất cao** |
| 3 | `OfficeController` có trang chạy SQL tùy ý và tài khoản ghi cứng | `he-thong` | Cao |
| 4 | Mật khẩu / secret dịch vụ họp trực tuyến, Cisco… lưu dạng rõ trong `SYSTEM_PARAMETER`; mật khẩu ứng dụng KNTC so nguyên văn (không băm) | `hop`, `tich-hop` | Cao |
| 5 | Tiếp nhận bàn giao hồ sơ với id bất kỳ ⇒ chiếm quyền sở hữu hồ sơ; API thống kê hồ sơ xem được đơn vị bất kỳ | `ho-so-cong-viec` | Cao |
| 6 | Màn chờ phê duyệt nhiệm vụ lấy `userId` do client gửi, không kiểm quyền | `nhiem-vu` | Trung bình |
| 7 | BE gần như không kiểm người gọi (quyền chỉ ở tầng hiển thị nút — đã xác nhận là thiết kế); các hệ quyền thao tác `has*Permission` / `officeCheckPermission` luôn đúng | nhiều phân hệ | Thiết kế (ghi nhận) |
| 8 | Danh sách bỏ qua JWT so khớp kiểu "chứa chuỗi" | `tich-hop`, `he-thong` | Trung bình |

Quyết định xử lý các lỗi này là câu **A5** trong file câu hỏi.

## 6. Lượt rà soát & làm mịn cuối

Do một agent rà soát toàn bộ, mình kiểm lại các điểm then chốt. Chi tiết: báo cáo rà soát (scratchpad).

- **`README.md`** viết lại: cây thư mục đúng (thêm `xu-ly-cong-viec`, `van-ban/chuyen-van-ban`), khung bài chuẩn 7 mục +
  bảng ký hiệu viết tắt dùng chung, bảng "Từ khóa → phân hệ" dựng lại theo ranh giới thật, bảng "Tình trạng tri thức".
- **`_chung/thuat-ngu.md`** viết lại theo bài mới; sửa dòng sai (vd. `WaitingNumberBookEntity` là số chờ / giữ số,
  không phải "chờ cấp số"); thêm thuật ngữ xuyên phân hệ (giá trị trạng thái thật, `SEND_TYPE`, ba nghĩa của KPI, cặp
  trình ký, bàn giao vs nộp lưu, thư viện = văn bản đã công khai…).
- **`kien-truc-tong-the.md`, `quy-uoc.md`, `thanh-phan-dung-chung.md`, `cach-lam-chuan/*`, `mau-dau-ra/*`**: sửa theo
  sự thật mới (quyền thật = menu theo vai trò + điều kiện hiện nút; `getPopupPermision` không phải kiểm quyền; đăng
  nhập; `jwt.ignore-apis`; Elasticsearch thay Solr; SMS chỉ ghi hàng đợi; file lưu đĩa — không MinIO; hai site công
  khai / nội bộ); thêm 9 bẫy toàn cục và mục hạ tầng / dịch vụ ngoài; mẫu giải pháp BA dùng mã vai trò thật
  `VT` / `LDDV` / `TTDV` / `NV`.
- **`huong-dan-ra-soat-nghiep-vu.md`**: ghi quy ước đợt này (nguồn DB DEV, tag sửa chéo, không ghi bí mật / IP, lỗi chỉ
  ghi nhận, câu hỏi chỉ hỏi ý đồ, khung 7.1 / 7.2).
- **Kiểm chéo 19 phân hệ**: 372 tham chiếu NV + 62 tham chiếu BR sang bài khác — sửa 2 số sai; chuẩn hóa ký hiệu viết
  tắt; 5 chỗ "chưa đối chiếu DB" trỏ sang phân hệ đã có số liệu; `chuyen-van-ban` đổi lại thứ tự mục 7 ↔ 8; 58 dấu ❓
  sót ngoài mục 7 đổi thành `(?)`; che IP nội bộ ở `hop`; không thấy lỗi font, không thấy mật khẩu / token thật.
- **Công cụ**: sửa `_tools/questions.py` để gom đúng mục 7.1 (khung mới) → `_chung/cau-hoi-mo.md` = 137 câu; sinh
  `_chung/cau-hoi-dot-2026-10.md` (file trả lời). Chưa chạy lại `scan.py` / `gen.py` — đợi quyết định A1.
- **Còn để ngỏ** (không tự chọn): mô tả chi tiết SMS 202 (gửi trợ lý khi lãnh đạo xử lý văn bản) và cách tính hạn xử
  lý theo `DOCUMENT_REQUEST_CONFIG` chưa có bài nào viết sâu; tên đúng của `MEETING_ASSISTANT.ASSI_TYPE = 3` ("cấp" hay
  "cặp" trình ký); dải mã SMS nhóm 300 (thiếu 306, 307 trên DB).

## 7. Việc còn lại

1. Câu hỏi **không trả lời một lượt** (chốt 2026-10-02): làm rõ dần khi phát triển tính năng liên quan — tra phân hệ
   trong [`cau-hoi-dot-2026-10.md`](cau-hoi-dot-2026-10.md) / mục 7.1, trả lời được câu nào thì chuyển sang 7.2 và chạy
   lại `_tools/questions.py` + `_tools/gom_cau_hoi.py`. Đã trả lời trong đợt: `xu-ly-cong-viec` Q16 (không dùng 4 menu
   "Xin ý kiến").
2. Nếu đồng ý A1: sửa `_tools/domains.py`, chạy lại `scan.py` + `gen.py`, cập nhật mục "Module".
3. Nếu A2 = (a): viết phân hệ `kien-nghi`.
4. Tùy A5: lập danh sách ATTT riêng hoặc mở BUG theo quy trình repo.

## 8. Gợi ý commit (DEV tự kiểm rồi chạy — Claude không commit)

```bash
git -C knowledge add -A
git -C knowledge commit -m "knowledge: viet lai 19 phan he tu code kha_develop + DB DEV (2026-09-29..10-02)"
```
