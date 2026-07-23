---
title: "参考项目比较研究"
status: active
type: research
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - research
  - reference-project
---


# 参考项目比较研究

> [!warning]
> 本文记录可借鉴机制和风险，不把任何项目视为 Heptalogos 的目标架构。

## AI Agent Book

**可借鉴**：把 Agent 视为模型、上下文和工具的组合；强调上下文工程、用户记忆、异步事件工具和评估驱动决策。尤其重要的是评估对象应是模型与 Harness 的组合。

**限制**：通用 Agent 方法需要补充 IM 特有的消息时机、群聊参与、长期身份和关系边界。

来源：<https://github.com/bojieli/ai-agent-book>

## MaiBot

**可借鉴**：把消息进入 Planner 的调度与最终回复生成分开；具备回复必要性、频率、等待和 focus 状态；记忆内核包含检索、情节、人物画像、维护和纠正等服务。

**风险**：长期演化中出现平台身份字段未贯穿序列化和业务逻辑的问题，说明跨平台身份必须从领域模型开始设计；大型记忆内核也容易积累复杂度。

来源：<https://github.com/Mai-with-u/MaiBot>

## WaifuBot

**可借鉴**：提供角色、短长期记忆、媒体、工具、权限和 WebUI 的产品功能矩阵，有助于发现运维和用户控制需求。

**风险**：功能覆盖不能替代领域边界；大量模式和开关可能让 Prompt、角色和工具逻辑纠缠。

来源：<https://github.com/sanxianxiaohuntun/waifubot>

## VCPToolBox

**可借鉴**：强调 AI 的持续存在和“信息主动流入上下文”；工具具有同步、异步、静态、常驻和预处理等生命周期；重视跨端时间线、上下文折叠和能力节点。

**风险**：整体语义管线如果缺乏显式契约，容易形成有机整体式隐式耦合；其专有记忆算法主张需要独立验证，不应直接采纳。

来源：<https://github.com/lioensky/VCPToolBox>

## AstrBot

**可借鉴**：清晰的平台抽象、统一事件队列、PipelineScheduler、插件和多平台基础设施；适合作为适配层和生态参考。

**风险**：每事件一条管道不自动解决连续消息聚合、会话串行、打断和持久调度。

来源：<https://github.com/AstrBotDevs/AstrBot>

## NapCatQQ

**可借鉴**：作为 QQ 协议边缘，提供丰富标准接口和长时运行基础。适合保持在系统边缘，通过适配器隔离。

**风险**：协议实现、平台政策和法律约束可能变化；核心系统不得依赖其内部对象和目录。

来源：<https://github.com/NapNeko/NapCatQQ>

## 比较结论

| 需求 | 最强参考 | Heptalogos 仍需解决 |
|---|---|---|
| 平台适配与插件 | AstrBot、NapCat | 消息连续性和领域身份 |
| 时机与群聊行为 | MaiBot | 可回放的唤醒与取消模型 |
| 长期记忆 | MaiBot、VCP、Agent Book | 来源、作用域和实验化分层 |
| 产品控制面 | WaifuBot、AstrBot | 研究状态和隐私治理 |
| 异步能力 | VCP、Agent Book | 结果事件化与角色连续性 |
| 评估 | Agent Book | 长期 IM 专属指标和虚拟时间 |
