# 获取车型库站点属性结构映射


- 层级：开放平台 > 商品 > TEMU全托采集箱 > 车型库
- 方法+路径：`POST /open/v1/product/collect_box/pddkj/vehicle_library/goods_vehicle_library_id_and_site_pid_info_map`
- 类型：读
- 原文：[468724009e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/468724009e0.md)

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
| `data.goodsVehicleLibraryIdAndSitePidInfoMap` | object | 否 | 车型库站点属性结构映射，key 为 vehicleLibraryId，value 为该站点的属性层级信息列表。 用于了解某站点车型库包含哪些层级属性（品牌/车系/年款等）及其对应的 pid， 结合 getVehicleLibraryPropDependencyTree 的树形数据使用 SitePidInfo 结构： - pddkjGoodsVehicleLibraryId: string 平台商品车型库ID - vehicleLibraryId: string 车型库ID - name: string 站点名称，如"美国站、加拿大站" - pidNameEn: string 属性英文名，如"Make"、"Model"、"Year" - parentPropertyDependencyId: string 父属性依赖ID - propertyDependencyId: string 属性依赖ID - pid: string 属性pid - pidName: string 属性中文名，如"汽车品牌"、"汽车型号" - level: string 层级序号 - status: string 状态，1=启用 |


&lt;details>&lt;summary>请求示例&lt;/summary>

```json
{
  "cid": 21502
}
```
&lt;/details>
