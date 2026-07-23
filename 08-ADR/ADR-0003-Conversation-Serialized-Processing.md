---
title: "ADR-0003 按 Agent 与会话串行处理"
status: proposed
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0003 按 Agent 与会话串行处理

## 状态

`proposed`

## 背景

IM 中连续消息和延迟发送容易发生竞态。

## 决策

使用 agent_id + conversation_id Mailbox；共享关系状态使用版本控制。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

全局单线程、每事件完全并行。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
