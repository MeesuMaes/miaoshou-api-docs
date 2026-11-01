# 保存采集箱店铺模式详情


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/save_shop_collect_item_info`
- 类型：写
- 原文：[471545325e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545325e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.detailId` | integer | 是 | 采集箱详情ID |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `shopCollectItemInfo.imgUrls` | array&lt;string> | 是 | 轮播图 |
| `shopCollectItemInfo.goodsLayerDecorationReqs` | array&lt;object> | 是 | 产品描述 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer | 否 | 字体大小 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string | 否 | 字体粗细 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string | 否 | 对齐方式 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string | 否 | 字体颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string | 否 | 背景颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer | 否 | 字体族 |
| `shopCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `shopCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `shopCollectItemInfo.productOriginCertFiles` | array&lt;object> | 否 | 原产地认证文件列表 |
| `shopCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `shopCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `shopCollectItemInfo.currency` | string | 否 | 店铺币种 |
| `shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `shopCollectItemInfo.productGuideFileUrl` | string | 否 | 产品说明书URL |
| `shopCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名 |
| `shopCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状 |
| `shopCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型 |
| `shopCollectItemInfo.outerPackageImgUrls` | array&lt;string> | 是 | 外包装图片URL列表 |
| `shopCollectItemInfo.site` | string | 否 | 站点（temu全托 目前只有PDDKJ） |
| `shopCollectItemInfo.editModel` | string | 是 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `shopCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版 2=套版） |
| `shopCollectItemInfo.basePlateSkuKey` | string | 否 | 底板SKU Key |
| `shopCollectItemInfo.sizeCharts` | array&lt;object> | 否 | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].manualEntryIds` | array&lt;integer> | 否 | 手动录入ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array&lt;integer> | 是 | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array&lt;object> | 是 | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array&lt;object> | 是 | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array&lt;object> | 是 | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `shopCollectItemInfo.vehicleLibraryRelationList` | array&lt;object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ \{ "vehicleLibraryId": 1, "productPropValueDependencyList": [ [\{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"\}, \{"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"\}, \{"level":3,"propertyValueDependencyId":300,"vidValue":"2022"\}, \{"level":4,"propertyValueDependencyId":400,"vidValue":"LE"\}, \{"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"\}] ] \} ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array&lt;int, array&lt;int, array\{vidValue: string, propertyValueDependencyId: string, level: string\}>> |
| `shopCollectItemInfo.translateLanguages` | array&lt;string> | 否 | 说明书需翻译语言列表 |
| `shopCollectItemInfo.goodsModelReqs` | array&lt;object> | 否 | 模特信息列表。requiredGoodsModel 为 true 的类目必填。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举 |
| `shopCollectItemInfo.goodsModelReqs[].modelId` | string | 是 | 模特ID |
| `shopCollectItemInfo.goodsModelReqs[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.goodsModelReqs[].modelName` | string | 是 | 模特名称 |
| `shopCollectItemInfo.goodsModelReqs[].modelType` | string | 是 | 模特类型 |
| `shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 是 | 模特图片URL |
| `shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 是 | 身高（cm） |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 是 | 试穿尺码规格名称 |
| `shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 是 | 试穿结果 |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 是 | 尺码规格ID |
| `shopCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `shopCollectItemInfo.attributes` | array&lt;object> | 是 | 商品属性列表 |
| `shopCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array&lt;object> | 是 | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `shopCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `shopCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `shopCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `shopCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes` | array&lt;object> | 是 | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].values` | array&lt;object> | 是 | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | 服饰类颜色图（服饰类必填） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `shopCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表 |
| `shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array&lt;string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
