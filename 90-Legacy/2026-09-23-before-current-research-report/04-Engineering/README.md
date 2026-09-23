# Engineering

本目录描述当前实现与近期工程工作。它比 `03-Concepts/` 更接近代码，比主仓库 README 更侧重跨模块设计。

## 文档

- [当前实现](Current-Implementation.md)：现有三个模块和真实边界。
- [近期工作](Near-Term-Work.md)：下一阶段可执行的系统切片。
- [接口与 Schema](Interfaces-and-Schemas.md)：领域契约、版本和跨语言规则。
- [测试与回放](Testing-and-Replay.md)：单元、场景、故障和评估方式。

## 使用规则

- 代码和测试是当前实现的最终事实来源。
- 本目录不复制每个类或配置项；只描述跨模块责任和工程约束。
- 功能完成、删除或改变边界时同步更新相关文档和 `00-Start/Current-State.md`。
- 临时实现方案不必写入 Decision，除非它影响长期数据或多个模块。
