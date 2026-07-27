---
title: "身份与会话模型"
status: proposed
type: domain-model
confidentiality: internal
created: 2026-07-23
updated: 2026-07-24
tags:
  - domain
  - identity
  - conversation
---


# 身份与会话模型

## 实体

### Person

现实中被系统认为是同一主体的人。身份合并需要用户确认或高置信证据，不能仅凭昵称。

### PlatformIdentity

```yaml
platform_identity_id: id
platform: qq | telegram | web | ...
platform_account_id: string
person_id: id?
valid_from: datetime
valid_to: datetime?
verification: unverified | user_confirmed | admin_confirmed
```

### AgentIdentity

Agent 在某个平台上的账号。不得用 QQ 账号作为未知平台默认身份。

实现必须区分长期主体、Platform Account、Protocol、Protocol Implementation、
Adapter Instance 和短期 Connection Session。同一 Platform Account 更换 OneBot /
Milky 或 NapCat / LLBot 后，内部账号身份和会话绑定保持连续。

### Conversation

表示私聊、群聊、频道、线程或 Web 会话。包含平台原生 ID、类型和父级关系。

### Membership

人物或 Agent 在会话中的成员关系、角色、权限、昵称和有效时间。

## 会话键

消息处理分区建议使用：

```text
agent_id + conversation_id
```

这保证同一 Agent 在同一会话中串行，但不阻止不同会话并发。

## 身份合并风险

错误合并比未合并更危险：会导致私密信息跨平台泄漏、关系错误共享和记忆混用。因此默认策略应偏保守。
