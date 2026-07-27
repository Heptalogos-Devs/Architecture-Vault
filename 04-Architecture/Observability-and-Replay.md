---
title: "可观测性与回放"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - architecture
  - observability
  - replay
---


# 可观测性与回放

## Trace 层级

- `event_trace`：事件接收、规范化和投影；
- `decision_trace`：窗口、唤醒、上下文和行为；
- `inference_trace`：模型、Prompt、Token、延迟和结构验证；
- `capability_trace`：工具参数、权限、执行和结果；
- `delivery_trace`：计划、取消、发送、重试和回执。

## 回放模式

### Deterministic Replay

使用已保存的模型与工具结果，验证状态和编排逻辑。

### Model Replay

固定事件和系统版本，重新调用模型比较行为变化。

### Counterfactual Replay

改变一个策略、上下文 Provider 或模型，比较结果。

### Shadow Replay

真实事件不发送输出，仅运行候选系统并与当前系统对比。

## 虚拟时钟

所有时间依赖都通过 Clock 端口。测试可推进时间，验证等待、过期、安静时段和承诺。

## 用户解释

系统可生成简短解释：“因为你引用了我之前的消息并补充了信息，所以我等待后一起回复。”这不是隐藏推理链，而是由结构化决策原因生成。

## Interaction Gateway 最小可观测闭环

- Evidence count/latest cursor 证明 Adapter 实际入账，而非只证明 LLBot 在运行。
- 每来源 Fusion cursor 证明 raw 已被中央事务处理。
- Canonical、filtered、opaque/diagnostic 数量解释 evidence 去向。
- Feed consumer checkpoint 证明 Reactor 已确认到哪个 ordinal。
- heartbeat 证明实例近期健康，但不能代替数据 cursor。
- recovery job 的 pages/messages/gap 证明重连补偿覆盖范围。
- Delivery 的 request/response evidence 与 Outcome 形成外部副作用对账链。
- Asset attempt、error、sha256 和 path 证明媒体是否真正归档。

在线探针应使用唯一文本标记：目标会话要求 evidence 与 canonical/feed 同时增长；
非目标控制会话只允许 evidence 增长。该方法避免把历史存量误判为当前采集成功。
