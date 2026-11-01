# 获取商品详情


- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/fetch/get_goods_info`
- 类型：读
- 原文：[479599764e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599764e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsId` | integer | 是 | 商品id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsDetail` | object | 否 |  |
| `data.goodsDetail.goodsId` | string | 否 | 商品ID |
| `data.goodsDetail.goodsGroupId` | string | 否 | 商品分组ID |
| `data.goodsDetail.goodsName` | string | 否 | 商品名称 |
| `data.goodsDetail.foreignGoodsName` | string | 否 | 商品英文 |
| `data.goodsDetail.goodsType` | string | 否 | 商品类型 |
| `data.goodsDetail.goodsMode` | string | 否 | 商品模式 single 单品 |
| `data.goodsDetail.goodsBrandId` | string | 否 | 商品品牌ID |
| `data.goodsDetail.units` | string | 否 | 商品单位 |
| `data.goodsDetail.itemNum` | string | 否 | 商品编号 |
| `data.goodsDetail.weight` | string | 否 | 商品重量 |
| `data.goodsDetail.width` | string | 否 | 商品宽度 |
| `data.goodsDetail.height` | string | 否 | 商品高度 |
| `data.goodsDetail.length` | string | 否 | 商品长度 |
| `data.goodsDetail.goodsStatus` | string | 否 | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `data.goodsDetail.goodsSaleStatus` | string | 否 | 商品销售状态 0普通 1热销 2 滞销 |
| `data.goodsDetail.isNew` | string | 否 | 是否新品 |
| `data.goodsDetail.isStockEmpty` | string | 否 | 是否库存为空 |
| `data.goodsDetail.marketName` | string | 否 | 市场名称 |
| `data.goodsDetail.staffName` | string | 否 | 档口名称 |
| `data.goodsDetail.invoiceNcm` | string | 否 | 发票NCM |
| `data.goodsDetail.icmsOrigem` | string | 否 | 发票-原场地 |
| `data.goodsDetail.invoiceNcmDesc` | string | 否 | 发票NCM描述 |
| `data.goodsDetail.gmtCreate` | string | 否 | 创建时间 |
| `data.goodsDetail.gmtModified` | string | 否 | 修改时间 |
| `data.goodsDetail.minGoodsSkuPurchasePrice` | string | 否 | 最小商品SKU采购价 |
| `data.goodsDetail.skuList` | array&lt;object> | 否 | SKU列表 |
| `data.goodsDetail.skuList[].goodsSkuId` | string | 否 | 商品SKU ID |
| `data.goodsDetail.skuList[].goodsId` | string | 否 | 商品ID |
| `data.goodsDetail.skuList[].status` | string | 否 | 商品状态 |
| `data.goodsDetail.skuList[].isInWarehouse` | string | 否 | 是否入库 |
| `data.goodsDetail.skuList[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsDetail.skuList[].goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsDetail.skuList[].goodsSkuCustomCode` | string | 否 | 商品编码 |
| `data.goodsDetail.skuList[].goodsSkuCustomBarcode` | string | 否 | 商品条码 |
| `data.goodsDetail.skuList[].appPictureId` | string | 否 | 图片ID |
| `data.goodsDetail.skuList[].logo` | string | 否 | 图片URL |
| `data.goodsDetail.skuList[].logoOssPath` | string | 否 | 图片OSS路径 |
| `data.goodsDetail.skuList[].purchasePrice` | string | 否 | 单价 |
| `data.goodsDetail.skuList[].stockNum` | string | 否 | 库存数量 |
| `data.goodsDetail.skuList[].lockStockNum` | string | 否 | 锁定库存数量 |
| `data.goodsDetail.skuList[].platformItemId` | string | 否 | 平台SKU ID |
| `data.goodsDetail.skuList[].defaultGoodsSupplierId` | string | 否 | 默认供应商ID |
| `data.goodsDetail.skuList[].weight` | string | 否 | 重量 |
| `data.goodsDetail.skuList[].width` | string | 否 | 宽度 |
| `data.goodsDetail.skuList[].height` | string | 否 | 高度 |
| `data.goodsDetail.skuList[].length` | string | 否 | 长度 |
| `data.goodsDetail.skuList[].lastPurchasePrice` | string | 否 | 最近一次购买价格 |
| `data.goodsDetail.skuList[].goodsMode` | string | 否 | 商品模式 |
| `data.goodsDetail.skuList[].goodsSkuNote` | string | 否 | 商品SKU备注 |
| `data.goodsDetail.skuList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsDetail.skuList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsDetail.skuList[].logoUrl` | string | 否 | 图片URL |
| `data.goodsDetail.skuList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsDetail.skuList[].goodsGroupId` | string | 否 | 商品分组ID |
| `data.goodsDetail.skuList[].goodsStatus` | string | 否 | 商品状态 |
| `data.goodsDetail.skuList[].foreignGoodsName` | string | 否 | 商品英文名称 |
| `data.goodsDetail.skuList[].goodsSaleStatus` | string | 否 | 销售状态 |
| `data.goodsDetail.skuList[].isNew` | string | 否 | 是否新品 |
| `data.goodsDetail.skuList[].isStockEmpty` | string | 否 | 是否库存为空 |
| `data.goodsDetail.skuList[].goodsBrandId` | string | 否 | 商品品牌ID |
| `data.goodsDetail.skuList[].units` | string | 否 | 商品单位 |
| `data.goodsDetail.skuList[].goodsGroupName` | string | 否 | 分组名称 |
| `data.goodsDetail.skuList[].goodsGroupBreadcrumb` | string | 否 | 分组路径 |
| `data.goodsDetail.skuList[].supplierList` | array&lt;object> | 否 | 供应商列表 |
| `data.goodsDetail.skuList[].supplierList[].goodsSupplierId` | string | 否 | 供应商id |
| `data.goodsDetail.skuList[].supplierList[].shopName` | string | 否 | 供应商名称 |
| `data.goodsDetail.skuList[].supplierList[].source` | string | 否 | 供应商类型code |
| `data.goodsDetail.skuList[].supplierList[].goodsSupplierGoodsSkuId` | string | 否 | 供应商商品sku id |
| `data.goodsDetail.skuList[].supplierList[].goodsSkuId` | string | 否 | sku id |
| `data.goodsDetail.skuList[].supplierList[].isDefault` | string | 否 | 是否默认供应商 |
| `data.goodsDetail.skuList[].supplierList[].skuSourceUrl` | string | 否 | 货源链接 |
| `data.goodsDetail.skuList[].supplierList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsDetail.skuList[].supplierList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsDetail.skuList[].supplierList[].ali1688ItemSku` | object | 否 | 1688 配对数据 |
| `data.goodsDetail.skuList[].supplierList[].purchaseRate` | object | 否 | 采购比例（本地商品数量：货源下单数量） |
| `data.goodsDetail.skuList[].goodsAttributeList` | array&lt;object> | 否 | 商品属性列表 |
| `data.goodsDetail.skuList[].goodsAttributeList[].goodsAttributeId` | string | 否 | ID |
| `data.goodsDetail.skuList[].goodsAttributeList[].goodsAttributeValueId` | string | 否 | 值ID |
| `data.goodsDetail.skuList[].goodsAttributeList[].attributeValue` | string | 否 | 属性值名称 |
| `data.goodsDetail.skuList[].goodsAttributeList[].attributeName` | string | 否 | 规格名称 |
| `data.goodsDetail.skuList[].platformOuterSkuIds` | array&lt;string> | 否 | 关联平台SKU |
| `data.goodsDetail.skuList[].platformSkuIds` | array&lt;string> | 否 | 关联的平台SKU Id |
| `data.goodsDetail.skuList[].goodsSkuBundleList` | array&lt;object> | 否 | 子商品信息 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsSkuId` | integer | 否 | 商品skuID |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsId` | integer | 否 | 商品ID |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsGroupId` | integer | 否 | 分组id |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].appAccountId` | integer | 否 | 应用账号ID |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].status` | string | 否 | 商品状态 1:在售 2:热销 4:新品 3:滞销 5:清仓 0:停售 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsSkuCustomBarcode` | string | 否 | 商品条码 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].logoOssPath` | string | 否 | 图片地址 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].purchasePrice` | string | 否 | 单价 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].stockNum` | string | 否 | 库存数量 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].lockStockNum` | string | 否 | 预占库存 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].platformItemId` | string | 否 | 平台商品id |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].defaultGoodsSupplierId` | string | 否 | 默认供应商ID |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].weight` | string | 否 | 重量 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].width` | string | 否 | 宽度 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].height` | string | 否 | 高度 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].length` | string | 否 | 长度 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].lastPurchasePrice` | string | 否 | 最近采购价 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsMode` | string | 否 | 商品类型 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].goodsSkuNote` | string | 否 | 商品SKU备注 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].gmtModified` | string | 否 | 修改时间 |
| `data.goodsDetail.skuList[].goodsSkuBundleList[].quantity` | string | 否 | 数量 |
| `data.goodsDetail.skuList[].goodsSkuPackagingList` | array&lt;object> | 否 |  |
| `data.goodsDetail.skuList[].goodsSkuPackagingList[].packagingId` | integer | 否 | 包材id |
| `data.goodsDetail.skuList[].goodsSkuPackagingList[].packableQuantity` | integer | 否 | 包材可包装数量 |
| `data.goodsDetail.skuList[].isExistParentGoodsSku` | string | 否 | 存在父商品 |
| `data.goodsDetail.skuList[].customsDeclaration` | object | 否 | 报关信息 |
| `data.goodsDetail.skuList[].customsDeclaration.productAttrs` | array&lt;string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
| `data.goodsDetail.skuList[].customsDeclaration.productSubAttrs` | object | 否 | 各申报属性的详细值 |
| `data.goodsDetail.skuList[].customsDeclaration.productChineseName` | string | 否 | 申报中文名称 |
| `data.goodsDetail.skuList[].customsDeclaration.productEnglishName` | string | 否 | 申报英文名称 |
| `data.goodsDetail.skuList[].customsDeclaration.productWeight` | string | 否 | 申报重量(g) |
| `data.goodsDetail.skuList[].customsDeclaration.productPrice` | string | 否 | 目的国申报金额(USD) |
| `data.goodsDetail.skuList[].customsDeclaration.exportCountryDeclaredPrice` | string | 否 | 出口国申报金额(USD) |
| `data.goodsDetail.skuList[].customsDeclaration.productMaterial` | string | 否 | 材质 |
| `data.goodsDetail.skuList[].customsDeclaration.productPurpose` | string | 否 | 用途 |
| `data.goodsDetail.skuList[].customsDeclaration.customCode` | string | 否 | 海关编码 |
| `data.goodsDetail.skuList[].isHavePermissions` | string | 否 | 是否有权限 |
| `data.goodsDetail.goodsGroupName` | string | 否 | 商品分组名称 |
| `data.goodsDetail.goodsGroupBreadcrumb` | string | 否 | 商品分组名称 |
