# Nous Wave 未决问题

本文件只保留仍然需要研究、实验或后续 Spec 才能决定的问题。

已经确定的领域边界、Authority、对象归属、跨系统职责以及本轮已经收敛的中层语义不再重复列为 OPEN。

# Memory 与认知结构

## Declarative identity matcher

目标语义已经区分“同一认知事项的 revision”和“新的 world state / cognition object”。

仍需在 Spec/研究中决定：

- referent、claim family、scope 和 valid-time 如何形成稳定 identity comparator；
- 模型辅助 identity proposal 如何被 deterministic constraints 限制；
- ambiguous merge/split 如何保留人工或领域 owner 可纠正性。

## CognitiveSchema formation

仍需研究：

- Schema 自动形成的 minimum evidence structure；
- 反例如何影响 scope；
- split / merge 的触发条件；
- Schema revision 与新 Schema object 的判定；
- 自动形成是否能稳定优于简单 synthesized declarative memory。

## 概念维护与 Accretion 算法

- Accretion 聚合函数、参数与默认策略；
- concept reuse/merge/split 的质量 policy；
- Query Representation 的具体压缩策略。

稳定引用、显式 identity resolution、自动概念维护和 Accretion 的 derived status 已锁定，算法研究在这些合同内进行。

# Self

Self 的对象粒度原则已经确定。

仍需研究：

- Self proposal 的接受门槛；
- personality/value/preference 的不同演化速度是否需要不同 policy；
- Narrative Identity 何时新建 thread、何时修订同一 thread；
- model reflection 与外部 evidence 的相对作用如何进入 proposal review。

# Social Cognition

Relation Type 必须声明自身 degree semantics 已确定。

仍需研究：

- reference profile 首批 relation ontology；
- 不同 relation type 的 degree update policy；
- 跨平台 entity binding 的证据聚合；
- group/community relation 的推导和冲突处理；
- LanguageConvention 自动形成的重复次数、时间跨度和 repair 信号参数。

# Motivation

Desired Condition 的 bounded typed expression、三值评价和 coverage requirement 已确定。

仍需研究：

- reference profile 首批 predicate/evaluator catalog；
- 不同外部资源的 observation coverage 如何描述；
- 周期性条件和滑动时间窗口的评价策略；
- evaluator revision 与 Desired Condition revision 的兼容规则；
- Motivation 中长期 priority relation 的形成和修订 policy。

# Cognitive Runtime

Episode 的 hierarchy/track 语义和 WorkContext checkpoint 已确定。

仍需研究：

- Episode boundary detector；
- attention utility function；
- urgency borrowing / anti-starvation 的参数；
- WorkContext continuity cost；
- Active Cognition 的 admission / eviction policy；
- accessibility 的函数形式和参数。

# Offline Cognition

MaintenanceNeed 与 bounded hypothesis exploration 已确定。

仍需研究：

- expected information gain estimator；
- counterexample search 的预算分配；
- MaintenanceNeed priority function；
- 多个 hypothesis 竞争资源时的调度；
- offline cross-domain proposal batching / coalescing 是否有价值。

# Retrieval 与 Serving 算法研究

以下必须通过实验决定：

- lexical / dense / entity / runtime lane 的默认融合；
-固定 RRF 是否需要 calibrated / learned fusion；
- multiview aggregation 是否值得超过简单 best-view baseline；
- AssociativeTopology 的真实增量；
- simple bounded graph expansion、PPR、competitive propagation、Wave 的质量—成本比较；
- Residual weak-cue retrieval；
- EPA / covariance / PCA family 在修正统计定义后是否仍有独立收益；
- reranker 在 latency / cost / quality 上的默认启用条件；
- dense backend / ANN implementation 的工程评测。

这些研究结果只有在稳定、多场景实验显示增益后，才可晋升为 reference profile 默认策略。

# 与 Heptalogos 的后续共同工作

Nous Wave 已确定：

- shared SubjectId；
- cognition / behavior Authority 分离；
- Desired Condition → Pursuit exact revision reference；
- behavior outcome / evidence receipt。

仍需与 Heptalogos 对齐：

- live cognition availability / stale-state degradation contract；
- cross-system revision notification / invalidation mechanics；
- behavior use event 回传的 stable identity；
- purge / permission change 对已投影行为上下文的失效；
- maintenance lease 的产品级 admission 与抢占机制。

Pursuit 自身生命周期继续由 Heptalogos 设计，不在 Nous Wave 建立第二套行为状态机。
