# -*- coding: utf-8 -*-
"""Sinh PDF huong dan mobile (tieng Viet) bang reportlab."""
import io
import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

FONT_DIR = r'C:\Windows\Fonts'
pdfmetrics.registerFont(TTFont('VN', FONT_DIR + r'\arial.ttf'))
pdfmetrics.registerFont(TTFont('VN-Bold', FONT_DIR + r'\arialbd.ttf'))
pdfmetrics.registerFont(TTFont('VN-Italic', FONT_DIR + r'\ariali.ttf'))
pdfmetrics.registerFont(TTFont('VNMono', FONT_DIR + r'\consola.ttf'))
pdfmetrics.registerFont(TTFont('VNMono-Bold', FONT_DIR + r'\consolab.ttf'))
pdfmetrics.registerFontFamily('VN', normal='VN', bold='VN-Bold', italic='VN-Italic')

ACCENT = colors.HexColor('#0B5394')
LIGHT = colors.HexColor('#EAF1F8')
GREY = colors.HexColor('#6B7280')
CODE_BG = colors.HexColor('#F4F5F7')
WARN_BG = colors.HexColor('#FFF6E5')

ss = getSampleStyleSheet()
S = {
    'title': ParagraphStyle('title', parent=ss['Title'], fontName='VN-Bold', fontSize=17,
                            leading=22, textColor=ACCENT, alignment=TA_LEFT, spaceAfter=2),
    'sub': ParagraphStyle('sub', fontName='VN', fontSize=9, leading=13, textColor=GREY, spaceAfter=10),
    'h1': ParagraphStyle('h1', fontName='VN-Bold', fontSize=12.5, leading=16, textColor=ACCENT,
                         spaceBefore=12, spaceAfter=5),
    'h2': ParagraphStyle('h2', fontName='VN-Bold', fontSize=10.5, leading=14, spaceBefore=8, spaceAfter=3),
    'p': ParagraphStyle('p', fontName='VN', fontSize=9.5, leading=13.5, spaceAfter=4),
    'li': ParagraphStyle('li', fontName='VN', fontSize=9.5, leading=13.5, leftIndent=11,
                         bulletIndent=2, spaceAfter=2),
    'cell': ParagraphStyle('cell', fontName='VN', fontSize=8.5, leading=11.5),
    'cellb': ParagraphStyle('cellb', fontName='VN-Bold', fontSize=8.5, leading=11.5, textColor=colors.white),
    'code': ParagraphStyle('code', fontName='VNMono', fontSize=8, leading=11,
                           backColor=CODE_BG, borderPadding=6, spaceBefore=3, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='VN', fontSize=9, leading=12.5, backColor=WARN_BG,
                           borderPadding=6, spaceBefore=2, spaceAfter=8),
}


def P(t, k='p'):
    return Paragraph(t, S[k])


def LI(t):
    return Paragraph(t, S['li'], bulletText='\u2022')


def CODE(t):
    t = (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
          .replace(' ', '&nbsp;').replace('\n', '<br/>'))
    return Paragraph(t, S['code'])


def TBL(header, rows, widths):
    data = [[Paragraph(h, S['cellb']) for h in header]]
    for r in rows:
        data.append([Paragraph(c, S['cell']) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT]),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#C7D2DD')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    return t


story = []

# ---- Bước 1
story.append(P(u'Bước 1 — Lấy danh sách đơn vị hợp lệ', 'h1'))
story.append(P(u'<font face="VNMono">POST /api/vhr-org/get-doc-manager-transfer-org-ids</font>'))
story.append(CODE(u'{ "builtOrgId": 9133734, "orgId": 148842 }'))
story.append(TBL([u'Tham số', u'Ý nghĩa', u'Truyền gì vào'],
                 [[u'<font face="VNMono">builtOrgId</font>', u'ID <b>đơn vị ban hành văn bản</b>',
                   u'<font face="VNMono">document.builtGroupId</font> — <b>không</b> phải đơn vị của user đăng nhập'],
                  [u'<font face="VNMono">orgId</font>', u'<b>Đơn vị user nhấn để tìm kiếm / xem danh sách cán bộ</b>',
                   u'ID đơn vị vừa chọn; <font face="VNMono">null</font> = toàn bộ phạm vi (khi tìm chung, không chọn đơn vị nào)']],
                 [70, 165, 245]))
story.append(Spacer(1, 6))
story.append(P(u'<b>Kết quả trả về:</b> <font face="VNMono">result.data</font> = <font face="VNMono">List&lt;Long&gt;</font> — '
               u'danh sách ID các đơn vị <b>được phép tìm cán bộ</b> bên trong đơn vị vừa chọn.'))
for t in [u'Trả về rỗng &rarr; hiển thị danh sách trống, <b>không cần gọi</b> <font face="VNMono">getListUser</font>.',
          u'Nếu user nhấn vào đơn vị chỉ dùng để mở cây (không thuộc phạm vi): API chỉ trả ID các đơn vị hợp lệ nằm dưới nó, '
          u'nên cán bộ của chính đơn vị đó sẽ không xuất hiện.']:
    story.append(LI(t))

# ---- Bước 2
story.append(P(u'Bước 2 — Cache key–value ở mobile', 'h1'))
story.append(P(u'Lưu <b>key = ID đơn vị user search</b> (<font face="VNMono">orgId</font>), '
               u'<b>value = list ID trả về ở Bước 1</b>:'))
story.append(CODE(u'scopeCache[ builtOrgId + "#" + (orgId ?? 0) ] = List<Long>'))
for t in [u'Lần sau user search lại đúng đơn vị đó &rarr; <b>lấy từ cache, không gọi API/DB nữa</b>, truyền thẳng vào '
          u'<font face="VNMono">getListUser</font>.',
          u'Đổi từ khoá tìm kiếm, chuyển trang, load more &rarr; <b>dùng lại list trong cache</b>, không gọi lại API Bước 1.',
          u'Nên debounce ô tìm kiếm 300–400 ms và huỷ request cũ.',
          u'Xoá cache khi: chuyển sang văn bản khác, kéo refresh, hoặc thoát màn.']:
    story.append(LI(t))

# ---- Bước 3
story.append(P(u'Bước 3 — Gọi staffAction.getListUser như hiện tại, chỉ thêm 3 tham số', 'h1'))
story.append(TBL([u'Tham số', u'Giá trị', u'Ý nghĩa'],
                 [[u'<font face="VNMono">lstGroupId</font>',
                   u'<font face="VNMono">[{"groupId":"&lt;id&gt;"}, …]</font> — list ID lấy ở Bước 1 / cache '
                   u'(<font face="VNMono">groupId</font> là <b>chuỗi</b>)',
                   u'Giới hạn phạm vi tìm kiếm'],
                  [u'<font face="VNMono">onlyParentGroup</font>', u'<font face="VNMono">"1"</font>',
                   u'Lọc <b>đúng</b> các đơn vị trong <font face="VNMono">lstGroupId</font> (không kéo theo đơn vị con)'],
                  [u'<font face="VNMono">user.checkListGroup</font>', u'<font face="VNMono">true</font>',
                   u'<b>Bật</b> việc lọc theo <font face="VNMono">lstGroupId</font>']],
                 [95, 190, 195]))
story.append(Spacer(1, 8))
story.append(P(u'<b>Lưu ý:</b> JSON dưới đây chỉ là <b>ví dụ minh hoạ</b> cho 3 tham số cần thêm — các tham số khác '
               u'(<font face="VNMono">type</font>, <font face="VNMono">searchType</font>, '
               u'<font face="VNMono">documentId</font>, phân trang, tìm nâng cao…) mobile <b>giữ nguyên</b> như đang gửi '
               u'cho màn đó; giá trị trong ví dụ không phải giá trị bắt buộc.', 'note'))
story.append(CODE(u'''{
  "user": {
    "sysOrgId": 148842,
    "checkListGroup": true,        // (bat buoc) bat loc theo lstGroupId
    "isTransferDocOut": true,
    "getByDefault": true,
    "status": 0
  },
  "lstGroupId": [ {"groupId":"148842"}, {"groupId":"9133734"}, {"groupId":"9134001"} ],
  "onlyParentGroup": "1",          // (bat buoc) loc dung cac don vi trong lstGroupId
  "keyword": "nguyen",
  "type": 1,
  "searchType": 1,
  "documentId": "123456",
  "startRecord": 0,
  "pageSize": 20
}'''))
story.append(P(u'Đếm tổng để phân trang: dùng cùng body, thêm <font face="VNMono">"isCount": "1"</font> và bỏ '
               u'<font face="VNMono">startRecord</font> / <font face="VNMono">pageSize</font>.'))
story.append(P(u'Kết quả trả về là danh sách cán bộ như hiện tại — <b>không cần lọc lại ở client</b>, server đã lọc đúng phạm vi.'))



def footer(canv, doc):
    canv.saveState()
    canv.setFont('VN', 7.5)
    canv.setFillColor(GREY)
    canv.drawString(18 * mm, 12 * mm, u'Hướng dẫn Mobile — lọc danh sách cán bộ theo phạm vi (văn thư phát hành chuyển VB đi)')
    canv.drawRightString(A4[0] - 18 * mm, 12 * mm, u'Trang %d' % doc.page)
    canv.setStrokeColor(colors.HexColor('#D8DEE6'))
    canv.line(18 * mm, 15 * mm, A4[0] - 18 * mm, 15 * mm)
    canv.restoreState()


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'yeu-cau',
                   'HuongDan-Mobile-Loc-Can-Bo-Theo-Pham-Vi.pdf')
doc = BaseDocTemplate(out, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                      topMargin=16 * mm, bottomMargin=20 * mm,
                      title=u'Huong dan Mobile - loc can bo theo pham vi',
                      author=u'Van phong so Khanh Hoa')
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
doc.addPageTemplates([PageTemplate(id='main', frames=[frame], onPage=footer)])
doc.build(story)
print('PDF:', out)
