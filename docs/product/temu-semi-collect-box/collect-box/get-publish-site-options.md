# 获取发布站点选项


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_publish_site_options`
- 类型：读
- 原文：[477347609e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347609e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.publishSiteOptions` | array&lt;object> | 否 | 发布站点选项列表，用于渲染 publishSiteList 下拉框。 将选中项的 key 填入 publishSiteList； 若选择了 EU（欧盟地区），还需从 getEuropeanRegionSiteList 中选取子站点填入 publishEuSiteList， 且 publishEuSiteList 不能少于 2 个 |
| `data.publishSiteOptions[].key` | string | 否 | 站点编码，填入 publishSiteList（如 US、EU、DE） |
| `data.publishSiteOptions[].value` | string | 否 | 站点中文名，用于展示（如 美国站、欧盟地区） |
| `data.getEuropeanRegionSiteList` | array&lt;object> | 否 | 欧盟子站点列表，用于渲染 publishEuSiteList 多选框。 仅当 publishSiteList 包含 EU 时需要填写； 将选中项的 site 填入 publishEuSiteList，isOpen 为 false 的子站点不可选 |
| `data.getEuropeanRegionSiteList[].site` | string | 否 | 欧盟子站点编码（如 DE、FR、IT），填入 publishEuSiteList |
| `data.getEuropeanRegionSiteList[].name` | string | 否 | 子站点中文名，用于展示（如 德国、法国） |
| `data.getEuropeanRegionSiteList[].siteId` | integer | 否 | 站点ID |
| `data.getEuropeanRegionSiteList[].isOpen` | boolean | 否 | 是否已开放，false 时前端置灰不可选 |
| `data.siteIdAndSiteMap` | object | 否 | siteId → 站点编码映射，key 为 siteId，value 为站点编码（如 US、DE） |
