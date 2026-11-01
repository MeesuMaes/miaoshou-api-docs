# 获取平台仓库列表


- 层级：开放平台 > 仓储 > 仓库 > 三方仓仓库
- 方法+路径：`POST /open/v1/ewm/third_warehouse/fetch/search_platform_warehouse_page`
- 类型：读
- 原文：[479592193e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592193e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `platformWarehouseType` | string | 是 | 平台类型 FBT / FBA |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.warehouseList` | array&lt;object> | 否 |  |
| `data.warehouseList[].logisticsAgentWarehouseId` | string | 否 | ID |
| `data.warehouseList[].logisticsAgentId` | string | 否 | 服务商ID |
| `data.warehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.warehouseList[].platformWarehouseId` | string | 否 | 平台仓库ID |
| `data.warehouseList[].platformWarehouseCode` | string | 否 | 平台仓库编码 |
| `data.warehouseList[].address` | string | 否 | 地址 |
| `data.warehouseList[].platformWarehouseType` | string | 否 | 平台仓库类型 |
| `data.warehouseList[].shopName` | string | 否 | 店铺名称 |
| `data.warehouseList[].thirdWarehouseProviderAuthId` | integer | 否 | 三方仓服务商授权ID |
| `data.total` | integer | 否 |  |
