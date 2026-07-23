---
title: "任务、承诺与自主"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - domain
  - task
  - autonomy
---


# 任务、承诺与自主

## 为什么承诺不是普通记忆

“明天提醒你”要求系统在未来执行动作、处理重启、取消和失败。仅保存一句文本无法保证履行，因此需要持久任务实体。

## Task

```yaml
task_id: uuid
owner_agent_id: id
requester: identity?
conversation_id: id?
type: reminder | monitor | research | workflow | follow_up
status: planned | waiting_confirmation | running | blocked | completed | failed | cancelled | expired
trigger: time-or-event-condition
policy: retry, timeout, notification
source_event_ids: []
result_event_ids: []
```

## Commitment

承诺是具有社会含义的任务约束：谁答应了谁、内容是什么、何时应履行、失败时如何沟通。承诺状态应影响未来行为和关系，但不能自动等于工具任务成功。

## 主动机会

环境事件、到期任务、长期未互动或新信息可以生成 `ProactiveOpportunity`。机会必须经过：

```text
价值评估 → 用户设置 → 安静时段 → 关系边界 → 频率预算 → 行为选择
```

## 自主性层级

- L0：只响应明确消息；
- L1：延迟、等待和取消；
- L2：履行用户明确设置的任务；
- L3：基于承诺和工具结果主动通知；
- L4：基于关系和环境产生建议；
- L5：自主创建长期目标。

早期实验建议止于 L3，L4 需要严格评估，L5 不属于 MVP。
