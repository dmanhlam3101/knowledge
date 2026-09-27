# Ký số — nghiệp vụ

> Ký số là **dịch vụ dùng chung**: văn bản đi (ký nháy/ký duyệt/đóng dấu), phiếu trình, hồ sơ, phiếu giao việc/đánh giá, biên bản họp đều gọi vào đây. Không có màn hình riêng lớn (2 zul) — chủ yếu là popup `signUsbToken.zul`, `signatureImageSelector.zul` nhúng ở các phân hệ, và quản trị chứng thư/ảnh chữ ký. BE gen-1 `Sign` (`SignResource`, 20 endpoint), `CloudCAAction`, `P12CertAction`, `CertManagementAction` (22), `imageSignAction`, `signBriefcaseAction`, `DocumentService` (`DocumentSignService`); gen-2 `StaffImageSignController`, `SignatureVerificationController`, `FileEncryptMapController`, `CaSupplierController`.

## 1. Phương thức ký (`getUserSignMethod`, `ca-supplier/get-list-sign-method`)

| Phương thức | Endpoint | Ghi chú |
|---|---|---|
| USB token (ký mềm phía client) | `Sign.SignSoft`, `SignSoftHashMutiFile` (ký hash nhiều file), `SignSoftAttachMutiFile` (+ file đính kèm), biến thể `*Brief` (hồ sơ), `*Doc` (văn bản đã ban hành); web `signUsbToken.zul` + plugin `com.viettel.plugin.webtwain` / `http/signature` | Web tính hash → client ký → BE ghép chữ ký |
| CloudCA (ký đám mây, OTP) | `Sign.SignCloudCA`, `CloudCAAction.authenticateUser`, `verifyOTPInSigning`, `registerDevice`, `deleteDevice`, `checkUserStatus`; `textAction.getListCloudCertificates`, `updateDefaultCloudCert`; bảng `EMP_CLOUD_CA`, `CLOUD_DEVICE_CERT` | Lỗi riêng `CLOUD_CA_SIGN_ERROR = 2300` |
| SIM CA (ký qua SIM) | `Sign.SignByCASIM`, `SignTextByCASIM`, `SIGN_SIM_CA = 33` | `voffMsspv20Seq.properties` |
| Ký ảnh / chữ ký hình | `imageSignAction.addSignImage`, `editSignImage`, `getImageSignByCardId`, `getListLocationByTextId`, `updateListLocation`; gen-2 `staff-image-sign`; `textAction.updateSignImageBySecrectary`, `getLastSignImageOfText` | Vị trí ký trên PDF (`MARK_LOCATION`) |
| Ký tự động | `AutoDigitalSign` (`AUTO_DIGSIG_TRANSACTION`) | ❓ dùng cho loại văn bản nào |
| Đóng dấu đơn vị | `textAction.markDocumentByOrg*`, `askForSeal`, `rejectMark`, `getOrgMarkedList`, `imageOrgAction.getOrgMarkList` (ảnh dấu `IMAGE_ORG`), `Sign.updateDatabaseAfterMark`, `TextMark` | Văn thư đóng dấu sau khi lãnh đạo ký |

## 2. Chứng thư số (`CertManagementAction`, `P12CertAction`)
Đăng ký (`makeCert`, gói `getListCertPackages`, OTP `confirmTransactionOtp`), kích hoạt (`activateCert`), gia hạn (`extendCert`, `signFileExtentCa`), đổi thông tin (`alterIdentification`), hủy (`cancelCert`, `cancelRegCert`), sao lưu/tải (`BackupCert`, `Download*FileInfoUser`), đổi mật khẩu P12 (`RequestResetCertificatePassword` → OTP → `updatePasswordP12Cert`), trạng thái (`getCertStateNow`, `listActiveCerts`), đồng bộ chứng thư (`textAction.synchonizeCertificate`, `getCertificateSynchronization`). Nhà cung cấp CA (`CA_SUPPLIER`, `CaSupplier`).

## 3. Xác thực chữ ký & file mật
- Xác thực chữ ký file ngoài: `DocumentAction.verifyExternalSignature`, gen-2 `SignatureVerificationController`.
- File mã hóa theo người/đơn vị: `FILE_ENCRYPT_MAP` (`FileEncryptMapController.get-list-file-encrypt-by-objectId/rootObjectId`), dùng bởi văn bản mật, phiếu trình, nắm tình hình.
- Kiểm tra thể thức trước ký: `DocumentFormalError`, `textAction.checkSpellText`.

## 4. Cặp trình ký (`signBriefcaseAction`)
Trợ lý gom nhiều văn bản vào "cặp" có mã vạch (`getBarcode`) cho lãnh đạo ký một lượt; trạng thái cặp (`getListSignBriefcaseStatus`, `updateStatusSignBriefcase`); đổi người ký (`updateSigner`). Web `requisition/file/*`.

## 5. Quy tắc
- QT1. Người ký phải có chứng thư hợp lệ (`getCertStateNow`, `get-next-signers-check-cert`) trước khi được đưa vào luồng.
- QT2. Ký xong luôn cập nhật DB qua `updateDatabaseSign` / `updateDatabaseAfterMark` (ký và ghi trạng thái là 2 bước).
- QT3. Ký nhiều file: hash từng file, một OTP/phiên (`*MutiFile`).
- QT4. Thư ký/trợ lý ký ảnh thay lãnh đạo theo ủy quyền (`SECRETARY_ROLE_ID_KEY`, `getLeaderOfAssitant`).
- QT5. Có khóa trạng thái ký (`LOCK_SIGN_STATE`, `STATUS_DELAY_SIGN = 417`) khi lãnh đạo hoãn ký.

## ❓
1. Phương thức nào đang dùng thực tế ở Khánh Hòa (USB token? CloudCA của nhà cung cấp nào?).
2. Ký tự động áp dụng ở đâu?
3. `DocumentSignKNTCService` / `AuthenticationKntcController` (KNTC = khiếu nại tố cáo?) là tích hợp với hệ thống nào?
