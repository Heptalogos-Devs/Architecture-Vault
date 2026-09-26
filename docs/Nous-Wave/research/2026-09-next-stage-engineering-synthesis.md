# Nous Wave 下一阶段研究综合：从目标设计走向工程计划

日期：2026-09-26

## 1. 结论摘要

Nous Wave 当前不需要再次重写宏观架构。

Architecture-Vault 已经稳定定义：

- Subject Foundation；
- Memory；
- Self；
- Social Cognition；
- Motivation；
- Cognitive Runtime；
- Evidence / Provenance / Time；
- Cognitive Query；
- Serving projections；
- Offline Cognition；
- Nous Wave ↔ Heptalogos Authority boundary；
- TypeScript Host + Rust Kernel 的目标物理边界。

当前真正的工程风险位于 **目标 ontology 与已有代码 ontology 的错位**：

- 代码已有大量 Memory、Runtime、Serving、NousQL、Authority Store 实现；
- 但部分实现基于上一代语义；
- 新 Target Design 尚未下降为完整 Executable Specs；
- 如果继续直接增加 Self / Social / Motivation 或高级 retrieval，会扩大旧语义的沉没成本。

因此下一阶段应先建立一条稳定的 semantic spine：

`Evidence/Time → Memory Authority → Runtime Use → QueryPlan → Serving Generation → Validation/Recovery`

然后再让 Self、Social、Motivation 等新领域接入同一 spine。

---

# 2. 当前代码事实对计划的影响

当前代码已经拥有：

- TypeScript Core 与 Rust Kernel；
- Subject identity / Character Seed lineage；
- Artifact 与 ObservationOccurrence；
- Memory Object / Revision；
- PostgreSQL Authority Store；
- Cognitive Runtime / Session / ResidentSet；
- Cognitive Query；
- NousQL parser/compiler；
- lexical / dense / topology serving；
- independent Serving generation；
- Context / Focus / Projection；
- basic suppression / purge / accessibility；
- model-assisted formation / consolidation。

但至少存在以下已确认的 semantic mismatch：

## 2.1 Memory class 仍为单轴

当前 Rust `MemoryClass`：

- `Specific`
- `Integrative`
- `Procedural`

目标设计要求：

- Cognitive Role：Experiential / Declarative / Procedural Experience；
- Formation Mode：Grounded / Synthesized；

两者正交。

因此这一问题会贯穿：

- Rust domain；
- Protobuf；
- PostgreSQL；
- formation / revision；
- query filter；
- client；
- tests。

## 2.2 Anchor 承担了不应统一的职责

当前 `Anchor / AnchorRevision / AnchorSupport` 是 Authority object。

目标设计已分开：

- CognitiveSchema：Memory Authority；
- AssociativeTopology：rebuildable Serving projection。

现有 Anchor 不能继续作为两者混合的稳定目标模型。

## 2.3 AssociationEvidence 仍压缩成通用数值支持

当前对象仍有：

`support_value: f64`

这会诱导实现把来源、关系类型、证据独立性、极性压缩为一个“强度真值”。

目标方向应保持：

- typed evidence；
- provenance；
- direction；
- polarity；
- validity；
- producer；
- dependency；

服务边权再由 generation builder 计算。

## 2.4 UseEvent 缺少调用方幂等身份

当前 runtime 在收到 use feedback 时内部生成 UUIDv7。

同一调用方事件重试可能形成多条长期 use record。

长期认知使用必须采用：

`caller stable event identity + normalized digest`

形成幂等合同。

## 2.5 Accessibility 当前被固定年龄阈值主导

当前默认：

- 90 days；
- 365 days；

然后映射 NORMAL / DEEP / EXPLICIT。

Target Design 已明确：

- accessibility 是 query-time eligibility；
- 时间只是一个因素；
- 不应把固定年龄阈值提升为认知事实；
- exact access / management / provenance trace 不应被 auto accessibility 吞掉。

## 2.6 Ranking 会受当前候选集合反向影响

当前 ranking 根据“本批候选实际出现了哪些 EvidenceFamily”重新计算融合分母；随后又使用同批相近候选的 topology median 计算额外 innovation。

目标设计要求：

- QueryPlan 在候选产生前固定 lane / budget / fusion；
- 某 lane 没结果就是零贡献；
- 无关候选加入不能改变其他 lane 的定义；
- topology 必须作为普通计划内 lane，而不是计划外隐藏加分。

---

# 3. 外部研究对 Nous Wave 的实际启发

以下研究只作为 evidence / comparative context，不替代项目 Authority。

## 3.1 LongMemEval-V2（2026）

LongMemEval-V2 不再只问“能否从历史里找回一句话”，而是评估：

- static state recall；
- dynamic state tracking；
- workflow knowledge；
- environment gotchas；
- premise awareness。

其意义是：长期记忆系统正在被要求维护 **状态变化、经验性程序知识和前提有效性**。

这直接支持 Nous Wave 把：

- valid time；
- revision；
- procedural experience；
- premise / provenance；

作为一级语义，而不是只优化 embedding recall。

来源：
https://arxiv.org/abs/2605.12493

## 3.2 Memora / FAMA（2026）

Memora 专门评价长时间用户交互中的：

- remembering；
- reasoning；
- recommending；

并引入 Forgetting-Aware Memory Accuracy，惩罚系统继续依赖已经 obsolete / invalidated 的记忆。

其结果指出现有 memory agent 很容易：

- 继续使用失效事实；
- 无法正确 reconcile evolving memories。

这强化了 Nous Wave 中：

- Object / Revision 分离；
- valid-time；
- correction vs world-state change；
- stale serving rejection；

的优先级。

来源：
https://arxiv.org/abs/2604.20006

## 3.3 Mem2ActBench（2026）

该 benchmark 关注“记忆是否真正进入后续行动参数和工具选择”，而不只是被动 QA。

这支持 Nous Wave 的：

`retrieved → presented → referenced → acted_on → outcome`

分层 use semantics。

Retrieved candidate 本身不应自动算作长期 meaningful use。

来源：
https://arxiv.org/abs/2601.19935

## 3.4 Provenance-aware memory（2026）

Agent Zero Memory 强调：

- episodic timeline；
- associative structure；
- semantic curated memory；
- every learned item carries origin/timestamp/evidence pointer；
- reading is evidence-locked。

该工作的具体体系不直接作为 Nous Wave 设计来源，但其结果说明：

> provenance-first memory 并不只是审计负担，它可以直接改善长期检索和回答可靠性。

来源：
https://arxiv.org/abs/2608.29606

## 3.5 W3C PROV

W3C PROV 将：

- Entity；
- Activity；
- Agent；
- Usage；
- Generation；
- Derivation；
- Revision；

作为可组合 provenance primitives。

Nous Wave 不需要实现 PROV-O / RDF，但其概念验证了当前方向：

- 派生对象有独立 identity；
- revision 产生新 entity/version；
- provenance 应保存 derivation path；
- responsibility / producer 与内容 identity 分离。

来源：
https://www.w3.org/TR/prov-primer/

---

# 4. 本轮建议直接收敛的设计问题

## 4.1 Declarative Memory identity

Declarative Memory 的 identity 不由文本相似度决定。

同一个 Memory Object 表示一个持续的 **cognitive matter**：

- aboutness / referent 基本连续；
- claim family 基本连续；
- semantic scope 基本连续；
- 所描述的 world-valid interval 指向同一个认知事项。

### Revision

如果新证据是在纠正、澄清、收窄或重新解释 **同一认知事项**，创建新 revision。

### New object

以下通常形成新对象：

- 新的世界状态发生在不同 valid interval；
- 新的独立事件；
- 从多个对象泛化形成新的综合主张；
- scope 已经改变到不再回答同一认知问题。

例：

- “Bob 2025 年住在 Paris”
- 后来得知“Bob 2025 年其实住在 Lyon”

属于同一 cognitive matter 的 correction revision。

而：

- “Bob 2026 年住在 Berlin”

描述新的 world state，应形成新 cognition 或 temporal successor，而不是把 2025 的认知改写成从未存在。

具体 identity comparator 和 dedup heuristic 留给 Spec。

---

## 4.2 Evidence dependency 与 independent corroboration

Authority 保存 provenance graph，不保存统一的全局 confidence number。

至少能够表达：

- source / observation；
- derived representation；
- cognitive derivation；
- producer / workflow；
- revision dependency。

独立佐证是 provenance graph 上的派生判断。

计划层使用以下语义分类即可：

- SAME_ROOT；
- SHARED_DERIVATION；
- PARTIALLY_SHARED；
- INDEPENDENT；
- UNKNOWN_DEPENDENCY。

`UNKNOWN_DEPENDENCY` 不能默认按独立佐证计票。

不同领域可以根据任务使用不同 aggregation，但必须保留底层 lineage。

---

## 4.3 Self object granularity

Self 不使用一个不断全文重写的巨大 Profile 作为唯一 Authority。

目标上区分：

### Independently revisable Self facets

适合独立 identity / revision 的内容包括：

- identity；
- role；
- capability；
- limitation；
- personality/tendency；
- value；
- long-term preference。

判断是否独立成对象的原则：

> 能否独立变化、独立被质疑、拥有独立证据或独立 scope。

### Narrative identity

叙事身份作为长期叙事结构引用：

- Episodes；
- Memories；
- Self revisions；
- long-term changes。

它组织连续性，不复制引用对象的权威内容。

具体表结构、对象数量和 API 留给 Self Spec。

---

## 4.4 Desired Condition representation

Desired Condition 采用 **bounded typed condition expression**，不发展成通用编程/规则语言。

目标语义：

- typed predicate/evaluator leaf；
- bounded `ALL / ANY / NOT` composition；
- applicability scope；
- temporal form；
- time window；
- observation coverage requirement；
- evaluator version / provenance。

Condition truth 使用：

- SATISFIED；
- VIOLATED；
- UNKNOWN。

Applicability 与 truth 分开表示。

Maintain / Avoid 等开放世界条件必须显式检查 observation coverage；“没看见反例”不能自动成为 SATISFIED。

领域复杂判断通过 versioned evaluator 扩展，不向 condition AST 塞任意脚本。

---

## 4.5 Episode hierarchy 与 overlap

Episode 允许层级组织。

同一个 Observation 可以属于不同 segmentation track，例如：

- interaction；
- task；
- social；
- environment。

不同 track 可以重叠。

在同一个：

`parent episode + segmentation track`

中，sibling Episode 默认形成有序、非重叠分段。

Episode boundary revision 只改变组织，不改写底层 Observation / Memory。

边界算法、阈值和模型属于研究 / Spec。

---

## 4.6 WorkContext checkpoint

WorkContext 是 Cognitive Runtime state，不是长期 Cognition Authority。

只有当上下文需要：

- long pause；
- process restart；
- cross-session resume；

时，才形成 durable checkpoint。

Checkpoint 只保存恢复认知工作所需的最小语义：

- purpose；
- unresolved questions；
- bounded object/revision refs；
- active constraints；
- expected revisions；
- resume conditions；
- budget/accounting summary。

不得把完整 prompt/cache/model hidden state 保存成 Authority。

恢复流程：

`checkpoint + current Authority → rehydrate → revalidate`

---

## 4.7 Attention allocation contract

目标设计只冻结 policy contract，不冻结一个伪精确的全局 score 公式。

多个 WorkContext 的 allocation 至少考虑：

- urgency / deadline；
- current interaction relevance；
- continuity cost；
- risk / importance；
- expected information gain；
- active Desire / Concern；
- starvation / fairness；
- available resource budget。

默认行为语义：

- bounded fair allocation；
- urgency borrowing；
- anti-starvation；
- explicit preemption。

具体 utility function 和参数在 Runtime Spec / experiments 中确定。

---

## 4.8 Social Relation semantics

每种 Relation Type 必须声明自己的语义属性，例如：

- directionality；
- optional symmetry / inverse semantics；
- allowed entity kinds；
- degree semantics；
- temporal semantics。

Degree 不是所有关系共享的 `[0,1]` 数值。

允许的目标语义至少包括：

- NONE；
- ORDINAL；
- BOUNDED_SCALAR；
- TYPED_STATE。

不同 relation type 的 degree 默认没有跨类型算术意义。

Epistemic certainty 与 relation degree 继续独立。

---

## 4.9 LanguageConvention acceptance

LanguageConvention 至少携带：

- social scope；
- optional context/topic scope；
- valid time；
- meaning / referent；
- evidence；
- epistemic state。

证据强度按语义来源区分：

- explicit explanation / confirmation；
- repeated external consistent use；
- successful interpretation + continued external use；
- repair sequence；
- one-shot contextual guess。

单次猜测只形成 hypothesis。

Subject 学会后自己的重复输出不构成新的 independent external evidence。

---

## 4.10 MaintenanceNeed

MaintenanceNeed 不成为新的 cognition domain。

它属于 Runtime / Offline Cognition 的 durable work obligation，用于表达：

- dependency revised；
- contradiction unresolved；
- Journal / Schema needs revalidation；
- DerivedRepresentation stale；
- Serving generation needs rebuild；
- cross-domain proposal needs review。

其 priority 是运行时派生值，不是认知真值。

---

## 4.11 Hypothesis stopping contract

Offline Cognition 每次探索必须有明确 Search/Exploration Envelope：

- total budget；
- source scope；
- counterexample / falsification budget；
- allowed tools/providers；
- expected information value；
- cancel/preemption conditions。

出现以下情况可以停止：

- budget exhausted；
- repeated loop；
- no new independent provenance roots；
- declared counterexample search exhausted；
- expected information gain below policy threshold；
- target owner backpressure；
- foreground preemption；
- permission / purge changes；
- explicit cancellation。

具体 information-gain metric 留给算法研究。

---

# 5. 仍应保持开放的问题

以下问题不应在本轮靠架构讨论伪造答案。

## 5.1 Memory / CognitiveSchema algorithms

- CognitiveSchema 自动形成、拆分、合并和 boundary discovery；
- Declarative object identity 的具体 matcher；
- automatic contradiction discovery；
- consolidation proposal generation。

## 5.2 Runtime algorithms

- accessibility function；
- attention utility function；
- Episode boundary detector；
- MaintenanceNeed priority function；
- information-gain estimator。

## 5.3 Retrieval research

- lexical / dense / entity lane 的 calibrated fusion；
- RRF 是否需要被 learned/calibrated fusion 替代；
- advanced multiview aggregation；
- topology lane 的真实增量；
- PPR / competitive propagation / Wave / simple expansion 比较；
- Residual weak-cue retrieval；
- EPA/PCA family 是否仍有独立价值。

## 5.4 Provider / implementation choices

以下不属于 Target Design OPEN：

- exact SQL schema；
- exact Protobuf shape；
- ANN backend；
- Tantivy 是否继续；
- usearch 是否继续；
- crate/package 物理划分；
-默认参数。

它们在 Plan/Spec/implementation 层处理。

---

# 6. 对下一阶段计划的直接结论

下一阶段应从“领域设计”转向“semantic spine engineering”。

顺序应是：

1. 先关闭目标设计和文档 Authority；
2. 然后写少量纵向 Specs；
3. 先 rebase Memory + Evidence + Runtime Use + Query + Serving；
4. 完成可验证的 Memory Reference Profile；
5. 再实现 Self；
6. 再实现 Social；
7. 再实现 Motivation / Desired Condition；
8. 再做 Offline Cognition 和 Heptalogos live integration；
9. 高级 retrieval 始终保持独立 research lane，只有实验支持时才晋升。

这是为了避免在旧 ontology 上继续扩建，而不是为了做更小的系统。
