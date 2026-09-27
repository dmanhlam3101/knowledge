# Liên thông — đặc thù

- Điểm vào từ ngoài là **gen-2 webhook** `VOConnectProcessorController` (`/api/hook`: `send-document`, `update-status-document`, `send-mission`, `revoke-document`) → `VOConnectProcessorService`(Impl). Sửa ở đây ảnh hưởng đối tác ngoài — cần test với trục giả lập (`postman/` có collection ❓).
- Phần gửi ra vẫn gen-1 (`ConnectDocumentAction` → `controler/*` → `ConnectDocumentDAO`), gắn vào bước ban hành trong `TextController` — sửa liên thông phải đọc `documentPromulgate`.
- Entity XML (`InObjectSendXmlEntity`, `InObjectReceiveXmlEntity`, `InternalDocSendXmlEntity`…) lưu nguyên gói tin — hữu ích để debug lỗi gửi/nhận.
- `document/goverment/govermentDocument.zul` + `GovermentDocumentVM`, `TransferGovermentDocumentVM` không gọi Business/facade nào → khả năng là màn chết mềm (VM tồn tại nhưng không còn dữ liệu) ❓.
- Migrate: `MigratedDoc*` gen-2 + `Files.DownloadStreamMigratedFile` gen-1; bảng `MIGRATED_FILES` — dữ liệu hệ thống cũ chỉ đọc.
