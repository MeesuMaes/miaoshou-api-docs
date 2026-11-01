# 获取定价模板列表


- 层级：开放平台 > 商品 > TK采集箱 > 定价模板
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/price_template/get_price_template_list`
- 类型：读
- 原文：[482189164e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189164e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 否 | 模板名称（模糊搜索） |
| `site` | string | 否 | 站点 |
| `siteType` | string | 否 | 站点类型：cross_border 跨境 / mainland 本土 |
| `pageNo` | integer | 是 | 页码 |
| `pageSize` | integer | 是 | 每页条数 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.priceTemplateList` | array&lt;object> | 否 | 定价模板列表 |
| `data.priceTemplateList[].priceTemplateId` | integer | 否 | 定价模板 ID |
| `data.priceTemplateList[].appAccountId` | integer | 否 | 主账号 ID |
| `data.priceTemplateList[].subAppAccountId` | integer | 否 | 子账号 ID |
| `data.priceTemplateList[].platform` | string | 否 | 平台标识，如 tiktok |
| `data.priceTemplateList[].site` | string | 否 | 站点，如 MY / PH / US |
| `data.priceTemplateList[].name` | string | 否 | 模板名称 |
| `data.priceTemplateList[].remark` | string | 否 | 备注 |
| `data.priceTemplateList[].currency` | string | 否 | 站点币种，如 MYR / PHP / USD |
| `data.priceTemplateList[].displayWeightUnit` | string | 否 | 重量单位显示类型：kilogram / gram |
| `data.priceTemplateList[].profitType` | string | 否 | 利润计算类型：percent 百分比 / fixed 固定金额 |
| `data.priceTemplateList[].profitPercent` | number | 否 | 利润百分比（profitType=percent 时生效） |
| `data.priceTemplateList[].fixedProfitAmount` | number | 否 | 固定利润金额（profitType=fixed 时生效） |
| `data.priceTemplateList[].exchangeRate` | number | 否 | 汇率（人民币兑站点币种） |
| `data.priceTemplateList[].discount` | number | 否 | 折扣率（0~1，如 0.9 表示九折） |
| `data.priceTemplateList[].priceTailComputeType` | string | 否 | 价格尾数处理类型：process_decimal / fixed_tail |
| `data.priceTemplateList[].priceTail` | string | 否 | 价格尾数值（priceTailComputeType=fixed_tail 时生效） |
| `data.priceTemplateList[].priceProcessDecimalType` | string | 否 | 小数处理类型：floor 向下 / ceil 向上 / round 四舍五入 |
| `data.priceTemplateList[].logisticsComputeType` | string | 否 | 国际物流计算类型：fixed / first_continued / weight_interval / official_freight_tpl |
| `data.priceTemplateList[].weightRefType` | string | 否 | 重量参考类型：weight / volume_weight / max_weight |
| `data.priceTemplateList[].firstWeightCharge` | number | 否 | 首重费用（国际物流 first_continued 类型时生效） |
| `data.priceTemplateList[].firstWeightInterval` | number | 否 | 首重区间（g 或 kg，取决于 displayWeightUnit） |
| `data.priceTemplateList[].continuedWeightCharge` | number | 否 | 续重费用（国际物流 first_continued 类型时生效） |
| `data.priceTemplateList[].continuedWeightInterval` | number | 否 | 续重区间（g 或 kg，取决于 displayWeightUnit） |
| `data.priceTemplateList[].logisticsCharge` | number | 否 | 固定物流费用（国际物流 fixed 类型时生效） |
| `data.priceTemplateList[].platformChargePercent` | number | 否 | 平台费率（百分比，如 2.12 表示 2.12%） |
| `data.priceTemplateList[].paymentChargePercent` | number | 否 | 支付手续费率 |
| `data.priceTemplateList[].activityChargePercent` | number | 否 | 活动费率 |
| `data.priceTemplateList[].withdrawChargePercent` | number | 否 | 提现手续费率 |
| `data.priceTemplateList[].otherCharge` | number | 否 | 其他杂费（站点币种） |
| `data.priceTemplateList[].isCalLightCargo` | integer | 否 | 是否计算抛货（轻货）：1 是 / 0 否 |
| `data.priceTemplateList[].lightCargoCoefficient` | integer | 否 | 抛货体积重系数（isCalLightCargo=1 时生效，单位：cm³/g） |
| `data.priceTemplateList[].weightLogisticsChargeList` | string | 否 | 分段重量物流费用列表（logisticsComputeType=weight_interval 时生效） 格式：[['minWeight'=>0, 'maxWeight'=>1000, 'charge'=>5.00], ...] |
| `data.priceTemplateList[].domesticLogisticsComputeType` | string | 否 | 国内物流计算类型：fixed / first_continued |
| `data.priceTemplateList[].domesticLogisticsFirstWeightCharge` | number | 否 | 国内物流首重费用 |
| `data.priceTemplateList[].domesticLogisticsFirstWeightInterval` | number | 否 | 国内物流首重区间 |
| `data.priceTemplateList[].domesticLogisticsContinuedWeightCharge` | number | 否 | 国内物流续重费用 |
| `data.priceTemplateList[].domesticLogisticsContinuedWeightInterval` | number | 否 | 国内物流续重区间 |
| `data.priceTemplateList[].domesticLogisticsCharge` | number | 否 | 国内物流固定费用（domesticLogisticsComputeType=fixed 时生效） |
| `data.priceTemplateList[].buyerLogisticCharge` | number | 否 | 买家承担物流费用 |
| `data.priceTemplateList[].sellerLogisticCharge` | number | 否 | 卖家承担物流费用 |
| `data.priceTemplateList[].hasSellerLogisticCharge` | integer | 否 | 是否存在卖家承担运费：1 是 / 0 否 |
| `data.priceTemplateList[].officialTplMode` | string | 否 | 官方运费模板模式（logisticsComputeType=official_freight_tpl 时生效） |
| `data.priceTemplateList[].officialTplLogisticsChannel` | string | 否 | 官方运费模板物流渠道 |
| `data.priceTemplateList[].snapshotId` | integer | 否 | 快照 ID（用于追溯模板历史版本） |
| `data.priceTemplateList[].gmtCreate` | string | 否 | 创建时间 |
| `data.priceTemplateList[].gmtModified` | string | 否 | 最后修改时间 |
| `data.total` | integer | 否 | 总数 |
| `data.pageNo` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页条数 |
