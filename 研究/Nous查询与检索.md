# Nous 查询、检索与认知关联研究

> 历史源码调查：其中的旧实现方案与施工选择属于当时背景。现行架构见[整体架构](../设计/整体架构与模块合同.md)。


## 结论与范围

NousQL、领域投影和认知检索已经具有相当完整的语义合同。原实现同时包含直接词项/向量召回、持久概念直接召回、原生 Wave、VCP DTSC 和 RiverMemo V3；这些算法共享认知与来源，拥有不同的数学步骤。新 Specs 应先完整承接这些能力，再决定实现与默认策略。

本报告固定读取 Nous 原 `master` 提交 **`412b062082afb75ccfae4c3f69fc606d3e3cc862`**。需求依据为[项目宪纲](../项目宪纲.md)第五编与[目的及能力保全](目的与能力保全.md)。原认知批注、查询/身份/工作上下文和成长图谱已完成调查线索用途，随历史材料归档退出当前目录；本报告自包含记录确认的语言、算法、消费者和源码定位。当前施工采用[NousQL合同](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/NousQL与检索合同.md)与[检索底座](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/检索服务与认知消费者.md)，算法质量、规模与默认选择的未决问题列于末节。

| 层次 | 本轮确认的内容 | 对修正 Specs 的意义 |
|---|---|---|
| 产品与语言合同 | 自然语言一等查询，`@/#/$` 语法岛，全部返回域，历史、来源、继续读取、可选增强 | 按完整语义保存 |
| 已接入算法 | 分通道召回、固定归一化 RRF、偏好、TagDirect、原生 Wave、DTSC/V3 readout | 分别写清输入、公式、参数、消费者 |
| 数学参考 | EPA、残差金字塔、图传播、双场、几何、形态、独立来源及条件创新 | 保留独立可核验合同和少量判别数值 |
| 待改算法与承载 | 无序成员到曲线的映射、部分能力旗标、权限子图重建成本、时间信号接线、跨进程票据承载 | 在实际负责处研究与重组 |

## 一、NousQL：已确定语言

### 自然文本与三类语法岛

一条查询包含必需的非空、未加引号的自然语言意图，以及任意位置的可选语法岛。普通中文、代词、省略句可直接执行；建议把已有把握的人物、事物和时间写清楚。`&&`、`||`、自然文本中的括号保持文本含义。语法岛在词边界识别；`\@`、`\#`、`\$`、`\\` 表示字面符号。解析使用 Chevrotain 的 text/island 双词法模式；长度上限 32 KiB、词法 token 上限 2048。[语言参考][nql-doc]、[解析器][parser]

| 语法 | 实际语义 |
|---|---|
| `@e("Alice")`、`@e("Alice","Bob")` | 绑定真实 Entity，形成 typed cue；最多 32 个不同实体 |
| `@tag("概念名")` | 绑定持久 Tag，直接召回 attachment；名称可指完整描述或规则 |
| `@schema(...)` | 绑定 CognitiveSchema，提供图式线索 |
| `@r(...)` | 绑定 Resource |
| `@object("宿主不透明引用")` | 外部对象线索；参数必须为引号文本 |
| `@ref(mem:zimug-tikub-lulid)` | 精确读取真实返回的 LexicalRef；示例地址须替换为已有地址 |
| `#migration`、`#("复杂概念短语")` | 临时语义文本线索；不解析为持久 Tag，不创建概念 |
| `$...` | 时间、返回域、硬约束、软偏好、努力程度及展开等控制 |

名称解析遇到未知、歧义、类型错配或墓碑，返回相应状态和可选择的候选；调用者选定真实短引用后继续。词项、向量与名称绑定承担各自语义。`@ref` 使该查询的候选集合闭合为精确目标，跳过相似召回、驻留召回、概念丰富和模型重排；即使没有 Serving/模型也应能读。对象地址在当前或 as-of 视图绑定 head；旧修订使用不可变修订地址。投影、时间、生命周期和权限继续约束精确读。[编译与身份绑定][compiler]、[真实 Core 消费者][core-consumer]、[Kernel 精确路径][kernel]

### 全部返回域与控制项

文档约定的默认集合与显式 `$return(cognition)` 是 `memory / schema / episode / journal`。实际Rust `ResultProjection::default`另含`self_facet / narrative_thread`，Core省略projection时会走该默认，形成一处实现/文档差异。新Spec需统一默认集合；全部域与其非空去重组合继续保留：

- `social_relation / language_convention`；
- `desire / concern / desired_condition`；
- `self_facet / narrative_thread`；
- 显式选择的 `evidence / resource`。

这些是 **13 个返回域**。Self、Social 和 Motivation 仍受主体能力供给约束；结果域决定返回什么，物理 lane 决定怎样召回。Tag 是稳定概念与查询线索，原 `$return` 列表没有独立 `tag` 域，但`reference_query_domain(Tag)`返回`concept`，所以query内Tag精确返回的投影存在缺口；正式concept owner读取仍可使用Tag稳定地址。[结果域与控制目录][parser-controls]、[投影编译][compiler]、[实际默认及Tag映射][projection-default]

| 控制 | 原合同 |
|---|---|
| `$time(axis,...)` | occurred、observed、valid、formed、recorded 五轴，可不同轴同时约束 |
| `$asof("带时区时间")`、`$asof(ago=30d)` | 选择 Authority 截点；原 wire 字段为 `asRecordedAt` |
| `$history` | 允许符合截点的旧认知修订作为独立文档；精确对象仍只绑定所选 head |
| `$source(...)`、`$exclude(source=...)` | 来源类别包含/排除 |
| `$modality(...)`、`$cognitiveRole(...)`、`$formationMode(...)`、`$evidenceClass(...)` | 模态与领域含义硬约束 |
| `$authority(...)`、`$current(none|prefer|required)` | 来源权威与 Resource freshness 要求 |
| `$prefer("文字")`、`$avoid("文字")`、`$prefer(recent,recorded)` | 只调整已合格结果的排序；recent 必须给时间轴 |
| `$effort(light|normal|deep|maximum)`、`$limit(1..2048)` | 有界工作量与返回数量 |
| `$explore`、`$materialize` | 显式允许有界联想；请求证据物化 |
| `$diagnostics(none|summary|full)` | 查询解释与实际资源诊断 |

`return / asof / history / effort / limit / diagnostics / explore / materialize` 是原 root-only 控制。同指令重复拒绝，`time` 按轴判重；`prefer/avoid` 可多项。结构化 `QueryExpr` 内仍有查询树执行机械，公开 NousQL 编译只产生一个 atom；研究修正规范时须分别记录这两层。[解析控制][parser-controls]、[编译器][compiler]

### 五轴、知识截点与当前权限

绝对时间须含时区。`at` 是点，匹配相同 instant 或包含该点的 interval；`from/to/within` 是起点包含、终点排除的非空区间，匹配区间中的 instant 或重叠的 interval。未知时间不匹配已知时间条件。同一 scope 的各轴取硬交集，须由同一合格来源满足，避免从不同观察各取一个条件拼接。相对语义时间使用 preparation 捕获的 Subject CognitiveClock；recorded 轴固定 `time:real`，相对 as-of 使用 captured recorded time。[时间编译][compiler-time]、[完整 Agent 手册][nql-agent]

历史查询还约束名字/别名、Tag canonicalization、对象 head、描述、attachment、AssociationEvidence、Entity binding、材料解释与 Serving 资产。WorkContext 中晚于截点的认知 anchor 在 representation/activation 前退出；当前问题和 purpose 保留。当前撤权、purge 和物理缺失始终参与最后读取。新 Specs 需要明确“主体当时知道什么”和“数据库当时记录什么”两种截点的组合，而不是把五轴过滤、as-of 与 history 合并为一个日期参数。[冻结绑定][bind]、[最终再次核验][finalize]

## 二、短引用是身份能力

LexicalRef 由类型前缀加三组 CVCVC Proquint 构成：每组按 `4+2+4+2+4` 位编码，共 48 位，三组从高位到低位。标准辅音表 `bdfghjklmnprstvz`，元音表 `aiou`。例如 `0x0123_4567_89ab → bahog-hijol-mokor`。它不是名称摘要，也不承担权限校验。[编码与标准向量][proquint]

对象与修订有各自地址：例如 `mem / memrev`、`schema / schemarev`、`ep / eprev`、`self / selfrev`、`rel / relrev`；材料区域、表示、人物、Tag、Subject、Session、WorkContext、Resource 同样可寻址。地址在 owner 事务中建立；48 位随机地址最多重试 32 次，数据库唯一约束消解碰撞。`lexical_bindings` 保存 canonical mapping，`lexical_visibility` 保存按 Subject 的可见名称与别名；Tag 合并由 canonical mapping 继续定位。展示读取目录不授予访问权。[类型目录][identity]、[实际分配事务][identity-bind]

会话内 `result:N` 是另一层短指称：保存查询顺序及实际不可变修订，供 `show / trace / use / context pin` 接续。AI 可优先看到正文、短引用、时间与认识立场；完整 canonical ID 和诊断保留在严格接口。[Agent 续读流程][nql-agent]

## 三、实际查询执行链与消费者

实际路径为：

1. CLI、Client、MCP 或认知输入调用 `CognitionService`，读取主体时钟，使用同一 NousQL compiler 和 Identity resolver。
2. Runtime 冻结 Authority/时间视图、当前 Session/WorkContext、SourceRead、配置和预算，生成 QueryRepresentation 与 QueryActivation。
3. Core 按 capability policy 准备可选 embedding、历史 embedding material、概念模型；同一次 query embedding 在 activation、dense、VCP 与叶子间复用。
4. Serving 供应 lexical/dense/TagDirect/选定 topology；领域 owner 供应 Entity、时间、图式等 direct lanes；Runtime 可加入当前合法驻留引用。
5. 按 canonical reference 合并；同 family 只保留最好 rank；投影过滤后按固定 RRF 融合，在 validation budget 内按 owner 批量核验并取得真实正文。
6. Core 可在这些已获准正文上做模型 rerank 和 Resource provider 动作；`finalizeQuery` 重新检查原 BoundQuery、修订 stamp、权限、purge，再输出并记录 QueryFeedback。

这条路径的实际消费者包括 Kernel `query_owners` 中的 Memory、Material、Self、Social、Motivation；Core `QueryOrchestrator` 的 embedding/rerank/resource 阶段；CLI 的查询、准备/检查和 `result:N`；自动认知 projection 与概念维护中的相关检索。相关调用均能追到原 Core 和 Kernel，VCP 不是孤立测试目录。[Core 调用链][orchestrator]、[Kernel 组合][kernel]、[批量最终物化][runtime]

QueryRepresentation 默认 8192 字符、每类最多 16 个上下文条目，组合意图、时间取向、实体/Tag/Schema 描述、当前认识、资源、当前对象、WorkContext 和 consumer/task，输出 digest 与裁剪标记。指称可以利用这些真实上下文，系统没有把任意代词拒之门外。[表示构造][representation]

### 基础召回、融合与偏好

- **词项**：Tantivy 对正文/标题按字段 tokenizer 产生 literal terms，以 Should/OR 召回；使用 BM25 分数排序。原配置 tokenizer 为 `default`，名称字段为 raw。授权与返回域先组成过滤 query，再取 Top-K；自然文本不直接作为 Tantivy 查询语法。[词项执行][lexical]、[字段配置][lexical-schema]
- **向量**：USearch F32，connectivity=16、expansion_add=40、expansion_search=32；按 embedding space 选 metric，结合 RoaringBitmap `filtered_search` 在 Top-K 前筛选。原 open 还把每个向量逐项读入 HashMap，存在索引外的向量内存副本。[ANN 执行][dense]、[打开与内存副本][dense-open]
- **TagDirect**：对激活 Tag 的 attachment 直接召回，同一候选取最大 activation strength；无需先扩散，postings 在没有向量时独立可用。[概念直接通道][concept-activation]
- **概念丰富**：off/existing/model，默认 off。existing 默认 cosine≥0.72、最多 8 个；模型只选冻结目录的 key（目录最多 32），最多 8 个 existing Tag 和 4 个临时 hypothesis，各临时文本≤512字符；不创建 Authority Tag。[参数][concept-config]、[模型合同][concept-model]

固定归一化 RRF 为：

```text
raw(d) = Σ_l w_l / (60 + rank_l(d))
score(d) = raw(d) / Σ_enabled_l w_l / 61
```

分母由冻结计划的 enabled families 决定。默认权重 exact=4、runtime=2、entity=2.5、lexical=dense=schema_direct=tag_direct=1.5、temporal=topology=1；一个 family 的多个变体不重复加分。等分按最好 lane rank、exact、稳定引用排序。[RRF 实现][rrf]、[参考参数][rrf-config]

原查询默认 limit=12。各 effort 的每 lane 预算为 `clamp(limit×[2,4,8,16],16,[128,512,2048,8192])`；最终核验预算为 `clamp(limit×4,32,4096)`；topology hops 为 1/2/3/4，states 为 128/512/2048/4096。预算截断返回 Partial 及具体诊断。[预算计划][plan]、[默认参数][rrf-config]

软偏好在 owner 读取后计算，默认每项±0.02、总和夹在±0.06。文本偏好是小写 whitespace term 的包含比例；recent 使用 `1/(1+age_seconds/2592000)`，先按所属时间域取合格时间。它与可访问性、VCP 时间后处理、硬时间条件分别计算。[偏好算法][preferences]

## 四、原生 Wave：证据图与有界传播

原生 `nous-node-potential-v1` 的领域图节点可包含认知、人物、Tag 和材料；边保留支持来源、basis class、relation、polarity、root。负证据不产生正流。对同 `(from,to,provenance_root)` 取最大 `class_quality×support_mass`，不同根求和，形成 raw support。[图构建][graph]

目标 inflow 参与 hub 校正：`penalty=clamp((inflow/median_positive_inflow)^-0.35,0.35,1.25)`；每节点保留最多 32 个邻居，按行归一到 outbound budget=0.9。默认 class quality：host_explicit=1、source_evidence=.9、cognitive_derivation=.75、derived_structure=.65、meaningful_use=.5。[Wave 参数][wave-config]

传播状态是 `(previous,current,hop,remaining_budget_steps,energy,origins)`。默认 hop≤4、states≤4096、minimum energy=.0001、初始步数4、每普通边耗1；立即回流乘.2。到同状态的路径合并 energy，并保留全部 source origins；FIR 权重按 `.55^hop` 归一。状态裁剪累计 discarded mass，输出 node potential、edge flow、first hop、来源与 complete。实际 topology lane 按 node potential 排序；无可映射显式 anchor 时，可从既有 lexical/dense 各提升最多4个弱 seed，权重 `.6/rank`。[传播核][wave]、[实际 lane][native-lane]

原生 EPA 是另一条训练合同：归一化向量、重复向量密度计数、最多256个代表点、加权均值与 `sqrt(weight)×centered_vector` 的 SVD，保留 energy≥.01、最多64轴；原生 residual pyramid 对每层 ANN 候选正交化，剔除共线方向后投影，产生残差与解释量。它们与下节 VCP reference 在采样、浮点、分层诊断上有明确差别。逐仓核查显示，这两个Native函数当前仅有自身/测试调用；生产`QueryObservation::native`直接执行propagate，实际已接入EPA/Pyramid的是VCP reference pipeline。它们作为可复用数学研究单元保留，尚无Native生产消费者。[原生 EPA][native-epa]、[原生 residual][native-residual]

## 五、VCP：一个查询观测，两类候选读出

### 实际接线与资产

原 registry 有四个 profile：`baseline-rrf`、默认 `nous-node-potential-v1`、`vcp-dtsc-v9.2.1-adapter-v1`、`vcp-rivermemo-v3.1-adapter-v1`。是否允许联想由 `$explore` 等 exploration intent 决定；物理 profile 和数值政策由可信 Host 配置。两个 VCP profile 已由 `ServingService.vcp_lane` 接入普通查询。[profile 注册][profiles]、[Serving 分派][query-serving]、[VCP 实际 lane][vcp-lane]

VCP generation 保存同一 Authority 水位、embedding space/producer、身份映射、向量、Tag labels、候选曲线及顺序来源、根谱系、pairwise、intrinsic residual/anchor、EPA 与 CSR transport。查询时核对 profile/policy/space/producer，复用共享 query embedding，再建立一个不可变 `VcpQueryObservation`。后续 DTSC/V3 不重复 embedding，不在候选 readout 中重新运行 ANN sensing。[generation][vcp-generation]、[观测准备][vcp-observation]、[统一 pipeline][pipeline]

### 共享数值步骤与默认参数

| 步骤 | 具体合同与计算 |
|---|---|
| EPA 训练 | 归一化 Tag vectors；12-bit xorshift density bucket；bucket score=`density^.65×residual^.35`，以 `exp(-3×max_sim²)` 抑制重复方向；默认64 anchors、32 samples/anchor、512 candidates、最多64 basis。SVD 行为 `sqrt(density)×(centroid-weighted_mean)`；在保留轴范围累计能量>95%时停止，最少8轴（受现有轴数限制）。采样代表数是诊断，SVD 行使用选中 centroid。 |
| EPA 查询 | f32 `q-mean`；各轴投影平方归一得 p；归一化 Shannon entropy H，logic_depth=`1-H`。dominant p>.05；首轴与其他轴的 `sqrt(p0·pi)>.15` 累加为 resonance。查询计算不读取训练 cached energies。 |
| 残差金字塔 | 默认最多3层、每层ANN取10 Tag；依返回序 Gram–Schmidt，相关轴贡献为0；f32投影累加，残差解释能量统一除原查询能量；剩余比例<.1停止。输出 coverage、coherence、novelty、activation。 |
| intrinsic residual | 离线从共同文档邻居构建局部子空间；默认 anchored_gs，最多48邻居/4轴、最少3邻居，按残差增益×新方向长度×log(1+cooccur weight)×semantic gate 贪心选轴，gain<.015停；另有 centroid/SVD。`anchor_gain=clamp(.75+1.25×residual_ratio, .5,2)`。 |
| 图构建 | 有序文档2..100 Tag产生全 pair；位置权重与距离衰减(.08)、forward=1/reverse=.35、语义峰值.65/σ=.25、reverse anchor boost 参与 fact mass；无序 membership 使用双向 `.49×semantic`。再 `log(1+mass)` 压缩、hub exponent=.3，outbound=.95，其中 wormhole reserve=.05。 |
| gating | 结合 logic_depth、entropy、resonance、Pyramid activation/coverage、core 与语言启发；层衰减.7，base boost=.6，动态 boost夹.3..2，core boost1.2..1.4；Unknown/cross-domain 技术词默认乘.05/.2。 |
| Sense | `(previous,node)` 状态带 energy/momentum；默认4 hops、2000 states（实际还受 effort budget限制）、每点20邻居；base momentum=2、firing=.1、普通边decay=.25、wormhole=.7、立即回流=.15、minimum current=.01、FIR gamma=.6。记录 edge flow 先于 momentum/state admission；最终 retained FIR node 分布归一后作为 source field。 |
| fusion | seed取已有门控权重与node energy最大值，截断 emergent、补core；近重复向量越过阈值后给保留项转入20%被合并权重；context均值归一，与原q按effective boost混合并归一。生产 adapter 当前 ghosts 为空。 |
| 双场 | 同一 source 与 transport，分别迭代 `f_next=(1-alpha)·source+alpha·Tᵀf`；local alpha=.15、transfer=.55，最多80轮，独立L1容差1e-9；按累计质量.8/.9取支持域，再投影回可用 Tag vectors。 |

源码：[EPA 训练][epa-train]及[SVD][epa-basis]、[EPA 查询][epa-analysis]、[Pyramid][pyramid]、[intrinsic][intrinsic]、[图 fact][vcp-graph]及[transport][vcp-transport]、[gating][gating]、[Sense][sense]、[fusion][fusion]、[双场][dual-fields]。这些数值是 Nous 固定提交的 typed defaults；外部 VCP 的 Rust fallback、`rag_params` 和实际 effective config 分别记录。

### DTSC 候选读出

DTSC 把候选的有序 Tag curve 投向查询能量场；exact contact 与 semantic interpolation 分开。默认 field 最少3 Tag、entropy≥.12、保留95%质量且最多48 field nodes；semantic contact cosine≥.5、核指数2、最多4邻居，public hub floor=.35。曲线 strong/weak contact=.16/.06、position decay=.035、正文 closure阈值.2。[场构建][dtsc-field]、[参数][dtsc-config]

候选测量包括 contact coverage、平均/最高 potential、相邻 Tag 球面弧长、transport方向、continuity、action quality、isolated ratio 和正文 closure。核心计算：

```text
confidence = coverage × (.55 + .45×evidence) × (1-.65×isolated_ratio)
geo_score = confidence × (.30×mean_potential + .20×max_potential
                         + .20×continuity + .15×action + .15×closure)
normalized_geo = clamp((geo_score-.015)/(.25-.015),0,1)
bonus = min(.35×qualified_confidence×qualified_strength, class_cap)
score = original_knn_score + bonus
```

direct/structural/thematic cap 分别为 .18/.10/.035；稀疏独立 contact 可缓解孤立惩罚，auxiliary/identity floors 默认关闭。场不可信、曲线无接触或低覆盖且无区分度时，归零所有 geometry bonus 并保留原输入顺序，返回明确 fallback reason。[曲线核][dtsc-curve]、[batch 信任与 fallback][dtsc]

### RiverMemo V3 候选读出

1. **候选池**：original query、denoised、local、transfer 四向量通道，各默认100；BM25/anchor各50，time沿query quota，union最多300。通道内 min-max/reciprocal rank归一，再结合max、mean、RRF及多源支持形成union score；先按命中通道数排序。生产候选供给还合入 lexical/dense 和 exact refs，BM25使用 `1/rank` proxy，time_score固定0。[pool][pool]、[真实供给][vcp-offers]
2. **query形态**：只看同一个 river 的hop、energy、edge flow，计算depth/spread、HHI concentration、shallow ratio、forward/same-level、chain/branch/merge、growth persistence。三个固定logit经稳定softmax得到atomic/propositional/narrative，随样本量与complete confidence向1/3 prior收缩；不读取候选或查询正文。[形态][shape]
3. **Ω门控**：edge数量、emergent/seed比例、正raw-flow熵三个[0,1]分量取epsilon-floor(.02)几何平均；incomplete乘.5；collapsed/sparse阈值.12/.45。[Ω][omega]
4. **路径与相对拓扑**：双场 potential、支持域和边方向构成path quality；query节点与候选Tag做exact或cosine≥.48对应，比较hop相对距离与候选位置差（temperature=.35），反向credit=.25；独立来源比例最低.15。只有node对应时reliability cap=.2。当前motif_score直接等于edge_topology_score。[路径几何][path]、[相对拓扑][relative-topology]
5. **直接anchor**：真实hop-0 core/seed exact或cosine≥.8接触，semantic discount=.7；mass、inbound specificity、正文closure、池内rarity通过noisy-OR合成。无明确直接来源时走fallback并把reliability封顶.5。[anchor][anchors]
6. **语义与结构基础分**：original/local/transfer cosine按 .25/.20/.15 归一加权，加最多.08的有界path reward。形态三权重分别使node/edge graph score混合，atomic的node份额.75，propositional=.25，narrative=.15。[基础分与可观察量][pure]
7. **条件创新**：以pure score、closure、direct evidence三维Gaussian找peer（bandwidth=.04/.10/.12）；异role权重.35，最少3 peers，ESS门槛2.5。`innovation=max(graph_score-E_peer[graph]-z×sqrt(var×(1+1/max(ESS,1))),0)`，z=1；乘候选置信、ESS置信、scale=.5和role multiplier，再取role cap与全局.08。direct/structural/thematic cap=.02/.045/.008，非direct通常不能越过direct frontier。[创新读出][innovation]
8. **最后分数**：`clamp(pure_score + bounded_innovation×Ω^gamma + anchor_bonus,0,1)`；gamma=1，anchor bonus最多.1，按batch均值+2σ及最小.05启动。V3将这些作为一个TopologyWave lane的rank返回，外层继续使用冻结RRF及领域最终核验。[readout组合][readout]、[lane输出][vcp-lane]

## 六、概念、关联、吸积和可访问性

### 概念及正式关系

Tag具有稳定ID、独立不可变revision、label/description/kind_hint、名称别名与来源。合并检查survivor和1..7个retired的expected revision，并在同事务更新canonical指向、lineage及别名；历史视图保留合并前映射。拆分创建2..8个child并保存lineage，原操作不自动把全部旧attachment分配给新child；附着和后续维护另有正式动作。[Tag事务][concept-transaction]

AssociationEvidence保留typed endpoints、relation、polarity、valid time、basis class、producer和实际basis。HostExplicit、SourceEvidence、CognitiveDerivation、DerivedStructure、MeaningfulUse分别校验；正meaningful-use支持只接受referenced/acted_on/result_supported/corrected/pinned，result_refuted只支持负关系，presented不能充当正支持。[关系依据规则][association]

### 吸积是可重建信号

`accretion_signal`按中心Tag/Schema/精确Memory取得当前合格成员，默认最多32。它测量独立已知根数、当前认知成员、跨Episode复现、observed跨度、关系degree/diversity、有意义使用、反例及语义coherence；coherence当前是“第一个成员与其余成员”的cached semantic均值。`broad_center`来自degree/成员数>32或coherence<.35；复现≥3或已有meaningful use影响review priority。实际消费者是概念维护plan的来源目录与reviewPriority，最终修改仍经领域owner采用。[吸积实现][accretion]、[实际消费者][accretion-consumer]

### 可访问性的实际公式

```text
A = ln(.02 + 1×(1+formation_age_days/30)^(-.5)
           + Σ_event weight(kind)×(1+event_age_days/30)^(-.5))
```

权重：referenced=1、acted_on=1.4、result_supported=1.1、result_refuted=1.2、corrected=1.5、pinned=2、presented=0。A≥-.8为Normal；-.8>A≥-1.6为Deep；更低为Explicit。Normal供普通召回，Deep要求deep/maximum，Explicit需精确提示；exact读取越过可访问性门槛，继续执行权限与生命周期。旧实现的时间输入来自记录时刻/UseEvent occurred_at及historical as-of；主体语义时钟如何统一参与老化，是新的时间Spec需要明确的一点。[公式与门槛][accessibility]、[参数][accessibility-config]

这是一项幂律随时间衰减的可想起程度。反驳和纠正能提高可访问性，认知可信与否由证据和修订决定。它应与展示频率、支持强度、管理抑制及彻底清除分别建模。

## 七、数值依据与真正的算法缺口

旧研究冻结 VCPToolBox **`e03b891d42055cdf3cab5dc961cc71dd5facd65a`**，manifest记录原文件blob与probe来源。原master有24份集中数值JSON，覆盖EPA/training、intrinsic、graph、Sense、pyramid、gating/fusion、双场、projection、DTSC/V3及组合pipeline；测试比较中间数值，部分标量abs/rel=1e-10/1e-12，f32向量与SVD有独立容差。旧记录的23项测试通过属于当时结果，本轮核实源码和固定fixture，没有重新跑该Rust测试。[来源manifest][upstream-manifest]、[数值目录][goldens]、[实际断言][golden-test]

固定提交显示以下具体问题：

| 问题 | 实现事实与下一研究动作 |
|---|---|
| 有序曲线的来源 | adapter明确区分SourceSequence与StableIdentity；生产`vcp/material.rs`当前全部给StableIdentity；无序membership在建图时position=0，在candidate curve却按稳定ID给1..N。DTSC/path/relative topology仍读取这个顺序。需比较真实来源顺序、无序readout和稳定控制顺序，确定何种关系拥有叙事方向。 |
| 共享原根与流量 | Native按边/root取max；VCP文档facts会累加，同时provenance按root取max。V3会按候选自身根分摊self/other并保留.15 floor。重复摘要增加transport与增加独立证据的作用需分别验证。 |
| 权限过滤成本 | SourceRead限制会调用VCP `authorized`，从允许文档重建generation、intrinsic、EPA及candidate/tag两份ANN。语义上排除了越权影响，代价覆盖整个授权子集；应测量后确定可复用资产和有界查询子图边界。 |
| 能力旗标与实际步骤 | Runtime closure把required residual_sensing直接判未实现；VCP pipeline实际运行Pyramid。需要明确该能力旗标约束的步骤，并统一required/forbidden行为。 |
| 时间增强 | VCP offers的time_score=0；外部插件TimeDecay是另一个按文本/路径日期的乘法后处理。Nous五轴和recent有自己的owner。时间研究应分别测量，不能只保留字段名。 |
| 形态、motif与启发参数 | morphology为固定经验logit；motif复用edge score；语言gate根据字符串启发识别技术/社会world；这些都有具体计算，默认收益尚需真实任务对照。 |
| 浮点与ANN条件 | reference Pyramid依赖ANN返回序；EPA与intrinsic用f32及SVD，等权tie存在原HashMap顺序边界。当前fixture冻结条件序列；真实ANN召回、并发、长期收益另需观测。 |

来源：[曲线顺序映射][vcp-order]、[VCP根与facts][vcp-roots]、[受限资产重建][vcp-authorized]、[residual旗标][residual-gap]、[实际time供给][vcp-offers]、[旧数值研究记录][conformance]。旧研究文档包含多个阶段的进展描述；本报告的接入状态以固定提交的实际调用为准。

原仓库LICENSE及源码SPDX为Apache-2.0；旧conformance文字中“Nous为MIT”的表述已经与该提交不一致。外部manifest登记VCP为CC-BY-NC-SA-4.0；原reference目录描述为独立数学实现。未来源码采用继续按具体来源与版本记录。[原LICENSE][license]、[外部来源记录][upstream-manifest]

## 八、基础设施要求与可替换的承载

| 责任 | 必需的能力 | 原承载与可研究的简化位置 |
|---|---|---|
| 权威与历史 | 稳定对象/修订、名称与关系历史、来源DAG、时间域、当前撤权/清除、同事务变更 | PostgreSQL与各语义owner；存储机械可复用成熟库 |
| Serving | lexical、ANN、concept postings、图/向量资产，空间/producer/policy签名，水位、历史视图及重建 | Tantivy/USearch/Roaring、不可变generation、发布/回收；具体引擎可换，读取语义需保留 |
| 数值 | SVD/稀疏矩阵、正交投影、有限步传播、双resolvent、几何与conditional统计 | nalgebra等成熟线代库承担机械，认知算法参数与步骤由retrieval owner承担 |
| 查询生命周期 | 同一次冻结输入、一次query embedding、可选增强预算、模型后当前权限再次核验、实际使用反馈 | 原Core/Kernel跨进程prepare/activate/query/finalize票据、进程Map、slot/lease；进程内组合可改为直接持有同一查询对象 |
| 模型执行 | capability required/preferred/forbidden、producer/space兼容、费用、trace、外部调用结果与恢复 | 采用成熟SDK与工作流执行，语义owner继续决定可读输入及正式采用 |
| 当前认知 | WorkContext、resident与situation、不同consumer/用途/听众、紧凑投影与原生历史更新 | 属于持续主体的真实能力；运行承载重组时继续有明确owner |

原`QueryPlan/BoundQuery/QueryActivation/QueryObservation`大部分表达真实的冻结语义与算法输入。可替换的是它们跨进程保存、传输和调度的具体机械；研究应把这部分与认知运行时的上下文、历史和反馈功能分别定位。可用同一条真实查询验证新边界：私密材料合法进入候选，模型重排期间上游收紧授权，最终输出及时移除相应候选。[原ticket/lease承载][lease]、[最终核验][finalize]、[资产生命周期][lifecycle]

## 九、源码复用、库边界与基础设置施工

### 可直接复制后改编的源码

实现阶段先迁入原函数及集中数值输入/expected，再替换其身份、存储、错误和调用边界。以下文件拥有可识别的实际算法；语言变化也应保持其中的领域步骤。

| 迁入单元 | 原文件与入口 | 改编责任 |
|---|---|---|
| 语言与短引用 | `apps/nous-core/src/nousql/{syntax,parser,compiler}.ts`的`parse / canonical / compileNousQL`；`persistence/src/proquint.rs`与`identity.rs` | 保留语法岛、全部域和时间/精确含义；compiler对接新正式合同，名称由Identity owner绑定；Proquint可采用库实现同一编码 |
| 基础融合与偏好 | `runtime/src/query/ranking.rs::rank_candidates_with_policy`、`preferences.rs::{score,apply}` | 提取归一化RRF、固定分母和软偏好计算；不迁入整个旧Runtime才能使用这些函数 |
| 原生检索数学与研究单元 | `retrieval/src/mechanisms/{cue_sensing,residual,graph,wave}.rs`；`topology_lane.rs` | 其中graph/wave/topology_lane有生产消费者；cue_sensing/residual为已实现的研究单元。分别保留代表点/加权PCA、分层正交化和实际状态传播/readout，不把二者接线状态混写 |
| VCP共享数学 | `retrieval/src/reference/{epa_training,intrinsic,graph,pyramid,gating,sense,fusion,fields,pipeline}.rs` | 函数`reference_train_epa / reference_intrinsic_residual / reference_graph_from_facts / reference_pyramid / reference_gate_tags / reference_sense / reference_fuse_observation / reference_dual_fields / reference_query_pipeline`直接按原组合关系迁入 |
| 两种VCP读出 | `reference/dtsc/{field,curve,config,mod}.rs`的`reference_dtsc`；`reference/{pool,geometry,topology,query_shape,anchors,observables,scoring,readout}.rs`的`reference_v3_readout` | 保留DTSC场信任/fallback、V3候选池、形态/Ω、相对拓扑、anchor与条件创新；分别对外提供lane rank及解释 |
| Authority适配 | `retrieval/src/vcp/{adapter,material,generation,index,graph,observation,readout,lane}.rs` | 保留identity/space/producer/root/curve-order映射和实际消费者；移除其对旧服务进程与不再采用存储协议的依赖 |
| 概念与使用规则 | `memory/src/service/{tag,topology,accretion,accessibility}.rs`；`concept_maintenance/plan.rs` | 保留expected revision、canonical merge/lineage、typed basis、独立根信号、幂律可访问性和维护目录；事务交给最终Authority owner |

对应算法及函数链接均在前文。原Rust数值模块已经依赖nalgebra和明确值结构。本轮选定以napi-rs同进程addon迁入，先复制、建立真实调用并迁移consumer，再讨论算法变动；文档FTS/持久dense采用LanceDB，旧Tantivy同义文档服务退出。

### 成熟库的实际API与替代范围

2026-10-20核对了当前安装的`ml-matrix 6.15.0`、`graphology 0.26.0`、`@lancedb/lancedb 0.40.0`声明，并查阅其官方接口。原Rust实现的nalgebra、Tantivy、USearch、Roaring调用直接可见于固定源码。

| 机械 | 可实际调用的接口 | 仍由算法/领域owner承担 |
|---|---|---|
| 保留Rust线代 | `DMatrix::from_row_slice(rows,dim,&values).svd(false,true)`；结果`v_t / singular_values` | EPA采样、density权重、中心化、轴能量阈值，以及f32计算位置 |
| 未采用的Node线代候选 | `new Matrix(rows)`；`new SingularValueDecomposition(A,{autoTranspose:true,computeLeftSingularVectors:false,computeRightSingularVectors:true})`；读取`rightSingularVectors / diagonal` | 该库API有效；本轮保留原nalgebra，不增加一次数值重写。[官方源码](https://github.com/mljs/matrix/blob/v6.15.0/src/dc/svd.js) |
| 未采用的Node邻接候选 | `new MultiDirectedGraph()`、`addNode`、`addDirectedEdgeWithKey`、`forEachOutboundEdge(node,callback)` | 本轮沿用原CSR/邻接数组；root去重、边类别质量、momentum、FIR、回流抑制和状态预算留原函数。[官方迭代API](https://graphology.github.io/iteration.html) |
| 原向量/词项索引 | USearch `Index::new / reserve / add / save / load / filtered_search`；Tantivy `TermQuery / BooleanQuery / ConstScoreQuery / TopDocs`；Roaring `contains` | embedding space、来源与域过滤、历史view、概念postings、各lane语义；这些库已被原代码实际采用 |
| 采用的文档索引 | Lance `connect / createTable / openTable`、`table.createIndex('text',{config:Index.fts({baseTokenizer:'icu',...})})`、`Index.ivfFlat`、`query().nearestTo(vector).where(predicate).limit(k).toArray()`；`mergeInsert(key).whenMatchedUpdateAll().whenNotMatchedInsertAll()` | 0.40的向量`.where`默认预过滤，`.postfilter()`显式后过滤；保持原授权/投影先于候选配额。内部VCP Tag/candidate USearch有不同消费者，继续保留。[VectorQuery API](https://lancedb.github.io/lancedb/js/classes/VectorQuery/)、[Index API](https://lancedb.github.io/lancedb/js/classes/Index/) |
| 两路hybrid机械 | Lance `rerankers.RRFReranker.create(60)`及`rerankHybrid(query,vecResults,ftsResults)` | 它处理vector/FTS两路，原查询还含Exact/Runtime/Entity/Temporal/Schema/Tag/Topology及不同权重，继续使用原统一融合函数。[官方RRF API](https://lancedb.github.io/lancedb/js/namespaces/rerankers/classes/RRFReranker/) |
| 解析执行 | Chevrotain `createToken / Lexer(modes) / EmbeddedActionsParser / RULE / ACTION` | `@/#/$`词法边界、selector arity、指令判重、projection、时间与Identity绑定；优先迁入已存在的三文件 |

### 可删的具体Runtime机械

原跨进程Core/Kernel query workflow把一次冻结查询切成prepare、activate、query、finalize RPC；`prepared.rs`用UUID、`QueryReservation`、进程内Map、bounded slots、`QueryLease`、take/release/expire保存跨RPC状态。若最终采用单进程组合，这套“保管并找回查询对象”的承载可以由直接持有的请求对象及成熟调用/执行框架替代。一次冻结视图、budget、取消、实际资产读取生命周期和模型后重验继续保留在调用者可依赖的查询操作里。[旧保管机械][lease]、[重验意义][finalize]

同样可替换的是Core/Kernel间的protobuf重复DTO转换、`kernel-client`式转发和为了远程分阶段执行建立的对应endpoint；是否存在真实进程边界是删除条件。`BoundQuery`中的Subject/时间/配置/授权字段、`QueryActivation`的共享embedding、lane rank合同、WorkContext/Resident、使用反馈和SourceRead各有实际消费者。它们应归入最终责任结构。结构化`QueryExpr`的all/any树也是原公开typed API的一部分，保留语义后再评估其必要性。

### 先完成设置、Serving底座及原消费者

1. **基础设置与执行资源**：明确进程支持与主体供给；提供identity/时间映射、SourceRead与受众、模型/embedding/rerank/concept角色、API凭据和费用/trace。配置先覆盖旧profile、capability policy、effort预算、VCP assets/query/readout参数；标出哪些实时生效、哪些需要重建。冻结查询记录实际有效配置与资源签名。
2. **统一权威读取**：正式owner提供按Subject的批量当前/历史对象、精确revision、Tag canonicalization、attachment、AssociationEvidence、来源根及授权视图。SourceRead、purge、名称历史和两种时间截点在这里落实，索引不另建权威。
3. **Serving资产底座**：按明确family管理lexical、dense、concept postings、native/VCP graph；确定embedding space/producer、历史revision文档、watermark/增量变更、构建/发布/readback/回收、原件与向量资产的真实路径和占用。先让原算法取得同一代、可追溯、可授权的输入。
4. **贯通原完整查询**：迁入原NousQL三文件、LexicalRef、QueryRepresentation、直接lanes、RRF/偏好、owner批量物化与最终重验；启用`query.prepare/run/expand/explain`、自然查询、exact续读、`$return/$asof/$history`以及实际结果反馈。
5. **原算法接入消费者**：依profile把原Native Wave、DTSC和RiverMemo接到同一个公开query操作；同一query的embedding、概念资产和observation复用。保持其intermediate measurements与解释字段，待真实场景暴露问题后，在负责函数中改进。
6. **把查询用于主体和成长**：自动projection按consumer/用途/受众取得当前Self、Social、Motivation和相关记忆；WorkContext与原生历史按各自owner更新；概念维护读取真实QueryFeedback/UseEvent/accretion目录，写入后重新进入Serving和下一次真实查询。

| 真实消费者 | 需要交付的调用与反馈 |
|---|---|
| CLI、MCP、普通Client | 自然NousQL、prepare/run/expand/explain、全域投影、短引用/result:N、exact read/trace/use、历史与错误恢复 |
| 深度认知接入 | 每次真实模型调用的当前projection与可继续检索；消费当前身份、认识程度、关系和语言惯例；返回实际presented/cited/adopted/outcome等事实 |
| 成长/概念维护 | 精确旧revision与来源目录、相关跨域检索、一跳正式关系、QueryFeedback/UseEvent和accretion，采用后索引可用 |
| 产品管理与研究 | 有效profile/参数/费用/trace、实际generation、partial/degradation、存储/重建状态；从同一个公开入口复现原查询 |

此顺序先使设置、检索服务和消费者完整，再进入算法对照与优化。阶段检验可继续复用少量连续真实场景和集中数值golden，避免为每个旧内部接口另建测试流程。

## 本轮已确定的合同修正

省略`$return`保留原实际行为：Memory四域加已供给Self两域；显式`$return(cognition)`仍是Memory四域。新增`$return(concept)`补齐概念精确返回的实际缺口，原13域全部保留。这是本轮依据宪纲与真实消费者作出的修正，正式合同见[NousQL与检索](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/NousQL与检索合同.md)。

数值采用与最小依赖闭包也已确定：`reference/**`共22文件只需serde/schemars/nalgebra/std及小型数值Error；Native四模块与VCP组合再需serde_json/blake3/Roaring/USearch。原USearch2.26.2的真实闭包包含cxx、cxx-build和默认numkong，构建需要C++；原toolchain为1.99.0、workspace最低1.98。napi-rs3提供普通`.node`与生成`.d.ts`，不拉入SQLx/tokio业务runtime/tonic。源码迁入表、TypedArray binding、构建/发布和唯一身份映射边界已写入[检索底座](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/检索服务与认知消费者.md)。这些是当前施工选择，原算法公式尚未改写。

历史两个截点的正式合同已由[时间与调度](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/时间与调度.md)确定；以下保留算法测量和具体消费者接线的问题。

## 十、Specs修正前的未决问题

1. **默认算法与研究可选项**：Native Wave、DTSC、RiverMemo V3各适合什么任务与数据量？用相同真实embedding/语料，在直接专名、弱线索、多跳解释、长经历顺序、重复原根、时间修订这几类查询中比较召回、延迟、内存、费用；据结果决定默认及启用条件。
2. **有序性从何而来**：哪些对象具有正式source sequence？Tag attachment本身是集合；Episode成员、材料区域与实际时间顺序可提供不同序列。先确定语义，再测曲线几何。
3. **历史资产成本**：依已定双截点合同，测量owner历史读取、版本posting和历史数值资产的复用/重建成本，确定实际保留与按需取得政策。
4. **可访问性和来源独立性**：明确衰减使用的时钟、多个根共同支持的权重、重复转述对流量和独立置信各有何影响；用有来源的连续使用轨迹定参数。
5. **规模与权限子图**：测定authorization bitmap构造、当前/历史资产、受限VCP重建、全向量副本的代价，再确定增量、缓存或有界图读取机制。
6. **增强能力合同**：统一residual、concept enrichment、rerank和multimodal各旗标与真实步骤；model output只选已供给的目录，临时假设与持久Authority分开。
7. **维护如何改变真实查询**：accretion目前进入概念维护目录；维护后的Tag/关联须在后续真实查询和自然认知投影中产生可观察差异，再判断算法与后台时机的收益。

以上问题需要调查或小规模判别实验。语言语义、全部领域与投影、稳定引用、来源与历史能力已经具备明确依据，修正Specs时应直接承接。

[nql-doc]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/reference/NOUSQL.md#L7
[nql-agent]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/agent/NOUSQL.md#L249
[parser]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/nousql/parser.ts#L34
[parser-controls]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/nousql/parser.ts#L333
[compiler]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/nousql/compiler.ts#L43
[compiler-time]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/nousql/compiler.ts#L297
[identity]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/persistence/src/identity.rs#L35
[identity-bind]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/persistence/src/identity.rs#L294
[proquint]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/persistence/src/proquint.rs#L7
[core-consumer]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/cognition/service.ts#L317
[orchestrator]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/query/orchestrator.ts#L51
[kernel]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-kernel/src/lib.rs#L381
[bind]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/bind.rs#L40
[plan]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/plan.rs#L38
[rrf]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/ranking.rs#L401
[rrf-config]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/config/reference/retrieval-ranking.json#L3
[preferences]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/preferences.rs#L73
[finalize]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/prepared.rs#L232
[lease]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/prepared.rs#L13
[runtime]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/orchestrate.rs#L139
[representation]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/representation.rs#L215
[concept-activation]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/concept/lane.rs#L9
[concept-model]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/concept_model.rs#L29
[concept-config]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/config/reference/query-concept-activation.json#L3
[lexical]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/lexical.rs#L294
[lexical-schema]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/lexical.rs#L389
[dense]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/dense.rs#L166
[dense-open]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/dense.rs#L57
[query-serving]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/query.rs#L262
[graph]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/graph.rs#L97
[wave]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/wave.rs#L71
[wave-config]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/config/reference/topology-wave.json#L3
[native-lane]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/topology_lane.rs#L12
[native-epa]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/cue_sensing.rs#L17
[native-residual]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/mechanisms/residual.rs#L70
[profiles]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/cognitive_profile.rs#L13
[vcp-generation]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/generation.rs#L27
[vcp-observation]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/observation.rs#L24
[vcp-lane]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/lane.rs#L8
[vcp-offers]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/lane.rs#L169
[vcp-order]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/adapter.rs#L51
[vcp-roots]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/graph.rs#L27
[vcp-authorized]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/vcp/index.rs#L180
[pipeline]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/pipeline.rs#L39
[epa-train]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/epa_training.rs#L243
[epa-basis]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/epa_training.rs#L184
[epa-analysis]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/fields.rs#L230
[pyramid]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/pyramid.rs#L160
[intrinsic]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/intrinsic.rs#L280
[vcp-graph]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/graph.rs#L65
[vcp-transport]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/graph.rs#L187
[gating]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/gating.rs#L83
[sense]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/sense.rs#L134
[fusion]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/fusion.rs#L213
[dual-fields]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/fields.rs#L134
[dtsc]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/dtsc/mod.rs#L94
[dtsc-curve]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/dtsc/curve.rs#L546
[dtsc-config]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/dtsc/config.rs#L27
[dtsc-field]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/dtsc/field.rs#L43
[pool]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/pool.rs#L51
[shape]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/query_shape.rs#L216
[omega]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/query_shape.rs#L85
[path]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/geometry.rs#L73
[relative-topology]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/topology.rs#L134
[anchors]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/anchors.rs#L132
[pure]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/observables.rs#L145
[innovation]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/scoring.rs#L267
[readout]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/reference/readout.rs#L235
[accessibility]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/memory/src/service/accessibility.rs#L86
[accessibility-config]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/config/reference/memory-accessibility.json#L3
[accretion]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/memory/src/service/accretion.rs#L73
[accretion-consumer]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/memory/src/service/concept_maintenance/plan.rs#L267
[concept-transaction]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/memory/src/service/tag.rs#L319
[association]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/memory/src/service/topology.rs#L380
[lifecycle]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/src/assets/lifecycle.rs#L97
[residual-gap]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/query/closure.rs#L5
[conformance]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/research/vcp-conformance.md#L5
[goldens]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/research/corpus/vcp/README.md#L1
[golden-test]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/retrieval/tests/vcp_reference.rs#L26
[upstream-manifest]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/research/corpus/cognitive-retrieval-sources.json#L4
[license]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/LICENSE#L2

[projection-default]: https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/core/src/query/expression.rs#L64
