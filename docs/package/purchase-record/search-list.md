# 采购记录列表


- 层级：开放平台 > 包裹 > 采购记录
- 方法+路径：`POST /open/v1/order/purchase_order/purchase_record/search_list`
- 类型：读
- 原文：[523326861e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523326861e0.md)

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
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `sortType` | string | 否 | 排序方式 |
| `shopIds` | array&lt;integer> | 否 | 店铺ids |
| `purchasePlatform` | string | 否 | 采购平台 |
| `purchaseOrderStatus` | string | 否 | 采购单状态 |
| `purchaseOrderSeller` | string | 否 | 采购单卖家/供应商 |
| `warningType` | string | 否 | 预警类型 |
| `snType` | string | 否 | 搜索类型: purchaseOrderSn, purchaseOrderBuyer, platformOrderSn, appPackageNo, waybillCode, logisticsName, platformOuterSkuId, platformItemId |
| `snValue` | string | 否 | 搜索值 |
| `gmtRangeType` | string | 否 | 时间范围类型: gmtPurchaseOrderStart, gmtLastRsync, gmtPay, gmtLastUrgeShip, gmtOrderStart, gmtShip, gmtSign, signDuringTime |
| `gmtRangeFrom` | string | 否 | 时间范围起始 |
| `gmtRangeTo` | string | 否 | 时间范围结束 |
| `relateStatus` | string | 否 | 关联状态 |
| `forwarderId` | integer | 否 | 货代id |
| `buyerPhone` | string | 否 | 收件人手机号 |
| `appPackageStatus` | string | 否 | 订单包裹状态 |
| `isFilterAbnormal` | integer | 否 | 是否过滤异常 |
| `gmtPurchaseOrderStartFrom` | string | 否 | 采购下单时间起始 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.list` | array&lt;object> | 否 |  |
| `data.list[].purchaseOrderSn` | string | 否 | 采购单号 |
| `data.list[].waybillCode` | string | 否 | 采购物流单号 |
| `data.list[].purchasePlatformName` | string | 否 | 采购平台名称 |
| `data.list[].gmtPurchaseOrderStart` | string | 否 | 采购时间 |
| `data.list[].purchaseOrderSeller` | string | 否 | 供应商名称 |
| `data.list[].purchaseOrderPayment` | string | 否 | 实付金额 |
| `data.list[].purchaseOrderShippingFee` | string | 否 | 运费金额 |
| `data.list[].purchaseOrderOtherFee` | string | 否 | 其他金额 |
| `data.list[].purchaseItems` | array&lt;object> | 否 | 采购商品列表 |
| `data.list[].purchaseItems[].sourceTitle` | string | 否 | 采购商品名称 |
| `data.list[].purchaseItems[].sourceSkuSubName` | string | 否 | 采购商品规格名称 |
| `data.list[].purchaseItems[].sourceSendGoodsAddress` | string | 否 | 采购商品发货地 |
| `data.list[].purchaseItems[].sourceUnitPrice` | string | 否 | 采购商品单价 |
| `data.list[].purchaseItems[].sourceQuantity` | string | 否 | 采购商品规格数量 |
| `data.list[].purchaseOrderPackages` | array&lt;object> | 否 | 采购物流包裹列表 |
| `data.list[].purchaseOrderPackages[].logisticsName` | string | 否 | 物流名称 |
| `data.list[].purchaseOrderPackages[].waybillCode` | string | 否 | 采购物流单号 |
| `data.list[].purchaseOrderPackages[].signDuringTime` | integer | 否 | 签收时长(秒) |
| `data.list[].purchaseOrderPackages[].isSubscribeLogistics` | integer | 否 | 是否订阅物流 |
| `data.list[].purchaseOrderPackages[].failCode` | string | 否 | 失败码 |
| `data.list[].purchaseOrderPackages[].failReason` | string | 否 | 失败原因 |
| `data.list[].purchaseOrderPackages[].gmtLastLogisticsTrace` | string | 否 | 最新物流轨迹时间 |
| `data.list[].purchaseOrderPackages[].gmtSign` | string | 否 | 签收时间 |
| `data.list[].purchaseOrderPackages[].gmtShip` | string | 否 | 发货时间 |
| `data.list[].opOrderPackageList` | array&lt;object> | 否 | 关联订单包裹列表 |
| `data.list[].opOrderPackageList[].platformOrderSn` | string | 否 | 订单号 |
| `data.list[].opOrderPackageList[].shopName` | string | 否 | 店铺 |
| `data.list[].opOrderPackageList[].platform` | string | 否 | 平台 |
| `data.list[].opOrderPackageList[].relateStatus` | string | 否 | 关联状态枚举值  normal:关联  cancel：取消关联 |
| `data.list[].opOrderPackageList[].purchaseItems` | array&lt;object> | 否 | 订单商品列表 |
| `data.list[].opOrderPackageList[].purchaseItems[].title` | string | 否 | 产品名称 |
| `data.list[].opOrderPackageList[].purchaseItems[].skuSubName` | string | 否 | 规格 |
| `data.list[].opOrderPackageList[].purchaseItems[].platformItemId` | string | 否 | 产品ID |
| `data.list[].opOrderPackageList[].purchaseItems[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.list[].opOrderPackageList[].purchaseItems[].unitPrice` | string | 否 | 单价 |
| `data.list[].opOrderPackageList[].purchaseItems[].quantity` | integer | 否 | 数量 |
| `data.list[].opOrderPackageList[].purchaseItems[].picUrl` | string | 否 | 产品图片 |
| `data.total` | integer | 否 |  |
