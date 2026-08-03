# 近期工作

本页描述目标功能切片，不承诺具体日期。顺序按依赖和研究价值排列。

## 1. 认知基础契约

交付：

- Event Envelope 与 schema version；
- 可替换 Clock；
- Cognitive Job、ObservationBatch、SubjectSnapshot；
- BehaviorIntent、ActionPlan 和 Trace 基础；
- 状态版本与统一提交接口；
- Fake Provider / Adapter / Clock。

完成标准：一个固定场景可以从事件进入 Job，产生结构化行为和持久计划，并确定性回放。

## 2. 消息窗口与可取消回应

交付：

- Conversation Mailbox；
- 连续消息 Observation Window；
- 基础 Wake-up Gate；
- 会话串行和过期取消；
- 延迟发送与 supersede；
- 窗口、取消和等待 Trace。

完成标准：连续消息不再逐条回复；补充、撤回和他人抢答可以使旧 ActionPlan 失效。

## 3. Cognitive Kernel 垂直切片

交付：

- 全局 ready-job 队列和单 active cognitive commit；
- 一致 Subject Snapshot；
- SituationFrame；
- 结构化行为模型调用；
- 确定性审查；
- 表达生成和输出验证。

完成标准：行为类别和最终文本可以独立评估，模型输出不能直接发送或写长期状态。

## 4. 任务、承诺与持久唤醒

交付：

- Task / Commitment 生命周期；
- 持久 Scheduler；
- 时区、安静时段和过期；
- ProactiveOpportunity Gate；
- 重启恢复。

完成标准：明确提醒和承诺在重启后仍履行，用户关闭和安静时段零违规。

## 5. 有来源的记忆与知识边界

交付：

- MemoryCandidate / MemoryRecord；
- 作用域、敏感度、冲突、替代和纠正；
- SQL + FTS 检索；
- ContextBlock 与 Provenance Manifest；
- 最小 Epistemic State。

完成标准：用户纠正传播到检索；私聊记忆不进入群聊；主体能承认知识边界。

## 6. 生活时间线与叙事现实

交付：

- Planned Schedule；
- Lived Timeline；
- Claim Ledger；
- Narrative Reality Review；
- 自我陈述冲突检测。

完成标准：表达模型不能无依据创建持续生活事实，冲突声明可以被定位和纠正。

## 7. 关系、人格和轻量情绪

交付：

- Core Identity version；
- Relation Evidence / View；
- Living State；
- 轻量 appraisal 与 affect；
- 用户管理和关闭入口。

完成标准：单事件不造成关系剧烈跳变，情绪不改变权限或核心人格。

## 8. 离线反思

在上述基础稳定后研究：

- 日记候选；
- 程序性反思；
- 自我叙事候选；
- 梦沙箱。

进入主线前必须通过事实污染、成本和消融门槛。

## 迁移原则

目标在线运行时若转向 TypeScript：

- 先冻结领域契约和场景；
- 以完整行为切片迁移；
- 迁移期间只有一个权威写入者；
- 不让 Python 与 TypeScript 同时拥有主体状态；
- 旧实现作为回放基线，而不是逐行翻译对象。
