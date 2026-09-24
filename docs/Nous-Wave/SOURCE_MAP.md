# 研究报告来源映射

## 资料基线与采用顺序

研究总报告以 `Nous_Wave_Current_Research_Package_2026-09-22` 的完整研究资料作为基础语义来源，并纳入 2026-09-24 对 Memory taxonomy、CognitiveSchema、Social Cognition、UseEvent、accessibility 与 retrieval 的进一步设计收敛。报告正文只描述当前有效设计，不保留研究轮次叙事；本文件负责记录来源和实现快照边界。

当前目标语义依据本报告和其研究资料；实现状态依据实际仓库源码与配置；Heptalogos 产品语义以当前个人仓库中的 Charter、Constitution、Architecture 与 Specs 为准；学校项目目标依据正式申报书与教务处材料。

当前代码快照：

- Nous Wave：`ArsvineZhu/Nous-Wave@e9af4ebd8a77d316c78764fd85836e6de8d9b7ee`（2026-09-23）。该提交包含此前未推送的 Memory semantic closure 等改动；GitHub 未显示对应 CI/status check，因此报告只把可定位实现记为实现事实，不新增 PASS 资格结论。
- Heptalogos：`ArsvineZhu/Heptalogos@a5287a01b42e3d09f445e96982caf6842ed74674`（2026-09-03），作为当前产品/架构仓库基线。
- `Heptalogos-Devs/Heptalogos@e00fea73feb67741e6637123deb2c56886961ba7`（2026-08-07）属于更早实现代，不作为当前 Heptalogos 产品 Authority；其去留与改名见仓库治理审查。

## 总报告章节来源

| 报告章节 | 主要研究/设计来源 | 实现或外部来源 |
|---|---|---|
| 1. 研究对象与问题 | 当前研究资料包；当前报告设计收敛 | Nous Wave README；Heptalogos Charter/Constitution |
| 2. 研究原则与不变量 | 当前研究资料包；COST / Library-First 方法 | Nous Wave / Heptalogos 治理文件 |
| 3. 主体、领域与权属 | 当前研究资料包；2026-09-24 owner/authority 收敛 | Heptalogos `project-charter.md`、`constitution.md`、`subject.md`、`research-subsystem-integration.md` |
| 4. 记忆语义模型 | 研究资料包；2026-09-24 Memory taxonomy/accessibility 收敛 | `memory-domain`、`memory-service`、Authority migrations |
| 5. 经历、日记与图式 | 研究资料包；2026-09-24 CognitiveSchema/Anchor 收敛 | 当前 Tag/Anchor/Association/Topology 源码；后者用于记录实现差距 |
| 6. 自我与人格 | 研究资料包 | McAdams/Pals；McAdams/McLean；Conway/Pleydell-Pearce |
| 7. 社会认知 | 2026-09-24 Social/Relationship/LanguageConvention 设计收敛 | Baldwin relational schemas；当前 Heptalogos advanced-cognition integration seam |
| 8. 动机与行为权限 | 研究资料包 | Rao/Georgeff；Singh；Heptalogos behavior authority |
| 9. 认知运行时与上下文 | 研究资料包；2026-09-24 UseEvent/accessibility 收敛 | `cognitive-runtime`、Host/Kernel runtime；Heptalogos Reaction/Context architecture |
| 10. 离线认知 | 研究资料包 | Heptalogos maintenance/advanced cognition boundary |
| 11. 检索语义 | 研究资料包；2026-09-24 fixed-plan fusion 收敛 | `query/plan.rs`、`ranking.rs`、Memory query/serving code |
| 12. 检索服务表示 | 研究资料包 | lexical/dense/serving generation code |
| 13. 联想检索与算法 | 研究资料包与算法实验摘要 | EPA/Residual/Wave/Ranking 当前源码；VCPToolBox lineage |
| 14. 外部知识资源 | 研究资料包 | Resource Awareness 实现；外部 KB/Resource 适配研究 |
| 15. 模型服务与 Heptalogos | 研究资料包；当前 NW/H owner boundary | Nous Core/Kernel provider seams；Heptalogos Product Host、AIRuntime、Machine Operations architecture |
| 16. 持久化、并发与可靠性 | 研究资料包 | PostgreSQL schema、projection serving、lifecycle 实现 |
| 17. 物理架构 | 研究资料包 | Nous workspace/Host/Kernel；Heptalogos Product Host current tree |
| 18. 当前实现与目标差距 | 本次代码审查 + 当前研究状态 | Nous `e9af4ebd`；Heptalogos `a5287a0`；组织旧 H `e00fea7` |
| 19. 证据与实验 | 研究资料包实验章节 | 对应算法源代码；原始脚本/输出仍应进一步归档 |
| 20. 待解决问题 | 当前报告设计状态 | 当前代码/Spec 差距 |
| 21. 研究与实现路线 | 当前依赖关系与 2026-10-27 中期交付目标 | Memory Reference Profile 的可继承代码基础 |
| 附录 | 当前术语、状态矩阵、不变量和数据流 | 当前仓库/实现快照 |

## Heptalogos 来源边界

Vault 中的旧 Heptalogos Knowledge Base 位于 `docs/Heptalogos/archive/`，仅用于历史检索。当前 Heptalogos 产品架构和规范来源是 `ArsvineZhu/Heptalogos`：

1. `AGENTS.md`
2. `project/governance/project-charter.md`
3. `project/governance/constitution.md`
4. `docs/architecture/**`
5. `specs/**`
6. 当前 code / qualification

组织内旧 `Heptalogos-Devs/Heptalogos` 不得继续被报告或 Vault 当成当前代码事实来源。

## 证据表达规则

- 设计结论、目标实现、已实现代码、已运行实验与资格 PASS 分开表达。
- `IMPLEMENTED` 仅表示当前源码存在相应路径；`VALIDATED`/`PASS` 需要对应运行证据。
- 研究资料包中的合成实验数字保留其原条件与限制，不升级为端到端效果结论。
- 最新设计对旧代码的否定不意味着旧代码全部删除；报告在第十八章区分可直接继承、需重设语义和应替换的部分。
- 当前 PDF 是生成制品；源文件发生设计更新后，在重新 clean build 前不把旧 PDF 当作最新文档快照。
