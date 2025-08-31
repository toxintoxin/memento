import os
import re
import yaml
from pathlib import Path

WEBSITE_DIR = os.path.dirname(os.path.abspath(__file__))  # path/website
CONTENT_DIR = os.path.join(WEBSITE_DIR, "content")  # path/website/content

TARGET_DIR = os.path.join(CONTENT_DIR, "docs")
OUTPUT_FILE = os.path.join(WEBSITE_DIR, "data", "docs_tree.yaml")


def slugify(input_str):
    # 1. 转小写
    slug = input_str.lower()
    # 2. 替换空格为 "-"
    slug = slug.replace(' ', '-')

    return slug

def slugify_link(input_str):
    # 去掉后缀
    relative_path = Path(input_str).with_suffix('')  
    # 转为 URL 风格
    url_style = relative_path.as_posix()
    # slugify
    url_style = slugify(url_style)

    return url_style

def read_md_title_toml(md_path: str) -> str | None:
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            second_line = f.readline().strip()
            third_line = f.readline().strip()
            return third_line.split('"')[1]
    except Exception:
        return None

def process_directory(directory_path, content_path):

    base_path = Path(content_path)
    dir_path = Path(directory_path)
    dir_name = dir_path.name
    
    # 检查是否存在index.md
    index_md = dir_path / "index.md"
    if index_md.exists():
        # 有index.md，leaf bundle
        return {
            'name': slugify(dir_name),
            'kind': 'page',
            'title': dir_name,
            'link': slugify_link(dir_path.relative_to(base_path))
        }
    else:
        # 没有index.md，创建section节点并处理子内容，实际并没有那个html
        node = {
            'name': slugify(dir_name),
            'kind': 'section',
            'title': dir_name,
            'link': slugify_link(dir_path.relative_to(base_path)),
            'children': []
        }
        
        # 获取所有子项
        for item in dir_path.iterdir():
            if item.is_dir():
                # 递归处理子目录
                child_node = process_directory(item, base_path)
                if child_node:
                    node['children'].append(child_node)
            elif item.is_file() and item.suffix.lower() == '.md' and item.name != 'index.md':
                # 处理Markdown文件（排除index.md）
                node['children'].append({
                    'name': item.stem,  # 去掉扩展名的文件名
                    'kind': 'page',
                    'title': read_md_title_toml(item),
                    'link': slugify_link(item.relative_to(base_path))
                })
        
        # 如果没有子内容，返回None（过滤空section）
        if not node['children']:
            return None
            
        return node

if __name__ == "__main__":
    # 直接使用process_directory处理目录
    target_node = process_directory(TARGET_DIR, CONTENT_DIR)
    
    try:
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(target_node, f, allow_unicode=True, sort_keys=False, indent=2)

        print(f"Tree YAML generated at: {OUTPUT_FILE}")
    except Exception as e:
        print(f"发生错误: {e}")
