# AI智能消除


- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/common/image_removal/remove_image`
- 类型：处理(生成内容)
- 原文：[482190901e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190901e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array&lt;string> | 是 | 待消除图片URL列表 |
| `traceInfo` | object | 是 | 调用场景信息 |
| `traceInfo.imageRemovalSource` | string | 是 | 图片消除业务来源 必传，可选值： collect_box-平台采集箱 collect_box_add-采集箱创建产品 common_collect_box-公共采集箱 common_collect_box_add-公共采集箱创建产品 item-在线产品 item_add-添加产品 |
| `traceInfo.collectBoxDetailId` | integer | 否 | 平台采集箱DetailId，imageRemovalSource=collect_box 时必传 |
| `traceInfo.commonCollectBoxDetailId` | integer | 否 | 公共采集箱DetailId，imageRemovalSource=common_collect_box 时必传 |
| `traceInfo.platform` | string | 否 | 平台（平台采集箱和在线产品必传） |
| `removeConfig` | object | 是 | 消除配置 |
| `removeConfig.isRemoveWatermark` | integer | 是 | 消除对象，是否去除水印（0=否，1=是） |
| `removeConfig.isRemoveLogo` | integer | 是 | 消除对象，是否去除logo（0=否，1=是） |
| `removeConfig.isRemoveText` | integer | 是 | 消除对象，是否去除文字（0=否，1=是） |
| `removeConfig.isRemovePsoriasis` | integer | 否 | 消除对象，是否去除牛皮藓（0=否，1=是） |
| `removeConfig.removeAreas` | array&lt;string> | 是 | 消除区域，可选值：background（背景区域）、subject（主体区域） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.imageRemovalUrlResultList` | array&lt;object> | 否 | 消除结果列表 |
| `data.imageRemovalUrlResultList[].result` | string | 否 | 单张消除结果（success/fail） |
| `data.imageRemovalUrlResultList[].reason` | string | 否 | 单张消除失败原因 |
| `data.imageRemovalUrlResultList[].oriImageUrl` | string | 否 | 原始图片URL |
| `data.imageRemovalUrlResultList[].newImageUrl` | string | 否 | 消除后图片URL |
| `data.imageRemovalUseNum` | integer | 否 | 图片消除使用次数 |
| `data.appResourceCode` | string | 否 | 应用资源编码 |
| `data.appResourceUseNum` | integer | 否 | 应用资源使用次数 |
| `data.freeUseNum` | integer | 否 | 免费使用次数 |
