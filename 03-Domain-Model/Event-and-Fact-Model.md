---
title: "事件与事实模型"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - domain
  - event
---


# 事件与事实模型

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
  agent_id: string?
  conversation_id: string?
  actor_identity_id: string?
  causation_id: uuid?
  correlation_id: uuid?
  idempotency_key: string?
  payload: object
  raw_reference: object?
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
