# Liên thông — ví dụ mẫu

| Việc | Mẫu |
|---|---|
| Webhook nhận dữ liệu từ hệ thống ngoài (gen-2) | `VOConnectProcessorController.send-document` → `VOConnectProcessorServiceImpl` (tạo văn bản đến + `CONNECT_DOCUMENT`) |
| Phản hồi trạng thái cho hệ thống ngoài | `update-status-document` |
| Thu hồi đã gửi | `revoke-document` + gen-1 `connectDocumentAction.doEvictionDoc` |
| Màn theo dõi gửi/nhận liên thông | `document/goverment/connectDocument.zul`, `connectDocument_detail.zul` + `vm/document/ConnectDocumentVM` → `ConnectDocumentBusiness` |
| Tìm & xem dữ liệu migrate chỉ đọc (gen-2) | `MigratedDocController.search` + `MigratedDocumentBusiness` + `document/migrate/migrated_document.zul` |
