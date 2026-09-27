# Sổ văn bản — nghiệp vụ

> Sổ văn bản (`TEXT_BOOK`) là nơi **cấp số** cho văn bản đến (số đến) và văn bản đi (số đi). Mỗi đơn vị có nhiều sổ theo loại văn bản / năm; văn thư quản lý. Web `document/textBook/*` (3 zul, `TextBookVM`), `document/bookDoc`, `bookDispatch` (legacy/☠); BE gen-1 `textBookAction` (`TextBookAction`, 25 endpoint); gen-2 `TextBookManagerController` (`/api/text-book`).

## Actor & thao tác
| Actor | Thao tác |
|---|---|
| Văn thư đơn vị | Tạo sổ (`insertTextBook`, kiểm tra trùng `checkExistTextBook`), sổ mặc định (`checkExistDefaultTextBook`, `checkIsDefaultTextBook`, `createDefaultTextBookForOrgs`), khóa/mở sổ (`toggleLockTextBook`), xóa (chặn nếu đã dùng `checkUsedTextBook`, `deleteTextBook`), chia sẻ sổ cho đơn vị con (`getShareOrgs`), kiểm tra sổ (`inspectTextBook` — `textBook_inspect.zul`) |
| Người cấp số | Lấy số tiếp theo (`getNextRegisterNumberByTextBookId`), chọn sổ theo ngữ cảnh: đến (`getAllTextBooksOfUserByOrgForDocIn*`), đi (`...ForDocOut*`, `...ForDocOutPublished`), có/không quản lý văn bản (`...NotDocManager`), theo loại (`getTextBooksByOrgIdAndDocType`, `getListDocumentTypeActive`) |
| Mọi người | Tra cứu sổ (`findListTextBooks`, `getTextBooksOfUser`), menu *Sổ văn bản đơn vị*, *Danh mục sổ văn bản*, *Thể loại văn bản* |

## Quy tắc
- QT1. Số trong một sổ tăng dần, duy nhất theo năm; trùng bị chặn (`is-duplicated-register-book-number` ở `van-ban/den`, `DocumentAction.GetRegisterNumberIndex`).
- QT2. Sổ bị khóa không cấp số được; sổ đã có văn bản không xóa được.
- QT3. Mỗi đơn vị phải có sổ mặc định; hệ thống có thể tạo hàng loạt cho các đơn vị (`createDefaultTextBookForOrgs`).
- QT4. Cấp số có hàng chờ (`WaitingNumberBookEntity`, `VBCCS` "chờ cấp số") — tránh trùng khi nhiều người cấp cùng lúc ❓ cơ chế khóa.
- QT5. "Người quản lý văn bản" (`HAVE_DOC_MANAGER`, `NotDocManager`) thấy sổ khác với người thường.

## ❓
1. Đánh số lại đầu năm thực hiện thế nào (tự động theo năm hay tạo sổ mới)?
2. Số văn bản có dạng mẫu (vd. `123/UBND-VP`) sinh từ đâu — sổ hay loại văn bản?
