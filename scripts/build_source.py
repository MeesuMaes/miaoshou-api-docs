#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把抓取下来的 Apifox 原始 Markdown（每页含 OpenAPI 3.0 YAML）编译成
source/*.md（人读的字段表）+ source/index.json（生成 docs 页面用）。

用法：
  python3 scripts/build_source.py --raw ../妙手开放平台文档 --out .
  python3 scripts/build_source.py --raw ../妙手开放平台文档 --out . --verify

--raw 指向用 docs-site-md-mirror 技能抓下来的目录（需含 api/ 与 llms.txt）。
--verify 只做比对，不写文件。

依赖：PyYAML（pip install pyyaml）。
"""
import argparse
import glob
import json
import os
import re
import sys

import yaml

APIFOX = "https://s.apifox.cn/fd54e57e-9b98-4c34-bada-306221c39e68/"
LOCAL = ""      # 由 --raw 注入
LLMS = ""       # 由 --raw 注入

MODULES = ["商品", "包裹", "采购", "仓储", "货源账号"]
FILE_OF = {"商品": "01-product.md", "包裹": "02-package.md", "采购": "03-purchase.md",
           "仓储": "04-warehouse.md", "货源账号": "05-source-account.md"}

# ---- 读/写/处理 判定 ----
PROC = re.compile(r"AI|翻译|润色|白底|智能消除|打水印")
WRITE = re.compile(r"创建|添加|编辑|保存|删除|发布|认领|提交|上传|同步|取消|标记|设置|申请|发货|修改|填写|更新|采集货源|下单|新建")


READ_HEAD = re.compile(r"^(获取|查询|搜索|查看|批量获取|根据|下载|导出)")


def classify(title: str) -> str:
    if READ_HEAD.match(title) or "发布记录" in title:
        return "读"
    if PROC.search(title):
        return "处理(生成内容)"
    if WRITE.search(title):
        return "写"
    return "读"


def one_line(s: str) -> str:
    if not s:
        return ""
    s = re.sub(r"\s*\n\s*", " ", str(s)).strip()
    return s.replace("|", "｜")


REF = re.compile(r"^#/components/schemas/(.+)$")


def deref(node, doc, depth=0):
    """递归展开 $ref / allOf，返回纯内联结构。"""
    if depth > 12 or not isinstance(node, (dict, list)):
        return node
    if isinstance(node, list):
        return [deref(x, doc, depth + 1) for x in node]
    ref = node.get("$ref")
    if ref:
        m = REF.match(str(ref).strip())
        if m:
            target = (doc.get("components") or {}).get("schemas", {}).get(m.group(1), {})
            merged = deref(target, doc, depth + 1)
            rest = {k: v for k, v in node.items() if k != "$ref"}
            if rest and isinstance(merged, dict):
                merged = {**merged, **deref(rest, doc, depth + 1)}
            return merged
        return {}
    out = {k: deref(v, doc, depth + 1) for k, v in node.items()}
    # allOf 合并（保留首个出现的属性顺序）
    if "allOf" in out:
        merged = {"properties": {}, "required": [], "x-apifox-orders": []}
        for sub in out["allOf"]:
            if not isinstance(sub, dict):
                continue
            for k, v in (sub.get("properties") or {}).items():
                merged["properties"].setdefault(k, v)
            merged["required"] += sub.get("required") or []
            merged["x-apifox-orders"] += [k for k in (sub.get("x-apifox-orders") or []) if k not in merged["x-apifox-orders"]]
        for k in ("properties", "required", "x-apifox-orders"):
            if out.get(k):
                if k == "properties":
                    for kk, vv in out[k].items():
                        merged["properties"].setdefault(kk, vv)
                elif k == "required":
                    merged[k] += out[k]
                else:
                    merged[k] += [x for x in out[k] if x not in merged[k]]
        if not any(k in out for k in ("type", "description")):
            merged["type"] = "object"
        out = {**{k: v for k, v in out.items() if k != "allOf"}, **merged}
    return out


def type_of(p: dict) -> str:
    t = p.get("type")
    if t == "array":
        it = p.get("items") or {}
        inner = it.get("type") or ("object" if it.get("properties") else "")
        return f"array<{inner}>" if inner else "array"
    return t or "object"


def ordered(props: dict, orders) -> list:
    keys = [k for k in (orders or []) if k in props]
    keys += [k for k in props if k not in keys]
    return keys


MAX_DEPTH = 7


def flatten(schema: dict, prefix: str = "", required=None, is_request=True, out=None,
            depth=0, seen=None):
    """把 schema 递归拍平成 (字段名, 类型, 是否必填, 说明) 列表。

    seen 记录「当前路径上」已展开的 schema，遇到自引用（如
    platformLogisticsProductMap → toLogisticsAgentProductInfo → 回到自身）直接停止，
    否则单页会膨胀到几百 KB。
    """
    out = out if out is not None else []
    seen = seen if seen is not None else set()
    if not isinstance(schema, dict) or depth > MAX_DEPTH:
        return out
    sid = id(schema)
    if sid in seen:
        return out
    seen = seen | {sid}
    props = schema.get("properties") or {}
    req = set(schema.get("required") or [])
    for k in ordered(props, schema.get("x-apifox-orders")):
        p = props[k] or {}
        name = f"{prefix}{k}"
        desc = one_line(p.get("description") or p.get("title") or "")
        ex = p.get("examples") or p.get("example")
        if ex is not None:
            if not isinstance(ex, list):
                ex = [ex]
            desc = (desc + f" 例:{json.dumps(ex, ensure_ascii=False, separators=(',', ':'))}").strip()
        out.append((name, type_of(p), "是" if k in req else "否", desc))
        # 递归：对象属性 / 对象数组
        if p.get("properties"):
            flatten(p, name + ".", req, is_request, out, depth + 1, seen)
        else:
            items = p.get("items") or {}
            if items.get("properties"):
                flatten(items, name + "[].", req, is_request, out, depth + 1, seen)
    return out


def table(rows) -> str:
    lines = ["| 字段 | 类型 | 必填 | 说明 |", "|---|---|---|---|"]
    for n, t, r, d in rows:
        lines.append(f"| `{n}` | {t} | {r} | {d} |")
    return "\n".join(lines)


MAX_EXAMPLE_LINES = 120


def pretty(ex) -> str:
    """example 可能是 JSON 字符串或对象，统一成 2 空格缩进 JSON；过长的截断。

    apifox 的 mock 示例在递归结构（如 platformLogisticsProductMap）上会展开成
    几百 KB，直接铺到页面里既慢又没价值，统一截到 120 行。
    """
    if isinstance(ex, str):
        try:
            ex = json.loads(ex)
        except Exception:
            return ex.strip()
    text = json.dumps(ex, ensure_ascii=False, indent=2)
    lines = text.splitlines()
    if len(lines) > MAX_EXAMPLE_LINES:
        lines = lines[:MAX_EXAMPLE_LINES] + ["  ... （示例过长，已截断）"]
    return "\n".join(lines)


def parse_doc(path: str):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    if not m:
        return None
    doc = yaml.safe_load(m.group(1))
    paths = doc.get("paths") or {}
    if not paths:
        return None
    api_path, item = next(iter(paths.items()))
    method = next(iter(item))
    op = item[method]
    tags = op.get("tags") or []
    tag = tags[0] if tags else ""
    req_media = ((op.get("requestBody") or {}).get("content") or {}).get("application/json") or {}
    req_schema = req_media.get("schema") or {}
    resp = (op.get("responses") or {})
    resp_obj = resp.get("200") or resp.get(200) or {}
    resp_media = (resp_obj.get("content") or {}).get("application/json") or {}
    resp_schema = resp_media.get("schema") or {}
    return {
        "title": (op.get("summary") or "").strip(),
        "desc": one_line(op.get("description")),
        "path": api_path,
        "method": method.upper(),
        "tag": tag,
        "req_schema": deref(req_schema, doc),
        "resp_schema": deref(resp_schema, doc),
        "req_example": req_media.get("example"),
        "resp_example": resp_media.get("example"),
        "file": path,
    }


def load_llms():
    """返回有序列表 [(crumb, title, aid, 说明)]，顺序即 apifox 导航顺序。"""
    out = []
    for line in open(LLMS, encoding="utf-8"):
        m = re.match(r"^- (.+?) \[(.+?)\]\((\S+?)\): ?(.*)$", line.strip())
        if not m:
            continue
        crumb, title, url, desc = m.groups()
        if crumb.strip().lower() == "docs":
            continue
        aid = url.rstrip("/").split("/")[-1].replace(".md", "")
        out.append((crumb.strip(), title.strip(), aid, desc.strip()))
    return out


def fname(title: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", title).strip()


def render(doc, aid, llms_desc):
    crumb = doc["tag"].replace("/", " > ")
    lines = [f"### {doc['title']}", "",
             f"- 层级：{crumb}",
             f"- 方法+路径：`{doc['method']} {doc['path']}`",
             f"- 类型：{classify(doc['title'])}",
             f"- 原文：[{aid}]({APIFOX}{aid}.md)（本地 raw/{aid}_{fname(doc['title'])}.md）"]
    note = llms_desc or doc["desc"]
    if note:
        lines.append(f"- 说明：{note}")
    req_rows = flatten(doc["req_schema"])
    resp_rows = flatten(doc["resp_schema"], is_request=False)
    lines += ["", "公共请求头：`x-app-key`、`x-timestamp`、`x-sign`（见 README 签名机制）", "",
              "**请求参数（JSON Body）**", "", table(req_rows) if req_rows else "无", "", "",
              "**响应字段（200）**", "", table(resp_rows) if resp_rows else "无"]
    blocks = []
    for key, label in (("req_example", "请求示例"), ("resp_example", "响应示例 200")):
        ex = doc.get(key)
        if ex is None:
            continue
        if isinstance(ex, list) and ex and all(isinstance(x, dict) and "value" in x for x in ex):
            for i, x in enumerate(ex, 1):
                blocks.append((f"{label} 示例 {i}", x["value"]))
        else:
            blocks.append((label, ex))
    for label, ex in blocks:
        lines += ["", f"<details><summary>{label}</summary>", "", "```json", pretty(ex), "```", "</details>"]
    return "\n".join(lines)


def collect():
    """返回 [(top, sub, doc, aid, llms_desc)]，按模块/层级/原始顺序。"""
    docs = {}
    for p in glob.glob(os.path.join(LOCAL, "api/**/*.md"), recursive=True):
        d = parse_doc(p)
        if not d or not d["tag"].startswith("开放平台/"):
            continue
        docs[(d["tag"].replace("/", " > "), d["title"])] = d
    items = []
    for crumb, title, aid, desc in load_llms():
        d = docs.get((crumb, title))
        if not d:
            print(f"  ! llms 有条目但没解析到原文: {crumb} / {title}")
            continue
        parts = d["tag"].split("/")[1:]
        items.append({"top": parts[0],
                      "sub": ">".join(parts[1:]) if len(parts) > 1 else "",
                      "doc": d, "aid": aid, "desc": desc})
    return items


def group_key(it):
    return it["sub"] or "-"


def build_module(top, items):
    """按 sub 分组，保持首次出现顺序。"""
    groups = {}
    for it in items:
        groups.setdefault(group_key(it), []).append(it)
    out = [f"# 妙手开放平台 · {top}模块", "",
           f"> 由 apifox 分享文档整理（{len(items)} 个接口）。字段说明原样摘自 OpenAPI 定义，未做改写；请求/响应以原文为准。",
           "", "## 目录", ""]
    for g, its in groups.items():
        out.append(f"- {g}（{len(its)}）")
    out.append("")
    for g, its in groups.items():
        out += [f"## {g}", ""]
        out.append("\n\n\n---\n\n".join(render(it["doc"], it["aid"], it["desc"]).rstrip() for it in its))
    return "\n".join(out).rstrip() + "\n"


def build_index(items):
    return [[it["top"], it["sub"], it["doc"]["title"], it["doc"]["method"], it["doc"]["path"],
             classify(it["doc"]["title"]), it["aid"]] for it in items]


FILE_OF_ = FILE_OF


def update_readme(repo, items):
    """更新 source/README.md 顶部统计 + 「二、全部接口索引」表，保留接入说明原文。"""
    import collections
    path = os.path.join(repo, "source", "README.md")
    text = open(path, encoding="utf-8").read()
    cnt = collections.Counter(it["top"] for it in items)
    wr = collections.Counter(it["top"] for it in items if classify(it["doc"]["title"]) == "写")
    typ = collections.Counter(classify(it["doc"]["title"]) for it in items)
    head = text.split("## 二、全部接口索引", 1)[0]

    # 顶部说明与文件表
    head = re.sub(r"> 来源：妙手开放平台 apifox 分享文档（1 篇快速接入 \+ \d+ 篇接口，[^）]*）。",
                  f"> 来源：妙手开放平台 apifox 分享文档（1 篇快速接入 + {len(items)} 篇接口，2026-11-25 同步）。", head)
    for top, f in FILE_OF_.items():
        head = re.sub(rf"\| \[{re.escape(f)}\]\([^)]*\) \| [^|]+ \| \d+ \| \d+ \|",
                      f"| [{f}]({f}) | {top}" + ("（含 SHEIN 全托/半托）" if top == "商品" else "（含出入库）" if top == "仓储" else "")
                      + f" | {cnt[top]} | {wr[top]} |", head)
    head = re.sub(r"合计 \d+ 个接口。类型：[^\n]*",
                  f"合计 {len(items)} 个接口。类型：读 {typ['读']} / 写 {typ['写']} / 处理(生成内容，AI/翻译/水印类) {typ['处理(生成内容)']} —— 按标题判定，仅供参考。", head)

    out = [head.rstrip(), "", "## 二、全部接口索引", ""]
    order = [t for t in MODULES if cnt[t]]
    for top in order:
        rows = [it for it in items if it["top"] == top]
        out += ["", f"### {top}（{len(rows)}，详见 [{FILE_OF_[top]}]({FILE_OF_[top]})）", "",
                "| 子模块 | 接口 | 方法 | 路径 | 类型 | 原文 |", "|---|---|---|---|---|---|"]
        for it in rows:
            d = it["doc"]
            out.append(f"| {it['sub'] or '-'} | {d['title']} | {d['method']} | `{d['path']}` | "
                       f"{classify(d['title'])} | [链接]({APIFOX}{it['aid']}.md) |")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    global LOCAL, LLMS
    ap = argparse.ArgumentParser(description="把 Apifox 抓取结果编译成 source/ 与 docs/ 的输入")
    ap.add_argument("--raw", required=True, help="抓取目录（含 api/ 与 llms.txt）")
    ap.add_argument("--out", required=True, help="仓库根目录（写入 source/ 与 README 索引）")
    ap.add_argument("--verify", action="store_true", help="只与现有 source/ 比对，不写文件")
    a = ap.parse_args()
    LOCAL = os.path.abspath(a.raw)
    LLMS = os.path.join(LOCAL, "llms.txt")
    verify = a.verify
    items = collect()
    print(f"解析到 {len(items)} 个接口")
    miss = [it for it in items if not it["aid"]]
    if miss:
        print(f"⚠ 未匹配到 aid 的: {len(miss)}")
        for it in miss[:5]:
            print("   ", it["doc"]["tag"], it["doc"]["title"])

    out_dirs = {t: [it for it in items if it["top"] == t] for t in MODULES}
    other = [it for it in items if it["top"] not in MODULES]
    if other:
        print("⚠ 未知顶层模块:", {(it["top"], it["doc"]["title"]) for it in other})

    if not verify:
        repo = os.path.abspath(a.out)
        src = os.path.join(repo, "source")
        os.makedirs(src, exist_ok=True)
        for top, its in out_dirs.items():
            text = build_module(top, its)
            open(os.path.join(src, FILE_OF[top]), "w", encoding="utf-8").write(text)
            print(f"  {FILE_OF[top]}: {len(its)} 接口")
        json.dump(build_index(items), open(os.path.join(src, "index.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("  index.json:", len(items), "条")
        update_readme(repo, items)
        print("  README.md 已同步统计与索引")
        return

    if verify:
        repo = os.path.join(os.path.abspath(a.out), "source")
        total_diff = 0
        for top, its in out_dirs.items():
            f = os.path.join(repo, FILE_OF[top])
            if not os.path.exists(f):
                continue
            old = open(f, encoding="utf-8").read()
            new = build_module(top, its)
            # 抽出各自的 ### 段落做比对
            def sections(t):
                d = {}
                for part in re.split(r"^### ", t, flags=re.M)[1:]:
                    title, body = part.split("\n", 1)
                    body = re.split(r"^## ", body, flags=re.M)[0]
                    d[title.strip()] = body
                return d
            so, sn = sections(old), sections(new)
            only_old = set(so) - set(sn)
            only_new = set(sn) - set(so)
            diff = [k for k in (set(so) & set(sn)) if so[k].rstrip() != sn[k].rstrip()]
            print(f"\n[{top}] 旧 {len(so)} / 新 {len(sn)} 段；仅旧有 {len(only_old)}，仅新有 {len(only_new)}，内容不同 {len(diff)}")
            if only_old:
                print("   仅旧有:", [k[:30] for k in sorted(only_old)][:8])
            if only_new:
                print("   仅新有:", [k[:30] for k in sorted(only_new)][:5])
            if diff:
                k = diff[0]
                import difflib
                d = list(difflib.unified_diff(so[k].splitlines(), sn[k].splitlines(),
                                              "repo", "gen", lineterm="", n=1))
                print(f"   首个差异段: {k.strip('# ')}")
                for l in d[:24]:
                    print("   ", l)
            total_diff += len(diff) + len(only_old) + len(only_new)
        print(f"\n合计差异项：{total_diff}")
        return


if __name__ == "__main__":
    main()
