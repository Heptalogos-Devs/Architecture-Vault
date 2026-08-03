# 当前实现

## 仓库组成

主仓库当前包含三个 Python 包和一个 React/TypeScript Web 应用：

```text
heptalogos-control-plane
├── heptalogos-reactor
└── heptalogos-interaction

apps/control-plane-web
```

运行基线为 Python 3.14；前端开发使用 Node 24、pnpm、React、TypeScript、Vite 和 MUI。当前实现事实以主仓库 README、各模块文档、测试和代码为准。

## Interaction Gateway

职责：

- 连接 Milky、OneBot 或 Fake Adapter；
- 每个 Adapter Instance 独立保存 raw Evidence；
- 验证账号和协议版本；
- 持久历史恢复与 gap 诊断；
- 将 Evidence 规范化并融合为 Canonical；
- 维护 Reactor Feed、cursor 和 consumer checkpoint；
- 接受 CommunicationIntent 并形成 DeliveryPlan；
- 记录 request / response Evidence 和 DeliveryOutcome；
- 下载媒体并写入本地 CAS。

关键语义：

- raw-first；
- 至少一次读取和幂等提交；
- request 发出后结果未知时为 `uncertain`；
- 平台账号和原 Adapter Instance 参与路由身份；
- Gateway 不实现人格、记忆、Prompt 或认知。

## Reactor

当前职责：

- 读取公共 Reactor Feed；
- 按私聊、群聊点名或前缀规则分类；
- 维护约二十条短 transcript；
- 使用 LangGraph 构建并调用一个 OpenAI-compatible 模型流程；
- 将非空文本作为 reply，空文本作为 ignore；
- 先持久化生成结果，再确定性提交 Intent；
- 在崩溃后进行 checkpoint 和 ack reconciliation；
- 提供脱敏 admin 查询和 failed-only retry。

当前不包含：

- Observation Window；
- 全局注意力；
- 长期记忆和关系；
- 工具和持久任务；
- 结构化 BehaviorIntent；
- 时间、日程和主动行为；
- 最终 Cognitive Kernel。

## Control Plane

职责：

- 组合 Interaction 和 Reactor 的公共 admin 服务；
- 生命周期、状态和运行控制；
- 默认脱敏查询、HMAC cursor 和单对象 reveal；
- Provider、Prompt、Secret 和配置管理；
- 安装、升级、回滚、卸载和组件所有权；
- 备份、恢复、重放、投影重建和维护 lease；
- 日志、指标、审计、持久操作和 WebSocket 通知；
- 提供版本化 `/api/v1`；
- 托管预构建的 React WebUI。

Control Plane 不跨库解释拥有模块的持久化 schema。

## 当前工程约束

- `domain` 不导入平台或模型 SDK；
- owning package 解释自己的数据库和管理视图；
- OpenAPI 与生成客户端由 CI 守护；
- SQLite migration 连续并带 checksum；
- 原始内容默认脱敏，不进入普通列表和 WebSocket；
- 关键状态转移和人工操作有审计；
- 前端制品嵌入 Python wheel，部署端不要求 Node。

## 目标栈与当前栈的关系

Vault 的目标设计建议未来在线权威运行时转向 TypeScript/Node.js，但这不是当前代码事实。迁移应以领域契约、回放场景和行为切片为单位，不以逐文件翻译 Python 为目标。
