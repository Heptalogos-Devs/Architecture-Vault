---
title: "垂直切片计划"
status: proposed
type: delivery
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - delivery
  - vertical-slice
---


# 垂直切片计划

## VS-0 可回放事件骨架

平台事件 → 规范化 → Ledger → 状态投影 → Trace → 回放。暂不调用模型。

## VS-1 逐消息基线

明确 @ 或私聊消息直接构建最小上下文并回复，形成可比较基线。

## VS-2 消息窗口和唤醒

加入 debounce、连续补充、撤回取消、群聊静默和过载背压。

## VS-3 行为与表达

引入 BehaviorIntent、输出检查和可取消 Outbox。

## VS-4 最小长期连续性

加入明确用户偏好、承诺任务、来源和纠正；不加入自由模型画像。

## VS-5 异步能力

加入一个感知工具和一个长耗时任务，结果事件化并根据当前情境通知。

每个切片必须有场景、指标和回放，不接受只完成代码路径。
