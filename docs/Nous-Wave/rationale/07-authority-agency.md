# 动机认知与主动行为

## 已确定的设计

Nous Wave 保存主体关于“希望什么、持续关心什么”的认知；Heptalogos 保存主体是否决定投入行为资源、如何行动以及承担了什么约束。

Nous Wave 的 Motivation 使用三类核心对象：愿望（Desire）、关切（Concern）和期望条件（Desired Condition）。Heptalogos 对某项期望条件作出持续追求决定后，建立主动追求状态（Pursuit）。一次具体决策中的 BehaviorIntent、行动计划以及 Commitment/Obligation 分别维护，不与 Pursuit 合并。

## 为什么不继续把 Goal 作为 Nous Wave 的核心术语

“Goal”在认知、代理和工程文献中承担的含义并不统一。有的工作把它理解为期望终态，有的工作只把已经通过可达性和一致性筛选的 desire 称作 goal，还有的 agent architecture 直接把 goal 的采用、执行、暂停和失败全部纳入一个生命周期。

如果 Nous Wave 直接拥有一个长期 `Goal` 对象，后续设计很容易把截止时间、执行进度、计划、暂停、重试和失败都继续塞入同一对象。这样 Motivation 会逐步取得 Heptalogos 的主动行为职责。

Nous Wave 因此只保存期望条件：主体希望什么状态在什么时间语义下成立。是否投入行动资源去追求它，由 Heptalogos 独立决定。

Rao 与 Georgeff 的 BDI 模型把 desire、goal 和 intention 分开；dMARS 的描述进一步把 intention 解释为主体对某个 goal 的行动承诺。Bratman 的规划理论也强调 desire 本身不足以构成 intention，intention 会约束后续行动和手段—目的推理。这些研究支持“期望认知”和“已经决定行动”之间存在实质区别；Nous Wave 与 Heptalogos 的具体分工仍由本项目自己的权威模型决定。

参考：

- Rao, A. S.; Georgeff, M. P. (1995). *BDI Agents: From Theory to Practice*.
- Stanford Encyclopedia of Philosophy, *Intention*, section “Intentions as Plans”.

## 期望条件

愿望可以保持模糊，例如“以后想多旅行”。当主体已经形成足够明确、可以依据证据评价的未来或持续状态时，形成期望条件。

期望条件至少包含三个语义部分：

1. 需要评价的状态条件；
2. 该条件适用的上下文；
3. 条件在时间上的要求。

时间要求使用四种基本形式：

- **达成（Achieve）**：希望条件在给定范围内至少成立一次；
- **终止（Cease）**：希望某个条件在给定范围内停止成立；
- **维持（Maintain）**：希望条件在指定范围内持续成立；
- **避免（Avoid）**：希望条件在指定范围内持续不成立。

这四种形式与 KAOS 等目标建模工作中的时间模式相近。Nous Wave 只借用它们表达时间语义，不采用 KAOS 的完整需求工程方法，也不要求所有期望条件都写成时序逻辑公式。

### 评价与观察覆盖

期望条件的评价需要证据。

“截至 10 月 27 日完成报告”在有可靠完成事实时可以判断已达成；没有看到完成证据，只能表示尚未确认达成。对于“持续保持某状态”和“避免某状态”更要区分事实与观察覆盖：在开放世界中，没有看到反例不能自动证明整个时间范围内从未发生反例。

因此期望条件的满足情况允许保持未知。评价机制需要同时考虑条件内容、时间范围和可用证据的覆盖范围。

### 期望仍被持有与期望是否满足

这两个问题分别记录。

主体可以继续重视一个已经暂时满足的维持条件，也可以撤回一个尚未满足的期望。历史上已经发生的满足、违反或未知评价不会因为主体后来改变想法而被改写。

## Heptalogos 的 Pursuit

Pursuit 表示行为侧已经决定持续投入主动性追求某一项期望条件。它需要引用期望条件的精确修订，而不能只保存一段复制的自然语言摘要。

形成 Pursuit 需要 Heptalogos 自己的行为判断。考虑因素可以包括当前情境、能力、资源、已有承诺、风险、时间压力、规范约束和其他 Pursuit。期望条件存在、重要或即将到期，都只能提供主动性输入，不能自动获得行为权威。

Nous Wave 可以通过上下文贡献、状态变化通知或其他正式合同让 Heptalogos 看到相关期望；具体传输机制不改变所有权。

### 修订与重新核验

Pursuit 绑定期望条件的具体修订。期望条件发生实质修订后，Heptalogos 重新判断当前 Pursuit 是否仍然对应新的期望。不能把已有 Pursuit 的来源引用直接改到新修订，从而掩盖主体曾经追求过不同目标的历史。

如果主体撤回期望，相关 Pursuit 进入重新审查。已经独立形成的外部承诺和义务不会因为认知期望撤回而自动消失。例如主体已经答应另一个人完成某项工作，此时“我现在不想做了”可以改变动机，但不能直接消除已经存在的社会义务。

## Pursuit、BehaviorIntent、ActionPlan 与 Commitment

这四个概念处于不同时间尺度和权威层次。

| 概念 | 主要问题 | 所有者 |
| --- | --- | --- |
| Desired Condition | 主体希望什么状态成立？ | Nous Wave / Motivation |
| Pursuit | 主体是否已经决定持续主动追求它？ | Heptalogos / Agency |
| BehaviorIntent | 当前一次决策准备做什么？ | Heptalogos / Behavior proposal |
| ActionPlan / InteractionPlan | 这次或这一阶段怎样实现？ | Heptalogos |
| Commitment / Obligation | 主体已经承担了什么约束性责任？ | Heptalogos |

一个 Pursuit 可以产生很多次 BehaviorIntent 和多版计划；一个 Commitment 也可能来自外部委托、承诺或规范要求，并不要求存在对应的 Nous Wave 期望条件。

当前 Reaction Spec 中的 BehaviorIntent 只处理当前行为提议，它不承担跨多次 Reaction 的长期主动追求状态。

## 行为结果回到认知

Heptalogos 的行为执行结果不能直接修改 Motivation。它返回可追溯结果和外部事实，Nous Wave 根据这些材料重新评价期望条件或形成修订提案。

一次任务失败通常只说明一种实现尝试失败；它不证明期望条件已经失效。一次局部任务成功也不证明更高层期望已经满足。

这种分工允许下面两种状态同时成立：

- 主体仍然希望 X；
- Heptalogos 当前决定不追求 X。

这对长期主体很重要：资源不足、规范限制或其他承诺可以暂时阻止行动，而不会要求主体伪装成“不再希望”原来的状态。

## 与现有 Heptalogos 行为主干的关系

Heptalogos 已经拥有 CognitiveOpportunity、Reaction、BehaviorIntent、Review、DecisionCommit、CommunicationCommit、ActionPlan 和 EffectOperation 等行为与执行概念。Pursuit 应作为跨多次行为决策的长期主动性状态接入这条主干，而不替代它们。

具体 Pursuit 生命周期、重新审查条件和与 WorkItem/Commitment 的持久化关系属于 Heptalogos 后续设计；Nous Wave 只要求跨系统引用、修订核验和结果回执语义稳定。
