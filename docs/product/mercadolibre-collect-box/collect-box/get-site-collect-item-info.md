# 获取采集箱详情


- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[482753644e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753644e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 否 | 店铺ID（切换店铺的时候调用） |
| `cid` | integer | 否 | 新类目id（切换类目时填写） |


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
| `data.siteCollectItemInfo` | object | 否 | 站点采集箱数据 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.siteCollectItemInfo.attributes` | array&lt;object> | 否 | 商品属性列表（品牌/型号等） |
| `data.siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.attributes[].valueType` | string | 否 | 属性数据类型 |
| `data.siteCollectItemInfo.attributes[].values` | array&lt;object> | 否 | 行属性值列表 |
| `data.siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.cateList` | array&lt;string> | 否 | 类目面包屑列表 |
| `data.siteCollectItemInfo.firstSkuKey` | string | 否 | 第一个SKU的key,对应skuMap中的key第一个分号数据:例如 ";0a310071;502c632b;"中的";0a310071;" |
| `data.siteCollectItemInfo.originPrice` | number | 否 | 原始价格 |
| `data.siteCollectItemInfo.price` | number | 否 | 价格 |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.notes` | string | 否 | 商品备注/描述 |
| `data.siteCollectItemInfo.notesFull` | string | 否 | 商品完整备注/描述 |
| `data.siteCollectItemInfo.warrantyType` | string | 否 | 保修类型 |
| `data.siteCollectItemInfo.warrantyTime` | string | 否 | 保修时长 |
| `data.siteCollectItemInfo.warrantyTimeUnit` | string | 否 | 保修时长单位 |
| `data.siteCollectItemInfo.sourceImgUrls` | array&lt;string> | 否 | 原始图片URL列表 |
| `data.siteCollectItemInfo.videoUrl` | string | 否 | 视频URL |
| `data.siteCollectItemInfo.sourceAddress` | string | 否 | 货源地址 |
| `data.siteCollectItemInfo.oriItemNum` | string | 否 | 原始货号 |
| `data.siteCollectItemInfo.sourceItemMetaInfo` | object | 否 | 货源商品元信息 |
| `data.siteCollectItemInfo.sourceItemMetaInfo.source` | string | 否 | 货源来源标识 |
| `data.siteCollectItemInfo.sourceItemMetaInfo.sourceNameFw` | string | 否 | 货源来源名称(服务端) |
| `data.siteCollectItemInfo.sourceItemMetaInfo.sourceAddress` | string | 否 | 货源地址 |
| `data.siteCollectItemInfo.sourceItemMetaInfo.sourceAddressFw` | string | 否 | 货源地址(服务端) |
| `data.siteCollectItemInfo.sourceItemMetaInfo.sourceItemId` | string | 否 | 货源商品ID |
| `data.siteCollectItemInfo.sourceItemMetaInfo.oriItemNum` | string | 否 | 原始货号 |
| `data.siteCollectItemInfo.sourceItemMetaInfo.maxSkuPrice` | number | 否 | 最大SKU价格 |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | integer | 否 | 主图APP视频ID |
| `data.siteCollectItemInfo.sourceItemUrl` | string | 否 | 货源商品URL |
| `data.siteCollectItemInfo.collectBoxDetailId` | string | 否 | 采集箱明细ID |
| `data.siteCollectItemInfo.detailId` | string | 否 | 明细ID |
| `data.siteCollectItemInfo.sourceList` | array&lt;object> | 否 | 货源列表 |
| `data.siteCollectItemInfo.sourceList[].remark` | string | 否 | 备注 |
| `data.siteCollectItemInfo.sourceList[].sourceItemId` | string | 否 | 货源商品ID |
| `data.siteCollectItemInfo.sourceList[].source` | string | 否 | 货源来源标识 |
| `data.siteCollectItemInfo.sourceList[].sourceSite` | string | 否 | 货源站点 |
| `data.siteCollectItemInfo.sourceList[].sourceItemUrl` | string | 否 | 货源商品URL |
| `data.siteCollectItemInfo.source` | string | 否 | 货源来源标识 |
| `data.siteCollectItemInfo.sourceNameFw` | string | 否 | 货源来源名称(服务端) |
| `data.siteCollectItemInfo.sourceAddressFw` | string | 否 | 货源地址(服务端) |
| `data.siteCollectItemInfo.sourceItemId` | string | 否 | 货源商品ID |
| `data.siteCollectItemInfo.maxSkuPrice` | number | 否 | 最大SKU价格 |
| `data.siteCollectItemInfo.mainImgVideoGmtExpire` | string | 否 | 主图视频过期时间 |
| `data.siteCollectItemInfo.siteAndListingTypeList` | array&lt;object> | 否 | 站点与刊登类型列表 |
| `data.siteCollectItemInfo.siteAndListingTypeList[].site` | string | 否 | 站点标识 |
| `data.siteCollectItemInfo.siteAndListingTypeList[].listingType` | string | 否 | 刊登类型 |
| `data.siteCollectItemInfo.siteAndTitleList` | array&lt;object> | 否 | 站点与标题列表 |
| `data.siteCollectItemInfo.siteAndTitleList[].site` | string | 否 | 站点标识 |
| `data.siteCollectItemInfo.siteAndTitleList[].title` | string | 否 | 站点商品标题 |
| `data.siteCollectItemInfo.pricingMode` | string | 否 | 售价模式 |
| `data.siteCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.saleAttributes` | array&lt;object> | 否 | 销售属性列表(如: 颜色/尺码) |
| `data.siteCollectItemInfo.saleAttributes[].name` | string | 否 | 销售属性名称(如: Color, Size) |
| `data.siteCollectItemInfo.saleAttributes[].values` | array&lt;object> | 否 | 销售属性值列表 |
| `data.siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识key |
| `data.siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 销售属性值名称 |
| `data.siteCollectItemInfo.sites` | array&lt;string> | 否 | 已选择的站点列表 |
| `data.siteCollectItemInfo.siteAndPriceMap` | object | 否 | 站点价格映射 格式\{ "AR": 5.73, "BR": 200, "CL": 300, "CO": 400, "MX": 500, "MX(Full)": 11.32, "UY": 5.73 \} 或\{\} |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射表,key为SKU组合key(如";0a310071;502c632b;"),value为SKU详情 |
| `data.siteCollectItemInfo.hasSaveSite` | integer | 否 | 是否已保存站点 |
| `data.siteCollectItemInfo.saveDetailTs` | integer | 否 | 保存明细时间戳 |
| `data.siteCollectItemInfo.hasSavePrice` | integer | 否 | 是否已保存价格 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点标识 |
| `data.siteCollectItemInfo.registrationType` | string | 否 | 注册类型 |
