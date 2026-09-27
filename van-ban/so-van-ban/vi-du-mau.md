# Sổ văn bản — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Màn quản lý sổ (list/detail/inspect trong 1 VM) | `document/textBook/textBook.zul`, `textBook_detail.zul`, `textBook_inspect.zul` + `vm/document/TextBookVM` → `TextBookBusiness` |
| Lấy số tiếp theo khi cấp số | `TextBookBusiness.getNextRegisterNumberByTextBookId` ← `RequisitionViewIssueNumberVM` (`van-ban/di`) |
| Combobox sổ theo ngữ cảnh | `getAllTextBooksOfUserByOrgForDocIn` / `ForDocOut` ← `InputDocument*VM`, `RequisitionVM` |
| Khóa/mở + chặn xóa khi đã dùng | `toggleLockTextBook`, `checkUsedTextBook` |
