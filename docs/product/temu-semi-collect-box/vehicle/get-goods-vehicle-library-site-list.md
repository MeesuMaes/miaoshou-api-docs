# 获取车型库站点列表


- 层级：开放平台 > 商品 > TEMU半托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj_choice/vehicle_library/get_goods_vehicle_library_site_list`
- 类型：读
- 原文：[468726296e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468726296e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cid` | integer | 否 | 类目ID，区分摩托车和汽车 ，不传返回全部 |


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.goodsVehicleLibrarySiteList` | array&lt;object> | 否 | 车型库站点列表，每项代表一个销售地区的车型库（如美国、欧洲等）。 根据产品的销售地区选择对应站点，取其 vehicleLibraryId 用于后续接口 |
| `data.goodsVehicleLibrarySiteList[].vehicleLibraryId` | integer | 否 | 车型库站点ID，选定站点后传入 getGoodsVehicleLibrarySiteTopPropDependencyList 获取顶级车型节点 |
| `data.goodsVehicleLibrarySiteList[].name` | string | 否 | 站点名称，如"美国"、"欧洲"，用于展示给用户选择 |
| `data.goodsVehicleLibrarySiteList[].pid` | integer | 否 | 属性ID |
| `data.goodsVehicleLibrarySiteList[].pidName` | string | 否 | 属性名称（中文），如"品牌"、"车系" |
| `data.goodsVehicleLibrarySiteList[].pidNameEn` | string | 否 | 属性名称（英文） |
| `data.goodsVehicleLibrarySiteList[].level` | integer | 否 | 层级（1=品牌，2=车系，3=年份，4=车型，5=发动机类型） |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "cid": 21502
}
```
&lt;/details>
