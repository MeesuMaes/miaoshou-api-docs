# 获取支持的翻译语言配置


- 层级：开放平台 > 商品 > AI公共服务 > 图片处理
- 方法+路径：`POST /open/v1/product/common/translate/get_support_language_config`
- 类型：读
- 原文：[484286513e0](https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/484286513e0.md)

公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见[快速接入](/quick-start)签名机制）

**请求参数（JSON Body）**

无


**响应字段（200）**

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `result` | string | 否 |  |
| `code` | string | 否 |  |
| `data` | object | 否 |  |
| `data.supportLanguageConfig` | object | 否 | 支持的语言配置 结构为 \{平台: \{类型: \{源语言: [目标语言列表]\}\}\} 平台可选值：aeAi / tosoiot / ykt 类型可选值：realTime（实时翻译）/ idle（闲时翻译） 源语言和目标语言为语言编码，如 zh、en、ja 等 示例：\{"ali": \{"realTime": \{"zh": ["en", "ja"], "en": ["zh", "ja"]\}\}\} |
