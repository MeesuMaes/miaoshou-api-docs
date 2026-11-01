# 获取品牌列表


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_brand_list`
- 类型：读
- 原文：[497001483e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/497001483e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `brandName` | string | 否 | 品牌名搜索关键字 |
| `nextPageToken` | string | 否 | 获取下一页数据的Token |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.brandList` | array&lt;object> | 否 | 品牌列表 |
| `data.brandList[].authorizedStatus` | string | 否 | 该品牌的授权状态（只有授权通过的品牌才会在前台展示）授权通过-AUTHORIZED，授权未通过-UNAUTHORIEZD |
| `data.brandList[].brandId` | string | 否 | 品牌ID |
| `data.brandList[].brandName` | string | 否 | 品牌名称 |
| `data.nextPageToken` | string | 否 | 获取下一页数据的Token |
| `data.totalCount` | integer | 否 | 品牌总数 |
