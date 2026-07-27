---
title: "ADR-0010 平台适配边界与规范交互事件"
status: accepted
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
  - platform-adapter
  - canonical-event
---

# ADR-0010 平台适配边界与规范交互事件

## 状态

`accepted`

## 背景

NapCat、LLBot、OneBot、Milky 和平台 SDK 表达的是外部协议与实现细节。若这些类型直接进入认知运行时，平台更换、回放、跨平台身份和能力治理都会与供应商生命周期耦合。

## 决策

采用三层入站边界：

```text
Platform Protocol Implementation
        ↓
Platform Adapter + Raw Event Ledger
        ↓
Canonical Interaction Event
        ↓
Heptalogos Runtime
```

- 外部平台不得直接调用 Persona、Memory、Behavior Policy 或 Conversation Mailbox。
- RawPlatformEvent 必须先以原始载荷或不可变引用持久化，再尝试规范化。
- Canonical Interaction Event 是运行时唯一接受的平台事实语言；核心不得导入 OneBot、Milky 或供应商 SDK 类型。
- 规范事件至少保留事件标识、平台与账号、会话、参与者、发生/观察时间、内容或载荷、引用、原始事件引用和 Trace 上下文。
- 未知事件、消息段和扩展字段必须可保存、可观察，并以 opaque 扩展表达，不能因无法规范化而丢弃原始事实。
- 适配器声明能力并将 PlatformAction 映射为白名单协议调用；模型不得构造任意平台 API、文件路径或 URL。
- 入站使用 Event Ledger，出站使用 Persistent Outbox；发送超时可以进入 `uncertain`，不得默认盲目重试。

## 替代方案

- 直接把平台 SDK 事件送入运行时：实现快，但无法保持平台中立和稳定回放。
- 只保存规范事件：节省存储，但协议升级后无法重新解释历史。
- 以完整 Bot Framework 作为运行时：其生命周期、插件和回调调度会与 Heptalogos 的 Mailbox、Scheduler 和 Replay 重叠。

## 后果

- 平台替换、Fake Adapter 测试和原始事实重放具有稳定边界。
- 需要维护 Raw DTO、规范事件、映射诊断和能力声明。
- 规范模型不能只取跨平台最小公分母；平台特性通过版本化扩展和 CapabilityDescriptor 保留。

## 验证与回退

- 契约测试覆盖已知与未知事件、消息段、重复、乱序、超大标识和异常时间戳。
- 核心测试只使用 Fake Adapter 即可运行；替换协议实现不得修改 Persona、Memory 或 Reactive Processor。
- 若某类平台语义无法无损映射，保留 RawReference 和平台扩展，不把供应商类型泄漏到核心。
