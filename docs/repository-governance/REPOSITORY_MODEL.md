# 仓库组织模型

## 目标仓库

### Heptalogos-Devs/Architecture-Vault

长期目标设计、设计决定、论证、研究和跨系统合同。负责生成目标设计 PDF。

### Heptalogos-Devs/Heptalogos

Heptalogos 当前产品代码、Specs、Plans、Qualification、工程治理和当前实现文档。

### Heptalogos-Devs/Nous-Wave

Nous Wave 当前代码、Specs、Plans、Qualification、工程治理和当前实现文档。

### Heptalogos-Devs/mid-term-paper

大创中期材料。它消费项目设计和实现事实，不成为架构权威。

## 迁移

当前个人仓库 `ArsvineZhu/Heptalogos` 和 `ArsvineZhu/Nous-Wave` 是当前开发来源。迁移到组织后使用上面的 canonical 名称。

现有组织仓库 `Heptalogos-Devs/Heptalogos` 保存较早实现。迁移当前仓库前先将旧仓库改名为 `Heptalogos-legacy` 并归档，随后把个人当前仓库转移到组织并保持 `Heptalogos` 名称。

Nous Wave 在组织内没有同名当前仓库，可直接转移。

## 旧项目

`BionicBot` 与 `Anthro` 属于早期实验项目，完成说明后归档。

`QQContextBot` 保留为独立的历史、数据与协议参考项目；如果已经不再维护，同样归档，但不把它视为当前 Heptalogos 或 Nous Wave 的实现分支。

归档仓库只保留历史代码和提交记录，不继续维护当前架构文档。

## 文档链接

迁移完成后，Vault 和组织主页只链接 canonical 组织仓库。代码仓库中的长期设计链接指向 Architecture-Vault，不保留复制正文。
