# 获取授权站点和名称映射


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_auth_site_and_site_name_map`
- 类型：读
- 原文：[482753639e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753639e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 否 | 店铺ID |
| `includeCbt` | integer | 是 | 是否包含CBT全球站点（1是 0否） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.siteAndSiteNameMap` | object | 否 | 站点和站点名称映射，格式:\{"AR":"阿根廷","BR":"巴西"\} |
