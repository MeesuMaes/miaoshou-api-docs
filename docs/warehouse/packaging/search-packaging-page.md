# 获取列表


- 层级：开放平台 > 仓储 > 商品包材
- 方法+路径：`POST /open/v1/ewm/packaging/fetch/search_packaging_page`
- 类型：读
- 原文：[479592181e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592181e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.packagingList` | array&lt;object> | 否 | 包材列表 |
| `data.packagingList[].packagingId` | string | 否 | ID |
| `data.packagingList[].packagingCode` | string | 否 | code |
| `data.packagingList[].name` | string | 否 | 包材名称 |
| `data.packagingList[].price` | string | 否 | 价格 |
| `data.packagingList[].length` | string | 否 | 长度 |
| `data.packagingList[].width` | string | 否 | 宽度 |
| `data.packagingList[].height` | string | 否 | 高度 |
| `data.packagingList[].weight` | string | 否 | 重量 |
| `data.packagingList[].remark` | string | 否 | 备注 |
| `data.packagingList[].gmtCreate` | string | 否 | 创建时间 |
| `data.packagingList[].gmtModified` | string | 否 | 更新时间 |
| `data.total` | integer | 否 | 总数 |
