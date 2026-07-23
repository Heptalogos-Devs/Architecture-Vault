---
title: "记忆生命周期系统"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - memory-lifecycle
---

# 记忆生命周期系统

## 目的

从事件形成有证据的记忆，并处理检索、合并、冲突、修正和删除。

## 输入

- 事件、情节候选、用户纠正
- MemoryQuery

## 输出

- MemoryCandidate
- MemoryRecord
- RetrievalBundle
- 维护事件

## 数据所有权

- 记忆主存储
- 索引投影
- 提取和维护策略

## 不变量

- 稳定记忆必须有来源
- 候选不等于事实
- 删除传播到索引

## 典型故障

- 错误提取
- 冲突静默覆盖
- 敏感信息越域
- 索引与主存储不一致

## 关键指标

- 记忆精确率/召回率
- 错误召回率
- 冲突处理率
- 纠正生效延迟

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 最小记忆类型
- 情节分割方法
- 访问次数是否影响显著性

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
