# 研究报告来源映射

## 资料基线与采用顺序

研究语义基线为完整的 `Nous_Wave_Current_Research_Package_2026-09-22` 目录，其中 15 份编号 Markdown、`MANIFEST.md` 和 `SHA256SUMS.json` 均已整理；清单列出的 16 个文件校验值全部匹配。

当前目标语义依据研究资料包；实现状态依据相应代码与配置；原始项目目标依据正式申报书；学校流程依据教务处通知、立项名单、中期审核表和填报指南。Nous Wave 代码基线为 HEAD `9794f44`，检视时工作区包含已暂存和未暂存改动；Heptalogos 代码基线为 HEAD `2f86311`，检视时工作区干净。

## 总报告章节来源

| 报告章节 | 主要研究资料 | 实现或外部来源 |
|---|---|---|
| 1. 研究对象与问题 | `00_START_HERE`；`01_MASTER_CURRENT_RESEARCH_SPEC` 第 1–2 节 | Nous Wave README；Heptalogos 产品与 Subject 包 README |
| 2. 研究原则与不变量 | `00_START_HERE`；`01_MASTER` 第 9–13 节；`10_RESEARCH_EVIDENCE_AND_EXPERIMENTS` 第 1 节 | `docs/Nous_Wave/ARCHITECTURE.md`；`crates/memory-domain/src/lib.rs` |
| 3. 主体、领域与权属 | `01_MASTER` 第 3–8 节；`02_DOMAIN_AND_AUTHORITY_MODEL` | `docs/Nous_Wave/DECISIONS.md`；主体架构与规格文件 |
| 4. 记忆语义模型 | `01_MASTER` 第 11–12 节；`02_DOMAIN_AND_AUTHORITY_MODEL` 第 4–6、12 节；`04_MEMORY_EPISODE_JOURNAL_SCHEMA` 第 1–5 节 | `crates/memory-domain/src/lib.rs`；记忆服务实现；`202609170003_memory_semantics.sql` |
| 5. 经历、日记、标签与图式 | `01_MASTER` 第 12–13 节；`04_MEMORY_EPISODE_JOURNAL_SCHEMA` 第 6–11 节；`11_OPEN_RESEARCH_QUESTIONS` 第 3 问 | `crates/memory-service/src/topology.rs`；`crates/authority-store/src/topology_input.rs` |
| 6. 自我与人格 | `01_MASTER` 第 5.2、8、21 节；`02_DOMAIN_AND_AUTHORITY_MODEL` 第 7–8 节；`11_OPEN_RESEARCH_QUESTIONS` 第 1 问 | McAdams 与 Pals 2006；McAdams 与 McLean 2013；Conway 与 Pleydell-Pearce 2000 |
| 7. 关系认知 | `01_MASTER` 第 5.3 节；`02_DOMAIN_AND_AUTHORITY_MODEL` 第 9 节；`11_OPEN_RESEARCH_QUESTIONS` | Baldwin 1992；Heptalogos Subject 规格 |
| 8. 动机与行为权限 | `01_MASTER` 第 5.4、7 节；`02_DOMAIN_AND_AUTHORITY_MODEL` 第 10 节；`07_RESOURCES_PROVIDERS_HEPTALOGOS` 第 8–12 节 | Rao 与 Georgeff 1995；Singh 1997、1999；Heptalogos Subject 包 |
| 9. 认知运行时与上下文 | `01_MASTER` 第 5.5、14–15 节；`03_COGNITIVE_RUNTIME_AND_CONTEXT` | `crates/cognitive-runtime/src/query`；`working_set.rs`；`apps/nous-core/src/cognition` |
| 10. 离线认知 | `01_MASTER` 第 16 节；`05_DREAM_HYPOTHESIS_OFFLINE_COGNITION` | Heptalogos `reaction-behavior.md`；Nous Dream 工作流的实现状态见代码差距章节 |
| 11. 检索语义 | `01_MASTER` 第 17 节；`06_RETRIEVAL_SERVING_AND_ALGORITHMS` 第 1–6 节 | `crates/cognitive-runtime/src/query/plan.rs`；`crates/memory-service/src/query.rs` |
| 12. 检索服务表示 | `01_MASTER` 第 9、17 节；`06_RETRIEVAL_SERVING_AND_ALGORITHMS` 第 5–7、15–16 节 | `dense.rs`；`lexical.rs`；`crates/authority-store/src/serving.rs` |
| 13. 联想检索与算法 | `06_RETRIEVAL_SERVING_AND_ALGORITHMS` 第 7–13 节；`10_RESEARCH_EVIDENCE_AND_EXPERIMENTS` 第 2–6 节；`13_EVIDENCE_INDEX` | `seams.rs`、`cue_sensing.rs`、`residual.rs`、`wave.rs`、`ranking.rs`；VCPToolBox commit `6a91ca5` |
| 14. 外部知识资源 | `01_MASTER` 第 18 节；`07_RESOURCES_PROVIDERS_HEPTALOGOS` 第 1–3 节；`10_RESEARCH_EVIDENCE_AND_EXPERIMENTS` 第 6 节 | `crates/cognitive-runtime/src/resources`；Heptalogos `ai-runtime.md` |
| 15. 模型服务与 Heptalogos | `01_MASTER` 第 3、18、20 节；`07_RESOURCES_PROVIDERS_HEPTALOGOS` 第 4–14 节 | `apps/nous-core/src/model`；`apps/nous-kernel`；Heptalogos 产品宿主及 `SubjectCognitionRuntime` 适配器 |
| 16. 持久化、并发与可靠性 | `01_MASTER` 第 19 节；`08_PERSISTENCE_CONCURRENCY_RELIABILITY` | `crates/authority-store/migrations`；投影和服务实现；`memory_lifecycle.rs` |
| 17. 物理架构 | `01_MASTER` 第 20 节；`09_PHYSICAL_ARCHITECTURE_AND_IMPLEMENTATION` | Nous Wave README、工作区清单、TypeScript Core、Rust Kernel、Heptalogos 产品宿主 |
| 18. 当前实现与目标差距 | `14_CURRENT_STATUS_MATRIX`；`09_PHYSICAL_ARCHITECTURE_AND_IMPLEMENTATION` | Nous Wave HEAD `9794f44` 与检视时工作区；Heptalogos HEAD `2f86311` 及资格记录 |
| 19. 证据与实验 | `10_RESEARCH_EVIDENCE_AND_EXPERIMENTS`；`13_EVIDENCE_INDEX` | 算法实现路径；试验摘要对应原始材料列入后续归档 |
| 20. 待解决问题 | `11_OPEN_RESEARCH_QUESTIONS`；`14_CURRENT_STATUS_MATRIX` | 当前语义规格与实现状态 |
| 21. 研究与实现路线 | `01_MASTER` 第 22 节；`09_PHYSICAL_ARCHITECTURE_AND_IMPLEMENTATION` 第 12 节 | 当前目标资料包；按依赖关系组织的后续工作 |
| 附录 | `12_GLOSSARY`；`13_EVIDENCE_INDEX`；`14_CURRENT_STATUS_MATRIX`；`MANIFEST` | SHA-256 校验记录、代码与资格记录 |

## 两份报告的内容安排

总报告依照研究依赖组织：问题与不变量（第 1–2 章），领域对象和运行时（第 3–10 章），查询、服务表示、算法与资源（第 11–15 章），持久化与物理架构（第 16–17 章），实现对照与证据（第 18–19 章），待解决问题与路线（第 20–21 章）。术语表、状态矩阵、不变量与数据流、复现信息作为附录。

中期报告按项目评审逻辑独立组织：项目概况、申报目标、已开展工作、阶段成果、原型、代表性认识、资格记录、项目问题、下一步计划、经费与成员分工、中期自评。报告以进展和成果证据为主线，不按总报告章节裁剪正文。

## 证据表达规则

- 目标设计对应研究资料包；实现状态对应代码路径和仓库基线。
- `PASS` 对应有日期、平台和范围的既有资格记录。
- 算法数值对应研究资料包中的试验摘要，原始脚本和输出纳入后续归档。
- Heptalogos 资格记录描述其对应本地路径；跨系统集成状态以两仓库实现对照说明。
- 项目编号、获批总额、个人支出和成员贡献据项目负责人提供的系统字段与阶段记录整理。
