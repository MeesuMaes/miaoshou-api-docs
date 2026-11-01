# 妙手开放平台 · 货源账号模块

> 由 apifox 分享文档整理（2 个接口）。字段说明原样摘自 OpenAPI 定义，未做改写；请求/响应以原文为准。

## 目录

- -（2）

## -

### 获取货源账号列表

- 层级：开放平台 > 货源账号
- 方法+路径：`POST /open/v1/resell_account/fetch/search_reseller_account_page`
- 类型：读
- 原文：[479848083e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479848083e0.md)（本地 raw/479848083e0_获取货源账号列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.resellerAccountList` | array<object> | 否 |  |
| `data.resellerAccountList[].resellerAccountId` | string | 否 | ID |
| `data.resellerAccountList[].resellerId` | string | 否 | 账号ID |
| `data.resellerAccountList[].resellerAccount` | string | 否 | 1688账号名称 |
| `data.resellerAccountList[].resellerNick` | string | 否 | 1688昵称 |
| `data.resellerAccountList[].platform` | string | 否 | 平台 |
| `data.resellerAccountList[].authStatus` | string | 否 | 授权状态 |
| `data.resellerAccountList[].status` | string | 否 | 状态 |
| `data.resellerAccountList[].gmtLastAuth` | string | 否 | 最后认证时间 |
| `data.resellerAccountList[].gmtCreate` | string | 否 | 创建时间 |
| `data.resellerAccountList[].gmtModified` | string | 否 | 修改时间 |
| `data.resellerAccountList[].gmtExpire` | string | 否 | 过期时间 |
| `data.total` | integer | 否 | 总计 |


---

### 获取账号地址列表

- 层级：开放平台 > 货源账号
- 方法+路径：`POST /open/v1/resell_account/fetch/get_reseller_account_address_list`
- 类型：读
- 原文：[479848084e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479848084e0.md)（本地 raw/479848084e0_获取账号地址列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `data.resellerAccountAddressList` | array<object> | 否 |  |
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

