# Open Questions

这里只列仍会影响设计或实验的问题。已有明确当前选择的内容应进入主题文档或 Decision。

## 认知运行

- 全局注意力何时允许抢占当前 Job？
- 初期是否足够使用不可抢占的短认知事务？
- Situation Interpretation、Appraisal 和 Behavior Decision 应合并到几次模型调用？
- 结构化输出失败时的保守降级是什么？

## 状态与身份

- Core Identity 的最小结构化字段是什么？
- Living State 中哪些维度真正影响行为，哪些只是伪精确装饰？
- 一个部署是否永远只维护一个主体，还是需要主体分区？

## 记忆与关系

- 哪类明确事实允许自动激活？
- 情节记忆如何分段和合并？
- 关系状态应保存哪些客观证据、统计和主观解释？
- 如何测试“自然召回”而不鼓励过度个性化？

## 时间与生活

- Planned Schedule、Lived Timeline 和 Claim Ledger 的最小事件集合是什么？
- 主体“睡觉、上课、考试”等活动如何开始、结束和被纠正？
- 错过的提醒在恢复后应发送、延后还是过期？

## 能力与安全

- MCP、Skill、工作流和原生工具需要多统一的 Capability 模型？
- 哪些风险等级必须人工确认？
- Python / Rust Worker 采用 stdio、本地 socket 还是持久队列？
- 如何限制子 Agent 的上下文和凭据，同时保留有效研究能力？

## 语言与迁移

- ~~TypeScript 在线运行时从哪个完整切片开始实现？~~ 已完成：全部切片已迁移。
- ~~当前 Python Gateway 是否先保留为独立边缘，还是与 Cognitive Kernel 一同迁移？~~ 已完成：Gateway 已迁移为 TypeScript。
- 如何用相同场景比较原 Python 实现与 TypeScript 实现？

## 产品与评估

- 用户如何查看和纠正记忆、关系与自我陈述？
- 哪些解释适合用户可见，哪些只用于内部 Trace？
- 长期影子实验需要多少真实场景和持续时间？
- 拟人化增益与打扰、隐私和成本如何共同评价？
