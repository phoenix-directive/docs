#!/usr/bin/env python3
"""
Export all threads of a common.xyz topic (default: Terra "2. Governance and Proposals")
to Markdown - one file per post, with full body text, all comments (nested replies),
and all embedded images downloaded locally.

Usage (from the folder you want the export in):
    python export_common.py
    python export_common.py --out D:\\other\\pd-docs\\common_backup
    python export_common.py --no-images

Only uses the Python standard library.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://common.xyz/api/internal/trpc/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
TOPIC_URL = "https://common.xyz/terra/discussions/1280-2.%20Governance%20and%20Proposals"


# ---------------------------------------------------------------- http helpers
def http_get(url, binary=False, retries=4, timeout=60):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                ctype = r.headers.get("Content-Type", "")
            return (data, ctype) if binary else data.decode("utf-8")
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (400, 401, 403, 404, 410):
                break  # permanent
        except Exception as e:  # network hiccup -> retry
            last = e
        time.sleep(1.5 * (attempt + 1))
    raise last


def trpc(procedure, params):
    url = API + procedure + "?input=" + urllib.parse.quote(json.dumps(params, separators=(",", ":")))
    j = json.loads(http_get(url))
    if "result" not in j:
        raise RuntimeError(f"{procedure} failed: {str(j)[:300]}")
    return j["result"]["data"]


def full_text(obj):
    """Bodies in list/get responses are cut at 2000 chars; the full text lives at content_url."""
    cu = obj.get("content_url")
    if cu:
        try:
            return http_get(cu)
        except Exception as e:
            print(f"  ! could not fetch full text {cu}: {e}", file=sys.stderr)
    return obj.get("body") or ""


# ---------------------------------------------------------------- fetching
def get_threads(community, topic_id):
    threads, page = [], 1
    while True:
        d = trpc("thread.getThreads", {
            "community_id": community, "limit": 50, "stage": "", "topic_id": topic_id,
            "archived": False, "withXRecentComments": 0, "direction": "forward", "cursor": page,
        })
        threads += d["results"]
        if page >= (d.get("totalPages") or 1):
            break
        page += 1
    return threads


def get_comment_level(thread_id, community, parent_id=None):
    out, page = [], 1
    while True:
        p = {"thread_id": thread_id, "community_id": community, "limit": 50, "page": page, "cursor": page}
        if parent_id is not None:
            p["parent_id"] = parent_id
        d = trpc("comment.getComments", p)
        out += d["results"]
        if page >= (d.get("totalPages") or 1):
            break
        page += 1
    return out


def get_all_comments(thread_id, community):
    seen, result = set(), []

    def walk(parent):
        for c in get_comment_level(thread_id, community, parent):
            if c["id"] in seen:
                continue
            seen.add(c["id"])
            result.append(c)
            if c.get("reply_count"):
                walk(c["id"])

    walk(None)
    for c in result:
        c["body"] = full_text(c)
    return result


def fetch_thread(t, community):
    try:
        full = trpc("thread.getThreadById", {"thread_id": t["id"]})
    except Exception as e:
        print(f"  ! getThreadById {t['id']} failed: {e}", file=sys.stderr)
        full = t
    merged = {**t, **{k: v for k, v in full.items() if v is not None}}
    merged["body"] = full_text(merged)
    merged["_comments"] = get_all_comments(t["id"], community)
    return merged


# ---------------------------------------------------------------- images
IMG_RE = re.compile(r'!\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)|<img[^>]+src=["\']([^"\']+)["\']', re.I)


def sniff_ext(data, ctype):
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:3] == b"\xff\xd8\xff":
        return "jpg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if b"<svg" in data[:500].lower():
        return "svg"
    if ctype.startswith("image/"):
        return ctype.split("/")[1].split(";")[0].replace("jpeg", "jpg")
    return None


def download_images(urls, img_dir):
    os.makedirs(img_dir, exist_ok=True)
    mapping, failed = {}, {}

    def one(u):
        base = "img_" + hashlib.sha1(u.encode()).hexdigest()[:12]
        for f in os.listdir(img_dir):  # already downloaded earlier run
            if f.startswith(base + "."):
                return u, f, None
        try:
            data, ctype = http_get(u, binary=True)
            ext = sniff_ext(data, ctype)
            if not ext:
                return u, None, f"not an image ({ctype})"
            name = f"{base}.{ext}"
            with open(os.path.join(img_dir, name), "wb") as fh:
                fh.write(data)
            return u, name, None
        except Exception as e:
            return u, None, str(e)

    with ThreadPoolExecutor(8) as ex:
        for u, name, err in ex.map(one, urls):
            if name:
                mapping[u] = name
            else:
                failed[u] = err
    return mapping, failed


# ---------------------------------------------------------------- markdown
def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "untitled").lower()).strip("-")
    return s[:70] or "untitled"


def who(name, addr):
    return f"{name or 'Anonymous'}" + (f" (`{addr}`)" if addr else "")


def localize(text, mapping):
    for u, name in mapping.items():
        text = text.replace(u, "images/" + name)
    return text


def thread_markdown(t, mapping, community):
    cs = t["_comments"]
    by_parent = {}
    for c in cs:
        by_parent.setdefault(c.get("parent_id") or "root", []).append(c)
    for lst in by_parent.values():
        lst.sort(key=lambda c: c.get("created_at") or "")

    collab = []
    for c in t.get("collaborators") or []:
        n = (((c.get("User") or {}).get("profile") or {}).get("name")) or c.get("address") or c.get("name")
        if n:
            collab.append(n)
    links = []
    for l in t.get("links") or []:
        links.append(f"{l.get('source', '')}: " + (f"{l['title']} – " if l.get("title") else "") + str(l.get("identifier") or l.get("url") or ""))

    addr = (t.get("Address") or {}).get("address")
    md = [f"# {t['title']}", ""]
    md.append(f"- **Thread ID:** {t['id']}")
    md.append(f"- **Author:** {who(t.get('profile_name'), addr)}")
    if collab:
        md.append(f"- **Collaborators:** {', '.join(collab)}")
    md.append(f"- **Created:** {t.get('created_at')}")
    md.append(f"- **Last edited:** {t.get('last_edited') or '-'}")
    md.append(f"- **Stage:** {t.get('stage') or '-'}")
    md.append(f"- **Views:** {t.get('view_count', '-')}")
    md.append(f"- **Reactions:** {t.get('reaction_count', 0)}")
    md.append(f"- **Comments:** {len(cs)}")
    md.append(f"- **Source:** https://common.xyz/{community}/discussion/{t['id']}-{slug(t['title'])}")
    if t.get("url"):
        md.append(f"- **Link:** {t['url']}")
    if links:
        md.append(f"- **Linked:** {'; '.join(links)}")
    md += ["", "---", "", localize(t["body"], mapping).strip(), "", "---", "", f"## Comments ({len(cs)})", ""]

    def render(parent, depth):
        out = []
        for c in by_parent.get(parent, []):
            pre = "> " * depth
            head = f"**{who(c.get('profile_name'), c.get('address'))}** — {c.get('created_at')}"
            if c.get("updated_at") and c.get("updated_at") != c.get("created_at"):
                head += f" (edited {c['updated_at']})"
            if c.get("deleted_at"):
                head += " [deleted]"
            if c.get("reaction_count"):
                head += f" — 👍 {c['reaction_count']}"
            body = "_[deleted]_" if c.get("deleted_at") else localize(c.get("body") or "", mapping).strip()
            block = f"{head}\n\n{body}"
            out.append("\n".join(pre + line for line in block.split("\n")))
            out.append("")
            out += render(c["id"], depth + 1)
        return out

    md += render("root", 0) if cs else ["_No comments._"]
    return "\n".join(md).replace("\r", "") + "\n"


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--community", default="terra")
    ap.add_argument("--topic", type=int, default=1280)
    ap.add_argument("--no-images", action="store_true")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    print("Listing threads ...")
    threads = get_threads(args.community, args.topic)
    print(f"  {len(threads)} threads")

    print("Fetching full posts + comments ...")
    full = []
    with ThreadPoolExecutor(6) as ex:
        for i, t in enumerate(ex.map(lambda t: fetch_thread(t, args.community), threads), 1):
            full.append(t)
            print(f"  [{i}/{len(threads)}] {t['id']} {t['title'][:60]}  ({len(t['_comments'])} comments)")

    mapping, failed = {}, {}
    if not args.no_images:
        urls = []
        for t in full:
            for text in [t["body"]] + [c.get("body") or "" for c in t["_comments"]]:
                for m in IMG_RE.finditer(text):
                    u = m.group(1) or m.group(2)
                    if u.startswith("http") and u not in urls:
                        urls.append(u)
        print(f"Downloading {len(urls)} images ...")
        mapping, failed = download_images(urls, os.path.join(args.out, "images"))
        print(f"  ok: {len(mapping)}  failed: {len(failed)}")

    print("Writing markdown ...")
    rows = []
    for t in full:
        name = f"{(t.get('created_at') or '')[:10]}_{t['id']}_{slug(t['title'])}.md"
        with open(os.path.join(args.out, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(thread_markdown(t, mapping, args.community))
        rows.append((t, name))

    idx = [f"# {args.community} – topic {args.topic} (backup)", "",
           f"Source: {TOPIC_URL}", f"Exported: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
           f"Threads: {len(rows)}", "",
           "| Date | ID | Title | Comments | File |", "|---|---|---|---|---|"]
    for t, name in rows:
        title = t["title"].replace("|", "\\|")
        idx.append(f"| {(t.get('created_at') or '')[:10]} | {t['id']} | {title} | {len(t['_comments'])} | [{name}]({name}) |")
    if mapping:
        idx += ["", f"## Images ({len(mapping)})", ""] + [f"- images/{n} ← {u}" for u, n in mapping.items()]
    if failed:
        idx += ["", f"### Not downloaded ({len(failed)})", ""] + [f"- {u} ({e})" for u, e in failed.items()]
    with open(os.path.join(args.out, "_index.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(idx) + "\n")

    print(f"Done: {len(rows)} posts, {sum(len(t['_comments']) for t in full)} comments, "
          f"{len(mapping)} images -> {args.out}")


if __name__ == "__main__":
    main()
