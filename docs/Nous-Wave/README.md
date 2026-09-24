# Nous Wave 当前研究总报告

本目录维护 Nous Wave 的**当前态研究与系统设计报告源文件**。基础研究资料来自 2026-09-22 的完整研究包，当前正文已进一步纳入 2026-09-24 对 Memory taxonomy、CognitiveSchema、Social Cognition、UseEvent、accessibility、retrieval 与 Heptalogos 边界的设计收敛。

当前代码审查基线：

- Nous Wave：`ArsvineZhu/Nous-Wave@e9af4ebd8a77d316c78764fd85836e6de8d9b7ee`
- Heptalogos：`ArsvineZhu/Heptalogos@a5287a01b42e3d09f445e96982caf6842ed74674`

章节资料来源和实现快照边界见 [SOURCE_MAP.md](SOURCE_MAP.md)。报告正文不记录设计演化史，只描述当前有效设计、实现事实、实验状态和真正开放的问题。

## 构建

正文采用 A4 双栏排版，封面、摘要和目录为单栏；跨栏图表在正文位置横跨两栏。构建说明见 [BUILD.md](BUILD.md)。

- [LaTeX 主文件](main.tex)
- [来源映射](SOURCE_MAP.md)
- [研究总报告 PDF](../../dist/Nous_Wave_Current_Research_Report.pdf)

> `dist/Nous_Wave_Current_Research_Report.pdf` 是生成制品。当前源文件发生设计更新后，在执行一次 clean XeLaTeX/Biber build 并完成引用/版面检查前，PDF 不应被视为最新设计快照；**源文件是当前 canonical document**。

## 当前设计收敛摘要

- Nous Wave 是可组合的 Subject cognition/personality platform；Memory 可独立服务普通 Agent/RAG，高级 Self/Social/Motivation 不是基础运行前提。
- Memory taxonomy 使用 `cognitive_role × formation_mode`，不再以 `Specific / Integrative / Procedural` 互斥分类。
- CognitiveSchema 是 Memory 域的一等对象族；目标架构不再保留万能 Anchor Authority。
- Social Cognition 取代较窄的 Relationship 顶层 owner，首批对象族为有向 RelationshipGraph 与 socially scoped LanguageConvention。
- UseEvent 需要 caller-stable identity 和幂等语义；`retrieved/exposed` 不等于 reinforcement。
- QueryPlan 在候选生成前冻结 lanes/weights/budgets；基础融合采用 object-level fixed-plan weighted RRF。
- EPA、Residual、Wave/PPR 都是算法实验，不能定义 Memory correctness；10 月 27 日前工程重点是 Memory Reference Profile 的完整纵向闭环。
