# AI属性匹配


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/ai_match_product_attribute`
- 类型：处理(生成内容)
- 原文：[482189161e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189161e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | integer | 是 | 采集箱详情ID |
| `cid` | string | 是 | 类目ID |
| `site` | string | 是 | 站点 |
| `shopIds` | array&lt;integer> | 否 | 店铺ID列表 当产品与店铺关联时传入，用于精确查找 |
| `productAttributes` | array&lt;object> | 否 | 当前产品属性列表 |
| `productAttributes[].attributeId` | string | 否 | 属性ID |
| `productAttributes[].attributeName` | string | 否 | 属性名称 |
| `productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.productAttributes` | array&lt;object> | 否 | AI匹配后的产品属性列表 |
| `data.productAttributes[].attributeId` | string | 否 | 属性ID |
| `data.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `data.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `data.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `data.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
