---
title: "ADR-0013 Central AI Validation Workflow"
status: accepted
type: adr
confidentiality: internal
created: 2026-07-25
updated: 2026-07-25
tags:
  - reactor
  - langgraph
  - validation
---

# ADR-0013 Central AI Validation Workflow

## 状态

`accepted`

## 决策

新增独立 workspace 包 `heptalogos-reactor`，以 LangGraph 验证中央
`Feed -> model -> Intent` 闭环。它只使用 Interaction 公开 Feed/Intent 门面，使用
独立 SQLite 保存可恢复模型结果和短会话。

该包是最终 Reactor 之前的流程验证，不引入工具、画像、视觉、长期记忆或自主决策。
模型供应商通过 OpenAI-compatible 配置隔离。

## 边界与后果

- Interaction 不依赖 LangChain；Reactor 依赖 Interaction 公共契约。
- 模型结果先持久化，随后提交确定性 Intent，避免崩溃后重复计费和发送。
- outbound 和未触发消息必须确认但不调用模型。
- 本次从 ADR-0012 的单代码包部署选择中拆出实验 Reactor 包，但仍是同仓库、本机
  SQLite 和启动器监督，不建立网络微服务或新的平台权威。
- 最终 Reactor 架构仍需基于验证证据另行决策。
