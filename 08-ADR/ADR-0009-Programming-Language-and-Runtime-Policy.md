---
title: "ADR-0009 编程语言与运行时政策"
status: accepted
type: adr
confidentiality: internal
created: 2026-07-23
updated: 2026-07-23
tags:
  - adr
  - language-policy
  - runtime
---

# ADR-0009 编程语言与运行时政策

## 状态

`accepted`

## 背景

Heptalogos 的早期不确定性集中在人格、记忆、消息聚合、行为策略和评估方法。项目同时需要可审计的持久化与调试控制面，但不能因预期中的性能或多平台需求提前形成多语言微服务。

## 决策

- Python 3.12+ 是认知运行时、实验、状态、记忆、调度和评估的主语言。
- TypeScript 用于 Web 控制面；仅当平台 SDK、故障域、权限或独立部署需求成立时承担独立 IM Gateway。
- SQL 是事件、状态、关系、记忆来源、任务、Outbox 和评估记录的基础语言。
- Rust 只在基准测试证明性能瓶颈，或安全隔离、WASM 宿主、单文件分发等边界明确时引入。
- C++ 不承载第一方领域和业务逻辑，仅作为推理引擎、硬件 SDK、编解码器等外部原生依赖。
- 跨语言契约以版本化 JSON Schema 为默认载体；控制面使用 OpenAPI。Protobuf 与 AsyncAPI 在吞吐或通道治理需求被证明后再评估。
- 同一领域契约不得分别手写多套模型；生成类型不得反向成为核心领域类型。

## 替代方案

- 全部使用 Python：控制面与 Node.js 优势平台的接入成本可能上升。
- 从第一阶段同时使用 Python、TypeScript、Rust 和 C++：增加构建、部署、ABI 与语义漂移风险。
- 以语言决定服务边界：会把实现偏好误当成故障域和所有权边界。

## 后果

- 研究阶段保持快速迭代，并给控制面和未来平台边缘保留合适工具链。
- 团队需要维护 Python 与 TypeScript 的契约生成和兼容性检查。
- Rust 或新的第一方语言必须通过 ADR 说明测量证据、边界、维护者和回退路径。

## 验证与回退

- CI 对 Python 模型、TypeScript 生成类型和 JSON Schema 运行兼容性测试。
- 若 Python 无法满足已量化的延迟、吞吐、内存或隔离目标，再以独立 ADR 引入 Rust。
- 若 TypeScript Gateway 没有形成独立部署或故障域，保持平台接入位于 Python 模块化单体中。
