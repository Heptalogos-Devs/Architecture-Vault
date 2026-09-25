# 认知与主动性

## 问题

持续主体需要同时保存“希望什么”和“已经决定追求什么”。两类状态具有不同后果。

Nous Wave 中的期望条件描述主体希望成立或保持的状态。它可以长期存在，即使主体当前没有采取行动。Heptalogos 需要额外状态表示行为侧已经采纳该期望并持续投入主动性。

## 当前选择

Heptalogos 使用 `Pursuit` 表示持续主动追求。Pursuit 引用一个期望条件的精确修订，并记录行为侧自己的状态和来源。

一次 Reaction 中的 `BehaviorIntent` 继续表示具体行为提议。`ActionPlan` 或 `InteractionPlan` 描述实现方式。`Commitment` 与 `Obligation` 表示已经承担的约束。它们各自承担不同生命周期。

## 设计后果

一个期望条件可以长期存在而没有 Pursuit。Heptalogos 可以采纳、延迟或停止追求某项期望。

期望条件被修订后，既有 Pursuit 需要重新核验引用的语义。重新核验不会改写已经发生的 Commitment、DecisionCommit 和外部效果。

行为结果以证据和回执返回 Nous Wave，由认知系统评价期望是否满足。一次 ActionPlan 成功不等于期望条件已经满足。

## 术语

本设计不使用单一 `Goal` 同时表示愿望、目标状态、主动追求、计划和承诺。跨系统合同使用“期望条件”和“主动追求”两个明确概念。
