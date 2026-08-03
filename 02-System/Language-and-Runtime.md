# 语言与运行时分工

## 结论

Heptalogos 面向大量云端 AI 供应商调用，而不是以本地模型训练或推理为中心。长期建议：

```text
TypeScript / Node.js  = 在线权威运行时
Python                = 研究、评估、离线认知和本地模型
Rust                  = 高风险、原生或需要强隔离的执行边界
SQL                   = 事实、状态、任务、记忆、Trace 和检索基础
```

## TypeScript / Node.js

负责：

- Interaction Gateway 和平台适配；
- Conversation Mailbox、Observation Window 和调度；
- Cognitive Kernel 与唯一认知提交；
- 云端模型 Provider、流式事件和取消；
- 身份、状态、关系、任务、在线记忆和 ActionPlan；
- Capability 编排与 Control Plane API；
- WebUI 和共享协议。

原因：系统主体是强状态、事件驱动、网络密集的在线应用。判别联合、异步流、AbortSignal 和前后端契约统一比本地 ML 生态更重要。

## Python

负责：

- 模型与 Prompt 评测；
- 场景结果统计和报告；
- 记忆提取、分段、向量和重排实验；
- 日记、反思和梦的离线候选生成；
- Notebook、数据分析和可视化；
- 极少数本地模型与多媒体研究 Worker。

Python 返回候选、分数、证据和报告，不直接修改在线权威数据库。

## Rust

只在边界成立时使用：

- 高风险系统能力；
- WASM 或插件沙箱；
- 不可信压缩包、文件和媒体解析；
- 本机原生集成；
- 经过测量的性能热点。

普通网络工具、云 API 和业务领域逻辑不因“性能”假设迁移到 Rust。

## SQL

SQL 不只是存储实现细节。它承担：

- 事务和唯一性；
- append-only 事实；
- cursor、lease、checkpoint 和 Outbox；
- 状态版本与乐观并发；
- 时间、作用域和全文检索；
- Trace、回放和实验数据。

## 跨语言协议

- 默认使用版本化 JSON Schema；
- HTTP 管理接口使用 OpenAPI；
- Worker 通过 stdio、本地 socket 或明确队列通信；
- 二进制协议只有在吞吐或体积数据证明必要后采用；
- 不在不同语言中手写多个相互独立的领域模型；
- 生成 DTO 不能反向成为核心领域模型。

## 重新考虑条件

- 云端推理不再是主要路线；
- 在线运行时形成 Node 无法满足的明确延迟、内存或可靠性目标；
- 产品转向深度 Windows 桌面集成；
- Gateway 形成独立高吞吐故障域；
- 本地模型成为核心能力而非少数 Worker。
