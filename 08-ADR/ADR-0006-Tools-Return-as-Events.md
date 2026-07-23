---
title: "ADR-0006 异步能力结果重新作为事件进入系统"
status: proposed
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0006 异步能力结果重新作为事件进入系统

## 状态

`proposed`

## 背景

隐藏回调会绕过状态、权限和审计。

## 决策

工具、媒体和任务结果写入 Ledger，再由正常管线处理。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

直接将结果追加到正在运行的模型循环。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
