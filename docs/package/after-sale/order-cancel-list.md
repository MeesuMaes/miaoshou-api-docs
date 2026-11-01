# 获取取消订单列表


- 层级：开放平台 > 包裹 > 售后
- 方法+路径：`POST /open/v1/order/after_sales/fetch/order_cancel_list`
- 类型：读
- 原文：[477739261e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477739261e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platformOrderSns` | string | 否 | 平台订单号 |
| `platform` | string | 否 | 平台 |
| `gmtStartFrom` | string | 否 | 售后起始时间 |
| `gmtStartTo` | string | 否 | 售后结束时间 |
| `page` | integer | 否 | 页码 |
| `pageSize` | integer | 否 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cancelList` | array&lt;object> | 否 | 取消订单列表 |
| `data.cancelList[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.cancelList[].shopId` | string | 否 | 店铺ID |
| `data.cancelList[].shopName` | string | 否 | 店铺名称 |
| `data.cancelList[].platform` | string | 否 | 平台 |
| `data.cancelList[].platformName` | string | 否 | 平台名称 |
| `data.cancelList[].site` | string | 否 | 站点 |
| `data.cancelList[].siteName` | string | 否 | 站点名称 |
| `data.cancelList[].textReason` | string | 否 | 取消原因（原文） |
| `data.cancelList[].textReasonCn` | string | 否 | 取消原因（中文） |
| `data.cancelList[].appReturnStatusText` | string | 否 | 妙手取消状态文案 |
| `data.cancelList[].appOrderStatus` | string | 否 | 订单状态 |
| `data.cancelList[].reverseTypeText` | string | 否 | 售后类型文案 |
| `data.cancelList[].gmtCreateTime` | string | 否 | 售后时间 |
| `data.cancelList[].items` | array&lt;object> | 否 | 商品列表 |
| `data.cancelList[].items[].title` | string | 否 | 商品标题 |
| `data.cancelList[].items[].picUrl` | string | 否 | 商品图片URL |
| `data.cancelList[].items[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.cancelList[].items[].platformSkuId` | string | 否 | 平台SKUID |
| `data.cancelList[].items[].quantity` | string | 否 | 数量 |
| `data.total` | integer | 否 | 总数 |
| `data.page` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页数量 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "platformOrderSns": "",
  "platform": "tiktok",
  "gmtStartFrom": "2026-06-24 16:58:32",
  "gmtStartTo": "2026-06-24 16:58:35",
  "page": 1,
  "pageSize": 20
}
```
&lt;/details>
