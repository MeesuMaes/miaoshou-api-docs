# 获取采集箱站点模式详情


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[449650816e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449650816e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `site` | string | 是 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 | ossMd5值 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array&lt;integer> | 否 | 已认领的店铺IDS |
| `data.isSupportMultiWarehouse` | integer | 否 | 是否支持多仓库 |
| `data.siteCollectItemInfo` | object | 否 | 店铺模式数据 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点代码（如 PH、MY） |
| `data.siteCollectItemInfo.detailId` | integer | 否 | 详情ID |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.notes` | string | 否 | 备注 |
| `data.siteCollectItemInfo.imgUrls` | array&lt;string> | 否 | 商品图片URL列表 |
| `data.siteCollectItemInfo.weight` | number | 否 | 重量（kg） |
| `data.siteCollectItemInfo.packageLength` | number | 否 | 包裹长度（cm） |
| `data.siteCollectItemInfo.packageWidth` | number | 否 | 包裹宽度（cm） |
| `data.siteCollectItemInfo.packageHeight` | number | 否 | 包裹高度（cm） |
| `data.siteCollectItemInfo.productCertifications` | array&lt;object> | 否 | 商品认证列表 |
| `data.siteCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `data.siteCollectItemInfo.productCertifications[].files` | array&lt;object> | 否 | 认证文件列表 |
| `data.siteCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（上传到TK的会有这个ID） |
| `data.siteCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `data.siteCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `data.siteCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `data.siteCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `data.siteCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型 |
| `data.siteCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU Map（key=SKU标识码，value=SKU条目） |
| `data.siteCollectItemInfo.skuPropertyList` | array&lt;object> | 否 | SKU销售属性列表 |
| `data.siteCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `data.siteCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值 |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性图片URL |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array&lt;string> | 否 | 补充SKU图片URL列表 |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图App端视频ID |
| `data.siteCollectItemInfo.mainImgPlatformVideoId` | string | 否 | 主图平台视频ID |
| `data.siteCollectItemInfo.isCodOpen` | string | 否 | 是否开启货到付款（1-是，0-否） |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.siteCollectItemInfo.productAttributes` | array&lt;object> | 否 | 商品属性列表 |
| `data.siteCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `data.siteCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.siteCollectItemInfo.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList` | array&lt;object> | 否 | 采集箱店铺维度配置列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点代码（如 PH、MY） |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].brandId` | string | 否 | 品牌ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].brandName` | string | 否 | 品牌名称 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].deliveryOptionSetType` | string | 否 | 配送选项设置类型 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].deliveryOptionIds` | array&lt;string> | 否 | 配送选项ID列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].manufacturerIds` | array&lt;string> | 否 | 制造商ID列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].responsiblePersonIds` | array&lt;string> | 否 | 责任人ID列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].sizeChartTemplateId` | string | 否 | 尺码表模板ID |
