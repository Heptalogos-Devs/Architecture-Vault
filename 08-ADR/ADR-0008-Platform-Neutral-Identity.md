---
title: "ADR-0008 平台感知的中立身份模型"
status: accepted
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0008 平台感知的中立身份模型

## 状态

`accepted`

## 背景

现有参考项目显示默认 QQ 身份会导致跨平台错误。

## 决策

区分 Person、PlatformIdentity、AgentIdentity、Conversation 和 Membership。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

全局 user_id、未知平台回退到 QQ。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
