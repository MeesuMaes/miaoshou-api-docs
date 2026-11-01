# 保存采集箱店铺模式详情


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/save_shop_collect_item_info`
- 类型：写
- 原文：[446814593e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814593e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ossMd5` | string | 是 | ossMd5值 |
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.notes` | string | 是 | 商品描述 |
| `shopCollectItemInfo.imgUrls` | array&lt;string> | 是 | 商品图片URL列表 |
| `shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `shopCollectItemInfo.weight` | number | 是 | 重量（kg） |
| `shopCollectItemInfo.packageLength` | number | 是 | 包装长度（cm） |
| `shopCollectItemInfo.packageWidth` | number | 是 | 包装宽度（cm） |
| `shopCollectItemInfo.packageHeight` | number | 是 | 包装高度（cm） |
| `shopCollectItemInfo.productCertifications` | array&lt;object> | 否 | 商品认证列表 |
| `shopCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `shopCollectItemInfo.productCertifications[].files` | array&lt;object> | 否 | 认证文件列表 |
| `shopCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（如果文件是TK的需要传这个ID） |
| `shopCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `shopCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `shopCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `shopCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `shopCollectItemInfo.isCodOpen` | string | 是 | 是否开启货到付款（1=是，0=否） |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.editModel` | string | 否 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.version` | string | 否 | 版本号 |
| `shopCollectItemInfo.shopId` | integer | 否 | 店铺ID |
| `shopCollectItemInfo.detailId` | integer | 否 | 采集箱详情ID |
| `shopCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型（仅支持image） |
| `shopCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `shopCollectItemInfo.deliveryOptionSetType` | string | 是 | 配送选项设置类型仅支持（仅default） |
| `shopCollectItemInfo.skuMap` | object | 否 | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `shopCollectItemInfo.skuPropertyList` | array&lt;object> | 否 | SKU 规格属性列表 |
| `shopCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称，如 Color、Size |
| `shopCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `shopCollectItemInfo.skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID（构造SkuMap的key时使用该值） |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值图片URL |
| `shopCollectItemInfo.productAttributes` | array&lt;object> | 否 | 商品属性列表 |
| `shopCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `shopCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `shopCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `shopCollectItemInfo.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `shopCollectItemInfo.manufacturerIds` | array&lt;string> | 否 | 制造商ID列表 |
| `shopCollectItemInfo.responsiblePersonIds` | array&lt;string> | 否 | 责任人ID列表 |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 是 | 采集箱详情OssMd5标识 |
