# 获取定价模板详情


- 层级：开放平台 > 商品 > SHEIN半托采集箱 > 定价模板
- 方法+路径：`POST /open/v1/product/collect_box/shein_choice/price_template/get_price_template`
- 类型：读
- 原文：[537697884e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537697884e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `priceTemplateId` | integer | 是 | 定价模板ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.priceTemplateData` | object | 否 | 定价模板详情 |
| `data.priceTemplateData.priceTemplateId` | integer | 否 | 定价模板ID |
| `data.priceTemplateData.appAccountId` | integer | 否 | 主账号ID |
| `data.priceTemplateData.subAppAccountId` | integer | 否 | 子账号ID |
| `data.priceTemplateData.platform` | string | 否 | 平台 |
| `data.priceTemplateData.site` | string | 否 | 站点 |
| `data.priceTemplateData.name` | string | 否 | 模板名称 |
| `data.priceTemplateData.remark` | string | 否 | 备注 |
| `data.priceTemplateData.profitType` | string | 否 | 利润方式 |
| `data.priceTemplateData.currency` | string | 否 | 币种 |
| `data.priceTemplateData.displayWeightUnit` | string | 否 | 重量单位 |
| `data.priceTemplateData.logisticsComputeType` | string | 否 | 运费计算方式 |
| `data.priceTemplateData.firstWeightCharge` | number | 否 | 首重价格 |
| `data.priceTemplateData.firstWeightInterval` | number | 否 | 首重 |
| `data.priceTemplateData.continuedWeightCharge` | number | 否 | 续重价格 |
| `data.priceTemplateData.continuedWeightInterval` | number | 否 | 续重 |
| `data.priceTemplateData.weightRefType` | string | 否 | 重量参考类型 |
| `data.priceTemplateData.weightLogisticsChargeList` | array&lt;object> | 否 | 重量运费阶梯 |
| `data.priceTemplateData.weightLogisticsChargeList[].minWeight` | number | 否 | 最小重量 |
| `data.priceTemplateData.weightLogisticsChargeList[].maxWeight` | number | 否 | 最大重量 |
| `data.priceTemplateData.weightLogisticsChargeList[].charge` | number | 否 | 区间运费 |
| `data.priceTemplateData.weightLogisticsChargeList[].continuedWeightCharge` | number | 否 | 续重价格 |
| `data.priceTemplateData.weightLogisticsChargeList[].continuedWeightInterval` | number | 否 | 续重区间 |
| `data.priceTemplateData.logisticsCharge` | number | 否 | 固定运费 |
| `data.priceTemplateData.platformChargePercent` | number | 否 | 平台手续费率 |
| `data.priceTemplateData.paymentChargePercent` | number | 否 | 支付手续费率 |
| `data.priceTemplateData.withdrawChargePercent` | number | 否 | 提现手续费率 |
| `data.priceTemplateData.tariffChargePercent` | number | 否 | 关税费率 |
| `data.priceTemplateData.otherCharge` | number | 否 | 其他费用 |
| `data.priceTemplateData.profitPercent` | number | 否 | 利润率 |
| `data.priceTemplateData.fixedProfitAmount` | number | 否 | 固定利润金额 |
| `data.priceTemplateData.exchangeRate` | number | 否 | 汇率 |
| `data.priceTemplateData.discount` | number | 否 | 折扣 |
| `data.priceTemplateData.priceTailComputeType` | string | 否 | 尾数计算方式 |
| `data.priceTemplateData.priceTail` | string | 否 | 尾数金额 |
| `data.priceTemplateData.priceProcessDecimalType` | string | 否 | 小数处理方式 |
| `data.priceTemplateData.officialTplMode` | string | 否 | 官方模板模式 |
| `data.priceTemplateData.officialTplLogisticsChannel` | string | 否 | 官方物流渠道 |
| `data.priceTemplateData.snapshotId` | integer | 否 | 快照ID |
| `data.priceTemplateData.gmtCreate` | string | 否 | 创建时间 |
| `data.priceTemplateData.gmtModified` | string | 否 | 更新时间 |
