# 批量删除公共采集箱产品


- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/batch_delete_common_collect_box_detail`
- 类型：写
- 原文：[446814584e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814584e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailIds` | array&lt;integer> | 是 | 公共采集箱ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |
