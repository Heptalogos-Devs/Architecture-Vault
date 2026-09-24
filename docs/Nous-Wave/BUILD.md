# Nous Wave 研究总报告编译说明

报告采用 A4 双栏中文技术报告版式。编排参考 [GB/T 7713.3-2014《科技报告编写规则》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E2BA32B0F5E570E5844A9E7E2D42393F)、[GB/T 7713.2-2022《学术论文编写规则》](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0B963916637B8F34B295FCF4A51A1BE5) 和 [ACM 双栏会议论文说明](https://compass.acm.org/camera-ready-instructions/)。文档使用 `ctexbook`、XeLaTeX 与 Biber。

## 编译

在仓库根目录运行：

```powershell
Set-Location docs/Nous-Wave
latexmk -C
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
Set-Location ../..
New-Item -ItemType Directory -Force dist
Copy-Item tmp/pdfs/research/main.pdf dist/Nous_Wave_Current_Research_Report.pdf
```

`latexmkrc` 将编译中间文件写入仓库根目录的 `tmp/pdfs/research`，并由 latexmk 调用 Biber。

## 当前构建状态

**当前 canonical source 已更新至 2026-09-24，尚未在本次文档增量中重新执行 TeX clean build。** 因此 `dist/Nous_Wave_Current_Research_Report.pdf` 在重新构建前只代表上一生成快照，不应被引用为最新设计内容。

合并当前源文件后，需要在装有 TeX Live 2026 的开发机执行上述 clean build，并检查：

- undefined citation / reference；
- Biber error / warning；
- missing glyph / font fallback；
- Overfull / 严重 Underfull；
- 大表格、TikZ 图、代码/路径换行；
- PDF metadata、目录、书签和超链接；
- 封面、摘要、普通双栏页、跨栏表、参考文献和附录的视觉结果。

检查完成后，再更新本节的“最新已验证构建记录”和 `dist` PDF。

## 上一已验证生成快照

2026 年 9 月 23 日曾完成一次干净构建，输出 41 页 A4 PDF。构建环境：TeX Live 2026、XeTeX 3.141592653-2.6-0.999998、latexmk 4.87、Biber 2.21。当次检查记录为：无未解析引文、交叉引用、缺字、Overfull 或 LaTeX fatal error；日志保留少量非致命 Underfull 提示。版面抽查覆盖封面、摘要、目录、双栏正文、图表、公式、伪代码和参考文献。

该记录仅证明 **2026-09-23 的源文件快照** 可以成功构建，不证明 2026-09-24 当前源文件已经验证。
