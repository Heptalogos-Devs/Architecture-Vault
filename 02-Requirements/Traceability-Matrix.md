---
title: "需求追踪矩阵"
status: active
type: requirements
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - requirements
  - traceability
---

# 需求追踪矩阵

| 领域 | 需求 ID | 主要组件 | 主要实验 |
|---|---|---|---|
| EVT | EVT-001, EVT-002, EVT-003, EVT-004, EVT-005 | [[05-Components/Event-Normalizer|事件规范化器]], [[05-Components/State-Projection|状态投影器]], [[05-Components/Evaluation-Harness|评估 Harness]] | E7 |
| IDN | IDN-001, IDN-002, IDN-003 | [[05-Components/Platform-Adapter|平台适配器]], [[05-Components/Event-Normalizer|事件规范化器]], [[05-Components/State-Projection|状态投影器]] | E7 |
| CNV | CNV-001, CNV-002, CNV-003, CNV-004, CNV-005 | [[05-Components/Conversation-Mailbox|会话 Mailbox]], [[05-Components/Wakeup-and-Response-Decision|唤醒与回应决策]], [[05-Components/Response-Scheduler-and-Outbox|响应调度与 Outbox]] | E1 |
| STA | STA-001, STA-002, STA-003, STA-004 | [[05-Components/State-Projection|状态投影器]], [[05-Components/Context-Builder|上下文构建器]] | E2/E4 |
| PER | PER-001, PER-002, PER-003 | [[05-Components/Behavior-Policy|行为策略]], [[05-Components/Context-Builder|上下文构建器]] | E2 |
| REL | REL-001, REL-002, REL-003 | [[05-Components/State-Projection|状态投影器]], [[05-Components/Memory-Lifecycle|记忆生命周期系统]], [[05-Components/Behavior-Policy|行为策略]] | E4 |
| MEM | MEM-001, MEM-002, MEM-003, MEM-004, MEM-005, MEM-006, MEM-007 | [[05-Components/Memory-Lifecycle|记忆生命周期系统]], [[05-Components/Context-Builder|上下文构建器]] | E3 |
| CTX | CTX-001, CTX-002, CTX-003, CTX-004 | [[05-Components/Context-Builder|上下文构建器]], [[05-Components/Behavior-Policy|行为策略]] | E2/E3 |
| BEH | BEH-001, BEH-002, BEH-003, BEH-004 | [[05-Components/Behavior-Policy|行为策略]], [[05-Components/Action-Planner|行动规划器]] | E2 |
| CAP | CAP-001, CAP-002, CAP-003, CAP-004, CAP-005 | [[05-Components/Capability-Registry-and-Executor|能力注册与执行器]], [[05-Components/Action-Planner|行动规划器]] | E6 |
| SCH | SCH-001, SCH-002, SCH-003 | [[05-Components/Response-Scheduler-and-Outbox|响应调度与 Outbox]], [[05-Components/Wakeup-and-Response-Decision|唤醒与回应决策]] | E5 |
| OUT | OUT-001, OUT-002, OUT-003 | [[05-Components/Response-Scheduler-and-Outbox|响应调度与 Outbox]], [[05-Components/Platform-Adapter|平台适配器]] | E1/E6 |
| OBS | OBS-001, OBS-002, OBS-003 | [[05-Components/Evaluation-Harness|评估 Harness]], [[05-Components/State-Projection|状态投影器]] | E7 |
| EVAL | EVAL-001, EVAL-002, EVAL-003, EVAL-004 | [[05-Components/Evaluation-Harness|评估 Harness]] | E7 |
| GOV | GOV-001, GOV-002, GOV-003 | [[05-Components/State-Projection|状态投影器]], [[05-Components/Memory-Lifecycle|记忆生命周期系统]], [[05-Components/Evaluation-Harness|评估 Harness]] | E3/E7 |

## 使用方式

需求改变时，先检查关联组件、实验、场景和 ADR。组件实现完成但没有场景证据，不视为需求完成。
