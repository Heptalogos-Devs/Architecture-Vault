---
title: "BionicBot 与 QQContextBot 经验"
status: active
type: research
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - research
  - prototype
---


# BionicBot 与 QQContextBot 经验

## BionicBot

当前可见结构验证了：模型调用、回复判断、智能延迟、短长期记忆、摘要、话题线程、群私聊处理都是实际需求。

其主要架构教训是 `ai_client` 容易吸收上下文、记忆、决策、延迟和模型访问等多重责任。继续扩展会使任何行为都无法独立测试。因此应把它视为需求发现和早期行为样本，而不是目标内核。

来源：<https://github.com/Heptalogos-Devs/BionicBot>

## QQContextBot

当前实现将静默记录与 Agent 回复分为两个插件，支持 SQLite 消息结构、媒体归档、转发解析、用户档案、工具循环、Trace 和会话记录。

### 可保留的资产

- 原始消息和消息段的数据模型；
- 合并转发、图片、视频、回复和 @ 的解析经验；
- Agent 工具化加载上下文的实验；
- 发送 Trace、测试和备份实践。

### 不应固化的边界

- Agent 通过跨插件数据库桥接直接读取 recorder；
- 用户档案使用单文件 JSON；
- 上下文主要依赖模型主动工具调用；
- 插件目录承担领域边界。

### 迁移方向

`qq_recorder` 可演化为平台事件采集与历史导入适配器；`grok` 中的工具注册、运行循环和投递经验可拆入能力、推理和 Outbox 实验，但不直接复制插件拓扑。

### QQ 入站证据更新

[[06-Research/EXP-QQ-INGRESS-001-NapCat-OneBot-Raw-Ledger|EXP-QQ-INGRESS-001]] 已将 `qq_recorder` 调整为原始帧先落盘、派生消息后处理的观测基线。历史检查确认固定消息段 allowlist 会遗漏语音、文件和视频段，因此“ORM 中没有结构化段”不能作为“平台未发送”的证据。该结果支持 [[08-ADR/ADR-0010-Platform-Adapter-Boundary-and-Canonical-Interaction-Events|ADR-0010]] 的 raw-first 边界，也为 Milky 对照实验提供同粒度证据。

来源：<https://github.com/Heptalogos-Devs/QQContextBot>
