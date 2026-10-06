# 认知图式、关联证据与联想拓扑

## 已确定的设计

三类对象承担不同职责：

- **认知图式**保存主体形成的结构性认知；
- **关联证据**保存有来源、有类型的关联依据；
- **联想拓扑**根据当前有效权威数据构建，是可重建的检索服务视图。

系统不建立一个同时充当长期认知结构和检索中心节点的统一权威对象。

## 统一语义枢纽的问题

一种表面上简洁的方案，是建立一个“语义枢纽”对象：既描述长期主题或结构，又充当检索图中的中心节点，并让支持度随使用不断积累。

这个对象混合了三类性质：

1. 主体认为什么结构存在；
2. 哪些经历和证据支持这个结构；
3. 当前检索算法认为哪个节点更适合作为连接或传播中心。

第三项会随索引、查询分布和算法变化，第一项却属于长期认知。二者共享身份后，检索行为可能反向改变主体认知。

典型反馈回路是：

```text
更容易被召回
→ 更频繁地被呈现或使用
→ 权重继续增加
→ 更容易被召回
```

如果系统把自身检索结果再次当作独立认知证据，这个回路会逐渐变成自我确认。

## 分解后的职责

### 标签

标签是有稳定身份、可修订文本表示的 durable semantic concept，可以表达主题、规则和经验模式。标签身份与显示字符串分离；同名只能帮助寻找候选，不能自动证明两个标签具有同一身份。其 canonical semantic representation、共享向量与 query-local activation 的边界见[时间、概念与查询](11-temporal-concept-query.md)。

### 认知图式

认知图式是主体接受的结构性认知，具有适用范围、支持、反例、边界、修订和生命周期。

### 联想拓扑

联想拓扑属于检索服务。它可以计算中心性、边导通率、过渡概率、枢纽抑制或针对当前查询的激活值，但这些量都不是主体认知真值。

## 关联证据

权威层保存可以解释的关系依据，例如：

- 同一观察上下文中的共现；
- 明确的先后顺序；
- 来源直接声明的关系；
- 多个独立来源的重复支持；
- 有明确语义的使用结果；
- 对认知图式的支持、反例或边界案例；
- 经领域核验接受的结构关系提案。

这些证据不应直接压缩成一个长期累加的通用“关联强度”。不同证据的语义不同，长期累加还会让权重失去可解释来源。

检索服务可以按版本化规则把当前有效关联证据聚合为边导通率。修改聚合函数、枢纽抑制或归一化方式时只需重建服务拓扑，不改写主体认知历史。

## 有限检索资源

联想扩展使用有限预算：

- 出边总量具有固定或归一化预算；
- 高扇出节点受到抑制；
- 跳数、节点数、状态数、执行时间和计算量都有上限；
- 需要统计独立证据时按共同来源祖先去重；
- 被截断或未探索的质量进入诊断；
- 单纯的召回、排序和呈现不生成新的关联证据。

经典扩散激活研究中的竞争和扇出效应为这种约束提供了问题背景，但 Nous Wave 不把具体心理学模型直接当作软件实现规范。

Anderson, J. R. (1983). *A Spreading Activation Theory of Memory*. Journal of Verbal Learning and Verbal Behavior 22(3):261–295. DOI: `10.1016/S0022-5371(83)90201-3`.

## Anchor 职责的归属与吸积

旧 Anchor 将长期概念、认知结构和 retrieval centrality 合并。长期价值由五个职责共同承担：

| 职责 | 所有者或表示 |
| --- | --- |
| stable concept identity | Tag |
| structural cognition | CognitiveSchema |
| typed relation support | AssociationEvidence |
| derived accumulation | Accretion |
| Serving propagation | AssociativeTopology |

Accretion 从当前认知、attachment、provenance roots、Episode recurrence、观察跨度、关系与 meaningful use 汇总概念中心的积累。它帮助安排 review、发现 reuse/merge/split 候选，也可以成为版本化 Serving feature。检索或呈现不增加独立根；反证和来源依赖保留自己的语义。将其设为可重算信号，算法变化便只影响服务与维护，而不改写认知历史。

## 自动维护与关系依据

Tag 的 create/reuse/revise/attach/detach/merge/split 和 AssociationEvidence 的 create/revoke 由维护提案建议，Memory owner 决定提交。后置 attachment 使用显式关系记录，历史 cognition revision 保留形成时的内容。merge/split 保存 lineage 和实际 exact supports；明确 alias 或语义分化可以由一项充分来源支持，不用统一的两独立根门槛代替领域判断。

Episode membership/order、同一次 observation 或显式 support 是结构 owner 已掌握的事实，可以直接形成结构关系依据或 Serving support adjacency。semantic relation 则携带 proposal 与明确 support，由 owner 核验主体、端点、生命周期、relation type、方向、极性、producer 和 provenance。

对所有 cognition 类型递归展开关系证明会把组织事实、语义判断和来源核验混在同一 theorem prover 内，迫使新增 owner 接受无关证明协议。关系自身的 typed validation 与掌握事实的 owner 足以表达当前合同。

## 提案与事务粒度

一次模型反思可以产生多项认知建议。若把它们绑定成一个超级事务，一项非法关系会撤销已成立的独立 Memory 或 Tag，也使崩溃恢复依赖整个 catalog 的持续有效性。逐项 typed owner mutation 让每个领域保持自己的并发、幂等、来源与生命周期语义。

模型输入快照、已取得 proposal 与 workflow outcome 保存一次；每项 action 使用稳定 operation identity，重放由 owner receipt 去重。后项非法保留前项独立提交，依赖失败结果的建议跳过；陈旧 proposal 结束，新的认知变化产生新机会。瞬时 transport/infrastructure 失败继续执行同一 proposal。Tag merge/split、Episode N-to-M partition 等单项领域操作仍以自身事务保持原子。
