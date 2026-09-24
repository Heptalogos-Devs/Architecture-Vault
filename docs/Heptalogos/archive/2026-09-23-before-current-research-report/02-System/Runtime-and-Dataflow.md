# 运行时与数据流

## 在线主循环

```text
Platform event
→ raw Evidence
→ Canonical fact
→ Reactor Feed
→ Conversation Mailbox
→ Observation Window
→ Cognitive Job
→ consistent Subject Snapshot
→ situation / retrieval / behavior
→ cognitive commit
→ expression
→ persistent ActionPlan
→ Delivery
→ DeliveryOutcome
→ new fact
```

## 接收与认知分离

平台事件、媒体下载、模型健康检查和只读检索可以并发。主体共享状态的最终提交、对外行为意图和自我陈述必须经过单一 Cognitive Commit Coordinator 或等价的串行保护。

“一个认知提交者”不等于所有代码运行在一个线程，也不等于不能并发调用多个模型。

## Conversation Mailbox

每个会话维护独立的逻辑顺序和待处理状态：

- 追加事件；
- 形成观察窗口；
- 追踪引用、撤回和媒体等待；
- 取消过期行为；
- 防止同一会话双重决策；
- 在重启后从持久记录恢复。

Mailbox 是调度边界，不是新的事实源。

## Observation Window

窗口根据语义完整性、静默间隔、会话类型、引用解析、媒体结果、当前紧迫度和最大期限决定何时关闭。固定 debounce 可以作为回退，但不能成为完整语义。

## Cognitive Job

一次 Job 代表主体对一个观察批次或内部唤醒进行认知。Job 应记录：

- 输入事实引用；
- 优先级和选择理由；
- 预期状态版本；
- 取消和过期条件；
- 模型、成本和时间预算；
- 运行阶段与恢复点。

## 统一认知提交

模型和模块只生成候选。提交阶段负责：

- 乐观版本检查；
- 事实、权限、作用域和叙事审查；
- 状态变化与 ActionPlan 的一致提交；
- 冲突后重新读取并重算；
- 记录结构化 Trace。

## 两阶段生成

推荐在线行为：

```text
结构化认知结果
→ 确定性审查与提交
→ 自然语言表达
→ 输出验证
```

表达模型只能使用已批准的行为、事实和声明，不能自行创造工具成功、关系升级或生活经历。

## 长任务

长工具、深度检索和媒体处理离开认知临界区：

1. 认知提交持久任务；
2. Executor 异步执行；
3. 生命周期和结果进入事实流；
4. 新 Job 决定如何处理和表达结果。

## 停止与恢复

- 所有关键任务都有稳定 ID 和幂等键；
- 取消首先阻止未发生的副作用；
- 已发出但结果未知的外部调用保留 `uncertain`；
- 重启后根据持久状态重领任务，而不是依赖内存队列；
- Clock 必须可替换，以支持虚拟时间和确定性回放。
