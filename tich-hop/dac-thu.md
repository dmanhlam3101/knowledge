# Tích hợp — đặc thù

- 19 controller thuộc phân hệ; gen-2 chiếm phần lớn (`Vhr*`, `Share*`, `AppMobile*`, `Public`, `Callback`); gen-1 giữ WOPI, Solr, VHR sync, ViettelPay, VContract, CM.
- `VhrOrgController` / `VhrEmployeeController` là **nguồn tra cứu đơn vị/người dùng chuẩn cho gen-2** — tính năng mới nên gọi đây thay vì `ISysOrganization` / `ISysUser` legacy.
- `ShareDocumentController` có endpoint `in` / `out` trùng tên nhiều verb — đọc kỹ `@GetMapping` / `@PostMapping`.
- WOPI: URL chứa `encryptedFileInfo`; `WOPIBusiness.files` + `convertPdf` được `AddAttachFileVM` (văn bản) và phiếu trình dùng; sửa WOPI test cả hai.
- Cấu hình URL tích hợp nằm ở nhiều file: web `application.properties` (`voffice.service.url*`, `sso.ws.url`), `edoc.properties`, `aqms.properties`, `collaboration.properties`, `sms.properties`, `credentials.properties`; BE `application-prod.properties` (`elasticsearch.*`, Redis, VHR…). Không hard-code URL trong code.
- `ConnectVHRVM` (`vps/sysConnectVHR`) là màn cấu hình cây đơn vị VHR ↔ VOffice — cấu trúc tổ chức tỉnh phụ thuộc bảng `CONNECT_VHR`.
