# 查询寻址与准备

## 三层寻址

Display Name / Alias → LexicalRef → Authority identity 分别承担候选发现、精确续接和领域身份。名称与描述会随认知演化，稳定地址则保持语义中立；改名或修订不重新分配地址，已进入历史的地址不能绑定给另一对象。Host Entity 和 Resource 继续使用宿主 canonical identity，稳定引用只提供可引用入口。

同名可能指向多个合法对象。Embedding 或模型可以帮助检索语义相关内容，却不能默默替调用方确定对象身份。唯一发现结果可绑定，歧义返回 candidates，未知返回显式结果；调用方选择或补充上下文后重新解析。

## 准备先于计划

Agent 或 consumer 提供能够独立解释的 semantic intent。PrepareQuery 解析 selector、固定 Session/WorkContext/Active Cognition、Situation 与 Configuration snapshot，再形成 Query Representation。QueryPlan 据此冻结 lanes、预算和融合；准备阶段无需调用 provider 或执行检索。

Representation 使用 Entity 显示名、Tag label/description、Schema/current cognition descriptor、WorkContext purpose、时间方向和 consumer/task 语义，保留对应 exact source refs。UUID、LexicalRef 和 revision IDs 负责绑定与约束，不能替代 semantic descriptor。有界、确定性的编译和显式截断诊断，让不同 retrieval profile 使用同一 prepared query semantic input；dense/sensing 和 rerank 可以共享该输入。具体压缩策略仍可研究。

## 一等纯文字查询、文本兼容性与 Agent loop

self-contained semantic text 是正式 Cognitive Query 的最小完整输入；无需 exact selector、WorkContext、概念模型或探索。raw-text compatibility 则是独立研究输入模式，不替代正式纯文字路径。TemporalFrame、ResultProjection、统一 QueryActivation 和历史隔离的选择理由见[时间、概念与查询](11-temporal-concept-query.md)。

外部 raw-text compatibility 独立使用原始文本，不注入 Entity/Tag/WorkContext oracle，也不冒充完整 cognitive input；实验结果单独解释。

Agent 可以多次调用工具：名称发现 → 收到候选 → 选取 LexicalRef → query preparation 与 inspection → query execution → 后续 exact continuation。单次查询只执行准备好的意图，通用 planning 与未闭合指代由 Agent/consumer 处理。

具体地址编码、词表、prefix、NousQL grammar、CLI commands 与 transport shapes 由代码仓库 Active Specs 和 Reference 维护。[目标设计](../TARGET_DESIGN.md)固定长期寻址、准备与 owner 语义。
