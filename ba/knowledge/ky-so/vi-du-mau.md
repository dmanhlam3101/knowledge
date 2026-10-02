# Ký số — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Ký số = tương tác **trình duyệt ↔ ứng dụng ký tại máy / MySign / SIM ↔ web ↔ BE**; thử phải có USB Token thật (đã cài ứng dụng ký), tài khoản MySign hoặc SIM CA thử — Postman không đủ. Khi copy, tránh các điểm ở `dac-thu.md` (nêu cuối từng mẫu).

## Mẫu 1 — Ký USB Token văn bản end-to-end (gen-1, đường đang dùng cho dự thảo / văn bản ký duyệt)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Popup xác nhận | `ZUL/widgets/confirmSign.zul:636-668`; CSVM `doSignUsbToken` :1836-1871 (kiểm xếp loại, `validateSign`, chứng thư người ký kế với văn bản mật, ảnh / vị trí ký, cảnh báo chân ký) | Chuỗi kiểm trước khi mở phiên ký |
| VM gọi | RVM `approveRequisitionInternal` :12187-12333 (rẽ theo hình thức ký 1 / 2 / 3 / 4 / 5 / 6) | Một chỗ rẽ nhánh theo `DIGITAL_SIGNATURE.TYPE` |
| Mở phiên | SVM `makeUsbSignalFileSession` :4444-4520 (`SecuritySession` + `Clients.evalJavaScript("security.usb…Request(...)")`) | Tạo phiên mã hóa ngữ cảnh, truyền id file đã mã hóa xuống JS |
| Trình duyệt | CHJS `usbSignAllFlatFormRequest` :916-1070 (cổng ứng dụng, lấy chứng thư, `PHASE_3` → ký hash → `PHASE_4` → `PHASE_X`, `reportActionResult`) | Trình tự pha |
| Servlet / phiên web | SSV :1595-1606, 1709-1732; SS `getDigestData` :843-1040 (hạn chứng thư, khớp USB đã xác nhận, gọi BE băm, nhớ `strUrl`), `appendSignature` :1849 | Kiểm chứng thư ở web; gửi bước 2 về đúng máy chủ băm |
| Business | `RB.getMultiFileDigests` :3959-4001, `appendMultiFileSignatures` :4021-4054 | Khóa `Sign.SignSoftHashMutiFile` / `Sign.SignSoftAttachMutiFile` |
| BE | `SR:88-103` → `SC.hashListFile` :511-892 (lọc văn bản, `setSignSession`) → `SU.hashListFile` :1480-2166; `SC.appendSignatureIntoListFile` :892-998 → `SU.appendSignatureIntoListFile` :2167-2816 | Lưu kết quả băm trong phiên; ghi DB ở bước gắn |

**Không copy**: cập nhật người ký ở bước băm (`dac-thu.md` L1); kiểm mã số thuế rỗng (L2); thêm một bộ `hash…` / `append…` thứ năm (bẫy 4) — ưu tiên Mẫu 2.

## Mẫu 2 — Ký USB cho đối tượng gen-2: **ký phiếu trình** (mẫu nên dùng khi làm đối tượng ký mới)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Mở phiên | SVM `makeUsbSignSubmissionForm` :4371-4430 (tải file đính kèm ý kiến rồi gọi `security.usbSignSubmissionRequest`) | Phiên ký gắn một id đối tượng |
| Trình duyệt | CHJS `usbSignSubmissionRequest` :1071-1170 | Hai pha băm / gắn |
| Servlet / phiên web | SSV lệnh `signsubmission` :1607-1616, 1733-1748; SS nhánh `getSubmissionFormId() != null` :846-862 (bước 1) và :1864 (bước 2) | Gọi một endpoint với `USBSignRequestDTO.step` 1 / 2 |
| Business | `BIZ/SubmissionFormBusiness.java` `signUsbSubmissionForm` :342-379 | — |
| BE gen-2 | `POST /api/submission-manager/submission-file/sign` (`BE2/controller/SubmissionManagerController.java:245`) → `SubmissionManagerServiceImpl.signSubmission` :1777-1925 (xem `../phieu-trinh/nghiep-vu.md` NV-08) | Endpoint gen-2 nhận bước + chứng thư / chữ ký, tự kiểm người tới lượt |

**Lưu ý**: nhánh này **không** qua kiểm "USB Token đã xác nhận" và hạn chứng thư của web (`dac-thu.md` bẫy 4, 11) — khi làm mới, đưa kiểm chứng thư vào BE.

## Mẫu 3 — Ký từ xa có popup đếm ngược và kết quả "thành công x / tổng y": **ký CloudCA (MySign)**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Gọi popup | RVM :12348-12404 (`new CloudCARequest(...)`, `ViewUtil.showPopupCloudCACountDown` — `WEB/voffice/util/ViewUtil.java:3449-3455`, đọc `SignResult` → `showResultMessage`) | Đóng gói yêu cầu ký vào một đối tượng truyền cho popup |
| Popup | `VIEW/widgets/cloud_ca_popup.zul` + CCVM :47, 74-206 (đếm ngược `js/countdown/CloudCATimeCircles.js`, sự kiện `start` / `finish`, `onSignEvent`) | Popup chờ xác nhận ngoài hệ thống |
| BE | `SC.signCloudCA` :3456-3734 (khóa văn bản đang chờ — `SU:5594-5650`, mã lỗi riêng 2300-2304 — `BE1/constants/ErrorCode.java:92-97`) | Khóa chống ký trùng có hạn; mã lỗi theo bước |

**Không copy**: hết giờ mà không hủy yêu cầu phía nhà cung cấp (L5); bỏ sót tham số khi chép từ yêu cầu vào phiên (L6); sửa trực tiếp hằng enum dùng chung (L8).

## Mẫu 4 — Ảnh theo loại có thời gian hiệu lực nối tiếp: **ảnh chữ ký người dùng**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Popup | `VIEW/widgets/imageSignature/insertSignatureImage.zul`, `updateSignatureImage.zul`; SIVM :110-584 | Một vùng tải ảnh cho mỗi loại (`areaTable`) |
| Kiểm | SIVM `validateAttachment` :196-218 (PNG, 90–1000 px), `validateSignatureImage` :433-480 (bắt buộc ngày, nối tiếp không chồng lấn với quá trình trước) | Kiểm chồng lấn khoảng hiệu lực theo loại |
| BE | `SISD.addSignatureImage` :46-96 (một khối PL/SQL: đóng ảnh trước `TO_DATE_ACTIVE = mới − 1` rồi chèn ảnh mới) | Tự đóng bản trước khi thêm bản mới |
| Chọn khi dùng | `SISD.getSignatureImageByCardId` :432-486 (hiệu lực tại ngày, ưu tiên loại) | Truy vấn "bản còn hiệu lực tại ngày X" |

**Không copy**: kiểm kích thước bằng `&&` như ảnh dấu (L16); để web tự ghi ngày hết hiệu lực bản trước như màn con dấu (`dac-thu.md` bẫy 14) — làm ở BE như ảnh chữ ký.

## Mẫu 5 — Đặt và lưu vị trí trên trang PDF theo từng người: **vị trí ảnh ký**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Màn PDF | `ZUL/widgets/securityPdfViewer.zul`; SPVM nạp vị trí :850-880, `saveSignatureImageLocation` :4314-4382 (gộp vị trí tự dò + thêm tay, quy đổi trang, đánh thứ tự theo cấp) | Kéo thả trên PDF rồi lưu một lượt |
| Business | `SIB.getListLocationByTextId` :258, `updateListLocation` :284 | — |
| BE | `ISD.updateListLocation` :1023-1118 (xóa mềm theo văn bản / file / người, chèn mới, đánh thứ tự), `ISD.autoDetectedSignLocation` :1194-1260 (đã lưu → dùng; chưa → dò chữ trong PDF) | "Vị trí lưu tay ưu tiên hơn vị trí tự dò" |

**Không copy**: xóa cờ ảnh của mọi người trong văn bản khi lưu cho một người (L15).

## Mẫu 6 — Phiếu theo dõi có mã vạch, trợ lý cập nhật trạng thái theo từng người, gửi SMS kết quả: **cặp trình ký**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Màn | `ZUL/requisition/file/requisitionFile.zul` (+ `requisitionFileAdd.zul`, `requisitionFileSearch.zul`) — RFVM; popup trạng thái `requisitionFileUpdateState.zul` — `RequisitionFileUpdateVM` | Hai tab "Trình ký / Xử lý" theo vai trò trợ lý |
| Mã vạch | `SBD:1100-1120` (sequence đệm 13 số, dùng lại mã cũ có điều kiện), `WEB/voffice/http/BarcodeServlet.java` (ảnh), `SBD:1906-2024` (in mã vạch lên PDF khi tải) | Cấp mã + in lên file khi tải |
| Trạng thái theo người | `SIGN_BRIEFCASE_SIGNER.STATUS` + bảng gợi ý bước kế `SIGN_BRIEFCASE_STATUS.NEXT_STATUS_ID` (`SBD:1431-1439`) | Bảng danh mục trạng thái có "bước kế" |
| SMS | `SBD:1361-1392` (mẫu 30, loại tin 110, thông báo) | — |

**Không copy**: không kiểm bước chuyển trạng thái ở BE, gửi lại người đã xong → SMS lặp, controller luôn trả thành công (`dac-thu.md` L27); dùng loại tin đã xóa (L28).
