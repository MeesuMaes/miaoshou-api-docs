# 获取定价模板列表


- 层级：开放平台 > 商品 > SHEIN全托采集箱 > 定价模板
- 方法+路径：`POST /open/v1/product/collect_box/shein/price_template/get_price_template_list`
- 类型：读
- 原文：[537694055e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537694055e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 否 | 模板名称 |
| `site` | string | 否 | 站点 |
| `pageNo` | integer | 否 | 页码，不传默认1 |
| `pageSize` | integer | 否 | 每页条数，不传默认20 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.priceTemplateList` | array&lt;object> | 否 | 定价模板列表 |
| `data.priceTemplateList[].priceTemplateId` | integer | 否 | 定价模板ID |
| `data.priceTemplateList[].subAppAccountId` | integer | 否 | 子账号ID |
| `data.priceTemplateList[].ownerSubAccountAliasName` | string | 否 | 子账号别名 |
| `data.priceTemplateList[].platform` | string | 否 | 平台 |
| `data.priceTemplateList[].site` | string | 否 | 站点 |
| `data.priceTemplateList[].name` | string | 否 | 模板名称 |
| `data.priceTemplateList[].remark` | string | 否 | 备注 |
| `data.priceTemplateList[].currency` | string | 否 | 币种 |
| `data.priceTemplateList[].snapshotId` | integer | 否 | 快照ID |
| `data.priceTemplateList[].gmtCreate` | string | 否 | 创建时间 |
| `data.priceTemplateList[].gmtModified` | string | 否 | 更新时间 |
| `data.total` | integer | 否 | 总数 |
| `data.pageNo` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页条数 |
