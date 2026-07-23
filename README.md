---
title: "Heptalogos Architecture Vault"
status: active
type: vault-guide
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - heptalogos
  - architecture
  - research
---

# Heptalogos Architecture Vault

> [!warning] 内部研究资料
> 本知识库基于 Heptalogos Devs 的内部完整描述、当前可见原型和公开参考项目形成。它处于研究与架构探索阶段，不是公开项目说明，也不代表架构已经定型。

这是一个面向研发阶段的 Obsidian 知识库，用于把项目的**问题空间、需求、领域概念、架构假设、组件责任、实验与决策**分开管理，并通过可追溯的链接把它们串成一张架构知识图谱。

本仓库按内部资料维护，应保持为 GitHub Private repository。若未来需要公开，必须先对内部描述、实现细节、来源笔记和引用内容进行脱敏与授权审核。

## 项目定位

Heptalogos 研究面向即时通信场景的 AI 拟人化交互系统。目标不是为模型添加一段角色提示词，而是探索一种能够在真实消息环境中保持**连续性、一致性、自主性、适应性与可控性**的长期运行系统。

## 阅读入口

| 主题 | 内容 | 入口 |
| --- | --- | --- |
| 项目总览 | 研究目标、五条主线、当前基线与未决议题 | [项目总览与导航](00-Home/Project-MOC.md) |
| 研究地图 | 研究问题、证据、假设与实验之间的关系 | [研究地图](00-Home/Research-Map.md) |
| 基础定义 | 问题空间、使命范围、原则、术语与风险 | [Foundations](01-Foundations/) |
| 需求体系 | 场景、功能需求、质量属性、安全控制与追踪矩阵 | [Requirements MOC](02-Requirements/Requirements-MOC.md) |
| 领域模型 | 身份、会话、关系、记忆、行为、任务与事件 | [Domain MOC](03-Domain-Model/Domain-MOC.md) |
| 架构设计 | 上下文、事件流、运行时、持久化、部署与故障恢复 | [Architecture MOC](04-Architecture/Architecture-MOC.md) |
| 组件规格 | 组件边界、输入输出、策略、调度与评估 | [Component MOC](05-Components/Component-MOC.md) |
| 研究与评估 | 假设、实验计划、指标、证据和参考项目 | [Research MOC](06-Research/Research-MOC.md) |
| 交付计划 | MVP、验收标准、垂直切片、路线图与测试策略 | [MVP Definition](07-Delivery/MVP-Definition.md) |
| 架构决策 | 已记录的架构选择及其理由 | [ADR MOC](08-ADR/ADR-MOC.md) |
| 可视化 | 需求到架构、系统拓扑等 Canvas | [Canvases](11-Canvases/) |

## 推荐阅读顺序

```mermaid
flowchart LR
    A[问题空间] --> B[需求]
    B --> C[领域模型]
    C --> D[架构基线]
    D --> E[组件规格]
    E --> F[MVP 与实验]
    F --> G[ADR 与迭代]
```

建议首次阅读按以下顺序进入：

1. [项目总览与导航](00-Home/Project-MOC.md)
2. [使命、目标与范围](01-Foundations/Mission-and-Scope.md)
3. [问题空间](01-Foundations/Problem-Space.md)
4. [需求地图](02-Requirements/Requirements-MOC.md)
5. [领域模型地图](03-Domain-Model/Domain-MOC.md)
6. [架构基线](04-Architecture/Architecture-Baseline.md)
7. [组件规格地图](05-Components/Component-MOC.md)
8. [MVP 定义](07-Delivery/MVP-Definition.md)
9. [架构决策记录](08-ADR/ADR-MOC.md)

## 五条研究主线

| 主线 | 核心问题 |
| --- | --- |
| 交互运行 | 如何处理消息流、时机、打断和非即时响应 |
| 持续状态 | 如何维持角色、会话、关系和任务状态 |
| 长期记忆 | 如何形成可追溯、可修正、按需出现的记忆 |
| 行为与能力 | 如何决定做什么，并安全使用工具完成行为 |
| 科学验证 | 如何证明某种设计真的改善拟人化交互 |

## 当前状态

- 研究阶段，当前版本为 `0.1`。
- 重点关注状态、记忆、消息处理、能力编排、主动行为和可观测性。
- 当前架构倾向于事件驱动、按会话串行处理、平台与模型解耦，并保留模块化单体作为早期实现边界。
- 具体角色状态、关系模型、记忆分层、主动行为价值函数和多 Agent 拓扑仍属于不同置信度的研究议题。
- 本仓库不包含生产实现、稳定公共 API 或生产级 SLA 承诺。

更细的事实与置信度说明见[信息状态与置信度](00-Home/Status-and-Confidence.md)。

## 文档状态约定

| 状态 | 含义 |
| --- | --- |
| `confirmed` | 来自内部权威描述或当前实现的已知事实 |
| `proposed` | 建议方案，尚未通过实验或 ADR 接受 |
| `hypothesis` | 可验证假设，不应作为既定事实 |
| `open` | 尚未解决的问题 |
| `deprecated` | 已失效但保留历史记录 |

每份文档还应区分事实、需求推断、设计建议、研究假设和工作名称。不要把工作名称或尚未验证的方案写成稳定 API 或既定事实。

## 维护规则

1. 需求必须有稳定 ID，不随实现名称变化。
2. 术语尚未确定时使用“工作名称”，并在[术语与命名](01-Foundations/Terminology-and-Naming.md)中登记。
3. 设计结论必须区分事实、推断、建议和待验证假设。
4. 重要架构选择通过 ADR 记录，不直接覆盖历史理由。
5. 实验结果应反向更新需求、假设和 ADR，而不是只记录模型分数。
6. 新证据的推荐流转路径为：

   ```text
   来源笔记 → 需求或假设 → 组件影响 → ADR → 测试与回放场景
   ```

## 使用方式

### 使用 Obsidian

将仓库根目录作为 Obsidian vault 打开，即可使用双向链接、标签、图谱和 Canvas。`.obsidian/` 中仅保留适合共享的基础设置；本机工作区状态不会纳入版本控制。

### 使用 GitHub

GitHub 可以直接阅读 Markdown 文件和目录导航。Obsidian 的 `[[双向链接]]`、图谱交互和 Canvas 的完整体验仍建议在 Obsidian 中使用。

## 仓库结构

```text
00-Home/          项目总览、研究地图、状态与置信度
01-Foundations/   问题空间、使命、原则、术语、风险与非目标
02-Requirements/  场景、功能需求、质量属性、安全与追踪矩阵
03-Domain-Model/  身份、会话、关系、记忆、事件、行为与任务
04-Architecture/ 运行时、事件流、持久化、部署、工具与故障恢复
05-Components/   组件职责、策略、调度、执行与评估
06-Research/     假设、实验、指标、证据与参考项目
07-Delivery/     MVP、验收标准、路线图、测试与垂直切片
08-ADR/          架构决策记录
09-Templates/    需求、场景、实验、研究、组件与 ADR 模板
10-Sources/      项目描述、来源笔记与参考项目
11-Canvases/     需求到架构、系统拓扑等可视化
99-Inbox/        尚未归档的输入
```

## 来源与边界

来源说明集中在 [10-Sources](10-Sources/)。引用或转述内容时，应保留来源、时间和证据等级；对于内部材料，应继续遵守原始访问权限和保密约束。

本仓库当前不附带开源许可证，也不授予复制、分发或商业使用权。任何公开发布或外部引用都需要单独确认授权。
