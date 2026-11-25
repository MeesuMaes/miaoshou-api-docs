# SHEIN 全托 / 半托铺货链路

> 2026-11 新增。此前版本的本文档写着「没有 SHEIN 采集箱接口」，该结论已作废 —— 妙手在 2026-11 补齐了 SHEIN 全托（`shein`）与半托（`shein_choice`）两套采集箱，各 18 个接口，合计 36 个。

## 1. 两个平台路径完全对称

```
/open/v1/product/collect_box/shein/...          # SHEIN 全托
/open/v1/product/collect_box/shein_choice/...   # SHEIN 半托
```

除平台代号外，接口名、参数结构、层级完全一致。**先做全托，半托复制改路径即可。**

| 子模块 | 接口数 | 接口 |
|---|---|---|
| 采集箱 | 12 | 获取采集箱列表 / 获取采集箱店铺模式详情 / 创建采集箱产品 / 编辑保存采集箱店铺模式详情 / 批量删除采集箱产品接口 / 获取店铺和类目树映射 / 获取类目树 / 获取类目属性规则 / 获取联动属性规则 / 获取店铺商品发布字段规范 / 获取尺码表模板列表 / 获取品牌列表 |
| 产品模板 | 2 | 获取产品模板列表 / 获取产品模板详情 |
| 产品发布 | 2 | 发布产品 / 发布记录列表 |
| 定价模板 | 2 | 获取定价模板列表 / 获取定价模板详情 |

## 2. 与 TK / TEMU 的关键差异（决定代码怎么写）

| 维度 | TK / TEMU | SHEIN 全托/半托 |
|---|---|---|
| 从公共采集箱「认领」 | 有 `claim` / `claim_to_shop` | **没有认领环节** |
| 建品入口 | 站点模式 + 店铺模式 两层写入 | `create_collect_box_item`：顶层 `shopIds` + `itemDetail`（站点模式数据，内含 `shopCollectItemInfo` 店铺模式） |
| 编辑 | `save_site_collect_item_info` / `save_shop_collect_item_info` | 只有 `save_shop_collect_item_info`（编辑保存采集箱店铺模式详情） |
| 发布 | `save_move_collect_task`（shopIds + detailIds） | 同名同参数：`shopIds` + `detailIds`（各 ≤200） |
| 发布结果 | `search_move_collect_list` | 同名，返回含 SHEIN 专属字段（视频上传任务等） |

结论：**SHEIN 是「直接建品 → 直接发布」的单层结构**，不需要经过公共采集箱的认领动作。如果沿用 TK 的两层写法，会在第一步就卡住。

## 3. 推荐调用顺序

```
① 摸清店铺
   get_shop_id_and_category_tree_map      # 店铺 → 类目树映射，先看这家店能发哪些类目
   get_category_tree_by_site              # 类目树
② 摸清必填项（每家店不同，必须逐店拉）
   get_shop_goods_metadata_info           # 类目属性规则/必填项
   get_category_attribute_rules           # 类目属性规则
   get_associated_attribute_rules         # 联动属性（选了 A 才出现 B）
   get_size_chart_list / get_brand_list   # 尺码模板、品牌
③ 建品
   create_collect_box_item                # shopIds + itemDetail
④ 回查/修正
   search_collect_box_detail_list         # 采集箱列表
   get_shop_collect_item_info             # 详情
   save_shop_collect_item_info            # 改
⑤ 定价
   get_price_template_list / get_price_template
⑥ 发布
   save_move_collect_task                 # shopIds + detailIds
⑦ 查结果
   search_move_collect_list               # 状态：success / fail / processing / cancel
```

## 4. 三个必须提前知道的坑

1. **`get_shop_goods_metadata_info` 的必填项因店而异。** 33 家店不能共用一套模板，批量铺货前必须把每家店的返回拉一遍做 diff，否则会大面积发布失败。
2. **发布后改不了。** 在线产品管理只有 Shopee 全球店有接口，SHEIN 商品发布即黑盒 —— 改价、改库存只能回妙手后台。
3. **`platform` 枚举文档滞后。** 「获取店铺数据列表」的 `platform` 说明里目前仍只列 tiktok / tiktokGlobal / pddkj / pddkjChoice / shopee / shopeeGlobal / mercadolibre / ozon，**没有 shein**。取 SHEIN 店铺 shopId 时不能照文档枚举写死，需实测确认传参方式。

## 5. 商品模块各子模块接口数（233 版）

| 子模块 | 接口数 | 其中写操作 |
|---|---|---|
| 店铺 | 1 | 0 |
| 公共采集箱 | 7 | 5 |
| TK采集箱 | 21 | 6 |
| TEMU全托采集箱 | 24 | 6 |
| TEMU半托采集箱 | 27 | 6 |
| OZON采集箱 | 10 | 3 |
| Shopee采集箱 | 14 | 5 |
| 在线产品管理 | 8 | 4 |
| Mercadolibre采集箱 | 16 | 4 |
| **SHEIN全托采集箱** | **18** | **4** |
| **SHEIN半托采集箱** | **18** | **4** |
| AI公共服务 | 10 | 0 |
| 图片空间 | 1 | 1 |
| 合计 | 175 | 48 |

## 6. 通用发布链路（其它平台，供对照）

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

路径规律：`/open/v1/product/collect_box/{平台}/collect_box/...`（采集箱）与 `/open/v1/product/collect_box/{平台}/move_collect/save_move_collect_task`（发布）、`.../move_collect/search_move_collect_list`（发布记录）；平台代号 tiktok / pddkj / pddkj_choice / ozon / shopee / mercadolibre / **shein / shein_choice**。

TK「发布产品」请求体：`shopIds`（店铺ID数组，≤200）+ `detailIds`（采集箱详情ID数组，≤200），响应仅 result/code（异步任务，结果需查发布记录列表）。

辅助：AI 公共服务（白底图、消除、水印、图片翻译、AI 生成标题/描述、润色规格）、图片空间（URL 上传）、TK/SHEIN 定价模板。
