# 获取尺码表domain列表


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_domain_list`
- 类型：读
- 原文：[482753635e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753635e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 否 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.domains` | array&lt;object> | 否 | domain列表 |
| `data.domains[].domainId` | string | 否 | domain ID |
| `data.domains[].domainName` | string | 否 | domain英文名称 |
| `data.domains[].domainZhName` | string | 否 | domain中文名称 |
