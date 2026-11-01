# AI生成支持的语言map


- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/get_language_name_code_map`
- 类型：处理(生成内容)
- 原文：[482190903e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190903e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.languageNameCodeMap` | object | 否 | 语言名称与语言代码的映射 key: 语言名称（如"繁体中文"、"泰语"） value: 语言代码（如"zh-TW"、"th"） |
