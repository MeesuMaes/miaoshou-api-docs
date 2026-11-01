# 全球产品详情（返回官方


- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/get_item_detail`
- 类型：读
- 原文：[480434402e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434402e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemId` | string | 是 | 平台产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemInfo` | object | 否 | 全球商品详情 |
| `data.itemInfo.globalItemId` | integer | 是 | Shopee 全球商品唯一标识 |
| `data.itemInfo.globalItemName` | string | 否 | 全球商品名称 |
| `data.itemInfo.description` | string | 否 | 全球商品描述 |
| `data.itemInfo.globalItemSku` | string | 否 | 全球商品 SKU |
| `data.itemInfo.globalItemStatus` | string | 否 | 商品状态（NORMAL） |
| `data.itemInfo.createTime` | integer | 否 | 创建时间戳 |
| `data.itemInfo.updateTime` | integer | 否 | 更新时间戳 |
| `data.itemInfo.stockInfo` | array&lt;object> | 否 | 库存信息（无规格时返回） |
| `data.itemInfo.stockInfo[].stockType` | integer | 否 | 库存类型 |
| `data.itemInfo.stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `data.itemInfo.stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `data.itemInfo.stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `data.itemInfo.priceInfo` | array&lt;object> | 否 | 价格信息（无规格时返回） |
| `data.itemInfo.priceInfo[].currency` | string | 否 | 币种 |
| `data.itemInfo.priceInfo[].originalPrice` | number | 否 | 原价 |
| `data.itemInfo.priceInfo[].sipItemPrice` | number | 否 | SIP 商品价格 |
| `data.itemInfo.priceInfo[].sipItemPriceSource` | string | 否 | SIP 价格来源（auto / manual） |
| `data.itemInfo.image` | object | 否 | 图片信息 |
| `data.itemInfo.image.imageIdList` | array&lt;string> | 是 | 图片 ID 列表 |
| `data.itemInfo.image.imageUrlList` | array&lt;string> | 否 | 图片 URL 列表 |
| `data.itemInfo.weight` | string | 否 | 重量，单位 KG |
| `data.itemInfo.dimension` | object | 否 | 包裹尺寸 |
| `data.itemInfo.dimension.packageLength` | integer | 否 | 包裹长度，单位 CM |
| `data.itemInfo.dimension.packageWidth` | integer | 否 | 包裹宽度，单位 CM |
| `data.itemInfo.dimension.packageHeight` | integer | 否 | 包裹高度，单位 CM |
| `data.itemInfo.preOrder` | object | 否 | 预售信息 |
| `data.itemInfo.preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `data.itemInfo.sizeChart` | string | 否 | 尺码表图片 URL |
| `data.itemInfo.condition` | string | 否 | 是否二手（NEW / USED） |
| `data.itemInfo.hasModel` | boolean | 否 | 是否包含规格 |
| `data.itemInfo.video` | array&lt;object> | 否 | 视频信息(获取商品详情时此字段有值, 编辑时此字段无效) |
| `data.itemInfo.video[].videoUrl` | string | 否 | 视频 URL |
| `data.itemInfo.video[].thumbnailUrl` | string | 否 | 视频缩略图 URL |
| `data.itemInfo.video[].duration` | integer | 否 | 视频时长，单位秒 |
| `data.itemInfo.videoUploadId` | string | 否 | 视频ID (通过上传视频接口获取，编辑商品时此字段用于更新商品视频) |
| `data.itemInfo.categoryId` | integer | 否 | 分类 ID |
| `data.itemInfo.brand` | object | 否 | 品牌信息 |
| `data.itemInfo.brand.brandId` | integer | 否 | 品牌 ID |
| `data.itemInfo.brand.originalBrandName` | string | 否 | 品牌原始名称 |
| `data.itemInfo.attributeList` | array&lt;object> | 否 | 属性列表 |
| `data.itemInfo.attributeList[].attributeId` | integer | 否 | 属性 ID |
| `data.itemInfo.attributeList[].originalAttributeName` | string | 否 | 属性名称 |
| `data.itemInfo.attributeList[].attributeValueList` | array&lt;object> | 否 | 属性值列表 |
| `data.itemInfo.attributeList[].attributeValueList[].valueId` | integer | 否 | 属性值 ID |
| `data.itemInfo.attributeList[].attributeValueList[].originalValueName` | string | 否 | 属性值名称 |
| `data.itemInfo.attributeList[].attributeValueList[].valueUnit` | string | 否 | 属性值单位 |
| `data.itemInfo.descriptionInfo` | object | 否 | 新版描述信息 |
| `data.itemInfo.descriptionInfo.extendedDescription` | object | 否 | 扩展描述 |
| `data.itemInfo.descriptionInfo.extendedDescription.fieldList` | array&lt;object> | 否 | 扩展描述字段列表 |
| `data.itemInfo.descriptionInfo.descriptionType` | string | 否 | 描述类型：normal / extended |
| `data.itemInfo.isFulfillmentByShopee` | boolean | 否 | 是否为 Shopee 履约商品 |
| `data.itemInfo.sizeChartId` | integer | 否 | 尺码表模板 ID |
| `data.modelList` | object | 否 | 全球规格列表 |
| `data.modelList.tierVariation` | array&lt;object> | 否 | 层级规格信息 |
| `data.modelList.tierVariation[].name` | string | 否 | 层级规格名称 |
| `data.modelList.tierVariation[].optionList` | array&lt;object> | 否 | 层级规格选项列表 |
| `data.modelList.tierVariation[].optionList[].option` | string | 否 | 层级规格选项值 |
| `data.modelList.tierVariation[].image` | object | 否 | 层级规格图片 |
| `data.modelList.tierVariation[].image.imageUrl` | string | 否 | 图片 URL |
| `data.modelList.tierVariation[].image.imageId` | string | 否 | 图片 ID |
| `data.modelList.globalModel` | array&lt;object> | 否 | 全球规格列表(SKU列表) |
| `data.modelList.globalModel[].globalModelId` | integer | 否 | 全球规格 ID |
| `data.modelList.globalModel[].globalModelSku` | string | 否 | 全球规格 SKU |
| `data.modelList.globalModel[].priceInfo` | object | 否 | 价格信息 |
| `data.modelList.globalModel[].priceInfo.originalPrice` | number | 否 | 原价 |
| `data.modelList.globalModel[].stockInfo` | array&lt;object> | 否 | 库存信息 |
| `data.modelList.globalModel[].stockInfo[].stockType` | integer | 否 | 库存类型：1 = WMS 在库，2 = 卖家在库 |
| `data.modelList.globalModel[].stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `data.modelList.globalModel[].stockInfo[].currentStock` | integer | 否 | 当前库存 |
| `data.modelList.globalModel[].stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `data.modelList.globalModel[].stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `data.modelList.globalModel[].tierIndex` | array&lt;integer> | 否 | 层级索引 |
| `data.modelList.globalModel[].weight` | string | 否 | 重量，单位 KG |
| `data.modelList.globalModel[].dimension` | object | 否 | 包裹尺寸 |
| `data.modelList.globalModel[].dimension.packageHeight` | integer | 是 | 包裹高度，单位 CM |
| `data.modelList.globalModel[].dimension.packageLength` | integer | 是 | 包裹长度，单位 CM |
| `data.modelList.globalModel[].dimension.packageWidth` | integer | 是 | 包裹宽度，单位 CM |
| `data.modelList.globalModel[].preOrder` | object | 否 | 预售信息 |
| `data.modelList.globalModel[].preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `data.modelList.globalModel[].isFulfillmentByShopee` | boolean | 否 | 是否为 FBS 规格 |
| `data.modelList.standardiseTierVariation` | array&lt;object> | 否 | 标准化层级规格信息 |
| `data.modelList.standardiseTierVariation[].variationId` | integer | 否 | 标准化层级规格 ID |
| `data.modelList.standardiseTierVariation[].variationName` | string | 否 | 标准化层级规格名称 |
| `data.modelList.standardiseTierVariation[].variationGroupId` | integer | 否 | 标准化层级规格组 ID |
| `data.modelList.standardiseTierVariation[].variationOptionList` | array&lt;object> | 否 | 标准化层级规格选项列表 |
| `data.modelList.standardiseTierVariation[].variationOptionList[].variationOptionId` | integer | 否 | 标准化层级规格选项 ID |
| `data.modelList.standardiseTierVariation[].variationOptionList[].variationOptionName` | string | 否 | 标准化层级规格选项名称 |
| `data.modelList.standardiseTierVariation[].imageId` | string | 否 | 图片 ID |
| `data.modelList.standardiseTierVariation[].imageUrl` | string | 否 | 图片 URL |
