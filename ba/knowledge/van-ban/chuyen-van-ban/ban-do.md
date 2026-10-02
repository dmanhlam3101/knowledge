# Bản đồ hệ thống — Chuyển văn bản – mọi luồng chuyển (đến: chuyển xử lý; đi: chuyển sau ban hành; tự động chuyển; giới hạn chuyển)

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 19 màn hình, 0 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `config/docAutoSendDocumentAdd_popup.zul` | `vm.config.DocumentProcessAutoSendConfigPopupVM` | `DocumentProcessTermBusiness`, `RequisitionBusiness` | — | BE |
| `config/docAutoSendDocumentConfig.zul` | `vm.config.DocumentProcessAutoSendConfigVM` | `DocumentProcessTermBusiness`, `RequisitionBusiness` | — | BE |
| `document/process/popupViewFlowDetail.zul` | `vm.document.PopupViewFlowDetailVM` | `DocumentBusiness` | — | BE |
| `document/process/viewFlow.zul` | `vm.document.PopupViewFlowVM` | `AnswerDocumentBusiness` | — | BE |
| `document/process/viewFlow_v2.zul` | `vm.document.PopupViewFlowVM` | `AnswerDocumentBusiness` | — | BE |
| `document/reportSendReceiveDoc/popUpMoveList.zul` | `vm.document.DocumentLookUpMoveList` | `DocumentBusiness` | — | BE |
| `document/transferDoc/configLimitTransfer.zul` | `vm.document.ConfigLimitTransferVM` | — | — | — |
| `document/transferDoc/popupTransferError.zul` | `vm.document.PopupTransferErrorVM` | — | — | — |
| `document/transferDoc/transferBriefDoc.zul` | `vm.document.TransferBriefDocVM` | `DocumentBusiness`, `EnterpriseBusiness`, `SearchSolrBusiness` | — | BE |
| `document/transferDoc/transferDoc.zul` | `vm.document.TransferDocumentVM` | `CVGroupBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `MissionIntegrationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferDoc_flow.zul` | `vm.document.TransferDocumentVM` | `CVGroupBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `MissionIntegrationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferDoc_flow_multi.zul` | `vm.document.TransferDocumentMultipleVM` | `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `MissionBusiness`, `MissionIntegrationBusiness`, `SearchSolrBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferDoc_multi.zul` | `vm.document.TransferDocumentVM` | `CVGroupBusiness`, `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `GraspSituationBusiness`, `MeetingAssistantBusiness`, `MissionBusiness`, `MissionIntegrationBusiness`, `RequisitionBusiness`, `SearchSolrBusiness`, `VhrEmployeeBusiness` | `ISysOrganization` | BE+LEGACY |
| `document/transferDoc/transferFinanceDoc.zul` | `vm.document.TransferFinanceDocumentVM` | `DocumentBusiness` | — | BE |
| `document/transferDoc/transferGroupEditor.zul` | `vm.document.DocumentGroupEditorVM` | `CVGroupBusiness`, `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `document/transferDoc/transferGroupEditor_vbd.zul` | `vm.document.DocumentGroupEditorVM` | `CVGroupBusiness`, `DocumentBusiness`, `RequisitionBusiness` | — | BE |
| `document/transferDoc/transfer_doc_in_flow.zul` | `vm.document.TransferDocumentInVM` | `ConnectDocumentBusiness`, `ConnectVHRBusiness`, `DocumentBusiness`, `DocumentRequestBusiness`, `EnterpriseBusiness`, `MissionIntegrationBusiness`, `SearchSolrBusiness` | — | BE |
| `document/transferDoc/viewListEmployee.zul` | `vm.document.TransferDocViewLstEmployeeVM` | — | — | — |
| `widgets/multiTypeObjectLookup.zul` | `widget.MultiTypeObjectLookupVM` | `ConnectDocumentBusiness` | `ISysOrganization` | BE+LEGACY |

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

_Không có Business riêng — màn hình phân hệ này dùng Business của phân hệ khác (xem cột "Gọi BE qua" ở mục 1)._

## 3. BE — Controller → logic / service → DAO / repository → bảng

### DocumentProcessTermConfigAction (gen1) — base `/documentProcessTermConfig`, 13 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/DocumentProcessTermConfigAction.java`

- Logic (gen-1 `controler/`): `DocumentProcessTermController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `DocumentRequestConfigDAO`
- Bảng (ước lượng từ SQL/@Table): `CONFIG_AUTO_SEND_DOCUMENT`, `DOCUMENT_REQUEST_CONFIG`, `DOCUMENT_REQUEST_CONFIG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/documentProcessTermConfig/addOrUpdateConfig` | `addOrUpdateConfig` |
| POST | `/documentProcessTermConfig/addOrUpdateAutoSendConfig` | `addOrUpdateAutoSendConfig` |
| POST | `/documentProcessTermConfig/getConfigs` | `getConfigs` |
| POST | `/documentProcessTermConfig/getAutoSendConfigs` | `getAutoSendConfigs` |
| POST | `/documentProcessTermConfig/getListAutoSendConfigs` | `getListAutoSendConfigs` |
| POST | `/documentProcessTermConfig/getOwnerConfigs` | `getOwnerConfigs` |
| POST | `/documentProcessTermConfig/getEmployeeStatus` | `getEmployeeStatus` |
| POST | `/documentProcessTermConfig/getConfigsByCondition` | `getConfigsByCondition` |
| POST | `/documentProcessTermConfig/getConfigsByListOrgIds` | `getConfigsByListOrgIds` |
| POST | `/documentProcessTermConfig/deleteConfig` | `deleteConfig` |
| POST | `/documentProcessTermConfig/saveAutoProcessSetting` | `saveAutoProcessSetting` |
| POST | `/documentProcessTermConfig/deleteAutoSendConfig` | `deleteAutoSendConfig` |
| POST | `/documentProcessTermConfig/getConfigDetail` | `getConfigDetail` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

_Không có facade legacy riêng._

## 5. Entity / bảng DB thuộc phân hệ

**Tổng hợp bảng chạm tới**: `CONFIG_AUTO_SEND_DOCUMENT`, `DOCUMENT_REQUEST_CONFIG`, `DOCUMENT_REQUEST_CONFIG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`
