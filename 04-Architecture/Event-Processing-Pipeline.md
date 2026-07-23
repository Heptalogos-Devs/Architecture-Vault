---
title: "事件处理管线"
status: proposed
type: architecture
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - architecture
  - event-pipeline
---


# 事件处理管线

## 阶段

1. **接收并落盘**：验证来源，把完整 RawPlatformEvent 或不可变引用写入 Raw Event Ledger，记录协议、实现与 schema 版本。
2. **宽容解码**：识别已知类型；未知事件、消息段和字段保存为 opaque 扩展并产生诊断。
3. **规范化**：转换消息段、平台动作、身份和 occurred/observed 时间字段，生成 Canonical Interaction Event。
4. **去重排序**：幂等键、序列和延迟事件处理。
5. **身份解析**：平台、账号、人物、会话、成员关系和 Agent 自身。
6. **事实提交**：规范事件写入 Canonical Event Ledger，再触发后续处理。
7. **确定性投影**：消息可见状态、成员、任务和发送状态。
8. **会话路由**：进入对应 Mailbox。
9. **观察聚合**：合并消息和派生结果。
10. **唤醒判断**：行动、等待、静默、取消或暂停。
11. **认知与行动**：上下文、行为、工具和表达。
12. **Outbox**：延迟、取消、发送、`uncertain` 对账和回执。
13. **后台沉淀**：记忆候选、情节、统计和评估样本。

## 顺序原则

原始事实必须先持久化，规范事件必须提交后再产生不可逆副作用。状态更新和发送不能依赖仅存在于内存中的平台回调或模型响应。

## 背压

群聊突发流量时，Mailbox 可执行：窗口延长、低价值事件摘要、媒体延后、最大并发限制和过载静默。背压策略本身需要进入 Trace。
