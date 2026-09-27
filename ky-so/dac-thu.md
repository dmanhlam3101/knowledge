# Ký số — đặc thù

- **Gần như toàn bộ gen-1**: `SignResource` (`/Sign`) → `controler/*` (`TextController` phần ký, `DocumentSignService`) → `TextSignDAO`, `DocumentSignDAO`, `EmpCloudCADAO`, `CloudDeviceCertDAO`, `AutoDigitalSignDAO`. Gen-2 chỉ có phần phụ (ảnh chữ ký nhân viên, xác thực chữ ký, file mã hóa, danh sách phương thức ký).
- Web: không có Business riêng — hàm ký nằm trong `RequisitionBusiness` (`Sign.*`, `CertManagementAction.*`, `P12CertAction.*`, `imageSignAction.*`), `TaskBusiness` (`Sign.signMultiFileTask`), `BriefBusiness`, `SubmissionFormBusiness` (`submission-file/sign`). Client ký USB: `web-spring/.../http/signature/`, `plugin/webtwain`, `SecurityServlet`, `ConfirmServlet`; facade legacy `IDigitalSignature`.
- Ký = tương tác 3 bên (trình duyệt/plugin ↔ web ↔ BE ↔ CA). Khi sửa: test trên máy có USB token thật hoặc tài khoản CloudCA test; Postman không đủ.
- Hash/ký nhiều biến thể `SignSoftHashMutiFile{,Brief,Doc}` / `SignSoftAttachMutiFile{,Brief,Doc}` — thêm loại đối tượng ký mới = thêm cặp hàm theo mẫu này (hoặc tốt hơn: một endpoint gen-2 nhận `objectType`).
- Mật khẩu chứng thư, OTP: không log; `credentials.properties` (web) chứa cấu hình nhạy cảm.
- `CertManagementAction` (22 endpoint) là tích hợp với hệ thống CA (đăng ký/gia hạn) — nghiệp vụ hiếm dùng nhưng dễ vỡ khi CA đổi API.
