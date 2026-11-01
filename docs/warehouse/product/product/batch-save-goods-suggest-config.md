# 安全库存批量设置


- 层级：开放平台 > 仓储 > 商品 > 商品
- 方法+路径：`POST /open/v1/ewm/goods/goods/operate/batch_save_goods_suggest_config`
- 类型：写
- 原文：[479599766e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599766e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSuggestConfigList` | array&lt;object> | 否 | 商品建议配置列表 |
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
