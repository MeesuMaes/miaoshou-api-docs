# 获取退货退款列表


- 层级：开放平台 > 包裹 > 售后
- 方法+路径：`POST /open/v1/order/after_sales/fetch/order_return_list`
- 类型：读
- 原文：[477739260e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477739260e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `gmtStartFrom` | string | 否 | 售后/订单起始时间 |
| `gmtStartTo` | string | 否 | 售后/订单结束时间 |
| `platformReturnSns` | string | 否 | 平台售后单号 |
| `platformOrderSns` | string | 否 | 平台订单号 |
| `platform` | string | 否 | 平台 |
| `page` | integer | 否 | 页码 |
| `pageSize` | integer | 否 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.returnList` | array&lt;object> | 否 | 退货退款单列表 |
| `data.returnList[].opOrderReturnId` | string | 否 | 售后单ID |
| `data.returnList[].opOrderId` | string | 否 | 订单ID |
| `data.returnList[].platformReturnSn` | string | 否 | 平台售后单号 |
| `data.returnList[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.returnList[].shopId` | string | 否 | 店铺ID |
| `data.returnList[].shopName` | string | 否 | 店铺名称 |
| `data.returnList[].shopNickName` | string | 否 | 店铺自定义名称 |
| `data.returnList[].platform` | string | 否 | 平台 |
| `data.returnList[].site` | string | 否 | 站点 |
| `data.returnList[].siteName` | string | 否 | 站点名称 |
| `data.returnList[].status` | string | 否 | 售后状态 |
| `data.returnList[].platformReturnStatus` | string | 否 | 平台售后状态 |
| `data.returnList[].appReturnStatusText` | string | 否 | 妙手售后状态文案 |
| `data.returnList[].reverseType` | string | 否 | 售后类型 |
| `data.returnList[].textReason` | string | 否 | 售后/退货原因文案（原文） |
| `data.returnList[].textReasonCn` | string | 否 | 售后/退货原因文案（中文） |
| `data.returnList[].refundAmount` | string | 否 | 退款金额 |
| `data.returnList[].currency` | string | 否 | 币种 |
| `data.returnList[].returnTrackingNo` | string | 否 | 退回运单号 |
| `data.returnList[].returnLogisticsCompany` | string | 否 | 退货物流商 |
| `data.returnList[].needsLogistics` | string | 否 | 是否需要退回物流 |
| `data.returnList[].gmtCreateTime` | string | 否 | 售后时间 |
| `data.returnList[].gmtDueDate` | string | 否 | 最晚处理时间 |
| `data.returnList[].items` | array&lt;object> | 否 | 商品列表 |
| `data.returnList[].items[].title` | string | 否 | 商品标题 |
| `data.returnList[].items[].picUrl` | string | 否 | 商品图片URL |
| `data.returnList[].items[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.returnList[].items[].platformSkuId` | string | 否 | 平台SKUID |
| `data.returnList[].items[].quantity` | string | 否 | 数量 |
| `data.returnList[].consigneeInfo` | object | 否 | 退货人信息 |
| `data.returnList[].consigneeInfo.opOrderId` | string | 否 | 订单ID |
| `data.returnList[].consigneeInfo.name` | string | 否 | 收件人姓名 |
| `data.returnList[].consigneeInfo.katakana` | string | 否 | 收件人假名/日语假名 |
| `data.returnList[].consigneeInfo.phone` | string | 否 | 收件人主电话 |
| `data.returnList[].consigneeInfo.phone1` | string | 否 | 收件人备用电话1 |
| `data.returnList[].consigneeInfo.phone2` | string | 否 | 收件人备用电话2 |
| `data.returnList[].consigneeInfo.email` | string | 否 | 收件人邮箱 |
| `data.returnList[].consigneeInfo.company` | string | 否 | 公司名称 |
| `data.returnList[].consigneeInfo.country` | string | 否 | 国家二字码 |
| `data.returnList[].consigneeInfo.countryName` | string | 否 | 国家名称 |
| `data.returnList[].consigneeInfo.state` | string | 否 | 省/州 |
| `data.returnList[].consigneeInfo.city` | string | 否 | 城市 |
| `data.returnList[].consigneeInfo.district` | string | 否 | 区 |
| `data.returnList[].consigneeInfo.town` | string | 否 | 镇/街道 |
| `data.returnList[].consigneeInfo.houseNumber` | string | 否 | 门牌号 |
| `data.returnList[].consigneeInfo.zipcode` | string | 否 | 邮编 |
| `data.returnList[].consigneeInfo.address` | string | 否 | 简化地址 |
| `data.returnList[].consigneeInfo.address1` | string | 否 | 详细地址1 |
| `data.returnList[].consigneeInfo.address2` | string | 否 | 详细地址2 |
| `data.returnList[].consigneeInfo.address3` | string | 否 | 详细地址3 |
| `data.returnList[].consigneeInfo.fullAddress` | string | 否 | 完整地址 |
| `data.returnList[].consigneeInfo.customsClearanceCode` | string | 否 | 清关编码 |
| `data.total` | integer | 否 | 总数 |
| `data.page` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页数量 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "gmtStartFrom": "2025-04-27 14:49:20",
  "gmtStartTo": "2025-04-27 14:49:24",
  "platformReturnSns": "",
  "platform": "shopee",
  "platformOrderSns": "",
  "page": 1,
  "pageSize": 20
}
```
&lt;/details>
