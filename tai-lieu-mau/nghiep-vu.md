# Thư viện, biểu mẫu, từ điển tag — nghiệp vụ

> Phân hệ nhỏ, hỗ trợ: **Biểu mẫu/mẫu văn bản** (`TEMPLATE`, gen-1 `tempAction`, web `template/*`, `templateReport/*`, `vm/template`), **Thư viện văn bản/thư viện cấu hình** (`library/*`, `treeLibrary`, `IDocumentLibrary`, menu *Thư viện văn bản*, *Cấu hình thư viện*), **Từ điển tag** (`TAG_DICTIONARY`, gen-2 `TagDictionaryController`), **Tài liệu cá nhân** (xem `van-ban/quan-ly-chung`).

## Chức năng
| Chức năng | Endpoint / màn |
|---|---|
| Quản lý mẫu (thêm/sửa/xóa/sắp xếp, thêm hàng loạt) | `tempAction.getListTemplate`, `addTemplate`, `editTemplate`, `deleteListTemplate`, `updateIndexTemplate`, `addListTemplate`, `searchTemplate` (`TemplateAction`, gen-1); web `vm/template/*` (5 VM), facade `ITemplate` |
| Mẫu báo cáo (in/xuất) | `templateReport/*.zul` (9), `com.viettel.report.template`, `com.viettel.util.exporter` (Excel/PDF/Word) |
| Mẫu văn bản mặc định theo loại (gen-2) | `DocController.add-document-template`, `get-document-template-default`, `search-document-template`; cột `ATTACH_TEMPLATE` (SQL `01062026_add_column_attach_template.sql`) |
| Thư viện văn bản (tra cứu văn bản công khai/đã ban hành theo cây) | `library/*.zul` (9), `treeLibrary.vm`, `DocumentAction.actionSearchDocViewLibrary`, `IDocumentLibrary`, menu *Thư viện văn bản*, *Tra cứu văn bản công khai* |
| Từ điển tag: tag cho văn bản/nhóm/người, gợi ý ô tìm kiếm | `tag-dictionary/get-list-tag-for-searchbox`, `get-list-tag-for-chosenbox`, `get-list-selected-tag-in-doc(-in-group/-in-staff)`, `get-tag-name-in-doc*`, `delete-tag`, `get-list-org-for-connect`, `get-build-group-id` (`TagDictionaryBusiness`, 14 hàm) |

## Quy tắc
- QT1. Mẫu có thứ tự hiển thị (`updateIndexTemplate`) và thuộc đơn vị/loại ❓.
- QT2. Tag gắn theo 3 mức: văn bản, văn bản-nhóm, văn bản-người (`EditDocumentTag`, `EditDocumentInGroupTag`, `EditDocumentInStaffTag` ở `DocumentAction`).
- QT3. Thư viện chỉ hiển thị văn bản đã công khai hoặc trong phạm vi được cấp.

## ❓
1. "Cấu hình thư viện" (menu quản trị) cấu hình cây thư mục hay quyền xem?
2. Mẫu văn bản (docx) có tích hợp WOPI để soạn thảo online không (`tich-hop`)?
