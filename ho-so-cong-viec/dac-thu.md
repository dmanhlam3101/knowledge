# Hồ sơ công việc — đặc thù

- **Lai gen-1/gen-2**: nghiệp vụ hồ sơ (CRUD, mượn/trả, kho/kệ/hộp, danh mục) ở gen-1 (`BriefManagementAction`, `CatalogBriefManagementAction`, `ShelveManagementAction`, `BoxManagementAction`, `StorageManagementAction`, `StoreTypeConfigAction` → `controler/*` → `BriefDAO`…); **nội dung hồ sơ** (thêm/xóa văn bản, file, đa phương tiện, số trang) ở `BriefDetailManagementController` (`/api/brief-detail`, đặt trong package gen-1 nhưng phong cách gen-2); **chia sẻ hồ sơ** ở gen-2 `BriefController` (`/api/brief`).
- Web: `BriefBusiness` 79 hàm; VM chính `BriefVM`, `BriefDetailVM`… (25 VM) — nhãn BE, tra cứu đơn vị legacy.
- `TypeConfigAction.getUserDocRolesByEmpId`, `getUserRolesDetail` được web gọi nhưng không nối được endpoint ❓ (đổi tên?).
- Hồ sơ móc với: văn bản (`processingTranferBriefDoc`, `addDocDraftToBrief`), phiếu trình (`add-to-brief`), ký số (`markDocumentByOrgForBrief`, `SignSoftHashMutiFileBrief`), chia sẻ ngoài (`/ext-brief`).
- SQL gần đây: `10012026_create_table_catalogin_brief_file.sql`, `20250303_add_column_table_brief_multimedia_file.sql` — đa phương tiện trong hồ sơ là tính năng mới.
