# 获取商品SKU安全库存列表


- 层级：开放平台 > 仓储 > 库存 > 自营仓库存
- 方法+路径：`POST /open/v1/ewm/storage/warehouse/fetch/get_goods_sku_safe_stock_num_list`
- 类型：读
- 原文：[479599785e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599785e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSkuOuterIds` | array&lt;string> | 是 | 商品sku |
| `warehouseId` | integer | 是 | 仓库id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuOuterIdAndSafeStockNumMap` | array&lt;object> | 否 |  |
| `data.goodsSkuOuterIdAndSafeStockNumMap[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsSkuOuterIdAndSafeStockNumMap[].safeStockNum` | integer | 否 | 库存安全数 |
