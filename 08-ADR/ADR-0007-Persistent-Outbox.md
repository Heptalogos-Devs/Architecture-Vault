---
title: "ADR-0007 使用持久化 Outbox 执行消息投递"
status: proposed
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0007 使用持久化 Outbox 执行消息投递

## 状态

`proposed`

## 背景

延迟、取消、重启和回执要求生成与发送解耦。

## 决策

ActionPlan 持久化并由工作器幂等发送。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

生成后直接调用平台 SDK、内存定时器。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
