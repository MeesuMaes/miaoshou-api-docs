# 创建采集箱商品


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/create_collect_box_item`
- 类型：写
- 原文：[471545322e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545322e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 SiteCollectItemInfoForSaveRo 注释。 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array&lt;object> | 是 | 店铺列表，保存站点模式必填。 保存时会校验每个店铺的存在性、运费模板、仓库配置； 每个子项的 shopId 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.itemNum` | string | 否 | 货号 |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array&lt;object> | 否 | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.imgUrls` | array&lt;string> | 是 | 轮播图 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版，2=套版） |
| `siteCollectItemInfo.basePlateSkuKey` | string | 否 | 底版 SKU Key |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状，取值参考 getItemOptions 接口返回的 outerPackageShapeOptions |
| `siteCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型，取值参考 getItemOptions 接口返回的 outerPackageTypeOptions |
| `siteCollectItemInfo.outerPackageImgUrls` | array&lt;string> | 是 | 外包装图片URL列表 |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array&lt;object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer | 否 | 字体大小 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string | 否 | 字体粗细 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string | 否 | 对齐方式 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string | 否 | 字体颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string | 否 | 背景颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer | 否 | 字体族 |
| `siteCollectItemInfo.productGuideFileUrl` | string | 否 | 产品说明书URL |
| `siteCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array&lt;string> | 否 | 展示尺码模板ID列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.sizeCharts` | array&lt;object> | 否 | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array&lt;integer> | 否 | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array&lt;integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array&lt;object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array&lt;object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array&lt;object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array&lt;object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ \{ "vehicleLibraryId": 1, "productPropValueDependencyList": [ [\{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"\}, \{"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"\}, \{"level":3,"propertyValueDependencyId":300,"vidValue":"2022"\}, \{"level":4,"propertyValueDependencyId":400,"vidValue":"LE"\}, \{"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"\}] ] \} ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array&lt;int, array&lt;int, array\{vidValue: string, propertyValueDependencyId: string, level: string\}>> |
| `siteCollectItemInfo.attributes` | array&lt;object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array&lt;object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array&lt;object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array&lt;object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写 |
| `siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array&lt;string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 创建成功的采集箱详情ID |
