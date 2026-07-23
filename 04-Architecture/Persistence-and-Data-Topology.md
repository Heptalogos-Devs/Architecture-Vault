---
title: "持久化与数据拓扑"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - architecture
  - data
  - persistence
---


# 持久化与数据拓扑

## MVP 建议

| 数据 | 初始实现 | 演化条件 |
|---|---|---|
| 事件、状态、关系、任务、Outbox | SQLite WAL | 多进程写入或规模需要时 PostgreSQL |
| 媒体和原始载荷 | 本地内容寻址目录 | 多节点或备份需求时 S3/MinIO |
| 全文检索 | SQLite FTS | 查询规模和语言需求超出时升级 |
| 向量检索 | 可选本地索引 | 证明语义检索有增益后独立化 |
| 队列 | DB 任务表 + 内存通知 | 吞吐或跨节点需要时 NATS/Redis/Kafka |
| Trace | 结构化表与 JSON | 规模需要时 OpenTelemetry 后端 |

## 数据产品

- Event Ledger：不可变事实；
- State Store：当前投影和版本；
- Memory Store：候选、活动、冲突和历史；
- Search Index：可重建派生物；
- Object Store：媒体与原始载荷；
- Task Store：长任务、承诺和调度；
- Outbox：待发送行动；
- Trace Store：研究和诊断轨迹。

## 一致性策略

以事件提交为事务边界。索引、画像和统计允许最终一致；高风险工具和发送使用幂等键及明确终态。
