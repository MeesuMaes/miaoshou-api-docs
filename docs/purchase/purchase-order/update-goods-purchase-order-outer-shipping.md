# 采购单更新平台运单信息


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_outer_shipping`
- 类型：写
- 原文：[479599777e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599777e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单ID |
| `purchaseOrderInfo` | object | 否 | 采购单信息 |
| `purchaseOrderInfo.purchasePlatform` | string | 否 | 下单平台 |
| `purchaseOrderInfo.purchaseOrderSn` | string | 否 | 货源单号 |
| `purchaseOrderInfo.purchaseOrderBuyer` | string | 否 | 买家帐号 |
| `purchaseOrderInfo.purchaseOrderSeller` | string | 否 | 卖家帐号 |
| `purchaseOrderInfo.purchaseOrderPackages` | array&lt;object> | 否 | 包裹信息 |
| `purchaseOrderInfo.purchaseOrderPackages[].purchaseOrderLogisticsName` | string | 否 | 物流公司 |
| `purchaseOrderInfo.purchaseOrderPackages[].purchaseOrderWaybillCode` | string | 否 | 快递单号 |
| `shippingId` | string | 否 | 运单ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
