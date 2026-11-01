# 签收记录列表


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order_receive/fetch/search_goods_purchase_order_receive_page`
- 类型：读
- 原文：[479599771e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599771e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `goodsSkuOuterIds` | string | 否 | 商品SKU |
| `goodsSkuOuterIdsRp` | string | 否 | 商品SKU搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsPurchaseOrderNumValue` | string | 否 | 采购单号，运单号 |
| `goodsPurchaseOrderNumRp` | string | 否 | 采购单号，运单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `waybillCode` | string | 否 | 采购物流单号 |
| `waybillCodeRp` | string | 否 | 采购物流单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsPurchaseOrderSnList` | array&lt;string> | 否 | 货源单号 |
| `goodsPurchaseOrderSnListRp` | string | 否 | 货源单号列表搜索类型;(rss:前缀,lss:后缀,ss:模糊,eq:精确) |
| `gmtCreateStart` | string | 否 | 采购单创建日期开始 |
| `gmtCreateEnd` | string | 否 | 采购单创建日期结束 |
| `source` | string | 否 | 来源1688/other |
| `tab` | string | 否 | 订单状态：inDraft:草稿箱;waitAudit:待审核;hasSend:待收货;finish:已完成;cancelAndReturn:已取消、已退货 |
| `goodsSupplierId` | integer | 否 | 供应商ID |
| `warehouseId` | array&lt;integer> | 否 | 收货仓库ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.purchaseOrderReceiveList` | array&lt;object> | 否 | 商品采购订单收货列表 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderId` | string | 否 | 采购单id |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderInternalSn` | string | 否 | 采购单号 |
| `data.purchaseOrderReceiveList[].createSubAppAccountName` | string | 否 | 创建人账号 姓名 |
| `data.purchaseOrderReceiveList[].gmtCreate` | string | 否 | 创建时间 |
| `data.purchaseOrderReceiveList[].gmtModified` | string | 否 | 更新时间 |
| `data.purchaseOrderReceiveList[].receiveInfo` | object | 否 | 签收明细 |
| `data.purchaseOrderReceiveList[].receiveInfo.goodsPurchaseOrderReceiveId` | string | 否 | 签收记录id |
| `data.purchaseOrderReceiveList[].receiveInfo.createSubAppAccountName` | string | 否 | 签收人姓名（子账号时展示） |
| `data.purchaseOrderReceiveList[].receiveInfo.gmtCreate` | string | 否 | 创建时间 |
| `data.purchaseOrderReceiveList[].receiveInfo.gmtReceive` | string | 否 | 签收时间 |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList` | array&lt;object> | 否 | 签收sku列表 |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].goodsPurchaseOrderReceiveSkuId` | string | 否 | ID |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].currentReceiveNum` | string | 否 | 本次签收数量 |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].warehouseShelfCellId` | string | 否 | 签收仓位id |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].goodsSkuId` | string | 否 | sku id |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo` | object | 否 | sku信息 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier` | object | 否 | 供应商 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.shopName` | string | 否 | 供货商名称 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.sellerId` | string | 否 | 供货商 ID |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.homeUrl` | string | 否 | 供货商店铺主页（有值时名称可点击跳转） |
| `data.purchaseOrderReceiveList[].shippingList` | array&lt;object> | 否 | 运单列表 |
| `data.purchaseOrderReceiveList[].shippingList[].goodsPurchaseOrderShippingId` | string | 否 | 运单 ID |
| `data.purchaseOrderReceiveList[].shippingList[].goodsPurchaseOrderId` | string | 否 | 关联采购单 ID |
| `data.purchaseOrderReceiveList[].shippingList[].platformOrderSn` | string | 否 | 货源单号 |
| `data.purchaseOrderReceiveList[].shippingList[].platformOrderStatus` | string | 否 | 平台订单状态 |
| `data.purchaseOrderReceiveList[].shippingList[].platformBuyer` | string | 否 | 平台买家账号 |
| `data.purchaseOrderReceiveList[].shippingList[].platformOrderStartTime` | string | 否 | 平台下单时间 |
| `data.purchaseOrderReceiveList[].shippingList[].platform` | string | 否 | 物流平台标识 |
| `data.purchaseOrderReceiveList[].shippingList[].platformName` | string | 否 | 物流平台名称 |
| `data.purchaseOrderReceiveList[].shippingList[].purchaseOrderDetailUrl` | string | 否 | 1688采购订单详情链接 |
| `data.purchaseOrderReceiveList[].shippingList[].platformOrderFullAddress` | string | 否 | 平台订单收货地址 |
| `data.purchaseOrderReceiveList[].shippingList[].platformOrderOriginStatus` | string | 否 | 1688订单状态 |
| `data.purchaseOrderReceiveList[].shippingList[].platformOrderOriginStatusText` | string | 否 | 平台订单原始状态文案（1688 订单状态展示） |
| `data.purchaseOrderReceiveList[].shippingList[].resellerAccount` | string | 否 | 买家账号 |
| `data.purchaseOrderReceiveList[].shippingList[].packageList` | array&lt;object> | 否 | 快递包裹列表 |
| `data.purchaseOrderReceiveList[].shippingList[].packageList[].goodsPurchaseOrderShippingPackageId` | string | 否 | 包裹 ID |
| `data.purchaseOrderReceiveList[].shippingList[].packageList[].goodsPurchaseOrderShippingId` | string | 否 | ID |
| `data.purchaseOrderReceiveList[].shippingList[].packageList[].goodsPurchaseOrderId` | string | 否 | 物流id |
| `data.purchaseOrderReceiveList[].shippingList[].packageList[].logisticsName` | string | 否 | 物流公司名称 |
| `data.purchaseOrderReceiveList[].shippingList[].packageList[].waybillCode` | string | 否 | 快递单号 |
| `data.purchaseOrderReceiveList[].shippingList[].packageList[].contactPhone` | string | 否 | 联系手机号 |
| `data.purchaseOrderReceiveList[].warehouse` | object | 否 | 仓库 |
| `data.purchaseOrderReceiveList[].warehouse.warehouseName` | string | 否 | 收货仓库名称 |
| `data.purchaseOrderReceiveList[].warehouse.fullAddress` | string | 否 | 仓库地址 |
| `data.purchaseOrderReceiveList[].warehouse.contactName` | string | 否 | 仓库联系人 |
| `data.purchaseOrderReceiveList[].warehouse.contactPhone` | string | 否 | 仓库联系电话 |
| `data.total` | integer | 否 | 总计 |
