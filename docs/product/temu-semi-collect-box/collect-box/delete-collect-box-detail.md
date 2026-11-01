# 批量删除采集箱产品接口


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/delete_collect_box_detail`
- 类型：写
- 原文：[477347617e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347617e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array&lt;integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successNum` | integer | 否 | 删除成功数量 |
| `data.failNum` | integer | 否 | 删除失败数量 |
| `data.errorMap` | object | 否 | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `data.errorMsg` | string | 否 | 拼接后的错误信息 |
