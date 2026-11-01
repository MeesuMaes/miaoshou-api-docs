# 获取缺货、备货建议列表


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_suggest/fetch/search_goods_purchase_suggest_page`
- 类型：读
- 原文：[479599782e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599782e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `warehouseId` | array&lt;integer> | 否 | 仓库ID |
| `goodsSupplierId` | integer | 否 | 供货商 |
| `type` | string | 否 | 类型(默认是备货),stockUp备货,outOfStock缺货 |
| `source` | string | 否 | other/1688 |
| `shopIds` | array&lt;integer> | 否 | 店铺id |
| `goodsCodeValue` | string | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.purchaseSuggestList` | array&lt;object> | 否 | 商品采购建议列表 |
| `data.purchaseSuggestList[].goodsId` | integer | 否 | 商品id |
| `data.purchaseSuggestList[].goodsSkuId` | integer | 否 | 商品sku id |
| `data.purchaseSuggestList[].dailySales` | integer | 否 | 日销量 |
| `data.purchaseSuggestList[].minTriggerSuggestNum` | integer | 否 | 采购下限 |
| `data.purchaseSuggestList[].maxPrepareDays` | integer | 否 | 最大备货天数 |
| `data.purchaseSuggestList[].minPrepareDays` | integer | 否 | 最小备货天数 |
| `data.purchaseSuggestList[].orderNeedNum` | integer | 否 | 订单需求量 |
| `data.purchaseSuggestList[].recentSaleNumDt7` | integer | 否 | 近7天销量 |
| `data.purchaseSuggestList[].recentSaleNumDt30` | integer | 否 | 近30天销量 |
| `data.purchaseSuggestList[].suggestNum` | integer | 否 | 建议数量 |
| `data.purchaseSuggestList[].safeStockNum` | integer | 否 | 安全库存 |
| `data.total` | integer | 否 | 总计 |
