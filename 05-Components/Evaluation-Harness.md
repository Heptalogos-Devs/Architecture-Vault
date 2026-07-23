---
title: "评估 Harness"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - evaluation-harness
---

# 评估 Harness

## 目的

通过场景、虚拟时间、回放、消融和模型替换评估整个系统组合。

## 输入

- Scenario
- SystemVersion
- Model/Policy variants

## 输出

- Trace
- MetricReport
- RegressionReport

## 数据所有权

- 环境状态、模拟平台、Judge、数据集版本

## 不变量

- 场景可重置
- 评分规则版本化
- 生产副作用隔离

## 典型故障

- Judge 偏差
- 测试泄漏
- 只测成功场景
- 不可复现的外部工具

## 关键指标

- 覆盖率
- 运行稳定性
- Judge 一致性
- 回归检测时间

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 人工评分采样策略
- 长期仿真用户模型

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
