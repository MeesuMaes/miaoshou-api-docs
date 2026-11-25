# 创建采集箱产品


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/create_collect_box_item`
- 类型：写
- 原文：[535697715e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/535697715e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array&lt;integer> | 是 | 店铺ids |
| `itemDetail` | object | 是 | 站点模式数据 |
| `itemDetail.title` | string | 是 | 商品标题 |
| `itemDetail.notes` | string | 是 | 商品描述 |
| `itemDetail.imgUrls` | array&lt;string> | 是 | 商品图片URL列表 |
| `itemDetail.brandId` | string | 否 | 品牌ID |
| `itemDetail.weight` | number | 是 | 重量（kg） |
| `itemDetail.packageLength` | number | 是 | 包装长度（cm） |
| `itemDetail.packageWidth` | number | 是 | 包装宽度（cm） |
| `itemDetail.packageHeight` | number | 是 | 包装高度（cm） |
| `itemDetail.productCertifications` | array&lt;object> | 否 | 商品认证列表 |
| `itemDetail.productCertifications[].id` | string | 否 | 认证ID |
| `itemDetail.productCertifications[].files` | array&lt;object> | 否 | 认证文件列表 |
| `itemDetail.productCertifications[].files[].fileId` | string | 否 | 文件ID（如果文件是TK的需要传这个ID） |
| `itemDetail.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `itemDetail.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `itemDetail.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `itemDetail.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `itemDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `itemDetail.isCodOpen` | string | 否 | 是否开启货到付款（1=是，0=否） |
| `itemDetail.cid` | string | 是 | 类目ID |
| `itemDetail.editModel` | string | 否 | 编辑模式（shop=店铺模式，site=站点模式） |
| `itemDetail.version` | string | 否 | 版本号 |
| `itemDetail.shopId` | integer | 否 | 店铺ID |
| `itemDetail.detailId` | integer | 否 | 采集箱详情ID |
| `itemDetail.sizeChartType` | string | 否 | 尺码表类型（仅支持image） |
| `itemDetail.sizeChart` | string | 否 | 尺码表图片URL |
| `itemDetail.deliveryOptionSetType` | string | 否 | 配送选项设置类型仅支持（仅default） |
| `itemDetail.skuMap` | object | 否 | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `itemDetail.skuPropertyList` | array&lt;object> | 否 | SKU 规格属性列表 |
| `itemDetail.skuPropertyList[].attrName` | string | 否 | 属性名称，如 Color、Size |
| `itemDetail.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `itemDetail.skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 |
| `itemDetail.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID（构造SkuMap的key时使用该值） |
| `itemDetail.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `itemDetail.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值图片URL |
| `itemDetail.productAttributes` | array&lt;object> | 否 | 商品属性列表 |
| `itemDetail.productAttributes[].attributeId` | string | 否 | 属性ID |
| `itemDetail.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `itemDetail.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `itemDetail.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `itemDetail.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `itemDetail.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `itemDetail.collectBoxDetailShopList` | array&lt;object> | 否 | 店铺特殊数据信息列表 |
| `itemDetail.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `itemDetail.collectBoxDetailShopList[].site` | string | 是 | 站点 |
| `itemDetail.collectBoxDetailShopList[].brandId` | string | 否 | 品牌ID |
| `itemDetail.collectBoxDetailShopList[].manufacturerIds` | array&lt;string> | 否 | 制造商ID列表 |
| `itemDetail.collectBoxDetailShopList[].responsiblePersonIds` | array&lt;string> | 否 | 责任人ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailId` | integer | 是 | 采集箱详情OssMd5标识 |
