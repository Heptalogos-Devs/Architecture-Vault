"""Build a fully offline SVG atlas and Markdown index from the current page manifest."""
from pathlib import Path
from html import escape
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
pages = json.loads((ROOT / 'pages.json').read_text())
sections, tabs = [], []
md = ['# Nous Wave × Heptalogos · 系统架构图集', '',
      '六张图使用当前 Spec 的同一套所有权：两个独立 TypeScript 产品及数据库，普通共享库和正式 Clients，原生执行与真实外部效果。', '',
      '[打开离线查看器](架构图集.html)。切换、缩放、拖动和来源链接均在本地工作。绿色虚线表示构建/普通库依赖，实线标签说明运行调用或事实交接。', '']
for index, page in enumerate(pages, 1):
    key, name, title = page['id'], page['file'], page['title']
    source_links = []
    for source in page['sources']:
        if not (ROOT.parent / source).is_file():
            raise ValueError(f'Missing Spec: {source}')
        source_links.append(f'<a href="../{escape(source)}" target="_blank" rel="noopener">{escape(Path(source).stem)}</a>')
    raw = (ROOT / 'svg' / (name + '.svg')).read_text()
    document = ET.fromstring(raw)
    width, height = map(float, document.attrib['viewBox'].split()[2:])
    svg = re.sub(r'^.*?(?=<svg\b)', '', raw, count=1, flags=re.S)
    svg = re.sub(r'(<a\b[^>]*?xlink:href=")\.\./\.\./', r'\1../', svg)
    svg = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{key}-{m.group(1)}"', svg)
    svg = svg.replace('<svg ', f'<svg class="diagram" data-base-w="{width}" data-base-h="{height}" ', 1)
    sections.append(f'''<section id="view-{key}" class="page" data-key="{key}" aria-labelledby="title-{key}">
<div class="section-head"><div><div class="eyebrow">架构图 {index:02d} / 06</div><h2 id="title-{key}">{escape(title)}</h2><p>{escape(page['description'])}</p><div class="sources">{''.join(source_links)}</div></div><a class="download" href="svg/{escape(name)}.svg" download>获取 SVG</a></div>
<div class="legend">蓝：Nous　橙：Hept　绿：普通库/通用机制　灰：原生或外部依赖　紫：共同主体　｜　点击图中模块查看当前 Spec</div>
<div class="viewport" tabindex="0"><div class="svg-host">{svg}</div></div><div class="view-foot">拖动查看 · Ctrl/⌘ + 滚轮缩放 · 点击模块打开本地 Spec</div></section>''')
    tabs.append(f'<button type="button" class="tab" data-tab="{key}" aria-controls="view-{key}" aria-selected="false">{escape(title)}</button>')
    md.extend([f'## {index}. {title}', '', page['description'], '', f'![{title}](svg/{name}.svg)', '',
               f'[编辑 DOT 源](src/{name}.dot) · ' + ' · '.join(f'[{Path(source).stem}](../{source})' for source in page['sources']), ''])
md.extend(['## 所有权与阅读规则', '',
 '- platform、contracts、Client、management-ui 为普通构建依赖，各产品单独实例化；共享 UI 使用 Vue/Vuetify，领域页面归各 apps/web。',
 '- AI SDK 承担普通角色调用；OpenClaw 承担专业 Task、工具、历史、Skills 和原生渠道。默认 QQ 为 OneBot 源码改编，AstrBot 保留可选接入及管理参考。',
 '- Lance 承担文档级 FTS/dense；原 Rust 数值库经 napi-rs 在 Nous 进程内调用，保留 Native/VCP、nalgebra 和内部 USearch。',
 '- Material 保全、实际消费和后续形成分别记录。世界/行为领域、原生执行及外部效果各有实际 owner。',
 '- clock.read 只读投影；capture/captureIn 保存源高水位与时间回执。DBOS 承担持久等待、长工作和恢复，普通领域直接短事务。',
 '', '## 依据', '', '[项目宪纲](../项目宪纲.md)与各图列出的当前设计文档。图展示目标责任，实际实施和验证进度见[研究入口](../研究/README.md)。', ''])
(ROOT / '系统架构图集.md').write_text('\n'.join(md))
css = (ROOT / 'viewer.css').read_text()
js = (ROOT / 'viewer.js').read_text()
html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none';style-src 'unsafe-inline';script-src 'unsafe-inline';img-src data:;connect-src 'none'"><title>Nous × Hept · 架构图集</title><style>{css}</style></head><body>
<header class="topbar"><div class="head-inner"><div class="eyebrow">SYSTEM ARCHITECTURE ATLAS</div><h1>Nous Wave × Heptalogos</h1><p class="subtitle">两个独立产品、普通共享库、真实领域与原生执行。所有图和交互离线内嵌。</p></div></header><main>
<nav aria-label="架构图导航">{''.join(tabs)}<div class="tools"><button class="tool" id="zoomout" aria-label="缩小">－</button><span id="zoomvalue" class="zoom-value">适配</span><button class="tool" id="zoomin" aria-label="放大">＋</button><button class="tool" id="fit">适配</button><button class="tool" id="actual">1:1</button></div></nav>
{''.join(sections)}
<div class="context"><h3>来源与可编辑文件</h3><div class="resource-row"><a href="系统架构图集.md">Markdown 图集</a><a href="README.md">重建方法</a><a href="../README.md">当前设计入口</a></div><p>图中模块链接对应当前本地 Spec；DOT 决定内容与连线，Graphviz 负责布局。页面不请求外部脚本、字体或网络资源。</p></div></main><script>{js}</script></body></html>'''
(ROOT / '架构图集.html').write_text(html)
print(f'Built {len(pages)} embedded diagrams; HTML {len(html)} chars')
