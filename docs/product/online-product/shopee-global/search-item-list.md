# 全球产品搜索


- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/search_item_list`
- 类型：读
- 原文：[480434401e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434401e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 页码，默认1 |
| `pageSize` | integer | 是 | 每页条数，默认20 |
| `filter` | object | 是 | 搜索条件 |
| `filter.shopId` | string | 是 | 店铺ID(必传,性能问题无法支持多店铺检索) |
| `filter.platformItemId` | string | 否 | 平台产品ID |
| `filter.itemNum` | string | 否 | 主货号 |
| `filter.cids` | array&lt;integer> | 否 | 类目ID |
| `filter.status` | string | 否 | 产品状态 |
| `filter.title` | string | 否 | 标题 |
| `filter.minStock` | string | 否 | 最小库存 |
| `filter.maxStock` | string | 否 | 最大库存 |
| `filter.publishedProductStatus` | string | 否 | 发布产品状态 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemList` | array&lt;object> | 否 | 产品列表 |
| `data.itemList[].shopId` | string | 否 | 店铺ID |
| `data.itemList[].itemId` | string | 否 | 产品ID |
| `data.itemList[].platformItemId` | string | 否 | 平台产品ID |
| `data.itemList[].title` | string | 否 | 标题 |
| `data.itemList[].picUrl` | string | 否 | 产品图片链接 |
| `data.itemList[].salePrice` | string | 否 | 售价 |
| `data.itemList[].stock` | string | 否 | 库存 |
| `data.itemList[].itemNum` | string | 否 | 主货号 |
| `data.itemList[].platformStatus` | string | 否 | 发布状态 |
| `data.itemList[].status` | string | 否 | 产品状态 |
| `data.itemList[].weight` | string | 否 | 重量 |
| `data.itemList[].gmtCreate` | string | 否 | 创建时间 |
| `data.total` | integer | 否 | 总数 |
