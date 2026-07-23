---
title: "推理与模型路由"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - architecture
  - inference
  - model-routing
---


# 推理与模型路由

## 任务抽象

业务代码提交 `InferenceTask`，不直接调用供应商 SDK。

```yaml
task_type: wakeup_score | situation | behavior | planning | expression | memory_extract | verify
input_contract: schema
output_contract: schema
latency_budget_ms: int
cost_budget: number
required_capabilities: [tool_call, vision, structured_output]
privacy_class: level
retry_policy: object
trace_context: ids
```

## 模型路由依据

- 任务类型和结构化输出可靠性；
- 上下文长度；
- 延迟与成本预算；
- 视觉、工具和推理能力；
- 数据地域和隐私策略；
- 当前供应商健康状态；
- 评估集上的任务表现。

## 失败策略

- 结构解析失败：修复、重试或切换模型；
- 超时：降级到规则或低成本模型；
- 行为决策失败：优先等待或静默，不应冒险发送；
- 表达失败：可重新生成，但保持同一 BehaviorIntent；
- 工具规划失败：不声称已执行。

## Prompt 作为程序资源

Prompt 需要 ID、版本、输入 schema、输出 schema、支持模型、评估集和变更说明。Prompt 不承担长期状态存储。
