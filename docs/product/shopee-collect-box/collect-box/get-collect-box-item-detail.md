# 获取采集箱产品的源数据


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_collect_box_item_detail`
- 类型：读
- 原文：[516157441e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157441e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemDetail` | object | 否 | 采集箱详情数据 |
| `data.itemDetail.title` | string | 是 | 标题 |
| `data.itemDetail.notes` | string | 是 | 简易描述 |
| `data.itemDetail.richTextDesc` | string | 否 | 图文描述 |
| `data.itemDetail.colorPropName` | string | 否 | 颜色属性名称（规格1属性名称） |
| `data.itemDetail.sizePropName` | string | 否 | 尺码属性名称(规格2属性名称) |
| `data.itemDetail.skuMap` | object | 否 | SKU映射 (多规格产品必填 |
| `data.itemDetail.colorMap` | object | 否 | 颜色映射 (多规格产品必填) |
| `data.itemDetail.sizeMap` | object | 否 | 尺寸映射 (多规格产品必填 |
| `data.itemDetail.imagePaths` | array&lt;string> | 否 | 图片路径列表 |
| `data.itemDetail.sourceAttrs` | array&lt;object> | 否 | 来源属性列表 |
| `data.itemDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `data.itemDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `data.itemDetail.brandName` | string | 否 | 品牌名称 |
| `data.itemDetail.itemNum` | string | 否 | 商品编码 |
| `data.itemDetail.width` | string | 否 | 宽度 |
| `data.itemDetail.length` | string | 否 | 长度 |
| `data.itemDetail.height` | string | 否 | 高度 |
| `data.itemDetail.weight` | number | 是 | 重量（kg） |
| `data.itemDetail.videoInfo` | object | 否 | 视频信息 |
| `data.itemDetail.videoInfo.videoUrl` | string | 否 | 视频url |
| `data.itemDetail.videoInfo.coverUrl` | string | 否 | 封面视频url |
| `data.itemDetail.appAccountId` | string | 否 | 应用账户ID |
| `data.itemDetail.subAppAccountId` | string | 否 | 子应用账户ID |
| `data.itemDetail.sourceItemId` | string | 否 | 来源商品ID |
| `data.itemDetail.source` | string | 否 | 来源 |
| `data.itemDetail.site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `data.itemDetail.price` | number | 否 | 价格 (单规格产品时必填) |
| `data.itemDetail.stock` | integer | 否 | 库存 (单规格产品时必填) |
| `data.itemDetail.packageLength` | string | 否 | 包裹长度 |
| `data.itemDetail.packageWidth` | string | 否 | 包裹宽度 |
| `data.itemDetail.packageHeight` | string | 否 | 包裹高度 |
| `data.itemDetail.imgUrls` | array&lt;string> | 是 | 图片URL列表 |
| `data.itemDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.itemDetail.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `data.itemDetail.isPreOrder` | integer | 是 | 是否预售 (0,1) |
| `data.itemDetail.daysToShip` | integer | 否 | 预购天数（当isPreOrder=1时必填） |
| `data.itemDetail.preOrderType` | string | 否 | 是否按SKU配置出货天数，枚举值：spu/sku |
| `data.ossMd5` | string | 否 | OSS数据的MD5值 |
