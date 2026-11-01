# 获取包装清单属性值列表


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_goods_accessories_list`
- 类型：读
- 原文：[501791146e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/501791146e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `fuzzyValue` | string | 否 | 属性值模糊搜索关键词（可选 未填写默认返回前100条数据） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsAccessoriesList` | array&lt;object> | 否 | 包装清单属性值列表，用于用户选择包装清单内容 最多返回 100 条 |
| `data.goodsAccessoriesList[].vid` | integer | 否 | 属性值ID |
| `data.goodsAccessoriesList[].unitCode` | integer | 否 | 单位编码 |
| `data.goodsAccessoriesList[].unitName` | string | 否 | 单位名称，用于展示 |
| `data.goodsAccessoriesList[].value` | string | 否 | 属性值名称 |
