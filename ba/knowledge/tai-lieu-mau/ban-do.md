# Bản đồ hệ thống — Thư viện, biểu mẫu, tài liệu cá nhân, từ điển tag

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 18 màn hình, 2 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `library/configlibrary.zul` | `vm.document.DocumentLibraryVM` | `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `library/documentAddLibrary.zul` | `vm.document.DocumentLibraryDetailVM` | — | — | — |
| `library/documentDetails.zul` | `vm.document.DocumentLibraryDetailVM` | — | — | — |
| `library/documentLibrary.zul` | `vm.document.DocumentLibraryVM` | `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `library/documentLibraryTree.zul` | `treeLibrary.vm.DocumentLibraryLookupVM` | — | `IDocumentLibrary` | LEGACY |
| `library/popupLibrary.zul` | `vm.document.DocumentLibraryVM` | `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `templateReport/addTemplateReport.zul` | `vm.template.AddTemplateReportVM` | `DocumentBusiness`, `MissionBusiness`, `OrientationBusiness`, `SearchSolrBusiness` | — | BE |
| `templateReport/configHeading.zul` | `vm.template.ConfigHeadingVM` | — | — | — |
| `templateReport/sendDayReport.zul` | `vm.template.SendDayReportVM` | `MissionBusiness` | — | BE |
| `templateReport/sendReport.zul` | `vm.template.WriteReportVM` | `DocumentBusiness`, `MissionBusiness`, `OrientationBusiness` | `ISysOrganization` | BE+LEGACY |
| `templateReport/summaryReport.zul` | `vm.template.SummaryReportVM` | `MissionBusiness` | — | BE |
| `templateReport/templateDayReport.zul` | `vm.template.SummaryReportVM` | `MissionBusiness` | — | BE |
| `templateReport/writeReport.zul` | `vm.template.WriteReportVM` | `DocumentBusiness`, `MissionBusiness`, `OrientationBusiness` | `ISysOrganization` | BE+LEGACY |
| `widgets/sourceLibraryDocument.zul` | `widget.SourceLibraryDocumentVM` | `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `widgets/sourceLookupDocumentLibrary.zul` | `widget.SourceLookupDocumentLibraryVM` | `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `widgets/template/calendar/templateCalendar_editor.zul` | `vm.meeting.MeetingVM` | `DocumentBusiness`, `MeetingBusiness`, `SearchSolrBusiness`, `SysUserBusiness` | `ICommon`, `IMeeting`, `IMeetingFrequency`, `ISysOrganization`, `ISysUser` | BE+LEGACY |
| `widgets/template/template.zul` | `widget.TemplateVM` | — | — | — |
| `widgets/template/template_viewDetail.zul` | `widget.TemplateVM` | — | — | — |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `treeLibrary.vm.DocumentLibraryTreeModel` | — | `ICommon` | LEGACY |
| `treeLibrary.vm.DocumentLibraryTreeVM` | `DocumentBusiness` | `IDocumentLibrary` | BE+LEGACY |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### TagDictionaryBusiness

`web-spring/src/main/java/com/voffice/service/business/TagDictionaryBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `api.tag-dictionary.delete-tag` | `/api/tag-dictionary/delete-tag` | `TagDictionaryController.deleteTag` | gen2 |
| `api.tag-dictionary.get-build-group-id` | `/api/tag-dictionary/get-build-group-id` | `TagDictionaryController.getBuild` | gen2 |
| `api.tag-dictionary.get-list-org-for-connect` | `/api/tag-dictionary/get-list-org-for-connect` | `TagDictionaryController.getListOrgForConnect` | gen2 |
| `api.tag-dictionary.get-list-selected-tag-in-doc` | `/api/tag-dictionary/get-list-selected-tag-in-doc` | `TagDictionaryController.getListSelectedTagInDoc` | gen2 |
| `api.tag-dictionary.get-list-selected-tag-in-doc-in-group` | `/api/tag-dictionary/get-list-selected-tag-in-doc-in-group` | `TagDictionaryController.getListSelectedTagInDocInGroup` | gen2 |
| `api.tag-dictionary.get-list-selected-tag-in-doc-in-staff` | `/api/tag-dictionary/get-list-selected-tag-in-doc-in-staff` | `TagDictionaryController.getListSelectedTagInDocInStaff` | gen2 |
| `api.tag-dictionary.get-list-tag-doc-manager-doc-in` | `/api/tag-dictionary/get-list-tag-doc-manager-doc-in` | `TagDictionaryController.getListOfTagForDocManagerDocIn` | gen2 |
| `api.tag-dictionary.get-list-tag-for-chosenbox` | `/api/tag-dictionary/get-list-tag-for-chosenbox` | `TagDictionaryController.getListOfTagForChosenBox` | gen2 |
| `api.tag-dictionary.get-list-tag-for-other` | `/api/tag-dictionary/get-list-tag-for-other` | `TagDictionaryController.getListOfTagForOther` | gen2 |
| `api.tag-dictionary.get-list-tag-for-searchbox` | `/api/tag-dictionary/get-list-tag-for-searchbox` | `TagDictionaryController.getListOfTagForSearchBox` | gen2 |
| `api.tag-dictionary.get-receiverIdVof2-by-doc-group-id` | `/api/tag-dictionary/get-receiverIdVof2-by-doc-group-id` | `TagDictionaryController.getReceiverVof2` | gen2 |
| `api.tag-dictionary.get-tag-name-in-doc` | `/api/tag-dictionary/get-tag-name-in-doc` | `TagDictionaryController.getTagNameInDoc` | gen2 |
| `api.tag-dictionary.get-tag-name-in-doc-group` | `/api/tag-dictionary/get-tag-name-in-doc-group` | `TagDictionaryController.getTagNameInDocInGroup` | gen2 |
| `api.tag-dictionary.get-tag-name-in-doc-staff` | `/api/tag-dictionary/get-tag-name-in-doc-staff` | `TagDictionaryController.getTagNameInDocInStaff` | gen2 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### TemplateAction (gen1) — base `/tempAction`, 12 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/TemplateAction.java`

- Logic (gen-1 `controler/`): `TemplateController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `TemplateDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `DOCUMENT_TYPE`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/tempAction/getListTemplate` | `getListTemplate` |
| POST | `/tempAction/addTemplate` | `addTemplate` |
| POST | `/tempAction/editTemplate` | `editTemplate` |
| POST | `/tempAction/deleteTemplate` | `deleteTemplate` |
| POST | `/tempAction/deleteListTemplate` | `deleteListTemplate` |
| POST | `/tempAction/updateIndexTemplate` | `updateIndexTemplate` |
| POST | `/tempAction/addListTemplate` | `addListTemplate` |
| POST | `/tempAction/delete` | `delete` |
| POST | `/tempAction/getTemplateDetail` | `getTemplateDetail` |
| POST | `/tempAction/searchTemplate` | `searchTemplate` |
| POST | `/tempAction/insertTemplate` | `insertTemplate` |
| POST | `/tempAction/updateTemplate` | `updateTemplate` |

</details>

### TagDictionaryController (gen2) — base `/api/tag-dictionary`, 14 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/TagDictionaryController.java`

- Service: `TagDictionaryService`, `TagDictionaryServiceImpl`
- Repository (JPA): `DocumentInGroupRepositoryJPA`, `TagDictionaryJpa`
- Bảng (ước lượng từ SQL/@Table): `DOCUMENT_IN_GROUP`, `TAG_DICTIONARY`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/tag-dictionary/get-list-tag-for-searchbox` | `getListOfTagForSearchBox` |
| POST | `/api/tag-dictionary/get-list-tag-for-chosenbox` | `getListOfTagForChosenBox` |
| POST | `/api/tag-dictionary/delete-tag` | `deleteTag` |
| POST | `/api/tag-dictionary/get-list-selected-tag-in-doc` | `getListSelectedTagInDoc` |
| POST | `/api/tag-dictionary/get-list-tag-doc-manager-doc-in` | `getListOfTagForDocManagerDocIn` |
| POST | `/api/tag-dictionary/get-list-selected-tag-in-doc-in-group` | `getListSelectedTagInDocInGroup` |
| POST | `/api/tag-dictionary/get-list-selected-tag-in-doc-in-staff` | `getListSelectedTagInDocInStaff` |
| POST | `/api/tag-dictionary/get-list-tag-for-other` | `getListOfTagForOther` |
| POST | `/api/tag-dictionary/get-list-org-for-connect` | `getListOrgForConnect` |
| POST | `/api/tag-dictionary/get-tag-name-in-doc` | `getTagNameInDoc` |
| POST | `/api/tag-dictionary/get-tag-name-in-doc-group` | `getTagNameInDocInGroup` |
| POST | `/api/tag-dictionary/get-tag-name-in-doc-staff` | `getTagNameInDocInStaff` |
| POST | `/api/tag-dictionary/get-build-group-id` | `getBuild` |
| POST | `/api/tag-dictionary/get-receiverIdVof2-by-doc-group-id` | `getReceiverVof2` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

| Facade | implements | Service | DAO | Entity (bảng) |
|---|---|---|---|---|
| `DocumentLibraryFacade` | `IDocumentLibrary` | `DocumentLibraryService` | `DocumentLibraryJpaDao` | `Document (DOCUMENT)` |
| `TemplateFacade` | `ITemplate` | `TemplateService` | `TemplateJpaDao` | `Template (TEMPLATE)` |

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `AttachTemplateEntity`→`ATTACH_TEMPLATE`, `DocumentTemplateEntity`→`DOCUMENT_TEMPLATE`, `TagDictionaryEntity`→`TAG_DICTIONARY`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `DocumentLibrary`→`DOCUMENT_LIBRARY`, `DocumentLibraryDetail`→`DOCUMENT_LIBRARY_DETAIL`, `Template`→`TEMPLATE`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH_TEMPLATE`, `DOCUMENT`, `DOCUMENT_IN_GROUP`, `DOCUMENT_LIBRARY`, `DOCUMENT_LIBRARY_DETAIL`, `DOCUMENT_TEMPLATE`, `DOCUMENT_TYPE`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `TAG_DICTIONARY`, `TEMPLATE`, `TEMPLATE_DIRECTING`, `TEMPLATE_ORG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`
