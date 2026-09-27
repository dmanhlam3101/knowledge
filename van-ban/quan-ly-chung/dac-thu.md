# Văn bản — quản lý chung — đặc thù

- Đây là "phân hệ kỹ thuật" gom phần dùng chung; phần lớn hàm nằm trong `DocumentBusiness` (178 hàm, xếp ở `van-ban/den`) và `DocumentAction` gen-1. `ban-do.md` của folder này liệt kê 10 Business nhỏ (loại văn bản, lịch sử, chat, lưu cá nhân, Solr, chia sẻ ngoài…) và 11 controller.
- `DocumentViewDetailVM` là **hub lớn nhất web** — mọi phân hệ nhúng vào đây (nhắc việc, công việc, họp, hồ sơ, ký, liên thông). Sửa nó = test toàn hệ thống. Ưu tiên thêm popup/VM riêng và nhúng, thay vì thêm code vào VM này.
- Tìm kiếm: 2 engine (Solr gen-1 `SolrSearchResource`, Elasticsearch `ElasticDocument*`/`els_query/`) ❓ cái nào đang sản xuất; `application-prod.properties` có `elasticsearch.host`.
- Loại văn bản đã lên gen-2 (`DocumentTypeController`) nhưng gen-1 vẫn có `DocumentService.getAllListDocumentTypes`, `getListDocTypes`, `textBookAction.getListDocumentTypeActive` — 3 nguồn đọc cùng bảng `DOCUMENT_TYPE`.
- Facade legacy còn dùng: `IDocument`, `IDocumentLibrary`, `IDocumentPublicStatus`, `IDocumentHandoverHistory`, `IFileAttachment` (`DocumentFacade` → `DocumentService` → `DocumentJpaDao`…) — web entity `Document`, `DocumentFile`, `DocumentArchive` map thẳng bảng `DOCUMENT*`.
- Màn ☠: `DocumentHandoverVM`, `DocumentHandoverHistoryVM`, `vps.vm.DocumentVM`, `SourceLookupDocumentVM2/3`, `SourceLookupDocumentOut`, `PopupTrackingDocument`, `InfoHastagDoc` — lookup văn bản cũ đã chết; lookup sống nằm trong `widget/` (xem `_chung/ban-do.md`).
