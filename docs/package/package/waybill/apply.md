# 申请运单号


- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking_no/apply`
- 类型：写
- 原文：[457255661e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457255661e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array&lt;object> | 是 |  |
| `data[].platformPackageNo` | string | 是 | 物流商单号 |
| `data[].headLogisticsNo` | string | 是 | 头程物流商跟踪号 |
| `data[].logisticsNo` | string | 是 | 物流商跟踪号 |
| `data[].logisticsType` | string | 是 | 物流类型 |
| `data[].headLogisticsNoCompany` | string | 是 | 头程物流商公司 |
