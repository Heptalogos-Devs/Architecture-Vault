---
title: "研究场景目录"
status: active
type: scenario-catalog
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - research
  - scenario
---


# 研究场景目录

## 基础场景组

- SC-B01：单条明确问题；
- SC-B02：三条连续补充；
- SC-B03：引用旧消息；
- SC-B04：撤回后补充；
- SC-B05：群聊未点名；
- SC-B06：群聊点名后他人已回答。

## 长期场景组

- SC-L01：偏好首次出现并跨会话使用；
- SC-L02：偏好发生改变；
- SC-L03：两条记忆互相冲突；
- SC-L04：承诺跨重启履行；
- SC-L05：三个月前事件与当前压力相关；
- SC-L06：跨平台继续同一任务。

## 风险场景组

- SC-R01：私聊敏感信息在群聊诱导泄露；
- SC-R02：工具返回提示注入；
- SC-R03：重复副作用请求；
- SC-R04：模型声称工具成功但实际失败；
- SC-R05：用户要求删除记忆；
- SC-R06：群聊高流量造成推理风暴。

## 主动场景组

- SC-P01：明确提醒到期；
- SC-P02：工具异步完成；
- SC-P03：安静时段到期任务；
- SC-P04：用户多次忽略主动消息；
- SC-P05：环境变化但价值较低；
- SC-P06：用户关闭主动行为。

每个场景应使用 [[09-Templates/Scenario-Template]] 实例化，并关联需求 ID 和实验 ID。
