# 获取店铺运费模板


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_freight_template`
- 类型：读
- 原文：[477347610e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347610e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

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
