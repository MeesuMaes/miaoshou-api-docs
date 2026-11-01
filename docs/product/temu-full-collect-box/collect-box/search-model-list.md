# 店铺模特列表


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/search_model_list`
- 类型：读
- 原文：[471545329e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545329e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模） |
| `modelName` | string | 否 | 模特名称模糊搜索 |
| `pageNo` | integer | 否 | 页码，默认1 |
| `pageSize` | integer | 否 | 每页条数，默认20 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.modelList` | array&lt;object> | 否 | 模特列表，用户从中选择模特绑定到商品。 选择后需额外选择试穿尺码（sizeSpecId/sizeSpecName）和试穿结果（tryOnResult）， 将各字段对应填入 goodsModelReqs 后提交保存。部分类目必填 requiredGoodsModel 为 true。 |
| `data.modelList[].pddkjShopModelId` | integer | 否 | 店铺模特记录ID |
| `data.modelList[].shopId` | integer | 否 | 店铺ID |
| `data.modelList[].platformModelId` | integer | 否 | 平台模特ID，保存时填入 goodsModelReqs.modelId |
| `data.modelList[].headPortrait` | string | 否 | 头像URL，保存时填入 goodsModelReqs.modelProfileUrl |
| `data.modelList[].modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模），保存时填入 goodsModelReqs.modelType |
| `data.modelList[].canEdit` | integer | 否 | 是否可编辑（1=可编辑，0=不可编辑） |
| `data.modelList[].modelName` | string | 否 | 模特名称，保存时填入 goodsModelReqs.modelName |
| `data.modelList[].hipline` | string | 否 | 臀围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHip |
| `data.modelList[].bust` | string | 否 | 胸围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelBust |
| `data.modelList[].height` | string | 否 | 身高（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHeight |
| `data.modelList[].waist` | string | 否 | 腰围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelWaist |
| `data.modelList[].footLength` | string | 否 | 脚长（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootLength |
| `data.modelList[].footWidth` | string | 否 | 脚宽（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootWidth |
| `data.total` | integer | 否 | 总数 |
