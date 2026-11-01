# 批量获取面单


- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/waybill/batch_get_waybill`
- 类型：读
- 原文：[523411122e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523411122e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array&lt;integer> | 是 | 订单包裹IDs |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.waybillPdfInfos` | array&lt;object> | 否 | 面单数据列表 |
| `data.waybillPdfInfos[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.waybillPdfInfos[].platformPackageId` | string | 否 | 平台包裹id |
| `data.waybillPdfInfos[].url` | string | 否 | 面单url |
| `data.waybillPdfInfos[].opOrderPackageId` | integer | 否 | 妙手包裹id |
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
