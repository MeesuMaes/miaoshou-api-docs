# 获取制造商列表


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_manufacturer_list`
- 类型：读
- 原文：[449869292e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449869292e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `refresh` | integer | 是 | 是否重新刷新数据（0=否，1=是） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.manufacturerList` | array&lt;object> | 否 | 制造商列表 |
| `data.manufacturerList[].id` | string | 否 | 制造商ID |
| `data.manufacturerList[].name` | string | 否 | 制造商名称 |
