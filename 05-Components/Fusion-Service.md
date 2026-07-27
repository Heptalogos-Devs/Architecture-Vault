---
title: "交互融合服务"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-24
updated: 2026-07-24
tags: [component, fusion]
---

# 交互融合服务

## 目的

从多个 Adapter Evidence Store 读取未融合记录，生成平台中立交互事实、多来源关联
和可恢复 source cursor。

## 输入与输出

- 输入：`EvidenceRecord v1`、Adapter/Account/Conversation binding、capture policy。
- 输出：`CanonicalInteraction v2`、provenance、diagnostic、asset job、source cursor。

## 不变量

- cursor 只能与 canonical/provenance 在同一 Gateway 事务中推进。
- payload hash 不用于合并两次真实接收。
- 无可靠稳定身份时宁可保留多个事实。
- 未知语义以 opaque 保存；allowlist 只过滤派生，不过滤 evidence。

## 当前执行机制

Gateway 轮询每个 `FusionSourceBinding`：从 Gateway 保存的 source cursor 开始读取该
Evidence Store，逐条调用与 adapter kind 对应的 normalizer，再由
`commit_fusion` 原子提交 result 和新 cursor。一个来源的空闲不阻止其他来源运行。

Normalizer 的结果可以是 canonical、filtered 或 diagnostic/opaque。稳定平台消息
身份允许实时、历史和不同 Adapter 观察关联同一事实，同时所有 provenance 仍保留；
无法证明相同时不猜测融合。

## 设计理由

cursor 放在 Gateway 而不是 Adapter 内，是因为“是否已形成中央事实”只能由中央事务
回答。若先在源库确认再写中央库，崩溃会永久跳过 evidence；若中央提交失败而 cursor
不动，重复 normalize 是安全且可审计的。
