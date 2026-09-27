# Hồ sơ công việc — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Thêm loại nội dung mới vào hồ sơ (kiểu "đa phương tiện") | gen-2-style `BriefDetailManagementController.brief-multimedia` (GET list, POST upload `upload-brief-multimedia-file`, DELETE `delete-brief-multimedia`) + SQL `20250303_add_column_table_brief_multimedia_file.sql` + web `BriefBusiness` `api.brief-detail.brief-multimedia` |
| Chia sẻ đối tượng cho danh sách người/đơn vị | gen-2 `BriefController`: `get-list-brief-share`, `get-page-brief-share`, `get-all-be-shared-id`, `get-count-brief-share`, `update-brief-share-list` |
| Danh mục phân cấp theo đơn vị | `CatalogBrief.searchListCatalogBrief`, `getListCatalogBriefByOrgId`, `searchListChildOrg` + `catalogBriefTree/*.zul` + `vm/catalogBriefTree` |
| Vị trí vật lý kho/kệ/hộp có ràng buộc | `Storages.*` / `Shelve.*` (`checkShelveNumFloor`) / `Boxs.*` + `storageManagement/`, `shelve/`, `boxManagement/` zul |
| Mượn/trả có lịch sử | `Brief.briefBorrow`, `briefLend`, `processBriefBorrow`, `getListBriefHistoryBorrow` |
| Quyền theo loại tài liệu | `TypeConfigAction.addRolesDocType`, `updateRolesDocType` + `vm/financialRecordsRoles` |
