# 通过采购单id批量添加1688商品采购单


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order_by_goods_purchase_order_ids`
- 类型：写
- 原文：[479599780e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599780e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderIds` | array&lt;integer> | 是 | 采购单IDs |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successDataList` | object | 否 | 成功数据列表 |
| `data.successDataList.index` | string | 否 | 序号 |
| `data.successDataList.goodsPurchaseOrderSn` | string | 否 | 采购单号 |
| `data.successDataList.purchaseOrderSn` | string | 否 | 1688单号 |
| `data.successDataList.goodsPurchaseOrderId` | string | 否 | 采购单ID |
| `data.errors` | object | 否 | 错误数据列表 |
| `data.errors.index` | string | 否 | 序号 |
| `data.errors.errorMsg` | string | 否 | 错误信息 |
| `data.errors.errorType` | string | 否 | 错误类型 |
| `data.errors.goodsPurchaseOrderSn` | string | 否 | 采购单号 |
| `data.errors.purchaseOrderSn` | string | 否 | 1688单号 |
| `data.errors.goodsPurchaseOrderId` | string | 否 | 采购单ID |
| `data.successGoodsPurchaseOrderIds` | array&lt;integer> | 否 | 成功的采购订单ID列表 |
