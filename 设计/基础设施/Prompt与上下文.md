# Prompt 与上下文

## 采用与责任

Prompt 机械位于 `packages/platform/src/prompts/`，经 `@nous-wave/platform/prompts` 导出。它组合原 Nous PromptRegistry、LiquidJS 10.30.0、Chokidar 6 和 PostgreSQL 修订；两个产品分别实例化、分别持有自己的资源和数据。完整 Prompt 文字、参数 schema、认知读取与成功消费均归产品领域。通用库只负责资源、模板、修订、预览与快照。

直接迁入原 Nous `apps/nous-core/src/model/prompts.ts` 和完整 `prompts/`，保留 realpath 根限制、128 KiB 限制、UTF-8/非空校验、SHA-256 与 program/config 来源。原 Hept `role-prompts.ts` 的五个完整职责迁入 Hept 资源目录。移植 MaiBot PromptManager 与 WebUI 中元信息、参数检查、版本激活、回退和预览的完整流程，渲染用 LiquidJS 替换手写 Formatter。固定提交、具体文件与许可见[研究报告](../../研究/第三方模型Prompt与管理.md)。

模型派发与实际请求追踪见[模型供应与调用](模型供应与调用.md)；共同 Ref、OriginIdentity、TimePoint、CallContext、Problem 使用[共同值](共同值与调用上下文.md)。认知候选、来源校验和预算选择归 Nous contexts/query owner，见[检索服务与认知消费者](检索服务与认知消费者.md)。

## 资源目录与正式值

程序资源随产品发行，保留原分目录。每个产品导出静态 PromptCatalog，避免依赖文件 stem 猜身份；原 `memory/formation.md` 与 `self/formation.md` 必须有不同 PromptId。Prompt 的语言、管理界面语言与主体自然语言分别选择。

```text
Nous-Wave/packages/nous/prompts/en/memory/formation.md
Nous-Wave/packages/nous/prompts/en/self/formation.md
Nous-Wave/packages/nous/prompts/zh-CN/query/concept-enrichment.md
Heptalogos/packages/hept/prompts/zh-CN/subject/deliberation.md
Heptalogos/packages/hept/prompts/zh-CN/subject/expression.md
<Paths.config>/prompts/<scope.kind>/<encoded-scope-id>/<locale>/<namespaced-id>.liquid
<Paths.config>/prompts/<scope.kind>/<encoded-scope-id>/<locale>/<namespaced-id>.meta.json
```

```ts
const PromptIdSchema = z.string().regex(/^[a-z][a-z0-9_-]*(\.[a-z][a-z0-9_-]*)+$/);
const PromptScopeSchema = z.discriminatedUnion('kind',[
  z.object({kind:z.literal('installation'),installationId:InstallationIdSchema}),
  z.object({kind:z.literal('subject'),subjectId:SubjectIdSchema}),
]);
const PromptBindingSchema = z.object({
  promptId:PromptIdSchema,
  locale:PromptLocaleSchema.optional(),
  revision:z.number().int().positive().optional(), // 未指定则取该范围当前激活项
});
interface PromptDescriptor<T> {
  id:string; owner:string; labelKey:string; descriptionKey:string;
  visibility:'standard'|'advanced'|'developer';
  locales:readonly string[]; defaultLocale:string;
  programFiles:Readonly<Record<string,string>>;
  paramsSchema:ZodType<T>; paramsSchemaRevision:string;
  examples:Readonly<Record<string,T>>;
  allowedPartials:readonly string[];
}
interface PromptSnapshotRef { id:string; digest:string }
interface PromptSnapshot {
  ref:PromptSnapshotRef;
  promptId:string; locale:string; scope:z.infer<typeof PromptScopeSchema>;
  sourceScope:z.infer<typeof PromptScopeSchema>;
  source:'program'|'override'; revision?:number;
  catalogRevision:string; paramsSchemaRevision:string;
  dependencies:readonly {
    promptId:string;locale:string;scope:z.infer<typeof PromptScopeSchema>;
    source:'program'|'override';revision?:number;digest:string;
  }[];
  engine:{name:'liquidjs';version:string;optionsDigest:string};
}
```

scope 表示请求覆盖所属产品范围，sourceScope 表示实际选中资源所属范围。RolePolicy 在 settings 中保存 PromptBinding，允许安装默认、主体、职责选择；同一 Prompt 内容只在 prompts owner 保存一次。Binding 未给 locale 时采用 platform.prompts.locale；查找顺序为显式锁定修订、主体激活覆盖、安装激活覆盖、程序该语言、程序默认语言。锁定修订须明确 locale，并只定位所请求 scope 的该修订；返回实际 locale/sourceScope/source/revision，失效或不兼容时返回错误。

上述资源随产品打包到 Paths.program 下，由 catalog 的 programFiles 与 programRoot 注入实际位置；原十五份英文全文在 en 目录保留；Nous 静态目录注册原16职责及 video_description、motivation_criterion，领域输入作为真实 SDK messages，程序资源参数为严格空对象。新中文资源单独归 zh-CN。覆盖编辑根使用 Paths.config/prompts，scope-id 经 encodeURIComponent 编码；不同主体与安装的编辑文件分别定位。程序/编辑路径和其他逻辑根采用[安装规范](安装与生命周期.md)。请求 scope 的 installationId 须与当前受权实例一致。

Prompt params 是有 schema 的普通数据；模板不能获得数据库对象、凭据、Actor 权限或带执行方法的对象。时间在参数中传入共同 TimePoint 和领域已格式化说明；模板不读本机当前时间。领域输出 schema 仍由领域 contracts 持有，Prompt 引用其身份与规则，不再保存一份可写输出 schema。

## 模板引擎与组成

选 LiquidJS 的严格 parse/render、异步渲染、内存 templates 与资源限制。将冻结的依赖闭包构造成内存模板表，运行时不允许模板任意读目录。静态 partial 使用固定名称，例如 `{% render identity, subject: subject %}`；该配置下名称不加引号。本轮对真实 10.30.0 的命名 partial、缺变量、原样 JSON 与 `A<B` 已运行验证。

```ts
const engine = new Liquid({
  templates:frozenSources,
  dynamicPartials:false, relativeReference:false,
  strictVariables:true, strictFilters:true, ownPropertyOnly:true,
  parseLimit:131072, renderLimit:100, memoryLimit:1048576,
  // 不设置 outputEscape；Prompt 保留实际文字和 JSON
});
const parsed = engine.parse(snapshot.source);
const text = await engine.render(parsed, descriptor.paramsSchema.parse(params));
```

上述 parseLimit 是字符数限制，Registry 另按 UTF-8 字节限制单资源 128 KiB；整个依赖闭包默认最多 32 个资源、512 KiB。renderLimit 为单次渲染毫秒预算，memoryLimit 为库所限制的对象/字符串量；另在结果处检查 256 KiB UTF-8 输出上限。使用 LiquidJS 的限制和错误，不另写解释器。

参数准备先由领域异步读取完成，再交给纯 renderer。固定 partial 依赖用 LiquidJS 公开 Template.partialScope()、children(false,false) 和 toPromise 遍历实际解析结果，并与 catalog 允许名单核对；候选激活前检查不存在、循环和超限。正式参数合同与严格 render 决定是否可采用。模板展开的 ref、来源与策略是 params 之外的结构化元数据，原样跟随实际 ContextView。

## 保存、激活与本地编辑

数据库不可变覆盖修订和 active head 是运行时权威。程序文件是发行默认；本地覆盖目录是受管理的导入/导出编辑面。所有入口调用同一 prompts.save/activate 流水线。运行中的 renderer 不一边读数据库、一边任意读可变覆盖文件。

```sql
create table prompt_revisions (
  id uuid primary key,
  prompt_id text not null, locale text not null,
  scope_kind text not null, scope_id text not null,
  revision bigint not null, source_text text not null,
  digest text not null, params_schema_revision text not null,
  dependencies jsonb not null, origin jsonb not null,
  actor jsonb not null, reason text, recorded_at timestamptz(6) not null,
  unique(prompt_id,locale,scope_kind,scope_id,revision)
);
create table prompt_heads (
  prompt_id text not null, locale text not null,
  scope_kind text not null, scope_id text not null,
  revision bigint not null,
  latest_revision bigint not null, active_revision bigint,
  primary key(prompt_id,locale,scope_kind,scope_id)
);
create table prompt_snapshots (
  id uuid primary key, digest text not null unique,
  manifest jsonb not null, recorded_at timestamptz(6) not null
);
create table prompt_change_receipts (
  operation_id text primary key,
  action text not null, prompt_id text not null, locale text not null,
  scope_kind text not null, scope_id text not null,
  request_digest text not null, result jsonb not null,
  actor_authority_ref text not null, consumer jsonb not null,
  recorded_at timestamptz(6) not null
);
```

heads 对 revisions 建相同复合键外键，事务结束前保证 latest/active 引用存在。head.revision 是 save/activate/reset 共同递增的 CAS 序号，latestRevision/activeRevision 是内容修订；激活不新增内容，但仍使 CAS 序号递增。read 同时返回请求层的 head 序号、实际 sourceScope/sourceRevision 及正文，管理端不从继承正文猜当前覆盖。原件正文、依赖正文、digest、参数合同摘要与渲染限制在 manifest 中冻结，发行文件与 active 变化后仍可复现已保存快照。当前参数合同不兼容时拒绝执行旧快照，历史读取仍可用。内容保留由 data owner 处理。

save/activate/reset先核验当前授权并查本owner的receipt：相同operation_id和规范请求digest返回原result，不先用旧expectedRevision拒绝成功重放；不同请求冲突。result包括保存/激活/恢复继承与no-op的原结果，在修改head的同一短事务保存。该表仅是Prompt正式幂等回执，不含运行步骤/租约。operation_id是稳定text key；复合save＋activate流程为两项真实操作分配稳定子key，文件导入也使用同合同。请求digest不混入重试时新取得的now/head/default。DBOS内步骤使用datasource，普通短写直接使用Kysely事务。

1. `save` 验证授权、expectedRevision、UTF-8/路径/体积、当前参数合同、模板语法和依赖。用声明 examples 运行同一 renderer，保存不可变候选修订并 CAS head/latest。保存默认不激活；相同候选可返回 no-op。
2. `activate` 校验 expectedRevision、候选及当时依赖闭包，在短事务 CAS head/active；保存完整 snapshot manifest。通知只带身份与 revision。
3. 新调用读取实际 heads 与 RoleBinding，生成一致 PromptSnapshot。旧调用持有原快照；遇授权撤销仍由真实派发边界重新检查。
4. 无效模板不成为活动版本，管理页保留原 active 和本次诊断。对未保存的编辑文字，preview 直接返回语法/参数诊断。历史恢复以新修订保存旧内容，再显式激活。
5. `reset` 清除所选范围的 active 覆盖，恢复上层来源；保留历史与正在引用的快照。程序资源不被删除。

读取依赖闭包在 repeatable-read 事务取得一致视图后释放连接，当前授权和 example 渲染在事务外完成；真正变更的短事务锁住 head，再计算闭包摘要并核对，依赖改变则返回 dependencies_changed。事务内不另借连接调用异步授权。快照同样先读取一致闭包、核验当前来源授权，再保存不可变 manifest；render 每次重新核验所引用范围的当前权限。

本地 `.meta.json` 保存 `{promptId,locale,scope,baseRevision,digest}`。导出使用 write-file-atomic 写正文与 manifest；开启 watcher 后，文件变更按 manifest.baseRevision 调用同一 save+activate 操作。API 同时改过时返回 revision_conflict，并停止该 baseRevision 文件的自动激活；管理端可读取当前版本并重新导出。自身导出的同 digest 不重复建立修订。启动在 Chokidar ready 后使用 getWatched() 的初始目录清单核验各 manifest，停机编辑也走同一导入/CAS 流程。

Chokidar 用 `ignoreInitial:true, awaitWriteFinish:{stabilityThreshold:200,pollInterval:50}`，收到稳定变更再读取候选。新 snapshot 每次直接读 SQL heads；运行时不维护可变 head cache。单进程 subscribe 和 PG NOTIFY 只供管理刷新提示，丢通知后新调用仍读实际版本。导出文件失败显示“数据库已保存、编辑目录未同步”，允许重新导出；运行采用数据库版本。close 等待本地正在导入的任务后关闭 watcher。

## 逐模型上下文与实际消费

Prompt 规定职责，Nous contexts 给出本次可用认知；原生历史与工具结果由实际执行者持有。通用 models 通过产品注册的回调组合，不在共享 prompts 库中依赖 Nous Client。

contextHooks由产品按真实能力注册。独立Nous、memory-only和绑定Hept使用各自已供给领域；独立Hept可只用其种子/近期事实与正式角色输入。要求Nous长期认知的角色遇连接不可用时报告具体缺项；无该要求的调用不强制连接Nous，也不把旧Self副本当当前权威。

```ts
interface ModelContextHooks {
  prepare(ctx:CallContext,input:{
    snapshot:InvocationSnapshot;stepNumber:number;
    messages:ModelMessage[];tools:ToolSet;model:LanguageModel;
    inputRefs:readonly Ref[];
    baseInstructions:Instructions;referenceTime:CapturedTime;
    previousPreparation?:ModelPreparation;
  }):Promise<{instructions?:string;inputRefs:Ref[];contextRef?:Ref}>;
}
interface ModelPreparation {
  referenceTime:CapturedTime;
  contextRef?:Ref; // kind=ContextView，仅为准备元数据
  inputDigest?:string; // 实际 V4 params 的 SHA-256
}
```

此处 ModelContextHooks 是同进程组合接口，可按调用传受信闭包，也可由产品全局注册。输入 Ref 表示原调用已声明依赖；Hook 保存实际 messages 资料时以 source.inputs 继承这些依赖，正文仍来自实际 messages。实际输入/结果持久化与接纳由 ModelData.saveInput/saveOutput/adopt 执行。ContextView Ref 只保存在 preparation，不作为事实来源传入 inputRefs。跨产品使用正式生成Client的contexts/encounters合同；角色、工作目标、情况、真实当前材料和查询时间参考由对应owner提供。输入ref固定修订，选区仅在Ref.selector；已供给Self时其当前身份完整优先，memory-only不补造Self，其余材料遵守可访问性、用途、受众、认知立场和token预算。不能把被过滤正文放到preview/trace的普通可读位置。

SDK 7 的 prepareStep.messages 包括前步 assistant/tool 结果，而且返回的 messages 会延续到后续步骤。正式组合使用冻结 baseRoleInstructions 重建每步 instructions，并保留当前 step.messages：

```ts
const contribution = await hooks.prepare(ctx, {
  snapshot:actualStepSnapshot,stepNumber:step.stepNumber,
  messages:hostMessages ?? step.messages,tools:actualTools,model,
  inputRefs,baseInstructions,referenceTime,previousPreparation,
});
return {
  instructions:joinInstructions(baseInstructions,contribution.instructions),
  messages:hostMessages ?? step.messages,
};
```

baseInstructions 包括该实际步骤冻结的 PromptSnapshot 及宿主合法指令。新步骤重读 Role/Prompt，已有步骤恢复使用原 snapshot/preparation；previousPreparation 让宿主按当前权限重读原 ContextView，并沿原 referenceTime 组合。Hook 读取 snapshot.inference 中的实际 maxOutputTokens 计算本步预算。宿主已有消息变换、媒体和 Provider 不透明部分继续由原执行 owner 执行。在 wrapGenerate/wrapStream 的实际 V4 params 保存最终通用参数与准备元数据；Provider request.body 可得时另存实际请求。准备前线索、最终语义输入、wire 请求分字段关联。

宿主的模型选择、active tools和语义消息变换先完成，再运行该prepare。实际边界核对输入/来源与准备版本；后置middleware若改变事实输入，须回到负责的prepare位置重做认知与预算。Provider协议表示转换继续由SDK承担。完整历史保留每个原消息/工具结果/压缩结果的真实来源依赖；来源撤权后，不能只从新认知slot排除正文而继续把旧历史发送出去。原生harness在其历史/压缩owner排除受限材料并建立合法输入，再prepare；无法排除时暂停该调用。

每次实际输出与 usage 持久保全，再按同 invocationId 接纳实际 Encounter；原调用者途中撤权不丢失已发生的结果、费用与原时域终止回执，读取结果仍按当前权限。ContextView 存在仅表示准备，preview/read/query 均不构成实际接触。输出 source.inputs 关联实际 inputPortions，根使用真实来源身份；同一 session 文档的新版本不成为新的独立事实根。worker/author 成果留在可信 Consumer 私有范围；只经正式发布操作选择可见输出节点，向主体交付发布 Ref。node selector 使用共同 `{kind:'node',pointer:'/content/0/text'}`，不整体发布含隐藏推理或工具正文的原生记录。

实际doX派发前取得[时间owner](时间与调度.md)的observed TimeCaptureReceipt并保存到输入快照，Provider terminal取得输出formed捕获；成功/可确认消费后accept传这两份原receipt。not_sent不造Encounter，恢复不再取now改写原capture。worker输出的formed不充当主体日后查看成果的observed，主体消费另取自己的capture。跨产品receipt按已绑定ClockSource校验，模型正文不能自报捕获；recorded始终是本次真实落库时间。schema解析失败仍按真实输入消费保存Encounter，业务mutation是否采用另由领域判定。

OpenClaw 在已有本地改编的真实 prepare/dispatch/accept 责任处采用同合同：包括工具后续、辅助摘要、压缩和子代理；consumer 固定为宿主绑定的实际工作范围。模型输入原件、历史、工具执行和 workspace 权限保持原生 owner；不得为接认知再维护一套历史或工具循环。

## 接口、配置与管理

```ts
createPrompts({
  installationId,db,programRoot,overrideRoot,catalog,settings,authorize,
  processBootId?,watchContext?,onError?,
}):Prompts
prompts.initialize() // 校验全部程序资源/examples，并按设置启动编辑监视
prompts.describe(ctx,{owner?,scope?})
prompts.list(ctx,{scope,cursor?,limit?})
prompts.read(ctx,{promptId,locale,scope,revision?})
prompts.history(ctx,{promptId,locale,scope,cursor?,limit?})
prompts.save(ctx,{promptId,locale,scope,expectedRevision,text,reason?})
prompts.activate(ctx,{promptId,locale,scope,expectedRevision,revision})
prompts.reset(ctx,{promptId,locale,scope,expectedRevision})
prompts.preview(ctx,{binding,scope,params,unsavedText?})
prompts.snapshot(ctx,{binding,scope})
prompts.render(ctx,{snapshot:PromptSnapshotRef,params})
prompts.exportFile(ctx,{promptId,locale,scope})
prompts.watch(ctx?) // 或由组合根注入 watchContext，取得当次可信管理身份
prompts.subscribe(change=>{/* 管理刷新提示 */})
prompts.close()
```

共享库导出 promptsMigration、PromptDatabase 与 promptsDefinition，由产品组合注册到自己的数据库和 settings。authorize 接收 `{action,promptId?,scope}`，映射产品实际 operation；配置采用 registerConsumer.snapshot()，不要求业务消费者持有 settings.read 管理权。watchContext 只由可信组合提供，文件导入每次仍检查当前授权。

HTTP 目录为 `GET /v1/prompts/catalog`，列表/读取/历史为 `GET /v1/prompts`、`GET /v1/prompts/read`、`GET /v1/prompts/history`，写入为 `POST /v1/prompts`、`/v1/prompts/activate`、`/v1/prompts/reset`，输入直接使用包含promptId/locale/scope的正式owner Schema。预览和冻结快照分别为 `POST /v1/prompts/preview` 与 `POST /v1/prompts/snapshot`；查询中的scope保留deepObject身份。CLI 提供 prompts list/read/edit/preview/activate/reset，Web 使用共享管理组件。普通预览返回 `{persisted:true,text,bytes,snapshot}`；未保存文字返回 `{persisted:false,text,bytes,snapshot:null,draft:{digest,promptId,locale,dependencies,engine}}`，正文和参数不落库。token 估算归实际模型 owner，真实调用预览读取已保存 actualInputRef。

| 配置 | 范围与默认 | 生效 |
|---|---|---|
| locale | 安装/主体，默认 zh-CN；不存在时用 descriptor.defaultLocale | 新快照 |
| watch.enabled | 安装，false；overrideRoot 由 Paths.config/prompts 注入 | watcher 热生效，使用原路径安全检查 |
| limits.sourceBytes/closureBytes/outputBytes/closureCount | 安装，128/512/256 KiB、32个；主体只能收紧 | 新保存/快照；既有快照保留采用值 |
| limits.renderMs/memoryBytes | 安装100ms/1MiB；主体只能收紧 | 新快照 |
| active/locked Binding | RolePolicy；当前 active | 新调用；历史快照不变 |
| revision 保留 | 默认保留全部被调用/激活引用版本；未引用草稿90天 | data owner按策略清理 |
| preview 参数保留 | 默认不持久化临时参数 | 显式保存测试样例才写受限资料 |

模块 namespace 为 platform.prompts，consumerId 为 prompts.registry。基础 schema 没有 default；独立 promptsDefaults 与字段元信息注册在 settings，遵守[配置与生效](配置与生效.md)的稀疏覆盖规则。locale/limits 在实际读取配置后报告 applied，watch 在 watcher 真实启动/关闭后报告；启动失败报告 /watch 不可用。改 Prompt 不自动调用模型，模型测试由显式有预算操作触发。

## 失败、恢复与当前替换

语法错误、缺变量、无权限来源和预算不足在派发前返回具体 Problem。没有可用活动 Prompt 的角色不可执行，其他管理仍可用。持久输出后的 accept 失败复用已保存输出和原 invocation；已发生的模型调用不重做。流式取消、未知 Provider 效果及费用处理由 models/operations 统一负责。

迁入原15份 Nous 资源、Registry 和 Hept 五份职责文字；保留原职责规则，按当前 contracts 改字段。当前 `packages/nous/src/platform/models.ts` 的两句通用 Prompt 与固定单 user 消息替换逻辑删除；两个产品散落的角色字符串、重复文件加载、缓存失效、手写花括号渲染与假 preview 删除。新的领域 RoleDescriptor 只声明自己的 Prompt/参数/上下文要求，机械由共享库承担。

共享 Prompt 已用真实 PostgreSQL 18 验证原十五份英文全文预览、单连接池中会查询 SQL 的授权、并发激活 CAS、幂等回执、当前撤权、冻结历史、未保存预览不落库、主体覆盖与继承、真实 Chokidar 修改/冲突恢复及新实例导入停机编辑。路径越界 symlink、无效 UTF-8、大小限制、循环 partial 和缺参数会拒绝。带工具/媒体的两步调用及输出接纳恢复由模型/认知 owner 的纵切面验证。
