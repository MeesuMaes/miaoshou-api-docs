# 包裹发货


- 层级：开放平台 > 包裹 > 包裹 > 发货
- 方法+路径：`POST /open/v1/order/package/ship_package/ship_packages`
- 类型：写
- 原文：[455694578e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455694578e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array&lt;integer> | 是 | 包裹IDs |
| `isVirtualShipment` | integer | 是 | 是否虚拟发货 |
| `tiktokLocalShopShipType` | string | 是 | 枚举值（1、2）;1、pick-up；2、drop-off |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | object | 是 |  |
| `data.successOpOrderPackageIds` | string | 是 |  |
| `data.failCount` | string | 是 |  |
| `data.shipFailErrors` | array&lt;object> | 是 |  |
| `data.shipFailErrors[].errMsg` | string | 是 | 错误描述 |
| `data.shipFailErrors[].errCode` | string | 是 | 错误code |
| `data.shipFailErrors[].opOrderPackageId` | string | 是 | 妙手包裹id |
| `data.shipFailErrors[].opOrderId` | string | 是 | 妙手订单id |
| `data.shipFailErrors[].platformOrderSn` | string | 是 | 妙手订单编号 |
| `data.shipFailErrors[].platformPackageId` | string | 是 | 平台包裹id |
| `data.shipFailErrors[].appPackageNo` | string | 是 | 包裹号 |
| `data.shipFailErrors[].logisticsNo` | string | 是 | 跟踪号 |
| `data.shipFailErrors[].logisticsCompany` | string | 是 | 物流公司 |
| `data.shipFailErrors[].logisticsAgentAuthId` | string | 是 | 授权id |
| `data.shipFailErrors[].logisticsAgentProductId` | string | 是 | 物流渠道id |
| `data.shipFailErrors[].logisticsAgentId` | string | 是 | 物流id |
| `data.shipFailErrors[].gentName` | string | 是 | 物流名称 |
| `data.successCount` | string | 是 |  |
