# 创建供应商


- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/operate/add_supplier`
- 类型：写
- 原文：[479653198e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479653198e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopName` | string | 是 | 供应商名称 |
| `source` | string | 是 | 供应商类型code |
| `homeUrl` | string | 否 | 主页网址 |
| `purchaseUrl` | string | 否 | 采购网址 |
| `arrivalDays` | string | 否 | 到货周期 |
| `accountNote` | string | 否 | 备注信息 |
| `address` | string | 否 | 地址 |
| `contactName` | string | 否 | 联系人姓名 |
| `contactPhone` | string | 否 | 联系人电话 |
| `companyPhone` | string | 否 | 公司电话 |
| `wangwang` | string | 否 | 网旺号 |
| `email` | string | 否 | 邮箱 |
| `qq` | string | 否 | QQ |
| `settlementMethod` | string | 否 | 结算方式 |
| `paymentMethod` | string | 否 | 付款方式 |
| `bankName` | string | 否 | 银行名称 |
| `bankCardNumber` | string | 否 | 银行账号 |
| `bankCardOwnerName` | string | 否 | 开户人姓名 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.@api` | object | 否 | POST |
