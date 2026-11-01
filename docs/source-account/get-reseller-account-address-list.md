# 获取账号地址列表


- 层级：开放平台 > 货源账号
- 方法+路径：`POST /open/v1/resell_account/fetch/get_reseller_account_address_list`
- 类型：读
- 原文：[479848084e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479848084e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `resellerAccountId` | integer | 是 | 采购账号id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.resellerAccountAddressList` | array&lt;object> | 否 |  |
| `data.resellerAccountAddressList[].provinceId` | string | 否 | 省ID |
| `data.resellerAccountAddressList[].cityId` | string | 否 | 市ID |
| `data.resellerAccountAddressList[].countyId` | string | 否 | 区县ID |
| `data.resellerAccountAddressList[].townId` | string | 否 | 镇街ID |
| `data.resellerAccountAddressList[].province` | string | 否 | 省 |
| `data.resellerAccountAddressList[].city` | string | 否 | 市 |
| `data.resellerAccountAddressList[].county` | string | 否 | 区县 |
| `data.resellerAccountAddressList[].town` | string | 否 | 镇街 |
| `data.resellerAccountAddressList[].fullname` | string | 否 | 姓名 |
| `data.resellerAccountAddressList[].mobile` | string | 否 | 手机 |
| `data.resellerAccountAddressList[].telephone` | string | 否 | 电话 |
| `data.resellerAccountAddressList[].address` | string | 否 | 地址 |
