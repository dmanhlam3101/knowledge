# knowledge/ — Bộ não dự án VOKhanhHoa (Văn phòng số)

Folder này là **tri thức dùng chung cho người và AI** để khi nhận một yêu cầu mới có thể nhanh chóng đưa ra
(1) **giải pháp nghiệp vụ** kiểu BA và (2) **hướng code** cho dev — đúng hướng, đúng chỗ, theo cách hệ thống đang làm.
Không cần đúng 100%, nhưng phải đủ để dev/BA có điểm bắt đầu chuẩn.

## Cấu trúc

```
knowledge/
├── README.md                 ← bạn đang đọc
├── _chung/                   ← dùng chung mọi phân hệ
│   ├── kien-truc-tong-the.md    web / BE gen-1 / BE gen-2, cơ chế gọi, session, DB, menu, i18n
│   ├── thuat-ngu.md             Text ≠ Document, requisition, ký nháy/ký duyệt/xét duyệt ...
│   ├── quy-uoc.md               naming, DEL_FLAG, sequence, transaction, response wrapper, log
│   ├── thanh-phan-dung-chung.md widget, lookup, tiện ích web dùng chung — tìm trước khi viết mới
│   ├── cach-lam-chuan/          CÔNG THỨC: thêm tính năng mới, thêm API BE, thêm màn hình web, sửa code cũ ...
│   ├── mau-dau-ra/              MẪU xuất kết quả: giải pháp BA, hướng dẫn kỹ thuật
│   ├── cau-hoi-mo.md            SINH TỰ ĐỘNG: gom mọi ❓ cần người xác nhận (_tools/questions.py)
│   └── ban-do-tong/             SINH TỰ ĐỘNG: toàn bộ endpoint, web→BE, entity↔bảng, thống kê
├── van-ban/                  ← phân hệ lớn nhất, tách 6 folder con
│   ├── den/  di/  luong-xu-ly/  so-van-ban/  lien-thong/  quan-ly-chung/
├── phieu-trinh/
├── ho-so-cong-viec/
├── nhiem-vu/                 mission – nhiệm vụ cá nhân/đơn vị, KHÔNG gắn văn bản
├── cong-viec/                task – công việc cá nhân, GẮN văn bản
├── hop/
├── ky-so/
├── kpi-danh-gia/
├── lich-nhac-viec/           nhắc việc = tính năng MỚI, là mẫu chuẩn cho tính năng mới
├── tai-lieu-mau/
├── he-thong/
├── tich-hop/
├── yeu-cau/                  các yêu cầu đã phân tích (giải pháp BA + hướng dẫn kỹ thuật) — ví dụ đầu ra thật
└── _tools/                   scan.py + domains.py + gen.py → sinh lại ban-do.md; questions.py → cau-hoi-mo.md
```

**Mỗi folder phân hệ có đúng 4 file** (để ai cũng biết tìm gì ở đâu):

| File | Nội dung | Ai viết |
|---|---|---|
| `nghiep-vu.md` | Actor, quy trình, trạng thái, quy tắc nghiệp vụ, thuật ngữ riêng | Người (AI nháp từ code, đánh `❓` chỗ chưa chắc) |
| `ban-do.md` | Màn hình → VM → Business → endpoint BE → service → DAO/repo → bảng. Nhãn BE / LEGACY / ☠ | **Máy sinh** — không sửa tay |
| `dac-thu.md` | Bẫy, quyết định riêng, chỗ "đừng đụng", tình trạng legacy vs mới | Người |
| `vi-du-mau.md` | Tính năng THẬT trong code để copy pattern khi thêm mới | Người |

## Cách dùng khi nhận một yêu cầu

1. **Xác định phân hệ** — dùng bảng dưới; nếu yêu cầu nói "nhiệm vụ" hỏi ngay: gắn văn bản (→ `cong-viec`) hay không (→ `nhiem-vu`).
2. **Đọc 4 file của phân hệ đó** (`nghiep-vu` → `dac-thu` → `ban-do` → `vi-du-mau`). Yêu cầu xuyên phân hệ thì đọc thêm phân hệ liên quan.
3. **Đọc `_chung/cach-lam-chuan/`** đúng loại việc (thêm API / thêm màn hình / sửa legacy / thêm trường).
4. **Mở code thật** theo đường dẫn trong `ban-do.md` và `vi-du-mau.md` để xác nhận trước khi kết luận.
5. **Xuất kết quả theo `_chung/mau-dau-ra/`** — một bản giải pháp BA + một bản hướng dẫn kỹ thuật.
6. **Sau khi làm xong**: cập nhật `nghiep-vu.md`/`dac-thu.md` nếu có tri thức mới; chạy lại `_tools` nếu thêm class/màn hình.

## Từ khóa → phân hệ

| Yêu cầu nhắc tới | Phân hệ |
|---|---|
| văn bản đến, tiếp nhận, bút phê, chuyển xử lý, chủ trì/phối hợp, hạn xử lý | `van-ban/den` |
| dự thảo, trình ký, ký nháy, ký duyệt, cấp số, ban hành, thu hồi/hủy ban hành, văn bản đi | `van-ban/di` |
| luồng ký, luồng xử lý, cấu hình bước ký, node | `van-ban/luong-xu-ly` |
| sổ văn bản, số đến/số đi, sổ đơn vị | `van-ban/so-van-ban` |
| liên thông, trục, gửi cơ quan ngoài, VPCP, VOConnect | `van-ban/lien-thong` |
| tìm kiếm văn bản, xem văn bản, bàn giao, phạm vi, loại văn bản, công khai | `van-ban/quan-ly-chung` |
| phiếu trình, tờ trình, xin ý kiến lãnh đạo (không phải văn bản đi) | `phieu-trinh` |
| hồ sơ, kệ, hộp, kho, lưu trữ, nộp lưu | `ho-so-cong-viec` |
| nhiệm vụ đơn vị, nhiệm vụ BGĐ giao, chỉ đạo, tiến độ, gia hạn, đóng nhiệm vụ | `nhiem-vu` |
| công việc cá nhân từ văn bản, phiếu giao việc, đánh giá nhiệm vụ tháng, KI cá nhân | `cong-viec` |
| lịch họp, phòng họp, biên bản, eCabinet, biểu quyết, cầu truyền hình | `hop` |
| ký số, USB token, CloudCA, chứng thư, ảnh chữ ký, đóng dấu | `ky-so` |
| KPI, tiêu chí, chấm điểm, thi đua, báo cáo định kỳ, thống kê | `kpi-danh-gia` |
| nhắc việc, thông báo, SMS, định hướng, nắm tình hình | `lich-nhac-viec` |
| thư viện, biểu mẫu, tài liệu cá nhân, tag | `tai-lieu-mau` |
| người dùng, vai trò, phân quyền, menu, đơn vị, danh mục, cấu hình | `he-thong` |
| VHR, ViettelPay, WOPI (Office online), Solr/ES, mobile, ứng dụng ngoài | `tich-hop` |

## Nguyên tắc giữ bộ tri thức sống

- `ban-do.md` **không bao giờ sửa tay** — chạy `python knowledge/_tools/scan.py && python knowledge/_tools/gen.py`.
- Tri thức viết tay chỉ ghi thứ **không suy ra được từ code**: tại sao, quy tắc nghiệp vụ, bẫy, quyết định.
- Mỗi lần AI/dev bị sửa ("không, ở đây phải làm X") → ghi một dòng vào `dac-thu.md` của phân hệ hoặc `_chung/quy-uoc.md`.
- `❓` = chỗ AI đoán từ code, cần người xác nhận. Xác nhận xong thì xóa dấu.
