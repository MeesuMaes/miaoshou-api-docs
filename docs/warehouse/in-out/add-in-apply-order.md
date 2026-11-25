# 新建入库申请单


- 层级：开放平台 > 仓储 > 出入库
- 方法+路径：`POST /open/v1/ewm/goods_out_in/operate/add_in_apply_order`
- 类型：写
- 原文：[532434241e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/532434241e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `warehouseId` | integer | 是 | 仓库ID |
| `bizCode` | string | 是 | 入库业务类型;(inventory_profit_in_storage:盘盈入库,allocate_in_storage:调拨入库,manual_return_in_storage:手动退货入库,manual_purchase_in_storage:手动采购入库,other_in_storage:其他入库) |
| `goodsSkuList` | array&lt;object> | 是 | 商品sku列表 |
| `goodsSkuList[].goodsSkuOuterId` | string | 是 | 商品SKU |
| `goodsSkuList[].purchasePrice` | string | 否 | 单价(入库时填写) |
| `goodsSkuList[].storageList` | array&lt;object> | 是 | 库存信息列表 |
| `goodsSkuList[].storageList[].warehouseShelfCellId` | integer | 是 | 仓位ID |
| `goodsSkuList[].storageList[].quantity` | integer | 是 | 出入库数量 |
| `note` | string | 否 | 备注 |
| `saveType` | string | 是 | 保存类型 save(保存), saveAndSubmit (保存并入库) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuWarehouseOutInApplyOrderId` | integer | 否 | 出入库申请单ID |
