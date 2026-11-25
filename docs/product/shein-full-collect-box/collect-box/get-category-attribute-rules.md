# 获取类目属性规则


- 层级：开放平台 > 商品 > SHEIN全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein/collect_box/get_category_attribute_rules`
- 类型：读
- 原文：[537694040e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537694040e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | string | 是 | 类目ID |
| `shopId` | integer | 否 | 主店铺ID，shopId和site必须传一个 |
| `site` | string | 否 | 站点，shopId和site必须传一个 |
| `shopIds` | array&lt;integer> | 否 | 需要同步查询的店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.attributeRuleList` | array&lt;object> | 否 | 类目属性规则列表 |
| `data.attributeRuleList[].id` | integer | 否 | 属性ID |
| `data.attributeRuleList[].name` | string | 否 | 属性名称 |
| `data.attributeRuleList[].requireExtraValue` | boolean | 否 | 是否需要附属值 |
| `data.attributeRuleList[].inputType` | string | 否 | 输入类型(singleSelect-multipleSelect-input 等) |
| `data.attributeRuleList[].group` | string | 否 | 属性分组(normal-sale-sizeChart) |
| `data.attributeRuleList[].isMainSale` | boolean | 否 | 是否主销售属性 |
| `data.attributeRuleList[].isComponent` | boolean | 否 | 是否组件属性 |
| `data.attributeRuleList[].isRequire` | boolean | 否 | 是否必填 |
| `data.attributeRuleList[].options` | array&lt;object> | 否 | 可选项列表 |
| `data.attributeRuleList[].options[].name` | string | 否 | 选项名称 |
| `data.attributeRuleList[].options[].id` | integer | 否 | 选项ID |
| `data.attributeRuleList[].options[].groupList` | array&lt;integer> | 否 | 选项所属分组列表 |
| `data.attributeRuleList[].isSupportCustom` | integer | 否 | 是否支持自定义值(0-否，1-是) |
| `data.attributeRuleList[].attributeRemarkList` | array&lt;object> | 否 | 属性备注列表 |
| `data.attributeRuleList[].attributeInputNum` | integer | 否 | 最大输入数量 |
| `data.categoryAttributeCheckRuleList` | array&lt;object> | 否 | 类目属性校验规则列表 |
| `data.categoryAttributeCheckRuleList[].needCheckAttrId` | string | 否 | 需要校验的属性ID |
| `data.categoryAttributeCheckRuleList[].needCheckCondition` | array&lt;object> | 否 | 命中条件，key 为属性ID，value 为允许的属性值ID列表 |
