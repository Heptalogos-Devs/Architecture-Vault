---
title: "研究地图"
status: active
type: moc
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - moc
  - research
---


# 研究地图

## 从目标到实验

| 研究目标 | 需要证明的能力 | 主要变量 | 主要实验 |
|---|---|---|---|
| 消息节奏更自然 | 能等待、合并、打断并在适当时机回应 | debounce、触发门、群聊密度 | [[06-Research/Experiment-Program#E1 消息窗口与时机]] |
| 角色长期一致 | 行为不因单轮 Prompt 漂移 | 状态模型、约束层、表达层 | [[06-Research/Experiment-Program#E2 行为与表达分离]] |
| 记忆准确且自然 | 相关记忆能出现，错误记忆可修正 | 检索、证据、合并、衰减 | [[06-Research/Experiment-Program#E3 记忆生命周期]] |
| 关系具有连续性 | 对不同用户产生合理差异且不过度拟合 | 关系维度、更新速率、作用域 | [[06-Research/Experiment-Program#E4 关系状态]] |
| 主动行为可接受 | 有价值、可解释、不会形成骚扰 | 触发、预算、静默时段 | [[06-Research/Experiment-Program#E5 主动行为]] |
| 工具不破坏角色 | 能力执行正确且表达保持连续 | 能力选择、异步结果、风险策略 | [[06-Research/Experiment-Program#E6 工具与角色连续性]] |

## 研究资料层级

1. **内部权威信息**：[[10-Sources/Internal-Project-Description]]
2. **当前原型证据**：[[06-Research/BionicBot-and-QQContextBot-Lessons]]
3. **外部参考机制**：[[06-Research/Reference-Projects-Comparative-Study]]
4. **设计推导**：需求、领域模型、架构和组件规格
5. **验证结果**：实验报告、回放数据与 ADR

> [!important]
> 参考项目只证明某些机制可以实现或暴露某些风险，不证明其架构适合 Heptalogos。
