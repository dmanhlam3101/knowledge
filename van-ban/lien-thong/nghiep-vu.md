# Liên thông văn bản — nghiệp vụ

> Gửi/nhận văn bản với **cơ quan ngoài hệ thống** (trục liên thông văn bản quốc gia / tỉnh, VPCP, đơn vị liên thông) và **giữa các đơn vị nội bộ** dùng chung hệ thống. Bảng `CONNECT_DOCUMENT` (trạng thái gửi/nhận), `CONNECT_PROCESS_IN`, `IN_OBJECT_*` (XML nhận/gửi theo chuẩn edXML), `INTERNAL_DOC_*` (liên thông nội bộ), `MIGRATED_DOC`/`MIGRATED_FILES` (văn bản chuyển từ hệ thống cũ). BE gen-1 `connectDocumentAction`, `DocOrgRepublish`, `textMarkSyncAction`; gen-2 `VOConnectProcessorController` (`/api/hook` — **webhook nhận từ trục**), `TextSyncController` (`/api/text/sync-text`), `MigratedDocController`. Web `document/goverment/*`, `document/migrate/*`, `ConnectDocumentBusiness`, `MigratedDocumentBusiness`; cấu hình `edoc.properties` (web).

## Luồng
| Chiều | Bước | Endpoint |
|---|---|---|
| **Gửi ra** (khi ban hành văn bản đi có người nhận là đơn vị liên thông) | Ban hành → sinh gói XML (`InObjectSendXml`/`InternalDocSendXml`) → gửi trục → cập nhật trạng thái (`addStateConnectDocument`) → xem chi tiết gửi (`getListConnectDocOutDetail`) → thu hồi (`/api/hook/revoke-document`, `doEvictionDoc`) | gen-1 `connectDocumentAction`, gen-2 `hook` |
| **Nhận vào** (trục gọi webhook) | `POST /api/hook/send-document` → tạo `CONNECT_DOCUMENT` + văn bản đến "chờ tiếp nhận" (`van-ban/den`, `update-exist-connect-document` nếu đã có) → văn thư tiếp nhận → `update-status-document` báo ngược trạng thái (đã nhận/đã xử lý/từ chối) | gen-2 `VOConnectProcessorController` |
| Nhận nhiệm vụ từ cấp trên | `POST /api/hook/send-mission` → nhiệm vụ (`nhiem-vu`) | gen-2 |
| Liên thông nội bộ (đơn vị cùng hệ thống, khác cây tổ chức) | `transferInternalOrgDoc`, `getListInternalOrg`, `TYPE_ORG_CONNECT = 3`, `TYPE_GROUP_CONNECT = 4`, menu *Đơn vị liên thông* | gen-1 |
| Văn bản từ VPCP | `document/goverment/govermentDocument.zul`, `transferGovermentDocument.zul` (VM không gọi dữ liệu — ❓ còn dùng), menu *Văn bản từ VPCP*, *Báo cáo VP CP* | |
| Đăng lại văn bản của đơn vị khác | `DocOrgRepublish.getBaseDocument` (`DocOrgRepublishAction`) | gen-1 |
| Đồng bộ dấu/ký với hệ thống khác | `textMarkSyncAction.*`, `TextSyncController.sync-text` | |
| Migrate hệ thống cũ | `document/migrate/*` + `MigratedDocumentVM` → `api.migrated-doc.search/detail`, `Files.DownloadStreamMigratedFile`, `verifyExternalSignatureMigratedDoc` | gen-2 + gen-1 |

## Quy tắc
- QT1. Đơn vị nhận liên thông phải có trong danh mục đơn vị liên thông (`getOrgConnectDocument`, cấu hình `VHROrgAction`/`Org`).
- QT2. Văn bản nhận từ trục **không được sửa nội dung**, chỉ tiếp nhận/trả lại; trạng thái phản hồi về trục theo chuẩn.
- QT3. Thu hồi văn bản đã gửi liên thông = `revoke-document` + hủy ban hành ở `van-ban/di` ❓ thứ tự.
- QT4. Webhook `/api/hook/*` phải nằm trong `jwtIgnoreConfig` hoặc dùng xác thực riêng ❓ (kiểm tra `WebSecurityConfig`).

## ❓
1. Trục đang kết nối là trục LGSP tỉnh Khánh Hòa hay trục văn bản quốc gia? Chuẩn edXML phiên bản nào?
2. `goverment/*` (VPCP) còn hoạt động hay là di sản Viettel?
3. `merge/` có liên quan tới migrate dữ liệu không?
