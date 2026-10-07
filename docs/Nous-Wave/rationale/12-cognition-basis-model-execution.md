# 认知、形成依据与模型执行

## 认知 Authority 记录什么

如果把 Memory 当作客观事实账本，真实来源上的错误解释就容易被误判为 Authority 损坏，或在纠正后被从历史中抹去。长期主体需要保存的是自己实际形成、保留、关联、修订和使用过的 cognition，包括错误和冲突。身份、来源和演化可以精确，文本解释仍可以错误。

因此 [目标设计](../TARGET_DESIGN.md)把 Subject cognition 的结构 Authority 与 cognitive quality 分开。Owner 保证自己控制的 identity、basis references、permissions、lifecycle、concurrency、idempotency、typed time 与 historical view；领域可以执行自己的接受规则，但不能将通用自然语言蕴含或事实正确性当作所有 owner 的共同证明义务。

Qualification 应继续观察错误之后发生什么：新来源是否改变 cognition、误解是否持续、错误是否传播到 Tag/Schema、current 如何变化、history/as-of 是否忠实。跨 Subject、缺失 basis、错误 immutable identity、future leakage、越权、幂等损坏或 purge bypass 则是必须阻断的结构失败。具体 qualification corpus、runner、分级与付费运行由代码仓库维护。

## 三种关系为何分开

一个来源可以真实存在，也确实被模型读过，但模型把其中日期解释错了。此时 provenance 和 formation basis 都合法，语义解释错误。用一个 support 字段同时表示三件事，会让 owner 无法说明实际保证了什么。

Provenance 保存实际来源、观察、派生与生产者链；formation basis 保存实际形成输入；epistemic judgment 保存“支持、反驳、纠正、削弱”等认识解释。Basis 不自动生成 epistemic support。Episode membership、Journal source membership 和 representation region map 等组织事实仍使用自己的结构关系。

Grounded formation 因而可以包含错误 cognition：它承诺显式 basis 与 preserved provenance，后续 cognition 可以纠正它。不同模型重述同一来源不增加独立来源根；ProducerSignature 解释形成条件，不替代来源独立性。

模型或确定性流程提出的 Tag/Association relation 也有这种区别。Owner 按 typed mutation 合同核验真实输入、身份、主体、生命周期与关系类型，不能因为模型声称支持就把自然语言解释提升成结构事实。认识关系可以被后续质疑或修订。

## 执行方式与认知工作为何独立

将 role 直接绑定到一个 model 会把“做什么”和“怎么调用”混在一起。同一个模型可以承担 formation 与 maintenance，同一资源也可以用不同 reasoning、timeout 或 service preference 执行。同一 role 可以显式配置多个 routes，也可以在一个合法部署中没有可执行 route。

ModelRole 保留语义工作与 Prompt/structured contract；ModelProfile 保留模型资源、协议和能力；ExecutionProfile 保留调用控制。RolePolicy 用有序 routes 和 optional/required 描述可用性，避免以 mini/pro 等营销名称写死认知分工。具体配置字段、SDK/adapter 与依赖版本由代码仓库负责。

## Fallback、重试与生产者

Fallback 只处理显式配置的 execution/infrastructure failure。自动按名称或能力猜测替代模型会绕过部署者的成本、隐私与目的地政策；owner semantic rejection 后静默升级模型又会把领域判断变成未授权的模型循环。新的语义尝试应由 workflow/Host 和预算明确拥有。

Operation 固定 RolePolicy、route 顺序、ExecutionProfiles、ModelProfiles 和生成合同。保存 proposal 后的提交或基础设施重试复用 proposal，避免重复生成改变语义。Fallback 的每个 attempt 保留稳定执行身份，成功 cognition/representation 的 ProducerSignature 指向实际成功执行，而不是只指向最初配置的 primary route。

Attempt、失败分类、fallback transition、successful route、usage 与 latency 由 receipt/telemetry 保留；credentials 和 raw provider bodies 不进入这些元数据。这让 cognition trajectory 的差异能关联到真实执行条件，同时保持 producer 与认知 Authority 的职责分离。
