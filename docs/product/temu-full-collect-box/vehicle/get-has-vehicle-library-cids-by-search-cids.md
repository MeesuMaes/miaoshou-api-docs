# 根据类目ID查询有车型库数据的类目列表


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_has_vehicle_library_cids_by_search_cids`
- 类型：读
- 原文：[468724007e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724007e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cids` | array&lt;integer> | 是 | 待查询的类目ID列表，传入产品所在类目的cid， 返回结果中包含的cid表示该类目支持车型库，发品时需填写车型适配信息 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.hasVehicleLibraryCids` | array&lt;integer> | 否 | 有车型库的类目ID列表，如果产品所属类目在此列表中， 则发品时需要填写车型适配信息（vehicleLibrary相关字段） |
