---
title: "Reactor 输入流"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-24
updated: 2026-07-24
tags: [component, reactor-feed]
---

# Reactor 输入流

## 目的

把 Canonical Ledger 投影为中央 Reactor 可消费、可恢复且可重建的输入流。

## 契约

- 输入：已提交的 `CanonicalInteraction v2`。
- 输出：有稳定序号的 `ReactorFeedItem v1`。
- 消费者以独立 checkpoint 确认成功处理；重复投递允许，副作用必须幂等。

## 不变量

- Feed 不是事实权威，不承载 Adapter DTO。
- 只有目标 capture scope 的交互进入第一版 Feed。
- Feed 可从 Canonical Ledger 全量重建。

## 消费语义

每个 consumer 拥有独立、单调递增的 checkpoint。读取 checkpoint 之后的稳定 ordinal，
处理成功后才 acknowledge；进程在处理后、确认前崩溃会收到重复 item。因此 Feed 提供
至少一次而非 exactly-once，Reactor 的 Intent 提交必须使用稳定幂等 ID。

当前 Interaction Gateway 到此为止：它不实现人格、记忆、模型或行为策略。这个限制
防止通信可靠性层因认知实现变化而失去可回放性。
