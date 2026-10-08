# YC_NV_08 — GHI CHÚ KỸ THUẬT CHO DEV (không phải checklist test)

> **Checklist để test là [checklist-test-giao-dien.md](checklist-test-giao-dien.md)** — 70 case bấm tay trên màn hình,
> không cần đọc mã nguồn. Tệp này chỉ là ghi chú kỹ thuật kèm theo, chỗ nào trong mã nguồn phải sửa và hai cái bẫy dễ
> làm lệch bảng. BA không cần đọc tệp này.
>
> Dùng khi code yêu cầu "thêm cột Hạn xử lý vào panel Danh sách người/ đơn vị cùng nhận".
> Nghiệp vụ: [thiet-ke-man-hinh.md](thiet-ke-man-hinh.md) · Đặc tả đầy đủ: [dac-ta.md](dac-ta.md) (quy tắc ở mục 4,
> điều kiện nghiệm thu ở mục 8, đường dữ liệu ở mục 10).
> Tích `[x]` khi xong. Dòng có **CHẶN** thì không tích được là chưa bàn giao được.
> Mục lục: 0 trước khi mở mã nguồn · 1 tầng dữ liệu · 2 tầng truyền dữ liệu · 3 tầng màn hình · 4 di động · 5 test · 6 không được làm · 7 định nghĩa hoàn thành.

## 0. Trước khi mở mã nguồn

- [ ] Đọc mục 4 của `dac-ta.md`: mười một quy tắc BR-01 → BR-11. Quan trọng nhất là BR-02, BR-03 (hạn của chính dòng),
      BR-05 (trống thì để trống), BR-10 (không tô màu).
- [ ] Đọc mục 10.7 ràng buộc triển khai, nhất là yêu cầu **sửa đủ mọi nhánh truy vấn**.
- [ ] Xác nhận phạm vi di động: TBD-01 đã chốt chưa. Chưa chốt thì làm phần web trước, phần dữ liệu vẫn làm vì web và
      di động dùng chung một hàm.
- [ ] Ghi lại nhánh và commit đang đứng (`git log -1 --oneline` trong `web-spring/` và `backend2.0/`) để có mốc so sánh
      trước khi sửa.

## 1. Tầng dữ liệu — truy vấn

Tệp: `backend2.0/backendvoffice/src/main/java/com/viettel/office/repositories/impl/DocumentRepositoryImpl.java`

- [ ] **CHẶN** `getDocComments(documentId, employeeId, listOrgIds, isGroupDocument)` quanh dòng 895 — thêm cột hạn vào
      **cả ba nhánh**: nhánh cá nhân (`document_in_staff`), nhánh đơn vị (`document_in_group`), nhánh văn bản ban hành.
- [ ] **CHẶN** `getDocComments(documentId, isGroupDocument, documentInStaffIdsViewComment, documentInGroupIdsViewComment)`
      quanh dòng 962 — thêm cột hạn vào **cả ba nhánh** của hàm nạp này.
- [ ] **CHẶN** `getParentDocComments(listStaffParentIds, listGroupParentIds)` quanh dòng 1040 — nhánh dòng cấp trên
      cũng phải có hạn, nếu không thì dòng cấp trên luôn trống sai dữ liệu (BR-08).
- [ ] Dùng đúng mẫu định dạng đang có trong cùng tệp: `to_char(<alias>.deadline_date, 'dd/MM/yyyy') deadlineDate`
      (xem các dòng 472, 494, 536, 598, 691 làm mẫu). Không tự định dạng ở tầng trên.
- [ ] Không thêm phép nối bảng nào. Hạn nằm ngay trên bảng đã có trong câu truy vấn (NFR-01).
- [ ] Không sửa điều kiện `where` của các truy vấn này. Số dòng trả về phải giữ nguyên trước và sau khi sửa.
- [ ] Đếm lại: tổng số nhánh truy vấn đã sửa phải là **bảy** (ba + ba + một).

## 2. Tầng truyền dữ liệu

- [ ] Thêm trường hạn vào `backend2.0/.../office/dto/response/DocCommentResponseDTO.java`. Kiểu chuỗi, đặt tên khớp
      bí danh trong truy vấn.
- [ ] Thêm trường tương ứng vào `web-spring/src/main/java/com/viettel/util/bean/DocCommentResponseDTO.java`. Lưu ý lớp
      này có **hàm khởi tạo đầy đủ tham số** — bổ sung tham số mới hoặc kiểm mọi nơi đang gọi nó.
- [ ] Thêm trường vào `web-spring/src/main/java/com/voffice/service/entity/DocCommentEntity.java` kèm hàm đọc và ghi,
      vì màn ZK đọc trực tiếp từ lớp này.
- [ ] Kiểm chỗ chuyển đổi giữa lớp phía máy chủ và lớp phía web để trường mới không bị rơi giữa đường.

## 3. Tầng màn hình

Tệp: `web-spring/src/main/webapp/view/voffice/document/reportSendReceiveDoc/popupVB.zul`, panel quanh dòng 2204.

- [ ] Thêm một `auxheader` nhãn "Hạn xử lý" vào **đúng vị trí thứ ba**, ngay sau nhãn thời gian chuyển.
- [ ] Thêm một `listheader` tương ứng để số cột ẩn khớp số ô. **Sai số lượng ở đây là lệch toàn bộ bảng.**
- [ ] Thêm một `listcell` vào `template name="model"` đúng vị trí thứ ba trong thứ tự ô.
- [ ] Đếm lại ba con số phải bằng nhau: số `auxheader` là chín, số `listheader` là chín, số `listcell` trong mẫu dòng là
      chín.
- [ ] Nhãn lấy từ tệp đa ngữ, không viết chữ cứng trong tệp màn hình. Khóa "Hạn xử lý" đã có sẵn trong
      `common_voffice_vi.properties`, ví dụ `voffice.receiveDoccument.label.deadline`. Thêm khóa mới thì phải thêm cho
      **mọi** tệp ngôn ngữ đang có.
- [ ] Ô căn giữa, hiện nguyên chuỗi, không thêm biểu tượng, không thêm sự kiện bấm (BR-09, BR-10).
- [ ] Rà lại bề rộng cột để bảng không tràn ngang. Thiếu chỗ thì thu hẹp hai cột đơn vị.

## 4. Phần ứng dụng di động

- [ ] Xác nhận hàm `getDocumentDetailMobile` trong `backend2.0/.../voffice/controler/DocumentController.java` dòng 4214
      đi qua cùng `getDocumentDetail`, nên trường mới tự có trong phản hồi của di động.
- [ ] Kiểm phần lọc riêng cho di động quanh dòng 4611 không làm mất trường mới.
- [ ] Gọi thử chức năng chi tiết văn bản cho di động, xem phản hồi có trường hạn và đúng giá trị từng dòng.
- [ ] Bàn giao tên trường và định dạng cho đội di động. Giao diện di động theo TBD-01.

## 5. Test

Toàn bộ case test nằm ở một chỗ duy nhất: [checklist-test-giao-dien.md](checklist-test-giao-dien.md).

- [ ] Tự chạy nhóm B và nhóm E1 trước khi gọi Tester. Đây là hai nhóm bắt lỗi lệch cột.
- [ ] Chạy nhóm E2, E3, E4 để chắc các luồng chuyển, xử lý và số đếm không đổi hành vi.
- [ ] Dựng trước chín văn bản mẫu theo mục A của tệp đó, nếu không sẽ thiếu trường hợp để thử.

## 6. Không được làm

- [ ] Không thêm, không sửa, không xóa cột cơ sở dữ liệu. Yêu cầu này không có phần chuyển đổi dữ liệu.
- [ ] Không tô màu, không gắn biểu tượng cho dòng quá hạn hay sắp đến hạn. BA đã chốt không làm.
- [ ] Không thêm chức năng gia hạn hay cho sửa hạn tại panel.
- [ ] Không đổi cách tính quá hạn ở hộp việc và ở thống kê, dù hai chỗ đang tính khác nhau. Việc đó đã được xác nhận là
      đúng nghiệp vụ, không thuộc yêu cầu này.
- [ ] Không thêm thuộc tính phục vụ kiểm thử vào tệp màn hình. Theo quy ước của dự án, đặt mã rõ nghĩa cho thành phần
      mới là đủ.
- [ ] Không chạy lệnh ghi dữ liệu trên cơ sở dữ liệu dùng chung. Cần dữ liệu thử thì tạo bằng chính giao diện chuyển
      văn bản.

## 7. Định nghĩa hoàn thành

- [ ] Bảy nhánh truy vấn đã sửa đủ, đã đếm lại.
- [ ] Ba con số trong tệp màn hình bằng nhau và bằng chín.
- [ ] Nhóm B và nhóm E1 của checklist test giao diện đã chạy hết, không còn case không đạt.
- [ ] Nhóm E2, E3, E4 đã chạy, không luồng nào đổi hành vi.
- [ ] Liệt kê tệp đã sửa và in lệnh commit gợi ý cho người kiểm tra. Theo quy ước dự án, DEV tự commit sau khi tự kiểm.
