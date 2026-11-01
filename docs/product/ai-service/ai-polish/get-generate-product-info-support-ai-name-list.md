# 获取支持的AI名称列表


- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/get_generate_product_info_support_ai_name_list`
- 类型：读
- 原文：[482190904e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190904e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.aiNameList` | array&lt;string> | 否 | 支持的AI名称列表 可选值：deepSeekR1/douBao1.6/tongYiQianWen |
