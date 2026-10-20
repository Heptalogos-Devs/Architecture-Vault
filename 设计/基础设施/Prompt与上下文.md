# Prompt 与上下文

## 采用与责任

Prompt 机械位于 `packages/platform/src/prompts/`，经 `@nous-wave/platform/prompts` 导出。它组合原 Nous PromptRegistry、LiquidJS 10.30.0、Chokidar 6 和 PostgreSQL 修订；两个产品分别实例化、分别持有自己的资源和数据。完整 Prompt 文字、参数 schema、认知读取与成功消费均归产品领域。通用库只负责资源、模板、修订、预览与快照。

直接迁入原 Nous `apps/nous-core/src/model/prompts.ts` 和完整 `prompts/`，保留 realpath 根限制、128 KiB 限制、UTF-8/非空校验、SHA-256 与 program/config 来源。原 Hept `role-prompts.ts` 的五个完整职责迁入 Hept 资源目录。移植 MaiBot PromptManager 与 WebUI 中元信息、参数检查、版本激活、回退和预览的完整流程，渲染用 LiquidJS 替换手写 Formatter。固定提交、具体文件与许可见[研究报告](../../研究/第三方模型Prompt与管理.md)。

模型派发与实际请求追踪见[模型供应与调用](模型供应与调用.md)；共同 Ref、OriginIdentity、TimePoint、CallContext、Problem 使用[共同值](共同值与调用上下文.md)。认知候选、来源校验和预算选择归 Nous contexts/query owner，见[检索服务与认知消费者](检索服务与认知消费者.md)。

## 资源目录与正式值

程序资源随产品发行，保留原分目录。每个产品导出静态 PromptCatalog，避免依赖文件 stem 猜身份；原 `memory/formation.md` 与 `self/formation.md` 必须有不同 PromptId。Prompt 的语言、管理界面语言与主体自然语言分别选择。

```text
Nous-Wave/prompts/zh-CN/memory/formation.md
Nous-Wave/prompts/zh-CN/self/formation.md
Nous-Wave/prompts/zh-CN/material/description.md
Heptalogos/prompts/zh-CN/subject/deliberation.md
Heptalogos/prompts/zh-CN/subject/expression.md
<Paths.config>/prompts/<locale>/<namespaced-id>.liquid
<Paths.config>/prompts/<locale>/<namespaced-id>.meta.json
```

```ts
const PromptIdSchema = z.string().regex(/^[a-z][a-z0-9_-]*(\.[a-z][a-z0-9_-]*)+$/);
const PromptScopeSchema = z.discriminatedUnion('kind',[
  z.object({kind:z.literal('installation'),installationId:InstallationIdSchema}),
  z.object({kind:z.literal('subject'),subjectId:SubjectIdSchema}),
]);
const PromptBindingSchema = z.object({
  promptId:PromptIdSchema,
  locale:z.string().min(1),
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
  source:'program'|'override'; revision?:number;
  catalogRevision:string; paramsSchemaRevision:string;
  dependencies:readonly {promptId:string;revision?:number;digest:string}[];
  engine:{name:'liquidjs';version:string;optionsDigest:string};
}
```

scope 表示覆盖所属产品范围。RolePolicy 在 settings 中保存 PromptBinding，允许安装默认、主体、职责选择；同一 Prompt 内容只在 prompts owner 保存一次。查找顺序为显式锁定修订、主体激活覆盖、安装激活覆盖、程序该语言、程序默认语言。返回实际 locale/source/revision；显式锁定失效或不兼容时返回错误，不静默改用其他文字。

上述仓库根prompts随产品打包到Paths.program下资源位置，实际路径由catalog/bootstrap注入；覆盖编辑根使用Paths.config。程序/编辑路径和其他逻辑根采用[安装规范](安装与生命周期.md)，不写死某台机器的data目录。请求scope的installationId仍须与当前受权实例一致。

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

参数准备先由领域异步读取完成，再交给纯 renderer。固定 partial 依赖由 catalog 允许名单及 LiquidJS 文件解析入口解析成闭包；候选激活前检查不存在、循环和超限。LiquidJS 实验性静态分析可给编辑器提示，正式参数合同与严格 render 决定是否可采用。模板展开的 ref、来源与策略是 params 之外的结构化元数据，原样跟随实际 ContextView，不从生成文本反向猜取。

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
  actor jsonb not null, recorded_at timestamptz(6) not null,
  unique(prompt_id,locale,scope_kind,scope_id,revision)
);
create table prompt_heads (
  prompt_id text not null, locale text not null,
  scope_kind text not null, scope_id text not null,
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

heads 对 revisions 建相同复合键外键，事务结束前保证 latest/active 引用存在。原件默认的 source/digest 在 manifest 中冻结；发行升级后历史调用仍能找到旧快照正文。内容采用 data owner 的压缩与保留机制；不再维护第三份自由变化的 Prompt 历史。

save/activate/reset先核验当前授权并查本owner的receipt：相同operation_id和规范请求digest返回原result，不先用旧expectedRevision拒绝成功重放；不同请求冲突。result包括保存/激活/恢复继承与no-op的原结果，在修改head的同一短事务保存。该表仅是Prompt正式幂等回执，不含运行步骤/租约。operation_id是稳定text key；复合save＋activate流程为两项真实操作分配稳定子key，文件导入也使用同合同。请求digest不混入重试时新取得的now/head/default。DBOS内步骤使用datasource，普通短写直接使用Kysely事务。

1. `save` 验证授权、expectedRevision、UTF-8/路径/体积、当前参数合同、模板语法和依赖。用声明 examples 运行同一 renderer，保存不可变候选修订并 CAS latest。保存默认不激活。
2. `activate` 校验 expectedRevision、候选及当时依赖闭包，在短事务 CAS active；保存完整 snapshot manifest。通知只带 ID/revision。
3. 新调用读取实际 heads 与 RoleBinding，生成一致 PromptSnapshot。旧调用持有原快照；遇授权撤销仍由真实派发边界重新检查。
4. 无效模板不成为活动版本，管理页保留原 active 和本次诊断。对未保存的编辑文字，preview 直接返回语法/参数诊断。历史恢复以新修订保存旧内容，再显式激活。
5. `reset` 清除所选范围的 active 覆盖，恢复上层来源；保留历史与正在引用的快照。程序资源不被删除。

本地 `.meta.json` 保存 `{promptId,locale,scope,baseRevision}`。导出按临时文件＋rename 写正文与 manifest；开启 watcher 后，文件变更按 manifest.baseRevision 调用同一 save+activate 操作。API 同时改过时返回 revision_conflict，在管理页显示文件内容与当前版本，停止该文件的自动激活。自身导出的同 digest 不重复建立修订。启动时先核对 manifest/数据库，不能用文件时间覆盖较新版本。

Chokidar 用 `ignoreInitial:true, awaitWriteFinish:{stabilityThreshold:200,pollInterval:50}`，收到稳定变更再读取候选；候选完整成功后替换 RegistrySnapshot。单进程通知直接失效；多进程用 PG LISTEN/NOTIFY，并在重连、调用边界重新核对 head。通知不是持久队列。导出文件失败显示“数据库已保存、编辑目录未同步”，允许重新导出；运行采用数据库版本。

## 逐模型上下文与实际消费

Prompt 规定职责，Nous contexts 给出本次可用认知；原生历史与工具结果由实际执行者持有。通用 models 通过产品注册的回调组合，不在共享 prompts 库中依赖 Nous Client。

contextHooks由产品按真实能力注册。独立Nous、memory-only和绑定Hept使用各自已供给领域；独立Hept可只用其种子/近期事实与正式角色输入。要求Nous长期认知的角色遇连接不可用时报告具体缺项；无该要求的调用不强制连接Nous，也不把旧Self副本当当前权威。

```ts
interface ContextHooks {
  prepare(ctx:CallContext,input:{
    invocationId:string; roleId:string; stepNumber:number;
    model:{resourceId:string;modelId:string;contextLimit:number};
    messages:readonly ModelMessage[]; // 同进程；原生边界用正式序列化合同
    instructions:Instructions|undefined;
    referenceTime:CapturedTime; // 查询参考，不构成实际观察
    latestMaterials:readonly Ref[];
    requiredSources:readonly Ref[];
    budget:{outputTokens:number;toolTokens:number;requiredTokens:number;
      mediaTokens?:number;cognitionTokens?:number};
  }):Promise<ContextContribution>;
  accept(ctx:CallContext,input:{
    invocationId:string;contextViewRef:Ref;outputRef:Ref;
    actualInputRef:Ref;status:'completed';
    observed:TimeCaptureReceipt;formed:TimeCaptureReceipt;
  }):Promise<void>;
}
interface ContextContribution {
  contextViewRef:Ref;
  instructions:string; // 已按该角色模板投影的本次认知 slot
  inputPortions:readonly {ref:Ref}[]; // 选区只位于共同Ref.selector
  estimatedTokens:number;
}
```

此处hooks是同进程组合接口。跨产品使用正式生成Client的contexts/encounters合同；角色、工作目标、情况、真实当前材料和查询时间参考由对应owner提供。输入ref固定修订，选区仅在Ref.selector；已供给Self时其当前身份完整优先，memory-only不补造Self，其余材料遵守可访问性、用途、受众、认知立场和token预算。不能把被过滤正文放到preview/trace的普通可读位置。

SDK 7 的 prepareStep.messages 包括前步 assistant/tool 结果，而且返回的 messages 会延续到后续步骤。正式组合使用冻结 baseRoleInstructions 重建每步 instructions，并保留当前 step.messages：

```ts
prepareStep: async step => {
  const cognition = await hooks.prepare(ctx, describeActualStep(step));
  stepContexts.set(step.stepNumber,cognition);
  return {
    instructions:joinInstructions(baseRoleInstructions,cognition.instructions),
    messages:step.messages,
  };
}
```

baseRoleInstructions 包括本次冻结 PromptSnapshot 及宿主合法指令；不能用 step.instructions 反复追加上一轮认知。宿主已有消息变换、媒体和 Provider 不透明部分继续由原执行 owner 执行。在 SDK onStepStart 保存 tools 转换后的语义输入，在 wrapGenerate/wrapStream 的实际 V4 params 保存最终通用参数；Provider request.body 可得时另存实际请求。准备前线索、最终语义输入、wire 请求分字段关联。

宿主的模型选择、active tools和语义消息变换先完成，再运行该prepare。实际边界核对输入/来源与准备版本；后置middleware若改变事实输入，须回到负责的prepare位置重做认知与预算。Provider协议表示转换继续由SDK承担。完整历史保留每个原消息/工具结果/压缩结果的真实来源依赖；来源撤权后，不能只从新认知slot排除正文而继续把旧历史发送出去。原生harness在其历史/压缩owner排除受限材料并建立合法输入，再prepare；无法排除时暂停该调用。

每次成功输出先持久，再按同 invocationId 接纳实际 Encounter。ContextView 存在仅表示准备，preview/read/query 均不构成实际接触。输出 source.inputs 关联实际 inputPortions，根使用真实来源身份；同一 session 文档的新版本不成为新的独立事实根。worker/author 成果留在可信 Consumer 私有范围；只经正式发布操作选择可见输出节点，向主体交付发布 Ref。node selector 使用共同 `{kind:'node',pointer:'/content/0/text'}`，不整体发布含隐藏推理或工具正文的原生记录。

实际doX派发前取得[时间owner](时间与调度.md)的observed TimeCaptureReceipt并保存到输入快照，Provider terminal取得输出formed捕获；成功/可确认消费后accept传这两份原receipt。not_sent不造Encounter，恢复不再取now改写原capture。worker输出的formed不充当主体日后查看成果的observed，主体消费另取自己的capture。跨产品receipt按已绑定ClockSource校验，模型正文不能自报捕获；recorded始终是本次真实落库时间。schema解析失败仍按真实输入消费保存Encounter，业务mutation是否采用另由领域判定。

OpenClaw 在已有本地改编的真实 prepare/dispatch/accept 责任处采用同合同：包括工具后续、辅助摘要、压缩和子代理；consumer 固定为宿主绑定的实际工作范围。模型输入原件、历史、工具执行和 workspace 权限保持原生 owner；不得为接认知再维护一套历史或工具循环。

## 接口、配置与管理

```ts
createPrompts({catalog,settings,data,clock,authorize,notifications}):Prompts
prompts.describe(ctx,{owner?,scope?})
prompts.list(ctx,{scope,cursor?,limit?})
prompts.read(ctx,{promptId,locale,scope,revision?})
prompts.save(ctx,{promptId,locale,scope,expectedRevision,text,reason?})
prompts.activate(ctx,{promptId,locale,scope,expectedRevision,revision})
prompts.reset(ctx,{promptId,locale,scope,expectedRevision})
prompts.preview(ctx,{binding,scope,params,unsavedText?})
prompts.snapshot(ctx,{binding,scope})
```

HTTP目录为`GET /v1/prompts/catalog`，列表/读取为`GET /v1/prompts`与`GET /v1/prompts/{id}`，写入为`POST /v1/prompts/{id}/revisions`、`/{id}/activate`、`/{id}/reset`。预览和冻结快照分别为`POST /v1/prompts/preview`与`POST /v1/prompts/snapshot`；不在id下再提供preview别名。ID按一个完整segment编码。CLI提供prompts list/read/edit/preview/activate/reset；Web采用AstrBot编辑器/角色能力表单和MaiBot版本/参数/预览交互。预览返回blocks/text、snapshot、来源、参数校验、体积和token估计方法；真实调用预览从已保存actualInputRef读取，不重跑已变化模板。

| 配置 | 范围与默认 | 生效 |
|---|---|---|
| locale/fallback | 安装默认 zh-CN；领域可声明其他默认语言 | 新快照 |
| watch.enabled / root | 安装，false；root 为 `Paths.config/prompts` | watcher 重载，使用原路径安全检查 |
| source/closure/output 限额 | 安装，128/512/256 KiB；依赖32个 | 新保存/渲染；主体只能收紧 |
| renderLimit | 安装100ms；职责可收紧 | 下次 render |
| active/locked Binding | RolePolicy；当前 active | 新调用；历史快照不变 |
| revision 保留 | 默认保留全部被调用/激活引用版本；未引用草稿90天 | data owner按策略清理 |
| preview 参数保留 | 默认不持久化临时参数 | 显式保存测试样例才写受限资料 |

所有 schema/defaults 注册在 settings，遵守[配置与生效](配置与生效.md)的稀疏覆盖规则。改 Prompt 不自动调用模型；模型测试由显式有预算操作触发。

## 失败、恢复与当前替换

语法错误、缺变量、无权限来源和预算不足在派发前返回具体 Problem。没有可用活动 Prompt 的角色不可执行，其他管理仍可用。持久输出后的 accept 失败复用已保存输出和原 invocation；已发生的模型调用不重做。流式取消、未知 Provider 效果及费用处理由 models/operations 统一负责。

迁入原15份 Nous 资源、Registry 和 Hept 五份职责文字；保留原职责规则，按当前 contracts 改字段。当前 `packages/nous/src/platform/models.ts` 的两句通用 Prompt 与固定单 user 消息替换逻辑删除；两个产品散落的角色字符串、重复文件加载、缓存失效、手写花括号渲染与假 preview 删除。新的领域 RoleDescriptor 只声明自己的 Prompt/参数/上下文要求，机械由共享库承担。

复用三个场景：完整原资源预览；API/本地编辑和并发冲突后新调用采用正确版本；带工具结果的两步调用保留媒体与历史且每步认知不同。规则测试保留路径越界、默认值不污染覆盖、无效激活保留旧版、成功输出恢复只接纳一次和私有成果选区发布。
