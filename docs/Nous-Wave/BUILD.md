# Nous Wave 目标设计编译说明

目标设计采用 A4 双栏中文技术文档版式，使用 `ctexbook`、XeLaTeX 与 `latexmk`。PDF 本身不包含研究参考文献，因此构建不需要 Biber。

## 本地编译

在仓库根目录运行：

```powershell
Set-Location docs/Nous-Wave
latexmk -C
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
Set-Location ../..
New-Item -ItemType Directory -Force dist
Copy-Item tmp/pdfs/target-design/main.pdf dist/Nous_Wave_Target_Design.pdf
```

`latexmkrc` 将中间文件写入 `tmp/pdfs/target-design`。

## GitHub Actions

`.github/workflows/build-pdf.yml` 在推送到 `main`、针对 `main` 的拉取请求和手动触发时编译目标设计。成功构建会：

1. 上传对应提交的 Actions artifact；
2. 在 `main` 成功构建时更新 `nous-wave-target-design-latest` Release 中的 `Nous_Wave_Target_Design.pdf`。

稳定下载地址：

`https://github.com/Heptalogos-Devs/Architecture-Vault/releases/download/nous-wave-target-design-latest/Nous_Wave_Target_Design.pdf`

## 验证要求

目标设计源文件发生变化后，至少检查：

- XeLaTeX clean build 成功；
- 无未解析交叉引用；
- 无 fatal error 和 Overfull；
- 封面、摘要、目录、宽表、架构图、附录能够正常渲染；
- 中文与英文术语无缺字；
- PDF metadata 与文件名为“Nous Wave 目标设计”。
