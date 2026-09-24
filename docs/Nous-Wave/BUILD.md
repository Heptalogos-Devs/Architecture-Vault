# Nous Wave 研究总报告编译说明

报告采用 A4 双栏中文技术报告版式。编排参考 [GB/T 7713.3-2014《科技报告编写规则》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E2BA32B0F5E570E5844A9E7E2D42393F)、[GB/T 7713.2-2022《学术论文编写规则》](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0B963916637B8F34B295FCF4A51A1BE5) 和 [ACM 双栏会议论文说明](https://compass.acm.org/camera-ready-instructions/)。文档使用 `ctexbook`、XeLaTeX 与 Biber。

## 本地编译

在仓库根目录运行：

```powershell
Set-Location docs/Nous-Wave
latexmk -C
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
Set-Location ../..
New-Item -ItemType Directory -Force dist
Copy-Item tmp/pdfs/research/main.pdf dist/Nous_Wave_Current_Research_Report.pdf
```

`latexmkrc` 将 `$pdf_mode` 设为 5（XeLaTeX），并将辅助文件和中间 PDF 写入仓库根目录的 `tmp/pdfs/research`。该目录和 LaTeX 生成的辅助文件由 `.gitignore` 忽略。`dist/Nous_Wave_Current_Research_Report.pdf` 是单独维护的发布快照。

## GitHub Actions 构建

[PDF 构建工作流](https://github.com/Heptalogos-Devs/Architecture-Vault/actions/workflows/build-pdf.yml) 会在推送到 `main`、针对 `main` 的拉取请求和手动运行时，使用 TeX Live 2026 与 XeLaTeX 编译当前报告。成功运行会将对应提交的 PDF 上传为 Actions artifact，保留 90 天；可从该次工作流运行页面下载。CI 不会自动提交生成文件；最新源代码对应的 PDF 以成功运行的 artifact 为准。

## 2026-09-24 当前源文件构建记录

使用 TeX Live 2026、XeTeX 3.141592653-2.6-0.999998、latexmk 4.87 和 Biber 2.21 完成 clean build。当前源文件输出 54 页 A4 PDF；构建退出码为 0，未解析引文/交叉引用和 LaTeX fatal error 计数为 0。日志仍有 17 条非致命 Overfull 诊断。

## 上一已验证生成快照

2026 年 9 月 23 日曾完成一次干净构建，输出 41 页 A4 PDF。构建环境：TeX Live 2026、XeTeX 3.141592653-2.6-0.999998、latexmk 4.87、Biber 2.21。当次检查记录为：无未解析引文、交叉引用、缺字、Overfull 或 LaTeX fatal error；日志保留少量非致命 Underfull 提示。版面抽查覆盖封面、摘要、目录、双栏正文、图表、公式、伪代码和参考文献。
