# -*- coding: utf-8 -*-
"""Gom câu hỏi còn mở của mọi phân hệ -> _chung/cau-hoi-mo.md (máy sinh, không sửa tay).

Khung bài chuẩn (xem _chung/huong-dan-ra-soat-nghiep-vu.md): câu hỏi còn mở nằm ở mục "### 7.1" của
`nghiep-vu.md`, mỗi câu một dòng bảng `| Qn | bối cảnh | câu hỏi |` (hoặc dòng danh sách `- **Qn.** ...`
ở bài cũ). Mục 7.2 (đã xác nhận) không được gom. Trả lời xong: chuyển câu sang 7.2 trong file gốc, chạy lại.
"""
import os, re

KNOW = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ROW = re.compile(r'^\| (Q\d+) \| (.*?) \| (.*) \|\s*$')
ITEM = re.compile(r'^- \*\*(Q\d+)\.?\*\*\.?\s*(.*)$')


def short(t, n=220):
    t = re.sub(r'\s+', ' ', t).strip()
    return t if len(t) <= n else t[:n].rstrip() + '…'


out = ['# Câu hỏi mở cần người xác nhận', '',
       '> Sinh bởi `_tools/questions.py` từ mục **7.1** của từng `nghiep-vu.md`. Không sửa tay. '
       'Trả lời xong: chuyển câu sang mục 7.2 của file gốc (kèm hệ quả ghi vào tri thức) rồi chạy lại script.', '']
total = 0
sections = []
for root, dirs, files in os.walk(KNOW):
    dirs[:] = sorted(d for d in dirs if not d.startswith(('.', '_')))
    if 'nghiep-vu.md' not in files:
        continue
    p = os.path.join(root, 'nghiep-vu.md')
    rel = os.path.relpath(p, KNOW).replace('\\', '/')
    text = open(p, encoding='utf-8').read()
    i = text.find('### 7.1')
    if i < 0:
        continue
    j = text.find('### 7.2', i)
    block = text[i:j if j > 0 else len(text)].splitlines()[1:]
    hits = []
    for line in block:
        m = ROW.match(line)
        if m and m.group(1) != '#':
            hits.append((m.group(1), short(m.group(3))))
            continue
        m = ITEM.match(line)
        if m:
            hits.append((m.group(1), short(m.group(2))))
    if hits:
        total += len(hits)
        sec = ['## %s (%d)' % (rel, len(hits)), '']
        sec += ['- [ ] **%s** — %s' % (q, t) for q, t in hits]
        sec.append('')
        sections.append(sec)
out.append('Tổng: **%d** câu.' % total)
out.append('')
for sec in sections:
    out += sec
with open(os.path.join(KNOW, '_chung', 'cau-hoi-mo.md'), 'w', encoding='utf-8', newline='') as fh:
    fh.write('\n'.join(out))
print('cau-hoi-mo.md:', total)
