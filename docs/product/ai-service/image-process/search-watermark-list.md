# 搜索水印列表


- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/item/tiktok/watermark/search_watermark_list`
- 类型：读
- 原文：[482200257e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482200257e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `watermarkIds` | string | 否 | 水印ID列表，多个以英文逗号分隔 |
| `watermarkName` | string | 否 | 水印名称（支持模糊搜索） |
| `watermarkSubType` | string | 是 | 水印子类型（normal=普通水印，byLayer=描述图水印） |
| `pageNo` | integer | 是 | $pageNo |
| `pageSize` | integer | 是 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.watermarkList` | array&lt;object> | 否 | 水印列表 |
| `data.watermarkList[].watermarkId` | string | 否 | 水印ID |
| `data.watermarkList[].appAccountId` | string | 否 | 应用账号ID |
| `data.watermarkList[].platform` | string | 否 | 平台 |
| `data.watermarkList[].watermarkImageUrl` | string | 否 | 水印图片URL |
| `data.watermarkList[].watermarkType` | string | 否 | 水印类型 |
| `data.watermarkList[].watermarkSubType` | string | 否 | 水印子类型 |
| `data.watermarkList[].name` | string | 否 | 水印名称 |
| `data.total` | integer | 否 | 总数 |
