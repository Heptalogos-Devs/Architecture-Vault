---
title: "能力注册与执行器"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - capability-registry-and-executor
---

# 能力注册与执行器

## 目的

发现、授权并执行工具、工作流、平台动作和子 Agent。

## 输入

- CapabilityRequest
- CapabilityDescriptor
- 确认结果

## 输出

- 执行生命周期事件
- 任务进度与结果

## 数据所有权

- 注册表、权限、执行适配和幂等

## 不变量

- 风险策略不可由模型覆盖
- 结果事件化
- 长任务可恢复或明确失败

## 典型故障

- 权限绕过
- 重复副作用
- 工具提示注入
- 任务失联

## 关键指标

- 成功率
- 确认率
- 超时率
- 幂等冲突
- 工具选择错误率

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- MCP/原生工具/Skill 的统一抽象
- 子 Agent 上下文隔离

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
