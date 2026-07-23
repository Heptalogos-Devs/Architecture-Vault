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

平台事件、模型结构输出、CapabilityDescriptor、任务事件和发送回执。平台契约必须覆盖已知/未知事件和消息段、可选/新增字段、超大标识、异常时间、重复、乱序，以及 Python/TypeScript 生成类型的一致性。

## 集成测试

SQLite 事务、Outbox、重启恢复、媒体工作器和索引重建。

QQ 边缘实验额外覆盖：Raw Event 先落盘、LLBot/Milky 版本记录、重连缺口、历史消息尽力补偿、发送超时进入 `uncertain`、能力白名单和多账号身份隔离。

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

## 协议故障与替换

- 在原始落盘后、规范化前，以及规范化后、Mailbox 投递前注入崩溃。
- 注入 WebSocket 断开、协议实现重启、重复/乱序投递、未知字段和发送超时。
- 同一契约套件运行于 Fake Milky Server、LLBot Milky 和另一 Milky 实现；核心测试不得导入 Milky 类型。
- NapCat + OneBot 11 作为对照，比较事件完整性、媒体与引用语义、重连恢复、标识稳定性和升级成本。
