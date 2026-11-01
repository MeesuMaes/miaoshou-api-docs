# 保存采集箱店铺模式详情


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/save_shop_collect_item_info`
- 类型：写
- 原文：[477347605e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347605e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

其他参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `timerToken(query)` | string | 否 |  |
| `Cookie(header)` | string | 否 |  |
| `X-Apifox-Debug(header)` | string | 否 |  |


**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.detailId` | integer | 是 | 采集箱详情ID |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `shopCollectItemInfo.imgUrls` | array&lt;string> | 是 | 类轮播图 |
| `shopCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `shopCollectItemInfo.goodsLayerDecorationReqs` | array&lt;object> | 是 | 产品描述 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
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
| `shopCollectItemInfo.site` | string | 否 | 站点（pddkjChoice 半托目前只有 sitePddKjChoice） |
| `shopCollectItemInfo.editModel` | string | 是 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `shopCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
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
| `shopCollectItemInfo.vehicleLibraryRelationList` | array&lt;object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表 |
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
| `shopCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `shopCollectItemInfo.publishSiteList` | array&lt;string> | 否 | 发布站点列表，pddkjChoice 必填，不能为空 |
| `shopCollectItemInfo.publishEuSiteList` | array&lt;string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `shopCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `shopCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型 |
| `shopCollectItemInfo.materialMultiLanguages` | array&lt;string> | 否 | 多语言素材语言列表 |
| `shopCollectItemInfo.isSetSitePrice` | integer | 否 | 是否设置了站点价格 |
| `shopCollectItemInfo.isSetSiteStock` | integer | 否 | 是否设置了站点库存 |
| `shopCollectItemInfo.shipmentLimitDay` | integer | 否 | 其他站点承诺发货时效 非定制品可选值只有 1,2 |
| `shopCollectItemInfo.siteFreightTemplateList` | array&lt;object> | 否 | 按站点维度的运费模板列表 |
| `shopCollectItemInfo.siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `shopCollectItemInfo.siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `shopCollectItemInfo.siteWarehouseList` | array&lt;object> | 否 | 按站点维度的仓库列表，EU 站点下还包含 subSiteWarehouseList（欧盟子站点仓库列表） |
| `shopCollectItemInfo.siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `shopCollectItemInfo.siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，非 EU 站点时必填 |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList` | array&lt;object> | 否 | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array&lt;string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
