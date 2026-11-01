# 获取商品SKU列表


- 层级：开放平台 > 仓储 > 商品 > 商品sku
- 方法+路径：`POST /open/v1/ewm/goods/goods_sku/fetch/search_goods_sku_page`
- 类型：读
- 原文：[479599770e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599770e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `groupId` | string | 否 | 分组ID |
| `goodsMode` | string | 是 | 商品类型 single(单规格),bundle(组合) |
| `goodsSkuOuterIds` | array&lt;string> | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuList` | array&lt;object> | 否 | sku列表 |
| `data.goodsSkuList[].goodsSkuId` | string | 否 | 商品SKU ID |
| `data.goodsSkuList[].goodsId` | string | 否 | 商品ID |
| `data.goodsSkuList[].status` | string | 否 | 商品状态 |
| `data.goodsSkuList[].isInWarehouse` | string | 否 | 是否入库 |
| `data.goodsSkuList[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsSkuList[].goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsSkuList[].goodsSkuCustomCode` | string | 否 | 商品编码 |
| `data.goodsSkuList[].goodsSkuCustomBarcode` | string | 否 | 商品条码 |
| `data.goodsSkuList[].appPictureId` | string | 否 | 图片ID |
| `data.goodsSkuList[].logo` | string | 否 | 图片URL |
| `data.goodsSkuList[].logoOssPath` | string | 否 | 图片OSS路径 |
| `data.goodsSkuList[].purchasePrice` | string | 否 | 单价 |
| `data.goodsSkuList[].stockNum` | string | 否 | 库存数量 |
| `data.goodsSkuList[].lockStockNum` | string | 否 | 锁定库存数量 |
| `data.goodsSkuList[].platformItemId` | string | 否 | 平台SKU ID |
| `data.goodsSkuList[].defaultGoodsSupplierId` | string | 否 | 默认供应商ID |
| `data.goodsSkuList[].weight` | string | 否 | 重量 |
| `data.goodsSkuList[].width` | string | 否 | 宽度 |
| `data.goodsSkuList[].height` | string | 否 | 高度 |
| `data.goodsSkuList[].length` | string | 否 | 长度 |
| `data.goodsSkuList[].lastPurchasePrice` | string | 否 | 最近一次购买价格 |
| `data.goodsSkuList[].goodsMode` | string | 否 | 商品模式 |
| `data.goodsSkuList[].goodsSkuNote` | string | 否 | 商品SKU备注 |
| `data.goodsSkuList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsSkuList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsSkuList[].logoUrl` | string | 否 | 图片URL |
| `data.goodsSkuList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsSkuList[].goodsGroupId` | string | 否 | 商品分组ID |
| `data.goodsSkuList[].goodsStatus` | string | 否 | 商品状态 |
| `data.goodsSkuList[].foreignGoodsName` | string | 否 | 商品英文名称 |
| `data.goodsSkuList[].goodsSaleStatus` | string | 否 | 销售状态 |
| `data.goodsSkuList[].isNew` | string | 否 | 是否新品 |
| `data.goodsSkuList[].isStockEmpty` | string | 否 | 是否库存为空 |
| `data.goodsSkuList[].goodsBrandId` | string | 否 | 商品品牌ID |
| `data.goodsSkuList[].units` | string | 否 | 商品单位 |
| `data.goodsSkuList[].goodsGroupName` | string | 否 | 分组名称 |
| `data.goodsSkuList[].goodsGroupBreadcrumb` | string | 否 | 分组路径 |
| `data.goodsSkuList[].supplierList` | array&lt;object> | 否 | 供应商列表 |
| `data.goodsSkuList[].supplierList[].goodsSupplierId` | string | 否 | 供应商id |
| `data.goodsSkuList[].supplierList[].shopName` | string | 否 | 供应商名称 |
| `data.goodsSkuList[].supplierList[].source` | string | 否 | 供应商类型code |
| `data.goodsSkuList[].supplierList[].goodsSupplierGoodsSkuId` | string | 否 | 供应商商品sku id |
| `data.goodsSkuList[].supplierList[].goodsSkuId` | string | 否 | sku id |
| `data.goodsSkuList[].supplierList[].isDefault` | string | 否 | 是否默认供应商 |
| `data.goodsSkuList[].supplierList[].skuSourceUrl` | string | 否 | 货源链接 |
| `data.goodsSkuList[].supplierList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsSkuList[].supplierList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku` | object | 否 | 1688 配对数据 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.ali1688ItemSkuId` | string | 否 | ID |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.sourceItemId` | string | 否 | 1688产品ID |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.sourceSpecId` | string | 否 | 1688规格id |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.sourceSkuId` | string | 否 | 1688skuID |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.imgUrl` | string | 否 | 图片地址 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.attributeDisplayName` | array&lt;string> | 否 | 属性显示名称 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.attributeValue` | array&lt;string> | 否 | 属性值 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.title` | string | 否 | 标题 |
| `data.goodsSkuList[].supplierList[].purchaseRate` | object | 否 | 采购比例（本地商品数量：货源下单数量） |
| `data.goodsSkuList[].supplierList[].purchaseRate.goodsSkuNum` | integer | 否 | 采购比例：商品数量 |
| `data.goodsSkuList[].supplierList[].purchaseRate.sourceNum` | integer | 否 | 采购比例：货源下单数量 |
| `data.goodsSkuList[].goodsAttributeList` | array&lt;object> | 否 | 商品属性列表 |
| `data.goodsSkuList[].goodsAttributeList[].goodsAttributeId` | string | 否 | ID |
| `data.goodsSkuList[].goodsAttributeList[].goodsAttributeValueId` | string | 否 | 值ID |
| `data.goodsSkuList[].goodsAttributeList[].attributeValue` | string | 否 | 属性值名称 |
| `data.goodsSkuList[].goodsAttributeList[].attributeName` | string | 否 | 规格名称 |
| `data.goodsSkuList[].platformOuterSkuIds` | array&lt;string> | 否 | 关联平台SKU |
| `data.goodsSkuList[].platformSkuIds` | array&lt;string> | 否 | 关联的平台SKU Id |
| `data.goodsSkuList[].goodsSkuBundleList` | array&lt;object> | 否 | 子商品信息 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsSkuId` | integer | 否 | 商品skuID |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsId` | integer | 否 | 商品ID |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsGroupId` | integer | 否 | 分组id |
| `data.goodsSkuList[].goodsSkuBundleList[].appAccountId` | integer | 否 | 应用账号ID |
| `data.goodsSkuList[].goodsSkuBundleList[].status` | string | 否 | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsSkuCustomBarcode` | string | 否 | 商品条码 |
| `data.goodsSkuList[].goodsSkuBundleList[].logoOssPath` | string | 否 | 图片地址 |
| `data.goodsSkuList[].goodsSkuBundleList[].purchasePrice` | string | 否 | 单价 |
| `data.goodsSkuList[].goodsSkuBundleList[].stockNum` | string | 否 | 库存数量 |
| `data.goodsSkuList[].goodsSkuBundleList[].lockStockNum` | string | 否 | 预占库存 |
| `data.goodsSkuList[].goodsSkuBundleList[].platformItemId` | string | 否 | 平台商品id |
| `data.goodsSkuList[].goodsSkuBundleList[].defaultGoodsSupplierId` | string | 否 | 默认供应商ID |
| `data.goodsSkuList[].goodsSkuBundleList[].weight` | string | 否 | 重量 |
| `data.goodsSkuList[].goodsSkuBundleList[].width` | string | 否 | 宽度 |
| `data.goodsSkuList[].goodsSkuBundleList[].height` | string | 否 | 高度 |
| `data.goodsSkuList[].goodsSkuBundleList[].length` | string | 否 | 长度 |
| `data.goodsSkuList[].goodsSkuBundleList[].lastPurchasePrice` | string | 否 | 最近采购价 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsMode` | string | 否 | 商品类型 |
| `data.goodsSkuList[].goodsSkuBundleList[].goodsSkuNote` | string | 否 | 商品SKU备注 |
| `data.goodsSkuList[].goodsSkuBundleList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsSkuList[].goodsSkuBundleList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsSkuList[].goodsSkuBundleList[].quantity` | string | 否 | 数量 |
| `data.goodsSkuList[].isExistParentGoodsSku` | string | 否 | 存在父商品 |
| `data.goodsSkuList[].customsDeclaration` | object | 否 | 报关信息 |
| `data.goodsSkuList[].customsDeclaration.productAttrs` | array&lt;string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
| `data.goodsSkuList[].customsDeclaration.productSubAttrs` | object | 否 | 各申报属性的详细值 |
| `data.goodsSkuList[].customsDeclaration.productSubAttrs.withBattery` | string | 否 | 带电报关属性：within_battery弱电，纯电：only_battery |
| `data.goodsSkuList[].customsDeclaration.productChineseName` | string | 否 | 申报中文名称 |
| `data.goodsSkuList[].customsDeclaration.productEnglishName` | string | 否 | 申报英文名称 |
| `data.goodsSkuList[].customsDeclaration.productWeight` | string | 否 | 申报重量(g) |
| `data.goodsSkuList[].customsDeclaration.productPrice` | string | 否 | 目的国申报金额(USD) |
| `data.goodsSkuList[].customsDeclaration.exportCountryDeclaredPrice` | string | 否 | 出口国申报金额(USD) |
| `data.goodsSkuList[].customsDeclaration.productMaterial` | string | 否 | 材质 |
| `data.goodsSkuList[].customsDeclaration.productPurpose` | string | 否 | 用途 |
| `data.goodsSkuList[].customsDeclaration.customCode` | string | 否 | 海关编码 |
| `data.goodsSkuList[].isHavePermissions` | string | 否 | 是否有权限 |
| `data.total` | integer | 否 | 总数 |
