# 获取尺码模板列表


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/collect_box/get_size_template_list`
- 类型：读
- 原文：[471545331e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545331e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

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
| `data.sizeTemplateList` | array&lt;object> | 否 | 尺码表模板列表，先选择一个模板，再取其sizeTemplateId调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `data.sizeTemplateList[].sizeTemplateId` | string | 否 | 尺码表模板ID，用于调用getSizeChartsBySizeTemplateId获取尺码表详情 |
| `data.sizeTemplateList[].name` | string | 否 | 模板名称 |
| `data.sizeTemplateList[].sizeTemplateSource` | string | 否 | 模板来源 |
| `data.minSizeChartNum` | integer | 否 | 最少尺码表数量，创建产品时需要填写的尺码表数量 |
| `data.classType` | integer | 否 | 是否需要多尺码表 0否 1是 为1是 需要填写重点展示部件 collectShowSizeTemplateIds |
