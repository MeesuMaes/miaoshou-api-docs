# 创建公共采集箱产品


- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/add_common_collect_box_detail`
- 类型：写
- 原文：[446814585e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814585e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | 是 | 产品标题 |
| `itemNum` | string | 否 | 产品主编号 |
| `notesText` | string | 否 | 简易描述 |
| `notes` | string | 否 | 详细描述（富文本格式） |
| `sourceAttrs` | array&lt;object> | 否 | 属性列表 |
| `sourceAttrs[].name` | string | 否 | 属性名 |
| `sourceAttrs[].value` | string | 否 | 属性值 |
| `price` | number | 否 | SPU货源价格，币种CNY，单规格的时候必填 |
| `stock` | integer | 否 | 总库存 |
| `imgUrls` | array&lt;string> | 否 | 图片URL列表 |
| `weight` | number | 否 | 重量(kg) |
| `packageLength` | number | 否 | 包装长度(cm) |
| `packageWidth` | number | 否 | 包装宽度(cm) |
| `packageHeight` | number | 否 | 包装高度(cm) |
| `colorPropName` | string | 否 | 颜色属性名 |
| `colorMap` | object | 否 | 颜色Map（key=颜色值，value=颜色条目） |
| `sizePropName` | string | 否 | 尺码属性名 |
| `sizeMap` | object | 否 | 尺码Map（key=尺码值，value=尺码条目） |
| `saleProp3Name` | string | 否 | 第三销售属性名 |
| `saleProp3Map` | object | 否 | 第三销售属性Map（key=属性ID，value=属性条目） |
| `skuMap` | object | 否 | SKU Map，key为SKU规格组合串，格式为「;颜色值;尺码值;」（分号分隔，首尾带分号），value为SKU数据 |
| `sizeChart` | string | 否 | 尺码表URL |
| `mainImgVideoUrl` | string | 否 | 主图视频URL |
| `mainImgAppVideoId` | string | 否 | 主图APP视频ID |
| `productCertifications` | array&lt;object> | 否 | 产品认证列表 |
| `productCertifications[].fileName` | string | 否 | 文件名称 |
| `productCertifications[].fileUrl` | string | 否 | 文件URL |
| `guideInfo` | object | 否 | 说明书信息 |
| `guideInfo.productGuideFileName` | string | 否 | 文件名称 |
| `guideInfo.productGuideFileUrl` | string | 否 | 文件URL |
| `sourceList` | array&lt;object> | 否 | 货源信息列表 |
| `sourceList[].remark` | string | 否 | 备注 |
| `sourceList[].sourceItemId` | string | 否 | 来源商品ID |
| `sourceList[].source` | string | 否 | 来源平台 |
| `sourceList[].sourceSite` | string | 否 | 来源站点 |
| `sourceList[].sourceItemUrl` | string | 否 | 来源商品链接 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.commonCollectBoxDetailId` | integer | 否 | 公共采集箱ID |
