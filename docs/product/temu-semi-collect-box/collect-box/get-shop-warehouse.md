# 获取店铺发货仓库（支持同步）


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 采集箱
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/collect_box/get_shop_warehouse`
- 类型：读
- 原文：[477347611e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/477347611e0.md).md）

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
| `data.shopIdAndWarehouseListMap` | object | 否 | 店铺仓库映射，key 为 shopId，value 为该店铺下所有站点的仓库列表。 使用方式： 1. 取 shopIdAndWarehouseListMap[shopId] 获取当前店铺的仓库列表； 2. warehouseDisable 该字段暂时不用 不需要判断； 3. 列表已按站点分组，同一站点下可选一个或多个仓库； 4. 为每个发布站点选定仓库后，将 warehouseId 填入 siteWarehouseList[].warehouseId、 site 填入 siteWarehouseList[].site，组成 siteWarehouseList 的每一项； Map value 为仓库列表，每一项结构如下： - warehouseId    string  仓库ID，填入 siteWarehouseList[].warehouseId - warehouseName  string  仓库名称，用于展示 - site           string  站点编码（如 US、DE），填入 siteWarehouseList[].site - shopId         string  所属店铺ID - siteName       string  站点中文名，用于展示 - warehouseDisable string 该字段暂时不用 不需要判断 - managementType string  仓库管理类型。null 或 "0" 为普通仓；"3" 为其他类型仓库 |
