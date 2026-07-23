---
title: "行为策略"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - behavior-policy
---

# 行为策略

## 目的

根据情境、角色、状态、关系和边界选择行为类别与社交目标。

## 输入

- ContextPacket
- PolicyVersion

## 输出

- BehaviorIntent
- DecisionReason

## 数据所有权

- 行为候选、约束和选择逻辑

## 不变量

- 不生成最终平台动作
- 安全策略优先
- 行为过期可检测

## 典型故障

- 人格漂移
- 过度回复
- 关系迎合
- 把模型猜测当事实

## 关键指标

- 行为类别准确率
- 一致性
- 静默合理性
- 策略违规率

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 单模型还是规则+模型
- BehaviorIntent schema 的最小字段

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
