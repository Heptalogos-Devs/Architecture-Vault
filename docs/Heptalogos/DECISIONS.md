# Heptalogos 设计决定

## Subject 与产品职责

### Heptalogos 承担行为侧 Subject

Heptalogos 维护 Subject 的主动性、交互、行为决定、承诺、外部效果和产品运行。认知长期状态由 Nous Wave 维护。

目标设计：第 1、2、4 节。

### 认知输入保留结构身份与可修订判断

Nous Wave 的认知 Authority 记录 Subject cognition 与演化，不认证 objective truth。Heptalogos 保留对象/revision、provenance、formation basis 与 epistemic judgment，按自身行为合同审查输入；认知错误和后续纠正不自动取得或撤销行为 Authority。

目标设计：第 6 节。

合同：[认知与主动性](../integration/cognition-agency.md)

### SubjectId 跨认知与行为系统保持一致

Nous Wave 和 Heptalogos 共享逻辑 `SubjectId`，各自维护自己的领域状态和修订。

目标设计：第 2、6 节。

## 主动性

### 主动追求由 Heptalogos 维护

`Pursuit` 表示行为侧已经决定持续投入行为资源追求某个期望条件。它引用 Nous Wave 中期望条件的精确修订。

目标设计：第 5 节。\
论证：[认知与主动性](rationale/01-cognition-agency.md)

### 一次行为提议与持续追求分别维护

`BehaviorIntent` 表示一次具体行为决策中的提议；`Pursuit` 表示跨多次 Reaction 延续的主动追求。计划、承诺和外部效果继续拥有各自身份。

目标设计：第 4、5、7 节。

## 行为权威

### 行为决定通过显式提交形成

模型、检索、认知系统和扩展提供输入或提案。对外行为必须经过 Heptalogos 的 Review 与 `DecisionCommit`。

目标设计：第 3、4 节。

### 安全政策和管理员强制由 Heptalogos 承担

行为许可、禁止、管理员强制约束和系统管理由 Heptalogos 的行为与规范权威维护，不依赖可演化认知。

目标设计：第 3、10、11 节。

## 产品运行

### 产品宿主与机器运维分离

正常产品宿主拥有产品 Authority。高权限机器维护位于独立机器运维平面，通过管理合同与宿主协作。

目标设计：第 3、8 节。

## 原生 OpenClaw 与持续主体生活

**决定：** Heptalogos 复用 Nous 正式认知集成与 OpenClaw 原生模型/工具/渠道/子 Agent 能力，继续拥有生活活动、消息感知、行为采纳、外部效果和产品管理。一次生成可以包含候选与草稿，真实执行/外发前必须获得行为许可。管理 API/CLI 不依赖模型或 GUI；运维 OpenClaw 具有独立实例、凭据及生命周期。旧 AIRuntime、Foundation 和固定第二次 Expression 调用不作为新产品结构前提。

目标设计：第 4、6、8 章。
共享合同：[认知与主动性](../integration/cognition-agency.md)。
