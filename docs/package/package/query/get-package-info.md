# 获取订单包裹详情


- 层级：开放平台 > 包裹 > 包裹 > 获取包裹
- 方法+路径：`POST /open/v1/order/package/fetch/get_package_info`
- 类型：读
- 原文：[524317132e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/524317132e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 订单包裹id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.orderPackageInfo` | object | 否 | 订单信息 |
| `data.orderPackageInfo.platform` | string | 否 | 归属平台 |
| `data.orderPackageInfo.platformName` | string | 否 | 平台名称 |
| `data.orderPackageInfo.site` | string | 否 | 站点 |
| `data.orderPackageInfo.siteName` | string | 否 | 站点名称 |
| `data.orderPackageInfo.shopId` | integer | 否 | 店铺id |
| `data.orderPackageInfo.shopNick` | string | 否 | 店铺别名 |
| `data.orderPackageInfo.shopName` | string | 否 | 店铺名称 |
| `data.orderPackageInfo.orderInfo` | object | 否 | 订单信息 |
| `data.orderPackageInfo.orderInfo.opOrderId` | integer | 否 | 订单id |
| `data.orderPackageInfo.orderInfo.shopId` | integer | 否 | 店铺id |
| `data.orderPackageInfo.orderInfo.platform` | string | 否 | 订单平台 |
| `data.orderPackageInfo.orderInfo.platformOrderSn` | string | 否 | 平台订单号 |
| `data.orderPackageInfo.orderInfo.platformOrderStatus` | string | 否 | 订单平台状态 |
| `data.orderPackageInfo.orderInfo.site` | string | 否 | 站点 |
| `data.orderPackageInfo.orderInfo.currency` | string | 否 | 货币单位 |
| `data.orderPackageInfo.orderInfo.orderAmount` | number | 否 | 订单金额 |
| `data.orderPackageInfo.orderInfo.productAmount` | number | 否 | 产品金额 |
| `data.orderPackageInfo.orderInfo.discountAmount` | number | 否 | 优惠金额 |
| `data.orderPackageInfo.orderInfo.estimatedShippingFee` | number | 否 | 预估运费费用 |
| `data.orderPackageInfo.orderInfo.actualShippingCost` | number | 否 | 实际运费 |
| `data.orderPackageInfo.orderInfo.payAmount` | number | 否 | 支付金额 |
| `data.orderPackageInfo.orderInfo.escrowAmount` | number | 否 | 预估回款金额 |
| `data.orderPackageInfo.orderInfo.commissionFee` | number | 否 | 平台佣金 |
| `data.orderPackageInfo.orderInfo.paymentMethod` | string | 否 | 支付方式 |
| `data.orderPackageInfo.orderInfo.gmtOrderStart` | string | 否 | 创建时间 |
| `data.orderPackageInfo.orderInfo.gmtOrderModified` | string | 否 | 修改时间 |
| `data.orderPackageInfo.orderInfo.gmtPay` | string | 否 | 支付时间 |
| `data.orderPackageInfo.orderInfo.gmtLastDelivery` | string | 否 | 最迟发货时间 |
| `data.orderPackageInfo.orderInfo.gmtDelivery` | string | 否 | 发货时间 |
| `data.orderPackageInfo.orderInfo.gmtRefund` | string | 否 | 取消时间 |
| `data.orderPackageInfo.orderInfo.gmtFinish` | string | 否 | 完结时间 |
| `data.orderPackageInfo.orderInfo.gmtSettlement` | string | 否 | 结算时间 |
| `data.orderPackageInfo.orderInfo.isCod` | boolean | 否 | 是否货到付款 |
| `data.orderPackageInfo.orderInfo.appOrderStatus` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageInfo.orderInfo.appNote` | string | 否 | 本地备注 |
| `data.orderPackageInfo.orderInfo.sellerNote` | string | 否 | 商家备注 |
| `data.orderPackageInfo.orderInfo.buyerMessage` | string | 否 | 卖家留言 |
| `data.orderPackageInfo.orderInfo.platformOrderDetailUrl` | string | 否 | 订单图片 url |
| `data.orderPackageInfo.orderInfo.platformWarehouseName` | string | 否 | 平台仓库名称 |
| `data.orderPackageInfo.orderInfo.appOrderStatusText` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageInfo.orderInfo.exchangeRate` | number | 否 | 费率 |
| `data.orderPackageInfo.consigneeInfo` | object | 否 | 收件人数据 |
| `data.orderPackageInfo.consigneeInfo.country` | string | 否 | 收件人国家二字码 |
| `data.orderPackageInfo.consigneeInfo.countryName` | string | 否 | 收件国家名称 |
| `data.orderPackageInfo.consigneeInfo.state` | string | 否 | 收件人 州/省 |
| `data.orderPackageInfo.consigneeInfo.city` | string | 否 | 收件人城市 |
| `data.orderPackageInfo.items` | array&lt;object> | 否 | 商品数据 |
| `data.orderPackageInfo.items[].opOrderItemId` | string | 否 | 订单item Id |
| `data.orderPackageInfo.items[].opOrderPackageId` | string | 否 | 妙手包裹id |
| `data.orderPackageInfo.items[].opOrderPackageItemId` | integer | 否 | 订单包裹item id |
| `data.orderPackageInfo.items[].platformOrderItemIndex` | string | 否 | 平台商品唯一标识 |
| `data.orderPackageInfo.items[].platformItemId` | string | 否 | 产品id |
| `data.orderPackageInfo.items[].platformSkuId` | string | 否 | 平台skuId |
| `data.orderPackageInfo.items[].platformItemNum` | string | 否 | 平台主货号 |
| `data.orderPackageInfo.items[].platformOuterSkuId` | string | 否 | 平台对外展示skuId |
| `data.orderPackageInfo.items[].title` | string | 否 | 标题 |
| `data.orderPackageInfo.items[].skuSubName` | string | 否 | 规格 |
| `data.orderPackageInfo.items[].quantity` | integer | 否 | 数量 |
| `data.orderPackageInfo.items[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageInfo.items[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageInfo.items[].picUrl` | string | 否 | 商品图片 |
| `data.orderPackageInfo.items[].originalPicUrl` | string | 否 | 商品原图 |
| `data.orderPackageInfo.items[].isGift` | string | 否 | 是否礼品 |
| `data.orderPackageInfo.giftItems` | array&lt;object> | 否 | 赠品数据 |
| `data.orderPackageInfo.giftItems[].opOrderPackageGiftId` | integer | 否 | 包裹赠品id |
| `data.orderPackageInfo.giftItems[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.orderPackageInfo.giftItems[].goodsId` | integer | 否 | 商品id |
| `data.orderPackageInfo.giftItems[].goodsSkuId` | integer | 否 | 商品skuId |
| `data.orderPackageInfo.giftItems[].goodsName` | string | 否 | 商品标题 |
| `data.orderPackageInfo.giftItems[].itemNum` | string | 否 | 平台主货号 |
| `data.orderPackageInfo.giftItems[].goodsSkuSubName` | string | 否 | 规格 |
| `data.orderPackageInfo.giftItems[].goodsSkuOuterId` | string | 否 | 对外展示 sku |
| `data.orderPackageInfo.giftItems[].quantity` | integer | 否 | 数量 |
| `data.orderPackageInfo.giftItems[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageInfo.giftItems[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageInfo.giftItems[].picUrl` | string | 否 | 图片 |
| `data.orderPackageInfo.logisticsAgentProductInfo` | object | 否 | 物流渠道数据/头程物流渠道数据 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageInfo.logisticsAgentProductInfo.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageInfo.logisticsAgentProductInfo.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageInfo.logisticsAgentProductInfo.status` | string | 否 | 渠道状态 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageInfo.logisticsAgentProductInfo.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageInfo.logisticsAgentProductInfo.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageInfo.logisticsAgentProductInfo.shippingFee` | number | 否 | 费用 |
| `data.orderPackageInfo.logisticsAgentProductInfo.shippingFeeCurrency` | string | 否 | 费用货币 |
| `data.orderPackageInfo.logisticsAgentProductInfo.warehouseName` | string | 否 | 仓库名称 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile` | object | 否 | 尾程物流渠道数据 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.status` | string | 否 | 渠道状态 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.combineProductName` | string | 否 | 拼接渠道 |
| `data.orderPackageInfo.appPackageNo` | string | 否 | 妙手包裹号 |
| `data.orderPackageInfo.platformPackageStatus` | string | 否 | 平台包裹状态 |
| `data.orderPackageInfo.appPackageStatus` | string | 否 | erp 包裹状态 |
| `data.orderPackageInfo.appPackageStatusText` | string | 否 | erp 包裹状态 |
| `data.orderPackageInfo.applyTrackingNoFailReason` | string | 否 | 申请失败原因 |
| `data.orderPackageInfo.applyTrackingNoFailCode` | string | 否 | 申请失败错误吗 |
| `data.orderPackageInfo.fulfillmentType` | string | 否 | 订单类型 |
| `data.orderPackageInfo.logisticsNo` | string | 否 | 跟踪号 |
| `data.orderPackageInfo.opOrderPackageId` | integer | 否 | 妙手包裹Id |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust` | object | 否 | 美客多重量尺寸和运费调整信息 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.weight` | number | 否 | 包裹重量 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.length` | number | 否 | 包裹长 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.height` | number | 否 | 包裹高 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.width` | number | 否 | 包裹宽 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.cost` | number | 否 | 商家运费 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.compensation` | number | 否 | 补扣运费 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.hasWeightDimensionDiff` | boolean | 否 | 包裹重量尺寸是否有差异 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "opOrderPackageId": 43717
}
```
&lt;/details>
