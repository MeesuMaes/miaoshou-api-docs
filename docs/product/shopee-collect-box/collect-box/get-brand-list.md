# 获取品牌列表


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_brand_list`
- 类型：读
- 原文：[516157444e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157444e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.isMandatory` | boolean | 否 | 品牌是否必填 |
| `data.inputType` | string | 否 | 输入类型 |
| `data.brandList` | array&lt;object> | 否 | 品牌列表 |
| `data.brandList[].brandId` | integer | 否 | 品牌ID |
| `data.brandList[].brandName` | string | 否 | 品牌名称 |
| `data.gmtModified` | string | 否 | 最后修改时间 |
| `data.isFromOss` | boolean | 否 | 是否来自OSS缓存 |
