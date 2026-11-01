# 获取尺码表表头和主属性信息


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_attribute_info`
- 类型：读
- 原文：[482753636e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753636e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `domainId` | string | 是 | 尺码表domain ID(对应getSizeChartDomainList返回的domainId) |
| `genderId` | string | 是 | 1.类目属性中的性别ID(getSiteCollectItemInfo中attributes->GENDER属性values中的name值； 2.在获取类目属性规则接口返回数据的productAttributeRules中对应GENDER属性规则values值的id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.mainAttributeList` | object | 否 | 主属性列表，格式\{MANUFACTURER_SIZE:\{name:"Manufacturer size",nameZh:"自定义尺码",unit:"US"\}\} |
| `data.measureTypeList` | object | 否 | 测量属性列表，格式\{BODY_MEASURE:\{name:"With body measurements",nameZh:"身体尺寸",relevanceRequired:["FILTRABLE_SIZE","CHEST_CIRCUMFERENCE_FROM"],unit:"US"\}\} |
| `data.isTopsAndBottoms` | boolean | 否 | 是否为上衣或下装 |
