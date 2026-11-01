# 获取采集箱站点模式详情


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[477347606e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347606e0.md)

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
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array&lt;integer> | 否 | 已认领的店铺IDS |
| `data.siteCollectItemInfo` | object | 否 | 站点模式数据，包含商品基础信息、属性、SKU、店铺列表、发布站点等 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.siteCollectItemInfo.saleAttributes` | array&lt;object> | 否 | 销售属性列表 |
| `data.siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 基础属性id |
| `data.siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 属性id |
| `data.siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 否 | 父规格ID |
| `data.siteCollectItemInfo.saleAttributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.saleAttributes[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `data.siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识码 |
| `data.siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `data.siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类货号（服饰类的货号是SKC级别的） |
| `data.siteCollectItemInfo.attributes` | array&lt;object> | 否 | 商品属性列表（成分/材质等） |
| `data.siteCollectItemInfo.attributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.siteCollectItemInfo.attributes[].pid` | integer | 否 | 基础属性id |
| `data.siteCollectItemInfo.attributes[].refPid` | integer | 否 | 属性id |
| `data.siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.attributes[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.attributes[].values[].vid` | integer | 否 | 属性值id |
| `data.siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位 |
| `data.siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例(所有成分比例之和需等于100) |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射（key=SKU标识码，value=SKU条目） |
| `data.siteCollectItemInfo.sizeCharts` | array&lt;object> | 否 | 尺码表列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 否 | 尺码模板来源 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.siteCollectItemInfo.sizeCharts[].elementIds` | array&lt;integer> | 否 | 元素ID列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems` | array&lt;object> | 否 | 尺码项列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 否 | 尺码名称 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array&lt;object> | 否 | 元素值列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array&lt;object> | 否 | 分组值列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与值映射 |
| `data.siteCollectItemInfo.sizeCharts[].manualEntryIds` | array&lt;integer> | 否 | 手动录入ID列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 否 | 尺码模板唯一ID |
| `data.siteCollectItemInfo.imgUrls` | array&lt;string> | 否 | 商品图片URL列表 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs` | array&lt;object> | 否 | 产品描述 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `data.siteCollectItemInfo.productOriginCountry` | string | 否 | 原产国 |
| `data.siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省 |
| `data.siteCollectItemInfo.shipmentLimitDay` | integer | 否 | 发货时效（天） |
| `data.siteCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 站点维度发货时效映射，key 为站点编码，value 为发货天数 |
| `data.siteCollectItemInfo.currency` | string | 否 | 币种 |
| `data.siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.siteCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为站点编码，value 为图片URL列表 |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图平台视频ID |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `data.siteCollectItemInfo.goodsModelReqs` | array&lt;object> | 否 | 模特信息列表 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelId` | string | 否 | 模特ID |
| `data.siteCollectItemInfo.goodsModelReqs[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.goodsModelReqs[].modelName` | string | 否 | 模特名称 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelType` | string | 否 | 模特类型 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 否 | 模特图片URL |
| `data.siteCollectItemInfo.goodsModelReqs[].modelHeight` | string | 否 | 身高（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 否 | 试穿尺码规格名称 |
| `data.siteCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 否 | 试穿结果 |
| `data.siteCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 否 | 尺码规格ID |
| `data.siteCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `data.siteCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.siteCollectItemInfo.publishSiteList` | array&lt;string> | 否 | 发布站点列表 |
| `data.siteCollectItemInfo.publishEuSiteList` | array&lt;string> | 否 | 欧盟发布站点列表 |
| `data.siteCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型 |
| `data.siteCollectItemInfo.materialMultiLanguages` | array&lt;string> | 否 | 多语言素材语言列表 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `data.siteCollectItemInfo.isBasePlate` | integer | 否 | 是否底版 |
| `data.siteCollectItemInfo.detailId` | string | 否 | 详情ID |
| `data.siteCollectItemInfo.vehicleLibraryRelationList` | array&lt;object> | 否 | 车辆库关联列表 |
| `data.siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 否 | 车型库站点ID |
| `data.siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 否 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array&lt;int, array&lt;int, array\{vidValue: string, propertyValueDependencyId: string, level: string\}>> |
| `data.siteCollectItemInfo.collectShowSizeTemplateIds` | array&lt;integer> | 否 | 采集展示尺码模板ID列表 |
| `data.siteCollectItemInfo.sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.siteCollectItemInfo.personalizationSwitch` | string | 否 | 个性化开关，0-关闭 1-开启 |
| `data.siteCollectItemInfo.discreetShipping` | string | 否 | 隐密发货 |
| `data.siteCollectItemInfo.collectBoxDetailShopList` | array&lt;object> | 否 | 店铺列表，站点模式关联的店铺详情列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].sizeTemplateId` | string | 否 | 尺码表模板ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array&lt;object> | 否 | 站点运费模板列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 否 | 站点编码，如 US、EU |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 否 | 运费模板ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array&lt;object> | 否 | 站点仓库列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 否 | 站点编码，如 US、EU |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | integer | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，US 站直接填写 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array&lt;object> | 否 | EU 站子站点仓库列表，US 站无此字段 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopName` | string | 否 | 店铺名称 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].currency` | string | 否 | 币种 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].itemNum` | string | 否 | 货号 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array&lt;string> | 否 | 发布站点列表 |
| `data.siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `data.siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array&lt;string> | 否 | 制造地点 |
