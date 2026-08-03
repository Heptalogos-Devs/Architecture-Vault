# Python 到目标 TypeScript 运行时的迁移说明

迁移不按文件或类逐行翻译，而按完整行为切片进行。

## 前置条件

- 固定 Event、BehaviorIntent、ActionPlan 和 Outcome 契约；
- 建立 Fake Adapter、Provider 和 Clock；
- 保存当前 Python 实现的回放场景；
- 明确迁移期间唯一权威写入者。

## 推荐顺序

1. 共享 Schema 和 Scenario Runtime；
2. Observation Window 与 BehaviorIntent 新切片；
3. TypeScript Cognitive Kernel；
4. 状态、任务和在线记忆；
5. 根据边缘 SDK 和故障域决定 Gateway 是否迁移；
6. Control Plane API 与在线运行时整合。

## 禁止

- Python 和 TypeScript 同时修改同一主体状态；
- 迁移期间改变领域语义却没有场景对照；
- 把旧 Python 内部类直接变成跨语言协议；
- 为迁移提前拆成微服务；
- 删除旧实现前失去回放基线。
