# 获取店铺仓库列表


- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_shop_warehouse_info_list`
- 类型：读
- 原文：[474774627e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774627e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array&lt;integer> | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopWarehouseInfoList` | array&lt;object> | 否 | 店铺仓库列表 |
| `data.shopWarehouseInfoList[].shopId` | integer | 否 | 店铺ID |
| `data.shopWarehouseInfoList[].shopNick` | string | 否 | 店铺名称 |
| `data.shopWarehouseInfoList[].warehouseList` | array&lt;object> | 否 | 仓库列表 |
| `data.shopWarehouseInfoList[].warehouseList[].shopId` | string | 否 | 店铺ID |
| `data.shopWarehouseInfoList[].warehouseList[].warehouseId` | string | 否 | 仓库ID |
| `data.shopWarehouseInfoList[].warehouseList[].name` | string | 否 | 仓库名称 |
| `data.shopWarehouseInfoList[].warehouseList[].warehouseType` | string | 否 | 仓库类型 |
| `data.shopWarehouseInfoList[].warehouseList[].isRfbs` | string | 否 | 是否是RFBS仓库 |
