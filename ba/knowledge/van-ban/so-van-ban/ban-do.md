# Bản đồ hệ thống — Sổ văn bản

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 9 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `document/bookDispatch/dispatch_Book_List.zul` | `vm.document.BookDispatchVM` | — | `IBookDispatch` | LEGACY |
| `document/bookDoc/bookContentDoc.zul` | `widget.SysMenuLookupVM` | — | `ISysMenu` | LEGACY |
| `document/bookDoc/bookDoc.zul` | `vps.vm.SysMenuVM` | — | `ISysMenu` | LEGACY |
| `document/bookDoc/documentBook.zul` | `vm.document.DocumentBookVM` | — | — | ☠ VM không tồn tại |
| `document/reportSendReceiveDoc/dispatch_Book_List.zul` | `vm.document.BookDispatchVM` | — | `IBookDispatch` | LEGACY |
| `document/reportSendReceiveDoc/lookUpDispatchDocument.zul` | `vm.document.BookDispatchVM` | — | `IBookDispatch` | LEGACY |
| `document/textBook/textBook.zul` | `vm.document.TextBookVM` | `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/textBook/textBook_detail.zul` | `vm.document.TextBookVM` | `RequisitionBusiness`, `TextBookBusiness` | — | BE |
| `document/textBook/textBook_inspect.zul` | `vm.document.TextBookVM` | `RequisitionBusiness`, `TextBookBusiness` | — | BE |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### TextBookBusiness

`web-spring/src/main/java/com/voffice/service/business/TextBookBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `textBookAction.checkExistDefaultTextBook` | `/textBookAction/checkExistDefaultTextBook` | `TextBookAction.checkExistDefaultTextBook` | gen1 |
| `textBookAction.checkExistTextBook` | `/textBookAction/checkExistTextBook` | `TextBookAction.checkExistTextBook` | gen1 |
| `textBookAction.checkIsDefaultTextBook` | `/textBookAction/checkIsDefaultTextBook` | `TextBookAction.checkIsDefaultTextBook` | gen1 |
| `textBookAction.checkUsedTextBook` | `/textBookAction/checkUsedTextBook` | `TextBookAction.checkUsedTextBook` | gen1 |
| `textBookAction.createDefaultTextBookForOrgs` | `/textBookAction/createDefaultTextBookForOrgs` | `TextBookAction.createDefaultTextBookForOrgs` | gen1 |
| `textBookAction.deleteTextBook` | `/textBookAction/deleteTextBook` | `TextBookAction.deleteTextBook` | gen1 |
| `textBookAction.findListTextBooks` | `/textBookAction/findListTextBooks` | `TextBookAction.findListTextBooks` | gen1 |
| `textBookAction.getAllTextBooksOfUser` | `/textBookAction/getAllTextBooksOfUser` | `TextBookAction.getAllTextBooksOfUser` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrg` | `/textBookAction/getAllTextBooksOfUserByOrg` | `TextBookAction.getAllTextBooksOfUserByOrg` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgForDocIn` | `/textBookAction/getAllTextBooksOfUserByOrgForDocIn` | `TextBookAction.getAllTextBooksOfUserByOrgForDocIn` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgForDocInNotDocManagerWithTime` | `/textBookAction/getAllTextBooksOfUserByOrgForDocInNotDocManagerWithTime` | `TextBookAction.getAllTextBooksOfUserByOrgForDocInNotDocManagerWithTime` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgForDocOut` | `/textBookAction/getAllTextBooksOfUserByOrgForDocOut` | `TextBookAction.getAllTextBooksOfUserByOrgForDocOut` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgForDocOutNotDocManager` | `/textBookAction/getAllTextBooksOfUserByOrgForDocOutNotDocManager` | `TextBookAction.getAllTextBooksOfUserByOrgForDocOutNotDocManager` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgForDocOutNotDocManagerWithTime` | `/textBookAction/getAllTextBooksOfUserByOrgForDocOutNotDocManagerWithTime` | `TextBookAction.getAllTextBooksOfUserByOrgForDocOutNotDocManagerWithTime` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgForDocOutPublished` | `/textBookAction/getAllTextBooksOfUserByOrgForDocOutPublished` | `TextBookAction.getAllTextBooksOfUserByOrgForDocOutPublished` | gen1 |
| `textBookAction.getAllTextBooksOfUserByOrgWithOutDocManager` | `/textBookAction/getAllTextBooksOfUserByOrgWithOutDocManager` | `TextBookAction.getAllTextBooksOfUserByOrgWithOutDocManager` | gen1 |
| `textBookAction.getListDocumentTypeActive` | `/textBookAction/getListDocumentTypeActive` | `TextBookAction.getListDocumentTypeActive` | gen1 |
| `textBookAction.getNextRegisterNumberByTextBookId` | `/textBookAction/getNextRegisterNumberByTextBookId` | `TextBookAction.getNextRegisterNumberByTextBookId` | gen1 |
| `textBookAction.getShareOrgs` | `/textBookAction/getShareOrgs` | `TextBookAction.getShareOrgs` | gen1 |
| `textBookAction.getTextBooksByOrgIdAndDocType` | `/textBookAction/getTextBooksByOrgIdAndDocType` | `TextBookAction.getTextBooksByOrgIdAndDocType` | gen1 |
| `textBookAction.getTextBooksOfUser` | `/textBookAction/getTextBooksOfUser` | `TextBookAction.getTextBooksOfUser` | gen1 |
| `textBookAction.getTextBooksOfUserByDocType` | `/textBookAction/getTextBooksOfUserByDocType` | `TextBookAction.getTextBooksOfUserByDocType` | gen1 |
| `textBookAction.insertTextBook` | `/textBookAction/insertTextBook` | `TextBookAction.insertTextBook` | gen1 |
| `textBookAction.inspectTextBook` | `/textBookAction/inspectTextBook` | `TextBookAction.inspectTextBook` | gen1 |
| `textBookAction.toggleLockTextBook` | `/textBookAction/toggleLockTextBook` | `TextBookAction.toggleLockTextBook` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### TextBookAction (gen1) — base `/textBookAction`, 25 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TextBookAction.java`

- Logic (gen-1 `controler/`): `TextBookController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `OrgDAO`, `TextBookDAO`
- Bảng (ước lượng từ SQL/@Table): `DATA_SOURCE`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_TYPE`, `EMPLOYEE_TYPE_PROCESS`, `FILTERED_DATA`, `HAS_DEFAULT`, `IMAGE_ORG`, `STAFF_GROUP_ROLE`, `SYSDATE`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_PROCESS`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/textBookAction/insertTextBook` | `insertTextBook` |
| POST | `/textBookAction/checkExistTextBook` | `checkExistTextBook` |
| POST | `/textBookAction/findListTextBooks` | `findListTextBooks` |
| POST | `/textBookAction/getShareOrgs` | `getShareOrgs` |
| POST | `/textBookAction/deleteTextBook` | `deleteTextBook` |
| POST | `/textBookAction/toggleLockTextBook` | `toggleLockTextBook` |
| POST | `/textBookAction/getNextRegisterNumberByTextBookId` | `getNextRegisterNumberByTextBookId` |
| POST | `/textBookAction/getTextBooksByOrgIdAndDocType` | `getTextBooksByOrgIdAndDocType` |
| POST | `/textBookAction/getTextBooksOfUser` | `getTextBooksOfUser` |
| POST | `/textBookAction/createDefaultTextBookForOrgs` | `createDefaultTextBookForOrgs` |
| POST | `/textBookAction/inspectTextBook` | `inspectTextBook` |
| POST | `/textBookAction/checkUsedTextBook` | `checkUsedTextBook` |
| POST | `/textBookAction/checkIsDefaultTextBook` | `checkIsDefaultTextBook` |
| POST | `/textBookAction/getTextBooksOfUserByDocType` | `getTextBooksOfUserByDocType` |
| POST | `/textBookAction/getAllTextBooksOfUser` | `getAllTextBooksOfUser` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrg` | `getAllTextBooksOfUserByOrg` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgForDocOut` | `getAllTextBooksOfUserByOrgForDocOut` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgForDocIn` | `getAllTextBooksOfUserByOrgForDocIn` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgForDocOutPublished` | `getAllTextBooksOfUserByOrgForDocOutPublished` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgWithOutDocManager` | `getAllTextBooksOfUserByOrgWithOutDocManager` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgForDocOutNotDocManager` | `getAllTextBooksOfUserByOrgForDocOutNotDocManager` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgForDocOutNotDocManagerWithTime` | `getAllTextBooksOfUserByOrgForDocOutNotDocManagerWithTime` |
| POST | `/textBookAction/getAllTextBooksOfUserByOrgForDocInNotDocManagerWithTime` | `getAllTextBooksOfUserByOrgForDocInNotDocManagerWithTime` |
| POST | `/textBookAction/checkExistDefaultTextBook` | `checkExistDefaultTextBook` |
| POST | `/textBookAction/getListDocumentTypeActive` | `getListDocumentTypeActive` |

</details>

### TextBookManagerController (gen2) — base `/api/text-book`, 4 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TextBookManagerController.java`

- Service: `TextBookService`, `TextBookServiceImpl`
- Repository (JPA): `DocumentRepositoryJPA`, `WaitingNumberBookRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `WAITING_NUMBER_BOOK`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/text-book/get-list-waiting-number` | `getListWaitingNumber` |
| POST | `/api/text-book/add-waiting-number` | `addWaitingNumber` |
| POST | `/api/text-book/delete-waiting-number/{id}` | `deleteWaitingNumber` |
| POST | `/api/text-book/edit-waiting-number/{id}` | `editWaitingNumber` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `BookDispatchFacade` | `IBookDispatch` | `BookDisPatchService` | `BookDispatchJpaDao` | `BookDispatch (BOOK_DISPATCH)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `TextBookEntity`→`TEXT_BOOK`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `BookDispatch`→`BOOK_DISPATCH`

**Tổng hợp bảng chạm tới**: `BOOK_DISPATCH`, `DATA_SOURCE`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_TYPE`, `EMPLOYEE_TYPE_PROCESS`, `FILTERED_DATA`, `HAS_DEFAULT`, `IMAGE_ORG`, `STAFF_GROUP_ROLE`, `SYSDATE`, `TEXT`, `TEXTBOOK_DOC`, `TEXT_BOOK`, `TEXT_BOOK_NUMBER`, `TEXT_BOOK_SHARE`, `TEXT_PROCESS`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`, `WAITING_NUMBER_BOOK`
