# 获取属性列表


- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/get_attribute_list`
- 类型：读
- 原文：[480434404e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434404e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 否 | 店铺ID |
| `site` | string | 否 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.attributes` | array&lt;object> | 否 | 属性列表 |
| `data.attributes[].attributeId` | integer | 否 |  |
| `data.attributes[].originalAttributeName` | string | 否 |  |
| `data.attributes[].displayAttributeName` | string | 否 |  |
| `data.attributes[].isMandatory` | boolean | 否 |  |
| `data.attributes[].inputValidationType` | string | 否 |  |
| `data.attributes[].formatType` | string | 否 |  |
| `data.attributes[].inputType` | string | 否 |  |
| `data.attributes[].attributeUnit` | array&lt;string> | 否 |  |
| `data.attributes[].attributeValueList` | array&lt;object> | 否 |  |
| `data.attributes[].attributeValueList[].valueId` | integer | 否 |  |
| `data.attributes[].attributeValueList[].originalValueName` | string | 否 |  |
| `data.attributes[].attributeValueList[].displayValueName` | string | 否 |  |
| `data.attributes[].attributeValueList[].parentAttributeList` | array&lt;object> | 否 |  |
| `data.attributes[].attributeValueList[].parentAttributeList[].parentAttributeId` | integer | 否 |  |
| `data.attributes[].attributeValueList[].parentAttributeList[].parentValueId` | integer | 否 |  |
| `data.attributes[].maxInputValueNumber` | integer | 否 |  |
| `data.attributes[].introduction` | string | 否 |  |
| `data.attributes[].mandatoryRegion` | array&lt;string> | 否 |  |
| `data.lang` | string | 否 | 语言 |
