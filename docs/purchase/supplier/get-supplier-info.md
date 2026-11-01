# 获取供应商信息


- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/get_supplier_info`
- 类型：读
- 原文：[479599790e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599790e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSupplierId` | integer | 是 | 供应商id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supplierDetail` | object | 否 | 供应商详情 |
| `data.supplierDetail.goodsSupplierId` | string | 否 | 供应商ID |
| `data.supplierDetail.source` | string | 否 | 供应商类型code |
| `data.supplierDetail.shopName` | string | 否 | 供应商名称 |
| `data.supplierDetail.homeUrl` | string | 否 | 主页url |
| `data.supplierDetail.purchaseUrl` | string | 否 | 采购网址 |
| `data.supplierDetail.address` | string | 否 | 详细地址 |
| `data.supplierDetail.arrivalDays` | string | 否 | 到货天数 |
| `data.supplierDetail.accountNote` | string | 否 | 账户备注 |
| `data.supplierDetail.contactName` | string | 否 | 联系人姓名 |
| `data.supplierDetail.contactPhone` | string | 否 | 联系人电话 |
| `data.supplierDetail.companyPhone` | string | 否 | 公司电话 |
| `data.supplierDetail.wangwang` | string | 否 | 淘宝旺旺 |
| `data.supplierDetail.email` | string | 否 | 邮箱 |
| `data.supplierDetail.qq` | string | 否 | QQ |
| `data.supplierDetail.settlementMethod` | string | 否 | 结算方式 |
| `data.supplierDetail.paymentMethod` | string | 否 | 付款方式 |
| `data.supplierDetail.bankName` | string | 否 | 银行名称 |
| `data.supplierDetail.bankCardOwnerName` | string | 否 | 开户名 |
| `data.supplierDetail.bankCardNumber` | string | 否 | 银行卡号 |
| `data.supplierDetail.totalPurchaseOrderNum` | string | 否 | 采购次数 |
| `data.supplierDetail.returnPurchaseGoodsRate` | string | 否 | 退货采购商品率 |
| `data.supplierDetail.exceptionPurchaseOrderRate` | string | 否 | 异常采购订单率 |
| `data.supplierDetail.supplyTime` | string | 否 | 供货时效 |
| `data.supplierDetail.totalPurchaseGoodsNum` | string | 否 | 总采购商品数 |
| `data.supplierDetail.returnPurchaseGoodsNum` | string | 否 | 退货采购商品数 |
| `data.supplierDetail.exceptionPurchaseOrderNum` | string | 否 | 异常采购订单数 |
| `data.supplierDetail.provinceName` | string | 否 | 省名称 |
| `data.supplierDetail.cityName` | string | 否 | 市名称 |
| `data.supplierDetail.countyName` | string | 否 | 区名称 |
| `data.supplierDetail.townName` | string | 否 | 镇名称 |
| `data.supplierDetail.fullAddress` | string | 否 | 完整地址 |
| `data.supplierDetail.sourceName` | string | 否 | 供应商类型名称 |
