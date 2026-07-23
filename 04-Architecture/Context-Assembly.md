---
title: "上下文组装架构"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - architecture
  - context
---


# 上下文组装架构

## ContextPacket

```yaml
situation: 当前情境和待决策问题
observations: 本次窗口事件
recent_history: 近期必要交互
persona_constraints: 角色定义片段
runtime_state: 当前运行状态
relationship_context: 关系事实与边界
memories: 带来源的召回结果
commitments: 未完成任务和承诺
environment: 时间、平台和可用状态
capabilities: 本次可用能力摘要
policies: 安全、隐私和用户设置
provenance_manifest: 每块来源与注入理由
budget_report: token 分配与舍弃信息
```

## Provider 模式

上下文编排器从只读 Provider 获取候选块，执行：

- 作用域和权限过滤；
- 相关性评分；
- 冲突检测；
- 去重和压缩；
- Token 预算分配；
- 模型能力适配；
- 来源清单生成。

## 防止超级模块

Provider 负责领域查询，Orchestrator 只负责编排。它不得直接依赖所有数据库表，也不得在读取过程中更新访问次数之外的长期业务状态；即使记录访问，也应异步事件化。

## 上下文稳定性

为保持 KV Cache 和调试能力，稳定规则、角色定义和工具摘要应采用固定顺序；动态记忆和观察放在后部，并记录版本和哈希。
