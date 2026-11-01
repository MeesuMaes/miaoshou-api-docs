# 获取尺码表详情


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_size_charts_by_size_template_id`
- 类型：读
- 原文：[471545332e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545332e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `sizeTemplateId` | integer | 是 | 尺码表模板ID |
| `sizeTemplateSource` | string | 是 | 尺码表模板来源（api/erp 尺码表模板列表中有返回这个字段） |
| `refresh` | integer | 否 | 是否刷新 1是 0否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeTemplateId` | string | 否 | 尺码表模板ID，创建产品时sizeCharts中需传此ID |
| `data.sizeCharts` | object | 否 | 尺码表数据，创建产品时按此结构填写sizeCharts |
| `data.sizeCharts.elementIds` | array&lt;integer> | 否 | 启用的尺码参数ID列表，必须包含sizeSpecMeta.elementList中所有necessary=true的项 |
| `data.sizeCharts.sizeItems` | array&lt;object> | 否 | 尺码行数据，每行对应一个尺码（如S/M/L），sizeName必须与saleAttributes中的尺码值一致 |
| `data.sizeCharts.sizeItems[].sizeName` | string | 否 | 尺码名称，如"one-size"、"S"、"M"、"L"，必须与saleAttributes中尺码属性的某个值完全一致 |
| `data.sizeCharts.sizeItems[].elementValueList` | array&lt;object> | 否 | 元素值列表 |
| `data.sizeCharts.sizeItems[].elementValueList[].elementId` | integer | 否 | 元素ID |
| `data.sizeCharts.sizeItems[].elementValueList[].elementValue` | string | 否 | 元素值 |
| `data.sizeCharts.sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与尺码名称映射 |
| `data.sizeCharts.elementIdAndIsRangeMap` | object | 否 | 参数ID是否支持范围值（如"12-13"），key为elementId，value为true表示支持范围 |
| `data.groupId` | integer | 否 | 尺码分组ID |
| `data.sizeSpecMeta` | object | 否 | 尺码规格元数据，elementList中的necessary=true项必须在sizeCharts.elementIds中包含 |
| `data.sizeSpecMeta.groupList` | array&lt;object> | 否 | 尺码分组列表 |
| `data.sizeSpecMeta.groupList[].id` | integer | 否 | 分组ID |
| `data.sizeSpecMeta.groupList[].name` | string | 否 | 分组名称 |
| `data.sizeSpecMeta.groupList[].unnecessary` | boolean | 否 | 是否非必填 |
| `data.sizeSpecMeta.elementList` | array&lt;object> | 否 | 所有可用的尺码参数列表，创建产品时参考此列表确定要填哪些参数，necessary=true的项必须在sizeCharts.elementIds中包含 |
| `data.sizeSpecMeta.elementList[].necessary` | boolean | 否 | 是否必填，为true时该参数必须包含在sizeCharts.elementIds中 |
| `data.sizeSpecMeta.elementList[].name` | string | 否 | 参数名称，如"胸围全围"、"衣长" |
| `data.sizeSpecMeta.elementList[].id` | integer | 否 | 参数ID，对应sizeItems中elementValueList的elementId |
| `data.sizeSpecMeta.elementList[].unit` | string | 否 | 单位，如"cm" |
