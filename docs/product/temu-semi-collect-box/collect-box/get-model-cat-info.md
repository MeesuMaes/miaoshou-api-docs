# 获取模特分类配置


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_model_cat_info`
- 类型：读
- 原文：[477347615e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347615e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID，从类目选择接口获取，切换类目后传入查询该类目的模特配置 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.modelCat` | object | 否 | 模特分类配置，为 null 表示该类目不支持模特功能 enabled=1 时展示模特绑定区域，按 modelType 区分成衣模特(0)或鞋模(1)进行筛选绑定。 |
| `data.modelCat.cid` | integer | 否 | 类目ID |
| `data.modelCat.modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模），展示模特绑定区域时按此类型筛选可用模特 |
| `data.modelCat.enabled` | integer | 否 | 是否启用模特（1=启用，0=禁用），为1时展示模特绑定区域 |
