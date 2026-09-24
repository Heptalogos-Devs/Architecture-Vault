# 能力、工具与子 Agent

## 基本定义

Capability 是主体可以请求的受控感知或执行能力，不只是一个函数 schema。它可以由普通代码、外部 API、工作流、MCP、浏览器自动化、Python Worker、Rust Executor 或子 Agent 实现。

## Capability Descriptor

至少描述：

- 名称、版本和用途；
- 输入和输出 schema；
- 副作用；
- 所需权限和凭据范围；
- 风险等级；
- 延迟、Token 和金钱成本；
- 可取消性和超时；
- 幂等与重试语义；
- 允许访问的网络、文件和平台动作；
- 执行结果如何事件化。

模型不能绕过 Registry 构造任意调用。

## 执行生命周期

```text
CapabilityRequest
→ policy filter
→ optional confirmation
→ persistent operation
→ claim / execute
→ progress events
→ succeeded / failed / uncertain / cancelled
→ fact stream
→ new Cognitive Job
```

长任务不阻塞认知临界区。工具完成后也不能直接发送消息或修改主体状态。

## 子 Agent

子 Agent 是能力执行后端，不是主体。适合：

- 深度检索；
- 代码分析；
- 文件摘要；
- 多媒体解析；
- 受限规划或模拟。

委派必须明确：

- goal；
- 输入引用；
- 允许上下文作用域；
- 允许能力；
- 时间、Token 和成本预算；
- 终止条件；
- 输出 schema；
- 证据要求。

子 Agent 不得：

- 读取全部人格或私密记忆；
- 修改身份、关系、情绪和事实；
- 直接给用户发消息；
- 自行增加工具权限；
- 将推测写成稳定记忆。

## 语言边界

- 普通网络和云 API 能力优先 TypeScript；
- 数据研究、本地模型和离线算法使用 Python Worker；
- 高风险系统操作、WASM 沙箱和不可信文件处理使用 Rust Worker；
- 外部工具无法明确幂等时必须保留不确定状态。

## 安全执行

隔离应组合：

- 独立进程或 WASM；
- 最小文件和网络权限；
- 临时目录与资源配额；
- 受限凭据；
- schema 和业务验证；
- 审计、超时和取消；
- 明确的输入输出协议。

语言本身不能替代权限边界。

## 开放问题

- MCP、原生工具和 Skill 的统一描述程度；
- 子 Agent 结果需要何种证据格式；
- Worker 的本地 IPC 协议；
- 高风险确认的交互方式；
- 能力健康、成本和路由如何进入模型选择。
