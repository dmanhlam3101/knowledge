# Văn bản đã ban hành — quản lý chung (xem / tìm kiếm / loại / phạm vi / bàn giao / lịch sử / thư viện) — nghiệp vụ

> Những gì dùng chung cho cả văn bản đến và đi **sau khi có số** (`DOCUMENT`), không thuộc riêng luồng đến hay đi. Web `vm/document/*` phần chung (`DocumentViewDetailVM`, `DocumentVM`, `DocumentSendSearchVM`, `viewDoc/`, `seachDoc/`, `managerDoc/`, `editDoc/`, `keyDoc/`, `supervisionDoc/`, `documentScope/`, `document_type/`, `documentHandover/`, `savePersonalDoc/`); BE gen-1 `DocumentAction` (chung), `DocumentHandoverAction`, `commentAction` (lưu cá nhân); gen-2 `DocumentTypeController`, `DocumentHistoryLogController`, `DocumentChatController`, `PersonalCategoryController`, `DocController` (mẫu văn bản, export).

## 1. Chức năng

| Chức năng | Actor | Endpoint / màn |
|---|---|---|
| **Xem chi tiết văn bản** (hub: file, người nhận, luồng, ý kiến, nhắc việc, công việc, họp, hồ sơ, lịch sử) | Mọi người có quyền (`checkPermitViewDocument`, `getDocumentViewerUserId`) | `DocumentViewDetailVM` + `document/viewDoc/*`; `getDocumentDetail`, `getDocumentAttach`, `getListAllFileDocAttach`, `getListCommentFromDocument` |
| **Tìm kiếm** (nâng cao + toàn văn Solr/ES) | Mọi người | `document/seachDoc/*`, `search/search_all.zul` (tìm tất cả: văn bản, họp, nhiệm vụ…), `DocumentAction.search`, `SearchSolrBusiness` (`solrSearch.*`), `ElasticDocument`, menu *Tìm kiếm văn bản*, *Tra cứu văn bản công khai* |
| Văn bản liên quan / trước-sau | | `getDocumentAdjacentList`, `getAdjacentListByDocumentId` (`document.documentAdjacent`), `getRepliedDocumentIds` |
| **Loại văn bản** (`DOCUMENT_TYPE`, gen-2) | Admin | `document-types/search|create|delete`, cấp cho đơn vị (`create-doc-type-org`, `granted-doc-type-to-orgs`), chuyển thành dùng chung (`convert-doc-type-to-common`), thứ tự (`get-max-order-number`); menu *Thể loại văn bản* |
| **Phạm vi văn bản** (`documentScope`) | Admin | `searchDocumentScope`, menu *Quản lý phạm vi văn bản*; giá trị `document.documentScope`: đơn thư / công văn đến tập đoàn / đến đơn vị khác |
| Thông tin/mẫu văn bản (`DocumentInformation`, template) | Admin | gen-2 `CategoryController.get-list-document-information`, `DocController.add-document-template`, `get-document-template-default`, `search-document-template` |
| **Lịch sử văn bản** | | gen-2 `document-history-log/search` (`DOCUMENT_HISTORY_LOG`), `getListDocumentHistory`, `ReportdocumentTransferHistory`, `DocumentCopyHistory` (`document-copy/check-permission` — sao y ❓) |
| **Trao đổi trên văn bản** (chat) | Người liên quan | gen-2 `doc-chat` (`DocumentChatController`), `TextChat` cho dự thảo; web `chat/*`, `BChat` |
| **Bàn giao** | Văn thư/lãnh đạo | `DocumentHandoverAction.*` (xem `van-ban/den`) |
| **Lưu cá nhân / thư viện cá nhân** | Mọi người | `commentAction.savePersonalStorage`, `searchPeronalStorage` (`SavePersonalDocBusiness`), danh mục cá nhân gen-2 `personal-category/*`; menu *Thư viện cá nhân*, TÀI LIỆU CÁ NHÂN |
| Tag văn bản | | `EditDocumentTag`, `EditDocumentInStaffTag`, `EditDocumentInGroupTag`, từ điển tag (`tai-lieu-mau`) |
| Khóa/mở, gia hạn, tách, xóa | Người có quyền | `lockDocument`, `unLockDocument`, `ExtendDocument`, `SplitDocument`, `DeleteDocument` |
| Sao y / bản sao | | `exportDocumentCopy`, `DocumentCopyHistory` |
| Đọc/chưa đọc, % đọc | | `UpdateReadingStatus`, `updateReadingStatusV2`, `get-percent-read-doc` |
| Chia sẻ ra ứng dụng ngoài | | `ext-doc.add-ext-doc`, `check-authorized-to-share` (`ShareExtDocBusiness`, chi tiết `tich-hop`) |

## 2. Quy tắc
- QT1. Quyền xem = người trong luồng nhận + quản lý văn bản + phạm vi (`documentScope`) + độ mật (file mã hóa). Không mở rộng quyền xem bằng cách bỏ kiểm tra `checkPermitViewDocument`.
- QT2. Loại văn bản có thể riêng đơn vị hoặc dùng chung; xóa loại đang dùng bị chặn ❓.
- QT3. Tìm toàn văn phụ thuộc index (Solr/ES) — văn bản mới ban hành phải được index (`indexEmployee` cho người; văn bản qua `ElasticDocument`) ❓ đồng bộ ra sao.
- QT4. Lịch sử là append-only (`DOCUMENT_HISTORY_LOG`).
