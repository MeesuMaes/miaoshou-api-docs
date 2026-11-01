# 根据站点获取运费模板(物流方式)


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_logistic_options_by_site`
- 类型：读
- 原文：[516157445e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157445e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.label` | string | 否 | 物流选项标签 |
| `data.value` | string | 否 | 物流选项值 |
| `data.feeType` | string | 否 | 运费类型 |
| `data.isEnableEditShippingFee` | boolean | 否 | 是否允许编辑运费 |
