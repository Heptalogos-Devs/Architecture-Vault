---
title: "需求地图"
status: active
type: moc
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - moc
  - requirements
---


# 需求地图

## 需求文档

- [[02-Requirements/Stakeholders-and-Actors|利益相关者与参与者]]
- [[02-Requirements/Functional-Requirements|功能需求目录]]
- [[02-Requirements/Quality-Attributes|质量属性]]
- [[02-Requirements/IM-Interaction-Scenarios|IM 交互场景]]
- [[02-Requirements/Lifecycle-and-Continuity|生命周期与连续性]]
- [[02-Requirements/Safety-Privacy-Control|安全、隐私与控制]]
- [[02-Requirements/Traceability-Matrix|需求追踪矩阵]]

## 优先级含义

- `P0`：MVP 或架构基础，不满足会导致核心研究失真。
- `P1`：验证完整机制需要，允许在后续垂直切片中实现。
- `P2`：扩展和产品化需求，当前不冻结设计。

## 需求不是模块清单

例如“记忆具有来源”不意味着必须存在名为 `MemoryProvenanceService` 的组件。需求约束系统行为，组件只是当前实现选择。
