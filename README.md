# Architecture-Vault

本仓库保存 Heptalogos / Nous Wave 的跨项目研究、长期架构与正式研究文档。各代码仓库维护自身可执行 Architecture、Specs、Plans、Qualification 和实现真值。

## 当前代码仓库

- **Heptalogos 当前产品/工程仓库：** [ArsvineZhu/Heptalogos](https://github.com/ArsvineZhu/Heptalogos)
- **Nous Wave 当前研究实现仓库：** [ArsvineZhu/Nous-Wave](https://github.com/ArsvineZhu/Nous-Wave)

组织内同名旧 `Heptalogos-Devs/Heptalogos` 目前属于更早实现代，不作为 current product truth；个人当前仓库后续计划迁入组织，具体顺序与风险见[仓库与文档对齐审查](docs/repository-governance/2026-09-24-repository-alignment-audit.md)。在迁移完成前，不要仅凭 GitHub organization/name 判断哪个代码树是当前版本。

## Heptalogos

- [Heptalogos 文档入口与当前来源说明](docs/Heptalogos/README.md)
- [旧知识库归档快照](docs/Heptalogos/archive/2026-09-23-before-current-research-report/README.md)

Vault 不复制 Heptalogos 全部实现规范。当前规范以个人仓库中的 `project/governance/`、`docs/architecture/`、`specs/` 和 code/qualification 为准。

## Nous Wave

- [当前研究总报告与源文件](docs/Nous-Wave/README.md)
- [报告编译说明](docs/Nous-Wave/BUILD.md)
- [仓库内 PDF 快照](dist/Nous_Wave_Current_Research_Report.pdf) — 最新源代码对应的 PDF 从 Actions 成功运行的 artifact 下载。
- [GitHub Actions PDF 构建](https://github.com/Heptalogos-Devs/Architecture-Vault/actions/workflows/build-pdf.yml) — 成功运行的 artifact 对应其源代码提交。

Nous Wave 当前研究报告承担跨项目 cognition/personality 设计基线；可执行 Architecture/Decisions/Specs 将在 Nous-Wave 代码仓库中按该设计重新下降。

## Repository Governance

- [2026-09-24 仓库与文档对齐审查](docs/repository-governance/2026-09-24-repository-alignment-audit.md)

任何 repository rename/archive/transfer 都应独立执行并保留 successor notice、HEAD/Repository ID、外部链接和回滚检查；Vault 中的治理建议本身不会自动改变 GitHub 仓库状态。
