# 查询尺码表模板列表


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/search_size_chart_template`
- 类型：读
- 原文：[482753641e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753641e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array&lt;integer> | 是 | 店铺ID列表 |
| `filter` | object | 否 |  |
| `filter.domainId` | string | 否 | 尺码表domain ID(对应getSizeChartDomainList返回的domainId) |
| `filter.genderId` | string | 否 | 类目属性中的性别ID |
| `filter.templateName` | string | 否 | 模板名称（模糊搜索） |
| `pageSize` | integer | 否 | 每页数量 |
| `pageNo` | integer | 否 | 当前页码 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeChartTemplateList` | array&lt;object> | 否 | 尺码表列表 |
| `data.sizeChartTemplateList[].attributes` | array&lt;object> | 否 | 尺码表模板属性列表 |
| `data.sizeChartTemplateList[].attributes[].id` | string | 否 | 属性ID |
| `data.sizeChartTemplateList[].attributes[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.sizeChartTemplateList[].attributes[].values[].id` | string | 否 | 属性值ID |
| `data.sizeChartTemplateList[].attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.sizeChartTemplateList[].chartId` | string | 否 | 平台尺码表ID |
| `data.sizeChartTemplateList[].copySerialNumber` | integer | 否 | 复制模板序列号 |
| `data.sizeChartTemplateList[].domainId` | string | 否 | 尺码表domainId |
| `data.sizeChartTemplateList[].genderId` | string | 否 | 性别ID |
| `data.sizeChartTemplateList[].mainAttributeId` | string | 否 | 主属性ID |
| `data.sizeChartTemplateList[].mainAttribute` | array&lt;object> | 否 | 主属性映射 |
| `data.sizeChartTemplateList[].mainAttribute[].attributes` | array&lt;object> | 否 | 表头英文名称 |
| `data.sizeChartTemplateList[].mainAttribute[].attributes[].siteId` | string | 否 | 站点ID |
| `data.sizeChartTemplateList[].mainAttribute[].attributes[].id` | string | 否 | 主属性属性ID |
| `data.sizeChartTemplateList[].measureType` | string | 否 | 测量类型 |
| `data.sizeChartTemplateList[].names` | object | 否 | 站点ID对应名称映射,格式\{MCO:"renzituo"\} |
| `data.sizeChartTemplateList[].rows` | array&lt;object> | 否 |  |
| `data.sizeChartTemplateList[].rows[].attributes` | array&lt;object> | 否 | 表头英文名称 |
| `data.sizeChartTemplateList[].rows[].attributes[].id` | string | 否 | 行属性ID |
| `data.sizeChartTemplateList[].rows[].attributes[].values` | array&lt;object> | 否 | 行属性值列表 |
| `data.sizeChartTemplateList[].rows[].id` | string | 否 | 行ID |
| `data.sizeChartTemplateList[].rows[].sites` | array&lt;string> | 否 | 站点ID列表 |
| `data.sizeChartTemplateList[].shopId` | integer | 否 | 店铺ID |
| `data.sizeChartTemplateList[].siteId` | string | 否 | 站点ID |
| `data.sizeChartTemplateList[].templateName` | string | 否 | 尺码模板名称 |
| `data.sizeChartTemplateList[].type` | string | 否 | 尺码模板类型 |
| `data.total` | integer | 否 | 总数 |
