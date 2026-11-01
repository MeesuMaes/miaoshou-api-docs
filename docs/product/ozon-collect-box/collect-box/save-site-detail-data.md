# 编辑采集箱站点模式数据


- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/save_site_detail_data`
- 类型：写
- 原文：[474774630e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774630e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 产品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 产品描述 |
| `siteCollectItemInfo.itemNum` | string | 是 | 合并编号 |
| `siteCollectItemInfo.vat` | string | 是 | 增值税税率(0-豁免，10-10%，20-20%) |
| `siteCollectItemInfo.packageInfoType` | string | 是 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `siteCollectItemInfo.packageInfo` | object | 是 | 商品级别包裹尺寸信息 |
| `siteCollectItemInfo.packageInfo.depth` | integer | 否 | 深度(长) |
| `siteCollectItemInfo.packageInfo.height` | integer | 否 | 高度 |
| `siteCollectItemInfo.packageInfo.width` | integer | 否 | 宽度 |
| `siteCollectItemInfo.packageInfo.dimensionUnit` | string | 否 | 尺寸单位(毫米mm) |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.skuSelectedAttrs` | array&lt;string> | 是 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `siteCollectItemInfo.weightInfo` | object | 是 | 商品级别重量信息 |
| `siteCollectItemInfo.weightInfo.weight` | number | 否 | 重量数值 |
| `siteCollectItemInfo.weightInfo.weightUnit` | string | 否 | 重量单位(g/kg) |
| `siteCollectItemInfo.reviewsPromoOperation` | string | 是 | 是否付费推广积分评价(enable-开启，disable-关闭) |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `siteCollectItemInfo.normalAttributes` | array&lt;object> | 是 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `siteCollectItemInfo.normalAttributes[].complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.normalAttributes[].values` | array&lt;object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.normalAttributes[].values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList` | array&lt;object> | 是 | 销售属性列表(定义变体维度及其可选值) |
| `siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `siteCollectItemInfo.saleAttributeList[].nameZh` | string | 否 | 销售属性中文名称(如商品颜色) |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object | 否 | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string | 否 | 关联属性ID |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string | 否 | 关联属性俄文名称 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string | 否 | 关联属性中文名称 |
| `siteCollectItemInfo.saleAttributeList[].attrValues` | array&lt;object> | 是 | 销售属性值列表(所有变体选项) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values` | array&lt;object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object | 否 | 关联属性值(如ColorName的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values` | array&lt;object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |
| `detailId` | integer | 是 | 采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
