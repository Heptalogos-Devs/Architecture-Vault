---
title: "状态投影器"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - state-projection
---

# 状态投影器

## 目的

从事件生成版本化、可查询的 Agent、会话、关系和任务状态。

## 输入

- 领域事件
- 人工修正事件

## 输出

- StateSnapshot
- 版本冲突事件

## 数据所有权

- Reducer
- 快照版本
- 重建和校验

## 不变量

- 确定性 reducer 无模型调用
- 快照可重建
- 敏感级别不降低

## 典型故障

- 投影版本不兼容
- 并发覆盖
- 历史事件缺失

## 关键指标

- 投影延迟
- 重建耗时
- 版本冲突率

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 哪些状态必须事件化
- 快照粒度和归档策略

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
