# 提交全球商品发布到店铺任务


- 层级：开放平台 > 商品 > Shopee采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/shopee/move_collect/save_move_collect_global_task`
- 类型：写
- 原文：[480434554e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434554e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopeeGlobalItemIds` | array&lt;integer> | 是 | 全球商品ID |
| `shopIds` | array&lt;integer> | 是 | 店铺ID |
| `isUseShopeeGlobalSetting` | integer | 否 | 是否使用全球发布配置;1是,0否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectTaskDetailIds` | array&lt;integer> | 否 | 任务ID |
