# 获取包裹物流轨迹


- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking/get_tracking_list`
- 类型：读
- 原文：[477263048e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477263048e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 订单包裹ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.trackingInfoList` | array&lt;object> | 否 | 物流轨迹列表 |
| `data.trackingInfoList[].description` | string | 否 | 物流轨迹明细 |
| `data.trackingInfoList[].descriptionCn` | string | 否 | 物流轨迹明细（中文） |
| `data.trackingInfoList[].gmtCreate` | string | 否 | 时间 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "opOrderPackageId": 1567020375
}
```
&lt;/details>
