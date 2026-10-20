# 查询与检索施工资源

这里保留4份原数值预设与6条查询，供检索owner复制后在正式负责位置接线。来源固定为 Nous master [`412b062082afb75ccfae4c3f69fc606d3e3cc862`](https://github.com/Heptalogos-Devs/Nous-Wave/tree/412b062082afb75ccfae4c3f69fc606d3e3cc862)。数值文件和许可证逐字节复制，SHA-256见[来源清单](来源.json)；查询text原样摘录，中文前提与检查说明为本轮新增。

## 数值预设

| 资源 | 实际消费者与用途 |
|---|---|
| [retrieval-ranking.json](数值预设/retrieval-ranking.json) | `rank_candidates_with_policy`固定归一化RRF及完整family权重、查询预算和偏好；k=60、单项偏好0.02、总额0.06 |
| [topology-wave.json](数值预设/topology-wave.json) | 原Native graph/wave；hop4、state4096、neighbor32以及全部root质量、种子、回流/FIR参数 |
| [query-concept-activation.json](数值预设/query-concept-activation.json) | 共享QueryActivation；最多8个activation、相似度0.72、模型catalog32 |
| [epa.json](数值预设/epa.json) | 原`mechanisms/cue_sensing::build_epa_basis`数值研究单元；minimum_samples8、representatives256、axes64及两项epsilon |

这些文件沿原`identity/values`形状保留出处和数值。施工时检索owner把字段迁入最终typed settings定义，分别提供无默认基础schema、defaults和稀疏JSON Patch；Rust入口接收已求值完整config。参数意义与源函数逐项对应，保留数字后再做算法实验。

EPA资源对应原研究函数；VCP的`VcpAssetPolicy`另有EPA训练参数与真实生产消费者，按[检索底座](../../设计/基础设施/检索服务与认知消费者.md)迁入。它们使用各自原合同。

## 查询输入

[查询.json](查询.json)含稳定例子ID、text、源行号、前提和检查点。执行环境先创建自己的真实Subject/Identity/Concept与材料；带Alice或Tag名称的例子使用实际目录绑定。无匹配资料时，正常得到空结果；歧义、未供给能力和缺资产沿正式Problem/状态返回。

1. `entity-cue`：明确人物，观察名字绑定与普通召回。
2. `same-occurrence-time`：发生和接触两轴要求同一source occurrence。
3. `historical-revisions`：现实as-of与旧修订共同使用。
4. `explicit-projection`：Memory/Schema两域在候选预算前过滤。
5. `bounded-association`：由Host选择profile并执行有界联想。
6. `persistent-concept`：正式Tag、membership和联想共享稳定概念。

当前合同对原语言作了明确补齐：省略$return为Memory四域加已供给Self两域；显式$return(cognition)仍四域；新增$return(concept)。这6条选定输入按[正式NousQL合同](../../设计/NousQL与检索合同.md)解释。施工可在同一真实场景中取得返回的Concept短引用，再以`这个概念 @ref(实际短引用) $return(concept)`精确续读；地址取实际结果，保持同一query/run来源与权限。

## 固定源与许可证

- [原查询手册与选定行](https://github.com/Heptalogos-Devs/Nous-Wave/blob/412b062082afb75ccfae4c3f69fc606d3e3cc862/docs/agent/NOUSQL.md#L66)。
- [原数值预设目录](https://github.com/Heptalogos-Devs/Nous-Wave/tree/412b062082afb75ccfae4c3f69fc606d3e3cc862/config/reference)。
- [原算法函数与消费者研究](../../研究/Nous查询与检索.md)。
- [随附Apache-2.0许可证](LICENSE-APACHE-2.0.txt)及[原版权NOTICE](NOTICE)。来源版权与原仓库NOTICE随迁入文件保留；这里未复制整个语料或运行框架。
