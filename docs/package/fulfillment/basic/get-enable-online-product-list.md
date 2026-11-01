# 获取当前包裹有效的线上物流列表


- 层级：开放平台 > 包裹 > 履约 > 基础管理
- 方法+路径：`POST /open/v1/order/logistics_agent/manage/get_enable_online_product_list`
- 类型：读
- 原文：[455611090e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455611090e0.md)
- 说明：在线发货以及拼接物流

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

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
| `data` | array&lt;object> | 是 |  |
| `data[].logisticsAgentAuthConfigOption` | object | 是 |  |
| `data[].logisticsAgentAuthConfigOption.label` | string | 否 | 渠道标签 |
| `data[].logisticsAgentAuthConfigOption.agentCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.agentName` | string | 否 | 物流商名称 |
| `data[].logisticsAgentAuthConfigOption.options` | array&lt;object> | 否 | 物流渠道数据 |
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
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap` | array&lt;object> | 否 | 拼接渠道数据 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].label` | string | 否 | 渠道标签 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].agentCode` | string | 否 | 物流渠道编码 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].agentName` | string | 否 | 物流商名称 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options` | array&lt;object> | 否 | 开启的渠道数据 |
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
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].lastMilePlatforms` | array&lt;string> | 否 | 尾程支持平台 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].estimatedInfo` | object | 否 | 渠道测算信息 |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].options[].lastMileLogisticsAgentAuthConfigId` | string | 否 | 尾程授权配置id |
| `data[].logisticsAgentAuthConfigOption.logisticsAgentAuthIdAndLastMileOptionInfoMap[].type` | string | 否 | logisticsAgent/物流商物流渠道，thirdWarehouse/三方仓物流渠道， supplier/供应商渠道 selfWarehouse/自营仓渠道 |


&lt;details>&lt;summary>响应示例 200&lt;/summary>

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
&lt;/details>
