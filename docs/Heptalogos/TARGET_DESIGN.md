# Heptalogos 目标设计

## 1. 系统定义

Heptalogos 是持续 Subject 的产品运行与行为系统。它承载真实即时通信及其他环境中的交互输入、主动性、行为判断、承诺、外部效果、产品管理和长期可靠运行。

Heptalogos 处理的不是“一个请求对应一句回复”的短生命周期智能体，而是同一个逻辑 Subject 如何跨时间、会话、平台、模型、进程和产品代次保持行为连续性，并在外部世界存在延迟、冲突和不确定性的情况下，以可追溯、可治理、可恢复的方式行动。

Subject 的长期认知由 Nous Wave 维护。Heptalogos 使用认知上下文、期望条件和其他正式认知输入形成行为判断，同时保留自己的行为 Authority。模型、提供方、提示词、会话、Host、呈现界面和系统助手都不是 Subject 本身；替换这些执行条件不会自动创建新的 Subject。

### 1.1 产品目标

Heptalogos 的目标包括：

- 在异步、多会话、多平台环境中保持同一 Subject 的行为连续性；
- 将观察、判断、行为、表达、承诺和外部结果区分为可追溯的语义对象；
- 允许 Subject 等待、沉默、取消、延迟或主动行动，而不是把“立即回复”当成唯一成功路径；
- 在外部副作用结果无法证明时诚实保存 `uncertain`，不伪造成功或失败；
- 让管理员的 Subject 交互、产品管理和机器运维拥有清晰且彼此独立的 Authority；
- 在模型、组件、进程或呈现界面替换后继续保持权威产品事实和 Subject 身份；
- 让实现机制、提供方和框架服从稳定产品合同，使基础设施变化不会重新定义 Subject 或产品 Authority。

### 1.2 目标产品形态

一个逻辑安装（Installation）运行一个当前 Product Host Authority，并承载一个持续的 Subject。呈现界面可以有多个实例和形态，但其生命周期不决定 Host、Subject 或持久产品状态的生命周期。

产品由以下长期角色组成：

- Installation：可识别、可管理、具有独立生命周期根的逻辑安装；
- Product Host：长期运行的无图形产品宿主，承载正常产品 Authority、Subject 生命周期与管理合同；
- 持续 Subject：跨模型、会话、平台和 Host 重启保持连续身份的行为主体；
- 管理入口：面向命令行、API、自动化和外部呈现界面的正常产品管理合同；
- Subject Chat：管理员与 Subject 的正式直接交互通道；
- Machine Operations Plane：独立于 Product Host 的机器、部署和紧急运维域；
- Bootstrap / Recovery：正常产品路径不可用时仍能工作的有界恢复入口；
- Nous Wave：同一 Subject 的长期认知系统。

## 2. Subject、身份与领域所有者

### 2.1 Subject 身份

`SubjectId` 表示跨模型、进程、会话以及 Nous Wave / Heptalogos 的逻辑主体身份。同一 `SubjectId` 在两个系统间保持连续，但两侧不共享一个可变主体对象。

Heptalogos 拥有行为与产品运行状态，包括 Reaction、Pursuit、行为提交、Commitment、消息、外部效果、Subject 生命周期以及相应的产品管理状态。

Nous Wave 拥有长期认知，包括 Memory、Self、Social Cognition、Motivation、Cognitive Runtime 及其内部来源和修订。

提示词、上下文、检索结果、模型消息和提供方运行时对象都是一次执行的投影或机制，不能替代 Subject 的长期状态。

### 2.2 长期对象必须有正式所有者

任何持久产品状态必须由明确的领域所有者维护。共享数据库事务、共享进程或共享界面不会自动改变语义所有权。

派生视图、索引、缓存、遥测、编译后的提示词和提供方检查点可以重建；它们不能成为权威事实的唯一来源。

## 3. Authority 模型

Heptalogos 至少区分以下 Authority：

### 3.1 Subject Authority

负责 Subject 的行为判断、行为采纳与拒绝、Commitment、CommunicationCommit 和其他由 Subject 拥有的行为状态。

模型输出、检索结果、Nous Wave 认知、工具建议、Extension 推断和审查结果默认只是信息或提案。它们可以影响行为判断，但不能自行成为正式行为。

### 3.2 Heptalogos System Authority

负责产品级管理语义，例如 Subject 生命周期、配置生效、Extension 与资源管理、数据生命周期、审批和其他正式管理操作。

系统管理权限不因某个请求出现在 Subject Chat 中而自动获得，也不因调用者是模型或系统助手而自动获得。

### 3.3 Machine Operations Authority

负责机器、部署、进程、文件系统、严重故障诊断与紧急维护。它拥有独立凭据、生命周期和故障域，不与 Product Host 的普通 System Authority 混用。

### 3.4 Recovery Authority

Bootstrap / Recovery 提供小型、固定、本地且不依赖 AI 的恢复动作集合。它用于正常管理路径不可用时恢复系统可操作性，不是完整 System Authority 的替代物，也不是通用 root shell。

### 3.5 Authority 交接

跨 Authority 请求可以传递：

- 意图；
- 有界上下文；
- 原因；
- 发起主体；
- 来源证据。

权威交接不传递权限。目标 Authority 必须重新执行自己的身份验证、授权、风险评估、审批和提交规则。

## 4. 行为模型

### 4.1 Reaction

Reaction 表示一次当前情境的有界认知与行为处理。一个 Reaction 可以读取多个上下文来源、等待新材料、调用模型或能力、被更新输入取代、产生候选行为，或者以不通信/沉默结束。

Reaction 不是 Subject 的完整长期状态，也不是长期目标或承诺。

### 4.2 BehaviorIntent 与 DecisionCommit

`BehaviorIntent` 是一次行为判断中的候选结果。它在当前 Subject 状态、输入修订、行为政策、Capability、权限、Commitment 和其他约束下接受审查。

只有通过拥有者的正式提交，候选才形成 `DecisionCommit`。`DecisionCommit` 是已经发生的行为权威记录；模型文本本身不等价于行为提交。

如果决定所依赖的关键输入在提交前发生有效变化，旧候选必须失去提交资格或重新验证。

### 4.3 行为与表达分离

系统先确定是否行动、对谁行动、行动类型与目标，再生成具体文本、音频或其他表达。

`CommunicationCommit` 表示已经决定向外表达的语义承诺。表达阶段将其实现为具体语言或媒体，但不得悄悄改变已提交的行为种类、目标或 Authority。

沉默是一等合法行为。它可以表示经过审议后不回应、策略抑制、等待更合适的时机、当前能力不足或其他正式原因。

## 5. 主动性、Pursuit 与承诺

### 5.1 期望条件与 Pursuit

Nous Wave 的 Motivation 可以形成 `Desired Condition`，描述 Subject 在认知上希望某状态成立、停止、持续或避免。

Desired Condition 的存在不创建行为义务，也不直接取得外部行为 Authority。

Desired Condition 或 Pursuit 都不能直接派发外部效果。每项外部效果仍须属于 Heptalogos 已正式提交的具体行为，并接受独立的效果记录与结果核验。

Heptalogos 使用 `Pursuit` 表示行为侧已经采纳并准备持续投入行为资源的主动追求。Pursuit 引用 `Desired Condition` 的精确修订，并保留其行为侧身份、采纳来源、状态和重新核验关系。

### 5.2 Pursuit 的持续性

Pursuit 可以跨多个 Reaction、会话和时间窗口持续。它可以：

- 形成新的认知处理机会；
- 改变行为判断所需的上下文；
- 参与多个主动追求之间的资源竞争；
- 因政策、能力、Commitment、时间、风险或资源约束被暂停、重新核验或结束。

主动行为受 Heptalogos 的行为政策、隐私和社会边界、安静时段与打扰限制约束。机会出现本身不等于许可或决定；主体可以行动、等待、抑制或结束追求。

`Desired Condition` 修订后，引用旧修订的 Pursuit 需要重新核验。期望条件被撤回不允许抹除已经发生的 `DecisionCommit`、Commitment 或 Effect 历史。

一次行为或外部效果失败只确定该次执行的结果，不自动判定长期期望失败，也不自动终结 Pursuit。Heptalogos 重新审查行为侧的后续追求；Nous Wave 根据带来源的行为结果评价认知期望。

### 5.3 对象分离

以下对象不可合并：

- Desired Condition：认知上的期望；
- Pursuit：行为侧持续主动追求；
- BehaviorIntent：一次具体判断中的候选行为；
- ActionPlan / InteractionPlan：实现一次已接受行为的步骤和组织；
- Commitment：Subject 已经承担的社会或行为承诺；
- Obligation：已经形成、需要后续履行或处理的约束；
- Effect：外部世界中的 consequential outcome。

它们分别维护身份、生命周期、来源和状态。

## 6. Nous Wave 认知接入

Nous Wave 是 Subject 的长期认知系统。Heptalogos 通过稳定的认知查询、上下文贡献、提案与回执、可用性和生命周期合同与其协作。

认知系统返回的内容必须能够保留其对象身份、修订、provenance、实际 formation basis、适用范围和可修订的 epistemic judgment。Nous Wave 的 cognition 表示 Subject 当前或历史认知，可能包含误解、矛盾与后续纠正；grounded、真实来源与模型生产者身份不保证客观正确性。Heptalogos 可以据此调整注意、Reaction、Pursuit 和行为判断，但不复制 Nous Wave 的内部认知模型。

消息、认知和其他上下文材料保留来源、用途和敏感范围。授权作用域先于语义相关性筛选；相关性不能扩大数据的允许用途。外部内容、检索结果和认知提案也不能成为系统指令或行为 Authority。

Heptalogos 将行为结果、Commitment 状态和可观察外部事实作为有来源的回执提供给 Nous Wave。Nous Wave 可以根据这些材料更新自己的认知。

“行动完成”和“期望满足”是两个不同判断：一个 `ActionPlan` 完成后，`Desired Condition` 仍可能未满足；期望条件已满足也不要求抹除相关行为历史。

安全政策、管理员强制规则、行为许可和有外部后果的效果审查由 Heptalogos 维护，不由可演化认知取得规范 Authority。

当 Nous Wave 不可用、信息过期或只能提供部分认知时，Heptalogos 依据自身 Readiness 和行为合同决定哪些功能可以降级、哪些行为必须阻塞；Product Host、Management 与 Recovery 的基本可操作性不依赖完整认知持续可用。

## 7. 消息、Subject Chat 与外部效果

### 7.1 消息领域所有权

外部协议驱动器（Driver）负责协议机制和边界映射；Messaging 领域负责规范消息语义。

规范消息模型至少区分平台、账号、远端会话、参与者、规范会话、规范消息和消息片段。不能依赖昵称或界面标签推断跨平台统一身份。

`MessageFact` 是不可变的权威消息事实。编辑、撤回、reaction 和回执等变化通过新的事实表达，不通过覆盖旧历史伪造“从未发生过”。

### 7.2 ConversationMailbox

ConversationMailbox 组织待处理消息事实的引用、当前 Reaction 和会话处理状态。它不复制 `MessageFact`，也不形成第二份消息真相。

### 7.3 Subject Chat

Subject Chat 是管理员与持续 Subject 之间的正式直接通道。它必须遵守与其他消息相同的消息和行为合同，不能成为呈现界面直接调用 Reactor 的快捷路径。

管理员在 Subject Chat 中可以具有特殊的 Subject 治理身份，但这仍属于 Subject Authority。系统管理意图必须显式交接到 System Authority。

本地 Subject Chat 的出站消息先形成权威 `MessageFact`；发送到界面客户端只是该事实的投影。客户端断线、关闭或漏掉实时事件不会把它变成外部效果不确定。恢复后通过权威查询或投影重新取得消息和状态。

### 7.4 EffectOperation

有外部后果的写入由明确的 `EffectOperation` 管理。外部效果至少允许以下结果：

- `prepared`：尚未派发；
- `dispatching`：正在派发；
- `succeeded`：已确认成功；
- `failed`：已确认失败；
- `uncertain`：结果无法确认。

传输成功不等于外部效果已经确定。网络超时、连接断开或提供方重试不得自动解释为“肯定失败”；无法证明幂等时也不得静默重发。

外部结果完成后重新进入产品事实和 Evidence 流，不能通过隐藏回调直接改写认知或行为状态。

## 8. Product Host 与持续运行模型

### 8.1 无图形界面的 Product Host

Product Host 是长期运行的无图形产品宿主。它承载：

- 运行时组合；
- Service 与 Capability 的可用性；
- 权威持久化访问；
- Messaging（消息领域）；
- AI 与 Capability 调用边界；
- 持久义务；
- Subject 行为处理；
- Management Contract（管理合同）；
- Evidence（证据）与 Execution Lineage（执行血缘）；
- 生命周期与恢复协调。

Presentation 不嵌入 Host Authority，也不决定 Host 生命周期。

### 8.2 Desired State 与 Actual State

长期意图和当前运行结果必须分离。

例如，Subject 可以持续保有“期望运行”的长期意图，同时因必要能力缺失而暂时处于阻塞状态。条件恢复后，运行时重新协调实际状态，不通过失败路径篡改长期意图。

### 8.3 持续协调

运行时不是一次性初始化和启动顺序，而是持续根据以下信息协调当前运行结构：

- Desired State（期望状态）；
- 当前组件和软件代次的运行资格；
- 配置；
- 组件间的依赖关系；
- 可用的 Service 和 Capability；
- 健康状态；
- 运行模式；
- 资源压力与准入状态。

冷启动只是第一次协调。

### 8.4 Readiness 与局部降级

Host、Management、Subject Base、External Messaging 和认知接入等部分可以有各自的 Readiness。非关键驱动器、提供方或 Extension 故障只影响依赖它的能力与就绪状态，不默认使整个 Host 不可操作。

Readiness 是显式的多状态产品语义，能够区分可用、运行中、降级、阻塞和失败等情形，而不是压成一个布尔值。Presentation 只能投影权威状态，不能用本地动画或连接状态猜测产品事实。

### 8.5 所有权与 fencing

任何能够提交权威变更或派发有外部后果效果的 Product Host 必须持有当前所有权。旧 Host、退休代次或失去当前运行资格的执行者不能继续取得新工作或提交当前结果。

所有权丢失时必须围栏隔离或停止提交；不能在原运行路径中悄然重新竞争并继续提交。

### 8.6 运行模式

系统可以进入安全模式、维护模式、紧急只读模式或 Recovery 等运行模式。它们收窄可执行行为和外部效果，同时保留诊断与恢复能力。

这些运行模式不静默改写长期 Desired State。

### 8.7 资源压力与准入

资源压力是显式产品状态。系统根据可观察的资源情况作出准入、降级、负载削减或阻塞决定，并使其对 Readiness 的影响可追溯。

提供方、队列、数据库连接池或其他实现组件的私有阈值不能暗中成为产品级准入政策。

在压力下优先保护恢复与必要管理、权威输入接纳与事实保全、已提交义务和外部效果协调，再考虑普通 Subject 工作和可选后台工作。

## 9. Service、Capability、Extension 与组合

### 9.1 Service 与 Capability

`Service` 表示稳定的长生命周期依赖合同；使用方依赖其合同，而不是具体提供方对象。

`Capability` 表示当前可用、可能由多个提供方实现的能力。能力可用性可以动态变化；提供方选择由稳定政策、兼容性和就绪状态决定，不能依赖注册或加载顺序。

服务依赖和多提供方 Capability 选择是不同问题；不能用注册或加载顺序代替其中任一语义。

### 9.2 Extension System

Extension System 是 Heptalogos 的统一模块运行环境，不只代表第三方插件。内建组件、第一方功能、驱动器、提供方和第三方 Extension 可以通过统一的生命周期与能力提供合同参与运行，但来源、信任等级和 Authority 仍分别判定。

### 9.3 Package、MicroSystem 与扩展能力

Package 是分发单位；MicroSystem 是运行单位。一个 package 可以支持一个或多个运行实例，运行实例也不等同于其代码或配置。

扩展可以通过 Heptalogos 拥有的合同提供 Service、Capability、驱动器、管理能力或 Presentation 投影。提供这些能力不赋予扩展相应领域的 Authority。代码代次、运行实例、配置、持久数据、秘密材料和派生数据拥有彼此独立的生命周期。

### 9.4 运行时边界

Extension 通过受限合同获得所需的 Service、Capability、配置、存储、Evidence、Execution Lineage 和生命周期能力；不获得 Host 根对象或其他所有者的原始权威存储。

通用框架、依赖注入、队列和扩展管理机制只提供运行支持，不形成第二套运行监督、Authority 或产品生命周期真相。

### 9.5 信任与隔离

签名、可信来源和权限声明不等于运行隔离。代码若在 Product Host 的同一进程中执行，就属于该进程的信任边界。

不可信代码必须运行在可证明的独立执行边界内；权限声明不能代替运行隔离。

## 10. 推理能力与集成边界

### 10.1 模型不是 Subject

模型、提供方、网关、协议和执行库属于可替换的推理机制。它们的更换、重新绑定或升级不改变 Subject 身份，也不产生 Subject、行为或系统 Authority。

每次模型调用都归属于明确的 Reaction 或其他有界活动。调用来源、适用范围、模型选择、资源限制和结果均保留足够的溯源信息。模型结果默认是信息或提案，不是权威状态。

### 10.2 Capability 与模型工具

Capability 是 Heptalogos 拥有的产品能力合同。AI Tool 只是把部分可用 Capability 投影为模型调用表面的一种形式。模型可请求已提供的能力，但不能创建能力、扩大其作用域或自行授予权限。

Capability 的可用状态、作用范围、风险、凭据、网络边界、代次和 Evidence 由相应产品 Authority 治理。模型库或扩展推断不能暗中改变这些规则。

### 10.3 Consequential 外部写入

发送消息、发布内容或修改远端资源等有外部后果的写入，不得隐藏在模型、工具循环或供应商的自动重试中。它们必须回到拥有该行为的计划与正式行为提交，并通过 EffectOperation 记录派发和外部结果。

### 10.4 集成协议

MCP 等集成协议提供编码、发现和传输机制，不因此获得 Extension、Subject、System 或 Capability Authority。远端提供的工具、资源和提示必须先按 Heptalogos 的政策、作用范围和效果语义进行规范化与审查，不能直接成为权威能力事实。

## 11. 产品管理、机器运维与管理员交互路径

### 11.1 权威管理合同

正常产品管理通过同一权威管理合同对外提供。CLI、HTTP/API、自动化和外部 Presentation 都是该合同的客户端或投影；业务规则不在各客户端重复实现。

管理变更应至少经历：

请求 → 规范化与验证 → 影响分析 → 身份验证、授权与风险评估 → 按需审批 → 所属服务提交 → 核验 → Evidence。

影响分析必须绑定当前输入与前提；当关键事实变化时，旧计划和审批不能自动授权新的结果。

### 11.2 直接管理（Direct Management）

直接管理是不依赖 AI 的确定性产品管理入口。管理员必须能够在没有 System Assistant 的情况下查看资源、Readiness、Subject 生命周期、配置、操作和 Evidence，并请求受治理的产品管理操作。

### 11.3 System Assistant / Maintenance Assistant

System Assistant 是独立 Machine Operations Plane 的产品体验。它可以解释状态、引导管理员，并在 Product Host 健康时通过正式管理合同请求普通产品操作。

当正常 Host/API/CLI 不可用时，Machine Operations Plane 可以依据独立机器权限执行机器级诊断和修复，但不得把这些行为伪装成普通产品管理变更，也不得把机器高权限凭据暴露给普通产品界面。

### 11.4 四条管理员 Authority 路径

产品明确区分：

- Subject Chat → Subject Authority；
- Direct Management → Heptalogos System Authority；
- System Assistant / Maintenance Assistant → Machine Operations Authority；
- Bootstrap / Recovery → bounded Recovery Authority。

它们可以共享产品视觉语言和身份语境，但不共享隐式权限。

## 12. 配置

配置属于正式产品语义，不等于散落的实现常量，也不等于某一种物理存储。每项配置由明确领域拥有，并具有适用范围、类型与约束、默认来源、敏感度、生效条件和实际使用方。

配置是否存在、普通管理员是否可见、是否可修改是三个不同判断。不可见或只读的配置仍有明确的所有者和 Authority。

不同配置范围可以由正式管理修订、声明式文件、领域原生配置源或只读派生视图维护。同一范围只有一个写入 Authority；文件解析结果、数据库投影和管理界面不能无意形成第二份权威事实。

影响行为的默认值必须有稳定来源。默认值或其来源发生变化时，系统将其作为明确配置变更处理，不能静默改变有效行为。

配置提案与配置生效分离。系统验证类型、语义约束、权限、影响和所需确认，再按声明的即时生效、重载、重启、维护或后续启动条件激活并核验结果。秘密材料由独立的 Secret Authority 拥有；配置可以引用秘密，但不保存明文。

## 13. 持久化、Evidence 与 Execution Lineage

### 13.1 权威事实先于异步义务

外部输入先成为权威事实，再形成后续持久义务。信号、通知、事件总线和唤醒提示只提示状态变化，不能承载唯一的持久真相。

权威事务保持短小，不跨模型调用、网络等待或人工等待。耗时推理在事务外执行；提交时重新验证所依赖的修订和权威版本。

### 13.2 持久义务

需要跨崩溃和重启继续处理的工作必须形成有明确所有者的持久义务。临时并发工作或提供方内部检查点不能成为唯一产品真相。

### 13.3 Evidence

Evidence 保存产品需要长期保留的来源、推导、调用、审查、提交、外部效果、管理操作和恢复结果。

Evidence 与遥测分离：遥测可以采样和过期；必需的产品 Evidence 不能因为数据导出、采样或仪表板而丢失。

### 13.4 Execution Lineage

Execution Lineage 为重要操作建立稳定的 Activity 身份，并记录其因果关系、关联、所有者、代次和结果。

Activity 身份不等同于可观测性 trace/span 身份。遥测是 Execution Lineage 的运行投影，不拥有执行血缘的 Authority。

### 13.5 追溯、重演与比较

重要行为和管理决定必须能够追溯到所依据的事实、修订、适用政策、调用来源、正式提交和外部结果，以便解释和比较行为轨迹。授权保留的证据引用提供这种依据，不要求重复复制受限内容。

确定性处理可以在隔离的分析过程中重演。模型、远程能力和外部效果的结果作为边界记录使用；分析性重演不得再次触发真实外部效果，也不得把历史结果当作外部世界当前状态。

## 14. 存储、DataOwner 与生命周期根

### 14.1 统一治理不等于统一物理存储

Foundation 统一所有者身份、生命周期、路径隔离、备份与恢复、清除与保留、可移植性、资源核算、健康状态和 Lineage；具体领域的数据模型、文件格式和存储引擎由语义所有者决定。

### 14.2 生命周期根

至少区分：

- 程序或 Package 代次；
- 运行实例元数据；
- 配置；
- 持久数据；
- 秘密材料；
- Blob 与 Artifact 内容；
- 缓存和派生索引；
- 运行、临时和会话数据；
- 备份与导出。

物理共置不等于生命周期所有权。升级或删除代码代次不自动删除配置、数据或秘密材料。

### 14.3 数据所有者（DataOwner）

复杂持久数据所有者必须说明其数据、权威或派生属性、适用版本、保留与清除要求、备份恢复和可移植性，以及资源和健康语义。

数据所有者可以选择托管关系存储、嵌入式存储、文件、专用索引或外部后端，只要权威状态对系统可识别，并参加正式生命周期治理。

### 14.4 Blob 与 Artifact

Blob 表示不可变、按内容寻址的字节；Artifact 表示具有所有权、来源、敏感度、生命周期和 Blob 引用的语义对象。

大内容不应因为业务对象需要引用它，就被重复复制到每条权威记录或文档中。

## 15. 备份、可移植性、更新与恢复

### 15.1 三种不同对象

系统明确区分：

- Installation Backup（安装备份）：恢复一个逻辑安装的产品运行基础以及各持久数据所有者参与的状态；
- Subject Bundle（主体包）：迁移由 Subject 拥有的可移植语义状态；
- Product Update（产品更新）：切换软件代次及其运行闭包。

它们不能共享一个模糊“导出/导入”语义。

### 15.2 备份闭包

Installation Backup 是各数据所有者共同形成的可恢复闭包，不等于复制单个数据库或目录。描述该闭包的清单保留各所有者与存储的身份、数据和合同版本、内容引用、所需软件代次、秘密材料的恢复要求，以及清除和保留约束。

不同存储后端不共享全局原子快照。协调过程只对需要的一致性范围建立最小屏障，分别取得可验证的快照或导出，再确认它们之间的引用闭合。

### 15.3 恢复语义

恢复会重新建立可运行的权威状态，但不会把外部世界回滚到备份时间点。

因此恢复后必须重新核验：

- 当前安装及其所有者关系；
- 身份、会话和授权是否仍然有效；
- 尚未完成的行为义务及其所属软件代次；
- 外部效果的不确定结果；
- 秘密、信任和所需软件来源；
- 已执行的数据清除和保留要求；
- 当前运行就绪状态。

无法证明某项外部效果是否已发生时，保留 `uncertain`，不得自动重发。恢复过程以权威事实和所有者状态重新协调；它不复活已正式清除的数据，也不伪造外部世界已经回滚。

### 15.4 软件代次

软件代次是不可变、可验证、可选择的运行闭包。新代次经过暂存、验证和切换后成为当前代次；失去当前资格的旧代次不能再取得新的当前工作。软件代次、持久工作所依赖的执行合同和扩展代次是不同版本轴。

回退是预先验证兼容性的恢复策略，不是简单切回旧目录。切换前必须证明数据、未完成义务、扩展、秘密与内容格式可由目标代次继续处理；无法证明时进入受保护的备份恢复或人工处理路径。

### 15.5 恢复原则

恢复优先级是：

1. 保全 Authority 与权威事实；
2. 保全外部效果的不确定性和已经存在的义务；
3. 进行有界清理与修复；
4. 无法证明安全继续时停止运行、隔离、阻塞或进入人工恢复；
5. 从当前权威事实重新协调。

恢复动作保持有界。无法证明安全继续时，系统明确阻塞、隔离相关代次或交由人工处理，不以复杂自动回退掩盖未知结果。

## 16. 呈现与 Control Plane 语义

Presentation 是产品合同的投影。浏览器、桌面端、CLI 或其他界面可以采用不同交互形态，但它们不拥有领域 Authority。

Control Plane 是同一产品的管理与 Subject 状态呈现界面，可以呈现 Subject 状态、Subject Chat、Direct Management、System Assistant 和注意力提示。具体页面、视觉样式、动画和前端实现由外部 Presentation 工作流负责，不进入本目标设计。

### 16.1 状态来自权威读取视图

Presentation 不通过颜色、动画、实时连接或本地缓存猜测产品状态。Subject 的期望状态与实际状态、Host 状态、管理员会话和 Subject 身份必须保持独立语义。

Presentation 断线、关闭或漏掉实时事件不得导致权威事实丢失；重新连接后通过正式查询和读取视图恢复。

### 16.2 渐进信息呈现

Control Plane 根据用户当前任务和风险渐进展示状态与操作，不要求始终展示所有内部资源。界面简洁不意味着后端丢失可治理状态；完整的机器可读合同与面向人的清晰呈现可以同时存在。

## 17. 目标物理结构

Heptalogos 面向一个逻辑安装、一个当前 Product Host Authority 和一个持续的逻辑 Subject。其目标部署包含以下物理边界：

- 一个长期运行的无图形 Product Host；
- 一个由 Foundation 协调事务性权威事实的核心；
- 由各语义所有者选择存储，不强迫不适合集中存放的数据共用后端；
- 独立的外部 Presentation 客户端，通过正式管理与 Subject 合同访问产品；
- 独立 Nous Wave 认知系统，与 Heptalogos 共享 `SubjectId` 并通过版本化语义合同交互；
- 独立 Machine Operations Plane，与 Product Host 的权限、生命周期和故障域分开；
- 有界 Bootstrap / Recovery 能力，在正常产品路径失效时仍能执行必要恢复。

正常产品 Authority 和机器运维 Authority 不共享凭据或生命周期。Foundation 协调权威事实；各领域所有者仍负责自己的数据语义及恢复合同。

## 18. 核心不变量

以下原则在实现机制变化时仍必须成立：

1. Subject 身份不等于模型、提供方、提示词、会话、Host 或 Presentation。
2. Heptalogos 与 Nous Wave 共享 `SubjectId`，但分别拥有行为状态与认知状态。
3. 提案不自动取得 Authority。
4. `Desired Condition` 不自动创建 `Pursuit`，`Pursuit` 不自动创建外部效果。
5. 行为决定与表达分离；沉默是合法结果。
6. 有外部后果的效果允许结果为 `uncertain`。
7. Subject Authority、System Authority、Machine Operations Authority 和 Recovery Authority 不隐式互换。
8. Desired State 与 Actual State 分离；失败或安全模式不静默改写长期意图。
9. 权威事实先于异步义务；唤醒信号、缓存和提供方内部检查点不替代持久真相。
10. Presentation、遥测、派生索引和框架对象不取得领域 Authority。
11. Service 与 Capability、Package 与 MicroSystem、程序与数据的生命周期保持区分。
12. 配置语义与配置存储分离；同一作用范围不允许多个隐式写入 Authority。
13. 统一存储治理不等于统一物理存储。
14. 旧 Host 或旧代次失去当前所有权后，不能继续提交当前变更或派发外部效果。
15. Installation Backup、Subject Bundle 和 Product Update 是不同产品合同。
16. 重要行为、管理、外部效果和恢复均保留来源、Evidence 与 Execution Lineage。
17. 数据的敏感范围和允许用途先于相关性；模型、检索和外部内容不能扩大访问范围或写入权限。
18. 主动行为受明确政策和用户控制；沉默、延后和抑制是合法结果，不得以虚构现实经历、虚假效果或情感压力换取拟人效果。
19. 无法证明安全继续时允许明确阻塞、fence 或人工恢复，不以“看似继续运行”代替真实性。
