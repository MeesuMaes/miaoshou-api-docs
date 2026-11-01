# 获取运单面单


- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/waybill/get_waybill`
- 类型：读
- 原文：[457264811e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457264811e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | string | 是 | 包裹id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array&lt;object> | 是 |  |
| `data[].waybillUrlInfo` | object | 是 | 成功数据 |
| `data[].waybillUrlInfo.platformOrderSn` | string | 是 | 平台单号 |
| `data[].waybillUrlInfo.platformPackageId` | string | 是 | 平台包裹id |
| `data[].waybillUrlInfo.url` | string | 是 | 面单url |
| `data[].error` | object | 是 |  |
| `data[].error.errMsg` | string | 是 | 错误描述 |
| `data[].error.errCode` | string | 是 | 错误code |
| `data[].error.opOrderPackageId` | string | 是 | 妙手包裹id |
| `data[].error.opOrderId` | string | 是 | 妙手订单id |
| `data[].error.platformOrderSn` | string | 是 | 妙手订单编号 |
| `data[].error.platformPackageId` | string | 是 | 平台包裹id |
| `data[].error.appPackageNo` | string | 是 | 包裹号 |
| `data[].error.logisticsNo` | string | 是 | 跟踪号 |
| `data[].error.logisticsCompany` | string | 是 | 物流公司 |
| `data[].error.logisticsAgentAuthId` | string | 是 | 授权id |
| `data[].error.logisticsAgentProductId` | string | 是 | 物流渠道id |
| `data[].error.logisticsAgentId` | string | 是 | 物流id |
| `data[].error.gentName` | string | 是 | 物流名称 |


&lt;details>&lt;summary>请求示例 示例 1&lt;/summary>

```json
{
  "opOrderPackageId": 43717
}
```
&lt;/details>

&lt;details>&lt;summary>请求示例 示例 2&lt;/summary>

```json
{
  "opOrderPackageId": 43717
}
```
&lt;/details>
