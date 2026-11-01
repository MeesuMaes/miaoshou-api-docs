# 获取三方仓商品库存列表


- 层级：开放平台 > 仓储 > 库存 > 三方仓sku库存
- 方法+路径：`POST /open/v1/ewm/storage/third_warehouse/fetch/search_third_goods_sku_warehouse_page`
- 类型：读
- 原文：[479599784e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599784e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `type` | string | 是 | 类型 1:第三方仓库服务商LogisticsAgent 2:第三方货代仓库服务商Forwarder 3:FBA仓库 4:FBT |
| `thirdWarehouseProviderAgentAuthIds` | array&lt;integer> | 否 | 第三方仓库服务商授权主键ID （选一个） |
| `thirdWarehouseForwarderProviderAuthIds` | array&lt;integer> | 否 | 第三方货代仓库服务商授权主键ID（选一个） |
| `thirdWarehouseProviderAuthId` | array&lt;integer> | 否 | FBA\FBA授权id |
| `warehouseIds` | array&lt;integer> | 是 | 仓库Ids |
| `keyword` | string | 否 | 第三方sku 多个用逗号分隔 |
| `matchSku` | string | 否 | 商品sku（映射关系） 多个用逗号分隔 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuWarehouseList` | object | 否 | 商品SKU库存数据 |
| `data.goodsSkuWarehouseList.goodsSkuOuterId` | string | 否 | 第三方sku |
| `data.goodsSkuWarehouseList.warehouseName` | string | 否 | 仓库名称 |
| `data.goodsSkuWarehouseList.logisticsAgentWarehouseId` | string | 否 | 第三方仓库id |
| `data.goodsSkuWarehouseList.stockNum` | string | 否 | 库存 |
| `data.goodsSkuWarehouseList.availableStockNum` | string | 否 | 可用库存 |
| `data.goodsSkuWarehouseList.lockedStockNum` | string | 否 | 预占库存 |
| `data.goodsSkuWarehouseList.frozenStockNum` | string | 否 | 待上架库存 |
| `data.goodsSkuWarehouseList.onWayStockNum` | string | 否 | 在途库存 |
| `data.goodsSkuWarehouseList.waitSubmitStockNum` | string | 否 | 待提交量 |
| `data.goodsSkuWarehouseList.onPlanNum` | string | 否 | 计划库存 |
| `data.goodsSkuWarehouseList.faultyStockNum` | integer | 否 | 次品库存数量 |
| `data.goodsSkuWarehouseList.notForSaleNum` | integer | 否 | 不可售数量（平台仓） |
| `data.goodsSkuWarehouseList.inboundNum` | integer | 否 | 入库数量（平台仓） |
| `data.goodsSkuWarehouseList.reservedNum` | integer | 否 | 活动预留数量 |
| `data.total` | integer | 否 |  |
