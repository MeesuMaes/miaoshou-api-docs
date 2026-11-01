# 获取商品销售数据列表


- 层级：开放平台 > 仓储 > 数据统计 > 销售数据
- 方法+路径：`POST /open/v1/ewm/stat/goods_sale_data/fetch/search_goods_sale_data_page`
- 类型：读
- 原文：[479602617e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479602617e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `shopIds` | array&lt;integer> | 是 | 店铺ID数组 |
| `gmtStart` | string | 是 | 开始日期如2022-07-01 |
| `gmtEnd` | string | 是 | 结束日期如2022-07-01 |
| `warehouseIds` | array&lt;integer> | 否 | 仓库ID数组 |
| `logisticsAgentWarehouseIds` | array&lt;integer> | 否 | 第三方仓库id |
| `goodsSkuOuterIds` | string | 否 | 商品SKU |
| `goodsSkuOuterIdsRp` | string | 否 | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsName` | string | 否 | 商品名称 |
| `goodsNameRp` | string | 否 | 商品名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsSkuCustomCodes` | string | 否 | 商品代码 |
| `goodsSkuCustomCodesRp` | string | 否 | 商品代码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `foreignGoodsName` | string | 否 | 商品外文名称 |
| `foreignGoodsNameRp` | string | 否 | 商品外文名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsGroupIds` | array&lt;integer> | 否 | 商品分组ID列表 |
| `shopFilterType` | string | 否 | 店铺类型shopId-按店铺Id,group-按店铺分组拣货单 |
| `shopGroupIds` | array&lt;integer> | 否 | 店铺分组id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSaleList` | array&lt;object> | 否 |  |
| `data.goodsSaleList[].goodsSkuId` | string | 否 | 商品sku Id |
| `data.goodsSaleList[].orderSaleCount` | string | 否 | 自营仓销售订单量 |
| `data.goodsSaleList[].goodsSaleCount` | string | 否 | 自营仓销量 |
| `data.goodsSaleList[].goodsRefundCount` | string | 否 | 退货数量 |
| `data.goodsSaleList[].goodsSaleAmount` | number | 否 | 销售金额 |
| `data.goodsSaleList[].goodsCostAmount` | number | 否 | 自营仓商品成本 |
| `data.goodsSaleList[].goodsRefundAmount` | number | 否 | 退款成本 |
| `data.goodsSaleList[].orderRefundAmount` | number | 否 | 退款金额 |
| `data.goodsSaleList[].goodsSkuInfo` | object | 否 | 商品信息 |
| `data.goodsSaleList[].goodsSkuInfo.goodsName` | string | 否 | 商品名称 |
| `data.goodsSaleList[].goodsSkuInfo.goodsMode` | string | 否 | 商品类型 |
| `data.goodsSaleList[].goodsSkuInfo.goodsId` | string | 否 | 商品id |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuId` | string | 否 | 商品SKUid |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuOuterId` | string | 否 | sku |
| `data.goodsSaleList[].goodsSkuInfo.logoOssPath` | string | 否 | 图片地址 |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsSaleList[].goodsSkuInfo.logoUrl` | string | 否 | 图片url |
| `data.goodsSaleList[].rank` | string | 否 | 排名 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales` | object | 否 | 三方仓销售数据 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuOrderSaleAmount` | number | 否 | 三方仓销售金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuOrderSaleCount` | integer | 否 | 三方仓销售订单量 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuGoodsSaleCount` | integer | 否 | 三方仓销量 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuGoodsCostAmount` | number | 否 | 三方仓商品成本 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList` | array&lt;object> | 否 | 三方仓销售数据列表 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentWarehouseId` | string | 否 | 仓库id |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentGoodsSkuId` | string | 否 | 第三方sku ID |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsSkuId` | string | 否 | 商品sku ID |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].orderSaleAmount` | string | 否 | 订单销售金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].orderSaleCount` | string | 否 | 商品成本金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsSaleCount` | string | 否 | 商品销售数量 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsCostAmount` | string | 否 | 商品成本金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentWarehouseName` | string | 否 | 仓库名称 |
| `data.total` | integer | 否 | 总数 |
