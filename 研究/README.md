# 当前研究

## Objective

弄清两个产品的长期目的、已经形成的功能和算法、原实现的重复机械，以及第三方真正提供的能力。在此基础上修订 Specs，形成可执行的整体架构和基础设施方案，再由当前 Coding Agent 实施。

## Decisions

- 需求以项目宪纲和用户当前修正为准；Vault 原文只压缩归档，不查看、不参考。
- 原 master、重建分支、历史批注分别作为实现事实、错误施工事实和调查线索，功能是否保留依据产品需求判断。
- NousQL 恢复既有语言语义；检索保全 VCP 和 Nous 的数学/算法合同；Prompt 作为资源；Hept 拥有世界映射，Nous 拥有通用认知时间合同。
- AstrBot 的管理与机制是研究素材，可选通信插件成果继续保留；Hept 的主体运行仍由 Hept 负责。
- 当前阶段不修改两个产品生产代码。下载、缓存与实验进入 `temp/spec-research/`，已有 `data/` 原地读取。

## Current Work

已完整阅读宪纲并核对历史批注/源码索引，调查master的查询检索、时间生活、消息媒体、Prompt/模型/配置/运行底座；核对MaiBot、AstrBot、OpenClaw、QQContextBot和核心依赖。已将实际行为、消费者、采用与替换决定整合到[架构](../设计/整体架构与模块合同.md)、[基础设施](../设计/基础设施/README.md)、[依赖来源](../依赖来源.md)和[施工顺序](../施工顺序.md)。当前收尾为合同、图、示例和内部链接一致检查及设计提交；产品生产代码未改。领域算法的质量/规模测量与完整行为施工按既定顺序继续。

| 研究材料 | 负责问题 |
|---|---|
| [目的与能力保全](目的与能力保全.md) | 产品目的、完整行为和架构取舍的判断依据 |
| [Nous 查询与检索](Nous查询与检索.md) | 既有语言、绑定、通道、算法与基础设施消费者 |
| [Hept 时间生活与消息](Hept时间生活与消息.md) | 通用时间、世界时间、持续生活、复杂消息和媒体 |
| [第三方模型 Prompt 与管理](第三方模型Prompt与管理.md) | 旧 Prompt、MaiBot/AstrBot/OpenClaw 的实际机制 |
| [基础设施与现有结构](基础设施与现有结构.md) | 配置、网络、存储、事务、生命周期及通用依赖 |

## 源码基线

| 仓库 | 本次核实的版本 |
|---|---|
| Nous 原 master | `412b062082afb75ccfae4c3f69fc606d3e3cc862` |
| Nous feat/spec-rebuild | `aee6a9f3fa870f226c67eb518072ef1343003a1f` |
| Hept 原 master | `21f0080460f3ee639deb9f5ea47282fb6c59df95` |
| Hept feat/spec-rebuild | `ddc0a8706468ad66b493bbc75a612b19993773b0` |

Nous调查时已有四个旧`.agents/skills/`文件暂存删除；用户已确认删除，现提交为`1e2f7a84`，没有修改产品生产源码。上表Nous重建提交是本轮核对功能时的检查点，其后的该提交仅删除这些技能文件。Hept工作树初始及本轮结束均干净。两个master只读工作树放在`temp/spec-research/nous-original`和`hept-original`；QQContextBot等研究副本放在同一临时根。

当前客户端与代码基线使用 Node 24、TypeScript 7、AI SDK 7、DBOS 5.3。具体依赖是否适合由实际源码、API 和消费者判断。
