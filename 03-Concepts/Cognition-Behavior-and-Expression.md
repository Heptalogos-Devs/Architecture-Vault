# 认知、行为与表达

## Cognitive Kernel

中央认知不是一个无限循环的通用 Agent，而是一个认知事务协调器：

```text
选择认知对象
+ 读取一致快照
+ 调度有限模型任务
+ 形成行为与状态候选
+ 执行确定性审查
+ 统一提交
```

它不拥有平台 SDK、数据库实现细节或具体工具代码。

## 认知阶段

建议阶段：

1. Feed Intake；
2. Observation Window；
3. Wake-up Gate；
4. Attention Selection；
5. Subject Snapshot；
6. Situation Interpretation；
7. Appraisal；
8. Memory / Epistemic Retrieval；
9. Behavior Decision；
10. Action Planning；
11. Narrative Reality Review；
12. Cognitive Commit；
13. Expression Rendering；
14. Output Verification；
15. Delivery。

阶段可以合并实现，但权威边界不能消失。

## Situation Frame

模型和规则处理的不是裸消息，而是结构化情境：

- 会话和参与者；
- 言语行为；
- 引用、撤回和媒体；
- 明确请求和隐含信号；
- 当前话题和未解决事项；
- 紧迫度、社会风险和隐私作用域；
- 不确定信息和证据引用。

## BehaviorIntent

BehaviorIntent 描述“做什么”，不包含最终措辞。候选包括：

- reply；
- wait / defer；
- silent / ignore；
- react；
- ask clarification；
- use capability；
- cancel；
- notify proactively。

它还应包含社会目标、姿态、时效、允许能力、约束和 reason codes。

## ActionPlan

ActionPlan 将行为转为可执行步骤。它必须：

- 持久化；
- 可取消；
- 可过期；
- 有稳定 ID 和幂等键；
- 描述副作用和依赖；
- 在执行结果后产生事件。

## 两次模型生成

### 认知生成

输出结构化候选：

- BehaviorIntent；
- StateChangeProposal；
- WorldStateProposal；
- CapabilityPlanProposal；
- 不确定性和证据引用。

### 表达生成

只根据已经批准的行为、事实、声明和风格生成自然语言。它不决定是否行动，也不能添加未批准事实。

## 审查

确定性规则优先检查：

- 权限和能力范围；
- 隐私作用域；
- 工具是否真实完成；
- 记忆和声明来源；
- 时间线、自我陈述和知识边界；
- 行为是否过期；
- 核心身份和安全边界。

模型可以辅助审查，但不能成为唯一安全门。

## 元认知

不保存自由形式隐藏思维链。元认知输出结构化结果：

- known unknowns；
- claim support；
- knowledge boundary；
- conflicting evidence；
- recommended conservative behavior。

## 开放问题

- 哪些阶段使用规则、小模型或主推理模型；
- BehaviorIntent 最小 schema；
- 全局注意力是否允许抢占；
- 认知提交与表达生成的精确顺序；
- 输出验证失败后的重写和降级策略。
