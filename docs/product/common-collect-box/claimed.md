# 认领到平台采集箱


- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/claimed`
- 类型：写
- 原文：[446814587e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814587e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailSerialNumberPlatformList` | array&lt;object> | 是 | 认领数据列表 |
| `detailSerialNumberPlatformList[].detailId` | integer | 是 | 公共采集箱ID |
| `detailSerialNumberPlatformList[].platform` | string | 是 | 认领的平台(TK-tiktok, temu全托-pddkj, temu半托-pddkjChoice, 虾皮-shopee, ozon-ozon,美客多-mercadolibre) |
| `detailSerialNumberPlatformList[].serialNumber` | integer | 是 | 序列号（默认传1） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.platformCollectBoxDetailIdMap` | object | 否 | 各平台采集箱详情ID映射 key: 平台名（如 tiktok），value: collectBoxId => detailId 的映射 |
