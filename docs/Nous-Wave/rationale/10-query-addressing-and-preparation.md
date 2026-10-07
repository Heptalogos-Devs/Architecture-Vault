# 查询寻址与准备

## 三层寻址

Display Name / Alias → LexicalRef → Authority identity 分别承担候选发现、精确续接和领域身份。名称与描述会随认知演化，稳定地址则保持语义中立；改名或修订不重新分配地址，已进入历史的地址不能绑定给另一对象。Host Entity 和 Resource 继续使用宿主 canonical identity，稳定引用只提供可引用入口。

同名可能指向多个合法对象。Embedding 或模型可以帮助检索语义相关内容，却不能默默替调用方确定对象身份。唯一发现结果可绑定，歧义返回 candidates，未知返回显式结果；调用方选择或补充上下文后重新解析。

## 准备先于计划

Agent 或 consumer 提供非空自然语言 intent。PrepareQuery 解析 selector，先冻结 QueryContextSnapshot 与 Configuration snapshot，再形成 QueryRepresentation。Snapshot 记录 foreground WorkContext revision、context text digest、typed cognition/Entity/Tag anchors、Session/runtime revision、实际 admitted ResidentSet refs、one-shot Situation、历史排除与截断。QueryPlan 据此冻结 lanes、预算和融合；准备阶段无需调用 provider 或执行检索。

Representation 使用 Entity 显示名、Tag label/description、Schema/current cognition descriptor、WorkContext purpose/context_text、时间方向和 consumer/task 语义，保留对应 exact source refs。UUID、LexicalRef 和 revision IDs 负责绑定与约束，不能替代 semantic descriptor。有界、确定性的编译和显式截断诊断，让不同 retrieval profile 使用同一 prepared query semantic input；dense/sensing 和 rerank 可以共享该输入。具体压缩策略仍可研究。

## 一等纯文字查询、可选 contextualization 与 Agent loop

非空 natural-language intent 是正式 Cognitive Query 的最小完整输入；无需 exact selector、WorkContext、概念模型或探索。Selector 和 directives 丰富文本意图，纯 selector 不成为 Cognitive Query。TemporalFrame、ResultProjection、统一 QueryActivation 和历史隔离的选择理由见[时间、概念与查询](11-temporal-concept-query.md)。

显式 referent 有助于词项、向量与概念激活，因而强推荐；普通代词或指示词仍可执行。Runtime 不通过语言词表判断 closure。Raw text、context-assisted representation 与 Host-explicit contextualized intent 的质量可分别比较；研究 plain baseline 用显式能力配置控制增强，不建立额外 compatibility 产品模式。

Reusable WorkContext 使 Agent 无需每轮重复搬运任务背景和 pinned anchors。任务文本属于操作上下文而非 evidence；固定 Entity/Tag 不重写原始 intent，也不使模型推断的概念自动变成长期 pin。Durable storage 和 representation section budget 分离，统一投影策略显式报告截断；所有 profiles 共用同一 prepared input。

prepare 保持 provider-free。未来 model-assisted contextualizer 可以位于 Host 层，是否调用由 workflow 和预算决定。

Agent 可以多次调用工具：名称发现 → 收到候选 → 选取 LexicalRef → query preparation 与 inspection → query execution → 后续 exact continuation。单次查询执行准备好的意图；Agent/consumer 可以主动补充 referent 或规划下一步，未经扩展的普通自然语言同样合法。

具体地址编码、词表、prefix、NousQL grammar、CLI commands 与 transport shapes 由代码仓库 Active Specs 和 Reference 维护。[目标设计](../TARGET_DESIGN.md)固定长期寻址、准备与 owner 语义。
