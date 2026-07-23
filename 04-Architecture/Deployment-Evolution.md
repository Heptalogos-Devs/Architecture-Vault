---
title: "部署演化路径"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - architecture
  - deployment
  - evolution
---


# 部署演化路径

## 阶段 A：单机研究运行时

Python 运行时、薄平台适配器、SQLite、本地媒体、进程内 Mailbox、DB 调度表；TypeScript 仅用于需要时的控制面。目标是回放、实验和领域边界。

## 阶段 B：多工作器

将媒体、Embedding、长任务和投递工作器独立运行，共享 PostgreSQL/对象存储。核心决策仍保持单一运行时或按 Agent 分片。

## 阶段 C：多实例与高可用

引入分布式租约、事件通知和外部队列。此时才评估 NATS、Kafka 或 Redis Streams。

## 阶段 D：能力节点与多地域

将 GPU、浏览器、设备控制和特定平台适配部署为能力节点。核心仍通过 CapabilityDescriptor 和结果事件交互。

## 拆分判据

- 资源隔离显著；
- 故障域需要隔离；
- 安全权限不同；
- 独立伸缩需求稳定；
- 团队所有权清晰；
- 接口已经通过单体内实践稳定。

## 语言与协议约束

- 新语言不得单独构成拆分理由，遵循 [[08-ADR/ADR-0009-Programming-Language-and-Runtime-Policy]]。
- 外部协议实现与运行时通过 RawPlatformEvent、Canonical Interaction Event、PlatformAction 和 CapabilityDescriptor 交互。
- LLBot + Milky 必须保持可替换边缘进程，不与认知运行时共享领域类型或生命周期。
