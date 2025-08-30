import os
import yaml

HELPER_DIR = os.path.dirname(os.path.abspath(__file__))  # path/website/helpers
WEBSITE_DIR = os.path.abspath(os.path.join(HELPER_DIR, ".."))  # path/website
CHECK_DIR = os.path.join(WEBSITE_DIR, "content", "docs")  # path/website/content/docs
OUTPUT_FILE = os.path.join(WEBSITE_DIR, "data", "docs_sidebar.yaml")  # path/website/data/docs_sidebar.yaml

IGNORED_DIRS = {"images", "assets", "static", ".git", ".github", ".idea", "__pycache__"}

def read_md_title_toml(md_path: str) -> str | None:
    """
    从 TOML front matter 读取 title
    """
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            second_line = f.readline().strip()
            third_line = f.readline().strip()
            return third_line.split('"')[1]
    except Exception:
        return None

def _nice_title(name: str) -> str:
    """把目录或文件名转成标题"""
    base = name.replace("-", " ").replace("_", " ").strip()
    return base.capitalize() if base else name

def build_sidebar(dir_path: str, url_path: str = ""):
    node = {}

    entries = sorted(os.listdir(dir_path), key=lambda s: s.lower())
    has_index = "index.md" in entries

    # 如果目录有 index.md → kind: page
    if has_index:
        node = {
            "kind": "page",
            "title": _nice_title(os.path.basename(dir_path)),
            "link": url_path + "/"
        }
        return node

    # 否则 → kind: section
    node = {
        "kind": "section",
        "title": _nice_title(os.path.basename(dir_path)),
        "children": {}
    }

    # 先处理同级 md 文件（排除 index.md）
    for fn in entries:
        full = os.path.join(dir_path, fn)
        if os.path.isfile(full) and fn.endswith(".md") and fn != "index.md":
            filename = os.path.splitext(fn)[0]
            title = read_md_title_toml(full) or filename
            node["children"][filename] = {
                "kind": "page",
                "title": title,
                "link": f"{url_path}/{filename}/"
            }

    # 递归处理子目录
    for fn in entries:
        full = os.path.join(dir_path, fn)
        if os.path.isdir(full) and fn not in IGNORED_DIRS:
            child_url = f"{url_path}/{fn}"
            node["children"][fn] = build_sidebar(full, child_url)

    return node

if __name__ == "__main__":
    sidebar = {"docs": build_sidebar(CHECK_DIR)}

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(sidebar, f, allow_unicode=True, sort_keys=False)

    print(f"Sidebar YAML generated at: {OUTPUT_FILE}")
