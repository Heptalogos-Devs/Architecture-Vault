---
title: "测试策略"
status: active
type: delivery
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - testing
  - delivery
---


# 测试策略

## 单元测试

Reducer、幂等、作用域、状态转换、预算、权限和取消逻辑。

## 契约测试

平台事件、模型结构输出、CapabilityDescriptor、任务事件和发送回执。

## 集成测试

SQLite 事务、Outbox、重启恢复、媒体工作器和索引重建。

## 场景测试

使用模拟平台、虚拟时间和确定工具覆盖 [[06-Research/Scenario-Catalog]]。

## 属性测试

- 重复事件不改变最终状态；
- 事件重排在允许窗口内产生等价投影；
- 删除后敏感数据不再被检索；
- 过期 Action 永不投递；
- 未确认高风险工具永不执行。

## 长期仿真

模拟数周交互，检测记忆累积、关系漂移、主动频率、未履行承诺和反馈环。
