# 查询出入库记录列表


- 层级：开放平台 > 仓储 > 出入库
- 方法+路径：`POST /open/v1/ewm/goods_out_in/fetch/search_goods_sku_warehouse_log_page`
- 类型：读
- 原文：[532434240e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/532434240e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 | 页数,默认1 |
| `pageSize` | integer | 是 | 每页数量,默认20 |
| `warehouseId` | integer | 否 | 仓库ID |
| `outInType` | string | 否 | 出入库类型;(in:入库,out:出库) |
| `bizCode` | string | 否 | 业务类型;(purchase_in_storage:采购入库,manual_purchase_in_storage:手动采购入库,allocate_in_storage:调拨入库,inventory_profit_in_storage:盘盈入库,manual_return_in_storage:手动退货入库,sale_out_storage:销售出库,manual_sale_out_storage:手动销售出库,allocate_out_storage:调拨出库,inventory_loss_out_storage:盘亏出库,manual_return_out_storage:手动退货出库) |
| `goodsSkuOuterIds` | string | 否 | 商品SKU编码,多个以逗号分隔 |
| `goodsSkuOuterIdsRp` | string | 否 | 商品SKU编码搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `bizNos` | string | 否 | 出入库单号,多个以逗号分隔 |
| `bizNosRp` | string | 否 | 出入库单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `platformOrderSns` | string | 否 | 订单号,多个以逗号分隔 |
| `platformOrderSnsRp` | string | 否 | 订单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `goodsPurchaseOrderInternalSn` | string | 否 | 采购单号,多个以逗号分隔 |
| `goodsPurchaseOrderInternalSnRp` | string | 否 | 采购单号搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `warehouseShelfCellCode` | string | 否 | 仓位 |
| `warehouseShelfCellCodeRp` | string | 否 | 仓位搜索类型:rss(前缀),lss(后缀),ss(模糊),eq(精确) |
| `gmtCreateStart` | string | 否 | 出入库开始时间(Y-m-d H:i:s) 不填默认最近90天 |
| `gmtCreateEnd` | string | 否 | 出入库结束时间(Y-m-d H:i:s) 不填默认最近90天 |
| `operateSubAccountId` | integer | 否 | 操作员子账号ID |
| `shopName` | string | 否 | 店铺名称 |
| `note` | string | 否 | 备注 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsSkuWarehouseLogList` | array&lt;object> | 否 | 出入库记录列表 |
| `data.goodsSkuWarehouseLogList[].goodsSkuWarehouseId` | integer | 否 | 商品SKU库存id |
| `data.goodsSkuWarehouseLogList[].bizCode` | string | 否 | 业务类型编码;(purchase_in_storage:采购入库,manual_purchase_in_storage:手动采购入库,allocate_in_storage:调拨入库,inventory_profit_in_storage:盘盈入库,manual_return_in_storage:手动退货入库,sale_out_storage:销售出库,manual_sale_out_storage:手动销售出库,allocate_out_storage:调拨出库,inventory_loss_out_storage:盘亏出库,manual_return_out_storage:手动退货出库) |
| `data.goodsSkuWarehouseLogList[].bizName` | string | 否 | 业务类型名称 |
| `data.goodsSkuWarehouseLogList[].bizNo` | string | 否 | 出入库单号 |
| `data.goodsSkuWarehouseLogList[].bizRelatedId` | integer | 否 | 业务关联ID(采购单/订单/调拨单/盘点单等主键) |
| `data.goodsSkuWarehouseLogList[].warehouseName` | string | 否 | 仓库名称 |
| `data.goodsSkuWarehouseLogList[].warehouseShelfCellCodesStr` | string | 否 | 仓位编码(逗号分隔) |
| `data.goodsSkuWarehouseLogList[].warehouseZoneNames` | array&lt;string> | 否 | 仓位区域名称列表 |
| `data.goodsSkuWarehouseLogList[].goodsName` | string | 否 | 商品名称 |
| `data.goodsSkuWarehouseLogList[].goodsSkuSubName` | string | 否 | 商品SKU名称 |
| `data.goodsSkuWarehouseLogList[].goodsSkuOuterId` | string | 否 | 商品SKU编码 |
| `data.goodsSkuWarehouseLogList[].logoUrl` | string | 否 | 商品主图URL |
| `data.goodsSkuWarehouseLogList[].isDelete` | integer | 否 | 商品是否已删除(0:未删除,1:已删除) |
| `data.goodsSkuWarehouseLogList[].beforeStockNum` | integer | 否 | 变更前库存 |
| `data.goodsSkuWarehouseLogList[].changeStockNum` | integer | 否 | 变更库存(正数入库/负数出库) |
| `data.goodsSkuWarehouseLogList[].afterStockNum` | integer | 否 | 变更后库存 |
| `data.goodsSkuWarehouseLogList[].prePurchasePrice` | string | 否 | 变更前采购价 |
| `data.goodsSkuWarehouseLogList[].purchasePrice` | string | 否 | 变更后采购价 |
| `data.goodsSkuWarehouseLogList[].outInPurchasePrice` | string | 否 | 本次出入库单价 |
| `data.goodsSkuWarehouseLogList[].changePrice` | string | 否 | 本次变更金额 |
| `data.goodsSkuWarehouseLogList[].goodsPurchaseOrderInternalSn` | string | 否 | 采购单内部编号 |
| `data.goodsSkuWarehouseLogList[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.goodsSkuWarehouseLogList[].thirdWarehouseStockOrderSn` | string | 否 | 三方仓出库单号 |
| `data.goodsSkuWarehouseLogList[].warehouseTakeStockTaskSn` | string | 否 | 盘点任务单号 |
| `data.goodsSkuWarehouseLogList[].deliveryOrderSn` | string | 否 | 发货单号 |
| `data.goodsSkuWarehouseLogList[].returnSn` | string | 否 | 退货单号 |
| `data.goodsSkuWarehouseLogList[].shopNick` | string | 否 | 店铺昵称 |
| `data.goodsSkuWarehouseLogList[].operatorName` | string | 否 | 操作员名称 |
| `data.goodsSkuWarehouseLogList[].note` | string | 否 | 备注 |
| `data.goodsSkuWarehouseLogList[].gmtCreate` | string | 否 | 创建时间 |
| `data.total` | integer | 否 | 总记录数 |
| `data.page` | integer | 否 | 当前页数 |
| `data.pageSize` | integer | 否 | 每页数量 |
