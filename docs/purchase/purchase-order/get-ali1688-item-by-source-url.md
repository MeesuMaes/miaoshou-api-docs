# 根据货源链接获取1688商品SKU列表


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/get_ali1688_item_by_source_url`
- 类型：读
- 原文：[532434244e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/532434244e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `sourceUrl` | string | 是 | 1688货源链接 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuList` | array&lt;object> | 否 | 商品列表信息 |
| `data.goodsSkuList[].sourceItemId` | string | 否 | 1688商品ID |
| `data.goodsSkuList[].sourceSkuId` | string | 否 | 1688 SKU ID |
| `data.goodsSkuList[].sourceSpecId` | string | 否 | 1688规格ID |
| `data.goodsSkuList[].sourceImgUrl` | string | 否 | 1688商品图片URL |
| `data.goodsSkuList[].sourceSkuSubName` | string | 否 | 1688 SKU规格名称 |
| `data.goodsSkuList[].sourcePrice` | string | 否 | 1688价格 |
| `data.goodsSkuList[].purchasePrice` | string | 否 | 采购价格 |
| `data.goodsSkuList[].sourceTitle` | string | 否 | 1688商品标题 |
| `data.goodsSkuList[].sourceProductUrl` | string | 否 | 1688商品链接 |
