# 当前目标架构

本页把愿景压缩为实现时使用的目标边界。

```text
Interaction Gateway
  raw evidence / canonical facts / delivery outcomes

Cognitive Runtime
  mailbox / observation / attention / snapshot / behavior / commit

Subject State
  identity / living state / relations / memory / epistemic state
  tasks / commitments / schedule / timeline / claims

Capability Runtime
  registry / policy / confirmation / durable execution / results

Control and Research
  config / correction / replay / metrics / experiments
```

## 在线权威

TypeScript/Node.js 目标运行时拥有事实消费、主体状态、行为提交、任务调度、在线记忆治理和能力授权。

## 离线候选

Python 负责分析、评测、本地模型、日记、反思、梦和检索算法候选，不直接写在线状态。

## 原生执行

Rust 负责需要强权限边界、WASM、原生系统访问或不可信文件处理的 Worker。

## 部署

早期仍是本机模块化单体：一个在线运行时、SQLite、本地 CAS、静态 WebUI，以及按需启动的 Python/Rust Worker。边界由权威和失败语义决定，不由进程数量决定。
