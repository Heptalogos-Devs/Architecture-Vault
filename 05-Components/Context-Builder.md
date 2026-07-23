---
title: "上下文构建器"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - context-builder
---

# 上下文构建器

## 目的

按行为需要从多个只读 Provider 组装有来源、预算受控的 ContextPacket。

## 输入

- Situation
- Provider candidates
- InferenceTask limits

## 输出

- ContextPacket
- BudgetReport
- ProvenanceManifest

## 数据所有权

- 候选选择、去重、冲突标记、压缩

## 不变量

- 读路径不写长期状态
- 每个动态块有注入原因
- 作用域先于相关性

## 典型故障

- 上下文过载
- 关键事实遗漏
- 冲突被压平
- Provider 成为隐式依赖

## 关键指标

- Token 构成
- 候选接受率
- 错误注入率
- 上下文构建延迟

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 预算分配算法
- 压缩由规则还是模型完成

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
