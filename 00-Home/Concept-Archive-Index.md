---
title: "Heptalogos 概念归档索引"
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

# Heptalogos 人工主体系统设想归档

- **状态**：Concept Archive
- **整理日期**：2026-07-27
- **用途**：记录 Heptalogos 未来人格反应、时间、关系、记忆、知识边界与叙事连续性系统的设计设想
- **定位**：以产品目标、概念边界和长期架构原则为主；具体实现仅作简要参考

## 文档索引

1. [01-人工主体愿景与总体模型](../03-Domain-Model/Artificial-Subject-Vision.md)
2. [02-核心人格、动态状态与统一主体](../03-Domain-Model/Core-Identity-and-Living-State.md)
3. [03-虚拟时间、情绪与注意力](../04-Architecture/Time-Emotion-and-Attention.md)
4. [04-社交关系、记忆、日记与梦](../03-Domain-Model/Social-Memory-Diary-and-Dream.md)
5. [05-认知领域与知识边界](../03-Domain-Model/Epistemic-Model-and-Knowledge-Boundaries.md)
6. [06-生活时间线与叙事现实提交](../04-Architecture/Lived-Timeline-and-Narrative-Commit.md)
7. [07-系统级原则与演进建议](../04-Architecture/System-Principles-and-Roadmap.md)
8. [ADR-0014：Central Reactor 采用全局单线程认知模型](../08-ADR/ADR-0014-Global-Single-Cognitive-Thread.md)

## 总体结论

Heptalogos 不应被定义为一个“按消息生成回复的聊天机器人”，而应被定义为：

> 一个拥有持续身份、主观时间、社会关系、情绪、知识边界、自传记忆与生活连续性，并通过 IM 平台同外部世界发生联系的人工主体。

基础模型提供广泛的潜在认知能力，但不能直接决定主体是谁、知道什么、经历过什么、正在做什么，或将如何对待不同的人。上述内容必须由持久状态、时间线和统一认知过程共同约束。

## 阅读顺序

首次阅读建议依次阅读 01、02、03、04、05、06、07。  
ADR-0014 单独记录“全局唯一认知线程”这一基础架构决策，可直接归入 ADR 目录。
