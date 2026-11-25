# raw/ —— apifox 原始抓取件

每篇接口的原始 Markdown（含完整 OpenAPI 3.0 YAML），文件名 `{apifox文件id}_{标题}.md`，
`source/*.md` 里每节的「原文」一行就是指向这里的文件。

- 来源：妙手开放平台 apifox 分享文档（需访问密码）
- 抓取：`docs-site-md-mirror` 技能的 `fetch_apifox.py`，2026-11-25 全量同步（233 个接口 + 1 篇快速接入）
- `llms.txt`：站点原始索引，保留以核对条目是否漏抓

重新抓取后，用 `scripts/build_source.py` 重新编译 `source/`：

```bash
pip install pyyaml
python3 scripts/build_source.py --raw raw --out .
python3 scripts/generate.py
```

注意：`build_source.py` 依赖 `raw/llms.txt` 的顺序与 `{id}_{标题}` 命名来建立映射。
