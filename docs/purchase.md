# 妙手开放平台 · 采购模块

> 由 apifox 分享文档整理（17 个接口）。字段说明原样摘自 OpenAPI 定义，未做改写；请求/响应以原文为准。

## 目录

- 采购单（12）
- 供应商（5）

## 采购单

### 添加采购单

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order`
- 类型：写
- 原文：[479599772e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599772e0.md)（本地 raw/479599772e0_添加采购单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `supplierId` | string | 是 | 供应商ID |
| `warehouseId` | string | 是 | 仓库ID |
| `warehouseType` | string | 是 | 仓库类型(self:自营仓,forwarder:货代仓库) |
| `thirdWarehouseProviderAuthId` | string | 否 | 三方仓授权id(仓库类型为forwarder时必填) |
| `gmtPredictArrival` | string | 否 | 预计到货时间 |
| `accountNote` | string | 否 | 采购备注 |
| `goodsShareFeeType` | string | 是 | 费用分摊方式，费用均摊方式1数量,2金额,3重量 |
| `otherFee` | string | 否 |  |
| `shippingFee` | string | 否 | 其他费用 |
| `goodsSkuList` | array<object> | 是 | 采购商品列表 |
| `goodsSkuList[].goodsSkuId` | integer | 是 | 商品SKU ID |
| `goodsSkuList[].purchaseNum` | integer | 是 | 采购数量 |
| `goodsSkuList[].purchasePrice` | string | 是 | 采购单价 |
| `goodsSkuList[].thirdWarehouseGoodsSkuId` | string | 否 | 映射的三方仓商品SKU ID(仓库类型为forwarder时必填) |
| `saveOption` | string | 是 | 存选项save保存,submitAudit提交审核,passAudit提交并通过审核 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsPurchaseOrderInternalSn` | string | 否 | 采购单号 |


---

### 创建1688采购单

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order`
- 类型：写
- 原文：[479599773e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599773e0.md)（本地 raw/479599773e0_创建1688采购单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderList` | array<object> | 是 | 采购单列表（可批量） |
| `goodsPurchaseOrderList[].resellerAccountId` | string | 是 | 1688采购账号ID |
| `goodsPurchaseOrderList[].supplierId` | string | 是 | 供应商ID |
| `goodsPurchaseOrderList[].warehouseId` | string | 是 | 收货仓库ID |
| `goodsPurchaseOrderList[].warehouseType` | string | 是 | 仓库类型(self:自营仓,forwarder:货代仓库) |
| `goodsPurchaseOrderList[].thirdWarehouseProviderAuthId` | string | 否 | 三方仓授权id(仓库类型为forwarder时必填) |
| `goodsPurchaseOrderList[].shippingFee` | string | 否 | 采购运费 |
| `goodsPurchaseOrderList[].otherFee` | string | 否 | 其他费用 |
| `goodsPurchaseOrderList[].discountFee` | string | 否 | 优惠金额 |
| `goodsPurchaseOrderList[].goodsShareFeeType` | string | 是 | 费用均摊方式：'1'(按数量) / '2'(按金额) / '3'(按重量) |
| `goodsPurchaseOrderList[].gmtPredictArrival` | string | 否 | 预计到货日期 |
| `goodsPurchaseOrderList[].accountNote` | string | 否 | 采购备注 |
| `goodsPurchaseOrderList[].buyerRemark` | string | 否 | 买家留言（1688下单用） |
| `goodsPurchaseOrderList[].flow` | string | 是 | 下单方式：general-批发、fenxiao-代发 |
| `goodsPurchaseOrderList[].consigneeInfo` | object | 是 | 收货地址信息 |
| `goodsPurchaseOrderList[].consigneeInfo.province` | string | 是 | 省 |
| `goodsPurchaseOrderList[].consigneeInfo.city` | string | 是 | 市 |
| `goodsPurchaseOrderList[].consigneeInfo.county` | string | 否 | 区 |
| `goodsPurchaseOrderList[].consigneeInfo.town` | string | 否 | 镇 |
| `goodsPurchaseOrderList[].consigneeInfo.fullname` | string | 是 | 全名 |
| `goodsPurchaseOrderList[].consigneeInfo.mobile` | string | 是 | 手机 |
| `goodsPurchaseOrderList[].consigneeInfo.address` | string | 是 | 地址 |
| `goodsPurchaseOrderList[].goodsSkuList` | array<object> | 是 | 商品列表信息 |
| `goodsPurchaseOrderList[].goodsSkuList[].goodsSkuId` | integer | 是 | 商品SKU ID |
| `goodsPurchaseOrderList[].goodsSkuList[].purchaseNum` | integer | 是 | 采购数量 |
| `goodsPurchaseOrderList[].goodsSkuList[].purchasePrice` | string | 是 | 采购单价 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceItemId` | string | 否 | 1688商品ID |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceSkuId` | string | 否 | 1688 SKU ID |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceSpecId` | string | 否 | 1688规格ID |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceImgUrl` | string | 否 | 1688商品图片URL |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceSkuSubName` | string | 否 | 1688 SKU规格名称 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourcePrice` | string | 否 | 1688价格 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceTitle` | string | 否 | 1688商品标题 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourceProductUrl` | string | 否 | 1688商品链接 |
| `goodsPurchaseOrderList[].goodsSkuList[].sourcePurchaseUrl` | string | 否 | 1688采购链接（同 productUrl） |
| `goodsPurchaseOrderList[].goodsSkuList[].thirdWarehouseGoodsSkuId` | string | 否 | 映射的三方仓商品SKU ID(仓库类型为forwarder时必填) |
| `saveOption` | string | 是 | 保存选项：save-保存到草稿箱，create1688Order-保存并下单 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successDataList` | object | 否 | 成功数据列表 |
| `data.successDataList.index` | string | 否 | 序号 |
| `data.successDataList.goodsPurchaseOrderSn` | string | 否 | 采购单号；【goodsPurchaseOrderInternalSn】含义相同 |
| `data.successDataList.purchaseOrderSn` | string | 否 | 1688单号 |
| `data.successDataList.goodsPurchaseOrderId` | string | 否 | 采购单ID |
| `data.errors` | object | 否 | 错误数据列表 |
| `data.errors.index` | string | 否 | 序号 |
| `data.errors.errorMsg` | string | 否 | 错误信息 |
| `data.errors.errorType` | string | 否 | 错误类型 |
| `data.errors.goodsPurchaseOrderSn` | string | 否 | 采购单号；【goodsPurchaseOrderInternalSn】含义相同 |
| `data.errors.purchaseOrderSn` | string | 否 | 1688单号 |
| `data.errors.goodsPurchaseOrderId` | string | 否 | 采购单ID |
| `data.successGoodsPurchaseOrderIds` | array<integer> | 否 | 成功的采购订单ID列表 |


<details><summary>请求示例</summary>

```json
{
  "goodsPurchaseOrderList": [
    {
      "resellerAccountId": "77650",
      "supplierId": "552956",
      "warehouseId": "1520732",
      "goodsShareFeeType": "2",
      "flow": "fenxiao",
      "consigneeInfo": {
        "province": "北京市",
        "city": "市辖区",
        "county": "朝阳区",
        "town": "左家庄街道",
        "fullname": "123",
        "mobile": "12343145351",
        "address": "cs",
        "fullAddress": "北京市市辖区朝阳区左家庄街道cs"
      },
      "goodsSkuList": [
        {
          "goodsSkuId": 337,
          "purchaseNum": 1,
          "purchasePrice": "19.9",
          "totalPurchasePrice": "19.9",
          "matchMethod": "current",
          "sourceItemId": "798612328767",
          "sourceSkuId": "5612944915631",
          "sourceSpecId": "d17349bf1623a54994ffb3c350509beb",
          "sourceImgUrl": "https://img.china.alibaba.com/img/ibank/O1CN01RFGytj20IMVFjcJc5_!!2210908056826-0-cib.jpg",
          "sourceSkuSubName": "粉色 均码",
          "sourceTitle": "法式冰丝镂空针织衫女夏季新款不规则设计感小众短袖T恤短款上衣",
          "sourceProductUrl": "https://detail.1688.com/offer/798612328767.html",
          "sourcePurchaseUrl": "https://detail.1688.com/offer/798612328767.html"
        }
      ]
    }
  ],
  "saveOption": "save"
}
```
</details>

---

### 编辑采购单

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order`
- 类型：写
- 原文：[479599774e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599774e0.md)（本地 raw/479599774e0_编辑采购单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `goodsSkuList` | array<object> | 否 | 采购商品列表 |
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


---

### 采购单动手填写运单号

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order_shipping`
- 类型：写
- 原文：[479599775e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599775e0.md)（本地 raw/479599775e0_采购单动手填写运单号.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单id |
| `packageList` | array<object> | 否 | 包裹列表 |
| `packageList[].logisticsName` | string | 否 | 物流公司 |
| `packageList[].waybillCode` | string | 否 | 快递单号 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 采购单修改运单信息

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_shipping`
- 类型：写
- 原文：[479599776e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599776e0.md)（本地 raw/479599776e0_采购单修改运单信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单id |
| `packageList` | array<object> | 否 | 包裹列表 |
| `packageList[].logisticsName` | string | 否 | 物流公司 |
| `packageList[].waybillCode` | string | 否 | 快递单号 |
| `orderShippingId` | string | 否 | 运单信息id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 采购单更新平台运单信息

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_outer_shipping`
- 类型：写
- 原文：[479599777e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599777e0.md)（本地 raw/479599777e0_采购单更新平台运单信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | string | 是 | 采购单ID |
| `purchaseOrderInfo` | object | 否 | 采购单信息 |
| `purchaseOrderInfo.purchasePlatform` | string | 否 | 下单平台 |
| `purchaseOrderInfo.purchaseOrderSn` | string | 否 | 货源单号 |
| `purchaseOrderInfo.purchaseOrderBuyer` | string | 否 | 买家帐号 |
| `purchaseOrderInfo.purchaseOrderSeller` | string | 否 | 卖家帐号 |
| `purchaseOrderInfo.purchaseOrderPackages` | array<object> | 否 | 包裹信息 |
| `purchaseOrderInfo.purchaseOrderPackages[].purchaseOrderLogisticsName` | string | 否 | 物流公司 |
| `purchaseOrderInfo.purchaseOrderPackages[].purchaseOrderWaybillCode` | string | 否 | 快递单号 |
| `shippingId` | string | 否 | 运单ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 取消采购单

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/cancel_goods_purchase_order`
- 类型：写
- 原文：[479599778e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599778e0.md)（本地 raw/479599778e0_取消采购单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |
| `cancelReason` | string | 是 | 取消原因 缺货：outOfStock，换货：exchangeGoods，不想要了：dontWant，其他：other |
| `cancelNote` | string | 否 | 备注说明 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 标记采购单结束

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/finish_goods_purchase_order`
- 类型：写
- 原文：[479599779e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599779e0.md)（本地 raw/479599779e0_标记采购单结束.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderId` | integer | 是 | 采购单ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 通过采购单id批量添加1688商品采购单

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order_by_goods_purchase_order_ids`
- 类型：写
- 原文：[479599780e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599780e0.md)（本地 raw/479599780e0_通过采购单id批量添加1688商品采购单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderIds` | array<integer> | 是 | 采购单IDs |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successDataList` | object | 否 | 成功数据列表 |
| `data.successDataList.index` | string | 否 | 序号 |
| `data.successDataList.goodsPurchaseOrderSn` | string | 否 | 采购单号 |
| `data.successDataList.purchaseOrderSn` | string | 否 | 1688单号 |
| `data.successDataList.goodsPurchaseOrderId` | string | 否 | 采购单ID |
| `data.errors` | object | 否 | 错误数据列表 |
| `data.errors.index` | string | 否 | 序号 |
| `data.errors.errorMsg` | string | 否 | 错误信息 |
| `data.errors.errorType` | string | 否 | 错误类型 |
| `data.errors.goodsPurchaseOrderSn` | string | 否 | 采购单号 |
| `data.errors.purchaseOrderSn` | string | 否 | 1688单号 |
| `data.errors.goodsPurchaseOrderId` | string | 否 | 采购单ID |
| `data.successGoodsPurchaseOrderIds` | array<integer> | 否 | 成功的采购订单ID列表 |


---

### 获取采购单列表

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/fetch/search_goods_purchase_order_page`
- 类型：读
- 原文：[479599781e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599781e0.md)（本地 raw/479599781e0_获取采购单列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsPurchaseOrderList` | array<object> | 否 | 商品采购订单列表 |
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
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderSkuList` | array<object> | 否 | SKU 明细列表 |
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
| `data.goodsPurchaseOrderList[].shippingList` | array<object> | 否 | 运单信息列表 |
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
| `data.goodsPurchaseOrderList[].shippingList[].packageList` | array<object> | 否 | 快递包裹列表 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].goodsPurchaseOrderShippingPackageId` | string | 否 | 包裹 ID |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].goodsPurchaseOrderShippingId` | string | 否 | ID |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].goodsPurchaseOrderId` | string | 否 | 物流id |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].logisticsName` | string | 否 | 物流公司名称 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].waybillCode` | string | 否 | 快递单号 |
| `data.goodsPurchaseOrderList[].shippingList[].packageList[].contactPhone` | string | 否 | 联系手机号 |
| `data.goodsPurchaseOrderList[].financePaymentList` | array<object> | 否 | 付款申请记录列表 |
| `data.goodsPurchaseOrderList[].financePaymentList[].id` | string | 否 | id |
| `data.goodsPurchaseOrderList[].financePaymentList[].paymentId` | string | 否 | 申请记录id |
| `data.goodsPurchaseOrderList[].financePaymentList[].paymentSn` | string | 否 | 付款申请单号 |
| `data.goodsPurchaseOrderList[].financePaymentList[].paymentAmount` | string | 否 | 申请付款金额 |
| `data.goodsPurchaseOrderList[].financePaymentList[].status` | string | 否 | 付款申请状态 |
| `data.goodsPurchaseOrderList[].financePaymentList[].statusText` | string | 否 | 付款申请状态文案 |
| `data.goodsPurchaseOrderList[].fianceReceiptList` | array<object> | 否 | 退款收款记录列表 |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].id` | string | 否 | id |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].receiptSn` | string | 否 | 收款单号 |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].receiptAmount` | string | 否 | 收款金额 |
| `data.goodsPurchaseOrderList[].fianceReceiptList[].statusText` | string | 否 | 收款状态文案 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList` | array<object> | 否 | 变更单记录列表 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].goodsPurchaseOrderModifyId` | string | 否 | 变更单 ID |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].goodsPurchaseOrderModifySn` | string | 否 | 变更单编号 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].status` | string | 否 | 变更单状态 |
| `data.goodsPurchaseOrderList[].goodsPurchaseOrderModifyList[].statusText` | string | 否 | 变更单状态文案 |
| `data.total` | integer | 否 | 总计 |


---

### 签收记录列表

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order_receive/fetch/search_goods_purchase_order_receive_page`
- 类型：读
- 原文：[479599771e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599771e0.md)（本地 raw/479599771e0_签收记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `goodsPurchaseOrderSnList` | array<string> | 否 | 货源单号 |
| `goodsPurchaseOrderSnListRp` | string | 否 | 货源单号列表搜索类型;(rss:前缀,lss:后缀,ss:模糊,eq:精确) |
| `gmtCreateStart` | string | 否 | 采购单创建日期开始 |
| `gmtCreateEnd` | string | 否 | 采购单创建日期结束 |
| `source` | string | 否 | 来源1688/other |
| `tab` | string | 否 | 订单状态：inDraft:草稿箱;waitAudit:待审核;hasSend:待收货;finish:已完成;cancelAndReturn:已取消、已退货 |
| `goodsSupplierId` | integer | 否 | 供应商ID |
| `warehouseId` | array<integer> | 否 | 收货仓库ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.purchaseOrderReceiveList` | array<object> | 否 | 商品采购订单收货列表 |
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
| `data.purchaseOrderReceiveList[].receiveInfo.skuList` | array<object> | 否 | 签收sku列表 |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].goodsPurchaseOrderReceiveSkuId` | string | 否 | ID |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].currentReceiveNum` | string | 否 | 本次签收数量 |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].warehouseShelfCellId` | string | 否 | 签收仓位id |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].goodsSkuId` | string | 否 | sku id |
| `data.purchaseOrderReceiveList[].receiveInfo.skuList[].orderSkuInfo` | object | 否 | sku信息 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier` | object | 否 | 供应商 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.shopName` | string | 否 | 供货商名称 |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.sellerId` | string | 否 | 供货商 ID |
| `data.purchaseOrderReceiveList[].goodsPurchaseOrderSupplier.homeUrl` | string | 否 | 供货商店铺主页（有值时名称可点击跳转） |
| `data.purchaseOrderReceiveList[].shippingList` | array<object> | 否 | 运单列表 |
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
| `data.purchaseOrderReceiveList[].shippingList[].packageList` | array<object> | 否 | 快递包裹列表 |
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


---

### 获取缺货、备货建议列表

- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_suggest/fetch/search_goods_purchase_suggest_page`
- 类型：读
- 原文：[479599782e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599782e0.md)（本地 raw/479599782e0_获取缺货、备货建议列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `warehouseId` | array<integer> | 否 | 仓库ID |
| `goodsSupplierId` | integer | 否 | 供货商 |
| `type` | string | 否 | 类型(默认是备货),stockUp备货,outOfStock缺货 |
| `source` | string | 否 | other/1688 |
| `shopIds` | array<integer> | 否 | 店铺id |
| `goodsCodeValue` | string | 否 | 商品sku |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.purchaseSuggestList` | array<object> | 否 | 商品采购建议列表 |
| `data.purchaseSuggestList[].goodsId` | integer | 否 | 商品id |
| `data.purchaseSuggestList[].goodsSkuId` | integer | 否 | 商品sku id |
| `data.purchaseSuggestList[].dailySales` | integer | 否 | 日销量 |
| `data.purchaseSuggestList[].minTriggerSuggestNum` | integer | 否 | 采购下限 |
| `data.purchaseSuggestList[].maxPrepareDays` | integer | 否 | 最大备货天数 |
| `data.purchaseSuggestList[].minPrepareDays` | integer | 否 | 最小备货天数 |
| `data.purchaseSuggestList[].orderNeedNum` | integer | 否 | 订单需求量 |
| `data.purchaseSuggestList[].recentSaleNumDt7` | integer | 否 | 近7天销量 |
| `data.purchaseSuggestList[].recentSaleNumDt30` | integer | 否 | 近30天销量 |
| `data.purchaseSuggestList[].suggestNum` | integer | 否 | 建议数量 |
| `data.purchaseSuggestList[].safeStockNum` | integer | 否 | 安全库存 |
| `data.total` | integer | 否 | 总计 |


## 供应商

### 获取供应商列表

- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/search_supplier_page`
- 类型：读
- 原文：[479599789e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599789e0.md)（本地 raw/479599789e0_获取供应商列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `data.supplierList` | array<object> | 否 | 供应商列表 |
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


---

### 获取供应商信息

- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/get_supplier_info`
- 类型：读
- 原文：[479599790e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599790e0.md)（本地 raw/479599790e0_获取供应商信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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


---

### 获取供应商类型列表

- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/fetch/get_supplier_platform_list`
- 类型：读
- 原文：[479599791e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599791e0.md)（本地 raw/479599791e0_获取供应商类型列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supplierPlatformOptions` | array<object> | 否 |  |
| `data.supplierPlatformOptions[].label` | string | 否 | 供应商类型名称 |
| `data.supplierPlatformOptions[].value` | string | 否 | 供应商类型code |


---

### 修改供应商

- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/operate/edit_supplier`
- 类型：写
- 原文：[479653199e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479653199e0.md)（本地 raw/479653199e0_修改供应商.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsSupplierId` | integer | 是 | 供应商id |
| `shopName` | string | 是 | 供应商名称 |
| `source` | string | 否 | 供应商类型code |
| `homeUrl` | string | 否 | 主页网址 |
| `purchaseUrl` | string | 否 | 采购网址 |
| `arrivalDays` | string | 否 | 到货周期 |
| `accountNote` | string | 否 | 备注 |
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
| `bankCardNumber` | string | 否 | 银行卡号 |
| `bankCardOwnerName` | string | 否 | 开户人姓名 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.@api` | object | 否 | POST |


---

### 创建供应商

- 层级：开放平台 > 采购 > 供应商
- 方法+路径：`POST /open/v1/ewm/supplier/operate/add_supplier`
- 类型：写
- 原文：[479653198e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479653198e0.md)（本地 raw/479653198e0_创建供应商.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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

