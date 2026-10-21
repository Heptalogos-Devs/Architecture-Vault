# 模型、Prompt 与完整步骤预览

[模型与Prompt资源.json](模型与Prompt资源.json)给出ProviderDefinition、SDK分支ModelDefinition、LanguageRolePolicy和Prompt的save/preview输入；[逐步消息预览.json](逐步消息预览.json)给出真实AI SDK消息形状的工具后续。它们是固定夹具，Ref、SecretRef和修订须由安装后的实际owner返回后使用。

模型名与64k/4096限制沿本轮已知模型资源配置，示例不声明当前网关价格。baseURL/networkProfileId/SecretRef由安装者绑定；文件不含秘密正文，也不会自动测试或派发。需要其他部署时通过正式资源配置更换，不在Provider调用中猜测模型名/价格。

## 配置采用

1. 先用secrets owner创建秘密并取得不透明SecretRef，配置network profile与该模型的ResourceNetworkScope。示例回环地址须明确configured_private及精确目标范围；profile负责连接，目标许可归实际资源owner。普通页面读取这些定义不会调用模型。
2. Provider定义通过`/v1/model-providers`管理；ModelDefinition通过`/v1/models`管理。角色在`/v1/roles/{id}`采用对应policy；resources中的revision取实际保存结果。SDK/native资源分别使用自己的定义分支。
3. 注册`query_concept_enrichment`领域RoleDescriptor，其kind=language、PromptId=`nous.query.concept-enrichment`、参数schema为空对象，输出合同仍由query owner持有。原始英文Prompt位于`packages/nous/prompts/en/query/concept-enrichment.md`，本例明确采用en；新增中文正文单独进入zh-CN资源。
4. 示例text完整迁入原Nous `412b0620`的查询Prompt；保留existing_tags/novel_concepts、目录key、数量上限、假设与长期事实区分。正式字段改动由该领域合同与资源一起迁移。
5. `promptSave`是owner函数输入；HTTP将promptId置于`POST /v1/prompts/{id}/revisions`路径，其余字段为body。调用携带稳定submissionId；激活通过`POST /v1/prompts/{id}/activate`，expectedRevision按真实head。
6. `promptPreview`发送到`POST /v1/prompts/preview`。预览只使用明确params和已选资源快照，不派发模型，不创建Encounter或observed。

基础schema无default；这些JSON显式给出所需值。Role的providerOptions与Prompt绑定在配置快照中冻结；变更后新调用采用新版本，正在执行的调用持有原快照和当前授权。

## 消息保留与认知slot

固定步骤含user→assistant tool-call→tool-result→user四条消息。工具调用和返回共享`call-source-1`，返回内容含固定Material修订。认知贡献的选区只在Ref.selector；这份完整材料未再切区。

[预览组装.mjs](预览组装.mjs)直接使用AI SDK公开modelMessageSchema和LiquidJS：

- 校验并保留整个ModelMessage数组，包括toolCallId、工具参数/结果及各parts。
- 渲染已冻结职责Prompt，再追加本次认知instructions；下一步从同一base重新合成，不累积上一轮slot。
- 原样传递当前step.messages。没有固定user占位符，也不把工具结果重写成另一条人工摘要。
- 输出可查看的完整语义输入、Prompt digest与明确的字节数。夹具的estimatedTokens是上下文估计，实际usage只能来自真正Provider结果。

该脚本只组装预览。实际调用的onStepStart/V4 params/可得request.body分别由模型owner保存；输出发生后，原observed/formed capture、费用和Encounter按[模型合同](../设计/基础设施/模型供应与调用.md)接纳。私有worker结果仍需选定发布后由主体实际查看。

依赖为AI SDK7.0.146与LiquidJS10.30.0。运行输出可重建，不需要数据库、凭据、网络或模型。这个小例子用于保护消息与资源组装边界，完整Provider/模型执行沿成熟SDK。
