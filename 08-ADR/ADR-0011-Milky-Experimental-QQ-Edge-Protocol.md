---
title: "ADR-0011 Milky 作为实验性 QQ 个人号边缘协议"
status: proposed
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
  - qq
  - milky
  - llbot
  - experiment
---

# ADR-0011 Milky 作为实验性 QQ 个人号边缘协议

## 状态

`proposed`

## 背景

QQ 个人号接入需要在协议语义、实现成熟度、事件恢复和替换成本之间权衡。Milky 提供独立协议规格与机器可读定义；LLBot 是当前可用于实验的实现之一，但 WebSocket 事件流不是可靠事件存储，普通 QQ 客户端兼容性也属于外部不确定性。

## 决策

- 以 LLBot + Milky + 自研薄适配器作为 QQ 个人号接入的实验性基线。
- Milky 是候选外部协议边界，LLBot 是可替换协议实现；二者都不是核心领域依赖或可靠性基础。
- 实验前固定 LLBot 版本或制品摘要、Milky 规格版本和 schema 版本。
- 自研适配器只包含异步 API Client、Event Client、生成的协议 DTO、连接生命周期、Raw Ledger、规范化、能力声明和投递跟踪。
- 不引入完整 Milky Bot Framework，也不把 NcatBot、NoneBot 或 Koishi 嵌入认知核心。
- QQ 官方机器人 API 未来作为独立 Platform Adapter，不作为个人号适配器的降级模式。
- 本 ADR 不作生产级、合规性或完整事件恢复承诺。

## 替代方案

- NapCat + OneBot 11 + 自研薄适配器：生态更成熟，保留为对照实验。
- NapCat + NcatBot：适合快速连通验证，但 NcatBot 不进入正式核心依赖。
- NoneBot/Koishi Gateway：多平台需求明确时重新评估。
- QQ 官方机器人 API：适合合规公开部署，但能力和交互主体不同。

## 后果

- 可以验证更现代的 QQ 语义和机器可读契约是否降低适配成本。
- 需要承担断线缺口、事件标识不统一、发送结果不确定和客户端升级风险。
- LLBot 与 Heptalogos 必须保持进程、许可和故障域边界。

## 验证与回退

进入主干前完成：

1. 官方示例、未知类型、重复、乱序和兼容性契约测试；
2. 私聊、群聊、临时会话、引用、媒体、文件、转发、撤回和平台状态垂直切片；
3. WebSocket 断开、LLBot 重启、各持久化边界崩溃和发送超时故障注入；
4. LLBot Milky、Fake Milky Server 和另一实现的替换性测试；
5. 文件、URL、任意 API 透传和多账号身份隔离安全测试。

若原始事件无法先落盘、核心依赖 Milky 类型、替换实现需要修改认知模块，或发送不确定性无法对账，则拒绝本 ADR，并回退到 Fake Adapter 或 NapCat + OneBot 11 对照基线。
