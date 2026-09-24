# Nous Wave 文档入口

本目录保存 Nous Wave 的目标设计、设计论证、研究证据、当前工程状态和实施计划。不同文档承担不同职责，不能互相替代。

## 首要文档

- **[目标设计 PDF](https://github.com/Heptalogos-Devs/Architecture-Vault/releases/download/nous-wave-target-design-latest/Nous_Wave_Target_Design.pdf)**：正式设计文档。只陈述系统应当是什么，不记录设计历史、方案比较、实验、代码现状或施工计划。
- **[LaTeX 目标设计源文件](main.tex)**：PDF 的规范源文件。
- **[文档职责与阅读顺序](DOCUMENT_MODEL.md)**：说明各类文档的权威范围。
- **[设计决定索引](DECISIONS.md)**：面向人和研发 Agent 的高密度入口，列出已经确定的设计决定及其详细位置。

## 论证与研究

- [设计论证](rationale/README.md)：解释设计选择、比较替代方案、记录失败模式和设计后果。这里可以讨论方案，但不覆盖目标设计。
- [研究与实验](research/README.md)：保存外部研究、算法实验、数学核对和软件研究快照。

## 工程推进

- [当前工程状态](CURRENT_STATE.md)：描述代码现在实际做到什么，不定义目标设计。
- [未决问题](OPEN_QUESTIONS.md)：记录尚未进入目标设计的研究问题和规格问题。
- [实施计划](plans/README.md)：从目标设计和当前状态下降到可执行规格、代码和验证。
- [实现审查](audits/README.md)：记录代码与目标设计之间的差距、缺陷和迁移事项。
- [编译说明](BUILD.md)：目标设计 PDF 的本地和持续集成构建方式。

## 建议阅读顺序

新的研发 Agent 依次读取：

1. `DOCUMENT_MODEL.md`
2. `DECISIONS.md`
3. 目标设计中与任务相关的章节
4. 对应的 `rationale/` 论证文档
5. `CURRENT_STATE.md` 与相关 `audits/`
6. 当前 `plans/`
7. 进入代码仓库后，再读取代码仓自身的架构、设计决定、可执行规格和实现

目标设计与设计论证发生冲突时，以目标设计为准；当前代码与目标设计发生冲突时，差异进入审查和计划，不反向改写目标设计。
