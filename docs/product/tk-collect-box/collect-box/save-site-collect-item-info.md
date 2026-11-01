# 保存采集箱站点模式详情


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/save_site_collect_item_info`
- 类型：写
- 原文：[449650817e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449650817e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ossMd5` | string | 是 | ossMd5值 |
| `site` | string | 是 | 站点 |
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 商品描述 |
| `siteCollectItemInfo.imgUrls` | array&lt;string> | 是 | 商品图片URL列表 |
| `siteCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `siteCollectItemInfo.weight` | number | 是 | 重量（kg） |
| `siteCollectItemInfo.packageLength` | number | 是 | 包装长度（cm） |
| `siteCollectItemInfo.packageWidth` | number | 是 | 包装宽度（cm） |
| `siteCollectItemInfo.packageHeight` | number | 是 | 包装高度（cm） |
| `siteCollectItemInfo.productCertifications` | array&lt;object> | 否 | 商品认证列表 |
| `siteCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `siteCollectItemInfo.productCertifications[].files` | array&lt;object> | 否 | 认证文件列表 |
| `siteCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（如果文件是TK的需要传这个ID） |
| `siteCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `siteCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.isCodOpen` | string | 是 | 是否开启货到付款（1=是，0=否） |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.editModel` | string | 否 | 编辑模式（shop=店铺模式，site=站点模式） |
| `siteCollectItemInfo.version` | string | 否 | 版本号 |
| `siteCollectItemInfo.shopId` | integer | 否 | 店铺ID |
| `siteCollectItemInfo.detailId` | integer | 否 | 采集箱详情ID |
| `siteCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型（仅支持image） |
| `siteCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `siteCollectItemInfo.deliveryOptionSetType` | string | 是 | 配送选项设置类型仅支持（仅default） |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `siteCollectItemInfo.skuPropertyList` | array&lt;object> | 否 | SKU 规格属性列表 |
| `siteCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称，如 Color、Size |
| `siteCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `siteCollectItemInfo.skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID（构造SkuMap的key时使用该值） |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值图片URL |
| `siteCollectItemInfo.productAttributes` | array&lt;object> | 否 | 商品属性列表 |
| `siteCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `siteCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `siteCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `siteCollectItemInfo.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `siteCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `siteCollectItemInfo.collectBoxDetailShopList` | array&lt;object> | 否 | 店铺特殊数据信息列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 是 | 站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].brandId` | string | 否 | 品牌ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].manufacturerIds` | array&lt;string> | 否 | 制造商ID列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].responsiblePersonIds` | array&lt;string> | 否 | 责任人ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 是 | 采集箱详情OssMd5标识 |
