# 获取站点顶级车型节点列表


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_top_prop_dependency_list`
- 类型：读
- 原文：[468726298e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726298e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `vehicleLibraryId` | integer | 是 | 车型库站点ID，从 getGoodsVehicleLibrarySiteList 返回的站点列表中取 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.topGoodsVehicleLibraryPropDependencyList` | array&lt;object> | 否 | 顶级车型节点列表（通常为品牌层），每项含 propertyValueDependencyId、vidValue 等字段。 取每项的 propertyValueDependencyId 作为 topPropertyValueDependencyId， 传入 getVehicleLibraryPropDependencyTree 获取该品牌下完整的车型树 |
| `data.topGoodsVehicleLibraryPropDependencyList[].pddkjGoodsVehicleLibraryPropDependencyId` | integer | 否 | 平台车型库属性依赖ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vehicleLibraryId` | integer | 否 | 车型库ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].topPropertyValueDependencyId` | integer | 否 | 顶级节点propertyValueDependencyId |
| `data.topGoodsVehicleLibraryPropDependencyList[].parentPropertyValueDependencyId` | integer | 否 | 父节点propertyValueDependencyId，顶级节点为0 |
| `data.topGoodsVehicleLibraryPropDependencyList[].propertyValueDependencyId` | integer | 否 | 当前节点propertyValueDependencyId |
| `data.topGoodsVehicleLibraryPropDependencyList[].propertyDependencyId` | integer | 否 | 属性依赖ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vid` | integer | 否 | 属性值ID |
| `data.topGoodsVehicleLibraryPropDependencyList[].vidValue` | string | 否 | 属性值文本，如品牌名"Country Coach" |
| `data.topGoodsVehicleLibraryPropDependencyList[].level` | integer | 否 | 层级序号 |
| `data.topGoodsVehicleLibraryPropDependencyList[].isLeaf` | integer | 否 | 是否为叶子节点，0=否，1=是 |
| `data.topGoodsVehicleLibraryPropDependencyList[].md5BreadcrumbVidValue` | string | 否 | 面包屑属性值的MD5 |
| `data.topGoodsVehicleLibraryPropDependencyList[].breadcrumbVidValue` | string | 否 | 面包屑属性值文本 |
| `data.topGoodsVehicleLibraryPropDependencyList[].breadcrumbPropertyValueDependencyId` | integer | 否 | 面包屑属性值依赖ID |
