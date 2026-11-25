# 创建采集箱产品


- 层级：开放平台 > 商品 > SHEIN全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein/collect_box/create_collect_box_item`
- 类型：写
- 原文：[537694036e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537694036e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.title` | string | 是 | 商品标题(最大1000字符，实际还会受店铺默认语言和类目标题长度限制) |
| `shopCollectItemInfo.chineseName` | string | 否 | 中文标题(中文店铺或中文翻译场景会使用) |
| `shopCollectItemInfo.notes` | string | 是 | 商品描述(必填，最大5000字符，且不能只包含数字) |
| `shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `shopCollectItemInfo.multiLanguageNotesMap` | object | 否 | 多语言描述映射 |
| `shopCollectItemInfo.brandName` | string | 否 | 品牌名称(部分类目按平台要求是否必填) |
| `shopCollectItemInfo.itemNum` | string | 是 | 货号(最大200字符) |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID(创建时必填，且必须是店铺站点下有效类目) |
| `shopCollectItemInfo.attributes` | array&lt;object> | 否 | 商品属性列表 |
| `shopCollectItemInfo.saleAttributes` | array&lt;object> | 是 | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].id` | string | 是 | 销售属性ID |
| `shopCollectItemInfo.saleAttributes[].name` | string | 是 | 销售属性名称 |
| `shopCollectItemInfo.saleAttributes[].values` | array&lt;object> | 是 | 销售属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].id` | string | 是 | 销售属性值ID(平台值或 mock 值) |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 销售属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].nameZh` | string | 否 | 销售属性中文名称(如颜色) |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU Key(用于与 skuMap 建立映射) |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | SKC 图片列表 |
| `shopCollectItemInfo.saleAttributes[].values[].skcTitle` | string | 否 | SKC 标题 |
| `shopCollectItemInfo.saleAttributes[].values[].multiLanguageSkcTitleMap` | object | 否 | 多语言 SKC 标题映射 |
| `shopCollectItemInfo.saleAttributes[].values[].squareImgUrl` | string | 否 | 方块图 URL |
| `shopCollectItemInfo.saleAttributes[].values[].pieceImgUrl` | string | 否 | 色块图 URL |
| `shopCollectItemInfo.saleAttributes[].values[].proofStockUrls` | array&lt;string> | 否 | 库存证明图片列表 |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 主销售属性供货方货号/卖家 SKU |
| `shopCollectItemInfo.saleAttributes[].values[].suggestedPrice` | number | 否 | 建议售价 |
| `shopCollectItemInfo.saleAttributes[].values[].suggestedPriceCurrency` | string | 否 | 建议售价币种(当 suggestedPrice 有值时必填) |
| `shopCollectItemInfo.saleAttributes[].values[].siteDetailImageInfoList` | array&lt;object> | 否 | 站点图配置列表 |
| `shopCollectItemInfo.saleAttributes[].values[].shelfWay` | integer | 否 | 上架方式(1-自动上架，2-定时上架) |
| `shopCollectItemInfo.saleAttributes[].values[].hopeOnSaleDate` | string | 否 | 期望上架时间(定时上架时必填) |
| `shopCollectItemInfo.saleAttributes[].values[].shelfRequire` | string | 否 | 是否强制上架/货架要求('0'-不到货上架，'1'-到货上架) |
| `shopCollectItemInfo.skuMap` | object | 否 | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |
| `shopCollectItemInfo.sizeChart` | array&lt;object> | 否 | 尺码表 |
| `shopCollectItemInfo.publishSites` | array&lt;string> | 否 | 发布站点列表 示例: ["SHEINUS","SHEINMX"] |
| `shopCollectItemInfo.videoPublishSites` | array&lt;string> | 否 | 视频发布站点列表 |
| `shopCollectItemInfo.imgUrls` | array&lt;string> | 否 | 商品图片列表 |
| `shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL(与 mainImgAppVideoId 二选一传入视频信息即可) |
| `shopCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图应用视频ID |
| `shopCollectItemInfo.isSpuPic` | boolean | 否 | 是否SPU图模式(false-旧版图片模式，true-新版/SPU图片模式) |
| `shopCollectItemInfo.spuImageDetailUrls` | array&lt;string> | 否 | SPU轮播图列表 |
| `shopCollectItemInfo.spuImageSquareUrl` | string | 否 | SPU方图(新版图片模式下，部分类目要求必填) |
| `shopCollectItemInfo.sourceList` | array&lt;object> | 否 | 来源列表 |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID(创建时必填) |
| `shopCollectItemInfo.copyType` | string | 否 | 复制类型 |
| `shopCollectItemInfo.sampleInfo` | array&lt;object> | 否 | 样品信息(当类目要求 sampleInfo 时必填) |
| `shopCollectItemInfo.ipCharacterList` | array&lt;object> | 否 | IP列表(当类目要求 IP 信息时传入) |
| `shopCollectItemInfo.sizeChartHasInit` | integer | 否 | 尺码表是否已初始化(0-未初始化，1-已初始化) |
| `shopCollectItemInfo.hasTranslate` | integer | 否 | 是否已翻译(0-否，1-是) |
| `shopCollectItemInfo.editDisplayConfig` | array&lt;object> | 否 | 编辑展示配置(界面展示辅助字段，如是否显示 skcTitle) |
| `shopCollectItemInfo.isSetSitePrice` | integer | 否 | 半托管是否按站点设置SKU价格(0-否，1-是；仅 shein_choice 使用) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 创建成功的采集箱详情ID |
