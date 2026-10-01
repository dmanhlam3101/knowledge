# -*- coding: utf-8 -*-
"""
Quy tắc gán mỗi thành phần code (zul, VM, Business, Controller, DAO, ...) vào một phân hệ nghiệp vụ.
Duyệt theo thứ tự, quy tắc khớp đầu tiên thắng -> quy tắc CỤ THỂ đặt TRƯỚC quy tắc chung.
Khớp trên chuỗi: đường dẫn file + tên class, đã lowercase.
Sửa file này rồi chạy lại gen.py khi thấy thành phần bị xếp sai (xem _chung/ban-do-tong/chua-xep.md).
"""
import re

DOMAINS = {
    'van-ban/den':          'Văn bản đến',
    'xu-ly-cong-viec':      'Xử lý công việc – giai đoạn TRƯỚC ban hành: dự thảo → xin ý kiến → trình ký → ký/phê duyệt → trả lại/từ chối (menu XỬ LÝ CÔNG VIỆC)',
    'van-ban/di':           'Văn bản đi – từ cấp số trở đi: cấp số → ban hành → văn bản ban hành → thu hồi/hủy',
    'van-ban/chuyen-van-ban': 'Chuyển văn bản – mọi luồng chuyển (đến: chuyển xử lý; đi: chuyển sau ban hành; tự động chuyển; giới hạn chuyển)',
    'van-ban/luong-xu-ly':  'Luồng xử lý / luồng ký',
    'van-ban/so-van-ban':   'Sổ văn bản',
    'van-ban/lien-thong':   'Liên thông văn bản (trục, VOConnect, cơ quan ngoài)',
    'van-ban/quan-ly-chung': 'Văn bản đã ban hành – xem / tìm kiếm / bàn giao / phạm vi / loại văn bản (dùng chung đến & đi)',
    'phieu-trinh':          'Phiếu trình',
    'ho-so-cong-viec':      'Hồ sơ công việc & lưu trữ (kệ / hộp / kho)',
    'nhiem-vu':             'Nhiệm vụ (mission) – của cá nhân / đơn vị, không gắn văn bản',
    'cong-viec':            'Công việc (task) – cá nhân, gắn văn bản',
    'hop':                  'Họp, lịch họp, phòng họp không giấy (eCabinet), biểu quyết',
    'ky-so':                'Ký số, chứng thư, CloudCA, ảnh chữ ký',
    'kpi-danh-gia':         'KPI, tiêu chí, đánh giá, báo cáo định kỳ, thống kê',
    'lich-nhac-viec':       'Nhắc việc (MỚI), thông báo, SMS, định hướng, nắm tình hình',
    'tai-lieu-mau':         'Thư viện, biểu mẫu, tài liệu cá nhân, từ điển tag',
    'he-thong':             'Quản trị hệ thống, danh mục, người dùng, vai trò, tổ chức, cấu hình',
    'tich-hop':             'Tích hợp ngoài: VHR, ViettelPay, WOPI, Solr/ES, mobile, chia sẻ ứng dụng ngoài',
    '_chung':               'Dùng chung: widget, chat, comment, file, common',
}

# (regex, domain)  – khớp đầu tiên thắng
RULES = [
    # ---- tên riêng khó đoán (đặt trước để thắng các quy tắc chung)
    # xếp lại theo rà soát module xu-ly-cong-viec (2026-09-30)
    (r'documentsigncontroller|documentsignservice|documentsignaction|textprocesscontroller|textprocessservice|textfilecontroller', 'xu-ly-cong-viec'),
    # xếp lại theo rà soát module van-ban/di (2026-10-01): cấp số thật = issussDocument.zul + DocumentLookUpVM
    (r'requisition_issue_number|requisition_vbbh|rejectpublish|documentpublishaction|textmarksync|issussdocument|documentlookupvm|documentoutvm|/documentout|popupvb_issue_number|popupaskforseal', 'van-ban/di'),
    (r'orgfollowerdocout', 'van-ban/quan-ly-chung'),
    (r'confirmsigndocumentdraft|popupselectrequisitionforsubmission', 'phieu-trinh'),
    (r'requisition/file/|requisitionfile|documentdraftfile|signusbtoken|signatureimageselector|p12cert|certmanagement|imagesign|image-sign|imageorgaction', 'ky-so'),
    (r'requisitionreport|textreport', 'kpi-danh-gia'),
    (r'submitforconsideration|documentproposalvm', 'van-ban/den'),
    (r'advancedsearchdocument|documentsendsearch', 'van-ban/quan-ly-chung'),
    (r'configdocmanager', 'he-thong'),
    (r'transfercontentdoc', 'he-thong'),
    (r'transferdoc/viewlisthistory|documentloginfovm', 'van-ban/quan-ly-chung'),
    (r'docautosenddocument|documentprocessautosendconfig|documentprocesstermconfigaction|documentrequestconfigdao|popupviewflow|popupmovelist|documentlookupmovelist', 'van-ban/chuyen-van-ban'),
    (r'proposalbusiness|proposalvm|requestcontroller|requestemail|\brequest\.java', 'phieu-trinh'),
    (r'agreechart|missionchart', 'nhiem-vu'),
    (r'taskfacade|\bitask\b', 'cong-viec'),
    (r'videoconference', 'hop'),
    (r'evaluationunit|orgki\b|ratingki|chart|docdailysummary|reportdailyhistory', 'kpi-danh-gia'),
    (r'alert\.java|orientorgmap', 'lich-nhac-viec'),
    (r'empca|documentformalerror', 'ky-so'),
    (r'extapp|extdocument|extshare|agencyservice', 'tich-hop'),
    (r'connectprocessin|inobject|internaldoc|migratedfiles', 'van-ban/lien-thong'),
    (r'flowentity|flowgrouptype|nodeaction|nodedeptuser|nodeentity|nodetonode', 'van-ban/luong-xu-ly'),
    (r'officepublishedreplacement|textmark|textreceiver|textservice|textentity|waitingnumberbook|textassistant|textedithistory|textpartner', 'van-ban/di'),
    (r'documentpublicstatus|documentprocessentity|documentarchive|documentfile|/entity/document\.java', 'van-ban/quan-ly-chung'),
    (r'changepassword|forgotpassword|/help\.zul|horizontalmenu|/index\.zul|profileinfo|register\.zul|selectrole|document_type', 'he-thong'),
    (r'search_all|popupchoosecondition|filecontroler|downloadallfile|imagedao|imageentity|emailmaster|emaildetail|/business/business\.java', '_chung'),
    (r'groupmanager|basecontroller|databasecontroller|securitycontroler|syncmenu|usercontroler|orgcontroller|cmcontroller|financedata|datareportexpense|adorgdao|mappingorg|orgdao|staffdao|employeedao|systemparameter|sysparameter|databasemanager|sourcemap|favourite|userdao|usermanu|userorgmap|userrole|banner|configdashboard|managerservice|systemdowntime|userdetails|usertoken|vipuser|usertableheader|area(entity)?\b|cvpriority|orgcombination|orglevel|orgmenu|securitytype|statusentity|timezone|messageentity|mappingresovle|primaryvariable|synchistory', 'he-thong'),
    # ---- văn bản: cụ thể trước
    (r'requisitionflow|flowmanager|flow-manager|/vm/flow/|/flow/|documentprocessterm|flowbusiness', 'van-ban/luong-xu-ly'),
    (r'textbook|bookdoc|bookdispatch|text-book', 'van-ban/so-van-ban'),
    (r'connectdocument|voconnect|/hook|goverment|docorgrepublish|textmarksync|textsync|/api/text$|migrateddoc|migratedocument|/migrate/', 'van-ban/lien-thong'),
    # chuyển văn bản: gom mọi luồng chuyển (đến + đi) vào 1 phân hệ riêng
    (r'transferdoc|transfer-doc|transferdocument|documenttransfer|transferbriefdoc|transferfinancedoc|configlimittransfer|limittransfer|popuptransfererror|multitypeobjectlookup', 'van-ban/chuyen-van-ban'),
    # trước ban hành (menu XỬ LÝ CÔNG VIỆC): dự thảo, trình ký, ký/phê duyệt, cho ý kiến
    (r'requisition|documentdraft|text-draft|textdraft|textcheckspell|textsign|historychangesign', 'xu-ly-cong-viec'),
    (r'textaction|textcontroller|textdao|text-process|textprocess|textfile|textcommon|textsearch|documentpublish|issuedocument|doc-out|docout|documentpublishedtmp|autodigitalsign|/vm/text', 'van-ban/di'),
    (r'docin|documentin|document-in|inputdoc|transferdoc|orgfollowerdocin|answerdoc|docleadercomment|documentsearchreceive|/document/process|documentreceive|reportsendreceivedoc|requesttoschedulemeetingdoc', 'van-ban/den'),
    (r'documenthandover|dochandover|documentscope|documenttype|document-types|documentinformality|documentcopy|documenthistorylog|document-history|documentkpi|document/|documentaction|documentbusiness|documentcontroller|documentdao|doccontroller|/api/doc$|/api/doc/|docservice|documentrequest|documentservice|documentsign|correctdocument|viewdoc|seachdoc|managerdoc|editdoc|keydoc|supervisiondoc|answerdocument|documentchat|doc-chat|answerdocumentaction|internaldocument|documentproposal|documentfacade|idocument\b|savepersonaldoc|personaldoccategory|personal-category', 'van-ban/quan-ly-chung'),
    # ---- phiếu trình
    (r'submissionform|submission|/vm/request|/request/|requestaction|requestbusiness', 'phieu-trinh'),
    # ---- hồ sơ
    (r'brief|shelve|boxs|boxmanagement|storage|storemanagement|storetypeconfig|typeconfigaction|catalogbrief', 'ho-so-cong-viec'),
    # ---- nhiệm vụ / công việc
    (r'mission|agreement|report-result|reportresult|workgroup|work-group|ext-mission|sharemission', 'nhiem-vu'),
    (r'/task|taskaction|taskservice|taskbusiness|personaltask|configtask|taskrating|asign_taskrating|taskdao|taskcontroller', 'cong-viec'),
    # ---- họp
    (r'meeting|meet\b|/api/meet|mettingweek|ecabinet|vote|scheduletomeeting|scheduleconfig|meetcontroller|meetservice', 'hop'),
    # ---- ký số
    (r'cloudca|p12cert|certmanagement|ca-supplier|casupplier|imagesign|image-sign|signbriefcase|file-encrypt|fileencrypt|/sign|signresource|signature|digitalsign|documentsignkntc|documentsignservice|empcloudca|clouddevicecert|signaturev', 'ky-so'),
    # ---- kpi
    (r'kpi|criteria|evaluatedorg|kiformula|ratioconfig|reportperiod|report-period|statistics|emprating|summaryusagereport|orgcriteria|proposepoint', 'kpi-danh-gia'),
    # ---- nhắc việc / thông báo
    (r'reminder|notice|notification|orientation|graspsituation|grasp_situation|smsintercept|smstask|/sms|multimedianotification|timeconfig', 'lich-nhac-viec'),
    # ---- tài liệu mẫu
    (r'template|tempaction|library|tagdictionary|tag-dictionary|treelibrary', 'tai-lieu-mau'),
    # ---- tích hợp
    (r'vhr|viettelpay|vcontract|wopi|solr|elastic|app-mobile|appmobile|mobile-publish|mobilepublish|ext-app|ext-doc|ext-brief|sharedocument|shareorg|shareextdoc|syncfav|connecteoffice|callback|/public|cmresource|\bcm\b|cmbusiness|enterprise|userdevice|user-device|kntc|vneid|sso', 'tich-hop'),
    # ---- hệ thống
    (r'admin|/config|configbusiness|category|/group|position|/vps/|sysuser|sysrole|sysorg|base-role|baserole|/menu|orgresource|/org\b|staffaction|cvgroup|imageorg|configparam|language|cache|/api/manager|managercontroller|authenticat|/log|logaction|logbusiness|version-control|versioncontrol|personalgroup|personaltreatmentstatus|user-table-header|home|pageintroduction|privateshortcut|systemmanager|system-downtime|leaderconfig|financialrecords|feedback|survey|/code/|codemaster|permission|roles|securityvm|lockstatus|mapconfig|indexcontroller|officecontroller|featuretrace|resovleissue', 'he-thong'),
    # ---- dùng chung
    (r'widget|chat|comment|/files|fileservice|attach|common|util|lookup|/mail', '_chung'),
]

_COMPILED = [(re.compile(p), d) for p, d in RULES]


def domain_of(*keys):
    """Trả về phân hệ cho một thành phần, dựa trên các chuỗi mô tả nó (path, tên class, base url ...)."""
    key = ' '.join(k for k in keys if k).lower().replace('\\', '/')
    for rx, d in _COMPILED:
        if rx.search(key):
            return d
    return None
