# 获取供应商仓库列表


- 层级：开放平台 > 仓储 > 仓库 > 自营仓仓库
- 方法+路径：`POST /open/v1/ewm/warehouse/fetch/supplier_warehouse_list`
- 类型：读
- 原文：[476990600e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/476990600e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supplierWarehouseList` | array&lt;object> | 否 | 供应商仓库列表 |
| `data.supplierWarehouseList[].warehouseId` | integer | 否 | 仓库ID |
| `data.supplierWarehouseList[].warehouseName` | string | 否 | 仓库名称 |
