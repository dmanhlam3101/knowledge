# Cách làm chuẩn: thêm một màn hình web (ZK MVVM) gọi BE

Mẫu: `view/voffice/reminder/*.zul` + `com.viettel.voffice.vm.reminder.*`.

## 1. Bộ file cho một màn hình danh sách + thêm/sửa + chi tiết

```
webapp/view/voffice/<domain>/
├── xxx.zul               khung: borderlayout, north = menuPathLabel + toolbarButton, center = include search + add
├── xxx_search.zul        form lọc + listbox + paging (id "includeSearch")
├── xxx_add.zul           form thêm/sửa (id "includeAdd"), ẩn/hiện theo VM
├── xxx_viewDetail.zul    popup chi tiết
└── xxx_add_modal.zul     (tuỳ chọn) bản modal để nhúng vào màn khác (vd. chi tiết văn bản)

java/com/viettel/voffice/vm/<domain>/
├── XxxVM.java            list + add (kế thừa SecurityVM<XxxEntity>)
├── XxxViewDetailVM.java
└── XxxLookupVM.java      (tuỳ chọn) popup chọn
```

## 2. Khung zul

```xml
<?page title="..." contentType="text/html;charset=UTF-8"?>
<zk>
  <div id="modelDiv" apply="org.zkoss.bind.BindComposer"
       viewModel="@id('vm') @init('com.viettel.voffice.vm.<domain>.XxxVM')"
       width="100%" height="100%">
    <borderlayout height="100%" sclass="content-panel-layout">
      <north border="none" sclass="tabpanelNorth">
        <div sclass="tabpanelLabel">
          <div sclass="leftTabpanelLabel" height="30px"><include src="/view/widgets/menuPathLabel.zul"/></div>
          <div sclass="rightTabpanelLabel"><include id="toolbar" src="/view/widgets/toolbarButton.zul"/></div>
        </div>
      </north>
      <center autoscroll="true">
        <div sclass="scrollbarCustom content-panel-layout-center">
          <include src="/view/voffice/<domain>/xxx_search.zul" id="includeSearch"/>
          <include src="/view/voffice/<domain>/xxx_add.zul" id="includeAdd"/>
        </div>
      </center>
    </borderlayout>
  </div>
</zk>
```

Trong file include, component được `@Wire("#includeSearch #xxxList")` từ VM cha. Binding: `@load(vm.list)`, `@command('doSearch')`, `@bind(vm.obj.field)`.

## 3. Khung VM

```java
@Init(superclass = true)
@AfterCompose(superclass = true)
public class XxxVM extends SecurityVM<XxxEntity> {
    @Wire("#includeSearch #xxxPaging") Paging xxxPaging;
    @Wire("#includeSearch #xxxList") Listbox xxxList;
    private XxxBusiness xxxBusiness;

    @Override
    protected void postViewInitialized() {          // được gọi sau @AfterCompose của SecurityVM
        xxxBusiness = new XxxBusiness(serviceConnection);   // serviceConnection có sẵn từ CommonModel
        super.paging = xxxPaging;
        // đọc tham số mở màn: ZkUtil.getParameter("viewType") ...
        doSearch();
    }

    @Command @NotifyChange({"list","totalCount"})
    public void doSearch() { list = xxxBusiness.search(buildSearchRequest()); }

    @Command
    public void onDoInsert() throws Exception {     // SecurityVM có sẵn chuỗi insert()/update()/validateDoSave()
        if (!validateDoSave()) return;
        boolean ok = xxxBusiness.save(buildSaveRequest());
        if (ok) { NotificationCenter.showSuccess(...); doSearch(); }
    }
}
```

Những gì `SecurityVM`/`CommonVM`/`CommonModel` đã cho sẵn (đừng viết lại): `serviceConnection`, `httpSession`, user hiện tại, `paging`, quản lý file đính kèm (`waitingUploadFiles`, `selectInfoTable`…), `screenName`/quyền, `insert()/update()/doSaveCallback()`.

## 4. Business phía web

```java
public class XxxBusiness extends Business {
    public XxxBusiness(ServiceConnection connection) { super(connection); }

    public List<XxxEntity> search(XxxSearchRequestDTO req) {
        String response = servePostRequest(new Gson().toJson(req), "api.xxx.search");   // → POST /api/xxx/search
        JsonObject root = new JsonParser().parse(response).getAsJsonObject();
        JsonElement data = root.has("data") ? root.get("data") : root.get("result");    // xem ReminderBusiness để lấy đúng nhánh
        return new Gson().fromJson(data, new TypeToken<List<XxxEntity>>(){}.getType());
    }
}
```

## 5. Những việc ngoài code — hay quên

| Việc | Ở đâu | Mẫu |
|---|---|---|
| Menu | `SYS_MENU` (SQL), URL = `/view/voffice/<domain>/xxx.zul` | `backend2.0/backendvoffice/sql/19122025_add_row_sys_menu.sql` |
| Gán menu cho vai trò | bảng **`ROLE_MENU`** (màn quản trị `roleMenu.zul` / `RoleMenuVM`); nếu chỉ mở cho một số đơn vị thì thêm `ORG_SYS_MENU` — **danh sách trắng**: chèn một dòng là mọi đơn vị khác mất menu | `he-thong` NV-09, NV-10, `dac-thu.md` bẫy 6–7; mẫu script `SQL/20250725_insert_menu_category_group.sql` (sửa 2026-10-02) |
| Nhãn đa ngôn ngữ | `common_voffice_vi.properties` (+ `_en`), key `voffice.<domain>.label.*` | Nhắc việc đang **ghi cứng tiếng Việt** trong zul / VM — đừng chép phần này (`lich-nhac-viec/dac-thu.md` mục 1) |
| Quyền nút | Điều kiện hiển thị viết trong VM (`visible="@load(vm.isXxx)"`), đặt ở **cả** màn chi tiết lẫn lưới nếu nút có ở hai nơi; BE không kiểm người gọi | kiến trúc tổng thể mục 5, bẫy 6 |
| Tra cứu đơn vị/người dùng trong màn | Dùng `iCommon.findById(SysOrganization.class, id)` / lookup widget sẵn có — đây là **ngoại lệ legacy được chấp nhận** cho tra cứu danh mục (reminder cũng dùng) | `ReminderVM.postViewInitialized` |
| Mở từ màn hình khác với tham số | `ZkUtil.getParameter("...")` + `LookupUtil.showDialog(...)` | `DocumentViewDetailVM` mở `reminder_add_modal.zul` |
| Reload màn cha sau khi lưu | `EventQueues.lookup(AppConstants.EVENT_QUEUE.EVENT_QUEUE_HOME_PAGE, true).publish(...)` | |
| Trang chủ / dashboard đếm số | `HomeBusiness`, `HomeController` (`/api/home`), `reminders.getCountReminderDashboard` | |

## 6. Kiểm tra trước khi giao

- Màn hình mở được từ menu với vai trò thường (không phải admin).
- Tìm kiếm + phân trang + thêm + sửa + xóa mềm hoạt động; F5 không lỗi (VM khởi tạo lại từ tham số).
- Không có `Delegate.getService(...)` mới ngoài `ICommonVoffice`/`ISysOrganization`/`ISysUser` cho tra cứu.
- `scan.py` thấy zul → VM → Business → endpoint nối đủ (không còn dấu hỏi "chưa nối" trong `ban-do.md`).
- Thêm dòng `SYS_MENU` **và** `ROLE_MENU`; người có vai trò được gán thấy menu (kiểm `ORG_SYS_MENU` nếu menu giới hạn đơn vị).
