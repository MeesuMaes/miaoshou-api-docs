# 获取公共采集箱详情


- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_detail`
- 类型：读
- 原文：[446814583e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814583e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailId` | integer | 是 | 公共采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editCommonCollectBoxDetail` | object | 否 | 公共采集箱详情 |
| `data.editCommonCollectBoxDetail.commonCollectBoxDetailId` | integer | 否 | 公共采集箱ID |
| `data.editCommonCollectBoxDetail.title` | string | 否 | 产品标题 |
| `data.editCommonCollectBoxDetail.itemNum` | string | 否 | 产品主编号 |
| `data.editCommonCollectBoxDetail.notesText` | string | 否 | 简易描述 |
| `data.editCommonCollectBoxDetail.notes` | string | 否 | 详细描述 |
| `data.editCommonCollectBoxDetail.cateList` | array&lt;string> | 否 | 类目列表 |
| `data.editCommonCollectBoxDetail.sourceAttrs` | array&lt;object> | 否 | 属性列表 |
| `data.editCommonCollectBoxDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `data.editCommonCollectBoxDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `data.editCommonCollectBoxDetail.price` | number | 否 | SPU货源价格 |
| `data.editCommonCollectBoxDetail.stock` | integer | 否 | 总库存 |
| `data.editCommonCollectBoxDetail.imgUrls` | array&lt;string> | 否 | 图片URL列表 |
| `data.editCommonCollectBoxDetail.colorMap` | object | 否 | 颜色Map（key=颜色值，value=颜色条目） |
| `data.editCommonCollectBoxDetail.sizeMap` | object | 否 | 尺码Map（key=尺码值，value=尺码条目） |
| `data.editCommonCollectBoxDetail.skuMap` | object | 否 | SKU Map（key=SKU规格组合串，value=SKU条目） |
| `data.editCommonCollectBoxDetail.weight` | number | 否 | 重量(kg) |
| `data.editCommonCollectBoxDetail.packageLength` | number | 否 | 包装长度(cm) |
| `data.editCommonCollectBoxDetail.packageWidth` | number | 否 | 包装宽度(cm) |
| `data.editCommonCollectBoxDetail.packageHeight` | number | 否 | 包装高度(cm) |
| `data.editCommonCollectBoxDetail.colorPropName` | string | 否 | 颜色属性名（对应 sourceAttrs 中的 name） |
| `data.editCommonCollectBoxDetail.sizePropName` | string | 否 | 尺码属性名（对应 sourceAttrs 中的 name） |
| `data.editCommonCollectBoxDetail.saleProp3Name` | string | 否 | 第三销售属性名 |
| `data.editCommonCollectBoxDetail.saleProp3Map` | object | 否 | 第三销售属性Map（key=属性ID，value=属性条目） |
| `data.editCommonCollectBoxDetail.sizeChart` | string | 否 | 尺码表URL |
| `data.editCommonCollectBoxDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.editCommonCollectBoxDetail.mainImgAppVideoId` | string | 否 | 主图APP视频ID |
| `data.editCommonCollectBoxDetail.productCertifications` | array&lt;object> | 否 | 产品认证列表 |
| `data.editCommonCollectBoxDetail.productCertifications[].fileName` | string | 否 | 文件名称 |
| `data.editCommonCollectBoxDetail.productCertifications[].fileUrl` | string | 否 | 文件URL |
| `data.editCommonCollectBoxDetail.guideInfo` | object | 否 | 说明书信息 |
| `data.editCommonCollectBoxDetail.guideInfo.productGuideFileName` | string | 否 | 文件名称 |
| `data.editCommonCollectBoxDetail.guideInfo.productGuideFileUrl` | string | 否 | 文件URL |
| `data.editCommonCollectBoxDetail.sourceMataInfo` | object | 否 | 货源元信息 |
| `data.editCommonCollectBoxDetail.sourceList` | array&lt;object> | 否 | 货源信息列表 |
| `data.editCommonCollectBoxDetail.sourceList[].remark` | string | 否 | 备注 |
| `data.editCommonCollectBoxDetail.sourceList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.editCommonCollectBoxDetail.sourceList[].source` | string | 否 | 来源平台 |
| `data.editCommonCollectBoxDetail.sourceList[].sourceSite` | string | 否 | 来源站点 |
| `data.editCommonCollectBoxDetail.sourceList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.editCommonCollectBoxDetail.sourceSupplierInfo` | object | 否 | 货源供应商信息 |
| `data.ossMd5` | string | 否 | 公共采集箱详情OssMd5标识 |
