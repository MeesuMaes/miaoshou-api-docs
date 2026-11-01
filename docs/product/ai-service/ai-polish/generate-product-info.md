# AI生成产品信息（标题/描述）


- 层级：开放平台 > 商品 > AI公共服务 > AI润色
- 方法+路径：`POST /open/v1/product/common/open_ai/generate_product_info`
- 类型：处理(生成内容)
- 原文：[482190902e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190902e0.md).md）

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `generateTypeList` | array&lt;string> | 是 | 生成类型列表 必传，可选值： title-生成标题 notes-生成描述 |
| `functionModule` | string | 是 | 功能模块 必传，可选值： createCollectBox-手动创建采集箱 editCollectBox-编辑采集箱 createItem-手动创建在线产品 editItem-编辑在线产品 |
| `functionModuleProductId` | integer | 否 | 功能模块产品ID 当functionModule为editCollectBox/editItem时必传 |
| `platform` | string | 是 | 平台 |
| `aiName` | string | 是 | AI名称 （使用接口 get_ai_name_list 获取的name） |
| `title` | string | 是 | 原始标题 |
| `originalContent` | string | 否 | 原始描述内容（生成描述时使用） |
| `titleLengthLimit` | integer | 否 | 标题长度限制 |
| `languageName` | string | 是 | 目标语言名称（使用接口 get_language_name_code_map 获取的code） |
| `keywordsList` | array&lt;string> | 否 | 关键词列表 |
| `negativeWordsList` | array&lt;string> | 否 | 排除词列表 |
| `categoryName` | string | 否 | 类目名称 |
| `site` | string | 否 | 站点 |
| `cid` | string | 否 | 类目ID |
| `imageInfoList` | array&lt;object> | 否 | 图片信息列表 |
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
| `data.titleResult.contents` | array&lt;string> | 否 | 标题内容列表 |
| `data.notesResult` | object | 否 | 描述生成结果 |
| `data.notesResult.result` | string | 否 | 结果状态：success/fail |
| `data.notesResult.contents` | array&lt;string> | 否 | 描述内容列表 |
