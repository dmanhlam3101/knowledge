# Bản đồ hệ thống — Hồ sơ công việc & lưu trữ (kệ / hộp / kho)

> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.
> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · **BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.
> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).


## 1. Màn hình (web)

Tổng: 35 màn hình, 4 VM không gắn zul trực tiếp.

| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |
|---|---|---|---|---|
| `boxManagement/boxManagement.zul` | `vm.boxs.BoxsVM` | `BoxsBusiness`, `StoragesBusiness` | — | BE |
| `brief/brief.zul` | `vm.brief.BriefVM` | `BoxsBusiness`, `BriefBusiness`, `CatalogBriefBusiness`, `DocumentBusiness`, `NotificationBusiness`, `StoragesBusiness` | `ISysUser` | BE+LEGACY |
| `brief/briefProcessing.zul` | `vm.brief.BriefVM` | `BoxsBusiness`, `BriefBusiness`, `CatalogBriefBusiness`, `DocumentBusiness`, `NotificationBusiness`, `StoragesBusiness` | `ISysUser` | BE+LEGACY |
| `brief/brief_borrow_list.zul` | `vm.brief.BorrowListBriefVM` | `BriefBusiness` | — | BE |
| `brief/brief_borrow_manager.zul` | `vm.brief.BorrowBriefVM` | `BriefBusiness` | — | BE |
| `brief/brief_info.zul` | `vm.brief.BriefInfoVM` | `AnswerDocumentBusiness`, `BriefBusiness`, `DocumentBusiness`, `DocumentPublishBusiness`, `RequisitionBusiness` | `ISysOrganization` | BE+LEGACY |
| `brief/brief_update.zul` | `vm.brief.BriefUpdateVM` | `BoxsBusiness`, `BriefBusiness`, `CatalogBriefBusiness`, `DocumentBusiness`, `StoragesBusiness` | `ISysOrganization` | BE+LEGACY |
| `brief/catalogBrief.zul` | `vm.brief.CatalogBriefVM` | `BriefBusiness`, `CatalogBriefBusiness`, `DocumentBusiness` | — | BE |
| `brief/receivedBrief.zul` | `vm.brief.ReceivedBriefVM` | `BriefBusiness`, `NotificationBusiness` | — | BE |
| `brief/widgets/AdditionalRequestBrief.zul` | `vm.brief.AdditionalRequestBriefVM` | `BriefBusiness` | — | BE |
| `brief/widgets/ApprovalBrief.zul` | `vm.brief.PopupBorrowBriefVM` | `BriefBusiness` | — | BE |
| `brief/widgets/BorrowBrief.zul` | `vm.brief.BorrowBriefVM` | `BriefBusiness` | — | BE |
| `brief/widgets/CompleteBrief.zul` | `vm.brief.CompleteBriefVm` | `BriefBusiness` | — | BE |
| `brief/widgets/LendBrief.zul` | `vm.brief.LendBriefVM` | `BriefBusiness` | — | BE |
| `brief/widgets/RejectBrief.zul` | `vm.brief.PopupBorrowBriefVM` | `BriefBusiness` | — | BE |
| `brief/widgets/addDocument.zul` | `vm.brief.AddDocumentVM` | `BriefBusiness` | — | BE |
| `brief/widgets/brief_attach_multimedia.zul` | `vm.brief.BriefAttachMultimediaVM` | `BriefBusiness` | `IVps` | BE+LEGACY |
| `brief/widgets/brief_info_history.zul` | `vm.brief.ViewHistoryVM` | `BriefBusiness` | — | BE |
| `brief/widgets/confirmModal.zul` | `vm.brief.ConfirmModalVM` | — | — | — |
| `brief/widgets/confirmNavigate.zul` | `vm.brief.confirmNavigateVM` | — | — | — |
| `brief/widgets/infoDetailDocument.zul` | `vm.brief.DetailDocumentVM` | `BriefBusiness`, `RequisitionBusiness` | — | BE |
| `brief/widgets/lookupSelectBrief.zul` | `vm.brief.AddDocToBriefLookupVM` | `BoxsBusiness`, `BriefBusiness`, `CatalogBriefBusiness`, `DocumentBusiness`, `StoragesBusiness` | — | BE |
| `brief/widgets/popupContent.zul` | `vm.brief.PopupContentBriefVM` | — | — | — |
| `brief/widgets/popupSelectBrief.zul` | `vm.brief.PopupSelectBriefVM` | `BoxsBusiness`, `BriefBusiness` | — | BE |
| `brief/widgets/process.zul` | `vm.brief.ProcessVM` | `BriefBusiness` | — | BE |
| `brief/widgets/receiveOrRejectBrief.zul` | `vm.brief.ReceiveOrRejectVM` | `BriefBusiness` | — | BE |
| `brief/widgets/shareBrief.zul` | `vm.brief.ShareBriefVM` | `BriefBusiness` | `IVps` | BE+LEGACY |
| `brief/widgets/sourceLookupBrief.zul` | `vm.brief.SourceLookupBriefVM` | `BriefBusiness` | — | BE |
| `brief/widgets/sourceLookupRadioBrief.zul` | `vm.brief.SourceLookupRadioBriefVM` | `BriefBusiness` | — | BE |
| `document/reportSendReceiveDoc/documentFinance.zul` | `vm.document.DocumentFinanceVM` | `DocumentBusiness` | — | BE |
| `shelve/shelve.zul` | `vm.shelve.ShelveVM` | `BoxsBusiness`, `ShelveBusiness`, `StoragesBusiness` | — | BE |
| `storageManagement/storageManagement.zul` | `vm.storages.StoragesVM` | `ShelveBusiness`, `StoragesBusiness` | — | BE |
| `widgets/popupSelectDocDraftForBrief.zul` | `widget.PopupSelectDocDraftForBriefVM` | — | — | — |
| `widgets/catalogBriefLookup.zul` | `widget.CatalogBriefLookupVM` | — | — | — |
| `widgets/sysStoragesLookup.zul` | `widget.SysStoragesLookupVM` | `StoragesBusiness` | — | BE |

<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>

| ViewModel | Gọi BE qua | Legacy | Nhãn |
|---|---|---|---|
| `vm.briefTree.SysBriefTreeModel` | — | `IVps` | LEGACY |
| `vm.briefTree.SysBriefTreeitemRenderer` | — | — | — |
| `vm.catalogBriefTree.SysCatalogBriefTreeModel` | — | `IVps` | LEGACY |
| `vm.catalogBriefTree.SysCatalogBriefTreeitemRenderer` | — | — | — |

</details>

## 2. Web → BE (Business → endpoint)

Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.

### BoxsBusiness

`web-spring/src/main/java/com/voffice/service/business/BoxsBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Boxs.addOrEditBox` | `/Boxs/addOrEditBox` | `BoxManagementAction.addOrEditBox` | gen1 |
| `Boxs.checkBoxExist` | `/Boxs/checkBoxExist` | `BoxManagementAction.checkBoxExist` | gen1 |
| `Boxs.deleteBox` | `/Boxs/deleteBox` | `BoxManagementAction.deleteBoxs` | gen1 |
| `Boxs.getListBoxs` | `/Boxs/getListBoxs` | `BoxManagementAction.getListBoxs` | gen1 |
| `Boxs.getListForCombobox` | `/Boxs/getListForCombobox` | `BoxManagementAction.getListForCombobox` | gen1 |
| `Brief.getListBrief` | `/Brief/getListBrief` | `BriefManagementAction.getListBrief` | gen1 |

### BriefBusiness

`web-spring/src/main/java/com/voffice/service/business/BriefBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Brief.addOrEditBrief` | `/Brief/addOrEditBrief` | `BriefManagementAction.addOrEditBrief` | gen1 |
| `Brief.briefBorrow` | `/Brief/briefBorrow` | `BriefManagementAction.briefBorrow` | gen1 |
| `Brief.briefLend` | `/Brief/briefLend` | `BriefManagementAction.briefLend` | gen1 |
| `Brief.checkBorrowBriefHardStatus` | `/Brief/checkBorrowBriefHardStatus` | `BriefManagementAction.checkBorrowBriefHardStatus` | gen1 |
| `Brief.checkBorrowDocument` | `/Brief/checkBorrowDocument` | `BriefManagementAction.checkBorrowDocument` | gen1 |
| `Brief.checkDuplicateRegisterNumber` | `/Brief/checkDuplicateRegisterNumber` | `BriefManagementAction.checkDuplicateRegisterNumber` | gen1 |
| `Brief.checkExistDocument` | `/Brief/checkExistDocument` | `BriefManagementAction.checkExistDocument` | gen1 |
| `Brief.checkHardStatusBrief` | `/Brief/checkHardStatusBrief` | `BriefManagementAction.checkHardStatusBrief` | gen1 |
| `Brief.checkViewBorrowBrief` | `/Brief/checkViewBorrowBrief` | `BriefManagementAction.checkViewBorrowBrief` | gen1 |
| `Brief.checkViewBriefInfoDetail` | `/Brief/checkViewBriefInfoDetail` | `BriefManagementAction.checkViewBriefInfoDetail` | gen1 |
| `Brief.completeBrief` | `/Brief/completeBrief` | `BriefManagementAction.completeBrief` | gen1 |
| `Brief.deleteBrief` | `/Brief/deleteBrief` | `BriefManagementAction.deleteBoxs` | gen1 |
| `Brief.getAbbreviationChildAndParentOrg` | `/Brief/getAbbreviationChildAndParentOrg` | `BriefManagementAction.getAbbreviationChildAndParentOrg` | gen1 |
| `Brief.getAreaNameById` | `/Brief/getAreaNameById` | `BriefManagementAction.getAreaNameById` | gen1 |
| `Brief.getBriefById` | `/Brief/getBriefById` | `BriefManagementAction.getBriefById` | gen1 |
| `Brief.getBriefDocumentForUpdate` | `/Brief/getBriefDocumentForUpdate` | `BriefManagementAction.getBriefDocumentForUpdate` | gen1 |
| `Brief.getBriefFileAttachmentDocument` | `/Brief/getBriefFileAttachmentDocument` | `BriefManagementAction.getBriefFileAttachmentDocument` | gen1 |
| `Brief.getBriefForUpdate` | `/Brief/getBriefForUpdate` | `BriefManagementAction.getBriefForUpdate` | gen1 |
| `Brief.getBriefProcessingStats` | `/Brief/getBriefProcessingStats` | `BriefManagementAction.getBriefProcessingStats` | gen1 |
| `Brief.getBriefsByCondition` | `/Brief/getBriefsByCondition` | `BriefManagementAction.getBriefsByCondition` | gen1 |
| `Brief.getCatalogBriefOfOrg` | `/Brief/getCatalogBriefOfOrg` | `BriefManagementAction.getCatalogBriefOfOrg` | gen1 |
| `Brief.getDataToExport` | `/Brief/getDataToExport` | `BriefManagementAction.getDataToExport` | gen1 |
| `Brief.getDocumentOfBrief` | `/Brief/getDocumentOfBrief` | `BriefManagementAction.getDocumentOfBrief` | gen1 |
| `Brief.getFileInfoById` | `/Brief/getFileInfoById` | `BriefManagementAction.getFileInfoById` | gen1 |
| `Brief.getHardStatusByBriefId` | `/Brief/getHardStatusByBriefId` | `BriefManagementAction.getHardStatusByBriefId` | gen1 |
| `Brief.getInfoFileBrief` | `/Brief/getInfoFileBrief` | `BriefManagementAction.getInfoFileBrief` | gen1 |
| `Brief.getListBrief` | `/Brief/getListBrief` | `BriefManagementAction.getListBrief` | gen1 |
| `Brief.getListBriefBorrow` | `/Brief/getListBriefBorrow` | `BriefManagementAction.getListBriefBorrow` | gen1 |
| `Brief.getListBriefForUpdate` | `/Brief/getListBriefForUpdate` | `BriefManagementAction.getListBriefForUpdate` | gen1 |
| `Brief.getListBriefHistoryBorrow` | `/Brief/getListBriefHistoryBorrow` | `BriefManagementAction.getListBriefHistoryBorrow` | gen1 |
| `Brief.getListBriefInfo` | `/Brief/getListBriefInfo` | `BriefManagementAction.getListBriefInfo` | gen1 |
| `Brief.getListBriefToUpdate` | `/Brief/getListBriefToUpdate` | `BriefManagementAction.getListBriefToUpdate` | gen1 |
| `Brief.getListBriefUpdate` | `/Brief/getListBriefUpdate` | `BriefManagementAction.getListBriefUpdate` | gen1 |
| `Brief.getListBriefsToTransfer` | `/Brief/getListBriefsToTransfer` | `BriefManagementAction.getListBriefsToTransfer` | gen1 |
| `Brief.getListDocumentHistory` | `/Brief/getListDocumentHistory` | `BriefManagementAction.getListDocumentHistory` | gen1 |
| `Brief.getListReceivedBrief` | `/Brief/getListReceivedBrief` | `BriefManagementAction.getListReceivedBrief` | gen1 |
| `Brief.getListTitleOrBaseOnOfBriefBorrow` | `/Brief/getListTitleOrBaseOnOfBriefBorrow` | `BriefManagementAction.getListTitleOrBaseOnOfBriefBorrow` | gen1 |
| `Brief.getMaxRegisterNumber` | `/Brief/getMaxRegisterNumber` | `BriefManagementAction.getMaxRegisterNumber` | gen1 |
| `Brief.getOrgListDefaultByUserId` | `/Brief/getOrgListDefaultByUserId` | `BriefManagementAction.getOrgListDefaultByUserId` | gen1 |
| `Brief.getRecentBorrowDocument` | `/Brief/getRecentBorrowDocument` | `BriefManagementAction.getRecentBorrowDocument` | gen1 |
| `Brief.processBrief` | `/Brief/processBrief` | `BriefManagementAction.processBrief` | gen1 |
| `Brief.processBriefBorrow` | `/Brief/processBriefBorrow` | `BriefManagementAction.processBriefBorrow` | gen1 |
| `Brief.requestCompleteBrief` | `/Brief/requestCompleteBrief` | `BriefManagementAction.requestCompleteBrief` | gen1 |
| `Brief.transferBrief` | `/Brief/transferBrief` | `BriefManagementAction.transferBrief` | gen1 |
| `Brief.update-file-brief` | `/Brief/update-file-brief` | `IndexController.redirect` | gen2 |
| `Storages.getOrgList` | `/Storages/getOrgList` | `StorageManagementAction.getOrgList` | gen1 |
| `api.brief-detail` | `/api/brief-detail` | `IndexController.redirect` | gen2 |
| `api.brief-detail.add-document-in-brief` | `/api/brief-detail/add-document-in-brief` | `BriefDetailManagementController.addDocumentInBrief` | gen1 |
| `api.brief-detail.brief-multimedia` | `/api/brief-detail/brief-multimedia` | `BriefDetailManagementController.updateBriefMultimedia` | gen1 |
| `api.brief-detail.check-permission-brief` | `/api/brief-detail/check-permission-brief` | `BriefDetailManagementController.checkPermissionBrief` | gen1 |
| `api.brief-detail.check-text-doc-for-submitting` | `/api/brief-detail/check-text-doc-for-submitting` | `BriefDetailManagementController.checkTextsAndDocumentsForSubmitting` | gen1 |
| `api.brief-detail.delete-document-in-brief` | `/api/brief-detail/delete-document-in-brief` | `BriefDetailManagementController.deleteDocumentInBrief` | gen1 |
| `api.brief-detail.get-file-brief` | `/api/brief-detail/get-file-brief` | `BriefDetailManagementController.getFileBrief` | gen1 |
| `api.brief-detail.get-list-file-attachment` | `/api/brief-detail/get-list-file-attachment` | `BriefDetailManagementController.getListFileAttachment` | gen1 |
| `api.brief-detail.swap-order-brief-multimedia` | `/api/brief-detail/swap-order-brief-multimedia` | `BriefDetailManagementController.swapOrderBriefMultimedia` | gen1 |
| `api.brief-detail.update-and-get-total-num-paper-brief` | `/api/brief-detail/update-and-get-total-num-paper-brief` | `BriefDetailManagementController.updateAndGetTotalNumPaperBrief` | gen1 |
| `api.brief-detail.update-order-document` | `/api/brief-detail/update-order-document` | `BriefDetailManagementController.changeOrderDocument` | gen1 |
| `api.brief-detail.update-order-file` | `/api/brief-detail/update-order-file` | `BriefDetailManagementController.changeOrderFile` | gen1 |
| `api.brief-detail.update-order-text` | `/api/brief-detail/update-order-text` | `BriefDetailManagementController.changeOrderText` | gen1 |
| `api.brief-detail.update-page-number-brief-document-map` | `/api/brief-detail/update-page-number-brief-document-map` | `BriefDetailManagementController.updateNumPageDocument` | gen1 |
| `api.brief-detail.update-page-number-file-attachment` | `/api/brief-detail/update-page-number-file-attachment` | `BriefDetailManagementController.updateNumPageFileAttach` | gen1 |
| `api.brief-detail.update-total-doc-and-num-pager` | `/api/brief-detail/update-total-doc-and-num-pager` | `BriefDetailManagementController.updateTotalDocAndNumPaper` | gen1 |
| `api.brief-detail.update-total-doc-brief` | `/api/brief-detail/update-total-doc-brief` | `BriefDetailManagementController.updateTotalDocBrief` | gen1 |
| `api.brief-detail.updateFilePageInBriefFilesAttach` | `/api/brief-detail/updateFilePageInBriefFilesAttach` | `BriefDetailManagementController.updateFilePageInBriefFilesAttach` | gen1 |
| `api.brief-detail.updatePaperNumberInBriefDocMap` | `/api/brief-detail/updatePaperNumberInBriefDocMap` | `BriefDetailManagementController.updateFilePagerInBriefDocMap` | gen1 |
| `api.brief-detail.upload-brief-multimedia-file` | `/api/brief-detail/upload-brief-multimedia-file` | `BriefDetailManagementController.uploadBriefMultimediaFile` | gen1 |
| `api.brief-detail.upload-file-attachment` | `/api/brief-detail/upload-file-attachment` | `BriefDetailManagementController.uploadFileAttachment` | gen1 |
| `api.brief.close-brief` | `/api/brief/close-brief` | `BriefController.closeBrief` | gen2 |
| `api.brief.get-all-be-shared-id` | `/api/brief/get-all-be-shared-id` | `BriefController.getAllBeSharedId` | gen2 |
| `api.brief.get-cert-shvb` | `/api/brief/get-cert-shvb` | `BriefController.getCertificateOfUserOrOrg` | gen2 |
| `api.brief.get-count-brief-share` | `/api/brief/get-count-brief-share` | `BriefController.getCountBriefShare` | gen2 |
| `api.brief.get-list-authorized-org-for-catalog` | `/api/brief/get-list-authorized-org-for-catalog` | `BriefController.getAuthorizedOrgListForCatalog` | gen2 |
| `api.brief.get-list-brief-share` | `/api/brief/get-list-brief-share` | `BriefController.getListBriefShare` | gen2 |
| `api.brief.get-page-brief-share` | `/api/brief/get-page-brief-share` | `BriefController.getPageBriefShare` | gen2 |
| `api.brief.submit-brief` | `/api/brief/submit-brief` | `BriefController.submitBrief` | gen2 |
| `api.brief.submit-brief-history` | `/api/brief/submit-brief-history` | `BriefController.getSubmitBriefHistory` | gen2 |
| `api.brief.unlock-brief` | `/api/brief/unlock-brief` | `BriefController.unLockBrief` | gen2 |
| `api.brief.update-brief-share-list` | `/api/brief/update-brief-share-list` | `BriefController.updateBriefShareList` | gen2 |
| `textAction.rollBackBrief` | `/textAction/rollBackBrief` | `TextAction.rollBackBrief` | gen1 |

### CatalogBriefBusiness

`web-spring/src/main/java/com/voffice/service/business/CatalogBriefBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Boxs.getListBoxs` | `/Boxs/getListBoxs` | `BoxManagementAction.getListBoxs` | gen1 |
| `CatalogBrief.checkIsCatalogBriefUsed` | `/CatalogBrief/checkIsCatalogBriefUsed` | `CatalogBriefManagementAction.checkIsCatalogBriefUsed` | gen1 |
| `CatalogBrief.deleteCatalogBrief` | `/CatalogBrief/deleteCatalogBrief` | `CatalogBriefManagementAction.deleteCatalogBrief` | gen1 |
| `CatalogBrief.getCheckInsertCatalogBriefPermission` | `/CatalogBrief/getCheckInsertCatalogBriefPermission` | `CatalogBriefManagementAction.getCheckInsertCatalogBriefPermission` | gen1 |
| `CatalogBrief.getListCatalogBriefByOrgId` | `/CatalogBrief/getListCatalogBriefByOrgId` | `CatalogBriefManagementAction.getListCatalogBriefByOrgId` | gen1 |
| `CatalogBrief.getListOrgByUserId` | `/CatalogBrief/getListOrgByUserId` | `CatalogBriefManagementAction.getListOrgByUserId` | gen1 |
| `CatalogBrief.saveCatalogBrief` | `/CatalogBrief/saveCatalogBrief` | `CatalogBriefManagementAction.saveCatalogBrief` | gen1 |
| `CatalogBrief.searchListCatalogBrief` | `/CatalogBrief/searchListCatalogBrief` | `CatalogBriefManagementAction.getListCatalogBrief` | gen1 |
| `CatalogBrief.searchListChildOrg` | `/CatalogBrief/searchListChildOrg` | `CatalogBriefManagementAction.getListChildOrg` | gen1 |

### ShelveBusiness

`web-spring/src/main/java/com/voffice/service/business/ShelveBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Shelve.addOrEditShelve` | `/Shelve/addOrEditShelve` | `ShelveManagementAction.addOrEditShelve` | gen1 |
| `Shelve.checkShelveExist` | `/Shelve/checkShelveExist` | `ShelveManagementAction.checkShelveExist` | gen1 |
| `Shelve.checkShelveNumFloor` | `/Shelve/checkShelveNumFloor` | `ShelveManagementAction.checkShelveNumFloor` | gen1 |
| `Shelve.deleteShelve` | `/Shelve/deleteShelve` | `ShelveManagementAction.deleteShelve` | gen1 |
| `Shelve.getListShelve` | `/Shelve/getListShelve` | `ShelveManagementAction.getListShelve` | gen1 |

### StoragesBusiness

`web-spring/src/main/java/com/voffice/service/business/StoragesBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `Storages.addOrEditStorage` | `/Storages/addOrEditStorage` | `StorageManagementAction.addOrEditStorage` | gen1 |
| `Storages.checkStorageExist` | `/Storages/checkStorageExist` | `StorageManagementAction.checkStorageExist` | gen1 |
| `Storages.checkStoragePermissions` | `/Storages/checkStoragePermissions` | `StorageManagementAction.checkStoragePermissions` | gen1 |
| `Storages.deleteStorage` | `/Storages/deleteStorage` | `StorageManagementAction.deleteStorages` | gen1 |
| `Storages.getListStorages` | `/Storages/getListStorages` | `StorageManagementAction.getListStorages` | gen1 |
| `Storages.getListSysRoleOrg` | `/Storages/getListSysRoleOrg` | `StorageManagementAction.getListSysRoleOrg` | gen1 |
| `Storages.getOrgList` | `/Storages/getOrgList` | `StorageManagementAction.getOrgList` | gen1 |
| `Storages.getStorageReport` | `/Storages/getStorageReport` | `StorageManagementAction.getStorageReport` | gen1 |

### StoreTypeConfigBusiness

`web-spring/src/main/java/com/voffice/service/business/StoreTypeConfigBusiness.java`

| Hàm (function key) | Endpoint BE | Controller.method | Gen |
|---|---|---|---|
| `TypeConfigAction.addRolesDocType` | `/TypeConfigAction/addRolesDocType` | `StoreTypeConfigAction.addRolesDocType` | gen1 |
| `TypeConfigAction.deleteUserDocRoles` | `/TypeConfigAction/deleteUserDocRoles` | `StoreTypeConfigAction.deleteUserDocRoles` | gen1 |
| `TypeConfigAction.getListConfig` | `/TypeConfigAction/getListConfig` | `StoreTypeConfigAction.getListConfig` | gen1 |
| `TypeConfigAction.getListDocType` | `/TypeConfigAction/getListDocType` | `StoreTypeConfigAction.getListDocType` | gen1 |
| `TypeConfigAction.getListFinancialDoc` | `/TypeConfigAction/getListFinancialDoc` | `StoreTypeConfigAction.getUserDocRolesByEmpId` | gen1 |
| `TypeConfigAction.getListUserDocTypeRoles` | `/TypeConfigAction/getListUserDocTypeRoles` | `StoreTypeConfigAction.getListUserDocTypeRoles` | gen1 |
| `TypeConfigAction.getUserDocRolesByEmpId` | `/TypeConfigAction/getUserDocRolesByEmpId` | `IndexController.redirect` | gen2 |
| `TypeConfigAction.getUserEntity` | `/TypeConfigAction/getUserEntity` | `StoreTypeConfigAction.getUserEntity` | gen1 |
| `TypeConfigAction.getUserRolesDetail` | `/TypeConfigAction/getUserRolesDetail` | `IndexController.redirect` | gen2 |
| `TypeConfigAction.updateRolesDocType` | `/TypeConfigAction/updateRolesDocType` | `StoreTypeConfigAction.updateRolesDocType` | gen1 |

## 3. BE — Controller → logic / service → DAO / repository → bảng

### BoxManagementAction (gen1) — base `/Boxs`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/BoxManagementAction.java`

- Logic (gen-1 `controler/`): `BoxManagementController`
- DAO (SQL thuần): `BoxManagementDAO`, `CommonDataBaseDaoVO2`, `StorageManagementDAO`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `BOXS`, `BRIEF`, `CV_PRIORITY`, `DOCUMENT_TYPE`, `FLOOR`, `SECURITY_TYPE`, `SHELVES`, `STORAGES`, `SYS_ROLE`, `USER_ROLE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Boxs/getListBoxs` | `getListBoxs` |
| POST | `/Boxs/deleteBox` | `deleteBoxs` |
| POST | `/Boxs/addOrEditBox` | `addOrEditBox` |
| POST | `/Boxs/getListForCombobox` | `getListForCombobox` |
| POST | `/Boxs/checkBoxExist` | `checkBoxExist` |

</details>

### BriefDetailManagementController (gen1) — base `/api/brief-detail`, 27 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/controler/BriefDetailManagementController.java`

- Service: `BriefDetailManagementService`, `BriefDetailManagementServiceImpl`
- DAO (SQL thuần): `BriefDetailManagementDAO`, `BriefManagementDAO`
- Repository (JPA): `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `BriefMultimediaFileJPA`, `BriefMultimediaJPA`, `CatalogingBriefFileRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `SubmissionMapRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH`, `ATTACH_TEMPLATE`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CV_PRIORITY`, `DOCUMENT`, `DOCUMENT_TYPE`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `SECURITY_TYPE`, `SHELVES`, `STORAGES`, `SUBMISSION_MAP`, `SYS_ROLE`, `TEXT`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/api/brief-detail/get-list-document-in` | `getListDocumentIn` |
| POST | `/api/brief-detail/get-list-text` | `getListText` |
| POST | `/api/brief-detail/check-text-doc-for-submitting` | `checkTextsAndDocumentsForSubmitting` |
| POST | `/api/brief-detail/delete-document-in-brief` | `deleteDocumentInBrief` |
| POST | `/api/brief-detail/add-document-in-brief` | `addDocumentInBrief` |
| POST | `/api/brief-detail/get-list-file-attachment` | `getListFileAttachment` |
| POST | `/api/brief-detail/upload-file-attachment` | `uploadFileAttachment` |
| POST | `/api/brief-detail/delete-file-attachment` | `deleteFileAttachment` |
| POST | `/api/brief-detail/check-permission-brief` | `checkPermissionBrief` |
| POST | `/api/brief-detail/update-page-number-brief-document-map` | `updateNumPageDocument` |
| POST | `/api/brief-detail/update-page-number-file-attachment` | `updateNumPageFileAttach` |
| GET | `/api/brief-detail/{briefId}/brief-multimedia` | `getListBriefMultimedia` |
| GET | `/api/brief-detail/brief-multimedia/{briefMultimediaId}` | `getBriefMultimediaById` |
| POST | `/api/brief-detail/brief-multimedia` | `createBriefMultimedia` |
| PUT | `/api/brief-detail/brief-multimedia` | `updateBriefMultimedia` |
| POST | `/api/brief-detail/upload-brief-multimedia-file` | `uploadBriefMultimediaFile` |
| POST | `/api/brief-detail/delete-brief-multimedia` | `deleteBriefMultimediaFile` |
| POST | `/api/brief-detail/update-order-text/{briefId}` | `changeOrderText` |
| POST | `/api/brief-detail/update-order-document/{briefId}` | `changeOrderDocument` |
| POST | `/api/brief-detail/update-order-file/{briefId}` | `changeOrderFile` |
| POST | `/api/brief-detail/swap-order-brief-multimedia/{briefId}` | `swapOrderBriefMultimedia` |
| POST | `/api/brief-detail/update-total-doc-brief/{briefId}` | `updateTotalDocBrief` |
| POST | `/api/brief-detail/update-and-get-total-num-paper-brief/{briefId}` | `updateAndGetTotalNumPaperBrief` |
| POST | `/api/brief-detail/get-file-brief/{briefId}` | `getFileBrief` |
| POST | `/api/brief-detail/update-total-doc-and-num-pager` | `updateTotalDocAndNumPaper` |
| POST | `/api/brief-detail/updatePaperNumberInBriefDocMap` | `updateFilePagerInBriefDocMap` |
| POST | `/api/brief-detail/updateFilePageInBriefFilesAttach/{briefDocumentId}` | `updateFilePageInBriefFilesAttach` |

</details>

### BriefManagementAction (gen1) — base `/Brief`, 47 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/BriefManagementAction.java`

- Logic (gen-1 `controler/`): `BriefManagementController`
- DAO (SQL thuần): `BriefManagementDAO`, `CatalogBriefDAO`, `CommonDataBaseDaoVO2`, `FileAttachmentDAO`, `OrgDAO`, `VHROrgDAO`
- Repository (JPA): `BriefEntityRepositoryJPA`, `CatalogingBriefFileRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `ATTACH_TEMPLATE`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CONNECT_VHR`, `DOCUMENT`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `EMPLOYEE_TYPE_PROCESS`, `FILES`, `FILES_ATTACHMENT`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FLOOR`, `IMAGE_ORG`, `MEETING`, `MEETING_CONFIG`, `SECURITY_TYPE`, `SHELVES`, `STAFF_GROUP_ROLE`, `STORAGES`, `SYS_ROLE`, `TEXT`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Brief/getListBrief` | `getListBrief` |
| POST | `/Brief/getBriefById` | `getBriefById` |
| POST | `/Brief/getBriefProcessingStats` | `getBriefProcessingStats` |
| POST | `/Brief/getListBriefToUpdate` | `getListBriefToUpdate` |
| POST | `/Brief/getListBriefInfo` | `getListBriefInfo` |
| POST | `/Brief/getListBriefHistoryBorrow` | `getListBriefHistoryBorrow` |
| POST | `/Brief/getListBriefUpdate` | `getListBriefUpdate` |
| POST | `/Brief/getListTitleOrBaseOnOfBriefBorrow` | `getListTitleOrBaseOnOfBriefBorrow` |
| POST | `/Brief/deleteBrief` | `deleteBoxs` |
| POST | `/Brief/addOrEditBrief` | `addOrEditBrief` |
| POST | `/Brief/briefBorrow` | `briefBorrow` |
| POST | `/Brief/briefLend` | `briefLend` |
| POST | `/Brief/transferBrief` | `transferBrief` |
| POST | `/Brief/processBrief` | `processBrief` |
| POST | `/Brief/processBriefBorrow` | `processBriefBorrow` |
| POST | `/Brief/requestCompleteBrief` | `requestCompleteBrief` |
| POST | `/Brief/completeBrief` | `completeBrief` |
| POST | `/Brief/checkBorrowDocument` | `checkBorrowDocument` |
| POST | `/Brief/getBriefForUpdate` | `getBriefForUpdate` |
| POST | `/Brief/getBriefDocumentForUpdate` | `getBriefDocumentForUpdate` |
| POST | `/Brief/getAbbreviationChildAndParentOrg` | `getAbbreviationChildAndParentOrg` |
| POST | `/Brief/getListBriefBorrow` | `getListBriefBorrow` |
| POST | `/Brief/getAreaNameById` | `getAreaNameById` |
| POST | `/Brief/getListReceivedBrief` | `getListReceivedBrief` |
| POST | `/Brief/getDataToExport` | `getDataToExport` |
| POST | `/Brief/getHardStatusByBriefId` | `getHardStatusByBriefId` |
| POST | `/Brief/getListDocumentHistory` | `getListDocumentHistory` |
| POST | `/Brief/checkExistDocument` | `checkExistDocument` |
| POST | `/Brief/checkHardStatusBrief` | `checkHardStatusBrief` |
| POST | `/Brief/checkViewBriefInfoDetail` | `checkViewBriefInfoDetail` |
| POST | `/Brief/checkViewBorrowBrief` | `checkViewBorrowBrief` |
| POST | `/Brief/getBriefFileAttachmentDocument` | `getBriefFileAttachmentDocument` |
| POST | `/Brief/getOrgListDefaultByUserId` | `getOrgListDefaultByUserId` |
| POST | `/Brief/getInfoFileBrief` | `getInfoFileBrief` |
| POST | `/Brief/getMaxRegisterNumber` | `getMaxRegisterNumber` |
| POST | `/Brief/checkDuplicateRegisterNumber` | `checkDuplicateRegisterNumber` |
| POST | `/Brief/getCatalogBriefOfOrg` | `getCatalogBriefOfOrg` |
| POST | `/Brief/getBriefsByCondition` | `getBriefsByCondition` |
| POST | `/Brief/getListBriefsToTransfer` | `getListBriefsToTransfer` |
| POST | `/Brief/getListBriefForUpdate` | `getListBriefForUpdate` |
| POST | `/Brief/getRecentBorrowDocument` | `getRecentBorrowDocument` |
| POST | `/Brief/checkBorrowBriefHardStatus` | `checkBorrowBriefHardStatus` |
| POST | `/Brief/getFileInfoById` | `getFileInfoById` |
| POST | `/Brief/getDocumentOfBrief` | `getDocumentOfBrief` |
| POST | `/Brief/AddBriefDocument` | `addBriefDocument` |
| POST | `/Brief/CheckBriefCode` | `checkBriefCode` |
| POST | `/Brief/update-file-brief/{briefId}` | `updateBriefFile` |

</details>

### CatalogBriefManagementAction (gen1) — base `/CatalogBrief`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/CatalogBriefManagementAction.java`

- Logic (gen-1 `controler/`): `CatalogBriefController`
- DAO (SQL thuần): `CatalogBriefDAO`, `CommonDataBaseDaoVO2`, `OrgDAO`
- Bảng (ước lượng từ SQL/@Table): `BRIEF`, `CATALOG_BRIEF`, `EMPLOYEE_TYPE_PROCESS`, `IMAGE_ORG`, `STAFF_GROUP_ROLE`, `SYS_ROLE`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/CatalogBrief/getListCatalogBriefByOrgId` | `getListCatalogBriefByOrgId` |
| POST | `/CatalogBrief/searchListCatalogBrief` | `getListCatalogBrief` |
| POST | `/CatalogBrief/getListOrgByUserId` | `getListOrgByUserId` |
| POST | `/CatalogBrief/getCheckInsertCatalogBriefPermission` | `getCheckInsertCatalogBriefPermission` |
| POST | `/CatalogBrief/searchListChildOrg` | `getListChildOrg` |
| POST | `/CatalogBrief/deleteCatalogBrief` | `deleteCatalogBrief` |
| POST | `/CatalogBrief/saveCatalogBrief` | `saveCatalogBrief` |
| POST | `/CatalogBrief/checkIsCatalogBriefUsed` | `checkIsCatalogBriefUsed` |

</details>

### ShelveManagementAction (gen1) — base `/Shelve`, 5 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/ShelveManagementAction.java`

- Logic (gen-1 `controler/`): `ShelveManagementController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `ShelveManagementDAO`, `StorageManagementDAO`
- Bảng (ước lượng từ SQL/@Table): `BOXS`, `BRIEF`, `SHELVES`, `STORAGES`, `SYS_ROLE`, `USER_ROLE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Shelve/getListShelve` | `getListShelve` |
| POST | `/Shelve/deleteShelve` | `deleteShelve` |
| POST | `/Shelve/addOrEditShelve` | `addOrEditShelve` |
| POST | `/Shelve/checkShelveExist` | `checkShelveExist` |
| POST | `/Shelve/checkShelveNumFloor` | `checkShelveNumFloor` |

</details>

### SignBriefcaseAction (gen1) — base `/signBriefcaseAction`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/SignBriefcaseAction.java`

- Logic (gen-1 `controler/`): `SignBriefcaseControler`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `SignBriefcaseDAO`
- Bảng (ước lượng từ SQL/@Table): `ATTACH_BRIEFCASE`, `MEETING_ASSISTANT`, `SIGN_BRIEFCASE`, `SIGN_BRIEFCASE_ATTACH`, `SIGN_BRIEFCASE_ATTACH_OTHER`, `SIGN_BRIEFCASE_SIGNER`, `SIGN_BRIEFCASE_STATUS`, `VHR_EMPLOYEE`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/signBriefcaseAction/addOrEditSignBriefcase` | `addOrEditSignBriefcase` |
| POST | `/signBriefcaseAction/deleteSignBriefcase` | `deleteSignBriefcase` |
| POST | `/signBriefcaseAction/getBarcode` | `getBarcode` |
| POST | `/signBriefcaseAction/getLeaderOfAssitant` | `getLeaderOfAssitant` |
| POST | `/signBriefcaseAction/getListSignBriefcase` | `getListSignBriefcase` |
| POST | `/signBriefcaseAction/getListSignBriefcaseStatus` | `getListSignBriefcaseStatus` |
| POST | `/signBriefcaseAction/getSignBriefcaseDetail` | `getSignBriefcaseDetail` |
| POST | `/signBriefcaseAction/updateSigner` | `updateSigner` |
| POST | `/signBriefcaseAction/updateStatusSignBriefcase` | `updateStatusSignBriefcase` |

</details>

### StorageManagementAction (gen1) — base `/Storages`, 9 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/StorageManagementAction.java`

- Logic (gen-1 `controler/`): `StorageManagementController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `StorageManagementDAO`
- Bảng (ước lượng từ SQL/@Table): `BOXS`, `BRIEF`, `SHELVES`, `STORAGES`, `SYS_ROLE`, `USER_ROLE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/Storages/getListStorages` | `getListStorages` |
| POST | `/Storages/deleteStorage` | `deleteStorages` |
| POST | `/Storages/addOrEditStorage` | `addOrEditStorage` |
| POST | `/Storages/checkStorageExist` | `checkStorageExist` |
| POST | `/Storages/getOrgList` | `getOrgList` |
| POST | `/Storages/getStorageReport` | `getStorageReport` |
| POST | `/Storages/checkStoragePermissions` | `checkStoragePermissions` |
| POST | `/Storages/getListSysRoleOrg` | `getListSysRoleOrg` |
| POST | `/Storages/getListSysRoleEvaluate` | `getListSysRoleEvaluate` |

</details>

### StoreTypeConfigAction (gen1) — base `/TypeConfigAction`, 8 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/voffice/action/StoreTypeConfigAction.java`

- Logic (gen-1 `controler/`): `StoreTypeConfigController`
- DAO (SQL thuần): `CommonDataBaseDaoVO2`, `StoreTypeConfigDAO`
- Bảng (ước lượng từ SQL/@Table): `DOCUMENT_TYPE`, `STORE_DOCUMENT_ROLE`, `STORE_TYPE_CONFIG`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| POST | `/TypeConfigAction/getListConfig` | `getListConfig` |
| POST | `/TypeConfigAction/getListDocType` | `getListDocType` |
| POST | `/TypeConfigAction/addRolesDocType` | `addRolesDocType` |
| POST | `/TypeConfigAction/updateRolesDocType` | `updateRolesDocType` |
| POST | `/TypeConfigAction/getListUserDocTypeRoles` | `getListUserDocTypeRoles` |
| POST | `/TypeConfigAction/deleteUserDocRoles` | `deleteUserDocRoles` |
| POST | `/TypeConfigAction/getUserEntity` | `getUserEntity` |
| REQUEST | `/TypeConfigAction/getListFinancialDoc` | `getUserDocRolesByEmpId` |

</details>

### BriefController (gen2) — base `/api/brief`, 11 endpoint

`backend2.0/backendvoffice/src/main/java/com/viettel/office/controller/BriefController.java`

- Logic (gen-1 `controler/`): `CommonControler`, `WOPIController`
- Service: `BriefService`, `BriefServiceImpl`, `BriefDetailManagementService`, `BriefDetailManagementServiceImpl`, `CategoryCommonService`, `CategoryCommonServiceImpl`, `CategoryCacheService`, `SubmissionManagerService`, `SubmissionManagerServiceImpl`, `DocCommentService`, `DocCommentServiceImpl`, `DocOutService`, `DocOutServiceImpl`, `SubmissionFormService`, `SubmissionFormServiceImpl`
- DAO (SQL thuần): `BriefDetailManagementDAO`, `BriefManagementDAO`, `CatalogBriefDAO`, `CommonDataBaseDaoVO2`, `CommonDAO`, `FilesCommentDraffDAO`, `HomeWidgetDAO`, `NotificationDAO`, `SmsDAO`, `SystemParameterDAO`, `UserDAO`, `UserRoleDAO`, `VHROrgDAO`, `DocumentDAO`, `FilesAttachmentDAO`, `TextDAO`, `DocumentSignDAO`, `P12CertDAO`, `StaffDAO`, `SubmissionFormEditHistoryDAO`, `TextSearchDAO`, `UserOrgMapDAO`, `AttachDAO`, `TextEditHistoryDAO`
- Repository (JPA): `BriefDocumentMapRepositoryJPA`, `BriefEntityRepositoryJPA`, `BriefMultimediaFileJPA`, `BriefMultimediaJPA`, `CatalogingBriefFileRepositoryJPA`, `DocumentRepositoryJPA`, `FileAttachmentJPA`, `FileAttachmentMapperRepositoryJPA`, `SubmissionMapRepositoryJPA`, `BriefShareEntityRepositoryJPA`, `BriefSubmitAttachFileEntityRepositoryJPA`, `BriefSubmitDocumentEntityRepositoryJPA`, `BriefSubmitRequestEntityRepositoryJPA`, `CategoryCommonRepositoryJPA`, `GroupApplyRepositoryJPA`, `FilesAttachmentJPA`, `PositionRepositoryJPA`, `SecurityTypeRepositoryJPA`, `SubmissionFileRepositoryJPA`, `SubmissionFormRepositoryJPA`, `DocumentInFileJPA`, `DocumentInGroupRepositoryJPA`, `DocumentInStaffRepositoryJPA`, `DocumentLeaderCommentRepositoryJPA`, `DocumentProcessRepositoryJPA`, `MeetingAssistantRepositoryJPA`, `UserRoleRepositoryJPA`, `VhrOrgRepositoryJPA`, `AttachRepositoryJPA`, `FileEncryptMapJPA`, `NodeActionRepositoryJPA`, `ReportDailyHistoryJPA`, `TextProcessRepositoryHistoryJPA`, `TextProcessRepositoryJPA`, `TextRepositoryJPA`, `NotificationRepositoryJPA`, `StaffImageSignJPA`, `SubmissionProcessRepositoryJPA`, `SubmissionMapFileJPA`, `TextAttachRepositoryJPA`, `AttachTemplateRepositoryJPA`
- Bảng (ước lượng từ SQL/@Table): `AREA`, `ATTACH`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_DOCUMENT`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EXT_APP`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVES`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`

<details><summary>Endpoint</summary>

| Verb | Path | Method |
|---|---|---|
| GET | `/api/brief/get-list-brief-share` | `getListBriefShare` |
| GET | `/api/brief/get-page-brief-share` | `getPageBriefShare` |
| GET | `/api/brief/get-all-be-shared-id` | `getAllBeSharedId` |
| GET | `/api/brief/get-count-brief-share` | `getCountBriefShare` |
| POST | `/api/brief/update-brief-share-list` | `updateBriefShareList` |
| GET | `/api/brief/get-list-authorized-org-for-catalog` | `getAuthorizedOrgListForCatalog` |
| POST | `/api/brief/submit-brief` | `submitBrief` |
| GET | `/api/brief/submit-brief-history/{briefId}` | `getSubmitBriefHistory` |
| POST | `/api/brief/close-brief/{briefId}` | `closeBrief` |
| POST | `/api/brief/unlock-brief/{briefId}` | `unLockBrief` |
| GET | `/api/brief/get-cert-shvb` | `getCertificateOfUserOrOrg` |

</details>

## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)

_Không có facade legacy riêng._

## 5. Entity / bảng DB thuộc phân hệ

**BE gen-2 (`com.viettel.office.entities`)**: `BriefDocumentEntity`→`BRIEF_DOCUMENT`, `BriefDocumentMapEntity`→`BRIEF_DOCUMENT_MAP`, `BriefEntity`→`BRIEF`, `BriefMultimediaEntity`→`BRIEF_MULTIMEDIA`, `BriefMultimediaFileEntity`→`BRIEF_MULTIMEDIA_FILE`, `BriefShareEntity`→`BRIEF_SHARE`, `BriefSubmitAttachFileEntity`→`BRIEF_SUBMIT_ATTACH_FILE`, `BriefSubmitDocumentEntity`→`BRIEF_SUBMIT_DOCUMENT`, `BriefSubmitRequestEntity`→`BRIEF_SUBMIT_REQUEST`, `CatalogingBriefFileEntity`→`CATALOGING_BRIEF_FILE`

**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: `Boxs`→`BOXS`, `BriefFilesAttachment`→`BRIEF_FILES_ATTACHMENT`, `BriefUpdate`→`BRIEF_UPDATE`, `Shelve`→`SHELVE`, `StoreTypeConfig`→`STORE_TYPE_CONFIG`

**Tổng hợp bảng chạm tới**: `AREA`, `ATTACH`, `ATTACH_BRIEFCASE`, `ATTACH_SAVEBEFORE`, `ATTACH_TEMPLATE`, `AUTO_DIGSIG_TRANSACTION`, `BOXS`, `BRIEF`, `BRIEF_BORROW`, `BRIEF_BORROW_DOC`, `BRIEF_BORROW_DOC_MAP`, `BRIEF_DOCUMENT`, `BRIEF_DOCUMENT_MAP`, `BRIEF_DOCUMENT_MAP_HISTORY`, `BRIEF_FILES_ATTACHMENT`, `BRIEF_FILES_ATTACHMENT_HISTORY`, `BRIEF_FILE_MAP`, `BRIEF_MARK`, `BRIEF_MULTIMEDIA`, `BRIEF_MULTIMEDIA_FILE`, `BRIEF_PROCESS`, `BRIEF_SHARE`, `BRIEF_SUBMIT_ATTACH_FILE`, `BRIEF_SUBMIT_DOCUMENT`, `BRIEF_SUBMIT_REQUEST`, `BRIEF_UPDATE`, `CATALOGING_BRIEF_FILE`, `CATALOG_BRIEF`, `CATEGORY_COMMON`, `CHART_AGREEMENT_PERMISSION`, `CONFIG_SMS_ORG`, `CONFIG_TEXT_SYNC`, `CONFIG_USER_DOCUMENT`, `CONFIG_VALUES`, `CONNECT_DOCUMENT`, `CONNECT_VHR`, `CV_GROUP`, `CV_PRIORITY`, `DIRECTOR_CONFIG`, `DOCUMENT`, `DOCUMENT_IN_CV_GROUP`, `DOCUMENT_IN_FILE`, `DOCUMENT_IN_GROUP`, `DOCUMENT_IN_LIST_REQUEST`, `DOCUMENT_IN_STAFF`, `DOCUMENT_IN_STAFF_NOTSEND`, `DOCUMENT_LEADER_COMMENT`, `DOCUMENT_MEETING_REQ`, `DOCUMENT_OFFICE_SEND`, `DOCUMENT_PROCESS`, `DOCUMENT_PUBLISHED`, `DOCUMENT_RECEIVERS`, `DOCUMENT_RECEIVE_MAP`, `DOCUMENT_REQUEST`, `DOCUMENT_REQUEST_LIST`, `DOCUMENT_SCOPE`, `DOCUMENT_SCOPE_DETAIL`, `DOCUMENT_SCOPE_REF`, `DOCUMENT_TYPE`, `DOCUMENT_TYPE_ORG`, `DOC_ORG_REPUBLISH`, `DOC_ORG_REPUBLISHED`, `EMPLOYEE_TYPE_PROCESS`, `EXT_APP`, `FILES`, `FILES_ATTACHMENT`, `FILES_ATTACHMENT_COMMENT`, `FILES_COMMENT_DRAFF`, `FILES_COMMENT_SIGN`, `FILE_ATTACHMENT`, `FILE_ATTACHMENT_MAPPER`, `FILE_ENCRYPT_MAP`, `FLOOR`, `GROUP_APPLY`, `GROUP_IN_CV_GROUP`, `GROUP_MAPPING`, `HOME_WIDGET`, `IMAGE_ORG`, `LOG_TRANSTION_SIGN`, `MARK_ATTACH_HISTORY`, `MARK_LOCATION`, `MEETING`, `MEETING_ASSISTANT`, `MEETING_CONFIG`, `MEETING_MEMBER`, `MEETING_MINUTES`, `MESSAGE`, `MIGRATED_DOCUMENT`, `MIGRATED_FILES`, `MISSION`, `MISSION_NORM`, `NODE_ACTION`, `NOTICE`, `NOTIFICATION`, `ORG_CRITERIA_SOURCE`, `ORG_LEVEL`, `P12_CERT`, `POSITION`, `READ_NOTICE_HISTORY`, `REMINDER`, `REMINDER_DOCUMENT_RELATIONS`, `REMINDER_REPLY`, `REPORT_DAILY_HISTORY`, `SEARCH_TEXT_DRAFT`, `SECURITY_TYPE`, `SHELVE`, `SHELVES`, `SIGN_BRIEFCASE`, `SIGN_BRIEFCASE_ATTACH`, `SIGN_BRIEFCASE_ATTACH_OTHER`, `SIGN_BRIEFCASE_SIGNER`, `SIGN_BRIEFCASE_STATUS`, `SMS_BLACK_LIST`, `SMS_MASTER`, `SOURCE_MAP`, `STAFF`, `STAFFGROUP`, `STAFF_GROUP_ROLE`, `STAFF_IMAGE_SIGN`, `STAFF_IN_CV_GROUP`, `STORAGES`, `STORE_DOCUMENT_ROLE`, `STORE_TYPE_CONFIG`, `STORE_UNFOLOW`, `SUBMISSION_FILE`, `SUBMISSION_FORM`, `SUBMISSION_FORM_EDIT_HISTORY`, `SUBMISSION_MAP`, `SUBMISSION_MAP_FILE`, `SUBMISSION_PROCESS`, `SYSTEM_PARAMETER`, `SYS_FUNCTION`, `SYS_FUNCTION_EMPLOYEE`, `SYS_MENU`, `SYS_MESS_MUTILANGUAGE`, `SYS_NOTIFICATION_MUTILANGUAGE`, `SYS_ROLE`, `TEXT`, `TEXT_ASSISTANT_CONFIG`, `TEXT_ATTACH`, `TEXT_ATTACH_BASE`, `TEXT_ATTACH_OTHER`, `TEXT_BOOK`, `TEXT_CHAIN`, `TEXT_DRAFT`, `TEXT_DRAFT_HISTORY`, `TEXT_EDIT_HISTORY`, `TEXT_EXPLANATION`, `TEXT_EXPLANATION_ATTACH`, `TEXT_MARK`, `TEXT_NOTE`, `TEXT_PROCESS`, `TEXT_PROCESS_FILES`, `TEXT_PROCESS_HISTORY`, `TEXT_PROCESS_PARTNER`, `TEXT_RECEIVER`, `TEXT_SIGN_LOCATION`, `TEXT_SIGN_LOCATION_PARTNER`, `TEXT_SIGN_NEXT`, `TEXT_TEXT_ATTACH`, `TIME_ZONE_LOCAL`, `TO_DATE`, `USER_ORG_MAP`, `USER_ROLE`, `VHR_EMPLOYEE`, `VHR_FOREIGN_CONFIG`, `VHR_ORG`
