# 获取类目属性信息


- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_category_attributes`
- 类型：读
- 原文：[516158667e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516158667e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.categoryAttributes` | array&lt;object> | 否 | 类目属性列表 |
| `data.categoryAttributes[].attributeId` | integer | 否 | 属性ID |
| `data.categoryAttributes[].attributeUnit` | array&lt;string> | 否 | 属性参数单位值（单选，前面一般跟数字配对） |
| `data.categoryAttributes[].attributeValueList` | array&lt;object> | 否 | 属性选项（单选选或者多选） |
| `data.categoryAttributes[].attributeValueList[].valueId` | integer | 否 | 属性值ID |
| `data.categoryAttributes[].attributeValueList[].displayValueName` | string | 否 | 属性值名称 |
| `data.categoryAttributes[].attributeValueList[].originalValueName` | string | 否 | 原始属性值名称 |
| `data.categoryAttributes[].displayAttributeName` | string | 否 | 属性别名（一般中文） |
| `data.categoryAttributes[].formatType` | string | 否 | 属性参数格式类型（NORMAL，QUANTITATIVE，YEAR_MONTH_DATE，YEAR_MONTH） |
| `data.categoryAttributes[].inputType` | string | 否 | 属性内容类型（DROP_DOWN,MULTIPLE_SELECT,TEXT_FILED,COMBO_BOX,MULTIPLE_SELECT_COMBO_BOX） |
| `data.categoryAttributes[].inputValidationType` | string | 否 | 属性内容校验类型（INT_TYPE STRING_TYPE ENUM_TYPE FLOAT_TYPE DATE_TYPE TIMESTAMP_TYPE） |
| `data.categoryAttributes[].isMandatory` | boolean | 否 | 是否必填 |
| `data.categoryAttributes[].maxInputValueNumber` | integer | 否 | 最大输入值数量（一般选项限制使用） |
| `data.categoryAttributes[].originalAttributeName` | string | 否 | 接口原始属性名 |
