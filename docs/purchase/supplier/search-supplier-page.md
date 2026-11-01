# 获取供应商列表


- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/search_supplier_page`
- 类型：读
- 原文：[479599789e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599789e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `source` | string | 否 | 供应商类型 |
| `settlementMethod` | string | 否 | 结算方式 payBeforeDelivery,payOnDelivery,payPeriod,payWeek,payHalfMonth,payMonth,installment |
| `goodsSupplierId` | integer | 否 | 供应商id |
| `paymentMethod` | string | 否 | 支付方式 bank:银行转账,thirdPay:第三方支付(支付宝等) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supplierList` | array&lt;object> | 否 | 供应商列表 |
| `data.supplierList[].goodsSupplierId` | string | 否 | 供应商ID |
| `data.supplierList[].source` | string | 否 | 供应商类型code |
| `data.supplierList[].shopName` | string | 否 | 供应商名称 |
| `data.supplierList[].homeUrl` | string | 否 | 主页url |
| `data.supplierList[].purchaseUrl` | string | 否 | 采购网址 |
| `data.supplierList[].address` | string | 否 | 详细地址 |
| `data.supplierList[].arrivalDays` | string | 否 | 到货天数 |
| `data.supplierList[].accountNote` | string | 否 | 账户备注 |
| `data.supplierList[].contactName` | string | 否 | 联系人姓名 |
| `data.supplierList[].contactPhone` | string | 否 | 联系人电话 |
| `data.supplierList[].companyPhone` | string | 否 | 公司电话 |
| `data.supplierList[].wangwang` | string | 否 | 淘宝旺旺 |
| `data.supplierList[].email` | string | 否 | 邮箱 |
| `data.supplierList[].qq` | string | 否 | QQ |
| `data.supplierList[].settlementMethod` | string | 否 | 结算方式 |
| `data.supplierList[].paymentMethod` | string | 否 | 付款方式 |
| `data.supplierList[].bankName` | string | 否 | 银行名称 |
| `data.supplierList[].bankCardOwnerName` | string | 否 | 开户名 |
| `data.supplierList[].bankCardNumber` | string | 否 | 银行卡号 |
| `data.supplierList[].totalPurchaseOrderNum` | string | 否 | 采购次数 |
| `data.supplierList[].returnPurchaseGoodsRate` | string | 否 | 退货采购商品率 |
| `data.supplierList[].exceptionPurchaseOrderRate` | string | 否 | 异常采购订单率 |
| `data.supplierList[].supplyTime` | string | 否 | 供货时效 |
| `data.supplierList[].totalPurchaseGoodsNum` | string | 否 | 总采购商品数 |
| `data.supplierList[].returnPurchaseGoodsNum` | string | 否 | 退货采购商品数 |
| `data.supplierList[].exceptionPurchaseOrderNum` | string | 否 | 异常采购订单数 |
| `data.supplierList[].provinceName` | string | 否 | 省名称 |
| `data.supplierList[].cityName` | string | 否 | 市名称 |
| `data.supplierList[].countyName` | string | 否 | 区名称 |
| `data.supplierList[].townName` | string | 否 | 镇名称 |
| `data.supplierList[].fullAddress` | string | 否 | 完整地址 |
| `data.supplierList[].sourceName` | string | 否 | 供应商类型名称 |
| `data.total` | integer | 否 | 总数 |
