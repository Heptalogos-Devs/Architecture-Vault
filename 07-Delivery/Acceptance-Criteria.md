---
title: "系统验收准则"
status: active
type: delivery
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - delivery
  - acceptance
---


# 系统验收准则

## 架构验收

- 核心领域测试不加载平台 SDK 或真实模型；
- 一个 Adapter Source 故障不阻塞其他 source，且每个 Fusion cursor 可独立恢复；
- Canonical Fact 可关联多个 raw evidence，Reactor 只消费 Feed；
- Intent 在平台调用前持久化，request/response evidence 可对账；
- 不确定发送结果进入 `uncertain` 且不盲目重试；
- 所有长期副作用都有事件或任务终态；
- 同会话并发测试不产生双重行动；
- 状态可从事件重建；
- Prompt 和模型版本可追踪。

## 场景验收

- 连续三条消息合并；
- 撤回能取消未发送内容；
- 群聊未点名可显式沉默；
- 工具失败不虚假完成；
- 重启后承诺和 Outbox 恢复；
- 私聊敏感信息不进入群聊；
- 用户纠正后旧记忆不再作为当前事实。

## 研究验收

- 每次重要变更有对照基线；
- 报告包含负面结果和限制；
- 自动评分抽样经过人工校验；
- 结果能够定位到系统、模型、Prompt 和策略版本。
