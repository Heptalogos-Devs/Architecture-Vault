# 第三方模型、Prompt 与管理设施

> 历史源码调查：其中的旧实现方案与施工选择属于当时背景。现行架构见[整体架构](../设计/整体架构与模块合同.md)。


研究日期：2026-10-20。本文为本轮源码研究与采用决策，需求依据是项目宪纲及用户当前修正。AstrBot 用于管理设施与界面复用，Hept 自己承载产品；OpenClaw 按实际能力模块采用。旧分支、旧提示词和已有改编均是研究材料。

## 1. 采用结论

1. **直接迁入原 Nous Prompt 资源与 Registry**，保留按职责分文件、程序资源与配置覆盖根、内容 digest、路径与体积检查。补齐版本、预览与热生效，删除当前重建中代替全部职责的两句通用提示。
2. **通用模板渲染选 LiquidJS，文件观察选 Chokidar，修订与激活记录使用已有 PostgreSQL。** MaiBot 的完整覆盖、参数检查、版本激活和调用预览流程作为改编依据；使用成熟引擎替换它的手写 Formatter、递归与花括号转义机械。
3. **模型访问直接用 AI SDK 7 的 Provider Registry 与各能力 API。** 产品只维护资源、职责、选择策略、权限、预算及实际调用记录；Provider 的协议、流解析与能力专有参数交给 SDK。文字、嵌入、重排、ASR/TTS 分别在其真实 Provider 方法边界计量。
4. **实际复制改编 MaiBot 的 FocusModeManager 与 MaisakaExpressionSelector 模块。** 保留焦点、跨会话事件、冷却、表达范围和候选选择，替换其配置、数据库、时钟、会话和模型执行依赖。Hept 不需要为了这两个模块常驻整个 MaiBot。
5. **管理前端采用 Vue 3＋Vuetify，复制 AstrBot 已有管理功能组件及依赖闭包。** 配置、Provider、Persona 能力、插件、工具、MCP、历史、日志与备份继续作为完整可用功能；API 调用改接我们拥有的正式服务。FastAPI 路由和服务组织也按完整功能流程搬用、改编，不将 AstrBotCoreLifecycle 引入 Hept。
6. **OpenClaw 优先采用它已有的包与能力责任模块。** `@openclaw/agent-core` 和 `@openclaw/llm-core` 在固定版本是 private workspace 包，需要形成明确的源码依赖制品；文件/进程工具、Skills 与沙箱也有真实宿主依赖。不能把“可复用源码”写成已存在的独立 npm SDK，更不应为一个工具任务默认携带 Gateway、渠道、控制台及全部插件构建。
7. **通用机械只维护一个普通共享库。** `@nous-wave/platform/*`在Nous仓提供bootstrap/settings/credentials/network/models/prompts/storage/operations/telemetry/time/data等独立入口，两产品独立factory/数据库；Hept用正式版本依赖。通用Vue组件另发`@nous-wave/management-ui`，保留独立AGPL许可，领域页面归各`apps/web/`。

本轮选择主要保留 TypeScript 服务与现有 Node 依赖。MaiBot 小模块移植进真实业务 owner，AstrBot Vue 功能在前端直接改编。Python 保留给已经采用、具有实质独立价值的成熟依赖；不为转发一个状态管理器另起 Python 全框架服务。

## 2. 固定来源与许可证

| 来源 | 固定版本或提交 | 本地位置 | 许可与采用边界 |
| --- | --- | --- | --- |
| 原 Nous | `412b062082afb75ccfae4c3f69fc606d3e3cc862` | `temp/spec-research/nous-original` | 原 Prompt Registry 标明 Apache-2.0；自有源码直接迁入 |
| 原 Hept | `21f0080460f3ee639deb9f5ea47282fb6c59df95` | `Heptalogos origin/master` | role-prompts 标明 AGPL-3.0-only；职责文字与网络实现均按源码核查 |
| MaiBot main | `ff0fe42500f5f7581e9655d1e78379407233207a` | `temp/spec-research/MaiBot` | 整仓 GPL-3.0；`src/llm_models/LICENSE` 另为 MIT，须按实际复制目录分别保留来源与许可 |
| AstrBot | `fc6b326fc9012873c4adc0183256c90d34a3d912`，4.29.1 | 现有 `Nous-Wave/data/upstream/AstrBot` | AGPL-3.0；管理/API/UI 以此提交为基准。当前本地 `347b2a3…` 只额外改了物理发送回执 |
| OpenClaw | `1b58cb9a1b4f4353e1add63c8506db4d890962e8`，v2026.10.5 | 现有 `Nous-Wave/data/upstream/openclaw` | MIT；本地 `ec69b550…` 及后续未提交接纳改编单独列为本项目实验，不能冒充上游合同 |
| AI SDK | `ai@7.0.146`，tag commit `0a5c786ef65bcd835328fb543685f6d8ef233dae` | 已安装 `ai/src` 与 `@ai-sdk/provider/src` | Apache-2.0；直接依赖正式 Provider 与模型接口 |
| LiquidJS／Handlebars／Chokidar | npm 元数据核对为 10.30.0／4.7.10／6.0.0 | 元数据缓存仅在 `temp/spec-research/npm-cache` | 均为 MIT；本轮选 LiquidJS＋Chokidar，未安装新生产依赖 |
| Cordis | 原 Hept lockfile 与研究探针固定 `4.0.0-rc.8` | `temp/spec-research/platform-probes/node_modules/cordis` | MIT；直接用 Context/Fiber/Effect，移除自有通用生命周期包装 |
| AI SDK MCP | `@ai-sdk/mcp@2.0.80` | `temp/spec-research/ai-sdk-mcp-2.0.80/package/src` | Apache-2.0；正式 HTTP/SSE 客户端与 tools 转换，stdio 当前仍是 Experimental 导出 |

上述路径都以 `/home/arsvine/Dev/Heptalogos-Devs/` 为根。新增研究源码与缓存统一放在 `temp/spec-research/`。本轮没有运行付费模型或大型构建。

主源码：[MaiBot](https://github.com/Mai-with-u/MaiBot/tree/ff0fe42500f5f7581e9655d1e78379407233207a)、[AstrBot](https://github.com/AstrBotDevs/AstrBot/tree/fc6b326fc9012873c4adc0183256c90d34a3d912)、[OpenClaw](https://github.com/openclaw/openclaw/tree/1b58cb9a1b4f4353e1add63c8506db4d890962e8)、[AI SDK](https://github.com/vercel/ai/tree/0a5c786ef65bcd835328fb543685f6d8ef233dae)。

## 3. 原 Nous 已经具备的 Prompt 能力

### 3.1 应直接迁入的文件

[原 PromptRegistry](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/apps/nous-core/src/model/prompts.ts) 提供 `load(role,path?) -> {id,digest,text}`。它已有以下实际行为：

- 职责映射到资源文件，外置覆盖显式使用 `config-prompts/` 前缀。
- `realpath` 后检查仍在允许根目录，拒绝目录、空文件、无效 UTF-8 和超过 128 KiB 的资源。
- SHA-256 标识实际文本，`id` 区分 program/config 来源。
- 读取机械已经复用 `get-stream`；无需换成一套新的文件读取框架。

完整资源目录共 15 份：

| 路径组 | 文件 |
| --- | --- |
| `query/` | `concept-enrichment.md` |
| `projection/` | `steward.md` |
| `memory/` | `formation.md`、`consolidation.md`、`concept-maintenance.md` |
| `self/` | `formation.md`、`reflection.md` |
| `subject/` | `reflection.md` |
| `episode/`、`journal/` | `segmentation.md`、`synthesis.md` |
| `motivation/` | `criterion.md` |
| `material/` | `description.md`、`structure.md`、`direct-structure.md`、`video-description.md` |

这些文本包含职责、输入目录、来源约束、原件与转述的区别、候选范围、时间、不确定性及输出合同。迁入时以当前领域合同审阅字段与职责，不将所有角色归并为“完成本次认知工作”。嵌入、重排、转录等职责也不必虚构一份聊天人格 Prompt。

原 `model/invocations.ts:79–125` 在创建模型执行器时加载角色 Prompt；`306–340` 支持一次调用显式重新选择 Prompt；`289–304` 将 Prompt digest 与模型、执行、角色配置 digest 进入 producer metadata。普通默认角色的 Prompt 被执行器初始化快照持有。新实现保留资源模型，补齐版本管理、预览与新调用采用的生效闭环。

原 Hept [role-prompts.ts](https://github.com/Heptalogos-Devs/Heptalogos/blob/21f0080460f3ee639deb9f5ea47282fb6c59df95/packages/application/product-host/src/role-prompts.ts) 已分别定义世界规划、主体审议、专业执行、自然表达、叙事审查。迁入其职责文字与版本身份，再移出代码常量成为可管理资源。审议、执行、自然表达和审查各有输入与行为责任，不能只换一个 role 字符串而共用空泛指令。

### 3.2 最省维护的组织

将`prompts.ts`通用Registry迁入`packages/platform/src/prompts/`，两个产品完整文字各放自己仓根`prompts/`并随包发行；共享成熟渲染器、watcher和资源修订，领域Prompt含义归对应产品。Registry只负责发现、选择、加载与不可变快照，认知查询、权限读取和世界解释由实际领域owner承担。

程序默认资源随产品分发；PostgreSQL 不可变覆盖修订与 active head 是安装后的运行权威。本地配置根作为导入/导出编辑面，带 baseRevision manifest；文件编辑与管理 API 进入同一个验证、CAS 保存和激活流程。运行调用按冻结修订读取，不混用正在变化的文件。

## 4. MaiBot：实际机制与可复制模块

### 4.1 PromptManager 与版本管理

固定提交中的实际路径是 [src/prompt/prompt_manager.py](https://github.com/Mai-with-u/MaiBot/blob/ff0fe42500f5f7581e9655d1e78379407233207a/src/prompt/prompt_manager.py)，并非旧的 `chat/utils` 路径。

| 责任 | 真实入口 | 已有行为 |
| --- | --- | --- |
| Prompt 克隆与上下文 | `Prompt.add_context`、`PromptManager.get_prompt/render_prompt`，67–293 行 | 注册命名上下文；获取克隆后渲染；支持同步/异步构造函数、嵌套块；缺变量和循环过深报错 |
| 资源发现与覆盖 | `PromptManager.load_prompts`，333–393 行；`src/common/prompt_i18n.py` | 程序 `prompts/<locale>/*.prompt` 与 `data/custom_prompts/<locale>`；返回实际 path、locale、customized；读取 `.meta.toml/.meta.json` 的名称、说明和 advanced 属性 |
| 缓存失效 | `get_prompt` 触发 `_reload_if_prompt_cache_changed`，395–417 行 | 比较 cache revision，构建新集合后替换，克隆不会污染注册原件 |
| 版本与激活 | `src/webui/routers/config.py:1003–1209` | 列出/读取/创建/删除版本、激活指定版本、恢复默认；激活前检查占位参数并写当前覆盖文件 |
| 调用预览 | `src/maisaka/display/prompt_cli_renderer.py`、`prompt_preview_logger.py` | 输出实际上下文、工具、尝试和 token 信息的可查看预览；多模态可采用二进制引用 |
| 失败调用快照 | `src/llm_models/request_snapshot.py` | 结构化 request/output/context items、失败快照与重放信息；当前快照格式版本为 6 |

`prompt_i18n.py:330–332` 的文件读取按路径缓存；`415–422` 显式清缓存并增加 revision。源码中的失效调用来自管理 API 保存、激活、删除等路径。直接手工修改资源文件还需要接入变更通知；不能将这个机制写成无条件的文件自动热更新。

该目录以 stem 生成全局 Prompt 名并拒绝重名；原 Nous 的 memory/formation 与 self/formation 因此需要显式 namespaced PromptId。移植元信息与管理流程时保留完整路径身份。

**采用方式**：迁入原 Nous Registry 作为文件与身份基底；实际移植 MaiBot 的资源元信息、版本管理、参数验证、激活与预览流程。渲染实现直接采用 LiquidJS，删除 Python Formatter、自定义递归和花括号转义机械。新结构不复制 MaiBot 的历史兼容目录查找与全目录删除重写：`save_prompts():295–320` 会删除活动目录中的自定义文件，该全量操作不适合作为一次保存单个 Prompt 的产品语义。

### 4.2 资源、模型与职责配置

[src/config/model_configs.py](https://github.com/Mai-with-u/MaiBot/blob/ff0fe42500f5f7581e9655d1e78379407233207a/src/config/model_configs.py) 将 `APIProvider`、`ModelInfo`、`TaskConfig` 和 `ModelTaskConfig` 分开。`TaskConfig:392–442` 包含 model_list、max_tokens、temperature、balance/random/sequential 选择及 hard_timeout。角色包括 replyer、planner、memory 等。

[src/config/config.py](https://github.com/Mai-with-u/MaiBot/blob/ff0fe42500f5f7581e9655d1e78379407233207a/src/config/config.py) 的 `ConfigManager` 分开管理 bot/model 配置、文件指纹、reload_revision 与按 scope/section 订阅的回调。`reload_config:569–644` 先加载校验候选，再替换当前引用；解析失败保留现用对象。回调失败单独记录，不抹掉已经载入的新配置。

`src/llm_models/utils_model.py:133–180` 的 `LLMOrchestrator` 按 task_name 读取实时 TaskConfig，每次请求刷新模型列表。`model_client/base_client.py:448–463,686–691` 的 ClientRegistry 监听配置改变并增加 cache generation，旧实例的请求可以收尾，新实例不会被旧初始化结果回填。

**采用方式**：沿用完整的“资源→模型→职责策略→单次快照”组织，保留可选模型和明确选择策略。TS 执行适配直接依赖 AI SDK Provider Registry，移植配置刷新与客户端 generation 机制；不再额外移植一整套 Python Provider 协议栈。MIT 的 `src/llm_models` 若有具体缺失能力可按模块复制，其 MIT 标识不延伸到 GPL 的 `src/config` 或 PromptManager。

### 4.3 Focus、表达、黑话与人物画像

| 能力 | 真实源码 | 复制或采用切口 |
| --- | --- | --- |
| 焦点管理 | `src/maisaka/focus/manager.py`，`FocusModeManager` | 复制完整状态与转移模块，保留 scope 内一个焦点、共享组、进入/释放/切换、冷却、@解除阻塞、已读与周期时间；替换 global_config、time、chat_manager 为 Hept 真实配置/时钟/会话入口，状态写入其业务事务 |
| 焦点运行材料 | `src/maisaka/focus/runtime_mixin.py` | 搬用跨聊天事件与切换材料的完整构造段，保留 at/mention/unread_count/unviewed_time、只在当前会话取历史、连续 idle 后退出及冷却唤醒。定时与持续进度接现有 DBOS，不复制另一套 asyncio 调度器 |
| 表达选择 | `src/chat/replyer/maisaka_expression_selector.py`，`MaisakaExpressionSelector` | 复制候选范围、选择、去重、表达意图和输出段组织；保留向量候选及加权选择能力。SQLModel 与 expression_vector_index 改接 Nous 正式查询，subagent 回调接统一模型角色；删除第二份向量索引与私有数据库查询 |
| 表达学习 | `src/learners/expression_learner.py` | 复制真实聊天源提取、去重、过滤、批次学习与更新流程；`275–325` 只选择 SessionBackedMessage，工具结果、记忆注入和规划思考不进入学习源 |
| 黑话学习 | `src/learners/jargon_learner.py`、`jargon_miner.py` | 采用带真实 message ID 的来源批次；保留上下文推断、常规含义对照、比较与不足时 no_info 的流程，进入 Nous 语言认知 owner |
| 人物资料与证据 | `src/person_info/person_info.py`、`src/common/database/database_model.py:419–447`、`src/services/person_fact_verifier.py` | 平台/user/person ID、群名片与认识时间分开。人物事实核对保留对应会话、对应人物、原消息与原引文；存储接 Nous 实体与社会认知，删除独立 memory_points 认知权威 |

Focus 上游常量 `FOCUS_SLOT_LIMIT=1`，是**每个 focus scope** 一个位置；可配置 focus_groups，未命中的会话有独立 scope。不能把它简单概括成整个安装永远只有一个群聊。焦点改变的是实际决策入口与材料，不是给每条消息加一个静态优先级数字。

`maisaka_chat_focus.prompt` 区分分析/动作与可见发言，`reply_reference` 是回复方向而非正文；表达随后使用身份、语气、关系及当前会话材料。`learn_style.prompt` 明确排除 SELF 的发言，`jargon_inference_with_context.prompt` 在证据不足时输出 no_info。应保留这些能力与真实数据流，避免只借用“自然、拟人”两句描述。

上述 Focus、表达与配置模块位于 GPL 范围。复制/移植时记录各自原始文件、提交、原许可和修改清单。选择 TS 移植是为了复用既有 TS 服务和持久化，不是换语言后重做一套简化算法。

## 5. AstrBot：实际可搬用的管理设施

### 5.1 管理接口与核心责任

[astrbot/dashboard/api/router.py](https://github.com/AstrBotDevs/AstrBot/blob/fc6b326fc9012873c4adc0183256c90d34a3d912/astrbot/dashboard/api/router.py) 将正式路由挂在 `/api/v1`，从 route 的 ScopeDependency 生成 OpenAPI 权限信息。接口层依赖服务对象，再进入持久化或运行管理器，适合直接作为产品 API／Service／Runtime 的完整功能组织基底。

| 功能 | API 文件与代表操作 | 实际责任与迁入方式 |
| --- | --- | --- |
| Config Profiles | `api/config_profiles.py`：schema、profiles CRUD、system-config/runtime、config-routes | `core/astrbot_config_mgr.py` 管 profile；`core/umop_config_router.py` 管会话路由；profile 与实际 source/provider/platform 分开。复制资源操作与响应组织，替换 core_lifecycle 依赖 |
| Provider 资源 | `api/providers.py`：provider-sources、models、providers、enabled、test、embedding-dimension | `services/config_service.py:ProviderConfigService` 与 `core/provider/manager.py`；同源连接配置供多个具体模型复用，模型覆盖源默认。迁入来源/模型/测试/可用性视图，执行对象由 AI SDK 适配生成 |
| Persona | `api/personas.py`、`services/persona_service.py`、`core/persona_mgr.py` | 文件夹、排序、默认选择、提示内容与 tools/skills/MCP 能力范围。复制管理流程；与 Nous 长期 Self/关系/经历的修改操作分开 |
| 插件 | `api/plugins.py`、`core/star/star_manager.py` | 安装、更新、启停、失败加载、重载、卸载及模块清理。迁入实际生命周期管理能力，接选定扩展框架，替换 Star/事件管线注册；不复制另一套 Python 插件宿主 |
| Tools／MCP | `api/tools.py`、`services/tools_service.py`、`core/agent/mcp_client.py` | 工具列表、权限、启停、服务器增改删、连接测试、失败回滚。复用 API 与 UI 流程，MCP 传输使用成熟客户端 |
| 历史 | `api/conversations.py`、`services/conversation_service.py` | 分页筛选、详情、历史内容、改名、单个/批量删除与导出。复制完整操作流程，数据读取改向 Hept 当前会话 owner |
| 日志／Trace | `api/logs.py`、`services/log_service.py` | history、live SSE、trace settings/history/detail，断线通过事件身份接续。日志只展示同一实际调用记录的派生视图 |
| 备份 | `api/backups.py`、`services/backup_service.py` | manifest、检查、导出/导入、分块上传、任务状态与下载。迁入 UI/API 和 manifest 操作组织；其内存 backup_tasks/progress 不替代本项目已选 DBOS 持久进度 |

`AstrBotConfig.save_config_async:294–376` 先建立隔离快照并分配 save revision，用临时文件＋fsync＋replace 防止较旧异步保存覆盖新文件。`ConfigProfileService.update_profile:691–761` 处理权限、保存、运行资源收尾与 pipeline reload，返回已保存及连接警告。`ProviderManager.reload:823–866` 对具体 Provider 加锁、终止并重新加载。**保存文件、有效运行对象与失败状态分别可观察**，这比一个不返回生效结果的 PUT JSON 更完整。

### 5.2 可直接复制的前端功能组

选 Vue 3＋Vuetify，保留组件功能，再在 API 入口换正式 Client。不要复制后换成 React 重画全部组件。

| 功能组 | 实际文件与依赖闭包起点 |
| --- | --- |
| 通用配置表单 | `dashboard/src/components/shared/AstrBotConfigV4.vue`、`ConfigItemRenderer.vue`、`ListConfigItem.vue`、`FileConfigItem.vue`、`ConfigDefaultReset.vue`，以及 `useConfigTextResolver` |
| Profile 与分层选择 | `components/config/ConfigProfileDrawer.vue`、`ConfigProfileMenu.vue`、`views/ConfigPage.vue` |
| Provider 来源及模型 | `components/provider/ProviderSourcesPanel.vue`、`ProviderSourceDialog.vue`、`ProviderModelsPanel.vue`、`ProviderChatCompletionPanel.vue`，以及 `useProviderSources`、`useProviderModelSelection`、`useProviderModelConfigDialog` |
| Persona 及能力 | `shared/PersonaForm.vue`、`PersonaCapabilitiesEditor.vue`、`PersonaCapabilityList.vue`、`PersonaQuickPreview.vue`、`PersonaSelector.vue` |
| Plugins／Tools／MCP | `extension/` 下列表、工具表、动作 composables、`McpServersSection.vue`，及搜索/确认/i18n/LazyMonacoEditor 依赖 |
| 会话历史 | `conversation/ConversationHistoryPreview.vue`、`useConversations.ts` |
| 日志与备份 | 对应 views、`shared/BackupDialog.vue` 与日志 SSE 服务入口 |

源码依赖 Vue、Vuetify、Pinia、vue-router、i18n、Axios、Monaco 等实际库；组件并非孤立的一张图片。例如 ConfigProfileDrawer 会加载整个 ConfigPage，MCP 组件引用 API、编辑器、i18n、搜索和确认交互。复制以完整功能组为单位，并保留这些真正使用的通用依赖；重连 `dashboard/src/api/v1` 到产品公开 Client，删除旧生成 Client 和旧 AstrBot 端点消费者。

上游 dashboard 在固定提交使用 TypeScript 5.1.6、vue-tsc 1.8.8、Hey API 0.60.0。这些工具链配置不应随 Vue 组件原样覆盖当前 Node24/TS7 工具链；先保留组件，再对实际编译器 API 消费者选择兼容版本。现有组件代码与其构建器是两个可独立更换的部分。

实际 ConfigProfileDrawer、AstrBotConfigV4、PersonaForm、McpServersSection 当前均为 JS SFC。本轮用 `@vue/compiler-sfc@3.3.4` 对四个原文件 parse＋compileScript 成功；采用 JS SFC＋Vue/Vite 构建、TS7 纯 contracts，无需为这些组件另装旧 TS 编译器。通用组件复制成单独 `@nous-wave/management-ui`，两个产品消费正式版本，各自保留领域页面。

### 5.3 原 Hept 已有的扩展框架

原 Hept `packages/runtime/runtime-substrate/src/cordis-adapter.ts` 已依赖 Cordis `4.0.0-rc.8`。真实公开 API 为 `new Context()`、可 await 的 `Context.plugin`、`ctx.effect`、Fiber 的 await/update/restart/dispose；Plugin.Config 接受 StandardSchema，Zod4 可直接参与校验。本轮探针加载插件、注册资源清理并 await dispose 均成功。

当前 adapter 又维护 Activation 状态、tracked task、late disposer、AbortController 和 timeout settlement。选定直接使用 Cordis 的生命周期与依赖机械；产品只保留业务 admission、外部 effect 收尾和 DBOS 长期进度。能力数据、权限与正在发生的业务工作仍归真实 owner，Fiber 不成为持久 workflow 或隔离沙箱。

**运行边界**：AstrBot 的管理功能复制后接入我们自己的对象与 owner。旧分支将收件、发送控制 HTTP 服务及账号作用域放进 AstrBot Star 的 initialize/terminate；这使 Hept 渠道寿命跟随整个 AstrBot。该承载方向与用户当前选择不符，应移除这条产品依赖，保留可复用的渠道/回执机械或选定协议模块。

## 6. OpenClaw：包、配置、工具和执行接缝

### 6.1 已存在的组织

| 责任 | 固定版本中的真实位置 | 采用判断 |
| --- | --- | --- |
| Provider 与流执行 | `packages/ai/`，`@openclaw/ai`，MIT | package.json 声明可复用 Provider/streaming runtime。优先直接包依赖；若所需制品不可独立取得，按固定源码构建对应包。避免同时从零再写一套协议适配 |
| 通用循环 | `packages/agent-core/`，`Agent`、agent-loop、agent-stream-response、runtime-deps | private workspace 包。`AgentCoreRuntimeDeps` 注入 streamSimple/completeSimple/runStream；它与 llm-core、normalization-core、ai 存在真实包依赖。采用须固定整个所需依赖闭包 |
| 消息与模型值 | `packages/llm-core/` | private workspace 包，包含文本、图像、thinking、tool call/result、原生不透明返回、usage 与 streaming event；按真实外部边界转换，不能把它们全压成一个字符串 |
| 工具 | `src/agents/core-coding-tools.ts`、`agent-tools.read.ts`、`bash-tools.*`、`src/agents/sessions/tools/` | read/write/edit/exec/process、预算、沙箱与 Skills 读取已成熟。复制改编该责任模块及其导入闭包，将宿主配置/会话/能力接口移到明确输入；不重新实现 cat/exec/工具循环 |
| Skills | `src/skills/loading/workspace-skill-loader.ts`、`runtime/refresh.ts`、`loading/workspace-skill-sources.ts` | 目录来源、覆盖、过滤、快照、读取与热刷新；优先模块复用，替换安装/工作空间 owner，保留能力 |
| 配置 | `src/config/types.models.ts`、`types.agents.ts`、`src/gateway/server-methods/config*`、`config-reload-plan.ts` | Provider 目录、agents.entries、校验、变更分类、生效计划与重启状态；复用配置机械及管理语义，产品角色与世界状态留在本产品 |
| 原生人格文档 | `workspace-bootstrap-policy.ts`、`workspace-bootstrap*.ts`、`system-prompt.ts` | AGENTS/SOUL/IDENTITY/USER/TOOLS 等文件的独立读取和职责；可作为人格资源导入材料，保持文件来源与实际修订 |
| 原生插件 | `src/plugins/registry-registrars-providers.ts`、`registry-registrars-tools-hooks.ts`、`registry-registrars-network.ts` | registerProvider、registerTool、Hook、Gateway method 是实际注册入口；从正式责任处改编扩展，不靠安装后查找 bundle 文本替换 |

[agent-core/package.json](https://github.com/openclaw/openclaw/blob/1b58cb9a1b4f4353e1add63c8506db4d890962e8/packages/agent-core/package.json) 和 [llm-core/package.json](https://github.com/openclaw/openclaw/blob/1b58cb9a1b4f4353e1add63c8506db4d890962e8/packages/llm-core/package.json) 明确 `private:true, version:0.0.0-private`。因此第一条施工动作应是把选定源码闭包产出成可用依赖，实际验证语言模型、工具、沙箱和历史；不在 Spec 中许诺一个尚不存在的即装即用独立包。

### 6.2 已有未完改编揭示的事实

当前本地改编在 `agent-stream-response.ts` 的 transformContext/convertToLlm 之后、实际 streamFunction 之前插入 prepare/dispatch；在 message_end 持久保存后 accept。辅助摘要另走 `harness/compaction/summarization-completion.ts`，手动压缩另建 session，Responses compact endpoint 又是独立 Provider 请求。**仅在普通 Agent 循环前挂一次 hook 会漏掉真实模型请求。**

本地原生会话保存调用身份、prepared/dispatched/not-dispatched/settled 与实际输出；失败后先补接纳，未知物理结果保留预留并阻止新派发。这些是执行宿主的真实责任，可以保留为选定模块的改编切口。后续接纳返回 outputRef、原 entry 元数据与最终文本选区的改编仍未交付正式包，按实验事实记录。

原本为接一个专业任务而构建整个 OpenClaw：现有构建日志显示顺带构建 96 个插件及 Control UI，完整一次约 4m41s；本机 3 GiB 运行图构建触及内存上限，6 GiB scope 可完成。采用的工具、执行、历史、Skills 与沙箱能力及真实依赖闭包形成正式制品，移除未采用的产品宿主构建责任。

### 6.3 物理回执与原生备份的真实闭包

默认OneBot源码为[`xucheng/openclaw-onebot@c926fe62db49f6ba66fe67ff0dba240efa8fc9dd`](https://github.com/xucheng/openclaw-onebot/tree/c926fe62db49f6ba66fe67ff0dba240efa8fc9dd)，MIT。outbound.ts::uploadFile保留upload_group_file/upload_private_file原ack；channel.ts:188当前以Date.now补messageId。OpenClaw的deliver-results.ts::observeDeliveryResult只接纳resolveReceiptSourceId成功的结果，无IDack会被丢成adapter_returned_no_identity。

采用时须同时改真实result/receipt类型、该recorder、receipt归一、queue持久owner、delivery-completion与recovery。deliver-queue-execute的onDeliveryResult目前只把result放进内存并调用persistQueuedPostSendState；后者只写markDeliveryPlatformOutcomeUnknown，尚未保存action/ack正文。需在既有delivery-queue-storage/worker的canonical entry/retained receipt按physicalCallId持久accepted operation，再回传产品；平台ID可缺失。recovery按证据跳过已确认的物理call并补交原结果，无ack继续unknown；一个piece成功不能提前完成多call batch。只改插件外层、meta或复用unknown marker仍无法恢复真实ack。完整施工合同归[媒体与材料](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/媒体与材料基础.md)。

整安装backup已提供commands/backup.ts::backupCreateCommand→infra/backup-create.ts::createBackupArchive，includeWorkspace默认true，agentRoots由backup-shared按全部配置agent发现；backupRestoreCommand验证后解到新staging并拒绝live覆盖。现有参数没有Subject子集。sessions.get仅recent有界内容；普通sessions.delete会archiveTranscript并返回archived路径。单Subject完整session/retained/call/queue/unknown/workspace导出、恢复与物理purge是需要在原SessionManager/backup/lifecycle owner补的窄scope接缝，详见[数据规范](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/数据生命周期与发行.md)。这些接口尚未作为上游能力提供。

backup-shared的rawCandidates还明确包括credentials/oauth，state本身也可能含auth；BackupCreateOptions没有excludeSecrets。backup-capture-privacy只验证排除private update-captures，不是secret脱敏合同。完整native安装备份必须按含秘密制品显式选择并加密；默认引用模式不能将这种archive标记为secrets.included=false。

## 7. AI SDK 7：实际能力与正确调用边界

源码以固定提交 `0a5c786…` 的 `packages/ai/src/` 和 `packages/provider/src/` 为准。主要入口是 `registry/provider-registry.ts`、`generate-text/generate-text.ts`、`middleware/wrap-language-model.ts`、`middleware/wrap-provider.ts`、`prompt/language-model-call-options.ts`。

### 7.1 Provider Registry 覆盖的模型族

正式工厂是 `createProviderRegistry(providers,{separator?,languageModelMiddleware?,imageModelMiddleware?})`。默认 ID 形式为 `providerId:modelId`，registry 负责分离 ID、找 Provider、返回对应 V4 模型；Provider 没有该能力或返回空值时抛 NoSuchModelError。它不负责本产品的凭据权限、预算、角色或价格。

| 能力 | Registry 方法 | 正式 SDK 操作与重要返回 |
| --- | --- | --- |
| 文本／工具／结构化／视觉输入 | `languageModel(id)` | `generateText/streamText`、`Output.object`、工具循环。每步可读 content、warnings、usage、request、response、providerMetadata；多模态内容继续用 SDK ModelMessage parts |
| 嵌入 | `embeddingModel(id)` | `embed/embedMany`；向量、`usage.tokens`、warnings、providerMetadata、可选原响应 |
| 重排 | `rerankingModel(id)` | `rerank`；ranking 含 originalIndex/score/document；response 含模型、时间、可选 headers/body。高层结果没有统一 LLM usage 字段 |
| 转录 | `transcriptionModel(id)` | 正式 `transcribe`，返回 text、segments(startSecond/endSecond)、language、durationInSeconds、warnings、responses、providerMetadata。`experimental_transcribe` 是 deprecated 别名；流式转录当前名为 `experimental_streamTranscribe` |
| 合成语音 | `speechModel(id)` | 正式 `generateSpeech`；返回音频文件、warnings、responses、providerMetadata。`experimental_generateSpeech` 是 deprecated 别名 |

`wrapProvider` 只给 language 和可选 image 套对应 middleware，其他模型方法原样转发。各模型的 `doEmbed/doRerank/doGenerate` 实际接口使用薄的产品调用计量层，或对应 SDK 生命周期事件；协议实现仍留给 Provider。

Transcription/Speech V4 原始结果含 `usage?:JSONObject` 和 `request?.body`；高层 TranscriptionResult/SpeechResult 未暴露统一 usage。SDK 内部结束事件实际携带原始 usage；若产品要保存原请求与计费事实，应在对应 Provider 边界保留它们，不能从高层文本或音频大小猜造 token。音频时长、字符或其他计费单位按真实 Provider／价目定义处理，未返回就记录未知。

### 7.2 便携推理参数与 Provider 参数

当前 `LanguageModelV4CallOptions.reasoning` 为 `provider-default|none|minimal|low|medium|high|xhigh|max`；`providerOptions` 是按 Provider 命名空间组织的专有对象。SDK Provider utils 已有 effort/budget 映射及 unsupported/compatibility warnings，具体 Provider 决定映射与专有选项优先级。

已安装 openai-compatible 的实际构造使用 `compatibleOptions.reasoningEffort ?? portableReasoning`。因此本产品保留便携 reasoning 和原样 ProviderOptions 两层；不再手写跨厂商映射，也不把所有 Provider 都强制降为 OpenAI chat/responses。高级界面显示实际采用的选项与 warning，避免“配置保存成功”被解释成模型确实支持该参数。

### 7.3 prepareStep 应保留真实消息

`generate-text.ts:901–987` 将前面步骤的实际 response messages 累积起来，向 prepareStep 提供当步 messages；返回新的 messages 会覆盖它们，并影响之后的步骤。工具材料还会继续转换为 Provider prompt。

认知 slot 的正常用法是按当前步骤准备资料、更新本次 instructions，并保留当步消息：

```ts
prepareStep: async step => {
  const selected = await cognition.prepare({ messages: step.messages, model: step.model });
  return { instructions: renderRoleAndCognition(selected), messages: step.messages };
}
```

上述代码只示意 SDK 消息保留边界；角色基准指令来自已选 PromptSnapshot，不能把上一步临时认知再追加成永久角色文字。若确有显式压缩/投影，messages 应是该真实投影结果，并保留变更来源、工具调用关联与模态内容。

### 7.4 准备输入、最终输入与实际请求分别记录

1. **资源与预览**：记录 Prompt 资源、修订/digest、模板参数和使用的输入引用；预览不创建实际接触。
2. **步骤最终语义输入**：onStepStart 在 prepareStep、工具选择与消息转换后提供 instructions/messages/promptMessages/stepTools/stepToolChoice。它比调用 prepare 前的业务 prompt 更接近实际模型输入。
3. **模型调用边界**：最靠近 Provider 的 wrapGenerate/wrapStream 取得变换后的 V4 params；此处冻结实际模型、参数、工具、模态、调用身份与预算，再委托 SDK 原方法。
4. **真实 Provider 请求与结果**：保存 SDK 返回的 request.body、response id/model/headers、warnings、usage.raw、providerMetadata。流与各非文本模型按其真实返回字段采集；SDK 未提供的字段不标成已捕获的 wire request。
5. **成功消费与恢复**：模型生成完成且结果持久保存之后才接纳实际接触。DBOS 恢复采用已保存输出与稳定调用身份；对已经派发但结果未知的调用先核实外部事实。

generateText 的 `usage` 是最后一步，`totalUsage` 是多步合计；逐次 ledger 使用每步结果。V4 原始 usage 的 inputTokens/outputTokens 是嵌套对象，高层 LanguageModelUsage 则是数值总量及 inputTokenDetails/outputTokenDetails。未知字段保留 undefined，不能统一填 0。跨产品或多个中间件不能再对同一个物理调用各记一次费用。

### 7.5 MCP 与错误的实际边界

官方 npm `@ai-sdk/mcp@2.0.80` 源码 `src/tool/mcp-client.ts` 提供 `createMCPClient`、tools/listTools/callTool/resources、initializeResult 和 close；HTTP/SSE transport 可注入 fetch、保存 sessionId/协议和接收过期通知，默认工具重试0。`@ai-sdk/mcp/mcp-stdio` 的导出仍名为 `Experimental_StdioMCPTransport`，其 StdioConfig 具备 command/args/env/cwd/stderr/shell。默认继承 HOME/PATH 等环境，受限运行要由真实执行宿主给出隔离环境，不能将 cwd 当成隔离。选直接依赖该客户端而不移植 AstrBot Python MCP 协议。

APICallError 的官方实现保存 requestBodyValues/responseBody/message/cause/data。DBOS5.3 的 Error 序列化会枚举自定义字段并递归 cause；普通日志字段 redact 无法清理自由文本正文。实际 Provider doX 在进入 durableCalls checkpoint 前提取安全 status/requestId/retry 分类，以安全官方 APICallError 保留 SDK 类型；raw 去秘密后按策略存受限 Artifact。错误、checkpoint 与诊断保留由同一个数据生命周期管理。

实际已安装`@dbos-inc/vercel-ai@0.5.4`的internal.withErrorClassification默认retriesAllowed=true；仅设置AI SDK maxRetries=0还会留下另一层自动重派。正式配置durableCalls/durableEmbeddingCalls的retriesAllowed=false，真实doX内仍先查长期ModelInvocation。该包已提供restoreAISDKErrorIdentity恢复SDK错误标记；同workflow并发durable model calls会拒绝，因此并行调用冻结稳定计划后分别使用官方子workflow。秘密使用范围也必须持续到stream/tool实际收尾，不能只包住SDK对象创建或把带apiKey实例放长期cache。

## 8. Prompt 与配置：选定的资源、生效和预览流程

### 8.1 模板库选择

| 方案 | 直接可用能力 | 维护代价与结论 |
| --- | --- | --- |
| Handlebars 4.7.10 | compile/precompile、partials、strict、noEscape、显式 partial context | 可用，但异步来源需先准备数据；Prompt 不应沿用默认 HTML 转义 |
| LiquidJS 10.30.0 | parse/render、异步渲染、目录/partials、自定义 fs、strictVariables/strictFilters、静态 partial 选择 | **采用**。适合资源目录、预览与固定模板依赖闭包，不另写解析器 |
| 原样搬 MaiBot Python 模板运行时 | 已有完整上下文构造、覆盖和 UI 管理行为 | 会把 paths/logger/locale/全局注册与 Python 宿主引入纯 TS 模型路径；采用其管理与交互流程，渲染机械由上述库承担 |

LiquidJS 静态变量分析当前为 experimental；可用于编辑预览的提示与诊断，实际调用仍靠正式参数 schema 与严格 render 检查。不要用实验分析树充当持久领域合同。库说明见 [options](https://liquidjs.com/tutorials/options.html)、[static analysis](https://liquidjs.com/tutorials/static-analysis.html)；Handlebars 的 [compile 选项](https://handlebarsjs.com/api-reference/compilation.html)用于上述比较。

实际探针位于 `temp/spec-research/platform-probes/{probe.mjs,result.json}`：Liquid 严格变量/固定 partial/原样 JSON、Handlebars 默认转义对比、Chokidar 稳定写入通知、Cordis 加载/清理以及上述四个 Vue SFC 编译均通过。LiquidJS `dynamicPartials:false` 的静态写法为未加引号的 partial 名，如 `{% render identity, subject: subject %}`；内存 templates 表冻结依赖闭包，运行时无需读取任意目录。

### 8.2 生命周期

- **发现**：稳定 PromptId、领域/职责、语言、默认文件、说明、可见层级、参数 schema、可选组成块。程序资源原路径可保留，便于持续查看与改进。
- **覆盖**：明确程序默认、安装覆盖、主体/职责绑定的优先级；返回每个生效值及来源。数据库修订为运行权威，文件经带 baseRevision 的同一保存/激活操作导入。
- **修订**：保存新文本或 partial 依赖形成不可变 revision/digest；激活指针单独更新。角色绑定可锁定某修订，或使用当前激活项。
- **预览**：同一个正式 renderer，使用明确的示例参数/已获准输入，返回组成块、实际文本、资源与依赖版本、缺失参数和预算估计。预览没有模型派发与 Encounter。
- **热生效**：Chokidar 负责文件稳定与通知；候选完整校验并成功 compile/render 后原子替换当前 RegistrySnapshot。失败保留现用快照并展示未生效原因。新调用取新快照，进行中的调用保留所采用版本。
- **调用追踪**：同时保存 PromptSnapshot、ConfigSnapshot、最终语义输入与实际 Provider attempt；日志/预览是它们的显示视图，不再建立一份可单独修改的 prompt 历史库。

### 8.3 稀疏覆盖的实际错误

当前重建 `packages/contracts/management.ts:21` 从含 default 的完整 Schema 调用 `.partial()` 生成 PatchSchema。根代理已用 Zod4.6.5 实测：`{n:default(7),flag:default(true)}.partial().parse({})` 仍补出 n 与 flag；只设置 n 也会补 flag。这会把不存在的覆盖项变为本层显式设置，污染安装/主体/职责合并结果。

采用 settings 的 JSON Patch 修改本层 sparse JSON，再合并各层、最后校验完整有效值与默认；来源追踪只标记实际出现的字段。专用资源输入如仍需要 PatchSchema，必须独立无 default。clear/reset、数组替换与对象合并使用同一 settings 语义。

## 9. 当前分支需要删除或替换的具体错误

| 位置与事实 | 造成的结果 | 纠偏与可删机械 |
| --- | --- | --- |
| 当前 Nous `platform/models.ts:58–62` 保存 step.messages 后，实际返回固定单 user 消息 | 被记录的输入与真正派发不一致，工具后续与多模态/用户任务被替换 | 使用 SDK 当步消息；角色与认知只更新明确 slot，删固定消息替换及其派生测试支架 |
| 当前同文件只用两句通用角色指令，未加载原 prompts/ | 记忆、形成、材料解释、表达等职责失去自己的完整规则 | 直接迁入原 Registry 与资源，按现合同修订，不从零手写一组短替代品 |
| 当前文字中间件只包 wrapGenerate | 流式及其他模型族没有进入同一实际调用事实路径 | 采用 SDK 的真实模型族接口与 wrapStream；删除手写 Provider 协议/响应解析，不建另一套模型循环 |
| 当前 OpenClaw 插件先截取最近输入，再截至 8000 字符 | 该材料是有界线索，不是最终实际模型输入；遗漏区间未由这份文本表示 | 将原始输入 trace 留在真正执行边界，认知线索与实际输入记录分开；显式保存 coverage/selector |
| 当前 Hept `integrations/astrbot/main.py:37–68,101–111` 把控制服务与收件绑定 Star 寿命 | Hept 的渠道运行随 AstrBot 启停，默认聊天被插件拦截；AstrBot 被当成产品宿主 | 复制需要的协议/回执责任模块，渠道归 Hept；AstrBot 管理 API/UI 实际改编后归本产品，移除整应用承载 |
| 原 Hept NetworkAccess 仅允许 POST、openai-chat/openai-responses，并缓冲完整 response body | 多模态上传、原生 Provider、代理及长流失去真实能力 | 使用 Node24 Fetch＋Undici8 Dispatcher1Wrapper 保留 Request/FormData/流与成熟代理；Provider 负责协议 |
| 当前同时维护产品模型资源与原生 Provider/agent 绑定，却只靠配置示例协调 | 用户必须重复配置，实际模型、预算和生效状态容易分叉 | 一份正式资源/职责配置驱动被采用执行模块；实际 Provider 身份进入每次快照与 trace，删除重复可写模型目录 |
| 为一个 read 工具任务默认构建整个 OpenClaw 控制台及插件集合 | 无关产品机械成为核心构建与升级负担 | 产出选定模块及依赖闭包的源码依赖制品，保留实际工具、Skills、历史、沙箱与执行能力 |

## 10. 已统一的接口与施工文档

本轮研究已落实为三个正式设计，公共值使用[共同值与调用上下文](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/共同值与调用上下文.md)，配置/网络/身份/数据分别引用其真实 owner：

- **Prompt 管理**：list/describe/read revision/save revision/activate/reset/preview；返回 source、digest、当前激活与实际生效 revision、校验问题。统一文件编辑与 API 修改的激活流程。
- **模型职责配置**：Resource 指实际 Provider/模型/能力/凭据/网络/价目；RolePolicy 指任务、候选资源、选择与推理参数、Prompt 绑定；InvocationSnapshot 指本次真实采用值。配置覆盖与秘密分别管理。
- **模型执行**：明确 Language/Embedding/Reranking/Transcription/Speech 操作；统一调用身份和费用 owner，保留各自真实输入、输出、usage 和 warning，而不是伪造一个最小共同 JSON 字符串。
- **逐步骤认知与 trace**：prepare 使用当前真实 step；只替换当次认知 slot；before-dispatch 固定最终输入；成功输出持久后 accept；preview、消费和输出发布各走真实业务操作。
- **执行模块与管理宿主**：OpenClaw 哪些源码闭包形成正式依赖，哪些工具/Skills/历史入口暴露给 Hept；AstrBot 复制出的 UI/API 面向我们的 owner，安装、权限、启停、备份与错误状态使用统一产品入口。
- **实际复制清单**：每个采用模块记录 upstream URL/commit、原文件、许可、保留的能力、替换的依赖与维护位置。复制后直接改正式责任结构，删除被替代接口与消费者，不保留平行旧运行路径。

施工入口：[模型供应与调用](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/模型供应与调用.md)、[Prompt与上下文](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/Prompt与上下文.md)、[管理呈现与扩展](https://github.com/Heptalogos-Devs/Architecture-Vault/blob/60122d8f4d10e867b47ad14fea2b119274ce473f/设计/基础设施/管理呈现与扩展.md)。
