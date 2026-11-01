# 同步店铺尺码表


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/rsync_size_chart_template`
- 类型：写
- 原文：[482753643e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753643e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array&lt;integer> | 是 | 店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndRsyncRet` | object | 否 | 店铺Id同步结果映射 key 为 shopId，value 为该店铺同步结果。 Map value 为该店铺同步结果，每一项结构如下： -result : 同步结果，success 表示成功，fail 表示失败 -reason : 同步失败原因，如果同步成功则为空 |
