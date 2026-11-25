# 获取产品模板列表


- 层级：开放平台 > 商品 > SHEIN全托采集箱 > 产品模板
- 方法+路径：`POST /open/v1/product/collect_box/shein/item_template/search_item_template_list`
- 类型：读
- 原文：[537694051e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537694051e0.md)

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
| `data.itemTemplateList` | array&lt;object> | 否 | 模板列表 |
| `data.itemTemplateList[].itemTemplateId` | string | 否 | 模板ID |
| `data.itemTemplateList[].subAppAccountId` | integer | 否 | 子账号ID |
| `data.itemTemplateList[].platform` | string | 否 | 平台 |
| `data.itemTemplateList[].shopId` | string | 否 | 店铺ID |
| `data.itemTemplateList[].shopName` | string | 否 | 店铺名称 |
| `data.itemTemplateList[].shopIsInvalid` | boolean | 否 | 店铺是否失效 |
| `data.itemTemplateList[].name` | string | 否 | 模板名称 |
| `data.itemTemplateList[].cid` | string | 否 | 类目ID |
| `data.itemTemplateList[].sites` | array&lt;string> | 否 | 站点列表 |
| `data.itemTemplateList[].moduleNameList` | array&lt;string> | 否 | 模块列表 |
| `data.itemTemplateList[].registrationType` | string | 否 | 产品类型 |
| `data.itemTemplateList[].gmtCreate` | string | 否 | 创建时间 |
| `data.itemTemplateList[].gmtModified` | string | 否 | 更新时间 |
| `data.total` | integer | 否 | 总数 |
| `data.pageNo` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页条数 |
