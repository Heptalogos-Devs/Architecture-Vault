# 当前状态

> 更新日期：2026-08-03

本文只描述当前仓库与近期方向。它是 Agent 判断“已经实现”和“准备实现”的首要文档，应随代码发生实质变化时同步更新。

## 当前定位

Heptalogos 处于研究原型阶段。当前实现已经建立可靠的交互事实链路和本机控制面，中央认知仍是验证性工作流；完整身份、长期记忆、关系、时间、承诺、知识边界和受控自主尚未形成统一 Cognitive Kernel。

## 已实现

### Interaction Gateway

```text
Raw platform bytes
→ Evidence
→ Canonical interaction
→ Reactor Feed
→ CommunicationIntent
→ DeliveryPlan
→ DeliveryOutcome
```

现有系统已经处理：

- 原始字节先落盘；
- 多来源规范化与融合；
- Feed cursor、checkpoint 与至少一次读取；
- Intent、Plan、请求证据、响应证据和 Outcome 分离；
- 平台调用结果的 `succeeded / failed / uncertain`；
- 历史恢复、资产任务、本地 CAS 和故障对账；
- 平台与模型 SDK 不进入核心领域。

### Reactor

当前 Reactor 验证 `Feed → 模型 → Intent` 边界：

- 按规则决定是否触发；
- 保存短会话 transcript；
- 构建普通 Prompt；
- 调用 OpenAI-compatible 模型；
- 生成 `reply / ignore`；
- 先持久化模型结果，再提交确定性 Intent；
- 在崩溃后复用结果并恢复确认流程。

它不是最终 Cognitive Kernel。

### Control Plane

当前 Control Plane 提供：

- 本机生命周期管理；
- 脱敏查询和单对象临时揭示；
- 配置、Provider、Prompt 和 Secret 管理；
- 安装、升级、回滚和卸载；
- 备份、恢复、重放和投影重建；
- 日志、指标、审计和持久操作；
- React/TypeScript Web 管理界面。

## 当前未实现的核心能力

- Observation Window 和 Conversation Mailbox；
- 全局注意力与单一认知提交；
- 结构化 BehaviorIntent 和 ActionPlan；
- 状态快照、身份、Living State 与关系；
- 记忆候选、冲突、纠正与检索；
- 任务、承诺、日程、生活时间线和 Claim Ledger；
- 知识边界和叙事现实审查；
- 能力注册、权限、确认和持久长任务；
- 日记、反思和梦沙箱；
- 完整 Scenario Runtime、虚拟时钟和消融评估。

## 当前目标方向

1. 把中央 Reactor 演化为拥有唯一认知提交权的 Cognitive Kernel。
2. 先完成消息窗口、调度、结构化行为、可取消 ActionPlan 和回放。
3. 再引入有来源的记忆、承诺、时间线、关系和知识边界。
4. 日记、复杂情绪、梦和高级自主必须晚于事实、状态和治理基础。
5. 面向云端 AI 供应商设计：在线权威系统优先考虑 TypeScript/Node.js；Python 保留研究、评估、本地模型和离线候选职责；Rust 仅用于安全或原生执行边界。

## 需要同步更新本文的情况

- 主运行时或语言政策改变；
- 新的权威状态域进入主分支；
- Gateway、Reactor、Control Plane 的职责发生变化；
- 目标里程碑完成或放弃；
- 某个概念从研究想法变成当前架构。
