# 获取商品基本选项


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_item_options`
- 类型：读
- 原文：[482753640e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753640e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.weightUnitOptions` | array&lt;object> | 否 | 重量单位选项，key/value 数组，保存到 siteCollectItemInfo.skuMap.weightUnit |
| `data.weightUnitOptions[].key` | string | 否 | 选项键值 |
| `data.weightUnitOptions[].value` | string | 否 | 选项显示文本 |
| `data.warrantyTypeOptions` | array&lt;object> | 否 | 保修类型选项，key/value 数组，保存到 siteCollectItemInfo.warrantyType,siteCollectItemInfo.warrantyTimeUnit |
| `data.warrantyTypeOptions[].key` | string | 否 | 选项键值 |
| `data.warrantyTypeOptions[].value` | string | 否 | 选项显示文本 |
| `data.warrantyTimeUnitOptions` | array&lt;object> | 否 | 保修时间单位选项，key/value 数组，保存到 siteCollectItemInfo.warrantyTimeUnit |
| `data.warrantyTimeUnitOptions[].key` | string | 否 | 选项键值 |
| `data.warrantyTimeUnitOptions[].value` | string | 否 | 选项显示文本 |
| `data.lengthUnitOptions` | array&lt;object> | 否 | 包裹尺寸单位选项，key/value 数组，保存到 siteCollectItemInfo.skuMap.lengthWidthHeightUnit |
| `data.lengthUnitOptions[].key` | string | 否 | 选项键值 |
| `data.lengthUnitOptions[].value` | string | 否 | 选项显示文本 |
| `data.siteAndSupportListingTypeOptions` | object | 否 | 站点和支持产品类型映射,格式:\{"BR":[\{"label":"经典（Classic）","value":"gold_special"\}]\} |
