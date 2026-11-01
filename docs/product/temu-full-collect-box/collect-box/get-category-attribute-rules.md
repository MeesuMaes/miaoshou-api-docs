# 获取类目属性规则


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_category_attribute_rules`
- 类型：读
- 原文：[471545320e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545320e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array&lt;integer> | 否 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.saleAttributeRules` | array&lt;object> | 否 | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `data.saleAttributeRules[].pid` | integer | 否 | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `data.saleAttributeRules[].templatePid` | integer | 否 | 模板属性ID，用于关联模板中的属性定义 |
| `data.saleAttributeRules[].refPid` | integer | 否 | 引用属性ID，表示该属性引用自哪个基础属性 |
| `data.saleAttributeRules[].name` | string | 否 | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `data.saleAttributeRules[].lang2Name` | string | 否 | 第二语言属性名称 |
| `data.saleAttributeRules[].isSale` | boolean | 否 | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `data.saleAttributeRules[].mainSale` | boolean | 否 | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `data.saleAttributeRules[].required` | boolean | 否 | 是否必填，为true时创建产品必须填写该属性 |
| `data.saleAttributeRules[].valueType` | string | 否 | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `data.saleAttributeRules[].controlType` | integer | 否 | 控件类型，决定前端展示方式 |
| `data.saleAttributeRules[].feature` | integer | 否 | 特征标记 |
| `data.saleAttributeRules[].chooseMaxNum` | integer | 否 | 最多可选数量，SELECT类型时最多可选几个value |
| `data.saleAttributeRules[].inputMaxNum` | integer | 否 | 输入最大数量，自定义输入的规格上限 |
| `data.saleAttributeRules[].minValue` | string | 否 | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `data.saleAttributeRules[].maxValue` | string | 否 | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `data.saleAttributeRules[].valuePrecision` | integer | 否 | 小数精度，数值保留几位小数 |
| `data.saleAttributeRules[].valueUnit` | array&lt;string> | 否 | 合法单位列表，输入时必须使用列表中的单位 |
| `data.saleAttributeRules[].valueRule` | integer | 否 | 值规则 |
| `data.saleAttributeRules[].propertyValueType` | integer | 否 | 属性值类型 |
| `data.saleAttributeRules[].parentSpecId` | integer | 否 | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `data.saleAttributeRules[].parentTemplatePid` | integer | 否 | 父模板属性ID |
| `data.saleAttributeRules[].templatePropertyValueParentList` | array&lt;object> | 否 | 父属性值模板ID列表，非string类型属性时使用 |
| `data.saleAttributeRules[].templatePropertyValueParentList[].parentVidList` | array&lt;integer> | 否 | 父属性值ID列表 |
| `data.saleAttributeRules[].showCondition` | array&lt;object> | 否 | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `data.saleAttributeRules[].showCondition[].parentRefPid` | integer | 否 | 父引用属性ID |
| `data.saleAttributeRules[].showCondition[].parentVids` | array&lt;integer> | 否 | 父属性值ID列表 |
| `data.saleAttributeRules[].showType` | integer | 否 | 展示类型 |
| `data.saleAttributeRules[].propertyChooseTitle` | string | 否 | 属性选择标题，SELECT类型时的选择提示文字 |
| `data.saleAttributeRules[].numberInputTitle` | string | 否 | 数字输入标题，INPUT类型时的输入提示文字 |
| `data.saleAttributeRules[].referenceType` | integer | 否 | 引用类型 |
| `data.saleAttributeRules[].valueInputSum` | integer | 否 | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `data.saleAttributeRules[].values` | array&lt;object> | 否 | 可选值列表，SELECT类型时从中选取vid和name |
| `data.saleAttributeRules[].values[].specId` | integer | 否 | 规格ID，自定义输入的值为null |
| `data.saleAttributeRules[].values[].vid` | integer | 否 | 属性值ID，填写属性时通过vid指定选中的值 |
| `data.saleAttributeRules[].values[].name` | string | 否 | 属性值名称，如"白色"、"XL"、"棉" |
| `data.saleAttributeRules[].values[].lang2Value` | string | 否 | 第二语言值 |
| `data.saleAttributeRules[].values[].extendInfo` | string | 否 | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `data.saleAttributeRules[].values[].group` | object | 否 | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `data.saleAttributeRules[].values[].parentVidList` | array&lt;integer> | 否 | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| `data.productAttributeRules` | array&lt;object> | 否 | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `data.productAttributeRules[].pid` | integer | 否 | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `data.productAttributeRules[].templatePid` | integer | 否 | 模板属性ID，用于关联模板中的属性定义 |
| `data.productAttributeRules[].refPid` | integer | 否 | 引用属性ID，表示该属性引用自哪个基础属性 |
| `data.productAttributeRules[].name` | string | 否 | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `data.productAttributeRules[].lang2Name` | string | 否 | 第二语言属性名称 |
| `data.productAttributeRules[].isSale` | boolean | 否 | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `data.productAttributeRules[].mainSale` | boolean | 否 | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `data.productAttributeRules[].required` | boolean | 否 | 是否必填，为true时创建产品必须填写该属性 |
| `data.productAttributeRules[].valueType` | string | 否 | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `data.productAttributeRules[].controlType` | integer | 否 | 控件类型，决定前端展示方式 |
| `data.productAttributeRules[].feature` | integer | 否 | 特征标记 |
| `data.productAttributeRules[].chooseMaxNum` | integer | 否 | 最多可选数量，SELECT类型时最多可选几个value |
| `data.productAttributeRules[].inputMaxNum` | integer | 否 | 输入最大数量，自定义输入的规格上限 |
| `data.productAttributeRules[].minValue` | string | 否 | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `data.productAttributeRules[].maxValue` | string | 否 | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `data.productAttributeRules[].valuePrecision` | integer | 否 | 小数精度，数值保留几位小数 |
| `data.productAttributeRules[].valueUnit` | array&lt;string> | 否 | 合法单位列表，输入时必须使用列表中的单位 |
| `data.productAttributeRules[].valueRule` | integer | 否 | 值规则 |
| `data.productAttributeRules[].propertyValueType` | integer | 否 | 属性值类型 |
| `data.productAttributeRules[].parentSpecId` | integer | 否 | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `data.productAttributeRules[].parentTemplatePid` | integer | 否 | 父模板属性ID |
| `data.productAttributeRules[].templatePropertyValueParentList` | array&lt;object> | 否 | 父属性值模板ID列表，非string类型属性时使用 |
| `data.productAttributeRules[].templatePropertyValueParentList[].parentVidList` | array&lt;integer> | 否 | 父属性值ID列表 |
| `data.productAttributeRules[].showCondition` | array&lt;object> | 否 | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `data.productAttributeRules[].showCondition[].parentRefPid` | integer | 否 | 父引用属性ID |
| `data.productAttributeRules[].showCondition[].parentVids` | array&lt;integer> | 否 | 父属性值ID列表 |
| `data.productAttributeRules[].showType` | integer | 否 | 展示类型 |
| `data.productAttributeRules[].propertyChooseTitle` | string | 否 | 属性选择标题，SELECT类型时的选择提示文字 |
| `data.productAttributeRules[].numberInputTitle` | string | 否 | 数字输入标题，INPUT类型时的输入提示文字 |
| `data.productAttributeRules[].referenceType` | integer | 否 | 引用类型 |
| `data.productAttributeRules[].valueInputSum` | integer | 否 | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `data.productAttributeRules[].values` | array&lt;object> | 否 | 可选值列表，SELECT类型时从中选取vid和name |
| `data.productAttributeRules[].values[].specId` | integer | 否 | 规格ID，自定义输入的值为null |
| `data.productAttributeRules[].values[].vid` | integer | 否 | 属性值ID，填写属性时通过vid指定选中的值 |
| `data.productAttributeRules[].values[].name` | string | 否 | 属性值名称，如"白色"、"XL"、"棉" |
| `data.productAttributeRules[].values[].lang2Value` | string | 否 | 第二语言值 |
| `data.productAttributeRules[].values[].extendInfo` | string | 否 | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `data.productAttributeRules[].values[].group` | object | 否 | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `data.productAttributeRules[].values[].parentVidList` | array&lt;integer> | 否 | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| `data.isSupportBasePlateCategory` | boolean | 否 | 是否支持底版/套版，为true时创建产品可设置isBasePlate |
| `data.requiredSizeTemplate` | boolean | 否 | 尺码模板是否必填，为true时创建产品必须传sizeCharts |
| `data.requiredGoodsModel` | boolean | 否 | 模特信息是否必填，为true时创建产品必须传goodsModelReqs |
| `data.requiredSizeChart` | boolean | 否 | 尺码表是否必填 |
| `data.inputMaxSpecNum` | integer | 否 | 自定义规格数量上限，saleAttributes中自定义输入的规格不能超过此值 0则不限制 |
| `data.isShoesClass` | boolean | 否 | 是否鞋类类目，为true时尺码表需按鞋码规则填写 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "cid": 1,
  "shopIds": [
    1
  ]
}
```
&lt;/details>
