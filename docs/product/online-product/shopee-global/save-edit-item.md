# 保存产品编辑


- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/save_edit_item`
- 类型：写
- 原文：[480434403e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434403e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `itemInfo` | object | 是 | 全球商品详情（前端修改后的 GetItemDetailVo.itemInfo，仅传新数据） |
| `itemInfo.globalItemId` | integer | 是 | Shopee 全球商品唯一标识 |
| `itemInfo.globalItemName` | string | 否 | 全球商品名称 |
| `itemInfo.description` | string | 否 | 全球商品描述 |
| `itemInfo.globalItemSku` | string | 否 | 全球商品 SKU |
| `itemInfo.globalItemStatus` | string | 否 | 商品状态（NORMAL） |
| `itemInfo.createTime` | integer | 否 | 创建时间戳 |
| `itemInfo.updateTime` | integer | 否 | 更新时间戳 |
| `itemInfo.stockInfo` | array&lt;object> | 否 | 库存信息（无规格时返回） |
| `itemInfo.stockInfo[].stockType` | integer | 否 | 库存类型 |
| `itemInfo.stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `itemInfo.stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `itemInfo.stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `itemInfo.priceInfo` | array&lt;object> | 否 | 价格信息（无规格时返回） |
| `itemInfo.priceInfo[].currency` | string | 否 | 币种 |
| `itemInfo.priceInfo[].originalPrice` | number | 否 | 原价 |
| `itemInfo.priceInfo[].sipItemPrice` | number | 否 | SIP 商品价格 |
| `itemInfo.priceInfo[].sipItemPriceSource` | string | 否 | SIP 价格来源（auto / manual） |
| `itemInfo.image` | object | 否 | 图片信息 |
| `itemInfo.image.imageIdList` | array&lt;string> | 是 | 图片 ID 列表 |
| `itemInfo.image.imageUrlList` | array&lt;string> | 否 | 图片 URL 列表 |
| `itemInfo.weight` | string | 否 | 重量，单位 KG |
| `itemInfo.dimension` | object | 否 | 包裹尺寸 |
| `itemInfo.dimension.packageLength` | integer | 否 | 包裹长度，单位 CM |
| `itemInfo.dimension.packageWidth` | integer | 否 | 包裹宽度，单位 CM |
| `itemInfo.dimension.packageHeight` | integer | 否 | 包裹高度，单位 CM |
| `itemInfo.preOrder` | object | 否 | 预售信息 |
| `itemInfo.preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `itemInfo.sizeChart` | string | 否 | 尺码表图片 URL |
| `itemInfo.condition` | string | 否 | 是否二手（NEW / USED） |
| `itemInfo.hasModel` | boolean | 否 | 是否包含规格 |
| `itemInfo.video` | array&lt;object> | 否 | 视频信息(获取商品详情时此字段有值, 编辑时此字段无效) |
| `itemInfo.video[].videoUrl` | string | 否 | 视频 URL |
| `itemInfo.video[].thumbnailUrl` | string | 否 | 视频缩略图 URL |
| `itemInfo.video[].duration` | integer | 否 | 视频时长，单位秒 |
| `itemInfo.videoUploadId` | string | 否 | 视频ID (通过上传视频接口获取，编辑商品时此字段用于更新商品视频) |
| `itemInfo.categoryId` | integer | 否 | 分类 ID |
| `itemInfo.brand` | object | 否 | 品牌信息 |
| `itemInfo.brand.brandId` | integer | 否 | 品牌 ID |
| `itemInfo.brand.originalBrandName` | string | 否 | 品牌原始名称 |
| `itemInfo.attributeList` | array&lt;object> | 否 | 属性列表 |
| `itemInfo.attributeList[].attributeId` | integer | 否 | 属性 ID |
| `itemInfo.attributeList[].originalAttributeName` | string | 否 | 属性名称 |
| `itemInfo.attributeList[].attributeValueList` | array&lt;object> | 否 | 属性值列表 |
| `itemInfo.attributeList[].attributeValueList[].valueId` | integer | 否 | 属性值 ID |
| `itemInfo.attributeList[].attributeValueList[].originalValueName` | string | 否 | 属性值名称 |
| `itemInfo.attributeList[].attributeValueList[].valueUnit` | string | 否 | 属性值单位 |
| `itemInfo.descriptionInfo` | object | 否 | 新版描述信息 |
| `itemInfo.descriptionInfo.extendedDescription` | object | 否 | 扩展描述 |
| `itemInfo.descriptionInfo.extendedDescription.fieldList` | array&lt;object> | 否 | 扩展描述字段列表 |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].fieldType` | string | 否 | 字段类型：text / image |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].text` | string | 否 | 文本内容（field_type 为 text 时返回） |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo` | object | 否 | 图片信息（field_type 为 image 时返回） |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo.imageId` | string | 否 | 图片 ID |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo.imageUrl` | string | 否 | 图片 URL |
| `itemInfo.descriptionInfo.descriptionType` | string | 否 | 描述类型：normal / extended |
| `itemInfo.isFulfillmentByShopee` | boolean | 否 | 是否为 Shopee 履约商品 |
| `itemInfo.sizeChartId` | integer | 否 | 尺码表模板 ID |
| `modelList` | object | 否 | 全球规格列表（前端修改后的 GetItemDetailVo.modelList，仅传新数据） |
| `modelList.tierVariation` | array&lt;object> | 否 | 层级规格信息 |
| `modelList.tierVariation[].name` | string | 否 | 层级规格名称 |
| `modelList.tierVariation[].optionList` | array&lt;object> | 否 | 层级规格选项列表 |
| `modelList.tierVariation[].optionList[].option` | string | 否 | 层级规格选项值 |
| `modelList.tierVariation[].image` | object | 否 | 层级规格图片 |
| `modelList.tierVariation[].image.imageUrl` | string | 否 | 图片 URL |
| `modelList.tierVariation[].image.imageId` | string | 否 | 图片 ID |
| `modelList.globalModel` | array&lt;object> | 否 | 全球规格列表(SKU列表) |
| `modelList.globalModel[].globalModelId` | integer | 否 | 全球规格 ID |
| `modelList.globalModel[].globalModelSku` | string | 否 | 全球规格 SKU |
| `modelList.globalModel[].priceInfo` | object | 否 | 价格信息 |
| `modelList.globalModel[].priceInfo.originalPrice` | number | 否 | 原价 |
| `modelList.globalModel[].stockInfo` | array&lt;object> | 否 | 库存信息 |
| `modelList.globalModel[].stockInfo[].stockType` | integer | 否 | 库存类型：1 = WMS 在库，2 = 卖家在库 |
| `modelList.globalModel[].stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `modelList.globalModel[].stockInfo[].currentStock` | integer | 否 | 当前库存 |
| `modelList.globalModel[].stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `modelList.globalModel[].stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `modelList.globalModel[].tierIndex` | array&lt;integer> | 否 | 层级索引 |
| `modelList.globalModel[].weight` | string | 否 | 重量，单位 KG |
| `modelList.globalModel[].dimension` | object | 否 | 包裹尺寸 |
| `modelList.globalModel[].dimension.packageHeight` | integer | 是 | 包裹高度，单位 CM |
| `modelList.globalModel[].dimension.packageLength` | integer | 是 | 包裹长度，单位 CM |
| `modelList.globalModel[].dimension.packageWidth` | integer | 是 | 包裹宽度，单位 CM |
| `modelList.globalModel[].preOrder` | object | 否 | 预售信息 |
| `modelList.globalModel[].preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `modelList.globalModel[].isFulfillmentByShopee` | boolean | 否 | 是否为 FBS 规格 |
| `modelList.standardiseTierVariation` | array&lt;object> | 否 | 标准化层级规格信息 |
| `modelList.standardiseTierVariation[].variationId` | integer | 否 | 标准化层级规格 ID |
| `modelList.standardiseTierVariation[].variationName` | string | 否 | 标准化层级规格名称 |
| `modelList.standardiseTierVariation[].variationGroupId` | integer | 否 | 标准化层级规格组 ID |
| `modelList.standardiseTierVariation[].variationOptionList` | array&lt;object> | 否 | 标准化层级规格选项列表 |
| `modelList.standardiseTierVariation[].variationOptionList[].variationOptionId` | integer | 否 | 标准化层级规格选项 ID |
| `modelList.standardiseTierVariation[].variationOptionList[].variationOptionName` | string | 否 | 标准化层级规格选项名称 |
| `modelList.standardiseTierVariation[].imageId` | string | 否 | 图片 ID |
| `modelList.standardiseTierVariation[].imageUrl` | string | 否 | 图片 URL |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
