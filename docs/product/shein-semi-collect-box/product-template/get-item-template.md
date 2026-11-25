# 获取产品模板详情


- 层级：开放平台 > 商品 > SHEIN半托采集箱 > 产品模板
- 方法+路径：`POST /open/v1/product/collect_box/shein_choice/item_template/get_item_template`
- 类型：读
- 原文：[537697879e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/537697879e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `itemTemplateId` | integer | 是 | 模板ID |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.itemTemplateData` | object | 否 | 模板详情 |
| `data.itemTemplateData.itemTemplateId` | integer | 否 | 模板ID |
| `data.itemTemplateData.appAccountId` | integer | 否 | 主账号ID |
| `data.itemTemplateData.subAppAccountId` | integer | 否 | 子账号ID |
| `data.itemTemplateData.platform` | string | 否 | 平台 |
| `data.itemTemplateData.shopId` | integer | 否 | 店铺ID |
| `data.itemTemplateData.name` | string | 否 | 模板名称 |
| `data.itemTemplateData.cid` | string | 否 | 类目ID |
| `data.itemTemplateData.copyNum` | integer | 否 | 复制次数 |
| `data.itemTemplateData.sites` | array&lt;string> | 否 | 站点列表 |
| `data.itemTemplateData.registrationType` | string | 否 | 产品类型 |
| `data.itemTemplateData.title` | string | 否 | 标题模块 |
| `data.itemTemplateData.attribute` | object | 否 | 属性模块 |
| `data.itemTemplateData.attribute.attributes` | array&lt;object> | 否 | 属性列表 |
| `data.itemTemplateData.attribute.cid` | string | 否 | 类目ID |
| `data.itemTemplateData.package` | object | 否 | 包装模块 |
| `data.itemTemplateData.package.weight` | number | 否 | 重量 |
| `data.itemTemplateData.package.width` | number | 否 | 宽 |
| `data.itemTemplateData.package.height` | number | 否 | 高 |
| `data.itemTemplateData.package.length` | number | 否 | 长 |
| `data.itemTemplateData.stopPurchase` | integer | 否 | 采购状态模块 |
| `data.itemTemplateData.gmtCreate` | string | 否 | 创建时间 |
| `data.itemTemplateData.gmtModified` | string | 否 | 更新时间 |
