---
title: "ADR-0002 关键事实使用追加式事件 Ledger"
status: proposed
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0002 关键事实使用追加式事件 Ledger

## 状态

`proposed`

## 背景

长期状态、撤回、工具和主动行为需要审计与回放。

## 决策

平台事实和关键行为结果追加记录；状态与索引作为投影。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

仅保存当前快照、完整 Event Sourcing 所有内部变化。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
