# 获取联动属性规则


- 层级：开放平台 > 商品 > SHEIN半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein_choice/collect_box/get_associated_attribute_rules`
- 类型：读
- 原文：[537697868e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537697868e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | string | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |
| `site` | string | 是 | 站点 |
| `attributes` | object | 是 | 已选属性列表 示例: [ \{ "id": 100018, "values": [ \{"id": 200001\} ] \}, \{ "id": 100019, "values": [ \{"id": 200010\}, \{"id": 200011\} ] \} ] |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.linkRuleAttributeList` | array&lt;object> | 否 | 联动属性规则列表 |
| `data.linkRuleAttributeList[].attributeId` | integer | 否 | 联动属性ID |
| `data.linkRuleAttributeList[].attributeValueList` | array&lt;integer> | 否 | 允许选择的属性值ID列表 |
| `data.linkRuleAttributeList[].attributeValuePreFillList` | array&lt;integer> | 否 | 预填属性值ID列表 |
