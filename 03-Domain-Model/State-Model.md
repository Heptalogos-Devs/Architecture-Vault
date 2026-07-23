---
title: "状态模型"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - domain
  - state
---


# 状态模型

## 状态分类

### 角色定义状态

人工维护、低频变化、版本化：身份、价值倾向、行为边界、表达偏好和能力认知。

### Agent 运行状态

短期变化：注意焦点、当前目标、活动水平、社交能量、等待事项、最近干扰。具体维度需要实验，不建议直接采用复杂情绪分类。

### 会话状态

参与者、活跃话题、待处理事件、未回复范围、当前行动、群聊压力和生命周期阶段。

### 关系状态

熟悉、信任边界、称呼、共享经历、互动统计和未完成事项。心理维度必须与事实证据分离。

### 任务状态

计划、执行、等待外部结果、需要确认、完成、失败、取消和过期。

## 状态更新模式

```text
Event → Deterministic Reducer → State Snapshot
      → Optional Interpretation → Proposed State Change
      → Policy Validation → StateChanged Event
```

模型不直接覆盖状态。它可以提出解释或候选更新，最终由策略验证并形成事件。

## 衰减

运行状态可按时间衰减；关系和记忆不能仅依赖统一指数衰减。不同字段需要明确语义，例如互动热度可衰减，已确认称呼偏好不应自然消失。
