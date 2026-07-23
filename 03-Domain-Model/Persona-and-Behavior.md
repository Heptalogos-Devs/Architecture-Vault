---
title: "角色与行为模型"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - domain
  - persona
  - behavior
---


# 角色与行为模型

## 三层分离

### 角色定义

描述长期规范：“是谁、重视什么、不能做什么”。

### 行为策略

根据情境和状态决定：“现在做什么”。

### 表达实现

把行为意图变成：“具体怎么说或怎么表现”。

## BehaviorIntent 候选结构

```yaml
behavior_id: uuid
act: wait | silence | react | reply | ask | tool | notify | cancel
social_target: identity-or-group
purpose: string
stance: concise structured fields
urgency: low | normal | high
expected_value: number?
interruption_cost: number?
allowed_capabilities: []
constraints: []
reason_summary: string
expires_at: datetime?
```

## 为什么分离

- 可以单独评估“是否应该回应”和“回应写得如何”；
- 更换表达模型不改变行为策略；
- 工具执行失败后可保持同一行为目标重新规划；
- 可检测文本是否背离已决定的边界。

## 行为不变量

- 不得以表达风格推断长期人格变化；
- 不得在没有证据时声称关系、记忆或工具结果；
- 沉默和等待必须有终止条件；
- 行为意图过期后不得继续执行。
