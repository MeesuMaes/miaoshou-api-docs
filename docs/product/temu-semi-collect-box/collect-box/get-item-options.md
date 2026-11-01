# 获取商品基本选项


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_item_options`
- 类型：读
- 原文：[477347601e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347601e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.outerPackageShapeOptions` | array&lt;object> | 否 | 外包装形状选项，key/value 数组，保存到 outerPackageShape |
| `data.outerPackageShapeOptions[].key` | integer | 否 | 选项键值 |
| `data.outerPackageShapeOptions[].value` | string | 否 | 选项显示文本 |
| `data.outerPackageTypeOptions` | array&lt;object> | 否 | 外包装类型选项，key/value 数组，保存到 outerPackageType |
| `data.outerPackageTypeOptions[].key` | integer | 否 | 选项键值 |
| `data.outerPackageTypeOptions[].value` | string | 否 | 选项显示文本 |
| `data.goodsModelTryOnResultMap` | array&lt;object> | 否 | 模特试穿结果枚举，格式为 [\{key: modelType, value: \{tryOnResult: label\}\}]。 保存时按 modelType 取对应枚举，将所选 tryOnResult 填入 goodsModelReqs[].tryOnResult |
| `data.goodsModelTryOnResultMap[].key` | integer | 否 | 模特类型（modelType） |
| `data.goodsModelTryOnResultMap[].value` | object | 否 | 试穿结果枚举映射，key 为 tryOnResult，value 为显示文本 |
| `data.catIdAndProductNameMaxLengthMap` | object | 否 | 类目标题最大长度映射，key 为 cid，value 为最大字符数 |
| `data.suggestedPriceCurrencyTypeAndNameList` | array&lt;object> | 否 | 建议售价币种列表，key/value 数组，保存到 skuMap[key].suggestedPriceCurrencyType |
| `data.suggestedPriceCurrencyTypeAndNameList[].key` | string | 否 | 选项键值 |
| `data.suggestedPriceCurrencyTypeAndNameList[].value` | string | 否 | 选项显示文本 |
| `data.skuClassificationList` | array&lt;object> | 否 | SKU 分类类型，key/value 数组，保存到 skuMap[key].skuClassification。 1=单品（numberOfPieces 只能为1）；2=同款多件装（numberOfPieces 必须>1）； 3=混合套装（需额外填写 individuallyPacked 和 productSkuAccessories）。 部分类目此字段必填 |
| `data.skuClassificationList[].key` | integer | 否 | 选项键值 |
| `data.skuClassificationList[].value` | string | 否 | 选项显示文本 |
| `data.skuPieceUnitCodeList` | array&lt;object> | 否 | 件数单位，key/value 数组，保存到 skuMap[key].pieceUnitCode。部分类目必填 |
| `data.skuPieceUnitCodeList[].key` | integer | 否 | 选项键值 |
| `data.skuPieceUnitCodeList[].value` | string | 否 | 选项显示文本 |
| `data.individuallyPackedList` | array&lt;object> | 否 | 是否独立包装，key/value 数组，保存到 skuMap[key].individuallyPacked。 skuClassification 为2或3时必填 |
| `data.individuallyPackedList[].key` | integer | 否 | 选项键值 |
| `data.individuallyPackedList[].value` | string | 否 | 选项显示文本 |
| `data.packageLimitConfig` | object | 否 | 包装限制配置 |
| `data.descModuleLimitConfig` | object | 否 | 描述模块限制配置，包含 descModuleMaxTextLength（最大文本长度） |
| `data.netContentCidList` | array&lt;integer> | 否 | 需要填写净含量的类目 cid 列表。 当商品 cid 在此列表中，skuClassification 为1或2时需填 netContentNumber/netContentUnitCode（取值见 netContentOptions）； skuClassification 为3时需填 totalNetContentNumber/totalNetContentUnitCode |
| `data.netContentOptions` | array&lt;object> | 否 | 净含量单位选项，key/value 数组，保存到 skuMap[key].netContentUnitCode |
| `data.netContentOptions[].key` | integer | 否 | 选项键值 |
| `data.netContentOptions[].value` | string | 否 | 选项显示文本 |
| `data.enTitleRefTypeList` | array&lt;object> | 否 | 英文标题参考类型选项 |
| `data.enTitleRefTypeList[].key` | string | 否 | 选项键值 |
| `data.enTitleRefTypeList[].value` | string | 否 | 选项显示文本 |
| `data.pieceNewUnitCodeList` | array&lt;object> | 否 | 共计内含单位选项，key/value 数组，保存到 skuMap[key].pieceNewUnitCode |
| `data.pieceNewUnitCodeList[].key` | integer | 否 | 选项键值 |
| `data.pieceNewUnitCodeList[].value` | string | 否 | 选项显示文本 |
| `data.mixTypeList` | array&lt;object> | 否 | 混合套装类型选项，key/value 数组，保存到 skuMap[key].mixedType。1=不同品，2=同品不同规格 |
| `data.mixTypeList[].key` | integer | 否 | 选项键值 |
| `data.mixTypeList[].value` | string | 否 | 选项显示文本 |
| `data.totalNetContentCidList` | array&lt;integer> | 否 | 需要填写总净含量的类目 cid 列表（混合套装场景） |
| `data.vehicleLibraryRequiredCidList` | array&lt;integer> | 否 | 需要填写车型库信息的类目 cid 列表 |
| `data.saleAttributeClothingColorMaxNum` | integer | 否 | 销售属性颜色最大数量 |
| `data.shipmentLimitDayOptions` | array&lt;object> | 否 | 发货限制天数选项 |
| `data.shipmentLimitDayOptions[].key` | integer | 否 | 选项键值 |
| `data.shipmentLimitDayOptions[].value` | string | 否 | 选项显示文本 |
| `data.attributeRuleGroupIdAndSizeChartsGroupIdMap` | object | 否 | 销售属性规则组ID和尺码表组ID映射 |
| `data.sizTypeAndSizeTypeNameMap` | object | 否 | 尺码类型映射 |
