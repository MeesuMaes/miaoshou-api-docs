# 获取站点编辑信息


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_site_detail_simple_data`
- 类型：读
- 原文：[480434496e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434496e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supportSizeChartInfo` | object | 否 | 尺码图支持信息 |
| `data.supportSizeChartInfo.shopeeCategorySupportSizeChartId` | integer | 否 | ID |
| `data.supportSizeChartInfo.site` | string | 否 | 站点 |
| `data.supportSizeChartInfo.cid` | integer | 否 | 类目ID |
| `data.supportSizeChartInfo.isSupportSizeChart` | integer | 否 | 是否支持尺码图表(0,1) |
| `data.supportSizeChartInfo.sizeChartMandatory` | integer | 否 | 尺码表是否强制 |
| `data.supportSizeChartInfo.supportImageSizeChart` | integer | 否 | 是否支持图片尺码表 |
| `data.supportSizeChartInfo.supportTemplateSizeChart` | integer | 否 | 是否支持模板尺码表 |
| `data.supportSizeChartInfo.gmtCreate` | string | 否 | 创建时间 |
| `data.supportSizeChartInfo.gmtModified` | string | 否 | 更新时间 |
| `data.siteDetailSimpleData` | object | 否 | 站点信息详情 |
| `data.siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `data.siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `data.siteDetailSimpleData.itemNum` | string | 否 | 主货号 |
| `data.siteDetailSimpleData.price` | string | 否 | 销售价(单规格产品时必填) |
| `data.siteDetailSimpleData.stock` | string | 否 | 库存(单规格产品时必填) |
| `data.siteDetailSimpleData.sellerStock` | array&lt;object> | 否 | 按仓库分配库存(单规格产品时选填) |
| `data.siteDetailSimpleData.sellerStock[].locationId` | string | 否 | 仓库ID |
| `data.siteDetailSimpleData.sellerStock[].stock` | integer | 否 | 库存数量 |
| `data.siteDetailSimpleData.sellerStock[].shopId` | integer | 否 | 店铺ID |
| `data.siteDetailSimpleData.colorPropName` | string | 否 | 颜色属性名称 |
| `data.siteDetailSimpleData.sizePropName` | string | 否 | 尺码属性名称 |
| `data.siteDetailSimpleData.colorMap` | object | 否 | 颜色Map，key为颜色名 |
| `data.siteDetailSimpleData.sizeMap` | object | 否 | 尺码Map，key为尺码名 |
| `data.siteDetailSimpleData.skuMap` | object | 否 | SKU Map，key为规格组合（如;121201;;） |
| `data.siteDetailSimpleData.imgUrls` | array&lt;string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `data.siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `data.siteDetailSimpleData.packageLength` | string | 否 | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `data.siteDetailSimpleData.packageWidth` | string | 否 | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `data.siteDetailSimpleData.packageHeight` | string | 否 | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `data.siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `data.siteDetailSimpleData.richTextDesc` | string | 否 | 富文本描述 |
| `data.siteDetailSimpleData.wholesaleList` | array&lt;object> | 否 | 批发列表 |
| `data.siteDetailSimpleData.wholesaleList[].min` | integer | 否 | 最小数量 |
| `data.siteDetailSimpleData.wholesaleList[].max` | integer | 否 | 最大数量 |
| `data.siteDetailSimpleData.wholesaleList[].price` | number | 否 | 批发单价 |
| `data.siteDetailSimpleData.attributeMaps` | object | 否 | 属性Map，key为属性ID |
| `data.siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `data.siteDetailSimpleData.brand.brandId` | integer | 否 | 品牌ID |
| `data.siteDetailSimpleData.brand.brandName` | string | 否 | 品牌名称 |
| `data.siteDetailSimpleData.logisticList` | array&lt;object> | 是 | 物流方式列表 |
| `data.siteDetailSimpleData.logisticList[].logisticId` | string | 否 | 物流方式ID |
| `data.siteDetailSimpleData.logisticList[].logisticName` | string | 否 | 物流方式名称 |
| `data.siteDetailSimpleData.logisticList[].enabled` | boolean | 否 | 是否启用 |
| `data.siteDetailSimpleData.logisticList[].estimatedShippingFee` | number | 否 | 预估运费 |
| `data.siteDetailSimpleData.logisticList[].isFree` | boolean | 否 | 是否包邮 |
| `data.siteDetailSimpleData.logisticList[].sizeId` | integer | 否 | 尺寸ID |
| `data.siteDetailSimpleData.logisticList[].customPrice` | string | 否 | 自定义运费 |
| `data.siteDetailSimpleData.logisticList[].site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `data.siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `data.siteDetailSimpleData.daysToShip` | integer | 否 | 发货天数 |
| `data.siteDetailSimpleData.sizeChart` | string | 否 | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `data.siteDetailSimpleData.mainImgVideoUrl` | string | 否 | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `data.siteDetailSimpleData.mainImgAppVideoId` | integer | 否 | 产品视频AppVideoId |
| `data.siteDetailSimpleData.mainImgVideoExpire` | string | 否 | 产品视频过期时间 |
| `data.siteDetailSimpleData.isMainImgVideoExpire` | integer | 否 | 产品视频是否过期 |
| `data.siteDetailSimpleData.originPrice` | string | 否 | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `data.siteDetailSimpleData.colorPropGroupName` | string | 否 | 颜色属性分组名称 |
| `data.siteDetailSimpleData.sizePropGroupName` | string | 否 | 尺码属性分组名称 |
| `data.siteDetailSimpleData.preOrderType` | string | 否 | 否按SKU配置出货天数，枚举值：spu/sku |
| `data.siteDetailSimpleData.sizeChartType` | string | 否 | 尺码表类型，部分类目必填，枚举值：template/image |
| `data.siteDetailSimpleData.shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `data.siteDetailSimpleData.certificationInfoList` | array&lt;object> | 否 | 商品认证信息列表 |
| `data.siteDetailSimpleData.certificationInfoList[].certificationType` | integer | 否 | 认证类型ID |
| `data.siteDetailSimpleData.certificationInfoList[].certificationNo` | string | 否 | 认证编码 |
| `data.siteDetailSimpleData.certificationInfoList[].expireTime` | integer | 否 | 过期时间(时间戳，例如1782748800) |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs` | array&lt;object> | 否 |  |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string | 否 | 文件类型 |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string | 否 | 文件名 |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string | 否 | 文件URL |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer | 否 | 文件UUID(例如：1782467304138) |
| `data.siteDetailSimpleData.certificationInfoList[].permitId` | integer | 否 | 认证ID |
| `data.siteDetailSimpleData.certificationInfoList[].name` | string | 否 | 认证名称 |
| `data.siteDetailSimpleData.isSuppSizechart` | integer | 否 | 是否支持尺码表 |
| `data.siteDetailSimpleData.hasTranslate` | integer | 否 | 是否已翻译（1=是） |
| `data.siteDetailSimpleData.barcode` | string | 否 | 识别码 |
| `data.siteDetailSimpleData.barcodeType` | string | 否 | 识别码类型 |
| `data.isFirstCreateSiteData` | boolean | 否 |  |
| `data.logisticOptions` | object | 否 |  |
| `data.ossMd5` | string | 否 |  |
