---
title: "唤醒与回应决策"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - wakeup-and-response-decision
---

# 唤醒与回应决策

## 目的

以低成本判断当前观察应行动、等待、静默、取消或暂停。

## 输入

- ObservationBatch
- 会话状态
- 轻量策略与模型

## 输出

- WakeupDecision
- 下一检查时间

## 数据所有权

- 触发门规则
- 回复必要性策略

## 不变量

- 快速路径不依赖主模型
- 静默与故障可区分
- 每个等待有下一检查条件

## 典型故障

- 过早回应
- 永远等待
- 群聊过度参与
- 主模型调用风暴

## 关键指标

- 触发准确率
- 过早回复率
- 漏答率
- 预筛选节省调用数

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 规则和小模型的边界
- 不同会话类型的阈值学习

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
