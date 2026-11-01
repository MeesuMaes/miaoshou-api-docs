# 通过货源链接采集货源


- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/fetch_item`
- 类型：写
- 原文：[446814581e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814581e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectLinks` | array&lt;string> | 是 | 链接列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sourceItemIdAndDetailIdMap` | object | 否 | 货源ID和公共采集箱ID的映射 |
