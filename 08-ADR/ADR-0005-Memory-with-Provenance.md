---
title: "ADR-0005 长期记忆必须带来源和生命周期"
status: accepted
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
---

# ADR-0005 长期记忆必须带来源和生命周期

## 状态

`accepted`

## 背景

错误记忆在长期系统中会自我强化。

## 决策

候选、来源、作用域、置信度、冲突、替代和删除是一等字段。

## 后果

- 获得更清晰的审计、测试或演化边界。
- 引入额外契约、存储或编排复杂度，需要通过实验确认收益。
- 实现必须提供迁移和回退路径。

## 替代方案

仅保存摘要、纯向量数据库。

## 验证

关联 [[06-Research/Experiment-Program]] 和 [[07-Delivery/Testing-Strategy]] 中对应实验。
