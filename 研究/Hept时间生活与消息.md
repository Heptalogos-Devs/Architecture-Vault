# Hept 时间、生活与完整消息：基础设施研究

研究日期：2026-10-20。目的：恢复原有领域能力对基础设施的真实要求，为后续 Spec 纠偏提供依据。生产代码开发暂停；本文的接口段落是候选设计，尚未进入正式合同。

## 结论

时间基础不能缩成世界对象上的 `clockId + ISO`。原 Nous 已有带域时间、修订、现实锚点、单调在线推进、持久高水位、幂等改钟、停机政策、到期投影和五轴联合证据；Hept 的日历、生活积分、前台、任务、发送和历史读取都消费这些区别。应恢复 `TimeDomain / ClockSegment / ClockRevision`，并由完整消费者决定捕获、查询、恢复与调度合同。

消息基础也不能缩成文本与附件标记。原 Hept 已区分原始平台事实、附件保全、引用与转发展开、通知、选定阅读、实际模型接触、表达采用和物理发送。默认 QQ 接入选择 `xucheng/openclaw-onebot` 的源码改编版，直接复用其 OpenClaw ChannelPlugin、多账号、WebSocket 与出站媒体接线；先复制旧 Hept 的保真解析、转发展开和媒体取得源码，再在该插件的实际 owner 改编。QQContextBot 的卡片、表情及内嵌转发纯函数作为增补来源。AstrBot 是可选渠道插件与管理参考。

需要保留的领域内容包括世界作者与主体视角、已实现区间与覆盖缺口、日程原实例身份、生活状态政策修订、后台工作成果的显式交付、当前发送权限与不可重复的实际效果。第三方提供时间算法、持久执行、协议、传输和存储机制；这些领域含义由产品模块承担。

## 权威与固定来源

需求依据为[项目宪纲](../项目宪纲.md)的第 26、34—44、45—48 节。当前自包含合同见[时间与调度](../设计/基础设施/时间与调度.md)、[媒体与材料基础](../设计/基础设施/媒体与材料基础.md)及[整体架构与模块合同](../设计/整体架构与模块合同.md)；实现事实以下列固定源码为准。

| 来源 | 固定版本 | 本地只读材料 |
|---|---|---|
| Heptalogos 原 master | `21f0080460f3ee639deb9f5ea47282fb6c59df95` | `../../temp/spec-research/hept-original/` |
| Nous-Wave 原 master | `412b062082afb75ccfae4c3f69fc606d3e3cc862` | `../../temp/spec-research/nous-original/` |
| QQContextBot | `3a7e9107584becce71d02cbe779b3669066612a5`，项目版本 1.5.1，MIT | `../../temp/spec-research/QQContextBot/` |
| OpenClaw OneBot | `c926fe62db49f6ba66fe67ff0dba240efa8fc9dd`，1.2.15，MIT | `../../temp/spec-research/openclaw-onebot/` |
| Temporal 验证依赖 | `@js-temporal/polyfill` 0.5.1，使用现存安装 | `../../temp/spec-research/probes/dst.mjs` |

未读取或采用 Vault。没有恢复用户已删除的施工方案。新增实验和结果均在 `temp/spec-research/probes/`。

## 一、时间能力及原有责任

### 1. 时域、时钟与世界各有身份

原 [Nous clock.md](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/specs/active/cognitive-runtime/clock.md) 用 Subject 主世界贯通通用时间能力，明确 `worldId` 与 `timeDomainRef` 独立。其代码中的 `ClockSnapshot` 包含 `subject_id, time_domain_ref, world_anchor, real_anchor, rate, world_now, recorded_at, revision`；`ClockChange` 是 configure / pause / advance / resume。旧实现尚未把 `TimeDomain`、`ClockSegment` 独立建成公开对象，段信息体现在当前锚点与各次改钟完整快照中。恢复独立类型属于本次接口纠偏，不能宣称旧代码已原样提供。[实际类型](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/subject_clock.rs#L18-L65)

在线 `RunningClock` 以 Rust `Instant` 的单调经过时间乘 rate 推进，输出截到 PostgreSQL 微秒精度，并维持 high-water。读钟不写数据库；领域 owner 在自己的 Authority 事务中调用 `capture_in`，将 checkpoint 与业务结果一起提交。原实现是单 Kernel 在线 owner，进程内映射由 Mutex 协调，不能直接扩称多进程时钟服务。[恢复与捕获](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/subject_clock.rs#L68-L192)

改钟使用 request digest、operationId 和 `subject_clock_changes` 保存完整结果；重放先返回旧回执，再考虑当前修订。新操作在锁内比较 expectedRevision，建立新锚点和 revision；同域禁止倒退，默认 real 被改变时转成显式 Subject 域。旧实现限制一个 Subject 一个主时间域，这一限制应由产品当前需求决定，通用值不应把时域身份固定为 WorldId。[改钟事务](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/runtime/src/subject_clock.rs#L194-L354)

旧 Hept 另有通用 `TimeService.now / monotonicNow / elapsedSince`，生产适配直接使用系统 UTC 与 `process.hrtime.bigint()`，FakeTimeService 可分别控制两种时钟。这一层适合网络超时、处理耗时和真实资源期限；它不替代带域认知钟。[基础契约](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/foundation/time-service/src/contracts.ts#L12-L37)

### 2. 五轴与两个历史问题

原 `TemporalExtent` 支持 unknown、instant、端点可省略的半开 interval；`DomainStamp` 保存域、坐标及现实记录点，跨域 compare 返回未知。`SourceTemporalEvidence` 每一行绑定同一个实际 occurrence 的 occurred、observed、现实 observed_at 和 recorded_at；多个来源的发生轴与观察轴不能拼成一个虚假共同见证。[基础类型与联合证据](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/crates/core/src/time.rs#L8-L265)

| 时间含义 | 需要回答的问题 | 必须保留的差别 |
|---|---|---|
| occurred | 事情何时发生 | 消息发送、工具执行、虚拟事件区间各用真实来源的域 |
| observed | 主体何时真正取得选定内容 | 系统收到、后台保全、目录展示均独立记录 |
| formed | 某个表示或认识何时形成 | 后做的摘要、分段与反思各有形成点，恢复复用原成果时间 |
| valid | 内容在何时适用 | 适用范围、发生时段和认知版本互相独立 |
| recorded | 权威记录在现实何时提交 | 始终现实 UTC；支持数据库历史截点 |

`knowledgeAtWorldTime` 回答角色在故事某时刻已知什么，`asRecordedAt` 回答数据库在现实截点持有什么。晚实现的虚拟昨夜见闻可以具有昨夜的叙事观察点，同时保留早晨的实现、现实交接与入库时间；真实昨夜 QQ 消息今天才看，实际接触是今天，不能事后用当前映射回推。来源范围与角色权限先过滤，再进行时间选择。原 Hept 的 world query 已分别按 recordedAt 取历史、按 perception.at 截断角色见闻。[世界历史读取](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-life.ts#L892-L957)

### 3. 离线、改钟竞争与 deadline

旧 Nous 恢复逻辑是：rate=0 保持；其余从持久 checkpoint 按非负现实经过时间以 1 倍补进，再恢复在线 rate。它没有自动按在线加速率补停机时间。Hept Profile/World 的 `simulate_elapsed / pause_with_host` 由 Host 生命周期适配明确操作：正常 stop 保存 before，按离线速率或 rate=0 做 CAS；start 只恢复自己保存的精确 paused revision。操作者中途改钟后返回 superseded；网络结果未知保留 unknown；异常退出留下关机时刻 gap。[Host 真实接线](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/product-host/src/world-host-runtime.ts#L88-L256)、[生命周期 receipt](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-lifecycle.ts#L272-L317)

原 `projectWorldDeadline` 返回 `due {at}`、`paused` 或 `unmapped`。同域到期点以 `realNow + (worldDue-worldNow)/rate` 投影；已到期在暂停钟上仍返回 due，尚未到期才返回 paused。调用方在改钟后重新投影，函数本身不建计时器。[官方 Client helper](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/packages/client/src/clock.ts#L6-L47)

Hept 原 world-runtime 读取正式 Clock，再投影生活节点；world 与 foreground 候选选择同一份原生 scheduler declaration。唤醒只是重新检查机会，不能自行认定世界已到期、主体已阅读或获得模型预算。新 Spec 应保留时钟/自然节点修订，旧唤醒先核对当前修订与语义 due，再继续同一领域操作。[节点投影](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/product-host/src/world-runtime.ts#L68-L115)、[单一声明选择](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/product-host/src/native-dispatch.ts#L20-L39)

### 4. 日历与 DST

旧日历已经支持 RRULE/RDATE/EXDATE、validThrough、生效修订区间、单次例外、移动、取消和显示时区。稳定实例 ID 使用 `worldId + ruleId + 原始当地 RECURRENCE-ID`，修改开始时间不换实例身份。this / future / unrealized 编辑保留已经实现的实例与旧规则版本。[合同](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-calendar-contracts.ts#L20-L101)、[实例与展开](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-calendar.ts#L29-L80)

实际组合是成熟 `rrule` 处理浮动当地复发坐标，Temporal 负责 IANA/DST 转精确点；不能把那个临时 Date 的 UTC 数字当真实时间。rule.disambiguation 支持 compatible / earlier / later / reject；实例保存 originalInterval 与 timezoneAdjusted。[转换位置](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-calendar.ts#L168-L300)。这与 [RFC 5545 的 RECURRENCE-ID](https://datatracker.ietf.org/doc/html/rfc5545#section-3.8.4.4) 原实例语义一致。

本地用 Temporal 0.5.1 实测纽约 2026-03-08 02:30：compatible/later 得 07:30Z，earlier 得 06:30Z，reject 抛 RangeError；2026-11-01 01:30 的 earlier/compatible 为 05:30Z，later 为 06:30Z。旧 `timezoneAdjusted = 当地输入是否被移动` 在秋季重叠时间为 false，因此预览还需展示所选 UTC/offset 和歧义政策。算法直接复用 Temporal，语义说明见 [TC39 官方文档](https://tc39.es/proposal-temporal/docs/timezone.html)。实测结果为 `temp/spec-research/probes/dst.jsonl`。

## 二、必须完整保留的 Hept 消费者

| 领域消费者 | 原有实际行为 | 对基础设施的要求 |
|---|---|---|
| WorldLife / Profile | 世界定义、地点与人物、作者创作范围、规则、未来安排、已实现历史 | 世界身份与时间域分离；采用 CAS、幂等结果与历史；作者和主体视角分别读取 |
| Calendar | planned/lived/combined、有界展开、原实例身份和例外 | 地方时间与精确点、IANA/DST、规则修订和现实历史截点 |
| WorldAction | move/participate/rest 有世界持续时间和后续地点结果 | 用世界 due，不用真实模型耗时替代；完成与原事件引用对应 |
| Living | 按已实现主活动积分，附属活动取最大负荷；按生效 Profile 修订分段；晚加入事件可回到旧 baseline 重算 | 半开区间、覆盖缺口、政策生效点、事务内事件与生活状态同时采用 |
| LifeActivity / WorkContext | adopted scope、时间窗口、progress、nextOpportunity、continuation | Subject/活动/运行身份分离；真实 maxRunMs 与世界窗口分离；恢复原目标与来源 |
| Attention / Reactor | 多来源候选，同一主观前台；通知 considered 与 read 分离；未知运行不换新付费请求 | 实际候选游标、选择与接触分开；前台顺序及延迟由成熟执行系统承担 |
| Native tasks | startExecution 后台 pending；保留 dispatch/input/run/results；ready 后显式 release/read | 原生幂等 requestId、父子运行、工具与来源授权、成果持久化及选定发布 |
| Agency / Narrative | 采用精确表达；当前权限核对；保存每次实际网络结果，再做后续语义整理 | 外部效果身份、dispatch 门、accepted/not_sent/unknown、原消息 ID、表达段对应关系 |
| Query / 管理 / 历史 | 查看日历、过去活动、当时见闻、当前解释与实际发送 | 纯读取不推进世界、不生成模型工作；五轴与现实 as-of 独立 |

WorldLife 已会拒绝未来历史、异域 patch、不存在的角色或地点、冲突地点和独占活动；细节必须处于已实现 parent 区间，perception 只能属于事件参与者。[采用规则](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-life.ts#L178-L315)。因此“读钟后把所有空白都写成自由活动”会丢失实际覆盖语义。旧固定课程实现先按实际地点与阻塞活动计算出席，缺席不向主体提供课堂正文；部分已实现时段不关闭未记录余段。[规则实现](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-rule-realization.ts#L18-L145)

生活状态读取也不将计划睡眠算成恢复。原积分按照实际活动区间与政策历史分段，拒绝同一身体同时睡眠和学习、拒绝多个主活动重复计费，允许有来源的有限事件 delta。[积分与重算](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/world-living.ts#L43-L235)

原 Task 接入保留同 requestId 的既有结果或 pending/uncertain，复杂工作由原生 agent/tool/subagent 执行；不是 Host 再建工具循环。[startExecution](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/product-host/src/subject-roles.ts#L246-L315)。完成只产生待看机会，主体选中精确结果后 `releaseResult` 形成后续 contacts。旧流程的接触在后续输入 admission 前提前提交，留下失败窗口，这个缺陷要在输入实际消费 owner 修正，不能把 ready、release 或上传文件统一标成经历。

### 效果恢复与旧支架的取舍

旧通用 EffectOperation 有 PREPARED → DISPATCHING → SUCCEEDED/FAILED/UNCERTAIN；先短事务确认 dispatch 门，再事务外调用，之后保存结果；异常归 uncertain，恢复只读 reconcile，不重新发写操作。[实际状态机](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/execution/effect-operation/src/service.ts#L352-L500)

旧 Agency 同时保存领域表达和物理回执；beginDelivery 在当前 Activity 行锁内核验最新取消/权限，已有 accepted 直接返回，in-flight/uncertain 阻止重发；回执持久后再通知其他 owner。[实际发送门](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/subject/src/agency.ts#L342-L447)。原 QQ adapter 还有每 source 仅一个 physical part 的限制，长草稿直接拒绝，属于待修能力缺口，不能写进通用新合同。[实际物理交接](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/openclaw-host/src/delivery.ts#L87-L219)

应保留上述效果事实与恢复规则。旧 EffectOperation 依赖的独立 ExecutionLineage、Evidence、Host fence 和自定义持久执行支架是否保留，应按成熟执行库能承担的机制整体收敛；不能因“旧代码已有”再搬一套平行运行平台。

## 三、消息与媒体的精确读写链

### 1. Hept 原有 owner

| 阶段 | 精确位置 | 读写内容 |
|---|---|---|
| 原始接入与段解析 | `packages/application/openclaw-host/src/parser.ts` 的 `parseMessageParts`；`lossless.ts` | 保留平台身份、完整 protected envelope、按 segment index 的 nativeDataRef；text/at/reply/forward/image/video/file/audio/mface/sticker/face/card/share/location/unknown |
| 收件事务 | `packages/product/messaging/src/service.ts:166` 的 `accept` | 按 conversation + nativeMessageId 去重；保存 sequence、事实、待处理引用、附件与转发引用；提前到达的撤回也进入 lifecycle |
| 附件保全 | `packages/application/openclaw-host/src/resources.ts:58` 的 pump；`media.ts` | 重新检查账号、群/私聊 receive 范围；按协议源取字节，核对 hash/length，CAS 更新 available/expired/failed |
| 受保护内容 | `packages/application/product-host/src/archive-store.ts:19` | 原始 JSON 和媒体字节各用内容地址；流式限额、hash、临时写入；读取验证完整性，目录元数据不带正文许可 |
| 转发展开 | `packages/application/openclaw-host/src/forward.ts:34` 的 `expandForwardReference` | 原节点 path/parentPath、claimedAuthor、发送时间、完整 parts、来源指针；depth/nodes/bytes/requests/cycle 限额和可续状态 |
| 历史补拉 | `packages/application/openclaw-host/src/history-sync.ts:22` 的 `synchronizeQqHistory` | 先接实时流，补拉复用同一 accept；保存原响应来源、native cursor、limited/gap/unavailable 与原因 |
| 阅读准备 | `packages/product/messaging/src/service.ts:363` 的 `prepareRead` | 根据实际授权会话取选定消息和 ready 附件；按完整消息单元做数量/字节预算，报告 omitted；未接触前已撤回正文 withheld |
| 媒体送入 Nous | `packages/application/product-host/src/selected-media.ts:20` 的 `createSelectedMediaUploader` | 从 exact message contact 取得原附件字节，上传正式 Artifact；保留 attachment_ref、part_index、原媒体类型、CAS 与 Artifact hash |
| 来源与实际接触 | `native-source-selection.ts`、`native-perceptions.ts`、`native-cognition.ts:1476` 的 `admitted` | 绑定当前 Task/Activity、实际被接受的 occurrence、consumer/projection；附件归原 message root；下游不能从未 admitted 的来源推导已知 |
| 发出与回执 | `packages/product/subject/src/agency.ts`、`packages/application/openclaw-host/src/delivery.ts` | 冻结表达与受众，发送前复核当前来源和权限；真实平台结果先落盘，认知整理失败不重做发送 |

上述路径均在固定 Hept commit 中，可由 [Messaging 读取](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/product/messaging/src/service.ts#L363-L460)、[附件获取](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/openclaw-host/src/resources.ts#L58-L155)、[转发原结构](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/openclaw-host/src/forward.ts#L34-L215)、[媒体精确来源](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/product-host/src/selected-media.ts#L19-L74) 核对。它们提供要承接的领域能力，不要求保留原包拓扑。

### 2. QQContextBot 可采用的实际能力

其 `qq_recorder` 是独立静默记录插件；`grok` 是可选 agent 回复插件。`MessageProcessor.process_message` 先在 inflight semaphore 内解析和事务保存；转发网络获取及图片/视频下载在外运行。转发有 API、URL+HTML 内嵌 JSON、inline node 三种来源；图片按内容 MD5、格式与日期归档；视频可经 NapCat `get_file` 把 file code 解析成实际本地路径/URL。SQLAlchemy AsyncSession 负责消息与关联行同事务保存。[收件顺序](https://github.com/Heptalogos-Devs/QQContextBot/blob/3a7e9107584becce71d02cbe779b3669066612a5/plugins/qq_recorder/processors.py#L53-L106)、[转发 fallback](https://github.com/Heptalogos-Devs/QQContextBot/blob/3a7e9107584becce71d02cbe779b3669066612a5/plugins/qq_recorder/processors.py#L192-L318)、[保存事务](https://github.com/Heptalogos-Devs/QQContextBot/blob/3a7e9107584becce71d02cbe779b3669066612a5/plugins/qq_recorder/storage.py#L253-L323)

值得直接参考和改编的源码是 card/app share 提取、QQ sticker 元数据、三路转发取得、NapCat 媒体定位，以及入库后继续保全的流程。GIF 原字节应保留，动画理解再由帧/时序派生承担。图片下载目前按块累计到内存后整体写文件；视频本地路径读取也整体读入，不能把这些实现描述成已经完成流式 CAS。[图片字节流程](https://github.com/Heptalogos-Devs/QQContextBot/blob/3a7e9107584becce71d02cbe779b3669066612a5/plugins/qq_recorder/image_handler.py#L117-L205)、[视频协议定位](https://github.com/Heptalogos-Devs/QQContextBot/blob/3a7e9107584becce71d02cbe779b3669066612a5/plugins/qq_recorder/video_handler.py#L79-L118)

### 3. 已核实的限制与缺陷

| 位置 | 实际事实 | 采用时的处理 |
|---|---|---|
| `message_parser.py:69,315` | allowlist 只有 text/image/video/at/reply/forward/face/json；record/file/mface/其他原段不进入 segments | 原生原件无损保存；未知类型保留 typed unknown + 原始段，不用 allowlist 丢弃 |
| `forward_parser.py:13,83,146` | ForwardNode 只有作者、depth、summary、children、forward_id；summary 把图/文件替成标签；flatten 每行 parent_forward_id 都为 None | 保留原节点 ID/路径、父子、原作者、时间、有序完整 parts 和媒体来源；summary 只是派生阅读表示 |
| `processors.py:95` | 转发 backfill 是 `asyncio.ensure_future`，进程结束后没有持久待续记录 | 持久进度由选定执行系统持有，原消息/来源状态由消息 owner 持有 |
| `storage.py:539` | backfill 删除旧 ForwardMessage 行再插入，未保存展开修订历史 | 原件与逐次取得的表示分开；采用正式修订，不覆盖已提供给调用者的旧引用 |
| `models.py:27` / `storage.py:293` | message_id 全库 unique，重复时直接取旧行；账号/会话未参与键，异内容没有 digest 比较 | 使用平台、登录账号、会话和原生消息 ID 的真实身份；同身份异正文走编辑/冲突合同 |
| `processors.py:143` / `outbound_recorder.py:118,147` | `datetime.fromtimestamp` / `datetime.now()` 是无时区本地 datetime | 分别保存现实 UTC platformSentAt、receivedAt、attemptedAt；主体 observed 另捕获正式域与映射 |
| `storage.py:774` / `models.py:194` | 视觉结果按 file_unique+model_used upsert，prompt/schema 改变会更新原行 | 原始媒体、派生表示、模型与提示版本、形成时间和来源修订都需持久可追溯 |
| `outbound_recorder.py:25,71` | 在原生发送返回后包装记录；缺 message_id 直接返回，入库失败只 warning；没有 not_sent/unknown 台账 | 保持原生发送 owner，实际物理调用前后写入精确状态及结果；不能用这个 recorder 代替效果恢复 |

前三项中的内容丢失和出站保存失败已用原源码直接验证：输入 `[text, record, file, mface, image, text]`，实际可保存段仅 `[text, image, text]`；嵌套节点输出丢失 time/原 parts 且两行 parent 都为 null；模拟原生 accepted 后 storage 抛错，包装器仍返回原平台 message_id，仅记 warning。脚本与输出分别为 `temp/spec-research/probes/message-and-time.py`、`message-and-time.jsonl`。这是解析和包装器的隔离实验，没有连接 QQ。

推荐采用方式：在选定的正式平台插件内复用和改编上述纯 Python 解析/协议取得 owner，修复原件与节点保存；继续调用平台原生发送、历史与媒体能力。产品消息权威落在 Hept 的正式模块与数据库。若使用该项目的存储源码，移入真实消息存储 owner 后替换相应旧实现；不让 QQContextBot SQLite 与 Hept 数据库同时维护两份可变事实。其可选 grok agent/tool loop 也不替代已选的原生专业执行环境。

### 4. 默认 QQ 接入的实际选择

现存 OpenClaw `data/upstream/openclaw/extensions` 在读取的本地 commit `ec69b5505e742c7b944827e3460899d2987fa24b` 中没有 QQ/OneBot channel；`extensions/tencent` 的 manifest 仅注册模型 provider。默认接入采用已拉取的 OpenClaw OneBot 源码，固定版本如上。其 manifest 是真实 `onebot` channel，依赖只有 `ws`，并已有多账号、连接重试、配置、语音转换、文件 staging、文本/媒体/文件/Reaction 的 API 调用。[固定入口](https://github.com/xucheng/openclaw-onebot/blob/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd/index.ts)、[channel owner](https://github.com/xucheng/openclaw-onebot/blob/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd/src/channel.ts#L47-L68)

| 必需入口 | 现成代码与缺口 | 在负责位置的改编 |
|---|---|---|
| 入站 raw / 完整 parts | `gateway.ts:559` 能取得原始 WebSocket 字符串，之后 JSON.parse；`bufferMessage` 提取 text/images/record；1.5 秒聚合后只传合并文本与图片标签，MessageSid 取最后一条 | 在当前 ws message owner 先保全 raw 并逐原生消息持久接纳，再提供元信息通知；Hept 产品接线由同一 Reactor 决定阅读/回复，删除该接线中的自动 agent 回复流程 |
| 数字与作者身份 | types 把 ID 定为 number，JSON.parse 会先经过浮点数 | 直接搬旧 `lossless.ts`，用 Node 24 JSON reviver 的 source 保留原数字词元；只将有界控制数转 number |
| 回复、转发、notice | 当前无转发展开/历史函数；notice 只 debug；sendText 接受 replyToId 却没放入 wire message | 复制旧 `parser.ts`、`source.ts`、`forward.ts`、`history.ts/history-sync.ts` 到该插件；恢复 reply 段、notice 变更与有界补拉，使用同一 OneBot API client |
| 入站媒体保全 | 已有语音路径及本地转换，图片只作为 URL 进入正文；缺原始媒体统一保存状态 | 搬旧 `media.ts/resources.ts` 的协议取得、export-root 校验、字节/hash/状态逻辑，传输使用插件现有 client 与 OpenClaw 成熟媒体 helper；原始语音、GIF 与派生分别保存 |
| 实际物理发送 | `outbound.ts:45` 的 callApi 是已存在的 HTTP 点；sendMedia 可先媒体后文本，当前只返回一个 messageId；文件 API 无 messageId 时以 Date.now 代替 | 在这个 callApi 及调用方记录每个真实变更请求的 dispatch、原生结果和表达段关联；暴露 receipt 数组，删除伪消息 ID；查询历史不归为发送 |

入站源码依据为 [原始 WS 点与 notice](https://github.com/xucheng/openclaw-onebot/blob/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd/src/gateway.ts#L559-L583)、[聚合后的上下文](https://github.com/xucheng/openclaw-onebot/blob/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd/src/gateway.ts#L243-L320)。物理调用依据为 [callApi/sendText](https://github.com/xucheng/openclaw-onebot/blob/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd/src/outbound.ts#L45-L83)、[sendMedia](https://github.com/xucheng/openclaw-onebot/blob/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd/src/channel.ts#L157-L189)。外层 `sendMedia` 的成功或异常不能覆盖内部两个实际调用的不同结果。

已把上述旧 Hept 8 个消息文件及 6 个时间文件原样复制到 `temp/spec-research/source-candidates/`，SHA-256 和固定 commit 记录在 `manifest.json`；后续施工从这些文件迁入目标 owner，再修改 imports、合同与原生 client 调用。旧 `transport.ts`、自有队列/fence 与宿主编排不迁入。QQContextBot 是 Python，默认插件是 TypeScript：`extract_app_shares`、sticker metadata/data tables、`parse_forward_embed` 的解码和兼容格式处理应从已复制原函数改编到当前 parser/forward，而不增加 Python 服务。它的 allowlist、flatten、SQLite、grok loop 不进入默认接线。

附加隔离实验使用原 OneBot channel/outbound/config/env 源码，以 Node 自带 stripTypeScriptTypes 运行，仅把未使用的 gateway import 换成桩；真实本地 HTTP 请求验证：媒体+正文发出两次 send_group_msg，返回仅第一个 ID；replyToId 未进入消息；上传文件缺 message_id 时返回当前毫秒数。原源码未修改，实验位于 `probes/onebot-outbound.mjs` 和 `.jsonl`。OpenClaw 2026.10.5 的 SDK 最终编译、持久入站接纳和实际 QQ 故障恢复仍由后续施工核验。

## 四、基础设施 Spec 的接口候选

以下是依据已核实消费者形成的候选轮廓；命名、精度和公开路由由根任务统一定稿，尚未通过新合同集成验证。

### 时间与调度

- `TimeDomain`：稳定域身份、可读含义、坐标说明；real 是保留域。World、Subject、Clock 各持独立引用。
- `ClockSegment`：segmentId、clockId、revision、timeDomainRef、domainAnchor、realAnchor、rate、开始/结束依据、离线政策；已结束段可查，当前段的每次读时值不产生新修订。
- `ClockSnapshot`：ClockRevision、当前段引用、同一次捕获的 domainNow 与 realNow、映射来源。捕获应能与所属业务事务/已保存模型成果绑定。
- `clock.read/capture/configure/pause/resume/advance/history/projectDeadline`：改钟采用 operationId+expectedRevision，保存同请求的精确回执；deadline 结果保持 due/paused/unmapped。真实超时、重试 backoff、任务 wall-clock limit 继续使用现实/单调时钟。
- 调度接入：领域保存语义 due 与当前自然节点；由成熟执行系统做现实延迟等待。改钟、改日历、暂停、恢复后重投影；到期回调核对 clock/node revision。无需每分钟模型心跳或另一套通用队列。
- 时间查询：提供 DomainExtent/DomainPredicate、每个实际接触的联合来源时间、`knowledgeAt` 与现实 `asRecordedAt`；未知域映射返回 unknown，不按裸数字比较。

Temporal 直接承担历法、IANA、DST 和时间算术；成熟 RFC 5545 库承担复发集合。时域/段/修订、业务捕获与实际来源关联是产品所需的少量领域语义，不能用 Date 算术省略，也不需要扩展成自有时间调度框架。

### 消息、资料与效果

- `messages.accept` 保全规范化结构和 raw source；`messages.read` 根据当前权限返回完整选定单元、可继续引用及 omitted 原因；`message-changes` 维护编辑/撤回历史与现行可用性。
- `sources.read` 能按 exact ref+revision+selector 返回原材料区域和当前政策；`sources.policies` 批量取得当前许可/撤回，不把引用字符串本身当权限。
- `blobs.putStream/readStream` 使用成熟内容存储与传输机制；Message/Media owner 保存来源、实际字节元数据、保全状态与当前许可。媒体下载、转录/视觉派生、选择区域、模型实际消费分别记录。
- `forward.expand` 保留原始响应、节点 path/parent、作者与发送点、完整 parts、continuation、明确预算/缺口；同一字段不同时承担原件与摘要。
- `native.tasks` 直接沿原生 start/inspect/cancel/history/现有恢复操作；返回选定成果的精确已保存引用，经实际发布/阅读进入主体。专业 worker 原始历史与主体已知内容分别授权。
- `effects.prepare/dispatch/inspect/reconcile` 的能力放到实际外部效果 owner：同一表达段可对应多个物理调用，一个物理调用也可含多个表达段；accepted 保留原生 messageId，not_sent 有确定依据，unknown 保留原操作供查询或显式解决。

最终共同纯值只共享通用身份、时间、来源、政策和 trace。World/Calendar/Activity/Pursuit/Commitment/Decision/Task/Expression/Message 的含义、修订和事务由 Hept 对应模块拥有；五轴和认知修订的含义由 Nous 认知 owner 拥有。

## 五、用少量真实场景检查基础设施闭合

1. 普通下午：课程进行中收到提及、GIF 与嵌套转发。先保全原件与到达时间，世界只实现已过部分，通知不带未读正文；主体打开后，所选消息/媒体区域成为本次实际模型输入，再形成接触。课堂余段及回复后的活动继续有据。
2. 停机与改钟：世界加速运行时正常停止，Host 保存精确停钟回执；停机期间管理员改变时钟，启动不能用旧配置覆盖。模拟断电只恢复持久高水位并保留未知关机范围。原 due 节点重新投影，不直接触发付费调用。
3. 后台查证与发出：Subject 委派有原目标的任务并继续生活；原生完成后成果待看，主体选择发布内容。文本与媒体造成多个物理调用，部分 accepted、部分 unknown；重启沿原结果继续，仅记录后续交接，已经发生的发送不重复。
4. 晚实现的过去：早晨补昨夜虚拟世界片段和合法角色见闻，五轴保存各自实际时间；查询“昨夜在故事中已知”与“昨夜数据库已记录”得到不同结果。真实昨夜 QQ 消息今天阅读保持今天实际接触。

本文已完成原源码检查、解析/出站包装器隔离实验与 Temporal DST 实验。尚待后续实现检验的是新的时域/时钟段合同、跨产品时间来源接入、持久执行与真实平台的组合故障恢复；本轮没有运行旧产品服务、付费模型或实际 QQ 账号。
