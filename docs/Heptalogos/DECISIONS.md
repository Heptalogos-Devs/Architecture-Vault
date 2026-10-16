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

**决定：** Heptalogos 复用 Nous 正式认知集成与 OpenClaw 原生模型/工具/渠道/子 Agent 能力，继续拥有生活活动、消息感知、行为采纳、外部效果和产品管理。主体审议先决定行为，所有生成式主体表达和人格动作经过独立可配置 renderer，再由窄语义读回与 NarrativeCommit 采用；真实执行/外发前必须获得行为许可。管理 API/CLI 不依赖模型或 GUI；运维 OpenClaw 具有独立实例、凭据及生命周期。旧 AIRuntime 与 Foundation 不作为产品结构前提；独立渲染职责必须存在，不以执行模型末段或框架自动 announce 代替。

目标设计：第 4、6、8 章。
共享合同：[认知与主动性](../integration/cognition-agency.md)。

### QQ 日常宿主、单一派发与实际恢复

**决定：** 第一方 QQ Channel 统一同账号协议接收和发送；Messaging 先保存事实，Life 再决定实际接触。行为采纳后交唯一 OpenClaw durable send，未知发送不自动重放。管理进程先于模型可用，OS 服务管理器监督进程，产品不复制通用运行图。活动、历史覆盖与真实结果支持同一 Subject 停止后续接，虚拟时间不替代实际跨日恢复。

目标设计：第 4、7、8、11、17 章。
共享合同：[认知与主动性](../integration/cognition-agency.md)。

### 世界生活、认识与听众版本分别连续

**决定：** WorldLife 拥有规则/日程、稳定人物/场景和正式已实现虚拟事件；无 IM 也能推进，默认离线按现实经过时间有界实现。专业执行、主观审议、人格渲染与窄语义读回分别绑定原生职责。NarrativeCommit 在短本地事务采用兼容生活细化、Claim、承诺和一份待派发请求。事先明确的隐瞒/谎言保留真实与听众版本，实际工具和发送状态不受改写。后台知识只有正式交给主体并接触后才可能成为个人认识。

目标设计：第 4、6、11、13 章。理由：持续独立主体的生活与知识连续性需要正式 owner，渠道或单次模型文本不能替代；短事务与原生执行仍然沿用。
共享合同：[认知与主动性](../integration/cognition-agency.md)。

### 程序组织单前台 Reactor 与局部交互

**决定：** 同一 Subject 只拥有一条前台主观决定链，后台世界/专业任务可并行；程序组织机会、情境卡、正式动作、交接与采用，强审议作语义选择。手机/QQ/浏览器/世界动作产生真实读取与 owner 结果；课表与 Seed 独立，Attention 全局选择，精力按已实现区间积分。理由：多群不应形成多个同时决策的主体，模型文本也不能替代实际操作；复用现有运行身份与短提交，不增通用运行平台。

目标设计：第 4、6、11 章。具体工程初值由代码仓配置/Spec维护。
共享合同：[认知与主动性](../integration/cognition-agency.md)。

### 同步继续信息与单原生后台压缩

**决定：** 关键进展同步保存；后台摘要只覆盖捕获的完整回合前缀，以原生 CAS 保留新尾部，硬超窗才前台等待。Activity/WorkContext、原生摘要、长期认知各有用途。理由：主体继续工作不能等待人格反思，后台总结不能覆盖新到消息或工具成果。

目标设计：第 6 章。共享合同：[认知与主动性](../integration/cognition-agency.md)。
