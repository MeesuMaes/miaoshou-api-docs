# 妙手开放平台 API 文档

由 apifox 分享文档整理的妙手开放平台 API 文档，基于 Rspress 构建，发布于 https://meesumaes.github.io/miaoshou-api-docs/

## 目录结构与生成

- `source/`：整理好的原始文档（README、01–05 模块、shein-notes、index.json）。
- `scripts/generate.py`：从 `source/` 生成 `docs/` 下全部页面（每个接口一页）和 `sidebar.json`（多级、默认折叠、POST 徽标）。
- 已接入 `@rspress/plugin-llms`，构建产物含 `llms.txt`、`llms-full.txt` 和每页 `.md`。

```bash
python3 scripts/generate.py   # 重新生成页面和侧边栏
npm install
npm run dev                   # 本地预览
npm run build                 # 构建到 doc_build/
```

推送到 main 后由 GitHub Actions 自动发布到 GitHub Pages。
