---
title: "路由与投递"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-24
updated: 2026-07-24
tags: [component, routing, delivery]
---

# 路由与投递

## 目的

把持久化 `CommunicationIntent` 转换为具体端点的 `DeliveryPlan`，并将平台调用证据
投影为 `DeliveryOutcome`。

## 第一版路由

1. 由入站事实触发时使用原平台账号、会话和 Adapter Instance。
2. 原实例不可用时只考虑同账号、显式配置的备用实例。
3. Intent 显式指定合法端点时使用该端点。
4. 其他情况生成 `MissingRoute`，不执行平台调用。

## 不变量

- Intent 先于平台调用持久化。
- request evidence 先于 API，response evidence 先于唤醒调用方。
- 请求可能已发出但无终态时生成 `uncertain`，不自动重试。
- Adapter 只做机械能力映射，不删除或改写业务内容。

## 状态机与崩溃窗口

```text
intent -> planned -> claimed
  -> request_recorded -> succeeded | failed | unsupported | uncertain
  \-> missing_route
```

- `claimed` lease 在 request evidence 前过期，可以安全重新领取。
- request evidence 已存在而 response 缺失时，请求可能已到达平台，只能进入
  `uncertain` 或人工 reconciliation。
- response evidence 必须在 Outcome 前落盘，使 Outcome 永远可回溯到协议原文。

## 设计理由

Intent 表达业务决定，Plan 表达端点选择，Outcome 表达外部世界的可知结果。三者分离
使备用路由、能力不支持和网络不确定不会反向改写 Reactor 的原始意图。
