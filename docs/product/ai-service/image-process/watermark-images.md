# 图片打水印


- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/item/tiktok/watermark/watermark_images`
- 类型：处理(生成内容)
- 原文：[482200258e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482200258e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array&lt;string> | 是 | 需要打水印的图片链接列表 |
| `watermarkId` | string | 是 | 用于打水印的水印ID |
| `collectBoxDetailId` | integer | 否 | 采集箱详情ID 若有就传 |
| `isAutoMatchImageSize` | boolean | 是 | 是否自动匹配图片大小 若开启，添加水印时将自动适配原图尺寸比例；若关闭，添加水印后输出的图片尺寸默认为 800×800 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.watermarkDetail` | array&lt;object> | 否 | 打水印结果列表，每项对应一张图片的处理结果 |
| `data.watermarkDetail[].imageUrl` | string | 否 | 原图片URL |
| `data.watermarkDetail[].result` | string | 否 | 打水印结果（success: 成功；fail: 失败） |
| `data.watermarkDetail[].watermarkImageUrl` | string | 否 | 打完水印后的图片URL，result 为 success 时有值 |
| `data.watermarkDetail[].msg` | string | 否 | 失败原因，result 为 fail 时有值 |
