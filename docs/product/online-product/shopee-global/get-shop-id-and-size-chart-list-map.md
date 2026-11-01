# 获取全球店铺类目尺寸模板列表


- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/get_shop_id_and_size_chart_list_map`
- 类型：读
- 原文：[480434405e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434405e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array&lt;integer> | 是 | 店铺ID列表 |
| `cid` | integer | 是 | 类目ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndSizeChartListMap` | object | 否 | 店铺ID与尺寸模板列表映射 |
