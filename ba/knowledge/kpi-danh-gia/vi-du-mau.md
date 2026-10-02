# KPI, chấm điểm, đánh giá, báo cáo — ví dụ mẫu để copy pattern

> Tính năng thật trên `kha_develop` (2026-10-02). Viết tắt như `nghiep-vu.md`. Phân hệ có ba thế hệ code; **tính năng mới làm theo gen-2** (mẫu 1–4). Cụm legacy (bộ tiêu chí, KPI đơn vị, đánh giá đơn vị, cấu hình tỷ lệ) chỉ để hiểu, **không copy** (`dac-thu.md` mục 1).

## Mẫu 1 — CRUD gen-2 có phạm vi dữ liệu kiểm ở BE: **Cấu hình người đánh giá / phê duyệt** (NV-03)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `ZUL/mission/reportPeriodConfig/reportPeriodConfig.zul` (+ `report_period_config_search.zul`, `report_period_config_add.zul`) | Khóa trường không cho đổi khi sửa (`isViewUpdate` — `report_period_config_add.zul:45-56`) |
| VM | RPCVM `validateDoSave` :638-667 (bắt buộc, kiểm trùng bằng `find-by-sys-user-id`), lookup giới hạn vai trò :141-152 | Kiểm trùng qua một endpoint đọc trước khi lưu |
| Business | RPCB (`api.report-period-config.*`) | Khóa `a.b` → URL `/a/b` |
| Controller | RPCC :28-62 (5 endpoint mỏng) | — |
| Service | RPCSI :28-115 — xóa mềm có `DELETED_BY` / `DELETED_DATE` (:93-96) | Xóa mềm đủ cột vết |
| Repository | RPCRI :27-128 — danh sách chỉ trong cây đơn vị người dùng là `ADMIN` / `ADMIN_LEVEL1` / `SUPPER_ADMIN` (`CONNECT BY` — :36-80) | **Phạm vi dữ liệu lọc ở BE** (ít màn trong hệ thống làm vậy) |
| Bảng | `REPORT_PERIOD_CONFIG` (sequence `REPORT_PERIOD_CONFIG_SEQ`, cột vết đủ, comment cột — DB DEV) | Migration có comment từng cột |

**Không copy**: kiểm trùng chỉ ở web (BE `create-or-update` không kiểm lại — RPCSI:55-78); ép kiểu generic sai (RPCSI:48).

## Mẫu 2 — Thêm / sửa / xóa mềm gen-2 validate lại ở BE: **Cổng KPI** (NV-21)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | `view/widgets/kpiPortal/add.zul` (popup), `ZUL/kpiPortal/kpi_search.zul` (nút theo `vm.isAdmin`) | Popup thêm / sửa phát lệnh làm mới danh sách (`refreshKpiPortalList` — KAVM:219-224; KPVM:330-333) |
| VM | KAVM `doSave` :121-226 (validate độ dài, bỏ trùng danh sách, đổi MB → byte :143-165) | Validate ở web để báo sớm |
| Controller | KPC :28-72 — `POST /update/{kpiId}`, `GET /{kpiId}`, `POST /delete/{kpiId}` | Id trên đường dẫn |
| Service | KPSI `create` :702-754, `update` :756-833 (**validate lại** tên, API, dung lượng, mục tiêu; **id đường dẫn phải trùng body** :769-772; chỉ ghi trường khác null; `CREATED_BY` / `UPDATED_BY` = `CoreUtils.getUserId()`), `delete` :838-859 (xóa mềm idempotent) | Khung "validate lại ở BE → ghi vết → xóa mềm idempotent" |
| Repository | `KpiPortalJPA` (`findActiveFunctions`, `countAllByIsActive`) | JPA thuần cho CRUD đơn giản |
| Truy vấn Elasticsearch | KPSI :135-260 (percentiles + filter theo luật khớp tên function — `toRule` :446-471) | Mẫu tổng hợp số liệu từ log ES |

**Không copy**: kiểu cột hẹp hơn giới hạn web (`TARGET NUMBER(3,2)` — `dac-thu.md` L28); Business đoán định dạng phản hồi bằng nhiều nhánh (KPB:23-87); trung bình của trung bình khi cần tỷ lệ theo số giao dịch.

## Mẫu 3 — Thống kê theo đơn vị nhiều chiều, phạm vi "đơn vị / đơn vị + trực thuộc": **Báo cáo tổng hợp — bảng văn bản đi** (NV-22)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| zul | SUZ:247-282 (bảng), SUZ:52-142 (bộ lọc đơn vị, phạm vi, khoảng ngày) | — |
| VM | UVM `fetchStatistics` :288-373 (5 truy vấn song song, sắp lại phía web), `doExport` :376-696 (Excel nhiều sheet từ mẫu `.xls`) | Chạy nhiều bảng song song, xuất từ cùng dữ liệu |
| Business | SRB:71-92 `servePostRequest("api.statistics.get-document-out-statistics")` | — |
| Controller → service | SRC:35-38 → SRS:41-43 | — |
| Repository | SRR `getDocumentOutStatisticsV2` :336-433 — CTE `org_scope` chọn phạm vi bằng `M_ORG_WITH_CHILD` (phạm vi 0) hoặc chính đơn vị (1); một tập gốc dùng chung (`/*+ MATERIALIZE */`); mọi điều kiện là tham số; tỷ lệ tính trong Java (:424-431) | **Mẫu SQL thống kê theo cây đơn vị** |
| Hạ tầng | `SQL/20260825_vptwd_optimization_database.sql:66-78` (view vật lý cây đơn vị phẳng, làm mới 30 phút) | Dùng lại `M_ORG_WITH_CHILD` thay vì `CONNECT BY` mỗi lần |

**Không copy**: phạm vi "đơn vị + trực thuộc" vừa cộng con vào dòng cha vừa liệt kê con (đếm hai lần — `dac-thu.md` bẫy 13); chia nguyên khi tính tỷ lệ (L29).

## Mẫu 4 — Quy trình "lập → chấm → gửi → duyệt / từ chối" có lịch sử thao tác: **Đánh giá công tác tuần** (NV-04 … NV-07)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| Hằng trạng thái | `C2:805-828` (`REP_IN.STATUS`), `C1:2663-2672` (loại lịch sử), `C1:2675-2681` (mã kết quả kiểm gửi) | Gom hằng trạng thái + mã kiểm hợp lệ thành enum số |
| Kiểm trước khi chuyển bước | `check-valid-send-approval` (RPIC:106 → RPISI:1327-1348 → RPIRI:815-875) trả mã lý do; web đổi mã → thông báo (`zk-label.properties:10427-10430`) | Endpoint "kiểm hợp lệ" tách khỏi endpoint ghi |
| Ghi lịch sử | RPISI:1280-1295 (`REPORT_PERIOD_HISTORY` với `ACTION_TYPE` + ý kiến) gọi ở mọi bước tạo / sửa / chấm / duyệt / từ chối / xóa | Một hàm ghi lịch sử dùng chung |
| Phân quyền dữ liệu theo cấu hình | RPIRI `sqlSelectWeek` :636-752 lọc `RATING_USER_ID` / `APPROVING_USER_ID` | Ai chấm / ai duyệt lấy từ bảng cấu hình, không từ vai trò |
| Xuất PDF | RPISI:358-404, 482-814 (OpenPDF, bảng gom theo cây nhóm) | — |

**Không copy**: hai đường duyệt không đồng bộ (`dac-thu.md` bẫy 1); `saveAll` entity dựng từ câu native (L4); ghi người cập nhật vào `DELETED_BY` (L2); đọc bảng xếp loại không lọc dòng chi tiết đã xóa (DB DEV ngày 2026-10-02: bộ `XLDGCN` đang dùng gồm 4 dòng đã xóa mềm — `dac-thu.md` L19); đặt trạng thái bằng số literal (`RPASI:123`); SQL dựng theo nhiều cờ trong một hàm (`sqlSelectWeek`); kiểm điểm / kiểm trùng chỉ ở web.

## Mẫu 5 — Sinh **văn bản trình ký** từ bảng số liệu (gen-1): **Tổng hợp chấm điểm đơn vị → trình ký** (NV-12)

| Tầng | Vị trí | Copy phần nào |
|---|---|---|
| VM | CORVM `doSubmit` :1142-1247 (một endpoint, `status` 0 lưu / 1 xem trước / 2 trình ký / 3 xem văn bản), kiểm người ký và ảnh chữ ký :1153-1172 | Một nút xem trước PDF trước khi trình |
| Controller | OC `createTextFromOrgCriteriaRatingTotalList` :680-729 | — |
| DAO | OCRTDAO `createTextFromOrgCriteriaRatingTotalList` :429-596: sinh PDF Jasper (`FU:5459-5620`, mẫu `report/template/cham_diem_don_vi.jrxml`) → khóa dữ liệu nguồn (`lock()` :707-732) → `DocumentSignDAO.addText` với thuộc tính mặc định đọc từ cấu hình JSON `json.text.default.from.orgrating` → `sendAndSign` → gắn `TEXT_ID` về bảng nguồn (:388-419) | Khung "khóa số liệu → sinh file → tạo TEXT → trình ký → lưu liên kết"; kiểm văn bản đã trình còn hiệu lực theo `TEXT.STATE` (:606-634) |

**Không copy**: chuỗi cố định trong PDF ("Hà Nội", "Văn phòng" — `dac-thu.md` bẫy 4); truy vấn theo kỳ không lọc loại kỳ (L26); id vai trò ghi cứng trong SQL.

## Mẫu 6 — Đọc cấu hình theo **đơn vị gần nhất có hiệu lực**

`VTER.getRatioConfigByOrg` :124-126 → facade `IRatioConfig.getRatioConfig` (RCF:204-217) → RCS:161-164 → `RCDAO.getRatioConfig` :104-121: một câu native leo cây `VHR_ORG` (`CONNECT BY PRIOR ORG_PARENT_ID`), lọc loại, `DEL_FLAG = 0`, khoảng hiệu lực (`TRUNC`), `ORDER BY ORG_LEVEL DESC`, lấy dòng đầu; quy điểm ra mức ở `VTER.getRankingKey` :153-170. Đây là cách chọn đúng nhất trong các bản (`dac-thu.md` bẫy 7) — khi viết gen-2 nên chuyển câu này sang repository BE thay vì copy facade.
