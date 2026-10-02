# -*- coding: utf-8 -*-
"""
Sinh ban-do.md cho từng phân hệ + các bảng tổng trong _chung/ban-do-tong/ từ out/graph.json.
Chạy:  python knowledge/_tools/scan.py && python knowledge/_tools/gen.py
"""
import os, json, collections
from domains import DOMAINS, domain_of

HERE = os.path.dirname(os.path.abspath(__file__))
KNOW = os.path.abspath(os.path.join(HERE, '..'))
g = json.load(open(os.path.join(HERE, 'out', 'graph.json'), encoding='utf-8'))
W, B, LINK = g['web'], g['be'], g['link']['function_to_endpoint']

HEADER = ("> **SINH TỰ ĐỘNG** bởi `knowledge/_tools/gen.py` từ code thật — đừng sửa tay. "
          "Xếp sai phân hệ → sửa `knowledge/_tools/domains.py` rồi chạy lại.\n"
          "> Nhãn màn hình: **BE** = VM gọi BE qua `*Business` (cơ chế MỚI) · **LEGACY** = VM gọi facade/DAO trực tiếp trong web (cơ chế CŨ) · "
          "**BE+LEGACY** = cả hai · **—** = không gọi dữ liệu.\n"
          "> Thế hệ BE: **gen-1** = `com.viettel.voffice` (Action → controler → DAO SQL thuần) · **gen-2** = `com.viettel.office` (Controller → Service → JPA Repository).\n")


def short_zul(z):
    for p in ('view/voffice/', 'view/'):
        if z.startswith(p):
            return z[len(p):]
    return z


def short_vm(fq):
    return fq.replace('com.viettel.voffice.', '').replace('com.viettel.', '')


def label(v):
    if v.get('missing'):
        return '☠ VM không tồn tại'
    b, r = bool(v['business']), bool(v['remote'])
    return 'BE+LEGACY' if b and r else 'BE' if b else 'LEGACY' if r else '—'


# ------------------------------------------------------------------ gán phân hệ
dom = collections.defaultdict(lambda: collections.defaultdict(list))  # domain -> kind -> [names]
unassigned = collections.defaultdict(list)


def assign(kind, name, *keys):
    d = domain_of(*keys)
    if d:
        dom[d][kind].append(name)
    else:
        unassigned[kind].append(name)
    return d


for z, vmfq in W['zul_vm'].items():
    assign('zul', z, z)
for fq, v in W['vm'].items():
    if not v['zul']:
        assign('vm_only', fq, v['path'] or fq)
for n, v in W['business'].items():
    assign('business', n, n, v['path'])
for n, v in W['facade'].items():
    assign('facade', n, n)
for n, v in B['controller'].items():
    assign('controller', n, v['base'], n, v['path'])
for n, v in B['logic'].items():
    assign('logic', n, n, v['path'])
for n, v in B['dao'].items():
    assign('dao', n, n, v['path'])
for n, v in B['service'].items():
    assign('be_service', n, n, v['path'])
for n, v in B['entity'].items():
    assign('be_entity', n, n, v['path'])
for n, v in W['entity'].items():
    assign('web_entity', n, n, v['path'])

# ------------------------------------------------------------------ duyệt phụ thuộc BE


def resolve_service(name):
    out = []
    for cand in (name, name + 'Impl'):
        if cand in B['service']:
            out.append(cand)
    return out


def trace_controller(cname):
    """Trả về (logics, services, daos, repos, tables)"""
    logics, services, daos, repos, tables = [], [], [], [], set()
    seen = set()

    def visit(dep, depth):
        if dep in seen or depth > 4:
            return
        seen.add(dep)
        if dep in B['logic']:
            logics.append(dep)
            tables.update(B['logic'][dep]['tables'])
            for d in B['logic'][dep]['deps']:
                visit(d, depth + 1)
        elif dep in B['dao']:
            daos.append(dep)
            tables.update(B['dao'][dep]['tables'])
        elif dep in B['repository']:
            repos.append(dep)
            ent = B['repository'][dep]['entity']
            if ent in B['entity']:
                tables.add(B['entity'][ent]['table'])
        else:
            for s in resolve_service(dep):
                if s not in services:
                    services.append(s)
                tables.update(B['service'][s].get('tables', []))
                for d in B['service'][s]['deps']:
                    visit(d, depth + 1)

    for d in B['controller'][cname]['deps']:
        visit(d, 0)
    return logics, services, daos, repos, sorted(tables)


def trace_facade(fname):
    f = W['facade'][fname]
    services, daos, ents = [], [], []
    for s in f['services']:
        if s in W['service']:
            services.append(s)
            for d in W['service'][s]['daos'] + W['service'][s]['dao_new']:
                if d in W['dao'] and d not in daos:
                    daos.append(d)
                    e = W['dao'][d]['entity']
                    if e and e in W['entity']:
                        ents.append('%s (%s)' % (e, W['entity'][e]['table']))
    return services, daos, sorted(set(ents))


def code(x):
    return '`%s`' % x if x else ''


def lst(xs, sep=', '):
    return sep.join(code(x) for x in xs) if xs else '—'


# ------------------------------------------------------------------ sinh ban-do.md cho từng phân hệ
os.makedirs(os.path.join(KNOW, '_chung', 'ban-do-tong'), exist_ok=True)
stats = {}
for d, title in DOMAINS.items():
    k = dom.get(d, {})
    out = ['# Bản đồ hệ thống — %s' % title, '', HEADER, '']
    zuls = sorted(k.get('zul', []))
    vm_only = sorted(k.get('vm_only', []))
    # 1. màn hình
    out += ['## 1. Màn hình (web)', '', 'Tổng: %d màn hình, %d VM không gắn zul trực tiếp.' % (len(zuls), len(vm_only)), '',
            '| Màn hình (.zul) | ViewModel | Gọi BE qua (Business) | Legacy (remote/facade) | Nhãn |', '|---|---|---|---|---|']
    all_tables = set()
    for z in zuls:
        fq = W['zul_vm'][z]
        v = W['vm'].get(fq, {'business': [], 'remote': [], 'path': None})
        out.append('| %s | %s | %s | %s | %s |' % (code(short_zul(z)), code(short_vm(fq)), lst(v['business']), lst(v['remote']), label(v)))
    if vm_only:
        out += ['', '<details><summary>VM không gắn zul trực tiếp (popup / include / dùng chung)</summary>', '',
                '| ViewModel | Gọi BE qua | Legacy | Nhãn |', '|---|---|---|---|']
        for fq in vm_only:
            v = W['vm'][fq]
            out.append('| %s | %s | %s | %s |' % (code(short_vm(fq)), lst(v['business']), lst(v['remote']), label(v)))
        out += ['', '</details>']
    # 2. web -> BE
    buss = sorted(k.get('business', []))
    out += ['', '## 2. Web → BE (Business → endpoint)', '',
            'Cách gọi: `new XxxBusiness(serviceConnection).serveProcessing("a.b", params)` → `POST {BE}/a/b`. '
            'Nguồn: `web-spring/src/main/java/com/voffice/service/business/`.', '']
    for b in buss:
        info = W['business'][b]
        out += ['### %s' % b, '', '`%s`' % info['path'], '', '| Hàm (function key) | Endpoint BE | Controller.method | Gen |', '|---|---|---|---|']
        for f in info['functions']:
            l = LINK.get(f)
            if l:
                c, m = l
                out.append('| `%s` | `/%s` | `%s.%s` | %s |' % (f, f.replace('.', '/'), c, m, B['controller'][c]['gen']))
            else:
                out.append('| `%s` | ❓ không tìm thấy endpoint | | |' % f)
        out.append('')
    if not buss:
        out += ['_Không có Business riêng — màn hình phân hệ này dùng Business của phân hệ khác (xem cột "Gọi BE qua" ở mục 1)._', '']
    # 3. BE
    ctrls = sorted(k.get('controller', []), key=lambda c: (B['controller'][c]['gen'], c))
    out += ['## 3. BE — Controller → logic / service → DAO / repository → bảng', '']
    for c in ctrls:
        info = B['controller'][c]
        logics, services, daos, repos, tables = trace_controller(c)
        all_tables.update(tables)
        out += ['### %s (%s) — base `%s`, %d endpoint' % (c, info['gen'], info['base'] or '/', len(info['endpoints'])), '',
                '`%s`' % info['path'], '']
        if logics:
            out.append('- Logic (gen-1 `controler/`): %s' % lst(logics))
        if services:
            out.append('- Service: %s' % lst(services))
        if daos:
            out.append('- DAO (SQL thuần): %s' % lst(daos))
        if repos:
            out.append('- Repository (JPA): %s' % lst(repos))
        out.append('- Bảng (ước lượng từ SQL/@Table): %s' % lst(tables))
        out += ['', '<details><summary>Endpoint</summary>', '', '| Verb | Path | Method |', '|---|---|---|']
        for e in info['endpoints']:
            out.append('| %s | `%s` | `%s` |' % (e['verb'], e['path'], e['method']))
        out += ['', '</details>', '']
    if not ctrls:
        out += ['_Không có controller BE riêng cho phân hệ này._', '']
    # 4. legacy web
    facs = sorted(k.get('facade', []))
    out += ['## 4. Web legacy — facade → service → JPA DAO → entity (query thẳng DB từ web, KHÔNG dùng cho tính năng mới)', '']
    if facs:
        out += ['| Facade | implements | Service | DAO | Entity (bảng) |', '|---|---|---|---|---|']
        for f in facs:
            services, daos, ents = trace_facade(f)
            for e in ents:
                all_tables.add(e.split('(')[-1].rstrip(')'))
            out.append('| %s | %s | %s | %s | %s |' % (code(f), lst(W['facade'][f]['implements']), lst(services), lst(daos), lst(ents)))
    else:
        out.append('_Không có facade legacy riêng._')
    # 5. entity
    ents_be = sorted(k.get('be_entity', []))
    ents_web = sorted(k.get('web_entity', []))
    out += ['', '## 5. Entity / bảng DB thuộc phân hệ', '']
    if ents_be:
        out += ['**BE gen-2 (`com.viettel.office.entities`)**: ' + ', '.join('`%s`→`%s`' % (e, B['entity'][e]['table']) for e in ents_be), '']
        all_tables.update(B['entity'][e]['table'] for e in ents_be)
    if ents_web:
        out += ['**Web (`com.viettel.voffice.entity`, dùng bởi legacy)**: ' + ', '.join('`%s`→`%s`' % (e, W['entity'][e]['table']) for e in ents_web), '']
        all_tables.update(W['entity'][e]['table'] for e in ents_web)
    out += ['**Tổng hợp bảng chạm tới**: ' + lst(sorted(all_tables)), '']
    # write
    ddir = os.path.join(KNOW, d)
    os.makedirs(ddir, exist_ok=True)
    with open(os.path.join(ddir, 'ban-do.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out))
    stats[d] = dict(man_hinh=len(zuls), vm_khac=len(vm_only), business=len(buss), controller=len(ctrls), facade=len(facs), bang=len(all_tables))

# ------------------------------------------------------------------ bảng tổng
T = os.path.join(KNOW, '_chung', 'ban-do-tong')

with open(os.path.join(T, 'thong-ke.md'), 'w', encoding='utf-8') as fh:
    fh.write('# Thống kê theo phân hệ\n\n' + HEADER + '\n| Phân hệ | Màn hình | VM khác | Business | Controller BE | Facade legacy | Bảng DB |\n|---|---|---|---|---|---|---|\n')
    for d, s in stats.items():
        fh.write('| [%s](../../%s/ban-do.md) | %d | %d | %d | %d | %d | %d |\n' % (d, d, s['man_hinh'], s['vm_khac'], s['business'], s['controller'], s['facade'], s['bang']))
    nf = len(LINK)
    fh.write('\nTổng: %d màn hình có VM, %d VM, %d Business với %d hàm gọi BE (%d nối được endpoint), %d controller BE / %d endpoint, %d facade legacy.\n' % (
        len(W['zul_vm']), len(W['vm']), len(W['business']), nf, sum(1 for v in LINK.values() if v),
        len(B['controller']), sum(len(c['endpoints']) for c in B['controller'].values()), len(W['facade'])))

with open(os.path.join(T, 'web-goi-be.md'), 'w', encoding='utf-8') as fh:
    fh.write('# Toàn bộ lệnh gọi web → BE\n\n' + HEADER + '\n| Business | Hàm | Endpoint | Controller.method | Gen |\n|---|---|---|---|---|\n')
    for b in sorted(W['business']):
        for f in W['business'][b]['functions']:
            l = LINK.get(f)
            fh.write('| `%s` | `%s` | `/%s` | %s | %s |\n' % (b, f, f.replace('.', '/'), ('`%s.%s`' % tuple(l)) if l else '❓', B['controller'][l[0]]['gen'] if l else ''))

with open(os.path.join(T, 'endpoints-be.md'), 'w', encoding='utf-8') as fh:
    fh.write('# Toàn bộ endpoint BE\n\n' + HEADER + '\n')
    for gen in ('gen1', 'gen2'):
        fh.write('\n## %s\n\n| Controller | Base | Verb | Path | Method | Phân hệ |\n|---|---|---|---|---|---|\n' % gen)
        for c in sorted(B['controller']):
            info = B['controller'][c]
            if info['gen'] != gen:
                continue
            d = domain_of(info['base'], c, info['path']) or '❓'
            for e in info['endpoints']:
                fh.write('| `%s` | `%s` | %s | `%s` | `%s` | %s |\n' % (c, info['base'] or '/', e['verb'], e['path'], e['method'], d))

with open(os.path.join(T, 'bang-db.md'), 'w', encoding='utf-8') as fh:
    fh.write('# Entity ↔ bảng DB\n\n' + HEADER + '\n## BE gen-2 (`com.viettel.office.entities`)\n\n| Entity | Bảng | Phân hệ | Repository |\n|---|---|---|---|\n')
    repo_by_ent = collections.defaultdict(list)
    for r, v in B['repository'].items():
        repo_by_ent[v['entity']].append(r)
    for e in sorted(B['entity']):
        v = B['entity'][e]
        fh.write('| `%s` | `%s` | %s | %s |\n' % (e, v['table'], domain_of(e, v['path']) or '❓', lst(sorted(repo_by_ent.get(e, [])))))
    fh.write('\n## Web (`com.viettel.voffice.entity`, `com.viettel.vps.entity` — dùng bởi legacy)\n\n| Entity | Bảng | Phân hệ |\n|---|---|---|\n')
    for e in sorted(W['entity']):
        v = W['entity'][e]
        fh.write('| `%s` | `%s` | %s |\n' % (e, v['table'], domain_of(e, v['path']) or '❓'))
    fh.write('\n## Bảng chạm tới bởi BE gen-1 DAO (ước lượng từ SQL)\n\n| DAO | Bảng |\n|---|---|\n')
    for dname in sorted(B['dao']):
        fh.write('| `%s` | %s |\n' % (dname, lst(B['dao'][dname]['tables'])))

with open(os.path.join(T, 'chua-xep.md'), 'w', encoding='utf-8') as fh:
    fh.write('# Thành phần chưa xếp được phân hệ\n\nThêm quy tắc vào `knowledge/_tools/domains.py` rồi chạy lại `gen.py`.\n')
    for kind, names in unassigned.items():
        fh.write('\n## %s (%d)\n\n' % (kind, len(names)))
        for n in sorted(names):
            fh.write('- `%s`\n' % n)

print('Đã sinh ban-do.md cho %d phân hệ; chưa xếp: %s' % (len(DOMAINS), {k: len(v) for k, v in unassigned.items()}))
for d, s in stats.items():
    print('  %-24s màn hình=%3d vm_khác=%3d business=%2d controller=%2d facade=%2d bảng=%3d' % (d, s['man_hinh'], s['vm_khac'], s['business'], s['controller'], s['facade'], s['bang']))
