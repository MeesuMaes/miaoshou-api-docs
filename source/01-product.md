# 妙手开放平台 · 商品模块

> 由 apifox 分享文档整理（138 个接口）。字段说明原样摘自 OpenAPI 定义，未做改写；请求/响应以原文为准。

## 目录

- 店铺（1）
- 公共采集箱（7）
- TK采集箱>采集箱（16）
- TK采集箱>产品发布（2）
- TK采集箱>定价模板（2）
- TEMU全托采集箱>产品发布（2）
- TEMU全托采集箱>车型库（5）
- TEMU全托采集箱>采集箱（17）
- TEMU半托采集箱>商品发布（2）
- TEMU半托采集箱>车型库（5）
- TEMU半托采集箱>采集箱（20）
- OZON采集箱>采集箱（8）
- OZON采集箱>产品发布（2）
- Shopee采集箱>采集箱（11）
- Shopee采集箱>商品发布（3）
- 在线产品管理>Shopee全球在线产品管理（8）
- Mercadolibre采集箱>发布产品（2）
- Mercadolibre采集箱>采集箱（14）
- AI公共服务>图片处理（6）
- AI公共服务>AI润色（4）
- 图片空间（1）

## 店铺

### 获取店铺数据列表

- 层级：开放平台 > 商品 > 店铺
- 方法+路径：`POST /open/v1/product/shop/shop/get_shop_list`
- 类型：读
- 原文：[446814596e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814596e0.md)（本地 raw/446814596e0_获取店铺数据列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platform` | string | 是 | 平台（TK普通店铺 = tiktok，TK全球店铺 = tiktokGlobal，TEMU全托=pddkj，TEMU半托=pddkjChoice，虾皮=shopee，虾皮全球=shopeeGlobal，美客多=mercadolibre，Ozon = ozon） |
| `site` | string | 是 | TK站点：站点（印尼 = ID, 越南 = VN, 泰国 = TH, 马来 = MY, 菲律宾 = PH, 巴西 = BR, 墨西哥 = MX, 西班牙 = ES, 法国 = FR, 英国 = GB, 全球 = TIKTOKGLOBAL, 全球 - 美国 = TIKTOKGLOBALUS, 欧盟 = TIKTOKGLOBALEU, 美国 = US, 德国 = DE, 意大利 = IT, 日本 = JP） TEMU全托：站点 PDDKJ TEMU半托：站点 PDDKJCHOICE 虾皮站点：站点（印尼 = ID, 台湾 = TW, 越南 = VN, 泰国 = TH, 马来西亚 = MY, 新加坡 = SG, 菲律宾 = PH, 巴西 = BR, 墨西哥 = MX, 智利 = CL, 哥伦比亚 = CO, 波兰 = PL, 西班牙 = ES, 法国 = FR, 阿根廷 = AR） 虾皮全球站点：站点（全球 = SHOPEEGLOBAL）美客多站点:传统模式=CBT,新UP发品模式=UP Ozon站点：站点 OZON |
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopList` | array<object> | 否 | 店铺列表 |
| `data.shopList[].shopId` | integer | 否 | 店铺ID |
| `data.shopList[].site` | string | 否 | 站点 |
| `data.shopList[].siteName` | string | 否 | 站点名称 |
| `data.shopList[].platformShopName` | string | 否 | 平台店铺名称 |
| `data.shopList[].shopNick` | string | 否 | 店铺别名 |
| `data.shopList[].platform` | string | 否 | 平台 |
| `data.shopList[].parentShopId` | integer | 否 | 全球主店铺ID |
| `data.shopList[].isCb` | integer | 否 | 是否是跨境店铺 |
| `data.shopList[].isCnsc` | integer | 否 | 是否是全球店铺 |
| `data.shopList[].status` | string | 否 | 店铺状态 |
| `data.shopList[].gmtExpire` | string | 否 | 过期时间 |
| `data.shopList[].gmtLastAuth` | string | 否 | 最后授权时间 |


<details><summary>请求示例</summary>

```json
{
  "platform": "shopee",
  "site": "PH",
  "pageNo": 1,
  "pageSize": 100
}
```
</details>

## 公共采集箱

### 通过货源链接采集货源

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/fetch_item`
- 类型：写
- 原文：[446814581e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814581e0.md)（本地 raw/446814581e0_通过货源链接采集货源.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectLinks` | array<string> | 是 | 链接列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sourceItemIdAndDetailIdMap` | object | 否 | 货源ID和公共采集箱ID的映射 |


---

### 创建公共采集箱产品

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/add_common_collect_box_detail`
- 类型：写
- 原文：[446814585e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814585e0.md)（本地 raw/446814585e0_创建公共采集箱产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | 是 | 产品标题 |
| `itemNum` | string | 否 | 产品主编号 |
| `notesText` | string | 否 | 简易描述 |
| `notes` | string | 否 | 详细描述（富文本格式） |
| `sourceAttrs` | array<object> | 否 | 属性列表 |
| `sourceAttrs[].name` | string | 否 | 属性名 |
| `sourceAttrs[].value` | string | 否 | 属性值 |
| `price` | number | 否 | SPU货源价格，币种CNY，单规格的时候必填 |
| `stock` | integer | 否 | 总库存 |
| `imgUrls` | array<string> | 否 | 图片URL列表 |
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
| `productCertifications` | array<object> | 否 | 产品认证列表 |
| `productCertifications[].fileName` | string | 否 | 文件名称 |
| `productCertifications[].fileUrl` | string | 否 | 文件URL |
| `guideInfo` | object | 否 | 说明书信息 |
| `guideInfo.productGuideFileName` | string | 否 | 文件名称 |
| `guideInfo.productGuideFileUrl` | string | 否 | 文件URL |
| `sourceList` | array<object> | 否 | 货源信息列表 |
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


---

### 获取公共采集箱列表

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_list`
- 类型：读
- 原文：[446814582e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814582e0.md)（本地 raw/446814582e0_获取公共采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.tabPaneName` | string | 否 | 状态(all-全部、noClaimed-未认领、claimed-已认领、collectFail-采集失败、collectSuccess-采集成功) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array<object> | 否 | 列表页数据列表 |
| `data.detailList[].commonCollectBoxDetailId` | integer | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | integer | 否 | 主账号ID |
| `data.detailList[].subAppAccountId` | integer | 否 | 子账号ID |
| `data.detailList[].itemNum` | string | 否 | 货号 |
| `data.detailList[].title` | string | 否 | 标题 |
| `data.detailList[].thumbnail` | string | 否 | 主图缩略图 |
| `data.detailList[].price` | number | 否 | 价格 |
| `data.detailList[].minSkuPrice` | number | 否 | 最低SKU价格 |
| `data.detailList[].maxSkuPrice` | number | 否 | 最高SKU价格 |
| `data.detailList[].stock` | integer | 否 | 库存 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].status` | string | 否 | 状态 |
| `data.detailList[].reason` | string | 否 | 失败原因 |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].gmtModified` | string | 否 | 修改时间 |
| `data.detailList[].weight` | number | 否 | 重量 |
| `data.detailList[].maxSkuWeight` | number | 否 | 最高SKU重量 |
| `data.detailList[].minSkuWeight` | number | 否 | 最低SKU重量 |
| `data.detailList[].commonCollectBoxGroupId` | integer | 否 | 采集箱分组ID |
| `data.detailList[].commonCollectBoxGroupName` | string | 否 | 采集箱分组名称 |
| `data.detailList[].sourceList` | array<object> | 否 | 来源信息列表 |
| `data.detailList[].sourceList[].remark` | string | 否 | 备注 |
| `data.detailList[].sourceList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.detailList[].sourceList[].source` | string | 否 | 来源平台 |
| `data.detailList[].sourceList[].sourceSite` | string | 否 | 来源站点 |
| `data.detailList[].sourceList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.detailList[].ownerSubAccountAliasName` | string | 否 | 子账号别名 |
| `data.detailList[].listThumbnail` | string | 否 | 列表缩略图 |
| `data.detailList[].isMark` | string | 否 | 是否标记 |
| `data.total` | integer | 否 | 总数 |
| `data.isCommonCollectHuger` | boolean | 否 | 是否数量巨大 |


<details><summary>请求示例</summary>

```json
{
  "pageNo": 1,
  "pageSize": 10
}
```
</details>

---

### 编辑公共采集箱产品

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/edit_common_collect_box_detail`
- 类型：写
- 原文：[446814586e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814586e0.md)（本地 raw/446814586e0_编辑公共采集箱产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailId` | integer | 是 | 公共采集箱ID |
| `editCommonCollectBoxDetail` | object | 是 | 公共采集箱详情数据 |
| `editCommonCollectBoxDetail.title` | string | 是 | 产品标题 |
| `editCommonCollectBoxDetail.itemNum` | string | 否 | 产品主编号 |
| `editCommonCollectBoxDetail.notesText` | string | 否 | 简易描述 |
| `editCommonCollectBoxDetail.notes` | string | 否 | 详细描述（富文本格式） |
| `editCommonCollectBoxDetail.sourceAttrs` | array<object> | 否 | 属性列表 |
| `editCommonCollectBoxDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `editCommonCollectBoxDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `editCommonCollectBoxDetail.price` | number | 否 | SPU货源价格，币种CNY，单规格的时候必填 |
| `editCommonCollectBoxDetail.stock` | integer | 否 | 总库存 |
| `editCommonCollectBoxDetail.imgUrls` | array<string> | 否 | 图片URL列表 |
| `editCommonCollectBoxDetail.weight` | number | 否 | 重量(kg) |
| `editCommonCollectBoxDetail.packageLength` | number | 否 | 包装长度(cm) |
| `editCommonCollectBoxDetail.packageWidth` | number | 否 | 包装宽度(cm) |
| `editCommonCollectBoxDetail.packageHeight` | number | 否 | 包装高度(cm) |
| `editCommonCollectBoxDetail.colorPropName` | string | 否 | 颜色属性名 |
| `editCommonCollectBoxDetail.colorMap` | object | 否 | 颜色Map（key=颜色值，value=颜色条目） |
| `editCommonCollectBoxDetail.sizePropName` | string | 否 | 尺码属性名 |
| `editCommonCollectBoxDetail.sizeMap` | object | 否 | 尺码Map（key=尺码值，value=尺码条目） |
| `editCommonCollectBoxDetail.saleProp3Name` | string | 否 | 第三销售属性名 |
| `editCommonCollectBoxDetail.saleProp3Map` | object | 否 | 第三销售属性Map（key=属性ID，value=属性条目） |
| `editCommonCollectBoxDetail.skuMap` | object | 否 | SKU Map，key为SKU规格组合串，格式为「;颜色值;尺码值;」（分号分隔，首尾带分号），value为SKU数据 |
| `editCommonCollectBoxDetail.sizeChart` | string | 否 | 尺码表URL |
| `editCommonCollectBoxDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `editCommonCollectBoxDetail.mainImgAppVideoId` | string | 否 | 主图APP视频ID |
| `editCommonCollectBoxDetail.productCertifications` | array<object> | 否 | 产品认证列表 |
| `editCommonCollectBoxDetail.productCertifications[].fileName` | string | 否 | 文件名称 |
| `editCommonCollectBoxDetail.productCertifications[].fileUrl` | string | 否 | 文件URL |
| `editCommonCollectBoxDetail.guideInfo` | object | 否 | 说明书信息 |
| `editCommonCollectBoxDetail.guideInfo.productGuideFileName` | string | 否 | 文件名称 |
| `editCommonCollectBoxDetail.guideInfo.productGuideFileUrl` | string | 否 | 文件URL |
| `editCommonCollectBoxDetail.sourceList` | array<object> | 否 | 货源信息列表 |
| `editCommonCollectBoxDetail.sourceList[].remark` | string | 否 | 备注 |
| `editCommonCollectBoxDetail.sourceList[].sourceItemId` | string | 否 | 来源商品ID |
| `editCommonCollectBoxDetail.sourceList[].source` | string | 否 | 来源平台 |
| `editCommonCollectBoxDetail.sourceList[].sourceSite` | string | 否 | 来源站点 |
| `editCommonCollectBoxDetail.sourceList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `ossMd5` | string | 是 | 公共采集箱详情OssMd5标识 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 是 | 公共采集箱详情OssMd5标识 |


---

### 获取公共采集箱详情

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_detail`
- 类型：读
- 原文：[446814583e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814583e0.md)（本地 raw/446814583e0_获取公共采集箱详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `data.editCommonCollectBoxDetail.cateList` | array<string> | 否 | 类目列表 |
| `data.editCommonCollectBoxDetail.sourceAttrs` | array<object> | 否 | 属性列表 |
| `data.editCommonCollectBoxDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `data.editCommonCollectBoxDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `data.editCommonCollectBoxDetail.price` | number | 否 | SPU货源价格 |
| `data.editCommonCollectBoxDetail.stock` | integer | 否 | 总库存 |
| `data.editCommonCollectBoxDetail.imgUrls` | array<string> | 否 | 图片URL列表 |
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
| `data.editCommonCollectBoxDetail.productCertifications` | array<object> | 否 | 产品认证列表 |
| `data.editCommonCollectBoxDetail.productCertifications[].fileName` | string | 否 | 文件名称 |
| `data.editCommonCollectBoxDetail.productCertifications[].fileUrl` | string | 否 | 文件URL |
| `data.editCommonCollectBoxDetail.guideInfo` | object | 否 | 说明书信息 |
| `data.editCommonCollectBoxDetail.guideInfo.productGuideFileName` | string | 否 | 文件名称 |
| `data.editCommonCollectBoxDetail.guideInfo.productGuideFileUrl` | string | 否 | 文件URL |
| `data.editCommonCollectBoxDetail.sourceMataInfo` | object | 否 | 货源元信息 |
| `data.editCommonCollectBoxDetail.sourceList` | array<object> | 否 | 货源信息列表 |
| `data.editCommonCollectBoxDetail.sourceList[].remark` | string | 否 | 备注 |
| `data.editCommonCollectBoxDetail.sourceList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.editCommonCollectBoxDetail.sourceList[].source` | string | 否 | 来源平台 |
| `data.editCommonCollectBoxDetail.sourceList[].sourceSite` | string | 否 | 来源站点 |
| `data.editCommonCollectBoxDetail.sourceList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.editCommonCollectBoxDetail.sourceSupplierInfo` | object | 否 | 货源供应商信息 |
| `data.ossMd5` | string | 否 | 公共采集箱详情OssMd5标识 |


---

### 批量删除公共采集箱产品

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/batch_delete_common_collect_box_detail`
- 类型：写
- 原文：[446814584e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814584e0.md)（本地 raw/446814584e0_批量删除公共采集箱产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `commonCollectBoxDetailIds` | array<integer> | 是 | 公共采集箱ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 认领到平台采集箱

- 层级：开放平台 > 商品 > 公共采集箱
- 方法+路径：`POST /open/v1/product/common_collect_box/common_collect_box/claimed`
- 类型：写
- 原文：[446814587e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814587e0.md)（本地 raw/446814587e0_认领到平台采集箱.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailSerialNumberPlatformList` | array<object> | 是 | 认领数据列表 |
| `detailSerialNumberPlatformList[].detailId` | integer | 是 | 公共采集箱ID |
| `detailSerialNumberPlatformList[].platform` | string | 是 | 认领的平台(TK-tiktok, temu全托-pddkj, temu半托-pddkjChoice, 虾皮-shopee, ozon-ozon,美客多-mercadolibre) |
| `detailSerialNumberPlatformList[].serialNumber` | integer | 是 | 序列号（默认传1） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.platformCollectBoxDetailIdMap` | object | 否 | 各平台采集箱详情ID映射 key: 平台名（如 tiktok），value: collectBoxId => detailId 的映射 |


## TK采集箱>采集箱

### 获取类目列表

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[446814588e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814588e0.md)（本地 raw/446814588e0_获取类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cateTree` | object | 否 | 分类树 Map（key=cid, value=分类节点） |


---

### 获取类目属性信息

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_category_metadata`
- 类型：读
- 原文：[446814589e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814589e0.md)（本地 raw/446814589e0_获取类目属性信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 否 | 站点(shopIds为空时必传) |
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array<integer> | 否 | 店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.categoryMetadata` | object | 否 | 分类元数据 |
| `data.categoryMetadata.categoryConfig` | object | 否 | 分类配置 |
| `data.categoryMetadata.categoryConfig.isSuppSizechart` | string | 否 | 是否支持尺码表 |
| `data.categoryMetadata.categoryConfig.isSuppCod` | boolean | 否 | 是否支持货到付款 |
| `data.categoryMetadata.categoryConfig.productCertifications` | array<object> | 否 | 商品认证列表 |
| `data.categoryMetadata.categoryConfig.productCertifications[].documentDetails` | string | 否 | 认证文件说明 |
| `data.categoryMetadata.categoryConfig.productCertifications[].id` | string | 否 | 认证ID |
| `data.categoryMetadata.categoryConfig.productCertifications[].isRequired` | boolean | 否 | 是否必填 |
| `data.categoryMetadata.categoryConfig.productCertifications[].name` | string | 否 | 认证名称 |
| `data.categoryMetadata.categoryConfig.productCertifications[].sampleImageUrl` | string | 否 | 示例图片URL |
| `data.categoryMetadata.categoryConfig.productCertifications[].isMandatory` | boolean | 否 | 是否强制要求 |
| `data.categoryMetadata.categoryConfig.productCertifications[].requirementConditions` | array<object> | 否 | 需求条件列表 |
| `data.categoryMetadata.categoryConfig.isSupportExemptionIdentifierCode` | string | 否 | 是否支持豁免标识码 |
| `data.categoryMetadata.categoryConfig.sizeChartIsSupported` | string | 否 | 尺码表是否支持 |
| `data.categoryMetadata.categoryConfig.sizeChartIsRequired` | string | 否 | 尺码表是否必填 |
| `data.categoryMetadata.categoryConfig.codIsSupported` | string | 否 | 货到付款是否支持 |
| `data.categoryMetadata.categoryConfig.packageDimensionIsRequired` | string | 否 | 包装尺寸是否必填 |
| `data.categoryMetadata.categoryConfig.eprIsRequired` | string | 否 | EPR是否必填 |
| `data.categoryMetadata.categoryConfig.responsiblePersonIsRequired` | string | 否 | 责任人是否必填 |
| `data.categoryMetadata.categoryConfig.manufacturerIsRequired` | string | 否 | 制造商是否必填 |
| `data.categoryMetadata.categoryConfig.isSizeChartMandatory` | string | 否 | 尺码表是否强制 |
| `data.categoryMetadata.categorySaleAttrList` | array<object> | 否 | 销售属性列表 |
| `data.categoryMetadata.categorySaleAttrList[].attrId` | string | 否 | 属性ID |
| `data.categoryMetadata.categorySaleAttrList[].name` | string | 否 | 属性名称（英文） |
| `data.categoryMetadata.categorySaleAttrList[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.categoryMetadata.categorySaleAttrList[].attributeType` | integer | 否 | 属性类型 |
| `data.categoryMetadata.categorySaleAttrList[].isMandatory` | boolean | 否 | 是否必填 |
| `data.categoryMetadata.categorySaleAttrList[].isMultipleSelected` | boolean | 否 | 是否可多选 |
| `data.categoryMetadata.categorySaleAttrList[].isCustomized` | boolean | 否 | 是否可自定义 |
| `data.categoryMetadata.categorySaleAttrList[].valueDataFormat` | object | 否 | 值数据格式 |
| `data.categoryMetadata.categorySaleAttrList[].isCertificationAttr` | boolean | 否 | 是否认证属性 |
| `data.categoryMetadata.categorySaleAttrList[].requirementConditions` | object | 否 | 需求条件 |
| `data.categoryMetadata.categorySaleAttrList[].valueIdAndRequiredAttrIdsMap` | object | 否 | 值ID与必填属性ID映射 |
| `data.categoryMetadata.categorySaleAttrList[].valueIdAndRequiredCertificationIdsMap` | object | 否 | 值ID与必填认证ID映射 |
| `data.categoryMetadata.categorySaleAttrList[].values` | array<object> | 否 | 属性值列表 |
| `data.categoryMetadata.categorySaleAttrList[].values[].id` | string | 否 | 属性值ID |
| `data.categoryMetadata.categorySaleAttrList[].values[].name` | string | 否 | 属性值名称（英文） |
| `data.categoryMetadata.categorySaleAttrList[].values[].valueNameAlias` | string | 否 | 属性值名称别名（中文） |
| `data.categoryMetadata.categorySaleAttrList[].optionalRegions` | array<string> | 否 | 可选地区列表 |
| `data.categoryMetadata.categorySaleAttrList[].requiredRegions` | array<string> | 否 | 必填地区列表 |
| `data.categoryMetadata.categoryProductAttrList` | array<object> | 否 | 商品属性列表 |
| `data.categoryMetadata.categoryProductAttrList[].attrId` | string | 否 | 属性ID |
| `data.categoryMetadata.categoryProductAttrList[].name` | string | 否 | 属性名称（英文） |
| `data.categoryMetadata.categoryProductAttrList[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.categoryMetadata.categoryProductAttrList[].attributeType` | integer | 否 | 属性类型 |
| `data.categoryMetadata.categoryProductAttrList[].isMandatory` | boolean | 否 | 是否必填 |
| `data.categoryMetadata.categoryProductAttrList[].isMultipleSelected` | boolean | 否 | 是否可多选 |
| `data.categoryMetadata.categoryProductAttrList[].isCustomized` | boolean | 否 | 是否可自定义 |
| `data.categoryMetadata.categoryProductAttrList[].valueDataFormat` | object | 否 | 值数据格式 |
| `data.categoryMetadata.categoryProductAttrList[].isCertificationAttr` | boolean | 否 | 是否认证属性 |
| `data.categoryMetadata.categoryProductAttrList[].requirementConditions` | object | 否 | 需求条件 |
| `data.categoryMetadata.categoryProductAttrList[].valueIdAndRequiredAttrIdsMap` | object | 否 | 值ID与必填属性ID映射 |
| `data.categoryMetadata.categoryProductAttrList[].valueIdAndRequiredCertificationIdsMap` | object | 否 | 值ID与必填认证ID映射 |
| `data.categoryMetadata.categoryProductAttrList[].values` | array<object> | 否 | 属性值列表 |
| `data.categoryMetadata.categoryProductAttrList[].values[].id` | string | 否 | 属性值ID |
| `data.categoryMetadata.categoryProductAttrList[].values[].name` | string | 否 | 属性值名称（英文） |
| `data.categoryMetadata.categoryProductAttrList[].values[].valueNameAlias` | string | 否 | 属性值名称别名（中文） |
| `data.categoryMetadata.categoryProductAttrList[].optionalRegions` | array<string> | 否 | 可选地区列表 |
| `data.categoryMetadata.categoryProductAttrList[].requiredRegions` | array<string> | 否 | 必填地区列表 |


---

### 获取店铺仓库列表

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_shop_warehouse_list`
- 类型：读
- 原文：[446814590e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814590e0.md)（本地 raw/446814590e0_获取店铺仓库列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopWarehouseList` | array<object> | 否 | 店铺仓库列表 |
| `data.shopWarehouseList[].shopId` | integer | 否 | 店铺ID |
| `data.shopWarehouseList[].shopName` | string | 否 | 店铺名称 |
| `data.shopWarehouseList[].platform` | string | 否 | 平台 |
| `data.shopWarehouseList[].site` | string | 否 | 站点 |
| `data.shopWarehouseList[].warehouseList` | array<object> | 否 | 仓库列表 |
| `data.shopWarehouseList[].warehouseList[].shopId` | string | 否 | 店铺ID |
| `data.shopWarehouseList[].warehouseList[].warehouseId` | string | 否 | 仓库ID |
| `data.shopWarehouseList[].warehouseList[].warehouseName` | string | 否 | 仓库名称 |
| `data.shopWarehouseList[].warehouseList[].warehouseSubType` | string | 否 | 仓库子类型 |
| `data.shopWarehouseList[].warehouseList[].warehouseEffectStatus` | string | 否 | 仓库生效状态 |
| `data.shopWarehouseList[].warehouseList[].isDefault` | string | 否 | 是否默认仓库 |
| `data.shopWarehouseList[].warehouseList[].inventoryRule` | object | 否 | 库存规则 |
| `data.shopWarehouseList[].warehouseList[].inventoryRule.allocationMode` | string | 否 | 库存分配模式 |
| `data.shopWarehouseList[].warehouseList[].inventoryRule.associatedWarehouses` | array<object> | 否 | 关联仓库列表 |


---

### 获取制造商列表

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_manufacturer_list`
- 类型：读
- 原文：[449869292e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449869292e0.md)（本地 raw/449869292e0_获取制造商列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `refresh` | integer | 是 | 是否重新刷新数据（0=否，1=是） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.manufacturerList` | array<object> | 否 | 制造商列表 |
| `data.manufacturerList[].id` | string | 否 | 制造商ID |
| `data.manufacturerList[].name` | string | 否 | 制造商名称 |


---

### 获取欧盟责任人列表

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_responsible_person_list`
- 类型：读
- 原文：[449869293e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449869293e0.md)（本地 raw/449869293e0_获取欧盟责任人列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `refresh` | integer | 是 | 是否重新刷新数据（0=否，1=是） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.responsiblePersonList` | array<object> | 否 | 欧盟责任人列表 |
| `data.responsiblePersonList[].id` | string | 否 | 欧盟责任人ID |
| `data.responsiblePersonList[].name` | string | 否 | 欧盟责任人名称 |


---

### 认领预发布店铺

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/claim_to_shop`
- 类型：写
- 原文：[446814594e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814594e0.md)（本地 raw/446814594e0_认领预发布店铺.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取采集箱列表

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[446814591e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814591e0.md)（本地 raw/446814591e0_获取采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array<object> | 否 | 采集箱数据列表 |
| `data.detailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.detailList[].itemNum` | string | 否 | 商品编号 |
| `data.detailList[].stock` | string | 否 | 库存 |
| `data.detailList[].price` | string | 否 | 价格 |
| `data.detailList[].thumbnail` | string | 否 | 缩略图 |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].editModel` | string | 否 | 编辑模式 |
| `data.detailList[].commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | string | 否 | 应用账户ID |
| `data.detailList[].subAppAccountId` | string | 否 | 子应用账户ID |
| `data.detailList[].platform` | string | 否 | 平台 |
| `data.detailList[].title` | string | 否 | 商品标题 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].copyType` | string | 否 | 复制类型 |
| `data.detailList[].collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.detailList[].collectBoxGroupName` | string | 否 | 采集箱分组名称 |
| `data.detailList[].collectBoxDetailShopList` | array<object> | 否 | 预发布店铺信息列表 |
| `data.detailList[].collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |
| `data.detailList[].isSupportReplicateProduct` | boolean | 否 | 是否支持新链路 |


---

### 获取采集箱店铺模式详情

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_shop_collect_item_info`
- 类型：读
- 原文：[446814592e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814592e0.md)（本地 raw/446814592e0_获取采集箱店铺模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 | ossMd5值 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array<integer> | 否 | 已认领的店铺IDS |
| `data.isSupportMultiWarehouse` | integer | 否 | 是否支持多仓库 |
| `data.shopCollectItemInfo` | object | 否 | 店铺模式数据 |
| `data.shopCollectItemInfo.site` | string | 否 | 站点代码（如 MY、SG） |
| `data.shopCollectItemInfo.shopId` | integer | 否 | 店铺ID |
| `data.shopCollectItemInfo.detailId` | integer | 否 | 详情ID |
| `data.shopCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.shopCollectItemInfo.oriTitle` | string | 否 | 商品原始标题 |
| `data.shopCollectItemInfo.notes` | string | 否 | 备注 |
| `data.shopCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `data.shopCollectItemInfo.brandName` | string | 否 | 品牌名称 |
| `data.shopCollectItemInfo.productAttributes` | array<object> | 否 | 商品属性列表 |
| `data.shopCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `data.shopCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.shopCollectItemInfo.productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `data.shopCollectItemInfo.skuMap` | object | 否 | SKU Map（key=SKU标识码，value=SKU条目） |
| `data.shopCollectItemInfo.skuPropertyList` | array<object> | 否 | SKU销售属性列表 |
| `data.shopCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `data.shopCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值 |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性图片URL |
| `data.shopCollectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 否 | 补充SKU图片URL列表 |
| `data.shopCollectItemInfo.imgUrls` | array<string> | 否 | 商品图片URL列表 |
| `data.shopCollectItemInfo.weight` | number | 否 | 重量（kg） |
| `data.shopCollectItemInfo.packageLength` | number | 否 | 包裹长度（cm） |
| `data.shopCollectItemInfo.packageWidth` | number | 否 | 包裹宽度（cm） |
| `data.shopCollectItemInfo.packageHeight` | number | 否 | 包裹高度（cm） |
| `data.shopCollectItemInfo.isCodOpen` | string | 否 | 是否开启货到付款（1-是，0-否） |
| `data.shopCollectItemInfo.productCertifications` | array<object> | 否 | 商品认证列表 |
| `data.shopCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `data.shopCollectItemInfo.productCertifications[].files` | array<object> | 否 | 认证文件列表 |
| `data.shopCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（上传到TK的会有这个ID） |
| `data.shopCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `data.shopCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `data.shopCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `data.shopCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `data.shopCollectItemInfo.mainImgPlatformVideoId` | string | 否 | 主图平台视频ID |
| `data.shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.shopCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.shopCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型 |
| `data.shopCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `data.shopCollectItemInfo.manufacturerIds` | array<string> | 否 | 制造商ID列表 |
| `data.shopCollectItemInfo.responsiblePersonIds` | array<string> | 否 | 责任人ID列表 |


---

### 保存采集箱店铺模式详情

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/save_shop_collect_item_info`
- 类型：写
- 原文：[446814593e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814593e0.md)（本地 raw/446814593e0_保存采集箱店铺模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ossMd5` | string | 是 | ossMd5值 |
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.notes` | string | 是 | 商品描述 |
| `shopCollectItemInfo.imgUrls` | array<string> | 是 | 商品图片URL列表 |
| `shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `shopCollectItemInfo.weight` | number | 是 | 重量（kg） |
| `shopCollectItemInfo.packageLength` | number | 是 | 包装长度（cm） |
| `shopCollectItemInfo.packageWidth` | number | 是 | 包装宽度（cm） |
| `shopCollectItemInfo.packageHeight` | number | 是 | 包装高度（cm） |
| `shopCollectItemInfo.productCertifications` | array<object> | 否 | 商品认证列表 |
| `shopCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `shopCollectItemInfo.productCertifications[].files` | array<object> | 否 | 认证文件列表 |
| `shopCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（如果文件是TK的需要传这个ID） |
| `shopCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `shopCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `shopCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `shopCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `shopCollectItemInfo.isCodOpen` | string | 是 | 是否开启货到付款（1=是，0=否） |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.editModel` | string | 否 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.version` | string | 否 | 版本号 |
| `shopCollectItemInfo.shopId` | integer | 否 | 店铺ID |
| `shopCollectItemInfo.detailId` | integer | 否 | 采集箱详情ID |
| `shopCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型（仅支持image） |
| `shopCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `shopCollectItemInfo.deliveryOptionSetType` | string | 是 | 配送选项设置类型仅支持（仅default） |
| `shopCollectItemInfo.skuMap` | object | 否 | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `shopCollectItemInfo.skuPropertyList` | array<object> | 否 | SKU 规格属性列表 |
| `shopCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称，如 Color、Size |
| `shopCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `shopCollectItemInfo.skuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID（构造SkuMap的key时使用该值） |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `shopCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值图片URL |
| `shopCollectItemInfo.productAttributes` | array<object> | 否 | 商品属性列表 |
| `shopCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `shopCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `shopCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `shopCollectItemInfo.productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `shopCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `shopCollectItemInfo.manufacturerIds` | array<string> | 否 | 制造商ID列表 |
| `shopCollectItemInfo.responsiblePersonIds` | array<string> | 否 | 责任人ID列表 |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 是 | 采集箱详情OssMd5标识 |


---

### 获取采集箱站点模式详情

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[449650816e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449650816e0.md)（本地 raw/449650816e0_获取采集箱站点模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `site` | string | 是 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 | ossMd5值 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array<integer> | 否 | 已认领的店铺IDS |
| `data.isSupportMultiWarehouse` | integer | 否 | 是否支持多仓库 |
| `data.siteCollectItemInfo` | object | 否 | 店铺模式数据 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点代码（如 PH、MY） |
| `data.siteCollectItemInfo.detailId` | integer | 否 | 详情ID |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.notes` | string | 否 | 备注 |
| `data.siteCollectItemInfo.imgUrls` | array<string> | 否 | 商品图片URL列表 |
| `data.siteCollectItemInfo.weight` | number | 否 | 重量（kg） |
| `data.siteCollectItemInfo.packageLength` | number | 否 | 包裹长度（cm） |
| `data.siteCollectItemInfo.packageWidth` | number | 否 | 包裹宽度（cm） |
| `data.siteCollectItemInfo.packageHeight` | number | 否 | 包裹高度（cm） |
| `data.siteCollectItemInfo.productCertifications` | array<object> | 否 | 商品认证列表 |
| `data.siteCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `data.siteCollectItemInfo.productCertifications[].files` | array<object> | 否 | 认证文件列表 |
| `data.siteCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（上传到TK的会有这个ID） |
| `data.siteCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `data.siteCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `data.siteCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `data.siteCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `data.siteCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型 |
| `data.siteCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU Map（key=SKU标识码，value=SKU条目） |
| `data.siteCollectItemInfo.skuPropertyList` | array<object> | 否 | SKU销售属性列表 |
| `data.siteCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `data.siteCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值 |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性图片URL |
| `data.siteCollectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 否 | 补充SKU图片URL列表 |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图App端视频ID |
| `data.siteCollectItemInfo.mainImgPlatformVideoId` | string | 否 | 主图平台视频ID |
| `data.siteCollectItemInfo.isCodOpen` | string | 否 | 是否开启货到付款（1-是，0-否） |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.siteCollectItemInfo.productAttributes` | array<object> | 否 | 商品属性列表 |
| `data.siteCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `data.siteCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `data.siteCollectItemInfo.productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 否 | 采集箱店铺维度配置列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点代码（如 PH、MY） |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].brandId` | string | 否 | 品牌ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].brandName` | string | 否 | 品牌名称 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].deliveryOptionSetType` | string | 否 | 配送选项设置类型 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].deliveryOptionIds` | array<string> | 否 | 配送选项ID列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].manufacturerIds` | array<string> | 否 | 制造商ID列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].responsiblePersonIds` | array<string> | 否 | 责任人ID列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].sizeChartTemplateId` | string | 否 | 尺码表模板ID |


---

### 保存采集箱站点模式详情

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/save_site_collect_item_info`
- 类型：写
- 原文：[449650817e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449650817e0.md)（本地 raw/449650817e0_保存采集箱站点模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ossMd5` | string | 是 | ossMd5值 |
| `site` | string | 是 | 站点 |
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 商品描述 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 商品图片URL列表 |
| `siteCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `siteCollectItemInfo.weight` | number | 是 | 重量（kg） |
| `siteCollectItemInfo.packageLength` | number | 是 | 包装长度（cm） |
| `siteCollectItemInfo.packageWidth` | number | 是 | 包装宽度（cm） |
| `siteCollectItemInfo.packageHeight` | number | 是 | 包装高度（cm） |
| `siteCollectItemInfo.productCertifications` | array<object> | 否 | 商品认证列表 |
| `siteCollectItemInfo.productCertifications[].id` | string | 否 | 认证ID |
| `siteCollectItemInfo.productCertifications[].files` | array<object> | 否 | 认证文件列表 |
| `siteCollectItemInfo.productCertifications[].files[].fileId` | string | 否 | 文件ID（如果文件是TK的需要传这个ID） |
| `siteCollectItemInfo.productCertifications[].files[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.productCertifications[].files[].fileType` | string | 否 | 文件类型（如 PDF） |
| `siteCollectItemInfo.productCertifications[].files[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productCertifications[].gmtExpirationDate` | string | 否 | 认证到期日期 |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.isCodOpen` | string | 是 | 是否开启货到付款（1=是，0=否） |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.editModel` | string | 否 | 编辑模式（shop=店铺模式，site=站点模式） |
| `siteCollectItemInfo.version` | string | 否 | 版本号 |
| `siteCollectItemInfo.shopId` | integer | 否 | 店铺ID |
| `siteCollectItemInfo.detailId` | integer | 否 | 采集箱详情ID |
| `siteCollectItemInfo.sizeChartType` | string | 否 | 尺码表类型（仅支持image） |
| `siteCollectItemInfo.sizeChart` | string | 否 | 尺码表图片URL |
| `siteCollectItemInfo.deliveryOptionSetType` | string | 是 | 配送选项设置类型仅支持（仅default） |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU Map，key为规格属性值ID组合串，格式为「;属性值ID1;属性值ID2;」（属性值ID从小到大，分号分隔，首尾带分号），value为SKU数据 |
| `siteCollectItemInfo.skuPropertyList` | array<object> | 否 | SKU 规格属性列表 |
| `siteCollectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称，如 Color、Size |
| `siteCollectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `siteCollectItemInfo.skuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID（构造SkuMap的key时使用该值） |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值图片URL |
| `siteCollectItemInfo.productAttributes` | array<object> | 否 | 商品属性列表 |
| `siteCollectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `siteCollectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `siteCollectItemInfo.productAttributes[].attributeNameAlias` | string | 否 | 属性名称别名（中文） |
| `siteCollectItemInfo.productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `siteCollectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 否 | 店铺特殊数据信息列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 是 | 站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].brandId` | string | 否 | 品牌ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].manufacturerIds` | array<string> | 否 | 制造商ID列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].responsiblePersonIds` | array<string> | 否 | 责任人ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 是 | 采集箱详情OssMd5标识 |


---

### 产品翻译

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/translate_collect_item_info`
- 类型：处理(生成内容)
- 原文：[482189160e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189160e0.md)（本地 raw/482189160e0_产品翻译.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `sourceLanguage` | string | 是 | 原始语言 可选值：auto(自动识别), zh(简体中文), zh-tw(中繁体), en(英文), th(泰文), vi(越南文), id(印尼文), ms(马来语), es(西班牙文), pt(葡萄牙语), pl(波兰语), fr(法文), bn(孟加拉语), it(意大利文), de(德语), fi(芬兰语), cs(捷克语), ja(日文), he(希伯来语), ur(乌尔都语), uk(乌克兰语), el(希腊语), kk(哈萨克语), nl(荷兰语), sv(瑞典语), ko(韩文), ru(俄文), ar(阿拉伯语), tr(土耳其语), ro(罗马尼亚语), bg(保加利亚语), hu(匈牙利语), se(瑞典语), ga(爱尔兰语) |
| `targetLanguage` | string | 是 | 目标语言 可选值：zh(简体中文), zh-tw(中繁体), en(英文), th(泰文), vi(越南文), id(印尼文), ms(马来语), es(西班牙文), pt(葡萄牙语), pl(波兰语), fr(法文), bn(孟加拉语), it(意大利文), de(德语), fi(芬兰语), cs(捷克语), ja(日文), he(希伯来语), ur(乌尔都语), uk(乌克兰语), el(希腊语), kk(哈萨克语), nl(荷兰语), sv(瑞典语), ko(韩文), ru(俄文), ar(阿拉伯语), tr(土耳其语), ro(罗马尼亚语), bg(保加利亚语), hu(匈牙利语), se(瑞典语), ga(爱尔兰语) |
| `collectItemInfo` | object | 是 | 需翻译的产品详情 |
| `collectItemInfo.title` | string | 否 | 商品标题 |
| `collectItemInfo.notes` | string | 否 | 备注 |
| `collectItemInfo.warrantyPolicy` | string | 否 | 保修政策 |
| `collectItemInfo.skuMap` | object | 否 | SKU Map（key=SKU标识码，value=SKU条目） |
| `collectItemInfo.skuPropertyList` | array<object> | 否 | SKU销售属性列表 |
| `collectItemInfo.skuPropertyList[].attrId` | string | 否 | 属性ID |
| `collectItemInfo.skuPropertyList[].attrName` | string | 否 | 属性名称 |
| `collectItemInfo.skuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 |
| `collectItemInfo.skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `collectItemInfo.skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值 |
| `collectItemInfo.skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性图片URL |
| `collectItemInfo.skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 否 | 补充SKU图片URL列表 |
| `collectItemInfo.productAttributes` | array<object> | 否 | 商品属性列表 |
| `collectItemInfo.productAttributes[].attributeId` | string | 否 | 属性ID |
| `collectItemInfo.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `collectItemInfo.productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `collectItemInfo.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `collectItemInfo.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |
| `isTranslateSkuItemNum` | integer | 是 | 是否翻译平台sku（0=否，1=是） |
| `isTranslateSkuProperty` | integer | 是 | 是否翻译SKU规格名称（0=否，1=是） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectItemInfo` | object | 否 | 翻译后的产品详情（只翻译，没有保存翻译后的数据，用户需自行保存） |


---

### AI匹配类目

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/ai_match_cid_by_shop_ids`
- 类型：处理(生成内容)
- 原文：[482189162e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189162e0.md)（本地 raw/482189162e0_AI匹配类目.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | integer | 是 | 采集箱详情ID |
| `shopIds` | array<integer> | 是 | 店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndCidMap` | object | 否 | 店铺与匹配CID的映射 示例：{ 100001 : 11231, 100002 : 12345 } |
| `data.failedShopIds` | array<integer> | 否 | 匹配失败的店铺ID列表，失败就代表没有这个店铺没有匹配上类目 |


---

### 批量删除采集箱产品接口

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/delete_collect_box_detail`
- 类型：写
- 原文：[496804330e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/496804330e0.md)（本地 raw/496804330e0_批量删除采集箱产品接口.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successNum` | integer | 否 | 删除成功数量 |
| `data.failNum` | integer | 否 | 删除失败数量 |
| `data.errorMap` | object | 否 | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `data.errorMsg` | string | 否 | 拼接后的错误信息 |


---

### AI属性匹配

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/ai_match_product_attribute`
- 类型：处理(生成内容)
- 原文：[482189161e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189161e0.md)（本地 raw/482189161e0_AI属性匹配.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | integer | 是 | 采集箱详情ID |
| `cid` | string | 是 | 类目ID |
| `site` | string | 是 | 站点 |
| `shopIds` | array<integer> | 否 | 店铺ID列表 当产品与店铺关联时传入，用于精确查找 |
| `productAttributes` | array<object> | 否 | 当前产品属性列表 |
| `productAttributes[].attributeId` | string | 否 | 属性ID |
| `productAttributes[].attributeName` | string | 否 | 属性名称 |
| `productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.productAttributes` | array<object> | 否 | AI匹配后的产品属性列表 |
| `data.productAttributes[].attributeId` | string | 否 | 属性ID |
| `data.productAttributes[].attributeName` | string | 否 | 属性名称 |
| `data.productAttributes[].attributeValues` | array<object> | 否 | 属性值列表 |
| `data.productAttributes[].attributeValues[].valueName` | string | 否 | 属性值名称 |
| `data.productAttributes[].attributeValues[].valueId` | string | 否 | 属性值ID |


---

### 获取品牌列表

- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_brand_list`
- 类型：读
- 原文：[497001483e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/497001483e0.md)（本地 raw/497001483e0_获取品牌列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `brandName` | string | 否 | 品牌名搜索关键字 |
| `nextPageToken` | string | 否 | 获取下一页数据的Token |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.brandList` | array<object> | 否 | 品牌列表 |
| `data.brandList[].authorizedStatus` | string | 否 | 该品牌的授权状态（只有授权通过的品牌才会在前台展示）授权通过-AUTHORIZED，授权未通过-UNAUTHORIEZD |
| `data.brandList[].brandId` | string | 否 | 品牌ID |
| `data.brandList[].brandName` | string | 否 | 品牌名称 |
| `data.nextPageToken` | string | 否 | 获取下一页数据的Token |
| `data.totalCount` | integer | 否 | 品牌总数 |


## TK采集箱>产品发布

### 发布产品

- 层级：开放平台 > 商品 > TK采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/save_move_collect_task`
- 类型：写
- 原文：[446814595e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814595e0.md)（本地 raw/446814595e0_发布产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 发布记录列表

- 层级：开放平台 > 商品 > TK采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/move_collect/search_move_collect_list`
- 类型：读
- 原文：[482189163e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189163e0.md)（本地 raw/482189163e0_发布记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array<object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |


## TK采集箱>定价模板

### 获取定价模板列表

- 层级：开放平台 > 商品 > TK采集箱 > 定价模板
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/price_template/get_price_template_list`
- 类型：读
- 原文：[482189164e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189164e0.md)（本地 raw/482189164e0_获取定价模板列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 否 | 模板名称（模糊搜索） |
| `site` | string | 否 | 站点 |
| `siteType` | string | 否 | 站点类型：cross_border 跨境 / mainland 本土 |
| `pageNo` | integer | 是 | 页码 |
| `pageSize` | integer | 是 | 每页条数 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.priceTemplateList` | array<object> | 否 | 定价模板列表 |
| `data.priceTemplateList[].priceTemplateId` | integer | 否 | 定价模板 ID |
| `data.priceTemplateList[].appAccountId` | integer | 否 | 主账号 ID |
| `data.priceTemplateList[].subAppAccountId` | integer | 否 | 子账号 ID |
| `data.priceTemplateList[].platform` | string | 否 | 平台标识，如 tiktok |
| `data.priceTemplateList[].site` | string | 否 | 站点，如 MY / PH / US |
| `data.priceTemplateList[].name` | string | 否 | 模板名称 |
| `data.priceTemplateList[].remark` | string | 否 | 备注 |
| `data.priceTemplateList[].currency` | string | 否 | 站点币种，如 MYR / PHP / USD |
| `data.priceTemplateList[].displayWeightUnit` | string | 否 | 重量单位显示类型：kilogram / gram |
| `data.priceTemplateList[].profitType` | string | 否 | 利润计算类型：percent 百分比 / fixed 固定金额 |
| `data.priceTemplateList[].profitPercent` | number | 否 | 利润百分比（profitType=percent 时生效） |
| `data.priceTemplateList[].fixedProfitAmount` | number | 否 | 固定利润金额（profitType=fixed 时生效） |
| `data.priceTemplateList[].exchangeRate` | number | 否 | 汇率（人民币兑站点币种） |
| `data.priceTemplateList[].discount` | number | 否 | 折扣率（0~1，如 0.9 表示九折） |
| `data.priceTemplateList[].priceTailComputeType` | string | 否 | 价格尾数处理类型：process_decimal / fixed_tail |
| `data.priceTemplateList[].priceTail` | string | 否 | 价格尾数值（priceTailComputeType=fixed_tail 时生效） |
| `data.priceTemplateList[].priceProcessDecimalType` | string | 否 | 小数处理类型：floor 向下 / ceil 向上 / round 四舍五入 |
| `data.priceTemplateList[].logisticsComputeType` | string | 否 | 国际物流计算类型：fixed / first_continued / weight_interval / official_freight_tpl |
| `data.priceTemplateList[].weightRefType` | string | 否 | 重量参考类型：weight / volume_weight / max_weight |
| `data.priceTemplateList[].firstWeightCharge` | number | 否 | 首重费用（国际物流 first_continued 类型时生效） |
| `data.priceTemplateList[].firstWeightInterval` | number | 否 | 首重区间（g 或 kg，取决于 displayWeightUnit） |
| `data.priceTemplateList[].continuedWeightCharge` | number | 否 | 续重费用（国际物流 first_continued 类型时生效） |
| `data.priceTemplateList[].continuedWeightInterval` | number | 否 | 续重区间（g 或 kg，取决于 displayWeightUnit） |
| `data.priceTemplateList[].logisticsCharge` | number | 否 | 固定物流费用（国际物流 fixed 类型时生效） |
| `data.priceTemplateList[].platformChargePercent` | number | 否 | 平台费率（百分比，如 2.12 表示 2.12%） |
| `data.priceTemplateList[].paymentChargePercent` | number | 否 | 支付手续费率 |
| `data.priceTemplateList[].activityChargePercent` | number | 否 | 活动费率 |
| `data.priceTemplateList[].withdrawChargePercent` | number | 否 | 提现手续费率 |
| `data.priceTemplateList[].otherCharge` | number | 否 | 其他杂费（站点币种） |
| `data.priceTemplateList[].isCalLightCargo` | integer | 否 | 是否计算抛货（轻货）：1 是 / 0 否 |
| `data.priceTemplateList[].lightCargoCoefficient` | integer | 否 | 抛货体积重系数（isCalLightCargo=1 时生效，单位：cm³/g） |
| `data.priceTemplateList[].weightLogisticsChargeList` | string | 否 | 分段重量物流费用列表（logisticsComputeType=weight_interval 时生效） 格式：[['minWeight'=>0, 'maxWeight'=>1000, 'charge'=>5.00], ...] |
| `data.priceTemplateList[].domesticLogisticsComputeType` | string | 否 | 国内物流计算类型：fixed / first_continued |
| `data.priceTemplateList[].domesticLogisticsFirstWeightCharge` | number | 否 | 国内物流首重费用 |
| `data.priceTemplateList[].domesticLogisticsFirstWeightInterval` | number | 否 | 国内物流首重区间 |
| `data.priceTemplateList[].domesticLogisticsContinuedWeightCharge` | number | 否 | 国内物流续重费用 |
| `data.priceTemplateList[].domesticLogisticsContinuedWeightInterval` | number | 否 | 国内物流续重区间 |
| `data.priceTemplateList[].domesticLogisticsCharge` | number | 否 | 国内物流固定费用（domesticLogisticsComputeType=fixed 时生效） |
| `data.priceTemplateList[].buyerLogisticCharge` | number | 否 | 买家承担物流费用 |
| `data.priceTemplateList[].sellerLogisticCharge` | number | 否 | 卖家承担物流费用 |
| `data.priceTemplateList[].hasSellerLogisticCharge` | integer | 否 | 是否存在卖家承担运费：1 是 / 0 否 |
| `data.priceTemplateList[].officialTplMode` | string | 否 | 官方运费模板模式（logisticsComputeType=official_freight_tpl 时生效） |
| `data.priceTemplateList[].officialTplLogisticsChannel` | string | 否 | 官方运费模板物流渠道 |
| `data.priceTemplateList[].snapshotId` | integer | 否 | 快照 ID（用于追溯模板历史版本） |
| `data.priceTemplateList[].gmtCreate` | string | 否 | 创建时间 |
| `data.priceTemplateList[].gmtModified` | string | 否 | 最后修改时间 |
| `data.total` | integer | 否 | 总数 |
| `data.pageNo` | integer | 否 | 当前页码 |
| `data.pageSize` | integer | 否 | 每页条数 |


---

### 获取各个站点的默认配置

- 层级：开放平台 > 商品 > TK采集箱 > 定价模板
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/price_template/get_site_default_setting`
- 类型：读
- 原文：[482189165e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189165e0.md)（本地 raw/482189165e0_获取各个站点的默认配置.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.siteAndBuyerLogisticDefaultChargeMap` | object | 否 | 站点买家物流默认运费（站点币种） |
| `data.siteAndBuyerLogisticDefaultChargeCNYMap` | object | 否 | 站点买家物流默认运费（人民币） |
| `data.siteAndDefaultPlatformInfrastructureChargeMap` | object | 否 | 站点默认平台基础设施费（站点币种） |
| `data.siteAndDefaultPlatformInfrastructureChargeCNYMap` | object | 否 | 站点默认平台基础设施费（人民币） |
| `data.tiktokCbSiteAndDefaultChargePercentMap` | object | 否 | 跨境站点默认费率 key=站点代码，value=各项费率明细 |
| `data.tiktokLocalDefaultChargePercentMap` | object | 否 | 本土站点默认费率 |
| `data.siteAndDefaultPlatformSupportChargeMap` | object | 否 | 站点默认平台支持费（站点币种） |
| `data.siteAndDefaultPlatformSupportChargeCNYMap` | object | 否 | 站点默认平台支持费（人民币） |


## TEMU全托采集箱>产品发布

### 发布产品

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/move_collect/save_move_collect_task`
- 类型：写
- 原文：[468724006e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724006e0.md)（本地 raw/468724006e0_发布产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 发布记录列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/move_collect/search_move_collect_list`
- 类型：读
- 原文：[511668107e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511668107e0.md)（本地 raw/511668107e0_发布记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array<object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |


## TEMU全托采集箱>车型库

### 获取车型库站点列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_list`
- 类型：读
- 原文：[468724008e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724008e0.md)（本地 raw/468724008e0_获取车型库站点列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 否 | 类目ID，区分摩托车和汽车 ，不传返回全部 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsVehicleLibrarySiteList` | array<object> | 否 | 车型库站点列表，每项代表一个销售地区的车型库（如美国、欧洲等）。 根据产品的销售地区选择对应站点，取其 vehicleLibraryId 用于后续接口 |
| `data.goodsVehicleLibrarySiteList[].vehicleLibraryId` | integer | 否 | 车型库站点ID，选定站点后传入 getGoodsVehicleLibrarySiteTopPropDependencyList 获取顶级车型节点 |
| `data.goodsVehicleLibrarySiteList[].name` | string | 否 | 站点名称，如"美国"、"欧洲"，用于展示给用户选择 |
| `data.goodsVehicleLibrarySiteList[].pid` | integer | 否 | 属性ID |
| `data.goodsVehicleLibrarySiteList[].pidName` | string | 否 | 属性名称（中文），如"品牌"、"车系" |
| `data.goodsVehicleLibrarySiteList[].pidNameEn` | string | 否 | 属性名称（英文） |
| `data.goodsVehicleLibrarySiteList[].level` | integer | 否 | 层级（1=品牌，2=车系，3=年份，4=车型，5=发动机类型） |


<details><summary>请求示例</summary>

```json
{
  "cid": 21502
}
```
</details>

---

### 获取车型库站点属性结构映射

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map`
- 类型：读
- 原文：[468724009e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724009e0.md)（本地 raw/468724009e0_获取车型库站点属性结构映射.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 否 | 类目ID，区分摩托车和汽车 ，不传返回全部 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsVehicleLibraryIdAndSitePidInfoMap` | object | 否 | 车型库站点属性结构映射，key 为 vehicleLibraryId，value 为该站点的属性层级信息列表。 用于了解某站点车型库包含哪些层级属性（品牌/车系/年款等）及其对应的 pid， 结合 getVehicleLibraryPropDependencyTree 的树形数据使用 SitePidInfo 结构： - pddkjGoodsVehicleLibraryId: string 平台商品车型库ID - vehicleLibraryId: string 车型库ID - name: string 站点名称，如"美国站、加拿大站" - pidNameEn: string 属性英文名，如"Make"、"Model"、"Year" - parentPropertyDependencyId: string 父属性依赖ID - propertyDependencyId: string 属性依赖ID - pid: string 属性pid - pidName: string 属性中文名，如"汽车品牌"、"汽车型号" - level: string 层级序号 - status: string 状态，1=启用 |


<details><summary>请求示例</summary>

```json
{
  "cid": 21502
}
```
</details>

---

### 获取站点顶级车型节点列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list`
- 类型：读
- 原文：[468724010e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724010e0.md)（本地 raw/468724010e0_获取站点顶级车型节点列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.topGoodsVehicleLibraryPropDependencyList` | array<object> | 否 | 顶级车型节点列表（通常为品牌层），每项含 propertyValueDependencyId、vidValue 等字段。 取每项的 propertyValueDependencyId 作为 topPropertyValueDependencyId， 传入 getVehicleLibraryPropDependencyTree 获取该品牌下完整的车型树 |
| `data.topGoodsVehicleLibraryPropDependencyList[].pddkjGoodsVehicleLibraryPropDependencyId` | integer | 否 | 平台车型库属性依赖ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vehicleLibraryId` | integer | 否 | 车型库ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].topPropertyValueDependencyId` | integer | 否 | 顶级节点propertyValueDependencyId |
| `data.topGoodsVehicleLibraryPropDependencyList[].parentPropertyValueDependencyId` | integer | 否 | 父节点propertyValueDependencyId，顶级节点为0 |
| `data.topGoodsVehicleLibraryPropDependencyList[].propertyValueDependencyId` | integer | 否 | 当前节点propertyValueDependencyId |
| `data.topGoodsVehicleLibraryPropDependencyList[].propertyDependencyId` | integer | 否 | 属性依赖ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vid` | integer | 否 | 属性值ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vidValue` | string | 否 | 属性值文本，如品牌名"Country Coach" |
| `data.topGoodsVehicleLibraryPropDependencyList[].level` | integer | 否 | 层级序号 |
| `data.topGoodsVehicleLibraryPropDependencyList[].isLeaf` | integer | 否 | 是否为叶子节点，0=否，1=是 |
| `data.topGoodsVehicleLibraryPropDependencyList[].md5BreadcrumbVidValue` | string | 否 | 面包屑属性值的MD5 |
| `data.topGoodsVehicleLibraryPropDependencyList[].breadcrumbVidValue` | string | 否 | 面包屑属性值文本 |
| `data.topGoodsVehicleLibraryPropDependencyList[].breadcrumbPropertyValueDependencyId` | integer | 否 | 面包屑属性值依赖ID |


---

### 获取车型属性依赖树

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_vehicle_library_prop_dependency_tree`
- 类型：读
- 原文：[468724011e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724011e0.md)（本地 raw/468724011e0_获取车型属性依赖树.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |
| `topPropertyValueDependencyId` | integer | 是 | 顶级节点ID，从 getGoodsVehicleLibrarySiteTopPropDependencyList 返回的列表中取 propertyValueDependencyId |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.vehicleLibraryPropDependencyTree` | object | 否 | 车型属性依赖树，key 为顶级节点的 propertyValueDependencyId，value 为节点数据（含 children 子节点）。 树形结构按品牌→车系→年份→车型→发动机类型逐级展开，isLeaf=1 的节点为叶子节点。 选中叶子节点后，将从根节点到该叶子节点的完整路径组装为一条车型路径， 每个路径节点取 propertyValueDependencyId、vidValue、level 填入 vehicleLibraryRelationList[].productPropValueDependencyList 中 |


---

### 根据类目ID查询有车型库数据的类目列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_has_vehicle_library_cids_by_search_cids`
- 类型：读
- 原文：[468724007e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724007e0.md)（本地 raw/468724007e0_根据类目ID查询有车型库数据的类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cids` | array<integer> | 是 | 待查询的类目ID列表，传入产品所在类目的cid， 返回结果中包含的cid表示该类目支持车型库，发品时需填写车型适配信息 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.hasVehicleLibraryCids` | array<integer> | 否 | 有车型库的类目ID列表，如果产品所属类目在此列表中， 则发品时需要填写车型适配信息（vehicleLibrary相关字段） |


## TEMU全托采集箱>采集箱

### 获取类目属性规则

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_category_attribute_rules`
- 类型：读
- 原文：[471545320e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545320e0.md)（本地 raw/471545320e0_获取类目属性规则.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array<integer> | 否 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.saleAttributeRules` | array<object> | 否 | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `data.saleAttributeRules[].pid` | integer | 否 | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `data.saleAttributeRules[].templatePid` | integer | 否 | 模板属性ID，用于关联模板中的属性定义 |
| `data.saleAttributeRules[].refPid` | integer | 否 | 引用属性ID，表示该属性引用自哪个基础属性 |
| `data.saleAttributeRules[].name` | string | 否 | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `data.saleAttributeRules[].lang2Name` | string | 否 | 第二语言属性名称 |
| `data.saleAttributeRules[].isSale` | boolean | 否 | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `data.saleAttributeRules[].mainSale` | boolean | 否 | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `data.saleAttributeRules[].required` | boolean | 否 | 是否必填，为true时创建产品必须填写该属性 |
| `data.saleAttributeRules[].valueType` | string | 否 | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `data.saleAttributeRules[].controlType` | integer | 否 | 控件类型，决定前端展示方式 |
| `data.saleAttributeRules[].feature` | integer | 否 | 特征标记 |
| `data.saleAttributeRules[].chooseMaxNum` | integer | 否 | 最多可选数量，SELECT类型时最多可选几个value |
| `data.saleAttributeRules[].inputMaxNum` | integer | 否 | 输入最大数量，自定义输入的规格上限 |
| `data.saleAttributeRules[].minValue` | string | 否 | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `data.saleAttributeRules[].maxValue` | string | 否 | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `data.saleAttributeRules[].valuePrecision` | integer | 否 | 小数精度，数值保留几位小数 |
| `data.saleAttributeRules[].valueUnit` | array<string> | 否 | 合法单位列表，输入时必须使用列表中的单位 |
| `data.saleAttributeRules[].valueRule` | integer | 否 | 值规则 |
| `data.saleAttributeRules[].propertyValueType` | integer | 否 | 属性值类型 |
| `data.saleAttributeRules[].parentSpecId` | integer | 否 | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `data.saleAttributeRules[].parentTemplatePid` | integer | 否 | 父模板属性ID |
| `data.saleAttributeRules[].templatePropertyValueParentList` | array<object> | 否 | 父属性值模板ID列表，非string类型属性时使用 |
| `data.saleAttributeRules[].templatePropertyValueParentList[].parentVidList` | array<integer> | 否 | 父属性值ID列表 |
| `data.saleAttributeRules[].showCondition` | array<object> | 否 | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `data.saleAttributeRules[].showCondition[].parentRefPid` | integer | 否 | 父引用属性ID |
| `data.saleAttributeRules[].showCondition[].parentVids` | array<integer> | 否 | 父属性值ID列表 |
| `data.saleAttributeRules[].showType` | integer | 否 | 展示类型 |
| `data.saleAttributeRules[].propertyChooseTitle` | string | 否 | 属性选择标题，SELECT类型时的选择提示文字 |
| `data.saleAttributeRules[].numberInputTitle` | string | 否 | 数字输入标题，INPUT类型时的输入提示文字 |
| `data.saleAttributeRules[].referenceType` | integer | 否 | 引用类型 |
| `data.saleAttributeRules[].valueInputSum` | integer | 否 | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `data.saleAttributeRules[].values` | array<object> | 否 | 可选值列表，SELECT类型时从中选取vid和name |
| `data.saleAttributeRules[].values[].specId` | integer | 否 | 规格ID，自定义输入的值为null |
| `data.saleAttributeRules[].values[].vid` | integer | 否 | 属性值ID，填写属性时通过vid指定选中的值 |
| `data.saleAttributeRules[].values[].name` | string | 否 | 属性值名称，如"白色"、"XL"、"棉" |
| `data.saleAttributeRules[].values[].lang2Value` | string | 否 | 第二语言值 |
| `data.saleAttributeRules[].values[].extendInfo` | string | 否 | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `data.saleAttributeRules[].values[].group` | object | 否 | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `data.saleAttributeRules[].values[].parentVidList` | array<integer> | 否 | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| `data.productAttributeRules` | array<object> | 否 | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `data.productAttributeRules[].pid` | integer | 否 | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `data.productAttributeRules[].templatePid` | integer | 否 | 模板属性ID，用于关联模板中的属性定义 |
| `data.productAttributeRules[].refPid` | integer | 否 | 引用属性ID，表示该属性引用自哪个基础属性 |
| `data.productAttributeRules[].name` | string | 否 | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `data.productAttributeRules[].lang2Name` | string | 否 | 第二语言属性名称 |
| `data.productAttributeRules[].isSale` | boolean | 否 | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `data.productAttributeRules[].mainSale` | boolean | 否 | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `data.productAttributeRules[].required` | boolean | 否 | 是否必填，为true时创建产品必须填写该属性 |
| `data.productAttributeRules[].valueType` | string | 否 | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `data.productAttributeRules[].controlType` | integer | 否 | 控件类型，决定前端展示方式 |
| `data.productAttributeRules[].feature` | integer | 否 | 特征标记 |
| `data.productAttributeRules[].chooseMaxNum` | integer | 否 | 最多可选数量，SELECT类型时最多可选几个value |
| `data.productAttributeRules[].inputMaxNum` | integer | 否 | 输入最大数量，自定义输入的规格上限 |
| `data.productAttributeRules[].minValue` | string | 否 | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `data.productAttributeRules[].maxValue` | string | 否 | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `data.productAttributeRules[].valuePrecision` | integer | 否 | 小数精度，数值保留几位小数 |
| `data.productAttributeRules[].valueUnit` | array<string> | 否 | 合法单位列表，输入时必须使用列表中的单位 |
| `data.productAttributeRules[].valueRule` | integer | 否 | 值规则 |
| `data.productAttributeRules[].propertyValueType` | integer | 否 | 属性值类型 |
| `data.productAttributeRules[].parentSpecId` | integer | 否 | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `data.productAttributeRules[].parentTemplatePid` | integer | 否 | 父模板属性ID |
| `data.productAttributeRules[].templatePropertyValueParentList` | array<object> | 否 | 父属性值模板ID列表，非string类型属性时使用 |
| `data.productAttributeRules[].templatePropertyValueParentList[].parentVidList` | array<integer> | 否 | 父属性值ID列表 |
| `data.productAttributeRules[].showCondition` | array<object> | 否 | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `data.productAttributeRules[].showCondition[].parentRefPid` | integer | 否 | 父引用属性ID |
| `data.productAttributeRules[].showCondition[].parentVids` | array<integer> | 否 | 父属性值ID列表 |
| `data.productAttributeRules[].showType` | integer | 否 | 展示类型 |
| `data.productAttributeRules[].propertyChooseTitle` | string | 否 | 属性选择标题，SELECT类型时的选择提示文字 |
| `data.productAttributeRules[].numberInputTitle` | string | 否 | 数字输入标题，INPUT类型时的输入提示文字 |
| `data.productAttributeRules[].referenceType` | integer | 否 | 引用类型 |
| `data.productAttributeRules[].valueInputSum` | integer | 否 | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `data.productAttributeRules[].values` | array<object> | 否 | 可选值列表，SELECT类型时从中选取vid和name |
| `data.productAttributeRules[].values[].specId` | integer | 否 | 规格ID，自定义输入的值为null |
| `data.productAttributeRules[].values[].vid` | integer | 否 | 属性值ID，填写属性时通过vid指定选中的值 |
| `data.productAttributeRules[].values[].name` | string | 否 | 属性值名称，如"白色"、"XL"、"棉" |
| `data.productAttributeRules[].values[].lang2Value` | string | 否 | 第二语言值 |
| `data.productAttributeRules[].values[].extendInfo` | string | 否 | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `data.productAttributeRules[].values[].group` | object | 否 | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `data.productAttributeRules[].values[].parentVidList` | array<integer> | 否 | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| `data.isSupportBasePlateCategory` | boolean | 否 | 是否支持底版/套版，为true时创建产品可设置isBasePlate |
| `data.requiredSizeTemplate` | boolean | 否 | 尺码模板是否必填，为true时创建产品必须传sizeCharts |
| `data.requiredGoodsModel` | boolean | 否 | 模特信息是否必填，为true时创建产品必须传goodsModelReqs |
| `data.requiredSizeChart` | boolean | 否 | 尺码表是否必填 |
| `data.inputMaxSpecNum` | integer | 否 | 自定义规格数量上限，saleAttributes中自定义输入的规格不能超过此值 0则不限制 |
| `data.isShoesClass` | boolean | 否 | 是否鞋类类目，为true时尺码表需按鞋码规则填写 |


<details><summary>请求示例</summary>

```json
{
  "cid": 1,
  "shopIds": [
    1
  ]
}
```
</details>

---

### 获取商品基本选项

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_item_options`
- 类型：读
- 原文：[471545321e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545321e0.md)（本地 raw/471545321e0_获取商品基本选项.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.outerPackageShapeOptions` | array<object> | 否 | 外包装形状选项，key/value 数组，保存到 outerPackageShape |
| `data.outerPackageShapeOptions[].key` | integer | 否 | 选项键值 |
| `data.outerPackageShapeOptions[].value` | string | 否 | 选项显示文本 |
| `data.outerPackageTypeOptions` | array<object> | 否 | 外包装类型选项，key/value 数组，保存到 outerPackageType |
| `data.outerPackageTypeOptions[].key` | integer | 否 | 选项键值 |
| `data.outerPackageTypeOptions[].value` | string | 否 | 选项显示文本 |
| `data.goodsModelTryOnResultMap` | array<object> | 否 | 模特试穿结果枚举，格式为 [{key: modelType, value: {tryOnResult: label}}]。 保存时按 modelType 取对应枚举，将所选 tryOnResult 填入 goodsModelReqs[].tryOnResult |
| `data.goodsModelTryOnResultMap[].key` | integer | 否 | 模特类型（modelType） |
| `data.goodsModelTryOnResultMap[].value` | object | 否 | 试穿结果枚举映射，key 为 tryOnResult，value 为显示文本 |
| `data.catIdAndProductNameMaxLengthMap` | object | 否 | 类目标题最大长度映射，key 为 cid，value 为最大字符数 |
| `data.suggestedPriceCurrencyTypeAndNameList` | array<object> | 否 | 建议售价币种列表，key/value 数组，保存到 skuMap[key].suggestedPriceCurrencyType |
| `data.suggestedPriceCurrencyTypeAndNameList[].key` | string | 否 | 选项键值 |
| `data.suggestedPriceCurrencyTypeAndNameList[].value` | string | 否 | 选项显示文本 |
| `data.skuClassificationList` | array<object> | 否 | SKU 分类类型，key/value 数组，保存到 skuMap[key].skuClassification。 1=单品（numberOfPieces 只能为1）；2=同款多件装（numberOfPieces 必须>1）； 3=混合套装（需额外填写 individuallyPacked 和 productSkuAccessories）。 部分类目此字段必填 |
| `data.skuClassificationList[].key` | integer | 否 | 选项键值 |
| `data.skuClassificationList[].value` | string | 否 | 选项显示文本 |
| `data.skuPieceUnitCodeList` | array<object> | 否 | 件数单位，key/value 数组，保存到 skuMap[key].pieceUnitCode。部分类目必填 |
| `data.skuPieceUnitCodeList[].key` | integer | 否 | 选项键值 |
| `data.skuPieceUnitCodeList[].value` | string | 否 | 选项显示文本 |
| `data.individuallyPackedList` | array<object> | 否 | 是否独立包装，key/value 数组，保存到 skuMap[key].individuallyPacked。 skuClassification 为2或3时必填 |
| `data.individuallyPackedList[].key` | integer | 否 | 选项键值 |
| `data.individuallyPackedList[].value` | string | 否 | 选项显示文本 |
| `data.packageLimitConfig` | object | 否 | 包装限制配置 |
| `data.descModuleLimitConfig` | object | 否 | 描述模块限制配置，包含 descModuleMaxTextLength（最大文本长度） |
| `data.netContentCidList` | array<integer> | 否 | 需要填写净含量的类目 cid 列表。 当商品 cid 在此列表中，skuClassification 为1或2时需填 netContentNumber/netContentUnitCode（取值见 netContentOptions）； skuClassification 为3时需填 totalNetContentNumber/totalNetContentUnitCode |
| `data.netContentOptions` | array<object> | 否 | 净含量单位选项，key/value 数组，保存到 skuMap[key].netContentUnitCode |
| `data.netContentOptions[].key` | integer | 否 | 选项键值 |
| `data.netContentOptions[].value` | string | 否 | 选项显示文本 |
| `data.enTitleRefTypeList` | array<object> | 否 | 英文标题参考类型选项 |
| `data.enTitleRefTypeList[].key` | string | 否 | 选项键值 |
| `data.enTitleRefTypeList[].value` | string | 否 | 选项显示文本 |
| `data.pieceNewUnitCodeList` | array<object> | 否 | 共计内含单位选项，key/value 数组，保存到 skuMap[key].pieceNewUnitCode |
| `data.pieceNewUnitCodeList[].key` | integer | 否 | 选项键值 |
| `data.pieceNewUnitCodeList[].value` | string | 否 | 选项显示文本 |
| `data.mixTypeList` | array<object> | 否 | 混合套装类型选项，key/value 数组，保存到 skuMap[key].mixedType。1=不同品，2=同品不同规格 |
| `data.mixTypeList[].key` | integer | 否 | 选项键值 |
| `data.mixTypeList[].value` | string | 否 | 选项显示文本 |
| `data.totalNetContentCidList` | array<integer> | 否 | 需要填写总净含量的类目 cid 列表（混合套装场景） |
| `data.vehicleLibraryRequiredCidList` | array<integer> | 否 | 需要填写车型库信息的类目 cid 列表 |
| `data.saleAttributeClothingColorMaxNum` | integer | 否 | 销售属性颜色最大数量 |
| `data.sizTypeAndSizeTypeNameMap` | object | 否 | 尺码类型映射 |


---

### 创建采集箱商品

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/create_collect_box_item`
- 类型：写
- 原文：[471545322e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545322e0.md)（本地 raw/471545322e0_创建采集箱商品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 SiteCollectItemInfoForSaveRo 注释。 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 保存时会校验每个店铺的存在性、运费模板、仓库配置； 每个子项的 shopId 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.itemNum` | string | 否 | 货号 |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> | 否 | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版，2=套版） |
| `siteCollectItemInfo.basePlateSkuKey` | string | 否 | 底版 SKU Key |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状，取值参考 getItemOptions 接口返回的 outerPackageShapeOptions |
| `siteCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型，取值参考 getItemOptions 接口返回的 outerPackageTypeOptions |
| `siteCollectItemInfo.outerPackageImgUrls` | array<string> | 是 | 外包装图片URL列表 |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
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
| `siteCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<string> | 否 | 展示尺码模板ID列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写 |
| `siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 创建成功的采集箱详情ID |


---

### 认领预发布店铺

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/claim_to_shop`
- 类型：写
- 原文：[471545323e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545323e0.md)（本地 raw/471545323e0_认领预发布店铺.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取采集箱店铺模式详情

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_shop_collect_item_info`
- 类型：读
- 原文：[471545324e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545324e0.md)（本地 raw/471545324e0_获取采集箱店铺模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |
| `cid` | integer | 否 | 新类目id（需要切换类目时填写新的cid，可以快速匹配相同属性，需要保存才能生效新的类目） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array<integer> | 否 | 已认领的店铺IDS |
| `data.shopCollectItemInfo` | object | 否 | 店铺模式数据 |
| `data.shopCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.shopCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表 |
| `data.shopCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.shopCollectItemInfo.saleAttributes[].pid` | integer | 否 | 基础属性id |
| `data.shopCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 属性id |
| `data.shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 否 | 父规格ID |
| `data.shopCollectItemInfo.saleAttributes[].name` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `data.shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识码 |
| `data.shopCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `data.shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类货号（服饰类的货号是SKC级别的） |
| `data.shopCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（成分/材质等） |
| `data.shopCollectItemInfo.attributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.shopCollectItemInfo.attributes[].pid` | integer | 否 | 基础属性id |
| `data.shopCollectItemInfo.attributes[].refPid` | integer | 否 | 属性id |
| `data.shopCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.attributes[].values` | array<object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.attributes[].values[].vid` | integer | 否 | 属性值id |
| `data.shopCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位 |
| `data.shopCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例(所有成分比例之和需等于100) |
| `data.shopCollectItemInfo.skuMap` | object | 否 | SKU映射（key=SKU标识码，value=SKU条目） |
| `data.shopCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 否 | 尺码模板来源 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 否 | 元素ID列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 否 | 尺码项列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 否 | 尺码名称 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 否 | 元素值列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 否 | 分组值列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与值映射 |
| `data.shopCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 否 | 尺码模板唯一ID |
| `data.shopCollectItemInfo.imgUrls` | array<string> | 否 | 商品图片URL列表 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 否 | 产品描述 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `data.shopCollectItemInfo.outerPackageShape` | integer | 否 | 外包装形状 |
| `data.shopCollectItemInfo.outerPackageType` | integer | 否 | 外包装类型 |
| `data.shopCollectItemInfo.outerPackageImgUrls` | array<string> | 否 | 外包装图片URL列表 |
| `data.shopCollectItemInfo.productOriginCountry` | string | 否 | 原产国 |
| `data.shopCollectItemInfo.productOriginProvince` | string | 否 | 原产省 |
| `data.shopCollectItemInfo.currency` | string | 否 | 币种 |
| `data.shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.shopCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图平台视频ID |
| `data.shopCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.shopCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `data.shopCollectItemInfo.goodsModelReqs` | array<object> | 否 | 模特信息列表 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelId` | string | 否 | 模特ID |
| `data.shopCollectItemInfo.goodsModelReqs[].shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.goodsModelReqs[].modelName` | string | 否 | 模特名称 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelType` | string | 否 | 模特类型 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 否 | 模特图片URL |
| `data.shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 否 | 身高（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 否 | 试穿尺码规格名称 |
| `data.shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 否 | 试穿结果 |
| `data.shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 否 | 尺码规格ID |
| `data.shopCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `data.shopCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.shopCollectItemInfo.site` | string | 否 | 站点 |
| `data.shopCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `data.shopCollectItemInfo.isBasePlate` | integer | 否 | 是否底版 |
| `data.shopCollectItemInfo.detailId` | string | 否 | 详情ID |
| `data.shopCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车辆库关联列表 |
| `data.shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 否 | 车型库站点ID |
| `data.shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 否 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `data.shopCollectItemInfo.collectShowSizeTemplateIds` | array<integer> | 否 | 采集展示尺码模板ID列表 |
| `data.shopCollectItemInfo.sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点 |


---

### 保存采集箱店铺模式详情

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/save_shop_collect_item_info`
- 类型：写
- 原文：[471545325e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545325e0.md)（本地 raw/471545325e0_保存采集箱店铺模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.detailId` | integer | 是 | 采集箱详情ID |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `shopCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `shopCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer | 否 | 字体大小 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string | 否 | 字体粗细 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string | 否 | 对齐方式 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string | 否 | 字体颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string | 否 | 背景颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer | 否 | 字体族 |
| `shopCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `shopCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `shopCollectItemInfo.productOriginCertFiles` | array<object> | 否 | 原产地认证文件列表 |
| `shopCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `shopCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `shopCollectItemInfo.currency` | string | 否 | 店铺币种 |
| `shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `shopCollectItemInfo.productGuideFileUrl` | string | 否 | 产品说明书URL |
| `shopCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名 |
| `shopCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状 |
| `shopCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型 |
| `shopCollectItemInfo.outerPackageImgUrls` | array<string> | 是 | 外包装图片URL列表 |
| `shopCollectItemInfo.site` | string | 否 | 站点（temu全托 目前只有PDDKJ） |
| `shopCollectItemInfo.editModel` | string | 是 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `shopCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版 2=套版） |
| `shopCollectItemInfo.basePlateSkuKey` | string | 否 | 底板SKU Key |
| `shopCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `shopCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `shopCollectItemInfo.translateLanguages` | array<string> | 否 | 说明书需翻译语言列表 |
| `shopCollectItemInfo.goodsModelReqs` | array<object> | 否 | 模特信息列表。requiredGoodsModel 为 true 的类目必填。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举 |
| `shopCollectItemInfo.goodsModelReqs[].modelId` | string | 是 | 模特ID |
| `shopCollectItemInfo.goodsModelReqs[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.goodsModelReqs[].modelName` | string | 是 | 模特名称 |
| `shopCollectItemInfo.goodsModelReqs[].modelType` | string | 是 | 模特类型 |
| `shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 是 | 模特图片URL |
| `shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 是 | 身高（cm） |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 是 | 试穿尺码规格名称 |
| `shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 是 | 试穿结果 |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 是 | 尺码规格ID |
| `shopCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `shopCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表 |
| `shopCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `shopCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `shopCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `shopCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `shopCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图（服饰类必填） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `shopCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表 |
| `shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取采集箱站点模式详情

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[471545326e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545326e0.md)（本地 raw/471545326e0_获取采集箱站点模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array<integer> | 否 | 已认领的店铺IDS |
| `data.siteCollectItemInfo` | object | 否 | 站点模式数据 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.siteCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表 |
| `data.siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 基础属性id |
| `data.siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 属性id |
| `data.siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 否 | 父规格ID |
| `data.siteCollectItemInfo.saleAttributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `data.siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识码 |
| `data.siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `data.siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类货号（服饰类的货号是SKC级别的） |
| `data.siteCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（成分/材质等） |
| `data.siteCollectItemInfo.attributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.siteCollectItemInfo.attributes[].pid` | integer | 否 | 基础属性id |
| `data.siteCollectItemInfo.attributes[].refPid` | integer | 否 | 属性id |
| `data.siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.attributes[].values` | array<object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.attributes[].values[].vid` | integer | 否 | 属性值id |
| `data.siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位 |
| `data.siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例(所有成分比例之和需等于100) |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射（key=SKU标识码，value=SKU条目） |
| `data.siteCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 否 | 尺码模板来源 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 否 | 元素ID列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 否 | 尺码项列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 否 | 尺码名称 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 否 | 元素值列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 否 | 分组值列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与值映射 |
| `data.siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 否 | 尺码模板唯一ID |
| `data.siteCollectItemInfo.imgUrls` | array<string> | 否 | 商品图片URL列表 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 否 | 产品描述 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `data.siteCollectItemInfo.outerPackageShape` | integer | 否 | 外包装形状 |
| `data.siteCollectItemInfo.outerPackageType` | integer | 否 | 外包装类型 |
| `data.siteCollectItemInfo.outerPackageImgUrls` | array<string> | 否 | 外包装图片URL列表 |
| `data.siteCollectItemInfo.productOriginCountry` | string | 否 | 原产国 |
| `data.siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省 |
| `data.siteCollectItemInfo.currency` | string | 否 | 币种 |
| `data.siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图平台视频ID |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `data.siteCollectItemInfo.goodsModelReqs` | array<object> | 否 | 模特信息列表 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelId` | string | 否 | 模特ID |
| `data.siteCollectItemInfo.goodsModelReqs[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.goodsModelReqs[].modelName` | string | 否 | 模特名称 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelType` | string | 否 | 模特类型 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 否 | 模特图片URL |
| `data.siteCollectItemInfo.goodsModelReqs[].modelHeight` | string | 否 | 身高（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 否 | 试穿尺码规格名称 |
| `data.siteCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 否 | 试穿结果 |
| `data.siteCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 否 | 尺码规格ID |
| `data.siteCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `data.siteCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `data.siteCollectItemInfo.isBasePlate` | integer | 否 | 是否底版 |
| `data.siteCollectItemInfo.detailId` | string | 否 | 详情ID |
| `data.siteCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车辆库关联列表 |
| `data.siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 否 | 车型库站点ID |
| `data.siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 否 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `data.siteCollectItemInfo.collectShowSizeTemplateIds` | array<integer> | 否 | 采集展示尺码模板ID列表 |
| `data.siteCollectItemInfo.sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 否 | 店铺列表，保存站点模式必填。 保存时会校验每个店铺的存在性、运费模板、仓库配置； 每个子项的 shopId 必填 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `data.siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点 |


---

### 保存采集箱站点模式详情

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/save_site_collect_item_info`
- 类型：写
- 原文：[471545327e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545327e0.md)（本地 raw/471545327e0_保存采集箱站点模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 保存时会校验每个店铺的存在性、运费模板、仓库配置； 每个子项的 shopId 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.itemNum` | string | 否 | 货号 |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> | 否 | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.isBasePlate` | integer | 是 | 是否底版/套版（0=无，1=底版，2=套版） |
| `siteCollectItemInfo.basePlateSkuKey` | string | 否 | 底版 SKU Key |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.outerPackageShape` | integer | 是 | 外包装形状，取值参考 getItemOptions 接口返回的 outerPackageShapeOptions |
| `siteCollectItemInfo.outerPackageType` | integer | 是 | 外包装类型，取值参考 getItemOptions 接口返回的 outerPackageTypeOptions |
| `siteCollectItemInfo.outerPackageImgUrls` | array<string> | 是 | 外包装图片URL列表 |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 是 | 类型（image=图片，text=文本） |
| `siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 是 | 内容 |
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
| `siteCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名 |
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<string> | 否 | 展示尺码模板ID列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [{"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取原产地国家列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_country_short_name_and_name_map`
- 类型：读
- 原文：[471545328e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545328e0.md)（本地 raw/471545328e0_获取原产地国家列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.countryShortNameAndNameMap` | object | 否 | 国家简码→中文名映射，key 为 shortName（如 CN），value 为中文名（如 中国大陆）。 可用于将已保存的 productOriginCountry 短码转换为可读名称展示 |
| `data.productOriginCountries` | array<object> | 否 | 完整国家列表，用于渲染原产地下拉选择器。 选择某个国家后将其 shortName 填入 productOriginCountry； 选择中国（shortName=CN）时，还需从 province 列表中选择省份，将省份 code 填入 productOriginProvince |
| `data.productOriginCountries[].code` | string | 否 | 国家编码（如 43） |
| `data.productOriginCountries[].name` | string | 否 | 英文名 |
| `data.productOriginCountries[].shortName` | string | 否 | 国家简码，填入 productOriginCountry（如 CN、US） |
| `data.productOriginCountries[].chineseName` | string | 否 | 中文名 |
| `data.productOriginCountries[].province` | array<object> | 否 | 省份列表，仅原产国为 CN 时有值。 选择中国后需从此列表选择省份，将省份 code 填入 productOriginProvince |
| `data.productOriginCountries[].province[].code` | string | 否 | 省份编码，原产国为 CN 时填入 productOriginProvince |
| `data.productOriginCountries[].province[].name` | string | 否 | 英文名 |
| `data.productOriginCountries[].province[].chineseName` | string | 否 | 中文名 |


---

### 店铺模特列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/search_model_list`
- 类型：读
- 原文：[471545329e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545329e0.md)（本地 raw/471545329e0_店铺模特列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模） |
| `modelName` | string | 否 | 模特名称模糊搜索 |
| `pageNo` | integer | 否 | 页码，默认1 |
| `pageSize` | integer | 否 | 每页条数，默认20 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.modelList` | array<object> | 否 | 模特列表，用户从中选择模特绑定到商品。 选择后需额外选择试穿尺码（sizeSpecId/sizeSpecName）和试穿结果（tryOnResult）， 将各字段对应填入 goodsModelReqs 后提交保存。部分类目必填 requiredGoodsModel 为 true。 |
| `data.modelList[].pddkjShopModelId` | integer | 否 | 店铺模特记录ID |
| `data.modelList[].shopId` | integer | 否 | 店铺ID |
| `data.modelList[].platformModelId` | integer | 否 | 平台模特ID，保存时填入 goodsModelReqs.modelId |
| `data.modelList[].headPortrait` | string | 否 | 头像URL，保存时填入 goodsModelReqs.modelProfileUrl |
| `data.modelList[].modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模），保存时填入 goodsModelReqs.modelType |
| `data.modelList[].canEdit` | integer | 否 | 是否可编辑（1=可编辑，0=不可编辑） |
| `data.modelList[].modelName` | string | 否 | 模特名称，保存时填入 goodsModelReqs.modelName |
| `data.modelList[].hipline` | string | 否 | 臀围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHip |
| `data.modelList[].bust` | string | 否 | 胸围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelBust |
| `data.modelList[].height` | string | 否 | 身高（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHeight |
| `data.modelList[].waist` | string | 否 | 腰围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelWaist |
| `data.modelList[].footLength` | string | 否 | 脚长（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootLength |
| `data.modelList[].footWidth` | string | 否 | 脚宽（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootWidth |
| `data.total` | integer | 否 | 总数 |


---

### 获取类目列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[471545330e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545330e0.md)（本地 raw/471545330e0_获取类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cateTree` | object | 否 | 分类树 Map（key=cid, value=分类节点） |


---

### 获取尺码模板列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_size_template_list`
- 类型：读
- 原文：[471545331e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545331e0.md)（本地 raw/471545331e0_获取尺码模板列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `isRsync` | integer | 否 | 是否同步 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeTemplateList` | array<object> | 否 | 尺码表模板列表，先选择一个模板，再取其sizeTemplateId调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `data.sizeTemplateList[].sizeTemplateId` | string | 否 | 尺码表模板ID，用于调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `data.sizeTemplateList[].name` | string | 否 | 模板名称 |
| `data.sizeTemplateList[].sizeTemplateSource` | string | 否 | 模板来源 |
| `data.minSizeChartNum` | integer | 否 | 最少尺码表数量，创建产品时需要填写的尺码表数量 |
| `data.classType` | integer | 否 | 是否需要多尺码表 0否 1是 为1是 需要填写重点展示部件 collectShowSizeTemplateIds |


---

### 获取尺码表详情

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_size_charts_by_size_template_id`
- 类型：读
- 原文：[471545332e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545332e0.md)（本地 raw/471545332e0_获取尺码表详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `sizeTemplateId` | integer | 是 | 尺码表模板ID |
| `sizeTemplateSource` | string | 是 | 尺码表模板来源（api/erp 尺码表模板列表中有返回这个字段） |
| `refresh` | integer | 否 | 是否刷新 1是 0否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeTemplateId` | string | 否 | 尺码表模板ID，创建产品时sizeCharts中需传此ID |
| `data.sizeCharts` | object | 否 | 尺码表数据，创建产品时按此结构填写sizeCharts |
| `data.sizeCharts.elementIds` | array<integer> | 否 | 启用的尺码参数ID列表，必须包含sizeSpecMeta.elementList中所有necessary=true的项 |
| `data.sizeCharts.sizeItems` | array<object> | 否 | 尺码行数据，每行对应一个尺码（如S/M/L），sizeName必须与saleAttributes中的尺码值一致 |
| `data.sizeCharts.sizeItems[].sizeName` | string | 否 | 尺码名称，如"one-size"、"S"、"M"、"L"，必须与saleAttributes中尺码属性的某个值完全一致 |
| `data.sizeCharts.sizeItems[].elementValueList` | array<object> | 否 | 元素值列表 |
| `data.sizeCharts.sizeItems[].elementValueList[].elementId` | integer | 否 | 元素ID |
| `data.sizeCharts.sizeItems[].elementValueList[].elementValue` | string | 否 | 元素值 |
| `data.sizeCharts.sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与尺码名称映射 |
| `data.sizeCharts.elementIdAndIsRangeMap` | object | 否 | 参数ID是否支持范围值（如"12-13"），key为elementId，value为true表示支持范围 |
| `data.groupId` | integer | 否 | 尺码分组ID |
| `data.sizeSpecMeta` | object | 否 | 尺码规格元数据，elementList中的necessary=true项必须在sizeCharts.elementIds中包含 |
| `data.sizeSpecMeta.groupList` | array<object> | 否 | 尺码分组列表 |
| `data.sizeSpecMeta.groupList[].id` | integer | 否 | 分组ID |
| `data.sizeSpecMeta.groupList[].name` | string | 否 | 分组名称 |
| `data.sizeSpecMeta.groupList[].unnecessary` | boolean | 否 | 是否非必填 |
| `data.sizeSpecMeta.elementList` | array<object> | 否 | 所有可用的尺码参数列表，创建产品时参考此列表确定要填哪些参数，necessary=true的项必须在sizeCharts.elementIds中包含 |
| `data.sizeSpecMeta.elementList[].necessary` | boolean | 否 | 是否必填，为true时该参数必须包含在sizeCharts.elementIds中 |
| `data.sizeSpecMeta.elementList[].name` | string | 否 | 参数名称，如"胸围全围"、"衣长" |
| `data.sizeSpecMeta.elementList[].id` | integer | 否 | 参数ID，对应sizeItems中elementValueList的elementId |
| `data.sizeSpecMeta.elementList[].unit` | string | 否 | 单位，如"cm" |


---

### 获取模特分类配置

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_model_cat_info`
- 类型：读
- 原文：[471545333e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545333e0.md)（本地 raw/471545333e0_获取模特分类配置.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID，从类目选择接口获取，切换类目后传入查询该类目的模特配置 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.modelCat` | object | 否 | 模特分类配置，为 null 表示该类目不支持模特功能 enabled=1 时展示模特绑定区域，按 modelType 区分成衣模特(0)或鞋模(1)进行筛选绑定。 |
| `data.modelCat.cid` | integer | 否 | 类目ID |
| `data.modelCat.modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模），展示模特绑定区域时按此类型筛选可用模特 |
| `data.modelCat.enabled` | integer | 否 | 是否启用模特（1=启用，0=禁用），为1时展示模特绑定区域 |


---

### 获取采集箱列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[471545334e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545334e0.md)（本地 raw/471545334e0_获取采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.itemNum` | string | 否 | 商品编号 |
| `data.stock` | string | 否 | 库存 |
| `data.price` | string | 否 | 价格 |
| `data.thumbnail` | string | 否 | 缩略图 |
| `data.gmtCreate` | string | 否 | 创建时间 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.appAccountId` | string | 否 | 应用账户ID |
| `data.subAppAccountId` | string | 否 | 子应用账户ID |
| `data.platform` | string | 否 | 平台 |
| `data.title` | string | 否 | 商品标题 |
| `data.remark` | string | 否 | 备注 |
| `data.copyType` | string | 否 | 复制类型 |
| `data.collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.collectBoxDetailShopList` | array<object> | 否 | 预发布店铺信息列表 |
| `data.collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |


---

### 批量删除采集箱产品接口

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/delete_collect_box_detail`
- 类型：写
- 原文：[471545335e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545335e0.md)（本地 raw/471545335e0_批量删除采集箱产品接口.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successNum` | integer | 否 | 删除成功数量 |
| `data.failNum` | integer | 否 | 删除失败数量 |
| `data.errorMap` | object | 否 | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `data.errorMsg` | string | 否 | 拼接后的错误信息 |


---

### 获取需要设置净重的类目列表

- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_need_set_net_weight_cid_list`
- 类型：读
- 原文：[490449047e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/490449047e0.md)（本地 raw/490449047e0_获取需要设置净重的类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cidList` | array<integer> | 否 | 需要设置净重的类目列表 |


## TEMU半托采集箱>商品发布

### 发布产品

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/move_collect/save_move_collect_task`
- 类型：写
- 原文：[468726294e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726294e0.md)（本地 raw/468726294e0_发布产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |
| `shopIdAndSitesMap` | object | 是 | 需要发布的店铺shopId和站点映射 key为shopId，value为该店铺下需要发布的站点列表 示例：{"shopId值":["CA","EU"],"shopId值":["CA"]} |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


<details><summary>请求示例</summary>

```json
{
  "detailIds": [],
  "shopIdAndSitesMap": {
    "fugiatfd0": [
      "qui dolor adipisicing",
      "sunt amet quis",
      "sed"
    ]
  }
}
```
</details>

---

### 发布记录列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/move_collect/search_move_collect_list`
- 类型：读
- 原文：[511667358e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511667358e0.md)（本地 raw/511667358e0_发布记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array<object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |


## TEMU半托采集箱>车型库

### 获取车型库站点列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_list`
- 类型：读
- 原文：[468726296e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726296e0.md)（本地 raw/468726296e0_获取车型库站点列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 否 | 类目ID，区分摩托车和汽车 ，不传返回全部 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsVehicleLibrarySiteList` | array<object> | 否 | 车型库站点列表，每项代表一个销售地区的车型库（如美国、欧洲等）。 根据产品的销售地区选择对应站点，取其 vehicleLibraryId 用于后续接口 |
| `data.goodsVehicleLibrarySiteList[].vehicleLibraryId` | integer | 否 | 车型库站点ID，选定站点后传入 getGoodsVehicleLibrarySiteTopPropDependencyList 获取顶级车型节点 |
| `data.goodsVehicleLibrarySiteList[].name` | string | 否 | 站点名称，如"美国"、"欧洲"，用于展示给用户选择 |
| `data.goodsVehicleLibrarySiteList[].pid` | integer | 否 | 属性ID |
| `data.goodsVehicleLibrarySiteList[].pidName` | string | 否 | 属性名称（中文），如"品牌"、"车系" |
| `data.goodsVehicleLibrarySiteList[].pidNameEn` | string | 否 | 属性名称（英文） |
| `data.goodsVehicleLibrarySiteList[].level` | integer | 否 | 层级（1=品牌，2=车系，3=年份，4=车型，5=发动机类型） |


<details><summary>请求示例</summary>

```json
{
  "cid": 21502
}
```
</details>

---

### 获取车型库站点属性结构映射

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map`
- 类型：读
- 原文：[468726297e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726297e0.md)（本地 raw/468726297e0_获取车型库站点属性结构映射.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 否 | 类目ID，区分摩托车和汽车 ，不传返回全部 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsVehicleLibraryIdAndSitePidInfoMap` | object | 否 | 车型库站点属性结构映射，key 为 vehicleLibraryId，value 为该站点的属性层级信息列表。 用于了解某站点车型库包含哪些层级属性（品牌/车系/年款等）及其对应的 pid， 结合 getVehicleLibraryPropDependencyTree 的树形数据使用 SitePidInfo 结构： - pddkjGoodsVehicleLibraryId: string 平台商品车型库ID - vehicleLibraryId: string 车型库ID - name: string 站点名称，如"美国站、加拿大站" - pidNameEn: string 属性英文名，如"Make"、"Model"、"Year" - parentPropertyDependencyId: string 父属性依赖ID - propertyDependencyId: string 属性依赖ID - pid: string 属性pid - pidName: string 属性中文名，如"汽车品牌"、"汽车型号" - level: string 层级序号 - status: string 状态，1=启用 |


<details><summary>请求示例</summary>

```json
{
  "cid": 21502
}
```
</details>

---

### 获取站点顶级车型节点列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list`
- 类型：读
- 原文：[468726298e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726298e0.md)（本地 raw/468726298e0_获取站点顶级车型节点列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.topGoodsVehicleLibraryPropDependencyList` | array<object> | 否 | 顶级车型节点列表（通常为品牌层），每项含 propertyValueDependencyId、vidValue 等字段。 取每项的 propertyValueDependencyId 作为 topPropertyValueDependencyId， 传入 getVehicleLibraryPropDependencyTree 获取该品牌下完整的车型树 |
| `data.topGoodsVehicleLibraryPropDependencyList[].pddkjGoodsVehicleLibraryPropDependencyId` | integer | 否 | 平台车型库属性依赖ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vehicleLibraryId` | integer | 否 | 车型库ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].topPropertyValueDependencyId` | integer | 否 | 顶级节点propertyValueDependencyId |
| `data.topGoodsVehicleLibraryPropDependencyList[].parentPropertyValueDependencyId` | integer | 否 | 父节点propertyValueDependencyId，顶级节点为0 |
| `data.topGoodsVehicleLibraryPropDependencyList[].propertyValueDependencyId` | integer | 否 | 当前节点propertyValueDependencyId |
| `data.topGoodsVehicleLibraryPropDependencyList[].propertyDependencyId` | integer | 否 | 属性依赖ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vid` | integer | 否 | 属性值ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vidValue` | string | 否 | 属性值文本，如品牌名"Country Coach" |
| `data.topGoodsVehicleLibraryPropDependencyList[].level` | integer | 否 | 层级序号 |
| `data.topGoodsVehicleLibraryPropDependencyList[].isLeaf` | integer | 否 | 是否为叶子节点，0=否，1=是 |
| `data.topGoodsVehicleLibraryPropDependencyList[].md5BreadcrumbVidValue` | string | 否 | 面包屑属性值的MD5 |
| `data.topGoodsVehicleLibraryPropDependencyList[].breadcrumbVidValue` | string | 否 | 面包屑属性值文本 |
| `data.topGoodsVehicleLibraryPropDependencyList[].breadcrumbPropertyValueDependencyId` | integer | 否 | 面包屑属性值依赖ID |


---

### 获取车型属性依赖树

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_vehicle_library_prop_dependency_tree`
- 类型：读
- 原文：[468726299e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726299e0.md)（本地 raw/468726299e0_获取车型属性依赖树.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |
| `topPropertyValueDependencyId` | integer | 是 | 顶级节点ID，从 getGoodsVehicleLibrarySiteTopPropDependencyList 返回的列表中取 propertyValueDependencyId |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.vehicleLibraryPropDependencyTree` | object | 否 | 车型属性依赖树，key 为顶级节点的 propertyValueDependencyId，value 为节点数据（含 children 子节点）。 树形结构按品牌→车系→年份→车型→发动机类型逐级展开，isLeaf=1 的节点为叶子节点。 选中叶子节点后，将从根节点到该叶子节点的完整路径组装为一条车型路径， 每个路径节点取 propertyValueDependencyId、vidValue、level 填入 vehicleLibraryRelationList[].productPropValueDependencyList 中 |


---

### 根据类目ID查询有车型库数据的类目列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_has_vehicle_library_cids_by_search_cids`
- 类型：读
- 原文：[468726295e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726295e0.md)（本地 raw/468726295e0_根据类目ID查询有车型库数据的类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cids` | array<integer> | 是 | 待查询的类目ID列表，传入产品所在类目的cid， 返回结果中包含的cid表示该类目支持车型库，发品时需填写车型适配信息 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.hasVehicleLibraryCids` | array<integer> | 否 | 有车型库的类目ID列表，如果产品所属类目在此列表中， 则发品时需要填写车型适配信息（vehicleLibrary相关字段） |


## TEMU半托采集箱>采集箱

### 获取类目属性规则

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_category_attribute_rules`
- 类型：读
- 原文：[477347599e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347599e0.md)（本地 raw/477347599e0_获取类目属性规则.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopIds` | array<integer> | 否 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.saleAttributeRules` | array<object> | 否 | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `data.saleAttributeRules[].pid` | integer | 否 | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `data.saleAttributeRules[].templatePid` | integer | 否 | 模板属性ID，用于关联模板中的属性定义 |
| `data.saleAttributeRules[].refPid` | integer | 否 | 引用属性ID，表示该属性引用自哪个基础属性 |
| `data.saleAttributeRules[].name` | string | 否 | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `data.saleAttributeRules[].lang2Name` | string | 否 | 第二语言属性名称 |
| `data.saleAttributeRules[].isSale` | boolean | 否 | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `data.saleAttributeRules[].mainSale` | boolean | 否 | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `data.saleAttributeRules[].required` | boolean | 否 | 是否必填，为true时创建产品必须填写该属性 |
| `data.saleAttributeRules[].valueType` | string | 否 | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `data.saleAttributeRules[].controlType` | integer | 否 | 控件类型，决定前端展示方式 |
| `data.saleAttributeRules[].feature` | integer | 否 | 特征标记 |
| `data.saleAttributeRules[].chooseMaxNum` | integer | 否 | 最多可选数量，SELECT类型时最多可选几个value |
| `data.saleAttributeRules[].inputMaxNum` | integer | 否 | 输入最大数量，自定义输入的规格上限 |
| `data.saleAttributeRules[].minValue` | string | 否 | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `data.saleAttributeRules[].maxValue` | string | 否 | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `data.saleAttributeRules[].valuePrecision` | integer | 否 | 小数精度，数值保留几位小数 |
| `data.saleAttributeRules[].valueUnit` | array<string> | 否 | 合法单位列表，输入时必须使用列表中的单位 |
| `data.saleAttributeRules[].valueRule` | integer | 否 | 值规则 |
| `data.saleAttributeRules[].propertyValueType` | integer | 否 | 属性值类型 |
| `data.saleAttributeRules[].parentSpecId` | integer | 否 | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `data.saleAttributeRules[].parentTemplatePid` | integer | 否 | 父模板属性ID |
| `data.saleAttributeRules[].templatePropertyValueParentList` | array<object> | 否 | 父属性值模板ID列表，非string类型属性时使用 |
| `data.saleAttributeRules[].templatePropertyValueParentList[].parentVidList` | array<integer> | 否 | 父属性值ID列表 |
| `data.saleAttributeRules[].showCondition` | array<object> | 否 | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `data.saleAttributeRules[].showCondition[].parentRefPid` | integer | 否 | 父引用属性ID |
| `data.saleAttributeRules[].showCondition[].parentVids` | array<integer> | 否 | 父属性值ID列表 |
| `data.saleAttributeRules[].showType` | integer | 否 | 展示类型 |
| `data.saleAttributeRules[].propertyChooseTitle` | string | 否 | 属性选择标题，SELECT类型时的选择提示文字 |
| `data.saleAttributeRules[].numberInputTitle` | string | 否 | 数字输入标题，INPUT类型时的输入提示文字 |
| `data.saleAttributeRules[].referenceType` | integer | 否 | 引用类型 |
| `data.saleAttributeRules[].valueInputSum` | integer | 否 | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `data.saleAttributeRules[].values` | array<object> | 否 | 可选值列表，SELECT类型时从中选取vid和name |
| `data.saleAttributeRules[].values[].specId` | integer | 否 | 规格ID，自定义输入的值为null |
| `data.saleAttributeRules[].values[].vid` | integer | 否 | 属性值ID，填写属性时通过vid指定选中的值 |
| `data.saleAttributeRules[].values[].name` | string | 否 | 属性值名称，如"白色"、"XL"、"棉" |
| `data.saleAttributeRules[].values[].lang2Value` | string | 否 | 第二语言值 |
| `data.saleAttributeRules[].values[].extendInfo` | string | 否 | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `data.saleAttributeRules[].values[].group` | object | 否 | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `data.saleAttributeRules[].values[].parentVidList` | array<integer> | 否 | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| `data.productAttributeRules` | array<object> | 否 | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `data.productAttributeRules[].pid` | integer | 否 | 属性ID，填写attributes/saleAttributes时通过pid指定属性 |
| `data.productAttributeRules[].templatePid` | integer | 否 | 模板属性ID，用于关联模板中的属性定义 |
| `data.productAttributeRules[].refPid` | integer | 否 | 引用属性ID，表示该属性引用自哪个基础属性 |
| `data.productAttributeRules[].name` | string | 否 | 属性名称，如"颜色"、"尺码"、"材质成分" |
| `data.productAttributeRules[].lang2Name` | string | 否 | 第二语言属性名称 |
| `data.productAttributeRules[].isSale` | boolean | 否 | 是否销售属性，true时该属性属于saleAttributes，false时属于attributes |
| `data.productAttributeRules[].mainSale` | boolean | 否 | 是否主销售属性，为true时该属性对应SKU图片，需填写skuMap中每个skuKey的图片 |
| `data.productAttributeRules[].required` | boolean | 否 | 是否必填，为true时创建产品必须填写该属性 |
| `data.productAttributeRules[].valueType` | string | 否 | 值类型：SELECT(从values中选择)、INPUT(自由输入)、TABLE(表格输入，如成分) |
| `data.productAttributeRules[].controlType` | integer | 否 | 控件类型，决定前端展示方式 |
| `data.productAttributeRules[].feature` | integer | 否 | 特征标记 |
| `data.productAttributeRules[].chooseMaxNum` | integer | 否 | 最多可选数量，SELECT类型时最多可选几个value |
| `data.productAttributeRules[].inputMaxNum` | integer | 否 | 输入最大数量，自定义输入的规格上限 |
| `data.productAttributeRules[].minValue` | string | 否 | 数字最小值，TABLE/INPUT类型时数值不能小于此值 |
| `data.productAttributeRules[].maxValue` | string | 否 | 数字最大值，TABLE/INPUT类型时数值不能大于此值 |
| `data.productAttributeRules[].valuePrecision` | integer | 否 | 小数精度，数值保留几位小数 |
| `data.productAttributeRules[].valueUnit` | array<string> | 否 | 合法单位列表，输入时必须使用列表中的单位 |
| `data.productAttributeRules[].valueRule` | integer | 否 | 值规则 |
| `data.productAttributeRules[].propertyValueType` | integer | 否 | 属性值类型 |
| `data.productAttributeRules[].parentSpecId` | integer | 否 | 父规格ID，存在时表示该属性依赖父属性的某个值 |
| `data.productAttributeRules[].parentTemplatePid` | integer | 否 | 父模板属性ID |
| `data.productAttributeRules[].templatePropertyValueParentList` | array<object> | 否 | 父属性值模板ID列表，非string类型属性时使用 |
| `data.productAttributeRules[].templatePropertyValueParentList[].parentVidList` | array<integer> | 否 | 父属性值ID列表 |
| `data.productAttributeRules[].showCondition` | array<object> | 否 | 显示条件，string类型属性时使用，满足条件时该属性才需要填写 |
| `data.productAttributeRules[].showCondition[].parentRefPid` | integer | 否 | 父引用属性ID |
| `data.productAttributeRules[].showCondition[].parentVids` | array<integer> | 否 | 父属性值ID列表 |
| `data.productAttributeRules[].showType` | integer | 否 | 展示类型 |
| `data.productAttributeRules[].propertyChooseTitle` | string | 否 | 属性选择标题，SELECT类型时的选择提示文字 |
| `data.productAttributeRules[].numberInputTitle` | string | 否 | 数字输入标题，INPUT类型时的输入提示文字 |
| `data.productAttributeRules[].referenceType` | integer | 否 | 引用类型 |
| `data.productAttributeRules[].valueInputSum` | integer | 否 | 值输入总和，TABLE类型时各值之和必须等于此值（如成分总和=100） |
| `data.productAttributeRules[].values` | array<object> | 否 | 可选值列表，SELECT类型时从中选取vid和name |
| `data.productAttributeRules[].values[].specId` | integer | 否 | 规格ID，自定义输入的值为null |
| `data.productAttributeRules[].values[].vid` | integer | 否 | 属性值ID，填写属性时通过vid指定选中的值 |
| `data.productAttributeRules[].values[].name` | string | 否 | 属性值名称，如"白色"、"XL"、"棉" |
| `data.productAttributeRules[].values[].lang2Value` | string | 否 | 第二语言值 |
| `data.productAttributeRules[].values[].extendInfo` | string | 否 | 扩展信息，如颜色属性的RGB值"(255,255,255,1)" |
| `data.productAttributeRules[].values[].group` | object | 否 | 值分组，含id和name，用于将值按组分类展示（如颜色按色系分组） |
| `data.productAttributeRules[].values[].parentVidList` | array<integer> | 否 | 父属性值ID列表，存在时表示该值依赖父属性的某个选项 |
| `data.isSupportBasePlateCategory` | boolean | 否 | 是否支持底版/套版，为true时创建产品可设置isBasePlate |
| `data.requiredSizeTemplate` | boolean | 否 | 尺码模板是否必填，为true时创建产品必须传sizeCharts |
| `data.requiredGoodsModel` | boolean | 否 | 模特信息是否必填，为true时创建产品必须传goodsModelReqs |
| `data.requiredSizeChart` | boolean | 否 | 尺码表是否必填 |
| `data.inputMaxSpecNum` | integer | 否 | 自定义规格数量上限，saleAttributes中自定义输入的规格不能超过此值 0则不限制 |
| `data.isShoesClass` | boolean | 否 | 是否鞋类类目，为true时尺码表需按鞋码规则填写 |
| `data.sizeAttributeGroupList` | array<object> | 否 | 尺码属性值组列表，pddkjChoice 独有字段，用于站点维度的尺码属性配置 |
| `data.sizeAttributeGroupList[].id` | integer | 否 | 尺码属性组ID |
| `data.sizeAttributeGroupList[].name` | string | 否 | 尺码属性组名称，如"英码"、"美码" |


<details><summary>请求示例</summary>

```json
{
  "cid": 1,
  "shopIds": [
    1
  ]
}
```
</details>

---

### 店铺模特列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/search_model_list`
- 类型：读
- 原文：[477347600e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347600e0.md)（本地 raw/477347600e0_店铺模特列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模） |
| `modelName` | string | 否 | 模特名称模糊搜索 |
| `pageNo` | integer | 否 | 页码，默认1 |
| `pageSize` | integer | 否 | 每页条数，默认20 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.modelList` | array<object> | 否 | 模特列表，用户从中选择模特绑定到商品。 选择后需额外选择试穿尺码（sizeSpecId/sizeSpecName）和试穿结果（tryOnResult）， 将各字段对应填入 goodsModelReqs 后提交保存。部分类目必填 requiredGoodsModel 为 true。 |
| `data.modelList[].pddkjChoiceShopModelId` | integer | 否 | 店铺模特记录ID |
| `data.modelList[].shopId` | integer | 否 | 店铺ID |
| `data.modelList[].platformModelId` | integer | 否 | 平台模特ID，保存时填入 goodsModelReqs.modelId |
| `data.modelList[].headPortrait` | string | 否 | 头像URL，保存时填入 goodsModelReqs.modelProfileUrl |
| `data.modelList[].modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模），保存时填入 goodsModelReqs.modelType |
| `data.modelList[].canEdit` | integer | 否 | 是否可编辑（1=可编辑，0=不可编辑） |
| `data.modelList[].modelName` | string | 否 | 模特名称，保存时填入 goodsModelReqs.modelName |
| `data.modelList[].hipline` | string | 否 | 臀围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHip |
| `data.modelList[].bust` | string | 否 | 胸围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelBust |
| `data.modelList[].height` | string | 否 | 身高（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelHeight |
| `data.modelList[].waist` | string | 否 | 腰围（cm），modelType=0 时有值，保存时填入 goodsModelReqs.modelWaist |
| `data.modelList[].footLength` | string | 否 | 脚长（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootLength |
| `data.modelList[].footWidth` | string | 否 | 脚宽（cm），modelType=1 时有值，保存时填入 goodsModelReqs.modelFootWidth |
| `data.total` | integer | 否 | 总数 |


---

### 获取商品基本选项

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_item_options`
- 类型：读
- 原文：[477347601e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347601e0.md)（本地 raw/477347601e0_获取商品基本选项.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.outerPackageShapeOptions` | array<object> | 否 | 外包装形状选项，key/value 数组，保存到 outerPackageShape |
| `data.outerPackageShapeOptions[].key` | integer | 否 | 选项键值 |
| `data.outerPackageShapeOptions[].value` | string | 否 | 选项显示文本 |
| `data.outerPackageTypeOptions` | array<object> | 否 | 外包装类型选项，key/value 数组，保存到 outerPackageType |
| `data.outerPackageTypeOptions[].key` | integer | 否 | 选项键值 |
| `data.outerPackageTypeOptions[].value` | string | 否 | 选项显示文本 |
| `data.goodsModelTryOnResultMap` | array<object> | 否 | 模特试穿结果枚举，格式为 [{key: modelType, value: {tryOnResult: label}}]。 保存时按 modelType 取对应枚举，将所选 tryOnResult 填入 goodsModelReqs[].tryOnResult |
| `data.goodsModelTryOnResultMap[].key` | integer | 否 | 模特类型（modelType） |
| `data.goodsModelTryOnResultMap[].value` | object | 否 | 试穿结果枚举映射，key 为 tryOnResult，value 为显示文本 |
| `data.catIdAndProductNameMaxLengthMap` | object | 否 | 类目标题最大长度映射，key 为 cid，value 为最大字符数 |
| `data.suggestedPriceCurrencyTypeAndNameList` | array<object> | 否 | 建议售价币种列表，key/value 数组，保存到 skuMap[key].suggestedPriceCurrencyType |
| `data.suggestedPriceCurrencyTypeAndNameList[].key` | string | 否 | 选项键值 |
| `data.suggestedPriceCurrencyTypeAndNameList[].value` | string | 否 | 选项显示文本 |
| `data.skuClassificationList` | array<object> | 否 | SKU 分类类型，key/value 数组，保存到 skuMap[key].skuClassification。 1=单品（numberOfPieces 只能为1）；2=同款多件装（numberOfPieces 必须>1）； 3=混合套装（需额外填写 individuallyPacked 和 productSkuAccessories）。 部分类目此字段必填 |
| `data.skuClassificationList[].key` | integer | 否 | 选项键值 |
| `data.skuClassificationList[].value` | string | 否 | 选项显示文本 |
| `data.skuPieceUnitCodeList` | array<object> | 否 | 件数单位，key/value 数组，保存到 skuMap[key].pieceUnitCode。部分类目必填 |
| `data.skuPieceUnitCodeList[].key` | integer | 否 | 选项键值 |
| `data.skuPieceUnitCodeList[].value` | string | 否 | 选项显示文本 |
| `data.individuallyPackedList` | array<object> | 否 | 是否独立包装，key/value 数组，保存到 skuMap[key].individuallyPacked。 skuClassification 为2或3时必填 |
| `data.individuallyPackedList[].key` | integer | 否 | 选项键值 |
| `data.individuallyPackedList[].value` | string | 否 | 选项显示文本 |
| `data.packageLimitConfig` | object | 否 | 包装限制配置 |
| `data.descModuleLimitConfig` | object | 否 | 描述模块限制配置，包含 descModuleMaxTextLength（最大文本长度） |
| `data.netContentCidList` | array<integer> | 否 | 需要填写净含量的类目 cid 列表。 当商品 cid 在此列表中，skuClassification 为1或2时需填 netContentNumber/netContentUnitCode（取值见 netContentOptions）； skuClassification 为3时需填 totalNetContentNumber/totalNetContentUnitCode |
| `data.netContentOptions` | array<object> | 否 | 净含量单位选项，key/value 数组，保存到 skuMap[key].netContentUnitCode |
| `data.netContentOptions[].key` | integer | 否 | 选项键值 |
| `data.netContentOptions[].value` | string | 否 | 选项显示文本 |
| `data.enTitleRefTypeList` | array<object> | 否 | 英文标题参考类型选项 |
| `data.enTitleRefTypeList[].key` | string | 否 | 选项键值 |
| `data.enTitleRefTypeList[].value` | string | 否 | 选项显示文本 |
| `data.pieceNewUnitCodeList` | array<object> | 否 | 共计内含单位选项，key/value 数组，保存到 skuMap[key].pieceNewUnitCode |
| `data.pieceNewUnitCodeList[].key` | integer | 否 | 选项键值 |
| `data.pieceNewUnitCodeList[].value` | string | 否 | 选项显示文本 |
| `data.mixTypeList` | array<object> | 否 | 混合套装类型选项，key/value 数组，保存到 skuMap[key].mixedType。1=不同品，2=同品不同规格 |
| `data.mixTypeList[].key` | integer | 否 | 选项键值 |
| `data.mixTypeList[].value` | string | 否 | 选项显示文本 |
| `data.totalNetContentCidList` | array<integer> | 否 | 需要填写总净含量的类目 cid 列表（混合套装场景） |
| `data.vehicleLibraryRequiredCidList` | array<integer> | 否 | 需要填写车型库信息的类目 cid 列表 |
| `data.saleAttributeClothingColorMaxNum` | integer | 否 | 销售属性颜色最大数量 |
| `data.shipmentLimitDayOptions` | array<object> | 否 | 发货限制天数选项 |
| `data.shipmentLimitDayOptions[].key` | integer | 否 | 选项键值 |
| `data.shipmentLimitDayOptions[].value` | string | 否 | 选项显示文本 |
| `data.attributeRuleGroupIdAndSizeChartsGroupIdMap` | object | 否 | 销售属性规则组ID和尺码表组ID映射 |
| `data.sizTypeAndSizeTypeNameMap` | object | 否 | 尺码类型映射 |


---

### 创建采集箱商品

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/create_collect_box_item`
- 类型：写
- 原文：[477347602e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347602e0.md)（本地 raw/477347602e0_创建采集箱商品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口。 pddkjChoice 特有：需填写 publishSiteList（发布站点）、siteAndSkuPriceMap（站点维度价格）、 siteAndWarehouseIdAndStockMap（站点+仓库库存）等 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array<string> | 否 | 发布站点列表，pddkjChoice 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array<object> | 否 | 站点仓库列表，US 站直接填 warehouseId，EU 站填 subSiteWarehouseList |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，非 EU 站点时必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array<object> | 否 | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array<object> | 否 | 站点运费模板列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguageType` | integer | 否 | 多语言素材类型 |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.translateLanguages` | array<string> | 否 | 翻译语言列表，指定需要自动翻译的目标语言编码（如 ["en","de","es"]） |
| `siteCollectItemInfo.itemNum` | string | 否 | 非服饰类主货号（skuMap 同级字段，与 skuMap 内各 SKU 的 itemNum 含义不同） |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> | 否 | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为该店铺对应的单条 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在此处独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.productMaterialImageUrl` | string | 否 | 实拍素材图URL |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
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
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<integer> | 否 | 展示尺码模板ID列表 |
| `siteCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `siteCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [ {"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `siteCollectItemInfo.publishSiteList` | array<string> | 是 | 发布站点列表，如['US','JP'] 取值参考 getPublishSiteOptions接口返回的站点列表 |
| `siteCollectItemInfo.publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.siteAndSkuPriceMap` | object | 否 | 按站点维度的 SKU 价格映射。 key 为站点编码，value 为该站点下各 SKU 的价格信息。 欧盟站点下还需填写 subSiteAndPriceMap（子站点价格），法国站点价格必填 |
| `siteCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `siteCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型，取值参考 PddkjChoiceConst |
| `siteCollectItemInfo.materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表，与 materialMultiLanguageType 配合使用， 决定哪些语言需要提供多语言图片素材 |
| `siteCollectItemInfo.discreetShipping` | string | 否 | 保密发货，0=关闭，1=开启 |
| `siteCollectItemInfo.currency` | string | 否 | 币种，如 CNY、USD |
| `siteCollectItemInfo.shipmentLimitDay` | integer | 否 | 其他站点承诺发货时效 非定制品可选值只有 1,2 |
| `siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 创建成功的采集箱详情ID |


<details><summary>请求示例</summary>

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
</details>

---

### 认领预发布店铺

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/claim_to_shop`
- 类型：写
- 原文：[477347603e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347603e0.md)（本地 raw/477347603e0_认领预发布店铺.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID（需要全量保存不在这里的店铺会被取消认领） |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取采集箱站点模式详情

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[477347606e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347606e0.md)（本地 raw/477347606e0_获取采集箱站点模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array<integer> | 否 | 已认领的店铺IDS |
| `data.siteCollectItemInfo` | object | 否 | 站点模式数据，包含商品基础信息、属性、SKU、店铺列表、发布站点等 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.siteCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表 |
| `data.siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 基础属性id |
| `data.siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 属性id |
| `data.siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 否 | 父规格ID |
| `data.siteCollectItemInfo.saleAttributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `data.siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识码 |
| `data.siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `data.siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类货号（服饰类的货号是SKC级别的） |
| `data.siteCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（成分/材质等） |
| `data.siteCollectItemInfo.attributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.siteCollectItemInfo.attributes[].pid` | integer | 否 | 基础属性id |
| `data.siteCollectItemInfo.attributes[].refPid` | integer | 否 | 属性id |
| `data.siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.attributes[].values` | array<object> | 否 | 属性值列表 |
| `data.siteCollectItemInfo.attributes[].values[].vid` | integer | 否 | 属性值id |
| `data.siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位 |
| `data.siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例(所有成分比例之和需等于100) |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射（key=SKU标识码，value=SKU条目） |
| `data.siteCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 否 | 尺码模板来源 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 否 | 元素ID列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 否 | 尺码项列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 否 | 尺码名称 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 否 | 元素值列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 否 | 分组值列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与值映射 |
| `data.siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `data.siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 否 | 尺码模板唯一ID |
| `data.siteCollectItemInfo.imgUrls` | array<string> | 否 | 商品图片URL列表 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 否 | 产品描述 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `data.siteCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `data.siteCollectItemInfo.productOriginCountry` | string | 否 | 原产国 |
| `data.siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省 |
| `data.siteCollectItemInfo.shipmentLimitDay` | integer | 否 | 发货时效（天） |
| `data.siteCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 站点维度发货时效映射，key 为站点编码，value 为发货天数 |
| `data.siteCollectItemInfo.currency` | string | 否 | 币种 |
| `data.siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.siteCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为站点编码，value 为图片URL列表 |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图平台视频ID |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `data.siteCollectItemInfo.goodsModelReqs` | array<object> | 否 | 模特信息列表 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelId` | string | 否 | 模特ID |
| `data.siteCollectItemInfo.goodsModelReqs[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.goodsModelReqs[].modelName` | string | 否 | 模特名称 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelType` | string | 否 | 模特类型 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 否 | 模特图片URL |
| `data.siteCollectItemInfo.goodsModelReqs[].modelHeight` | string | 否 | 身高（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 否 | 试穿尺码规格名称 |
| `data.siteCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 否 | 试穿结果 |
| `data.siteCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 否 | 尺码规格ID |
| `data.siteCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `data.siteCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `data.siteCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `data.siteCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.siteCollectItemInfo.publishSiteList` | array<string> | 否 | 发布站点列表 |
| `data.siteCollectItemInfo.publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表 |
| `data.siteCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型 |
| `data.siteCollectItemInfo.materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `data.siteCollectItemInfo.isBasePlate` | integer | 否 | 是否底版 |
| `data.siteCollectItemInfo.detailId` | string | 否 | 详情ID |
| `data.siteCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车辆库关联列表 |
| `data.siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 否 | 车型库站点ID |
| `data.siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 否 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `data.siteCollectItemInfo.collectShowSizeTemplateIds` | array<integer> | 否 | 采集展示尺码模板ID列表 |
| `data.siteCollectItemInfo.sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.siteCollectItemInfo.personalizationSwitch` | string | 否 | 个性化开关，0-关闭 1-开启 |
| `data.siteCollectItemInfo.discreetShipping` | string | 否 | 隐密发货 |
| `data.siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 否 | 店铺列表，站点模式关联的店铺详情列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].sizeTemplateId` | string | 否 | 尺码表模板ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array<object> | 否 | 站点运费模板列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 否 | 站点编码，如 US、EU |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 否 | 运费模板ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array<object> | 否 | 站点仓库列表 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 否 | 站点编码，如 US、EU |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | integer | 否 | 店铺ID |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，US 站直接填写 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array<object> | 否 | EU 站子站点仓库列表，US 站无此字段 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].shopName` | string | 否 | 店铺名称 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].currency` | string | 否 | 币种 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].itemNum` | string | 否 | 货号 |
| `data.siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array<string> | 否 | 发布站点列表 |
| `data.siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在 shopIdAndGoodsModelReqMap 中独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `data.siteCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点 |


---

### 保存采集箱店铺模式详情

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/save_shop_collect_item_info`
- 类型：写
- 原文：[477347605e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347605e0.md)（本地 raw/477347605e0_保存采集箱店铺模式详情.md）

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
| `shopCollectItemInfo` | object | 是 | 店铺模式数据 |
| `shopCollectItemInfo.detailId` | integer | 是 | 采集箱详情ID |
| `shopCollectItemInfo.cid` | string | 是 | 类目ID |
| `shopCollectItemInfo.shopId` | integer | 是 | 店铺ID |
| `shopCollectItemInfo.title` | string | 是 | 商品标题 |
| `shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `shopCollectItemInfo.imgUrls` | array<string> | 是 | 类轮播图 |
| `shopCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `shopCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontSize` | integer | 否 | 字体大小 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontWeight` | string | 否 | 字体粗细 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.align` | string | 否 | 对齐方式 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontColor` | string | 否 | 字体颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.backgroundColor` | string | 否 | 背景颜色 |
| `shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails.fontFamily` | integer | 否 | 字体族 |
| `shopCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `shopCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `shopCollectItemInfo.productOriginCertFiles` | array<object> | 否 | 原产地认证文件列表 |
| `shopCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `shopCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `shopCollectItemInfo.currency` | string | 否 | 店铺币种 |
| `shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `shopCollectItemInfo.productGuideFileUrl` | string | 否 | 产品说明书URL |
| `shopCollectItemInfo.productGuideFileName` | string | 否 | 产品说明书文件名 |
| `shopCollectItemInfo.site` | string | 否 | 站点（pddkjChoice 半托目前只有 sitePddKjChoice） |
| `shopCollectItemInfo.editModel` | string | 是 | 编辑模式（shop=店铺模式，site=站点模式） |
| `shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `shopCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `shopCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `shopCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `shopCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表 |
| `shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `shopCollectItemInfo.translateLanguages` | array<string> | 否 | 说明书需翻译语言列表 |
| `shopCollectItemInfo.goodsModelReqs` | array<object> | 否 | 模特信息列表。requiredGoodsModel 为 true 的类目必填。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举 |
| `shopCollectItemInfo.goodsModelReqs[].modelId` | string | 是 | 模特ID |
| `shopCollectItemInfo.goodsModelReqs[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.goodsModelReqs[].modelName` | string | 是 | 模特名称 |
| `shopCollectItemInfo.goodsModelReqs[].modelType` | string | 是 | 模特类型 |
| `shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 是 | 模特图片URL |
| `shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 是 | 身高（cm） |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 是 | 试穿尺码规格名称 |
| `shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 是 | 试穿结果 |
| `shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 是 | 尺码规格ID |
| `shopCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `shopCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表 |
| `shopCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `shopCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `shopCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `shopCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `shopCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `shopCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `shopCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `shopCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `shopCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `shopCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `shopCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `shopCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图（服饰类必填） |
| `shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `shopCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `shopCollectItemInfo.publishSiteList` | array<string> | 否 | 发布站点列表，pddkjChoice 必填，不能为空 |
| `shopCollectItemInfo.publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `shopCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `shopCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型 |
| `shopCollectItemInfo.materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表 |
| `shopCollectItemInfo.isSetSitePrice` | integer | 否 | 是否设置了站点价格 |
| `shopCollectItemInfo.isSetSiteStock` | integer | 否 | 是否设置了站点库存 |
| `shopCollectItemInfo.shipmentLimitDay` | integer | 否 | 其他站点承诺发货时效 非定制品可选值只有 1,2 |
| `shopCollectItemInfo.siteFreightTemplateList` | array<object> | 否 | 按站点维度的运费模板列表 |
| `shopCollectItemInfo.siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `shopCollectItemInfo.siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `shopCollectItemInfo.siteWarehouseList` | array<object> | 否 | 按站点维度的仓库列表，EU 站点下还包含 subSiteWarehouseList（欧盟子站点仓库列表） |
| `shopCollectItemInfo.siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `shopCollectItemInfo.siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `shopCollectItemInfo.siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，非 EU 站点时必填 |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList` | array<object> | 否 | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点区域简称列表，制造地必须包含原产国(数据通过 【获取原产地国家列表】接口获取) |
| `detailId` | integer | 是 | 采集箱详情ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取采集箱店铺模式详情

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_collect_item_info`
- 类型：读
- 原文：[477347604e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347604e0.md)（本地 raw/477347604e0_获取采集箱店铺模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |
| `shopId` | integer | 是 | 店铺ID |
| `cid` | integer | 否 | 新类目id（需要切换类目时填写新的cid，可以快速匹配相同属性，需要保存才能生效新的类目） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.claimToShopIds` | array<integer> | 否 | 已认领的店铺IDS |
| `data.shopCollectItemInfo` | object | 否 | 店铺模式数据，包含商品基础信息、属性、SKU、发布站点、仓库库存等 |
| `data.shopCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.shopCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.shopCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表 |
| `data.shopCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.shopCollectItemInfo.saleAttributes[].pid` | integer | 否 | 基础属性id |
| `data.shopCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 属性id |
| `data.shopCollectItemInfo.saleAttributes[].parentSpecId` | integer | 否 | 父规格ID |
| `data.shopCollectItemInfo.saleAttributes[].name` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `data.shopCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识码 |
| `data.shopCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图 URL列表（非服饰类没有该字段） |
| `data.shopCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类货号（服饰类的货号是SKC级别的） |
| `data.shopCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（成分/材质等） |
| `data.shopCollectItemInfo.attributes[].templatePid` | integer | 否 | 模板属性ID |
| `data.shopCollectItemInfo.attributes[].pid` | integer | 否 | 基础属性id |
| `data.shopCollectItemInfo.attributes[].refPid` | integer | 否 | 属性id |
| `data.shopCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.shopCollectItemInfo.attributes[].values` | array<object> | 否 | 属性值列表 |
| `data.shopCollectItemInfo.attributes[].values[].vid` | integer | 否 | 属性值id |
| `data.shopCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.shopCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位 |
| `data.shopCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例(所有成分比例之和需等于100) |
| `data.shopCollectItemInfo.skuMap` | object | 否 | SKU映射（key=SKU标识码，value=SKU条目） |
| `data.shopCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 否 | 尺码模板来源 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.shopCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 否 | 元素ID列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 否 | 尺码项列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 否 | 尺码名称 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 否 | 元素值列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 否 | 分组值列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与值映射 |
| `data.shopCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `data.shopCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 否 | 尺码模板唯一ID |
| `data.shopCollectItemInfo.imgUrls` | array<string> | 否 | 商品图片URL列表 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 否 | 产品描述 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].type` | string | 否 | 类型（image=图片，text=文本） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content` | object | 否 | 内容 |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.imgUrl` | string | 否 | 图片URL（type=image时使用） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.text` | string | 否 | 文本内容（type=text时使用） |
| `data.shopCollectItemInfo.goodsLayerDecorationReqs[].content.textModuleDetails` | object | 否 | 文本模块详情（type=text时使用） |
| `data.shopCollectItemInfo.productOriginCountry` | string | 否 | 原产国 |
| `data.shopCollectItemInfo.productOriginProvince` | string | 否 | 原产省 |
| `data.shopCollectItemInfo.shipmentLimitDay` | integer | 否 | 发货时效（天） |
| `data.shopCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 站点维度发货时效映射，key 为站点编码，value 为发货天数 |
| `data.shopCollectItemInfo.currency` | string | 否 | 币种 |
| `data.shopCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射 |
| `data.shopCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为站点编码，value 为图片URL列表 |
| `data.shopCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.shopCollectItemInfo.mainImgAppVideoId` | string | 否 | 主图平台视频ID |
| `data.shopCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.shopCollectItemInfo.outerGoodsUrl` | string | 否 | 外部商品链接 |
| `data.shopCollectItemInfo.goodsModelReqs` | array<object> | 否 | 模特信息列表 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelId` | string | 否 | 模特ID |
| `data.shopCollectItemInfo.goodsModelReqs[].shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.goodsModelReqs[].modelName` | string | 否 | 模特名称 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelType` | string | 否 | 模特类型 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelProfileUrl` | string | 否 | 模特图片URL |
| `data.shopCollectItemInfo.goodsModelReqs[].modelHeight` | string | 否 | 身高（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].sizeSpecName` | string | 否 | 试穿尺码规格名称 |
| `data.shopCollectItemInfo.goodsModelReqs[].tryOnResult` | string | 否 | 试穿结果 |
| `data.shopCollectItemInfo.goodsModelReqs[].sizeSpecId` | integer | 否 | 尺码规格ID |
| `data.shopCollectItemInfo.goodsModelReqs[].modelBust` | string | 否 | 胸围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelWaist` | string | 否 | 腰围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelHip` | string | 否 | 臀围（cm） |
| `data.shopCollectItemInfo.goodsModelReqs[].modelFootLength` | string | 否 | 脚长（cm），鞋类专用 |
| `data.shopCollectItemInfo.goodsModelReqs[].modelFootWidth` | string | 否 | 脚宽（cm），鞋类专用 |
| `data.shopCollectItemInfo.editModel` | string | 否 | 编辑模式 |
| `data.shopCollectItemInfo.publishSiteList` | array<string> | 否 | 发布站点列表 |
| `data.shopCollectItemInfo.publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表 |
| `data.shopCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型 |
| `data.shopCollectItemInfo.materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表 |
| `data.shopCollectItemInfo.site` | string | 否 | 站点 |
| `data.shopCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.brandId` | string | 否 | 品牌ID |
| `data.shopCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `data.shopCollectItemInfo.isBasePlate` | integer | 否 | 是否底版 |
| `data.shopCollectItemInfo.detailId` | string | 否 | 详情ID |
| `data.shopCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车辆库关联列表 |
| `data.shopCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 否 | 车型库站点ID |
| `data.shopCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 否 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `data.shopCollectItemInfo.collectShowSizeTemplateIds` | array<integer> | 否 | 重点展示部件Ids classTypeMultipleSizeCharts |
| `data.shopCollectItemInfo.sizeTemplateId` | string | 否 | 尺码模板ID |
| `data.shopCollectItemInfo.personalizationSwitch` | string | 否 | 个性化开关，0-关闭 1-开启 |
| `data.shopCollectItemInfo.discreetShipping` | string | 否 | 隐密发货 |
| `data.shopCollectItemInfo.siteFreightTemplateList` | array<object> | 否 | 按站点维度的运费模板列表，每项包含 site、shopId、freightTemplateId |
| `data.shopCollectItemInfo.siteFreightTemplateList[].site` | string | 否 | 站点编码，如 US、EU |
| `data.shopCollectItemInfo.siteFreightTemplateList[].shopId` | string | 否 | 店铺ID |
| `data.shopCollectItemInfo.siteFreightTemplateList[].freightTemplateId` | string | 否 | 运费模板ID |
| `data.shopCollectItemInfo.siteWarehouseList` | array<object> | 否 | 按站点维度的仓库列表，每项包含 site、shopId、warehouseId； EU 站点下还包含 subSiteWarehouseList（子站点仓库列表） |
| `data.shopCollectItemInfo.siteWarehouseList[].site` | string | 否 | 站点编码，如 US、EU |
| `data.shopCollectItemInfo.siteWarehouseList[].shopId` | integer | 否 | 店铺ID |
| `data.shopCollectItemInfo.siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，US 站直接填写 |
| `data.shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList` | array<object> | 否 | EU 站子站点仓库列表，US 站无此字段 |
| `data.shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 否 | 仓库ID |
| `data.shopCollectItemInfo.siteWarehouseList[].subSiteWarehouseList[].site` | string | 否 | 子站点编码（如 DE、FR） |
| `data.shopCollectItemInfo.manufacturingLocationRegionShortNameList` | array<string> | 否 | 制造地点 |


---

### 保存采集箱站点模式详情

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/save_site_collect_item_info`
- 类型：写
- 原文：[477347607e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347607e0.md)（本地 raw/477347607e0_保存采集箱站点模式详情.md）

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
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 PddkjChoice\CollectItemInfoForSave\SiteCollectItemInfoForSaveRo 注释 |
| `siteCollectItemInfo.collectBoxDetailShopList` | array<object> | 是 | 店铺列表，保存站点模式必填。 |
| `siteCollectItemInfo.collectBoxDetailShopList[].shopId` | integer | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishSiteList` | array<string> | 否 | 发布站点列表，pddkjChoice 必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList` | array<object> | 否 | 站点仓库列表，US 站直接填 warehouseId，EU 站填 subSiteWarehouseList |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].warehouseId` | string | 否 | 仓库ID，非 EU 站点时必填 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList` | array<object> | 否 | 欧盟子站点仓库列表，EU 站点时必填，每项包含 site（子站点编码）和 warehouseId |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].site` | string | 是 | 子站点编码，如 DE、FR、IT 等欧盟子站点 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteWarehouseList[].subSiteWarehouseList[].warehouseId` | string | 是 | 仓库ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList` | array<object> | 否 | 站点运费模板列表 |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].site` | string | 是 | 站点编码，如 US、EU |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].siteFreightTemplateList[].freightTemplateId` | string | 是 | 运费模板ID |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguageType` | integer | 否 | 多语言素材类型 |
| `siteCollectItemInfo.collectBoxDetailShopList[].materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID，通过搜索类目获得。用于调用 getCategoryAttributeRules 获取属性规则、getModelCatInfo 获取模特配置 |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.multiLanguageTitleMap` | object | 否 | 多语言标题映射，key 为语言编码（如 en），value 为对应语言标题 |
| `siteCollectItemInfo.translateLanguages` | array<string> | 否 | 翻译语言列表，指定需要自动翻译的目标语言编码（如 ["en","de","es"]） |
| `siteCollectItemInfo.itemNum` | string | 否 | 非服饰类主货号（skuMap 同级字段，与 skuMap 内各 SKU 的 itemNum 含义不同） |
| `siteCollectItemInfo.productOriginCountry` | string | 是 | 原产国 |
| `siteCollectItemInfo.productOriginProvince` | string | 否 | 原产省编码（原产国为中国时需要填写省份） |
| `siteCollectItemInfo.productOriginCertFiles` | array<object> | 否 | 原产地认证文件列表 |
| `siteCollectItemInfo.productOriginCertFiles[].fileUrl` | string | 否 | 文件URL |
| `siteCollectItemInfo.productOriginCertFiles[].fileName` | string | 否 | 文件名 |
| `siteCollectItemInfo.imgUrls` | array<string> | 是 | 轮播图 |
| `siteCollectItemInfo.multiLanguageImgUrlsMap` | object | 否 | 多语言轮播图映射，key 为语言编码，value 为图片URL列表。 pddkjChoice 非中文站点按 materialMultiLanguageType 和 materialMultiLanguages 校验 |
| `siteCollectItemInfo.shopIdAndGoodsModelReqMap` | object | 否 | 店铺维度的模特信息映射，key 为 shopId，value 为该店铺对应的单条 GoodsModelRo。 requiredGoodsModel 为 true 的类目时，collectBoxDetailShopList 中的每个店铺都必须在此处独立配置模特。 每条记录的 tryOnResult 取值来自 getItemOptions 返回的 goodsModelTryOnResultMap，按 modelType 取对应枚举。 模特试穿尺码需与 saleAttributes 中的规格值匹配 |
| `siteCollectItemInfo.productMaterialImageUrl` | string | 否 | 实拍素材图URL |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.goodsLayerDecorationReqs` | array<object> | 是 | 产品描述 |
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
| `siteCollectItemInfo.collectShowSizeTemplateIds` | array<integer> | 否 | 展示尺码模板ID列表 |
| `siteCollectItemInfo.sizeAttributeValueGroupId` | integer | 否 | 尺码属性值组ID |
| `siteCollectItemInfo.sizeCharts` | array<object> | 否 | 尺码表列表 |
| `siteCollectItemInfo.sizeCharts[].manualEntryIds` | array<integer> | 否 | 手动录入ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateId` | string | 是 | 尺码模板ID |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateSource` | string | 是 | 尺码模板来源 |
| `siteCollectItemInfo.sizeCharts[].elementIds` | array<integer> | 是 | 元素ID列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems` | array<object> | 是 | 尺码项列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].sizeName` | string | 是 | 尺码名称 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList` | array<object> | 是 | 元素值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementId` | integer | 是 | 元素ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].elementValueList[].elementValue` | string | 是 | 元素值 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList` | array<object> | 是 | 分组值列表 |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupValueList[].groupId` | integer | 是 | 分组ID |
| `siteCollectItemInfo.sizeCharts[].sizeItems[].groupIdAndValueMap` | object | 是 | 分组ID与值映射 |
| `siteCollectItemInfo.sizeCharts[].sizeTemplateUniqueId` | string | 是 | 尺码模板唯一ID |
| `siteCollectItemInfo.vehicleLibraryRelationList` | array<object> | 否 | 车型库关联列表，类目支持车型库时填写（通过 getHasVehicleLibraryCidsBySearchCids 确认）。 每项对应一个车型库站点（vehicleLibraryId 来自 getGoodsVehicleLibrarySiteList）， productPropValueDependencyList 为该站点下选择的车型路径列表，展示示意： [ { "vehicleLibraryId": 1, "productPropValueDependencyList": [ [ {"level":1,"propertyValueDependencyId":100,"vidValue":"Toyota"}, {"level":2,"propertyValueDependencyId":200,"vidValue":"Camry"}, {"level":3,"propertyValueDependencyId":300,"vidValue":"2022"}, {"level":4,"propertyValueDependencyId":400,"vidValue":"LE"}, {"level":5,"propertyValueDependencyId":500,"vidValue":"2.5L 4-Cylinder"}] ] } ] 每条路径通过 getVehicleLibraryPropDependencyTree 逐级选择叶子节点后组装， 其中 propertyValueDependencyId 和 vidValue 取自树形节点数据 |
| `siteCollectItemInfo.vehicleLibraryRelationList[].vehicleLibraryId` | string | 是 | 车型库站点ID |
| `siteCollectItemInfo.vehicleLibraryRelationList[].productPropValueDependencyList` | object | 是 | 车型列表（二维数组：多条路径，每条路径直接是节点数组，没有中间对象包装） 实际结构：array<int, array<int, array{vidValue: string, propertyValueDependencyId: string, level: string}>> |
| `siteCollectItemInfo.attributes` | array<object> | 是 | 商品属性列表，取值参考 getCategoryAttributeRules 接口返回的属性规则 |
| `siteCollectItemInfo.attributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].vid` | integer | 是 | 属性值ID |
| `siteCollectItemInfo.attributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.attributes[].values[].valueUnit` | string | 否 | 属性值单位，没有的情况传空字符串 |
| `siteCollectItemInfo.attributes[].values[].numberValue` | integer | 否 | 成分比例 总合需要为100 |
| `siteCollectItemInfo.attributes[].pid` | string | 是 | 属性ID |
| `siteCollectItemInfo.attributes[].templatePid` | string | 是 | 模板属性ID |
| `siteCollectItemInfo.attributes[].refPid` | string | 是 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes` | array<object> | 是 | 销售属性列表 |
| `siteCollectItemInfo.saleAttributes[].name` | string | 是 | 属性名称 |
| `siteCollectItemInfo.saleAttributes[].parentSpecId` | integer | 是 | 父规格ID |
| `siteCollectItemInfo.saleAttributes[].pid` | integer | 否 | 属性ID |
| `siteCollectItemInfo.saleAttributes[].refPid` | integer | 否 | 引用属性ID |
| `siteCollectItemInfo.saleAttributes[].templatePid` | integer | 否 | 模板属性ID |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 是 | 属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].vid` | integer | 否 | 属性值ID |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 是 | SKU Key 生成方式为 属性值名称name md5后取前8位作为skuKey |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 是 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes[].values[].imgUrls` | array<string> | 否 | 服饰类颜色图（服饰类必填） |
| `siteCollectItemInfo.saleAttributes[].values[].itemNum` | string | 否 | 服饰类主货号（服饰类每个SKC都可以设置主货号） |
| `siteCollectItemInfo.skuMap` | object | 是 | SKU Map，key 为规格属性值 ID 组合串，格式为「;skuKey1;skuKey2;」，value 为 SKU 数据。 各 SKU 的 skuClassification/pieceUnitCode/individuallyPacked 取值参考 getItemOptions 接口返回的对应列表。 非服饰类 SKU 的预览图在 imgUrl 中填写。 pddkjChoice 特有：法国站点 skuClassification/numberOfPieces/pieceUnitCode 必填； 混合套装(skuClassification=3)时 productSkuAccessories 必填； 非服饰类 SKU 需填 multiLanguageImgUrlMap（多语言预览图） |
| `siteCollectItemInfo.publishSiteList` | array<string> | 是 | 发布站点列表，如['US','JP'] 取值参考 getPublishSiteOptions接口返回的站点列表 |
| `siteCollectItemInfo.publishEuSiteList` | array<string> | 否 | 欧盟发布站点列表，有值时不能小于2个 |
| `siteCollectItemInfo.siteAndSkuPriceMap` | object | 否 | 按站点维度的 SKU 价格映射。 key 为站点编码，value 为该站点下各 SKU 的价格信息。 欧盟站点下还需填写 subSiteAndPriceMap（子站点价格），法国站点价格必填 |
| `siteCollectItemInfo.siteShipmentLimitDayMap` | object | 否 | 按站点维度的发货时效映射，key 为站点编码，value 为发货天数（非定制品可选值如下）。 US：1, 2, 7, 9 MX：1, 2, 7, 8, 9, 10, 11, 12, 13 CL：1, 2, 7, 8, 9, 10, 11, 12 PE：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15 CO：1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 EC：1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 EU：1, 2, 8, 9, 10, 11, 12 |
| `siteCollectItemInfo.materialMultiLanguageType` | string | 否 | 多语言素材类型，取值参考 PddkjChoiceConst |
| `siteCollectItemInfo.materialMultiLanguages` | array<string> | 否 | 多语言素材语言列表，与 materialMultiLanguageType 配合使用， 决定哪些语言需要提供多语言图片素材 |
| `siteCollectItemInfo.discreetShipping` | string | 否 | 保密发货，0=关闭，1=开启 |
| `siteCollectItemInfo.currency` | string | 否 | 币种，如 CNY、USD |
| `siteCollectItemInfo.shipmentLimitDay` | integer | 否 | 其他站点承诺发货时效 非定制品可选值只有 1,2 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取原产地国家列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_country_short_name_and_name_map`
- 类型：读
- 原文：[477347608e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347608e0.md)（本地 raw/477347608e0_获取原产地国家列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.countryShortNameAndNameMap` | object | 否 | 国家简码→中文名映射，key 为 shortName（如 CN），value 为中文名（如 中国大陆）。 可用于将已保存的 productOriginCountry 短码转换为可读名称展示 |
| `data.productOriginCountries` | array<object> | 否 | 完整国家列表，用于渲染原产地下拉选择器。 选择某个国家后将其 shortName 填入 productOriginCountry； 选择中国（shortName=CN）时，还需从 province 列表中选择省份，将省份 code 填入 productOriginProvince |
| `data.productOriginCountries[].code` | string | 否 | 国家编码（如 43） |
| `data.productOriginCountries[].name` | string | 否 | 英文名 |
| `data.productOriginCountries[].shortName` | string | 否 | 国家简码，填入 productOriginCountry（如 CN、US） |
| `data.productOriginCountries[].chineseName` | string | 否 | 中文名 |
| `data.productOriginCountries[].province` | array<object> | 否 | 省份列表，仅原产国为 CN 时有值。 选择中国后需从此列表选择省份，将省份 code 填入 productOriginProvince |
| `data.productOriginCountries[].province[].code` | string | 否 | 省份编码，原产国为 CN 时填入 productOriginProvince |
| `data.productOriginCountries[].province[].name` | string | 否 | 英文名 |
| `data.productOriginCountries[].province[].chineseName` | string | 否 | 中文名 |


---

### 获取发布站点选项

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_publish_site_options`
- 类型：读
- 原文：[477347609e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347609e0.md)（本地 raw/477347609e0_获取发布站点选项.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.publishSiteOptions` | array<object> | 否 | 发布站点选项列表，用于渲染 publishSiteList 下拉框。 将选中项的 key 填入 publishSiteList； 若选择了 EU（欧盟地区），还需从 getEuropeanRegionSiteList 中选取子站点填入 publishEuSiteList， 且 publishEuSiteList 不能少于 2 个 |
| `data.publishSiteOptions[].key` | string | 否 | 站点编码，填入 publishSiteList（如 US、EU、DE） |
| `data.publishSiteOptions[].value` | string | 否 | 站点中文名，用于展示（如 美国站、欧盟地区） |
| `data.getEuropeanRegionSiteList` | array<object> | 否 | 欧盟子站点列表，用于渲染 publishEuSiteList 多选框。 仅当 publishSiteList 包含 EU 时需要填写； 将选中项的 site 填入 publishEuSiteList，isOpen 为 false 的子站点不可选 |
| `data.getEuropeanRegionSiteList[].site` | string | 否 | 欧盟子站点编码（如 DE、FR、IT），填入 publishEuSiteList |
| `data.getEuropeanRegionSiteList[].name` | string | 否 | 子站点中文名，用于展示（如 德国、法国） |
| `data.getEuropeanRegionSiteList[].siteId` | integer | 否 | 站点ID |
| `data.getEuropeanRegionSiteList[].isOpen` | boolean | 否 | 是否已开放，false 时前端置灰不可选 |
| `data.siteIdAndSiteMap` | object | 否 | siteId → 站点编码映射，key 为 siteId，value 为站点编码（如 US、DE） |


---

### 获取店铺运费模板

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_freight_template`
- 类型：读
- 原文：[477347610e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347610e0.md)（本地 raw/477347610e0_获取店铺运费模板.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `isRsync` | integer | 否 | 是否同步最新数据，1 同步，0 不同步（默认 0） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndFreightTemplateListMap` | object | 否 | 店铺运费模板映射，key 为 shopId，value 为该店铺下所有站点的运费模板列表。 使用方式： 1. 取 shopIdAndFreightTemplateListMap[shopId] 获取当前店铺的模板列表； 2. 列表已按站点分组，同一站点可能有多个模板可选（展示 templateName 供用户选择）； 3. 用户为每个发布站点选定模板后，将所选条目的 templateId 作为 freightTemplateId、 site 原样填入，组成 siteFreightTemplateList 的每一项； 4. siteFreightTemplateList 须覆盖 publishSiteList 中的每个站点，否则校验失败 Map value 为运费模板列表，每一项结构如下： - templateId   string  运费模板ID - templateName string  运费模板名称，用于展示 - site         string  站点编码（如 US、EU、DE） - siteName     string  站点中文名，用于展示 |


---

### 获取店铺发货仓库（支持同步）

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_warehouse`
- 类型：读
- 原文：[477347611e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347611e0.md)（本地 raw/477347611e0_获取店铺发货仓库（支持同步）.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `isRsync` | integer | 否 | 是否同步最新数据，1 同步，0 不同步（默认 0） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndWarehouseListMap` | object | 否 | 店铺仓库映射，key 为 shopId，value 为该店铺下所有站点的仓库列表。 使用方式： 1. 取 shopIdAndWarehouseListMap[shopId] 获取当前店铺的仓库列表； 2. warehouseDisable 该字段暂时不用 不需要判断； 3. 列表已按站点分组，同一站点下可选一个或多个仓库； 4. 为每个发布站点选定仓库后，将 warehouseId 填入 siteWarehouseList[].warehouseId、 site 填入 siteWarehouseList[].site，组成 siteWarehouseList 的每一项； Map value 为仓库列表，每一项结构如下： - warehouseId    string  仓库ID，填入 siteWarehouseList[].warehouseId - warehouseName  string  仓库名称，用于展示 - site           string  站点编码（如 US、DE），填入 siteWarehouseList[].site - shopId         string  所属店铺ID - siteName       string  站点中文名，用于展示 - warehouseDisable string 该字段暂时不用 不需要判断 - managementType string  仓库管理类型。null 或 "0" 为普通仓；"3" 为其他类型仓库 |


---

### 获取类目列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[477347612e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347612e0.md)（本地 raw/477347612e0_获取类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cateTree` | object | 否 | 分类树 Map（key=cid, value=分类节点） |


---

### 获取尺码模板列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_size_template_list`
- 类型：读
- 原文：[477347613e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347613e0.md)（本地 raw/477347613e0_获取尺码模板列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `isRsync` | integer | 否 | 是否同步 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeTemplateList` | array<object> | 否 | 尺码表模板列表，先选择一个模板，再取其sizeTemplateId调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `data.sizeTemplateList[].sizeTemplateId` | string | 否 | 尺码表模板ID，用于调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `data.sizeTemplateList[].name` | string | 否 | 模板名称 |
| `data.sizeTemplateList[].sizeTemplateSource` | string | 否 | 模板来源 |
| `data.minSizeChartNum` | integer | 否 | 最少尺码表数量，创建产品时需要填写的尺码表数量 |
| `data.classType` | integer | 否 | 是否需要多尺码表 0否 1是 为1是 需要填写重点展示部件 collectShowSizeTemplateIds |


---

### 获取尺码表详情

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_size_charts_by_size_template_id`
- 类型：读
- 原文：[477347614e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347614e0.md)（本地 raw/477347614e0_获取尺码表详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `sizeTemplateId` | integer | 是 | 尺码表模板ID |
| `sizeTemplateSource` | string | 是 | 尺码表模板来源（api/erp 尺码表模板列表中有返回这个字段） |
| `refresh` | integer | 否 | 是否刷新 1是 0否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeTemplateId` | string | 否 | 尺码表模板ID，创建产品时sizeCharts中需传此ID |
| `data.sizeCharts` | object | 否 | 尺码表数据，创建产品时按此结构填写sizeCharts |
| `data.sizeCharts.elementIds` | array<integer> | 否 | 启用的尺码参数ID列表，必须包含sizeSpecMeta.elementList中所有necessary=true的项 |
| `data.sizeCharts.sizeItems` | array<object> | 否 | 尺码行数据，每行对应一个尺码（如S/M/L），sizeName必须与saleAttributes中的尺码值一致 |
| `data.sizeCharts.sizeItems[].sizeName` | string | 否 | 尺码名称，如"one-size"、"S"、"M"、"L"，必须与saleAttributes中尺码属性的某个值完全一致 |
| `data.sizeCharts.sizeItems[].elementValueList` | array<object> | 否 | 元素值列表 |
| `data.sizeCharts.sizeItems[].elementValueList[].elementId` | integer | 否 | 元素ID |
| `data.sizeCharts.sizeItems[].elementValueList[].elementValue` | string | 否 | 元素值 |
| `data.sizeCharts.sizeItems[].groupIdAndValueMap` | object | 否 | 分组ID与尺码名称映射 |
| `data.sizeCharts.elementIdAndIsRangeMap` | object | 否 | 参数ID是否支持范围值（如"12-13"），key为elementId，value为true表示支持范围 |
| `data.groupId` | integer | 否 | 尺码分组ID |
| `data.sizeSpecMeta` | object | 否 | 尺码规格元数据，elementList中的necessary=true项必须在sizeCharts.elementIds中包含 |
| `data.sizeSpecMeta.groupList` | array<object> | 否 | 尺码分组列表 |
| `data.sizeSpecMeta.groupList[].id` | integer | 否 | 分组ID |
| `data.sizeSpecMeta.groupList[].name` | string | 否 | 分组名称 |
| `data.sizeSpecMeta.groupList[].unnecessary` | boolean | 否 | 是否非必填 |
| `data.sizeSpecMeta.elementList` | array<object> | 否 | 所有可用的尺码参数列表，创建产品时参考此列表确定要填哪些参数，necessary=true的项必须在sizeCharts.elementIds中包含 |
| `data.sizeSpecMeta.elementList[].necessary` | boolean | 否 | 是否必填，为true时该参数必须包含在sizeCharts.elementIds中 |
| `data.sizeSpecMeta.elementList[].name` | string | 否 | 参数名称，如"胸围全围"、"衣长" |
| `data.sizeSpecMeta.elementList[].id` | integer | 否 | 参数ID，对应sizeItems中elementValueList的elementId |
| `data.sizeSpecMeta.elementList[].unit` | string | 否 | 单位，如"cm" |


---

### 获取模特分类配置

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_model_cat_info`
- 类型：读
- 原文：[477347615e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347615e0.md)（本地 raw/477347615e0_获取模特分类配置.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID，从类目选择接口获取，切换类目后传入查询该类目的模特配置 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.modelCat` | object | 否 | 模特分类配置，为 null 表示该类目不支持模特功能 enabled=1 时展示模特绑定区域，按 modelType 区分成衣模特(0)或鞋模(1)进行筛选绑定。 |
| `data.modelCat.cid` | integer | 否 | 类目ID |
| `data.modelCat.modelType` | integer | 否 | 模特类型（0=成衣模特，1=鞋模），展示模特绑定区域时按此类型筛选可用模特 |
| `data.modelCat.enabled` | integer | 否 | 是否启用模特（1=启用，0=禁用），为1时展示模特绑定区域 |


---

### 获取采集箱列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[477347616e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347616e0.md)（本地 raw/477347616e0_获取采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.itemNum` | string | 否 | 商品编号 |
| `data.stock` | string | 否 | 库存 |
| `data.price` | string | 否 | 价格 |
| `data.thumbnail` | string | 否 | 缩略图 |
| `data.gmtCreate` | string | 否 | 创建时间 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.appAccountId` | string | 否 | 应用账户ID |
| `data.subAppAccountId` | string | 否 | 子应用账户ID |
| `data.platform` | string | 否 | 平台 |
| `data.title` | string | 否 | 商品标题 |
| `data.remark` | string | 否 | 备注 |
| `data.copyType` | string | 否 | 复制类型 |
| `data.collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.collectBoxDetailShopList` | array<object> | 否 | 预发布店铺信息列表 |
| `data.collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |


---

### 批量删除采集箱产品接口

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/delete_collect_box_detail`
- 类型：写
- 原文：[477347617e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347617e0.md)（本地 raw/477347617e0_批量删除采集箱产品接口.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successNum` | integer | 否 | 删除成功数量 |
| `data.failNum` | integer | 否 | 删除失败数量 |
| `data.errorMap` | object | 否 | 删除失败的明细映射，key 为 collectBoxDetailId，value 为失败原因 |
| `data.errorMsg` | string | 否 | 拼接后的错误信息 |


---

### 获取包装清单属性值列表

- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_goods_accessories_list`
- 类型：读
- 原文：[501791146e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/501791146e0.md)（本地 raw/501791146e0_获取包装清单属性值列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `fuzzyValue` | string | 否 | 属性值模糊搜索关键词（可选 未填写默认返回前100条数据） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsAccessoriesList` | array<object> | 否 | 包装清单属性值列表，用于用户选择包装清单内容 最多返回 100 条 |
| `data.goodsAccessoriesList[].vid` | integer | 否 | 属性值ID |
| `data.goodsAccessoriesList[].unitCode` | integer | 否 | 单位编码 |
| `data.goodsAccessoriesList[].unitName` | string | 否 | 单位名称，用于展示 |
| `data.goodsAccessoriesList[].value` | string | 否 | 属性值名称 |


## OZON采集箱>采集箱

### 获取采集箱编辑币种

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_account_setting_edit_currency`
- 类型：读
- 原文：[474774623e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774623e0.md)（本地 raw/474774623e0_获取采集箱编辑币种.md）
- 说明：ozon采集箱涉及售价、原价、最低售价均为该币种，货源价格为CNY

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.editCurrency` | string | 否 | 编辑币种 |


---

### 获取类目列表

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[474774625e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774625e0.md)（本地 raw/474774625e0_获取类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 (暂时只支持OZON) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cateTree` | object | 否 | 分类树 Map（key=cid, value=分类节点） |


---

### 获取类目属性信息

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_category_attributes`
- 类型：读
- 原文：[474774626e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774626e0.md)（本地 raw/474774626e0_获取类目属性信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.categoryAttributes` | array<object> | 否 | 类目属性列表 |
| `data.categoryAttributes[].cid` | integer | 否 | 类目ID |
| `data.categoryAttributes[].attrId` | integer | 否 | 属性ID |
| `data.categoryAttributes[].name` | string | 否 | 属性名称 |
| `data.categoryAttributes[].nameZh` | string | 否 | 属性中文名称 |
| `data.categoryAttributes[].key` | string | 否 | 属性所属类型，可以理解为该属性所代表的类型（Brand-品牌，ColorSample-颜色样本，Season-季节，Material-材料，RichContentJson-富文本JSON，SizeGridJson-尺码表JSON，DuvetCoversSize-被套尺寸，SexMaster-性别） |
| `data.categoryAttributes[].type` | string | 否 | 属性值填写的类型（String-字符串，Integer-整数，Decimal-浮点数） |
| `data.categoryAttributes[].isVariant` | integer | 否 | 是否是销售属性，（1-是，0-否） |
| `data.categoryAttributes[].isCollection` | integer | 否 | 是否是下来选项，（1-是，0-否） |
| `data.categoryAttributes[].isRequired` | integer | 否 | 是否是必填选项，（1-是，0-否） |
| `data.categoryAttributes[].dictionaryId` | integer | 否 | 下拉选项字典ID |
| `data.categoryAttributes[].dictionaryValues` | array<object> | 否 | 下拉选项值列表（前1000个） |
| `data.categoryAttributes[].dictionaryValues[].id` | integer | 否 | 属性值ID |
| `data.categoryAttributes[].dictionaryValues[].value` | string | 否 | 属性值数据 |
| `data.categoryAttributes[].dictionaryValues[].valueZh` | string | 否 | 属性值中文数据 |
| `data.categoryAttributes[].description` | string | 否 | 属性详细描述 |
| `data.categoryAttributes[].descriptionZh` | string | 否 | 属性中文详细描述 |
| `data.categoryAttributes[].tooltip` | string | 否 | 属性填写提示 |
| `data.categoryAttributes[].tooltipZh` | string | 否 | 属性中文填写提示 |


---

### 获取采集箱列表

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[474774624e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774624e0.md)（本地 raw/474774624e0_获取采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(空字符串-全部、notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array<object> | 否 | 采集箱数据列表 |
| `data.detailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.detailList[].itemNum` | string | 否 | 商品编号 |
| `data.detailList[].stock` | string | 否 | 库存 |
| `data.detailList[].minSkuPrice` | string | 否 | 最小sku价格 |
| `data.detailList[].maxSkuPrice` | string | 否 | 最大sku价格 |
| `data.detailList[].thumbnail` | string | 否 | 缩略图 |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | string | 否 | 应用账户ID |
| `data.detailList[].subAppAccountId` | string | 否 | 子应用账户ID |
| `data.detailList[].platform` | string | 否 | 平台 |
| `data.detailList[].title` | string | 否 | 商品标题 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].copyType` | string | 否 | 复制类型 |
| `data.detailList[].collectBoxGroupId` | string | 否 | 采集箱分组ID |


---

### 获取店铺仓库列表

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_shop_warehouse_info_list`
- 类型：读
- 原文：[474774627e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774627e0.md)（本地 raw/474774627e0_获取店铺仓库列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopWarehouseInfoList` | array<object> | 否 | 店铺仓库列表 |
| `data.shopWarehouseInfoList[].shopId` | integer | 否 | 店铺ID |
| `data.shopWarehouseInfoList[].shopNick` | string | 否 | 店铺名称 |
| `data.shopWarehouseInfoList[].warehouseList` | array<object> | 否 | 仓库列表 |
| `data.shopWarehouseInfoList[].warehouseList[].shopId` | string | 否 | 店铺ID |
| `data.shopWarehouseInfoList[].warehouseList[].warehouseId` | string | 否 | 仓库ID |
| `data.shopWarehouseInfoList[].warehouseList[].name` | string | 否 | 仓库名称 |
| `data.shopWarehouseInfoList[].warehouseList[].warehouseType` | string | 否 | 仓库类型 |
| `data.shopWarehouseInfoList[].warehouseList[].isRfbs` | string | 否 | 是否是RFBS仓库 |


---

### 获取采集箱站点模式详情

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[474774628e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774628e0.md)（本地 raw/474774628e0_获取采集箱站点模式详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.siteCollectItemInfo` | object | 否 | 站点数据 |
| `data.siteCollectItemInfo.detailId` | string | 否 | 采集箱详情ID |
| `data.siteCollectItemInfo.site` | string | 否 | 站点 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 合并编号 |
| `data.siteCollectItemInfo.notes` | string | 否 | 商品描述 |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.packageInfoType` | string | 否 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `data.siteCollectItemInfo.packageInfo` | object | 否 | 商品级别包裹尺寸信息 |
| `data.siteCollectItemInfo.packageInfo.depth` | integer | 否 | 深度(长) |
| `data.siteCollectItemInfo.packageInfo.height` | integer | 否 | 高度 |
| `data.siteCollectItemInfo.packageInfo.width` | integer | 否 | 宽度 |
| `data.siteCollectItemInfo.packageInfo.dimensionUnit` | string | 否 | 尺寸单位(毫米mm) |
| `data.siteCollectItemInfo.weightInfo` | object | 否 | 商品级别重量信息 |
| `data.siteCollectItemInfo.weightInfo.weight` | number | 否 | 重量数值 |
| `data.siteCollectItemInfo.weightInfo.weightUnit` | string | 否 | 重量单位(g/kg) |
| `data.siteCollectItemInfo.vat` | string | 否 | 增值税税率(0-豁免，10-10%，20-20%) |
| `data.siteCollectItemInfo.skuSelectedAttrs` | array<string> | 否 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射关系，key为saleAttributeList销售属性里valueKey用分号加首尾分号的拼接值，如：“;红色;S;” |
| `data.siteCollectItemInfo.saleAttributeList` | array<object> | 否 | 销售属性列表(定义变体维度及其可选值) |
| `data.siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `data.siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `data.siteCollectItemInfo.saleAttributeList[].nameZh` | string | 否 | 销售属性中文名称(如商品颜色) |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object | 否 | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string | 否 | 关联属性ID |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string | 否 | 关联属性俄文名称 |
| `data.siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string | 否 | 关联属性中文名称 |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues` | array<object> | 是 | 销售属性值列表(所有变体选项) |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `data.siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object | 否 | 关联属性值(如ColorName的字典值) |
| `data.siteCollectItemInfo.normalAttributes` | array<object> | 否 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `data.siteCollectItemInfo.normalAttributes[].complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `data.siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `data.siteCollectItemInfo.normalAttributes[].values` | array<object> | 是 | 属性字典值列表 |
| `data.siteCollectItemInfo.normalAttributes[].values[].value` | string | 否 | 属性值文本值 |
| `data.siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `data.siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.siteCollectItemInfo.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `data.siteCollectItemInfo.videos` | array<object> | 否 | 产品描述视频列表 |
| `data.siteCollectItemInfo.videos[].mainImgVideoUrl` | string | 否 | 视频URL |
| `data.siteCollectItemInfo.videos[].mainImgAppVideoId` | integer | 否 | 视频ID |
| `data.siteCollectItemInfo.reviewsPromoOperation` | string | 否 | 是否付费推广积分评价(enable-开启，disable-关闭) |


---

### 创建采集箱站点模式数据

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/create_collect_box_item`
- 类型：写
- 原文：[474774629e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774629e0.md)（本地 raw/474774629e0_创建采集箱站点模式数据.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 产品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 产品描述 |
| `siteCollectItemInfo.itemNum` | string | 是 | 合并编号 |
| `siteCollectItemInfo.vat` | string | 是 | 增值税税率(0-豁免，10-10%，20-20%) |
| `siteCollectItemInfo.packageInfoType` | string | 是 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `siteCollectItemInfo.packageInfo` | object | 是 | 商品级别包裹尺寸信息 |
| `siteCollectItemInfo.packageInfo.depth` | integer | 否 | 深度(长) |
| `siteCollectItemInfo.packageInfo.height` | integer | 否 | 高度 |
| `siteCollectItemInfo.packageInfo.width` | integer | 否 | 宽度 |
| `siteCollectItemInfo.packageInfo.dimensionUnit` | string | 否 | 尺寸单位(毫米mm) |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.skuSelectedAttrs` | array<string> | 是 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `siteCollectItemInfo.weightInfo` | object | 是 | 商品级别重量信息 |
| `siteCollectItemInfo.weightInfo.weight` | number | 否 | 重量数值 |
| `siteCollectItemInfo.weightInfo.weightUnit` | string | 否 | 重量单位(g/kg) |
| `siteCollectItemInfo.reviewsPromoOperation` | string | 是 | 是否付费推广积分评价(enable-开启，disable-关闭) |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `siteCollectItemInfo.normalAttributes` | array<object> | 是 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `siteCollectItemInfo.normalAttributes[].complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.normalAttributes[].values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.normalAttributes[].values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList` | array<object> | 是 | 销售属性列表(定义变体维度及其可选值) |
| `siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `siteCollectItemInfo.saleAttributeList[].nameZh` | string | 否 | 销售属性中文名称(如商品颜色) |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object | 否 | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string | 否 | 关联属性ID |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string | 否 | 关联属性俄文名称 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string | 否 | 关联属性中文名称 |
| `siteCollectItemInfo.saleAttributeList[].attrValues` | array<object> | 是 | 销售属性值列表(所有变体选项) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object | 否 | 关联属性值(如ColorName的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 编辑采集箱站点模式数据

- 层级：开放平台 > 商品 > OZON采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/ozon/collect_box/save_site_detail_data`
- 类型：写
- 原文：[474774630e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774630e0.md)（本地 raw/474774630e0_编辑采集箱站点模式数据.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.title` | string | 是 | 产品标题 |
| `siteCollectItemInfo.notes` | string | 是 | 产品描述 |
| `siteCollectItemInfo.itemNum` | string | 是 | 合并编号 |
| `siteCollectItemInfo.vat` | string | 是 | 增值税税率(0-豁免，10-10%，20-20%) |
| `siteCollectItemInfo.packageInfoType` | string | 是 | 包裹信息类型(spu-按spu编辑，sku-按sku编辑) |
| `siteCollectItemInfo.packageInfo` | object | 是 | 商品级别包裹尺寸信息 |
| `siteCollectItemInfo.packageInfo.depth` | integer | 否 | 深度(长) |
| `siteCollectItemInfo.packageInfo.height` | integer | 否 | 高度 |
| `siteCollectItemInfo.packageInfo.width` | integer | 否 | 宽度 |
| `siteCollectItemInfo.packageInfo.dimensionUnit` | string | 否 | 尺寸单位(毫米mm) |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.skuSelectedAttrs` | array<string> | 是 | SKU选中的特殊属性项，需要填写特殊属性项sku里的相关字段在发布的时候生效(title-sku标题，price-原价，minPrice-最低售价，barcode-条码) |
| `siteCollectItemInfo.weightInfo` | object | 是 | 商品级别重量信息 |
| `siteCollectItemInfo.weightInfo.weight` | number | 否 | 重量数值 |
| `siteCollectItemInfo.weightInfo.weightUnit` | string | 否 | 重量单位(g/kg) |
| `siteCollectItemInfo.reviewsPromoOperation` | string | 是 | 是否付费推广积分评价(enable-开启，disable-关闭) |
| `siteCollectItemInfo.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `siteCollectItemInfo.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `siteCollectItemInfo.normalAttributes` | array<object> | 是 | 普通属性列表(非销售维度的商品属性，如品牌、富文本等) |
| `siteCollectItemInfo.normalAttributes[].complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.normalAttributes[].id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.normalAttributes[].values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.normalAttributes[].values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.normalAttributes[].values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList` | array<object> | 是 | 销售属性列表(定义变体维度及其可选值) |
| `siteCollectItemInfo.saleAttributeList[].attrId` | string | 是 | 销售属性ID |
| `siteCollectItemInfo.saleAttributeList[].name` | string | 是 | 销售属性俄文名称(如Цвет товара) |
| `siteCollectItemInfo.saleAttributeList[].nameZh` | string | 否 | 销售属性中文名称(如商品颜色) |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute` | object | 否 | 关联销售属性信息，代表一个销售属性附带另一个销售属性，被关联的销售属性不作为独立的销售属性，只和关联的销售属性一同设置。目前仅支持【商品颜色（attrId=10096）】关联【颜色名称（attrId=10097）】，以及【俄罗斯尺码（attrId=4295/4298）】关联【由制造商规定尺码（attrId=9533）】 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.attrId` | string | 否 | 关联属性ID |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.name` | string | 否 | 关联属性俄文名称 |
| `siteCollectItemInfo.saleAttributeList[].relationSaleAttribute.nameZh` | string | 否 | 关联属性中文名称 |
| `siteCollectItemInfo.saleAttributeList[].attrValues` | array<object> | 是 | 销售属性值列表(所有变体选项) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].valueKey` | string | 是 | 变体值唯一键(如"红色") |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values` | object | 是 | 主属性值(如ColorBase的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].values.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues` | object | 否 | 关联属性值(如ColorName的字典值) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.complexId` | integer | 否 | 复合属性ID(0表示非复合属性) |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.id` | string | 是 | 属性值ID |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values` | array<object> | 是 | 属性字典值列表 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].value` | string | 否 | 属性值文本值 |
| `siteCollectItemInfo.saleAttributeList[].attrValues[].relationValues.values[].dictionaryValueId` | integer | 是 | 字典值ID(0表示自定义值) |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU Map，key为销售属性列表里的变体值唯一键构成的组合串，格式为「;valueKey1;valueKey2;」（分号分隔，首尾带分号），value为SKU数据 |
| `detailId` | integer | 是 | 采集箱ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


## OZON采集箱>产品发布

### 发布记录列表

- 层级：开放平台 > 商品 > OZON采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/ozon/move_collect/search_move_collect_list`
- 类型：读
- 原文：[511671956e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511671956e0.md)（本地 raw/511671956e0_发布记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array<object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].subDetailList` | array<object> | 否 | SKU对应产品发布详情 |
| `data.moveCollectDetailList[].subDetailList[].ozonOfferId` | string | 否 | 平台SKU |
| `data.moveCollectDetailList[].subDetailList[].platformItemId` | string | 否 | 产品ID |
| `data.moveCollectDetailList[].subDetailList[].stock` | string | 否 | 库存 |
| `data.moveCollectDetailList[].subDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].subDetailList[].reason` | string | 否 | 发布失败原因 |
| `data.moveCollectDetailList[].subDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].subDetailList[].gmtModified` | string | 否 | 更新时间 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |


---

### 发布产品

- 层级：开放平台 > 商品 > OZON采集箱 > 产品发布
- 方法+路径：`POST /open/v1/product/collect_box/ozon/move_collect/save_move_collect_task`
- 类型：写
- 原文：[474774631e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774631e0.md)（本地 raw/474774631e0_发布产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


## Shopee采集箱>采集箱

### 获取站点编辑信息

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_site_detail_simple_data`
- 类型：读
- 原文：[480434496e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434496e0.md)（本地 raw/480434496e0_获取站点编辑信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supportSizeChartInfo` | object | 否 | 尺码图支持信息 |
| `data.supportSizeChartInfo.shopeeCategorySupportSizeChartId` | integer | 否 | ID |
| `data.supportSizeChartInfo.site` | string | 否 | 站点 |
| `data.supportSizeChartInfo.cid` | integer | 否 | 类目ID |
| `data.supportSizeChartInfo.isSupportSizeChart` | integer | 否 | 是否支持尺码图表(0,1) |
| `data.supportSizeChartInfo.sizeChartMandatory` | integer | 否 | 尺码表是否强制 |
| `data.supportSizeChartInfo.supportImageSizeChart` | integer | 否 | 是否支持图片尺码表 |
| `data.supportSizeChartInfo.supportTemplateSizeChart` | integer | 否 | 是否支持模板尺码表 |
| `data.supportSizeChartInfo.gmtCreate` | string | 否 | 创建时间 |
| `data.supportSizeChartInfo.gmtModified` | string | 否 | 更新时间 |
| `data.siteDetailSimpleData` | object | 否 | 站点信息详情 |
| `data.siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `data.siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `data.siteDetailSimpleData.itemNum` | string | 否 | 主货号 |
| `data.siteDetailSimpleData.price` | string | 否 | 销售价(单规格产品时必填) |
| `data.siteDetailSimpleData.stock` | string | 否 | 库存(单规格产品时必填) |
| `data.siteDetailSimpleData.sellerStock` | array<object> | 否 | 按仓库分配库存(单规格产品时选填) |
| `data.siteDetailSimpleData.sellerStock[].locationId` | string | 否 | 仓库ID |
| `data.siteDetailSimpleData.sellerStock[].stock` | integer | 否 | 库存数量 |
| `data.siteDetailSimpleData.sellerStock[].shopId` | integer | 否 | 店铺ID |
| `data.siteDetailSimpleData.colorPropName` | string | 否 | 颜色属性名称 |
| `data.siteDetailSimpleData.sizePropName` | string | 否 | 尺码属性名称 |
| `data.siteDetailSimpleData.colorMap` | object | 否 | 颜色Map，key为颜色名 |
| `data.siteDetailSimpleData.sizeMap` | object | 否 | 尺码Map，key为尺码名 |
| `data.siteDetailSimpleData.skuMap` | object | 否 | SKU Map，key为规格组合（如;121201;;） |
| `data.siteDetailSimpleData.imgUrls` | array<string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `data.siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `data.siteDetailSimpleData.packageLength` | string | 否 | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `data.siteDetailSimpleData.packageWidth` | string | 否 | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `data.siteDetailSimpleData.packageHeight` | string | 否 | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `data.siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `data.siteDetailSimpleData.richTextDesc` | string | 否 | 富文本描述 |
| `data.siteDetailSimpleData.wholesaleList` | array<object> | 否 | 批发列表 |
| `data.siteDetailSimpleData.wholesaleList[].min` | integer | 否 | 最小数量 |
| `data.siteDetailSimpleData.wholesaleList[].max` | integer | 否 | 最大数量 |
| `data.siteDetailSimpleData.wholesaleList[].price` | number | 否 | 批发单价 |
| `data.siteDetailSimpleData.attributeMaps` | object | 否 | 属性Map，key为属性ID |
| `data.siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `data.siteDetailSimpleData.brand.brandId` | integer | 否 | 品牌ID |
| `data.siteDetailSimpleData.brand.brandName` | string | 否 | 品牌名称 |
| `data.siteDetailSimpleData.logisticList` | array<object> | 是 | 物流方式列表 |
| `data.siteDetailSimpleData.logisticList[].logisticId` | string | 否 | 物流方式ID |
| `data.siteDetailSimpleData.logisticList[].logisticName` | string | 否 | 物流方式名称 |
| `data.siteDetailSimpleData.logisticList[].enabled` | boolean | 否 | 是否启用 |
| `data.siteDetailSimpleData.logisticList[].estimatedShippingFee` | number | 否 | 预估运费 |
| `data.siteDetailSimpleData.logisticList[].isFree` | boolean | 否 | 是否包邮 |
| `data.siteDetailSimpleData.logisticList[].sizeId` | integer | 否 | 尺寸ID |
| `data.siteDetailSimpleData.logisticList[].customPrice` | string | 否 | 自定义运费 |
| `data.siteDetailSimpleData.logisticList[].site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `data.siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `data.siteDetailSimpleData.daysToShip` | integer | 否 | 发货天数 |
| `data.siteDetailSimpleData.sizeChart` | string | 否 | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `data.siteDetailSimpleData.mainImgVideoUrl` | string | 否 | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `data.siteDetailSimpleData.mainImgAppVideoId` | integer | 否 | 产品视频AppVideoId |
| `data.siteDetailSimpleData.mainImgVideoExpire` | string | 否 | 产品视频过期时间 |
| `data.siteDetailSimpleData.isMainImgVideoExpire` | integer | 否 | 产品视频是否过期 |
| `data.siteDetailSimpleData.originPrice` | string | 否 | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `data.siteDetailSimpleData.colorPropGroupName` | string | 否 | 颜色属性分组名称 |
| `data.siteDetailSimpleData.sizePropGroupName` | string | 否 | 尺码属性分组名称 |
| `data.siteDetailSimpleData.preOrderType` | string | 否 | 否按SKU配置出货天数，枚举值：spu/sku |
| `data.siteDetailSimpleData.sizeChartType` | string | 否 | 尺码表类型，部分类目必填，枚举值：template/image |
| `data.siteDetailSimpleData.shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `data.siteDetailSimpleData.certificationInfoList` | array<object> | 否 | 商品认证信息列表 |
| `data.siteDetailSimpleData.certificationInfoList[].certificationType` | integer | 否 | 认证类型ID |
| `data.siteDetailSimpleData.certificationInfoList[].certificationNo` | string | 否 | 认证编码 |
| `data.siteDetailSimpleData.certificationInfoList[].expireTime` | integer | 否 | 过期时间(时间戳，例如1782748800) |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs` | array<object> | 否 |  |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string | 否 | 文件类型 |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string | 否 | 文件名 |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string | 否 | 文件URL |
| `data.siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer | 否 | 文件UUID(例如：1782467304138) |
| `data.siteDetailSimpleData.certificationInfoList[].permitId` | integer | 否 | 认证ID |
| `data.siteDetailSimpleData.certificationInfoList[].name` | string | 否 | 认证名称 |
| `data.siteDetailSimpleData.isSuppSizechart` | integer | 否 | 是否支持尺码表 |
| `data.siteDetailSimpleData.hasTranslate` | integer | 否 | 是否已翻译（1=是） |
| `data.siteDetailSimpleData.barcode` | string | 否 | 识别码 |
| `data.siteDetailSimpleData.barcodeType` | string | 否 | 识别码类型 |
| `data.isFirstCreateSiteData` | boolean | 否 |  |
| `data.logisticOptions` | object | 否 |  |
| `data.ossMd5` | string | 否 |  |


---

### 保存站点编辑数据

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/save_site_detail_data`
- 类型：写
- 原文：[516157439e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157439e0.md)（本地 raw/516157439e0_保存站点编辑数据.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `ossMd5` | string | 是 | OSS数据的MD5值 |
| `siteDetailSimpleData` | object | 是 | 站点编辑数据（完整siteDetailSimpleData对象） |
| `siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `siteDetailSimpleData.itemNum` | string | 否 | 主货号 |
| `siteDetailSimpleData.price` | string | 否 | 销售价(单规格产品时必填) |
| `siteDetailSimpleData.stock` | string | 否 | 库存(单规格产品时必填) |
| `siteDetailSimpleData.sellerStock` | array<object> | 否 | 按仓库分配库存(单规格产品时选填) |
| `siteDetailSimpleData.sellerStock[].locationId` | string | 否 | 仓库ID |
| `siteDetailSimpleData.sellerStock[].stock` | integer | 否 | 库存数量 |
| `siteDetailSimpleData.sellerStock[].shopId` | integer | 否 | 店铺ID |
| `siteDetailSimpleData.colorPropName` | string | 否 | 颜色属性名称 |
| `siteDetailSimpleData.sizePropName` | string | 否 | 尺码属性名称 |
| `siteDetailSimpleData.colorMap` | object | 否 | 颜色Map，key为颜色名 |
| `siteDetailSimpleData.sizeMap` | object | 否 | 尺码Map，key为尺码名 |
| `siteDetailSimpleData.skuMap` | object | 否 | SKU Map，key为规格组合（如;121201;;） |
| `siteDetailSimpleData.imgUrls` | array<string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `siteDetailSimpleData.packageLength` | string | 否 | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageWidth` | string | 否 | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageHeight` | string | 否 | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `siteDetailSimpleData.richTextDesc` | string | 否 | 富文本描述 |
| `siteDetailSimpleData.wholesaleList` | array<object> | 否 | 批发列表 |
| `siteDetailSimpleData.wholesaleList[].min` | integer | 否 | 最小数量 |
| `siteDetailSimpleData.wholesaleList[].max` | integer | 否 | 最大数量 |
| `siteDetailSimpleData.wholesaleList[].price` | number | 否 | 批发单价 |
| `siteDetailSimpleData.attributeMaps` | object | 否 | 属性Map，key为属性ID |
| `siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `siteDetailSimpleData.brand.brandId` | integer | 否 | 品牌ID |
| `siteDetailSimpleData.brand.brandName` | string | 否 | 品牌名称 |
| `siteDetailSimpleData.logisticList` | array<object> | 是 | 物流方式列表 |
| `siteDetailSimpleData.logisticList[].logisticId` | string | 否 | 物流方式ID |
| `siteDetailSimpleData.logisticList[].logisticName` | string | 否 | 物流方式名称 |
| `siteDetailSimpleData.logisticList[].enabled` | boolean | 否 | 是否启用 |
| `siteDetailSimpleData.logisticList[].estimatedShippingFee` | number | 否 | 预估运费 |
| `siteDetailSimpleData.logisticList[].isFree` | boolean | 否 | 是否包邮 |
| `siteDetailSimpleData.logisticList[].sizeId` | integer | 否 | 尺寸ID |
| `siteDetailSimpleData.logisticList[].customPrice` | string | 否 | 自定义运费 |
| `siteDetailSimpleData.logisticList[].site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `siteDetailSimpleData.daysToShip` | integer | 否 | 发货天数 |
| `siteDetailSimpleData.sizeChart` | string | 否 | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `siteDetailSimpleData.mainImgVideoUrl` | string | 否 | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `siteDetailSimpleData.mainImgAppVideoId` | integer | 否 | 产品视频AppVideoId |
| `siteDetailSimpleData.mainImgVideoExpire` | string | 否 | 产品视频过期时间 |
| `siteDetailSimpleData.isMainImgVideoExpire` | integer | 否 | 产品视频是否过期 |
| `siteDetailSimpleData.originPrice` | string | 否 | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `siteDetailSimpleData.colorPropGroupName` | string | 否 | 颜色属性分组名称 |
| `siteDetailSimpleData.sizePropGroupName` | string | 否 | 尺码属性分组名称 |
| `siteDetailSimpleData.preOrderType` | string | 否 | 否按SKU配置出货天数，枚举值：spu/sku |
| `siteDetailSimpleData.sizeChartType` | string | 否 | 尺码表类型，部分类目必填，枚举值：template/image |
| `siteDetailSimpleData.shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `siteDetailSimpleData.certificationInfoList` | array<object> | 否 | 商品认证信息列表 |
| `siteDetailSimpleData.certificationInfoList[].certificationType` | integer | 否 | 认证类型ID |
| `siteDetailSimpleData.certificationInfoList[].certificationNo` | string | 否 | 认证编码 |
| `siteDetailSimpleData.certificationInfoList[].expireTime` | integer | 否 | 过期时间(时间戳，例如1782748800) |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs` | array<object> | 否 |  |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string | 否 | 文件类型 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string | 否 | 文件名 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string | 否 | 文件URL |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer | 否 | 文件UUID(例如：1782467304138) |
| `siteDetailSimpleData.certificationInfoList[].permitId` | integer | 否 | 认证ID |
| `siteDetailSimpleData.certificationInfoList[].name` | string | 否 | 认证名称 |
| `siteDetailSimpleData.isSuppSizechart` | integer | 否 | 是否支持尺码表 |
| `siteDetailSimpleData.hasTranslate` | integer | 否 | 是否已翻译（1=是） |
| `siteDetailSimpleData.barcode` | string | 否 | 识别码 |
| `siteDetailSimpleData.barcodeType` | string | 否 | 识别码类型 |
| `syncSites` | array<string> | 否 | 需要同步的其他站点列表 |
| `syncSiteFields` | array<string> | 否 | 需要同步的站点字段列表 |
| `shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 | OSS数据的MD5值 |
| `data.syncErrors` | array<object> | 否 | 同步错误列表 |
| `data.syncErrors[].site` | string | 否 | 站点 |
| `data.syncErrors[].errorMsg` | string | 否 | 错误信息 |


---

### 创建采集箱SPU（手动添加商品）

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/create_collect_box_item`
- 类型：写
- 原文：[516157440e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157440e0.md)（本地 raw/516157440e0_创建采集箱SPU（手动添加商品）.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData` | object | 是 | 站点编辑数据（完整siteDetailSimpleData对象） |
| `siteDetailSimpleData.cid` | integer | 是 | 类目ID |
| `siteDetailSimpleData.title` | string | 是 | 商品标题 |
| `siteDetailSimpleData.itemNum` | string | 否 | 主货号 |
| `siteDetailSimpleData.price` | string | 否 | 销售价(单规格产品时必填) |
| `siteDetailSimpleData.stock` | string | 否 | 库存(单规格产品时必填) |
| `siteDetailSimpleData.sellerStock` | array<object> | 否 | 按仓库分配库存(单规格产品时选填) |
| `siteDetailSimpleData.sellerStock[].locationId` | string | 否 | 仓库ID |
| `siteDetailSimpleData.sellerStock[].stock` | integer | 否 | 库存数量 |
| `siteDetailSimpleData.sellerStock[].shopId` | integer | 否 | 店铺ID |
| `siteDetailSimpleData.colorPropName` | string | 否 | 颜色属性名称 |
| `siteDetailSimpleData.sizePropName` | string | 否 | 尺码属性名称 |
| `siteDetailSimpleData.colorMap` | object | 否 | 颜色Map，key为颜色名 |
| `siteDetailSimpleData.sizeMap` | object | 否 | 尺码Map，key为尺码名 |
| `siteDetailSimpleData.skuMap` | object | 否 | SKU Map，key为规格组合（如;121201;;） |
| `siteDetailSimpleData.imgUrls` | array<string> | 是 | 产品图片URL(图片格式：JPG, JPEG, PNG; 图片大小不能超过3M；图片建议尺寸：800x800) |
| `siteDetailSimpleData.weight` | number | 是 | 重量（kg） |
| `siteDetailSimpleData.packageLength` | string | 否 | 包裹长度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageWidth` | string | 否 | 包裹宽度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.packageHeight` | string | 否 | 包裹高度（cm, 包裹尺寸大小必须全填或者全不填） |
| `siteDetailSimpleData.notes` | string | 是 | 商品描述 |
| `siteDetailSimpleData.richTextDesc` | string | 否 | 富文本描述 |
| `siteDetailSimpleData.wholesaleList` | array<object> | 否 | 批发列表 |
| `siteDetailSimpleData.wholesaleList[].min` | integer | 否 | 最小数量 |
| `siteDetailSimpleData.wholesaleList[].max` | integer | 否 | 最大数量 |
| `siteDetailSimpleData.wholesaleList[].price` | number | 否 | 批发单价 |
| `siteDetailSimpleData.attributeMaps` | object | 否 | 属性Map，key为属性ID |
| `siteDetailSimpleData.brand` | object | 是 | 品牌信息 |
| `siteDetailSimpleData.brand.brandId` | integer | 否 | 品牌ID |
| `siteDetailSimpleData.brand.brandName` | string | 否 | 品牌名称 |
| `siteDetailSimpleData.logisticList` | array<object> | 是 | 物流方式列表 |
| `siteDetailSimpleData.logisticList[].logisticId` | string | 否 | 物流方式ID |
| `siteDetailSimpleData.logisticList[].logisticName` | string | 否 | 物流方式名称 |
| `siteDetailSimpleData.logisticList[].enabled` | boolean | 否 | 是否启用 |
| `siteDetailSimpleData.logisticList[].estimatedShippingFee` | number | 否 | 预估运费 |
| `siteDetailSimpleData.logisticList[].isFree` | boolean | 否 | 是否包邮 |
| `siteDetailSimpleData.logisticList[].sizeId` | integer | 否 | 尺寸ID |
| `siteDetailSimpleData.logisticList[].customPrice` | string | 否 | 自定义运费 |
| `siteDetailSimpleData.logisticList[].site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `siteDetailSimpleData.isPreOrder` | integer | 是 | 是否预售（1=是，0=否） |
| `siteDetailSimpleData.daysToShip` | integer | 否 | 发货天数 |
| `siteDetailSimpleData.sizeChart` | string | 否 | 尺码表图片URL,当尺码表类型为image时，该字段必填 |
| `siteDetailSimpleData.mainImgVideoUrl` | string | 否 | 产品视频URL(视频像素不超过1280×1280px，视频时长10s~60s，大小必须小于30M，格式为MP4) |
| `siteDetailSimpleData.mainImgAppVideoId` | integer | 否 | 产品视频AppVideoId |
| `siteDetailSimpleData.mainImgVideoExpire` | string | 否 | 产品视频过期时间 |
| `siteDetailSimpleData.isMainImgVideoExpire` | integer | 否 | 产品视频是否过期 |
| `siteDetailSimpleData.originPrice` | string | 否 | 货源价格(如果是站点产品数据，表示货源价格字段；如果是源数据，这个价格不要更改，无意义) |
| `siteDetailSimpleData.colorPropGroupName` | string | 否 | 颜色属性分组名称 |
| `siteDetailSimpleData.sizePropGroupName` | string | 否 | 尺码属性分组名称 |
| `siteDetailSimpleData.preOrderType` | string | 否 | 否按SKU配置出货天数，枚举值：spu/sku |
| `siteDetailSimpleData.sizeChartType` | string | 否 | 尺码表类型，部分类目必填，枚举值：template/image |
| `siteDetailSimpleData.shopIdAndSizeChartIdMap` | object | 否 | 店铺ID与尺码表ID映射,当尺码表类型为template时，该字段必填 |
| `siteDetailSimpleData.certificationInfoList` | array<object> | 否 | 商品认证信息列表 |
| `siteDetailSimpleData.certificationInfoList[].certificationType` | integer | 否 | 认证类型ID |
| `siteDetailSimpleData.certificationInfoList[].certificationNo` | string | 否 | 认证编码 |
| `siteDetailSimpleData.certificationInfoList[].expireTime` | integer | 否 | 过期时间(时间戳，例如1782748800) |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs` | array<object> | 否 |  |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileType` | string | 否 | 文件类型 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileName` | string | 否 | 文件名 |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].fileUrl` | string | 否 | 文件URL |
| `siteDetailSimpleData.certificationInfoList[].certificationProofs[].uid` | integer | 否 | 文件UUID(例如：1782467304138) |
| `siteDetailSimpleData.certificationInfoList[].permitId` | integer | 否 | 认证ID |
| `siteDetailSimpleData.certificationInfoList[].name` | string | 否 | 认证名称 |
| `siteDetailSimpleData.isSuppSizechart` | integer | 否 | 是否支持尺码表 |
| `siteDetailSimpleData.hasTranslate` | integer | 否 | 是否已翻译（1=是） |
| `siteDetailSimpleData.barcode` | string | 否 | 识别码 |
| `siteDetailSimpleData.barcodeType` | string | 否 | 识别码类型 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 采集箱详情ID |


---

### 获取采集箱产品的源数据

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_collect_box_item_detail`
- 类型：读
- 原文：[516157441e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157441e0.md)（本地 raw/516157441e0_获取采集箱产品的源数据.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemDetail` | object | 否 | 采集箱详情数据 |
| `data.itemDetail.title` | string | 是 | 标题 |
| `data.itemDetail.notes` | string | 是 | 简易描述 |
| `data.itemDetail.richTextDesc` | string | 否 | 图文描述 |
| `data.itemDetail.colorPropName` | string | 否 | 颜色属性名称（规格1属性名称） |
| `data.itemDetail.sizePropName` | string | 否 | 尺码属性名称(规格2属性名称) |
| `data.itemDetail.skuMap` | object | 否 | SKU映射 (多规格产品必填 |
| `data.itemDetail.colorMap` | object | 否 | 颜色映射 (多规格产品必填) |
| `data.itemDetail.sizeMap` | object | 否 | 尺寸映射 (多规格产品必填 |
| `data.itemDetail.imagePaths` | array<string> | 否 | 图片路径列表 |
| `data.itemDetail.sourceAttrs` | array<object> | 否 | 来源属性列表 |
| `data.itemDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `data.itemDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `data.itemDetail.brandName` | string | 否 | 品牌名称 |
| `data.itemDetail.itemNum` | string | 否 | 商品编码 |
| `data.itemDetail.width` | string | 否 | 宽度 |
| `data.itemDetail.length` | string | 否 | 长度 |
| `data.itemDetail.height` | string | 否 | 高度 |
| `data.itemDetail.weight` | number | 是 | 重量（kg） |
| `data.itemDetail.videoInfo` | object | 否 | 视频信息 |
| `data.itemDetail.videoInfo.videoUrl` | string | 否 | 视频url |
| `data.itemDetail.videoInfo.coverUrl` | string | 否 | 封面视频url |
| `data.itemDetail.appAccountId` | string | 否 | 应用账户ID |
| `data.itemDetail.subAppAccountId` | string | 否 | 子应用账户ID |
| `data.itemDetail.sourceItemId` | string | 否 | 来源商品ID |
| `data.itemDetail.source` | string | 否 | 来源 |
| `data.itemDetail.site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `data.itemDetail.price` | number | 否 | 价格 (单规格产品时必填) |
| `data.itemDetail.stock` | integer | 否 | 库存 (单规格产品时必填) |
| `data.itemDetail.packageLength` | string | 否 | 包裹长度 |
| `data.itemDetail.packageWidth` | string | 否 | 包裹宽度 |
| `data.itemDetail.packageHeight` | string | 否 | 包裹高度 |
| `data.itemDetail.imgUrls` | array<string> | 是 | 图片URL列表 |
| `data.itemDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `data.itemDetail.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `data.itemDetail.isPreOrder` | integer | 是 | 是否预售 (0,1) |
| `data.itemDetail.daysToShip` | integer | 否 | 预购天数（当isPreOrder=1时必填） |
| `data.itemDetail.preOrderType` | string | 否 | 是否按SKU配置出货天数，枚举值：spu/sku |
| `data.ossMd5` | string | 否 | OSS数据的MD5值 |


---

### 保存采集箱产品源数据信息

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/save_edit_item`
- 类型：写
- 原文：[516157442e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157442e0.md)（本地 raw/516157442e0_保存采集箱产品源数据信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `collectBoxDetailId` | string | 是 | 采集箱ID |
| `itemDetail` | object | 是 | 采集箱详情数据 |
| `itemDetail.title` | string | 是 | 标题 |
| `itemDetail.notes` | string | 是 | 简易描述 |
| `itemDetail.richTextDesc` | string | 否 | 图文描述 |
| `itemDetail.colorPropName` | string | 否 | 颜色属性名称（规格1属性名称） |
| `itemDetail.sizePropName` | string | 否 | 尺码属性名称(规格2属性名称) |
| `itemDetail.skuMap` | object | 否 | SKU映射 (多规格产品必填 |
| `itemDetail.colorMap` | object | 否 | 颜色映射 (多规格产品必填) |
| `itemDetail.sizeMap` | object | 否 | 尺寸映射 (多规格产品必填 |
| `itemDetail.imagePaths` | array<string> | 否 | 图片路径列表 |
| `itemDetail.sourceAttrs` | array<object> | 否 | 来源属性列表 |
| `itemDetail.sourceAttrs[].name` | string | 否 | 属性名 |
| `itemDetail.sourceAttrs[].value` | string | 否 | 属性值 |
| `itemDetail.brandName` | string | 否 | 品牌名称 |
| `itemDetail.itemNum` | string | 否 | 商品编码 |
| `itemDetail.width` | string | 否 | 宽度 |
| `itemDetail.length` | string | 否 | 长度 |
| `itemDetail.height` | string | 否 | 高度 |
| `itemDetail.weight` | number | 是 | 重量（kg） |
| `itemDetail.videoInfo` | object | 否 | 视频信息 |
| `itemDetail.videoInfo.videoUrl` | string | 否 | 视频url |
| `itemDetail.videoInfo.coverUrl` | string | 否 | 封面视频url |
| `itemDetail.appAccountId` | string | 否 | 应用账户ID |
| `itemDetail.subAppAccountId` | string | 否 | 子应用账户ID |
| `itemDetail.sourceItemId` | string | 否 | 来源商品ID |
| `itemDetail.source` | string | 否 | 来源 |
| `itemDetail.site` | string | 否 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |
| `itemDetail.price` | number | 否 | 价格 (单规格产品时必填) |
| `itemDetail.stock` | integer | 否 | 库存 (单规格产品时必填) |
| `itemDetail.packageLength` | string | 否 | 包裹长度 |
| `itemDetail.packageWidth` | string | 否 | 包裹宽度 |
| `itemDetail.packageHeight` | string | 否 | 包裹高度 |
| `itemDetail.imgUrls` | array<string> | 是 | 图片URL列表 |
| `itemDetail.mainImgVideoUrl` | string | 否 | 主图视频URL |
| `itemDetail.mainImgAppVideoId` | integer | 否 | 主图应用视频ID |
| `itemDetail.isPreOrder` | integer | 是 | 是否预售 (0,1) |
| `itemDetail.daysToShip` | integer | 否 | 预购天数（当isPreOrder=1时必填） |
| `itemDetail.preOrderType` | string | 否 | 是否按SKU配置出货天数，枚举值：spu/sku |
| `ossMd5` | string | 是 | OSS标识 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.ossMd5` | string | 否 |  |


---

### 获取采集箱列表

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/search_collect_box_detail_list`
- 类型：读
- 原文：[516157443e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157443e0.md)（本地 raw/516157443e0_获取采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 否 | 当前页码 |
| `pageSize` | integer | 否 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.detailList` | array<object> | 否 | 采集箱数据列表 |
| `data.detailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.detailList[].itemNum` | string | 否 | 商品编号 |
| `data.detailList[].stock` | string | 否 | 库存 |
| `data.detailList[].price` | string | 否 | 价格 |
| `data.detailList[].thumbnail` | string | 否 | 缩略图 |
| `data.detailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.detailList[].editModel` | string | 否 | 编辑模式 |
| `data.detailList[].commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.detailList[].appAccountId` | string | 否 | 应用账户ID |
| `data.detailList[].subAppAccountId` | string | 否 | 子应用账户ID |
| `data.detailList[].platform` | string | 否 | 平台 |
| `data.detailList[].title` | string | 否 | 商品标题 |
| `data.detailList[].remark` | string | 否 | 备注 |
| `data.detailList[].copyType` | string | 否 | 复制类型 |
| `data.detailList[].collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.detailList[].collectBoxDetailShopList` | array<object> | 否 | 预发布店铺信息列表 |
| `data.detailList[].collectBoxDetailShopList[].shopId` | string | 否 | 店铺ID |


---

### 获取品牌列表

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_brand_list`
- 类型：读
- 原文：[516157444e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157444e0.md)（本地 raw/516157444e0_获取品牌列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.isMandatory` | boolean | 否 | 品牌是否必填 |
| `data.inputType` | string | 否 | 输入类型 |
| `data.brandList` | array<object> | 否 | 品牌列表 |
| `data.brandList[].brandId` | integer | 否 | 品牌ID |
| `data.brandList[].brandName` | string | 否 | 品牌名称 |
| `data.gmtModified` | string | 否 | 最后修改时间 |
| `data.isFromOss` | boolean | 否 | 是否来自OSS缓存 |


---

### 根据站点获取运费模板(物流方式)

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_logistic_options_by_site`
- 类型：读
- 原文：[516157445e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157445e0.md)（本地 raw/516157445e0_根据站点获取运费模板(物流方式).md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.label` | string | 否 | 物流选项标签 |
| `data.value` | string | 否 | 物流选项值 |
| `data.feeType` | string | 否 | 运费类型 |
| `data.isEnableEditShippingFee` | boolean | 否 | 是否允许编辑运费 |


---

### 获取类目树

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[516157446e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157446e0.md)（本地 raw/516157446e0_获取类目树.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 站点 如: TW, ID, MY, SHOPEEGLOBAL |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cateTree` | object | 否 | 分类树 Map（key=cid, value=分类节点） |


---

### 获取类目属性信息

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_category_attributes`
- 类型：读
- 原文：[516158667e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516158667e0.md)（本地 raw/516158667e0_获取类目属性信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `site` | string | 是 | 站点，如: SHOPEEGLOBAL, TW, ID, MY |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.categoryAttributes` | array<object> | 否 | 类目属性列表 |
| `data.categoryAttributes[].attributeId` | integer | 否 | 属性ID |
| `data.categoryAttributes[].attributeUnit` | array<string> | 否 | 属性参数单位值（单选，前面一般跟数字配对） |
| `data.categoryAttributes[].attributeValueList` | array<object> | 否 | 属性选项（单选选或者多选） |
| `data.categoryAttributes[].attributeValueList[].valueId` | integer | 否 | 属性值ID |
| `data.categoryAttributes[].attributeValueList[].displayValueName` | string | 否 | 属性值名称 |
| `data.categoryAttributes[].attributeValueList[].originalValueName` | string | 否 | 原始属性值名称 |
| `data.categoryAttributes[].displayAttributeName` | string | 否 | 属性别名（一般中文） |
| `data.categoryAttributes[].formatType` | string | 否 | 属性参数格式类型（NORMAL，QUANTITATIVE，YEAR_MONTH_DATE，YEAR_MONTH） |
| `data.categoryAttributes[].inputType` | string | 否 | 属性内容类型（DROP_DOWN,MULTIPLE_SELECT,TEXT_FILED,COMBO_BOX,MULTIPLE_SELECT_COMBO_BOX） |
| `data.categoryAttributes[].inputValidationType` | string | 否 | 属性内容校验类型（INT_TYPE STRING_TYPE ENUM_TYPE FLOAT_TYPE DATE_TYPE TIMESTAMP_TYPE） |
| `data.categoryAttributes[].isMandatory` | boolean | 否 | 是否必填 |
| `data.categoryAttributes[].maxInputValueNumber` | integer | 否 | 最大输入值数量（一般选项限制使用） |
| `data.categoryAttributes[].originalAttributeName` | string | 否 | 接口原始属性名 |


---

### 获取仓库信息列表

- 层级：开放平台 > 商品 > Shopee采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/shopee/collect_box/get_global_shop_warehouse`
- 类型：读
- 原文：[516158668e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516158668e0.md)（本地 raw/516158668e0_获取仓库信息列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.warehouseLocationList` | array<object> | 否 | 仓库信息列表 |
| `data.warehouseLocationList[].locationId` | string | 否 | 属性ID |
| `data.warehouseLocationList[].shopName` | string | 否 | 店铺别名 |
| `data.warehouseLocationList[].warehouseLocationType` | string | 否 | 仓库类型（local本土，cb跨境） |
| `data.warehouseLocationList[].warehouseName` | string | 否 | 仓库名称 |


## Shopee采集箱>商品发布

### 发布记录列表

- 层级：开放平台 > 商品 > Shopee采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/shopee/move_collect/search_move_collect_list`
- 类型：读
- 原文：[511672303e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511672303e0.md)（本地 raw/511672303e0_发布记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array<object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |


---

### 提交全球商品发布到店铺任务

- 层级：开放平台 > 商品 > Shopee采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/shopee/move_collect/save_move_collect_global_task`
- 类型：写
- 原文：[480434554e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434554e0.md)（本地 raw/480434554e0_提交全球商品发布到店铺任务.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopeeGlobalItemIds` | array<integer> | 是 | 全球商品ID |
| `shopIds` | array<integer> | 是 | 店铺ID |
| `isUseShopeeGlobalSetting` | integer | 否 | 是否使用全球发布配置;1是,0否 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectTaskDetailIds` | array<integer> | 否 | 任务ID |


---

### 采集箱产品发布任务

- 层级：开放平台 > 商品 > Shopee采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/shopee/move_collect/save_move_collect_task`
- 类型：写
- 原文：[480434555e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434555e0.md)（本地 raw/480434555e0_采集箱产品发布任务.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID |
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


## 在线产品管理>Shopee全球在线产品管理

### 全球产品搜索

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/search_item_list`
- 类型：读
- 原文：[480434401e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434401e0.md)（本地 raw/480434401e0_全球产品搜索.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 页码，默认1 |
| `pageSize` | integer | 是 | 每页条数，默认20 |
| `filter` | object | 是 | 搜索条件 |
| `filter.shopId` | string | 是 | 店铺ID(必传,性能问题无法支持多店铺检索) |
| `filter.platformItemId` | string | 否 | 平台产品ID |
| `filter.itemNum` | string | 否 | 主货号 |
| `filter.cids` | array<integer> | 否 | 类目ID |
| `filter.status` | string | 否 | 产品状态 |
| `filter.title` | string | 否 | 标题 |
| `filter.minStock` | string | 否 | 最小库存 |
| `filter.maxStock` | string | 否 | 最大库存 |
| `filter.publishedProductStatus` | string | 否 | 发布产品状态 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemList` | array<object> | 否 | 产品列表 |
| `data.itemList[].shopId` | string | 否 | 店铺ID |
| `data.itemList[].itemId` | string | 否 | 产品ID |
| `data.itemList[].platformItemId` | string | 否 | 平台产品ID |
| `data.itemList[].title` | string | 否 | 标题 |
| `data.itemList[].picUrl` | string | 否 | 产品图片链接 |
| `data.itemList[].salePrice` | string | 否 | 售价 |
| `data.itemList[].stock` | string | 否 | 库存 |
| `data.itemList[].itemNum` | string | 否 | 主货号 |
| `data.itemList[].platformStatus` | string | 否 | 发布状态 |
| `data.itemList[].status` | string | 否 | 产品状态 |
| `data.itemList[].weight` | string | 否 | 重量 |
| `data.itemList[].gmtCreate` | string | 否 | 创建时间 |
| `data.total` | integer | 否 | 总数 |


---

### 全球产品详情（返回官方

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/get_item_detail`
- 类型：读
- 原文：[480434402e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434402e0.md)（本地 raw/480434402e0_全球产品详情（返回官方.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemId` | string | 是 | 平台产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemInfo` | object | 否 | 全球商品详情 |
| `data.itemInfo.globalItemId` | integer | 是 | Shopee 全球商品唯一标识 |
| `data.itemInfo.globalItemName` | string | 否 | 全球商品名称 |
| `data.itemInfo.description` | string | 否 | 全球商品描述 |
| `data.itemInfo.globalItemSku` | string | 否 | 全球商品 SKU |
| `data.itemInfo.globalItemStatus` | string | 否 | 商品状态（NORMAL） |
| `data.itemInfo.createTime` | integer | 否 | 创建时间戳 |
| `data.itemInfo.updateTime` | integer | 否 | 更新时间戳 |
| `data.itemInfo.stockInfo` | array<object> | 否 | 库存信息（无规格时返回） |
| `data.itemInfo.stockInfo[].stockType` | integer | 否 | 库存类型 |
| `data.itemInfo.stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `data.itemInfo.stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `data.itemInfo.stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `data.itemInfo.priceInfo` | array<object> | 否 | 价格信息（无规格时返回） |
| `data.itemInfo.priceInfo[].currency` | string | 否 | 币种 |
| `data.itemInfo.priceInfo[].originalPrice` | number | 否 | 原价 |
| `data.itemInfo.priceInfo[].sipItemPrice` | number | 否 | SIP 商品价格 |
| `data.itemInfo.priceInfo[].sipItemPriceSource` | string | 否 | SIP 价格来源（auto / manual） |
| `data.itemInfo.image` | object | 否 | 图片信息 |
| `data.itemInfo.image.imageIdList` | array<string> | 是 | 图片 ID 列表 |
| `data.itemInfo.image.imageUrlList` | array<string> | 否 | 图片 URL 列表 |
| `data.itemInfo.weight` | string | 否 | 重量，单位 KG |
| `data.itemInfo.dimension` | object | 否 | 包裹尺寸 |
| `data.itemInfo.dimension.packageLength` | integer | 否 | 包裹长度，单位 CM |
| `data.itemInfo.dimension.packageWidth` | integer | 否 | 包裹宽度，单位 CM |
| `data.itemInfo.dimension.packageHeight` | integer | 否 | 包裹高度，单位 CM |
| `data.itemInfo.preOrder` | object | 否 | 预售信息 |
| `data.itemInfo.preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `data.itemInfo.sizeChart` | string | 否 | 尺码表图片 URL |
| `data.itemInfo.condition` | string | 否 | 是否二手（NEW / USED） |
| `data.itemInfo.hasModel` | boolean | 否 | 是否包含规格 |
| `data.itemInfo.video` | array<object> | 否 | 视频信息(获取商品详情时此字段有值, 编辑时此字段无效) |
| `data.itemInfo.video[].videoUrl` | string | 否 | 视频 URL |
| `data.itemInfo.video[].thumbnailUrl` | string | 否 | 视频缩略图 URL |
| `data.itemInfo.video[].duration` | integer | 否 | 视频时长，单位秒 |
| `data.itemInfo.videoUploadId` | string | 否 | 视频ID (通过上传视频接口获取，编辑商品时此字段用于更新商品视频) |
| `data.itemInfo.categoryId` | integer | 否 | 分类 ID |
| `data.itemInfo.brand` | object | 否 | 品牌信息 |
| `data.itemInfo.brand.brandId` | integer | 否 | 品牌 ID |
| `data.itemInfo.brand.originalBrandName` | string | 否 | 品牌原始名称 |
| `data.itemInfo.attributeList` | array<object> | 否 | 属性列表 |
| `data.itemInfo.attributeList[].attributeId` | integer | 否 | 属性 ID |
| `data.itemInfo.attributeList[].originalAttributeName` | string | 否 | 属性名称 |
| `data.itemInfo.attributeList[].attributeValueList` | array<object> | 否 | 属性值列表 |
| `data.itemInfo.attributeList[].attributeValueList[].valueId` | integer | 否 | 属性值 ID |
| `data.itemInfo.attributeList[].attributeValueList[].originalValueName` | string | 否 | 属性值名称 |
| `data.itemInfo.attributeList[].attributeValueList[].valueUnit` | string | 否 | 属性值单位 |
| `data.itemInfo.descriptionInfo` | object | 否 | 新版描述信息 |
| `data.itemInfo.descriptionInfo.extendedDescription` | object | 否 | 扩展描述 |
| `data.itemInfo.descriptionInfo.extendedDescription.fieldList` | array<object> | 否 | 扩展描述字段列表 |
| `data.itemInfo.descriptionInfo.descriptionType` | string | 否 | 描述类型：normal / extended |
| `data.itemInfo.isFulfillmentByShopee` | boolean | 否 | 是否为 Shopee 履约商品 |
| `data.itemInfo.sizeChartId` | integer | 否 | 尺码表模板 ID |
| `data.modelList` | object | 否 | 全球规格列表 |
| `data.modelList.tierVariation` | array<object> | 否 | 层级规格信息 |
| `data.modelList.tierVariation[].name` | string | 否 | 层级规格名称 |
| `data.modelList.tierVariation[].optionList` | array<object> | 否 | 层级规格选项列表 |
| `data.modelList.tierVariation[].optionList[].option` | string | 否 | 层级规格选项值 |
| `data.modelList.tierVariation[].image` | object | 否 | 层级规格图片 |
| `data.modelList.tierVariation[].image.imageUrl` | string | 否 | 图片 URL |
| `data.modelList.tierVariation[].image.imageId` | string | 否 | 图片 ID |
| `data.modelList.globalModel` | array<object> | 否 | 全球规格列表(SKU列表) |
| `data.modelList.globalModel[].globalModelId` | integer | 否 | 全球规格 ID |
| `data.modelList.globalModel[].globalModelSku` | string | 否 | 全球规格 SKU |
| `data.modelList.globalModel[].priceInfo` | object | 否 | 价格信息 |
| `data.modelList.globalModel[].priceInfo.originalPrice` | number | 否 | 原价 |
| `data.modelList.globalModel[].stockInfo` | array<object> | 否 | 库存信息 |
| `data.modelList.globalModel[].stockInfo[].stockType` | integer | 否 | 库存类型：1 = WMS 在库，2 = 卖家在库 |
| `data.modelList.globalModel[].stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `data.modelList.globalModel[].stockInfo[].currentStock` | integer | 否 | 当前库存 |
| `data.modelList.globalModel[].stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `data.modelList.globalModel[].stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `data.modelList.globalModel[].tierIndex` | array<integer> | 否 | 层级索引 |
| `data.modelList.globalModel[].weight` | string | 否 | 重量，单位 KG |
| `data.modelList.globalModel[].dimension` | object | 否 | 包裹尺寸 |
| `data.modelList.globalModel[].dimension.packageHeight` | integer | 是 | 包裹高度，单位 CM |
| `data.modelList.globalModel[].dimension.packageLength` | integer | 是 | 包裹长度，单位 CM |
| `data.modelList.globalModel[].dimension.packageWidth` | integer | 是 | 包裹宽度，单位 CM |
| `data.modelList.globalModel[].preOrder` | object | 否 | 预售信息 |
| `data.modelList.globalModel[].preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `data.modelList.globalModel[].isFulfillmentByShopee` | boolean | 否 | 是否为 FBS 规格 |
| `data.modelList.standardiseTierVariation` | array<object> | 否 | 标准化层级规格信息 |
| `data.modelList.standardiseTierVariation[].variationId` | integer | 否 | 标准化层级规格 ID |
| `data.modelList.standardiseTierVariation[].variationName` | string | 否 | 标准化层级规格名称 |
| `data.modelList.standardiseTierVariation[].variationGroupId` | integer | 否 | 标准化层级规格组 ID |
| `data.modelList.standardiseTierVariation[].variationOptionList` | array<object> | 否 | 标准化层级规格选项列表 |
| `data.modelList.standardiseTierVariation[].variationOptionList[].variationOptionId` | integer | 否 | 标准化层级规格选项 ID |
| `data.modelList.standardiseTierVariation[].variationOptionList[].variationOptionName` | string | 否 | 标准化层级规格选项名称 |
| `data.modelList.standardiseTierVariation[].imageId` | string | 否 | 图片 ID |
| `data.modelList.standardiseTierVariation[].imageUrl` | string | 否 | 图片 URL |


---

### 保存产品编辑

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/save_edit_item`
- 类型：写
- 原文：[480434403e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434403e0.md)（本地 raw/480434403e0_保存产品编辑.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `itemInfo` | object | 是 | 全球商品详情（前端修改后的 GetItemDetailVo.itemInfo，仅传新数据） |
| `itemInfo.globalItemId` | integer | 是 | Shopee 全球商品唯一标识 |
| `itemInfo.globalItemName` | string | 否 | 全球商品名称 |
| `itemInfo.description` | string | 否 | 全球商品描述 |
| `itemInfo.globalItemSku` | string | 否 | 全球商品 SKU |
| `itemInfo.globalItemStatus` | string | 否 | 商品状态（NORMAL） |
| `itemInfo.createTime` | integer | 否 | 创建时间戳 |
| `itemInfo.updateTime` | integer | 否 | 更新时间戳 |
| `itemInfo.stockInfo` | array<object> | 否 | 库存信息（无规格时返回） |
| `itemInfo.stockInfo[].stockType` | integer | 否 | 库存类型 |
| `itemInfo.stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `itemInfo.stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `itemInfo.stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `itemInfo.priceInfo` | array<object> | 否 | 价格信息（无规格时返回） |
| `itemInfo.priceInfo[].currency` | string | 否 | 币种 |
| `itemInfo.priceInfo[].originalPrice` | number | 否 | 原价 |
| `itemInfo.priceInfo[].sipItemPrice` | number | 否 | SIP 商品价格 |
| `itemInfo.priceInfo[].sipItemPriceSource` | string | 否 | SIP 价格来源（auto / manual） |
| `itemInfo.image` | object | 否 | 图片信息 |
| `itemInfo.image.imageIdList` | array<string> | 是 | 图片 ID 列表 |
| `itemInfo.image.imageUrlList` | array<string> | 否 | 图片 URL 列表 |
| `itemInfo.weight` | string | 否 | 重量，单位 KG |
| `itemInfo.dimension` | object | 否 | 包裹尺寸 |
| `itemInfo.dimension.packageLength` | integer | 否 | 包裹长度，单位 CM |
| `itemInfo.dimension.packageWidth` | integer | 否 | 包裹宽度，单位 CM |
| `itemInfo.dimension.packageHeight` | integer | 否 | 包裹高度，单位 CM |
| `itemInfo.preOrder` | object | 否 | 预售信息 |
| `itemInfo.preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `itemInfo.sizeChart` | string | 否 | 尺码表图片 URL |
| `itemInfo.condition` | string | 否 | 是否二手（NEW / USED） |
| `itemInfo.hasModel` | boolean | 否 | 是否包含规格 |
| `itemInfo.video` | array<object> | 否 | 视频信息(获取商品详情时此字段有值, 编辑时此字段无效) |
| `itemInfo.video[].videoUrl` | string | 否 | 视频 URL |
| `itemInfo.video[].thumbnailUrl` | string | 否 | 视频缩略图 URL |
| `itemInfo.video[].duration` | integer | 否 | 视频时长，单位秒 |
| `itemInfo.videoUploadId` | string | 否 | 视频ID (通过上传视频接口获取，编辑商品时此字段用于更新商品视频) |
| `itemInfo.categoryId` | integer | 否 | 分类 ID |
| `itemInfo.brand` | object | 否 | 品牌信息 |
| `itemInfo.brand.brandId` | integer | 否 | 品牌 ID |
| `itemInfo.brand.originalBrandName` | string | 否 | 品牌原始名称 |
| `itemInfo.attributeList` | array<object> | 否 | 属性列表 |
| `itemInfo.attributeList[].attributeId` | integer | 否 | 属性 ID |
| `itemInfo.attributeList[].originalAttributeName` | string | 否 | 属性名称 |
| `itemInfo.attributeList[].attributeValueList` | array<object> | 否 | 属性值列表 |
| `itemInfo.attributeList[].attributeValueList[].valueId` | integer | 否 | 属性值 ID |
| `itemInfo.attributeList[].attributeValueList[].originalValueName` | string | 否 | 属性值名称 |
| `itemInfo.attributeList[].attributeValueList[].valueUnit` | string | 否 | 属性值单位 |
| `itemInfo.descriptionInfo` | object | 否 | 新版描述信息 |
| `itemInfo.descriptionInfo.extendedDescription` | object | 否 | 扩展描述 |
| `itemInfo.descriptionInfo.extendedDescription.fieldList` | array<object> | 否 | 扩展描述字段列表 |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].fieldType` | string | 否 | 字段类型：text / image |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].text` | string | 否 | 文本内容（field_type 为 text 时返回） |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo` | object | 否 | 图片信息（field_type 为 image 时返回） |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo.imageId` | string | 否 | 图片 ID |
| `itemInfo.descriptionInfo.extendedDescription.fieldList[].imageInfo.imageUrl` | string | 否 | 图片 URL |
| `itemInfo.descriptionInfo.descriptionType` | string | 否 | 描述类型：normal / extended |
| `itemInfo.isFulfillmentByShopee` | boolean | 否 | 是否为 Shopee 履约商品 |
| `itemInfo.sizeChartId` | integer | 否 | 尺码表模板 ID |
| `modelList` | object | 否 | 全球规格列表（前端修改后的 GetItemDetailVo.modelList，仅传新数据） |
| `modelList.tierVariation` | array<object> | 否 | 层级规格信息 |
| `modelList.tierVariation[].name` | string | 否 | 层级规格名称 |
| `modelList.tierVariation[].optionList` | array<object> | 否 | 层级规格选项列表 |
| `modelList.tierVariation[].optionList[].option` | string | 否 | 层级规格选项值 |
| `modelList.tierVariation[].image` | object | 否 | 层级规格图片 |
| `modelList.tierVariation[].image.imageUrl` | string | 否 | 图片 URL |
| `modelList.tierVariation[].image.imageId` | string | 否 | 图片 ID |
| `modelList.globalModel` | array<object> | 否 | 全球规格列表(SKU列表) |
| `modelList.globalModel[].globalModelId` | integer | 否 | 全球规格 ID |
| `modelList.globalModel[].globalModelSku` | string | 否 | 全球规格 SKU |
| `modelList.globalModel[].priceInfo` | object | 否 | 价格信息 |
| `modelList.globalModel[].priceInfo.originalPrice` | number | 否 | 原价 |
| `modelList.globalModel[].stockInfo` | array<object> | 否 | 库存信息 |
| `modelList.globalModel[].stockInfo[].stockType` | integer | 否 | 库存类型：1 = WMS 在库，2 = 卖家在库 |
| `modelList.globalModel[].stockInfo[].stockLocationId` | string | 否 | 库存位置 ID |
| `modelList.globalModel[].stockInfo[].currentStock` | integer | 否 | 当前库存 |
| `modelList.globalModel[].stockInfo[].normalStock` | integer | 否 | 正常库存 |
| `modelList.globalModel[].stockInfo[].reservedStock` | integer | 否 | 预留库存 |
| `modelList.globalModel[].tierIndex` | array<integer> | 否 | 层级索引 |
| `modelList.globalModel[].weight` | string | 否 | 重量，单位 KG |
| `modelList.globalModel[].dimension` | object | 否 | 包裹尺寸 |
| `modelList.globalModel[].dimension.packageHeight` | integer | 是 | 包裹高度，单位 CM |
| `modelList.globalModel[].dimension.packageLength` | integer | 是 | 包裹长度，单位 CM |
| `modelList.globalModel[].dimension.packageWidth` | integer | 是 | 包裹宽度，单位 CM |
| `modelList.globalModel[].preOrder` | object | 否 | 预售信息 |
| `modelList.globalModel[].preOrder.daysToShip` | integer | 是 | 发货天数（DTS） |
| `modelList.globalModel[].isFulfillmentByShopee` | boolean | 否 | 是否为 FBS 规格 |
| `modelList.standardiseTierVariation` | array<object> | 否 | 标准化层级规格信息 |
| `modelList.standardiseTierVariation[].variationId` | integer | 否 | 标准化层级规格 ID |
| `modelList.standardiseTierVariation[].variationName` | string | 否 | 标准化层级规格名称 |
| `modelList.standardiseTierVariation[].variationGroupId` | integer | 否 | 标准化层级规格组 ID |
| `modelList.standardiseTierVariation[].variationOptionList` | array<object> | 否 | 标准化层级规格选项列表 |
| `modelList.standardiseTierVariation[].variationOptionList[].variationOptionId` | integer | 否 | 标准化层级规格选项 ID |
| `modelList.standardiseTierVariation[].variationOptionList[].variationOptionName` | string | 否 | 标准化层级规格选项名称 |
| `modelList.standardiseTierVariation[].imageId` | string | 否 | 图片 ID |
| `modelList.standardiseTierVariation[].imageUrl` | string | 否 | 图片 URL |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 获取属性列表

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/get_attribute_list`
- 类型：读
- 原文：[480434404e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434404e0.md)（本地 raw/480434404e0_获取属性列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 否 | 店铺ID |
| `site` | string | 否 | 站点 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.attributes` | array<object> | 否 | 属性列表 |
| `data.attributes[].attributeId` | integer | 否 |  |
| `data.attributes[].originalAttributeName` | string | 否 |  |
| `data.attributes[].displayAttributeName` | string | 否 |  |
| `data.attributes[].isMandatory` | boolean | 否 |  |
| `data.attributes[].inputValidationType` | string | 否 |  |
| `data.attributes[].formatType` | string | 否 |  |
| `data.attributes[].inputType` | string | 否 |  |
| `data.attributes[].attributeUnit` | array<string> | 否 |  |
| `data.attributes[].attributeValueList` | array<object> | 否 |  |
| `data.attributes[].attributeValueList[].valueId` | integer | 否 |  |
| `data.attributes[].attributeValueList[].originalValueName` | string | 否 |  |
| `data.attributes[].attributeValueList[].displayValueName` | string | 否 |  |
| `data.attributes[].attributeValueList[].parentAttributeList` | array<object> | 否 |  |
| `data.attributes[].attributeValueList[].parentAttributeList[].parentAttributeId` | integer | 否 |  |
| `data.attributes[].attributeValueList[].parentAttributeList[].parentValueId` | integer | 否 |  |
| `data.attributes[].maxInputValueNumber` | integer | 否 |  |
| `data.attributes[].introduction` | string | 否 |  |
| `data.attributes[].mandatoryRegion` | array<string> | 否 |  |
| `data.lang` | string | 否 | 语言 |


---

### 获取全球店铺类目尺寸模板列表

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/get_shop_id_and_size_chart_list_map`
- 类型：读
- 原文：[480434405e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434405e0.md)（本地 raw/480434405e0_获取全球店铺类目尺寸模板列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |
| `cid` | integer | 是 | 类目ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndSizeChartListMap` | object | 否 | 店铺ID与尺寸模板列表映射 |


---

### 上传商品视频

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/upload_item_video`
- 类型：写
- 原文：[480434406e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434406e0.md)（本地 raw/480434406e0_上传商品视频.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `sourceVideoUrl` | string | 是 | 视频URL |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.videoUploadId` | integer | 否 |  |


---

### 同步产品

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/rsync_item_single`
- 类型：写
- 原文：[480434407e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434407e0.md)（本地 raw/480434407e0_同步产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemIds` | array<string> | 是 | 平台产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.successPlatformItemIds` | array<string> | 否 |  |
| `data.failedPlatformItemIds` | array<string> | 否 |  |
| `data.errorMap` | object | 否 |  |


---

### 全球产品删除

- 层级：开放平台 > 商品 > 在线产品管理 > Shopee全球在线产品管理
- 方法+路径：`POST /open/v1/product/item/shopee_global/item/delete_item`
- 类型：写
- 原文：[480434408e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434408e0.md)（本地 raw/480434408e0_全球产品删除.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 是 | 店铺ID |
| `platformItemId` | string | 是 | 平台产品ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


## Mercadolibre采集箱>发布产品

### 发布产品

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 发布产品
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/move_collect/save_move_collect_task`
- 类型：写
- 原文：[482757484e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482757484e0.md)（本地 raw/482757484e0_发布产品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array<integer> | 是 | 采集箱详情ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 发布记录列表

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 发布产品
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/move_collect/search_move_collect_list`
- 类型：读
- 原文：[511672449e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511672449e0.md)（本地 raw/511672449e0_发布记录列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(success-发布成功、fail-发布失败、processing-发布中、cancel-已取消) |
| `filter.itemId` | string | 否 | 产品ID |
| `filter.sourceItemId` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.moveCollectDetailList` | array<object> | 否 | 发布记录列表 |
| `data.moveCollectDetailList[].subDetailList` | array<object> | 否 | SKU对应产品发布详情（传统模式） |
| `data.moveCollectDetailList[].subDetailList[].platformItemId` | string | 否 | 对应站点产品ID |
| `data.moveCollectDetailList[].subDetailList[].site` | string | 否 | 对应站点 |
| `data.moveCollectDetailList[].subDetailList[].siteName` | string | 否 | 对应站点别名 |
| `data.moveCollectDetailList[].subDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].subDetailList[].reason` | string | 否 | 发布失败原因 |
| `data.moveCollectDetailList[].subDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].subDetailList[].gmtModified` | string | 否 | 更新时间 |
| `data.moveCollectDetailList[].skuSubDetailList` | array<object> | 否 | SKU对应产品发布详情（UP模式） |
| `data.moveCollectDetailList[].skuSubDetailList[].cbtItemId` | string | 否 | CBT产品ID |
| `data.moveCollectDetailList[].skuSubDetailList[].platformItemId` | string | 否 | 对应站点产品ID |
| `data.moveCollectDetailList[].skuSubDetailList[].site` | string | 否 | 对应站点 |
| `data.moveCollectDetailList[].skuSubDetailList[].siteName` | string | 否 | 对应站点别名 |
| `data.moveCollectDetailList[].skuSubDetailList[].sku` | string | 否 | sku |
| `data.moveCollectDetailList[].skuSubDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].skuSubDetailList[].reason` | string | 否 | 发布失败原因 |
| `data.moveCollectDetailList[].skuSubDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].skuSubDetailList[].gmtModified` | string | 否 | 更新时间 |
| `data.moveCollectDetailList[].moveCollectTaskDetailId` | string | 否 | 发布任务详情ID |
| `data.moveCollectDetailList[].collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.moveCollectDetailList[].shopId` | string | 否 | 店铺ID |
| `data.moveCollectDetailList[].itemNum` | string | 否 | 商品编号 |
| `data.moveCollectDetailList[].cid` | string | 否 | 类目ID |
| `data.moveCollectDetailList[].source` | string | 否 | 来源平台 |
| `data.moveCollectDetailList[].sourceSite` | string | 否 | 来源站点 |
| `data.moveCollectDetailList[].sourceItemId` | string | 否 | 来源商品ID |
| `data.moveCollectDetailList[].title` | string | 否 | 商品标题 |
| `data.moveCollectDetailList[].thumbnail` | string | 否 | 缩略图 |
| `data.moveCollectDetailList[].isTiming` | string | 否 | 是否定时发布 |
| `data.moveCollectDetailList[].status` | string | 否 | 发布状态 |
| `data.moveCollectDetailList[].reason` | string | 否 | 失败原因 |
| `data.moveCollectDetailList[].gmtCreate` | string | 否 | 创建时间 |
| `data.moveCollectDetailList[].gmtModified` | string | 否 | 修改时间 |
| `data.moveCollectDetailList[].platformItemId` | string | 否 | 平台商品ID |
| `data.moveCollectDetailList[].isRenewItem` | boolean | 否 | 是否翻新 |
| `data.moveCollectDetailList[].shopName` | string | 否 | 店铺名称 |
| `data.moveCollectDetailList[].siteName` | string | 否 | 站点名称 |
| `data.moveCollectDetailList[].site` | string | 否 | 站点 |
| `data.moveCollectDetailList[].sourceItemUrl` | string | 否 | 来源商品链接 |
| `data.moveCollectDetailList[].itemEditUrl` | string | 否 | 商品编辑链接 |
| `data.moveCollectDetailList[].breadcrumb` | string | 否 | 类目路径 |
| `data.moveCollectDetailList[].ownerSubAppAccountId` | integer | 否 | 归属子账号ID |
| `data.moveCollectDetailList[].ownerSubAccountAliasName` | string | 否 | 归属子账号名称 |
| `data.total` | integer | 否 | 总数 |


## Mercadolibre采集箱>采集箱

### 获取类目属性规则

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_attribute_rules`
- 类型：读
- 原文：[482753632e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753632e0.md)（本地 raw/482753632e0_获取类目属性规则.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.saleAttributeRules` | array<object> | 否 | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `data.saleAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.saleAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.saleAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.saleAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.saleAttributeRules[].id` | string | 否 | 属性ID |
| `data.saleAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.saleAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.saleAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.saleAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.saleAttributeRules[].values` | array<object> | 否 | 可选值列表,从中选取name |
| `data.saleAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.saleAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.saleAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.saleAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.productAttributeRules` | array<object> | 否 | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `data.productAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.productAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.productAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.productAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.productAttributeRules[].id` | string | 否 | 属性ID |
| `data.productAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.productAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.productAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.productAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.productAttributeRules[].values` | array<object> | 否 | 可选值列表,从中选取name |
| `data.productAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.productAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.productAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.productAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.skuAttributeRules` | array<object> | 否 | SKU属性规则列表，创建产品时需按此规则填写attributes |
| `data.skuAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.skuAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.skuAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.skuAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.skuAttributeRules[].id` | string | 否 | 属性ID |
| `data.skuAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.skuAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.skuAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.skuAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.skuAttributeRules[].values` | array<object> | 否 | 可选值列表,从中选取name |
| `data.skuAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.skuAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.skuAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.skuAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |


---

### 获取类目配置

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_setting`
- 类型：读
- 原文：[482753633e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753633e0.md)（本地 raw/482753633e0_获取类目配置.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 是 | 类目ID |
| `shopId` | integer | 是 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.catalogDomain` | string | 否 | 类目domain |
| `data.maxDescriptionLength` | integer | 否 | 类目最大描述长度 |
| `data.maxTitleLength` | integer | 否 | 类目最大标题长度 |


---

### 获取尺码表domain列表

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_domain_list`
- 类型：读
- 原文：[482753635e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753635e0.md)（本地 raw/482753635e0_获取尺码表domain列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 否 | 店铺ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.domains` | array<object> | 否 | domain列表 |
| `data.domains[].domainId` | string | 否 | domain ID |
| `data.domains[].domainName` | string | 否 | domain英文名称 |
| `data.domains[].domainZhName` | string | 否 | domain中文名称 |


---

### 获取尺码表表头和主属性信息

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_attribute_info`
- 类型：读
- 原文：[482753636e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753636e0.md)（本地 raw/482753636e0_获取尺码表表头和主属性信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `domainId` | string | 是 | 尺码表domain ID(对应getSizeChartDomainList返回的domainId) |
| `genderId` | string | 是 | 1.类目属性中的性别ID(getSiteCollectItemInfo中attributes->GENDER属性values中的name值； 2.在获取类目属性规则接口返回数据的productAttributeRules中对应GENDER属性规则values值的id |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.mainAttributeList` | object | 否 | 主属性列表，格式{MANUFACTURER_SIZE:{name:"Manufacturer size",nameZh:"自定义尺码",unit:"US"}} |
| `data.measureTypeList` | object | 否 | 测量属性列表，格式{BODY_MEASURE:{name:"With body measurements",nameZh:"身体尺寸",relevanceRequired:["FILTRABLE_SIZE","CHEST_CIRCUMFERENCE_FROM"],unit:"US"}} |
| `data.isTopsAndBottoms` | boolean | 否 | 是否为上衣或下装 |


---

### 获取尺码表所需填写属性信息

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_need_attribute_info`
- 类型：读
- 原文：[482753637e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753637e0.md)（本地 raw/482753637e0_获取尺码表所需填写属性信息.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `domainId` | string | 是 | domain ID(对应getSizeChartDomainList返回的domainId) |
| `genderId` | string | 是 | 1.类目属性中的性别ID(getSiteCollectItemInfo中attributes->GENDER属性values中的name值； 2.在获取类目属性规则接口返回数据的productAttributeRules中对应GENDER属性规则values值的id |
| `measureType` | string | 是 | 测量类型(对应getSizeChartAttributeInfo返回的measureTypeList key) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeChartIdAndInfoMap` | object | 否 | 尺码ID和尺码内容映射 |
| `data.equivalencies` | array<string> | 否 | 尺码列表(XL,XXL等) |


---

### 获取授权站点和名称映射

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_auth_site_and_site_name_map`
- 类型：读
- 原文：[482753639e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753639e0.md)（本地 raw/482753639e0_获取授权站点和名称映射.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopId` | integer | 否 | 店铺ID |
| `includeCbt` | integer | 是 | 是否包含CBT全球站点（1是 0否） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.siteAndSiteNameMap` | object | 否 | 站点和站点名称映射，格式:{"AR":"阿根廷","BR":"巴西"} |


---

### 获取商品基本选项

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_item_options`
- 类型：读
- 原文：[482753640e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753640e0.md)（本地 raw/482753640e0_获取商品基本选项.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.weightUnitOptions` | array<object> | 否 | 重量单位选项，key/value 数组，保存到 siteCollectItemInfo.skuMap.weightUnit |
| `data.weightUnitOptions[].key` | string | 否 | 选项键值 |
| `data.weightUnitOptions[].value` | string | 否 | 选项显示文本 |
| `data.warrantyTypeOptions` | array<object> | 否 | 保修类型选项，key/value 数组，保存到 siteCollectItemInfo.warrantyType,siteCollectItemInfo.warrantyTimeUnit |
| `data.warrantyTypeOptions[].key` | string | 否 | 选项键值 |
| `data.warrantyTypeOptions[].value` | string | 否 | 选项显示文本 |
| `data.warrantyTimeUnitOptions` | array<object> | 否 | 保修时间单位选项，key/value 数组，保存到 siteCollectItemInfo.warrantyTimeUnit |
| `data.warrantyTimeUnitOptions[].key` | string | 否 | 选项键值 |
| `data.warrantyTimeUnitOptions[].value` | string | 否 | 选项显示文本 |
| `data.lengthUnitOptions` | array<object> | 否 | 包裹尺寸单位选项，key/value 数组，保存到 siteCollectItemInfo.skuMap.lengthWidthHeightUnit |
| `data.lengthUnitOptions[].key` | string | 否 | 选项键值 |
| `data.lengthUnitOptions[].value` | string | 否 | 选项显示文本 |
| `data.siteAndSupportListingTypeOptions` | object | 否 | 站点和支持产品类型映射,格式:{"BR":[{"label":"经典（Classic）","value":"gold_special"}]} |


---

### 查询尺码表模板列表

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/search_size_chart_template`
- 类型：读
- 原文：[482753641e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753641e0.md)（本地 raw/482753641e0_查询尺码表模板列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |
| `filter` | object | 否 |  |
| `filter.domainId` | string | 否 | 尺码表domain ID(对应getSizeChartDomainList返回的domainId) |
| `filter.genderId` | string | 否 | 类目属性中的性别ID |
| `filter.templateName` | string | 否 | 模板名称（模糊搜索） |
| `pageSize` | integer | 否 | 每页数量 |
| `pageNo` | integer | 否 | 当前页码 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.sizeChartTemplateList` | array<object> | 否 | 尺码表列表 |
| `data.sizeChartTemplateList[].attributes` | array<object> | 否 | 尺码表模板属性列表 |
| `data.sizeChartTemplateList[].attributes[].id` | string | 否 | 属性ID |
| `data.sizeChartTemplateList[].attributes[].values` | array<object> | 否 | 属性值列表 |
| `data.sizeChartTemplateList[].attributes[].values[].id` | string | 否 | 属性值ID |
| `data.sizeChartTemplateList[].attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.sizeChartTemplateList[].chartId` | string | 否 | 平台尺码表ID |
| `data.sizeChartTemplateList[].copySerialNumber` | integer | 否 | 复制模板序列号 |
| `data.sizeChartTemplateList[].domainId` | string | 否 | 尺码表domainId |
| `data.sizeChartTemplateList[].genderId` | string | 否 | 性别ID |
| `data.sizeChartTemplateList[].mainAttributeId` | string | 否 | 主属性ID |
| `data.sizeChartTemplateList[].mainAttribute` | array<object> | 否 | 主属性映射 |
| `data.sizeChartTemplateList[].mainAttribute[].attributes` | array<object> | 否 | 表头英文名称 |
| `data.sizeChartTemplateList[].mainAttribute[].attributes[].siteId` | string | 否 | 站点ID |
| `data.sizeChartTemplateList[].mainAttribute[].attributes[].id` | string | 否 | 主属性属性ID |
| `data.sizeChartTemplateList[].measureType` | string | 否 | 测量类型 |
| `data.sizeChartTemplateList[].names` | object | 否 | 站点ID对应名称映射,格式{MCO:"renzituo"} |
| `data.sizeChartTemplateList[].rows` | array<object> | 否 |  |
| `data.sizeChartTemplateList[].rows[].attributes` | array<object> | 否 | 表头英文名称 |
| `data.sizeChartTemplateList[].rows[].attributes[].id` | string | 否 | 行属性ID |
| `data.sizeChartTemplateList[].rows[].attributes[].values` | array<object> | 否 | 行属性值列表 |
| `data.sizeChartTemplateList[].rows[].id` | string | 否 | 行ID |
| `data.sizeChartTemplateList[].rows[].sites` | array<string> | 否 | 站点ID列表 |
| `data.sizeChartTemplateList[].shopId` | integer | 否 | 店铺ID |
| `data.sizeChartTemplateList[].siteId` | string | 否 | 站点ID |
| `data.sizeChartTemplateList[].templateName` | string | 否 | 尺码模板名称 |
| `data.sizeChartTemplateList[].type` | string | 否 | 尺码模板类型 |
| `data.total` | integer | 否 | 总数 |


---

### 获取采集箱详情

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_site_collect_item_info`
- 类型：读
- 原文：[482753644e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753644e0.md)（本地 raw/482753644e0_获取采集箱详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

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
| `data.saleAttributeRules` | array<object> | 否 | 销售属性规则列表，创建产品时需按此规则填写saleAttributes |
| `data.saleAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.saleAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.saleAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.saleAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.saleAttributeRules[].id` | string | 否 | 属性ID |
| `data.saleAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.saleAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.saleAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.saleAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.saleAttributeRules[].values` | array<object> | 否 | 可选值列表,从中选取name |
| `data.saleAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.saleAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.saleAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.saleAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.productAttributeRules` | array<object> | 否 | 产品属性规则列表，创建产品时需按此规则填写attributes |
| `data.productAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.productAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.productAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.productAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.productAttributeRules[].id` | string | 否 | 属性ID |
| `data.productAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.productAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.productAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.productAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.productAttributeRules[].values` | array<object> | 否 | 可选值列表,从中选取name |
| `data.productAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.productAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.productAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.productAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.skuAttributeRules` | array<object> | 否 | SKU属性规则列表，创建产品时需按此规则填写attributes |
| `data.skuAttributeRules[].attributeGroupId` | string | 否 | 属性组ID,暂无用 |
| `data.skuAttributeRules[].attributeGroupName` | string | 否 | 属性组名称,暂无用 |
| `data.skuAttributeRules[].displayName` | string | 否 | 属性显示名称 |
| `data.skuAttributeRules[].hierarchy` | string | 否 | 层级(枚举值:CHILD_DEPENDENT-子属性,PARENT_PK-必填主属性,FAMILY-选填主属性,ITEM-前台展示属性) |
| `data.skuAttributeRules[].id` | string | 否 | 属性ID |
| `data.skuAttributeRules[].name` | string | 否 | 属性英文名称，如"Color"等 |
| `data.skuAttributeRules[].relevance` | integer | 否 | 属性权重(1:核心属性,2:次级属性，3:选填属性) |
| `data.skuAttributeRules[].tags` | object | 否 | 标签映射(hidden：是否为隐藏属性,readOnly：是否为只读属性,multivalued：是否为多值属性,allowVariations：是否为变体属性,definesPicture：是否能定义图片,required：是否为必填属性,catalogRequired:readOnly或hidden为false时catalogRequired为true必填,gridFilter:暂无用) |
| `data.skuAttributeRules[].valueType` | string | 否 | 属性类型(list:列表类型,string:字符串类型,grid_id:尺码表网格id,boolean:布尔类型) |
| `data.skuAttributeRules[].values` | array<object> | 否 | 可选值列表,从中选取name |
| `data.skuAttributeRules[].values[].id` | string | 否 | 选项id |
| `data.skuAttributeRules[].values[].displayName` | string | 否 | 选项显示名称 |
| `data.skuAttributeRules[].values[].name` | string | 否 | 选项英文名称 |
| `data.skuAttributeRules[].values[].metadata` | object | 否 | 属性值规则(rgb:颜色RGB值，parentId：父属性值ID，value：布尔值) |
| `data.siteCollectItemInfo` | object | 否 | 站点采集箱数据 |
| `data.siteCollectItemInfo.title` | string | 否 | 商品标题 |
| `data.siteCollectItemInfo.itemNum` | string | 否 | 非服饰类货号 |
| `data.siteCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（品牌/型号等） |
| `data.siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `data.siteCollectItemInfo.attributes[].valueType` | string | 否 | 属性数据类型 |
| `data.siteCollectItemInfo.attributes[].values` | array<object> | 否 | 行属性值列表 |
| `data.siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `data.siteCollectItemInfo.cateList` | array<string> | 否 | 类目面包屑列表 |
| `data.siteCollectItemInfo.firstSkuKey` | string | 否 | 第一个SKU的key,对应skuMap中的key第一个分号数据:例如 ";0a310071;502c632b;"中的";0a310071;" |
| `data.siteCollectItemInfo.originPrice` | number | 否 | 原始价格 |
| `data.siteCollectItemInfo.price` | number | 否 | 价格 |
| `data.siteCollectItemInfo.cid` | string | 否 | 类目ID |
| `data.siteCollectItemInfo.notes` | string | 否 | 商品备注/描述 |
| `data.siteCollectItemInfo.notesFull` | string | 否 | 商品完整备注/描述 |
| `data.siteCollectItemInfo.warrantyType` | string | 否 | 保修类型 |
| `data.siteCollectItemInfo.warrantyTime` | string | 否 | 保修时长 |
| `data.siteCollectItemInfo.warrantyTimeUnit` | string | 否 | 保修时长单位 |
| `data.siteCollectItemInfo.sourceImgUrls` | array<string> | 否 | 原始图片URL列表 |
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
| `data.siteCollectItemInfo.sourceList` | array<object> | 否 | 货源列表 |
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
| `data.siteCollectItemInfo.siteAndListingTypeList` | array<object> | 否 | 站点与刊登类型列表 |
| `data.siteCollectItemInfo.siteAndListingTypeList[].site` | string | 否 | 站点标识 |
| `data.siteCollectItemInfo.siteAndListingTypeList[].listingType` | string | 否 | 刊登类型 |
| `data.siteCollectItemInfo.siteAndTitleList` | array<object> | 否 | 站点与标题列表 |
| `data.siteCollectItemInfo.siteAndTitleList[].site` | string | 否 | 站点标识 |
| `data.siteCollectItemInfo.siteAndTitleList[].title` | string | 否 | 站点商品标题 |
| `data.siteCollectItemInfo.pricingMode` | string | 否 | 售价模式 |
| `data.siteCollectItemInfo.shopId` | string | 否 | 店铺ID |
| `data.siteCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表(如: 颜色/尺码) |
| `data.siteCollectItemInfo.saleAttributes[].name` | string | 否 | 销售属性名称(如: Color, Size) |
| `data.siteCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 销售属性值列表 |
| `data.siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识key |
| `data.siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 销售属性值名称 |
| `data.siteCollectItemInfo.sites` | array<string> | 否 | 已选择的站点列表 |
| `data.siteCollectItemInfo.siteAndPriceMap` | object | 否 | 站点价格映射 格式{ "AR": 5.73, "BR": 200, "CL": 300, "CO": 400, "MX": 500, "MX(Full)": 11.32, "UY": 5.73 } 或{} |
| `data.siteCollectItemInfo.skuMap` | object | 否 | SKU映射表,key为SKU组合key(如";0a310071;502c632b;"),value为SKU详情 |
| `data.siteCollectItemInfo.hasSaveSite` | integer | 否 | 是否已保存站点 |
| `data.siteCollectItemInfo.saveDetailTs` | integer | 否 | 保存明细时间戳 |
| `data.siteCollectItemInfo.hasSavePrice` | integer | 否 | 是否已保存价格 |
| `data.siteCollectItemInfo.site` | string | 否 | 站点标识 |
| `data.siteCollectItemInfo.registrationType` | string | 否 | 注册类型 |


---

### 创建采集箱商品

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/create_collect_box_item`
- 类型：写
- 原文：[482753646e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753646e0.md)（本地 raw/482753646e0_创建采集箱商品.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `siteCollectItemInfo` | object | 是 | 站点模式数据，各字段用途详见 SiteCollectItemInfoForSaveRo 注释。 cid 用于校验属性规则和模特配置，各枚举字段取值参考 getItemOptions / getCategoryAttributeRules 接口 |
| `siteCollectItemInfo.price` | number | 是 | 价格 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string | 否 | 商品备注/描述 |
| `siteCollectItemInfo.warrantyType` | string | 是 | 保修类型(sellerWarranty:卖家保修,factoryWarranty:工厂保修,noWarranty:无保修) |
| `siteCollectItemInfo.warrantyTime` | integer | 是 | 保修时长 |
| `siteCollectItemInfo.warrantyTimeUnit` | string | 是 | 保修时长单位(days:天,years:年,months:月) |
| `siteCollectItemInfo.videoUrl` | string | 否 | 视频URL |
| `siteCollectItemInfo.sourceList` | array<object> | 否 | 货源列表 |
| `siteCollectItemInfo.sourceList[].source` | string | 否 | 货源来源标识 |
| `siteCollectItemInfo.sourceList[].sourceItemId` | string | 否 | 货源商品ID |
| `siteCollectItemInfo.sourceList[].sourceSite` | string | 否 | 货源站点 |
| `siteCollectItemInfo.sourceList[].sourceItemUrl` | string | 否 | 货源商品URL |
| `siteCollectItemInfo.detailId` | string | 否 | 明细ID |
| `siteCollectItemInfo.firstSkuKey` | string | 否 | 第一个SKU的key,对应skuMap中的key |
| `siteCollectItemInfo.siteAndListingTypeList` | array<object> | 否 | 站点与刊登类型列表 |
| `siteCollectItemInfo.siteAndListingTypeList[].site` | string | 否 | 站点标识 |
| `siteCollectItemInfo.siteAndListingTypeList[].listingType` | string | 否 | 刊登类型 |
| `siteCollectItemInfo.siteAndTitleList` | array<object> | 否 | 站点与标题列表 |
| `siteCollectItemInfo.siteAndTitleList[].site` | string | 否 | 站点标识 |
| `siteCollectItemInfo.siteAndTitleList[].title` | string | 否 | 站点商品标题 |
| `siteCollectItemInfo.pricingMode` | string | 否 | 售价模式(sellPrice:售价, netProceeds:净收益) |
| `siteCollectItemInfo.shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（品牌/型号等） |
| `siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 否 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表(如: 颜色/尺码) |
| `siteCollectItemInfo.saleAttributes[].name` | string | 否 | 销售属性名称(如: Color, Size) |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 销售属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | integer | 否 | SKU标识key |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 销售属性值名称 |
| `siteCollectItemInfo.saleAttributes[].id` | string | 否 | 销售属性ID(如: COLOR, SIZE) |
| `siteCollectItemInfo.sites` | array<string> | 是 | 已选择的站点列表,结构["BR","BR(Full)(Up)"] |
| `siteCollectItemInfo.siteAndPriceMap` | object | 是 | 站点价格映射,结构 {"MX": 100, "AR": 100} |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU映射表,key为SKU组合key,value为SKU详情(当类目规则saleAttributes不为空时必填) |
| `siteCollectItemInfo.hasSaveSite` | integer | 否 | 是否已保存站点(1:是;0:否) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | integer | 否 | 创建成功的采集箱详情ID |


---

### 保存采集箱站点详情

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/save_site_collect_item_info`
- 类型：写
- 原文：[482753647e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753647e0.md)（本地 raw/482753647e0_保存采集箱站点详情.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailId` | integer | 是 | 采集箱详情ID |
| `siteCollectItemInfo` | object | 是 | 站点模式数据 |
| `siteCollectItemInfo.price` | number | 是 | 价格 |
| `siteCollectItemInfo.cid` | string | 是 | 类目ID |
| `siteCollectItemInfo.title` | string | 是 | 商品标题 |
| `siteCollectItemInfo.notes` | string | 否 | 商品备注/描述 |
| `siteCollectItemInfo.warrantyType` | string | 是 | 保修类型(sellerWarranty:卖家保修,factoryWarranty:工厂保修,noWarranty:无保修) |
| `siteCollectItemInfo.warrantyTime` | integer | 是 | 保修时长 |
| `siteCollectItemInfo.warrantyTimeUnit` | string | 是 | 保修时长单位(days:天,years:年,months:月) |
| `siteCollectItemInfo.videoUrl` | string | 否 | 视频URL |
| `siteCollectItemInfo.sourceList` | array<object> | 否 | 货源列表 |
| `siteCollectItemInfo.sourceList[].source` | string | 否 | 货源来源标识 |
| `siteCollectItemInfo.sourceList[].sourceItemId` | string | 否 | 货源商品ID |
| `siteCollectItemInfo.sourceList[].sourceSite` | string | 否 | 货源站点 |
| `siteCollectItemInfo.sourceList[].sourceItemUrl` | string | 否 | 货源商品URL |
| `siteCollectItemInfo.detailId` | string | 否 | 明细ID |
| `siteCollectItemInfo.firstSkuKey` | string | 否 | 第一个SKU的key,对应skuMap中的key |
| `siteCollectItemInfo.siteAndListingTypeList` | array<object> | 否 | 站点与刊登类型列表 |
| `siteCollectItemInfo.siteAndListingTypeList[].site` | string | 否 | 站点标识 |
| `siteCollectItemInfo.siteAndListingTypeList[].listingType` | string | 否 | 刊登类型 |
| `siteCollectItemInfo.siteAndTitleList` | array<object> | 否 | 站点与标题列表 |
| `siteCollectItemInfo.siteAndTitleList[].site` | string | 否 | 站点标识 |
| `siteCollectItemInfo.siteAndTitleList[].title` | string | 否 | 站点商品标题 |
| `siteCollectItemInfo.pricingMode` | string | 否 | 售价模式(sellPrice:售价, netProceeds:净收益) |
| `siteCollectItemInfo.shopId` | string | 是 | 店铺ID |
| `siteCollectItemInfo.attributes` | array<object> | 否 | 商品属性列表（品牌/型号等） |
| `siteCollectItemInfo.attributes[].name` | string | 否 | 属性名称 |
| `siteCollectItemInfo.attributes[].values` | array<object> | 否 | 属性值列表 |
| `siteCollectItemInfo.attributes[].values[].name` | string | 否 | 属性值名称 |
| `siteCollectItemInfo.saleAttributes` | array<object> | 否 | 销售属性列表(如: 颜色/尺码) |
| `siteCollectItemInfo.saleAttributes[].name` | string | 否 | 销售属性名称(如: Color, Size) |
| `siteCollectItemInfo.saleAttributes[].values` | array<object> | 否 | 销售属性值列表 |
| `siteCollectItemInfo.saleAttributes[].values[].skuKey` | string | 否 | SKU标识key |
| `siteCollectItemInfo.saleAttributes[].values[].name` | string | 否 | 销售属性值名称 |
| `siteCollectItemInfo.saleAttributes[].id` | string | 否 | 销售属性ID(如: COLOR, SIZE) |
| `siteCollectItemInfo.sites` | array<string> | 是 | 已选择的站点列表,结构["BR","BR(Full)(Up)"] |
| `siteCollectItemInfo.siteAndPriceMap` | object | 是 | 站点价格映射 |
| `siteCollectItemInfo.skuMap` | object | 否 | SKU映射表,key为SKU组合key,value为SKU详情(当类目规则saleAttributes不为空时必填) |
| `siteCollectItemInfo.hasSaveSite` | integer | 否 | 是否已保存站点(1:是;0:否) |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


---

### 同步店铺尺码表

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/rsync_size_chart_template`
- 类型：写
- 原文：[482753643e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753643e0.md)（本地 raw/482753643e0_同步店铺尺码表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `shopIds` | array<integer> | 是 | 店铺ID列表 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.shopIdAndRsyncRet` | object | 否 | 店铺Id同步结果映射 key 为 shopId，value 为该店铺同步结果。 Map value 为该店铺同步结果，每一项结构如下： -result : 同步结果，success 表示成功，fail 表示失败 -reason : 同步失败原因，如果同步成功则为空 |


---

### 获取采集箱列表

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/search_collect_box_detailList`
- 类型：读
- 原文：[482753630e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753630e0.md)（本地 raw/482753630e0_获取采集箱列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `pageNo` | integer | 是 | 当前页码 |
| `pageSize` | integer | 是 | 每页数量 |
| `filter` | object | 否 | 过滤器 |
| `filter.status` | string | 否 | 状态(notPublished-未发布、timingPublish-定时发布、published-已发布) |
| `filter.filterCidSite` | string | 否 | 过滤类目站点(固定值-CBT) |
| `filter.sourceItemIdKeyword` | string | 否 | 货源ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.collectBoxDetailId` | string | 否 | 采集箱详情ID |
| `data.itemNum` | string | 否 | 商品编号 |
| `data.breadcrumb` | string | 否 | 类目面包屑 |
| `data.cid` | string | 否 | 类目ID |
| `data.globalPrice` | string | 否 | 全球净收益/售价 |
| `data.stock` | string | 否 | 库存 |
| `data.price` | string | 否 | 货源价格 |
| `data.thumbnail` | string | 否 | 缩略图 |
| `data.gmtCreate` | string | 否 | 创建时间 |
| `data.editModel` | string | 否 | 编辑模式 |
| `data.commonCollectBoxDetailId` | string | 否 | 公共采集箱详情ID |
| `data.appAccountId` | string | 否 | 应用账户ID |
| `data.subAppAccountId` | string | 否 | 子应用账户ID |
| `data.platform` | string | 否 | 平台 |
| `data.title` | string | 否 | 商品标题 |
| `data.remark` | string | 否 | 备注 |
| `data.copyType` | string | 否 | 复制类型 |
| `data.collectBoxGroupId` | string | 否 | 采集箱分组ID |
| `data.collectBoxDetailShop` | object | 否 | 预发布店铺信息 |
| `data.collectBoxDetailShop.shopId` | string | 否 | 店铺ID |
| `data.collectBoxDetailShop.pricingMode` | string | 否 | 售价模式 |
| `data.collectBoxDetailShop.siteAndMaxPriceMap` | object | 否 | 站点最大价格映射 |
| `data.collectBoxDetailShop.siteAndMinPriceMap` | object | 否 | 站点最小价格映射 |
| `data.collectBoxDetailShop.siteAndPriceMap` | object | 否 | 站点价格映射 |
| `data.collectBoxDetailShop.sites` | array<string> | 否 | 已选择的站点列表(BR(Full)(Up)、BR(Full)等) |


---

### 获取类目列表

- 层级：开放平台 > 商品 > Mercadolibre采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/mercadolibre/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[484103119e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484103119e0.md)（本地 raw/484103119e0_获取类目列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `site` | string | 是 | 美客多站点，固定值“CBT” |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.cateTree` | object | 否 | 分类树 Map（key=cid, value=分类节点） |


## AI公共服务>图片处理

### AI白底图

- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/picture/matting/auto_ai_matting_multi`
- 类型：处理(生成内容)
- 原文：[482201652e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482201652e0.md)（本地 raw/482201652e0_AI白底图.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imgUrls` | array<string> | 是 | 图片URL列表，（不计重复） |
| `imageScene` | integer | 是 | 图片应用场景 1-产品图片 2-描述图片 3-sku或产品属性图片 4-证书图片 5-尺寸图图片 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.imgMattingList` | array<object> | 否 | AI白底图结果列表 |
| `data.imgMattingList[].result` | string | 否 | 单张AI白底图结果（success/fail） |
| `data.imgMattingList[].width` | integer | 否 | 图片宽度 |
| `data.imgMattingList[].height` | integer | 否 | 图片高度 |
| `data.imgMattingList[].md5` | string | 否 | 图片MD5 |
| `data.imgMattingList[].newImageUrl` | string | 否 | 抠图后图片URL |
| `data.imgMattingList[].oriImageUrl` | string | 否 | 原始图片URL |


---

### AI智能消除

- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/common/image_removal/remove_image`
- 类型：处理(生成内容)
- 原文：[482190901e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190901e0.md)（本地 raw/482190901e0_AI智能消除.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array<string> | 是 | 待消除图片URL列表 |
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
| `removeConfig.removeAreas` | array<string> | 是 | 消除区域，可选值：background（背景区域）、subject（主体区域） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.imageRemovalUrlResultList` | array<object> | 否 | 消除结果列表 |
| `data.imageRemovalUrlResultList[].result` | string | 否 | 单张消除结果（success/fail） |
| `data.imageRemovalUrlResultList[].reason` | string | 否 | 单张消除失败原因 |
| `data.imageRemovalUrlResultList[].oriImageUrl` | string | 否 | 原始图片URL |
| `data.imageRemovalUrlResultList[].newImageUrl` | string | 否 | 消除后图片URL |
| `data.imageRemovalUseNum` | integer | 否 | 图片消除使用次数 |
| `data.appResourceCode` | string | 否 | 应用资源编码 |
| `data.appResourceUseNum` | integer | 否 | 应用资源使用次数 |
| `data.freeUseNum` | integer | 否 | 免费使用次数 |


---

### 搜索水印列表

- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/item/tiktok/watermark/search_watermark_list`
- 类型：读
- 原文：[482200257e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482200257e0.md)（本地 raw/482200257e0_搜索水印列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `watermarkIds` | string | 否 | 水印ID列表，多个以英文逗号分隔 |
| `watermarkName` | string | 否 | 水印名称（支持模糊搜索） |
| `watermarkSubType` | string | 是 | 水印子类型（normal=普通水印，byLayer=描述图水印） |
| `pageNo` | integer | 是 | $pageNo |
| `pageSize` | integer | 是 | 每页数量 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.watermarkList` | array<object> | 否 | 水印列表 |
| `data.watermarkList[].watermarkId` | string | 否 | 水印ID |
| `data.watermarkList[].appAccountId` | string | 否 | 应用账号ID |
| `data.watermarkList[].platform` | string | 否 | 平台 |
| `data.watermarkList[].watermarkImageUrl` | string | 否 | 水印图片URL |
| `data.watermarkList[].watermarkType` | string | 否 | 水印类型 |
| `data.watermarkList[].watermarkSubType` | string | 否 | 水印子类型 |
| `data.watermarkList[].name` | string | 否 | 水印名称 |
| `data.total` | integer | 否 | 总数 |


---

### 图片打水印

- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/item/tiktok/watermark/watermark_images`
- 类型：处理(生成内容)
- 原文：[482200258e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482200258e0.md)（本地 raw/482200258e0_图片打水印.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array<string> | 是 | 需要打水印的图片链接列表 |
| `watermarkId` | string | 是 | 用于打水印的水印ID |
| `collectBoxDetailId` | integer | 否 | 采集箱详情ID 若有就传 |
| `isAutoMatchImageSize` | boolean | 是 | 是否自动匹配图片大小 若开启，添加水印时将自动适配原图尺寸比例；若关闭，添加水印后输出的图片尺寸默认为 800×800 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.watermarkDetail` | array<object> | 否 | 打水印结果列表，每项对应一张图片的处理结果 |
| `data.watermarkDetail[].imageUrl` | string | 否 | 原图片URL |
| `data.watermarkDetail[].result` | string | 否 | 打水印结果（success: 成功；fail: 失败） |
| `data.watermarkDetail[].watermarkImageUrl` | string | 否 | 打完水印后的图片URL，result 为 success 时有值 |
| `data.watermarkDetail[].msg` | string | 否 | 失败原因，result 为 fail 时有值 |


---

### 获取支持的翻译语言配置

- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/common/translate/get_support_language_config`
- 类型：读
- 原文：[484286513e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286513e0.md)（本地 raw/484286513e0_获取支持的翻译语言配置.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supportLanguageConfig` | object | 否 | 支持的语言配置 结构为 {平台: {类型: {源语言: [目标语言列表]}}} 平台可选值：aeAi / tosoiot / ykt 类型可选值：realTime（实时翻译）/ idle（闲时翻译） 源语言和目标语言为语言编码，如 zh、en、ja 等 示例：{"ali": {"realTime": {"zh": ["en", "ja"], "en": ["zh", "ja"]}}} |


---

### 图片翻译

- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/common/translate/translate_image`
- 类型：处理(生成内容)
- 原文：[484286514e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286514e0.md)（本地 raw/484286514e0_图片翻译.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imageUrls` | array<string> | 是 | 待翻译图片URL列表 |
| `sourceLang` | string | 是 | 源语言编码（如 zh、en），可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig |
| `targetLang` | string | 是 | 目标语言编码，可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig |
| `translatePlatform` | string | 是 | 翻译平台（ali / aeAi / tosoiot / ykt），可选值见 getSupportLanguageConfig 返回的 supportLanguageConfig 的键 |
| `noTranslateImageTextOptions` | array<string> | 否 | 不翻译的图片文字选项，可选值：textInTheProduct（不翻译产品文案）、brand（不翻译品牌），不传则都翻译 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.translateImageUrlResultList` | array<object> | 否 | 翻译成功结果列表 |
| `data.translateImageUrlResultList[].oriImageUrl` | string | 否 | 原始图片URL |
| `data.translateImageUrlResultList[].newImageUrl` | string | 否 | 翻译后图片URL |
| `data.translateImageUrlResultList[].result` | string | 否 | 单张翻译结果（success/fail） |
| `data.translateImageUrlErrorResultList` | array<object> | 否 | 翻译失败结果列表 |
| `data.translateImageUrlErrorResultList[].failImageCount` | integer | 否 | 失败图片数量 |
| `data.translateImageUrlErrorResultList[].failImageUrls` | array<string> | 否 | 失败图片URL列表 |
| `data.translateImageUrlErrorResultList[].reason` | string | 否 | 失败原因 |


## AI公共服务>AI润色

### AI生成产品信息（标题/描述）

- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/generate_product_info`
- 类型：处理(生成内容)
- 原文：[482190902e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190902e0.md)（本地 raw/482190902e0_AI生成产品信息（标题_描述）.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `generateTypeList` | array<string> | 是 | 生成类型列表 必传，可选值： title-生成标题 notes-生成描述 |
| `functionModule` | string | 是 | 功能模块 必传，可选值： createCollectBox-手动创建采集箱 editCollectBox-编辑采集箱 createItem-手动创建在线产品 editItem-编辑在线产品 |
| `functionModuleProductId` | integer | 否 | 功能模块产品ID 当functionModule为editCollectBox/editItem时必传 |
| `platform` | string | 是 | 平台 |
| `aiName` | string | 是 | AI名称 （使用接口 get_ai_name_list 获取的name） |
| `title` | string | 是 | 原始标题 |
| `originalContent` | string | 否 | 原始描述内容（生成描述时使用） |
| `titleLengthLimit` | integer | 否 | 标题长度限制 |
| `languageName` | string | 是 | 目标语言名称（使用接口 get_language_name_code_map 获取的code） |
| `keywordsList` | array<string> | 否 | 关键词列表 |
| `negativeWordsList` | array<string> | 否 | 排除词列表 |
| `categoryName` | string | 否 | 类目名称 |
| `site` | string | 否 | 站点 |
| `cid` | string | 否 | 类目ID |
| `imageInfoList` | array<object> | 否 | 图片信息列表 |
| `imageInfoList[].imageUrl` | string | 是 | 图片URL |
| `imageInfoList[].imageSource` | string | 否 | 图片来源 可选值：productImage-产品图片 otherImage-其他图片 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.titleResult` | object | 否 | 标题生成结果 |
| `data.titleResult.result` | string | 否 | 结果状态：success/fail |
| `data.titleResult.contents` | array<string> | 否 | 标题内容列表 |
| `data.notesResult` | object | 否 | 描述生成结果 |
| `data.notesResult.result` | string | 否 | 结果状态：success/fail |
| `data.notesResult.contents` | array<string> | 否 | 描述内容列表 |


---

### AI生成支持的语言map

- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/get_language_name_code_map`
- 类型：处理(生成内容)
- 原文：[482190903e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190903e0.md)（本地 raw/482190903e0_AI生成支持的语言map.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.languageNameCodeMap` | object | 否 | 语言名称与语言代码的映射 key: 语言名称（如"繁体中文"、"泰语"） value: 语言代码（如"zh-TW"、"th"） |


---

### 获取支持的AI名称列表

- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/get_generate_product_info_support_ai_name_list`
- 类型：读
- 原文：[482190904e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190904e0.md)（本地 raw/482190904e0_获取支持的AI名称列表.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.aiNameList` | array<string> | 否 | 支持的AI名称列表 可选值：deepSeekR1/douBao1.6/tongYiQianWen |


---

### AI润色销售规格

- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/generate_sku_spec_name`
- 类型：处理(生成内容)
- 原文：[484286515e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286515e0.md)（本地 raw/484286515e0_AI润色销售规格.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `platform` | string | 是 | 平台（目前只支持tiktok） |
| `title` | string | 否 | 原始标题（作为AI润色上下文） |
| `aiName` | string | 是 | AI模型名称（目前只支持 douBao1.6） |
| `languageName` | string | 否 | 目标语言名称（取值见 getLanguageNameCodeMap 接口，默认"当前语言"） |
| `functionModule` | string | 是 | 功能模块，可选值：createCollectBox / editCollectBox / createItem / editItem |
| `skuPropertyList` | array<object> | 是 | SKU属性列表 |
| `skuPropertyList[].attrName` | string | 否 | 属性名称（如 Color、规格） |
| `skuPropertyList[].attrId` | string | 否 | 属性ID（可为空字符串） |
| `skuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 每项包含 attrValueId/attrValue/imgUrl/supplementarySkuImageUrls |
| `skuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `skuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `skuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值主图URL（无图时为空字符串） |
| `skuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 否 | 补充SKU图片URL列表 |
| `productId` | integer | 否 | 产品ID（functionModule 为 editCollectBox / editItem 时传入） |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.newSkuPropertyList` | array<object> | 否 | AI润色后的SKU规格列表 格式：[{"name": "Color", "valueList": ["Red", "Blue"]}, ...] |
| `data.newSkuPropertyList[].attrName` | string | 否 | 属性名称（如 Color、规格） |
| `data.newSkuPropertyList[].attrId` | string | 否 | 属性ID（可为空字符串） |
| `data.newSkuPropertyList[].attrValueList` | array<object> | 否 | 属性值列表 每项包含 attrValueId/attrValue/imgUrl/supplementarySkuImageUrls |
| `data.newSkuPropertyList[].attrValueList[].attrValueId` | string | 否 | 属性值ID |
| `data.newSkuPropertyList[].attrValueList[].attrValue` | string | 否 | 属性值名称 |
| `data.newSkuPropertyList[].attrValueList[].imgUrl` | string | 否 | 属性值主图URL（无图时为空字符串） |
| `data.newSkuPropertyList[].attrValueList[].supplementarySkuImageUrls` | array<string> | 否 | 补充SKU图片URL列表 |
| `data.reasoningContent` | string | 否 | AI思考过程内容（部分AI模型返回的推理过程） |
| `data.openaiRequestLogId` | integer | 否 | AI请求日志ID（对应历史记录ID，默认0） |


## 图片空间

### 通过图片URL上传图片到图片空间

- 层级：开放平台 > 商品 > 图片空间
- 方法+路径：`POST /open/v1/product/picture/picture_space/upload_picture_link`
- 类型：写
- 原文：[519663381e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/519663381e0.md)（本地 raw/519663381e0_通过图片URL上传图片到图片空间.md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `imgUrl` | string | 是 | 图片URL |
| `scene` | string | 是 | 图片场景，产品：product，分销：distributionGoods，仓库产品：stockGoods |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.appPictureId` | integer | 否 | 图片空间中的图片ID，成功时有值 |
| `data.picturePath` | string | 否 | 上传后的图片URL，成功时有值 |
| `data.width` | integer | 否 | 图片宽度，成功时有值 |
| `data.height` | integer | 否 | 图片高度，成功时有值 |
| `data.md5` | string | 否 | 图片MD5，成功时有值 |

