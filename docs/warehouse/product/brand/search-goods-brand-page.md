# 获取列表


- 层级：开放平台 > 仓储 > 商品 > 商品品牌
- 方法+路径：`POST /open/v1/ewm/goods/goods_brand/fetch/search_goods_brand_page`
- 类型：读
- 原文：[479599768e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599768e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.brandList` | array&lt;object> | 否 |  |
| `data.brandList[].goodsBrandId` | integer | 否 | 商品品牌ID |
| `data.brandList[].brandName` | string | 否 | 品牌名称 |
| `data.total` | integer | 否 | 总计 |
