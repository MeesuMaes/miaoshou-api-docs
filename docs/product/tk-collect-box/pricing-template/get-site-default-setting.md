# 获取各个站点的默认配置


- 层级：开放平台 > 商品 > TK采集箱 > 定价模板
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/price_template/get_site_default_setting`
- 类型：读
- 原文：[482189165e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189165e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.siteAndBuyerLogisticDefaultChargeMap` | object | 否 | 站点买家物流默认运费（站点币种） |
| `data.siteAndBuyerLogisticDefaultChargeCNYMap` | object | 否 | 站点买家物流默认运费（人民币） |
| `data.siteAndDefaultPlatformInfrastructureChargeMap` | object | 否 | 站点默认平台基础设施费（站点币种） |
| `data.siteAndDefaultPlatformInfrastructureChargeCNYMap` | object | 否 | 站点默认平台基础设施费（人民币） |
| `data.tiktokCbSiteAndDefaultChargePercentMap` | object | 否 | 跨境站点默认费率 key=站点代码，value=各项费率明细 |
| `data.tiktokLocalDefaultChargePercentMap` | object | 否 | 本土站点默认费率 |
| `data.siteAndDefaultPlatformSupportChargeMap` | object | 否 | 站点默认平台支持费（站点币种） |
| `data.siteAndDefaultPlatformSupportChargeCNYMap` | object | 否 | 站点默认平台支持费（人民币） |
