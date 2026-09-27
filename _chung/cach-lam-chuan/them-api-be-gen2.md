# Cách làm chuẩn: thêm một endpoint BE gen-2

Dùng khi: web/mobile cần dữ liệu hoặc thao tác mới, kể cả cho phân hệ đang chạy gen-1 (thêm endpoint gen-2 mới **thay vì** đục vào `controler/*Controller` gen-1).

## Khung code (rút từ `ReminderController` / `ReminderServiceImpl`)

```java
// controller/XxxController.java
@RestController
@RequestMapping("/api/xxx")                      // kebab-case; hoặc tên ngắn như "/reminders"
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class XxxController {
    XxxService xxxService;

    @PostMapping(value = "/search", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<ResultResponse<Page<XxxResponseDTO>>> search(@RequestBody XxxSearchRequestDTO request) {
        request.setUserId(getUserId());          // import static com.viettel.office.core.utils.CoreUtils.getUserId
        return ResponseUtils.getResponseEntity(xxxService.search(request));
    }

    @PostMapping(value = "/insertOrUpdate", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<ResultResponse<Long>> save(@RequestBody XxxSaveRequestDTO request) {
        return ResponseUtils.getResponseEntity(xxxService.save(request, getUserId()));
    }
}

// services/impl/XxxServiceImpl.java
@Service @RequiredArgsConstructor @Log4j2
public class XxxServiceImpl implements XxxService {
    private final XxxRepositoryJPA xxxRepo;
    private final XxxRepository xxxSqlRepo;       // nếu cần SQL tay

    @Override @Transactional(readOnly = true)
    public Page<XxxResponseDTO> search(XxxSearchRequestDTO req) { ... }

    @Override @Transactional(rollbackFor = Exception.class)
    public Long save(XxxSaveRequestDTO req, Long userId) {
        // validate → map DTO→entity → set createdBy/updatedBy/delFlag=0 → xxxRepo.save
    }
}

// repositories/jpa/XxxRepositoryJPA.java
public interface XxxRepositoryJPA extends JpaRepository<XxxEntity, Long> {
    @Query("SELECT new com.viettel.office.dto.response.xxx.XxxResponseDTO(e.id, e.name) FROM XxxEntity e WHERE e.delFlag = 0 AND e.orgId = :orgId")
    List<XxxResponseDTO> findByOrg(@Param("orgId") Long orgId);

    @Modifying
    @Query("UPDATE XxxEntity e SET e.delFlag = 1, e.updatedAt = :now, e.updatedBy = :userId WHERE e.id = :id")
    int softDelete(@Param("id") Long id, @Param("now") Date now, @Param("userId") Long userId);
}
```

## Checklist

- [ ] Đặt tên endpoint theo động từ nghiệp vụ: `search`, `getDetail`, `insertOrUpdate`, `delete`, `approve`, `reply`, `remindAgain` (đúng phong cách reminder). Tất cả **POST**.
- [ ] Không nhận `userId`/`orgId` ghi từ client; lấy từ JWT (`getUserId()`), rồi tra org của user khi cần.
- [ ] Phân trang: `Pageable` / `Page<T>` (gen-2) hoặc `startRecord/pageSize` khi web cũ yêu cầu.
- [ ] Soft delete, lọc `delFlag = 0` mọi query.
- [ ] Lỗi nghiệp vụ: throw exception riêng hoặc `ResponseUtils.getResponseEntity(ErrorApp.X, null)`; message vào `messages_vi.properties`.
- [ ] Nếu endpoint phục vụ ứng dụng ngoài/mobile: prefix `/ext-*` hoặc `/api/app-mobile` và kiểm tra `jwtIgnoreConfig` nếu cần bỏ JWT.
- [ ] Ghi Swagger annotation nếu team đang dùng (`/voffice-api-docs`).
- [ ] Thêm hàm tương ứng vào `web-spring/.../com/voffice/service/business/XxxBusiness` với key `"api.xxx.search"` (dấu `.` ↔ `/`).
- [ ] Chạy `knowledge/_tools/scan.py && gen.py` — endpoint mới sẽ xuất hiện trong `ban-do.md` và `web-goi-be.md`.

## Khi nào KHÔNG làm gen-2 mới

- Chỉ sửa một điều kiện nhỏ trong endpoint gen-1 đang được nhiều màn hình dùng → sửa tại chỗ, thêm hàm `...V2` nếu thay đổi hành vi (xem `sua-tinh-nang-cu.md`).
- Dữ liệu chỉ có ở tầng web legacy (`ISysOrganization`, `ISysUser`) và màn hình đang legacy toàn phần → cân nhắc giữ legacy cho nhất quán, nhưng ghi vào `dac-thu.md` là nợ kỹ thuật.
