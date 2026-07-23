---
title: "事件规范化器"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - event-normalizer
---

# 事件规范化器

## 目的

把平台事实转换为版本化内部事件，并完成去重、时间和内容段基础处理。

## 输入

- RawPlatformEvent
- 平台能力与身份上下文

## 输出

- EventEnvelope
- RawReference
- 规范化诊断

## 数据所有权

- 事件 schema 映射
- 幂等键规则

## 不变量

- 编辑与撤回生成新事件
- 时间字段保留 occurred/observed
- 未知字段可保留扩展

## 典型故障

- 无法解析转发树
- 媒体引用失效
- 平台 ID 不稳定

## 关键指标

- 去重命中率
- 解析失败率
- 未知 segment 比例

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 事件 schema 扩展机制
- 跨平台消息段最小公分母

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
