---
title: "事件与事实模型"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - domain
  - event
---


# 事件与事实模型

## 原始事实与规范事实

平台输入分两层保存：

```text
RawPlatformEvent
  platform
  bot_account
  transport
  protocol_version
  observed_at
  raw_payload / blob_reference
  payload_hash
  trace_context
        ↓ normalize
Canonical Interaction Event
        ↓
EventEnvelope
```

RawPlatformEvent 是重新解释、协议升级和诊断的证据；Canonical Interaction Event 是核心运行时唯一接受的平台事实。规范化失败、未知事件或未知消息段不删除原始事实，而是记录诊断和 opaque 扩展。

同一逻辑交互可以关联实时、历史恢复或多个 Adapter Instance 的多个 Evidence
Source。Raw reception 永不合并；Canonical 合并必须依据平台账号、原生会话和稳定
平台消息身份。Reactor Input Feed 是 Canonical Ledger 的可重建投影，不是事实权威。

## 事件最小包络

```yaml
EventEnvelope:
  event_id: uuid
  event_type: string
  schema_version: string
  occurred_at: datetime
  observed_at: datetime
  producer: string
  platform: string?
  platform_account_id: string?
  agent_id: string?
  conversation_id: string?
  actor_identity_id: string?
  causation_id: uuid?
  correlation_id: uuid?
  idempotency_key: string?
  payload: object
  provenance_sources: array
  extensions: object?
  sensitivity: enum
```

## 事件类别

- 平台输入：消息、编辑、撤回、反应、成员、权限、连接。
- 媒体派生：下载、解析、OCR、ASR、视觉分析。
- 推理过程：决策开始、模型响应、验证结果。
- 能力过程：调用请求、确认、执行、进度、结果、失败。
- 状态变化：关系、运行状态、任务和记忆的显式更新。
- 行动过程：计划、调度、取消、发送、回执。
- 治理过程：人工纠正、删除、导入、配置发布。

## 事件与命令

`SendMessageRequested` 是命令；`MessageSendSucceeded` 是事件。不要用过去时命名尚未发生的意图。

## 不变量

- `event_id` 全局唯一；
- 同一幂等键的业务效果唯一；
- 事件写入后内容不修改；
- 更正通过新事件表达；
- 原始平台时间与系统观察时间同时保留；
- 敏感级别不能在派生中自动降低。
- 平台 SDK 和协议 DTO 不得作为 `payload` 的核心契约；
- 每个规范平台事件必须能追溯到 RawPlatformEvent 或明确记录缺失原因；
- 未知平台语义必须可保存、可观察，不以静默丢弃换取统一。
- 进程内事实的嵌套 JSON 必须递归不可变，并与构造时传入的可变容器解耦；
  序列化和协议边界通过显式副本转换，不暴露事实内部引用。

参见 [[08-ADR/ADR-0010-Platform-Adapter-Boundary-and-Canonical-Interaction-Events]]。
双向网关边界见 [[08-ADR/ADR-0012-Canonical-Interaction-Gateway]]。
