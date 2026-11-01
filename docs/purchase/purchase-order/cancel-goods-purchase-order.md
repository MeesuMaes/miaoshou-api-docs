# 取消采购单


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/cancel_goods_purchase_order`
- 类型：写
- 原文：[479599778e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599778e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |
| `cancelReason` | string | 是 | 取消原因 缺货：outOfStock，换货：exchangeGoods，不想要了：dontWant，其他：other |
| `cancelNote` | string | 否 | 备注说明 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
