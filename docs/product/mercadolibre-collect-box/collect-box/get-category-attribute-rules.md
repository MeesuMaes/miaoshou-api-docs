# 获取类目属性规则


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_attribute_rules`
- 类型：读
- 原文：[482753632e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753632e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.saleAttributeRules` | array&lt;object> | 否 | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `data.saleAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.saleAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.saleAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.saleAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.saleAttributeRules[].id` | string | 否 | 属性ID |
| `data.saleAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.saleAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.saleAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.saleAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.saleAttributeRules[].values` | array&lt;object> | 否 | 可选值列表,从中选取name |
| `data.saleAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.saleAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.saleAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.saleAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.productAttributeRules` | array&lt;object> | 否 | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `data.productAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.productAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.productAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.productAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.productAttributeRules[].id` | string | 否 | 属性ID |
| `data.productAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.productAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.productAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.productAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.productAttributeRules[].values` | array&lt;object> | 否 | 可选值列表,从中选取name |
| `data.productAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.productAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.productAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.productAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.skuAttributeRules` | array&lt;object> | 否 | SKU属性规则列表，创建产品时需按此规则填写attributes |
| `data.skuAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.skuAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.skuAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.skuAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.skuAttributeRules[].id` | string | 否 | 属性ID |
| `data.skuAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.skuAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.skuAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.skuAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.skuAttributeRules[].values` | array&lt;object> | 否 | 可选值列表,从中选取name |
| `data.skuAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.skuAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.skuAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.skuAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
