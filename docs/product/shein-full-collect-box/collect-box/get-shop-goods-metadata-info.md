# 获取店铺商品发布字段规范


- 层级：开放平台 > 商品 > SHEIN全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein/collect_box/get_shop_goods_metadata_info`
- 类型：读
- 原文：[537694045e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537694045e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `cid` | string | 是 | 类目ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopGoodsMetadataInfo` | object | 否 | 店铺商品发布字段规范 |
| `data.shopGoodsMetadataInfo.competingProductLink` | object | 否 | 参考竞品链接配置 |
| `data.shopGoodsMetadataInfo.competingProductLink.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.competingProductLink.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.competingProductLink.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.proofStockUrls` | object | 否 | 库存证明图配置 |
| `data.shopGoodsMetadataInfo.proofStockUrls.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.proofStockUrls.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.proofStockUrls.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.sampleInfo` | object | 否 | 样品信息配置 |
| `data.shopGoodsMetadataInfo.sampleInfo.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.sampleInfo.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.sampleInfo.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.brandCode` | object | 否 | 品牌配置 |
| `data.shopGoodsMetadataInfo.brandCode.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.brandCode.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.brandCode.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.ipCharacter` | object | 否 | IP 配置 |
| `data.shopGoodsMetadataInfo.ipCharacter.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.ipCharacter.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.ipCharacter.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.minimumStockQuantity` | object | 否 | 最小起订量配置 |
| `data.shopGoodsMetadataInfo.minimumStockQuantity.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.minimumStockQuantity.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.minimumStockQuantity.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.productDetailPic` | object | 否 | 详情图配置 |
| `data.shopGoodsMetadataInfo.productDetailPic.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.productDetailPic.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.productDetailPic.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.quantityInfo` | object | 否 | 件数信息配置 |
| `data.shopGoodsMetadataInfo.quantityInfo.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.quantityInfo.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.quantityInfo.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.productVideo` | object | 否 | 商品视频配置 |
| `data.shopGoodsMetadataInfo.productVideo.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.productVideo.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.productVideo.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.supplierBarcode` | object | 否 | 供应商条码配置 |
| `data.shopGoodsMetadataInfo.supplierBarcode.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.supplierBarcode.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.supplierBarcode.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.packageType` | object | 否 | 包装类型配置 |
| `data.shopGoodsMetadataInfo.packageType.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.packageType.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.packageType.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.suggestPrice` | object | 否 | 建议售价配置 |
| `data.shopGoodsMetadataInfo.suggestPrice.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.suggestPrice.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.suggestPrice.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.skcTitle` | object | 否 | SKC 标题配置 |
| `data.shopGoodsMetadataInfo.skcTitle.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.skcTitle.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.skcTitle.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.shelfRequire` | object | 否 | 首次上架要求配置 |
| `data.shopGoodsMetadataInfo.shelfRequire.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.shelfRequire.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.shelfRequire.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.spuImageDetail` | object | 否 | SPU 轮播图配置 |
| `data.shopGoodsMetadataInfo.spuImageDetail.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.spuImageDetail.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.spuImageDetail.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.spuImageSquare` | object | 否 | SPU 方图配置 |
| `data.shopGoodsMetadataInfo.spuImageSquare.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.spuImageSquare.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.spuImageSquare.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.skcImageDetail` | object | 否 | SKC 细节图配置 |
| `data.shopGoodsMetadataInfo.skcImageDetail.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.skcImageDetail.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.skcImageDetail.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.skcImageSquare` | object | 否 | SKC 方图配置 |
| `data.shopGoodsMetadataInfo.skcImageSquare.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.skcImageSquare.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.skcImageSquare.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.skuImageDetail` | object | 否 | SKU 图配置 |
| `data.shopGoodsMetadataInfo.skuImageDetail.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.skuImageDetail.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.skuImageDetail.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.switchSpuPicture` | object | 否 | 是否支持切换 SPU 图模式 |
| `data.shopGoodsMetadataInfo.switchSpuPicture.show` | boolean | 否 | 是否展示 |
| `data.shopGoodsMetadataInfo.switchSpuPicture.required` | boolean | 否 | 是否必填 |
| `data.shopGoodsMetadataInfo.switchSpuPicture.single` | boolean | 否 | 是否单张/单值模式 |
| `data.shopGoodsMetadataInfo.defaultLanguage` | string | 否 | 默认语言 |
| `data.shopGoodsMetadataInfo.defaultLanguageTitleMaxLength` | integer | 否 | 默认语言标题最大长度 |
| `data.shopGoodsMetadataInfo.defaultLanguageDescMaxLength` | integer | 否 | 默认语言描述最大长度 |
| `data.shopGoodsMetadataInfo.languageTitleMaxLengthList` | array&lt;object> | 否 | 多语言标题长度限制 |
| `data.shopGoodsMetadataInfo.languageTitleMaxLengthList[].language` | string | 否 | ERP 语言编码 |
| `data.shopGoodsMetadataInfo.languageTitleMaxLengthList[].maxLength` | integer | 否 | 该语言标题最大长度 |
| `data.shopGoodsMetadataInfo.supportSaleAttributeSort` | boolean | 否 | 是否支持销售属性排序 |
