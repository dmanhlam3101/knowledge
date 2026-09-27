# Thư viện, biểu mẫu, tag — đặc thù

- Mẫu = gen-1 (`TemplateAction` `/tempAction`, 12 endpoint) + facade legacy `ITemplate` (web `TemplateFacade`) → 2 đường đọc bảng `TEMPLATE`. Tag = gen-2 thuần (`TagDictionaryController`, 14 endpoint, không có gen-1) — mẫu gen-2 tốt cho "danh mục gợi ý/autocomplete".
- Thư viện dùng `IDocumentLibrary` (legacy) trong `DocumentPublishVM`, `treeLibrary.vm.*` — nhãn LEGACY/BE+LEGACY.
- Xuất báo cáo (`exporter`, `report/template`) là code web thuần Java 8 (POI/iText) — không qua BE; thêm mẫu xuất mới = thêm class trong `com.viettel.util.exporter` + zul trong `templateReport/`.
- `TemplateFilter` (web `http/`) xử lý URL mẫu ❓.
