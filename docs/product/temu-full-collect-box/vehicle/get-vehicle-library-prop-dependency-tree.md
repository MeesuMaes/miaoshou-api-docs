# 获取车型属性依赖树


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/get_vehicle_library_prop_dependency_tree`
- 类型：读
- 原文：[468724011e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724011e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |
| `topPropertyValueDependencyId` | integer | 是 | 顶级节点ID，从 getGoodsVehicleLibrarySiteTopPropDependencyList 返回的列表中取 propertyValueDependencyId |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.vehicleLibraryPropDependencyTree` | object | 否 | 车型属性依赖树，key 为顶级节点的 propertyValueDependencyId，value 为节点数据（含 children 子节点）。 树形结构按品牌→车系→年份→车型→发动机类型逐级展开，isLeaf=1 的节点为叶子节点。 选中叶子节点后，将从根节点到该叶子节点的完整路径组装为一条车型路径， 每个路径节点取 propertyValueDependencyId、vidValue、level 填入 vehicleLibraryRelationList[].productPropValueDependencyList 中 |
