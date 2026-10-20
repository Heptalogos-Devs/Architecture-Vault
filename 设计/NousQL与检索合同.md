# NousQL 与检索合同

## 目的与责任

NousQL 直接表达主体的认知查询：自然语言意图、具体身份、时间与历史、来源、返回域、偏好、联想和继续读取共同组成完整能力。原 `master@412b0620` 的正式语言、parser/compiler、实际检索与数值依据见[查询研究](../研究/Nous查询与检索.md)。本规范承接有效旧功能，并明确默认投影和概念投影的修正。

`query.prepare / run / expand / explain` 是唯一公开查询操作组。实现位于 Nous 的 query/retrieval owner，同进程调用 Identity、Material、Memory、Concept、Self、Social、Motivation、Resource 等正式 owner。`contexts`、CLI、MCP、Web 和成长都是消费者；`knowledge` 不再充当跨领域写入及查询中转。

自然语言与结构化查询使用同一编译结果和执行路径。结构化接口不是一套私有增强入口。所有公开 Zod 合同随 OpenAPI/Client 一起生成；当前生产者和消费者在实施时一并迁移。

## 一条文本查询

```nousql
我们上次和 Alice 讨论的那家咖啡店叫什么？
```

未加引号的非空 Unicode 自然语言已经是完整查询。建议在已知信息足够时补出具体人物、对象、事件和时间；不确定的指称继续保留其意图与不确定性。语法岛以外的文本作为原始 intent，普通文字中的 `&&`、`||` 和括号保持文字含义。

```nousql
Alice 提到的咖啡店 @e("Alice") #周末见面 $time(observed,within=30d) $limit(10)
```

保留原三类语法岛及词边界规则，字面符号用 `\@ / \# / \$ / \\` 转义。输入最大 32 KiB、词法 token 最大 2048；超限与语法错误返回可定位的输入错误。实际实施先迁入原 `syntax.ts / parser.ts / compiler.ts` 后改编正式值合同，删除当前分支 `FIND/RETURN/...` DSL 的实现、文档和专属测试。

## 身份、概念与精确读取

| 语法 | 绑定与执行 |
|---|---|
| `@e("Alice")`、`@e("Alice","Bob")` | Entity typed cue；允许1..32个不同人物/实体 |
| `@tag("概念名称或描述")` | 绑定持久 Semantic Concept；按正式 membership 直接召回 |
| `@schema(...)` | 绑定图式，取得直接相关认识 |
| `@r(...)` | 绑定正式 Resource |
| `@object("宿主引用")` | 外部对象typed cue，参数为引号中的opaque ref |
| `@ref(mem:zimug-tikub-lulid)` | 精确对象/修订读取；必须使用真实已返回地址 |
| `#概念词`、`#("较长概念短语")` | 临时语义文本线索，不创建或假定持久概念 |

除 `@e` 外各 selector 接受一个定位参数。名字和 LexicalRef 都经 Identity owner；`@object` 是宿主明确提供的外部引用。名字匹配使用当前/历史正式名称和别名，不从向量分数猜出canonical identity。

绑定失败使用共同Problem，明确区分 `query.unknown_reference / query.ambiguous_reference / query.reference_type_mismatch / query.reference_tombstoned`。歧义结果返回当前可披露的候选名称、类型和LexicalRef，Agent选定真实候选后继续；有权限限制的候选按来源owner规则隐藏。

LexicalRef使用类型前缀与48位标准Proquint三组CVCVC。对象与不可变修订各自可寻址；地址在owner事务内建立，名称变化与概念合并不改变原身份的可追溯性。`result:N` 由消费者当前查询结果目录解析成精确revision，与持久LexicalRef分别保存。

`@ref`闭合该查询的候选集合为所绑定的目标：不做相似搜索、驻留召回、概念丰富或模型重排。可变对象绑定冻结视图中的head，不受 `$history` 展开成多个修订；旧revision使用其不可变地址。精确读取可在检索索引或模型不可用时执行，仍检查projection、时间、来源、权限和生命周期。

## 全部返回域与默认投影

原13域全部保留；本轮新增 `concept` 补齐原Tag引用映射到concept而projection没有该项的缺口。

| 返回域 | 正式owner与内容 |
|---|---|
| `memory` | Memory：具体长期认识与修订 |
| `schema` | CognitiveSchema：模式、适用情境、支持和反例 |
| `episode` | Episode：分轨道、有成员和层级的经历 |
| `journal` | Journal：引用实际经历、保留写作视角的日记 |
| `self_facet` | Self：独立自我事项、范围、立场、例外与领域知识 |
| `narrative_thread` | Self：叙事身份、解释及精确认知来源 |
| `social_relation` | Social：有方向、有情境、带typed degree的关系 |
| `language_convention` | Social：说话者/群体/会话范围内的用语与语用 |
| `desire` | Motivation：愿望 |
| `concern` | Motivation：关切 |
| `desired_condition` | Motivation：带组合条件与时间含义的可评价期望 |
| `evidence` | Material/Source：获准原件、区域、观察和派生表示 |
| `resource` | Resource：稳定外部对象、来源版本及获准操作 |
| `concept` | Concept：稳定概念、定义、别名、修订和成员/lineage |

**省略 `$return`**：使用Memory四域，加上已经供给Self时的Self两域。memory-only主体默认仍为四域。**显式 `$return(cognition)`**：精确表示 `memory,schema,episode,journal` 四域。其余 `$return(...)` 是非空去重域集合，禁止与 `cognition` 混写。

显式请求未供给/进程不支持的领域返回 `query.capability_unavailable`，category为`unavailable`；省略return时按主体实际已供给能力确定默认。领域能力、结果域与检索lane分开建模。`concept`为本轮修正后的合同，原版13域的实现事实保留在研究文档。

公开`QueryDomainSchema`是上表14项的单一Zod enum；文本$return、结构化projection、候选domain、`QueryResult.items/externalResults`及expand均引用它。`cognition`只在输入编译时展开，不成为第15个结果域。每个item的objectRef.kind由对应owner注册，domain不从一个旧KnowledgeKind枚举推导。

投影在索引/直接候选配额前生效，并在融合、owner读取与最终返回继续核验；不能先用无关域占满Top-K再过滤。

## 时间与历史

| 含义 | 查询方式 |
|---|---|
| 来源事件发生 | `$time(occurred,...)` |
| 主体实际接触 | `$time(observed,...)` |
| 内容适用 | `$time(valid,...)` |
| 认知/派生形成 | `$time(formed,...)` |
| 数据正式记录 | `$time(recorded,...)` |
| 数据库在某现实截点的认识 | `$asof("2026-10-20T00:00:00Z")`、`$asof(ago=30d)` |
| 目标主体语义时刻的知情视图 | QueryRequest的`knowledgeAt:TimePoint`，与as-of可同时使用 |
| 旧认知修订作为独立文档 | `$history` |

`knowledgeAt`此次明确保留在完整查询请求/界面时间选择中，文本语法岛继续使用已确定语言；自然语言中的“她当时知道什么”可由消费者在有确定时间时填写该字段。命名与行为统一后再研究是否为其增加专门语法。

`$time`参数保留 `at / from / to / within / domain`。绝对时间必须含时区；point匹配相同instant或包含该点的interval；range为非空半开区间，匹配其中instant或重叠interval。未知时间不满足已知条件。同轴重复拒绝，`at`或`within`不与其他窗口形式混写。不同轴取硬交集，同一返回项须有同一合格来源满足所请求的发生/接触条件。

时间值直接引入共同/时间合同，不重定义clockId版TimePoint。规范输入`knowledgeAt?:TimePoint`和`asRecordedAt?:TimePoint`；后者必须属于保留现实域，$asof编译为它。文本与结构化请求同时给出同一截点时须规范化后相同，冲突即validation。输入时区归一后使用UTC六位微秒，摘要和cursor不经Date。

相对时间在每次新run内部一次`clock.read`得到的`referenceTime:CapturedTime`上解释；recorded轴固定现实域，相对as-of使用同次realAt。普通查询和独立prepare不写Clock capture/checkpoint，也不创造主体observed；真正形成或消费由对应owner取得正式capture receipt。不同时间域须有正式映射；未知映射返回明确不可用，网络deadline、预算窗口和文件时间使用现实时间。

历史读取同时恢复相应截点的head、名称/别名、概念canonicalization、membership、AssociationEvidence和可用表示。当前context中晚于目标截点的anchor退出历史表示与activation，当前问题和purpose保留。当前撤权/传播限制、purge和物理缺失继续即时生效。历史查询只读已有事实，不为填补空白生成新世界事件或认知。prepare和纯历史精确读取不付费；普通语义历史查询可在已允许的embedding能力和预算内，为现有历史材料取得兼容向量并构建对应view，记录实际费用和资产工作。资产缺失时返回具体状态，不借用未来资料。

## 硬约束、偏好与能力

保留 `$source / $exclude(source=...) / $modality / $cognitiveRole / $formationMode / $evidenceClass / $authority / $current` 的原含义。公开值由各领域schema定义：认知角色、形成方式和认识立场分别表达，不压成一个通用type。

`$prefer("文本") / $avoid("文本") / $prefer(recent,axis)` 在硬条件成立后调整排序；默认使用原±.02单项、±.06总额及recent曲线。`$effort(light|normal|deep|maximum)`、`$limit(1..2048)`、`$diagnostics(none|summary|full)`、`$explore`、`$materialize`保留。

`return / asof / history / effort / limit / diagnostics / explore / materialize`为root-only；同指令按原规则判重。结构化接口可表达原QueryExpr的all/any组合，子表达式只能收窄硬范围；顶层域、时间视图、capability和operation预算统一冻结。自然文本中的布尔符号不解释成这棵树。

`textEmbedding / multimodalInterpretation / residualSensing / rerank / queryConceptEnrichment`分别接受`required / preferred / forbidden`。forbidden在调用provider/算法前生效；required无法满足时返回具体原因；preferred失败时给degradation并执行仍然合格的路径。`$explore`表达联想意图，物理profile由Host设置；原residual旗标与实际Pyramid接线的差异在恢复时统一，不保留两个含义。

## 一次完整run

1. 验证可信Actor、Subject、consumer、purpose、audience，解析文本或结构化输入与静态规则。
2. 创建一次内部冻结QueryView：同次Clock读取、两种历史截点、域、SourceRead、各namespace配置revision/definitionRevision、模型/embedding space/producer、context及预算；用一次短的一致读取取得owner可见水位与身份/别名视图，绑定选定截点的真实身份和head。Actor只保存authorityRef等受信身份，权限在实际读取/派发前重新取得；短读取结束后再进入模型/网络工作。
3. 组织同一QueryRepresentation与QueryActivation：intent、选定视图内的实体/概念描述、真实WorkContext/当前材料；可选existing/model概念丰富只使用已供给目录及临时hypothesis。
4. 在域/来源许可范围先生成lexical、dense、TagDirect，以及owner direct/当前runtime lanes；有exploration才运行选定Native/DTSC/V3 profile。
5. 每个family取同一reference最好rank，使用原固定归一化加权RRF；在最终validation budget内按正式owner批量读取，不扫描全部正文。
6. owner检查修订、历史、实际知情、认识范围、可访问性、来源、当前权限、生命周期，返回完整语义单元；再应用软偏好。
7. 可选模型rerank仅取得已许可的候选正文；Resource动作只经资源owner；模型后由同一owner再次核验原冻结条件、实际来源/图支持依赖及当前限制。撤权使旧授权视图计算失效，按新合法范围重算未付费步骤或返回具体状态，既有模型事实与费用保留。
8. 返回带实际身份/修订、自然正文、匹配理由、认识立场、来源与时间的结果；保存有界查询反馈及实际返回成员，供后续UseEvent引用。

精确路径与普通路径共享最终核验。无模型配置的基础词项/精确查询、无Hept的memory-only查询均完整可用。

## 公开操作及返回

| 操作 | 输入与输出责任 |
|---|---|
| `query.prepare` | 同run的公开QueryRequest；只读展示canonical/bound表达、Clock、域、时间、身份、表示、能力和预计预算，不调用模型/embedding、不登记实际使用 |
| `query.run` | `QueryRequest`：`text`或`expression`二选一，可含Session/WorkContext/situation、knowledgeAt/asRecordedAt及capabilities；cursor续页读取原run收据并核验输入摘要，输出`QueryResult`、queryId及精确结果 |
| `query.expand` | queryId+精确返回项/Ref、要读的`content/sources/relations/members/history`、范围与预算；沿原run冻结视图，每项归其owner，当前权限继续重验。无queryId的独立精确展开必须显式给时间视图，省略表示当前只读视图 |
| `query.explain` | 已保存queryId或新QueryRequest；分别给实际执行trace或只读plan，不用一次新模型运行冒充旧解释 |

public prepare是一次独立预览；实际新run读取自己的执行快照。run内部直接持有冻结QueryView，不建立旧Core/Kernel UUID票据往返。查询收据/结果目录记录冻结元数据、已返回固定成员和实际使用事实，供同一run恢复/续页/expand，不承担工作流进度；有付费步骤的执行恢复交给正式平台工作流。cursor续页复用原queryId、视图和已采用配置，不再次运行付费增强；过期/已清除收据返回具体not_found或conflict，客户端明确发起新查询。

`QueryResult`包含`queryId / items / externalResults / status / degradation / diagnostics? / nextCursor?`。两个结果数组均使用上述14域与同一命中外壳；外部资源动作经资源owner返回实际产品对象Ref/OriginIdentity，不伪造外部字符串Ref或第15域。每个item有`domain / objectRef / revisionRef? / lexicalRef? / title? / text / epistemic / sourceRefs / time / matchReasons / readActions`。domain-specific完整对象通过`expand`或owner正式读取得到；统一命中外壳不覆盖其领域内容。

状态区分`complete / partial / degraded`。无命中表示已执行的合格路径没有结果；能力缺失、预算截断、待重建资产和当前限制产生具体状态。结果量小于limit时仍可带nextCursor；分页绑定Subject、authorityRef/consumer、用途/听众、查询、冻结视图与算法配置，不跨查询套用cursor。只有实际可继续的扫描/成员位置才返回cursor；不可恢复的预算截断给partial及原因，不虚构下一页。

## Agent交付与场景

默认展示紧凑自然文本：`[result:1 | mem:真实地址 | 形成时刻] 正文`，随后给必要来源、立场和可执行续读动作。内部UUID、缓存key、数值signature和数据库字段只在机器合同或技术诊断中展开。

保留一个连续场景：同名人物各自说过相似内容，Agent先绑定人物，再按当时知情/记录截点查记忆与日记；选择真实短引用后读来源和概念，后来纠正通过同一对象的新revision出现；再查询历史仍保留旧理解。场景同时覆盖默认Self投影、显式return、concept精确读、来源撤权与多通道解释。算法规则复用原集中golden，语言规则复用原parser的判别输入。
