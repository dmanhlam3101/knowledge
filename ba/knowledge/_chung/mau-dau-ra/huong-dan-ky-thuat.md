# MẪU: Hướng dẫn kỹ thuật cho dev

> Xuất kèm giải pháp BA. Mục tiêu: dev mở đúng file, làm đúng tầng, theo đúng pattern. Mọi đường dẫn phải là đường dẫn thật (đã kiểm tra tồn tại). Chỗ đoán đánh `❓`.

---

# [Tên yêu cầu] — hướng dẫn kỹ thuật

**Phân hệ:** … · **Tầng chạm tới:** Web / BE gen-1 / BE gen-2 / DB · **Loại việc:** thêm tính năng mới / sửa cũ / thêm trường / thêm API
**Cách làm chuẩn áp dụng:** `_chung/cach-lam-chuan/<file>.md`

## 1. Hiện trạng kỹ thuật (từ `ban-do.md`)
| Thành phần | Đường dẫn | Nhãn | Ghi chú |
|---|---|---|---|
| Màn hình | `web-spring/src/main/webapp/view/voffice/...zul` | BE / LEGACY / BE+LEGACY | |
| ViewModel | `web-spring/src/main/java/com/viettel/voffice/vm/...VM.java` | | |
| Business → endpoint | `XxxBusiness.fn` → `/a/b` → `XxxController.method` (gen-1/2) | | |
| Logic/Service | … | | |
| DAO/Repository → bảng | … → `TABLE_A`, `TABLE_B` | | |

## 2. Thiết kế thay đổi
### 2.1 DB
```sql
-- file: backend2.0/backendvoffice/sql/<DDMMYYYY>_<mo_ta>.sql
```
### 2.2 BE
| Bước | File (mới/sửa) | Nội dung |
|---|---|---|
| 1 | `entities/XxxEntity.java` (mới) | … |
| 2 | `repositories/jpa/XxxRepositoryJPA.java` (mới) | … |
| 3 | `services/impl/XxxServiceImpl.java` (mới) | … |
| 4 | `controller/XxxController.java` (mới) — `POST /api/xxx/...` | … |
| 5 | (nếu sửa gen-1) `controler/TextController.java#method` | thêm hàm `...V2`, không đổi hàm cũ |

Ký hợp đồng API (request/response JSON mẫu):
```json
```

### 2.3 Web
| Bước | File | Nội dung |
|---|---|---|
| 1 | `com/voffice/service/business/XxxBusiness.java` | hàm `...` gọi `"api.xxx...."` |
| 2 | `vm/<domain>/XxxVM.java` | `@Command ...` |
| 3 | `view/voffice/<domain>/xxx.zul` | … |
| 4 | `common_voffice_vi.properties` | key … |
| 5 | SQL `SYS_MENU` + `ROLE_MENU` (+ `ORG_SYS_MENU` nếu chỉ mở cho một số đơn vị) (nếu màn hình mới) | `he-thong/dac-thu.md` bẫy 6–7 |
| 6 | Điều kiện hiện nút trong VM (quyền) | BE không kiểm người gọi — kiến trúc tổng thể bẫy 6 |

## 3. Mẫu code để copy
- Tính năng tương tự đã có: `knowledge/<phanhe>/vi-du-mau.md` → mục "…"
- Class mẫu: `…`

## 4. Kiểm thử
- Case chính: …
- Case biên / phân quyền: …
- Màn hình/endpoint khác dùng chung phải chạy lại: …

## 5. Rủi ro & lưu ý
- Từ `knowledge/<phanhe>/dac-thu.md`: …
- Nợ kỹ thuật tạo ra (nếu có): …

## 6. Việc cần người khác
- DBA: chạy SQL … · Admin: gán menu/quyền … · BA: xác nhận ❓ …
