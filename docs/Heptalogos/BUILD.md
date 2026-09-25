# Heptalogos 目标设计 PDF 构建

构建需要 XeLaTeX、`latexmk` 和仓库中的 `latexmkrc`。在 Heptalogos 文档目录执行：

```powershell
latexmk -C
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

PDF 与中间文件写入仓库根目录下的 `tmp/pdfs/heptalogos-target-design/`。本地生成文件已由根目录 `.gitignore` 排除。

修改目标设计源文件后，执行干净构建，检查交叉引用、页面锚点、字体和错误告警，并将 PDF 每页渲染成图像检查标题、段落、页码与表格布局。GitHub Actions 使用相同的 LaTeX 源构建并发布目标设计 PDF。
