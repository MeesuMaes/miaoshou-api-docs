# 与 SHEIN 的关系及商品发布链路

## 1. 本文档中没有 SHEIN 采集箱

- 192 个接口中**没有 SHEIN 采集箱/SHEIN 发布接口**。商品模块覆盖的平台为：TikTok、TEMU 全托、TEMU 半托、OZON、Shopee、Mercadolibre（美客多）。
- 「获取店铺数据列表」的 `platform` 枚举也只有：tiktok / tiktokGlobal / pddkj / pddkjChoice / shopee / shopeeGlobal / mercadolibre / ozon，**无 shein**。
- 「认领到平台采集箱」的 `platform` 取值：tiktok / pddkj / pddkjChoice / shopee / ozon / mercadolibre，**无 shein**。
- 全部原文中 “shein” 仅出现在包裹模块「获取当前包裹有效的线上物流列表」的 `preRequestId`（预下单请求id）字段说明：“shein 专属”。即包裹物流侧对 SHEIN 订单有字段支持，但商品发布侧无。
- 因此若要用妙手发布 SHEIN 商品，需向妙手确认是否有未公开/未在本分享中的 SHEIN 采集箱接口；按本文档无法实现。

## 2. 商品模块各子模块接口数

| 子模块 | 接口数 | 其中写操作 |
|---|---|---|
| 店铺 | 1 | 0 |
| 公共采集箱 | 7 | 5 |
| TK采集箱 | 20 | 5 |
| TEMU全托采集箱 | 24 | 6 |
| TEMU半托采集箱 | 27 | 6 |
| OZON采集箱 | 10 | 3 |
| Shopee采集箱 | 14 | 5 |
| 在线产品管理 | 8 | 4 |
| Mercadolibre采集箱 | 16 | 4 |
| AI公共服务 | 10 | 0 |
| 图片空间 | 1 | 1 |

## 3. 通用商品发布链路（按接口推断，各平台路径同构）

```
采集 → 公共采集箱 → 认领到平台采集箱 → (认领预发布店铺) → 编辑(店铺/站点模式详情) → 发布产品 → 发布记录列表
```

| 步骤 | 接口（示例） | 路径 |
|---|---|---|
| 1 采集 | 公共采集箱 · 通过货源链接采集货源 | `/open/v1/product/common_collect_box/common_collect_box/fetch_item` |
| 1' 手工建品 | 公共采集箱 · 创建公共采集箱产品 | `/open/v1/product/common_collect_box/common_collect_box/add_common_collect_box_detail` |
| 2 查看公共采集箱 | 公共采集箱 · 获取公共采集箱列表 | `/open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_list` |
| 3 认领到平台采集箱 | 公共采集箱 · 认领到平台采集箱 | `/open/v1/product/common_collect_box/common_collect_box/claimed` |
| 4 认领到预发布店铺(TK/TEMU) | TK采集箱>采集箱 · 认领预发布店铺 | `/open/v1/product/collect_box/tiktok/collect_box/claim_to_shop` |
| 4' 平台采集箱直接建品 | TEMU全托采集箱>采集箱 · 创建采集箱商品 | `/open/v1/product/collect_box/pddkj/collect_box/create_collect_box_item` |
| 5 准备类目/属性 | TK采集箱>采集箱 · 获取类目属性信息 | `/open/v1/product/collect_box/tiktok/collect_box/get_category_metadata` |
| 6 编辑店铺模式 | TK采集箱>采集箱 · 保存采集箱店铺模式详情 | `/open/v1/product/collect_box/tiktok/collect_box/save_shop_collect_item_info` |
| 6' 编辑站点模式 | TK采集箱>采集箱 · 保存采集箱站点模式详情 | `/open/v1/product/collect_box/tiktok/collect_box/save_site_collect_item_info` |
| 7 发布 | TK采集箱>产品发布 · 发布产品 | `/open/v1/product/collect_box/tiktok/collect_box/save_move_collect_task` |
| 8 查结果 | TK采集箱>产品发布 · 发布记录列表 | `/open/v1/product/collect_box/tiktok/move_collect/search_move_collect_list` |

路径规律：`/open/v1/product/collect_box/{平台}/collect_box/...`（采集箱）与 `/open/v1/product/collect_box/{平台}/move_collect/save_move_collect_task`（发布）、`.../move_collect/search_move_collect_list`（发布记录）；平台代号 tiktok / pddkj / pddkj_choice / ozon / shopee / mercadolibre。

TK「发布产品」请求体：`shopIds`（店铺ID数组，≤200）+ `detailIds`（采集箱详情ID数组，≤200），响应仅 result/code（异步任务，结果需查发布记录列表）。

辅助：AI 公共服务（白底图、消除、水印、图片翻译、AI 生成标题/描述、润色规格）、图片空间（URL 上传）、TK 定价模板。
