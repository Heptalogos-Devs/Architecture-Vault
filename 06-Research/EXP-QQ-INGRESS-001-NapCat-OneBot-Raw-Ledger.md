---
title: "EXP-QQ-INGRESS-001 NapCat OneBot 原始入站账本"
status: active
type: experiment
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - experiment
  - qq
  - napcat
  - onebot
  - raw-event-ledger
---

# EXP-QQ-INGRESS-001 NapCat OneBot 原始入站账本

## 假设

在 NcatBot 类型化分发之外建立同源、独立的 NapCat Forward WebSocket 旁路，并将每个观察到的帧先写入 append-only SQLite 账本，可以：

1. 保存被框架未知类型过滤或字段裁剪掉的平台事实；
2. 区分平台未发送、传输断连、类型化投影丢失和业务处理失败；
3. 为未来 OneBot、Milky 或其他平台适配器提供可回放的对照样本。

## 背景与关联需求

关联 [[08-ADR/ADR-0010-Platform-Adapter-Boundary-and-Canonical-Interaction-Events|ADR-0010]] 与 [[08-ADR/ADR-0011-Milky-Experimental-QQ-Edge-Protocol|ADR-0011]]。

QQContextBot 的历史 ORM 投影以消息为中心。对专用测试群（标识已脱敏）的基线检查发现：1,713 条历史消息中，有 10 条消息没有任何 `message_segments` 投影；其原始 CQ 类型为 7 条语音、2 条文件和 1 条视频。原因是固定消息段 allowlist 丢弃了这些类型，而非没有原始输入。

## 对照与实验组

- 对照组：现有 NcatBot 回调进入 `qq_recorder` ORM 投影。
- 实验组：独立 NapCat Forward WebSocket 的原始帧账本，同时运行现有投影。
- 比较单位：一次 WebSocket 帧观察及其可识别的 `message_id`，不以内容哈希去重。

## 数据集和场景

- 专用测试群：真实标识仅保存在本地运行配置中，不进入仓库。
- 历史数据：截至 2026-07-23 的 recorder SQLite。
- 实时数据：用户连续发送的文本、回复、@、图片、表情、语音、视频、文件、转发、JSON 卡片，以及安全的平台通知事件。
- 全事件旁路采集；报告阶段可按测试群过滤。

原始账本和媒体包含个人信息，仅在本地保留。可共享样本必须通过脱敏 fixture 导出。

## 自变量、控制变量和混杂因素

- 自变量：是否启用 raw-first 旁路；消息段是否使用固定 allowlist。
- 控制变量：同一 NapCat 实例、同一账号、同一测试群、同一测试时段。
- 混杂因素：QQ 客户端上传转换、NapCat 版本、断线重连窗口、媒体 URL 有效期、NcatBot 与旁路连接的观察顺序。

## 指标与否决项

- 原始帧总量、事件类型和消息段类型覆盖；
- 原始消息事件到 ORM `messages` 的投影率；
- 重复帧、乱序事件、无效编码或 JSON 的数量；
- 媒体引用的 downloaded、oversized、failed、missing_reference 状态；
- 连接、断开和重试诊断；
- 未知事件、段或扩展字段是否仍能从原始载荷重放。

否决项：原始帧在解析前被覆盖或去重；未知类型仍被丢弃；原始证据与派生投影无法关联；采集阻塞主要消息事件循环。

## 执行版本

- QQContextBot / `qq_recorder`: 1.6.0。
- NcatBot: 5.5.4（本地已安装版本；实时窗口开始时再次记录到 session）。
- 外部协议：NapCat Forward WebSocket / OneBot 11。
- 原始账本：`data/qq_recorder/data/raw_events.db`。
- 观测工具：`scripts/observe_qq_ingress.py`。
- 测试规格：QRI-01 至 QRI-05。

## 结果

### 已确认

- 独立 Forward WebSocket 可以与现有适配器并行连接并接收帧。
- 既有 recorder 定向测试基线为 32 项通过。
- 历史缺失可由 CQ 原文恢复：7 个 `record`、2 个 `file`、1 个 `video`。
- 新实现保存 exact raw bytes、SHA-256、观察顺序、连接 session 和解析诊断；重复帧保留为不同观察。
- 正常 ORM 投影不再对白名单外消息段做静默丢弃。

### 实时序列结果

2026-07-23 命名窗口 `qq-ingress-20260723` 已完成：

- 专用群共观察到 29 个事件：26 个群消息、2 个 `group_upload`、1 个 `group_ban.ban`；
- 29/29 原始载荷解析成功，26/26 带消息标识的事件进入 recorder ORM，投影缺失为 0；
- 专用群窗口内没有重复帧或乱序事件，连接 session 内记录到 1 次成功连接；
- 顶层覆盖 `text`、`face`、`reply`、`at`、`image`、`record`、`video`、`file`、`forward` 和 `json`；
- 两个合并转发分别生成 18 个一级节点，以及 2 个一级节点加 18 个二级节点；
- 4 个图片源和 1 个语音源完成内容寻址归档；转发中的重复引用保留观察记录，但共享实际二进制；
- 视频事件完整保存了 908,734 字节声明和本地路径，但平台给出的 `Ori` 路径在归档时已不存在；
- 两个群文件的事件、名称、大小、notice ID 和 message file ID 均已保存，但二进制下载被 NapCat `packetBackend` 拒绝。当前 QQ `9.9.27-46233-x64` 与 NapCat 提示的 PacketBackend 架构不兼容。

实时数据证明 raw ledger 可以区分“事件未接收”“ORM 投影遗漏”“引用已接收但媒体不可取”三类状态。Windows 本地路径被错误当作 URL scheme 的实现缺陷已修复，语音随后成功补取；视频源已经消失，不能从现有证据恢复二进制。

对账还发现 ORM 曾在实际下载前用平台 `file` 名称设置
`downloaded=true`。该派生状态与下载失败日志矛盾，已改为只有归档成功后才设置，并校正本轮视频记录。这个反例说明 derived projection 不能替代 raw evidence，也不能把“平台给出来源引用”等同于“本地已持久化”。

## 限制与反例

- Forward WebSocket 本身不是可靠消息队列；断线期间平台未重放的事件仍可能形成不可恢复缺口。
- 旁路与 NcatBot 投影之间没有平台提供的统一投递事务，只能通过消息标识和观察时间对账。
- 文件和媒体 URL 可能过期，原始引用已保存不等于二进制一定能下载。
- 该实验验证 NapCat/OneBot 作为对照边缘实现，不证明其适合作为 Heptalogos 核心依赖。

## 架构影响

继续实验。该实现是 [[08-ADR/ADR-0010-Platform-Adapter-Boundary-and-Canonical-Interaction-Events|ADR-0010]] 的观测基础，不是最终 Canonical Interaction Event 运行时：

- 保留独立原始账本与派生投影的分层；
- 未来适配器以相同观测契约写入 raw ledger；
- Canonical event 只覆盖稳定核心，OneBot 特有字段保留版本化扩展与 raw reference；
- NcatBot 继续作为当前连通和投影实现，不进入未来认知核心。
