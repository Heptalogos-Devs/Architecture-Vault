---
title: "故障模式与恢复"
status: active
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - architecture
  - failure
  - recovery
---


# 故障模式与恢复

| 故障 | 危险结果 | 恢复策略 |
|---|---|---|
| 重复平台事件 | 重复状态与回复 | 幂等键、事件去重 |
| 事件先处理后落库 | 崩溃后无法回放 | 先提交事实再副作用 |
| 模型超时 | Mailbox 阻塞 | 超时、取消、降级等待 |
| 工具完成但回调丢失 | 用户认为未完成或重复执行 | 持久任务、幂等查询、结果事件 |
| 发送成功但回执丢失 | 重试导致重复消息 | 平台消息 ID、幂等 Outbox、对账 |
| 状态投影损坏 | 行为基于错误状态 | 从事件重建、快照校验 |
| 向量索引损坏 | 记忆召回缺失 | 索引视为可重建派生物 |
| Prompt/schema 不兼容 | 结构输出失败 | 版本匹配、验证和回滚 |
| 平台禁言或断线 | 已计划动作堆积 | 能力状态事件、暂停与过期 |
| 用户删除数据 | 派生索引仍残留 | 删除编排与墓碑事件 |
| 高流量群聊 | 推理风暴 | 背压、聚合、限额、降级静默 |
| 关系/记忆反馈环 | 错误长期强化 | 证据分级、人工纠正、回放检测 |
| Adapter UI 运行但采集进程退出 | 长期静默缺数 | heartbeat、status、前台监督与唯一标记探针 |
| 历史 API 无法覆盖 checkpoint | 误以为重连已补全 | 有界恢复、`gap` 状态和 diagnostic |
| Evidence 已写但 Fusion 崩溃 | 派生暂时缺失 | cursor 不推进，重启后幂等重读 |
| 媒体 URL 失效或下载中断 | 文本事实被媒体阻塞 | 先提交消息，持久 attempt/error，独立重试 |

## 安全默认

- 每个 Adapter Instance 使用独立 heartbeat、lease 和恢复状态；一个来源失败不阻塞
  其他来源的 Fusion。
- Fusion cursor 只在 Canonical 事务提交后推进。
- Delivery Plan 在 request evidence 前崩溃可以重新领取；request evidence 后缺少
  terminal response 时进入 `uncertain`，不得自动重试。
- 跨 Evidence/Gateway 数据库不假设原子事务，以稳定 ID、reconciliation 和
  append-only evidence 恢复。

在无法确定是否应发送时，优先等待或静默；在无法确定工具是否成功时，优先报告未确认；在无法确定数据作用域时，优先不注入。

## 完整性声明

“进程在运行”不等于“目标数据完整”。运行验收必须同时检查 Evidence 最新 cursor、
Fusion source cursor、目标 canonical/feed 增量、heartbeat、history gap 和 asset
状态。任何 gap diagnostic 都必须进入观察报告，不能用后续 healthy heartbeat 覆盖。
