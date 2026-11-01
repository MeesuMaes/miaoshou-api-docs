# AI匹配类目


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/ai_match_cid_by_shop_ids`
- 类型：处理(生成内容)
- 原文：[482189162e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189162e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | integer | 是 | 采集箱详情ID |
| `shopIds` | array&lt;integer> | 是 | 店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndCidMap` | object | 否 | 店铺与匹配CID的映射 示例：\{ 100001 : 11231, 100002 : 12345 \} |
| `data.failedShopIds` | array&lt;integer> | 否 | 匹配失败的店铺ID列表，失败就代表没有这个店铺没有匹配上类目 |
