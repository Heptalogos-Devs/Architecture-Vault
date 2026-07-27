---
title: "信息状态与置信度"
status: active
type: governance
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - governance
  - confidence
---


# 信息状态与置信度

## 信息类型

| 标签 | 定义 | 处理方式 |
|---|---|---|
| `事实` | 内部描述明确声明，或当前代码直接证实 | 可作为约束，但需注意时效 |
| `需求推断` | 从目标和场景推导出的必要能力 | 进入需求评审 |
| `设计建议` | 满足需求的一种候选方案 | 通过 ADR 与实验决定 |
| `研究假设` | 可能带来收益但尚未证实 | 必须定义反证条件 |
| `工作名称` | 为讨论方便暂用的模块或概念名 | 不应绑定公开 API |

## 当前置信度

- **高置信度**：项目处于研究阶段；核心关注状态、记忆、消息处理、能力和评估；需要平台与模型解耦。
- **中置信度**：事件驱动、按会话串行处理、持久化 Outbox、带来源记忆是合适的初始方向。
- **已接受架构边界**：Adapter Evidence、Canonical Interaction、Reactor Feed、
  Outbound Intent 与 Delivery Outcome 分离；第一版为单包多运行角色。
- **代码已验证的当前机制**：每实例 Evidence DB、逐来源事务 cursor、raw-all 与
  derived-allowlist、持久历史恢复、资产 CAS、原端点路由和 request 后
  `uncertain` 语义。
- **低置信度**：具体角色状态维度、记忆分层数量、关系数学模型、多 Agent 拓扑。

`healthy` heartbeat 只证明实例近期完成运行循环，不单独证明数据完整。完整性判断必须
联合 Evidence cursor、Fusion cursor、canonical/feed 增量、recovery gap 和 asset
状态。

## 变更纪律

当发现新证据时，应更新：

```text
来源笔记 → 需求或假设 → 组件影响 → ADR → 测试与回放场景
```
