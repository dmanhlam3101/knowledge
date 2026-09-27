# Thư viện, biểu mẫu, tag — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Autocomplete/gợi ý tag cho ô tìm kiếm & chosenbox (gen-2) | `TagDictionaryController.get-list-tag-for-searchbox`, `get-list-tag-for-chosenbox` ← `TagDictionaryBusiness` ← widget tìm kiếm trong `DocumentSendSearchVM` |
| Gắn tag cho đối tượng ở 3 mức | `DocumentAction.EditDocumentTag / EditDocumentInGroupTag / EditDocumentInStaffTag` + `get-list-selected-tag-in-doc*` |
| CRUD mẫu có sắp thứ tự & thao tác hàng loạt (gen-1) | `TemplateAction.addListTemplate`, `deleteListTemplate`, `updateIndexTemplate` ← `vm/template` |
| Xuất Excel/PDF/Word từ dữ liệu | `com.viettel.util.exporter.*` + `templateReport/*.zul` (vd. `RequisitionReportVM` dùng exporter) |
| Cây thư viện | `treeLibrary.vm.*` + `library/*.zul` |
