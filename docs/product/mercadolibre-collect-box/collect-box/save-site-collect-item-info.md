# 保存采集箱站点详情


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/save_site_collect_item_info`
- 类型：写
- 原文：[482753647e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753647e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.price` | number | 是 | 价格 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string | 否 | 商品备注/描述 |
| `siteCollectItemInfo.warrantyType` | string | 是 | 保修类型(sellerWarranty:卖家保修,factoryWarranty:工厂保修,noWarranty:无保修) |
| `siteCollectItemInfo.warrantyTime` | integer | 是 | 保修时长 |
| `siteCollectItemInfo.warrantyTimeUnit` | string | 是 | 保修时长单位(days:天,years:年,months:月) |
| `siteCollectItemInfo.videoUrl` | string | 否 | 视频URL |
| `siteCollectItemInfo.sourceList` | array&lt;object> | 否 | 货源列表 |
| `siteCollectItemInfo.sourceList[].source` | string | 否 | 货源来源标识 |
| `siteCollectItemInfo.sourceList[].sourceItemId` | string | 否 | 货源商品ID |
| `siteCollectItemInfo.sourceList[].sourceSite` | string | 否 | 货源站点 |
| `siteCollectItemInfo.sourceList[].sourceItemUrl` | string | 否 | 货源商品URL |
| `siteCollectItemInfo.detailId` | string | 否 | 明细ID |
| `siteCollectItemInfo.firstSkuKey` | string | 否 | 第一个SKU的key,对应skuMap中的key |
| `siteCollectItemInfo.siteAndListingTypeList` | array&lt;object> | 否 | 站点与刊登类型列表 |
| `siteCollectItemInfo.siteAndListingTypeList[].site` | string | 否 | 站点标识 |
| `siteCollectItemInfo.siteAndListingTypeList[].listingType` | string | 否 | 刊登类型 |
| `siteCollectItemInfo.siteAndTitleList` | array&lt;object> | 否 | 站点与标题列表 |
| `siteCollectItemInfo.siteAndTitleList[].site` | string | 否 | 站点标识 |
| `siteCollectItemInfo.siteAndTitleList[].title` | string | 否 | 站点商品标题 |
| `siteCollectItemInfo.pricingMode` | string | 否 | 售价模式(sellPrice:售价, netProceeds:净收益) |
| `siteCollectItemInfo.shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.attributes` | array&lt;object> | 否 | 商品属性列表（品牌/型号等） |
| `siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array&lt;object> | 否 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes` | array&lt;object> | 否 | 销售属性列表(如: 颜色/尺码) |
| `siteCollectItemInfo.saleAttributes[].name` | string | 否 | 销售属性名称(如: Color, Size) |
| `siteCollectItemInfo.saleAttributes[].values` | array&lt;object> | 否 | 销售属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识key |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 销售属性值名称 |
| `siteCollectItemInfo.saleAttributes[].id` | string | 否 | 销售属性ID(如: COLOR, SIZE) |
| `siteCollectItemInfo.sites` | array&lt;string> | 是 | 已选择的站点列表,结构["BR","BR(Full)(Up)"] |
| `siteCollectItemInfo.siteAndPriceMap` | object | 是 | 站点价格映射 |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU映射表,key为SKU组合key,value为SKU详情(当类目规则saleAttributes不为空时必填) |
| `siteCollectItemInfo.hasSaveSite` | integer | 否 | 是否已保存站点(1:是;0:否) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
