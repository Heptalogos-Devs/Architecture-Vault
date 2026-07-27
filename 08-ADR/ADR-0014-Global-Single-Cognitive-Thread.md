---
title: "ADR-0014：Central Reactor 采用全局单线程认知模型"
status: proposed
type: concept
confidentiality: internal
created: 2026-07-27
updated: 2026-07-27
tags:
  - concept
  - heptalogos
---

> 本文档由概念归档整理并纳入 Architecture Vault，作为长期设计与研究材料。

# ADR-0014：Central Reactor 采用全局单线程认知模型

- **状态**：Accepted
- **日期**：2026-07-27
- **决策范围**：Reactor、Attention、未来人格与认知系统

## 背景

Heptalogos 的目标不是高吞吐量客服机器人，也不是“每个会话一个 Agent”的多会话自动回复平台。

系统要模拟的是一个真实主体操作 IM 平台：

- 多个平台和联系人可以同时发来消息；
- 主体一次只能真正关注和处理一个认知任务；
- 其他消息可以继续到达并积压；
- 主体会在会话之间切换注意力，而不是并行思考。

因此，需要决定 Reactor 应采用每会话并发 Worker，还是保持全局串行。

## 决策

Central Reactor 采用：

```text
Global Single Cognitive Thread
```

即：

> 任意时刻只允许一个 Active Cognitive Task。

系统允许多个会话同时产生待处理事件，但不允许多个独立模型推理流程同时代表同一主体进行认知和决策。

## 架构含义

### Interaction

Interaction 继续支持：

- 多协议；
- 多连接；
- 并发接收；
- 持续保存；
- Feed 积压。

### Reactor

Reactor 负责：

```text
Feed
  ↓
Attention Scheduler
  ↓
选择一个当前认知对象
  ↓
理解、召回、判断和行为规划
  ↓
CommunicationIntent
```

整个过程保持全局串行。

## 理由

### 符合产品目标

真人可以同时收到多条消息，但不能同时认真处理多个独立会话。

### 保证全局状态唯一

未来系统只有一份：

- 情绪；
- 注意力；
- 工作记忆；
- 当前活动；
- 自我叙事；
- 当前目标。

并发推理会导致这些状态出现语义冲突。

### 保持一个主体

Heptalogos 的目标不是让每个聊天窗口拥有一个 AI，而是让一个主体在多个聊天窗口之间切换注意力。

## 不代表什么

全局串行不意味着：

- Interaction 只能接收一条消息；
- Feed 不能积压；
- 所有消息必须严格 FIFO；
- 主体不能被高优先级事件打断。

## 注意力调度

未来应引入 Attention Scheduler。  
其职责不是提高并发，而是决定下一步处理哪个会话。

可能考虑：

- 联系人优先级；
- 是否被点名；
- 紧急程度；
- 当前会话连续性；
- 连续追问；
- 未完成承诺；
- 当前活动；
- 情绪和精力。

每次仍只选择一个认知对象。

## 可中断串行

允许：

```text
处理 A
  ↓
保存未完成状态
  ↓
切换到高优先级 B
  ↓
处理 B
  ↓
恢复 A
```

这属于可中断串行，不属于并发认知。

## 后果

### 优点

- 符合真人注意力模型；
- 全局状态天然一致；
- 行为更容易解释；
- 适合作为持续数字人格；
- 避免多个推理流程争夺同一主体状态。

### 缺点

- 吞吐量有限；
- 回复可能积压；
- 不适合高流量客服场景；
- 需要专门处理优先级、打断和恢复。

这些缺点属于产品定位的自然结果，而不是架构缺陷。

## 后续工作

后续 ADR 应进一步定义：

- Attention Scheduler；
- Agent State Snapshot；
- Conversation Switching；
- Interrupt 与 Resume；
- Human-like Delay；
- Draft 与未完成认知状态；
- Cognitive Commit。

## 结论

Heptalogos 始终只有一个中央认知体。

Interaction 并发接收世界发生的事件；  
Reactor 以全局单线程方式，在这些事件之间分配唯一注意力，并形成持续一致的主体行为。
