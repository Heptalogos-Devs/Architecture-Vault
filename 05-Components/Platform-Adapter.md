---
title: "平台适配器"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - platform-adapter
---

# 平台适配器

## 目的

在平台 SDK 与内部事件/动作契约之间转换，不承担认知逻辑。

## 输入

- 平台回调、WebSocket 或轮询事件
- 内部 PlatformAction

## 输出

- RawPlatformEvent
- 标准化前的发送回执和能力状态
- 协议连接、断开、版本和观测缺口事件

## 数据所有权

- 连接状态
- 平台账号元数据
- 短期 SDK 资源

## 不变量

- 不得丢弃原始载荷引用
- 不得调用模型或写记忆
- 发送必须返回可对账标识
- 不得把平台 SDK、OneBot 或 Milky 类型暴露给核心
- 不得提供任意 API、文件路径或 URL 透传
- 发送超时必须表达为可对账的 `uncertain`，不得默认盲目重试

## 典型故障

- 协议版本变化
- 账号离线或禁言
- 速率限制
- 平台能力不支持

## 关键指标

- 连接可用率
- 事件延迟
- 规范化失败率
- 发送重试率

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- 是否每个平台独立进程
- 如何表达平台特有事件而不污染通用契约

## QQ 个人号实验实现

`heptalogos-adapter-milky` 是 proposed 薄适配器：LLBot 提供 Milky HTTP/WebSocket，适配器负责连接生命周期、原始事件落盘、规范化、身份映射、能力白名单和投递对账。完整 Bot Framework 不进入核心。

参见 [[08-ADR/ADR-0010-Platform-Adapter-Boundary-and-Canonical-Interaction-Events]] 与 [[08-ADR/ADR-0011-Milky-Experimental-QQ-Edge-Protocol]]。

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
