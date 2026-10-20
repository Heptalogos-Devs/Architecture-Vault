# Nous Wave × Heptalogos · 六图架构图集

打开[离线查看器](架构图集.html)，或阅读[Markdown 图集](系统架构图集.md)。实际边界见[贯通示例](../示例/README.md)。六张图统一采用当前 Spec 的架构和所有权；点击模块可打开相应本地设计页。

- `src/*.dot`：六张可编辑 Graphviz 源，保存模块、调用关系和 Spec 链接。
- `svg/`：六张独立矢量图。
- `pages.json`：页面标题、摘要与来源索引。
- `render_svg.py`：调用成熟 Graphviz 布局，生成 SVG 并检查来源链接。
- `build_viewer.py`、`viewer.css`、`viewer.js`：生成内嵌 SVG、CSS、JS 的离线 HTML 和 Markdown。

有 Graphviz CLI 时：

```sh
python render_svg.py
python build_viewer.py
```

本轮环境使用 `@viz-js/viz` 3.31.0 的 Graphviz WASM。工具依赖和缓存放工作区 temp，查看器无需该依赖：

```sh
npm install --prefix ../../temp/spec-research/atlas-tools \
  --cache ../../temp/spec-research/npm-cache --ignore-scripts \
  --no-audit --no-fund @viz-js/viz@3.31.0
python render_svg.py --wasm \
  ../../temp/spec-research/atlas-tools/node_modules/@viz-js/viz/dist/viz.js
python build_viewer.py
```

颜色：紫为共同主体，蓝为 Nous，橙为 Hept，绿为共享普通库/通用机制，灰为原生或外部依赖。实线标签说明运行调用、事务或事实交接；绿色虚线表示构建/普通库依赖，其他虚线依标签表达可选或受限接线。

依据为[项目宪纲](../项目宪纲.md)、[当前设计入口](../README.md)和各图列出的现行 Spec。两产品各自运行和保存数据；`@nous-wave/platform`、纯 contracts 与 Vue/Vuetify management-ui 按普通库独立发行。图展示目标责任，施工进度见[研究入口](../研究/README.md)。

PNG 是临时检查产物，放 `temp/spec-research/atlas-preview/`；SVG 与 DOT 是本目录维护的正式图源和结果。
