# 妙手开放平台 API 文档

由 apifox 分享文档整理的妙手开放平台 API 文档，基于 Rspress 构建，发布于 https://meesumaes.github.io/miaoshou-api-docs/

- 当前同步：**233 个接口**（2026-11-25），商品 175 / 仓储 21 / 采购 18 / 包裹 17 / 货源账号 2。
- 本轮新增：**SHEIN 全托、半托采集箱各 18 个**（`shein` / `shein_choice`）、仓储**出入库** 3 个、运单批量 2 个、采购记录 2 个、1688 货源反查 1 个、TK 手动建品 1 个。

## 目录结构与生成

- `raw/`：apifox 原始抓取件（每页含完整 OpenAPI 3.0 YAML），文件名 `{文件id}_{标题}.md`。
- `source/`：编译后的文档（README、01–05 模块、shein-notes、index.json）。
- `scripts/build_source.py`：`raw/` → `source/`（字段表 + index.json + README 索引），需要 PyYAML。
- `scripts/generate.py`：`source/` → `docs/` 下全部页面（每个接口一页）和 `sidebar.json`（多级、默认折叠、POST 徽标）。
- 已接入 `@rspress/plugin-llms`，构建产物含 `llms.txt`、`llms-full.txt` 和每页 `.md`。
- 原始 apifox 页面链接保留在每个接口页的「原文」一行，字段说明均摘自原文 OpenAPI 定义。

```bash
pip install pyyaml
python3 scripts/build_source.py --raw raw --out .   # 重新编译 source/
python3 scripts/generate.py                          # 重新生成页面和侧边栏
npm install
npm run dev                   # 本地预览
npm run build                 # 构建到 doc_build/
```

> 本地构建若报 `Rspack FS Error: IO error`，是 Node 被注入了文件系统代理，`env -u NODE_OPTIONS npm run build` 即可。

推送到 main 后由 GitHub Actions 自动发布到 GitHub Pages。
