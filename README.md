# knowledge/ — Bộ não dự án VOKhanhHoa (Văn phòng số)

Folder này là **tri thức dùng chung cho người và AI** để khi nhận một yêu cầu mới có thể nhanh chóng đưa ra
(1) **giải pháp nghiệp vụ** kiểu BA và (2) **hướng code** cho dev — đúng hướng, đúng chỗ, theo cách hệ thống đang làm.
Không cần đúng 100%, nhưng phải đủ để dev/BA có điểm bắt đầu chuẩn.

> Đợt viết lại 2026-09-29 → 2026-10-02: 19 phân hệ được viết lại từ code nhánh `kha_develop` (web-spring + backend2.0)
> và đối chiếu DB DEV (chỉ SELECT). Bảng "Tình trạng tri thức" ở cuối file. (sửa 2026-10-02: cập nhật cây thư mục,
> bảng từ khóa theo ranh giới thật của bài mới, thêm khung bài chuẩn + cách đọc.)

## Cấu trúc

```
knowledge/
├── README.md                 ← bạn đang đọc
├── _chung/                   ← dùng chung mọi phân hệ
│   ├── kien-truc-tong-the.md    web / BE gen-1 / BE gen-2, cơ chế gọi, đăng nhập, quyền, DB, menu, hạ tầng ngoài, bẫy toàn cục
│   ├── thuat-ngu.md             thuật ngữ xuyên phân hệ ↔ tên trong code (mỗi dòng trỏ sang phân hệ chi tiết)
│   ├── quy-uoc.md               naming, DEL_FLAG, sequence, transaction, response wrapper, log
│   ├── thanh-phan-dung-chung.md widget, lookup, tiện ích web dùng chung — tìm trước khi viết mới
│   ├── huong-dan-ra-soat-nghiep-vu.md  KHUNG BÀI CHUẨN + quy tắc viết / rà soát tri thức (đọc trước khi sửa bài)
│   ├── cach-lam-chuan/          CÔNG THỨC: thêm tính năng mới, thêm API BE, thêm màn hình web, sửa code cũ, thêm trường
│   ├── mau-dau-ra/              MẪU xuất kết quả: giải pháp BA, hướng dẫn kỹ thuật
│   ├── cau-hoi-mo.md            SINH TỰ ĐỘNG: gom câu hỏi mục 7.1 của mọi phân hệ (_tools/questions.py)
│   ├── cau-hoi-dot-2026-10.md   phiếu câu hỏi gom từ mục 7.1 + 5 quyết định chung (trả lời dần khi làm tính năng liên quan; _tools/gom_cau_hoi.py)
│   ├── bao-cao-dot-viet-lai-2026-10.md  báo cáo tổng hợp đợt viết lại 2026-09-29 → 10-02
│   ├── ban-do.md                SINH TỰ ĐỘNG: widget / thành phần web dùng chung
│   └── ban-do-tong/             SINH TỰ ĐỘNG: toàn bộ endpoint, web→BE, entity↔bảng, thống kê
├── xu-ly-cong-viec/          dự thảo → trình ký / xin ý kiến → ký nháy / ký duyệt / phê duyệt → trả lại (TRƯỚC cấp số)
├── van-ban/                  văn bản đã có bản ghi DOCUMENT, tách 7 folder con
│   ├── di/                      chờ cấp số → cấp số → đóng dấu → ban hành; hủy ban hành; công khai; văn bản thay thế
│   ├── den/                     phía người nhận: tiếp nhận / vào sổ đến → hộp việc → cho ý kiến → hoàn thành / trả lại
│   ├── chuyen-van-ban/          MỌI luồng chuyển (văn bản đến, văn thư chuyển văn bản đi = "ban hành", tự động chuyển, thu hồi)
│   ├── luong-xu-ly/             cấu hình luồng FLOW / NODE và quy tắc tính người / đơn vị ở bước kế
│   ├── so-van-ban/              sổ, cơ chế sinh số, số chờ, báo cáo / in sổ
│   ├── lien-thong/              trục liên thông cơ quan ngoài, VOConnect (tenant khác), nhiệm vụ qua trục, migrate
│   └── quan-ly-chung/           tra cứu / tìm kiếm, quyền xem, nhật ký, bàn giao văn bản, phạm vi, thể loại, tài liệu cá nhân
├── phieu-trinh/              phiếu xin ý kiến nội bộ (không số, không sổ), có thể kèm dự thảo
├── ho-so-cong-viec/          hồ sơ (BRIEF): lập, gắn tài liệu, chia sẻ, bàn giao, đóng, nộp sang phần mềm số hóa, mượn, kho
├── nhiem-vu/                 MISSION — đơn vị giao đơn vị / cá nhân chủ trì; tiến độ, duyệt hai cấp, gia hạn, đóng
├── cong-viec/                TASK — việc của MỘT cá nhân theo kỳ; phiếu giao việc / phiếu đánh giá; KI cá nhân
├── hop/                      lịch họp / lịch công tác, duyệt lịch, phòng họp, cầu truyền hình, eCabinet, lịch tuần
├── ky-so/                    cơ chế ký số dùng chung, chứng thư, ảnh chữ ký, con dấu, đóng dấu số, cặp trình ký
├── kpi-danh-gia/             đánh giá công tác tuần, chấm điểm thi đua đơn vị, KPI / KI đơn vị, theo dõi & thống kê
├── lich-nhac-viec/           nhắc việc (gen-2 — mẫu chuẩn cho tính năng mới), thông báo, SMS, nắm tình hình, định hướng
├── tai-lieu-mau/             thư viện văn bản công khai, biểu mẫu, tag văn bản, màn báo cáo theo mẫu
├── he-thong/                 đăng nhập, phiên / menu, người dùng, vai trò, đơn vị, nhóm, danh mục, tham số, trang chủ
├── tich-hop/                 hệ thống ngoài (trừ trục văn bản): /ext-*, KNTC, VHR, SSO/VNeID connector, WOPI, ES, mobile, file / hai site
├── yeu-cau/                  các yêu cầu đã phân tích (giải pháp BA + hướng dẫn kỹ thuật) — ví dụ đầu ra thật
└── _tools/                   scan.py + domains.py + gen.py → sinh lại ban-do.md; questions.py → cau-hoi-mo.md; gom_cau_hoi.py → cau-hoi-dot-2026-10.md
```

**Mỗi folder phân hệ có đúng 4 file** (để ai cũng biết tìm gì ở đâu):

| File | Nội dung | Ai viết |
|---|---|---|
| `nghiep-vu.md` | Bài chính theo **khung chuẩn 7 mục** (dưới đây): phạm vi, actor, nghiệp vụ `NV-xx` + quy tắc `BR-xx`, sơ đồ, data model, glossary, câu hỏi | Người (AI viết từ code, mọi khẳng định có `file:dòng`) |
| `ban-do.md` | Màn hình → VM → Business → endpoint BE → service → DAO/repo → bảng. Nhãn BE / LEGACY / ☠ | **Máy sinh** — không sửa tay |
| `dac-thu.md` | Tình trạng kỹ thuật (tầng nào làm gì), bẫy, chỗ "đừng đụng", **lỗi hệ thống — ghi nhận** (`L-xx`) | Người |
| `vi-du-mau.md` | Tính năng THẬT trong code để copy pattern khi thêm mới (nên copy / không nên copy) | Người |

## Khung bài chuẩn `nghiep-vu.md` và cách đọc

Chi tiết quy tắc: [`_chung/huong-dan-ra-soat-nghiep-vu.md`](_chung/huong-dan-ra-soat-nghiep-vu.md).

| Mục | Nội dung | Đọc để |
|---|---|---|
| 1. Tổng quan | 1.1 Phạm vi (**gồm** / **KHÔNG gồm → trỏ phân hệ nào**), menu thật (DB DEV `SYS_MENU`), widget trang chủ, actor + mã vai trò, "Sửa so với knowledge cũ" | biết yêu cầu có thuộc phân hệ này không |
| 2. Module | bảng zul → VM → Business → endpoint → service → DAO → bảng | mở đúng file code |
| 3. Nghiệp vụ | `### NV-xx` — mục đích, actor / quyền, luồng FE → BE → DB, `**BR-xx.**` quy tắc, trạng thái (giá trị số thật), bảng, tích hợp, edge case | as-is chi tiết, quy tắc cần giữ |
| 4. Sơ đồ | Mermaid `flowchart` / `sequenceDiagram` / `stateDiagram-v2` | nhìn nhanh luồng / trạng thái |
| 5. Data model | `erDiagram` + cột quan trọng (chỉ quan hệ có bằng chứng; DB DEV gần như không có FK) | thiết kế dữ liệu |
| 6. Glossary | thuật ngữ nghiệp vụ ↔ tên trong code | dịch yêu cầu sang code |
| 7. [CẦN XÁC NHẬN] | **7.1** câu hỏi còn mở (`Qn`, chỉ hỏi ý đồ nghiệp vụ) · **7.2** đã xác nhận (sự thật đã chốt, `Xn`) | biết chỗ nào chắc, chỗ nào còn treo |

Cách đọc tham chiếu:

- `NV-xx` / `BR-xx` không kèm tiền tố = trong cùng bài. Tham chiếu sang bài khác ghi **`<ký hiệu> NV-xx`** hoặc `` `<phân hệ>` NV-xx ``.
  Ký hiệu thống nhất: `XLCV` xu-ly-cong-viec · `VBĐi` van-ban/di · `VBĐ` van-ban/den · `CVB` van-ban/chuyen-van-ban ·
  `LXL` van-ban/luong-xu-ly · `SVB` van-ban/so-van-ban · `LT` van-ban/lien-thong · `QLC` van-ban/quan-ly-chung ·
  `PT` phieu-trinh · `LNV` lich-nhac-viec · `NVu` nhiem-vu · `CV` cong-viec · `HSCV` ho-so-cong-viec · `KS` ky-so · `HT` he-thong
  (hop, kpi-danh-gia, tich-hop, tai-lieu-mau ghi tên folder trong backtick).
- Nguồn dữ liệu ghi dạng **"DB DEV `<BẢNG>` ngày YYYY-MM-DD"** = số liệu do người điều phối tra DB DEV (chỉ SELECT) — là ảnh chụp tại ngày đó, không phải hằng số.
- Tag **"(sửa YYYY-MM-DD: lý do)"** = sửa tri thức cũ; **"(sửa chéo YYYY-MM-DD theo `<phân hệ>`)"** = sửa theo sự thật đã chốt ở bài khác.
- Lỗi nghi vấn / thiếu kiểm tra / code chết chỉ ghi ở `dac-thu.md` (mục "lỗi hệ thống — ghi nhận"), không ghi thành câu hỏi.
- Cấu hình bí mật (mật khẩu, khóa, token, địa chỉ máy chủ) chỉ ghi **tên khóa** — "(có khai — không ghi giá trị)".

## Cách dùng khi nhận một yêu cầu

1. **Xác định phân hệ** — dùng bảng dưới, rồi đọc mục **1.1 Phạm vi** của bài đó (bảng "KHÔNG gồm" chỉ đúng nơi).
   Yêu cầu nói "nhiệm vụ" / "công việc" thì hỏi: việc **đơn vị giao đơn vị hoặc giao một cá nhân chủ trì**, duyệt tiến độ hai cấp (→ `nhiem-vu`, bảng `MISSION`)
   hay việc **của một cá nhân trong kỳ**, có phiếu giao việc / phiếu đánh giá / KI (→ `cong-viec`, bảng `TASK`)?
   Cả hai **đều có thể** lấy văn bản làm nguồn gốc (`SOURCE_MAP`) — "có gắn văn bản hay không" KHÔNG phải tiêu chí phân biệt (sửa 2026-10-02 theo `nhiem-vu`, `cong-viec`).
   Giao việc **kèm văn bản cho đơn vị, đơn vị trả lời** là **nhắc việc** (→ `lich-nhac-viec`).
2. **Đọc 4 file của phân hệ đó** (`nghiep-vu` → `dac-thu` → `ban-do` → `vi-du-mau`). Yêu cầu xuyên phân hệ thì đọc thêm phân hệ liên quan (theo bảng "KHÔNG gồm").
3. **Đọc `_chung/cach-lam-chuan/`** đúng loại việc (thêm API / thêm màn hình / sửa legacy / thêm trường).
4. **Mở code thật** theo đường dẫn trong `ban-do.md` và `vi-du-mau.md` để xác nhận trước khi kết luận.
5. **Xuất kết quả theo `_chung/mau-dau-ra/`** — một bản giải pháp BA + một bản hướng dẫn kỹ thuật.
6. **Sau khi làm xong**: cập nhật `nghiep-vu.md`/`dac-thu.md` nếu có tri thức mới; chạy lại `_tools` nếu thêm class/màn hình.

## Từ khóa → phân hệ

| Yêu cầu nhắc tới | Phân hệ |
|---|---|
| dự thảo, soạn văn bản, trình ký, trình xin ý kiến / cho ý kiến (dự thảo), ký nháy, ký duyệt, phê duyệt, đọc soát, văn thư xét duyệt, trả lại / từ chối trong luồng ký, hủy luồng, thu hồi ký, khai "nơi nhận dự kiến", "Chuyển cấp số", hộp *Dự thảo* / *Văn bản ký duyệt* | `xu-ly-cong-viec` |
| chờ cấp số, cấp số, cấp số & đóng dấu, xin dấu / đóng dấu / từ chối / hủy đóng dấu, tự động ban hành, hủy ban hành / từ chối cấp số, **công khai văn bản** (VBĐi NV-12), văn bản thay thế, phát hành ra ngoài, xóa / khôi phục văn bản đi, hộp *Văn bản ban hành* / *Văn bản đóng dấu* | `van-ban/di` |
| văn bản đến, tiếp nhận / vào sổ đến, nhập văn bản đến, bút phê / ý kiến lãnh đạo, hoàn thành, trả lại / đề nghị trả lại, nhận để biết, đã đọc / chưa đọc, hạn xử lý / sắp đến hạn / quá hạn, tra cứu văn bản đến, theo dõi văn bản đến đơn vị | `van-ban/den` |
| chuyển văn bản / chuyển xử lý, vai trò **chủ trì / phối hợp / nhận để biết / nắm tình hình** khi chuyển, chuyển theo luồng / tự do, chuyển nhiều văn bản, "ban hành" = văn thư chuyển văn bản đã cấp số, tự động chuyển nơi nhận dự kiến / sau tiếp nhận, thu hồi văn bản đã chuyển, giới hạn chuyển, ngưỡng số người nhận, nhóm nhận, trợ lý cùng nhận | `van-ban/chuyen-van-ban` |
| luồng ký / luồng xử lý (cấu hình), nút, đường nối, hành động, nhóm luồng, người ký tiếp theo, đổi người ký, thêm người ký ngoài luồng | `van-ban/luong-xu-ly` |
| sổ văn bản, số đi / số đến, sinh số, cấp bù số, sổ dùng chung, sổ mặc định theo năm, số chờ / giữ số, **báo cáo / in sổ** ("Báo cáo văn bản đi đến", mục lục, sổ đăng ký) | `van-ban/so-van-ban` |
| liên thông, trục, gửi cơ quan ngoài, mã định danh, VOConnect / tenant khác, văn bản VPCP, migrate văn bản cũ | `van-ban/lien-thong` |
| tra cứu / tìm kiếm văn bản (toàn văn), theo dõi văn bản đơn vị / văn bản đi đơn vị, tình hình xử lý cá nhân, quyền xem văn bản, nhật ký thao tác, **bàn giao văn bản**, phạm vi văn bản, thể loại / lĩnh vực / độ khẩn / độ mật, tài liệu cá nhân, ghi chú trao đổi, mẫu ý kiến chuyển | `van-ban/quan-ly-chung` |
| phiếu trình, tờ trình, xin ý kiến lãnh đạo bằng phiếu (không số, không sổ), chuyển tiếp để biết phiếu, theo dõi phiếu trình | `phieu-trinh` |
| kiến nghị / khó khăn vướng mắc (`REQUEST`) — chưa có phân hệ riêng | tạm ở `phieu-trinh` PT NV-18 (khó khăn vướng mắc của tiến độ nhiệm vụ: `nhiem-vu` NV-11) |
| hồ sơ, thư mục hồ sơ, chia sẻ / bàn giao / tiếp nhận hồ sơ, đóng hồ sơ, **nộp lưu** (nộp sang phần mềm số hóa văn bản), mượn / trả, kho – kệ – hộp | `ho-so-cong-viec` |
| nhiệm vụ đơn vị / nhiệm vụ cá nhân chủ trì, giao nhiệm vụ, tiến độ, duyệt hai cấp, gia hạn, đóng, chuyển đơn vị thực hiện, phối hợp, biên bản họp / kết luận sinh nhiệm vụ, nhiệm vụ định kỳ, phiếu giao / đánh giá nhiệm vụ tháng, báo cáo đơn vị theo mẫu (nghiệp vụ / BE), báo cáo / dashboard nhiệm vụ | `nhiem-vu` |
| công việc cá nhân, giao / tự đề xuất công việc, phiếu giao việc, phiếu đánh giá công việc, **KI cá nhân / KI đơn vị hằng tháng**, thống kê công việc, cấu hình thời gian giao / đánh giá | `cong-viec` |
| lịch họp / lịch công tác, đặt / duyệt lịch (QLLH), phòng họp, cầu truyền hình, trợ lý lãnh đạo, lịch tuần, eCabinet, biểu quyết, báo cáo quân số | `hop` |
| ký số, USB Token, SIM CA, CloudCA / MySign, chứng thư, ảnh chữ ký, vị trí ký, con dấu đơn vị, đóng dấu số (cơ chế), xác thực chữ ký, **cặp trình ký**, giao dịch ký của hệ thống ngoài | `ky-so` |
| **đánh giá công tác tuần**, nhóm nhiệm vụ (`WORK_GROUP`), chấm điểm thi đua đơn vị / tiêu chí, **KPI đơn vị** / nề nếp, đề xuất cộng điểm, cấu hình tỷ lệ / KI, theo dõi KPI xử lý, cổng KPI, báo cáo tổng hợp sử dụng (nội dung), báo cáo văn bản trình ký, thỏa thuận hợp tác, OKR | `kpi-danh-gia` |
| nhắc việc (gắn văn bản), thông báo (chuông), thông báo chung / bảng tin, SMS (hàng đợi, mẫu tin, chặn tin), lãnh đạo không nhận email / SMS, **nắm tình hình** / thông tin phục vụ lãnh đạo, định hướng | `lich-nhac-viec` |
| thư viện văn bản (= văn bản đã công khai), thư mục thư viện, biểu mẫu, tag văn bản, màn báo cáo theo mẫu (phía màn) | `tai-lieu-mau` |
| **đăng nhập** (form, SSO, VNeID, eCabinet, OTP), phiên / menu theo vai trò – đơn vị, người dùng, vai trò, gán menu, đơn vị, nhóm, danh mục chung, tham số, văn thư đơn vị, trang chủ / widget, phản ánh, phiên bản | `he-thong` |
| hệ thống tích hợp / ứng dụng ngoài (`/ext-*`), **KNTC**, Thư viện điện tử, VHR (API), SSO / VNeID (connector), **WOPI** soạn thảo trực tuyến, **Elasticsearch**, mobile (kiểm phiên bản, thiết bị nhận thông báo), **ViettelPay**, lưu trữ file / hai site, cây tổ chức Đảng | `tich-hop` |

## Tình trạng tri thức (sau đợt viết lại, 2026-10-02)

| Phân hệ | Số NV | Quy tắc BR | Ngày viết lại | Câu hỏi còn mở (7.1) |
|---|---|---|---|---|
| `xu-ly-cong-viec` | 20 | BR-01 … BR-57 | 2026-09-30 | 1 |
| `van-ban/di` | 17 | BR-01 … BR-42 | 2026-09-30 | 0 |
| `van-ban/den` | 18 | BR-01 … BR-49 | 2026-10-01 | 0 |
| `van-ban/chuyen-van-ban` | 22 | BR-01 … BR-57 | 2026-10-01 | 0 |
| `van-ban/luong-xu-ly` | 14 | BR-01 … BR-44 | 2026-10-01 | 8 |
| `van-ban/so-van-ban` | 13 | BR-01 … BR-34 | 2026-10-01 | 10 |
| `van-ban/lien-thong` | 13 | BR-01 … BR-32 | 2026-10-01 | 10 |
| `van-ban/quan-ly-chung` | 18 | BR-01 … BR-40 | 2026-10-01 | 9 |
| `phieu-trinh` | 19 | BR-01 … BR-48 | 2026-10-01 | 1 |
| `lich-nhac-viec` | 20 | BR-01 … BR-44 | 2026-10-01 | 10 |
| `nhiem-vu` | 20 | BR-01 … BR-36 | 2026-10-01 | 10 |
| `cong-viec` | 14 | BR-01 … BR-33 | 2026-10-01 | 10 |
| `ho-so-cong-viec` | 22 | BR-01 … BR-49 | 2026-10-01 | 10 |
| `hop` | 18 | BR-01 … BR-35 | 2026-10-01 | 10 |
| `ky-so` | 17 | BR-01 … BR-46 | 2026-10-01 | 10 |
| `he-thong` | 20 | BR-01 … BR-40 | 2026-10-02 | 10 |
| `kpi-danh-gia` | 26 | BR-01 … BR-68 | 2026-10-02 | 10 |
| `tich-hop` | 16 | BR-01 … BR-29 | 2026-10-02 | 10 |
| `tai-lieu-mau` | 10 | BR-01 … BR-22 | 2026-10-02 | 8 |
| **Tổng** | **337** | | | **137** |

BR đánh số liên tục trong từng bài (một số bài có BR phụ dạng `BR-14a`). Câu hỏi còn mở đang gom ở
[`_chung/cau-hoi-dot-2026-10.md`](_chung/cau-hoi-dot-2026-10.md) (kèm 5 quyết định chung A1–A5) để chủ dự án trả lời.

## Nguyên tắc giữ bộ tri thức sống

- `ban-do.md` **không bao giờ sửa tay** — chạy `python knowledge/_tools/scan.py && python knowledge/_tools/gen.py`.
- Tri thức viết tay chỉ ghi thứ **không suy ra được từ code**: tại sao, quy tắc nghiệp vụ, bẫy, quyết định.
- Mỗi lần AI/dev bị sửa ("không, ở đây phải làm X") → ghi một dòng vào `dac-thu.md` của phân hệ hoặc `_chung/quy-uoc.md`.
- Câu hỏi còn mở nằm ở **mục 7.1** của từng bài (bảng mã `Qn`); trả lời xong thì chuyển sang 7.2 và sửa NV / BR liên quan. Ngoài mục 7 không dùng `❓` (trích bài cũ ghi `(?)`).
  `_tools/questions.py` gom các bảng `Qn` mục 7.1 → `_chung/cau-hoi-mo.md` (chạy lại sau mỗi lần trả lời).
