# 获取订单包裹列表


- 层级：开放平台 > 包裹 > 包裹 > 获取包裹
- 方法+路径：`POST /open/v1/order/package/fetch/search_package_list`
- 类型：读
- 原文：[524317133e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/524317133e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `platform` | string | 否 | 平台 |
| `shopIds` | array&lt;integer> | 否 | 店铺ids |
| `appPackageStatus` | string | 否 | 包裹状态 |
| `platformOrderSns` | string | 否 | 订单号[多个逗号分割] |
| `gmtCreateFrom` | string | 否 | 妙手创建时间 -开始 |
| `gmtCreateTo` | string | 否 | 妙手创建时间 -结束 |
| `gmtModifiedFrom` | string | 否 | 妙手修改时间 -开始 |
| `gmtModifiedTo` | string | 否 | 妙手修改时间 -结束 |
| `appPackageTab` | string | 否 | 妙手包裹tab(顶层tab) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.orderPackageList` | array&lt;object> | 否 | 订单列表信息 |
| `data.orderPackageList[].platform` | string | 否 | 归属平台 |
| `data.orderPackageList[].platformName` | string | 否 | 平台名称 |
| `data.orderPackageList[].site` | string | 否 | 站点 |
| `data.orderPackageList[].siteName` | string | 否 | 站点名称 |
| `data.orderPackageList[].shopId` | integer | 否 | 店铺id |
| `data.orderPackageList[].shopNick` | string | 否 | 店铺别名 |
| `data.orderPackageList[].shopName` | string | 否 | 店铺名称 |
| `data.orderPackageList[].orderInfo` | object | 否 | 订单信息 |
| `data.orderPackageList[].orderInfo.opOrderId` | integer | 否 | 订单id |
| `data.orderPackageList[].orderInfo.shopId` | integer | 否 | 店铺id |
| `data.orderPackageList[].orderInfo.platform` | string | 否 | 订单平台 |
| `data.orderPackageList[].orderInfo.platformOrderSn` | string | 否 | 平台订单号 |
| `data.orderPackageList[].orderInfo.platformOrderStatus` | string | 否 | 订单平台状态 |
| `data.orderPackageList[].orderInfo.site` | string | 否 | 站点 |
| `data.orderPackageList[].orderInfo.currency` | string | 否 | 货币单位 |
| `data.orderPackageList[].orderInfo.orderAmount` | number | 否 | 订单金额 |
| `data.orderPackageList[].orderInfo.productAmount` | number | 否 | 产品金额 |
| `data.orderPackageList[].orderInfo.discountAmount` | number | 否 | 优惠金额 |
| `data.orderPackageList[].orderInfo.estimatedShippingFee` | number | 否 | 预估运费费用 |
| `data.orderPackageList[].orderInfo.actualShippingCost` | number | 否 | 实际运费 |
| `data.orderPackageList[].orderInfo.payAmount` | number | 否 | 支付金额 |
| `data.orderPackageList[].orderInfo.escrowAmount` | number | 否 | 预估回款金额 |
| `data.orderPackageList[].orderInfo.commissionFee` | number | 否 | 平台佣金 |
| `data.orderPackageList[].orderInfo.paymentMethod` | string | 否 | 支付方式 |
| `data.orderPackageList[].orderInfo.gmtOrderStart` | string | 否 | 创建时间 |
| `data.orderPackageList[].orderInfo.gmtOrderModified` | string | 否 | 修改时间 |
| `data.orderPackageList[].orderInfo.gmtPay` | string | 否 | 支付时间 |
| `data.orderPackageList[].orderInfo.gmtLastDelivery` | string | 否 | 最迟发货时间 |
| `data.orderPackageList[].orderInfo.gmtDelivery` | string | 否 | 发货时间 |
| `data.orderPackageList[].orderInfo.gmtRefund` | string | 否 | 取消时间 |
| `data.orderPackageList[].orderInfo.gmtFinish` | string | 否 | 完结时间 |
| `data.orderPackageList[].orderInfo.gmtSettlement` | string | 否 | 结算时间 |
| `data.orderPackageList[].orderInfo.isCod` | boolean | 否 | 是否货到付款 |
| `data.orderPackageList[].orderInfo.appOrderStatus` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageList[].orderInfo.appNote` | string | 否 | 本地备注 |
| `data.orderPackageList[].orderInfo.sellerNote` | string | 否 | 商家备注 |
| `data.orderPackageList[].orderInfo.buyerMessage` | string | 否 | 卖家留言 |
| `data.orderPackageList[].orderInfo.platformOrderDetailUrl` | string | 否 | 订单图片 url |
| `data.orderPackageList[].orderInfo.platformWarehouseName` | string | 否 | 平台仓库名称 |
| `data.orderPackageList[].orderInfo.appOrderStatusText` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageList[].orderInfo.exchangeRate` | number | 否 | 费率 |
| `data.orderPackageList[].consigneeInfo` | object | 否 | 收件人数据 |
| `data.orderPackageList[].consigneeInfo.country` | string | 否 | 收件人国家二字码 |
| `data.orderPackageList[].consigneeInfo.countryName` | string | 否 | 收件国家名称 |
| `data.orderPackageList[].consigneeInfo.state` | string | 否 | 收件人 州/省 |
| `data.orderPackageList[].consigneeInfo.city` | string | 否 | 收件人城市 |
| `data.orderPackageList[].items` | array&lt;object> | 否 | 商品数据 |
| `data.orderPackageList[].items[].opOrderItemId` | string | 否 | 订单item Id |
| `data.orderPackageList[].items[].opOrderPackageId` | string | 否 | 妙手包裹id |
| `data.orderPackageList[].items[].opOrderPackageItemId` | integer | 否 | 订单包裹item id |
| `data.orderPackageList[].items[].platformOrderItemIndex` | string | 否 | 平台商品唯一标识 |
| `data.orderPackageList[].items[].platformItemId` | string | 否 | 产品id |
| `data.orderPackageList[].items[].platformSkuId` | string | 否 | 平台skuId |
| `data.orderPackageList[].items[].platformItemNum` | string | 否 | 平台主货号 |
| `data.orderPackageList[].items[].platformOuterSkuId` | string | 否 | 平台对外展示skuId |
| `data.orderPackageList[].items[].title` | string | 否 | 标题 |
| `data.orderPackageList[].items[].skuSubName` | string | 否 | 规格 |
| `data.orderPackageList[].items[].quantity` | integer | 否 | 数量 |
| `data.orderPackageList[].items[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageList[].items[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageList[].items[].picUrl` | string | 否 | 商品图片 |
| `data.orderPackageList[].items[].originalPicUrl` | string | 否 | 商品原图 |
| `data.orderPackageList[].items[].isGift` | string | 否 | 是否礼品 |
| `data.orderPackageList[].giftItems` | array&lt;object> | 否 | 赠品数据 |
| `data.orderPackageList[].giftItems[].opOrderPackageGiftId` | integer | 否 | 包裹赠品id |
| `data.orderPackageList[].giftItems[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.orderPackageList[].giftItems[].goodsId` | integer | 否 | 商品id |
| `data.orderPackageList[].giftItems[].goodsSkuId` | integer | 否 | 商品skuId |
| `data.orderPackageList[].giftItems[].goodsName` | string | 否 | 商品标题 |
| `data.orderPackageList[].giftItems[].itemNum` | string | 否 | 平台主货号 |
| `data.orderPackageList[].giftItems[].goodsSkuSubName` | string | 否 | 规格 |
| `data.orderPackageList[].giftItems[].goodsSkuOuterId` | string | 否 | 对外展示 sku |
| `data.orderPackageList[].giftItems[].quantity` | integer | 否 | 数量 |
| `data.orderPackageList[].giftItems[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageList[].giftItems[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageList[].giftItems[].picUrl` | string | 否 | 图片 |
| `data.orderPackageList[].logisticsAgentProductInfo` | object | 否 | 物流渠道数据/头程物流渠道数据 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageList[].logisticsAgentProductInfo.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageList[].logisticsAgentProductInfo.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageList[].logisticsAgentProductInfo.status` | string | 否 | 渠道状态 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageList[].logisticsAgentProductInfo.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageList[].logisticsAgentProductInfo.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageList[].logisticsAgentProductInfo.shippingFee` | number | 否 | 费用 |
| `data.orderPackageList[].logisticsAgentProductInfo.shippingFeeCurrency` | string | 否 | 费用货币 |
| `data.orderPackageList[].logisticsAgentProductInfo.warehouseName` | string | 否 | 仓库名称 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile` | object | 否 | 尾程物流渠道数据 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.status` | string | 否 | 渠道状态 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.combineProductName` | string | 否 | 拼接渠道 |
| `data.orderPackageList[].appPackageNo` | string | 否 | 妙手包裹号 |
| `data.orderPackageList[].platformPackageStatus` | string | 否 | 平台包裹状态 |
| `data.orderPackageList[].appPackageStatus` | string | 否 | erp 包裹状态 |
| `data.orderPackageList[].appPackageStatusText` | string | 否 | erp 包裹状态 |
| `data.orderPackageList[].applyTrackingNoFailReason` | string | 否 | 申请失败原因 |
| `data.orderPackageList[].applyTrackingNoFailCode` | string | 否 | 申请失败错误吗 |
| `data.orderPackageList[].fulfillmentType` | string | 否 | 订单类型 |
| `data.orderPackageList[].logisticsNo` | string | 否 | 跟踪号 |
| `data.orderPackageList[].opOrderPackageId` | integer | 否 | 妙手包裹Id |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust` | object | 否 | 美客多重量尺寸和运费调整信息 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.weight` | number | 否 | 包裹重量 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.length` | number | 否 | 包裹长 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.height` | number | 否 | 包裹高 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.width` | number | 否 | 包裹宽 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.cost` | number | 否 | 商家运费 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.compensation` | number | 否 | 补扣运费 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.hasWeightDimensionDiff` | boolean | 否 | 包裹重量尺寸是否有差异 |
| `data.total` | integer | 否 | 总数 |
| `data.page` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页数量 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "page": 1,
  "pageSize": 10
}
```
&lt;/details>
