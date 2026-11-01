# 获取采集箱店铺模式详情


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_shop_collect_item_info`
- 类型：读
- 原文：[471545324e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545324e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |
| `cid` | integer | 否 | 新类目id（需要切换类目时填写新的cid，可以快速匹配相同属性，需要保存才能生效新的类目） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array&lt;integer> | 否 | 已认领的店铺IDS |
| `data.shopCollectItemInfo` | object | 否 | 店铺模式数据 |
| `data.shopCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.shopCollectItemInfo.saleAttributes` | array&lt;object> | 否 | 销售属性列表 |
| `data.shopCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.shopCollectItemInfo.saleAttributes[].pid` | integer | 否 | 基础属性id |
| `data.shopCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 属性id |
| `data.shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 否 | 父规格ID |
| `data.shopCollectItemInfo.saleAttributes[].name` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.saleAttributes[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `data.shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识码 |
| `data.shopCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `data.shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类货号（服饰类的货号是SKC级别的） |
| `data.shopCollectItemInfo.attributes` | array&lt;object> | 否 | 商品属性列表（成分/材质等） |
| `data.shopCollectItemInfo.attributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.shopCollectItemInfo.attributes[].pid` | integer | 否 | 基础属性id |
| `data.shopCollectItemInfo.attributes[].refPid` | integer | 否 | 属性id |
| `data.shopCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.attributes[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.attributes[].values[].vid` | integer | 否 | 属性值id |
| `data.shopCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位 |
| `data.shopCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例(所有成分比例之和需等于100) |
| `data.shopCollectItemInfo.skuMap` | object | 否 | SKU映射（key=SKU标识码，value=SKU条目） |
| `data.shopCollectItemInfo.sizeCharts` | array&lt;object> | 否 | 尺码表列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 否 | 尺码模板来源 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.shopCollectItemInfo.sizeCharts[].elementIds` | array&lt;integer> | 否 | 元素ID列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems` | array&lt;object> | 否 | 尺码项列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 否 | 尺码名称 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array&lt;object> | 否 | 元素值列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array&lt;object> | 否 | 分组值列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与值映射 |
| `data.shopCollectItemInfo.sizeCharts[].manualEntryIds` | array&lt;integer> | 否 | 手动录入ID列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 否 | 尺码模板唯一ID |
| `data.shopCollectItemInfo.imgUrls` | array&lt;string> | 否 | 商品图片URL列表 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs` | array&lt;object> | 否 | 产品描述 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `data.shopCollectItemInfo.outerPackageShape` | integer | 否 | 外包装形状 |
| `data.shopCollectItemInfo.outerPackageType` | integer | 否 | 外包装类型 |
| `data.shopCollectItemInfo.outerPackageImgUrls` | array&lt;string> | 否 | 外包装图片URL列表 |
| `data.shopCollectItemInfo.productOriginCountry` | string | 否 | 原产国 |
| `data.shopCollectItemInfo.productOriginProvince` | string | 否 | 原产省 |
| `data.shopCollectItemInfo.currency` | string | 否 | 币种 |
| `data.shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.shopCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图平台视频ID |
| `data.shopCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.shopCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `data.shopCollectItemInfo.goodsModelReqs` | array&lt;object> | 否 | 模特信息列表 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelId` | string | 否 | 模特ID |
| `data.shopCollectItemInfo.goodsModelReqs[].shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.goodsModelReqs[].modelName` | string | 否 | 模特名称 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelType` | string | 否 | 模特类型 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 否 | 模特图片URL |
| `data.shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 否 | 身高（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 否 | 试穿尺码规格名称 |
| `data.shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 否 | 试穿结果 |
| `data.shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 否 | 尺码规格ID |
| `data.shopCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `data.shopCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.shopCollectItemInfo.site` | string | 否 | 站点 |
| `data.shopCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `data.shopCollectItemInfo.isBasePlate` | integer | 否 | 是否底版 |
| `data.shopCollectItemInfo.detailId` | string | 否 | 详情ID |
| `data.shopCollectItemInfo.vehicleLibraryRelationList` | array&lt;object> | 否 | 车辆库关联列表 |
| `data.shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 否 | 车型库站点ID |
| `data.shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 否 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array&lt;int, array&lt;int, array\{vidValue: string, propertyValueDependencyId: string, level: string\}>> |
| `data.shopCollectItemInfo.collectShowSizeTemplateIds` | array&lt;integer> | 否 | 采集展示尺码模板ID列表 |
| `data.shopCollectItemInfo.sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array&lt;string> | 否 | 制造地点 |
