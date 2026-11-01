# 采购记录详情


- 层级：开放平台 > 包裹 > 采购记录
- 方法+路径：`POST /open/v1/order/purchase_order/purchase_record/get_detail`
- 类型：读
- 原文：[523329034e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523329034e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

其他参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `timerToken(query)` | string | 否 |  |
| `Cookie(header)` | string | 否 |  |
| `X-Apifox-Debug(header)` | string | 否 |  |


**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `purchaseOrderSn` | string | 否 | 采购单号 |
| `waybillCode` | string | 否 | 采购物流单号 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detail` | object | 否 |  |
| `data.detail.purchaseOrderSn` | string | 否 | 采购单号 |
| `data.detail.waybillCode` | string | 否 | 采购物流单号 |
| `data.detail.purchasePlatformName` | string | 否 | 采购平台名称 |
| `data.detail.gmtPurchaseOrderStart` | string | 否 | 采购时间 |
| `data.detail.purchaseOrderSeller` | string | 否 | 供应商名称 |
| `data.detail.purchaseItems` | array&lt;object> | 否 | 采购商品列表 |
| `data.detail.purchaseItems[].sourceTitle` | string | 否 | 采购商品名称 |
| `data.detail.purchaseItems[].sourceSkuSubName` | string | 否 | 采购商品规格名称 |
| `data.detail.purchaseItems[].sourceSendGoodsAddress` | string | 否 | 采购商品发货地 |
| `data.detail.purchaseItems[].sourceUnitPrice` | string | 否 | 采购商品单价 |
| `data.detail.purchaseItems[].sourceQuantity` | string | 否 | 采购商品规格数量 |
| `data.detail.purchaseOrderPackages` | array&lt;object> | 否 | 采购物流包裹列表 |
| `data.detail.purchaseOrderPackages[].logisticsName` | string | 否 | 物流名称 |
| `data.detail.purchaseOrderPackages[].waybillCode` | string | 否 | 采购物流单号 |
| `data.detail.purchaseOrderPackages[].signDuringTime` | integer | 否 | 签收时长(秒) |
| `data.detail.purchaseOrderPackages[].isSubscribeLogistics` | integer | 否 | 是否订阅物流 |
| `data.detail.purchaseOrderPackages[].failCode` | string | 否 | 失败码 |
| `data.detail.purchaseOrderPackages[].failReason` | string | 否 | 失败原因 |
| `data.detail.purchaseOrderPackages[].gmtLastLogisticsTrace` | string | 否 | 最新物流轨迹时间 |
| `data.detail.purchaseOrderPackages[].gmtSign` | string | 否 | 签收时间 |
| `data.detail.purchaseOrderPackages[].gmtShip` | string | 否 | 发货时间 |
| `data.detail.opOrderPackageList` | array&lt;object> | 否 | 关联订单包裹列表 |
| `data.detail.opOrderPackageList[].platformOrderSn` | string | 否 | 订单号 |
| `data.detail.opOrderPackageList[].shopName` | string | 否 | 店铺 |
| `data.detail.opOrderPackageList[].platform` | string | 否 | 平台 |
| `data.detail.opOrderPackageList[].relateStatus` | string | 否 | 关联状态 |
| `data.detail.opOrderPackageList[].purchaseItems` | array&lt;object> | 否 | 订单商品列表 |
| `data.detail.opOrderPackageList[].purchaseItems[].title` | string | 否 | 产品名称 |
| `data.detail.opOrderPackageList[].purchaseItems[].skuSubName` | string | 否 | 规格 |
| `data.detail.opOrderPackageList[].purchaseItems[].platformItemId` | string | 否 | 产品ID |
| `data.detail.opOrderPackageList[].purchaseItems[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.detail.opOrderPackageList[].purchaseItems[].unitPrice` | string | 否 | 单价 |
| `data.detail.opOrderPackageList[].purchaseItems[].quantity` | integer | 否 | 数量 |
| `data.detail.opOrderPackageList[].purchaseItems[].picUrl` | string | 否 | 产品图片 |
| `data.detail.purchaseOrderPayment` | string | 否 | 实付金额 |
| `data.detail.purchaseOrderShippingFee` | string | 否 | 运费金额 |
| `data.detail.purchaseOrderOtherFee` | string | 否 | 其他金额 |
