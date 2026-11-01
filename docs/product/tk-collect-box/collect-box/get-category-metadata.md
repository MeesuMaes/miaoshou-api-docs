# 获取类目属性信息


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_category_metadata`
- 类型：读
- 原文：[446814589e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814589e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 否 | 站点(shopIds为空时必传) |
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array&lt;integer> | 否 | 店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.categoryMetadata` | object | 否 | 分类元数据 |
| `data.categoryMetadata.categoryConfig` | object | 否 | 分类配置 |
| `data.categoryMetadata.categoryConfig.isSuppSizechart` | string | 否 | 是否支持尺码表 |
| `data.categoryMetadata.categoryConfig.isSuppCod` | boolean | 否 | 是否支持货到付款 |
| `data.categoryMetadata.categoryConfig.productCertifications` | array&lt;object> | 否 | 商品认证列表 |
| `data.categoryMetadata.categoryConfig.productCertifications[].documentDetails` | string | 否 | 认证文件说明 |
| `data.categoryMetadata.categoryConfig.productCertifications[].id` | string | 否 | 认证ID |
| `data.categoryMetadata.categoryConfig.productCertifications[].isRequired` | boolean | 否 | 是否必填 |
| `data.categoryMetadata.categoryConfig.productCertifications[].name` | string | 否 | 认证名称 |
| `data.categoryMetadata.categoryConfig.productCertifications[].sampleImageUrl` | string | 否 | 示例图片URL |
| `data.categoryMetadata.categoryConfig.productCertifications[].isMandatory` | boolean | 否 | 是否强制要求 |
| `data.categoryMetadata.categoryConfig.productCertifications[].requirementConditions` | array&lt;object> | 否 | 需求条件列表 |
| `data.categoryMetadata.categoryConfig.isSupportExemptionIdentifierCode` | string | 否 | 是否支持豁免标识码 |
| `data.categoryMetadata.categoryConfig.sizeChartIsSupported` | string | 否 | 尺码表是否支持 |
| `data.categoryMetadata.categoryConfig.sizeChartIsRequired` | string | 否 | 尺码表是否必填 |
| `data.categoryMetadata.categoryConfig.codIsSupported` | string | 否 | 货到付款是否支持 |
| `data.categoryMetadata.categoryConfig.packageDimensionIsRequired` | string | 否 | 包装尺寸是否必填 |
| `data.categoryMetadata.categoryConfig.eprIsRequired` | string | 否 | EPR是否必填 |
| `data.categoryMetadata.categoryConfig.responsiblePersonIsRequired` | string | 否 | 责任人是否必填 |
| `data.categoryMetadata.categoryConfig.manufacturerIsRequired` | string | 否 | 制造商是否必填 |
| `data.categoryMetadata.categoryConfig.isSizeChartMandatory` | string | 否 | 尺码表是否强制 |
| `data.categoryMetadata.categorySaleAttrList` | array&lt;object> | 否 | 销售属性列表 |
| `data.categoryMetadata.categorySaleAttrList[].attrId` | string | 否 | 属性ID |
| `data.categoryMetadata.categorySaleAttrList[].name` | string | 否 | 属性名称（英文） |
| `data.categoryMetadata.categorySaleAttrList[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.categoryMetadata.categorySaleAttrList[].attributeType` | integer | 否 | 属性类型 |
| `data.categoryMetadata.categorySaleAttrList[].isMandatory` | boolean | 否 | 是否必填 |
| `data.categoryMetadata.categorySaleAttrList[].isMultipleSelected` | boolean | 否 | 是否可多选 |
| `data.categoryMetadata.categorySaleAttrList[].isCustomized` | boolean | 否 | 是否可自定义 |
| `data.categoryMetadata.categorySaleAttrList[].valueDataFormat` | object | 否 | 值数据格式 |
| `data.categoryMetadata.categorySaleAttrList[].isCertificationAttr` | boolean | 否 | 是否认证属性 |
| `data.categoryMetadata.categorySaleAttrList[].requirementConditions` | object | 否 | 需求条件 |
| `data.categoryMetadata.categorySaleAttrList[].valueIdAndRequiredAttrIdsMap` | object | 否 | 值ID与必填属性ID映射 |
| `data.categoryMetadata.categorySaleAttrList[].valueIdAndRequiredCertificationIdsMap` | object | 否 | 值ID与必填认证ID映射 |
| `data.categoryMetadata.categorySaleAttrList[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.categoryMetadata.categorySaleAttrList[].values[].id` | string | 否 | 属性值ID |
| `data.categoryMetadata.categorySaleAttrList[].values[].name` | string | 否 | 属性值名称（英文） |
| `data.categoryMetadata.categorySaleAttrList[].values[].valueNameAlias` | string | 否 | 属性值名称别名（中文） |
| `data.categoryMetadata.categorySaleAttrList[].optionalRegions` | array&lt;string> | 否 | 可选地区列表 |
| `data.categoryMetadata.categorySaleAttrList[].requiredRegions` | array&lt;string> | 否 | 必填地区列表 |
| `data.categoryMetadata.categoryProductAttrList` | array&lt;object> | 否 | 商品属性列表 |
| `data.categoryMetadata.categoryProductAttrList[].attrId` | string | 否 | 属性ID |
| `data.categoryMetadata.categoryProductAttrList[].name` | string | 否 | 属性名称（英文） |
| `data.categoryMetadata.categoryProductAttrList[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.categoryMetadata.categoryProductAttrList[].attributeType` | integer | 否 | 属性类型 |
| `data.categoryMetadata.categoryProductAttrList[].isMandatory` | boolean | 否 | 是否必填 |
| `data.categoryMetadata.categoryProductAttrList[].isMultipleSelected` | boolean | 否 | 是否可多选 |
| `data.categoryMetadata.categoryProductAttrList[].isCustomized` | boolean | 否 | 是否可自定义 |
| `data.categoryMetadata.categoryProductAttrList[].valueDataFormat` | object | 否 | 值数据格式 |
| `data.categoryMetadata.categoryProductAttrList[].isCertificationAttr` | boolean | 否 | 是否认证属性 |
| `data.categoryMetadata.categoryProductAttrList[].requirementConditions` | object | 否 | 需求条件 |
| `data.categoryMetadata.categoryProductAttrList[].valueIdAndRequiredAttrIdsMap` | object | 否 | 值ID与必填属性ID映射 |
| `data.categoryMetadata.categoryProductAttrList[].valueIdAndRequiredCertificationIdsMap` | object | 否 | 值ID与必填认证ID映射 |
| `data.categoryMetadata.categoryProductAttrList[].values` | array&lt;object> | 否 | 属性值列表 |
| `data.categoryMetadata.categoryProductAttrList[].values[].id` | string | 否 | 属性值ID |
| `data.categoryMetadata.categoryProductAttrList[].values[].name` | string | 否 | 属性值名称（英文） |
| `data.categoryMetadata.categoryProductAttrList[].values[].valueNameAlias` | string | 否 | 属性值名称别名（中文） |
| `data.categoryMetadata.categoryProductAttrList[].optionalRegions` | array&lt;string> | 否 | 可选地区列表 |
| `data.categoryMetadata.categoryProductAttrList[].requiredRegions` | array&lt;string> | 否 | 必填地区列表 |
