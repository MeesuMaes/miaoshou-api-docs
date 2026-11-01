# 编辑采购单


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order`
- 类型：写
- 原文：[479599774e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599774e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |
| `supplierId` | string | 是 | 供应商ID |
| `warehouseId` | string | 是 | 仓库ID |
| `warehouseType` | string | 是 | 仓库类型(self:自营仓,forwarder:货代仓库) |
| `thirdWarehouseProviderAuthId` | string | 否 | 三方仓授权id(仓库类型为forwarder时必填) |
| `gmtPredictArrival` | string | 否 | 预计到货时间 |
| `accountNote` | string | 否 | 采购备注 |
| `goodsShareFeeType` | string | 否 | 费用分摊方式，费用均摊方式1数量,2金额,3重量 |
| `ali1688Payment` | string | 否 | 1688费用 |
| `totalPurchasePrice` | string | 否 | 总采购价格 |
| `discountFee` | string | 否 | 折扣费用 |
| `otherFee` | string | 否 | 其他费用 |
| `shippingFee` | string | 否 |  |
| `goodsSkuList` | array&lt;object> | 否 | 采购商品列表 |
| `goodsSkuList[].goodsPurchaseOrderSkuId` | integer | 否 | 采购单SKU记录ID（编辑时有值） |
| `goodsSkuList[].goodsSkuId` | integer | 是 | 商品SKU ID |
| `goodsSkuList[].purchaseNum` | integer | 是 | 采购数量 |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价 |
| `goodsSkuList[].sourceItemId` | string | 否 | 1688商品ID |
| `goodsSkuList[].sourceSkuId` | string | 否 | 1688 SKU ID |
| `goodsSkuList[].sourceSpecId` | string | 否 | 1688规格ID |
| `goodsSkuList[].sourceImgUrl` | string | 否 | 1688商品图片URL |
| `goodsSkuList[].sourceSkuSubName` | string | 否 | 1688 SKU规格名称 |
| `goodsSkuList[].sourcePrice` | string | 否 | 1688价格 |
| `goodsSkuList[].sourceTitle` | string | 否 | 1688商品标题 |
| `goodsSkuList[].sourceProductUrl` | string | 否 | 1688商品链接 |
| `goodsSkuList[].sourcePurchaseUrl` | string | 否 | 1688采购链接（同 productUrl） |
| `goodsSkuList[].thirdWarehouseGoodsSkuId` | string | 是 | 映射的三方仓商品SKU ID(仓库类型为forwarder时必填) |
| `saveOption` | string | 否 | 存选项save保存,submitAudit提交审核,passAudit提交并通过审核 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsPurchaseOrderInternalSn` | string | 否 | 采购单号 |
