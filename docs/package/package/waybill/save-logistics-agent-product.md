# 设置包裹物流


- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking_no/save_logistics_agent_product`
- 类型：写
- 原文：[457269520e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457269520e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array&lt;integer> | 是 | 包裹IDs |
| `logisticsAgentAuthConfigId` | integer | 是 | 授权物流配置ID |
| `type` | string | 是 | logisticsAgent-物流商，thirdWarehouse-三方仓物流 |
| `logisticsAgentWarehouseChannelConfigId` | integer | 否 | type=thirdWarehouse时必填 |
| `aliexpressDomesticLogisticsCompanyName` | string | 否 | 速卖通国内物流公司 |
| `aliexpressDomesticLogisticsCompanyId` | integer | 否 | 速卖通国内物流公司ID |
| `aliexpressDomesticTrackingNo` | string | 否 | 速卖通国内物流单号 |
| `warehouseId` | integer | 否 | 暂时只对temu在线物流生效 |
| `partItemRelationSupplierGoodsProcessType` | string | 否 | skipPackage 跳过整个包裹， skipNotRelationItem 跳过没关联的商品 |
| `isShipLater` | string | 否 | 暂时只对temu在线物流生效 |
| `packageWeightAndDimension` | object | 是 | \{"1044122969":\{"length":1,"width":1,"height":1,"dimensionUnit":"in","weight":1,"weightUnit":"lb","isSavePackageWeightAndDimension":0\}\} |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array&lt;object> | 是 |  |
| `data[].successCount` | string | 是 |  |
| `data[].failCount` | string | 是 |  |
| `data[].errors` | object | 是 |  |
| `data[].errors.errMsg` | string | 是 | 错误描述 |
| `data[].errors.errCode` | string | 是 | 错误code |
| `data[].errors.opOrderPackageId` | string | 是 | 妙手包裹id |
| `data[].errors.opOrderId` | string | 是 | 妙手订单id |
| `data[].errors.platformOrderSn` | string | 是 | 妙手订单编号 |
| `data[].errors.platformPackageId` | string | 是 | 平台包裹id |
| `data[].errors.appPackageNo` | string | 是 | 包裹号 |
| `data[].errors.logisticsNo` | string | 是 | 跟踪号 |
| `data[].errors.logisticsCompany` | string | 是 | 物流公司 |
| `data[].errors.logisticsAgentAuthId` | string | 是 | 授权id |
| `data[].errors.logisticsAgentProductId` | string | 是 | 物流渠道id |
| `data[].errors.logisticsAgentId` | string | 是 | 物流id |
| `data[].errors.gentName` | string | 是 | 物流名称 |
