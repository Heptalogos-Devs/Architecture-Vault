---
title: "事件处理管线"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - architecture
  - event-pipeline
---


# 事件处理管线

## 阶段

1. **接收并落盘**：验证来源，把完整 RawPlatformEvent 或不可变引用写入 Raw Event Ledger，记录协议、实现与 schema 版本。
2. **宽容解码**：识别已知类型；未知事件、消息段和字段保存为 opaque 扩展并产生诊断。
3. **规范化**：转换消息段、平台动作、身份和 occurred/observed 时间字段，生成 Canonical Interaction Event。
4. **多来源融合**：按稳定平台消息身份建立 Canonical Fact 与多个 provenance，
   payload hash 只用于完整性。
5. **身份解析**：平台、账号、人物、会话、成员关系和 Agent 自身。
6. **事实提交**：规范事件写入 Canonical Event Ledger，再触发后续处理。
7. **确定性投影**：消息可见状态、成员、任务和发送状态。
8. **Reactor Feed**：生成可重建投影并由独立 consumer checkpoint 确认。
9. **观察聚合**：合并消息和派生结果。
10. **唤醒判断**：行动、等待、静默、取消或暂停。
11. **认知与行动**：上下文、行为、工具和表达。
12. **Intent 与 Delivery**：持久化 Intent、规划端点、写入调用前后 evidence，
    生成成功、失败、不支持或 `uncertain` Outcome。
13. **后台沉淀**：记忆候选、情节、统计和评估样本。

## 顺序原则

原始事实必须先持久化，规范事件必须提交后再产生不可逆副作用。状态更新和发送不能依赖仅存在于内存中的平台回调或模型响应。

## 背压

群聊突发流量时，Mailbox 可执行：窗口延长、低价值事件摘要、媒体延后、最大并发限制和过载静默。背压策略本身需要进入 Trace。

## 当前 Interaction Gateway 的事务切点

1. Adapter 收到 frame 后先提交 Evidence DB，才解析 sequence 或交给响应匹配器。
2. Fusion 逐来源读取 cursor 之后的记录；Canonical、provenance、Feed/asset 派生和
   cursor 在同一 Gateway DB 事务提交。
3. 出站先提交 Intent/Plan；worker claim 后先写 request evidence，再调用平台。
4. 平台返回后先写 response evidence，再提交 Outcome。
5. 媒体任务与消息事实解耦，下载失败不回滚 canonical 消息。

跨 Evidence DB 与 Gateway DB 没有伪造的分布式事务。崩溃后由重复读取、稳定 ID 和
reconciliation 收敛；request evidence 后的未知调用结果收敛为 `uncertain`。
