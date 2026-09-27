# Thống kê theo phân hệ

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).

| Phân hệ | Màn hình | VM khác | Business | Controller BE | Facade legacy | Bảng DB |
|---|---|---|---|---|---|---|
| [van-ban/den](../../van-ban/den/ban-do.md) | 71 | 0 | 1 | 6 | 0 | 128 |
| [van-ban/di](../../van-ban/di/ban-do.md) | 47 | 10 | 3 | 9 | 1 | 227 |
| [van-ban/luong-xu-ly](../../van-ban/luong-xu-ly/ban-do.md) | 7 | 0 | 2 | 2 | 1 | 103 |
| [van-ban/so-van-ban](../../van-ban/so-van-ban/ban-do.md) | 7 | 0 | 1 | 2 | 1 | 22 |
| [van-ban/lien-thong](../../van-ban/lien-thong/ban-do.md) | 6 | 0 | 2 | 5 | 0 | 186 |
| [van-ban/quan-ly-chung](../../van-ban/quan-ly-chung/ban-do.md) | 32 | 1 | 10 | 11 | 3 | 317 |
| [phieu-trinh](../../phieu-trinh/ban-do.md) | 23 | 3 | 2 | 2 | 0 | 134 |
| [ho-so-cong-viec](../../ho-so-cong-viec/ban-do.md) | 34 | 4 | 6 | 9 | 0 | 167 |
| [nhiem-vu](../../nhiem-vu/ban-do.md) | 61 | 8 | 6 | 10 | 2 | 207 |
| [cong-viec](../../cong-viec/ban-do.md) | 30 | 3 | 3 | 3 | 2 | 155 |
| [hop](../../hop/ban-do.md) | 60 | 6 | 5 | 10 | 7 | 198 |
| [ky-so](../../ky-so/ban-do.md) | 2 | 0 | 0 | 8 | 1 | 220 |
| [kpi-danh-gia](../../kpi-danh-gia/ban-do.md) | 28 | 3 | 8 | 7 | 8 | 70 |
| [lich-nhac-viec](../../lich-nhac-viec/ban-do.md) | 19 | 1 | 4 | 5 | 4 | 33 |
| [tai-lieu-mau](../../tai-lieu-mau/ban-do.md) | 18 | 2 | 1 | 2 | 2 | 17 |
| [he-thong](../../he-thong/ban-do.md) | 78 | 3 | 14 | 30 | 8 | 261 |
| [tich-hop](../../tich-hop/ban-do.md) | 8 | 2 | 8 | 20 | 1 | 247 |
| [_chung](../../_chung/ban-do.md) | 95 | 12 | 3 | 4 | 3 | 212 |

Tổng: 626 màn hình có VM, 556 VM, 79 Business với 1153 hàm gọi BE (1146 nối được endpoint), 145 controller BE / 1737 endpoint, 44 facade legacy.
