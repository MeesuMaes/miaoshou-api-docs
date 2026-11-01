# 添加商品


- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/operate/add_goods`
- 类型：写
- 原文：[479599765e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599765e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsGroupId` | integer | 否 | 商品分组ID |
| `goodsMode` | string | 否 | 商品模式 single(单品) |
| `goodsName` | string | 是 | 商品中文名称 |
| `goodsStatus` | string | 是 | 商品状态：0:停售1:在售2:热销4:新品3:滞销5:清仓 |
| `foreignGoodsName` | string | 否 | 商品外文名称 |
| `marketName` | string | 否 | 采购档口 |
| `staffName` | string | 否 | 采购档口 |
| `goodsGroupName` | string | 否 | 商品分组名称 |
| `invoiceNcm` | string | 否 | 巴西发票NCM编码 |
| `icmsOrigem` | string | 否 | 巴西ICMS原产地编码 |
| `units` | string | 否 | 商品单位 |
| `goodsBrandId` | string | 否 | 商品品牌ID |
| `goodsSkuList` | array&lt;object> | 是 | SKU列表 |
| `goodsSkuList[].goodsSkuId` | integer | 否 | SKU ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsSkuOuterId` | string | 否 | 商品SKU编码 |
| `goodsSkuList[].platformOuterSkuIds` | array&lt;string> | 否 | 平台外部SKU ID列表 |
| `goodsSkuList[].platformSkuIds` | array&lt;string> | 否 | 平台内部SKU ID列表 |
| `goodsSkuList[].skuImgUrl` | string | 否 | SKU图片URL |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价（参考价格） |
| `goodsSkuList[].weight` | string | 否 | 重量(KG) |
| `goodsSkuList[].width` | string | 否 | 宽度 |
| `goodsSkuList[].height` | string | 否 | 高度 |
| `goodsSkuList[].length` | string | 否 | 长度 |
| `goodsSkuList[].goodsSkuBundleList` | array&lt;object> | 否 | 组合品子商品列表（组合品模式） |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuOuterId` | string | 否 | 子商品SKU编码 |
| `goodsSkuList[].goodsSkuBundleList[].goodsName` | string | 否 | 子商品名称 |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuSubName` | string | 否 | 子商品规格名称 |
| `goodsSkuList[].goodsSkuBundleList[].logoUrl` | string | 否 | 子商品图片URL |
| `goodsSkuList[].goodsSkuBundleList[].quantity` | string | 否 | 组合数量 |
| `goodsSkuList[].customsDeclaration` | object | 否 | 报关/清关申报信息 |
| `goodsSkuList[].customsDeclaration.productAttrs` | array&lt;string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
| `goodsSkuList[].customsDeclaration.productSubAttrs` | object | 否 | 各申报属性的详细值 |
| `goodsSkuList[].customsDeclaration.productSubAttrs.withBattery` | string | 否 | 带电报关属性：within_battery弱电，纯电：only_battery |
| `goodsSkuList[].customsDeclaration.productChineseName` | string | 否 | 申报中文名称 |
| `goodsSkuList[].customsDeclaration.productEnglishName` | string | 否 | 申报英文名称 |
| `goodsSkuList[].customsDeclaration.productWeight` | string | 否 | 申报重量(g) |
| `goodsSkuList[].customsDeclaration.productPrice` | string | 否 | 目的国申报金额(USD) |
| `goodsSkuList[].customsDeclaration.exportCountryDeclaredPrice` | string | 否 | 出口国申报金额(USD) |
| `goodsSkuList[].customsDeclaration.productMaterial` | string | 否 | 材质 |
| `goodsSkuList[].customsDeclaration.productPurpose` | string | 否 | 用途 |
| `goodsSkuList[].customsDeclaration.customCode` | string | 否 | 海关编码 |
| `goodsSkuList[].goodsSkuCustomCode` | string | 否 | 商品代码(UPC/ISBN/SN/GTIN) |
| `goodsSkuList[].goodsSkuNote` | string | 否 | SKU备注 |
| `goodsSkuList[].goodsSkuPackagingList` | array&lt;object> | 否 | 包材列表 |
| `goodsSkuList[].goodsSkuPackagingList[].packagingId` | integer | 否 | 包材ID |
| `goodsSkuList[].goodsSkuPackagingList[].packableQuantity` | integer | 否 | 该包材可包装的商品数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsId` | integer | 否 | 商品id |
| `data.goodsSkuIds` | integer | 否 | sku id |
