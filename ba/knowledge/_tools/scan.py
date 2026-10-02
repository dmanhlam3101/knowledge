# -*- coding: utf-8 -*-
"""
Quét code web-spring + backend2.0 -> knowledge/_tools/out/graph.json
Chạy:  python knowledge/_tools/scan.py   (từ root workspace)
Không cần thư viện ngoài. Python 3.8+.
"""
import os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WEB_JAVA = os.path.join(ROOT, 'web-spring', 'src', 'main', 'java')
WEB_ZUL = os.path.join(ROOT, 'web-spring', 'src', 'main', 'webapp')
BE_JAVA = os.path.join(ROOT, 'backend2.0', 'backendvoffice', 'src', 'main', 'java')
OUT = os.path.join(os.path.dirname(__file__), 'out')
os.makedirs(OUT, exist_ok=True)


def walk(base, ext):
    for d, _, fs in os.walk(base):
        for f in fs:
            if f.endswith(ext):
                yield os.path.join(d, f)


def read(p):
    for enc in ('utf-8', 'latin-1'):
        try:
            with open(p, encoding=enc) as fh:
                return fh.read()
        except UnicodeDecodeError:
            continue
    return ''


def rel(p, base):
    return os.path.relpath(p, base).replace('\\', '/')


def strip_comments(src):
    src = re.sub(r'/\*.*?\*/', '', src, flags=re.S)
    return re.sub(r'//[^\n]*', '', src)


# ---------------------------------------------------------------- WEB
zul_vm = {}
zul_inc = {}
RE_VM = re.compile(r"viewModel\s*=\s*\"[^\"]*@init\(\s*'([\w.]+)'")
RE_INC = re.compile(r"<include[^>]*src\s*=\s*\"([^\"]+)\"")
for p in walk(WEB_ZUL, '.zul'):
    s = read(p)
    r = rel(p, WEB_ZUL)
    m = RE_VM.findall(s)
    if m:
        zul_vm[r] = m[0]
    inc = [i for i in RE_INC.findall(s) if not i.startswith('@')]
    if inc:
        zul_inc[r] = inc

web_classes = {}
for p in walk(WEB_JAVA, '.java'):
    r = rel(p, WEB_JAVA)
    fq = r[:-5].replace('/', '.')
    web_classes[fq.split('.')[-1]] = {'fqcn': fq, 'path': 'web-spring/src/main/java/' + r}

RE_BUS_NEW = re.compile(r'new\s+(\w+Business)\s*\(')
RE_DELEG = re.compile(r'Delegate\.getService\(\s*(\w+)\.class')
RE_FUNC = re.compile(r'(?:serveProcessing|servePostRequest|serveGetRequest|downloadFile|downloadFileContent|sendPostRequest)\s*\((?:[^;]*?,\s*)?"([\w.\-]+)')
RE_FUNC2 = re.compile(r'"([a-zA-Z][\w\-]*\.[a-zA-Z][\w.\-]*)"')
RE_AUTOW = re.compile(r'@Autowired[^;]*?\b(?:private|protected|public)?\s*([\w<>]+)\s+(\w+)\s*;', re.S)
RE_IMPL = re.compile(r'class\s+(\w+)\s+(?:extends\s+[\w<>]+\s+)?implements\s+([\w,\s]+)\{')
RE_EXT = re.compile(r'class\s+(\w+)\s+extends\s+([\w]+)(?:<([\w]+)>)?')
RE_TABLE = re.compile(r'@Table\s*\(\s*name\s*=\s*"(\w+)"')
RE_ENTITY = re.compile(r'@Entity')

vm = {}
business = {}
facade = {}
web_service = {}
web_dao = {}
web_entity = {}
BUSINESS_NAMES = {n for n, i in web_classes.items() if n.endswith('Business') and 'com/voffice/service/business' in i['path'] and n != 'Business'}
REMOTE_NAMES = {n for n, i in web_classes.items() if '/remote/' in i['path']}
RE_TOKEN = re.compile(r'\b([A-Z]\w+)\b')
RE_EXTENDS = re.compile(r'class\s+\w+\s+extends\s+(\w+)')

for simple, info in web_classes.items():
    p = os.path.join(ROOT, info['path'])
    s = strip_comments(read(p))
    fq = info['fqcn']
    if '.vm.' in fq or simple.endswith('VM'):
        body = chr(10).join(l for l in s.splitlines() if not l.strip().startswith('import '))
        toks = set(RE_TOKEN.findall(body))
        m = RE_EXTENDS.search(s)
        vm[fq] = {'path': info['path'],
                  'business': sorted((toks & BUSINESS_NAMES) | set(RE_BUS_NEW.findall(s))),
                  'remote': sorted((toks & REMOTE_NAMES) | set(RE_DELEG.findall(s))),
                  'extends': m.group(1) if m else None,
                  'zul': []}
    if simple.endswith('Business') and 'com/voffice/service/business' in info['path']:
        funcs = set(RE_FUNC.findall(s))
        funcs |= {f for f in RE_FUNC2.findall(s) if not f.startswith(('com.', 'java.', 'org.', 'voffice.', 'app.', 'common.', 'yyyy', 'dd.', 'HH.'))
                  and not f.endswith(('.zul', '.pdf', '.xlsx', '.xls', '.docx', '.doc', '.jpg', '.png', '.class', '.txt', '.json', '.xml'))}
        funcs = {f.rstrip('.').split('/')[0].rstrip('.') for f in funcs}
        business[simple] = {'path': info['path'], 'functions': sorted(funcs)}
    if 'voffice/facade/' in info['path'] or 'common/facade/' in info['path']:
        m = RE_IMPL.search(s)
        facade[simple] = {'path': info['path'],
                          'implements': [i.strip() for i in m.group(2).split(',')] if m else [],
                          'services': sorted({t for t, n in RE_AUTOW.findall(s)})}
    if simple.endswith('Service') and '/service/' in info['path'] and 'com/voffice' not in info['path']:
        web_service[simple] = {'path': info['path'],
                               'daos': sorted({t for t, n in RE_AUTOW.findall(s) if 'Dao' in t}),
                               'dao_new': sorted(set(re.findall(r'new\s+(\w+Dao)\s*\(', s)))}
    if simple.endswith('Dao') and '/dao/' in info['path']:
        m = RE_EXT.search(s)
        web_dao[simple] = {'path': info['path'], 'entity': m.group(3) if m and m.group(3) else None}
    if RE_ENTITY.search(s):
        m = RE_TABLE.search(s)
        web_entity[simple] = {'path': info['path'], 'table': m.group(1) if m else simple.upper()}

for z, v in zul_vm.items():
    if v in vm:
        vm[v]['zul'].append(z)
    else:
        vm[v] = {'path': None, 'business': [], 'remote': [], 'extends': None, 'zul': [z], 'missing': True}

# ---------------------------------------------------------------- BE
be_classes = {}
for p in walk(BE_JAVA, '.java'):
    r = rel(p, BE_JAVA)
    fq = r[:-5].replace('/', '.')
    be_classes[fq.split('.')[-1]] = {'fqcn': fq, 'path': 'backend2.0/backendvoffice/src/main/java/' + r}

RE_CLASS_MAP = re.compile(r'@RequestMapping\s*\(\s*(?:value\s*=\s*)?((?:[\w.]+\s*\+\s*)?"[^"]+")')
RE_METH = re.compile(
    r'@(Post|Get|Put|Delete|Request)Mapping\s*(?:\(\s*(?:value\s*=\s*|path\s*=\s*)?(?:"([^"]*)"|\{\s*"([^"]*)")?[^)]*\))?'
    r'\s*(?:@\w+(?:\([^)]*\))?\s*)*(?:public|protected)?\s+[\w<>\[\], ?]+\s+(\w+)\s*\(', re.S)
RE_REPO = re.compile(r'interface\s+(\w+)\s+extends\s+[^{]*?(?:JpaRepository|CrudRepository|PagingAndSortingRepository|JpaSpecificationExecutor)\s*<\s*(\w+)')
RE_FIELD_TYPES = re.compile(r'(?:@Autowired|@Inject|@Resource)[^;]*?\b(?:private|protected|public)?\s*(?:final\s+)?([\w<>]+)\s+(\w+)\s*;', re.S)
RE_CTOR_FIELDS = re.compile(r'(?:private|protected|public)?\s*final\s+([\w<>]+)\s+(\w+)\s*;')
RE_SQL_TABLE = re.compile(r'\b(?:FROM|JOIN|INTO|UPDATE)\s+([A-Za-z][A-Za-z0-9_]*[A-Z_][A-Za-z0-9_]*)\b', re.I)
SQL_STOP = {'SELECT', 'WHERE', 'DUAL', 'AND', 'OR', 'NOT', 'SET', 'VALUES', 'TABLE', 'THE', 'A', 'AN', 'ON', 'IN', 'AS'}
PREFIX = {'Constants.REQUEST_MAPPING_PREFIX': '/api', 'Constants.PUBLIC_REQUEST_MAPPING_PREFIX': '/public/api',
          'REQUEST_MAPPING_PREFIX': '/api', 'PUBLIC_REQUEST_MAPPING_PREFIX': '/public/api'}


def resolve_base(expr):
    m = re.match(r'(?:([\w.]+)\s*\+\s*)?"([^"]+)"', expr.strip())
    if not m:
        return ''
    return PREFIX.get(m.group(1) or '', '') + m.group(2)


def sql_tables(s):
    out = {}
    for t in RE_SQL_TABLE.findall(s):
        u = t.upper()
        if u in SQL_STOP or len(u) < 4 or u.startswith(('CLASS', 'OBJECT')):
            continue
        out[u] = out.get(u, 0) + 1
    return sorted(k for k, v in out.items() if v >= 1)


def deps_of(s):
    return sorted({t for t, n in RE_FIELD_TYPES.findall(s)} | {t for t, n in RE_CTOR_FIELDS.findall(s)})


controllers, be_logic, be_services, be_daos, be_repos, be_entities = {}, {}, {}, {}, {}, {}
for simple, info in be_classes.items():
    p = os.path.join(ROOT, info['path'])
    s = strip_comments(read(p))
    gen = 'gen2' if '/com/viettel/office/' in info['path'] else 'gen1'
    if re.search(r'^\s*@(RestController|Controller)\b', s, re.M):
        m = RE_CLASS_MAP.search(s)
        base = resolve_base(m.group(1)) if m else ''
        eps = []
        for verb, v1, v2, name in RE_METH.findall(s):
            path = v1 or v2 or ''
            full = (base.rstrip('/') + '/' + path.strip('/')).rstrip('/') or '/'
            eps.append({'verb': verb.upper(), 'path': full, 'method': name})
        controllers[simple] = {'path': info['path'], 'gen': gen, 'base': base, 'endpoints': eps, 'deps': deps_of(s)}
    elif '/voffice/controler/' in info['path']:
        be_logic[simple] = {'path': info['path'], 'gen': 'gen1', 'deps': deps_of(s), 'tables': sql_tables(s)}
    elif '/database/dao/' in info['path']:
        be_daos[simple] = {'path': info['path'], 'gen': 'gen1', 'tables': sql_tables(s)}
    elif '/office/services/' in info['path'] or simple.endswith('ServiceImpl') or (simple.endswith('Service') and '@Service' in s):
        native = len(re.findall(r'createNativeQuery|nativeQuery\s*=\s*true', s))
        be_services[simple] = {'path': info['path'], 'gen': gen, 'deps': deps_of(s), 'native_queries': native,
                               'tables': sql_tables(s) if native else []}
    m = RE_REPO.search(s)
    if m:
        be_repos[m.group(1)] = {'path': info['path'], 'entity': m.group(2)}
    if RE_ENTITY.search(s):
        t = RE_TABLE.search(s)
        be_entities[simple] = {'path': info['path'], 'table': t.group(1) if t else simple.upper()}

# ---------------------------------------------------------------- link web function -> BE endpoint
ep_index = {}
ep_wild = []
for c, info in controllers.items():
    for e in info['endpoints']:
        key = e['path'].strip('/').lower()
        ep_index[key] = (c, e['method'])
        if '{' in key:
            ep_wild.append((re.compile('^' + re.sub(r'\{[^}]*\}', '[^/]+', key) + '$'), (c, e['method'])))
            ep_wild.append((re.compile('^' + re.sub(r'/\{[^}]*\}', '', key) + '$'), (c, e['method'])))
func_link = {}
for b, info in business.items():
    for f in info['functions']:
        key = f.replace('.', '/').lower()
        hit = ep_index.get(key)
        if not hit:
            for rx, v in ep_wild:
                if rx.match(key):
                    hit = v
                    break
        func_link[f] = hit

graph = {
    'web': {'zul_vm': zul_vm, 'zul_include': zul_inc, 'vm': vm, 'business': business, 'facade': facade,
            'service': web_service, 'dao': web_dao, 'entity': web_entity},
    'be': {'controller': controllers, 'logic': be_logic, 'service': be_services, 'dao': be_daos,
           'repository': be_repos, 'entity': be_entities},
    'link': {'function_to_endpoint': func_link},
}
with open(os.path.join(OUT, 'graph.json'), 'w', encoding='utf-8') as fh:
    json.dump(graph, fh, ensure_ascii=False, indent=1)

nf = sum(len(b['functions']) for b in business.values())
linked = sum(1 for v in func_link.values() if v)
print("WEB: zul=%d vm=%d business=%d functions=%d facade=%d service=%d dao=%d entity=%d" % (
    len(zul_vm), len(vm), len(business), nf, len(facade), len(web_service), len(web_dao), len(web_entity)))
print("BE : controller=%d endpoints=%d logic(gen1)=%d dao(gen1)=%d service(gen2)=%d repo=%d entity=%d" % (
    len(controllers), sum(len(c['endpoints']) for c in controllers.values()), len(be_logic), len(be_daos),
    len(be_services), len(be_repos), len(be_entities)))
print("LINK web function -> BE endpoint: %d/%d matched" % (linked, nf))
