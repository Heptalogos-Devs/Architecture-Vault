---
title: "内部项目完整描述"
status: confirmed
type: source
confidentiality: restricted
created: 2026-07-23
updated: 2026-07-23
tags:
  - source
  - internal
---


# 内部项目完整描述

> [!danger] Restricted
> 本文是内部权威描述的镜像，不能自动用于公开 README、演示或外部设计说明。

<div align="center">

# Heptalogos Devs

**Researching human-like interaction systems for instant messaging platforms.**

面向 IM 平台的 AI 拟人化交互系统研究与原型开发。

</div>

---

## About

Heptalogos Devs 是一个由学生组成的早期研发团队，主要研究如何让 AI 在即时通信环境中表现出更稳定、连续且具有个体差异的交互行为。

我们的目标不是简单地为大语言模型增加角色提示词，而是构建一套适用于 IM 场景的完整运行系统，使 AI 能够处理长期关系、上下文变化、消息节奏、主动行为与个性一致性。

项目目前处于研究和原型开发阶段，相关仓库主要用于团队内部协作、架构验证与实验实现。

## Research Areas

### Persona Runtime

构建独立于单次提示词的角色运行时，统一管理：

* 人格设定与行为约束
* 当前情绪和内部状态
* 用户关系与交互边界
* 对话风格与表达习惯
* 长期行为一致性

### Long-term Memory

研究多层次长期记忆系统，包括：

* 工作记忆与当前会话状态
* 情节记忆与关键事件
* 用户画像与关系记忆
* 语义知识与事实记录
* 记忆提取、衰减、合并与修正

记忆不会被简单地作为全部上下文直接注入，而是根据当前消息、关系状态和任务需要动态检索。

### Reactive Message Processing

面向真实 IM 环境设计反应式消息处理器，用于处理：

* 连续发送的多条消息
* 消息合并与延迟响应
* 引用、撤回、回复和表情反应
* 群聊与私聊中的上下文差异
* 消息优先级与打断机制
* 主动消息与非即时响应

### Agent and Tool Integration

探索人格系统与外部能力的协同方式，包括：

* 工具调用
* 工作流执行
* 搜索与知识检索
* 日程与提醒
* 多代理协作
* 平台适配与事件分发

工具能力应服务于角色行为，而不是破坏角色连续性。

### Evaluation

研究适用于拟人化 IM 系统的评估方法，例如：

* 人格一致性
* 长期记忆准确性
* 情绪与关系连续性
* 消息时机合理性
* 主动行为可控性
* 对不同用户的差异化响应

## System Direction

当前系统方向可以概括为：

```text
IM Platform
    │
    ▼
Event Adapter
    │
    ▼
Reactive Message Processor
    │
    ├── Context Builder
    ├── Memory Retrieval
    ├── Persona Runtime
    ├── State Management
    ├── Tool / Agent Router
    └── Response Scheduler
    │
    ▼
Message Output
```

系统采用模块化设计，尽量降低 IM 平台、模型供应商、记忆实现与人格逻辑之间的耦合。

## Current Stage

项目目前重点包括：

* 明确整体系统架构
* 实现最小可用原型
* 验证多层次记忆方案
* 设计反应式消息处理流程
* 建立人格状态和关系状态模型
* 适配不同 IM 平台与模型接口
* 构建可复现的测试与评估方法

现阶段不承诺生产可用性、稳定 API 或向后兼容性。

## Engineering Principles

* **State over prompt**
  将人格和关系视为持续状态，而不是一次性提示词。

* **Event-driven processing**
  以消息事件为基本输入，而不是仅处理完整对话轮次。

* **Memory with provenance**
  记录记忆来源、时间、置信度与更新过程。

* **Controlled autonomy**
  主动行为必须可配置、可解释并受明确边界约束。

* **Platform independence**
  核心逻辑不依赖特定 IM 平台或模型服务。

* **Incremental development**
  优先验证关键假设，避免在早期构建过度复杂的系统。

## Repositories

部分研发仓库可能在早期阶段保持私有。

公开仓库将在具备基本可用性、文档和维护条件后逐步发布。

## Status

> Early-stage research and prototyping.

系统架构、接口和实现方案仍可能发生较大变化，不建议依赖当前代码构建生产服务。

---

<div align="center">

**Heptalogos Devs**

Human-like AI interaction for instant messaging.

</div>
