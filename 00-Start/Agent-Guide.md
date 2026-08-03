# AI Agent 阅读与工作指南

本文件是所有参与 Heptalogos 的 AI Agent 的默认入口。

## 最小阅读顺序

开始任何较大任务前，依次读取：

1. `00-Start/README.md`
2. `01-Vision/Project-Vision.md`
3. `02-System/System-Overview.md`
4. `00-Start/Current-State.md`
5. 与任务相关的 `03-Concepts/` 或 `04-Engineering/` 文档
6. `05-Decisions/Decision-Index.md` 中相关决定

不要默认扫描整个 Vault。需要历史理由时再查看 Git 历史。

## 信息优先级

发生冲突时按以下顺序判断：

1. 当前代码、测试和真实数据；
2. `00-Start/Current-State.md`；
3. `02-System/` 和 `04-Engineering/` 中标为当前的内容；
4. `05-Decisions/` 中仍有效的决定；
5. `03-Concepts/` 中的目标模型；
6. `06-Research/` 中尚未验证的想法；
7. `07-Inbox/` 中未整理的输入。

文档不能覆盖代码事实，概念目标也不能冒充当前实现。

## 工作方式

- 先确认任务属于当前实现、目标设计还是研究实验。
- 保留 Heptalogos 的领域词汇，不用通用 Agent 框架术语替换核心概念。
- 平台 SDK、模型 SDK 和框架对象不得成为核心领域类型。
- 新设计优先更新相关主题文档；只有跨系统且长期稳定的选择才新增 Decision。
- 小修正直接修改正文，不为每次变更制造审批记录。
- 不确定内容写成“开放问题”或放入 `07-Inbox/Questions.md`。
- 引用外部资料时写明来源和可借鉴点，不把参考项目整体当作方案。

## 输出要求

提出架构或实现建议时，至少说明：

- 解决什么问题；
- 影响哪些领域和权威边界；
- 哪些状态或事实由谁拥有；
- 失败、取消、重启和回放如何处理；
- 哪些内容是事实，哪些是推断或建议。

## 禁止事项

- 不把 Heptalogos 简化为聊天机器人或单次 ReAct Agent。
- 不让模型输出直接发送、直接写长期事实或直接提升权限。
- 不让 Python、TypeScript、Rust 等不同运行时共同拥有同一权威状态。
- 不因语言、框架或数据库偏好任意拆分服务。
- 不保存或披露隐藏思维链；Trace 应记录结构化输入、决定、理由代码和结果。
