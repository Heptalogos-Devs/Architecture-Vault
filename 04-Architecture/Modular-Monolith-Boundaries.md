---
title: "模块化单体边界"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - architecture
  - modular-monolith
---


# 模块化单体边界

## 推荐模块

| 模块 | 拥有的数据 | 对外提供 |
|---|---|---|
| ingestion | 原始载荷引用、规范化记录 | 标准事件提交 |
| identity | 人物、平台身份、成员关系 | 身份解析 |
| conversation | Mailbox、窗口、会话状态 | 观察批次与唤醒 |
| state | Agent/关系/任务投影 | 版本化状态查询与命令 |
| memory | 记忆及索引 | 候选、检索、修正 |
| cognition | ContextPacket、行为和计划 | BehaviorIntent、ActionPlan |
| capability | 能力描述、任务执行 | 执行结果事件 |
| scheduling | 调度、Outbox | 唤醒和投递任务 |
| delivery | 平台动作执行状态 | 回执事件 |
| evaluation | 场景、Trace、指标 | 回放与报告 |
| control | 配置、治理操作 | 管理 API |

## 模块规则

- 不直接访问其他模块的表；通过接口或只读视图；
- 跨模块写操作使用命令或事件；
- DTO 位于 `contracts`，领域实体不跨模块共享；
- 同进程调用允许，但必须保持边界，避免伪微服务 HTTP；
- 只有被证明需要独立伸缩或隔离时才拆进程。
