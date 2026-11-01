# 获取需要设置净重的类目列表


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_need_set_net_weight_cid_list`
- 类型：读
- 原文：[490449047e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/490449047e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cidList` | array&lt;integer> | 否 | 需要设置净重的类目列表 |
