# 获取尺码表所需填写属性信息


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_need_attribute_info`
- 类型：读
- 原文：[482753637e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753637e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `domainId` | string | 是 | domain ID(对应getSizeChartDomainList返回的domainId) |
| `genderId` | string | 是 | 1.类目属性中的性别ID(getSiteCollectItemInfo中attributes->GENDER属性values中的name值； 2.在获取类目属性规则接口返回数据的productAttributeRules中对应GENDER属性规则values值的id |
| `measureType` | string | 是 | 测量类型(对应getSizeChartAttributeInfo返回的measureTypeList key) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeChartIdAndInfoMap` | object | 否 | 尺码ID和尺码内容映射 |
| `data.equivalencies` | array&lt;string> | 否 | 尺码列表(XL,XXL等) |
