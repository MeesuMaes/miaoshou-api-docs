# 获取采集箱列表


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/search_collect_box_detailList`
- 类型：读
- 原文：[482753630e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753630e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.filterCidSite` | string | 否 | 过滤类目站点(固定值-CBT) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.itemNum` | string | 否 | 商品编号 |
| `data.breadcrumb` | string | 否 | 类目面包屑 |
| `data.cid` | string | 否 | 类目ID |
| `data.globalPrice` | string | 否 | 全球净收益/售价 |
| `data.stock` | string | 否 | 库存 |
| `data.price` | string | 否 | 货源价格 |
| `data.thumbnail` | string | 否 | 缩略图 |
| `data.gmtCreate` | string | 否 | 创建时间 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.appAccountId` | string | 否 | 应用账户ID |
| `data.subAppAccountId` | string | 否 | 子应用账户ID |
| `data.platform` | string | 否 | 平台 |
| `data.title` | string | 否 | 商品标题 |
| `data.remark` | string | 否 | 备注 |
| `data.copyType` | string | 否 | 复制类型 |
| `data.collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.collectBoxDetailShop` | object | 否 | 预发布店铺信息 |
| `data.collectBoxDetailShop.shopId` | string | 否 | 店铺ID |
| `data.collectBoxDetailShop.pricingMode` | string | 否 | 售价模式 |
| `data.collectBoxDetailShop.siteAndMaxPriceMap` | object | 否 | 站点最大价格映射 |
| `data.collectBoxDetailShop.siteAndMinPriceMap` | object | 否 | 站点最小价格映射 |
| `data.collectBoxDetailShop.siteAndPriceMap` | object | 否 | 站点价格映射 |
| `data.collectBoxDetailShop.sites` | array&lt;string> | 否 | 已选择的站点列表(BR(Full)(Up)、BR(Full)等) |
