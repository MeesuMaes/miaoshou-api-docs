# 图片翻译


- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/common/translate/translate_image`
- 类型：处理(生成内容)
- 原文：[484286514e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286514e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array&lt;string> | 是 | 待翻译图片URL列表 |
| `sourceLang` | string | 是 | 源语言编码（如 zh、en），可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig |
| `targetLang` | string | 是 | 目标语言编码，可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig |
| `translatePlatform` | string | 是 | 翻译平台（ali / aeAi / tosoiot / ykt），可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig 的键 |
| `noTranslateImageTextOptions` | array&lt;string> | 否 | 不翻译的图片文字选项，可选值：textInTheProduct（不翻译产品文案）、brand（不翻译品牌），不传则都翻译 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.translateImageUrlResultList` | array&lt;object> | 否 | 翻译成功结果列表 |
| `data.translateImageUrlResultList[].oriImageUrl` | string | 否 | 原始图片URL |
| `data.translateImageUrlResultList[].newImageUrl` | string | 否 | 翻译后图片URL |
| `data.translateImageUrlResultList[].result` | string | 否 | 单张翻译结果（success/fail） |
| `data.translateImageUrlErrorResultList` | array&lt;object> | 否 | 翻译失败结果列表 |
| `data.translateImageUrlErrorResultList[].failImageCount` | integer | 否 | 失败图片数量 |
| `data.translateImageUrlErrorResultList[].failImageUrls` | array&lt;string> | 否 | 失败图片URL列表 |
| `data.translateImageUrlErrorResultList[].reason` | string | 否 | 失败原因 |
