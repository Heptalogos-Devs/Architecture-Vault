---
title: "系统级原则与演进建议"
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

# 系统级原则与演进建议

- **状态**：Concept
- **主题**：跨模块设计原则、优先级与后续 ADR 方向

## 1. 系统级原则

### 1.1 只有一个主体

所有模块共同维护一个持续主体，而不是形成多个并行人格。

### 1.2 事实与主观解释分离

```text
事实：对方发来了一句话。
解释：主体认为对方在生气。
```

二者必须使用不同来源和可信度。

### 1.3 人格与情绪分离

人格长期稳定；情绪短期波动。  
情绪不能轻易重写人格。

### 1.4 记忆与原始记录分离

原始事件保留客观记录；记忆允许压缩、遗忘和主观重构。

### 1.5 梦与现实分离

梦可以影响感受和联想，但不能升级为客观证据。

### 1.6 基础模型能力与主体知识分离

模型知道什么，不代表主体知道什么。

### 1.7 计划、经历和声明分离

原计划、实际发生和对外说法不应存为同一类数据。

### 1.8 接收与认知分离

Interaction 并发接收世界事件；Reactor 全局串行处理认知任务。

### 1.9 认知与行为执行分离

形成“想回复”的决定，与真正通过 IM 发送消息，是两个不同阶段。

### 1.10 状态变化可追溯

系统应能够说明：

- 为什么情绪改变；
- 为什么关系改变；
- 为什么形成某条记忆；
- 为什么没有回复；
- 为什么产生某个生活事件；
- 为什么某段内容被判定为知识越界。

## 2. 建议的总体分层

### 2.1 事实层

- Interaction Evidence；
- Canonical Events；
- Delivery Outcomes；
- Clock Events；
- Planned Schedule；
- Lived Timeline。

### 2.2 主体状态层

- Core Identity；
- Emotional State；
- Epistemic State；
- Social Relations；
- Goals；
- Attention；
- Current Activity。

### 2.3 主观认知层

- Episodic Memory；
- Semantic Memory；
- Autobiographical Memory；
- Beliefs；
- Diary；
- Dreams；
- Self-Narrative。

### 2.4 认知执行层

- Appraisal；
- Recall；
- Knowledge Boundary；
- Reality Review；
- Deliberation；
- Cognitive Commit。

### 2.5 外部行为层

- CommunicationIntent；
- Delay；
- Reply；
- Ignore；
- Defer；
- Proactive Action。

## 3. 推荐的演进顺序

### 阶段一：持续性基础

优先建立：

- 全局串行 Reactor；
- 持久 Feed；
- 单一 active conversation；
- 基础身份；
- 基础日程和活动状态；
- 基础关系记录；
- 事实事件与回复记录。

### 阶段二：一致性

增加：

- 生活时间线；
- 自我陈述账本；
- 回复前现实审查；
- 简单知识领域限制；
- 基础情绪状态；
- 相关记忆召回。

### 阶段三：主观性

增加：

- 关系动态；
- 自传记忆；
- 日记；
- 自我叙事；
- 未完成目标；
- 情绪衰减与事件评价。

### 阶段四：高级离线认知

增加：

- 梦；
- 非平凡联想；
- 长期人格缓慢演化；
- 更复杂的遗忘和记忆重构；
- 可中断注意力；
- 主动行为。

## 4. 应避免的过早复杂化

早期不宜优先投入：

- 多 Agent；
- 分布式认知；
- 每会话并发 Worker；
- 复杂向量基础设施；
- 高精度心理学参数；
- 大规模工具生态；
- 让每个模块各自直接调用模型并修改状态。

这些能力可能增加复杂度，却不一定增强“同一个主体持续存在”的核心体验。

## 5. 后续 ADR 建议

后续可以分别形成 ADR：

1. Agent State Snapshot 与统一提交；
2. Planned Schedule 与 Lived Timeline 分离；
3. Self-Narrative Ledger；
4. Epistemic State 与知识越界审查；
5. Memory Taxonomy 与召回策略；
6. Diary 作为主观记忆；
7. Dream 内容的非事实隔离；
8. Attention Scheduler 与可中断串行；
9. 事实、信念、声明与想象的来源模型；
10. 行为规划与自然语言实现分离。

## 6. 衡量标准

未来设计应优先衡量：

- 主体连续性；
- 跨时间一致性；
- 跨会话一致性；
- 人格稳定性；
- 关系差异性；
- 知识表现是否符合角色；
- 生活事实是否能够持续；
- 行为是否具有可解释原因。

吞吐量和即时响应速度不是首要指标。

## 7. 总结

整个系统的关键不是让 AI “表现得更像人”，而是让它真正拥有一套持续、受约束、可追溯的内部世界。

拟人化语言只是结果。  
持续身份、主观时间、关系、知识边界、记忆和生活连续性才是基础。
