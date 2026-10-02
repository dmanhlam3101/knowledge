# -*- coding: utf-8 -*-
"""Gom mục 7.1 (câu hỏi còn mở) của mọi phân hệ vào một file để chủ dự án trả lời một lượt.
Ghi đè knowledge/_chung/cau-hoi-dot-2026-10.md (phần câu hỏi theo phân hệ được sinh lại;
phần đầu 'Quyết định chung' lấy từ _tools/cau-hoi-dot-dau.md — sửa phần A ở đó)."""
import io, os, re

KNOW = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = [
    ('xu-ly-cong-viec', 'Xử lý công việc (dự thảo → ký)'),
    ('van-ban/di', 'Văn bản đi'),
    ('van-ban/chuyen-van-ban', 'Chuyển văn bản'),
    ('van-ban/den', 'Văn bản đến'),
    ('phieu-trinh', 'Phiếu trình'),
    ('lich-nhac-viec', 'Nhắc việc / thông báo / SMS / nắm tình hình / định hướng'),
    ('van-ban/luong-xu-ly', 'Luồng xử lý (cấu hình luồng ký)'),
    ('van-ban/so-van-ban', 'Sổ văn bản'),
    ('van-ban/lien-thong', 'Liên thông văn bản'),
    ('van-ban/quan-ly-chung', 'Quản lý chung văn bản'),
    ('nhiem-vu', 'Nhiệm vụ'),
    ('cong-viec', 'Công việc cá nhân'),
    ('ho-so-cong-viec', 'Hồ sơ công việc / lưu trữ'),
    ('hop', 'Họp / lịch'),
    ('ky-so', 'Ký số'),
    ('he-thong', 'Hệ thống / quản trị'),
    ('kpi-danh-gia', 'KPI / đánh giá / báo cáo'),
    ('tich-hop', 'Tích hợp'),
    ('tai-lieu-mau', 'Tài liệu mẫu / thư viện'),
]

out = []
total = 0
summary = []
for dom, name in ORDER:
    p = os.path.join(KNOW, dom, 'nghiep-vu.md')
    s = io.open(p, encoding='utf-8').read()
    i = s.find('### 7.1')
    j = s.find('### 7.2', i)
    block = s[i:j] if i >= 0 else ''
    lines = block.splitlines()[1:]
    qrows = [l for l in lines if re.match(r'^\| Q\d+ \|', l) or re.match(r'^- \*\*Q\d+', l)]
    if not qrows:
        summary.append((dom, name, 0))
        continue
    total += len(qrows)
    summary.append((dom, name, len(qrows)))
    rel = os.path.relpath(p, os.path.join(KNOW, '_chung')).replace('\\', '/')
    out.append('## %s — `%s` (%d câu)' % (name, dom, len(qrows)))
    out.append('')
    out.append('Nguồn: [%s](%s) mục 7.1 — mỗi câu có mã NV/BR để tra ngữ cảnh.' % (dom + '/nghiep-vu.md', rel))
    out.append('')
    for l in qrows:
        if l.startswith('|'):
            cells = [c.strip() for c in l.strip().strip('|').split(' | ')]
            qid, ctx, q = cells[0], cells[1], ' — '.join(cells[2:])
        else:
            m = re.match(r'^- \*\*(Q\d+)\.?\*\*\.?\s*(.*)$', l)
            qid, ctx, q = m.group(1), '', m.group(2)
        out.append('### %s · %s' % (dom, qid))
        out.append('')
        if ctx:
            out.append('**Hiện trạng:** ' + ctx)
            out.append('')
        out.append('**Câu hỏi:** ' + q)
        out.append('')
        out.append('> **Trả lời:** ')
        out.append('')
    out.append('')

head = io.open(os.path.join(HERE, 'cau-hoi-dot-dau.md'), encoding='utf-8').read()
tbl = ['| Phân hệ | Thư mục | Số câu |', '|---|---|---|']
for dom, name, n in summary:
    tbl.append('| %s | `%s` | %s |' % (name, dom, n if n else '— (đã trả lời hết)'))
tbl.append('| **Tổng** | | **%d** |' % total)
doc = head.replace('{{BANG_TONG}}', '\n'.join(tbl)).replace('{{TONG}}', str(total)) + '\n' + '\n'.join(out)
dst = os.path.join(KNOW, '_chung', 'cau-hoi-dot-2026-10.md')
io.open(dst, 'w', encoding='utf-8', newline='').write(doc)
print(dst, total)
