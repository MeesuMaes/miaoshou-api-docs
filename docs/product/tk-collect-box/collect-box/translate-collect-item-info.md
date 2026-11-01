# 产品翻译


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/translate_collect_item_info`
- 类型：处理(生成内容)
- 原文：[482189160e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189160e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `sourceLanguage` | string | 是 | 原始语言 可选值：auto(自动识别), zh(简体中文), zh-tw(中繁体), en(英文), th(泰文), vi(越南文), id(印尼文), ms(马来语), es(西班牙文), pt(葡萄牙语), pl(波兰语), fr(法文), bn(孟加拉语), it(意大利文), de(德语), fi(芬兰语), cs(捷克语), ja(日文), he(希伯来语), ur(乌尔都语), uk(乌克兰语), el(希腊语), kk(哈萨克语), nl(荷兰语), sv(瑞典语), ko(韩文), ru(俄文), ar(阿拉伯语), tr(土耳其语), ro(罗马尼亚语), bg(保加利亚语), hu(匈牙利语), se(瑞典语), ga(爱尔兰语) |
| `targetLanguage` | string | 是 | 目标语言 可选值：zh(简体中文), zh-tw(中繁体), en(英文), th(泰文), vi(越南文), id(印尼文), ms(马来语), es(西班牙文), pt(葡萄牙语), pl(波兰语), fr(法文), bn(孟加拉语), it(意大利文), de(德语), fi(芬兰语), cs(捷克语), ja(日文), he(希伯来语), ur(乌尔都语), uk(乌克兰语), el(希腊语), kk(哈萨克语), nl(荷兰语), sv(瑞典语), ko(韩文), ru(俄文), ar(阿拉伯语), tr(土耳其语), ro(罗马尼亚语), bg(保加利亚语), hu(匈牙利语), se(瑞典语), ga(爱尔兰语) |
| `collectItemInfo` | object | 是 | 需翻译的产品详情 |
| `collectItemInfo.title` | string | 否 | 商品标题 |
| `collectItemInfo.notes` | string | 否 | 备注 |
| `collectItemInfo.warrantyPolicy` | string | 否 | 保修政策 |
| `collectItemInfo.skuMap` | object | 否 | SKU Map（key=SKU标识码，value=SKU条目） |
| `collectItemInfo.skuPropertyList` | array&lt;object> | 否 | SKU销售属性列表 |
| `collectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `collectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称 |
| `collectItemInfo.skuPropertyList[].attrValueList` | array&lt;object> | 否 | 属性值列表 |
| `collectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `collectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值 |
| `collectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性图片URL |
| `collectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array&lt;string> | 否 | 补充SKU图片URL列表 |
| `collectItemInfo.productAttributes` | array&lt;object> | 否 | 商品属性列表 |
| `collectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `collectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `collectItemInfo.productAttributes[].attributeValues` | array&lt;object> | 否 | 属性值列表 |
| `collectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `collectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `isTranslateSkuItemNum` | integer | 是 | 是否翻译平台sku（0=否，1=是） |
| `isTranslateSkuProperty` | integer | 是 | 是否翻译SKU规格名称（0=否，1=是） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectItemInfo` | object | 否 | 翻译后的产品详情（只翻译，没有保存翻译后的数据，用户需自行保存） |
