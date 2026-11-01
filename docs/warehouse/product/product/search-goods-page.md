# 获取多规格商品列表


- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/fetch/search_goods_page`
- 类型：读
- 原文：[479599763e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599763e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `goodsSkuOuterIds` | array&lt;string> | 否 | sku |
| `groupId` | string | 否 | 分组ID |
| `itemNum` | array&lt;string> | 否 | SPU |
| `keyword` | string | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsList` | array&lt;object> | 否 |  |
| `data.goodsList[].goodsId` | string | 否 | 商品ID |
| `data.goodsList[].goodsGroupId` | string | 否 | 商品分组ID |
| `data.goodsList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsList[].foreignGoodsName` | string | 否 | 商品英文 |
| `data.goodsList[].goodsType` | string | 否 | 商品类型 |
| `data.goodsList[].goodsMode` | string | 否 | 商品模式 single 单品 |
| `data.goodsList[].goodsBrandId` | string | 否 | 商品品牌ID |
| `data.goodsList[].units` | string | 否 | 商品单位 |
| `data.goodsList[].itemNum` | string | 否 | 商品编号 |
| `data.goodsList[].weight` | string | 否 | 商品重量 |
| `data.goodsList[].width` | string | 否 | 商品宽度 |
| `data.goodsList[].height` | string | 否 | 商品高度 |
| `data.goodsList[].length` | string | 否 | 商品长度 |
| `data.goodsList[].goodsStatus` | string | 否 | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `data.goodsList[].goodsSaleStatus` | string | 否 | 商品销售状态 0普通 1热销 2 滞销 |
| `data.goodsList[].isNew` | string | 否 | 是否新品 |
| `data.goodsList[].isStockEmpty` | string | 否 | 是否库存为空 |
| `data.goodsList[].marketName` | string | 否 | 市场名称 |
| `data.goodsList[].staffName` | string | 否 | 档口名称 |
| `data.goodsList[].invoiceNcm` | string | 否 | 发票NCM |
| `data.goodsList[].icmsOrigem` | string | 否 | 发票-原场地 |
| `data.goodsList[].invoiceNcmDesc` | string | 否 | 发票NCM描述 |
| `data.goodsList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsList[].minGoodsSkuPurchasePrice` | string | 否 | 最小商品SKU采购价 |
| `data.goodsList[].skuList` | array&lt;object> | 否 | SKU列表 |
| `data.goodsList[].skuList[].goodsSkuId` | string | 否 | 商品SKU ID |
| `data.goodsList[].skuList[].goodsId` | string | 否 | 商品ID |
| `data.goodsList[].skuList[].status` | string | 否 | 商品状态 |
| `data.goodsList[].skuList[].isInWarehouse` | string | 否 | 是否入库 |
| `data.goodsList[].skuList[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsList[].skuList[].goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsList[].skuList[].goodsSkuCustomCode` | string | 否 | 商品编码 |
| `data.goodsList[].skuList[].goodsSkuCustomBarcode` | string | 否 | 商品条码 |
| `data.goodsList[].skuList[].appPictureId` | string | 否 | 图片ID |
| `data.goodsList[].skuList[].logo` | string | 否 | 图片URL |
| `data.goodsList[].skuList[].logoOssPath` | string | 否 | 图片OSS路径 |
| `data.goodsList[].skuList[].purchasePrice` | string | 否 | 单价 |
| `data.goodsList[].skuList[].stockNum` | string | 否 | 库存数量 |
| `data.goodsList[].skuList[].lockStockNum` | string | 否 | 锁定库存数量 |
| `data.goodsList[].skuList[].platformItemId` | string | 否 | 平台SKU ID |
| `data.goodsList[].skuList[].defaultGoodsSupplierId` | string | 否 | 默认供应商ID |
| `data.goodsList[].skuList[].weight` | string | 否 | 重量 |
| `data.goodsList[].skuList[].width` | string | 否 | 宽度 |
| `data.goodsList[].skuList[].height` | string | 否 | 高度 |
| `data.goodsList[].skuList[].length` | string | 否 | 长度 |
| `data.goodsList[].skuList[].lastPurchasePrice` | string | 否 | 最近一次购买价格 |
| `data.goodsList[].skuList[].goodsMode` | string | 否 | 商品模式 |
| `data.goodsList[].skuList[].goodsSkuNote` | string | 否 | 商品SKU备注 |
| `data.goodsList[].skuList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsList[].skuList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsList[].skuList[].logoUrl` | string | 否 | 图片URL |
| `data.goodsList[].skuList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsList[].skuList[].goodsGroupId` | string | 否 | 商品分组ID |
| `data.goodsList[].skuList[].goodsStatus` | string | 否 | 商品状态 |
| `data.goodsList[].skuList[].foreignGoodsName` | string | 否 | 商品英文名称 |
| `data.goodsList[].skuList[].goodsSaleStatus` | string | 否 | 销售状态 |
| `data.goodsList[].skuList[].isNew` | string | 否 | 是否新品 |
| `data.goodsList[].skuList[].isStockEmpty` | string | 否 | 是否库存为空 |
| `data.goodsList[].skuList[].goodsBrandId` | string | 否 | 商品品牌ID |
| `data.goodsList[].skuList[].units` | string | 否 | 商品单位 |
| `data.goodsList[].skuList[].goodsGroupName` | string | 否 | 分组名称 |
| `data.goodsList[].skuList[].goodsGroupBreadcrumb` | string | 否 | 分组路径 |
| `data.goodsList[].skuList[].supplierList` | array&lt;object> | 否 | 供应商列表 |
| `data.goodsList[].skuList[].supplierList[].goodsSupplierId` | string | 否 | 供应商id |
| `data.goodsList[].skuList[].supplierList[].shopName` | string | 否 | 供应商名称 |
| `data.goodsList[].skuList[].supplierList[].source` | string | 否 | 供应商类型code |
| `data.goodsList[].skuList[].supplierList[].goodsSupplierGoodsSkuId` | string | 否 | 供应商商品sku id |
| `data.goodsList[].skuList[].supplierList[].goodsSkuId` | string | 否 | sku id |
| `data.goodsList[].skuList[].supplierList[].isDefault` | string | 否 | 是否默认供应商 |
| `data.goodsList[].skuList[].supplierList[].skuSourceUrl` | string | 否 | 货源链接 |
| `data.goodsList[].skuList[].supplierList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsList[].skuList[].supplierList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsList[].skuList[].supplierList[].ali1688ItemSku` | object | 否 | 1688 配对数据 |
| `data.goodsList[].skuList[].supplierList[].purchaseRate` | object | 否 | 采购比例（本地商品数量：货源下单数量） |
| `data.goodsList[].skuList[].goodsAttributeList` | array&lt;object> | 否 | 商品属性列表 |
| `data.goodsList[].skuList[].goodsAttributeList[].goodsAttributeId` | string | 否 | ID |
| `data.goodsList[].skuList[].goodsAttributeList[].goodsAttributeValueId` | string | 否 | 值ID |
| `data.goodsList[].skuList[].goodsAttributeList[].attributeValue` | string | 否 | 属性值名称 |
| `data.goodsList[].skuList[].goodsAttributeList[].attributeName` | string | 否 | 规格名称 |
| `data.goodsList[].skuList[].platformOuterSkuIds` | array&lt;string> | 否 | 关联平台SKU |
| `data.goodsList[].skuList[].platformSkuIds` | array&lt;string> | 否 | 关联的平台SKU Id |
| `data.goodsList[].skuList[].goodsSkuBundleList` | array&lt;object> | 否 | 子商品信息 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsSkuId` | integer | 否 | 商品skuID |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsId` | integer | 否 | 商品ID |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsGroupId` | integer | 否 | 分组id |
| `data.goodsList[].skuList[].goodsSkuBundleList[].appAccountId` | integer | 否 | 应用账号ID |
| `data.goodsList[].skuList[].goodsSkuBundleList[].status` | string | 否 | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsSkuCustomBarcode` | string | 否 | 商品条码 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].logoOssPath` | string | 否 | 图片地址 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].purchasePrice` | string | 否 | 单价 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].stockNum` | string | 否 | 库存数量 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].lockStockNum` | string | 否 | 预占库存 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].platformItemId` | string | 否 | 平台商品id |
| `data.goodsList[].skuList[].goodsSkuBundleList[].defaultGoodsSupplierId` | string | 否 | 默认供应商ID |
| `data.goodsList[].skuList[].goodsSkuBundleList[].weight` | string | 否 | 重量 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].width` | string | 否 | 宽度 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].height` | string | 否 | 高度 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].length` | string | 否 | 长度 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].lastPurchasePrice` | string | 否 | 最近采购价 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsMode` | string | 否 | 商品类型 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].goodsSkuNote` | string | 否 | 商品SKU备注 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsList[].skuList[].goodsSkuBundleList[].quantity` | string | 否 | 数量 |
| `data.goodsList[].skuList[].isExistParentGoodsSku` | string | 否 | 存在父商品 |
| `data.goodsList[].skuList[].customsDeclaration` | object | 否 | 报关信息 |
| `data.goodsList[].skuList[].customsDeclaration.productAttrs` | array&lt;string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
| `data.goodsList[].skuList[].customsDeclaration.productSubAttrs` | object | 否 | 各申报属性的详细值 |
| `data.goodsList[].skuList[].customsDeclaration.productChineseName` | string | 否 | 申报中文名称 |
| `data.goodsList[].skuList[].customsDeclaration.productEnglishName` | string | 否 | 申报英文名称 |
| `data.goodsList[].skuList[].customsDeclaration.productWeight` | string | 否 | 申报重量(g) |
| `data.goodsList[].skuList[].customsDeclaration.productPrice` | string | 否 | 目的国申报金额(USD) |
| `data.goodsList[].skuList[].customsDeclaration.exportCountryDeclaredPrice` | string | 否 | 出口国申报金额(USD) |
| `data.goodsList[].skuList[].customsDeclaration.productMaterial` | string | 否 | 材质 |
| `data.goodsList[].skuList[].customsDeclaration.productPurpose` | string | 否 | 用途 |
| `data.goodsList[].skuList[].customsDeclaration.customCode` | string | 否 | 海关编码 |
| `data.goodsList[].skuList[].isHavePermissions` | string | 否 | 是否有权限 |
| `data.goodsList[].goodsGroupName` | string | 否 | 商品分组名称 |
| `data.goodsList[].goodsGroupBreadcrumb` | string | 否 | 商品分组名称 |
| `data.goodsList[].goodsPackagingList` | array&lt;object> | 否 | 商品包装列表 |
| `data.goodsList[].goodsPackagingList[].packagingId` | integer | 否 | 包材id |
| `data.goodsList[].goodsPackagingList[].packableQuantity` | integer | 否 | 包材可包装数量 |
