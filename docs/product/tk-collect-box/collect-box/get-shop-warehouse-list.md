# 获取店铺仓库列表


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_shop_warehouse_list`
- 类型：读
- 原文：[446814590e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814590e0.md)

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
| `data.shopWarehouseList` | array&lt;object> | 否 | 店铺仓库列表 |
| `data.shopWarehouseList[].shopId` | integer | 否 | 店铺ID |
| `data.shopWarehouseList[].shopName` | string | 否 | 店铺名称 |
| `data.shopWarehouseList[].platform` | string | 否 | 平台 |
| `data.shopWarehouseList[].site` | string | 否 | 站点 |
| `data.shopWarehouseList[].warehouseList` | array&lt;object> | 否 | 仓库列表 |
| `data.shopWarehouseList[].warehouseList[].shopId` | string | 否 | 店铺ID |
| `data.shopWarehouseList[].warehouseList[].warehouseId` | string | 否 | 仓库ID |
| `data.shopWarehouseList[].warehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.shopWarehouseList[].warehouseList[].warehouseSubType` | string | 否 | 仓库子类型 |
| `data.shopWarehouseList[].warehouseList[].warehouseEffectStatus` | string | 否 | 仓库生效状态 |
| `data.shopWarehouseList[].warehouseList[].isDefault` | string | 否 | 是否默认仓库 |
| `data.shopWarehouseList[].warehouseList[].inventoryRule` | object | 否 | 库存规则 |
| `data.shopWarehouseList[].warehouseList[].inventoryRule.allocationMode` | string | 否 | 库存分配模式 |
| `data.shopWarehouseList[].warehouseList[].inventoryRule.associatedWarehouses` | array&lt;object> | 否 | 关联仓库列表 |
