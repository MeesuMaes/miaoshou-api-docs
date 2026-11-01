# 获取采购单列表


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/fetch/search_goods_purchase_order_page`
- 类型：读
- 原文：[479599781e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599781e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsPurchaseOrderList` | array&lt;object> | 否 | 商品采购订单列表 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderId` | integer | 否 | 采购单ID |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderInternalSn` | string | 否 | 采购单号 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSn` | string | 否 | 1688货源单号；有值代表已下1688单 |
| `data.goodsPurchaseOrderList[].goodsPurchasePlatform` | string | 否 | 采购平台标识 other/1688 |
| `data.goodsPurchaseOrderList[].status` | string | 否 | 订单状态 |
| `data.goodsPurchaseOrderList[].goodsPurchaseTotalPrice` | string | 否 | 商品总采购价 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderAmount` | string | 否 | 订单应付金额 |
| `data.goodsPurchaseOrderList[].shippingFee` | string | 否 | 运费 |
| `data.goodsPurchaseOrderList[].otherFee` | string | 否 | 其他费用 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderDiscount` | string | 否 | 折扣金额 |
| `data.goodsPurchaseOrderList[].confirmPaymentAmount` | string | 否 | 已付款金额 |
| `data.goodsPurchaseOrderList[].applyPaymentAmount` | string | 否 | 已申请付款金额 |
| `data.goodsPurchaseOrderList[].goodsPurchaseTotalNum` | string | 否 | 采购总数量 |
| `data.goodsPurchaseOrderList[].gmtCreate` | string | 否 | 创建时间 |
| `data.goodsPurchaseOrderList[].gmtPredictArrival` | string | 否 | 预计到货时间 |
| `data.goodsPurchaseOrderList[].createSubAppAccountName` | string | 否 | 创建人（采购员）姓名 |
| `data.goodsPurchaseOrderList[].resellerAccount` | string | 否 | 1688货源账号 |
| `data.goodsPurchaseOrderList[].accountNote` | string | 否 | 备注内容 |
| `data.goodsPurchaseOrderList[].auditReason` | string | 否 | 审核不通过原因 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSupplier` | object | 否 | 供货商信息 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSupplier.shopName` | string | 否 | 供货商名称 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSupplier.sellerId` | string | 否 | 供货商 ID |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSupplier.homeUrl` | string | 否 | 供货商店铺主页（有值时名称可点击跳转） |
| `data.goodsPurchaseOrderList[].warehouse` | object | 否 | 收货仓库信息 |
| `data.goodsPurchaseOrderList[].warehouse.warehouseName` | string | 否 | 收货仓库名称 |
| `data.goodsPurchaseOrderList[].warehouse.fullAddress` | string | 否 | 仓库地址 |
| `data.goodsPurchaseOrderList[].warehouse.contactName` | string | 否 | 仓库联系人 |
| `data.goodsPurchaseOrderList[].warehouse.contactPhone` | string | 否 | 仓库联系电话 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList` | array&lt;object> | 否 | SKU 明细列表 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsPurchaseOrderSkuId` | integer | 否 | ID |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsSkuId` | string | 否 | 商品 SKU ID |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsSkuSubName` | string | 否 | 规格名称 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].goodsSkuOuterId` | string | 否 | 商品 SKU |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].logoUrl` | string | 否 | 商品图片 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].purchaseNum` | string | 否 | 采购数量 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].purchasePrice` | string | 否 | 采购单价 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].receiveNum` | string | 否 | 已收货数量（到货量列及到货量汇总用） |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].totalPurchasePrice` | string | 否 | SKU 小计金额 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].ali1688SkuInfo` | object | 否 | 1688 SKU 信息（1688 采购单专用） |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].ali1688SkuInfo.imgUrl` | string | 否 | 1688 商品图片 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].ali1688SkuInfo.title` | string | 否 | 1688 商品标题 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].ali1688SkuInfo.productUrl` | string | 否 | 1688 商品链接 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].ali1688SkuInfo.skuSubName` | string | 否 | 1688 规格名称 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList[].ali1688SkuInfo.quantity` | integer | 否 | 1688 侧采购数量（摘要区件数汇总用） |
| `data.goodsPurchaseOrderList[].shippingList` | array&lt;object> | 否 | 运单信息列表 |
| `data.goodsPurchaseOrderList[].shippingList[].goodsPurchaseOrderShippingId` | string | 否 | 运单 ID |
| `data.goodsPurchaseOrderList[].shippingList[].goodsPurchaseOrderId` | string | 否 | 关联采购单 ID |
| `data.goodsPurchaseOrderList[].shippingList[].platformOrderSn` | string | 否 | 货源单号 |
| `data.goodsPurchaseOrderList[].shippingList[].platformOrderStatus` | string | 否 | 平台订单状态 |
| `data.goodsPurchaseOrderList[].shippingList[].platformBuyer` | string | 否 | 平台买家账号 |
| `data.goodsPurchaseOrderList[].shippingList[].platformOrderStartTime` | string | 否 | 平台下单时间 |
| `data.goodsPurchaseOrderList[].shippingList[].platform` | string | 否 | 物流平台标识 |
| `data.goodsPurchaseOrderList[].shippingList[].platformName` | string | 否 | 物流平台名称 |
| `data.goodsPurchaseOrderList[].shippingList[].purchaseOrderDetailUrl` | string | 否 | 1688采购订单详情链接 |
| `data.goodsPurchaseOrderList[].shippingList[].platformOrderFullAddress` | string | 否 | 平台订单收货地址 |
| `data.goodsPurchaseOrderList[].shippingList[].platformOrderOriginStatus` | string | 否 | 1688订单状态 |
| `data.goodsPurchaseOrderList[].shippingList[].platformOrderOriginStatusText` | string | 否 | 平台订单原始状态文案（1688 订单状态展示） |
| `data.goodsPurchaseOrderList[].shippingList[].resellerAccount` | string | 否 | 买家账号 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList` | array&lt;object> | 否 | 快递包裹列表 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].goodsPurchaseOrderShippingPackageId` | string | 否 | 包裹 ID |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].goodsPurchaseOrderShippingId` | string | 否 | ID |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].goodsPurchaseOrderId` | string | 否 | 物流id |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].logisticsName` | string | 否 | 物流公司名称 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].waybillCode` | string | 否 | 快递单号 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].contactPhone` | string | 否 | 联系手机号 |
| `data.goodsPurchaseOrderList[].financePaymentList` | array&lt;object> | 否 | 付款申请记录列表 |
| `data.goodsPurchaseOrderList[].financePaymentList[].id` | string | 否 | id |
| `data.goodsPurchaseOrderList[].financePaymentList[].paymentId` | string | 否 | 申请记录id |
| `data.goodsPurchaseOrderList[].financePaymentList[].paymentSn` | string | 否 | 付款申请单号 |
| `data.goodsPurchaseOrderList[].financePaymentList[].paymentAmount` | string | 否 | 申请付款金额 |
| `data.goodsPurchaseOrderList[].financePaymentList[].status` | string | 否 | 付款申请状态 |
| `data.goodsPurchaseOrderList[].financePaymentList[].statusText` | string | 否 | 付款申请状态文案 |
| `data.goodsPurchaseOrderList[].fianceReceiptList` | array&lt;object> | 否 | 退款收款记录列表 |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].id` | string | 否 | id |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].receiptSn` | string | 否 | 收款单号 |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].receiptAmount` | string | 否 | 收款金额 |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].statusText` | string | 否 | 收款状态文案 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList` | array&lt;object> | 否 | 变更单记录列表 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].goodsPurchaseOrderModifyId` | string | 否 | 变更单 ID |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].goodsPurchaseOrderModifySn` | string | 否 | 变更单编号 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].status` | string | 否 | 变更单状态 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].statusText` | string | 否 | 变更单状态文案 |
| `data.total` | integer | 否 | 总计 |
