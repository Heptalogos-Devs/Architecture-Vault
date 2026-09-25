# Heptalogos 设计决定

## Subject 与产品职责

### Heptalogos 承担行为侧 Subject

Heptalogos 维护 Subject 的主动性、交互、行为决定、承诺、外部效果和产品运行。认知长期状态由 Nous Wave 维护。

目标设计：第 1、2、4 章。

### SubjectId 跨认知与行为系统保持一致

Nous Wave 和 Heptalogos 共享逻辑 `SubjectId`，各自维护自己的领域状态和修订。

目标设计：第 2、4 章。

## 主动性

### 主动追求由 Heptalogos 维护

`Pursuit` 表示行为侧已经决定持续投入行为资源追求某个期望条件。它引用 Nous Wave 中期望条件的精确修订。

目标设计：第 5 章。  
论证：[认知与主动性](rationale/01-cognition-agency.md)

### 一次行为提议与持续追求分别维护

`BehaviorIntent` 表示一次具体行为决策中的提议；`Pursuit` 表示跨多次 Reaction 延续的主动追求。计划、承诺和外部效果继续拥有各自身份。

目标设计：第 5、6、7 章。

## 行为权威

### 行为决定通过显式提交形成

模型、检索、认知系统和扩展提供输入或提案。对外行为必须经过 Heptalogos 的 Review 与 `DecisionCommit`。

目标设计：第 2、6 章。

### 安全政策和管理员强制由 Heptalogos 承担

行为许可、禁止、管理员强制约束和系统管理由 Heptalogos 的行为与规范权威维护，不依赖可演化认知。

目标设计：第 2、8 章。

## 产品运行

### 产品宿主与机器运维分离

正常产品宿主拥有产品 Authority。高权限机器维护位于独立机器运维平面，通过管理合同与宿主协作。

目标设计：第 3、8 章。
