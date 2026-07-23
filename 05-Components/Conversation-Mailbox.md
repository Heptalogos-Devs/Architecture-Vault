---
title: "会话 Mailbox"
status: proposed
type: component-spec
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - component
  - conversation-mailbox
---

# 会话 Mailbox

## 目的

按 Agent 与会话串行处理事件，维护活动生命周期、取消令牌和待处理窗口。

## 输入

- 已提交 EventEnvelope
- 定时唤醒

## 输出

- ObservationBatch
- 取消命令
- 生命周期事件

## 数据所有权

- 活动会话运行状态
- 待处理索引
- 并发顺序

## 不变量

- 同分区内决策不并发
- 事件索引单调前进
- 重启后可从存储恢复

## 典型故障

- 处理超时
- 热会话积压
- 毒事件反复失败

## 关键指标

- 队列深度
- 窗口等待时间
- 取消率
- 每会话吞吐

## 接口原则

- 输入输出使用版本化契约，不传递平台 SDK 或供应商对象。
- 所有长期副作用都返回事件或显式命令结果。
- 调用方不得绕过组件接口直接修改其拥有的数据。

## 待研究问题

- Actor 框架还是轻量 asyncio 实现
- 空闲会话休眠和恢复方式

## 相关需求

参见 [[02-Requirements/Functional-Requirements]] 与 [[02-Requirements/Traceability-Matrix]]。
