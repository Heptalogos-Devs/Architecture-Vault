---
title: "响应调度与 Outbox"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - component
  - response-scheduler-and-outbox
---

# 响应调度与 Outbox

## 目的

持久化、延迟、取消和可靠投递 ActionPlan。

## 输入

- ActionPlan
- 新事件取消信号
- 平台能力状态

## 输出

- OutboxRecord
- DeliveryCommand
- 过期/取消事件
- CommunicationIntent、DeliveryPlan 与 DeliveryOutcome

## 数据所有权

- 时机、分段、顺序、重试和幂等

## 不变量

- 发送前可取消
- 过期动作不发送
- 同一幂等键至多一个业务结果
- Intent 先于 Plan，Plan 先于平台 request evidence
- `uncertain` 是终止自动重试的可对账状态

## 典型故障

- 发送成功回执丢失
- 重启后重复发送
- 延迟动作语义过期

## 关键指标

- 端到端延迟
- 取消率
- 重复率
- 投递成功率
- 过期率

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 打字延迟模型
- 跨平台发送顺序与并发

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
