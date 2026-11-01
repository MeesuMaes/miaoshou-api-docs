# 发布产品


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 商品发布
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/move_collect/save_move_collect_task`
- 类型：写
- 原文：[468726294e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726294e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `detailIds` | array&lt;integer> | 是 | 采集箱详情ID |
| `shopIdAndSitesMap` | object | 是 | 需要发布的店铺shopId和站点映射 key为shopId，value为该店铺下需要发布的站点列表 示例：\{"shopId值":["CA","EU"],"shopId值":["CA"]\} |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 是 | 返回结果 例:["success"] |
| `code` | string | 是 | 结果码/错误码 |


&lt;details>&lt;summary>请求示例&lt;/summary>

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
&lt;/details>
