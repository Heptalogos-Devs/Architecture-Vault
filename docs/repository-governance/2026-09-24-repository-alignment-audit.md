# Heptalogos / Nous Wave 仓库与文档对齐审查

审查日期：2026-09-24

本文件记录 Architecture-Vault、Heptalogos、Nous Wave 及组织内历史项目之间的当前事实关系，并提出非破坏性的整改顺序。它是仓库治理审查，不替代各项目自己的 Architecture / Specs。

## 1. 审查结论

当前最重要的问题不是代码“散落在两个账号”本身，而是 **同名仓库与文档入口仍然向外表达多个互相矛盾的 current truth**：

- `ArsvineZhu/Heptalogos` 已经演化为当前 Product Host / Foundation / Product-Subject 架构；
- `Heptalogos-Devs/Heptalogos` 停留在更早的 Interaction/Reactor/Control Plane 实现代，却仍未 archive；
- Architecture-Vault 已正确把现行 Heptalogos 文档入口指向个人仓库，但 Nous Wave 报告中仍有少量上一代 Heptalogos/OpenClaw 描述；
- `ArsvineZhu/Nous-Wave` 是当前 Nous Wave 实现仓库，组织中尚不存在同名 Nous Wave 仓库；
- BionicBot、Anthro、QQContextBot 是明显早于当前 Heptalogos / Nous Wave 架构的独立原型或前身，但仍作为普通 active repositories 展示。

因此应先建立 source-of-truth 与 successor 关系，再执行 rename/archive/transfer。不要直接删除历史仓库，也不要把两个 Heptalogos 代码树做普通 Git merge。

## 2. 当前仓库矩阵

| 仓库 | 最近审查到的代码基线 | 当前判断 | 建议角色 |
|---|---|---|---|
| `Heptalogos-Devs/Architecture-Vault` | main `4f56fb7` 起，本次分支继续更新 | 当前跨项目研究/架构资料库 | **保留为 canonical Architecture/Research Vault** |
| `ArsvineZhu/Heptalogos` | `a5287a0`，2026-09-03 | 当前 Heptalogos 产品/工程代 | **最终迁入组织并成为 `Heptalogos-Devs/Heptalogos`** |
| `Heptalogos-Devs/Heptalogos` | `e00fea7`，2026-08-07 | 旧实现代，和个人当前仓库不是简单快进关系 | **改名 + successor notice + archive** |
| `ArsvineZhu/Nous-Wave` | `e9af4ebd`，2026-09-23 | 当前 Nous Wave 研究实现 | **最终迁入 `Heptalogos-Devs/Nous-Wave`** |
| `Heptalogos-Devs/BionicBot` | `686cc57`，2025-12-19 | 早期 QQ bot 原型 | 若无独立维护需求，标记 predecessor 后 archive |
| `Heptalogos-Devs/Anthro` | `e0e224a`，2026-01-13 | 早期消息重要度/摘要/向量库实验系统 | 若无独立研究用途，标记 historical experiment 后 archive |
| `Heptalogos-Devs/QQContextBot` | `5da9fe5`，2026-06-06 | 较完整的 QQ recorder + multi-tool agent 原型 | 保留作 predecessor/data-pipeline reference 或 archive；不要称 current Heptalogos |
| `Heptalogos-Devs/mid-term-paper` | 单独中期材料仓库 | 当前交付辅助仓库 | 继续独立维护，引用 canonical code/docs 而不复制架构 Authority |
| `.github` / `.github-private` | 组织治理仓库 | 组织元数据/配置 | 保留 |

“archive”表示 GitHub Archive + 明确 successor banner，而不是删除。是否仍有真实用户、部署、外部链接或独立研究价值，需要在执行前人工确认。

## 3. Heptalogos 文档漂移

### 3.1 当前个人仓库已经是另一代架构

`ArsvineZhu/Heptalogos` 当前 README、Project Charter、Constitution、`docs/architecture/` 与 `specs/` 已经形成新的工程结构：

- Foundation closed；
- headless Product Host + initial Management surface；
- current development 进入 Product/Subject path；
- Subject != Model；State > Prompt；Proposal != Authority；
- Advanced Cognition 不由 Foundation 内部实现，而通过稳定 contracts 接入；
- OpenClaw 属独立 Machine Operations Plane，不是 Subject cognition runtime。

因此 Vault 或其他文档若仍描述旧组织仓库中的 `Interaction -> Reactor -> Control Plane` 为“当前 Heptalogos”，或者把 OpenClaw 描述为当前 Subject cognition owner，均应标记过期。

### 3.2 与最新 Nous Wave 研究仍有未同步处

个人 Heptalogos 当前 Constitution/advanced-cognition seam 的原则仍然合理：Foundation 不应冻结 Memory、Persona、Relationship 等内部模型。但最新 Nous Wave 研究已经更进一步确定：

- Nous Wave 是可组合的 Subject Cognition & Personality Platform，而不仅是 Memory service；
- 顶层 cognition owners 目标为 Memory / Self / Social / Motivation / Runtime；
- Persona 属 Self；
- Social 至少拥有 RelationshipGraph 与 LanguageConvention；
- Goal 属 Nous Motivation，binding Commitment / Action / Effect 属 Heptalogos；
- H 应把 Nous Wave 视作这些高级 cognition capability 的优先具体 owner/provider，而不是未来在 H Foundation 内重新发明对应 ontology。

这些内容应通过新的跨项目 integration contract 同步到 Heptalogos，而不是直接把 Nous 内部 schema 复制进 H。

## 4. Architecture-Vault 的角色

建议固定三层知识 Authority：

1. **Architecture-Vault**：跨项目研究、系统边界、长期架构、正式研究报告、跨仓 migration/audit；
2. **Heptalogos repo**：Heptalogos 当前可执行 Architecture / Specs / Plans / Qualification / code truth；
3. **Nous-Wave repo**：Nous Wave 当前可执行 Architecture / Decisions / Specs / code truth。

Vault 不应复制两个项目所有 implementation spec；项目仓库也不应各自保存互相冲突的跨项目研究长文。跨系统的 owner/boundary 结论先在 Vault 收敛，再分别下降到 H/NW 的 executable specs。

## 5. 推荐迁移顺序

### Phase A — 先修真值，不移动仓库

1. 合并本次 Architecture-Vault 文档更新。
2. 在 Vault 根 README 明确 current code repositories 与旧组织仓库状态。
3. 更新 Nous Wave 报告中的 H/OpenClaw/current SHA 描述。
4. 在个人 Heptalogos 与 Nous-Wave 后续 Architecture re-authoring 中引用 Vault 当前跨系统边界。
5. 确认中期材料只引用当前 personal repo SHAs / Vault report，不再引用旧组织 H 为 current。

### Phase B — 给历史仓库加 successor notice

在任何 archive/rename 前，为旧仓库 README 顶部加入类似：

> Historical predecessor / archived implementation generation. Current Heptalogos development continues at `<canonical repo>`.

至少处理：

- `Heptalogos-Devs/Heptalogos`
- `Heptalogos-Devs/BionicBot`
- `Heptalogos-Devs/Anthro`
- `Heptalogos-Devs/QQContextBot`（若决定不再独立维护）

不要删除 release/tag/issue/history。

### Phase C — 解决 Heptalogos 名称冲突

组织已经占用 `Heptalogos-Devs/Heptalogos`，因此个人当前仓库不能直接以同名 transfer 进入组织。推荐：

1. 冻结迁移窗口，记录两仓 HEAD、open issues/PR、release/tag、Actions、Pages、deploy hooks、secrets/environment、branch settings；
2. 将旧组织仓库改名为明确的历史名称，例如 `Heptalogos-legacy-pre-rebase`（最终名字由维护者决定）；
3. 在旧仓库 README 写 successor URL 后 archive；
4. 把 `ArsvineZhu/Heptalogos` transfer 到 `Heptalogos-Devs`，保留 canonical name `Heptalogos`；
5. 核对 GitHub redirect、Actions/permissions、package/container links、submodule/remote、文档和部署配置；
6. 更新 Vault / org profile / mid-term-paper 的 canonical links。

不建议把两个 Heptalogos 仓库 merge 后再迁移；旧组织仓库是历史实现代，应作为 lineage 保存，而不是污染当前代码历史。

### Phase D — 迁移 Nous Wave

组织目前没有 `Nous-Wave` 名称冲突。Memory Reference Profile 的 Architecture/Spec 稳定后，可把 `ArsvineZhu/Nous-Wave` transfer 为 `Heptalogos-Devs/Nous-Wave`。迁移前同样检查 Actions、Pages、packages、webhooks、deploy keys、branch rules、external links 和本地 remotes。

将迁移与大规模 semantic rebase 分开提交/操作：先保证仓库身份迁移可逆和可验证，再开始 code architecture rebase，避免出问题时无法判断原因来自 GitHub governance 还是代码变化。

### Phase E — 清理组织历史项目

对于 BionicBot / Anthro / QQContextBot，逐个作“仍是独立产品吗？”判断：

- 若没有部署、用户、独立研究线或维护计划：加 predecessor notice 后 archive；
- 若仍有独立用途：保留，但 README 明确“不是当前 Heptalogos / Nous Wave”，并说明与新项目的关系；
- 不为了“组织看起来整洁”删除历史源码。

## 6. 建议的最终组织形态

```text
Heptalogos-Devs/
├── Heptalogos                 # current product / agency runtime
├── Nous-Wave                  # current cognition/personality platform
├── Architecture-Vault         # cross-project research and architecture
├── mid-term-paper             # project deliverable, if still useful
├── .github
├── .github-private
└── archived predecessors
    ├── Heptalogos-legacy-pre-rebase
    ├── BionicBot
    ├── Anthro
    └── QQContextBot            # if no longer independently maintained
```

GitHub 实际 archive repository 仍位于组织根列表，不会真的形成 `archived predecessors/` 目录；上图表示逻辑分类。

## 7. 文档整改优先级

### P0 — 立即消除 current-truth 冲突

- Vault Nous report：当前 H/NW SHA、Social/CognitiveSchema/Memory taxonomy、Anchor、UseEvent、retrieval 状态；
- Vault Heptalogos entry：明确个人仓库是当前实现，组织同名仓库是旧实现代；
- current PDF 在重编译前标记为 generated artifact that may lag source；
- 中期材料引用当前仓库与当前 report source。

### P1 — Architecture re-authoring

- Nous Wave：重写 `ARCHITECTURE.md`、`DECISIONS.md`、Memory executable Spec；
- Heptalogos：补充明确的 Nous Wave cognition-provider integration decision/spec，不把 NW 内部 ontology复制进 Foundation；
- 两边共享跨系统合同：Subject provisioning、Observation、Context、Goal/Commitment、Use/Outcome、Maintenance。

### P2 — 仓库迁移与归档

完成 successor notices、迁移检查表和回滚点后，再执行 rename/archive/transfer。

## 8. 本次未执行的破坏性操作

本次审查只更新 Architecture-Vault 设计和治理文档，没有执行：

- repository rename；
- repository transfer；
- GitHub archive；
- 删除旧仓库/分支/历史；
- 修改 Heptalogos/Nous-Wave 代码；
- 更改 Actions/secrets/branch rules。

这些操作应在维护者确认最终名称与迁移窗口后独立执行，并在每一步记录前后 repository id、HEAD 与验证结果。
