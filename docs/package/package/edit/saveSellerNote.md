# 保存包裹商家备注


- 层级：开放平台 > 包裹 > 包裹 > 基础信息修改
- 方法+路径：`POST /open/v1/order/package/base_info_modify/saveSellerNote`
- 类型：写
- 原文：[457240926e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457240926e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderIds` | array&lt;string> | 是 | 订单id |
| `sellerNote` | string | 是 | 备注内容 |
| `isCoverOriginalSellerNote` | integer | 是 | 1 是 0 否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array&lt;object> | 是 |  |
| `data[].sellerNoteMap` | array&lt;string> | 是 | orderId -note 的map |
| `data[].successCount` | string | 是 |  |
| `data[].failCount` | string | 是 |  |
| `data[].failResultMap` | object | 是 | orderId -note 的map |
