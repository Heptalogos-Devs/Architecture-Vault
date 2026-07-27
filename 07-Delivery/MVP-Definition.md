---
title: "MVP 定义"
status: accepted
type: delivery
confidentiality: internal
created: 2026-07-23
updated: 2026-07-26
tags:
  - delivery
  - mvp
---


# MVP 定义

## MVP 研究目标

验证“事件流 + 会话串行 + 消息窗口 + 行为/表达分离 + 可取消投递 + 回放”是否能够产生比普通逐消息机器人更稳定的 IM 行为。

## 包含

- 单一 QQ 平台薄适配器；LLBot + Milky 为 proposed 实验基线，NapCat + OneBot 11 为对照方案；
- 标准事件和原始载荷引用；
- SQLite 事件库、状态快照和 Outbox；
- 按会话 Mailbox；
- 连续消息窗口和基础唤醒门；
- 最小角色定义、会话状态和明确用户偏好；
- BehaviorIntent 与文本表达分离；
- 可取消延迟发送；
- 完整 Trace、虚拟时钟和事件回放；
- 20—30 个核心场景。
- Fake Adapter 契约基线，以及协议实现替换不进入认知核心的证明。

## 不包含

- 复杂情绪模型；
- 图记忆或自研语义动力学；
- 多 Agent 社会；
- 多地域分布式运行；
- 开放式自主目标；
- 大型插件市场；
- 完整 WebUI 产品。
- QQ 个人号接入的生产级、合规性或完整事件恢复承诺。

## MVP 成功标准

相对于逐消息直接回复基线：碎片回复和过期回复显著下降；明确问题漏答不显著增加；事件回放可复现；无私聊信息越域；系统能够在重启后恢复待执行动作。
