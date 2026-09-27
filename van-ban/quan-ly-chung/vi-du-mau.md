# Văn bản — quản lý chung — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Danh mục có cấp phát cho đơn vị / chuyển dùng chung (gen-2) | `DocumentTypeController` (`create-doc-type-org`, `granted-doc-type-to-orgs`, `convert-doc-type-to-common`, `get-by-organization`) ← `DocumentTypeBusiness` ← `vm/document` ❓ `DocumentTypeVM` / `document_type/document_type.zul` |
| Log lịch sử append-only + tìm kiếm (gen-2) | `DocumentHistoryLogController.search`, entity `DocumentHistoryLogEntity` ← `DocumentHistoryLogBusiness` |
| Chat/ghi chú gắn đối tượng (gen-2) | `DocumentChatController` (GET/POST/DELETE `doc-chat`) ← `DocumentBusiness` `api.doc-chat*` ← `vm/chat` |
| Danh mục cá nhân + lưu đối tượng vào danh mục | gen-2 `PersonalCategoryController` + gen-1 `commentAction.savePersonalStorage` ← `PersonalDocCategoryBusiness`, `SavePersonalDocBusiness` ← `savePersonalDoc/*.zul` |
| Popup xem chi tiết văn bản từ bất kỳ đâu | `LookupUtil.showDialog(... "/view/voffice/document/viewDoc/…zul" ...)` + `DocumentViewDetailVM` nhận `documentId` qua `ZkUtil.getParameter` |
| Tìm kiếm tất cả (cross-domain) | `search/search_all.zul` + `vm/search/*` → `HomeController.search-all` (gen-2) + `solrSearch.getListItem` |
| Lookup chọn văn bản (sống) | `widget/SourceLookupDocument*` còn tồn tại — tra `_chung/ban-do.md` mục 1 (không ☠) |
