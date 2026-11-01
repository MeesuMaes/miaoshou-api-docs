# 获取类目列表


- 层级：开放平台 > 商品 > TK采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/tiktok/collect_box/get_category_tree_by_site`
- 类型：读
- 原文：[446814588e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814588e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

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
