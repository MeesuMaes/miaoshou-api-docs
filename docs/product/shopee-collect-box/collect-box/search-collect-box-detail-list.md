# 获取采集箱列表


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[516157443e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157443e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array&lt;object> | 否 | 采集箱数据列表 |
| `data.detailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.detailList[].itemNum` | string | 否 | 商品编号 |
| `data.detailList[].stock` | string | 否 | 库存 |
| `data.detailList[].price` | string | 否 | 价格 |
| `data.detailList[].thumbnail` | string | 否 | 缩略图 |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].editModel` | string | 否 | 编辑模式 |
| `data.detailList[].commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | string | 否 | 应用账户ID |
| `data.detailList[].subAppAccountId` | string | 否 | 子应用账户ID |
| `data.detailList[].platform` | string | 否 | 平台 |
| `data.detailList[].title` | string | 否 | 商品标题 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].copyType` | string | 否 | 复制类型 |
| `data.detailList[].collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.detailList[].collectBoxDetailShopList` | array&lt;object> | 否 | 预发布店铺信息列表 |
| `data.detailList[].collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |
