# 创建1688采购单


- 层级：开放平台 > 采购 > 采购单
- 方法+路径：`POST /open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order`
- 类型：写
- 原文：[479599773e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599773e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `goodsPurchaseOrderList` | array&lt;object> | 是 | 采购单列表（可批量） |
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
| `goodsPurchaseOrderList[].goodsSkuList` | array&lt;object> | 是 | 商品列表信息 |
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
| `data.successGoodsPurchaseOrderIds` | array&lt;integer> | 否 | 成功的采购订单ID列表 |


&lt;details>&lt;summary>请求示例&lt;/summary>

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
&lt;/details>
