# 基础设施施工 Goal

## Objective

以完整既有能力为目标，先完成 Nous Wave 与 Heptalogos 可独立运行的公共底座，再接回认知与生活领域。减少自有机械、重复状态、跨层流程和维护成本；保留宪纲要求、旧功能与有效算法。当前研究和方案在本目录，实际施工按[顺序](施工顺序.md)推进。

## Decisions

- 宪纲最高；当前Specs为设计入口，原Vault仅压缩归档。原master用于恢复能力和迁入源码，feat/spec-rebuild为具体纠偏对象。
- 两个TS/Node产品、两个权威数据库；共享普通platform/contracts/client/management-ui发行包。跨产品只用正式SDK，不依赖相邻仓库。
- 通用机制优先采用成熟库；可迁入的旧算法、Prompt、保真消息和第三方功能组先复制再改编。OpenClaw保持原生执行/工具/历史，DBOS只负责真正持久工作。
- NousQL保持自然语言和语法岛；VCP/Native数学与Rust实现继续利用。Prompt是正式资源；世界分段时钟归Hept，通用认知时间归Nous。
- 所有真实调用从第一条链就携带配置、权限、时间、费用和trace。未知外部效果先核实原操作。一个事实一个owner，没有兼容、双写或旁路。

## Current Work

当前已实施共享Bootstrap、storage、settings、credentials、network、Prompt、五族Models与两产品Time owner；正在闭合OpenClaw逐调用/Worker委派、统一管理入口与独立发行制品。空安装CLI/HTTP、单连接事务与当前授权、正式SDK/DBOS恢复、Clock分段/DST/期限和调用数据恢复已通过真实场景。详细未完能力以两个产品的docs/construction.md为准。

下一步完成原生闭环，再按[施工顺序](施工顺序.md)补齐完整媒体/扩展、Web与i18n、全部owner数据生命周期和跨平台发行；完整NousQL/VCP/认知与生活领域在基础底座可用后施工。未经授权的FIND/RETURN替代DSL已从当前代码和专属测试删除；现行普通自然语言与结构化检索保留，正式语言仍沿原master语法岛合同迁入。

每个单元交付实际操作和管理入口，同步类型、生产者、消费者、资源和文档，删除被替代实现。下载、缓存、实验安装放工作区temp；已有data研究资料就地读取。以少量真实场景和必要规则验证完成行为，不建设新的运行/测试平台。
