# 获取三方仓授权列表


- 层级：开放平台 > 仓储 > 仓库 > 三方仓仓库
- 方法+路径：`POST /open/v1/ewm/third_warehouse/fetch/search_third_provider_auth_page`
- 类型：读
- 原文：[479592192e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592192e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `page` | integer | 是 |  |
| `pageSize` | integer | 是 |  |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.providerAuthList` | object | 否 | 第三方授权列表 |
| `data.providerAuthList.thirdWarehouseProviderAuthId` | string | 否 | 授权ID |
| `data.providerAuthList.providerId` | string | 否 | 服务商ID |
| `data.providerAuthList.type` | string | 否 | 三方仓类型 forwarder:货代；logisticsAgent 三方服务商 |
| `data.providerAuthList.appCustomerId` | string | 否 | 授权id |
| `data.providerAuthList.nickname` | string | 否 | 昵称 |
| `data.providerAuthList.status` | string | 否 | 状态 |
| `data.providerAuthList.isPlatformWarehouse` | string | 否 | 是否平台仓库 |
| `data.providerAuthList.providerName` | string | 否 | 服务商名称 |
| `data.providerAuthList.providerCode` | string | 否 | 服务商Code |
| `data.providerAuthList.authAgentWarehouseList` | array&lt;object> | 否 | 授权三方服务商仓库列表 |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentWarehouseAuthId` | string | 否 | 仓库授权id |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentCustomerId` | string | 否 | 服务商授权Id |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentWarehouseId` | string | 否 | 仓库id |
| `data.providerAuthList.authAgentWarehouseList[].isDisabled` | string | 否 | 是否禁用 1禁用 |
| `data.providerAuthList.authAgentWarehouseList[].nickname` | string | 否 | 昵称 |
| `data.providerAuthList.authAgentWarehouseList[].logisticsAgentId` | string | 否 | 服务商id |
| `data.providerAuthList.authAgentWarehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.providerAuthList.authAgentWarehouseList[].platformWarehouseCode` | string | 否 | 平台仓库编码 |
| `data.providerAuthList.authAgentWarehouseList[].address` | string | 否 | 地址 |
| `data.providerAuthList.authAgentWarehouseList[].contactPhone` | string | 否 | 联系电话 |
| `data.providerAuthList.authAgentWarehouseList[].contactName` | string | 否 | 联系人名称 |
| `data.providerAuthList.authForwarderWarehouseList` | array&lt;object> | 否 | 授权货代仓库列表 |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderWarehouseAuthId` | string | 否 | 货代服务商仓库授权id |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderCustomerId` | string | 否 | 货代服务商授权id |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderWarehouseId` | string | 否 | 货代服务商仓库id |
| `data.providerAuthList.authForwarderWarehouseList[].isDisabled` | string | 否 | 是否禁用 |
| `data.providerAuthList.authForwarderWarehouseList[].nickname` | string | 否 | 昵称 |
| `data.providerAuthList.authForwarderWarehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.providerAuthList.authForwarderWarehouseList[].forwarderProviderId` | string | 否 | 货代服务商id |
| `data.providerAuthList.authForwarderWarehouseList[].address` | string | 否 | 地址 |
| `data.providerAuthList.authForwarderWarehouseList[].contactPhone` | string | 否 | 联系电话 |
| `data.providerAuthList.authForwarderWarehouseList[].contactName` | string | 否 | 联系人 |
| `data.total` | integer | 否 | 总数 |
