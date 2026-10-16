# Nous Wave 目标设计

本文是 Nous Wave Target Design 的唯一直接编辑来源。它定义长期目标语义、领域边界、对象关系、权威、不变量、运行时合同、查询语义、持久化原则和与 Heptalogos 的系统边界。跨系统详细合同由[认知与主动性合同](../integration/cognition-agency.md)唯一维护；任何发布物都只能从本文派生，不能形成并行 Authority。

## 1. 系统定义与适用范围

### 系统定义

Nous Wave 是面向长期运行人工智能主体的认知与人格平台。系统维护跨模型、会话、进程和检索索引持续存在的主体认知，使主体能够保留经历、修订认知、维护自我与社会关系，并在后续推理和行为中按来源、权限和上下文重新取得这些认知。

主体由稳定的逻辑身份及其认知状态定义。模型、模型服务商、会话和进程是可替换的执行条件；模型更换不得改变主体标识，也不得使持久认知失去来源谱系、修订历史或当前状态。

Nous Wave 负责认知语义与认知权威。通用数据库、索引、向量检索、对象存储、模型调用和协议传输由成熟基础设施承担；这些机制可以替换，只要不改变本文规定的对象身份、领域归属、写入权限和可追溯性。

### 能力组合

同一套基础语义支持不同能力组合，不建立彼此分叉的产品实现。

| 能力组合 | 组成 | 用途 |
| --- | --- | --- |
| 记忆型能力组合 | 主体基础、记忆、认知运行时、认知查询、检索服务、外部资源接口 | 为普通智能体、检索增强生成或其他调用方提供长期、可修订、可追溯的主体记忆。 |
| 完整主体能力组合 | 记忆型能力组合，加上自我、社会认知、动机和跨领域离线认知 | 维护长期主体的自我理解、社会世界、目标与离线认知演化。 |

高级认知领域建立在同一主体基础、证据模型、修订机制和查询体系之上。未启用某个高级领域时，其缺失不得削弱记忆型能力组合的完整性。

记忆是最小完整认知能力。主体可以只供给记忆而不启用自我、社会认知或其他高级领域；这种能力组合仍必须能够独立启动、形成、查询、服务、恢复和清除记忆。自我、社会认知、动机以及后续高级领域是可选的认知所有者，不因共享基础设施而成为记忆运行的前置条件。

进程能力与主体能力分别表示两种不同状态：

- **Process Capability** 表示当前部署实际提供并可启动的领域实现上限；
- **Subject Capability** 表示某个主体已经被明确供给的领域集合。

主体能力不能超过进程能力。未供给的领域没有隐式空状态，也不通过空表、占位对象或“查询不到对象”来模拟启用。新主体的默认供给可以由管理配置决定，但主体创建后保存展开后的 typed capability set；后续默认配置变化不隐式改写既有主体。

### 主体与模型

主体标识（SubjectId）是跨限界上下文保持一致的逻辑身份。模型实例、模型名称、供应商账户、聊天线程、登录会话和宿主进程均不得作为主体身份。

模型输出只能以明确的角色进入系统：生成派生表示、形成候选提案、执行重排或生成表达。模型输出本身不具有认知权威。任何持久认知写入都由相应领域所有者按照当前对象状态、证据、权限和并发条件决定。

### 设计抽象边界

系统架构固定语义所有权、对象关系、生命周期边界、运行时边界、查询语义、持久化不变量以及与 Heptalogos 的系统边界。具体算法参数、数据库表、接口字段和部署细节可以在保持这些语义约束的前提下独立演化。

## 2. 系统不变量与权威模型

### 认知 Authority 的含义

持久接受一项 cognition 表示它属于 Subject 当前或历史认知状态，不表示其命题客观为真。Memory、Tag、Schema、Journal、Self 和其他认知领域可以保存误解、局部解释、矛盾、过时判断、后续纠正和持续错误；内容错误不会使其精确身份、来源与演化历史失效。

Owner 严格保证自己控制的结构事实：Subject 归属、对象与不可变 revision 身份、provenance lineage、真实 formation basis 引用、权限、生命周期、并发、幂等、清除、类型化时间与历史视图。自然语言蕴含和事实正确性属于认知质量，不能作为所有 owner 的通用不变量。模型即使返回结构化输出，也只产生提案或派生表示；领域按自身合同提交结构合法的认知，后续认知可以纠正、反驳或保留它。

结构破坏与认知质量错误分别评价。跨 Subject 引用、缺失 basis、可变 head 冒充 exact revision、未来状态进入历史切面、越权或 purge bypass 必须阻止；错误归因、时间解释错误、Tag 过度合并和未能纠正属于可追踪的认知质量问题。

### 核心不变量

| 不变量 | 含义 |
| --- | --- |
| 主体身份与模型身份分离 | 主体可以更换模型、供应商和运行进程而保持同一逻辑身份。 |
| 材料、观察事件与认知对象分离 | 原始内容、主体的一次实际接触和长期认知分别拥有独立身份。 |
| 来源提及与认知指向分离 | 来源中出现某实体，不等于形成的认知必然以该实体为语义对象。 |
| 来源、形成依据与认识判断分离 | provenance 保证实际 lineage，formation basis 表示实际输入，epistemic judgment 表示可修订的语义解释。 |
| 证据谱系与独立佐证数量分离 | 多个派生表示如果共享同一来源祖先，只构成同源证据。 |
| 认知权威、认知运行时与服务投影分离 | 可重建索引、运行时驻留状态和持久认知分别维护。 |
| 候选提案与权威认知分离 | 模型、离线认知和跨领域推理默认只产生提案，目标领域所有者决定是否提交。 |
| 检索、呈现、实际使用与长期强化分离 | 被召回或进入上下文不自动增加长期认知支持度。 |
| 可访问性、相关性、抑制与清除分离 | 回忆难度、当前查询相关程度、普通访问限制和破坏性删除使用不同状态与权限。 |
| 配置与语义不变量分离 | 可调参数、策略和资源预算可以配置；对象身份、领域所有权、不可变修订、幂等语义、精确修订依赖和清除语义不得通过配置关闭。 |
| 配置能力与暴露层级分离 | 配置项先具有稳定身份、类型、默认值、校验和作用域，再由元数据声明 Developer、Advanced 或 Standard 暴露等级。系统不变量不属于可修改配置层级。 |
| 配置快照与执行一致性 | 一次认知形成、查询或服务投影构建使用固定的解析配置快照，不从多个时间点拼接混合策略。 |
| 认知目标与行为承诺分离 | Nous Wave 保存目标和关切；有约束力的承诺、义务和外部执行由 Heptalogos 管理。 |
| 外部资源与主体认知分离 | 搜索结果和知识库内容只有在主体实际接触并经过认知形成流程后，才可能成为主体认知。 |

### 类型化权威

系统不使用一条覆盖所有语义的全局优先级。不同权威类型分别作用于其负责的事实和操作。

- 来源与证据权威：精确记录材料内容、观察事件、来源区域与实际派生过程；来源中的自然语言主张不因被记录而成为客观事实。
- 认知权威：由记忆、自我、社会认知和动机等领域维护主体当前接受的认知及其修订。
- 行为与规范权威：由 Heptalogos 维护允许、禁止、承诺、义务、行为决策和外部效果。
- 管理权威：负责主体生命周期、抑制、恢复、清除、配置和其他显式管理操作。

同一输入可以同时影响多个权威类型，但必须通过各自的领域合同分别处理。例如，一条用户消息首先形成来源事实和观察记录；它可以触发自我或记忆提案，也可以触发 Heptalogos 的行为策略调整。任何一个结果都不能替代其他权威类型的判断。

### 跨领域提案

跨领域变化统一通过类型明确的提案传递。提案至少引用目标领域、目标操作、实际输入对象及其修订、formation basis、provenance、生产者身份和形成上下文；需要认识关系时另行声明 typed epistemic judgment。目标领域在提交前重新核验来源可用性、当前对象版本、生命周期、访问控制和并发版本。

一个领域不得直接修改另一个领域的权威对象。跨领域原子一致性通过提案引用、提交序号和结果回执建立，而不是通过共享可变对象实现。

### 管理操作

自然语言内容不自动获得管理权限。抑制、恢复和清除由显式管理接口和授权上下文触发。普通对话中出现“忘记”“不要再提”等表达时，系统可以记录为观察、偏好或管理建议；破坏性清除仍需独立的管理授权。

### 配置基础服务

Configuration Service 是与主体基础同层的共享基础设施，负责配置描述、解析、覆盖、快照和来源诊断。需要运行策略或资源参数的领域所有者注册自己拥有的配置 key、类型、参考默认值、校验、作用域、应用方式和暴露等级；领域算法接收解析后的 typed policy，不直接从全局配置按字符串读取。

可修改配置按 Developer、Advanced 和 Standard 三个暴露等级描述。Developer 设置面向部署、底层算法和系统管理；Advanced 设置允许有经验的用户调整重要策略或成本；Standard 设置只用于普通用户能够理解且安全修改的产品行为。对象身份、修订、生命周期、并发、幂等、权限和清除等系统不变量不是配置项。

配置解析支持 reference default、部署文件、持久 system override 和持久 subject override 的确定性覆盖顺序。配置项声明 SystemOnly 或 SubjectOverrideAllowed；主体覆盖不能越过作用域。配置修改属于管理权威，不取得任何认知领域对象的写入权。一次 query、认知形成或 Serving generation 在 operation 开始时固定一个 immutable snapshot，并在相关诊断、形成记录或服务代次中保存实际影响该结果的 key subset digest。

启动可以保留极小的 bootstrap configuration，以便在配置服务打开前获得数据库、对象存储和 Serving 根目录等鸡生蛋参数。算法、查询、可访问性、拓扑和领域形成策略不因此建立第二套 Kernel 全局配置入口。Configuration Service 不成为全局 service locator、领域语义权威、动态插件注册表或跨进程 hot-reload bus。

## 3. 认知领域与主体边界

### 领域所有者

顶层认知领域按照稳定身份、修订、生命周期、查询语义和写入权限划分。领域名称描述语义所有权，不要求一一对应独立进程、代码包或数据库。

| 领域 | 职责 |
| --- | --- |
| 主体基础 | 主体标识、证据基础、跨域引用、生产者标识和共同时间/版本语义。 |
| 记忆 | 长期记忆、经历片段、日记、认知图式、标签和关联证据。 |
| 自我 | 主体对自身身份、角色、能力、倾向、价值和叙事连续性的长期认知。 |
| 社会认知 | 主体视角下的人际与群体关系、社会角色以及具有社会作用域的语言惯例。 |
| 动机 | 愿望、目标、关切和面向未来状态的优先关系。 |
| 认知运行时 | 会话、活动认知、工作上下文、注意分配、即时评价、驻留集和调用方工作集。 |

经历维护、日记维护和离线认知属于跨领域工作流。它们可以读取多个领域并产生提案，但不形成独立的超级权威。

### 领域对象与领域边界

一个领域可以拥有多种一等对象。对象是否需要独立身份，由其生命周期、修订、写入和查询合同决定，而不是由术语数量决定。记忆域因此可以同时拥有记忆、经历片段、日记和认知图式；社会认知可以同时拥有关系认知和语言惯例。

领域间通过稳定引用连接。引用必须指向对象和必要的修订身份，不通过复制另一领域的完整状态建立一致性。来源发生修订、撤回、抑制或清除时，依赖对象根据自身合同进入重新核验、冲突或失效状态。

### 认知对象的可引用地址

面向模型、Agent 和人类工具的可引用地址与显示名称、内部权威身份分别维护。
>
显示名称和别名用于发现候选，可以变化，也可能在同一主体内产生多个候选。发现结果唯一时可以绑定到稳定引用；存在多个候选时返回歧义及候选，不通过语义相似度、向量检索或模型猜测选择身份。
>
系统为需要被模型或 Agent 精确继续引用的对象提供稳定、语义中立的 Lexical Reference。Lexical Reference 解析到对应领域的 Authority identity；它不承担对象的可变语义描述。对象改名、Tag 修订或显示描述变化不会重新分配既有稳定地址。已经进入历史引用的地址不得重新绑定给另一个对象。
>
Nous 自己拥有的认知对象继续由各领域 Authority identity 决定真实对象身份。Host-owned Entity 和 Resource 继续保留宿主 canonical identity；Lexical Reference 不创建第二套实体权威。
>
具体地址编码、词表、prefix 和存储方式属于代码仓库 Spec。

### 主体供给与能力配置

主体创建时由宿主或独立客户端分配 SubjectId，并按所需能力组合供给对应认知领域。未启用的领域没有隐式默认状态，也不通过空表、空插件或占位对象模拟存在。

Subject 是独立、持续的个体；数据管理者、Host、模型或执行者的身份不创建认知上的从属关系。主体创建可无认知种子，也可提供用于初始自我认知和倾向的来源。无 Seed 时只创建实际请求的能力和结构事实，不生成个人传记、虚构经历或默认人格量表。系统与行为宪制由宿主或 Heptalogos 的规范权威维护，不通过认知种子取得行为上的最高权限。

### 主体分支

主体分支创建新的 SubjectId。分支可以共享分支点之前的不可变来源和认知历史，但分支后的对象头、对象纪元、运行时状态、服务投影和管理生命周期相互独立。

恢复同一主体的备份属于身份连续性的恢复操作；克隆或分支属于创建新主体。二者在管理接口和审计记录中必须区分。

## 4. 证据、来源与时间

### 来源对象

Nous Wave 以可追溯来源作为认知形成的基础。来源层至少包含原始材料、观察事件、派生表示和证据引用。

- 原始材料（Artifact）：稳定的内容实体，可以是消息载荷、文件、网页快照、图像、音频、工具输出或其他材料。
- 观察事件（ObservationOccurrence）：主体在特定时间、渠道和上下文中实际接触某份材料或事件的一次记录。同一材料可以对应多次观察事件。
- 派生表示（DerivedRepresentation）：由解析器、光学字符识别、模型或其他转换生成的版本化表示，保存生产者、版本、输入来源和区域映射。
- 证据引用（EvidenceRef）：指向观察事件、来源区域、派生表示或派生区域的稳定引用。

原始材料的内容去重不得消除观察事件身份。主体两次看到相同内容时，可以共享材料实体，但必须保留两次实际接触。

### 来源谱系

所有派生表示保存完整来源链。多个摘要、转写或模型派生如果来自同一原始来源，只构成同一来源祖先的不同表示。系统计算独立佐证时以来源祖先和形成过程为依据，不按文本数量、向量点数量或派生表示数量计数。

生产者签名记录生成派生表示或提案所需的实现身份，包括模型、版本、工作流和关键配置。生产者签名用于重建、失效判断和审计，不成为认知权威状态本身。

### Provenance、formation basis 与 epistemic judgment

三层语义分别维护：

- **Provenance** 回答对象实际源自哪些来源、观察、表示和生产者，是由 owner 精确核验的结构谱系。
- **Formation basis** 回答形成该 cognition 或 proposal 时实际使用了哪些来源或 cognition 输入。合法 basis 不证明输入蕴含认知文本；错误解释仍可以具有真实且精确的 basis。
- **Epistemic judgment** 表示 Subject 或系统认为某项 cognition/evidence supports、contradicts、corroborates、weakens、corrects、counterexample 或 inferred-from 另一项内容。这些关系是可修订、可争议的语义判断，不能从“形成时使用过”自动推得。

Episode/Journal 的成员、来源区域与表示映射等结构关系按自身类型表达，不伪装为认识支持。`support` 只用于实际认识关系；query result 的 source/basis/derived-from handle 暴露 lineage，不承诺事实证明。模型生产者身份帮助分析错误，但不能替代来源根独立性。

### 证据依赖与独立佐证

证据是否独立由来源谱系决定，不由证据记录数量、文本数量、派生表示数量或模型数量决定。

系统保存来源、观察、派生表示、认知推导和生产者之间的可追溯依赖关系。多个 EvidenceRef 若回溯到同一来源祖先，或其中一个由另一个直接派生，必须保留这种依赖关系。

领域在需要判断独立佐证时，从来源谱系派生依赖关系。至少能够区分：

- 同一来源根；
- 共享派生路径；
- 部分共享来源；
- 已知独立来源；
- 来源依赖未知。

来源依赖未知时不得自动按独立佐证处理。认知 Authority 不保存一个能够替代来源结构的全局统一置信分数。领域可以根据具体任务计算认识状态、证据充分性或服务排序，但这些派生结果不得删除或覆盖底层 provenance。

### 世界经历、运行资料与陈述来源

受信 Host 世界操作已采用的 `world_realized` 事件，在相应角色实际接触可见投影时成为合法虚拟经历来源。它保留 world/event、发生范围、世界内感知点、真实生成/交接/记录时间、可见 actor 和 producer/规则及共同起源。合法虚拟经历可以支持该世界的 Self、Memory、关系、语言惯例和期望评价，不证明真实平台效果或现实社会共识。

初始设定、计划、世界作者草稿、普通模型输出、主观 belief 和实际 statement 分别标明。`execution_only` 内容属于后台执行，不进入 Subject Observation/Episode/反思候选；正式释放后创建 `subject_experience` contact，引用原结果。身份与性质来自认证调用绑定，模型不能自填字段冒充世界 owner。主体说过某话只证明表达事实，不认证话中命题。

虚拟 actor 使用 Host world-scoped EntityRef；多个 NPC 若共享生成源仍保留同源关系。知识/社会来源的独立性不由 actor 数、模型数量或重复自述推导。世界隐藏事实不进入主体候选、摘要或长期认识，普通删除和传播限制同样适用于这些来源。

### 来源提及与认知指向

来源提及（EntityMention）记录材料某一区域明确出现的实体。认知指向（CognitionAboutness）记录某项认知在语义上涉及的实体、角色或关系。二者分别维护。

认知指向可以由多个来源共同支持，也可以在来源中没有出现规范实体名称时通过其他证据得到。来源提及不能因为某个认知指向该实体而被反向伪造。

### 时间语义

系统分别记录以下时间：

- 发生时间：外部事件实际发生的时间或时间范围。
- 观察时间：主体实际接触事件或材料的时间。
- 有效时间：某项主张在所描述世界中成立的时间范围。
- 形成时间：主体形成某项认知的时间。
- 记录时间：系统持久化相应记录的时间。
- 权威提交序号：同一主体范围内用于确定持久提交顺序的单调序号。

未知时间保持未知。时间范围允许开放端点。读取层可以派生最早、最晚或聚合时间视图，但派生值不写回为新的来源事实。

发生、观察、有效和形成时间通过 DomainStamp 明确所属域、点/范围或未知；记录时间和 Authority 提交顺序保持现实 UTC 及真实提交次序。世界身份与时间域是不同引用，没有显式映射的跨域比较返回未知。真实 QQ/网页/工具接触不允许回填观察时间。

已实现故事中的 `knowledgeAtWorldTime` 与数据库历史的 `asRecordedAt` 分别查询。恢复时晚实现的虚拟见闻保存原世界发生/感知点与当前实际生成、接触和提交时间；它可用于故事时间切面，不能进入早于提交的数据库切面。既有 Claim 和知情记录约束晚实现，无法相容时形成当前新发现或拒绝，不回填成早已知道。

### CognitiveClock 与 TemporalFrame

Subject CognitiveClock 是主体认知相对时间的唯一基准。在线 Host 可使它跟随现实时间；历史重放、模拟和测试可以独立设置或推进。查询准备捕获一次 clock，固定相对时间的绝对解释；基础设施 timeout、retry 和 worker lease 继续使用基础设施时间。

TemporalFrame 统一查询的认知时间基准、Authority view 和 revision view，同时保留 scoped five-axis filters。发生、观察、有效、形成和记录时间可以在同一 scope 中同时约束，按交集解释；不同时间轴不互相替代。

Authority view 默认为 current，也可以选择 as-of：读取该 Subject 在指定现实提交截点之前已经存在的有效状态。Memory、Tag、CognitiveSchema、Episode、Journal 的 effective revision、lifecycle、Tag aliases 与 merge/split canonicalization、有效 AssociationEvidence 都按该时刻解释。未来形成或改变的认知不得通过候选、描述、向量或拓扑进入历史查询。

revision view 默认为所选 Authority view 的 effective head。显式 history 允许该视图中 eligible historical revisions 成为独立候选，保留对象和修订身份，并继续满足 as-of 与五轴约束。

当前 query text 与 WorkContext 的 purpose/context_text 可以表达现在提出的问题。QueryContextSnapshot 排除 as-of 之后的 cognition anchors、未来 Tag meaning/attachment 和在切面尚不存在的 Tag；这些内容不成为历史激活 seed，也不提供未来 descriptor。排除在 inspection 中明确报告。Entity 和 Resource 的稳定身份可以表达现在的问题，但不能携带未来认知内容。

历史视图保留当时实际 cognition，即使它后来被判为错误。更新的 correction 不把过去的误解改写成新认知；当前 permission/purge fences 仍然有效。

## 5. 记忆

### 记忆对象

记忆是主体接受并决定长期保留的认知。每个记忆对象具有稳定身份，内容通过不可变修订演化；当前修订、对象生命周期和并发版本分别维护。

记忆形成可以由确定性流程或模型辅助流程提出。所有形成请求必须给出主张内容、语义指向、实际 formation basis、provenance 和形成上下文。模型生成的内容以提案进入记忆域，记忆域核验来源、当前对象状态和写入权限后提交。

### 认知角色

认知角色描述一条记忆在主体认知中承担的作用。它与证据数量和形成方式分开。

| 认知角色 | 定义 |
| --- | --- |
| 经历性记忆（Experiential） | 保存主体经历、接触或参与过的事件，以及主体对该次经历的长期认知。 |
| 陈述性记忆（Declarative） | 保存主体长期接受的事实、命题、判断或解释。 |
| 程序经验（Procedural Experience） | 保存主体从经验中形成的做法、步骤或策略性认识。它属于认知，不直接构成可执行行为规则。 |

### 形成方式

形成方式描述某一修订依据什么形成。

- 经历落地形成（Grounded）：具有显式来源或 cognition basis 并保留 provenance，主要依据一个有界经历、观察事件或来源上下文形成；它不表示文本已被客观验证。
- 综合形成（Synthesized）：依据多个认知对象、多个经历或多个独立来源综合形成。

认知角色和形成方式是独立属性。同一种认知角色可以采用不同形成方式；同一种形成方式也可以产生不同认知角色。对象身份不通过一个混合所有含义的单一类型枚举定义。

### 陈述性记忆的身份连续性

一个陈述性 Memory Object 表示一个持续的认知事项，而不是一段文本。

判断新内容是否属于同一对象修订时，需要保持对以下语义的连续性：

- 认知指向的对象或关系；
- 核心主张所属的 claim family；
- 主张的适用范围；
- 所描述世界状态的有效时间范围。

对同一认知事项的纠正、澄清、范围收窄或重新解释形成新 revision。

新的世界状态、独立事件、不同有效时间中的状态变化、从多个对象形成的泛化或新的认知问题形成新的 Memory Object，并可通过时间后继、推导、替代依据或其他语义关系与既有对象连接。对象身份的判断不能只依赖文本相似度、向量距离或字符串键。

### 修订与关系

对同一认知的修正、澄清或重新解释创建新修订；独立的新事件或新认知创建新对象。当前修订表示该对象当前被采用的内容版本。新 revision 表示较新的 cognition，可能是纠正、澄清、重新解释、收窄或改述，不承诺普遍的真值升级。

对象之间可以建立显式关系，包括推导、支持、矛盾、替代依据和其他具有领域语义的关系。矛盾关系不自动撤回任一对象；撤回表示领域所有者不再接受某项认知，必须由独立生命周期操作表达。

内容修订、对象生命周期、抑制状态和访问策略使用不同状态维度。仅改变抑制、固定访问或运行时驻留时，不创建虚假的内容修订。

### 记忆可访问性

记忆是否长期存在、当前是否允许普通访问、当前是否容易被召回以及与某次查询是否相关，分别由认知权威、管理生命周期、可访问性策略和查询相关性处理。

时间流逝本身不删除记忆。自动可访问性在查询时根据认知年龄、类型化使用、当前线索、工作上下文和查询预算计算；具体函数和参数由下游算法规格确定。精确管理读取和合法的来源追溯不因自动可访问性降低而丢失对象身份。

## 6. 经历组织、日记与认知图式

### 经历片段

经历片段（Episode）组织连续经历流中的事件。它保存成员观察或认知的引用、顺序、角色、时间范围和边界解释。参与者变化、场景变化、任务状态变化、主题或因果断裂、明确完成事件和持续闲置都可以成为边界信号。

经历片段具有独立身份和修订；边界可以拆分、合并和重新分段。边界修订只改变事件组织，不改写原始观察事件或成员记忆。会话描述运行连续性，经历片段描述事件组织，二者不共享身份。

### 经历片段的层级与分段轨道

经历片段允许形成层级。一个较长时期可以包含多个较短 Episode；子片段的成员和边界通过稳定引用组织，不复制底层 Observation 或 Memory。

同一观察可以同时参与不同的经历组织视角。系统允许按不同 segmentation track 形成 Episode，例如交互、任务、社会活动或环境事件。不同 track 的 Episode 可以时间重叠。

在同一 parent Episode 和同一 segmentation track 内，sibling Episode 默认形成按时间有序的非重叠分段。需要表达并行活动时，应使用不同 track 或显式父子结构，而不是让同一分段轨道任意重叠。

边界信号只形成分段提案；参与者变化、场景变化、任务转移、目标变化、因果断裂、主题变化、预测误差和持续空闲都可以提供边界证据。Episode Authority 由经历组织 owner 决定，边界算法、阈值和模型属于研究或后续 Spec。

### 日记

日记（Journal）是对一段经历、阶段或时期的可修订叙事对象。日记引用经历片段、观察事件、记忆及其修订，并保存生产者和来源谱系。

日记用于保留较长时间尺度的经验上下文，支持回顾、自我叙事、检索和离线认知。日记不承担外部事实权威，也不是形成记忆的必经阶段。依赖来源发生实质修订、撤回、抑制或清除时，日记进入重新核验或形成新修订。

### 认知图式

认知图式（CognitiveSchema）表示主体从多个经历和认知中形成的可泛化结构。认知图式属于记忆域，并作为独立对象族维护稳定身份、修订、适用范围和生命周期。

一个认知图式至少表达：结构性主张、适用范围、支持认知、反例、边界案例和来源谱系。新的支持证据可以更新支持关系而不修改图式内容修订；只有结构解释、适用范围或边界发生变化时才创建内容修订。

认知图式支持拆分、合并、修订和撤回。反例不会自动删除图式；反例参与适用范围判断、冲突处理和后续修订。

### 标签与关联证据

标签（Tag）是具有稳定身份、可修订文本语义表示的 durable semantic concept。它可以表达主题、规则、事件或经验模式、程序与因果概念，或一句话及较长概念描述，不限定为分类枚举或 hashtag。标签身份与显示名称分离；相同字符串只能作为解析候选，不能自动证明两个标签具有同一语义身份。

Tag 的 effective label、description 和语义 kind 形成唯一、版本化、确定性且有界的 canonical semantic representation。它用于共享 embedding、query activation 与 associative retrieval；opaque TagId 和 LexicalRef 只负责身份，alias 用于发现，不默认加入概念 embedding。修订改变语义表示，稳定身份保持连续。

关联证据（AssociationEvidence）记录认知对象之间有来源、有类型的关联依据，例如共现、顺序、显式关系、程序关系、共同结果或图式支持。关联证据保存来源、方向、极性、有效范围和生产者信息。

检索图中的中心性、传播质量和边权不构成认知对象。系统不定义同时承担认知结构和检索中心性的统一权威对象。认知结构由认知图式表达；检索拓扑由服务层根据当前有效关联证据重建。

### 概念形成与演化

Tag 可以由显式管理操作或认知维护形成。认知维护读取当前认知、来源、实体、既有 Tag 和关联上下文，形成 create、reuse、revise、attach、detach、merge、split 等提案；Memory owner 对实际 Tag 操作负责。

Tag 与既有 Cognition 的后置关联使用显式关系记录，不为了增加一个后来形成的概念而重写历史 cognition revision。Tag 自身内容发生实质语义变化时创建 Tag revision；merge/split 保留 lineage 和实际 formation basis。Tag 的概念解释和关联判断也可以出错并被修订。

一次模型输出可以包含多个维护建议。每个被接受的领域操作按自己的 Authority mutation 合同提交。模型建议列表本身不建立跨所有动作的超级事务语义。需要天然原子性的领域操作，例如 Tag merge、Tag split、Episode partition，自身继续保持原子。

### Semantic Concept Plane

Durable Tag、query-local Tag activation、concept proposal、AssociationEvidence 和 derived Accretion 共同构成 Semantic Concept Plane。长期概念由 Memory owner 维护；查询激活属于 Runtime；concept vectors 和 direct attachment postings 属于可重建 Serving，不能建立并行 Tag Authority。

Host 可以在 formation 时提供已解析的 explicit Tag identity。Memory owner 验证主体、active/canonical state、合并映射与数量，作为该 cognition revision 形成时已知的概念上下文提交。后置 attachment 继续使用有来源的 AssociationEvidence，不重写历史 revision。

长期 inferred Tag 统一通过 concept maintenance 形成；Memory formation model 不复制另一套长期 Tag inference。query execution 可以按配置形成既有 Tag activation 或 novel concept hypothesis，它们保持 ephemeral，不直接 create、revise、merge 或 split durable Tag。

### 语义吸积

系统可以从当前有效 Cognition、Tag attachment、AssociationEvidence、Episode recurrence、来源谱系、时间跨度和有意义 UseEvent 派生语义吸积信号。

吸积信号用于发现稳定概念中心、提高 concept review 优先级、提供 Tag reuse/merge/split 候选信号，并可在版本化检索算法中作为 feature。

吸积信号可删除和重算，不构成新的 Cognition Authority，不替代底层 provenance，不把检索次数或普通呈现转换成认知支持。系统不重新建立同时承担认知结构和 retrieval centrality 的 Anchor Authority。

## 7. 自我与人格

### 自我领域

自我（Self）维护主体对自身长期身份、特征与连续性的认知。自我领域至少包含自我模型、倾向与人格风格、价值与长期偏好、叙事身份四类表示；这些表示属于同一领域，共享来源、修订和查询基础。

- 自我模型：表达主体身份、角色、能力、局限以及对自身当前状态的长期认识。
- 倾向与人格风格：表达相对稳定的反应倾向、互动风格和习惯性适应。人格风格（Persona）是自我领域中的表示，不建立并列的顶层权威。
- 价值与长期偏好：表达跨具体情境相对稳定的评价取向、长期重视事项和持久偏好。
- 叙事身份：表达主体对自身来历、经历、变化、连续性和长期方向的组织性理解。

### 自我对象的粒度

Self 不以一份不断全文重写的单一 Profile 作为全部自我 Authority。

身份、角色、能力、局限、人格倾向、价值和长期偏好等自我认知，在能够独立变化、独立被质疑、拥有独立来源或拥有独立适用范围时，维护独立稳定身份和 revision。紧密耦合且无法独立解释的内容可以由同一对象表达。对象粒度服务于可修订性、来源清晰度和查询语义，不以最细原子化为目标。

叙事身份维护主体对来历、变化和长期连续性的组织性解释。叙事对象通过稳定引用关联 Episode、Memory 和 Self revision；它不复制这些对象的权威内容，也不通过叙事重写历史来源。

### 认知种子

认知种子（Cognitive Seed）是用于主体初始化的人类编写结构化来源文档集。它可以由一份带有明确章节的文档组成，也可以拆分为少量职责清楚的文档；物理文件数量不改变其认知语义。

每个种子版本都保持原文不变并具有稳定来源身份。采用种子时绑定一个确定版本，并保存该版本的实例快照或等价的完整内容身份。后续认知演化作用于由种子形成的认知对象，不修改最初采用的种子原文。

认知种子是初始化来源，不是当前自我状态本身。主体供给时，种子中的内容按照语义归属形成相应领域的初始化提案：身份、自我认知、人格倾向、价值、长期偏好和叙事起点进入自我领域；过去经历和初始知识可以进入记忆领域；人物、关系和社会语言约定可以进入社会认知；愿望、关切和期望条件可以进入动机领域。未启用的领域不创建占位认知，其对应种子内容仍保留在来源快照中，可在该领域启用后重新解释。

将新的种子版本应用于已经存在的主体属于显式导入或重新初始化操作。新内容形成新的来源关系和认知提案，不覆盖主体最初的种子历史，也不把已有认知历史改写成来自新版本。

产品安全规则、操作权限、管理员强制行为和不可绕过的行为限制由宿主或 Heptalogos 的规范权威维护，不写入认知种子承担安全责任。

可读 soul 可以是初始化来源，也可以是当前认知的派生视图。当前视图从正式对象投影，编辑必须通过显式提案/采用操作；不得与数据库双写。Seed 的虚构背景保留设定或叙事来源，不创建冒充真实接触的 Occurrence。

### 主体知识与 EpistemicView

Self 的 domain-knowledge facet 保存可独立修订的领域/主题、当前熟悉程度、能做与不会的内容、适用情境、学习兴趣引用、支持和反例。具体知识和学习经历仍由 Memory 等原 owner 保存。熟悉程度可表达 unfamiliar/aware/conversational/practiced/specialized，是本人认识的说明，不是模型能力或工具权限等级；亲历、听说、阅读、练习的来源性质分别保留。

EpistemicView 是 Runtime/Projection 按用途、话题、世界时间、参与者、受众和 WorkContext 形成的派生认识视图，组合相关领域知识、具体认识、经验、未知/新近性限制、执行协助和学习机会。权限与角色可见性在候选检索前执行，覆盖不足不等于永远不知道；必需知识立场和反例先于可选正文进入预算。

无 Seed 不造专业经历或学校背景；普通语言常识和推理可用，不为每句话登记 Memory。后台专家知识、未交给主体的阅读和工具结果不自动成为个人知识；正式 handoff/接触后可作为刚获得的信息，解释、练习与实际结果为后续认识修订提供来源。一次看过不机械晋升为专业掌握。当前临时理解可用于当前工作，长期能力概括由已有反思与 owner 形成。

### 自我演化

自我认知通过证据、经历、反思和跨领域提案逐步修订。来源于认知种子的内容保留其来源关系，但不会因为来源于种子而永久获得高于后续认知的特殊认知权威。

人格倾向、价值与长期偏好的变化需要保留修订和来源；叙事身份可以重新组织既有经历和自我解释，但不能改写作为来源存在的历史观察和材料。主体身份连续性由稳定 SubjectId 和自我修订谱系共同支撑，不依赖一份永远不可变化的人格文本。

管理全量读取、自动上下文与反思候选分别承担自己的范围。必需身份独立取得，候选先按生命周期、有效时间和结构作用域筛选，再按任务检索；预算限制本次候选与完整语义单元，不以库内总项数或第一页作为可用性条件。正文与依据由 owner 在合理读取范围内批量组合，未选入不表示不存在。

真实接触、结果、纠正和来源变化产生有界共享反思机会。Self、Social 和 Motivation 共用实际来源准备、授权、预算和已保存模型成果，分别提交并返回动作结果。自动成长由显式政策启用，不能纳入 purge 或系统权限操作；同一来源的轮询和主体自述不产生独立佐证。

### 自我与其他领域

长期稳定的价值取向、偏好和人格特征由自我领域维护；面向未来状态的愿望、关切和期望条件由动机领域维护。具体经历和关于自身的事件由记忆域保存，并可以成为自我修订的证据。

社会关系对主体行为的影响由社会认知提供关系上下文，自我领域不复制针对具体对象的关系状态。行为表达和主动追求由 Heptalogos 根据自我、社会认知、动机和当前情境共同决定。

## 8. 社会认知

### 社会认知领域

社会认知（Social Cognition）维护其语义依赖特定个人、二人关系、群体、频道或社区的长期认知。领域至少包含关系认知图和语言惯例两类一等对象族。

普通世界知识和通用语言知识不因涉及人物而进入社会认知。只有在去除具体社会作用域后语义会发生变化的长期认知，才由社会认知领域拥有。

### 关系认知图

关系认知图保存某个主体对社会世界的长期认识。每项关系认知都属于一个拥有者主体，并连接来源实体、关系类型和目标实体。关系默认具有方向性。

关系认知至少包含：

- 拥有该认知的主体；
- 关系的来源实体和目标实体；
- 关系类型；
- 在该关系类型具有程度语义时的可选关系程度；
- 主体对该关系判断的认识状态；
- 支持与反驳证据、有效时间和修订历史。

关系程度与认识确定程度分别表示。主体可以低确定度地认为两人关系非常亲密，也可以高确定度地认为两人只有普通联系。不同关系类型的程度值没有默认的跨类型算术意义。

关系图中的路径用于检索、相关对象发现和假设形成。关系不具有默认传递性；由多跳路径推导出的新关系首先形成假设，经过证据搜索和社会认知领域核验后才能提交。

### 关系类型语义

每种 Relation Type 必须声明自己的结构语义，包括：

- 方向性；
- 可选的对称或逆关系语义；
- 允许连接的实体类型；
- 是否存在关系程度；
- 程度采用何种操作语义；
- 时间有效性规则。

关系程度不是所有关系共享的通用 [0,1] 数值。一个关系类型可以没有程度，也可以采用有序等级、有界标量或类型化状态。不同关系类型之间的程度没有默认的算术可比性。

关系程度与主体对该关系判断的认识状态继续独立维护。

关系类型可使用有向 familiarity、affinity、限定领域的 trust、closeness、collaboration、mentor_of、member_of 和 conflict_with。其程度分别为有序等级、有界好感、领域内等级、合作/冲突状态或无程度，不跨类型加总。双向读取返回各自记录或未知；对称关系由规范端点对象投影，不双写镜像，逆关系不推导相同程度。

### 语言惯例

语言惯例（LanguageConvention）保存特定社会作用域内形成的词义、称呼、黑话、简称和语用约定。每项语言惯例至少包含表达形式、社会作用域、语义或指代、可选语用角色、认识状态、证据、有效时间和修订。

社会作用域可以是个人、二人关系、群体、社区或频道。查询时依据当前参与者和场景选择适用的惯例；不同作用域可以同时保留彼此不同的含义。

显式解释或确认、独立外部参与者反复一致使用、成功理解后继续按同一语义交流以及修复过程，都可以成为惯例证据。单次上下文猜测只能形成 hypothesis。主体学习某一惯例后自己的重复输出不构成新的独立外部证据。

理解入口保留原话、说话者、受众、活动与时间，返回候选含义、作用域、来源、冲突及省略。表达再次按实际受众选择使用或解释，不永久把原话替换为猜测。个人、双方、群体、频道和活动可组合限制；同形异义可以并存。来源传播权限在检索前生效，不由社会作用域代替。

### 实体身份

社会认知引用已经绑定的实体身份。昵称、显示名称和向量相似度不直接合并人物身份。跨平台身份关联保存独立来源和证据；平台好友关系、群角色和账号信息可以作为来源事实，再由社会认知领域形成长期关系认知。

## 9. 动机

### 动机领域

动机（Motivation）维护主体关于“希望什么、持续关心什么”的长期认知。核心对象包括愿望、关切和期望条件。

- 愿望（Desire）：主体希望某种状态出现、持续或改变的倾向。愿望可以保持模糊，不要求已经具有稳定的判断条件。
- 关切（Concern）：主体需要持续关注、保护、改善或避免恶化的事项。关切可以长期存在，并持续影响注意、评价和后续愿望形成。
- 期望条件（Desired Condition）：已经足够明确、可以依据证据判断其满足情况的未来或持续状态条件。它描述主体希望什么成立，不表示主体已经决定采取行动。

动机对象具有稳定身份、来源、修订和生命周期。不同动机之间可以建立支持、细化、前置、冲突、替代和长期优先等关系。只有长期稳定且需要跨会话保留的优先关系进入动机权威；当前情境下的注意优先级由认知运行时计算。

### 期望条件的结构化表示

期望条件使用有界、类型化的条件表达。

基本条件由版本化 predicate 或 evaluator 表达；复杂条件可以通过有限的 ALL、ANY 和 NOT 组合。目标设计不把期望条件扩展为任意脚本、通用编程语言或工作流定义。

期望条件同时保存：

- 条件表达；
- 时间形式；
- 时间范围；
- 适用上下文；
- 评价所需的观察覆盖要求；
- evaluator 版本与来源。

条件真值至少区分：

- SATISFIED；
- VIOLATED；
- UNKNOWN。

适用性与条件真值分别判断。开放世界中的 Maintain 和 Avoid 条件只有在声明的观察覆盖足够时才能形成满足判断。没有观察到反例本身不证明条件成立。领域复杂判断通过版本化 evaluator 扩展，并保留其评价来源和 revision。

### 期望条件的时间形式

期望条件由待判断条件、适用范围和时间语义共同构成。目标设计使用四种基本时间形式：

- 达成（Achieve）：希望某个条件在给定时间范围内至少成立一次。
- 终止（Cease）：希望某个当前或可能成立的条件在给定时间范围内停止成立。
- 维持（Maintain）：希望某个条件在指定时间范围内持续成立。
- 避免（Avoid）：希望某个条件在指定时间范围内持续不成立。

期望条件可以带有开始时间、截止时间、持续窗口或开放时间范围，也可以声明使该条件适用的上下文。时间形式描述主体希望世界呈现怎样的时间性质，不规定具体计划或执行步骤。

期望条件的满足判断必须引用可追溯证据。缺少足够观察覆盖时保持未知；系统不能因为“没有看到反例”就自动证明维持或避免条件已经满足，也不能因为截止时间经过就无证据地断言外部世界一定没有发生目标事件。

期望条件是否仍被主体持有，与它当前是否满足分别表示。条件得到满足不会自动删除动机；主体撤回或修订某项期望，也不会改写过去已经发生的满足或违反事实。

### 动机与主动行为

Nous Wave 保存愿望、关切和期望条件。Heptalogos 决定主体是否为某项期望投入持续主动行为。

当 Heptalogos 决定持续追求一个期望条件时，行为侧建立主动追求状态（Pursuit），并引用该期望条件的精确修订。主动追求状态属于 Heptalogos 的行为与主动性权威，不属于 Nous Wave 的动机对象。

期望条件的存在、重要或临近截止时间都不会自动创建主动追求状态。Heptalogos 根据当前情境、既有承诺、能力、资源、风险、规范和其他主动追求进行审查，可以采纳、延迟、暂停或结束追求。

期望条件发生实质修订时，已有主动追求必须重新核验其来源修订，不能静默改为追求新的语义。主体撤回某项期望时，相关主动追求进入重新审查；已经形成的外部承诺和义务仍按照 Heptalogos 自身的规范生命周期处理。

### 主动追求、行为提议与承诺

以下对象分别维护身份、生命周期、来源和状态：

- Desired Condition：认知上的期望；
- Pursuit：行为侧持续主动追求；
- BehaviorIntent：一次具体判断中的候选行为；
- ActionPlan / InteractionPlan：实现一次已接受行为的步骤和组织；
- Commitment：主体已经承担的社会或行为承诺；
- Obligation：已经形成、需要后续履行或处理的约束；
- Effect：外部世界中的 consequential outcome。

Heptalogos 的行为结果、外部状态变化、完成、失败、取消和拒绝通过类型明确的回执与证据返回 Nous Wave。Nous Wave 依据期望条件自身的判断语义更新满足评价或形成动机修订提案。一次行动失败不等于期望条件失效，一次局部任务完成也不自动证明长期期望已经满足。

### 动机与运行时

持久动机保存长期愿望、关切和期望条件；认知运行时决定当前哪些动机进入前台并影响注意、检索和即时评价。运行时优先级可以随情境变化，不要求每次前台调整都形成新的持久动机修订。

## 10. 认知运行时

### 运行时状态

认知运行时组织当前可供推理和调用方使用的认知状态。临时运行状态可以丢失并从 Authority 与 durable Runtime checkpoints 重建，任何持久认知状态都不依赖进程内缓存存活。

- 会话（Session）：一段连续运行范围，不等同于聊天线程或经历片段。
- 活动认知（Active Cognition）：当前较容易重新激活的认知引用和少量运行元数据。
- 工作上下文（WorkContext）：属于 Subject-level Cognitive Runtime、可暂停、恢复和结束的任务或问题上下文；同一主体可以同时存在多个工作上下文，并可由该主体的后续 Session 继续。
- 驻留集（ResidentSet）：当前运行时直接保留的认知引用集合。淘汰只改变运行时可用性，不修改持久认知。
- 调用方工作集（ConsumerWorkingSet）：按调用方能力、意图和预算选择的有界认知集合。
- 受管理上下文（Managed Context）：为模型或其他有状态消费者维护的上下文同步状态。

同一 Subject 可以同时服务多个 Session 和多个 consumer。它们共享 Subject 所属的 durable cognition；Session 的 ResidentSet、foreground WorkContext binding、runtime revision 和其他需要隔离的运行时状态分别维护。WorkContext 保存有界的任务连续性、可复用 context_text 与 typed cognition/Entity/Tag anchors，不复制 Memory。ConsumerWorkingSet 与 UseEvent 按调用方和事件身份记录，不通过复制 Subject Memory 建立独立认知权威。

### 受管理模型输入

一次调用明确绑定 Subject、Session、执行者、工作、用途与受众。当前语义事实和相关证据通过正式 Projection/ContextCompiler 共同选取，调用方不逐域复制选择逻辑。身份与情境指导、原始材料及认知 Authority 保留不同地位；认知内容不能授予系统、工具或行为权限。

每次实际模型提交，包括工具后续、重试、handoff、子执行者和压缩后的下一步，自动准备并应用适用认知。RESET 替换当前 slice，APPEND 仅续接已同步的不可变前缀；应用成功后才推进 cursor。当前认知 slice 不进入长期历史摘要，不成为第二份可写状态。 原生 compactor 仅对已结束回合固定前缀后台生成，并核对 generation、前缀与当前来源许可后发布，保留未覆盖历史和新增尾部；与手动及硬超窗压缩共享同一所有者。当前世界/时钟/权限每次重建，摘要不替代实际进展或长期认识。必需认知不可用时终止相关调用。

Nous 提供可独立安装的正式 OpenClaw 集成，并由 Heptalogos 原样复用。模型连接、工具循环、渠道、Computer use、skills、子 Agent 与 transcript/压缩复用原生执行能力；缺少必需控制时在受控分发修正唯一正式入口，不以 best-effort hook 或第二个 Agent Runtime 替代。跨系统职责见[认知与主动性合同](../integration/cognition-agency.md)。

### 注意与即时评价

注意分配在有限预算下选择当前需要处理的信息、工作上下文和认知对象。即时评价根据自我、社会认知、动机和当前环境估计相关性、机会、风险、可控性等运行时性质。

注意和即时评价主要属于运行时。只有形成稳定、可追溯且需要跨会话长期保留的倾向时，才通过相应领域提案进入自我、社会认知、动机或记忆。

### 多工作上下文的资源分配

多个 WorkContext 竞争有限认知资源时，Runtime 的分配策略至少考虑：

- 当前交互相关性；
- 紧急度和截止时间；
- 连续性成本；
- 风险和重要性；
- 预期信息价值；
- 当前 Desire / Concern；
- 公平性与防饥饿；
- 可用预算。

目标运行语义要求有界公平分配、紧急借用、显式抢占和防饥饿。具体 utility function 和参数由下游 Runtime Spec 与实验确定。

### 可复用 WorkContext 与持久检查点

WorkContext 属于 Cognitive Runtime。短生命周期运行细节、prompt、cache、候选排序和模型内部状态可以丢失并重建。

WorkContext 是可持久保存、更新、暂停和复用的 Runtime state。Host/Agent 可以一次保存长任务背景，后续 query 自动读取 foreground WorkContext；跨进程或跨 Session 恢复时使用 durable checkpoint。

检查点保存继续该认知工作所必需的有界状态，例如：

- purpose；
- context_text：Host/Agent 编写的任务历史、决定、当前调查和操作背景；
- unresolved_questions；
- cognition_anchors：用于精确续接的对象/revision 引用；
- entity_anchors：已解析的稳定 EntityRef；
- tag_anchors：稳定 durable Tag identity；
- 当前约束；
- 提交时依赖的 expected revision；
- 恢复条件；
- 资源和预算摘要。

context_text 是操作上下文，不是 evidence，也不因持久保存而成为 Memory。显式 pin 的 Entity/Tag 不改写原始 query text；可选模型推断的 Tag 不自动写入 WorkContext。持久存储的上限与单次表示的投影预算分别管理，不能因 embedding 输入有界而把长期任务文本压成同一小窗口。

Session 保存可选的 foreground WorkContext binding。Active Cognition 是 ResidentSet、当前 WorkContext cognition anchors 与请求 Situation refs 的运行时视图，不建立新的 durable cognition Authority。

恢复时以当前 Authority 重新核验检查点。检查点不得成为长期认知 Authority。 有意义结果、目标切换、委派让出、取消和完成前同步保留最小继续信息，引用已有成果，不等摘要或反思完成，不以逐 token 日记恢复运行。Heptalogos 的单前台与焦点属于产品语义，Nous 不建立第二个 Reactor。

### 使用事件

长期使用事件记录调用方对某项认知的真实使用及后续结果。候选生成、检索命中、排序和过滤属于检索轨迹，不直接成为长期使用事件。

使用事件可以区分呈现、引用、据此行动、结果支持、结果反驳、纠正和显式固定等语义。它可以影响 ResidentSet、accessibility、review priority 和维护信号，不能把 cognition 投票成真；result_refuted 保留负反馈含义。仅进入调用方上下文的呈现不等于有意义使用，也不自动改变长期关联或可访问性。

每个需要持久记录的使用事件由调用方提供稳定事件标识。重试同一事件必须得到幂等结果；相同事件标识携带不同内容时返回冲突。使用事件与由其直接触发的运行时更新保持一致提交。

### Query feedback

Host 报告有意义使用时可以关联实际产生该结果的 query。Runtime 保存有界、可过期的 query feedback：prepared intent/activation digest、explicit/inferred concept refs、bounded novel hypotheses、returned exact revisions、可验证的 seed context 与 profile identity。它不保存 raw artifact、完整 prompt、provider secrets 或整份 retrieved text。

关联反馈验证同 Subject、有效 query correlation 和返回修订 membership。达到 review 条件后只 enqueue 现有 concept MaintenanceNeed；后续 Host grant 才允许维护读取反馈并建议 reuse/create/revise/merge/split Tag 或 AssociationEvidence。query hypothesis 只作为 meaningful-use maintenance signal；语义关联仍需真实 cognition/source basis 与明确的 epistemic judgment。query exposure、presentation 和 activation 次数不构成长期强化、独立根或 Accretion 支持。

### 可访问性

可访问性描述在当前线索和上下文中取得某项认知的难易程度。自动可访问性是查询时派生状态，可以考虑认知年龄、类型化使用、当前线索、工作上下文和查询预算。

自动可访问性不修改认知权威状态和生命周期。显式固定、精确访问限制、抑制和清除分别由独立策略或管理状态表达。自动策略不得仅依据固定年龄把仍然合法存在的认知永久变成不可恢复对象。

### 多角色认知交付

同一 Subject 的多个 Agent/用途共享唯一认知，每个执行者保有独立 binding、cursor 和工作历史。Host 的 world/deliberation/execution/render/review 职责与 Nous 的认知 ModelRole 配置分别拥有；认证用途决定读取视角和接触性质。新 role 不继承污染的旧私有 transcript，RESET/压缩后重新获取当前世界与认识。

Subject 审议与人格渲染必须取得适用的 EpistemicView、Self、社会用语和相关经历；world author 与专业执行仅取得其任务需要且允许的内容。依赖缺失时停止相关必需调用，不能退回默认助手，维护实例保持独立。正式 SDK 在首轮、工具后续、子 Agent 和压缩后持续应用同一合同，不另建每域拼装或 provider registry。

### 受管理上下文

对有状态消费者追加上下文前，系统核对调用方身份、策略、提示前缀、来源修订、访问控制、对象生命周期和渲染合同。上述条件发生不兼容变化时重建上下文；满足兼容条件时可以追加。上下文缓存永远不代替认知权威。

## 11. 离线认知

### 维护授权

离线认知在宿主提供的维护租约内运行。维护租约明确允许的时段、计算资源、模型服务、网络权限、预算、取消条件和抢占规则。宿主决定何时允许维护；Nous Wave 决定在授权范围内处理哪些认知需求。

维护工作可以包括经历片段整理、日记维护、派生表示重建、认知图式复核、跨领域一致性检查、假设探索和服务投影维护。

### Host 授权的模型活动

Host 发起 form 时授权 formation model 工作；Host 发起 query 时，可以按冻结的 Configuration 与 CapabilityPolicy 使用 query embedding 和可选 concept enrichment model。MaintenanceNeed 可以自动 enqueue，但 maintenance model 只在 Host grant 的租约和预算内运行。后台 scheduler 不自行取得 LLM 调用机会。

### MaintenanceNeed

MaintenanceNeed 表示系统已经发现某项认知维护工作需要后续处理。它是 Runtime / Offline Cognition 的 durable work obligation，不形成新的顶层认知领域，也不表示 Subject 接受了一项新的长期认知。

MaintenanceNeed 可以由以下情况产生：

- 依赖对象修订；
- 未解决矛盾；
- Journal 或 CognitiveSchema 需要重新核验；
- DerivedRepresentation 失效；
- Serving generation 需要重建；
- 跨领域 proposal 等待复核。

优先级由当前影响、陈旧程度、依赖范围、预期修正价值、成本和宿主预算派生，不成为持久认知权威状态。

### 输入快照

每次离线认知运行固定输入快照。快照至少记录主体标识、输入对象及其修订、来源和证据版本、访问控制与生命周期、权威提交水位、工作流版本、生产者签名和资源预算。

离线运行期间发生的新提交不自动进入既有快照。运行结果在提交前重新核验当前权威状态。

### 概念与关联维护

accepted/revised cognition、显式有意义使用以及其他领域事件可以产生 concept/association MaintenanceNeed。

维护工作固定当前输入快照，模型或确定性过程提出有限的 Tag 和 AssociationEvidence 操作。结构所有者已经直接掌握的事实可以直接产生结构关系依据，无需经通用模型重新推断。

语义关系提案携带实际 formation basis、provenance 与明确的 epistemic judgment。目标 owner 核验引用、主体、生命周期、relation type 和 lineage 后按领域合同提交，不以通用自然语言蕴含证明代替结构核验。

模型 proposal 被领域 owner 判为非法时，本次 proposal 结束；新的认知变化或显式 review 可以形成新的维护机会。provider、transport 等瞬时失败可以复用已经保存的 proposal 或输入快照重试，不因重试重复模型付费调用。

一次提案可以包含多个 ordered suggestions；每项接受的操作使用由 workflow 身份、动作顺序与动作类型稳定派生的 operation identity。领域 owner 的幂等回执支持崩溃后继续执行；后项非法不回滚已成功的独立前项，依赖失败结果的后项跳过。输入修订已陈旧的提案结束，由新的领域变化或显式 review 产生新的维护机会。owner invariant 或数据损坏暴露为工程失败。

### 假设

离线探索首先产生假设（Hypothesis）。假设包含候选主张、适用范围、实际输入修订与 formation basis、provenance、明确的支持/反例等 epistemic judgment、不确定性、目标领域、拟议操作、生产者和运行标识。

假设没有跨领域写入权限。提交前执行来源重新核验、共同来源祖先展开、反例搜索、对象版本核验、访问控制核验和清除状态核验；随后由目标领域所有者接受、拒绝、标记冲突或判定过期。

多个模型给出相同判断不自动构成多个独立证据。独立性由来源谱系和外部观察决定。

### Hypothesis exploration envelope

每次离线 hypothesis exploration 在开始时固定有界探索范围，包括：

- 总资源预算；
- 来源范围；
- 反例或证伪搜索预算；
- 允许使用的能力；
- 预期信息价值；
- 取消和抢占条件。

预算耗尽、重复循环、没有新增独立来源、声明的反例搜索范围已耗尽、预期信息增益过低、目标领域背压、前台任务抢占、权限变化、清除操作和显式取消均可终止探索。停止原因属于运行记录，不自动决定 hypothesis 真伪。

## 12. 认知查询与检索

### 认知查询

认知查询必须包含非空自然语言 intent，而不暴露具体检索算法开关。Selector、Tag、概念、时间、上下文、projection 与 exploration 只能丰富意图，不能代替文本；纯结构读取属于 exact domain API。查询可以指定主体、领域和对象范围，以及实体、时间、语义线索、硬约束、软偏好、调用方能力、计算预算、材料展开要求和诊断需求。

硬约束决定对象是否合法；软偏好只影响合法对象之间的排序。按稳定身份进行的精确读取直接访问权威对象，不经过相似度检索。

### 最小查询与结果投影

非空 natural-language intent 本身构成完整的一等 Cognitive Query：Text → lexical + dense → fixed fusion → owner validation。Entity、Tag、Schema、WorkContext、Situation、Agent loop 和 associative exploration 都是可选增强，纯文字路径不依赖 concept model 或 concept Serving asset。

Prepared Cognitive Query 从语义上分别包含 Cue Expression、TemporalFrame 与 scoped filters、Cognitive Context、ExplorationFrame、ResultProjection 和 Execution Policy。查询意图与最终返回对象类型独立；默认 recall 返回所选视图中 eligible Cognition，即 Memory、CognitiveSchema、Episode 和 Journal。Evidence 和 Resource 可以作为 provenance/material 参与；调用方明确选择 projection 或 resource intent 时才作为顶层结果。exact target 同样满足 ResultProjection。

### 查询准备与引用解析

Cognitive Query 在 QueryPlan 形成前完成引用解析。

自然语言名称和别名用于 identity discovery；稳定引用用于 exact continuation。未知引用和歧义引用以显式结果返回。调用方或 Agent 可以补充上下文、选择候选并重新提交。查询执行器不通过 embedding 或模型隐式决定对象身份。

自然语言 referent 显式化是强推荐的质量增强：明确名称有利于 lexical、embedding 和 concept activation；它不是查询资格条件。包含任何语言的代词或指示词的普通 text 均可执行，Runtime 不实现多语言 coreference/pronoun hard gate。Raw intent、context-assisted representation 与 Host 显式 contextualized intent 都是正式路径；原始文本保持可识别。显式未解析的机器占位符与 typed identity 的 unknown/ambiguity 仍可返回结构错误。

准备按统一流水线执行：Original Intent + query-local cues + foreground WorkContext + Session Runtime/ResidentSet + one-shot Situation → QueryContextSnapshot → QueryRepresentation → QueryActivation → QueryPlan → retrieval profiles。

QueryContextSnapshot 冻结实际使用的 WorkContext identity/revision、适用的 Session/runtime revision、context text digest、Entity/Tag/cognition anchors、实际接纳的 resident/runtime refs、one-shot Situation、历史排除与截断/降级。它是 ephemeral prepared state，不是新的 durable Authority。准备阶段无 provider/model 调用；同一查询的后续 representation、activation 与所有 profiles 只消费这份冻结输入。

opaque identity 用于绑定和约束；显示名、Tag 描述、WorkContext purpose/context_text 等 semantic descriptor 用于 QueryRepresentation。统一 representation policy 分配总预算与 section 预算，保留 Intent，依次优先接纳 explicit query cues、pinned Entity/Tag、任务文本、exact cognition anchors、Session runtime 和较低优先级材料；实际截断显式报告。持久 context 存储和 query projection 上限分别配置。改变算法 profile 不能改变同一 prepared query 的 semantic input。

Bare text 是普通产品路径；研究 plain baseline 通过显式能力与配置关闭增强，不建立 product-level text-only compatibility 模式。

Agent 可以把 identity discovery、query preparation、query execution 和后续 exact continuation 组合成多次工具调用。可选 model-assisted contextualizer 可以由 Host 在 Runtime 之上提供，不成为 deterministic prepare 的必需调用。NousQL 的长期输入模型是 unquoted Unicode text + syntax islands；具体 grammar、escaping、CLI 命令、显示与 local receipts 由代码仓库 Specs/Reference 维护。

### QueryActivation 与检索模式

准备阶段先冻结 QueryContextSnapshot，再固定 QueryRepresentation、TemporalFrame、ResultProjection 与配置，不调用 provider/model。执行阶段按允许的能力从同一 prepared input 生成共享 query embedding，再形成统一 QueryActivation：semantic text、exact Entity/Tag/Schema、current cognition、WorkContext/Situation refs、explicit/inferred Tags 与可选 novel concept hypotheses。冻结后的 activation 是 Runtime-only state，不形成长期 Cognition Authority；各 profile 消费同一语义输入，不各自定义概念集合。

QueryActivation 保留 Tag origin：explicit_query、work_context、existing_semantic_match、model_inferred、runtime_situation。Pinned WorkContext Tags 持续贡献 context activation，无需 Agent 每轮重复；各 profile 不自行推断另一套 Tags。Resident cognition 继续通过 exact refs 提供 runtime/topology context，不自动把全部 resident attachments 转成 Tag activation。

exact Tag identity 与 semantic concept cue 分别表示精确引用和语义线索。概念 cue 不承诺存在同名 durable Tag；semantic/model activation 可以选取既有 Tag，却不承担歧义 identity resolution。可选 query concept model 仅从有界 catalog 选择已有概念或产生无 TagId 的 bounded hypothesis。

Direct concept recall 从 explicit/inferred Tag activation 读取直接 attached cognition，不进行多跳，也不要求 associative exploration。只有调用方显式选择 associative exploration 时，QueryActivation 的 Tag、Entity、Schema、current cognition 与 lexical/dense promoted seeds 才作为传播起点。Retrieval profile 决定具体有界传播算法；Query DSL 不暴露 hop、field、EPA、DTSC 等内部参数。

### 查询计划

查询执行前生成固定查询计划（QueryPlan）。计划在看到候选结果之前确定检索通道、各通道预算、融合参数、拓扑预算、可选重排、材料展开预算和一致性要求。

计划中的某个检索通道没有产生结果时，该通道贡献为零。结果集合本身不得反向改变其他检索通道的权重或归一化尺度。

### 检索通道

| 通道 | 职责 |
| --- | --- |
| 精确读取 | 按对象身份、修订和精确键读取。 |
| 实体检索 | 按认知指向、实体绑定和来源提及召回相关对象。 |
| 词项检索 | 处理短语、代码、路径、专名和其他词项线索。 |
| 稠密检索 | 按规范表示、语义片段或来源约束的召回视图检索。 |
| 直接概念检索 | 从 Tag activation 直接召回 attached cognition，不进行扩散。 |
| 时间检索 | 按发生、观察、有效、形成和记录时间过滤或排序。 |
| 运行时检索 | 从活动认知、驻留集和工作上下文中取得当前相关对象。 |
| 拓扑检索 | 在有界关联拓扑中生成候选排序。 |
| 资源检索 | 查询外部知识或数据源，并按需将实际接触结果形成观察事件。 |
| 可选重排 | 对已通过硬约束的候选集执行二次排序。 |

### 候选身份与多视图

候选的语义身份由主体、领域所有者、对象身份和修订身份确定。一个修订可以拥有规范表示、段落表示、召回线索和其他服务视图；这些视图属于同一认知对象，不构成多份独立证据。

每个检索通道先将视图命中聚合到对象修订层，再参与跨通道融合。视图数量不得直接形成额外投票权。

### 融合与最终校验

跨通道融合函数由查询计划固定，并满足以下约束：参数在候选生成前确定；缺失通道的贡献明确；候选集合中出现无关对象时，不改变既有通道的定义；拓扑检索以普通通道身份参与，不使用计划之外的隐藏加分。

融合与可选重排完成后，返回结果前由各语义 owner 重新核验所选 Authority/revision view 中的修订、对象生命周期、访问策略、访问控制、来源状态以及抑制和清除状态。Memory 负责认知对象，Material 负责观察与派生材料的精确 lineage、材料展开和五轴时间；Runtime 编排这些 owner 的结果。来源上的多个时间约束必须由同一实际观察元组联合满足，不能拼接不同来源的时间轴；未知时间不满足已知时间约束。服务投影过期时可以降级、重建或明确失败，不能把过期投影当作权威认知。

### 诊断

查询结果能够区分权威对象不存在、访问受限、对象被抑制、服务投影不可用或过期、预算不足、来源不可展开、线索不足和真正未知。预算导致的召回不足不得被报告为主体没有相应认知。

## 13. 检索服务与联想结构

### 服务视图

权威认知对象可以派生多个服务视图，包括精确索引、词项文档、稠密向量、实体与标签倒排、语义片段、召回线索、联想拓扑和其他读优化表示。服务视图可以独立失效、删除和重建，不改变权威对象身份。

稠密向量视图绑定完整的向量空间身份。向量空间身份至少能够区分模型或权重、任务、分词和预处理、池化、归一化方式及维度。不同向量空间不得直接混用向量分数。

### 服务代次

每类服务投影按照不可变代次发布。代次记录输入权威水位、实现身份、关键配置摘要、制品身份和必要的校验信息。构建完成并通过一致性检查后再切换当前代次。

查询返回前仍以权威对象为最终依据。服务代次负责高效召回和排序，不拥有认知权威状态。

### 共享概念服务资产

Tag semantic embeddings 是跨 retrieval profiles 共享的 rebuildable concept Serving asset，与 direct attachment postings、必要 lexical material 和 canonicalization metadata 共同服务 direct recall 与 diffusion。Native、VCP 及其他算法复用相同 Tag representation 和 embedding；profile 切换本身不产生另一套概念向量。Embedding 绑定有效 Tag revision、表示版本、vector space 与所选 Authority view。

### 历史服务视图

as-of fence 在候选生成前作用于 lexical、dense、concept、topology 及 query descriptors，不能先用 current vectors/topology 召回未来候选再在末端按记录时间过滤。各 semantic owner 投影自己拥有的历史有效状态；Serving 从该 snapshot 构建可重建历史代次，不复制另一份 durable cognition 或建立独立 history database。

兼容身份使用 canonical effective state 的 view digest；两个时间点投影为同一有效状态时可以复用同一资产。历史代次不发布为 current，受 request read lease、grace 与回收策略保护。不可变 revision 文本继续按内容身份复用 embedding；historical-compatible lane 不可用时显式 unavailable/degraded，不借用未来 current asset。

历史查询同时遵守当前权限、抑制和清除边界；as-of 不恢复已清除内容，也不绕过管理权威。

### 联想拓扑

联想拓扑（AssociativeTopology）是从记忆、标签、经历片段、认知图式、社会关系和关联证据派生的可重建服务图。节点和边的服务权重由版本化构建规则生成。

拓扑构建遵守有限资源原则：出边质量具有固定或归一化预算；高连接度节点受到枢纽或扇出抑制；查询扩展具有跳数、节点、状态、时间和计算预算；共同来源祖先在需要时去重；被截断或未探索的质量能够进入诊断。

负向、矛盾和反例关系具有独立语义，不能在没有定义转换规则时直接作为普通非负传播边使用。

AssociativeTopology 可以消费版本化的 derived Accretion feature，其权重属于 Serving generation。Accretion 的改变只触发服务或维护重算，不写回为 Cognition Authority state。

### 关联证据与服务权重

关联证据保存有来源、有类型的认知关系依据。服务层根据当前有效关联证据、关系类型、方向、极性、来源独立性、对象生命周期和查询意图计算拓扑边权。

系统不保存一个由检索次数不断累加的通用“关联强度真值”。被召回、排序或呈现不会自动生成新的关联证据。只有具有独立语义的外部观察、明确使用结果或领域修订才能成为新的长期支持来源。

## 14. 外部资源与模型能力

### 外部资源

外部资源（Resource）表示主体或调用方可以访问的知识库、文档集合、数据库、搜索服务或其他数据源。Nous Wave 保存资源身份、版本、访问范围和稳定引用，不复制成熟知识库已经提供的全文解析、同步和索引机制。

资源适配器至少提供资源描述、搜索、材料展开、版本检查和访问检查能力。搜索结果包含资源、条目、版本或修订、内容摘要或校验信息、来源区域、观察时间和访问范围。

资源搜索命中仍然属于外部材料。只有主体或认知消费者实际接触结果时才形成观察事件；只有经过目标领域形成和核验流程后才成为长期认知。

### 稳定引用

外部资源引用应尽可能包含提供方身份、资源身份、条目身份、版本或修订、内容摘要、来源区域坐标、获取或观察时间和访问范围。引用在资源更新后能够判断是否仍指向同一内容。

外部资源撤回、权限变化或版本变化会使依赖的派生表示和认知对象进入重新核验流程，不通过静默替换来源内容保持表面一致。

### 模型能力

模型和模型服务按能力合同接入。系统至少区分向量嵌入、重排、结构化提案生成、文本派生、视觉派生和语音派生等能力。

能力合同描述输入输出结构、模型或实现身份、隐私边界、可用性、成本和资源限制。所有派生内容和提案保存生产者签名，使后续重建和失效判断能够识别生成条件。

本地模型网关与远程接口在认知语义中承担相同角色。部署位置不改变权威边界；主体身份和认知状态不得绑定到某个具体模型服务。

### ModelRole、ExecutionProfile 与 ModelProfile

模型工作与模型资源按三层独立表达：

| 概念 | 所有语义 |
| --- | --- |
| ModelRole | 正在执行的认知工作及其 Prompt/structured-output 合同，例如 formation、consolidation、concept maintenance 与 query enrichment。 |
| ModelProfile | 实际模型资源、gateway、protocol、model identifier/revision、capabilities 与适用的 embedding contract。 |
| ExecutionProfile | 调用方式：model profile ref、reasoning/inference controls、temperature、top_p、output budget、timeout、有界 provider options 与可表达的 service/latency preference。 |

同一 ModelProfile 可供多个 roles 使用，也可有不同 ExecutionProfiles；同一 ExecutionProfile 可被多个 roles 引用。模型营销档位不成为硬编码语义。控制组合必须符合实际 protocol/capabilities，不支持的配置显式拒绝。

### RolePolicy、fallback 与执行快照

RolePolicy 将一个 ModelRole 绑定到有序 ExecutionProfile routes 与 optional/required availability。一个 role 可以有零、一或多个 executable routes；Capability 清楚报告未配置、不可用、可降级或必需能力阻塞。Route 顺序表达偏好，不另建 preferred requirement。

Fallback 仅按显式配置的有限 route 顺序处理 execution/infrastructure failure，例如缺失凭据、gateway 不可用、transport、timeout、rate/resource error、protocol/output 或 structured-output failure。Core 不按模型名称或相似能力自动发现替代资源。Owner semantic rejection 不静默触发下一模型；新语义尝试必须由 workflow/Host 的授权和预算拥有。

Operation 开始时冻结 RolePolicy、route 顺序、ExecutionProfiles、ModelProfiles、Prompt/structured contract 与 provider destination policy。配置改变不改写执行中的路线；已有保存 proposal 的基础设施重试复用 proposal，不重新生成。允许 fallback 时，每次 attempt 有稳定执行身份。

### 实际生产者身份

ProducerSignature 记录成功生成 cognition/representation 的实际执行，至少保留 role、model profile、实际 model/revision、successful ExecutionProfile、reasoning/inference controls digest、Prompt id/digest、structured contract digest、RolePolicy digest 与 implementation/protocol。原始媒体或直接协议派生也遵守同一身份合同。

Operation receipt/telemetry 记录 attempted routes、失败分类、fallback transition、成功 route、usage 与 latency；凭据和 raw provider body 不进入这些元数据。ProducerSignature 不把模型输出升级为事实证明，也不把共享 source root 的不同生产者算成独立佐证。

## 15. 持久化、一致性与清除

### 身份层级

持久化层至少区分主体标识、对象标识、修订标识、对象纪元、主体权威提交序号、运行时修订、服务视图集合、服务代次以及请求和事件的幂等标识。

对象标识表示稳定语义对象；修订标识表示不可变内容版本；对象纪元表示当前对象头、生命周期和其他可变对象状态的并发版本；权威提交序号为同一主体提供持久提交顺序。

### 权威写入

权威写入遵循统一的事务语义：

1. 验证请求和权限；
2. 检查幂等身份；
3. 核验预期对象纪元和当前修订；
4. 重新验证来源、访问控制和生命周期；
5. 写入不可变修订和关系；
6. 更新对象头、生命周期和纪元；
7. 记录权威变更及幂等结果；
8. 提交事务。

模型调用、网络搜索和其他不可控外部操作在权威写事务之外完成。它们的结果以带来源和生产者信息的提案进入事务。

同一个幂等请求重复到达时返回同一语义结果。相同幂等标识携带不同规范化内容时返回冲突，不把两次请求视为两个独立操作。

### 投影变化与恢复

权威提交记录需要失效或重建的服务投影类别和处理水位。投影构建器允许重试、崩溃恢复和全量重建；任何旧投影都不能覆盖较新的权威状态。

依赖其他认知对象的日记、认知图式、综合记忆、自我叙事和其他派生认知保存依赖引用。来源修订、撤回、抑制、清除或权限变化时，依赖对象按领域合同重新核验、标记冲突或进入失效状态。

### 对象存储

大型材料和二进制内容写入不可变对象库。写入流程先生成临时对象并校验摘要，再发布稳定对象句柄，最后在权威事务中提交引用。崩溃可以留下未引用对象并由垃圾回收清理，已提交权威引用不得指向不存在的对象。

### 清除

清除（Purge）由管理权威执行。清除流程先隔离普通读取并取消或标记依赖提案，然后按策略处理权威内容，再失效服务投影、缓存和受管理上下文，最后清理对象库中的相关材料并记录不可逆的清除回执。

清除完成后不得保留能够恢复被清除内容的向量、摘要或派生材料。必要的审计记录只保存操作身份、时间、范围和结果等不含被清除语义内容的信息。

## 16. 与 Heptalogos 的系统边界

### 共享主体身份

Nous Wave 与 Heptalogos 使用同一稳定 SubjectId，但分别维护认知主体和行为主体的领域状态。共享标识用于引用同一长期主体，不表示两个系统共享可变对象或数据库事务。

### 职责划分

| 系统 | 主要职责 | 主要输出 |
| --- | --- | --- |
| Nous Wave | 观察与证据、记忆、自我、社会认知、动机、认知运行时、认知查询、资源认知和离线认知 | 认知对象、上下文贡献、认知提案、愿望、关切、期望条件、使用与认知状态 |
| Heptalogos | 外部即时通信和环境摄入、规范交互事实、认知机会与行为调度、主动追求、行为审查、承诺与义务、通信提交、工具与外部效果、产品生命周期 | 主动追求状态、行为决策、约束性承诺、行动计划、外部效果、维护机会和结果回执 |

### 交互数据流

外部世界事实由 Heptalogos 或其他宿主摄入并建立规范交互事实。主体实际接触相应材料时，Nous Wave 记录观察事件和证据，并根据领域规则形成认知提案。

行为处理需要长期主体状态时，Heptalogos 通过认知查询或上下文贡献接口读取 Nous Wave。返回的记忆、自我、社会认知和动机只作为行为决策输入；行为权限和外部效果仍由 Heptalogos 决定。

Heptalogos 对行为结果、外部效果和后续反馈建立自己的权威记录，并把需要影响认知的事实和使用结果返回 Nous Wave。认知领域依据这些证据独立决定是否形成或修订认知。

### 动机与主动追求

Nous Wave 的期望条件描述主体希望某个未来或持续状态如何成立。Heptalogos 的主动追求状态描述主体已经决定持续投入行为资源去追求哪一项期望条件。

Heptalogos 可以根据当前情境、时间、能力、资源、规范、既有承诺和其他主动追求决定采纳、延迟、暂停或结束追求。主动追求引用期望条件的精确修订；期望条件发生实质修订时，行为侧重新核验，不能静默改变既有主动追求的目标语义。

一次具体行为提议、行动计划和承诺分别承担不同职责。行为提议属于当前决策候选；行动计划描述实现手段；承诺与义务表示已经形成的约束。它们都不能反向改写 Nous Wave 的期望条件。

期望条件被撤回后，Heptalogos 重新审查相关主动追求；已经存在的对外承诺、义务和不可逆效果按照行为与规范权威自己的生命周期继续处理。行为执行结果作为证据返回 Nous Wave，用于期望条件的满足评价和后续动机修订。

### 维护机会

Heptalogos 或其他宿主可以根据空闲、离线、维护模式和资源状态向 Nous Wave 授予维护租约。Nous Wave 在租约内选择认知维护工作，并在前台活动抢占或宿主取消时停止。

### 权限关系

Nous Wave 的记忆、自我、社会认知、愿望和期望条件不能绕过 Heptalogos 的系统安全、操作权限和行为规范。Heptalogos 的系统管理命令也不伪装为主体自然形成的认知；需要修改认知时，通过明确的管理或认知提案接口执行。

## 17. 物理架构

### 宿主与内核

目标实现由 TypeScript 宿主和 Rust 内核组成。TypeScript 宿主负责模型服务、外部资源适配、调用方上下文、离线认知工作流、维护租约集成和面向产品的编排；Rust 内核负责认知领域语义、权威写入验证、持久化一致性、认知查询、检索计划、服务投影生命周期和管理操作。

宿主不得直接绕过内核修改认知权威。内核不直接拥有模型供应商账户、外部资源凭据或产品行为调度。

Rust 内核的基础服务包含 Configuration Service。它与 Subject Core、Cognitive Runtime、Query、Serving 及各认知领域共享配置合同，但不得依赖 Memory、Self、Social 或其他具体认知 owner。各领域仍分别拥有自己的对象、形成、修订、生命周期和查询语义；共享配置基础设施不演化为跨领域超级权威。

目标数据流可以概括为：

~~~text
调用方 / Heptalogos
        ↓
Nous Wave 宿主（TypeScript）
        ↓
Nous Wave 内核（Rust）
        ├── structured Authority persistence
        ├── immutable large-object storage
        └── rebuildable lexical / dense / concept / topology Serving families
~~~

各具体数据库、对象存储、词项引擎、ANN 引擎和图服务均属于可替换实现组件。它们必须通过稳定能力合同接入，并能够在不改变语义所有权的前提下替换或重建。

### 持久化与检索组件

结构化 Authority persistence 保存认知权威数据和事务状态。不可变对象库保存大型材料和二进制对象。词项、稠密、共享概念和联想拓扑均属于可重建的 Serving family。

Serving 组件不拥有认知权威状态。具体 provider 的选择由工作负载、过滤能力、多视图支持、资源占用、备份恢复和运维成本的下游评测决定；除非另有独立的长期设计决定，Target Design 不锁定 provider。

### 部署原则

参考部署以个人计算机本地运行优先，允许本地模型与远程模型服务并存。配置、数据和可执行实例分别维护，使实例升级或替换不要求删除主体数据。

管理接口为未来 CLI、管理 API 和图形界面提供稳定能力边界；目标设计不要求在 Nous Wave 仓库中实现特定 GUI。物理模块可以随着工程需要重组，只要不改变本文规定的语义所有权和系统边界。

# 附录 A：术语表

| 术语 | 定义 |
| --- | --- |
| 主体（Subject） | 跨模型、会话和执行进程保持逻辑身份的长期主体。 |
| 主体标识（SubjectId） | 在 Nous Wave 与其他限界上下文之间保持一致的主体逻辑标识。 |
| 认知权威（Cognitive Authority） | 对持久认知对象、修订、生命周期与写入权限具有决定作用的数据与领域合同。 |
| 服务投影（Serving Projection） | 从权威数据构建并可独立重建的索引、向量、拓扑或其他读优化表示。 |
| 原始材料（Artifact） | 稳定的来源内容实体。 |
| 观察事件（ObservationOccurrence） | 主体对材料或事件的一次实际接触记录。 |
| 派生表示（DerivedRepresentation） | 由解析器、模型或其他转换生成并保留来源链的版本化表示。 |
| 证据引用（EvidenceRef） | 指向观察事件、来源区域或派生表示的稳定引用。 |
| 认知指向（CognitionAboutness） | 某项认知在语义上涉及的实体、角色或关系。 |
| 记忆（Memory） | 由记忆域接受并长期保留的主体认知。 |
| 经历片段（Episode） | 对连续经历流进行组织并可修订的事件结构。 |
| 日记（Journal） | 对一段经历或时期进行组织的可修订叙事对象。 |
| 认知图式（CognitiveSchema） | 从多个经历和认知中形成的、具有适用范围和反例的结构性认知。 |
| 标签（Tag） | 有稳定身份、可修订文本表示的 durable semantic concept。 |
| CognitiveClock | Subject 的认知相对时间基准。 |
| TemporalFrame | 捕获 clock、Authority view 与 revision view 的查询时间语义。 |
| QueryContextSnapshot | 冻结实际接纳的任务、Session、typed anchors、Situation、历史排除与截断的 prepared context。 |
| QueryRepresentation | 从 frozen context 编译的有界确定性语义表示。 |
| QueryActivation | 冻结且临时的统一 query-side 概念与上下文激活。 |
| ResultProjection | 与 query intent 分离的返回对象类型选择。 |
| 关联证据（AssociationEvidence） | 认知对象之间具有来源和类型的关联依据。 |
| 自我（Self） | 主体对自身身份、角色、能力、倾向、价值和叙事连续性的长期认知领域。 |
| 社会认知（Social Cognition） | 依赖具体个人、关系、群体、频道或社区语境的长期认知领域。 |
| 语言惯例（LanguageConvention） | 特定社会作用域内的词义、称呼、简称、黑话或语用约定。 |
| 动机（Motivation） | 主体关于愿望、目标、关切和未来状态优先关系的认知领域。 |
| 认知运行时（Cognitive Runtime） | 组织活动认知、工作上下文、注意、驻留集和调用方工作集的运行状态。 |
| 工作上下文（WorkContext） | 保存任务文本与 cognition/Entity/Tag anchors、可持久复用的 Runtime state。 |
| Formation basis | 形成 cognition 或 proposal 时实际使用的精确输入，不证明自然语言蕴含。 |
| Epistemic judgment | 可修订的支持、反驳、纠正等认识关系。 |
| ModelRole / ExecutionProfile / ModelProfile | 分别表达认知工作、执行控制与实际模型资源。 |
| 使用事件（UseEvent） | 调用方对认知对象的真实使用及结果回执。 |
| 可访问性（Accessibility） | 某项认知在当前线索和上下文中被取得的难易程度。 |
| 假设（Hypothesis） | 需要目标领域所有者核验后才能形成权威认知的候选主张。 |
| 维护租约（Maintenance Lease） | 宿主授权离线认知使用的时间、资源、模型、网络和取消边界。 |
| 外部资源（Resource） | 可搜索和展开的外部知识或数据源描述。 |
| 清除（Purge） | 由管理权威执行并覆盖权威数据、服务投影、缓存和材料的破坏性清除流程。 |

# 附录 B：核心数据流

## 认知形成

1. 宿主或外部系统保存原始材料或规范外部事实。
2. 主体实际接触相应内容时形成观察事件。
3. 证据引用固定来源区域、派生表示和来源谱系。
4. 确定性流程或模型产生认知提案，并声明目标领域、主张、认知指向和输入修订。
5. 目标领域所有者核验证据、权限、对象状态和并发版本。
6. 通过核验后提交不可变修订，推进对象头和权威提交序号。
7. 权威变更使相关服务投影失效或进入增量更新流程。

## 认知检索

1. 调用方提交认知查询和计算预算。
2. 系统完成引用解析，冻结 QueryContextSnapshot 与配置，再编译有界确定性的 QueryRepresentation，绑定硬约束、软偏好、主体范围和调用方能力。
3. 在所选 TemporalFrame 内形成统一 QueryActivation，随后在候选生成前固定检索通道、预算和融合参数。
4. 各检索通道生成服务视图命中，并在对象修订层聚合。
5. 跨通道融合和可选重排产生候选顺序。
6. 返回前重新核验所选 Authority/revision view、生命周期、当前访问策略和来源状态，应用 ResultProjection。
7. 实际进入调用方上下文的对象可以记录呈现事件；进一步引用、行动或结果另行记录类型化使用事件。

## 离线认知

1. 宿主授予维护租约。
2. Nous Wave 固定输入对象、来源、访问控制和权威水位快照。
3. 离线流程执行有界回放、比较、反例搜索和关联探索。
4. 结果首先形成假设。
5. 提交前重新核验来源、当前修订、权限和清除状态。
6. 目标领域所有者决定接受、拒绝、标记冲突或判定过期。

## 行为反馈

动机目标、记忆、自我和社会认知可以作为 Heptalogos 的行为决策输入。Heptalogos 形成的承诺、执行结果和外部效果通过类型明确的结果回执返回 Nous Wave。回执本身形成来源事实或使用结果，再由认知领域决定是否形成长期修订。
