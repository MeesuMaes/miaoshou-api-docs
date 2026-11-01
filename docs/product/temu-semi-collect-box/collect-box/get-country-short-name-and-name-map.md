# 获取原产地国家列表


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_country_short_name_and_name_map`
- 类型：读
- 原文：[477347608e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347608e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.countryShortNameAndNameMap` | object | 否 | 国家简码→中文名映射，key 为 shortName（如 CN），value 为中文名（如 中国大陆）。 可用于将已保存的 productOriginCountry 短码转换为可读名称展示 |
| `data.productOriginCountries` | array&lt;object> | 否 | 完整国家列表，用于渲染原产地下拉选择器。 选择某个国家后将其 shortName 填入 productOriginCountry； 选择中国（shortName=CN）时，还需从 province 列表中选择省份，将省份 code 填入 productOriginProvince |
| `data.productOriginCountries[].code` | string | 否 | 国家编码（如 43） |
| `data.productOriginCountries[].name` | string | 否 | 英文名 |
| `data.productOriginCountries[].shortName` | string | 否 | 国家简码，填入 productOriginCountry（如 CN、US） |
| `data.productOriginCountries[].chineseName` | string | 否 | 中文名 |
| `data.productOriginCountries[].province` | array&lt;object> | 否 | 省份列表，仅原产国为 CN 时有值。 选择中国后需从此列表选择省份，将省份 code 填入 productOriginProvince |
| `data.productOriginCountries[].province[].code` | string | 否 | 省份编码，原产国为 CN 时填入 productOriginProvince |
| `data.productOriginCountries[].province[].name` | string | 否 | 英文名 |
| `data.productOriginCountries[].province[].chineseName` | string | 否 | 中文名 |
