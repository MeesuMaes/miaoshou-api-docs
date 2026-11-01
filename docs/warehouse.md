# 妙手开放平台 · 仓储模块

> 由 apifox 分享文档整理（18 个接口）。字段说明原样摘自 OpenAPI 定义，未做改写；请求/响应以原文为准。

## 目录

- 商品>商品（5）
- 商品>商品品牌（1）
- 商品>商品分组（1）
- 商品>商品sku（1）
- 商品包材（1）
- 数据统计>销售数据（1）
- 数据统计>商品周转分析（1）
- 库存>三方仓sku库存（1）
- 库存>自营仓库存（2）
- 仓库>自营仓仓库（2）
- 仓库>三方仓仓库（2）

## 商品>商品

### 获取多规格商品列表

- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/fetch/search_goods_page`
- 类型：读
- 原文：[479599763e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599763e0.md)（本地 raw/479599763e0_获取多规格商品列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `goodsSkuOuterIds` | array<string> | 否 | sku |
| `groupId` | string | 否 | 分组ID |
| `itemNum` | array<string> | 否 | SPU |
| `keyword` | string | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsList` | array<object> | 否 |  |
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
| `data.goodsList[].skuList` | array<object> | 否 | SKU列表 |
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
| `data.goodsList[].skuList[].supplierList` | array<object> | 否 | 供应商列表 |
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
| `data.goodsList[].skuList[].goodsAttributeList` | array<object> | 否 | 商品属性列表 |
| `data.goodsList[].skuList[].goodsAttributeList[].goodsAttributeId` | string | 否 | ID |
| `data.goodsList[].skuList[].goodsAttributeList[].goodsAttributeValueId` | string | 否 | 值ID |
| `data.goodsList[].skuList[].goodsAttributeList[].attributeValue` | string | 否 | 属性值名称 |
| `data.goodsList[].skuList[].goodsAttributeList[].attributeName` | string | 否 | 规格名称 |
| `data.goodsList[].skuList[].platformOuterSkuIds` | array<string> | 否 | 关联平台SKU |
| `data.goodsList[].skuList[].platformSkuIds` | array<string> | 否 | 关联的平台SKU Id |
| `data.goodsList[].skuList[].goodsSkuBundleList` | array<object> | 否 | 子商品信息 |
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
| `data.goodsList[].skuList[].customsDeclaration.productAttrs` | array<string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
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
| `data.goodsList[].goodsPackagingList` | array<object> | 否 | 商品包装列表 |
| `data.goodsList[].goodsPackagingList[].packagingId` | integer | 否 | 包材id |
| `data.goodsList[].goodsPackagingList[].packableQuantity` | integer | 否 | 包材可包装数量 |


---

### 获取商品详情

- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/fetch/get_goods_info`
- 类型：读
- 原文：[479599764e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599764e0.md)（本地 raw/479599764e0_获取商品详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `data.goodsDetail.skuList` | array<object> | 否 | SKU列表 |
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
| `data.goodsDetail.skuList[].supplierList` | array<object> | 否 | 供应商列表 |
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
| `data.goodsDetail.skuList[].goodsAttributeList` | array<object> | 否 | 商品属性列表 |
| `data.goodsDetail.skuList[].goodsAttributeList[].goodsAttributeId` | string | 否 | ID |
| `data.goodsDetail.skuList[].goodsAttributeList[].goodsAttributeValueId` | string | 否 | 值ID |
| `data.goodsDetail.skuList[].goodsAttributeList[].attributeValue` | string | 否 | 属性值名称 |
| `data.goodsDetail.skuList[].goodsAttributeList[].attributeName` | string | 否 | 规格名称 |
| `data.goodsDetail.skuList[].platformOuterSkuIds` | array<string> | 否 | 关联平台SKU |
| `data.goodsDetail.skuList[].platformSkuIds` | array<string> | 否 | 关联的平台SKU Id |
| `data.goodsDetail.skuList[].goodsSkuBundleList` | array<object> | 否 | 子商品信息 |
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
| `data.goodsDetail.skuList[].goodsSkuPackagingList` | array<object> | 否 |  |
| `data.goodsDetail.skuList[].goodsSkuPackagingList[].packagingId` | integer | 否 | 包材id |
| `data.goodsDetail.skuList[].goodsSkuPackagingList[].packableQuantity` | integer | 否 | 包材可包装数量 |
| `data.goodsDetail.skuList[].isExistParentGoodsSku` | string | 否 | 存在父商品 |
| `data.goodsDetail.skuList[].customsDeclaration` | object | 否 | 报关信息 |
| `data.goodsDetail.skuList[].customsDeclaration.productAttrs` | array<string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
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


---

### 添加商品

- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/operate/add_goods`
- 类型：写
- 原文：[479599765e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599765e0.md)（本地 raw/479599765e0_添加商品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `goodsSkuList` | array<object> | 是 | SKU列表 |
| `goodsSkuList[].goodsSkuId` | integer | 否 | SKU ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsSkuOuterId` | string | 否 | 商品SKU编码 |
| `goodsSkuList[].platformOuterSkuIds` | array<string> | 否 | 平台外部SKU ID列表 |
| `goodsSkuList[].platformSkuIds` | array<string> | 否 | 平台内部SKU ID列表 |
| `goodsSkuList[].skuImgUrl` | string | 否 | SKU图片URL |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价（参考价格） |
| `goodsSkuList[].weight` | string | 否 | 重量(KG) |
| `goodsSkuList[].width` | string | 否 | 宽度 |
| `goodsSkuList[].height` | string | 否 | 高度 |
| `goodsSkuList[].length` | string | 否 | 长度 |
| `goodsSkuList[].goodsSkuBundleList` | array<object> | 否 | 组合品子商品列表（组合品模式） |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuOuterId` | string | 否 | 子商品SKU编码 |
| `goodsSkuList[].goodsSkuBundleList[].goodsName` | string | 否 | 子商品名称 |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuSubName` | string | 否 | 子商品规格名称 |
| `goodsSkuList[].goodsSkuBundleList[].logoUrl` | string | 否 | 子商品图片URL |
| `goodsSkuList[].goodsSkuBundleList[].quantity` | string | 否 | 组合数量 |
| `goodsSkuList[].customsDeclaration` | object | 否 | 报关/清关申报信息 |
| `goodsSkuList[].customsDeclaration.productAttrs` | array<string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
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
| `goodsSkuList[].goodsSkuPackagingList` | array<object> | 否 | 包材列表 |
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


---

### 安全库存批量设置

- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/operate/batch_save_goods_suggest_config`
- 类型：写
- 原文：[479599766e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599766e0.md)（本地 raw/479599766e0_安全库存批量设置.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSuggestConfigList` | array<object> | 否 | 商品建议配置列表 |
| `goodsSuggestConfigList[].goodsSkuId` | integer | 是 | 商品sku id |
| `goodsSuggestConfigList[].warehouseId` | integer | 是 | 仓库id |
| `goodsSuggestConfigList[].computeMode` | string | 是 | 计算方式 固定值：newValue |
| `goodsSuggestConfigList[].safeStock` | integer | 是 | 安全库存 |
| `goodsSuggestConfigList[].minTriggerSuggestNum` | integer | 否 | 库存下限 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successCnt` | integer | 否 | 成功数量 |


---

### 修改商品

- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/operate/edit_goods`
- 类型：写
- 原文：[479599767e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599767e0.md)（本地 raw/479599767e0_修改商品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsId` | integer | 是 | 商品ID |
| `goodsGroupId` | string | 否 | 商品分组ID |
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
| `goodsSkuList` | array<object> | 是 | SKU列表 |
| `goodsSkuList[].goodsSkuId` | integer | 否 | SKU ID，创建时为空，编辑时有值 |
| `goodsSkuList[].goodsSkuOuterId` | string | 否 | 商品SKU编码 |
| `goodsSkuList[].platformOuterSkuIds` | array<string> | 否 | 平台外部SKU ID列表 |
| `goodsSkuList[].platformSkuIds` | array<string> | 否 | 平台内部SKU ID列表 |
| `goodsSkuList[].skuImgUrl` | string | 否 | SKU图片URL |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价（参考价格） |
| `goodsSkuList[].weight` | string | 否 | 重量(KG) |
| `goodsSkuList[].width` | string | 否 | 宽度 |
| `goodsSkuList[].height` | string | 否 | 高度 |
| `goodsSkuList[].length` | string | 否 | 长度 |
| `goodsSkuList[].goodsSkuBundleList` | array<object> | 否 | 组合品子商品列表（组合品模式） |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuOuterId` | string | 否 | 子商品SKU编码 |
| `goodsSkuList[].goodsSkuBundleList[].goodsName` | string | 否 | 子商品名称 |
| `goodsSkuList[].goodsSkuBundleList[].goodsSkuSubName` | string | 否 | 子商品规格名称 |
| `goodsSkuList[].goodsSkuBundleList[].logoUrl` | string | 否 | 子商品图片URL |
| `goodsSkuList[].goodsSkuBundleList[].quantity` | string | 否 | 组合数量 |
| `goodsSkuList[].customsDeclaration` | object | 否 | 报关/清关申报信息 |
| `goodsSkuList[].customsDeclaration.productAttrs` | array<string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
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
| `goodsSkuList[].goodsSkuPackagingList` | array<object> | 否 | 包材列表 |
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


## 商品>商品品牌

### 获取列表

- 层级：开放平台 > 仓储 > 商品 > 商品品牌
- 方法+路径：`POST /open/v1/ewm/goods/goods_brand/fetch/search_goods_brand_page`
- 类型：读
- 原文：[479599768e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599768e0.md)（本地 raw/479599768e0_获取列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.brandList` | array<object> | 否 |  |
| `data.brandList[].goodsBrandId` | integer | 否 | 商品品牌ID |
| `data.brandList[].brandName` | string | 否 | 品牌名称 |
| `data.total` | integer | 否 | 总计 |


## 商品>商品分组

### 获取商品分组列表

- 层级：开放平台 > 仓储 > 商品 > 商品分组
- 方法+路径：`POST /open/v1/ewm/goods/goods_group/fetch/get_goods_group_list`
- 类型：读
- 原文：[479599769e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599769e0.md)（本地 raw/479599769e0_获取商品分组列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsGroupTree` | array<object> | 否 |  |
| `data.goodsGroupTree[].goodsGroupId` | string | 否 | 分组ID |
| `data.goodsGroupTree[].parentGoodsGroupId` | string | 否 | 父分组ID |
| `data.goodsGroupTree[].groupName` | string | 否 | 分组名称 |
| `data.goodsGroupTree[].level` | string | 否 | 级别 |
| `data.goodsGroupTree[].sort` | string | 否 | 排序 |
| `data.goodsGroupTree[].subGroups` | array<object> | 否 | 子分组 |


## 商品>商品sku

### 获取商品SKU列表

- 层级：开放平台 > 仓储 > 商品 > 商品sku
- 方法+路径：`POST /open/v1/ewm/goods/goods_sku/fetch/search_goods_sku_page`
- 类型：读
- 原文：[479599770e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599770e0.md)（本地 raw/479599770e0_获取商品SKU列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `groupId` | string | 否 | 分组ID |
| `goodsMode` | string | 是 | 商品类型 single(单规格),bundle(组合) |
| `goodsSkuOuterIds` | array<string> | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuList` | array<object> | 否 | sku列表 |
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
| `data.goodsSkuList[].supplierList` | array<object> | 否 | 供应商列表 |
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
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.attributeDisplayName` | array<string> | 否 | 属性显示名称 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.attributeValue` | array<string> | 否 | 属性值 |
| `data.goodsSkuList[].supplierList[].ali1688ItemSku.title` | string | 否 | 标题 |
| `data.goodsSkuList[].supplierList[].purchaseRate` | object | 否 | 采购比例（本地商品数量：货源下单数量） |
| `data.goodsSkuList[].supplierList[].purchaseRate.goodsSkuNum` | integer | 否 | 采购比例：商品数量 |
| `data.goodsSkuList[].supplierList[].purchaseRate.sourceNum` | integer | 否 | 采购比例：货源下单数量 |
| `data.goodsSkuList[].goodsAttributeList` | array<object> | 否 | 商品属性列表 |
| `data.goodsSkuList[].goodsAttributeList[].goodsAttributeId` | string | 否 | ID |
| `data.goodsSkuList[].goodsAttributeList[].goodsAttributeValueId` | string | 否 | 值ID |
| `data.goodsSkuList[].goodsAttributeList[].attributeValue` | string | 否 | 属性值名称 |
| `data.goodsSkuList[].goodsAttributeList[].attributeName` | string | 否 | 规格名称 |
| `data.goodsSkuList[].platformOuterSkuIds` | array<string> | 否 | 关联平台SKU |
| `data.goodsSkuList[].platformSkuIds` | array<string> | 否 | 关联的平台SKU Id |
| `data.goodsSkuList[].goodsSkuBundleList` | array<object> | 否 | 子商品信息 |
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
| `data.goodsSkuList[].customsDeclaration.productAttrs` | array<string> | 否 | 申报属性  带电:with_battery, 含非液体化妆品:aneroid_markup, 特货(敏感货):special_product |
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


## 商品包材

### 获取列表

- 层级：开放平台 > 仓储 > 商品包材
- 方法+路径：`POST /open/v1/ewm/packaging/fetch/search_packaging_page`
- 类型：读
- 原文：[479592181e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592181e0.md)（本地 raw/479592181e0_获取列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.packagingList` | array<object> | 否 | 包材列表 |
| `data.packagingList[].packagingId` | string | 否 | ID |
| `data.packagingList[].packagingCode` | string | 否 | code |
| `data.packagingList[].name` | string | 否 | 包材名称 |
| `data.packagingList[].price` | string | 否 | 价格 |
| `data.packagingList[].length` | string | 否 | 长度 |
| `data.packagingList[].width` | string | 否 | 宽度 |
| `data.packagingList[].height` | string | 否 | 高度 |
| `data.packagingList[].weight` | string | 否 | 重量 |
| `data.packagingList[].remark` | string | 否 | 备注 |
| `data.packagingList[].gmtCreate` | string | 否 | 创建时间 |
| `data.packagingList[].gmtModified` | string | 否 | 更新时间 |
| `data.total` | integer | 否 | 总数 |


## 数据统计>销售数据

### 获取商品销售数据列表

- 层级：开放平台 > 仓储 > 数据统计 > 销售数据
- 方法+路径：`POST /open/v1/ewm/stat/goods_sale_data/fetch/search_goods_sale_data_page`
- 类型：读
- 原文：[479602617e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479602617e0.md)（本地 raw/479602617e0_获取商品销售数据列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `shopIds` | array<integer> | 是 | 店铺ID数组 |
| `gmtStart` | string | 是 | 开始日期如2022-07-01 |
| `gmtEnd` | string | 是 | 结束日期如2022-07-01 |
| `warehouseIds` | array<integer> | 否 | 仓库ID数组 |
| `logisticsAgentWarehouseIds` | array<integer> | 否 | 第三方仓库id |
| `goodsSkuOuterIds` | string | 否 | 商品SKU |
| `goodsSkuOuterIdsRp` | string | 否 | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsName` | string | 否 | 商品名称 |
| `goodsNameRp` | string | 否 | 商品名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsSkuCustomCodes` | string | 否 | 商品代码 |
| `goodsSkuCustomCodesRp` | string | 否 | 商品代码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `foreignGoodsName` | string | 否 | 商品外文名称 |
| `foreignGoodsNameRp` | string | 否 | 商品外文名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsGroupIds` | array<integer> | 否 | 商品分组ID列表 |
| `shopFilterType` | string | 否 | 店铺类型shopId-按店铺Id,group-按店铺分组拣货单 |
| `shopGroupIds` | array<integer> | 否 | 店铺分组id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSaleList` | array<object> | 否 |  |
| `data.goodsSaleList[].goodsSkuId` | string | 否 | 商品sku Id |
| `data.goodsSaleList[].orderSaleCount` | string | 否 | 自营仓销售订单量 |
| `data.goodsSaleList[].goodsSaleCount` | string | 否 | 自营仓销量 |
| `data.goodsSaleList[].goodsRefundCount` | string | 否 | 退货数量 |
| `data.goodsSaleList[].goodsSaleAmount` | number | 否 | 销售金额 |
| `data.goodsSaleList[].goodsCostAmount` | number | 否 | 自营仓商品成本 |
| `data.goodsSaleList[].goodsRefundAmount` | number | 否 | 退款成本 |
| `data.goodsSaleList[].orderRefundAmount` | number | 否 | 退款金额 |
| `data.goodsSaleList[].goodsSkuInfo` | object | 否 | 商品信息 |
| `data.goodsSaleList[].goodsSkuInfo.goodsName` | string | 否 | 商品名称 |
| `data.goodsSaleList[].goodsSkuInfo.goodsMode` | string | 否 | 商品类型 |
| `data.goodsSaleList[].goodsSkuInfo.goodsId` | string | 否 | 商品id |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuId` | string | 否 | 商品SKUid |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuOuterId` | string | 否 | sku |
| `data.goodsSaleList[].goodsSkuInfo.logoOssPath` | string | 否 | 图片地址 |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsSaleList[].goodsSkuInfo.goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsSaleList[].goodsSkuInfo.logoUrl` | string | 否 | 图片url |
| `data.goodsSaleList[].rank` | string | 否 | 排名 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales` | object | 否 | 三方仓销售数据 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuOrderSaleAmount` | number | 否 | 三方仓销售金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuOrderSaleCount` | integer | 否 | 三方仓销售订单量 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuGoodsSaleCount` | integer | 否 | 三方仓销量 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuAllSales.logisticsAgentGoodsSkuGoodsCostAmount` | number | 否 | 三方仓商品成本 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList` | array<object> | 否 | 三方仓销售数据列表 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentWarehouseId` | string | 否 | 仓库id |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentGoodsSkuId` | string | 否 | 第三方sku ID |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsSkuId` | string | 否 | 商品sku ID |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].orderSaleAmount` | string | 否 | 订单销售金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].orderSaleCount` | string | 否 | 商品成本金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsSaleCount` | string | 否 | 商品销售数量 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].goodsCostAmount` | string | 否 | 商品成本金额 |
| `data.goodsSaleList[].logisticsAgentGoodsSkuSalesList[].logisticsAgentWarehouseName` | string | 否 | 仓库名称 |
| `data.total` | integer | 否 | 总数 |


## 数据统计>商品周转分析

### 获取商品周转数据列表

- 层级：开放平台 > 仓储 > 数据统计 > 商品周转分析
- 方法+路径：`POST /open/v1/ewm/stat/goods_turnover_data/fetch/search_goods_turnover_data_page`
- 类型：读
- 原文：[479602618e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479602618e0.md)（本地 raw/479602618e0_获取商品周转数据列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `gmtStart` | string | 是 | 开始日期如2022-07-01 |
| `gmtEnd` | string | 是 | 结束日期如2022-07-01 |
| `warehouseIds` | array<integer> | 否 | 仓库ID数组 |
| `goodsSkuOuterIds` | string | 否 | 商品SKU |
| `goodsSkuOuterIdsRp` | string | 否 | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsName` | string | 否 | 商品名称 |
| `goodsNameRp` | string | 否 | 商品名称搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确),ass(多个关键词同时匹配) |
| `goodsGroupIds` | array<integer> | 否 | 商品分组ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsList` | array<object> | 否 |  |
| `data.goodsList[].rank` | string | 否 | 排名 |
| `data.goodsList[].turnoverRate` | string | 否 | 周转率（%） |
| `data.goodsList[].turnoverDay` | string | 否 | 周转天数（天） |
| `data.goodsList[].saleRate` | string | 否 | 动销率（%） |
| `data.goodsList[].endDtStockNum` | string | 否 | 期末库存总量 |
| `data.goodsList[].endDtStockCostAmount` | string | 否 | 期末库存成本 |
| `data.goodsList[].startDtStockNum` | string | 否 | 期初库存总量 |
| `data.goodsList[].startDtStockCostAmount` | string | 否 | 期初库存成本 |
| `data.goodsList[].confirmUseGoodsSkuWarehouseCount` | string | 否 | 销售出库数量 |
| `data.goodsList[].confirmUseGoodsSkuWarehouseCostAmount` | string | 否 | 销售出库成本 |
| `data.goodsList[].otherOutStorageCount` | string | 否 | 其他出库数量 |
| `data.goodsList[].otherOutStorageCostAmount` | string | 否 | 其他出库成本 |
| `data.goodsList[].allInStorageCount` | string | 否 | 入库数量 |
| `data.goodsList[].allInStorageCostAmount` | string | 否 | 入库成本 |
| `data.goodsList[].goodsSkuInfo` | object | 否 | 商品信息 |
| `data.goodsList[].goodsSkuInfo.goodsName` | string | 否 | 商品名称 |
| `data.goodsList[].goodsSkuInfo.goodsMode` | string | 否 | 商品类型 |
| `data.goodsList[].goodsSkuInfo.goodsId` | string | 否 | 商品id |
| `data.goodsList[].goodsSkuInfo.goodsSkuId` | string | 否 | 商品SKUid |
| `data.goodsList[].goodsSkuInfo.goodsSkuOuterId` | string | 否 | sku |
| `data.goodsList[].goodsSkuInfo.logoOssPath` | string | 否 | 图片地址 |
| `data.goodsList[].goodsSkuInfo.goodsSkuSubName` | string | 否 | 规格 |
| `data.goodsList[].goodsSkuInfo.goodsSkuCustomCode` | string | 否 | 商品代码 |
| `data.goodsList[].goodsSkuInfo.logoUrl` | string | 否 | 图片url |
| `data.total` | integer | 否 | 总数 |


## 库存>三方仓sku库存

### 获取三方仓商品库存列表

- 层级：开放平台 > 仓储 > 库存 > 三方仓sku库存
- 方法+路径：`POST /open/v1/ewm/storage/third_warehouse/fetch/search_third_goods_sku_warehouse_page`
- 类型：读
- 原文：[479599784e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599784e0.md)（本地 raw/479599784e0_获取三方仓商品库存列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `type` | string | 是 | 类型 1:第三方仓库服务商LogisticsAgent 2:第三方货代仓库服务商Forwarder 3:FBA仓库 4:FBT |
| `thirdWarehouseProviderAgentAuthIds` | array<integer> | 否 | 第三方仓库服务商授权主键ID （选一个） |
| `thirdWarehouseForwarderProviderAuthIds` | array<integer> | 否 | 第三方货代仓库服务商授权主键ID（选一个） |
| `thirdWarehouseProviderAuthId` | array<integer> | 否 | FBA\FBA授权id |
| `warehouseIds` | array<integer> | 是 | 仓库Ids |
| `keyword` | string | 否 | 第三方sku 多个用逗号分隔 |
| `matchSku` | string | 否 | 商品sku（映射关系） 多个用逗号分隔 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuWarehouseList` | object | 否 | 商品SKU库存数据 |
| `data.goodsSkuWarehouseList.goodsSkuOuterId` | string | 否 | 第三方sku |
| `data.goodsSkuWarehouseList.warehouseName` | string | 否 | 仓库名称 |
| `data.goodsSkuWarehouseList.logisticsAgentWarehouseId` | string | 否 | 第三方仓库id |
| `data.goodsSkuWarehouseList.stockNum` | string | 否 | 库存 |
| `data.goodsSkuWarehouseList.availableStockNum` | string | 否 | 可用库存 |
| `data.goodsSkuWarehouseList.lockedStockNum` | string | 否 | 预占库存 |
| `data.goodsSkuWarehouseList.frozenStockNum` | string | 否 | 待上架库存 |
| `data.goodsSkuWarehouseList.onWayStockNum` | string | 否 | 在途库存 |
| `data.goodsSkuWarehouseList.waitSubmitStockNum` | string | 否 | 待提交量 |
| `data.goodsSkuWarehouseList.onPlanNum` | string | 否 | 计划库存 |
| `data.goodsSkuWarehouseList.faultyStockNum` | integer | 否 | 次品库存数量 |
| `data.goodsSkuWarehouseList.notForSaleNum` | integer | 否 | 不可售数量（平台仓） |
| `data.goodsSkuWarehouseList.inboundNum` | integer | 否 | 入库数量（平台仓） |
| `data.goodsSkuWarehouseList.reservedNum` | integer | 否 | 活动预留数量 |
| `data.total` | integer | 否 |  |


## 库存>自营仓库存

### 获取自营仓商品库存列表

- 层级：开放平台 > 仓储 > 库存 > 自营仓库存
- 方法+路径：`POST /open/v1/ewm/storage/warehouse/fetch/search_goods_sku_warehouse_page`
- 类型：读
- 原文：[479599786e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599786e0.md)（本地 raw/479599786e0_获取自营仓商品库存列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `warehouseIds` | array<integer> | 否 | 仓库ids |
| `goodsSkuOuterIds` | array<string> | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuWarehouseList` | array<object> | 否 | 商品SKU库存数据 |
| `data.goodsSkuWarehouseList[].goodsSkuWarehouseId` | string | 否 | 仓库id |
| `data.goodsSkuWarehouseList[].goodsSkuId` | string | 否 | 商品skuid |
| `data.goodsSkuWarehouseList[].goodsId` | string | 否 | 商品id |
| `data.goodsSkuWarehouseList[].stockNum` | string | 否 | 总库存 |
| `data.goodsSkuWarehouseList[].availableStockNum` | string | 否 | 可用库存 |
| `data.goodsSkuWarehouseList[].lockedStockNum` | string | 否 | 预占库存 |
| `data.goodsSkuWarehouseList[].onWayNum` | string | 否 | 在途库存 |
| `data.goodsSkuWarehouseList[].onPlanNum` | string | 否 | 计划库存 |
| `data.total` | integer | 否 |  |


---

### 获取商品SKU安全库存列表

- 层级：开放平台 > 仓储 > 库存 > 自营仓库存
- 方法+路径：`POST /open/v1/ewm/storage/warehouse/fetch/get_goods_sku_safe_stock_num_list`
- 类型：读
- 原文：[479599785e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599785e0.md)（本地 raw/479599785e0_获取商品SKU安全库存列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSkuOuterIds` | array<string> | 是 | 商品sku |
| `warehouseId` | integer | 是 | 仓库id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuOuterIdAndSafeStockNumMap` | array<object> | 否 |  |
| `data.goodsSkuOuterIdAndSafeStockNumMap[].goodsSkuOuterId` | string | 否 | 商品SKU |
| `data.goodsSkuOuterIdAndSafeStockNumMap[].safeStockNum` | integer | 否 | 库存安全数 |


## 仓库>自营仓仓库

### 获取供应商仓库列表

- 层级：开放平台 > 仓储 > 仓库 > 自营仓仓库
- 方法+路径：`POST /open/v1/ewm/warehouse/fetch/supplier_warehouse_list`
- 类型：读
- 原文：[476990600e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/476990600e0.md)（本地 raw/476990600e0_获取供应商仓库列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supplierWarehouseList` | array<object> | 否 | 供应商仓库列表 |
| `data.supplierWarehouseList[].warehouseId` | integer | 否 | 仓库ID |
| `data.supplierWarehouseList[].warehouseName` | string | 否 | 仓库名称 |


---

### 获取自营仓仓库列表

- 层级：开放平台 > 仓储 > 仓库 > 自营仓仓库
- 方法+路径：`POST /open/v1/ewm/warehouse/fetch/search_warehouse_page`
- 类型：读
- 原文：[476435300e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/476435300e0.md)（本地 raw/476435300e0_获取自营仓仓库列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.warehouseList` | array<object> | 否 |  |
| `data.warehouseList[].warehouseId` | integer | 否 | 仓库ID |
| `data.warehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.warehouseList[].address` | string | 否 | 地址 |
| `data.warehouseList[].fullAddress` | string | 否 | 详细地址 |
| `data.warehouseList[].isDefault` | integer | 否 | 是否默认仓库 |
| `data.total` | integer | 否 |  |


## 仓库>三方仓仓库

### 获取三方仓授权列表

- 层级：开放平台 > 仓储 > 仓库 > 三方仓仓库
- 方法+路径：`POST /open/v1/ewm/third_warehouse/fetch/search_third_provider_auth_page`
- 类型：读
- 原文：[479592192e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592192e0.md)（本地 raw/479592192e0_获取三方仓授权列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.providerAuthList` | object | 否 | 第三方授权列表 |
| `data.providerAuthList.thirdWarehouseProviderAuthId` | string | 否 | 授权ID |
| `data.providerAuthList.providerId` | string | 否 | 服务商ID |
| `data.providerAuthList.type` | string | 否 | 三方仓类型 forwarder:货代；logisticsAgent 三方服务商 |
| `data.providerAuthList.appCustomerId` | string | 否 | 授权id |
| `data.providerAuthList.nickname` | string | 否 | 昵称 |
| `data.providerAuthList.status` | string | 否 | 状态 |
| `data.providerAuthList.isPlatformWarehouse` | string | 否 | 是否平台仓库 |
| `data.providerAuthList.providerName` | string | 否 | 服务商名称 |
| `data.providerAuthList.providerCode` | string | 否 | 服务商Code |
| `data.providerAuthList.authAgentWarehouseList` | array<object> | 否 | 授权三方服务商仓库列表 |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentWarehouseAuthId` | string | 否 | 仓库授权id |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentCustomerId` | string | 否 | 服务商授权Id |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentWarehouseId` | string | 否 | 仓库id |
| `data.providerAuthList.authAgentWarehouseList[].isDisabled` | string | 否 | 是否禁用 1禁用 |
| `data.providerAuthList.authAgentWarehouseList[].nickname` | string | 否 | 昵称 |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentId` | string | 否 | 服务商id |
| `data.providerAuthList.authAgentWarehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.providerAuthList.authAgentWarehouseList[].platformWarehouseCode` | string | 否 | 平台仓库编码 |
| `data.providerAuthList.authAgentWarehouseList[].address` | string | 否 | 地址 |
| `data.providerAuthList.authAgentWarehouseList[].contactPhone` | string | 否 | 联系电话 |
| `data.providerAuthList.authAgentWarehouseList[].contactName` | string | 否 | 联系人名称 |
| `data.providerAuthList.authForwarderWarehouseList` | array<object> | 否 | 授权货代仓库列表 |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderWarehouseAuthId` | string | 否 | 货代服务商仓库授权id |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderCustomerId` | string | 否 | 货代服务商授权id |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderWarehouseId` | string | 否 | 货代服务商仓库id |
| `data.providerAuthList.authForwarderWarehouseList[].isDisabled` | string | 否 | 是否禁用 |
| `data.providerAuthList.authForwarderWarehouseList[].nickname` | string | 否 | 昵称 |
| `data.providerAuthList.authForwarderWarehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderId` | string | 否 | 货代服务商id |
| `data.providerAuthList.authForwarderWarehouseList[].address` | string | 否 | 地址 |
| `data.providerAuthList.authForwarderWarehouseList[].contactPhone` | string | 否 | 联系电话 |
| `data.providerAuthList.authForwarderWarehouseList[].contactName` | string | 否 | 联系人 |
| `data.total` | integer | 否 | 总数 |


---

### 获取平台仓库列表

- 层级：开放平台 > 仓储 > 仓库 > 三方仓仓库
- 方法+路径：`POST /open/v1/ewm/third_warehouse/fetch/search_platform_warehouse_page`
- 类型：读
- 原文：[479592193e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592193e0.md)（本地 raw/479592193e0_获取平台仓库列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `platformWarehouseType` | string | 是 | 平台类型 FBT / FBA |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.warehouseList` | array<object> | 否 |  |
| `data.warehouseList[].logisticsAgentWarehouseId` | string | 否 | ID |
| `data.warehouseList[].logisticsAgentId` | string | 否 | 服务商ID |
| `data.warehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.warehouseList[].platformWarehouseId` | string | 否 | 平台仓库ID |
| `data.warehouseList[].platformWarehouseCode` | string | 否 | 平台仓库编码 |
| `data.warehouseList[].address` | string | 否 | 地址 |
| `data.warehouseList[].platformWarehouseType` | string | 否 | 平台仓库类型 |
| `data.warehouseList[].shopName` | string | 否 | 店铺名称 |
| `data.warehouseList[].thirdWarehouseProviderAuthId` | integer | 否 | 三方仓服务商授权ID |
| `data.total` | integer | 否 |  |

