# 同步产品


- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/rsync_item_single`
- 类型：写
- 原文：[480434407e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434407e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemIds` | array&lt;string> | 是 | 平台产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successPlatformItemIds` | array&lt;string> | 否 |  |
| `data.failedPlatformItemIds` | array&lt;string> | 否 |  |
| `data.errorMap` | object | 否 |  |
