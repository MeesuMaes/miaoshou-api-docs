# 保存采集箱产品源数据信息


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/save_edit_item`
- 类型：写
- 原文：[516157442e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157442e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | string | 是 | 采集箱ID |
| `itemDetail` | object | 是 | 采集箱详情数据 |
| `itemDetail.title` | string | 是 | 标题 |
| `itemDetail.notes` | string | 是 | 简易描述 |
| `itemDetail.richTextDesc` | string | 否 | 图文描述 |
| `itemDetail.colorPropName` | string | 否 | 颜色属性名称（规格1属性名称） |
| `itemDetail.sizePropName` | string | 否 | 尺码属性名称(规格2属性名称) |
| `itemDetail.skuMap` | object | 否 | SKU映射 (多规格产品必填 |
| `itemDetail.colorMap` | object | 否 | 颜色映射 (多规格产品必填) |
| `itemDetail.sizeMap` | object | 否 | 尺寸映射 (多规格产品必填 |
| `itemDetail.imagePaths` | array&lt;string> | 否 | 图片路径列表 |
| `itemDetail.sourceAttrs` | array&lt;object> | 否 | 来源属性列表 |
| `itemDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `itemDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `itemDetail.brandName` | string | 否 | 品牌名称 |
| `itemDetail.itemNum` | string | 否 | 商品编码 |
| `itemDetail.width` | string | 否 | 宽度 |
| `itemDetail.length` | string | 否 | 长度 |
| `itemDetail.height` | string | 否 | 高度 |
| `itemDetail.weight` | number | 是 | 重量（kg） |
| `itemDetail.videoInfo` | object | 否 | 视频信息 |
| `itemDetail.videoInfo.videoUrl` | string | 否 | 视频url |
| `itemDetail.videoInfo.coverUrl` | string | 否 | 封面视频url |
| `itemDetail.appAccountId` | string | 否 | 应用账户ID |
| `itemDetail.subAppAccountId` | string | 否 | 子应用账户ID |
| `itemDetail.sourceItemId` | string | 否 | 来源商品ID |
| `itemDetail.source` | string | 否 | 来源 |
| `itemDetail.site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `itemDetail.price` | number | 否 | 价格 (单规格产品时必填) |
| `itemDetail.stock` | integer | 否 | 库存 (单规格产品时必填) |
| `itemDetail.packageLength` | string | 否 | 包裹长度 |
| `itemDetail.packageWidth` | string | 否 | 包裹宽度 |
| `itemDetail.packageHeight` | string | 否 | 包裹高度 |
| `itemDetail.imgUrls` | array&lt;string> | 是 | 图片URL列表 |
| `itemDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `itemDetail.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `itemDetail.isPreOrder` | integer | 是 | 是否预售 (0,1) |
| `itemDetail.daysToShip` | integer | 否 | 预购天数（当isPreOrder=1时必填） |
| `itemDetail.preOrderType` | string | 否 | 是否按SKU配置出货天数，枚举值：spu/sku |
| `ossMd5` | string | 是 | OSS标识 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 |  |
