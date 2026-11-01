# 发布记录列表


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/move_collect/search_move_collect_list`
- 类型：读
- 原文：[511668107e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511668107e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array&lt;object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |
