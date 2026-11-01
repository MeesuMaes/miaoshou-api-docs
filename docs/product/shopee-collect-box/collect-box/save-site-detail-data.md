# 保存站点编辑数据


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/save_site_detail_data`
- 类型：写
- 原文：[516157439e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157439e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `ossMd5` | string | 是 | OSS数据的MD5值 |
| `siteDetailSimpleData` | object | 是 | 站点编辑数据（完整siteDetailSimpleData对象） |
| `siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `siteDetailSimpleData.itemNum` | string | 否 | 主货号 |
| `siteDetailSimpleData.price` | string | 否 | 销售价(单规格产品时必填) |
| `siteDetailSimpleData.stock` | string | 否 | 库存(单规格产品时必填) |
| `siteDetailSimpleData.sellerStock` | array&lt;object> | 否 | 按仓库分配库存(单规格产品时选填) |
| `siteDetailSimpleData.sellerStock[].locationId` | string | 否 | 仓库ID |
| `siteDetailSimpleData.sellerStock[].stock` | integer | 否 | 库存数量 |
| `siteDetailSimpleData.sellerStock[].shopId` | integer | 否 | 店铺ID |
| `siteDetailSimpleData.colorPropName` | string | 否 | 颜色属性名称 |
| `siteDetailSimpleData.sizePropName` | string | 否 | 尺码属性名称 |
| `siteDetailSimpleData.colorMap` | object | 否 | 颜色Map，key为颜色名 |
| `siteDetailSimpleData.sizeMap` | object | 否 | 尺码Map，key为尺码名 |
| `siteDetailSimpleData.skuMap` | object | 否 | SKU Map，key为规格组合（如;121201;;） |
| `siteDetailSimpleData.imgUrls` | array&lt;string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `siteDetailSimpleData.packageLength` | string | 否 | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageWidth` | string | 否 | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageHeight` | string | 否 | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `siteDetailSimpleData.richTextDesc` | string | 否 | 富文本描述 |
| `siteDetailSimpleData.wholesaleList` | array&lt;object> | 否 | 批发列表 |
| `siteDetailSimpleData.wholesaleList[].min` | integer | 否 | 最小数量 |
| `siteDetailSimpleData.wholesaleList[].max` | integer | 否 | 最大数量 |
| `siteDetailSimpleData.wholesaleList[].price` | number | 否 | 批发单价 |
| `siteDetailSimpleData.attributeMaps` | object | 否 | 属性Map，key为属性ID |
| `siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `siteDetailSimpleData.brand.brandId` | integer | 否 | 品牌ID |
| `siteDetailSimpleData.brand.brandName` | string | 否 | 品牌名称 |
| `siteDetailSimpleData.logisticList` | array&lt;object> | 是 | 物流方式列表 |
| `siteDetailSimpleData.logisticList[].logisticId` | string | 否 | 物流方式ID |
| `siteDetailSimpleData.logisticList[].logisticName` | string | 否 | 物流方式名称 |
| `siteDetailSimpleData.logisticList[].enabled` | boolean | 否 | 是否启用 |
| `siteDetailSimpleData.logisticList[].estimatedShippingFee` | number | 否 | 预估运费 |
| `siteDetailSimpleData.logisticList[].isFree` | boolean | 否 | 是否包邮 |
| `siteDetailSimpleData.logisticList[].sizeId` | integer | 否 | 尺寸ID |
| `siteDetailSimpleData.logisticList[].customPrice` | string | 否 | 自定义运费 |
| `siteDetailSimpleData.logisticList[].site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `siteDetailSimpleData.daysToShip` | integer | 否 | 发货天数 |
| `siteDetailSimpleData.sizeChart` | string | 否 | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `siteDetailSimpleData.mainImgVideoUrl` | string | 否 | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `siteDetailSimpleData.mainImgAppVideoId` | integer | 否 | 产品视频AppVideoId |
| `siteDetailSimpleData.mainImgVideoExpire` | string | 否 | 产品视频过期时间 |
| `siteDetailSimpleData.isMainImgVideoExpire` | integer | 否 | 产品视频是否过期 |
| `siteDetailSimpleData.originPrice` | string | 否 | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `siteDetailSimpleData.colorPropGroupName` | string | 否 | 颜色属性分组名称 |
| `siteDetailSimpleData.sizePropGroupName` | string | 否 | 尺码属性分组名称 |
| `siteDetailSimpleData.preOrderType` | string | 否 | 否按SKU配置出货天数，枚举值：spu/sku |
| `siteDetailSimpleData.sizeChartType` | string | 否 | 尺码表类型，部分类目必填，枚举值：template/image |
| `siteDetailSimpleData.shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `siteDetailSimpleData.certificationInfoList` | array&lt;object> | 否 | 商品认证信息列表 |
| `siteDetailSimpleData.certificationInfoList[].certificationType` | integer | 否 | 认证类型ID |
| `siteDetailSimpleData.certificationInfoList[].certificationNo` | string | 否 | 认证编码 |
| `siteDetailSimpleData.certificationInfoList[].expireTime` | integer | 否 | 过期时间(时间戳，例如1782748800) |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs` | array&lt;object> | 否 |  |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string | 否 | 文件类型 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string | 否 | 文件名 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string | 否 | 文件URL |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer | 否 | 文件UUID(例如：1782467304138) |
| `siteDetailSimpleData.certificationInfoList[].permitId` | integer | 否 | 认证ID |
| `siteDetailSimpleData.certificationInfoList[].name` | string | 否 | 认证名称 |
| `siteDetailSimpleData.isSuppSizechart` | integer | 否 | 是否支持尺码表 |
| `siteDetailSimpleData.hasTranslate` | integer | 否 | 是否已翻译（1=是） |
| `siteDetailSimpleData.barcode` | string | 否 | 识别码 |
| `siteDetailSimpleData.barcodeType` | string | 否 | 识别码类型 |
| `syncSites` | array&lt;string> | 否 | 需要同步的其他站点列表 |
| `syncSiteFields` | array&lt;string> | 否 | 需要同步的站点字段列表 |
| `shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 | OSS数据的MD5值 |
| `data.syncErrors` | array&lt;object> | 否 | 同步错误列表 |
| `data.syncErrors[].site` | string | 否 | 站点 |
| `data.syncErrors[].errorMsg` | string | 否 | 错误信息 |
