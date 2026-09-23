# Nous Wave 研究总报告编译说明

报告采用 A4 双栏中文技术报告版式。编排参考 [GB/T 7713.3-2014《科技报告编写规则》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E2BA32B0F5E570E5844A9E7E2D42393F)、[GB/T 7713.2-2022《学术论文编写规则》](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0B963916637B8F34B295FCF4A51A1BE5) 和 [ACM 双栏会议论文说明](https://compass.acm.org/camera-ready-instructions/)。文档使用 `ctexbook`、XeLaTeX 与 Biber。

## 编译

在仓库根目录运行：

```powershell
Set-Location docs/current-research-report
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
Set-Location ../..
New-Item -ItemType Directory -Force dist
Copy-Item tmp/pdfs/research/main.pdf dist/Nous_Wave_Current_Research_Report.pdf
```

`latexmkrc` 将编译中间文件写入仓库根目录的 `tmp/pdfs/research`，并由 latexmk 调用 Biber。

## 本次报告构建记录

2026 年 9 月 23 日完成干净构建，输出 41 页 A4 PDF。构建环境为 TeX Live 2026、XeTeX 3.141592653-2.6-0.999998、latexmk 4.87、Biber 2.21。检查结果为：无未解析引文、交叉引用、缺字、Overfull 与 LaTeX 错误；日志保留少量非致命 Underfull 提示。版面抽查覆盖封面、摘要、目录、双栏正文、图表、公式、伪代码和参考文献，PDF 文本检查覆盖占位符与未解析引用。