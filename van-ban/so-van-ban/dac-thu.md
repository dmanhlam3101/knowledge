# Sổ văn bản — đặc thù

- gen-1 `TextBookAction` (`/textBookAction`) → `controler/*` → `TextBookDAO`; gen-2 `TextBookManagerController` (`/api/text-book`) mới, ít hàm ❓ web đã gọi chưa (xem `ban-do.md` mục 2).
- `TextBookBusiness` (25 hàm) được gọi từ nhiều phân hệ (văn bản đến/đi, migrate, tìm kiếm) — đổi chữ ký hàm ảnh hưởng rộng.
- `document/bookDoc/*` và `bookDispatch/*` là màn **legacy** (`IBookDispatch`, `ISysMenu`) và có màn ☠ (`DocumentBookVM`) — màn sổ thật là `document/textBook/*`.
- Nhiều biến thể `getAllTextBooksOfUserByOrgFor*` phân biệt ngữ cảnh — thêm ngữ cảnh mới = thêm biến thể (hoặc tốt hơn: 1 endpoint gen-2 có tham số).
