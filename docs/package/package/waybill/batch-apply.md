# 批量申请运单号


- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking_no/batch_apply`
- 类型：写
- 原文：[523411121e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523411121e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array&lt;integer> | 是 | 订单包裹IDs |
| `shippingMethod` | string | 否 | 配送方式 (shopee专用) |
| `addressId` | string | 否 | 取件地址 (shopee专用) shippingMethod为pickup时必填 |
| `pickupTimeId` | integer | 否 | 取件时间ID (shopee专用) |
| `trackingNo` | string | 否 | 运单号(shopee专用) |
| `slug` | string | 否 | 物流渠道(shopee专用) |
| `senderRealName` | string | 否 | 发件人名称(shopee专用) |
| `isShipAfterHasLogisticsNo` | string | 否 | 是否获取跟踪单号并发货 |
| `isSetDefaultAddress` | string | 否 | 是否设置为默认地址(shopee专用) |
| `partItemRelationSupplierGoodsProcessType` | string | 否 | 部分商品关联了分销商品时候处理方式，skipPackage 跳过整个包裹， skipNotRelationItem 跳过没关联的商品 |
| `isConfirmSupplierGoodsSkuIdChange` | integer | 否 | 推送供应商商品是否改变0、1 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.trackingNoInfos` | array&lt;object> | 否 | 运单号数据列表 |
| `data.trackingNoInfos[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.trackingNoInfos[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.trackingNoInfos[].platformPackageId` | string | 否 | 平台包裹id |
| `data.trackingNoInfos[].logisticsNo` | string | 否 | 运单号 |
| `data.errors` | array&lt;object> | 否 | 错误数据 |
| `data.errors[].errMsg` | string | 否 | 错误描述 |
| `data.errors[].errCode` | string | 否 | 错误code |
| `data.errors[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.errors[].opOrderId` | integer | 否 | 妙手订单id |
| `data.errors[].platformOrderSn` | string | 否 | 妙手订单编号 |
| `data.errors[].platformPackageId` | string | 否 | 平台包裹id |
| `data.errors[].appPackageNo` | string | 否 | 包裹号 |
| `data.errors[].logisticsNo` | string | 否 | 跟踪号 |
| `data.errors[].logisticsCompany` | string | 否 | 物流公司 |
| `data.errors[].logisticsAgentAuthId` | string | 否 | 授权id |
| `data.errors[].logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.errors[].logisticsAgentId` | integer | 否 | 物流id |
| `data.errors[].agentName` | string | 否 | 物流名称 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "opOrderPackageIds": [
    2008407593,
    1999236402,
    1992973198,
    1990087996,
    1990087975,
    1990077182,
    1990059646,
    1276648263,
    1274794190,
    1274740924,
    1274689828,
    1274624282,
    1274624254,
    1274121129,
    1274044406,
    1273927611,
    1273924534,
    1271460840,
    1271458829,
    1271158800
  ]
}
```
&lt;/details>
