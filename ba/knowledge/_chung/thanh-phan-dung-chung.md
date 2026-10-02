# Thành phần dùng chung (web) — tìm trước khi viết mới

`view/widgets/*.zul` (112 file) + `com.viettel.voffice.widget.*` (206 class). Bản đồ đầy đủ: [`ban-do.md`](ban-do.md) (mục 1 — nhãn ☠ là widget chết). Dưới đây là nhóm chức năng để tra nhanh.

| Nhóm | Widget (zul) | Dùng cho |
|---|---|---|
| **Khung màn hình** | `menuPathLabel.zul`, `menuPathLabelVbbh.zul`, `toolbarButton.zul` (+ biến thể `toolbarButton{Info,Kpi,KpiPortal,KpiStatistic,SavePerDoc,SysUser,TaskRequisition,AuthenHistory,IntegratedSys}.zul`, `toolBarButton_Mission.zul`, `toolbarSign.zul`), `menubar.zul`, `mainMenuTree.zul`, `sysMenuTree.zul` | Mọi màn hình danh sách; toolbar có nút theo quyền |
| **Chọn người / đơn vị** | `sysUserLookup.zul`, `userLookup.zul`, `commonUserLookup.zul`, `userWSLookup.zul`, `subUserFlowLookup.zul`, `userFlowLookup.zul` (theo luồng), `sysOrganizationLookup.zul`, `sysOrgWS2Lookup.zul`, `connecVHRLookup.zul` / `connecVHRLookupVbd.zul` / `connectVHRGroupLookUp.zul` (cây VHR), `commanderLookup.zul`, `commanderSearchSysUser.zul`, `selectedCommander.zul`, `assignDirectorToMeetingLookup.zul`, `processGroupWSLookup.zul` | Giao việc, chuyển văn bản, chọn người ký, mời họp |
| **Chọn người ký / đối tượng ký** | `objectSignLookup2.zul`, `objectSignSearchSysUser.zul`, `objectSignSearchSysSubUser.zul`, `objectSignSearchSysOrg.zul`, `selectedObjectSign.zul`, `requisitionAssignLookup.zul`, `requisitionFlowLookup.zul`, `changeSignerHistory.zul`, `cloud_ca_list.zul`, `cloud_ca_popup.zul`, `popupAddCert.zul`, `certificateMessageBox.zul`, `imageSignature/` | Trình ký, ký số |
| **File đính kèm** | `attachment.zul`, `fileAttachment.zul`, `files.zul`, `docattachment.zul`, `docattachmentAppend.zul`, `docattachmentApen.zul`, `popupEditPageFile.zul` | Upload/xem file, số trang; VM nền `SecurityVM` quản lý danh sách file |
| **Chọn đối tượng nhận khi chuyển văn bản** | `multiTypeObjectLookup.zul` (`MultiTypeObjectLookupVM`, 5 tab: đơn vị / cá nhân / nhóm / nhóm đơn vị liên thông / đơn vị liên thông — phạm vi chọn tính theo từng trường hợp) | Mọi popup Chuyển văn bản — `van-ban/chuyen-van-ban` NV-02, NV-03 (sửa 2026-10-02) |
| **Xác nhận ký** | `confirmSign.zul` (`ConfirmSignVM` — nút Ký duyệt / Ký nháy / Đóng dấu / Ký CloudCA, chọn USB Token / SIM CA theo cấu hình người dùng) | Mọi bước ký số — `ky-so` NV-01 … NV-06 |
| **Chọn đối tượng nghiệp vụ** | `processingObjectLookup.zul`, `multiTypeObjectLookup.zul`, `catalogBriefLookup.zul`, `sysStoragesLookup.zul`, `workGroupLookup.zul`, `workGroupItemAddLookup.zul`, `createWorkLookup.zul`, `flowHistoryLookup.zul`, `videoConferenceGroupLookup.zul`, `videoConferenceRoomLookup.zul`, `alertLookup.zul`, `permissionLookup.zul`, `sysMenuLookup.zul`, `sysOperationLookup.zul`, `sysCatTypeLookup.zul` | Popup chọn văn bản/hồ sơ/kho/nhóm/luồng/phòng |
| **Xác nhận / nhập nhanh** | `confirm.zul`, `confirmApproved.zul`, `confirmInput.zul` (nhập lý do), `confirmSplitDocument.zul`, `confirmSplitManualDocument.zul`, `warningPresidentConflictMessageBox.zul` | Hộp thoại chuẩn — dùng thay vì viết popup mới |
| **Trang chủ / cá nhân** | `homeSetting.zul`, `create_home_widget.zul`, `create_home_widget_detail.zul`, `savePerDoc.zul`, `configPersonalDocCategory.zul`, `assignDocumentCategory.zul`, `noteBook.zul`, `versionControl.zul`, `work_result.zul` | Dashboard, lưu cá nhân |
| **Theo phân hệ** | `mission/`, `task/`, `template/`, `kpiPortal/`, `meetingRoomImage.zul`, `updateInfoCreateMeeting.zul`, `cbxOrgMark.zul`, `archiveDocumentButton.zul`, `advancedSearchDocumentToolbarButton.zul`, `documentPendingReceptionToolbarButton.zul`, `documentReturnedToolbarButton.zul`, `orgFollowDocInToolbarButton.zul` | Nút/toolbar chuyên biệt |

## Tiện ích Java dùng chung

| Class | Dùng cho |
|---|---|
| `LookupUtil.showLookup / showDialog / showCommentViewer` (`com.viettel.zk.common`) | Mở popup chọn / dialog. `LookupUtil.getPopupPermision` **không** kiểm quyền nút — chỉ đếm số cửa sổ popup đang mở theo `screenName` để không mở trùng (`LookupUtil.java:71-94`) (sửa 2026-10-02) |
| `ZkUtil.getParameter` (`com.viettel.zk.common`) | Đọc tham số truyền vào màn |
| `NotificationCenter`, `CustomMessageBox` (`com.viettel.util.notification`) | Thông báo trên màn (toast), hỏi xác nhận — **không** phải thông báo chuông / SMS |
| `MultimediaNotificationCenter` (`voffice.util`) | Web **ghi thẳng** hàng đợi SMS `SMS_MASTER` / email lịch họp (legacy — dùng ở họp, đánh giá); tính năng mới ghi SMS / thông báo qua BE (`SmsDAO`, `NotificationAction`) — `lich-nhac-viec` NV-11, NV-13 |
| `CommonResourcesUtil.getLabel / getWebserviceValue` | i18n, cấu hình |
| `DateUtil`, `ConverterUtil`, `CommonUtil`, `FileUtil`, `HTTPDownloadUtil` (`com.viettel.util`, `voffice.util`) | Ngày, chuyển đổi, file |
| `com.viettel.util.exporter.*`, `com.viettel.util.excel.*` | Xuất Excel/PDF/Word |
| `SessionUtil` (`voffice.util`) | Session, `getWebServiceConnection` |
| `Delegate.getService(I*.class)` (`util.servicelocator`) | Facade legacy — tính năng mới chỉ dùng cho tra cứu danh mục (code cũ còn ghi thẳng DB qua đây: họp, quản trị hệ thống… — kiến trúc tổng thể mục 3) |
| `EventQueues.lookup(AppConstants.EVENT_QUEUE.*)` | Reload giữa các VM |
| `CommonLookupVM`, `SecurityVM`, `CommonVM`, `CommonModel` (`voffice.common`) | Lớp nền VM |
| `com.viettel.voffice.http.*Servlet` (`PdfViewerServlet`, `GetServlet`, `BarcodeServlet`, `ShareFolderServlet`, `ProcessServlet`) | Xem PDF, tải file, mã vạch |

## Chat / comment (BE gen-2 nhỏ)

`DocumentChatController` (`/api/doc-chat`), `TextChatController` (`/api/text-chat`), `CommentAction` (`/commentAction`: bình luận + lưu cá nhân), `TextFileCommentAction` (ghi chú trên file PDF: `getListTextNote`, `updateTextFileComment`), web `chat/*`, `BChatFacade`. Bảng `MESSAGE`, `*_CHAT`.
