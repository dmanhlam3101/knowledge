# -*- coding: utf-8 -*-
"""Gom mọi dòng có ❓ trong knowledge/ (trừ ban-do.md sinh tự động) -> _chung/cau-hoi-mo.md"""
import os, re

KNOW = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
out = ['# Câu hỏi mở cần người xác nhận', '',
       '> Sinh bởi `_tools/questions.py`. Trả lời xong: sửa file gốc (xóa ❓), chạy lại script. '
       'Đây là danh sách việc cho BA / người biết nghiệp vụ.', '']
total = 0
for root, _, files in os.walk(KNOW):
    for f in sorted(files):
        if not f.endswith('.md') or f in ('ban-do.md', 'cau-hoi-mo.md', 'README.md') or '_tools' in root or 'ban-do-tong' in root or 'mau-dau-ra' in root:
            continue
        p = os.path.join(root, f)
        rel = os.path.relpath(p, KNOW).replace('\\', '/')
        hits = []
        in_q = False
        for i, line in enumerate(open(p, encoding='utf-8'), 1):
            st = line.strip()
            if st.startswith('#'):
                in_q = '❓' in st
                continue
            if (in_q and re.match(r'\d+\.', st)) or ('❓' in st):
                hits.append((i, re.sub(r'\s+', ' ', st)))
        if hits:
            out.append('## %s (%d)' % (rel, len(hits)))
            out.append('')
            for i, t in hits:
                out.append('- [ ] L%d: %s' % (i, t))
            out.append('')
            total += len(hits)
out.insert(3, 'Tổng: **%d** câu.' % total)
with open(os.path.join(KNOW, '_chung', 'cau-hoi-mo.md'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
print('cau-hoi-mo.md:', total)
