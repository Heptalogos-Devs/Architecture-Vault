# API、CLI、SDK 与 i18n

## 一个 owner，多种入口

领域方法与 Zod contracts 是业务权威。HTTP、生成 SDK、CLI、Web、MCP 和原生接入分别负责认证上下文、传输与呈现，调用相同 owner 方法；每个入口保留完整的类型、修订、来源、时间、权限、失败与恢复含义。同进程直接调用正式 owner，跨产品使用正式 SDK。

公共值采用[共同值与调用上下文](共同值与调用上下文.md)，认证和当前授权采用[身份权限与密钥](身份权限与密钥.md)，长工作与实际效果由 DBOS/operations 和各领域持有。根操作目录列出全部正式能力，本规范规定它们如何一致地成为可用入口。

通用 HTTP 采用 Fastify 5.12.5、fastify-type-provider-zod 7.0.0、Zod4 与 `@fastify/swagger`，静态注册明确路由。客户端采用官方 OpenAPI Generator 7.26.0 的 typescript-fetch。上游入口、当前已安装源码和生成实测是版本依据；原 HeyAPI 对 TS compiler AST 的依赖在 TS7 失败，替换生成 owner，不安装第二套 TS。

## 合同、路由和 OpenAPI

```text
packages/contracts/src/common.ts             # 纯共同值
packages/contracts/src/<domain>.ts           # 各领域公开schema/type
apps/server/src/routes/<domain>.ts          # 明确method/path/operationId/handler
packages/contracts/openapi/<product>.json  # 从实际路由生成
packages/client/src/generated/              # 官方generator产物
packages/client/src/{client,problem,streams}.ts
apps/cli/src/commands/<owner>.ts
```

每份公开 schema 标明真实拥有者；可复用递归/联合类型以稳定 ID 注册到 Zod registry。request、response、Problem、分页和二进制说明都进入正式 OpenAPI。JSON Schema 转换直接用库的 `createJsonSchemaTransform`、`createJsonSchemaTransformObject`，target 为 `openapi-3.0`，文档版本为 **3.0.3**；不写另一个 schema 转换器。

```ts
const server = Fastify(hostOptions).withTypeProvider<ZodTypeProvider>();
server.setValidatorCompiler(validatorCompiler);
server.setSerializerCompiler(serializerCompiler);
await server.register(swagger,{
  openapi:{openapi:'3.0.3',info:{title:productName,version}},
  transform:createJsonSchemaTransform({zodToJsonConfig:{target:'openapi-3.0'}}),
  transformObject:createJsonSchemaTransformObject({
    zodToJsonConfig:{target:'openapi-3.0'},
  }),
});
server.post('/v1/subjects/:subjectId/query/run',{
  schema:{operationId:'queryRun',tags:['Query'],
    params:SubjectPathSchema,body:QueryRunSchema,
    response:{200:QueryResultSchema,400:ProblemSchema,403:ProblemSchema,
      409:ProblemSchema,503:ProblemSchema}},
},async request => query.run(await trustedContext(request),request.body));
```

这是明确路由到真实 query owner 的例子，授权边界仍由具体方法和真实资源派发检查。`query.prepare/run/expand/explain` 是唯一公开查询操作组，参见[NousQL](../NousQL与检索合同.md)。各 Memory/Concept/Self/Social/Motivation 等领域持有自己的创建/修订/合并/采用操作；删除旧 `knowledge.query/create/revise` 通用转发入口及其消费者。

schema-only 生成只实例化 Fastify 路由/合同，不连接数据库、启动 DBOS、解析秘密、启用 Subject 或探测模型。生成器不会创建一个可作为正式服务运行的“关闭认证模式”。正常 Host 的业务 handler 始终有真实 factory/认证。

模型管理固定使用`/v1/model-providers`、`/v1/models`、`/v1/roles`、`/v1/model-invocations`；原生调用prepare为`/v1/model-invocations/native/prepare`，dispatch/completion为`/v1/model-invocations/{id}/dispatch`与`/{id}/completion`。tags/operationId、SDK和所有管理消费者同形，删除旧嵌套别名。

日期与微秒时间在合同中是字符串，Money/数量是精确十进制字符串，Ref/OriginIdentity 保持不同命名类型。OpenAPI 的 nullable、递归 `$ref`、discriminator、additionalProperties 和可选字段按3.0.3导出；生成后验证这些具体形状与序列化结果。JSON object/array 不塞成 `content:string` 规避生成问题。

## 生成与普通发行包

官方 Generator 使用固定 `v7.26.0` JAR 或容器制品。开发缓存与产物试验进入工作区 temp，具体下载由明确 acquire/generate 命令完成；普通运行不下载 generator。Java/JAR 为开发生成依赖，不进入 Node 客户端运行闭包。

```text
openapi-generator generate
  -i packages/contracts/openapi/nous.json
  -g typescript-fetch
  -o packages/client/src/generated
  --additional-properties importFileExtension=.js,dateLibrary=string,
    withoutRuntimeChecks=true,hideGenerationTimestamp=true
```

调用由脚本使用参数数组传给正式 generator。`dateLibrary=string` 是官方 typescript-fetch 选项，保留原始时间字符串；`.js` 相对导入用于 ESM，关闭时间戳使产物确定。参见[官方选项](https://openapi-generator.tech/docs/generators/typescript-fetch/)及[固定版本实现](https://github.com/OpenAPITools/openapi-generator/blob/v7.26.0/modules/openapi-generator/src/main/java/org/openapitools/codegen/languages/TypeScriptFetchClientCodegen.java)。生成 API 使用稳定 tags 与 operationId，避免整个产品堆成一个匿名 DefaultApi。

| 普通包 | 内容与 export | 运行依赖边界 |
|---|---|---|
| `@nous-wave/contracts` / Hept contracts | `./common`、各领域 schema/type 与纯描述值 | Zod与纯值；浏览器可用，无pg/fs/Node模块 |
| `@nous-wave/client` / Hept client | 生成 APIs/models/runtime，安全 Problem 适配、标准流与必要便利方法 | WHATWG fetch/streams；服务凭据与浏览器session分别配置 |
| `@nous-wave/platform` | bootstrap/settings/credentials/network/models/prompts/storage/operations/telemetry/time/data等独立入口 | 普通库，各产品独立实例；子入口只装载自身所需能力 |
| `@nous-wave/management-ui` | AstrBot改编通用Vue/Vuetify组件与composables | Vue/Vuetify peers、纯contracts和传入Client；独立AGPL来源/许可 |
| 产品主库/应用 | 自己的factory、领域、HTTP、CLI、Web和迁移 | 本产品数据库与配置；Hept经正式版本依赖Nous公共包 |

生产 `exports` 指向包内编译 JS 与 d.ts；package.json 的 files 包含真实dist与必要资源。使用正常 pack/publish 生成版本 tarball，不引用相邻仓库、temp/data路径或开发 `.ts`。源码中的 workspace 依赖通过包管理器正式打包重写为版本；安装到空目录后可独立 import/run。`platform/models/contracts` 等纯 schema 子入口不得先从根 barrel 引入凭据或数据库代码。

platform直接复制Hept AGPL源码，整体按AGPL-3.0-only发行，保留原Nous Apache与其他第三方来源；组合产品采用相容AGPL。没有Hept源码的纯contracts/client可独立Apache发行，management-ui保留其独立AGPL归属。各包源码/资源/许可随正常制品保全，不以共同目录位置推定所有文件许可相同。

生成产物只由生成命令维护；手写便利方法调用生成 API/同一公开路径，不再提供任意 `request<T>` 作为所有正式能力的唯一实现。二进制、SSE与需要原始 Response 的调用可使用生成 API 的 Raw 响应入口，必要薄适配也复用其 fetch 配置、授权与Problem解析。

## 调用、身份、幂等与错误

浏览器用每产品自己的 Better Auth 用户 session、cookie prefix、trustedOrigins 与 CORS；跨产品联合管理显式建立两个登录态。服务 SDK 从受限凭据取得 bearer，绝不下发到普通浏览器。Node SDK 可注入 `network.client(...).fetch`，浏览器用标准 fetch 与所需 credentials；不另造万能代理或第三认证服务。

公开业务 body 只接受该操作数据，不接受可自选 Actor/grants。服务端从账号/API key 实际 ID与委派创建 CallContext。caller 可请求已授权范围内的 purpose/audience；Subject/Consumer/目标仍由当前委派与业务绑定核验。traceparent、idempotency-key 是关联/幂等身份，不授予权限。

| Header/值 | 语义 |
|---|---|
| `Authorization` / session cookie | 成熟认证机制；日志不输出 |
| `traceparent` | 标准W3C关联；host建立当前trace，拒绝非法格式 |
| `idempotency-key` | 需要幂等的写操作稳定submission身份；同身份不同规范输入conflict |
| `x-purpose` / `x-audience` | 请求范围；服务端只采纳当前授权允许值，audience使用共同scope IDs |
| `Accept-Language` | 管理呈现偏好；不改变业务内容/Prompt/主体语言 |
| expectedRevision | 所属owner的body CAS字段；不再提供第二套If-Match修改语义 |

写操作按所属owner保存submission结果与规范输入hash。普通短写由Kysely业务事务原子提交；只有在DBOS workflow中执行的采用步骤才使用官方datasource同时提交业务与该checkpoint。外部派发使用同一个正式operation/稳定身份，unknown时核实原调用；HTTP/SDK/CLI不通过“再发一次POST”提供隐式恢复。网络重连、认证刷新或页面重开不得生成新的业务submission来规避原结果。

错误返回共同 Problem，`Content-Type:application/problem+json`。HTTP状态保留语义，主要使用400输入、401认证、403权限、404可披露不存在、409修订/状态冲突、422领域输入、429资源/预算限制、503实际依赖不可用；具体status由owner Problem给出。不要将所有异常压成HTTP500或把空数组冒充失败。

SDK只将校验成功的 Problem 包进 `ProblemError`，保留 code/category/messageKey/args/retry/operationId/traceId；未知响应保存安全status/关联ID并报告传输错误。禁止 `Object.assign(new Error(), untrustedJson)` 扩展任意远端字段。普通日志不直接打印 SDK/DBOS 原 Error 或正文，自由文本与受限原始诊断依[模型错误边界](模型供应与调用.md#53-provider-错误的保存边界)和诊断数据owner处理。

分页统一 `{items,nextCursor?}`，游标由owner绑定Subject/consumer/权限范围、过滤、排序和读视图；下一页仍检查当前权限。默认50、上限200，特殊大量检索预算由正式领域合同声明。结果上限、截断、索引水位和partial coverage是显式字段；不返回伪造完整总数。

## 长工作、等待、流与取消

同步读取和短事务直接返回结果；有外部资源/持续进度的正式工作返回 `202 + OperationRef`。查询操作可以按领域合同等待当前工作，仍保留相同operation身份；UI、CLI与SDK均能立即显示已接纳的ID。

```ts
client.operations.inspect({operationId,signal?})
client.operations.events({operationId,after?,signal?}) // AsyncIterable<OperationEvent>
client.operations.wait({operationId,signal?})
client.operations.cancel({operationId,reason,submissionId})
```

OperationEvent 的业务状态/进度取自DBOS与真实领域记录。HTTP `GET /v1/operations/{id}/events` 用SSE，id为owner已保存变化的opaque游标，event为状态/进度/Problem/结束；不为SSE建立第二队列、日志数据库或持久outbox。心跳无业务event身份。断线从Last-Event-ID续接；保留范围有缺口时返回当前快照和reset信息，客户端重新读取，不把漏过的进度补造为事实。

SDK流解析直接用成熟 `eventsource-parser` 和Web Streams；保留标准Response、取消与背压，避免先arrayBuffer全部内容。订阅断开/AbortSignal仅终止本次等待；真正取消调用 `operations.cancel`，由owner检查是否可取消、停新接纳并保存真实结果。已派发外部效果的 unknown/accepted 不随用户取消被改为not_sent。CLI `--wait` 是相同SDK等待，Ctrl-C结束等待；`operations cancel`才提交业务取消。

模型文字流保留SDK现有stream parts；工具、usage、warning与最终结果关联同一调用。视频/音频/附件使用二进制上传/下载与正式Blob/Material Ref，不塞入控制JSON的base64字段。SDK便利方法在原生Request/FormData/流上构造必要headers；Content-Length/断点范围/下载有效期由真实存储owner合同决定。

## CLI：完整基础操作与离线范围

CLI采用Commander，交互引导使用Clack；原Hept lockfile已使用Commander15.0.0与`@clack/prompts`1.7.0。复制原CLI真实命令组织、参数读取与错误出口后改接正式SDK；选定版本由lockfile固定。正常命令都有 `--help`、稳定 `--json`、可传入JSON/标准输入/文件的结构化参数，适合人和脚本。

全局选择包括 `--endpoint`、`--installation`、`--subject`、`--locale`、`--json`、`--wait`；不从当前目录隐式取得其他主体权限。credential用OS/keyring/受保护locator引用或受控stdin，不使用shell历史中明文参数。Clack向导只负责收集明确输入并调用同一命令方法，非TTY不弹交互。

| 组 | 基础操作与真实owner |
|---|---|
| `status / operations / diagnostics` | 总体与分项状态、inspect/list/wait/cancel/reconcile、受限trace/Artifact读取 |
| `auth / delegations / secrets` | 登录/登出/session、受限服务委派、SecretRef状态/创建/轮换/撤销；读取不返回秘密 |
| `settings / models / prompts / network` | describe/get/change/reset/history/restore；资源与Role管理；预览/激活/测试/调用；网络profile/probe |
| `subjects / capabilities` | 创建/绑定/供给/启动/暂停/继续/停止、依赖与实际可用性 |
| Nous `query` | prepare/run/expand/explain；文本NousQL/完整结构化输入、历史时间/域/来源、LexicalRef/result目录续读 |
| Nous `materials / resources / contexts / encounters / work-contexts` | 保全原件/区域、读取/派生/发布、来源展开；当前工作与逐调用准备/实际消费 |
| Nous 领域组 | identity/entities/concepts/memories/schemas/episodes/journals/self/social/motivation的各正式list/read/history及所属修改/形成/合并操作 |
| Nous `retrieval / growth` | 资产/空间/算法profile、更新/重建/回收；形成/维护进度和实际结果 |
| Hept `worlds / clocks / calendar / life / attention` | 世界/时间映射与历史、日历/活动/生活策略、状态与注意材料；调用各领域操作 |
| Hept `pursuits / tasks / commitments` | 正式目标/Task/承诺管理、原生run检查/成果查看/继续/取消、预算与履行事实 |
| Hept `conversations / messages / expressions / effects` | 本地收件、完整parts/修订/反馈、自然表达、逐物理回执、unknown核实 |
| `extensions / tools / mcp / skills` | 目录/安装/启停/重载/权限/资源测试；原生能力委托真实owner |
| `data / backup` | manifest/检查/导出/导入/恢复/分叉/清除范围与pending，进度与实际下载 |

表中组是正式操作目录的CLI组织；不通过“任意kind＋任意JSON”实现领域写入。子命令参数由相应公开schema约束，help显示输入范围、默认值与所需scope。尚未供给的能力显示具体状态，不能用一个通用noop宣称命令已完整。

离线命令只组合本机Bootstrap/Service/Runtime/Recovery能力：

| 离线组 | 可用范围 |
|---|---|
| `init / bootstrap inspect/configure / doctor` | 目录/locator/依赖与引导、首次管理员；主HTTP不可用时仍可执行 |
| `runtime list/acquire/inspect` | 显式取得已选Node/PG/FFmpeg/OpenClaw等正式制品、版本/平台/来源校验 |
| `service install/start/stop/status/uninstall` | 受权OS服务操作，采用systemd/SCM/Shawl/launchd |
| `recovery inspect/reset-administrator/revoke-credential/rotate-signing-secret/restore-backup/repair-locator` | 真实本机Recovery证明下的有限恢复；不要求模型在线 |

离线模式不绕过HTTP授权直接写Memory/World表，也不把服务bearer视作OS shell权限。服务与恢复具体流程见[安装与生命周期](安装与生命周期.md)、[身份权限与密钥](身份权限与密钥.md)。原生整安装backup/restore由OpenClaw已有backup owner承担；单主体范围使用[数据规范](数据生命周期与发行.md#原生资料的真实owner)中需要建设的native.data窄操作，不将其描述为上游已提供的sessions.export。

机器输出成功写stdout，错误Problem写stderr；日志/进度不污染JSON。固定exit code为0成功、2输入、3认证/权限、4依赖/资源不可用、5待核实外部效果、1其他失败，SIGINT为130。异步接纳成功可退出0并带OperationRef/实际状态；`--wait` 采用最终实际结果。普通read成功展示unknown仍是读取成功；请求执行收到effect_unknown Problem则退出5。

## MCP：正式业务子集

MCP服务直接依赖`@modelcontextprotocol/sdk`（已采用OpenClaw固定依赖1.32.0），使用官方Server、request schemas、stdio/StreamableHTTP transport和取消/进度。参考复制OpenClaw `src/mcp/tools-stdio-server.ts` 的Server/handler/关闭收尾组织，替换其工具表与宿主依赖；协议、JSON-RPC、连接管理沿用SDK。

默认提供获准的查询与阅读业务子集：query.prepare/run/expand/explain、领域目录/精确read/history、材料区域/来源、当前工作Context、操作状态与等待。输出保留正式Ref、LexicalRef、结果目录、时间、认识立场、来源、coverage与Problem；structuredContent使用相同业务结果，text只是适合模型阅读的呈现。MCP inputSchema从同一公开Zod输入生成，不维护另一套“简化记忆搜索”语义。

允许的写工具来自明确的业务operation allowlist与当前委派，按原子业务操作逐项注册；不暴露任意SQL、generic knowledge write、System/Machine万能工具或可由参数选择的Actor。MCP服务连接上下文绑定真实Subject/consumer/purpose/audience，工具参数只能请求获准范围。列目录可过滤当前不可见项，执行和每次外部dispatch仍重新授权。

MCP resources/templates以正式对象/目录为可读入口，URI映射到真实Ref/owner方法；分页、选区、历史与当前权限保持原样。读取URI不授予资料访问；query结果中的 `result:N` 继续由当前结果目录解析，不把N当全局对象ID。MCP Server提供的Prompt为明确可选帮助，不覆盖主体身份或宿主授权。

stdio stdout仅协议，日志走stderr；HTTP使用正常认证/授权与正式网络入口。断开取消等待/未接纳工作，已接纳的业务仍由其owner保存并按原operation查询。对会引发实际模型/工具/发送的操作，预算和unknown处理与HTTP一致。MCP客户端管理见[管理呈现与扩展](管理呈现与扩展.md#toolsmcp-与-skills)。

## 语言资源与呈现

Web沿用复制组件现有vue-i18n；CLI/服务回退文案采用i18next。统一稳定语义key、参数名与语言目录，界面文字不散落在handler/错误分支。通用组件的key在management-ui命名空间，平台与产品领域分别拥有自己的命名空间。

```text
resources/locales/zh-CN/common.json
resources/locales/zh-CN/platform.models.json
resources/locales/zh-CN/platform.prompts.json
resources/locales/zh-CN/nous.query.json
resources/locales/zh-CN/hept.communication.json
resources/locales/en-US/...
```

```json
{
  "settings.revision_conflict": "设置已更新，当前版本为 {revision}",
  "models.invocation_unknown": "调用结果待核实：{invocationId}",
  "prompts.source.program": "程序默认",
  "operations.waiting": "等待 {operationId}"
}
```

共同文案使用两引擎都可配置的命名变量子集：Vue默认`{name}`，i18next设置interpolation prefix/suffix为`{`/`}`。语言文件使用完整稳定key的flat JSON，同locale合并时拒绝重名；Vue用flatJson解析，i18next设keySeparator:false。关闭字符串HTML转义后由Vue文本节点/CLI普通输出呈现，禁止将翻译后的远端参数直接v-html。复杂复数/性别在各端的成熟引擎资源中表达，保留同一语义key与参数合同；不手写模板/语言解析器。日期、数字、币种与复数规则使用Intl及所用i18n库，服务合同时间/Money不随显示locale改变。

i18next保留 `skipOnVariables:true`，插入的远端参数不再解释成嵌套翻译；参数只给该key声明的名称。相关能力直接使用[官方interpolation选项](https://www.i18next.com/translation-function/interpolation)、[keySeparator配置](https://www.i18next.com/overview/configuration-options)和[Vue flatJson](https://vue-i18n.intlify.dev/api/general.html#flatjson)。

默认界面zh-CN，支持en-US回退资源；语言tag以Intl标准规范化。顺序为当前用户偏好、Accept-Language/CLI locale、产品默认；缺key返回同key的默认语言与安全Problem.message。字段labelKey/descriptionKey、Role/Prompt元信息、Problem.messageKey和CLI help从所属owner资源发布，不能把自由错误文本当可稳定匹配的key。

UI语言、Prompt locale、Subject自然语言与世界/会话语言分别保存。修改管理语言不改Prompt或主体的说话习惯；表达语言来自身份、实际交往、语言认知与领域选择。模型输出、原消息、人物名称和资料正文不自动机器翻译；有翻译能力时作为明确派生资料保存来源与实际调用。

语言资源随代码/Prompt发行并有版本，服务Problem携带稳定key/args与安全fallback，浏览器可独立更新翻译。普通运行无需请求模型翻译管理页。动态schema字段必须有默认语言key；构建检查声明key和默认资源存在，翻译遗漏可在管理诊断中定位。

## 迁入、替换与检查

保留当前Fastify/Zod/OpenAPI3.0.3静态注册与官方Generator7.26生成成果，按真实领域目录重组路由和tags。替换HeyAPI compiler-API生成路径、默认单DefaultApi、公开任意request泛型包装、硬编码错误文本和两份不一致schema。NousQL/领域具体合同迁移时同步HTTP/SDK/CLI/MCP/UI当前消费者，删除旧通用knowledge写入和查询旁路。

原CLI的路径、参数和明确离线能力先迁入，再接Commander/Clack与正式Client。AstrBot i18n、对话历史、表单和SSE交互按完整功能组复制；删除旧端点/生成器/客户端和重叠网络封装。复用库版本、代码源/许可与实际改编列表进入发行清单，普通包各自保有必要许可。

完整验收使用少量路径：空目录安装SDK产物并按两个真实账号连接独立产品；从CLI/MCP/Web执行同一NousQL、来源续读和一次有修订冲突的领域操作；长工作断线续接/取消等待/显式业务取消；主HTTP不可用时本机doctor和有限恢复；切换界面语言仍保留微秒时间、Money与Prompt语言。必要规则检查覆盖公开schema/生成一致、Error安全边界、幂等冲突、未知不重发、纯contracts入口、运行产物无相邻源码依赖与默认翻译key完整。
