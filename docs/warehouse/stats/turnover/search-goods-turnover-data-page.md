# 获取商品周转数据列表


- 层级：开放平台 > 仓储 > 数据统计 > 商品周转分析
- 方法+路径：`POST /open/v1/ewm/stat/goods_turnover_data/fetch/search_goods_turnover_data_page`
- 类型：读
- 原文：[479602618e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479602618e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `gmtStart` | string | 是 | 开始日期如2022-07-01 |
| `gmtEnd` | string | 是 | 结束日期如2022-07-01 |
| `warehouseIds` | array&lt;integer> | 否 | 仓库ID数组 |
| `goodsSkuOuterIds` | string | 否 | 商品SKU |
| `goodsSkuOuterIdsRp` | string | 否 | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsName` | string | 否 | 商品名称 |
| `goodsNameRp` | string | 否 | 商品名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsGroupIds` | array&lt;integer> | 否 | 商品分组ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsList` | array&lt;object> | 否 |  |
| `data.goodsList[].rank` | string | 否 | 排名 |
| `data.goodsList[].turnoverRate` | string | 否 | 周转率（%） |
| `data.goodsList[].turnoverDay` | string | 否 | 周转天数（天） |
| `data.goodsList[].saleRate` | string | 否 | 动销率（%） |
| `data.goodsList[].endDtStockNum` | string | 否 | 期末库存总量 |
| `data.goodsList[].endDtStockCostAmount` | string | 否 | 期末库存成本 |
| `data.goodsList[].startDtStockNum` | string | 否 | 期初库存总量 |
| `data.goodsList[].startDtStockCostAmount` | string | 否 | 期初库存成本 |
| `data.goodsList[].confirmUseGoodsSkuWarehouseCount` | string | 否 | 销售出库数量 |
| `data.goodsList[].confirmUseGoodsSkuWarehouseCostAmount` | string | 否 | 销售出库成本 |
| `data.goodsList[].otherOutStorageCount` | string | 否 | 其他出库数量 |
| `data.goodsList[].otherOutStorageCostAmount` | string | 否 | 其他出库成本 |
| `data.goodsList[].allInStorageCount` | string | 否 | 入库数量 |
| `data.goodsList[].allInStorageCostAmount` | string | 否 | 入库成本 |
| `data.goodsList[].goodsSkuInfo` | object | 否 | 商品信息 |
| `data.goodsList[].goodsSkuInfo.goodsName` | string | 否 | 商品名称 |
| `data.goodsList[].goodsSkuInfo.goodsMode` | string | 否 | 商品类型 |
| `data.goodsList[].goodsSkuInfo.goodsId` | string | 否 | 商品id |
| `data.goodsList[].goodsSkuInfo.goodsSkuId` | string | 否 | 商品SKUid |
| `data.goodsList[].goodsSkuInfo.goodsSkuOuterId` | string | 否 | sku |
| `data.goodsList[].goodsSkuInfo.logoOssPath` | string | 否 | 图片地址 |
| `data.goodsList[].goodsSkuInfo.goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsList[].goodsSkuInfo.goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsList[].goodsSkuInfo.logoUrl` | string | 否 | 图片url |
| `data.total` | integer | 否 | 总数 |
