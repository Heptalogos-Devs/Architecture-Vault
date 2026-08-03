# 身份、人格与动态生命状态

## 三层分离

```text
Core Identity     主体长期是谁
Living State      主体此刻怎样
Expression Style  本次如何表达
```

三者互相影响，但不能互相覆盖。

## Core Identity

Core Identity 是版本化、低频变化的主体规范，包括：

- 身份事实与社会角色；
- 人格基线；
- 价值取向和行为边界；
- 长期偏好；
- 语言习惯的稳定部分；
- 自我叙事的核心主题。

它不是一段 Persona Prompt。Prompt 只是将其中与当前任务有关的部分编译进模型上下文。

模型不能直接修改 Core Identity。长期变化应由人工配置、明确成长事件或经过严格审查的慢速候选产生，并保留版本历史。

## Living State

Living State 表示短期处境，例如：

- 当前活动与地点；
- 精力、压力、睡眠和社交意愿；
- 当前目标和未完成事项；
- 当前注意对象；
- 是否能阅读、思考、回复或使用工具；
- 轻量情绪状态。

状态变化需要原因、来源和时间。时间衰减、日程和外部事件可以更新 Living State，但不得改变权限或核心人格。

## 情绪

早期只保留少量可解释维度：

```text
valence
arousal
energy
stress
irritability
social_willingness
confidence
```

情绪由事件结合目标、关系、确定性、可控性和主体基线进行 appraisal 后更新。

情绪可以轻微影响：

- 回复长度与延迟；
- 是否愿意展开话题；
- 表达直接度；
- 对打断和话题切换的容忍。

情绪不能：

- 改变事实；
- 提升权限；
- 自动升级关系；
- 绕过安全策略；
- 通过冷落或负罪感惩罚用户。

## 主体快照

一次认知使用一致的 Subject Snapshot，其中包含相关版本引用，而不是各模块在推理途中任意读取最新值。

快照至少标明：

- identity version；
- living-state version；
- relation and task versions；
- schedule / timeline position；
- privacy and capability permissions；
- snapshot time。

认知提交时若关键版本已变化，应重新读取并重算，而不是覆盖更新。

## 开放问题

- Core Identity 中哪些字段需要结构化，哪些保留文本叙事；
- Living State 的最小维度；
- 情绪机制对行为是否有独立增益；
- 主体成长如何与人工配置、日记和事实事件结合。
