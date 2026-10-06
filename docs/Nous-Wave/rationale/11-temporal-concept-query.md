# 时间、概念与查询

## 已确定的设计

[目标设计](../TARGET_DESIGN.md)将 Bare Text Query、TemporalFrame、Semantic Concept Plane、QueryActivation 和 Host feedback 置于同一查询与认知演化模型中。[决定索引](../DECISIONS.md)记录已接受结论；阈值、默认 enrichment 策略、质量成本和历史资产保留策略见[未决问题](../OPEN_QUESTIONS.md)。具体 NousQL 字符语法、数据结构、CLI 和缓存表由代码仓库负责。

## 查询意图与结果类型

以 Memory 等对象名作为 query directive，容易混淆“是否查询记忆”和“希望返回哪种对象”。把 Cue Expression 和 ResultProjection 分开，使调用方先表达问题，再限定需要的结果形态。默认 Cognition 包括 Memory、CognitiveSchema、Episode 和 Journal；Evidence/Resource 可以支持结果而不占据默认顶层结果。

self-contained semantic text 已经能够表达完整问题。要求所有查询先有 Entity、Tag、WorkContext 或 Agent loop，会使普通检索依赖与问题无关的状态和模型成本。Bare Text Query 因此是正式路径：lexical+dense → fixed fusion → owner validation。Context 和概念激活扩展能力，同时保持最小输入完整。

## Filter、as-of 和 history 的不同问题

五轴 filter 问“事件何时发生、主体何时观察、主张何时有效、认知何时形成、记录何时提交”；as-of 问“主体当时已经知道什么”；history 问“认知有哪些 eligible revisions”。一个 recorded-time predicate 不能代替完整历史视图。

例如，未来修订的 Tag 描述可能通过 current embedding 召回旧 Memory，即使末端过滤保留的 Memory 早于 cutoff，查询也已使用未来概念。未来 merge、Schema supports 和 AssociationEvidence 同样会改变候选图。因此历史隔离必须在 descriptors、identity canonicalization 和每个 Serving lane 的候选生成前完成。

current revision view 选择指定视图中的 effective head；history 将 eligible prior revisions 纳入候选。各 owner 解释自己的 revision/lifecycle，Serving 构建 disposable projection，Runtime 组合统一视图。以 effective state 而非任意时间点识别资产，可复用等价 snapshot，避免每次时间查询永久复制索引。

Subject CognitiveClock 固定相对时间解释，使在线运行、历史重放和测试使用同一语义。基础设施时间继续负责 timeout、retry 和 leases。准备时捕获一次 clock，执行中时钟推进不重绑已经准备的 query。

## Tag 的身份与语义

稳定 Tag 可以表达经验规则或一句话式概念。仅以 label 当分类 key，会丢掉 description 对复杂概念的解释；将 opaque identity 当 embedding 文本，又会让地址代替语义。

唯一 canonical semantic representation 由 effective label、description 和 kind 组成，身份与 alias discovery 另行保存。各 profile 复用 shared concept embedding asset；修订改变文本与向量身份，切换传播算法不重建另一套概念语义。

Formation-time explicit Tag 是 Host 已知的概念上下文，由 Memory owner 验证并提交。后置 attachment 用 AssociationEvidence 表达，不重写形成时的 revision。长期 inferred Tag 统一交给 concept maintenance，避免 formation 和 maintenance 各自维护 reuse/merge policy。

## Durable concept 与 QueryActivation

查询可以激活已有 Tag，或提出 novel concept hypothesis；它们描述当次检索线索，不能直接成为主体已经接受的概念。统一 QueryActivation 保存 exact refs、explicit/inferred concepts、runtime context 和探索意图，各算法读取同一输入。

语义激活并不承担名称歧义消解。明确 Tag selector 仍要求唯一 identity resolution；semantic cue 则可以匹配相关既有概念，不声称同名 Tag 存在。可选模型只能选择 supplied catalog 或给出有界无身份 hypothesis。

## Direct recall 与 diffusion

已知概念的直接 attachments 是可解释的单步召回，不应被迫依赖扩散。TagDirect 不要求 exploration，也不会在无 attachment 时自动转入多跳。

显式 associative exploration 使用相同 activation，加上 lexical/dense promoted seeds。Native、DTSC 和 RiverMemo 的传播权重与物理机制属于 profile；Agent 只表达需要联想扩展。Direct/explore 分离也使纯文字路径可以独立验收。

## Query feedback 与 Host 模型授权

曝光次数和 activation 次数若直接增加长期支持，会制造检索自我强化。Runtime 因此只保留有界、可过期的 query correlation；Host 的 meaningful UseEvent 证明实际使用，并关联 query 返回的 exact revision。

达到 review 条件只产生 MaintenanceNeed。Host grant 后，maintenance 才能读取 repeated inferred Tags、novel hypotheses 和实际 use context，提交有来源的 concept proposal。query hypothesis 不是事实来源，AssociationEvidence 仍需真实 cognition/source supports。presented 不构成长久强化或独立 provenance。

Host 发起 form/query 授权相应模型工作；系统可以自动 enqueue needs、构建 Serving 或计算允许的查询激活，但后台 scheduler 不自行授权 LLM maintenance。该边界把可重建运行机制、维护机会和长期认知接受分别交给正确 owner。
