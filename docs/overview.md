# 妙手开放平台 API 文档（整理版）

> 来源：妙手开放平台 apifox 分享文档（1 篇快速接入 + 192 篇接口，2026-11-01 下载）。原始 Markdown 在 `../raw/`；本文档字段说明均摘自原文 OpenAPI 定义。

## 文件

| 文件 | 内容 | 接口数 | 写操作 |
|---|---|---|---|
| [01-product.md](/product/) | 商品 | 138 | 39 |
| [02-package.md](/package) | 包裹 | 17 | 6 |
| [03-purchase.md](/purchase) | 采购 | 17 | 11 |
| [04-warehouse.md](/warehouse) | 仓储 | 18 | 3 |
| [05-source-account.md](/source-account) | 货源账号 | 2 | 0 |
| [shein-notes.md](/shein) | 与 SHEIN 的关系、各平台采集箱统计、商品发布链路 | - | - |

合计 192 个接口。类型：读 / 写 / 处理(生成内容，AI/翻译/水印类)——按标题判定，仅供参考。

## 一、接入概要（摘自「快速接入」）

### 二、接口域名说明

#### 2.1 正式环境域名
- **接口基础域名**：`https://openapi-erp.91miaoshou.com`
- **接口完整地址格式**：`正式域名 + 接口路径`
- **示例**：  
  接口路径 `/open/v1/order/create`  
  完整请求地址：`https://openapi-erp.91miaoshou.com/open/v1/order/create`

> 注意：签名拼接时 **只传接口路径** `/open/v1/order/create`，**不要带域名、不要带 query 参数**。

---

### 三、接入流程

```
注册应用 → 获取密钥 → 生成签名 → 调用 API
```

#### 3.1 注册应用

1. 登录妙手
2. 进入「开放平台」→「创建应用」
3. 填写应用名称、描述等信息
4. 提交审核（审核通过后即可使用）

#### 3.2 获取密钥

应用创建成功后，系统会分配：

| 字段 | 说明 | 示例 |
|------|------|------|
| AppKey | 应用标识（公开） | `ak_1234567890abcdef` |
| AppSecret | 应用密钥（保密） | `as_xxxxxxxxxxxxxxxx` |

**⚠️ 安全提示**：AppSecret请妥善保存，不要泄露给他人。

#### 3.3 IP 白名单配置（可选）

用户可在后台配置 IP 白名单：

| 配置情况 | 效果 |
|----------|------|
| 不配置 | 该用户下的所有应用允许任意 IP 访问 |
| 配置白名单 | 仅允许白名单内的 IP 访问该用户下的所有应用 |

**说明**：
- 白名单是**账户级别**的配置，一个用户只有一份白名单
- 该用户下的**所有应用共享同一份白名单**
- 配置白名单后，该用户的所有应用都只能从指定 IP 调用
- 不同用户的白名单相互独立

---

### 四、签名机制

#### 4.1 签名算法

- **算法**：HmacSHA256
- **输出**：hex 字符串（小写）
- **签名有效期**：5分钟（timestamp 与服务器时间偏差超过 300 秒则拒绝）

#### 4.2 签名公式

```
sign = HmacSHA256(appSecret, appSecret + path + timestamp + appKey + bodyJson + appSecret)
```

**拼接规则**：
1. 以 AppSecret 开头
2. 拼接请求路径（不含域名、不含Query参数）
3. 拼接时间戳（秒级 Unix 时间戳）
4. 拼接 AppKey
5. 拼接请求 Body（JSON 字符串，无 body 则拼空字符串）
6. 以 AppSecret 结尾

#### 4.3 请求头参数

每次请求需在 HTTP Header 中携带以下参数：

| 参数名 | 必填 | 说明 |
|--------|------|------|
| x-app-key | 是 | 应用 Key |
| x-timestamp | 是 | 秒级 Unix 时间戳 |
| x-sign | 是 | 签名值 |

---

#### 5.2 Python 示例

```python
import hmac
import hashlib
import time

def generate_sign(app_secret, path, timestamp, app_key, body_json=None):
    """生成签名
    :param app_secret: 应用密钥
    :param path: 请求路径（不含 Query String、不含域名）
    :param timestamp: 秒级 Unix 时间戳
    :param app_key: 应用 Key
    :param body_json: 请求 Body JSON 字符串
    """
    content = app_secret + path + str(timestamp) + app_key

    if body_json:
        content += body_json
    content += app_secret

    sign = hmac.new(
        app_secret.encode('utf-8'),
        content.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    return sign

## 使用示例
app_secret = "as_xxxxxxxxxxxxxxxx"
app_key = "ak_1234567890abcdef"
path = "/open/v1/order/create"
timestamp = int(time.time())

## POST 请求示例
body_json = '{"orderNo":"ORD2024001","amount":100.00}'
sign = generate_sign(app_secret, path, timestamp, app_key, body_json)
print(f"POST sign: {sign}")
```

### 六、响应格式

#### 6.1 成功响应

```json
{
    "result": "success",
    "code": "success",
    "message": "success",
    "data": {
        "orderId": "12345",
        "orderNo": "ORD2024001",
        "status": "pending"
    }
}
```

#### 6.2 失败响应

```json
{
    "result": "fail",
    "code": "signInvalid",
    "message": "签名验证不通过",
    "data": null
}
```

#### 6.3 常见错误码

| 错误码 | 说明 | 处理建议 |
|--------|------|---------|
| success | 成功 | - |
| appNotFound | 应用不存在或已禁用 | 检查 x-app-key 是否正确，应用是否已审核通过 |
| signMissing | 缺少签名参数 | 检查请求头是否包含 x-app-key、x-timestamp、x-sign |
| signExpired | 请求已过期 | 检查本机时间是否准确，timestamp 是否为秒级 Unix 时间戳 |
| signInvalid | 签名验证不通过 | 检查签名算法是否正确，AppSecret 是否正确 |
| appNoPermission | 应用无权限访问该接口 | 检查应用是否有该接口的调用权限 |
| ipNotInWhitelist | IP 不在白名单中 | 检查请求 IP 是否在账户白名单配置中 |
| accountQpsRateLimit | 账户每秒请求频率超限 | 降低请求频率，或联系平台提升限额 |
| accountQpmRateLimit | 账户每分钟请求频率超限 | 降低请求频率，或联系平台提升限额 |
| accountQpdRateLimit | 账户每天请求频率超限 | 降低请求频率，或联系平台提升限额 |
| appQpsRateLimit | 应用每秒请求频率超限 | 降低请求频率，或联系平台提升限额 |
| appQpmRateLimit | 应用每分钟请求频率超限 | 降低请求频率，或联系平台提升限额 |
| appQpdRateLimit | 应用每天请求频率超限 | 降低请求频率，或联系平台提升限额 |
| apiQpsRateLimit | 应用接口每秒请求频率超限 | 降低请求频率，或联系平台提升限额 |
| apiQpmRateLimit | 应用接口每分钟请求频率超限 | 降低请求频率，或联系平台提升限额 |
| apiQpdRateLimit | 应用接口每天请求频率超限 | 降低请求频率，或联系平台提升限额 |
| platformQpsRateLimit | 平台接口每秒请求频率超限 | 降低请求频率，或联系平台提升限额 |
| platformQpmRateLimit | 平台接口每分钟请求频率超限 | 降低请求频率，或联系平台提升限额 |
| platformQpdRateLimit | 平台接口每天请求频率超限 | 降低请求频率，或联系平台提升限额 |
| accountApiQpsRateLimit | 账户接口每秒请求频率超限 | 降低请求频率，或联系平台提升限额 |
| accountApiQpmRateLimit | 账户接口每分钟请求频率超限 | 降低请求频率，或联系平台提升限额 |
| accountApiQpdRateLimit | 账户接口每天请求频率超限 | 降低请求频率，或联系平台提升限额 |
| routeNotFound | 路由不存在 | 检查请求路径是否正确、域名路径是否拼接错误 |
| upstreamError | 下游服务连接失败 | 下游服务异常，稍后重试 |
| upstreamConnectTimeout | 下游服务连接超时 | 下游服务异常，稍后重试 |
| upstreamReadTimeout | 下游服务响应超时 | 下游服务异常，稍后重试 |
| upstreamDnsError | 下游服务域名解析失败 | 检查接口域名是否正确、本地DNS是否可正常解析 |
| upstreamReset | 下游服务连接被重置 | 下游服务异常，稍后重试 |
| systemError | 系统内部错误 | 稍后重试，或联系平台技术支持 |
| redisConnectionError | 缓存服务连接失败 | 稍后重试，或联系平台技术支持 |
| redisTimeout | 缓存服务响应超时 | 稍后重试，或联系平台技术支持 |

---

### 七、常见问题

#### Q1: 签名总是验证失败？

检查以下几点：
1. AppSecret 是否正确（注意区分大小写）
2. 时间戳是否为**秒级** Unix 时间戳（不是毫秒）
3. 签名路径是否带了域名、多余参数（只能传纯接口路径）
4. POST 请求是否正确拼接了 Body，无 body 需拼空串
5. 签名输出是否为**小写 hex**

#### Q2: 返回 "请求已过期"？

检查服务器时间是否与标准时间同步，timestamp 偏差不能超过 300 秒；必须使用**秒级**时间戳。

#### Q3: 域名解析失败、ping 找不到主机？
1. 确认域名拼写：`openapi-erp.91miaoshou.com`
2. 切换本地公共 DNS：阿里 223.5.5.5 或 114.114.114.114
3. 检查本地网络防火墙、代理是否拦截域名解析

#### Q4: 支持哪些 HTTP 方法？

目前仅支持 **POST** 方法，Content-Type 固定为 `application/json`。

## 二、全部接口索引


### 商品（138，详见 [01-product.md](/product/)）

| 子模块 | 接口 | 方法 | 路径 | 类型 | 原文 |
|---|---|---|---|---|---|
| 店铺 | 获取店铺数据列表 | POST | `/open/v1/product/shop/shop/get_shop_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814596e0.md) |
| 公共采集箱 | 通过货源链接采集货源 | POST | `/open/v1/product/common_collect_box/common_collect_box/fetch_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814581e0.md) |
| 公共采集箱 | 创建公共采集箱产品 | POST | `/open/v1/product/common_collect_box/common_collect_box/add_common_collect_box_detail` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814585e0.md) |
| 公共采集箱 | 获取公共采集箱列表 | POST | `/open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814582e0.md) |
| 公共采集箱 | 编辑公共采集箱产品 | POST | `/open/v1/product/common_collect_box/common_collect_box/edit_common_collect_box_detail` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814586e0.md) |
| 公共采集箱 | 获取公共采集箱详情 | POST | `/open/v1/product/common_collect_box/common_collect_box/get_common_collect_box_detail` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814583e0.md) |
| 公共采集箱 | 批量删除公共采集箱产品 | POST | `/open/v1/product/common_collect_box/common_collect_box/batch_delete_common_collect_box_detail` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814584e0.md) |
| 公共采集箱 | 认领到平台采集箱 | POST | `/open/v1/product/common_collect_box/common_collect_box/claimed` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814587e0.md) |
| TK采集箱>采集箱 | 获取类目列表 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_category_tree_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814588e0.md) |
| TK采集箱>采集箱 | 获取类目属性信息 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_category_metadata` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814589e0.md) |
| TK采集箱>采集箱 | 获取店铺仓库列表 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_shop_warehouse_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814590e0.md) |
| TK采集箱>采集箱 | 获取制造商列表 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_manufacturer_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449869292e0.md) |
| TK采集箱>采集箱 | 获取欧盟责任人列表 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_responsible_person_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449869293e0.md) |
| TK采集箱>采集箱 | 认领预发布店铺 | POST | `/open/v1/product/collect_box/tiktok/collect_box/claim_to_shop` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814594e0.md) |
| TK采集箱>采集箱 | 获取采集箱列表 | POST | `/open/v1/product/collect_box/tiktok/collect_box/search_collect_box_detail_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814591e0.md) |
| TK采集箱>采集箱 | 获取采集箱店铺模式详情 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_shop_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814592e0.md) |
| TK采集箱>采集箱 | 保存采集箱店铺模式详情 | POST | `/open/v1/product/collect_box/tiktok/collect_box/save_shop_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814593e0.md) |
| TK采集箱>采集箱 | 获取采集箱站点模式详情 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_site_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449650816e0.md) |
| TK采集箱>采集箱 | 保存采集箱站点模式详情 | POST | `/open/v1/product/collect_box/tiktok/collect_box/save_site_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/449650817e0.md) |
| TK采集箱>采集箱 | 产品翻译 | POST | `/open/v1/product/collect_box/tiktok/collect_box/translate_collect_item_info` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189160e0.md) |
| TK采集箱>采集箱 | AI匹配类目 | POST | `/open/v1/product/collect_box/tiktok/collect_box/ai_match_cid_by_shop_ids` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189162e0.md) |
| TK采集箱>采集箱 | 批量删除采集箱产品接口 | POST | `/open/v1/product/collect_box/tiktok/collect_box/delete_collect_box_detail` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/496804330e0.md) |
| TK采集箱>采集箱 | AI属性匹配 | POST | `/open/v1/product/collect_box/tiktok/collect_box/ai_match_product_attribute` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189161e0.md) |
| TK采集箱>采集箱 | 获取品牌列表 | POST | `/open/v1/product/collect_box/tiktok/collect_box/get_brand_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/497001483e0.md) |
| TK采集箱>产品发布 | 发布产品 | POST | `/open/v1/product/collect_box/tiktok/collect_box/save_move_collect_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/446814595e0.md) |
| TK采集箱>产品发布 | 发布记录列表 | POST | `/open/v1/product/collect_box/tiktok/move_collect/search_move_collect_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189163e0.md) |
| TK采集箱>定价模板 | 获取定价模板列表 | POST | `/open/v1/product/collect_box/tiktok/price_template/get_price_template_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189164e0.md) |
| TK采集箱>定价模板 | 获取各个站点的默认配置 | POST | `/open/v1/product/collect_box/tiktok/price_template/get_site_default_setting` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482189165e0.md) |
| TEMU全托采集箱>产品发布 | 发布产品 | POST | `/open/v1/product/collect_box/pddkj/move_collect/save_move_collect_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724006e0.md) |
| TEMU全托采集箱>产品发布 | 发布记录列表 | POST | `/open/v1/product/collect_box/pddkj/move_collect/search_move_collect_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511668107e0.md) |
| TEMU全托采集箱>车型库 | 获取车型库站点列表 | POST | `/open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724008e0.md) |
| TEMU全托采集箱>车型库 | 获取车型库站点属性结构映射 | POST | `/open/v1/product/collect_box/pddkj/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724009e0.md) |
| TEMU全托采集箱>车型库 | 获取站点顶级车型节点列表 | POST | `/open/v1/product/collect_box/pddkj/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724010e0.md) |
| TEMU全托采集箱>车型库 | 获取车型属性依赖树 | POST | `/open/v1/product/collect_box/pddkj/vehicle_library/get_vehicle_library_prop_dependency_tree` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724011e0.md) |
| TEMU全托采集箱>车型库 | 根据类目ID查询有车型库数据的类目列表 | POST | `/open/v1/product/collect_box/pddkj/vehicle_library/get_has_vehicle_library_cids_by_search_cids` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724007e0.md) |
| TEMU全托采集箱>采集箱 | 获取类目属性规则 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_category_attribute_rules` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545320e0.md) |
| TEMU全托采集箱>采集箱 | 获取商品基本选项 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_item_options` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545321e0.md) |
| TEMU全托采集箱>采集箱 | 创建采集箱商品 | POST | `/open/v1/product/collect_box/pddkj/collect_box/create_collect_box_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545322e0.md) |
| TEMU全托采集箱>采集箱 | 认领预发布店铺 | POST | `/open/v1/product/collect_box/pddkj/collect_box/claim_to_shop` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545323e0.md) |
| TEMU全托采集箱>采集箱 | 获取采集箱店铺模式详情 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_shop_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545324e0.md) |
| TEMU全托采集箱>采集箱 | 保存采集箱店铺模式详情 | POST | `/open/v1/product/collect_box/pddkj/collect_box/save_shop_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545325e0.md) |
| TEMU全托采集箱>采集箱 | 获取采集箱站点模式详情 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_site_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545326e0.md) |
| TEMU全托采集箱>采集箱 | 保存采集箱站点模式详情 | POST | `/open/v1/product/collect_box/pddkj/collect_box/save_site_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545327e0.md) |
| TEMU全托采集箱>采集箱 | 获取原产地国家列表 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_country_short_name_and_name_map` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545328e0.md) |
| TEMU全托采集箱>采集箱 | 店铺模特列表 | POST | `/open/v1/product/collect_box/pddkj/collect_box/search_model_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545329e0.md) |
| TEMU全托采集箱>采集箱 | 获取类目列表 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_category_tree_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545330e0.md) |
| TEMU全托采集箱>采集箱 | 获取尺码模板列表 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_size_template_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545331e0.md) |
| TEMU全托采集箱>采集箱 | 获取尺码表详情 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_size_charts_by_size_template_id` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545332e0.md) |
| TEMU全托采集箱>采集箱 | 获取模特分类配置 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_model_cat_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545333e0.md) |
| TEMU全托采集箱>采集箱 | 获取采集箱列表 | POST | `/open/v1/product/collect_box/pddkj/collect_box/search_collect_box_detail_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545334e0.md) |
| TEMU全托采集箱>采集箱 | 批量删除采集箱产品接口 | POST | `/open/v1/product/collect_box/pddkj/collect_box/delete_collect_box_detail` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/471545335e0.md) |
| TEMU全托采集箱>采集箱 | 获取需要设置净重的类目列表 | POST | `/open/v1/product/collect_box/pddkj/collect_box/get_need_set_net_weight_cid_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/490449047e0.md) |
| TEMU半托采集箱>商品发布 | 发布产品 | POST | `/open/v1/product/collect_box/pddkj_choice/move_collect/save_move_collect_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726294e0.md) |
| TEMU半托采集箱>商品发布 | 发布记录列表 | POST | `/open/v1/product/collect_box/pddkj_choice/move_collect/search_move_collect_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511667358e0.md) |
| TEMU半托采集箱>车型库 | 获取车型库站点列表 | POST | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726296e0.md) |
| TEMU半托采集箱>车型库 | 获取车型库站点属性结构映射 | POST | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726297e0.md) |
| TEMU半托采集箱>车型库 | 获取站点顶级车型节点列表 | POST | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726298e0.md) |
| TEMU半托采集箱>车型库 | 获取车型属性依赖树 | POST | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_vehicle_library_prop_dependency_tree` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726299e0.md) |
| TEMU半托采集箱>车型库 | 根据类目ID查询有车型库数据的类目列表 | POST | `/open/v1/product/collect_box/pddkj_choice/vehicle_library/get_has_vehicle_library_cids_by_search_cids` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726295e0.md) |
| TEMU半托采集箱>采集箱 | 获取类目属性规则 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_category_attribute_rules` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347599e0.md) |
| TEMU半托采集箱>采集箱 | 店铺模特列表 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/search_model_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347600e0.md) |
| TEMU半托采集箱>采集箱 | 获取商品基本选项 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_item_options` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347601e0.md) |
| TEMU半托采集箱>采集箱 | 创建采集箱商品 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/create_collect_box_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347602e0.md) |
| TEMU半托采集箱>采集箱 | 认领预发布店铺 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/claim_to_shop` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347603e0.md) |
| TEMU半托采集箱>采集箱 | 获取采集箱站点模式详情 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_site_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347606e0.md) |
| TEMU半托采集箱>采集箱 | 保存采集箱店铺模式详情 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/save_shop_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347605e0.md) |
| TEMU半托采集箱>采集箱 | 获取采集箱店铺模式详情 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347604e0.md) |
| TEMU半托采集箱>采集箱 | 保存采集箱站点模式详情 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/save_site_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347607e0.md) |
| TEMU半托采集箱>采集箱 | 获取原产地国家列表 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_country_short_name_and_name_map` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347608e0.md) |
| TEMU半托采集箱>采集箱 | 获取发布站点选项 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_publish_site_options` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347609e0.md) |
| TEMU半托采集箱>采集箱 | 获取店铺运费模板 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_freight_template` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347610e0.md) |
| TEMU半托采集箱>采集箱 | 获取店铺发货仓库（支持同步） | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_warehouse` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347611e0.md) |
| TEMU半托采集箱>采集箱 | 获取类目列表 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_category_tree_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347612e0.md) |
| TEMU半托采集箱>采集箱 | 获取尺码模板列表 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_size_template_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347613e0.md) |
| TEMU半托采集箱>采集箱 | 获取尺码表详情 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_size_charts_by_size_template_id` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347614e0.md) |
| TEMU半托采集箱>采集箱 | 获取模特分类配置 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_model_cat_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347615e0.md) |
| TEMU半托采集箱>采集箱 | 获取采集箱列表 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/search_collect_box_detail_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347616e0.md) |
| TEMU半托采集箱>采集箱 | 批量删除采集箱产品接口 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/delete_collect_box_detail` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347617e0.md) |
| TEMU半托采集箱>采集箱 | 获取包装清单属性值列表 | POST | `/open/v1/product/collect_box/pddkj_choice/collect_box/get_goods_accessories_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/501791146e0.md) |
| OZON采集箱>采集箱 | 获取采集箱编辑币种 | POST | `/open/v1/product/collect_box/ozon/collect_box/get_account_setting_edit_currency` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774623e0.md) |
| OZON采集箱>采集箱 | 获取类目列表 | POST | `/open/v1/product/collect_box/ozon/collect_box/get_category_tree_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774625e0.md) |
| OZON采集箱>采集箱 | 获取类目属性信息 | POST | `/open/v1/product/collect_box/ozon/collect_box/get_category_attributes` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774626e0.md) |
| OZON采集箱>采集箱 | 获取采集箱列表 | POST | `/open/v1/product/collect_box/ozon/collect_box/search_collect_box_detail_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774624e0.md) |
| OZON采集箱>采集箱 | 获取店铺仓库列表 | POST | `/open/v1/product/collect_box/ozon/collect_box/get_shop_warehouse_info_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774627e0.md) |
| OZON采集箱>采集箱 | 获取采集箱站点模式详情 | POST | `/open/v1/product/collect_box/ozon/collect_box/get_site_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774628e0.md) |
| OZON采集箱>采集箱 | 创建采集箱站点模式数据 | POST | `/open/v1/product/collect_box/ozon/collect_box/create_collect_box_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774629e0.md) |
| OZON采集箱>采集箱 | 编辑采集箱站点模式数据 | POST | `/open/v1/product/collect_box/ozon/collect_box/save_site_detail_data` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774630e0.md) |
| OZON采集箱>产品发布 | 发布记录列表 | POST | `/open/v1/product/collect_box/ozon/move_collect/search_move_collect_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511671956e0.md) |
| OZON采集箱>产品发布 | 发布产品 | POST | `/open/v1/product/collect_box/ozon/move_collect/save_move_collect_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/474774631e0.md) |
| Shopee采集箱>采集箱 | 获取站点编辑信息 | POST | `/open/v1/product/collect_box/shopee/collect_box/get_site_detail_simple_data` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434496e0.md) |
| Shopee采集箱>采集箱 | 保存站点编辑数据 | POST | `/open/v1/product/collect_box/shopee/collect_box/save_site_detail_data` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157439e0.md) |
| Shopee采集箱>采集箱 | 创建采集箱SPU（手动添加商品） | POST | `/open/v1/product/collect_box/shopee/collect_box/create_collect_box_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157440e0.md) |
| Shopee采集箱>采集箱 | 获取采集箱产品的源数据 | POST | `/open/v1/product/collect_box/shopee/collect_box/get_collect_box_item_detail` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157441e0.md) |
| Shopee采集箱>采集箱 | 保存采集箱产品源数据信息 | POST | `/open/v1/product/collect_box/shopee/collect_box/save_edit_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157442e0.md) |
| Shopee采集箱>采集箱 | 获取采集箱列表 | POST | `/open/v1/product/collect_box/shopee/collect_box/search_collect_box_detail_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157443e0.md) |
| Shopee采集箱>采集箱 | 获取品牌列表 | POST | `/open/v1/product/collect_box/shopee/collect_box/get_brand_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157444e0.md) |
| Shopee采集箱>采集箱 | 根据站点获取运费模板(物流方式) | POST | `/open/v1/product/collect_box/shopee/collect_box/get_logistic_options_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157445e0.md) |
| Shopee采集箱>采集箱 | 获取类目树 | POST | `/open/v1/product/collect_box/shopee/collect_box/get_category_tree_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516157446e0.md) |
| Shopee采集箱>采集箱 | 获取类目属性信息 | POST | `/open/v1/product/collect_box/shopee/collect_box/get_category_attributes` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516158667e0.md) |
| Shopee采集箱>采集箱 | 获取仓库信息列表 | POST | `/open/v1/product/collect_box/shopee/collect_box/get_global_shop_warehouse` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/516158668e0.md) |
| Shopee采集箱>商品发布 | 发布记录列表 | POST | `/open/v1/product/collect_box/shopee/move_collect/search_move_collect_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511672303e0.md) |
| Shopee采集箱>商品发布 | 提交全球商品发布到店铺任务 | POST | `/open/v1/product/collect_box/shopee/move_collect/save_move_collect_global_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434554e0.md) |
| Shopee采集箱>商品发布 | 采集箱产品发布任务 | POST | `/open/v1/product/collect_box/shopee/move_collect/save_move_collect_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434555e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 全球产品搜索 | POST | `/open/v1/product/item/shopee_global/item/search_item_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434401e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 全球产品详情（返回官方 | POST | `/open/v1/product/item/shopee_global/item/get_item_detail` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434402e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 保存产品编辑 | POST | `/open/v1/product/item/shopee_global/item/save_edit_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434403e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 获取属性列表 | POST | `/open/v1/product/item/shopee_global/item/get_attribute_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434404e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 获取全球店铺类目尺寸模板列表 | POST | `/open/v1/product/item/shopee_global/item/get_shop_id_and_size_chart_list_map` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434405e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 上传商品视频 | POST | `/open/v1/product/item/shopee_global/item/upload_item_video` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434406e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 同步产品 | POST | `/open/v1/product/item/shopee_global/item/rsync_item_single` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434407e0.md) |
| 在线产品管理>Shopee全球在线产品管理 | 全球产品删除 | POST | `/open/v1/product/item/shopee_global/item/delete_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/480434408e0.md) |
| Mercadolibre采集箱>发布产品 | 发布产品 | POST | `/open/v1/product/collect_box/mercadolibre/move_collect/save_move_collect_task` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482757484e0.md) |
| Mercadolibre采集箱>发布产品 | 发布记录列表 | POST | `/open/v1/product/collect_box/mercadolibre/move_collect/search_move_collect_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/511672449e0.md) |
| Mercadolibre采集箱>采集箱 | 获取类目属性规则 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_category_attribute_rules` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753632e0.md) |
| Mercadolibre采集箱>采集箱 | 获取类目配置 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_category_setting` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753633e0.md) |
| Mercadolibre采集箱>采集箱 | 获取尺码表domain列表 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_domain_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753635e0.md) |
| Mercadolibre采集箱>采集箱 | 获取尺码表表头和主属性信息 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_attribute_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753636e0.md) |
| Mercadolibre采集箱>采集箱 | 获取尺码表所需填写属性信息 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_size_chart_need_attribute_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753637e0.md) |
| Mercadolibre采集箱>采集箱 | 获取授权站点和名称映射 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_auth_site_and_site_name_map` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753639e0.md) |
| Mercadolibre采集箱>采集箱 | 获取商品基本选项 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_item_options` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753640e0.md) |
| Mercadolibre采集箱>采集箱 | 查询尺码表模板列表 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/search_size_chart_template` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753641e0.md) |
| Mercadolibre采集箱>采集箱 | 获取采集箱详情 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_site_collect_item_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753644e0.md) |
| Mercadolibre采集箱>采集箱 | 创建采集箱商品 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/create_collect_box_item` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753646e0.md) |
| Mercadolibre采集箱>采集箱 | 保存采集箱站点详情 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/save_site_collect_item_info` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753647e0.md) |
| Mercadolibre采集箱>采集箱 | 同步店铺尺码表 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/rsync_size_chart_template` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753643e0.md) |
| Mercadolibre采集箱>采集箱 | 获取采集箱列表 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/search_collect_box_detailList` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482753630e0.md) |
| Mercadolibre采集箱>采集箱 | 获取类目列表 | POST | `/open/v1/product/collect_box/mercadolibre/collect_box/get_category_tree_by_site` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484103119e0.md) |
| AI公共服务>图片处理 | AI白底图 | POST | `/open/v1/product/picture/matting/auto_ai_matting_multi` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482201652e0.md) |
| AI公共服务>图片处理 | AI智能消除 | POST | `/open/v1/product/common/image_removal/remove_image` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190901e0.md) |
| AI公共服务>图片处理 | 搜索水印列表 | POST | `/open/v1/product/item/tiktok/watermark/search_watermark_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482200257e0.md) |
| AI公共服务>图片处理 | 图片打水印 | POST | `/open/v1/product/item/tiktok/watermark/watermark_images` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482200258e0.md) |
| AI公共服务>图片处理 | 获取支持的翻译语言配置 | POST | `/open/v1/product/common/translate/get_support_language_config` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286513e0.md) |
| AI公共服务>图片处理 | 图片翻译 | POST | `/open/v1/product/common/translate/translate_image` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286514e0.md) |
| AI公共服务>AI润色 | AI生成产品信息（标题/描述） | POST | `/open/v1/product/common/open_ai/generate_product_info` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190902e0.md) |
| AI公共服务>AI润色 | AI生成支持的语言map | POST | `/open/v1/product/common/open_ai/get_language_name_code_map` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190903e0.md) |
| AI公共服务>AI润色 | 获取支持的AI名称列表 | POST | `/open/v1/product/common/open_ai/get_generate_product_info_support_ai_name_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/482190904e0.md) |
| AI公共服务>AI润色 | AI润色销售规格 | POST | `/open/v1/product/common/open_ai/generate_sku_spec_name` | 处理(生成内容) | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286515e0.md) |
| 图片空间 | 通过图片URL上传图片到图片空间 | POST | `/open/v1/product/picture/picture_space/upload_picture_link` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/519663381e0.md) |

### 包裹（17，详见 [02-package.md](/package)）

| 子模块 | 接口 | 方法 | 路径 | 类型 | 原文 |
|---|---|---|---|---|---|
| 履约>基础管理 | 获取当前账号有效的线下物流列表 | POST | `/open/v1/order/logistics_agent/manage/get_enable_offline_product_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455528071e0.md) |
| 履约>基础管理 | 获取当前包裹有效的线上物流列表 | POST | `/open/v1/order/logistics_agent/manage/get_enable_online_product_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455611090e0.md) |
| 售后 | 获取退货退款列表 | POST | `/open/v1/order/after_sales/fetch/order_return_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477739260e0.md) |
| 售后 | 获取取消订单列表 | POST | `/open/v1/order/after_sales/fetch/order_cancel_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477739261e0.md) |
| 包裹>运单 | 申请运单号 | POST | `/open/v1/order/package/logistics/tracking_no/apply` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457255661e0.md) |
| 包裹>运单 | 批量申请运单号 | POST | `/open/v1/order/package/logistics/tracking_no/batch_apply` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523411121e0.md) |
| 包裹>运单 | 设置包裹物流 | POST | `/open/v1/order/package/logistics/tracking_no/save_logistics_agent_product` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457269520e0.md) |
| 包裹>运单 | 获取包裹物流轨迹 | POST | `/open/v1/order/package/logistics/tracking/get_tracking_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477263048e0.md) |
| 包裹>运单 | 获取运单面单 | POST | `/open/v1/order/package/logistics/waybill/get_waybill` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457264811e0.md) |
| 包裹>运单 | 批量获取面单 | POST | `/open/v1/order/package/logistics/waybill/batch_get_waybill` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523411122e0.md) |
| 包裹>基础信息修改 | 保存包裹本地备注 | POST | `/open/v1/order/package/base_info_modify/saveOrderPackageAppNote` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457235460e0.md) |
| 包裹>基础信息修改 | 保存包裹商家备注 | POST | `/open/v1/order/package/base_info_modify/saveSellerNote` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/457240926e0.md) |
| 包裹>获取包裹 | 获取订单包裹详情 | POST | `/open/v1/order/package/fetch/get_package_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/524317132e0.md) |
| 包裹>获取包裹 | 获取订单包裹列表 | POST | `/open/v1/order/package/fetch/search_package_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/524317133e0.md) |
| 包裹>发货 | 包裹发货 | POST | `/open/v1/order/package/ship_package/ship_packages` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/455694578e0.md) |
| 采购记录 | 采购记录列表 | POST | `/open/v1/order/purchase_order/purchase_record/search_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523326861e0.md) |
| 采购记录 | 采购记录详情 | POST | `/open/v1/order/purchase_order/purchase_record/get_detail` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/523329034e0.md) |

### 采购（17，详见 [03-purchase.md](/purchase)）

| 子模块 | 接口 | 方法 | 路径 | 类型 | 原文 |
|---|---|---|---|---|---|
| 采购单 | 添加采购单 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599772e0.md) |
| 采购单 | 创建1688采购单 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599773e0.md) |
| 采购单 | 编辑采购单 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599774e0.md) |
| 采购单 | 采购单动手填写运单号 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/add_goods_purchase_order_shipping` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599775e0.md) |
| 采购单 | 采购单修改运单信息 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_shipping` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599776e0.md) |
| 采购单 | 采购单更新平台运单信息 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/update_goods_purchase_order_outer_shipping` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599777e0.md) |
| 采购单 | 取消采购单 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/cancel_goods_purchase_order` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599778e0.md) |
| 采购单 | 标记采购单结束 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/finish_goods_purchase_order` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599779e0.md) |
| 采购单 | 通过采购单id批量添加1688商品采购单 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/operate/batch_add1688_goods_purchase_order_by_goods_purchase_order_ids` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599780e0.md) |
| 采购单 | 获取采购单列表 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order/fetch/search_goods_purchase_order_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599781e0.md) |
| 采购单 | 签收记录列表 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_order_receive/fetch/search_goods_purchase_order_receive_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599771e0.md) |
| 采购单 | 获取缺货、备货建议列表 | POST | `/open/v1/ewm/goods_purchase_order/goods_purchase_suggest/fetch/search_goods_purchase_suggest_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599782e0.md) |
| 供应商 | 获取供应商列表 | POST | `/open/v1/ewm/supplier/fetch/search_supplier_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599789e0.md) |
| 供应商 | 获取供应商信息 | POST | `/open/v1/ewm/supplier/fetch/get_supplier_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599790e0.md) |
| 供应商 | 获取供应商类型列表 | POST | `/open/v1/ewm/supplier/fetch/get_supplier_platform_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599791e0.md) |
| 供应商 | 修改供应商 | POST | `/open/v1/ewm/supplier/operate/edit_supplier` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479653199e0.md) |
| 供应商 | 创建供应商 | POST | `/open/v1/ewm/supplier/operate/add_supplier` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479653198e0.md) |

### 仓储（18，详见 [04-warehouse.md](/warehouse)）

| 子模块 | 接口 | 方法 | 路径 | 类型 | 原文 |
|---|---|---|---|---|---|
| 商品>商品 | 获取多规格商品列表 | POST | `/open/v1/ewm/goods/goods/fetch/search_goods_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599763e0.md) |
| 商品>商品 | 获取商品详情 | POST | `/open/v1/ewm/goods/goods/fetch/get_goods_info` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599764e0.md) |
| 商品>商品 | 添加商品 | POST | `/open/v1/ewm/goods/goods/operate/add_goods` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599765e0.md) |
| 商品>商品 | 安全库存批量设置 | POST | `/open/v1/ewm/goods/goods/operate/batch_save_goods_suggest_config` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599766e0.md) |
| 商品>商品 | 修改商品 | POST | `/open/v1/ewm/goods/goods/operate/edit_goods` | 写 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599767e0.md) |
| 商品>商品品牌 | 获取列表 | POST | `/open/v1/ewm/goods/goods_brand/fetch/search_goods_brand_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599768e0.md) |
| 商品>商品分组 | 获取商品分组列表 | POST | `/open/v1/ewm/goods/goods_group/fetch/get_goods_group_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599769e0.md) |
| 商品>商品sku | 获取商品SKU列表 | POST | `/open/v1/ewm/goods/goods_sku/fetch/search_goods_sku_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599770e0.md) |
| 商品包材 | 获取列表 | POST | `/open/v1/ewm/packaging/fetch/search_packaging_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592181e0.md) |
| 数据统计>销售数据 | 获取商品销售数据列表 | POST | `/open/v1/ewm/stat/goods_sale_data/fetch/search_goods_sale_data_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479602617e0.md) |
| 数据统计>商品周转分析 | 获取商品周转数据列表 | POST | `/open/v1/ewm/stat/goods_turnover_data/fetch/search_goods_turnover_data_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479602618e0.md) |
| 库存>三方仓sku库存 | 获取三方仓商品库存列表 | POST | `/open/v1/ewm/storage/third_warehouse/fetch/search_third_goods_sku_warehouse_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599784e0.md) |
| 库存>自营仓库存 | 获取自营仓商品库存列表 | POST | `/open/v1/ewm/storage/warehouse/fetch/search_goods_sku_warehouse_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599786e0.md) |
| 库存>自营仓库存 | 获取商品SKU安全库存列表 | POST | `/open/v1/ewm/storage/warehouse/fetch/get_goods_sku_safe_stock_num_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479599785e0.md) |
| 仓库>自营仓仓库 | 获取供应商仓库列表 | POST | `/open/v1/ewm/warehouse/fetch/supplier_warehouse_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/476990600e0.md) |
| 仓库>自营仓仓库 | 获取自营仓仓库列表 | POST | `/open/v1/ewm/warehouse/fetch/search_warehouse_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/476435300e0.md) |
| 仓库>三方仓仓库 | 获取三方仓授权列表 | POST | `/open/v1/ewm/third_warehouse/fetch/search_third_provider_auth_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592192e0.md) |
| 仓库>三方仓仓库 | 获取平台仓库列表 | POST | `/open/v1/ewm/third_warehouse/fetch/search_platform_warehouse_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479592193e0.md) |

### 货源账号（2，详见 [05-source-account.md](/source-account)）

| 子模块 | 接口 | 方法 | 路径 | 类型 | 原文 |
|---|---|---|---|---|---|
| - | 获取货源账号列表 | POST | `/open/v1/resell_account/fetch/search_reseller_account_page` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479848083e0.md) |
| - | 获取账号地址列表 | POST | `/open/v1/resell_account/fetch/get_reseller_account_address_list` | 读 | [链接](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/479848084e0.md) |
