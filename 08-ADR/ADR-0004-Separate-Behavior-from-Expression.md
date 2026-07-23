---
title: "ADR-0004 行为选择与表达生成分离"
status: proposed
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0004 行为选择与表达生成分离

## 状态

`proposed`

## 背景

文本风格不能替代是否应行动和行动目标。

## 决策

先产生 BehaviorIntent，再计划工具和生成表达。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

单次模型直接生成最终消息。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
