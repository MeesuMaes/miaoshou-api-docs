# 获取公共采集箱列表


- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_list`
- 类型：读
- 原文：[446814582e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814582e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.tabPaneName` | string | 否 | 状态(all-全部、noClaimed-未认领、claimed-已认领、collectFail-采集失败、collectSuccess-采集成功) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array&lt;object> | 否 | 列表页数据列表 |
| `data.detailList[].commonCollectBoxDetailId` | integer | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | integer | 否 | 主账号ID |
| `data.detailList[].subAppAccountId` | integer | 否 | 子账号ID |
| `data.detailList[].itemNum` | string | 否 | 货号 |
| `data.detailList[].title` | string | 否 | 标题 |
| `data.detailList[].thumbnail` | string | 否 | 主图缩略图 |
| `data.detailList[].price` | number | 否 | 价格 |
| `data.detailList[].minSkuPrice` | number | 否 | 最低SKU价格 |
| `data.detailList[].maxSkuPrice` | number | 否 | 最高SKU价格 |
| `data.detailList[].stock` | integer | 否 | 库存 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].status` | string | 否 | 状态 |
| `data.detailList[].reason` | string | 否 | 失败原因 |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].gmtModified` | string | 否 | 修改时间 |
| `data.detailList[].weight` | number | 否 | 重量 |
| `data.detailList[].maxSkuWeight` | number | 否 | 最高SKU重量 |
| `data.detailList[].minSkuWeight` | number | 否 | 最低SKU重量 |
| `data.detailList[].commonCollectBoxGroupId` | integer | 否 | 采集箱分组ID |
| `data.detailList[].commonCollectBoxGroupName` | string | 否 | 采集箱分组名称 |
| `data.detailList[].sourceList` | array&lt;object> | 否 | 来源信息列表 |
| `data.detailList[].sourceList[].remark` | string | 否 | 备注 |
| `data.detailList[].sourceList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.detailList[].sourceList[].source` | string | 否 | 来源平台 |
| `data.detailList[].sourceList[].sourceSite` | string | 否 | 来源站点 |
| `data.detailList[].sourceList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.detailList[].ownerSubAccountAliasName` | string | 否 | 子账号别名 |
| `data.detailList[].listThumbnail` | string | 否 | 列表缩略图 |
| `data.detailList[].isMark` | string | 否 | 是否标记 |
| `data.total` | integer | 否 | 总数 |
| `data.isCommonCollectHuger` | boolean | 否 | 是否数量巨大 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "pageNo": 1,
  "pageSize": 10
}
```
&lt;/details>
