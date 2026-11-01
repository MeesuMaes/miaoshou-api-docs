# 创建采集箱商品


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/create_collect_box_item`
- 类型：写
- 原文：[477347602e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347602e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口。 pddkjChoice 特有：需填写 publishSiteList（发布站点）、siteAndSkuPriceMap（站点维度价格）、 siteAndWarehouseIdAndStockMap（站点+仓库库存）等 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array&lt;object> | 是 | 店铺列表，保存站点模式必填。 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array&lt;string> | 否 | 发布站点列表，pddkjChoice 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishEuSiteList` | array&lt;string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array&lt;object> | 否 | 站点仓库列表，US 站直接填 warehouseId，EU 站填 subSiteWarehouseList |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，非 EU 站点时必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array&lt;object> | 否 | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array&lt;object> | 否 | 站点运费模板列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguageType` | integer | 否 | 多语言素材类型 |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguages` | array&lt;string> | 否 | 多语言素材语言列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.translateLanguages` | array&lt;string> | 否 | 翻译语言列表，指定需要自动翻译的目标语言编码（如 ["en","de","es"]） |
| `siteCollectItemInfo.itemNum` | string | 否 | 非服饰类主货号（skuMap 同级字段，与 skuMap 内各 SKU 的 itemNum 含义不同） |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array&lt;object> | 否 | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.imgUrls` | array&lt;string> | 是 | 轮播图 |
| `siteCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为该店铺对应的单条 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在此处独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.productMaterialImageUrl` | string | 否 | 实拍素材图URL |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array&lt;object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer | 否 | 字体大小 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string | 否 | 字体粗细 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string | 否 | 对齐方式 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string | 否 | 字体颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string | 否 | 背景颜色 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer | 否 | 字体族 |
| `siteCollectItemInfo.productGuideFileUrl` | string | 否 | 产品说明书URL |
| `siteCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名，最多25个字 |
| `siteCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array&lt;integer> | 否 | 展示尺码模板ID列表 |
| `siteCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `siteCollectItemInfo.sizeCharts` | array&lt;object> | 否 | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array&lt;integer> | 否 | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array&lt;integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array&lt;object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array&lt;object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array&lt;object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array&lt;object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ \{ "vehicleLibraryId": 1, "productPropValueDependencyList": [ [ \{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"\}, \{"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"\}, \{"level":3,"propertyValueDependencyId":300,"vidValue":"2022"\}, \{"level":4,"propertyValueDependencyId":400,"vidValue":"LE"\}, \{"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"\}] ] \} ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array&lt;int, array&lt;int, array\{vidValue: string, propertyValueDependencyId: string, level: string\}>> |
| `siteCollectItemInfo.attributes` | array&lt;object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array&lt;object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array&lt;object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array&lt;object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array&lt;string> | 否 | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `siteCollectItemInfo.publishSiteList` | array&lt;string> | 是 | 发布站点列表，如['US','JP'] 取值参考 getPublishSiteOptions接口返回的站点列表 |
| `siteCollectItemInfo.publishEuSiteList` | array&lt;string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.siteAndSkuPriceMap` | object | 否 | 按站点维度的 SKU 价格映射。 key 为站点编码，value 为该站点下各 SKU 的价格信息。 欧盟站点下还需填写 subSiteAndPriceMap（子站点价格），法国站点价格必填 |
| `siteCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `siteCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型，取值参考 PddkjChoiceConst |
| `siteCollectItemInfo.materialMultiLanguages` | array&lt;string> | 否 | 多语言素材语言列表，与 materialMultiLanguageType 配合使用， 决定哪些语言需要提供多语言图片素材 |
| `siteCollectItemInfo.discreetShipping` | string | 否 | 保密发货，0=关闭，1=开启 |
| `siteCollectItemInfo.currency` | string | 否 | 币种，如 CNY、USD |
| `siteCollectItemInfo.shipmentLimitDay` | integer | 否 | 其他站点承诺发货时效 非定制品可选值只有 1,2 |
| `siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array&lt;string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 创建成功的采集箱详情ID |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "siteCollectItemInfo": {
    "cid": "29172",
    "title": "New Style Comfortable Breathable Casual Shoes Lightweight Running Sneakers Men Women",
    "multiLanguageTitleMap": {
      "en": "New Style Comfortable Breathable Casual Shoes Lightweight Running Sneakers Men Women"
    },
    "productOriginCountry": "CN",
    "productOriginProvince": "43000000000011",
    "imgUrls": [
      "https://img.kwcdn.com/product/fancy/739386b8-e67b-4372-96b2-8fcfd2474b73.jpg",
      "https://img.kwcdn.com/product/fancy/c678d99a-3248-4105-9997-2f8080d77419.jpg",
      "https://img.kwcdn.com/product/fancy/33094a94-bb6b-40ab-b13a-c20ba801d251.jpg"
    ],
    "goodsLayerDecorationReqs": [
      {
        "type": "image",
        "content": {
          "imgUrl": "https://img.kwcdn.com/product/fancy/739386b8-e67b-4372-96b2-8fcfd2474b73.jpg"
        }
      },
      {
        "type": "text",
        "content": {
          "text": "Product description here",
          "textModuleDetails": {
            "fontSize": 14,
            "fontWeight": "normal",
            "align": "left",
            "fontColor": "#000000",
            "backgroundColor": "#FFFFFF",
            "fontFamily": 1
          }
        }
      }
    ],
    "attributes": [
      {
        "templatePid": "1700252",
        "pid": "10",
        "refPid": "26",
        "name": "图案",
        "values": [
          {
            "vid": 222,
            "name": "格子",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700254",
        "pid": "709",
        "refPid": "466",
        "name": "鞋跟类型",
        "values": [
          {
            "vid": 19005,
            "name": "粗跟",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700255",
        "pid": "703",
        "refPid": "419",
        "name": "关闭",
        "values": [
          {
            "vid": 18910,
            "name": "拉链",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700256",
        "pid": "554",
        "refPid": "420",
        "name": "脚趾样式",
        "values": [
          {
            "vid": 15038,
            "name": "尖头",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700261",
        "pid": "1734",
        "refPid": "3672",
        "name": "跟高类型",
        "values": [
          {
            "vid": 62870,
            "name": "中跟",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700263",
        "pid": "1294",
        "refPid": "1259",
        "name": "鞋面材料",
        "values": [
          {
            "vid": 31111,
            "name": "橡胶",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700264",
        "pid": "1293",
        "refPid": "1260",
        "name": "内里材料",
        "values": [
          {
            "vid": 63606,
            "name": "橡胶",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700265",
        "pid": "1290",
        "refPid": "1262",
        "name": "鞋垫材料",
        "values": [
          {
            "vid": 31052,
            "name": "橡胶",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700266",
        "pid": "1289",
        "refPid": "1261",
        "name": "鞋底材料",
        "values": [
          {
            "vid": 31037,
            "name": "橡胶",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700268",
        "pid": "4",
        "refPid": "20",
        "name": "护理说明",
        "values": [
          {
            "vid": 26001,
            "name": "可机洗且不可干洗",
            "valueUnit": ""
          }
        ]
      },
      {
        "templatePid": "1700271",
        "pid": "2394",
        "refPid": "7654",
        "name": "内里是否加绒",
        "values": [
          {
            "vid": 404104,
            "name": "是",
            "valueUnit": ""
          }
        ]
      }
    ],
    "saleAttributes": [
      {
        "templatePid": 1700250,
        "pid": 13,
        "refPid": 63,
        "parentSpecId": 1001,
        "name": "颜色",
        "values": [
          {
            "vid": 0,
            "skuKey": "9d2d1f62",
            "name": "黑色"
          },
          {
            "vid": 0,
            "skuKey": "3ef2c074",
            "name": "棕色"
          }
        ]
      },
      {
        "templatePid": 1700251,
        "pid": 14,
        "refPid": 65,
        "parentSpecId": 3001,
        "name": "尺码",
        "values": [
          {
            "vid": 0,
            "skuKey": "19ca14e7",
            "name": "36"
          },
          {
            "vid": 0,
            "skuKey": "17798773321231",
            "name": "36.5"
          },
          {
            "vid": 0,
            "skuKey": "a5bfc9e0",
            "name": "37"
          }
        ]
      }
    ],
    "skuMap": {
      ";9d2d1f62;19ca14e7;": {
        "price": "9999",
        "originPrice": 64,
        "stock": "0",
        "itemNum": "853842038631@A@15",
        "length": "10",
        "width": "20",
        "height": "10",
        "weight": 700,
        "isSensitive": "0",
        "sensitiveTypes": [],
        "sensitiveLimit": {
          "maxBatteryCapacity": 10
        },
        "barCodeType": "UPC",
        "barCode": "",
        "imgUrl": "https://img.kwcdn.com/product/fancy/739386b8-e67b-4372-96b2-8fcfd2474b73.jpg",
        "multiLanguageImgUrlMap": {
          "en": "https://img.kwcdn.com/product/fancy/739386b8-e67b-4372-96b2-8fcfd2474b73.jpg"
        },
        "suggestedPrice": 0,
        "suggestedPriceCurrencyType": "GBP",
        "goodsSkuId": null,
        "isSupplierDisable": "0",
        "numberOfPieces": 3,
        "skuClassification": 3,
        "productSkuAccessories": [
          {
            "vid": 222143,
            "num": 3,
            "unitCode": 1
          }
     
...（已截断，完整见原文）
```
&lt;/details>
