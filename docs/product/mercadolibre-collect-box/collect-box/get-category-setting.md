# 获取类目配置


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_setting`
- 类型：读
- 原文：[482753633e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753633e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.catalogDomain` | string | 否 | 类目domain |
| `data.maxDescriptionLength` | integer | 否 | 类目最大描述长度 |
| `data.maxTitleLength` | integer | 否 | 类目最大标题长度 |
