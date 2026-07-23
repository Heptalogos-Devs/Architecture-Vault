---
title: "行动与投递模型"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - domain
  - action
  - delivery
---


# 行动与投递模型

## ActionPlan

```yaml
action_id: uuid
behavior_id: uuid
action_type: send_text | quote | react | media | tool | schedule | cancel
target: platform + conversation + message?
payload: object
earliest_at: datetime
expires_at: datetime?
cancellable: bool
cancel_on_event_types: []
idempotency_key: string
retry_policy: object
platform_fallback: object
status: planned | scheduled | executing | delivered | failed | cancelled | expired
```

## 生成与投递分离

表达生成只产生候选内容；投递层决定何时、以何种平台动作发送。延迟期间的新事件可以让计划过期、取消或重新渲染。

## Outbox 模式

持久化 Outbox 保存待执行动作，工作器原子领取并发送。发送回执形成事件，状态投影再更新 Action 状态。

## 平台降级

例如目标平台不支持表情反应时，可以：

1. 放弃该低价值动作；
2. 转换为短文本；
3. 在其他授权渠道通知。

降级必须由策略定义，不能由适配器任意改变语义。
