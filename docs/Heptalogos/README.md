# Heptalogos

Architecture-Vault 只保存 Heptalogos 的跨项目研究入口与历史知识库快照；现行产品 Architecture、Specs、Plans、Qualification 和实现维护在当前工程仓库。

## 当前工程来源

当前 Heptalogos 产品/工程 Authority：

- [ArsvineZhu/Heptalogos](https://github.com/ArsvineZhu/Heptalogos)
- 当前审查基线：`a5287a01b42e3d09f445e96982caf6842ed74674`（2026-09-03）
- 建议阅读顺序：`AGENTS.md` → `project/governance/project-charter.md` → `project/governance/constitution.md` → `INDEX.md` → `docs/architecture/` / `specs/` → current code/qualification。

个人仓库当前已经进入 headless Product Host / Product-Subject path；OpenClaw 在当前架构中属于独立 Machine Operations Plane，不是 Subject cognition runtime。Advanced Cognition 通过 Foundation 的 Service/Capability、Context/Activity contribution、Evidence/provenance 与 authority ceiling 接入；Memory/Self/Social/Motivation 等内部 ontology 由 Nous Wave 等认知系统负责，不应复制进 Foundation。

## 组织内旧 Heptalogos 仓库

`Heptalogos-Devs/Heptalogos` 当前最新审查提交为 `e00fea73feb67741e6637123deb2c56886961ba7`（2026-08-07），属于更早的 Interaction/Reactor/Control Plane 实现代。它目前尚未 archive，但**不作为 current Heptalogos product truth**。

后续计划是先为旧组织仓库加入 successor notice 并改名/归档，再把个人当前仓库迁入 `Heptalogos-Devs` 取得 canonical `Heptalogos` 名称。具体步骤见：

- [仓库与文档对齐审查](../repository-governance/2026-09-24-repository-alignment-audit.md)

在迁移完成前，文档和中期材料都应显式引用 `ArsvineZhu/Heptalogos`，避免同名仓库造成歧义。

## Vault 历史资料

旧 Architecture-Vault Knowledge Base 作为历史资料保留：

- [2026-09-23 旧知识库快照](archive/2026-09-23-before-current-research-report/README.md)
- 更早审批式目录可通过 Git 历史（如 `6d5497f85a9230909f43827e86216fe50d0e5311`）检索。

这些材料用于追溯概念来源，不覆盖当前 Heptalogos 仓库中的 Charter、Constitution、Architecture 或 Specs。
