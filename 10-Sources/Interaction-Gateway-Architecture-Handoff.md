---
title: "多平台 IM 交互网关架构交接"
status: confirmed
type: source-note
confidentiality: internal
created: 2026-07-24
updated: 2026-07-24
tags:
  - source
  - interaction-gateway
  - architecture-handoff
---

# 多平台 IM 交互网关架构交接

## 来源

- 原始文件：`heptalogos_interaction_gateway_architecture.md`
- 接收时间：2026-07-24
- 来源性质：内部架构交接
- 原始状态：架构草案 / 实施基线
- 本库处理：核心判断进入 accepted ADR-0012；精确 schema、跨平台身份、复杂降级和
  分布式部署继续保留为 proposed/open。

原始文件保留在项目所有者的内部资料目录中；本笔记记录其可执行架构结论，避免把
本机绝对路径或潜在私密内容纳入仓库。

## 核心结论

Heptalogos 的 IM 边界应是以 Canonical Interaction 为稳定边界的双向通信网关，
而不是若干 SDK 的统一 `send/receive` 包装器。网关由以下权威记录组成：

1. Adapter Evidence Ledger：保存协议实现实际观察和执行的原始事实。
2. Canonical Interaction Ledger：保存融合后的平台中立交互事实及多来源。
3. Reactor Feed / Outbound Intent Ledger：隔离反应器输入与反应器决策。
4. Delivery Plan、Adapter Evidence 与 Canonical Outcome：保存路由、平台调用及结果。

平台、平台账号、协议、协议实现、适配器实例和连接会话必须分离。一个主体可以拥有
多个平台账号；同一平台账号可以由多个适配器实例承载。跨平台身份不得由昵称等弱信号
自动合并。

## 可靠性结论

- raw evidence 必须先于解释和副作用提交。
- Fusion 为每个来源保存独立 cursor，只有 canonical 提交后才推进。
- Reactor Feed 是可重建投影，不是权威事实库。
- Intent 必须在平台调用前持久化，Delivery Plan 与 Intent 分离。
- 请求可能到达平台但响应丢失时必须形成 `uncertain`，不得盲目重试。
- 媒体拥有独立资产生命周期，不阻塞消息事实进入反应器。
- 系统采用持久化、至少一次、可重放和幂等，不承诺 exactly-once。

## 第一阶段边界

- 单包多运行角色，每个 Adapter Instance 独立 Evidence SQLite，中央 Gateway SQLite。
- QQ 使用 LLBot/Milky 与 NapCat/OneBot 双协议；多账号和主备用 Fake 验证。
- 入站完成 Evidence → Fusion → Canonical → Reactor Feed。
- 出站完成 Intent → Route → Delivery → Evidence → Outcome。
- 默认保持原平台账号、原会话和原 Adapter Instance；只允许显式同账号备用。
- 不实现中央 Reactor 内部、自动跨平台身份、自动跨账号回退或双活发送。

## 后续开放问题

- Canonical schema 的长期版本策略。
- 人工跨平台身份声明与拆分工作流。
- 多来源内容冲突和人工核验。
- 媒体未就绪时 Reactor Feed 的高级聚合策略。
- 从 SQLite 迁移到外部数据库或队列的量化触发条件。

## 关联

- [[08-ADR/ADR-0012-Canonical-Interaction-Gateway]]
- [[04-Architecture/Architecture-Baseline]]
- [[03-Domain-Model/Event-and-Fact-Model]]
- [[03-Domain-Model/Action-and-Delivery]]

