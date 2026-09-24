# Architecture-Vault

Architecture-Vault 保存 Heptalogos / Nous Wave 的跨项目目标设计、设计论证、研究证据和长期架构资料。各代码仓库维护自身执行期的架构、设计决定、实施计划、可执行规格、资格记录和代码真值。

## Nous Wave

Nous Wave 文档按职责分层：

- [Nous Wave 文档入口](docs/Nous-Wave/README.md)
- [文档职责与权威层级](docs/Nous-Wave/DOCUMENT_MODEL.md)
- [设计决定索引](docs/Nous-Wave/DECISIONS.md)
- [目标设计 LaTeX 源文件](docs/Nous-Wave/main.tex)
- [目标设计 PDF 构建](https://github.com/Heptalogos-Devs/Architecture-Vault/actions/workflows/build-pdf.yml)
- [稳定目标设计 PDF](https://github.com/Heptalogos-Devs/Architecture-Vault/releases/download/nous-wave-target-design-latest/Nous_Wave_Target_Design.pdf)

目标设计 PDF 只陈述系统应当是什么。方案比较、数学候选、外部研究、算法实验、当前代码差距和交付计划分别保存在 `rationale/`、`research/`、`CURRENT_STATE.md`、`audits/` 和 `plans/`。

## 当前代码仓库

- **Heptalogos 当前产品与工程仓库：** [ArsvineZhu/Heptalogos](https://github.com/ArsvineZhu/Heptalogos)
- **Nous Wave 当前研究实现仓库：** [ArsvineZhu/Nous-Wave](https://github.com/ArsvineZhu/Nous-Wave)

组织内同名旧 `Heptalogos-Devs/Heptalogos` 属于更早实现代，不作为当前产品真值。迁移和归档建议见[仓库与文档对齐审查](docs/repository-governance/2026-09-24-repository-alignment-audit.md)。

## Heptalogos

- [Heptalogos 文档入口与当前来源说明](docs/Heptalogos/README.md)
- [旧知识库归档快照](docs/Heptalogos/archive/2026-09-23-before-current-research-report/README.md)

Vault 不复制 Heptalogos 的全部实现规范。当前实现规范以 Heptalogos 代码仓库中的治理、架构、规格、资格记录和代码为准。

## 仓库治理

- [2026-09-24 仓库与文档对齐审查](docs/repository-governance/2026-09-24-repository-alignment-audit.md)
