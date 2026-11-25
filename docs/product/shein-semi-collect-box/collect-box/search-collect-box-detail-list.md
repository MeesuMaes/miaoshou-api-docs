# 获取采集箱列表


- 层级：开放平台 > 商品 > SHEIN半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shein_choice/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[537697859e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537697859e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 页码，不传默认1 |
| `pageSize` | integer | 否 | 每页条数，不传默认20 |
| `filter` | object | 否 | 查询筛选条件 |
| `filter.claimPublishShopStatus` | string | 否 | 认领发布店铺状态(空字符串-全部、published-已发布、notPublished-未发布) |
| `filter.titleType` | string | 否 | 标题搜索类型(multi-多标题、single-单标题) |
| `filter.remarkType` | string | 否 | 备注搜索类型(multi-多备注、single-单备注) |
| `filter.status` | string | 否 | 状态(空字符串-全部、notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID关键字 |
| `filter.titleKeyword` | string | 否 | 标题关键字 |
| `filter.source` | string | 否 | 采集来源(authShop-授权店铺、manual-手工创建等) |
| `filter.authShopId` | integer | 否 | 授权店铺ID |
| `filter.claimPublishShopIds` | array&lt;integer> | 否 | 认领发布店铺ID列表 |
| `filter.minPrice` | string | 否 | 最低价格 |
| `filter.maxPrice` | string | 否 | 最高价格 |
| `filter.isMark` | string | 否 | 是否标记(空字符串-全部、marked-已标记、notMarked-未标记) |
| `filter.remarkKeyword` | string | 否 | 备注关键字 |
| `filter.ownerAccountIds` | array&lt;string> | 否 | 归属账号ID列表 |
| `filter.groupIds` | array&lt;integer> | 否 | 采集箱分组ID列表 |
| `filter.createStartTime` | string | 否 | 创建开始时间 示例: 2026-11-09 00:00:00 |
| `filter.createEndTime` | string | 否 | 创建结束时间 示例: 2026-11-09 23:59:59 |
| `filter.itemNumKeyword` | string | 否 | 主货号关键字 |
| `filter.cid` | integer | 否 | 类目ID |
| `filter.infringementDetectResult` | string | 否 | 侵权检测结果(toCheck-建议侵权排查、noInfringement-暂未发现侵权、handled-侵权项已处理、detecting-侵权项检测中) |
| `filter.filterCidSite` | string | 否 | 类目筛选站点 示例: SHEIN、SHEINOBM |
| `filter.taskTypeAndStatusListMap` | array&lt;object> | 否 | 任务类型与状态列表映射 示例: \{"imageTranslate":["wait","processing"],"videoGenerate":["finish"]\} |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array&lt;object> | 否 | 采集箱数据列表 |
| `data.detailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.detailList[].commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | string | 否 | 应用账户ID |
| `data.detailList[].subAppAccountId` | string | 否 | 子应用账户ID |
| `data.detailList[].platform` | string | 否 | 平台 |
| `data.detailList[].itemNum` | string | 否 | 商品编号 |
| `data.detailList[].source` | string | 否 | 采集来源 |
| `data.detailList[].sourceSite` | string | 否 | 来源站点 |
| `data.detailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.detailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.detailList[].authShopId` | string | 否 | 授权店铺ID |
| `data.detailList[].title` | string | 否 | 标题 |
| `data.detailList[].thumbnail` | string | 否 | 缩略图 |
| `data.detailList[].price` | string | 否 | 价格 |
| `data.detailList[].minSkuPrice` | string | 否 | 最低SKU价格 |
| `data.detailList[].maxSkuPrice` | string | 否 | 最高SKU价格 |
| `data.detailList[].stock` | string | 否 | 库存 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].isCollect` | string | 否 | 是否已采集 |
| `data.detailList[].isEditTag` | string | 否 | 是否编辑标记 |
| `data.detailList[].isMark` | string | 否 | 是否标记 |
| `data.detailList[].copyType` | string | 否 | 复制类型 |
| `data.detailList[].sourceShopName` | string | 否 | 来源店铺名称 |
| `data.detailList[].shopIds` | array&lt;object> | 否 | 店铺ID列表 |
| `data.detailList[].siteAndCidMap` | array&lt;object> | 否 | 站点类目映射 |
| `data.detailList[].status` | string | 否 | 状态 |
| `data.detailList[].reason` | string | 否 | 原因 |
| `data.detailList[].hostname` | string | 否 | 主机名 |
| `data.detailList[].dataPath` | string | 否 | 数据路径 |
| `data.detailList[].dataPathIsUse` | string | 否 | 数据路径是否使用 |
| `data.detailList[].collectBoxDetailTaskId` | string | 否 | 采集箱详情任务ID |
| `data.detailList[].collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].gmtModified` | string | 否 | 更新时间 |
| `data.detailList[].maxWeight` | string | 否 | 最大重量 |
| `data.detailList[].minWeight` | string | 否 | 最小重量 |
| `data.detailList[].maxSkuWeight` | string | 否 | 最大SKU重量 |
| `data.detailList[].minSkuWeight` | string | 否 | 最小SKU重量 |
| `data.detailList[].importTemplateType` | string | 否 | 导入模板类型 |
| `data.detailList[].sourceCurrency` | string | 否 | 货源币种 |
| `data.detailList[].sourceCurrencyMinSkuPrice` | string | 否 | 货源币种最低SKU价格 |
| `data.detailList[].sourceCurrencyMaxSkuPrice` | string | 否 | 货源币种最高SKU价格 |
| `data.detailList[].sitePriceMap` | array&lt;object> | 否 | 站点价格映射 |
| `data.detailList[].siteMinSkuPriceMap` | array&lt;object> | 否 | 站点最低SKU价格映射 |
| `data.detailList[].siteMaxSkuPriceMap` | array&lt;object> | 否 | 站点最高SKU价格映射 |
| `data.detailList[].siteAndCatMap` | array&lt;object> | 否 | 站点类目信息映射 |
| `data.detailList[].pubShopList` | array&lt;object> | 否 | 发布店铺列表 |
| `data.detailList[].hasProcessingPublishTask` | boolean | 否 | 是否存在进行中的发布任务 |
| `data.detailList[].timingShopList` | array&lt;object> | 否 | 定时发布店铺列表 |
| `data.detailList[].hasTimingPublishTask` | boolean | 否 | 是否存在定时发布任务 |
| `data.detailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.detailList[].sourceList` | array&lt;object> | 否 | 来源列表 |
| `data.detailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号别名 |
| `data.detailList[].collectBoxGroupName` | string | 否 | 采集箱分组名称 |
| `data.detailList[].oriSource` | string | 否 | 原始来源 |
| `data.detailList[].taskProcessStatusList` | array&lt;object> | 否 | 任务处理状态列表 |
| `data.detailList[].infringementDetectResult` | string | 否 | 侵权检测结果 |
| `data.detailList[].listThumbnail` | string | 否 | 列表缩略图 |
| `data.detailList[].collectBoxDetailShopList` | array&lt;object> | 否 | 店铺列表 |
| `data.detailList[].collectBoxDetailSite` | array&lt;object> | 否 | 站点信息 |
| `data.detailList[].isHasProcessingAiOptimizeTask` | integer | 否 | 是否存在进行中的AI优化任务 |
| `data.total` | integer | 否 | 总数 |
| `data.pageNo` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页条数 |
