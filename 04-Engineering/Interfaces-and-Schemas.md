# 接口与 Schema

## 领域通信

模块通过命令、查询、事件和结果协作：

- Query：只读，不产生隐式长期副作用；
- Command：请求拥有模块执行状态变化；
- Event：描述已经发生的事实；
- Proposal：模型或离线 Worker 提交的候选，不具备权威；
- Result：命令或能力执行的明确结果。

不要用模糊的 `message` 或 `payload` 类型承载全部语义。

## Event Envelope

所有跨模块长期事件至少包含：

```yaml
event_id: stable-id
event_type: cognition.behavior.committed
schema_version: 1.0
occurred_at: instant
observed_at: instant
subject_id: subject-ref
conversation_id: optional-conversation-ref
causation_id: optional-event-ref
correlation_id: optional-job-ref
producer: component/version
payload: typed-object
provenance:
  source_event_ids: []
  model_run_ids: []
  policy_versions: []
```

时间、因果、关联和来源不能只藏在 payload 中。

## 版本策略

- 事件和跨进程命令使用显式 `schema_version`；
- 兼容变化可以增加可选字段；
- 删除、改名和语义变化需要新版本或迁移；
- 消费者对未知字段宽容，对未知事件类型明确记录；
- Prompt、模型 Profile、策略和提取器也有版本；
- Trace 能定位完整版本集合。

## JSON Schema

跨语言默认以 JSON Schema 为规范来源。生成：

- TypeScript DTO 和 runtime validator；
- Python Pydantic 或类型模型；
- 测试样本和兼容性用例。

生成类型服务于传输边界，不直接成为领域内部对象。核心模块可将 DTO 转换为自己的值对象。

## OpenAPI

Control Plane HTTP API 使用 OpenAPI：

- 公开 read model 与内部领域状态分离；
- 默认脱敏；
- 分页、过滤和排序有 allowlist；
- 写操作使用资源版本、operation ID 和确认；
- WebSocket 只发送有限通知，不发送正文或 reveal 内容。

## Worker 协议

Python / Rust Worker 的请求至少包含：

- operation ID；
- task type 和 schema version；
- 输入引用而非无界数据库访问；
- 允许作用域和能力；
- 预算、超时和取消；
- 预期输出 schema；
- provenance requirements。

结果只返回：

- structured proposal / result；
- evidence references；
- usage and timings；
- error classification；
- deterministic artifacts。

Worker 不获得在线数据库写权限。

## 幂等和不确定性

命令接口需要明确幂等依据：

- append observation：event ID；
- cognitive commit：job ID + expected versions；
- schedule wakeup：schedule ID / dedupe key；
- execute capability：operation ID；
- submit intent：intent ID；
- correction：correction event ID。

外部副作用接口必须定义 `success / failed / uncertain / cancelled`，不能只返回布尔值。

## 契约检查

CI 应检查：

- Schema 格式和引用；
- TypeScript / Python 生成制品无漂移；
- 旧版本样本仍可读取；
- 枚举和判别联合穷尽性；
- OpenAPI 客户端生成无差异；
- 敏感字段不进入普通 read model。
