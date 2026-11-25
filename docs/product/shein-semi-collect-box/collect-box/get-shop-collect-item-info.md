# 获取采集箱店铺模式详情


- 层级：开放平台 > 商品 > SHEIN半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein_choice/collect_box/get_shop_collect_item_info`
- 类型：读
- 原文：[537697861e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537697861e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |
| `cid` | string | 否 | 类目ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.claimToShopIds` | array&lt;integer> | 否 | 可认领店铺ID列表 |
| `data.currencyCodeList` | array&lt;string> | 否 | 币种编码列表 |
| `data.attributeRuleList` | array&lt;object> | 否 | 类目属性规则列表 |
| `data.attributeRuleList[].id` | integer | 否 | 属性ID |
| `data.attributeRuleList[].name` | string | 否 | 属性名称 |
| `data.attributeRuleList[].requireExtraValue` | boolean | 否 | 是否需要附属值 |
| `data.attributeRuleList[].inputType` | string | 否 | 输入类型(singleSelect-multipleSelect-input 等) |
| `data.attributeRuleList[].group` | string | 否 | 属性分组(normal-sale-sizeChart) |
| `data.attributeRuleList[].isMainSale` | boolean | 否 | 是否主销售属性 |
| `data.attributeRuleList[].isComponent` | boolean | 否 | 是否组件属性 |
| `data.attributeRuleList[].isRequire` | boolean | 否 | 是否必填 |
| `data.attributeRuleList[].options` | array&lt;object> | 否 | 可选项列表 |
| `data.attributeRuleList[].options[].name` | string | 否 | 选项名称 |
| `data.attributeRuleList[].options[].id` | integer | 否 | 选项ID |
| `data.attributeRuleList[].options[].groupList` | array&lt;integer> | 否 | 选项所属分组列表 |
| `data.attributeRuleList[].isSupportCustom` | integer | 否 | 是否支持自定义值(0-否，1-是) |
| `data.attributeRuleList[].attributeRemarkList` | array&lt;object> | 否 | 属性备注列表 |
| `data.attributeRuleList[].attributeInputNum` | integer | 否 | 最大输入数量 |
| `data.categoryAttributeCheckRuleList` | array&lt;object> | 否 | 类目属性校验规则列表 |
| `data.categoryAttributeCheckRuleList[].needCheckAttrId` | string | 否 | 需要校验的属性ID |
| `data.categoryAttributeCheckRuleList[].needCheckCondition` | array&lt;object> | 否 | 命中条件，key 为属性ID，value 为允许的属性值ID列表 |
| `data.shopCollectItemInfo` | object | 否 | 店铺采集商品详情 |
| `data.shopCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.shopCollectItemInfo.notes` | string | 否 | 商品描述 |
| `data.shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.shopCollectItemInfo.multiLanguageNotesMap` | object | 否 | 多语言描述映射 |
| `data.shopCollectItemInfo.brandName` | string | 否 | 品牌名称 |
| `data.shopCollectItemInfo.itemNum` | string | 否 | 货号 |
| `data.shopCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.shopCollectItemInfo.attributes` | array&lt;object> | 否 | 商品属性列表 |
| `data.shopCollectItemInfo.saleAttributes` | array&lt;object> | 否 | 销售属性列表 |
| `data.shopCollectItemInfo.saleAttributes[].id` | string | 是 | 销售属性ID |
| `data.shopCollectItemInfo.saleAttributes[].name` | string | 是 | 销售属性名称 |
| `data.shopCollectItemInfo.saleAttributes[].values` | array&lt;object> | 是 | 销售属性值列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].id` | string | 是 | 销售属性值ID(平台值或 mock 值) |
| `data.shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 销售属性值名称 |
| `data.shopCollectItemInfo.saleAttributes[].values[].nameZh` | string | 否 | 销售属性中文名称(如颜色) |
| `data.shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU Key(用于与 skuMap 建立映射) |
| `data.shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | SKC 图片列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].skcTitle` | string | 否 | SKC 标题 |
| `data.shopCollectItemInfo.saleAttributes[].values[].multiLanguageSkcTitleMap` | object | 否 | 多语言 SKC 标题映射 |
| `data.shopCollectItemInfo.saleAttributes[].values[].squareImgUrl` | string | 否 | 方块图 URL |
| `data.shopCollectItemInfo.saleAttributes[].values[].pieceImgUrl` | string | 否 | 色块图 URL |
| `data.shopCollectItemInfo.saleAttributes[].values[].proofStockUrls` | array&lt;string> | 否 | 库存证明图片列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 主销售属性供货方货号/卖家 SKU |
| `data.shopCollectItemInfo.saleAttributes[].values[].suggestedPrice` | number | 否 | 建议售价 |
| `data.shopCollectItemInfo.saleAttributes[].values[].suggestedPriceCurrency` | string | 否 | 建议售价币种(当 suggestedPrice 有值时必填) |
| `data.shopCollectItemInfo.saleAttributes[].values[].siteDetailImageInfoList` | array&lt;object> | 否 | 站点图配置列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].shelfWay` | integer | 否 | 上架方式(1-自动上架，2-定时上架) |
| `data.shopCollectItemInfo.saleAttributes[].values[].hopeOnSaleDate` | string | 否 | 期望上架时间(定时上架时必填) |
| `data.shopCollectItemInfo.saleAttributes[].values[].shelfRequire` | string | 否 | 是否强制上架/货架要求('0'-不到货上架，'1'-到货上架) |
| `data.shopCollectItemInfo.skuMap` | object | 否 | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |
| `data.shopCollectItemInfo.sizeChart` | array&lt;object> | 否 | 尺码表 |
| `data.shopCollectItemInfo.videoPublishSites` | array&lt;string> | 否 | 视频发布站点列表 |
| `data.shopCollectItemInfo.imgUrls` | array&lt;string> | 否 | 商品图片列表 |
| `data.shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.shopCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图应用视频ID |
| `data.shopCollectItemInfo.isSpuPic` | boolean | 否 | 是否SPU图模式 |
| `data.shopCollectItemInfo.spuImageDetailUrls` | array&lt;string> | 否 | SPU轮播图列表 |
| `data.shopCollectItemInfo.spuImageSquareUrl` | string | 否 | SPU方图 |
| `data.shopCollectItemInfo.sourceList` | array&lt;object> | 否 | 来源列表 |
| `data.shopCollectItemInfo.breadcrumb` | string | 否 | 类目面包屑 |
| `data.shopCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.shopCollectItemInfo.copyType` | string | 否 | 复制类型 |
| `data.shopCollectItemInfo.ipCharacterList` | array&lt;object> | 否 | IP形象列表 |
| `data.shopCollectItemInfo.cateList` | array&lt;object> | 否 | 类目链路 |
| `data.shopCollectItemInfo.sourceProductSizeChart` | array&lt;object> | 否 | 来源商品尺码表 |
| `data.shopCollectItemInfo.sourceBodySizeChart` | array&lt;object> | 否 | 来源人体尺码表 |
| `data.shopCollectItemInfo.sizeChartHasInit` | integer | 否 | 尺码表是否已初始化 |
| `data.shopCollectItemInfo.editDisplayConfig` | array&lt;object> | 否 | 编辑展示配置 |
| `data.shopCollectItemInfo.isSetSitePrice` | integer | 否 | 半托管是否按站点设置SKU价格(0-否，1-是；仅 shein_choice 使用) |
