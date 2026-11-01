# 获取供应商类型列表


- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/get_supplier_platform_list`
- 类型：读
- 原文：[479599791e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599791e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supplierPlatformOptions` | array&lt;object> | 否 |  |
| `data.supplierPlatformOptions[].label` | string | 否 | 供应商类型名称 |
| `data.supplierPlatformOptions[].value` | string | 否 | 供应商类型code |
