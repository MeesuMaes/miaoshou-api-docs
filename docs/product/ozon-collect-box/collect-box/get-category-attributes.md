# 获取类目属性信息


- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_category_attributes`
- 类型：读
- 原文：[474774626e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774626e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.categoryAttributes` | array&lt;object> | 否 | 类目属性列表 |
| `data.categoryAttributes[].cid` | integer | 否 | 类目ID |
| `data.categoryAttributes[].attrId` | integer | 否 | 属性ID |
| `data.categoryAttributes[].name` | string | 否 | 属性名称 |
| `data.categoryAttributes[].nameZh` | string | 否 | 属性中文名称 |
| `data.categoryAttributes[].key` | string | 否 | 属性所属类型，可以理解为该属性所代表的类型（Brand-品牌，ColorSample-颜色样本，Season-季节，Material-材料，RichContentJson-富文本JSON，SizeGridJson-尺码表JSON，DuvetCoversSize-被套尺寸，SexMaster-性别） |
| `data.categoryAttributes[].type` | string | 否 | 属性值填写的类型（String-字符串，Integer-整数，Decimal-浮点数） |
| `data.categoryAttributes[].isVariant` | integer | 否 | 是否是销售属性，（1-是，0-否） |
| `data.categoryAttributes[].isCollection` | integer | 否 | 是否是下来选项，（1-是，0-否） |
| `data.categoryAttributes[].isRequired` | integer | 否 | 是否是必填选项，（1-是，0-否） |
| `data.categoryAttributes[].dictionaryId` | integer | 否 | 下拉选项字典ID |
| `data.categoryAttributes[].dictionaryValues` | array&lt;object> | 否 | 下拉选项值列表（前1000个） |
| `data.categoryAttributes[].dictionaryValues[].id` | integer | 否 | 属性值ID |
| `data.categoryAttributes[].dictionaryValues[].value` | string | 否 | 属性值数据 |
| `data.categoryAttributes[].dictionaryValues[].valueZh` | string | 否 | 属性值中文数据 |
| `data.categoryAttributes[].description` | string | 否 | 属性详细描述 |
| `data.categoryAttributes[].descriptionZh` | string | 否 | 属性中文详细描述 |
| `data.categoryAttributes[].tooltip` | string | 否 | 属性填写提示 |
| `data.categoryAttributes[].tooltipZh` | string | 否 | 属性中文填写提示 |
