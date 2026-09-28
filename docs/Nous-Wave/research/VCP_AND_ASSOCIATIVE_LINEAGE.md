# VCP 与联想检索算法谱系

本文属于 `RESEARCH`，不构成 Target Design、默认算法或认知 Authority。它记录历史能力目标、已观察的数学性质和后续实验边界，避免阶段性实现收敛时丢失原始设计意图。

## 状态标签

- `TARGET`：长期目标设计中保留的能力方向。
- `CURRENT MILESTONE`：当前 Memory Reference Profile 允许验证的有限范围。
- `IMPLEMENTED`：当前代码中已有实现；实现存在不等于已通过系统级 Qualification。
- `EXPERIMENTAL`：可运行的研究或服务实现，不是 production default。
- `RESEARCH OPEN`：尚未由实验或后续 Spec 决定。
- `DEFERRED`：本轮明确不施工。

## Anchor lineage — `RESEARCH OPEN`

早期 Anchor 研究线试图提供一个可以动态积累关联的认知地标，目标能力包括：

- dynamic accretion；
- long-distance association；
- wormhole-like associative jump；
- stable, independently addressable landmark；
- split、merge、weaken、revoke 等结构演化设想。

当前 Target Design 已把其中一部分职责分解到 `Tag`、`AssociationEvidence`、`CognitiveSchema` 和 `AssociativeTopology`。这些对象分别承担语义线索、带来源的关联依据、结构性认知和可重建检索图的职责。

仍然开放的问题是：是否仍需要一个拥有独立 identity、revision 和 lifecycle 的一等 Anchor cognition object。本文不替后续研究回答 Yes/No；本轮不恢复旧 Anchor Authority，也不实现新的 Anchor 对象。

## Algorithm lineage

### EPA / weighted PCA — `CURRENT MILESTONE` / `EXPERIMENTAL`

EPA 的目标是感知 cue embedding space 的结构，作为诊断或候选增强的研究工具。当前实现从 Tag vectors 构建不可变 basis，Serving 只保存可重建投影，EPA 不取得 Authority。

压缩代表向量时，重复计数必须同时进入均值和协方差几何：

```text
mean = sum(w_i * x_i) / sum(w_i)
row_i = sqrt(w_i) * (x_i - mean)
```

已记录的 `240 / 40 / 20` 反例显示，只给均值加权而不给中心化矩阵行加 `sqrt(w_i)` 会改变主方向和能量比例。该结果只证明数学转写问题，不证明 EPA 提升检索质量。修正后仍需在固定语料和查询集上独立评估。

### Residual / Residual Pyramid — `IMPLEMENTED` / `EXPERIMENTAL`

Residual 研究线的目标是在主语义解释后寻找较弱、相对独立的 cue，以避免 dominant direction 淹没弱线索。当前代码保留受控的 residual seam；既有性质试验在相同精确余弦提供器和正交化条件下未发现候选路径、能量或最终残差差异。

真实语料上的召回、精确率、延迟和成本增益仍为 `RESEARCH OPEN`。Residual discovery 在当前 Wave seed policy 中保持默认关闭。

### Wave — `IMPLEMENTED` / `EXPERIMENTAL`

Wave 是当前保留的 bounded associative propagation reference implementation。它使用有界 hop/state budget、typed seed weights、非负普通拓扑边和包含剩余预算的传播状态；contradiction、counterexample 和 negative association 不进入普通 positive adjacency。

这些约束证明实现遵守 reference contract 的局部性质，不证明 Wave 相对 Exact + Entity + Lexical + Dense + Runtime/Temporal baseline 的系统级增量。Wave 只有在 deterministic corpus、oracle、restart/rebuild 和 scale correctness gate 全部通过后才允许进入对照实验。

### River / restart-field lineage — `RESEARCH OPEN` / `DEFERRED`

River、local field、source field 与 restart field 是早期联想传播组合的历史谱系。它们表达局部场、转移后的重启场和来源场等探索目标，不能在当前闭环中与 Wave、Residual 或 reranker 一起打开后再把总收益归因于某一个算法。

本轮只保留 lineage 记录，不将 River/restart-field 加入 production default，也不恢复旧算法组合为永久适配层。后续实验必须拆分机制、固定 corpus/query/filter/budget/provider/final validator，并单独记录 attribution。

## 研究顺序

1. 先完成 Memory Reference Profile 的 Authority、Runtime、Query、Serving、lifecycle 和 recovery correctness。
2. 修正 EPA weighted PCA 的数学转写并运行显式展开样本回归；该回归只证明数学等价性。
3. 在 admission gate PASS 后，比较固定 baseline 与同条件 baseline + Wave。
4. 后续再分别评估 Residual、River/restart-field、PPR 或其他图传播机制。

任何研究结果都必须保留适用条件、资源成本、失败场景和 provenance/Authority 限制，不把局部数学性质写成生产检索收益。
