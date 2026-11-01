# AI润色销售规格


- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/generate_sku_spec_name`
- 类型：处理(生成内容)
- 原文：[484286515e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286515e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platform` | string | 是 | 平台（目前只支持tiktok） |
| `title` | string | 否 | 原始标题（作为AI润色上下文） |
| `aiName` | string | 是 | AI模型名称（目前只支持 douBao1.6） |
| `languageName` | string | 否 | 目标语言名称（取值见 getLanguageNameCodeMap 接口，默认"当前语言"） |
| `functionModule` | string | 是 | 功能模块，可选值：createCollectBox / editCollectBox / createItem / editItem |
| `skuPropertyList` | array&lt;object> | 是 | SKU属性列表 |
| `skuPropertyList[].attrName` | string | 否 | 属性名称（如 Color、规格） |
| `skuPropertyList[].attrId` | string | 否 | 属性ID（可为空字符串） |
| `skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 每项包含 attrValueId/attrValue/imgUrl/supplementarySkuImageUrls |
| `skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值主图URL（无图时为空字符串） |
| `skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array&lt;string> | 否 | 补充SKU图片URL列表 |
| `productId` | integer | 否 | 产品ID（functionModule 为 editCollectBox / editItem 时传入） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.newSkuPropertyList` | array&lt;object> | 否 | AI润色后的SKU规格列表 格式：[\{"name": "Color", "valueList": ["Red", "Blue"]\}, ...] |
| `data.newSkuPropertyList[].attrName` | string | 否 | 属性名称（如 Color、规格） |
| `data.newSkuPropertyList[].attrId` | string | 否 | 属性ID（可为空字符串） |
| `data.newSkuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 每项包含 attrValueId/attrValue/imgUrl/supplementarySkuImageUrls |
| `data.newSkuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `data.newSkuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `data.newSkuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值主图URL（无图时为空字符串） |
| `data.newSkuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array&lt;string> | 否 | 补充SKU图片URL列表 |
| `data.reasoningContent` | string | 否 | AI思考过程内容（部分AI模型返回的推理过程） |
| `data.openaiRequestLogId` | integer | 否 | AI请求日志ID（对应历史记录ID，默认0） |
