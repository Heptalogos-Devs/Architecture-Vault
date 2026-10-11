# Nous Wave 设计决定索引

本文件只列已经确定的设计决定，并指向目标设计和对应论证。详细规范性语义以 [Nous Wave 目标设计](TARGET_DESIGN.md) 为准。

## 系统与权威

### 主体身份独立于模型

**决定：** `SubjectId` 表示长期主体身份；模型、模型服务商、会话和运行进程都是可替换执行条件。

目标设计：第 1、3 章。
论证：[认知权威与行为权威](rationale/07-authority-agency.md)

### 认知权威、认知运行时和服务投影分离

**决定：** 持久认知、认知运行时、检索服务投影使用不同身份和生命周期。索引、向量、传播状态和中心性不能成为认知权威状态。

目标设计：第 2、10、13、15 章。
论证：[持久认知与服务投影](rationale/08-persistence-serving.md)

### 跨领域写入通过提案

**决定：** 模型、离线认知和其他领域默认只能提交带来源和输入修订的提案；目标领域所有者负责核验和最终写入。

目标设计：第 2、3、11 章。
论证：[认知权威与行为权威](rationale/07-authority-agency.md)

### Configuration Service 是共享基础设施

**决定：** Nous Wave 建立统一 Configuration Service。各 subsystem/domain owner 注册自己拥有的配置 key、类型、参考默认值、校验、暴露等级、作用域和应用方式；服务统一负责解析、覆盖、快照、来源诊断和 digest。Leaf algorithm 接收 typed policy，不直接按字符串读取全局配置。

目标设计：第 2、17 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### 配置层级与系统不变量分离

**决定：** 可修改配置按 Developer、Advanced、Standard 描述暴露等级；对象身份、领域所有权、不可变修订、生命周期、并发、幂等、权限和清除等系统不变量不成为配置开关。配置元数据与配置能力同时建立，未来管理界面只消费同一份描述。

目标设计：第 2 章。

### 同一主体可并行服务多个会话与调用方

**决定：** 一个 Subject 可以同时被多个 Session 和多个 consumer 使用。durable cognition 归 Subject 共享；ResidentSet、foreground WorkContext binding、runtime revision 等 Session 运行时状态按 Session 隔离；WorkContext 保存有界任务连续性、context_text 与 typed cognition/Entity/Tag anchors，不复制 Memory；ConsumerWorkingSet 与 UseEvent 按调用方和事件身份隔离。Session 或 consumer 不拥有复制的 Subject Memory。

目标设计：第 3、10 章。

论证：[持久认知与服务投影](rationale/08-persistence-serving.md)

### Memory-only 是正式能力组合

**决定：** Memory 是最小完整认知能力。Self、Social Cognition、Motivation 以及后续高级领域均为可选 owner；关闭这些领域不能削弱 Memory 的启动、查询、Serving、restart、rebuild、purge 或恢复语义。

目标设计：第 1、3、17 章。

### Process Capability 与 Subject Capability 分离

**决定：** Process Capability 表示当前部署提供的领域上限；Subject Capability 表示某个主体已经明确供给的领域集合。主体能力不得超过进程能力，未供给领域不通过空状态或占位对象模拟存在。新主体可以使用配置提供的默认供给，但已创建主体的 typed capability set 不随默认配置变化。

目标设计：第 1、3 章。

### 认知 operation 使用单一不可变配置快照

**决定：** 一次认知形成、查询或 Serving 构建固定一个 resolved ConfigSnapshot。reference default、部署文件、system override、subject override 按确定顺序解析；影响 Authority formation 或服务制品的 key subset digest 随相关记录保存，后续配置变化不重写历史语义。

目标设计：第 2、13、15 章。

### Cognition Authority 表达主体认知与演化

**决定：** 持久 cognition 属于 Subject 当前或历史状态，不认证 objective truth。Owner 保证身份、真实 basis/provenance、权限、生命周期、并发、幂等、清除与历史切面；事实错误和自然语言蕴含错误属于认知质量。新 revision 不承诺真值升级，历史认知不被后来的纠正改写。

目标设计：第 2、4、5 章。
论证：[认知、形成依据与模型执行](rationale/12-cognition-basis-model-execution.md)

### Provenance、formation basis 与 epistemic judgment 分离

**决定：** Provenance 是真实来源谱系；basis 是形成时实际使用的输入；support/contradict/correct 等认识关系是可修订语义判断。Grounded 表示显式 basis 与 provenance，不表示客观核实；使用事件和不同模型的同源重述不制造真值或独立佐证。

目标设计：第 4、5、10 章。
论证：[认知、形成依据与模型执行](rationale/12-cognition-basis-model-execution.md)

### 模型角色、执行方式与资源独立

**决定：** ModelRole 表示认知工作，ExecutionProfile 表示调用控制，ModelProfile 表示资源。同一模型可服务多个 roles；一个 role 可有零、一或多个显式 routes。RolePolicy 使用 optional/required 与 route 顺序表达可用性和偏好。

目标设计：第 14 章。
论证：[认知、形成依据与模型执行](rationale/12-cognition-basis-model-execution.md)

### Fallback 与实际生产者由冻结 policy 决定

**决定：** 本次调用在内存中固定 RolePolicy/routes、execution/model profiles 与生成合同。Fallback 仅限配置内的 infrastructure/execution failure；owner semantic rejection 不自动换模型。ProducerSignature 绑定实际成功 route 与执行控制；不要求持久化调用快照、失败尝试或中间提案以恢复执行。

目标设计：第 14 章。
论证：[认知、形成依据与模型执行](rationale/12-cognition-basis-model-execution.md)

## 寻址、查询与概念维护

### AI/Agent 可引用地址与 Authority identity 分离

**决定：** Name/Alias 用于 discovery，稳定且语义中立的 LexicalRef 用于 exact continuation；各 owner Authority identity 决定对象身份。歧义显式返回候选，Host-owned Entity/Resource 保持宿主 canonical identity。

目标设计：第 3 章。
论证：[设计论证](rationale/10-query-addressing-and-preparation.md)

### Query preparation precedes QueryPlan

**决定：** 引用解析后先冻结 QueryContextSnapshot 与 ConfigSnapshot，再形成 QueryRepresentation、共享 QueryActivation 和 QueryPlan；unknown/ambiguous 以显式结果返回，Agent 可以补充上下文、选择候选并多轮 resolve。

目标设计：第 12 章。
论证：[设计论证](rationale/10-query-addressing-and-preparation.md)

### Runtime context 可复用且先冻结

**决定：** Foreground WorkContext 和 Session ResidentSet 自动接纳；显式 pinned Entity/Tag/cognition、one-shot Situation 与 query cues 共同形成 QueryContextSnapshot。Snapshot 保存实际 context revisions、digest、admitted refs、历史排除与截断；所有 profiles 共用由此产生的 representation/activation，不自行推断另一套 Tags。

目标设计：第 10、12 章。
论证：[查询寻址与准备](rationale/10-query-addressing-and-preparation.md)

### Query semantic representation 包含当前认知上下文

**决定：** semantic intent、resolved semantic descriptors、当前认知、WorkContext 与 Situation 编译为有界、确定性的表示，保留 exact source refs；opaque IDs 只负责绑定和约束。同一 prepared query 的 semantic input 不随 profile 改变。

目标设计：第 12 章。
论证：[设计论证](rationale/10-query-addressing-and-preparation.md)

### Tag 与 AssociationEvidence 支持自动认知维护

**决定：** accepted/revised cognition、有意义 UseEvent 或显式 review 可以触发有界模型或确定性提案，各领域 owner 验证并执行 mutation；后置 Tag attachment 不改写历史 cognition revision。

目标设计：第 6、11 章。
论证：[设计论证](rationale/02-schema-association.md)

### Semantic Accretion 是派生信号

**决定：** 从 provenance、recurrence、association 和有意义 use 派生吸积信号，用于概念演化和版本化检索；可删除重算，不构成 Anchor Authority、认知 truth 或通用 strength。

目标设计：第 6、13 章。
论证：[设计论证](rationale/02-schema-association.md)

### 模型建议列表不建立超级事务

**决定：** 每项建议按领域 owner mutation 合同直接提交；Tag merge/split 和 Episode partition 等天然原子操作继续原子。后项非法保留前项独立提交。运行失败明确报告，已完成领域结果保留；不维护跨进程恢复提案执行的检查点。

目标设计：第 6、11、15 章。
论证：[设计论证](rationale/02-schema-association.md)

### Bare text 是一等 Cognitive Query

**决定：** 非空自然语言 intent 独立走 lexical+dense、固定融合和 owner validation；代词与指示词不阻止执行，contextualization、concept enrichment 与 exploration 均为可选质量增强。纯 selector/时间/context 不能代替 text intent。

目标设计：第 12 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### ResultProjection 与 query intent 分离

**决定：** 默认返回 Memory/Schema/Episode/Journal；Evidence/Resource 在明确 projection 或 resource intent 时成为顶层结果，exact target 同样受投影约束。

目标设计：第 12 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### TemporalFrame 统一认知时间与历史修订视图

**决定：** 相对时间绑定准备时捕获的 Subject CognitiveClock；多轴 filters 取交集；Authority as-of 与 current/history revision view 分别表示。

目标设计：第 4、12 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### 历史查询隔离完整 Authority/Serving view

**决定：** 候选生成、描述、Tag canonicalization、concept vectors 与 topology 均只读所选有效历史状态；权限和 purge 边界仍有效。

目标设计：第 4、13、15 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### Tag 是可嵌入语义概念身份

**决定：** effective label/description/kind 形成唯一 canonical semantic representation，表达主题、规则和经验模式；身份与显示字符串独立。

目标设计：第 6 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### QueryActivation 保持 ephemeral

**决定：** 各 profile 共享 explicit/inferred concepts 和 exact context；novel hypothesis 不直接创建 durable Tag。

目标设计：第 6、12 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### direct Tag recall 与 associative diffusion 分离

**决定：** Tag activation 可直接召回 attachments；只有显式 associative exploration 才传播，DSL 不暴露物理算法参数。

目标设计：第 12、13 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### Host feedback 可进入后续 concept maintenance

**决定：** 有意义 UseEvent 可关联实际 query 的有界概念反馈；阈值只 enqueue need，proposal 仍需真实 formation basis/provenance、明确认识关系与 owner 核验。

目标设计：第 10、11 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### 模型工作机会由 Host 授权

**决定：** form/query 明确授权各自模型工作；maintenance model 仅在 Host grant 内执行，自动 enqueue 不授权后台 LLM。

目标设计：第 11、14 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

### concept vectors 跨算法复用

**决定：** Tag embedding 与 direct postings 是 profile-independent Serving；历史视图按 effective-state digest 复用，read lease 保护并可回收。

目标设计：第 13、17 章。
论证：[时间、概念与查询](rationale/11-temporal-concept-query.md)

## 自我与初始化

### 认知种子是版本化来源文档

**决定：** Cognitive Seed 是人类编写的结构化主体初始化来源。原始版本保持不变；主体创建时绑定精确版本并保存实例快照或等价内容身份，后续认知演化不修改原始种子。

目标设计：第 7 章。\
论证：[认知种子与静态自我档案](rationale/09-cognitive-seed-self-profile.md)

### 认知种子按语义归属初始化多个领域

**决定：** 种子中的身份、自我认知、人格、价值和叙事内容进入 Self；经历与初始知识可以进入 Memory；人物关系和语言惯例可以进入 Social；愿望、关切和期望条件可以进入 Motivation。Seed 本身不成为跨领域超级对象。

目标设计：第 7 章。\
论证：[认知种子与静态自我档案](rationale/09-cognitive-seed-self-profile.md)

### 安全与管理员强制规则不由认知种子承担

**决定：** 安全政策、操作权限、管理员强制行为和不可绕过的行为限制由 Heptalogos 或宿主的行为与规范权威维护，不依赖会演化的 Self 或 Cognitive Seed。

目标设计：第 2、7、16 章。\
论证：[认知权威与行为权威](rationale/07-authority-agency.md)

## 记忆

### 认知角色与形成方式分别表示

**决定：** 记忆至少分别记录认知角色和形成方式。认知角色包含经历性记忆、陈述性记忆和程序经验；形成方式包含经历落地形成和综合形成。

目标设计：第 5 章。
论证：[记忆分类与认知图式](rationale/01-memory-model.md)

### 认知图式属于记忆领域的一等对象族

**决定：** 认知图式具有独立身份、修订、适用范围、支持、反例、拆分和合并语义，由记忆领域拥有。

目标设计：第 6 章。
论证：[记忆分类与认知图式](rationale/01-memory-model.md)

### 认知结构与检索拓扑分离

**决定：** 结构性认知由认知图式表达；检索中心性和传播结构由可重建联想拓扑表达。系统不建立兼具两种职责的统一权威对象。

目标设计：第 6、13 章。
论证：[认知图式、关联证据与联想拓扑](rationale/02-schema-association.md)

### 关联证据与服务边权分离

**决定：** 权威层保存有来源、有类型的关联证据；服务层根据当前有效证据计算边权。检索次数本身不生成长期关联支持。

目标设计：第 6、13 章。
论证：[认知图式、关联证据与联想拓扑](rationale/02-schema-association.md)

## 社会认知

### 社会认知是独立顶层领域

**决定：** 社会认知维护依赖具体个人、二人关系、群体、频道或社区语境的长期认知，首批对象族为关系认知图和语言惯例。

目标设计：第 8 章。
论证：[社会认知领域](rationale/03-social-cognition.md)

### 关系认知默认有向

**决定：** `A → B` 的关系认知不自动生成 `B → A`。对称或逆向查询由查询或服务投影层处理。

目标设计：第 8 章。
论证：[社会认知领域](rationale/03-social-cognition.md)

### 关系程度与认识确定度分离

**决定：** 关系本身的程度和主体对该判断的确定程度是两个独立属性；不得用同一个数值同时表示。

目标设计：第 8 章。
论证：[社会认知领域](rationale/03-social-cognition.md)

### 关系类型自己声明 degree 语义

**决定：** Relation Type 声明方向性、可选逆/对称关系、允许实体类型、degree semantics 和 temporal semantics。Degree 可不存在，也可以是 ordinal、bounded scalar 或 typed state；不同 relation type 的 degree 默认不可直接算术比较。Relation degree 与 epistemic certainty 继续分离。

目标设计：第 8 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### 语言惯例具有社会作用域

**决定：** 黑话、称呼和语用约定按个人、二人关系、群体、社区或频道等作用域维护；主体自己的重复输出不构成新的独立外部证据。

目标设计：第 8 章。
论证：[社会认知领域](rationale/03-social-cognition.md)

### LanguageConvention 的接受要求外部社会证据

**决定：** 显式解释/确认、独立外部一致使用、成功理解后的持续外部使用和修复过程可以支持 LanguageConvention；单次上下文猜测只形成 hypothesis；主体自己的重复输出不构成新的独立外部证据。

目标设计：第 8 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

## 动机与主动性

### Motivation 使用愿望、关切和期望条件

**决定：** Nous Wave 的 Motivation 保存 Desire、Concern 和 Desired Condition。期望条件表示能够依据证据评价的期望未来或持续状态，不表示主体已经决定采取行动。

目标设计：第 9 章。\
论证：[动机认知与主动行为](rationale/07-authority-agency.md)

### 期望条件采用四种基本时间形式

**决定：** 期望条件区分达成、终止、维持和避免四种时间形式，并可带时间范围和适用上下文。满足判断由证据支持；观察覆盖不足时保持未知。

目标设计：第 9 章。\
论证：[动机认知与主动行为](rationale/07-authority-agency.md)

### 期望条件与主动追求分离

**决定：** Nous Wave 维护期望条件；Heptalogos 维护是否持续投入行为资源的 Pursuit。期望条件存在不会自动产生主动追求，Pursuit 必须引用期望条件的精确修订并由行为侧独立采纳。

目标设计：第 9、16 章。\
论证：[动机认知与主动行为](rationale/07-authority-agency.md)

### 主动追求、行为提议、行动计划与承诺分别维护

**决定：** Pursuit 表示长期主动追求；BehaviorIntent 表示一次决策中的行为提议；ActionPlan/InteractionPlan 表示实现手段；Commitment/Obligation 表示具有约束力的责任。它们不合并为同一 Goal 状态机。

目标设计：第 9、16 章。\
论证：[动机认知与主动行为](rationale/07-authority-agency.md)

## 运行时与检索

### 检索轨迹与长期使用事件分离

**决定：** 候选生成、召回和排序等属于检索轨迹；只有真实呈现、引用、据此行动和结果等语义进入长期使用事件。

目标设计：第 10 章。
论证：[使用事件与可访问性](rationale/04-runtime-accessibility-use.md)

### 长期使用事件必须幂等

**决定：** 调用方为长期使用事件提供稳定事件标识；重试同一事件不能制造额外认知使用。

目标设计：第 10、15 章。
论证：[使用事件与可访问性](rationale/04-runtime-accessibility-use.md)

### 自动可访问性是查询时状态

**决定：** 自动可访问性不是长期认知权威状态；固定年龄不能自动删除或永久隐藏仍合法存在的认知。

目标设计：第 5、10 章。
论证：[使用事件与可访问性](rationale/04-runtime-accessibility-use.md)

### 查询计划在候选产生前固定

**决定：** 查询计划预先确定检索通道、预算和融合参数；实际候选集合不能反向改变其他通道的权重或归一化定义。

目标设计：第 12 章。
论证：[检索计划与结果融合](rationale/05-retrieval-fusion.md)

### 多个服务视图先聚合到对象修订

**决定：** 同一修订的规范表示、段落表示和召回线索等视图不构成多份独立证据；跨通道融合前先聚合到对象修订层。

目标设计：第 12、13 章。
论证：[检索计划与结果融合](rationale/05-retrieval-fusion.md)

### 拓扑检索是普通检索通道

**决定：** 联想拓扑输出有界候选排序，并通过查询计划参与统一融合；不得在计划之外提供隐藏加分。

目标设计：第 12、13 章。
论证：[联想检索机制](rationale/06-associative-retrieval.md)

## 本轮设计收敛

### 陈述性记忆身份以认知事项连续性为准

**决定：** 陈述性 Memory Object 表示一个持续的认知事项。对同一 referent、claim family、scope 和 world-valid interval 的纠正、澄清、收窄或重新解释形成 revision；新的世界状态、独立事件、不同有效时间中的状态变化或新的综合主张形成新的认知对象。文本相似度和向量距离不能单独决定对象身份。

目标设计：第 5 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### 证据独立性从 provenance 派生

**决定：** Authority 保存来源、观察、派生和认知推导的 provenance；独立佐证是对 lineage 的派生判断。共享来源、共享派生和未知依赖不能被多个记录数量自动放大成多份独立支持。系统不建立替代来源结构的统一全局置信分数。

目标设计：第 4 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### Self 由可独立修订的自我认知和叙事组织共同构成

**决定：** 身份、角色、能力、局限、人格倾向、价值和长期偏好在能够独立变化、被质疑、拥有来源或拥有 scope 时维护独立对象身份；Narrative Identity 引用 Episode、Memory 和 Self revision 组织长期连续性，不复制这些对象的权威内容。

目标设计：第 7 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### Desired Condition 使用有界类型化条件表达

**决定：** Desired Condition 使用版本化 predicate/evaluator 叶子和有限 ALL / ANY / NOT 组合，并单独声明 temporal form、applicability、time window 和 observation coverage。条件真值至少区分 satisfied、violated 和 unknown；Maintain/Avoid 等开放世界条件不能因未观察到反例而自动判定满足。通用脚本和完整规则语言不进入 Desired Condition 核心模型。

目标设计：第 9 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### Episode 支持层级与分段轨道

**决定：** Episode 可以形成层级；同一 Observation 可参与多个 segmentation track。不同 track 可以重叠；同一 parent + track 中 sibling Episode 默认形成有序非重叠分段。分段算法只提出边界候选，不直接取得 Episode Authority。

目标设计：第 6 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### Durable WorkContext checkpoint 属于 Runtime state

**决定：** WorkContext 在需要长暂停、跨进程或跨 Session 恢复时可以形成 durable checkpoint。WorkContext 保存可复用 purpose/context_text、未决问题、cognition/Entity/Tag anchors、约束、expected revision、恢复条件和预算摘要；storage bound 与 query projection budget 分离；恢复时重新核验当前 Authority。Prompt/cache/model hidden state 不成为认知 Authority。

目标设计：第 10 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### 多 WorkContext 分配采用有界公平、紧急借用和防饥饿语义

**决定：** Runtime 的资源分配必须允许有界公平份额、紧急任务临时借用、显式抢占和防饥饿。精确 utility function 与参数属于 Runtime Spec/algorithm research。

目标设计：第 10 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### MaintenanceNeed 是运行工作义务而非认知领域

**决定：** 依赖修订、矛盾、过期派生、Journal/Schema 重核验和 Serving rebuild 等维护需求通过 Runtime/Offline Cognition 的 durable work obligation 表达，不建立新的 Cognition Authority。

目标设计：第 11 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

### Hypothesis exploration 必须有有界搜索范围和停止语义

**决定：** Offline hypothesis exploration 在开始时固定资源、来源、反例搜索、能力和抢占 envelope；无新独立来源、预算耗尽、反例搜索耗尽、低信息增益、循环、背压、权限变化和显式取消均可成为停止原因。停止不等同于 hypothesis 被证明或证伪。

目标设计：第 11 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)

## Nous Wave 与 Heptalogos

### 共享主体标识，分离认知与行为状态

**决定：** Nous Wave 与 Heptalogos 使用同一逻辑主体标识，但分别维护认知主体和行为主体的权威状态。Nous Wave 的认知状态只作为 Heptalogos 行为判断的输入，不直接取得行为权限。

目标设计：第 3、16 章。
论证：[认知权威与行为权威](rationale/07-authority-agency.md)

## 物理架构

### TypeScript 宿主与 Rust 内核

**决定：** TypeScript 宿主负责模型、资源、上下文和离线流程编排；Rust 内核负责领域语义、认知权威、查询和服务投影生命周期。structured Authority persistence 保存结构化权威数据，大型材料进入 immutable object storage。

目标设计：第 17 章。
论证：[持久认知与服务投影](rationale/08-persistence-serving.md)

### Generic serving/storage provider 不自动成为长期架构 Authority

**决定：** Target Design 固定 TypeScript Host、Rust Kernel、structured Authority store、immutable object storage 以及可重建 lexical/dense/concept/topology Serving family。具体 provider 若没有单独长期决定，则继续属于 implementation/Plan/Spec 层，不在 Target Design 中永久锁定。

目标设计：第 17 章。
论证：[下一阶段研究综合](research/2026-09-next-stage-engineering-synthesis.md)
