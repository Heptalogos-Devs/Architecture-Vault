---
title: "持久化与数据拓扑"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
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

## Interaction Gateway 数据权威

- 每个 Adapter Instance 使用独立 Evidence SQLite，保存原始收发和 transport。
- Gateway SQLite 保存 source cursor、Canonical、provenance、Reactor Feed、
  consumer checkpoint、Intent、Plan、lease 和 Outcome。
- 跨库不假设分布式事务；使用稳定 ID、持久 cursor、lease 和 reconciliation。
- 旧 Edge 数据库只读封存，通过 raw replay importer 进入新数据产品。

### 物理边界与恢复依据

| 物理存储 | 权威内容 | 恢复依据 |
|---|---|---|
| 每实例 Evidence SQLite | raw bytes、session/sequence、API、history job/checkpoint | append order、checksum、pending job |
| Gateway SQLite | cursor、canonical/provenance、Feed、Intent、Plan/lease、Outcome、asset metadata | 单库事务、稳定 ID、reconciliation |
| 本地 CAS | 媒体和文件 bytes | SHA-256、size、asset attempt |

Evidence 与 Gateway 使用不同 schema identity 和独立、连续、带 checksum 的 migration。
直接复制正在运行的 SQLite 文件不构成备份；运维命令使用 SQLite snapshot 并生成 hash
清单。

### 一致性不是“所有东西一张表”

入站跨库窗口允许 Evidence 已存在而 Gateway cursor 尚未推进，下次 Fusion 会重读。
出站跨越数据库和外部平台，只有 request 前的 lease 可安全重领；request 后无 response
必须标记 `uncertain`。这种显式不一致比试图用本地事务掩盖外部副作用更可靠。
