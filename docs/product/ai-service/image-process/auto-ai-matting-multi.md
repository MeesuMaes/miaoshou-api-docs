# AI白底图


- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/picture/matting/auto_ai_matting_multi`
- 类型：处理(生成内容)
- 原文：[482201652e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482201652e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imgUrls` | array&lt;string> | 是 | 图片URL列表，（不计重复） |
| `imageScene` | integer | 是 | 图片应用场景 1-产品图片 2-描述图片 3-sku或产品属性图片 4-证书图片 5-尺寸图图片 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.imgMattingList` | array&lt;object> | 否 | AI白底图结果列表 |
| `data.imgMattingList[].result` | string | 否 | 单张AI白底图结果（success/fail） |
| `data.imgMattingList[].width` | integer | 否 | 图片宽度 |
| `data.imgMattingList[].height` | integer | 否 | 图片高度 |
| `data.imgMattingList[].md5` | string | 否 | 图片MD5 |
| `data.imgMattingList[].newImageUrl` | string | 否 | 抠图后图片URL |
| `data.imgMattingList[].oriImageUrl` | string | 否 | 原始图片URL |
