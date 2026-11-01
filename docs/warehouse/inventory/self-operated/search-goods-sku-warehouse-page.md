# 获取自营仓商品库存列表


- 层级：开放平台 > 仓储 > 库存 > 自营仓库存
- 方法+路径：`POST /open/v1/ewm/storage/warehouse/fetch/search_goods_sku_warehouse_page`
- 类型：读
- 原文：[479599786e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599786e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `warehouseIds` | array&lt;integer> | 否 | 仓库ids |
| `goodsSkuOuterIds` | array&lt;string> | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuWarehouseList` | array&lt;object> | 否 | 商品SKU库存数据 |
| `data.goodsSkuWarehouseList[].goodsSkuWarehouseId` | string | 否 | 仓库id |
| `data.goodsSkuWarehouseList[].goodsSkuId` | string | 否 | 商品skuid |
| `data.goodsSkuWarehouseList[].goodsId` | string | 否 | 商品id |
| `data.goodsSkuWarehouseList[].stockNum` | string | 否 | 总库存 |
| `data.goodsSkuWarehouseList[].availableStockNum` | string | 否 | 可用库存 |
| `data.goodsSkuWarehouseList[].lockedStockNum` | string | 否 | 预占库存 |
| `data.goodsSkuWarehouseList[].onWayNum` | string | 否 | 在途库存 |
| `data.goodsSkuWarehouseList[].onPlanNum` | string | 否 | 计划库存 |
| `data.total` | integer | 否 |  |
