---
title: "可观测性与回放"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
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
