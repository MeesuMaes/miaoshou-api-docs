# 获取仓库信息列表


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_global_shop_warehouse`
- 类型：读
- 原文：[516158668e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516158668e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.warehouseLocationList` | array&lt;object> | 否 | 仓库信息列表 |
| `data.warehouseLocationList[].locationId` | string | 否 | 属性ID |
| `data.warehouseLocationList[].shopName` | string | 否 | 店铺别名 |
| `data.warehouseLocationList[].warehouseLocationType` | string | 否 | 仓库类型（local本土，cb跨境） |
| `data.warehouseLocationList[].warehouseName` | string | 否 | 仓库名称 |
