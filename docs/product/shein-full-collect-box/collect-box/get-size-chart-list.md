# 获取尺码表模板列表


- 层级：开放平台 > 商品 > SHEIN全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein/collect_box/get_size_chart_list`
- 类型：读
- 原文：[537694046e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537694046e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 页码，不传默认1 |
| `pageSize` | integer | 否 | 每页条数，不传默认20 |
| `site` | string | 是 | 站点 |
| `name` | string | 否 | 尺码表名称 |
| `cid` | string | 否 | 类目ID |
| `saleAttributeId` | integer | 否 | 销售属性ID |
| `saleAttributeIds` | array&lt;integer> | 否 | 销售属性ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeChartList` | array&lt;object> | 否 | 尺码表列表 |
| `data.sizeChartList[].sheinSizeChartTemplateId` | string | 否 | shein 尺码表模板ID |
| `data.sizeChartList[].sheinChoiceSizeChartTemplateId` | string | 否 | shein choice 尺码表模板ID |
| `data.sizeChartList[].appAccountId` | string | 否 | 主账号ID |
| `data.sizeChartList[].subAppAccountId` | integer | 否 | 子账号ID |
| `data.sizeChartList[].name` | string | 否 | 模板名称 |
| `data.sizeChartList[].site` | string | 否 | 站点 |
| `data.sizeChartList[].cid` | string | 否 | 类目ID |
| `data.sizeChartList[].saleAttributeId` | string | 否 | 销售属性ID |
| `data.sizeChartList[].saleAttributeName` | string | 否 | 销售属性名称 |
| `data.sizeChartList[].sizeChart` | array&lt;object> | 否 | 尺码表内容 |
| `data.sizeChartList[].breadcrumb` | string | 否 | 类目面包屑 |
| `data.sizeChartList[].gmtCreate` | string | 否 | 创建时间 |
| `data.sizeChartList[].gmtModified` | string | 否 | 更新时间 |
| `data.total` | integer | 否 | 总条数 |
| `data.pageNo` | integer | 否 | 页码 |
| `data.pageSize` | integer | 否 | 每页条数 |
