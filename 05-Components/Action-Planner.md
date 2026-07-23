---
title: "行动规划器"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - action-planner
---

# 行动规划器

## 目的

把行为意图转成工具、等待、表达和发送等可执行步骤。

## 输入

- BehaviorIntent
- 能力候选
- 当前任务状态

## 输出

- ActionPlan
- CapabilityRequest
- 等待条件

## 数据所有权

- 步骤依赖、预算、终止和补偿策略

## 不变量

- 未完成工具不能标记成功
- 每步有终止条件
- 副作用步骤幂等

## 典型故障

- 循环调用
- 工具粒度不匹配
- 异步结果无归属

## 关键指标

- 计划完成率
- 平均步骤
- 重规划率
- 无效工具调用率

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 规划是否需要专用模型
- 何时使用工作流而非开放式 Agent

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
