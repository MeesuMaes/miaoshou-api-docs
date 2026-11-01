#!/usr/bin/env python3
"""从 source/ 下整理好的文档生成 docs/ 页面和 sidebar.json。用法：python3 scripts/generate.py"""
import json, os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, DOCS = os.path.join(ROOT, 'source'), os.path.join(ROOT, 'docs')
APIFOX = 'https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/'
SLUG = {
 '商品':'product','包裹':'package','采购':'purchase','仓储':'warehouse','货源账号':'source-account',
 '店铺':'shop','公共采集箱':'common-collect-box','TK采集箱':'tk-collect-box','TEMU全托采集箱':'temu-full-collect-box',
 'TEMU半托采集箱':'temu-semi-collect-box','OZON采集箱':'ozon-collect-box','Shopee采集箱':'shopee-collect-box',
 '在线产品管理':'online-product','Shopee全球在线产品管理':'shopee-global','Mercadolibre采集箱':'mercadolibre-collect-box',
 'AI公共服务':'ai-service','AI润色':'ai-polish','图片处理':'image-process','图片空间':'image-space',
 '采集箱':'collect-box','产品发布':'publish','商品发布':'publish','发布产品':'publish','定价模板':'pricing-template','车型库':'vehicle',
 '发货':'ship','基础信息修改':'edit','获取包裹':'query','运单':'waybill','售后':'after-sale','履约':'fulfillment','基础管理':'basic',
 '采购记录':'purchase-record','供应商':'supplier','采购单':'purchase-order',
 '仓库':'warehouse','三方仓仓库':'third-party','自营仓仓库':'self-operated','商品sku':'sku','商品分组':'group','商品品牌':'brand',
 '商品包材':'packaging','库存':'inventory','三方仓sku库存':'third-party','自营仓库存':'self-operated','数据统计':'stats',
 '商品周转分析':'turnover','销售数据':'sales',
}
FILES = ['01-product.md','02-package.md','03-purchase.md','04-warehouse.md','05-source-account.md']
POST = ('<svg xmlns="http://www.w3.org/2000/svg" width="36" height="16"><rect width="36" height="16" rx="4" fill="#fff1e6"/>'
        '<text x="18" y="12" font-size="9" font-weight="700" font-family="sans-serif" text-anchor="middle" fill="#f97316">POST</text></svg>')

def esc(t):  # MDX 安全：表格/正文里的 { } < 转义（代码块除外）
    out, code = [], False
    for line in t.split('\n'):
        if line.lstrip().startswith('```'): code = not code
        if not code:
            parts = re.split(r'(`[^`]*`)', line)
            line = ''.join(p if p.startswith('`') else p.replace('{','\\{').replace('}','\\}').replace('<','&lt;') for p in parts)
        out.append(line)
    return '\n'.join(out)

def w(rel, text):
    p = os.path.join(DOCS, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(text)

def main():
    for d in os.listdir(DOCS):
        if d != 'public': shutil.rmtree(os.path.join(DOCS, d)) if os.path.isdir(os.path.join(DOCS, d)) else os.remove(os.path.join(DOCS, d))
    idx = json.load(open(os.path.join(SRC, 'index.json')))
    sections = {}
    for f in FILES:
        for part in re.split(r'^### ', open(os.path.join(SRC, f)).read(), flags=re.M)[1:]:
            title, body = part.split('\n', 1)
            body = re.split(r'^## ', body, flags=re.M)[0].rstrip().rstrip('-').rstrip()
            m = re.search(r'`(?:GET|POST)\s+(\S+)`', body)
            sections[(title.strip(), m.group(1) if m else '')] = body
    tree, used = {}, set()
    for top, sub, title, method, path, rw, aid in idx:
        levels = [top] + [s for s in sub.split('>') if s] if sub else [top]
        if top == '货源账号': levels = [top]
        dirs = '/'.join(SLUG[l] for l in levels)
        leaf = path.rstrip('/').split('/')[-1].replace('_', '-')
        url = f'/{dirs}/{leaf}'
        if url in used: url += '-' + aid
        used.add(url)
        body = sections.get((title, path)) or sections.get(next((k for k in sections if k[0] == title), None), '')
        body = re.sub(r'（本地 raw/[^）]*）', '', body)
        body = body.replace('（见 README 签名机制）', '（见[快速接入](/quick-start)签名机制）')
        w(url.lstrip('/') + '.md', f'# {title}\n\n{esc(body)}\n')
        node = tree
        for l in levels: node = node.setdefault(l, {})
        node.setdefault('_items', []).append({'text': title, 'link': url, 'tag': POST})
    count = len(used)
    def build(name, node, prefix):
        slug = prefix + '/' + SLUG[name]
        items = list(node.get('_items', [])) + [build(k, v, slug) for k, v in node.items() if k != '_items']
        lines = [f'# {name}\n', f'共 {sum(1 for _ in leaves(node))} 个接口。\n']
        lines += [f'- [{t}]({u})' for t, u in leaves(node)]
        w(slug.lstrip('/') + '/index.md', '\n'.join(lines) + '\n')
        return {'text': name, 'link': slug + '/', 'collapsed': True, 'items': items}
    def leaves(node):
        for i in node.get('_items', []): yield i['text'], i['link']
        for k, v in node.items():
            if k != '_items': yield from leaves(v)
    readme = open(os.path.join(SRC, 'README.md')).read()
    qs = readme.split('## 一、接入概要（摘自「快速接入」）', 1)[1].split('## 二、全部接口索引', 1)[0]
    w('quick-start.md', '# 快速接入\n' + esc(qs) + f'\n\n原文：[{APIFOX}8586023m0.md]({APIFOX}8586023m0.md)\n')
    shein = open(os.path.join(SRC, 'shein-notes.md')).read()
    for f, u in [('README.md', '/quick-start'), ('01-product.md', '/product/'), ('02-package.md', '/package/'),
                 ('03-purchase.md', '/purchase/'), ('04-warehouse.md', '/warehouse/'), ('05-source-account.md', '/source-account/')]:
        shein = shein.replace(f']({f})', f']({u})')
    w('shein.md', esc(shein))
    groups = [build(k, tree[k], '') for k in ['商品', '包裹', '采购', '仓储', '货源账号']]
    side = [{'text': '开放平台', 'collapsed': False, 'items': [{'text': '快速接入', 'link': '/quick-start'}] + groups},
            {'text': '与 SHEIN 的关系', 'link': '/shein'}]
    json.dump(side, open(os.path.join(ROOT, 'sidebar.json'), 'w'), ensure_ascii=False, indent=1)
    w('index.md', '''---
pageType: home
hero:
  name: 妙手开放平台 API 文档
  tagline: 由 apifox 分享文档整理：商品、包裹、采购、仓储、货源账号
  actions:
    - theme: brand
      text: 快速接入
      link: /quick-start
    - theme: alt
      text: 商品接口
      link: /product/
---
''')
    print(f'生成接口页 {count} 个')

if __name__ == '__main__':
    main()
