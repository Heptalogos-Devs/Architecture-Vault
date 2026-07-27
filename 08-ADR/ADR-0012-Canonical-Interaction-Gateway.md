---
title: "ADR-0012 Canonical Interaction Gateway"
status: accepted
type: adr
confidentiality: internal
created: 2026-07-24
updated: 2026-07-24
tags:
  - adr
  - interaction-gateway
  - evidence
  - delivery
---

# ADR-0012 Canonical Interaction Gateway

## 状态

`accepted`

## 背景

当前 Edge 已证明 raw-first、协议隔离、媒体归档和持久恢复可行，但其单活动适配器、
单数据库和单 `EventEnvelope` 边界不足以表达多账号、多来源融合、可恢复 Reactor
Feed 和可靠出站。

## 决策

采用以 Canonical Interaction 为稳定边界的双向通信网关：

```text
Adapter Evidence → Fusion → Canonical Ledger → Reactor Feed
Reactor Intent → Routing → Delivery Plan → Adapter Evidence → Outcome
```

- 每个 Adapter Instance 拥有独立 Evidence Store，中央 Gateway Store 保存
  Canonical、Feed、Intent、Delivery 和 cursor。
- Evidence、Canonical、Feed、Intent、Plan 与 Outcome 是不同权威记录。
- 平台、平台账号、协议、实现、适配器实例和连接会话分别建模。
- 一个 Canonical Fact 可以关联多个 Evidence Source；raw reception 不合并。
- Reactor 只消费 Feed、提交 Intent，不直接读取 Adapter DB 或调用平台。
- 默认回复原端点；只允许同账号显式备用，不自动跨账号或跨平台。
- 平台调用前后都保存 evidence；不确定结果进入 `uncertain` 且不盲目重试。
- 初期使用 `heptalogos-interaction` 单代码包和多运行角色，不拆微服务。

## 后果

- 旧 Edge DB 只读封存，通过 raw replay importer 进入新模型。
- 需要维护 Evidence、Canonical、Feed、Intent、Plan 与 Outcome 的版本化契约。
- SQLite 仍可用于单机研究，但不同数据权威使用不同 schema identity 和数据库。
- Adapter 失败可隔离；跨数据库工作通过 cursor、lease、reconciliation 恢复。

## 设计哲学

该决策优先建立“谁对什么事实负责”，再决定进程如何部署。单包多角色降低当前运维
成本，但 Evidence、Canonical、Feed、Intent、Plan 与 Outcome 仍保持独立权威。
系统接受至少一次读取和最终收敛，不以无法实现的跨 SQLite/QQ exactly-once 作为
承诺。遇到外部副作用未知时保留 `uncertain`，因为可解释的不确定性优于看似成功的
自动重试。

Capture scope 采用 raw-all/derived-allowlist，是对可回放性与认知最小化的折中：
Adapter 已观察到的原文不被后验策略删除，非目标内容又不会进入 Canonical、Feed 和
资产管线。

## 与既有 ADR 的关系

- 扩展 ADR-0007 的 Outbox，使 Intent、Plan、Attempt 和 Outcome 分离。
- 扩展 ADR-0010 的三层入站边界，加入多来源 Fusion 和 Reactor Feed。
- 保留 ADR-0011 的 Milky 实验地位，并要求 OneBot/Milky 通过同一契约。

## 验证

- Fake 多账号、多来源和主备故障测试。
- Milky/OneBot adapter contract。
- Fusion cursor、重复来源、opaque、allowlist 和崩溃恢复测试。
- Delivery 的调用前、调用中、响应后崩溃矩阵及 `uncertain` 对账。
- 旧库只读、幂等 replay 和 hash 对账。
