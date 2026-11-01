# 获取采集箱站点模式详情


- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[474774628e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774628e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.siteCollectItemInfo` | object | 否 | 站点数据 |
| `data.siteCollectItemInfo.detailId` | string | 否 | 采集箱详情ID |
| `data.siteCollectItemInfo.site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 合并编号 |
| `data.siteCollectItemInfo.notes` | string | 否 | 商品描述 |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.packageInfoType` | string | 否 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `data.siteCollectItemInfo.packageInfo` | object | 否 | 商品级别包裹尺寸信息 |
| `data.siteCollectItemInfo.packageInfo.depth` | integer | 否 | 深度(长) |
| `data.siteCollectItemInfo.packageInfo.height` | integer | 否 | 高度 |
| `data.siteCollectItemInfo.packageInfo.width` | integer | 否 | 宽度 |
| `data.siteCollectItemInfo.packageInfo.dimensionUnit` | string | 否 | 尺寸单位(毫米mm) |
| `data.siteCollectItemInfo.weightInfo` | object | 否 | 商品级别重量信息 |
| `data.siteCollectItemInfo.weightInfo.weight` | number | 否 | 重量数值 |
| `data.siteCollectItemInfo.weightInfo.weightUnit` | string | 否 | 重量单位(g/kg) |
| `data.siteCollectItemInfo.vat` | string | 否 | 增值税税率(0-豁免，10-10%，20-20%) |
| `data.siteCollectItemInfo.skuSelectedAttrs` | array&lt;string> | 否 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射关系，key为saleAttributeList销售属性里valueKey用分号加首尾分号的拼接值，如：“;红色;S;” |
| `data.siteCollectItemInfo.saleAttributeList` | array&lt;object> | 否 | 销售属性列表(定义变体维度及其可选值) |
| `data.siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `data.siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `data.siteCollectItemInfo.saleAttributeList[].nameZh` | string | 否 | 销售属性中文名称(如商品颜色) |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object | 否 | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string | 否 | 关联属性ID |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string | 否 | 关联属性俄文名称 |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string | 否 | 关联属性中文名称 |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues` | array&lt;object> | 是 | 销售属性值列表(所有变体选项) |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object | 否 | 关联属性值(如ColorName的字典值) |
| `data.siteCollectItemInfo.normalAttributes` | array&lt;object> | 否 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `data.siteCollectItemInfo.normalAttributes[].complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `data.siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `data.siteCollectItemInfo.normalAttributes[].values` | array&lt;object> | 是 | 属性字典值列表 |
| `data.siteCollectItemInfo.normalAttributes[].values[].value` | string | 否 | 属性值文本值 |
| `data.siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `data.siteCollectItemInfo.videos` | array&lt;object> | 否 | 产品描述视频列表 |
| `data.siteCollectItemInfo.videos[].mainImgVideoUrl` | string | 否 | 视频URL |
| `data.siteCollectItemInfo.videos[].mainImgAppVideoId` | integer | 否 | 视频ID |
| `data.siteCollectItemInfo.reviewsPromoOperation` | string | 否 | 是否付费推广积分评价(enable-开启，disable-关闭) |
