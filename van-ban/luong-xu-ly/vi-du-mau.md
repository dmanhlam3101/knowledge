# Luồng xử lý / luồng ký — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-01). Viết tắt như `nghiep-vu.md`. Phân hệ là **gen-2 thuần** (không gen-1 tương đương) — mẫu tốt cho "màn cấu hình quản trị + đồ thị" và "API gợi ý người xử lý theo cấu hình".

## Mẫu 1 — CRUD cấu hình quản trị có kiểm vai trò ở BE, bật/tắt, xóa mềm, lịch sử: **Quản lý luồng**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/flow/flow.zul` (borderlayout + toolbar chung + 3 include search / edit / config — :7-37); lưới `flow_search.zul:157-237` (nút thao tác theo `isActive`, phân trang server + chọn cỡ trang) | Khung màn quản trị một zul, nhiều chế độ |
| VM | FVM kế thừa `CommonVM<Flow>`: `getDataList` / `countDataList` (:97-113), `validateBusinessDoSave` kiểm mã trùng qua BE (:399-412), `insert` / `update` / `delete` (:415-460), `doLock` có hộp xác nhận (:468-495) | Dùng khung `CommonVM` sẵn (toolbar Thêm / Lưu / Hủy) |
| Business | `FB.createOrUpdate` (:30-42), `getListFlow` đọc `content` + `totalElements` của `Page` (:56-80), path variable ghép chuỗi (`toggle-active-flow.` + id — :160-167) | Đọc `Page` gen-2 về web |
| Controller | `FMC:38-96` — endpoint mỏng, `ResponseUtils.getResponseEntity` | |
| Service | `FMSI.getListFlow` kiểm người gọi có vai trò `ADMIN` / `ADMIN_LEVEL1`, không có → `ErrorApp.FORBIDDEN` (:119-136); `createFlow` / `updateFlow` đặt vết người tạo / sửa (:155-182); `deleteFlow` xóa mềm (:186-196); `toggleActiveFlow` (:477-490) | Kiểm vai trò ở BE cho danh sách quản trị |
| Repository | `FRI.getListFlow`: JPQL dựng chuỗi, lọc cây đơn vị `vo.path LIKE '%/<id>/%'` cho nhiều đơn vị quản trị, tìm không dấu `handleVietnamese(...) LIKE ... ESCAPE '/'` (:42-88) | Lọc theo cây đơn vị; tìm kiếm không dấu |

**Không copy**: lịch sử ghi Elasticsearch ném lỗi sau khi đã lưu (`dac-thu` L7); `getFlowById` chỉ đọc bản ghi đang hoạt động (L1); kiểm mã trùng chỉ ở web (L3).

## Mẫu 2 — Lưu một đồ thị (nút + cạnh + thuộc tính) vẽ trên canvas: **Sơ đồ luồng**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul + JS | `ZUL/flow/flow_config.zul` (toolbar thêm nút theo loại, chế độ nối, xóa — :21-30; canvas :31-34; hàm cầu nối `zAu.send(new zk.Event(...))` :37-125); `JS` (`addNewNode` :158-227, chặn tự nối / nối trùng :1143-1156, nhấp đúp mở popup :1219-1230) | Cầu nối canvas ↔ VM bằng sự kiện ZK, không giữ trạng thái ở JS |
| VM | FVM giữ `nodes` / `nodeToNodes` phía server, cập nhật theo từng sự kiện (:173-279); popup cấu hình nút / cạnh qua `ViewUtil.createLookupConfigNode` / `createLookupConfigNodeAction` (`WEB/voffice/util/ViewUtil.java:3660-3668`; FVM :282-332) | Danh sách thực thể ở VM, popup trả về bằng `SearchEvent` |
| Cấp id trước | `GET /nodes/next-id` → `node_seq.nextval` (`NRJ:28-29`); sao chép cấp hàng loạt `CONNECT BY LEVEL <= :amount` (`NRJ:36-37`) | Id ổn định cho thực thể được nơi khác tham chiếu (`LIST_NODE_ID`) |
| Lưu | `FMSI.saveNodes` `@Transactional` (:288-380): xóa phần thừa, lưu nút giữ id, thay toàn bộ quan hệ con | Lưu cả đồ thị trong một giao dịch |
| Sao chép | `FMSI.copyFlow` (:200-284): ánh xạ id cũ → id mới rồi đổi đầu / cuối cạnh | Nhân bản đồ thị |

**Không copy**: cách xóa quan hệ con theo danh sách "giữ lại / gửi lên" làm sót bản ghi mồ côi (`dac-thu` L2); không kiểm cấu trúc đồ thị (L13); không khóa đồng thời (bẫy 4).

## Mẫu 3 — API gợi ý "ai ở bước kế tiếp" theo cấu hình, có phân trang và gom vai trò: **`doc-in/get-users-next-step` (V2)**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Business web | `DOCB.getListDocInUserFlowByOrg` / `getListOrgFlow` (:5669, :5773) | |
| Controller | `FMC:203-208` đặt `flowType` cố định theo endpoint | Một service, nhiều endpoint theo ngữ cảnh |
| Ngữ cảnh | `FMSI.getDocInParams` (:2057-2190): đọc bản ghi luân chuyển → chọn cấu hình theo thuộc tính đối tượng (`FRI.findFlowIdsByConfigTypeDoc` :105-184, có phương án mặc định) → nút hiện tại → nút kế theo hành động; truy vấn độc lập chạy song song `CompletableFuture` (:2104-2155) | Tách "xác định ngữ cảnh" khỏi "lấy danh sách" |
| Danh sách | `FMSI.getEmployeeSendDocsV2` (:2502-2704): gộp + khử trùng điều kiện (:2514-2535), phân trang id nhân sự trước (`VERI.getListEmployeeConfigNodes` qua bảng tạm theo phiên :567-720), nạp vai trò sau (`VERI.getListEmployeeAndRolesConfigNodes` :485-562), tra hành động theo **lô 20** có phương án dự phòng từng dòng (:2621-2674) | Mẫu khắc phục N+1 khi mỗi dòng cần thêm dữ liệu |
| Đánh dấu | chứng thư bảo mật cho văn bản mật (:2319-2325), cờ nắm tình hình (:2327-2334) | Bổ sung cờ sau khi phân trang |

**Không copy**: cache tĩnh tham số hệ thống không có hạn (bẫy 10); ba bản logic đơn vị logic (bẫy 6).

## Mẫu 4 — API thay thế danh sách có ràng buộc chặt + audit: **Cập nhật luồng ký tuần tự (`PUT /doc-out/{textId}/signing-flow`)**

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Web | `RB.replaceSequentialSigningFlow` gửi PUT qua `servePutRequestMappingType` (:6853-6862) | Gọi PUT từ web |
| Service | `SFUS.update` (:81-209): khóa bản ghi cha `findByTextIdForUpdate` (:86) → kiểm trạng thái cha → kiểm đúng người hiện tại (lỗi 403 — :223-230) → kiểm hình dạng yêu cầu (không xóa / không đổi phần đã xong, không di chuyển vị trí hiện tại, không trùng id, `clientRef` cho dòng mới — :232-282) → dựng danh sách mong muốn → giới hạn số dòng thêm, mã lỗi riêng `40005` (:172-179) → lưu, xóa phần bỏ → đồng bộ lịch sử + audit `HISTORY_CHANGE_SIGN` (:204-205, :500-540) → trả kết quả kèm `clientRef` để client ghép id mới (:542-587) | Khung "khóa → kiểm người → kiểm hình dạng → diff → lưu → audit" cho API sửa danh sách có thứ tự |
| Kiểm danh mục | `resolveIdentity` (vai trò `LDDV`/`TTDV`, đơn vị / chức vụ còn hoạt động — :374-410), `resolveAction` (chỉ `SIGN`/`APPROVE`/`SIGN_INITIAL` có trong `NODE_ACTION` văn bản đi — :412-422) | Kiểm giá trị đầu vào theo danh mục thật |
