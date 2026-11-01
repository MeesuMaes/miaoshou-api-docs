# 妙手开放平台 · 包裹模块

> 由 apifox 分享文档整理（17 个接口）。字段说明原样摘自 OpenAPI 定义，未做改写；请求/响应以原文为准。

## 目录

- 履约>基础管理（2）
- 售后（2）
- 包裹>运单（6）
- 包裹>基础信息修改（2）
- 包裹>获取包裹（2）
- 包裹>发货（1）
- 采购记录（2）

## 履约>基础管理

### 获取当前账号有效的线下物流列表

- 层级：开放平台 > 包裹 > 履约 > 基础管理
- 方法+路径：`POST /open/v1/order/logistics_agent/manage/get_enable_offline_product_list`
- 类型：读
- 原文：[455528071e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455528071e0.md)（本地 raw/455528071e0_获取当前账号有效的线下物流列表.md）
- 说明：三方物流商以及三方仓

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `logisticsAgentId` | integer | 否 | 物流id |
| `opOrderPackageIds` | array<integer> | 否 | 包裹ids |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | object | 是 |  |
| `data.logisticsAgentAuthConfigOption` | object | 否 |  |
| `data.logisticsAgentAuthConfigOption.` | object | 是 |  |
| `data.logisticsAgentAuthConfigOption..label` | string | 是 | 标签 |
| `data.logisticsAgentAuthConfigOption..agentCode` | string | 是 | 物流商代码 |
| `data.logisticsAgentAuthConfigOption..agentName` | string | 是 | 物流商名称 |
| `data.logisticsAgentAuthConfigOption..options` | array<object> | 是 | 渠道信息 |
| `data.logisticsAgentAuthConfigOption..options[].label` | string | 是 | 渠道标签 |
| `data.logisticsAgentAuthConfigOption..options[].logisticsAgentAuthId` | integer | 是 | 物流授权id |
| `data.logisticsAgentAuthConfigOption..options[].logisticsAgentProductId` | integer | 是 | 物流渠道id |
| `data.logisticsAgentAuthConfigOption..options[].productCode` | string | 是 | 物流渠道编码 |
| `data.logisticsAgentAuthConfigOption..options[].logisticsCompany` | string | 是 | 物流公司 |
| `data.logisticsAgentAuthConfigOption..options[].status` | string | 是 | 渠道状态 |
| `data.logisticsAgentAuthConfigOption..options[].isEnabled` | boolean | 是 | 是否启用 |
| `data.logisticsAgentAuthConfigOption..options[].isSupportPlatformLastMile` | integer | 是 | 是否支持尾程平台 |
| `data.logisticsAgentAuthConfigOption..options[].productName` | string | 是 | 物流渠道名称 |
| `data.logisticsAgentAuthConfigOption..options[].platformLogisticsProductMap` | object | 是 | 平台渠道映射表 |
| `data.logisticsAgentAuthConfigOption..options[].toLogisticsAgentProductInfo` | object | 是 |  |
| `data.logisticsAgentAuthConfigOption..options[].value` | string | 是 | 映射尾程配置id |
| `data.logisticsAgentAuthConfigOption..logisticsAgentWarehouseName` | string | 是 | 仓库id |
| `data.logisticsAgentAuthConfigOption..logisticsAgentWarehouseId` | string | 是 | 仓库名称 |
| `data.logisticsAgentAuthConfigOption..type` | string | 是 | logisticsAgent/物流商物流渠道，thirdWarehouse/三方仓物流渠道， supplier/供应商渠道 selfWarehouse/自营仓渠道 |


<details><summary>请求示例</summary>

```json
{
    "logisticsAgentId": 573,
    "opOrderPackageIds": [
        043701
    ]
}
```
</details>

<details><summary>响应示例 200</summary>

```json
{
  "result": "success",
  "code": "success",
  "message": "",
  "data": {
    "logisticsAgentAuthConfigOption": {
      "4403605": {
        "label": "德鑫-预发布",
        "agentCode": "qingZhouSystem_deXing",
        "agentName": "深圳市德鑫供应链有限公司",
        "options": [
          {
            "label": "TK-LAX 美国快线小包",
            "value": "8601322",
            "logisticsAgentAuthId": "4403605",
            "logisticsAgentProductId": "29322155",
            "productCode": "TK-LAX_MGKXXB",
            "logisticsCompany": null,
            "status": "normal",
            "isEnabled": 1,
            "logisticsFreightTemplateId": null,
            "platformAndShopIdAndPickupAddressIdMap": null,
            "platformAndShopIdAndLastMileWarehouseIdMap": null,
            "platformLogisticsProductMap": {
              "tiktok": {
                "platform": "tiktok",
                "productKeyword": [
                  "realTime"
                ],
                "printWaybillType": "lastMile"
              }
            },
            "isSupportPlatformLastMile": "1",
            "agentCode": "qingZhouSystem_deXing",
            "productName": "TK-LAX 美国快线小包"
          },
          {
            "label": "Y2-ORD美中 服装普货",
            "value": "8608543",
            "logisticsAgentAuthId": "4403605",
            "logisticsAgentProductId": "29322162",
            "productCode": "Y2-ORDMZ_FZPH",
            "logisticsCompany": null,
            "status": "normal",
            "isEnabled": 1,
            "logisticsFreightTemplateId": null,
            "platformAndShopIdAndPickupAddressIdMap": null,
            "platformAndShopIdAndLastMileWarehouseIdMap": null,
            "platformLogisticsProductMap": {
              "pddkjChoice": {
                "platform": null,
                "productKeyword": [
                  "realTime"
                ],
                "printWaybillType": "firstMile"
              }
            },
            "isSupportPlatformLastMile": "1",
            "agentCode": "qingZhouSystem_deXing",
            "productName": "Y2-ORD美中 服装普货"
          }
        ],
        "type": "logisticsAgent"
      },
      "4403606": {
        "agentCode": "qingZhouSystem_deXing",
        "agentName": "深圳市德鑫供应链有限公司",
        "label": "德鑫-预发布",
        "options": [
          {
            "isEnabled": true,
            "isSupportPlatformLastMile": 1,
            "label": "TK-LAX 美国快线小包",
            "logisticsAgentAuthId": "4403605",
            "logisticsAgentProductId": 29322155,
            "logisticsCompany": null,
            "logisticsFreightTemplateId": null,
            "productCode": "TK-LAX_MGKXXB",
            "productName": "TK-LAX 美国快线小包",
            "status": "normal",
            "platformLogisticsProductMap": {
              "tiktok": {
                "platform": "tiktok",
                "printWaybillType": "lastMile",
                "productKeyword": [
                  "realTime"
                ]
              }
            },
            "toLogisticsAgentProductInfo": null
          },
          {
            "isEnabled": true,
            "isSupportPlatformLastMile": 1,
            "label": "Y2-ORD美中 服装普货",
            "logisticsAgentAuthId": "4403605",
            "logisticsAgentProductId": 29322162,
            "logisticsCompany": null,
            "logisticsFreightTemplateId": null,
            "productCode": "Y2-ORDMZ_FZPH",
            "productName": "Y2-ORD美中 服装普货",
            "status": "normal",
            "platformLogisticsProductMap": {
              "pddkjChoice": {
                "platform": null,
                "printWaybillType": "firstMile",
                "productKeyword": [
                  "realTime"
                ]
              }
            },
            "toLogisticsAgentProductInfo": null
          }
        ],
        "type": "logisticsAgent",
        "logisticsAgentWarehouseName": null,
        "logisticsAgentWarehouseId": null
      },
      "4403607": {
        "agentCode": "yuanCang",
        "agentName": "元仓",
        "label": "元仓-yc_mQ354NBQlDixWaOAUca0GcAZB - YCMY-TENGFEI",
        "options": [
          {
            "isEnabled": true,
            "isSupportPlatformLastMile": 0,
            "label": "TikTok-J&T Express",
            "logisticsAgentAuthId": "thirdWarehouse-1422",
            "logisticsAgentProductId": 1072238,
            "logisticsCompany": "",
            "logisticsFreightTemplateId": null,
            "productCode": "YT013",
            "productName": null,
            "status": "normal",
            "platformLogisticsProductMap": null,
            "toLogisticsAgentProductInfo": null
          }
        ],
        "type": "thirdWarehouse",
        "logisticsAgentWarehouseName": null,
        "logisticsAgentWarehouseId": null
      },
      "4403608": {
        "agentCode": "fbac",
        "agentName": "FBAC",
        "label": "fbac - 加州仓",
        "options": [
          {
            "isEnabled": true,
            "isSupportPlatformLastMile": 0,
            "label": "自传Label",
            "logisticsAgentAuthId": "thirdWarehouse-5731",
            "logisticsAgentProductId": 1494,
            "logisticsCompany": "",
            "logisticsFreightTemplateId": null,
            "productCode": "自传Label",
            "productName": null,
            "status": "normal",
            "platformLogisticsProductMap": null,
            "toLogisticsAgentProductInfo": null
          }
        ],
        "type": "thirdWarehouse",
        "logisticsAgentWarehouseName": null,
        "logisticsAgentWarehouseId": null
      },
      "4403609": {
        "agentCode": "yiCang_kuaiMa",
        "agentName": "快马",
        "label": "kuaima - 美国洛杉矶仓",
        "options": [
          {
            "isEnabled": true,
            "isSupportPlatformLastMile": 0,
            "label": "USPS_93U",
            "logisticsAgentAuthId": "thirdWarehouse-7471",
            "logisticsAgentProductId": 6245,
            "logisticsCompany": "",
        
...（已截断，完整见原文）
```
</details>

---

### 获取当前包裹有效的线上物流列表

- 层级：开放平台 > 包裹 > 履约 > 基础管理
- 方法+路径：`POST /open/v1/order/logistics_agent/manage/get_enable_online_product_list`
- 类型：读
- 原文：[455611090e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455611090e0.md)（本地 raw/455611090e0_获取当前包裹有效的线上物流列表.md）
- 说明：在线发货以及拼接物流

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹id |
| `logisticsAgentAuthId` | integer | 是 | 物流授权id |
| `agentCode` | string | 是 | 物流商编码 |
| `weight` | string | 否 | 小数点后两位 |
| `length` | string | 否 | 长 |
| `width` | string | 否 | 宽 |
| `height` | string | 否 | 高 |
| `weightUnit` | string | 否 | 枚举值 g、mg、kg、oz、lbs |
| `dimensionUnit` | string | 否 | 枚举值 cm、in、mm、m、ft |
| `signatureOnDelivery` | boolean | 否 | temu 专属字段 |
| `warehouseId` | string | 否 | 仓库id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array<object> | 是 |  |
| `data[].logisticsAgentAuthConfigOption` | object | 是 |  |
| `data[].logisticsAgentAuthConfigOption.label` | string | 否 | 渠道标签 |
| `data[].logisticsAgentAuthConfigOption.agentCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.agentName` | string | 否 | 物流商名称 |
| `data[].logisticsAgentAuthConfigOption.options` | array<object> | 否 | 物流渠道数据 |
| `data[].logisticsAgentAuthConfigOption.options[].label` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.options[].logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data[].logisticsAgentAuthConfigOption.options[].logisticsAgentProductId` | string | 否 | 物流渠道id |
| `data[].logisticsAgentAuthConfigOption.options[].productCode` | string | 否 | 物流渠道code |
| `data[].logisticsAgentAuthConfigOption.options[].logisticsCompany` | string | 否 | 物流公司 |
| `data[].logisticsAgentAuthConfigOption.options[].status` | string | 否 | 渠道状态 |
| `data[].logisticsAgentAuthConfigOption.options[].isEnabled` | integer | 否 | 是否启用 |
| `data[].logisticsAgentAuthConfigOption.options[].isSupportPlatformLastMile` | string | 否 | 是否支持尾程平台 |
| `data[].logisticsAgentAuthConfigOption.options[].agentCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.options[].productName` | string | 否 | 物流渠道名称 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo` | object | 否 | 物流预估费用 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.fee` | string | 是 | 物流费用 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.currency` | string | 是 | 物流费用货币单位 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.estimatedDayStr` | string | 是 | 预估履约时间段 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.estimatedDayUnit` | string | 是 | 预估履约时间单位 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.signServiceName` | null | 是 | temu 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.signServiceId` | null | 是 | temu 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.estimatedMinDayStr` | string | 是 | 预估履约时间 最小时间 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.estimatedMaxDayStr` | string | 是 | 预估履约时间 最大时间 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.preRequestId` | string | 是 | shein 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.aplLevelCode` | string | 是 | 速卖通 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.aplLevelName` | string | 是 | 速卖通 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.aplLevelRank` | string | 是 | 速卖通 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.aplDeliveryTag` | string | 是 | 速卖通 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.aplDeliveryName` | string | 是 | 速卖通 专属 |
| `data[].logisticsAgentAuthConfigOption.options[].estimatedInfo.aplDeliveryRank` | string | 是 | 速卖通 专属 |
| `data[].logisticsAgentAuthConfigOption.type` | string | 否 | logisticsAgent/物流商物流渠道，thirdWarehouse/三方仓物流渠道， supplier/供应商渠道 selfWarehouse/自营仓渠道 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap` | array<object> | 否 | 拼接渠道数据 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].label` | string | 否 | 渠道标签 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].agentCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].agentName` | string | 否 | 物流商名称 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options` | array<object> | 否 | 开启的渠道数据 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].label` | string | 否 | 渠道标签 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].logisticsAgentProductId` | string | 否 | 物流渠道id |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].productCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].logisticsCompany` | string | 否 | 物流公司 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].status` | string | 否 | 渠道状态 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].isEnabled` | boolean | 否 | 是否启用 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].platformLogisticsProductMap` |  | 否 |  |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].isSupportPlatformLastMile` | string | 否 | 是否支持尾程平台 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].agentCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].productName` | string | 否 | 物流渠道名称 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].lastMilePlatforms` | array<string> | 否 | 尾程支持平台 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].estimatedInfo` | object | 否 | 渠道测算信息 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].lastMileLogisticsAgentAuthConfigId` | string | 否 | 尾程授权配置id |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].type` | string | 否 | logisticsAgent/物流商物流渠道，thirdWarehouse/三方仓物流渠道， supplier/供应商渠道 selfWarehouse/自营仓渠道 |


<details><summary>响应示例 200</summary>

```json
{
  "result": "success",
  "logisticsAgentAuthConfigOption": [
    {
      "label": "et ut",
      "agentCode": "25",
      "agentName": "介秀兰",
      "options": [
        {
          "label": "incididunt aliqua nostrud fugiat consequat",
          "logisticsAgentAuthId": "66",
          "logisticsAgentProductId": "56",
          "productCode": "64",
          "logisticsCompany": "ex nostrud sit in laborum",
          "status": "eu non consectetur reprehenderit tempor",
          "isEnabled": 6,
          "isSupportPlatformLastMile": "non",
          "agentCode": "29",
          "productName": "优雅的橡胶球",
          "estimatedInfo": {
            "fee": "non pariatur do",
            "currency": "consectetur ut",
            "estimatedDayStr": "2026-08-28",
            "estimatedDayUnit": "2026-11-14",
            "signServiceName": null,
            "signServiceId": null,
            "estimatedMinDayStr": "2027-02-18",
            "estimatedMaxDayStr": "2026-08-24",
            "preRequestId": "11",
            "aplLevelCode": "29",
            "aplLevelName": "泰敬彪",
            "aplLevelRank": "dolore occaecat sint labore",
            "aplDeliveryTag": "id in nostrud nulla",
            "aplDeliveryName": "清国兰",
            "aplDeliveryRank": "est minim"
          }
        },
        {
          "label": "officia aliquip Ut est",
          "logisticsAgentAuthId": "45",
          "logisticsAgentProductId": "25",
          "productCode": "9",
          "logisticsCompany": "in consequat nostrud nulla eu",
          "status": "cillum",
          "isEnabled": 86,
          "isSupportPlatformLastMile": "enim Duis laboris consequat in",
          "agentCode": "35",
          "productName": "回收的钢鸡肉",
          "estimatedInfo": {
            "fee": "cupidatat",
            "currency": "eu ipsum velit minim",
            "estimatedDayStr": "2026-02-26",
            "estimatedDayUnit": "2025-05-13",
            "signServiceName": null,
            "signServiceId": null,
            "estimatedMinDayStr": "2026-10-23",
            "estimatedMaxDayStr": "2026-08-11",
            "preRequestId": "87",
            "aplLevelCode": "38",
            "aplLevelName": "钦诚",
            "aplLevelRank": "nulla",
            "aplDeliveryTag": "consequat",
            "aplDeliveryName": "繁雅鑫",
            "aplDeliveryRank": "qui mollit esse"
          }
        }
      ],
      "type": "culpa",
      "logisticsAgentAuthIdAndLastMileOptionInfoMap": [
        {
          "label": "ex consequat nostrud quis",
          "agentCode": "41",
          "agentName": "青振东",
          "options": [
            {
              "label": "sunt deserunt nisi Lorem",
              "logisticsAgentAuthId": "36",
              "logisticsAgentProductId": "26",
              "productCode": "50",
              "logisticsCompany": "in do Ut anim",
              "status": "in cillum",
              "isEnabled": true,
              "platformLogisticsProductMap": {
                "pddkjChoice": {
                  "platform": null,
                  "productKeyword": [
                    "deserunt consectetur ullamco non veniam",
                    "adipisicing",
                    "cillum id magna"
                  ],
                  "printWaybillType": "et ut in"
                }
              },
              "isSupportPlatformLastMile": "sed cillum cupidatat sint dolor",
              "agentCode": "23",
              "productName": "好吃钢桌子",
              "lastMilePlatforms": [
                "ipsum amet dolore esse quis"
              ],
              "estimatedInfo": {
                "fee": "dolor voluptate dolore",
                "currency": "ullamco sint deserunt dolor nostrud",
                "estimatedDayStr": "2025-09-26",
                "estimatedDayUnit": "2025-06-07",
                "signServiceName": null,
                "signServiceId": null,
                "estimatedMinDayStr": "2027-01-02",
                "estimatedMaxDayStr": "2026-03-11",
                "preRequestId": "23",
                "apiLevelCode": "95",
                "apiLevelName": "蔺燕",
                "apiLevelRank": "in eu nisi commodo Excepteur",
                "apiDeliveryTag": "57",
                "apiDeliveryName": "夙伟",
                "apiDeliveryRank": "89"
              },
              "lastMileLogisticsAgentAuthConfigId": "18"
            },
            {
              "label": "ullamco elit",
              "logisticsAgentAuthId": "37",
              "logisticsAgentProductId": "38",
              "productCode": "16",
              "logisticsCompany": "ad",
              "status": "dolore dolore",
              "isEnabled": false,
              "platformLogisticsProductMap": {
                "pddkjChoice": {
                  "platform": null,
                  "productKeyword": [
                    "consequat nisi"
                  ],
                  "printWaybillType": "consequat tempor Lorem occaecat"
                }
              },
              "isSupportPlatformLastMile": "minim enim eu sint esse",
              "agentCode": "9",
              "productName": "智能的塑料肥皂",
              "lastMilePlatforms": [
                "consequat mollit",
                "sint id do occaecat in",
                "dolor"
              ],
              "estimatedInfo": {
                "fee": "amet ut",
                "currency": "elit laboris dolore nisi enim",
                "estimatedDayStr": "2026-04-22",
                "estimatedDayUnit": "2026-04-09",
                "signServiceName": null,
                "signServiceId": null,
                "estimatedMinDayStr": "2026-11-09",
                "estimatedMaxDayStr": "2026-11-10",
                "preRequestId": "68",
                "apiLevelCode": "69",
                "apiLevelName": "刑浩辰",
                "apiLevelRank": "minim culpa",
                "apiDeliveryTag": "1",
                "apiDeliveryName": "历燕",
                "apiDeliveryRank": "36"
           
...（已截断，完整见原文）
```
</details>

## 售后

### 获取退货退款列表

- 层级：开放平台 > 包裹 > 售后
- 方法+路径：`POST /open/v1/order/after_sales/fetch/order_return_list`
- 类型：读
- 原文：[477739260e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477739260e0.md)（本地 raw/477739260e0_获取退货退款列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `gmtStartFrom` | string | 否 | 售后/订单起始时间 |
| `gmtStartTo` | string | 否 | 售后/订单结束时间 |
| `platformReturnSns` | string | 否 | 平台售后单号 |
| `platformOrderSns` | string | 否 | 平台订单号 |
| `platform` | string | 否 | 平台 |
| `page` | integer | 否 | 页码 |
| `pageSize` | integer | 否 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.returnList` | array<object> | 否 | 退货退款单列表 |
| `data.returnList[].opOrderReturnId` | string | 否 | 售后单ID |
| `data.returnList[].opOrderId` | string | 否 | 订单ID |
| `data.returnList[].platformReturnSn` | string | 否 | 平台售后单号 |
| `data.returnList[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.returnList[].shopId` | string | 否 | 店铺ID |
| `data.returnList[].shopName` | string | 否 | 店铺名称 |
| `data.returnList[].shopNickName` | string | 否 | 店铺自定义名称 |
| `data.returnList[].platform` | string | 否 | 平台 |
| `data.returnList[].site` | string | 否 | 站点 |
| `data.returnList[].siteName` | string | 否 | 站点名称 |
| `data.returnList[].status` | string | 否 | 售后状态 |
| `data.returnList[].platformReturnStatus` | string | 否 | 平台售后状态 |
| `data.returnList[].appReturnStatusText` | string | 否 | 妙手售后状态文案 |
| `data.returnList[].reverseType` | string | 否 | 售后类型 |
| `data.returnList[].textReason` | string | 否 | 售后/退货原因文案（原文） |
| `data.returnList[].textReasonCn` | string | 否 | 售后/退货原因文案（中文） |
| `data.returnList[].refundAmount` | string | 否 | 退款金额 |
| `data.returnList[].currency` | string | 否 | 币种 |
| `data.returnList[].returnTrackingNo` | string | 否 | 退回运单号 |
| `data.returnList[].returnLogisticsCompany` | string | 否 | 退货物流商 |
| `data.returnList[].needsLogistics` | string | 否 | 是否需要退回物流 |
| `data.returnList[].gmtCreateTime` | string | 否 | 售后时间 |
| `data.returnList[].gmtDueDate` | string | 否 | 最晚处理时间 |
| `data.returnList[].items` | array<object> | 否 | 商品列表 |
| `data.returnList[].items[].title` | string | 否 | 商品标题 |
| `data.returnList[].items[].picUrl` | string | 否 | 商品图片URL |
| `data.returnList[].items[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.returnList[].items[].platformSkuId` | string | 否 | 平台SKUID |
| `data.returnList[].items[].quantity` | string | 否 | 数量 |
| `data.returnList[].consigneeInfo` | object | 否 | 退货人信息 |
| `data.returnList[].consigneeInfo.opOrderId` | string | 否 | 订单ID |
| `data.returnList[].consigneeInfo.name` | string | 否 | 收件人姓名 |
| `data.returnList[].consigneeInfo.katakana` | string | 否 | 收件人假名/日语假名 |
| `data.returnList[].consigneeInfo.phone` | string | 否 | 收件人主电话 |
| `data.returnList[].consigneeInfo.phone1` | string | 否 | 收件人备用电话1 |
| `data.returnList[].consigneeInfo.phone2` | string | 否 | 收件人备用电话2 |
| `data.returnList[].consigneeInfo.email` | string | 否 | 收件人邮箱 |
| `data.returnList[].consigneeInfo.company` | string | 否 | 公司名称 |
| `data.returnList[].consigneeInfo.country` | string | 否 | 国家二字码 |
| `data.returnList[].consigneeInfo.countryName` | string | 否 | 国家名称 |
| `data.returnList[].consigneeInfo.state` | string | 否 | 省/州 |
| `data.returnList[].consigneeInfo.city` | string | 否 | 城市 |
| `data.returnList[].consigneeInfo.district` | string | 否 | 区 |
| `data.returnList[].consigneeInfo.town` | string | 否 | 镇/街道 |
| `data.returnList[].consigneeInfo.houseNumber` | string | 否 | 门牌号 |
| `data.returnList[].consigneeInfo.zipcode` | string | 否 | 邮编 |
| `data.returnList[].consigneeInfo.address` | string | 否 | 简化地址 |
| `data.returnList[].consigneeInfo.address1` | string | 否 | 详细地址1 |
| `data.returnList[].consigneeInfo.address2` | string | 否 | 详细地址2 |
| `data.returnList[].consigneeInfo.address3` | string | 否 | 详细地址3 |
| `data.returnList[].consigneeInfo.fullAddress` | string | 否 | 完整地址 |
| `data.returnList[].consigneeInfo.customsClearanceCode` | string | 否 | 清关编码 |
| `data.total` | integer | 否 | 总数 |
| `data.page` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页数量 |


<details><summary>请求示例</summary>

```json
{
  "gmtStartFrom": "2025-04-27 14:49:20",
  "gmtStartTo": "2025-04-27 14:49:24",
  "platformReturnSns": "",
  "platform": "shopee",
  "platformOrderSns": "",
  "page": 1,
  "pageSize": 20
}
```
</details>

---

### 获取取消订单列表

- 层级：开放平台 > 包裹 > 售后
- 方法+路径：`POST /open/v1/order/after_sales/fetch/order_cancel_list`
- 类型：读
- 原文：[477739261e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477739261e0.md)（本地 raw/477739261e0_获取取消订单列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platformOrderSns` | string | 否 | 平台订单号 |
| `platform` | string | 否 | 平台 |
| `gmtStartFrom` | string | 否 | 售后起始时间 |
| `gmtStartTo` | string | 否 | 售后结束时间 |
| `page` | integer | 否 | 页码 |
| `pageSize` | integer | 否 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cancelList` | array<object> | 否 | 取消订单列表 |
| `data.cancelList[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.cancelList[].shopId` | string | 否 | 店铺ID |
| `data.cancelList[].shopName` | string | 否 | 店铺名称 |
| `data.cancelList[].platform` | string | 否 | 平台 |
| `data.cancelList[].platformName` | string | 否 | 平台名称 |
| `data.cancelList[].site` | string | 否 | 站点 |
| `data.cancelList[].siteName` | string | 否 | 站点名称 |
| `data.cancelList[].textReason` | string | 否 | 取消原因（原文） |
| `data.cancelList[].textReasonCn` | string | 否 | 取消原因（中文） |
| `data.cancelList[].appReturnStatusText` | string | 否 | 妙手取消状态文案 |
| `data.cancelList[].appOrderStatus` | string | 否 | 订单状态 |
| `data.cancelList[].reverseTypeText` | string | 否 | 售后类型文案 |
| `data.cancelList[].gmtCreateTime` | string | 否 | 售后时间 |
| `data.cancelList[].items` | array<object> | 否 | 商品列表 |
| `data.cancelList[].items[].title` | string | 否 | 商品标题 |
| `data.cancelList[].items[].picUrl` | string | 否 | 商品图片URL |
| `data.cancelList[].items[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.cancelList[].items[].platformSkuId` | string | 否 | 平台SKUID |
| `data.cancelList[].items[].quantity` | string | 否 | 数量 |
| `data.total` | integer | 否 | 总数 |
| `data.page` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页数量 |


<details><summary>请求示例</summary>

```json
{
  "platformOrderSns": "",
  "platform": "tiktok",
  "gmtStartFrom": "2026-06-24 16:58:32",
  "gmtStartTo": "2026-06-24 16:58:35",
  "page": 1,
  "pageSize": 20
}
```
</details>

## 包裹>运单

### 申请运单号

- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking_no/apply`
- 类型：写
- 原文：[457255661e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457255661e0.md)（本地 raw/457255661e0_申请运单号.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array<object> | 是 |  |
| `data[].platformPackageNo` | string | 是 | 物流商单号 |
| `data[].headLogisticsNo` | string | 是 | 头程物流商跟踪号 |
| `data[].logisticsNo` | string | 是 | 物流商跟踪号 |
| `data[].logisticsType` | string | 是 | 物流类型 |
| `data[].headLogisticsNoCompany` | string | 是 | 头程物流商公司 |


---

### 批量申请运单号

- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking_no/batch_apply`
- 类型：写
- 原文：[523411121e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523411121e0.md)（本地 raw/523411121e0_批量申请运单号.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 订单包裹IDs |
| `shippingMethod` | string | 否 | 配送方式 (shopee专用) |
| `addressId` | string | 否 | 取件地址 (shopee专用) shippingMethod为pickup时必填 |
| `pickupTimeId` | integer | 否 | 取件时间ID (shopee专用) |
| `trackingNo` | string | 否 | 运单号(shopee专用) |
| `slug` | string | 否 | 物流渠道(shopee专用) |
| `senderRealName` | string | 否 | 发件人名称(shopee专用) |
| `isShipAfterHasLogisticsNo` | string | 否 | 是否获取跟踪单号并发货 |
| `isSetDefaultAddress` | string | 否 | 是否设置为默认地址(shopee专用) |
| `partItemRelationSupplierGoodsProcessType` | string | 否 | 部分商品关联了分销商品时候处理方式，skipPackage 跳过整个包裹， skipNotRelationItem 跳过没关联的商品 |
| `isConfirmSupplierGoodsSkuIdChange` | integer | 否 | 推送供应商商品是否改变0、1 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.trackingNoInfos` | array<object> | 否 | 运单号数据列表 |
| `data.trackingNoInfos[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.trackingNoInfos[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.trackingNoInfos[].platformPackageId` | string | 否 | 平台包裹id |
| `data.trackingNoInfos[].logisticsNo` | string | 否 | 运单号 |
| `data.errors` | array<object> | 否 | 错误数据 |
| `data.errors[].errMsg` | string | 否 | 错误描述 |
| `data.errors[].errCode` | string | 否 | 错误code |
| `data.errors[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.errors[].opOrderId` | integer | 否 | 妙手订单id |
| `data.errors[].platformOrderSn` | string | 否 | 妙手订单编号 |
| `data.errors[].platformPackageId` | string | 否 | 平台包裹id |
| `data.errors[].appPackageNo` | string | 否 | 包裹号 |
| `data.errors[].logisticsNo` | string | 否 | 跟踪号 |
| `data.errors[].logisticsCompany` | string | 否 | 物流公司 |
| `data.errors[].logisticsAgentAuthId` | string | 否 | 授权id |
| `data.errors[].logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.errors[].logisticsAgentId` | integer | 否 | 物流id |
| `data.errors[].agentName` | string | 否 | 物流名称 |


<details><summary>请求示例</summary>

```json
{
  "opOrderPackageIds": [
    2008407593,
    1999236402,
    1992973198,
    1990087996,
    1990087975,
    1990077182,
    1990059646,
    1276648263,
    1274794190,
    1274740924,
    1274689828,
    1274624282,
    1274624254,
    1274121129,
    1274044406,
    1273927611,
    1273924534,
    1271460840,
    1271458829,
    1271158800
  ]
}
```
</details>

---

### 设置包裹物流

- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking_no/save_logistics_agent_product`
- 类型：写
- 原文：[457269520e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457269520e0.md)（本地 raw/457269520e0_设置包裹物流.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 包裹IDs |
| `logisticsAgentAuthConfigId` | integer | 是 | 授权物流配置ID |
| `type` | string | 是 | logisticsAgent-物流商，thirdWarehouse-三方仓物流 |
| `logisticsAgentWarehouseChannelConfigId` | integer | 否 | type=thirdWarehouse时必填 |
| `aliexpressDomesticLogisticsCompanyName` | string | 否 | 速卖通国内物流公司 |
| `aliexpressDomesticLogisticsCompanyId` | integer | 否 | 速卖通国内物流公司ID |
| `aliexpressDomesticTrackingNo` | string | 否 | 速卖通国内物流单号 |
| `warehouseId` | integer | 否 | 暂时只对temu在线物流生效 |
| `partItemRelationSupplierGoodsProcessType` | string | 否 | skipPackage 跳过整个包裹， skipNotRelationItem 跳过没关联的商品 |
| `isShipLater` | string | 否 | 暂时只对temu在线物流生效 |
| `packageWeightAndDimension` | object | 是 | {"1044122969":{"length":1,"width":1,"height":1,"dimensionUnit":"in","weight":1,"weightUnit":"lb","isSavePackageWeightAndDimension":0}} |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array<object> | 是 |  |
| `data[].successCount` | string | 是 |  |
| `data[].failCount` | string | 是 |  |
| `data[].errors` | object | 是 |  |
| `data[].errors.errMsg` | string | 是 | 错误描述 |
| `data[].errors.errCode` | string | 是 | 错误code |
| `data[].errors.opOrderPackageId` | string | 是 | 妙手包裹id |
| `data[].errors.opOrderId` | string | 是 | 妙手订单id |
| `data[].errors.platformOrderSn` | string | 是 | 妙手订单编号 |
| `data[].errors.platformPackageId` | string | 是 | 平台包裹id |
| `data[].errors.appPackageNo` | string | 是 | 包裹号 |
| `data[].errors.logisticsNo` | string | 是 | 跟踪号 |
| `data[].errors.logisticsCompany` | string | 是 | 物流公司 |
| `data[].errors.logisticsAgentAuthId` | string | 是 | 授权id |
| `data[].errors.logisticsAgentProductId` | string | 是 | 物流渠道id |
| `data[].errors.logisticsAgentId` | string | 是 | 物流id |
| `data[].errors.gentName` | string | 是 | 物流名称 |


---

### 获取包裹物流轨迹

- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/tracking/get_tracking_list`
- 类型：读
- 原文：[477263048e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477263048e0.md)（本地 raw/477263048e0_获取包裹物流轨迹.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 订单包裹ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.trackingInfoList` | array<object> | 否 | 物流轨迹列表 |
| `data.trackingInfoList[].description` | string | 否 | 物流轨迹明细 |
| `data.trackingInfoList[].descriptionCn` | string | 否 | 物流轨迹明细（中文） |
| `data.trackingInfoList[].gmtCreate` | string | 否 | 时间 |


<details><summary>请求示例</summary>

```json
{
  "opOrderPackageId": 1567020375
}
```
</details>

---

### 获取运单面单

- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/waybill/get_waybill`
- 类型：读
- 原文：[457264811e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457264811e0.md)（本地 raw/457264811e0_获取运单面单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | string | 是 | 包裹id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array<object> | 是 |  |
| `data[].waybillUrlInfo` | object | 是 | 成功数据 |
| `data[].waybillUrlInfo.platformOrderSn` | string | 是 | 平台单号 |
| `data[].waybillUrlInfo.platformPackageId` | string | 是 | 平台包裹id |
| `data[].waybillUrlInfo.url` | string | 是 | 面单url |
| `data[].error` | object | 是 |  |
| `data[].error.errMsg` | string | 是 | 错误描述 |
| `data[].error.errCode` | string | 是 | 错误code |
| `data[].error.opOrderPackageId` | string | 是 | 妙手包裹id |
| `data[].error.opOrderId` | string | 是 | 妙手订单id |
| `data[].error.platformOrderSn` | string | 是 | 妙手订单编号 |
| `data[].error.platformPackageId` | string | 是 | 平台包裹id |
| `data[].error.appPackageNo` | string | 是 | 包裹号 |
| `data[].error.logisticsNo` | string | 是 | 跟踪号 |
| `data[].error.logisticsCompany` | string | 是 | 物流公司 |
| `data[].error.logisticsAgentAuthId` | string | 是 | 授权id |
| `data[].error.logisticsAgentProductId` | string | 是 | 物流渠道id |
| `data[].error.logisticsAgentId` | string | 是 | 物流id |
| `data[].error.gentName` | string | 是 | 物流名称 |


<details><summary>请求示例 示例 1</summary>

```json
{
  "opOrderPackageId": 43717
}
```
</details>

<details><summary>请求示例 示例 2</summary>

```json
{
  "opOrderPackageId": 43717
}
```
</details>

---

### 批量获取面单

- 层级：开放平台 > 包裹 > 包裹 > 运单
- 方法+路径：`POST /open/v1/order/package/logistics/waybill/batch_get_waybill`
- 类型：读
- 原文：[523411122e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523411122e0.md)（本地 raw/523411122e0_批量获取面单.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 订单包裹IDs |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.waybillPdfInfos` | array<object> | 否 | 面单数据列表 |
| `data.waybillPdfInfos[].platformOrderSn` | string | 否 | 平台订单号 |
| `data.waybillPdfInfos[].platformPackageId` | string | 否 | 平台包裹id |
| `data.waybillPdfInfos[].url` | string | 否 | 面单url |
| `data.waybillPdfInfos[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.errors` | array<object> | 否 | 错误数据 |
| `data.errors[].errMsg` | string | 否 | 错误描述 |
| `data.errors[].errCode` | string | 否 | 错误code |
| `data.errors[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.errors[].opOrderId` | integer | 否 | 妙手订单id |
| `data.errors[].platformOrderSn` | string | 否 | 妙手订单编号 |
| `data.errors[].platformPackageId` | string | 否 | 平台包裹id |
| `data.errors[].appPackageNo` | string | 否 | 包裹号 |
| `data.errors[].logisticsNo` | string | 否 | 跟踪号 |
| `data.errors[].logisticsCompany` | string | 否 | 物流公司 |
| `data.errors[].logisticsAgentAuthId` | string | 否 | 授权id |
| `data.errors[].logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.errors[].logisticsAgentId` | integer | 否 | 物流id |
| `data.errors[].agentName` | string | 否 | 物流名称 |


<details><summary>请求示例</summary>

```json
{
  "opOrderPackageIds": [
    2008407593,
    1999236402,
    1992973198,
    1990087996,
    1990087975,
    1990077182,
    1990059646,
    1276648263,
    1274794190,
    1274740924,
    1274689828,
    1274624282,
    1274624254,
    1274121129,
    1274044406,
    1273927611,
    1273924534,
    1271460840,
    1271458829,
    1271158800
  ]
}
```
</details>

## 包裹>基础信息修改

### 保存包裹本地备注

- 层级：开放平台 > 包裹 > 包裹 > 基础信息修改
- 方法+路径：`POST /open/v1/order/package/base_info_modify/saveOrderPackageAppNote`
- 类型：写
- 原文：[457235460e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457235460e0.md)（本地 raw/457235460e0_保存包裹本地备注.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 包裹id |
| `appNote` | string | 是 | 本地备注内容 |
| `isRsyncToForwarder` | integer | 是 | 1 是 0 否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array<string> | 是 |  |


---

### 保存包裹商家备注

- 层级：开放平台 > 包裹 > 包裹 > 基础信息修改
- 方法+路径：`POST /open/v1/order/package/base_info_modify/saveSellerNote`
- 类型：写
- 原文：[457240926e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457240926e0.md)（本地 raw/457240926e0_保存包裹商家备注.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderIds` | array<string> | 是 | 订单id |
| `sellerNote` | string | 是 | 备注内容 |
| `isCoverOriginalSellerNote` | integer | 是 | 1 是 0 否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | array<object> | 是 |  |
| `data[].sellerNoteMap` | array<string> | 是 | orderId -note 的map |
| `data[].successCount` | string | 是 |  |
| `data[].failCount` | string | 是 |  |
| `data[].failResultMap` | object | 是 | orderId -note 的map |


## 包裹>获取包裹

### 获取订单包裹详情

- 层级：开放平台 > 包裹 > 包裹 > 获取包裹
- 方法+路径：`POST /open/v1/order/package/fetch/get_package_info`
- 类型：读
- 原文：[524317132e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/524317132e0.md)（本地 raw/524317132e0_获取订单包裹详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageId` | integer | 是 | 订单包裹id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.orderPackageInfo` | object | 否 | 订单信息 |
| `data.orderPackageInfo.platform` | string | 否 | 归属平台 |
| `data.orderPackageInfo.platformName` | string | 否 | 平台名称 |
| `data.orderPackageInfo.site` | string | 否 | 站点 |
| `data.orderPackageInfo.siteName` | string | 否 | 站点名称 |
| `data.orderPackageInfo.shopId` | integer | 否 | 店铺id |
| `data.orderPackageInfo.shopNick` | string | 否 | 店铺别名 |
| `data.orderPackageInfo.shopName` | string | 否 | 店铺名称 |
| `data.orderPackageInfo.orderInfo` | object | 否 | 订单信息 |
| `data.orderPackageInfo.orderInfo.opOrderId` | integer | 否 | 订单id |
| `data.orderPackageInfo.orderInfo.shopId` | integer | 否 | 店铺id |
| `data.orderPackageInfo.orderInfo.platform` | string | 否 | 订单平台 |
| `data.orderPackageInfo.orderInfo.platformOrderSn` | string | 否 | 平台订单号 |
| `data.orderPackageInfo.orderInfo.platformOrderStatus` | string | 否 | 订单平台状态 |
| `data.orderPackageInfo.orderInfo.site` | string | 否 | 站点 |
| `data.orderPackageInfo.orderInfo.currency` | string | 否 | 货币单位 |
| `data.orderPackageInfo.orderInfo.orderAmount` | number | 否 | 订单金额 |
| `data.orderPackageInfo.orderInfo.productAmount` | number | 否 | 产品金额 |
| `data.orderPackageInfo.orderInfo.discountAmount` | number | 否 | 优惠金额 |
| `data.orderPackageInfo.orderInfo.estimatedShippingFee` | number | 否 | 预估运费费用 |
| `data.orderPackageInfo.orderInfo.actualShippingCost` | number | 否 | 实际运费 |
| `data.orderPackageInfo.orderInfo.payAmount` | number | 否 | 支付金额 |
| `data.orderPackageInfo.orderInfo.escrowAmount` | number | 否 | 预估回款金额 |
| `data.orderPackageInfo.orderInfo.commissionFee` | number | 否 | 平台佣金 |
| `data.orderPackageInfo.orderInfo.paymentMethod` | string | 否 | 支付方式 |
| `data.orderPackageInfo.orderInfo.gmtOrderStart` | string | 否 | 创建时间 |
| `data.orderPackageInfo.orderInfo.gmtOrderModified` | string | 否 | 修改时间 |
| `data.orderPackageInfo.orderInfo.gmtPay` | string | 否 | 支付时间 |
| `data.orderPackageInfo.orderInfo.gmtLastDelivery` | string | 否 | 最迟发货时间 |
| `data.orderPackageInfo.orderInfo.gmtDelivery` | string | 否 | 发货时间 |
| `data.orderPackageInfo.orderInfo.gmtRefund` | string | 否 | 取消时间 |
| `data.orderPackageInfo.orderInfo.gmtFinish` | string | 否 | 完结时间 |
| `data.orderPackageInfo.orderInfo.gmtSettlement` | string | 否 | 结算时间 |
| `data.orderPackageInfo.orderInfo.isCod` | boolean | 否 | 是否货到付款 |
| `data.orderPackageInfo.orderInfo.appOrderStatus` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageInfo.orderInfo.appNote` | string | 否 | 本地备注 |
| `data.orderPackageInfo.orderInfo.sellerNote` | string | 否 | 商家备注 |
| `data.orderPackageInfo.orderInfo.buyerMessage` | string | 否 | 卖家留言 |
| `data.orderPackageInfo.orderInfo.platformOrderDetailUrl` | string | 否 | 订单图片 url |
| `data.orderPackageInfo.orderInfo.platformWarehouseName` | string | 否 | 平台仓库名称 |
| `data.orderPackageInfo.orderInfo.appOrderStatusText` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageInfo.orderInfo.exchangeRate` | number | 否 | 费率 |
| `data.orderPackageInfo.consigneeInfo` | object | 否 | 收件人数据 |
| `data.orderPackageInfo.consigneeInfo.country` | string | 否 | 收件人国家二字码 |
| `data.orderPackageInfo.consigneeInfo.countryName` | string | 否 | 收件国家名称 |
| `data.orderPackageInfo.consigneeInfo.state` | string | 否 | 收件人 州/省 |
| `data.orderPackageInfo.consigneeInfo.city` | string | 否 | 收件人城市 |
| `data.orderPackageInfo.items` | array<object> | 否 | 商品数据 |
| `data.orderPackageInfo.items[].opOrderItemId` | string | 否 | 订单item Id |
| `data.orderPackageInfo.items[].opOrderPackageId` | string | 否 | 妙手包裹id |
| `data.orderPackageInfo.items[].opOrderPackageItemId` | integer | 否 | 订单包裹item id |
| `data.orderPackageInfo.items[].platformOrderItemIndex` | string | 否 | 平台商品唯一标识 |
| `data.orderPackageInfo.items[].platformItemId` | string | 否 | 产品id |
| `data.orderPackageInfo.items[].platformSkuId` | string | 否 | 平台skuId |
| `data.orderPackageInfo.items[].platformItemNum` | string | 否 | 平台主货号 |
| `data.orderPackageInfo.items[].platformOuterSkuId` | string | 否 | 平台对外展示skuId |
| `data.orderPackageInfo.items[].title` | string | 否 | 标题 |
| `data.orderPackageInfo.items[].skuSubName` | string | 否 | 规格 |
| `data.orderPackageInfo.items[].quantity` | integer | 否 | 数量 |
| `data.orderPackageInfo.items[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageInfo.items[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageInfo.items[].picUrl` | string | 否 | 商品图片 |
| `data.orderPackageInfo.items[].originalPicUrl` | string | 否 | 商品原图 |
| `data.orderPackageInfo.items[].isGift` | string | 否 | 是否礼品 |
| `data.orderPackageInfo.giftItems` | array<object> | 否 | 赠品数据 |
| `data.orderPackageInfo.giftItems[].opOrderPackageGiftId` | integer | 否 | 包裹赠品id |
| `data.orderPackageInfo.giftItems[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.orderPackageInfo.giftItems[].goodsId` | integer | 否 | 商品id |
| `data.orderPackageInfo.giftItems[].goodsSkuId` | integer | 否 | 商品skuId |
| `data.orderPackageInfo.giftItems[].goodsName` | string | 否 | 商品标题 |
| `data.orderPackageInfo.giftItems[].itemNum` | string | 否 | 平台主货号 |
| `data.orderPackageInfo.giftItems[].goodsSkuSubName` | string | 否 | 规格 |
| `data.orderPackageInfo.giftItems[].goodsSkuOuterId` | string | 否 | 对外展示 sku |
| `data.orderPackageInfo.giftItems[].quantity` | integer | 否 | 数量 |
| `data.orderPackageInfo.giftItems[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageInfo.giftItems[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageInfo.giftItems[].picUrl` | string | 否 | 图片 |
| `data.orderPackageInfo.logisticsAgentProductInfo` | object | 否 | 物流渠道数据/头程物流渠道数据 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageInfo.logisticsAgentProductInfo.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageInfo.logisticsAgentProductInfo.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageInfo.logisticsAgentProductInfo.status` | string | 否 | 渠道状态 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageInfo.logisticsAgentProductInfo.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageInfo.logisticsAgentProductInfo.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageInfo.logisticsAgentProductInfo.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageInfo.logisticsAgentProductInfo.shippingFee` | number | 否 | 费用 |
| `data.orderPackageInfo.logisticsAgentProductInfo.shippingFeeCurrency` | string | 否 | 费用货币 |
| `data.orderPackageInfo.logisticsAgentProductInfo.warehouseName` | string | 否 | 仓库名称 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile` | object | 否 | 尾程物流渠道数据 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.status` | string | 否 | 渠道状态 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageInfo.opOrderPackageToPlatformLastMile.combineProductName` | string | 否 | 拼接渠道 |
| `data.orderPackageInfo.appPackageNo` | string | 否 | 妙手包裹号 |
| `data.orderPackageInfo.platformPackageStatus` | string | 否 | 平台包裹状态 |
| `data.orderPackageInfo.appPackageStatus` | string | 否 | erp 包裹状态 |
| `data.orderPackageInfo.appPackageStatusText` | string | 否 | erp 包裹状态 |
| `data.orderPackageInfo.applyTrackingNoFailReason` | string | 否 | 申请失败原因 |
| `data.orderPackageInfo.applyTrackingNoFailCode` | string | 否 | 申请失败错误吗 |
| `data.orderPackageInfo.fulfillmentType` | string | 否 | 订单类型 |
| `data.orderPackageInfo.logisticsNo` | string | 否 | 跟踪号 |
| `data.orderPackageInfo.opOrderPackageId` | integer | 否 | 妙手包裹Id |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust` | object | 否 | 美客多重量尺寸和运费调整信息 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.weight` | number | 否 | 包裹重量 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.length` | number | 否 | 包裹长 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.height` | number | 否 | 包裹高 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.width` | number | 否 | 包裹宽 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.cost` | number | 否 | 商家运费 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.compensation` | number | 否 | 补扣运费 |
| `data.orderPackageInfo.mercadoWeightDimensionFreightAdjust.hasWeightDimensionDiff` | boolean | 否 | 包裹重量尺寸是否有差异 |


<details><summary>请求示例</summary>

```json
{
  "opOrderPackageId": 43717
}
```
</details>

---

### 获取订单包裹列表

- 层级：开放平台 > 包裹 > 包裹 > 获取包裹
- 方法+路径：`POST /open/v1/order/package/fetch/search_package_list`
- 类型：读
- 原文：[524317133e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/524317133e0.md)（本地 raw/524317133e0_获取订单包裹列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `platform` | string | 否 | 平台 |
| `shopIds` | array<integer> | 否 | 店铺ids |
| `appPackageStatus` | string | 否 | 包裹状态 |
| `platformOrderSns` | string | 否 | 订单号[多个逗号分割] |
| `gmtCreateFrom` | string | 否 | 妙手创建时间 -开始 |
| `gmtCreateTo` | string | 否 | 妙手创建时间 -结束 |
| `gmtModifiedFrom` | string | 否 | 妙手修改时间 -开始 |
| `gmtModifiedTo` | string | 否 | 妙手修改时间 -结束 |
| `appPackageTab` | string | 否 | 妙手包裹tab(顶层tab) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.orderPackageList` | array<object> | 否 | 订单列表信息 |
| `data.orderPackageList[].platform` | string | 否 | 归属平台 |
| `data.orderPackageList[].platformName` | string | 否 | 平台名称 |
| `data.orderPackageList[].site` | string | 否 | 站点 |
| `data.orderPackageList[].siteName` | string | 否 | 站点名称 |
| `data.orderPackageList[].shopId` | integer | 否 | 店铺id |
| `data.orderPackageList[].shopNick` | string | 否 | 店铺别名 |
| `data.orderPackageList[].shopName` | string | 否 | 店铺名称 |
| `data.orderPackageList[].orderInfo` | object | 否 | 订单信息 |
| `data.orderPackageList[].orderInfo.opOrderId` | integer | 否 | 订单id |
| `data.orderPackageList[].orderInfo.shopId` | integer | 否 | 店铺id |
| `data.orderPackageList[].orderInfo.platform` | string | 否 | 订单平台 |
| `data.orderPackageList[].orderInfo.platformOrderSn` | string | 否 | 平台订单号 |
| `data.orderPackageList[].orderInfo.platformOrderStatus` | string | 否 | 订单平台状态 |
| `data.orderPackageList[].orderInfo.site` | string | 否 | 站点 |
| `data.orderPackageList[].orderInfo.currency` | string | 否 | 货币单位 |
| `data.orderPackageList[].orderInfo.orderAmount` | number | 否 | 订单金额 |
| `data.orderPackageList[].orderInfo.productAmount` | number | 否 | 产品金额 |
| `data.orderPackageList[].orderInfo.discountAmount` | number | 否 | 优惠金额 |
| `data.orderPackageList[].orderInfo.estimatedShippingFee` | number | 否 | 预估运费费用 |
| `data.orderPackageList[].orderInfo.actualShippingCost` | number | 否 | 实际运费 |
| `data.orderPackageList[].orderInfo.payAmount` | number | 否 | 支付金额 |
| `data.orderPackageList[].orderInfo.escrowAmount` | number | 否 | 预估回款金额 |
| `data.orderPackageList[].orderInfo.commissionFee` | number | 否 | 平台佣金 |
| `data.orderPackageList[].orderInfo.paymentMethod` | string | 否 | 支付方式 |
| `data.orderPackageList[].orderInfo.gmtOrderStart` | string | 否 | 创建时间 |
| `data.orderPackageList[].orderInfo.gmtOrderModified` | string | 否 | 修改时间 |
| `data.orderPackageList[].orderInfo.gmtPay` | string | 否 | 支付时间 |
| `data.orderPackageList[].orderInfo.gmtLastDelivery` | string | 否 | 最迟发货时间 |
| `data.orderPackageList[].orderInfo.gmtDelivery` | string | 否 | 发货时间 |
| `data.orderPackageList[].orderInfo.gmtRefund` | string | 否 | 取消时间 |
| `data.orderPackageList[].orderInfo.gmtFinish` | string | 否 | 完结时间 |
| `data.orderPackageList[].orderInfo.gmtSettlement` | string | 否 | 结算时间 |
| `data.orderPackageList[].orderInfo.isCod` | boolean | 否 | 是否货到付款 |
| `data.orderPackageList[].orderInfo.appOrderStatus` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageList[].orderInfo.appNote` | string | 否 | 本地备注 |
| `data.orderPackageList[].orderInfo.sellerNote` | string | 否 | 商家备注 |
| `data.orderPackageList[].orderInfo.buyerMessage` | string | 否 | 卖家留言 |
| `data.orderPackageList[].orderInfo.platformOrderDetailUrl` | string | 否 | 订单图片 url |
| `data.orderPackageList[].orderInfo.platformWarehouseName` | string | 否 | 平台仓库名称 |
| `data.orderPackageList[].orderInfo.appOrderStatusText` | string | 否 | 妙手平台订单状态 |
| `data.orderPackageList[].orderInfo.exchangeRate` | number | 否 | 费率 |
| `data.orderPackageList[].consigneeInfo` | object | 否 | 收件人数据 |
| `data.orderPackageList[].consigneeInfo.country` | string | 否 | 收件人国家二字码 |
| `data.orderPackageList[].consigneeInfo.countryName` | string | 否 | 收件国家名称 |
| `data.orderPackageList[].consigneeInfo.state` | string | 否 | 收件人 州/省 |
| `data.orderPackageList[].consigneeInfo.city` | string | 否 | 收件人城市 |
| `data.orderPackageList[].items` | array<object> | 否 | 商品数据 |
| `data.orderPackageList[].items[].opOrderItemId` | string | 否 | 订单item Id |
| `data.orderPackageList[].items[].opOrderPackageId` | string | 否 | 妙手包裹id |
| `data.orderPackageList[].items[].opOrderPackageItemId` | integer | 否 | 订单包裹item id |
| `data.orderPackageList[].items[].platformOrderItemIndex` | string | 否 | 平台商品唯一标识 |
| `data.orderPackageList[].items[].platformItemId` | string | 否 | 产品id |
| `data.orderPackageList[].items[].platformSkuId` | string | 否 | 平台skuId |
| `data.orderPackageList[].items[].platformItemNum` | string | 否 | 平台主货号 |
| `data.orderPackageList[].items[].platformOuterSkuId` | string | 否 | 平台对外展示skuId |
| `data.orderPackageList[].items[].title` | string | 否 | 标题 |
| `data.orderPackageList[].items[].skuSubName` | string | 否 | 规格 |
| `data.orderPackageList[].items[].quantity` | integer | 否 | 数量 |
| `data.orderPackageList[].items[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageList[].items[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageList[].items[].picUrl` | string | 否 | 商品图片 |
| `data.orderPackageList[].items[].originalPicUrl` | string | 否 | 商品原图 |
| `data.orderPackageList[].items[].isGift` | string | 否 | 是否礼品 |
| `data.orderPackageList[].giftItems` | array<object> | 否 | 赠品数据 |
| `data.orderPackageList[].giftItems[].opOrderPackageGiftId` | integer | 否 | 包裹赠品id |
| `data.orderPackageList[].giftItems[].opOrderPackageId` | integer | 否 | 妙手包裹id |
| `data.orderPackageList[].giftItems[].goodsId` | integer | 否 | 商品id |
| `data.orderPackageList[].giftItems[].goodsSkuId` | integer | 否 | 商品skuId |
| `data.orderPackageList[].giftItems[].goodsName` | string | 否 | 商品标题 |
| `data.orderPackageList[].giftItems[].itemNum` | string | 否 | 平台主货号 |
| `data.orderPackageList[].giftItems[].goodsSkuSubName` | string | 否 | 规格 |
| `data.orderPackageList[].giftItems[].goodsSkuOuterId` | string | 否 | 对外展示 sku |
| `data.orderPackageList[].giftItems[].quantity` | integer | 否 | 数量 |
| `data.orderPackageList[].giftItems[].originalPrice` | number | 否 | 原始价格 |
| `data.orderPackageList[].giftItems[].discountedPrice` | number | 否 | 折扣价格 |
| `data.orderPackageList[].giftItems[].picUrl` | string | 否 | 图片 |
| `data.orderPackageList[].logisticsAgentProductInfo` | object | 否 | 物流渠道数据/头程物流渠道数据 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageList[].logisticsAgentProductInfo.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageList[].logisticsAgentProductInfo.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageList[].logisticsAgentProductInfo.status` | string | 否 | 渠道状态 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageList[].logisticsAgentProductInfo.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageList[].logisticsAgentProductInfo.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageList[].logisticsAgentProductInfo.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageList[].logisticsAgentProductInfo.shippingFee` | number | 否 | 费用 |
| `data.orderPackageList[].logisticsAgentProductInfo.shippingFeeCurrency` | string | 否 | 费用货币 |
| `data.orderPackageList[].logisticsAgentProductInfo.warehouseName` | string | 否 | 仓库名称 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile` | object | 否 | 尾程物流渠道数据 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentProductId` | integer | 否 | 物流渠道id |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentId` | integer | 否 | 物流id |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.productCode` | string | 否 | 物流渠道编码 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.productName` | string | 否 | 物流渠道名称 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.status` | string | 否 | 渠道状态 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentAuthId` | string | 否 | 物流授权id |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsAgentAuthConfigId` | integer | 否 | 物流授权配置 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.platformPackageNo` | string | 否 | 物流运单包裹号 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsNo` | string | 否 | 物流跟踪号 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.logisticsCompany` | string | 否 | 物流公司 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.extInfo` | string | 否 | 物流拓展信息 |
| `data.orderPackageList[].opOrderPackageToPlatformLastMile.combineProductName` | string | 否 | 拼接渠道 |
| `data.orderPackageList[].appPackageNo` | string | 否 | 妙手包裹号 |
| `data.orderPackageList[].platformPackageStatus` | string | 否 | 平台包裹状态 |
| `data.orderPackageList[].appPackageStatus` | string | 否 | erp 包裹状态 |
| `data.orderPackageList[].appPackageStatusText` | string | 否 | erp 包裹状态 |
| `data.orderPackageList[].applyTrackingNoFailReason` | string | 否 | 申请失败原因 |
| `data.orderPackageList[].applyTrackingNoFailCode` | string | 否 | 申请失败错误吗 |
| `data.orderPackageList[].fulfillmentType` | string | 否 | 订单类型 |
| `data.orderPackageList[].logisticsNo` | string | 否 | 跟踪号 |
| `data.orderPackageList[].opOrderPackageId` | integer | 否 | 妙手包裹Id |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust` | object | 否 | 美客多重量尺寸和运费调整信息 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.weight` | number | 否 | 包裹重量 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.length` | number | 否 | 包裹长 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.height` | number | 否 | 包裹高 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.width` | number | 否 | 包裹宽 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.cost` | number | 否 | 商家运费 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.compensation` | number | 否 | 补扣运费 |
| `data.orderPackageList[].mercadoWeightDimensionFreightAdjust.hasWeightDimensionDiff` | boolean | 否 | 包裹重量尺寸是否有差异 |
| `data.total` | integer | 否 | 总数 |
| `data.page` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页数量 |


<details><summary>请求示例</summary>

```json
{
  "page": 1,
  "pageSize": 10
}
```
</details>

## 包裹>发货

### 包裹发货

- 层级：开放平台 > 包裹 > 包裹 > 发货
- 方法+路径：`POST /open/v1/order/package/ship_package/ship_packages`
- 类型：写
- 原文：[455694578e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455694578e0.md)（本地 raw/455694578e0_包裹发货.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `opOrderPackageIds` | array<integer> | 是 | 包裹IDs |
| `isVirtualShipment` | integer | 是 | 是否虚拟发货 |
| `tiktokLocalShopShipType` | string | 是 | 枚举值（1、2）;1、pick-up；2、drop-off |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 |  |
| `code` | string | 是 |  |
| `message` | string | 是 |  |
| `data` | object | 是 |  |
| `data.successOpOrderPackageIds` | string | 是 |  |
| `data.failCount` | string | 是 |  |
| `data.shipFailErrors` | array<object> | 是 |  |
| `data.shipFailErrors[].errMsg` | string | 是 | 错误描述 |
| `data.shipFailErrors[].errCode` | string | 是 | 错误code |
| `data.shipFailErrors[].opOrderPackageId` | string | 是 | 妙手包裹id |
| `data.shipFailErrors[].opOrderId` | string | 是 | 妙手订单id |
| `data.shipFailErrors[].platformOrderSn` | string | 是 | 妙手订单编号 |
| `data.shipFailErrors[].platformPackageId` | string | 是 | 平台包裹id |
| `data.shipFailErrors[].appPackageNo` | string | 是 | 包裹号 |
| `data.shipFailErrors[].logisticsNo` | string | 是 | 跟踪号 |
| `data.shipFailErrors[].logisticsCompany` | string | 是 | 物流公司 |
| `data.shipFailErrors[].logisticsAgentAuthId` | string | 是 | 授权id |
| `data.shipFailErrors[].logisticsAgentProductId` | string | 是 | 物流渠道id |
| `data.shipFailErrors[].logisticsAgentId` | string | 是 | 物流id |
| `data.shipFailErrors[].gentName` | string | 是 | 物流名称 |
| `data.successCount` | string | 是 |  |


## 采购记录

### 采购记录列表

- 层级：开放平台 > 包裹 > 采购记录
- 方法+路径：`POST /open/v1/order/purchase_order/purchase_record/search_list`
- 类型：读
- 原文：[523326861e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523326861e0.md)（本地 raw/523326861e0_采购记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

其他参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `timerToken(query)` | string | 否 |  |
| `Cookie(header)` | string | 否 |  |
| `X-Apifox-Debug(header)` | string | 否 |  |


**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |
| `sortType` | string | 否 | 排序方式 |
| `shopIds` | array<integer> | 否 | 店铺ids |
| `purchasePlatform` | string | 否 | 采购平台 |
| `purchaseOrderStatus` | string | 否 | 采购单状态 |
| `purchaseOrderSeller` | string | 否 | 采购单卖家/供应商 |
| `warningType` | string | 否 | 预警类型 |
| `snType` | string | 否 | 搜索类型: purchaseOrderSn, purchaseOrderBuyer, platformOrderSn, appPackageNo, waybillCode, logisticsName, platformOuterSkuId, platformItemId |
| `snValue` | string | 否 | 搜索值 |
| `gmtRangeType` | string | 否 | 时间范围类型: gmtPurchaseOrderStart, gmtLastRsync, gmtPay, gmtLastUrgeShip, gmtOrderStart, gmtShip, gmtSign, signDuringTime |
| `gmtRangeFrom` | string | 否 | 时间范围起始 |
| `gmtRangeTo` | string | 否 | 时间范围结束 |
| `relateStatus` | string | 否 | 关联状态 |
| `forwarderId` | integer | 否 | 货代id |
| `buyerPhone` | string | 否 | 收件人手机号 |
| `appPackageStatus` | string | 否 | 订单包裹状态 |
| `isFilterAbnormal` | integer | 否 | 是否过滤异常 |
| `gmtPurchaseOrderStartFrom` | string | 否 | 采购下单时间起始 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.list` | array<object> | 否 |  |
| `data.list[].purchaseOrderSn` | string | 否 | 采购单号 |
| `data.list[].waybillCode` | string | 否 | 采购物流单号 |
| `data.list[].purchasePlatformName` | string | 否 | 采购平台名称 |
| `data.list[].gmtPurchaseOrderStart` | string | 否 | 采购时间 |
| `data.list[].purchaseOrderSeller` | string | 否 | 供应商名称 |
| `data.list[].purchaseOrderPayment` | string | 否 | 实付金额 |
| `data.list[].purchaseOrderShippingFee` | string | 否 | 运费金额 |
| `data.list[].purchaseOrderOtherFee` | string | 否 | 其他金额 |
| `data.list[].purchaseItems` | array<object> | 否 | 采购商品列表 |
| `data.list[].purchaseItems[].sourceTitle` | string | 否 | 采购商品名称 |
| `data.list[].purchaseItems[].sourceSkuSubName` | string | 否 | 采购商品规格名称 |
| `data.list[].purchaseItems[].sourceSendGoodsAddress` | string | 否 | 采购商品发货地 |
| `data.list[].purchaseItems[].sourceUnitPrice` | string | 否 | 采购商品单价 |
| `data.list[].purchaseItems[].sourceQuantity` | string | 否 | 采购商品规格数量 |
| `data.list[].purchaseOrderPackages` | array<object> | 否 | 采购物流包裹列表 |
| `data.list[].purchaseOrderPackages[].logisticsName` | string | 否 | 物流名称 |
| `data.list[].purchaseOrderPackages[].waybillCode` | string | 否 | 采购物流单号 |
| `data.list[].purchaseOrderPackages[].signDuringTime` | integer | 否 | 签收时长(秒) |
| `data.list[].purchaseOrderPackages[].isSubscribeLogistics` | integer | 否 | 是否订阅物流 |
| `data.list[].purchaseOrderPackages[].failCode` | string | 否 | 失败码 |
| `data.list[].purchaseOrderPackages[].failReason` | string | 否 | 失败原因 |
| `data.list[].purchaseOrderPackages[].gmtLastLogisticsTrace` | string | 否 | 最新物流轨迹时间 |
| `data.list[].purchaseOrderPackages[].gmtSign` | string | 否 | 签收时间 |
| `data.list[].purchaseOrderPackages[].gmtShip` | string | 否 | 发货时间 |
| `data.list[].opOrderPackageList` | array<object> | 否 | 关联订单包裹列表 |
| `data.list[].opOrderPackageList[].platformOrderSn` | string | 否 | 订单号 |
| `data.list[].opOrderPackageList[].shopName` | string | 否 | 店铺 |
| `data.list[].opOrderPackageList[].platform` | string | 否 | 平台 |
| `data.list[].opOrderPackageList[].relateStatus` | string | 否 | 关联状态枚举值  normal:关联  cancel：取消关联 |
| `data.list[].opOrderPackageList[].purchaseItems` | array<object> | 否 | 订单商品列表 |
| `data.list[].opOrderPackageList[].purchaseItems[].title` | string | 否 | 产品名称 |
| `data.list[].opOrderPackageList[].purchaseItems[].skuSubName` | string | 否 | 规格 |
| `data.list[].opOrderPackageList[].purchaseItems[].platformItemId` | string | 否 | 产品ID |
| `data.list[].opOrderPackageList[].purchaseItems[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.list[].opOrderPackageList[].purchaseItems[].unitPrice` | string | 否 | 单价 |
| `data.list[].opOrderPackageList[].purchaseItems[].quantity` | integer | 否 | 数量 |
| `data.list[].opOrderPackageList[].purchaseItems[].picUrl` | string | 否 | 产品图片 |
| `data.total` | integer | 否 |  |


---

### 采购记录详情

- 层级：开放平台 > 包裹 > 采购记录
- 方法+路径：`POST /open/v1/order/purchase_order/purchase_record/get_detail`
- 类型：读
- 原文：[523329034e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523329034e0.md)（本地 raw/523329034e0_采购记录详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

其他参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `timerToken(query)` | string | 否 |  |
| `Cookie(header)` | string | 否 |  |
| `X-Apifox-Debug(header)` | string | 否 |  |


**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `purchaseOrderSn` | string | 否 | 采购单号 |
| `waybillCode` | string | 否 | 采购物流单号 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detail` | object | 否 |  |
| `data.detail.purchaseOrderSn` | string | 否 | 采购单号 |
| `data.detail.waybillCode` | string | 否 | 采购物流单号 |
| `data.detail.purchasePlatformName` | string | 否 | 采购平台名称 |
| `data.detail.gmtPurchaseOrderStart` | string | 否 | 采购时间 |
| `data.detail.purchaseOrderSeller` | string | 否 | 供应商名称 |
| `data.detail.purchaseItems` | array<object> | 否 | 采购商品列表 |
| `data.detail.purchaseItems[].sourceTitle` | string | 否 | 采购商品名称 |
| `data.detail.purchaseItems[].sourceSkuSubName` | string | 否 | 采购商品规格名称 |
| `data.detail.purchaseItems[].sourceSendGoodsAddress` | string | 否 | 采购商品发货地 |
| `data.detail.purchaseItems[].sourceUnitPrice` | string | 否 | 采购商品单价 |
| `data.detail.purchaseItems[].sourceQuantity` | string | 否 | 采购商品规格数量 |
| `data.detail.purchaseOrderPackages` | array<object> | 否 | 采购物流包裹列表 |
| `data.detail.purchaseOrderPackages[].logisticsName` | string | 否 | 物流名称 |
| `data.detail.purchaseOrderPackages[].waybillCode` | string | 否 | 采购物流单号 |
| `data.detail.purchaseOrderPackages[].signDuringTime` | integer | 否 | 签收时长(秒) |
| `data.detail.purchaseOrderPackages[].isSubscribeLogistics` | integer | 否 | 是否订阅物流 |
| `data.detail.purchaseOrderPackages[].failCode` | string | 否 | 失败码 |
| `data.detail.purchaseOrderPackages[].failReason` | string | 否 | 失败原因 |
| `data.detail.purchaseOrderPackages[].gmtLastLogisticsTrace` | string | 否 | 最新物流轨迹时间 |
| `data.detail.purchaseOrderPackages[].gmtSign` | string | 否 | 签收时间 |
| `data.detail.purchaseOrderPackages[].gmtShip` | string | 否 | 发货时间 |
| `data.detail.opOrderPackageList` | array<object> | 否 | 关联订单包裹列表 |
| `data.detail.opOrderPackageList[].platformOrderSn` | string | 否 | 订单号 |
| `data.detail.opOrderPackageList[].shopName` | string | 否 | 店铺 |
| `data.detail.opOrderPackageList[].platform` | string | 否 | 平台 |
| `data.detail.opOrderPackageList[].relateStatus` | string | 否 | 关联状态 |
| `data.detail.opOrderPackageList[].purchaseItems` | array<object> | 否 | 订单商品列表 |
| `data.detail.opOrderPackageList[].purchaseItems[].title` | string | 否 | 产品名称 |
| `data.detail.opOrderPackageList[].purchaseItems[].skuSubName` | string | 否 | 规格 |
| `data.detail.opOrderPackageList[].purchaseItems[].platformItemId` | string | 否 | 产品ID |
| `data.detail.opOrderPackageList[].purchaseItems[].platformOuterSkuId` | string | 否 | 平台SKU |
| `data.detail.opOrderPackageList[].purchaseItems[].unitPrice` | string | 否 | 单价 |
| `data.detail.opOrderPackageList[].purchaseItems[].quantity` | integer | 否 | 数量 |
| `data.detail.opOrderPackageList[].purchaseItems[].picUrl` | string | 否 | 产品图片 |
| `data.detail.purchaseOrderPayment` | string | 否 | 实付金额 |
| `data.detail.purchaseOrderShippingFee` | string | 否 | 运费金额 |
| `data.detail.purchaseOrderOtherFee` | string | 否 | 其他金额 |

