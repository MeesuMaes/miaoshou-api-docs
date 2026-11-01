# 获取当前账号有效的线下物流列表


- 层级：开放平台 > 包裹 > 履约 > 基础管理
- 方法+路径：`POST /open/v1/order/logistics_agent/manage/get_enable_offline_product_list`
- 类型：读
- 原文：[455528071e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455528071e0.md)
- 说明：三方物流商以及三方仓

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `logisticsAgentId` | integer | 否 | 物流id |
| `opOrderPackageIds` | array&lt;integer> | 否 | 包裹ids |


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
| `data.logisticsAgentAuthConfigOption..options` | array&lt;object> | 是 | 渠道信息 |
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


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
    "logisticsAgentId": 573,
    "opOrderPackageIds": [
        043701
    ]
}
```
&lt;/details>

&lt;details>&lt;summary>响应示例 200&lt;/summary>

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
&lt;/details>
