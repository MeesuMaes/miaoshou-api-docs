# 获取商品分组列表


- 层级：开放平台 > 仓储 > 商品 > 商品分组
- 方法+路径：`POST /open/v1/ewm/goods/goods_group/fetch/get_goods_group_list`
- 类型：读
- 原文：[479599769e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599769e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsGroupTree` | array&lt;object> | 否 |  |
| `data.goodsGroupTree[].goodsGroupId` | string | 否 | 分组ID |
| `data.goodsGroupTree[].parentGoodsGroupId` | string | 否 | 父分组ID |
| `data.goodsGroupTree[].groupName` | string | 否 | 分组名称 |
| `data.goodsGroupTree[].level` | string | 否 | 级别 |
| `data.goodsGroupTree[].sort` | string | 否 | 排序 |
| `data.goodsGroupTree[].subGroups` | array&lt;object> | 否 | 子分组 |
