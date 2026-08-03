# Heptalogos Knowledge Vault

Heptalogos 的共享设计知识库，服务于三人团队和参与开发的 AI Agents。

它不是需求审批系统、架构委员会档案或正式规范仓库。目标是让当前理念、系统边界、概念模型、工程状态和实验信息容易写、容易找、容易被 Agent 切片读取。

> 内部资料。仓库应保持私有；公开前需检查内部描述、实现细节、个人数据和外部引用授权。

## 从这里开始

- [入口与导航](00-Start/README.md)
- [AI Agent 指南](00-Start/Agent-Guide.md)
- [当前状态](00-Start/Current-State.md)
- [项目愿景](01-Vision/Project-Vision.md)
- [系统总览](02-System/System-Overview.md)
- [概念地图](03-Concepts/Concept-Map.md)
- [近期工作](04-Engineering/Near-Term-Work.md)
- [关键决定](05-Decisions/Decision-Index.md)

## 项目定义

Heptalogos 研究一种在真实即时通信事件流中长期存在的人工主体系统。

它不是每次收到消息才临时拼装的角色，也不是每个会话各自运行的独立 Agent。目标是让同一个主体在时间、关系、经历、任务、知识边界和多个通信平台之间保持可识别、可解释且受控的连续行为。

```text
World events
→ facts
→ subject snapshot
→ cognition
→ behavior
→ action
→ new experience
```

## 目录

```text
00-Start/       入口、当前状态、Agent 指南和团队协作
01-Vision/      项目目标、原则、边界和核心场景
02-System/      系统结构、运行时、数据权威、安全和评估
03-Concepts/    身份、记忆、关系、时间、认知和能力等概念
04-Engineering/ 当前实现、近期工作、Schema、测试和回放
05-Decisions/   少量长期关键选择及重新考虑条件
06-Research/    实验、指标、外部参考和研究笔记
07-Inbox/       未整理的想法、资料和问题
```

旧版 `00-Home`、`01-Foundations`、`02-Requirements`、`03-Domain-Model`、`04-Architecture`、`05-Components`、`06-Research`、`07-Delivery`、`08-ADR` 等审批式结构已被本结构取代。旧内容由 Git 历史保留；有效认识已重新写入当前主题文档。

## 使用规则

- 直接修改最相关的主题文档，不等待审批。
- 讨论产生更好结论后修改正文，Git 历史保存旧观点。
- 只使用 `idea / draft / active / archive`，且仅在状态容易误解时标注。
- 小实现选择不写 Decision。
- 当前实现与目标设计必须明确区分。
- 代码和测试优先于文档中的实现描述。
- 外部参考不能直接替代项目自己的证据和实验。
- 不要求阅读整个 Vault；从入口按任务读取。

## Obsidian 与 GitHub

将仓库根目录作为 Obsidian Vault 打开。新文件默认进入 `07-Inbox`，内部链接使用普通 Markdown 相对路径或 Obsidian 双向链接均可。

GitHub 也应能完整阅读主要导航；文档不能依赖只有本机才存在的插件或数据库。

## 当前技术方向

- TypeScript / Node.js：目标在线权威运行时；
- Python：当前实现，以及未来的研究、评估、离线认知和本地模型；
- Rust：高风险、原生和安全隔离的执行边界；
- SQL / SQLite：事实、状态、记忆、任务、Trace 和检索基础。

详细理由见 [语言与运行时](02-System/Language-and-Runtime.md) 和 [D-003](05-Decisions/D-003-Language-Roles.md)。
