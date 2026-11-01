# 获取自营仓仓库列表


- 层级：开放平台 > 仓储 > 仓库 > 自营仓仓库
- 方法+路径：`POST /open/v1/ewm/warehouse/fetch/search_warehouse_page`
- 类型：读
- 原文：[476435300e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/476435300e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.warehouseList` | array&lt;object> | 否 |  |
| `data.warehouseList[].warehouseId` | integer | 否 | 仓库ID |
| `data.warehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.warehouseList[].address` | string | 否 | 地址 |
| `data.warehouseList[].fullAddress` | string | 否 | 详细地址 |
| `data.warehouseList[].isDefault` | integer | 否 | 是否默认仓库 |
| `data.total` | integer | 否 |  |
