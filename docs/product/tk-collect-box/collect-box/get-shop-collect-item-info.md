# 获取采集箱店铺模式详情


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_shop_collect_item_info`
- 类型：读
- 原文：[446814592e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814592e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |


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
| `data.shopCollectItemInfo` | object | 否 | 店铺模式数据 |
| `data.shopCollectItemInfo.site` | string | 否 | 站点代码（如 MY、SG） |
| `data.shopCollectItemInfo.shopId` | integer | 否 | 店铺ID |
| `data.shopCollectItemInfo.detailId` | integer | 否 | 详情ID |
| `data.shopCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.shopCollectItemInfo.oriTitle` | string | 否 | 商品原始标题 |
| `data.shopCollectItemInfo.notes` | string | 否 | 备注 |
| `data.shopCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `data.shopCollectItemInfo.brandName` | string | 否 | 品牌名称 |
| `data.shopCollectItemInfo.productAttributes` | array&lt;object> | 否 | 商品属性列表 |
| `data.shopCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `data.shopCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.shopCollectItemInfo.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `data.shopCollectItemInfo.skuMap` | object | 否 | SKU Map（key=SKU标识码，value=SKU条目） |
| `data.shopCollectItemInfo.skuPropertyList` | array&lt;object> | 否 | SKU销售属性列表 |
| `data.shopCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `data.shopCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值 |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性图片URL |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array&lt;string> | 否 | 补充SKU图片URL列表 |
| `data.shopCollectItemInfo.imgUrls` | array&lt;string> | 否 | 商品图片URL列表 |
| `data.shopCollectItemInfo.weight` | number | 否 | 重量（kg） |
| `data.shopCollectItemInfo.packageLength` | number | 否 | 包裹长度（cm） |
| `data.shopCollectItemInfo.packageWidth` | number | 否 | 包裹宽度（cm） |
| `data.shopCollectItemInfo.packageHeight` | number | 否 | 包裹高度（cm） |
| `data.shopCollectItemInfo.isCodOpen` | string | 否 | 是否开启货到付款（1-是，0-否） |
| `data.shopCollectItemInfo.productCertifications` | array&lt;object> | 否 | 商品认证列表 |
| `data.shopCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `data.shopCollectItemInfo.productCertifications[].files` | array&lt;object> | 否 | 认证文件列表 |
| `data.shopCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（上传到TK的会有这个ID） |
| `data.shopCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `data.shopCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `data.shopCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `data.shopCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `data.shopCollectItemInfo.mainImgPlatformVideoId` | string | 否 | 主图平台视频ID |
| `data.shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.shopCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.shopCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型 |
| `data.shopCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `data.shopCollectItemInfo.manufacturerIds` | array&lt;string> | 否 | 制造商ID列表 |
| `data.shopCollectItemInfo.responsiblePersonIds` | array&lt;string> | 否 | 责任人ID列表 |
