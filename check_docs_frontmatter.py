import os
import re

WEBSITE_DIR = os.path.dirname(os.path.abspath(__file__))  # path/website
CHECK_DIR = os.path.join(WEBSITE_DIR, "content", "docs")  # path/website/content/docs

DATE_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}$')  # YYYY-MM-DD

# -------------------------
# Functions
# -------------------------
def check_md_files(root_dir):
    errors = []
    stats = {
        "total": 0,
        "index_total": 0,
        "index_ok": 0,
        "index_err": 0,
        "other_total": 0,
        "other_ok": 0,
        "other_err": 0,
    }

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                stats["total"] += 1
                file_path = os.path.join(dirpath, filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        first_line = f.readline().strip()
                        second_line = f.readline().strip()
                        third_line = f.readline().strip()
                except Exception as e:
                    errors.append(f"[ERROR] Cannot read {file_path} ({e})")
                    continue

                if filename == "_index.md":
                    stats["index_total"] += 1
                    if first_line == "+++":
                        if second_line.startswith("title = "):
                            stats["index_ok"] += 1
                        else:
                            stats["index_err"] += 1
                            errors.append(f"[ERROR] {file_path} second line should start with 'title = '")
                    else:
                        stats["index_err"] += 1
                        errors.append(f"[ERROR] {file_path} first line should be '+++'")
                else:
                    stats["other_total"] += 1
                    if first_line == "+++":
                        if second_line.startswith("lastmod = "):
                            value = second_line.split("=", 1)[1].strip().strip('"').strip("'")
                            if DATE_PATTERN.match(value):
                                if third_line.startswith("title = "):
                                    stats["other_ok"] += 1
                                else:
                                    stats["other_err"] += 1
                                    errors.append(f"[ERROR] {file_path} third line should start with 'title = '")
                            else:
                                stats["other_err"] += 1
                                errors.append(f"[ERROR] {file_path} lastmod is invalid: '{value}' (should be YYYY-MM-DD)")
                        else:
                            stats["other_err"] += 1
                            errors.append(f"[ERROR] {file_path} second line should start with 'lastmod = '")
                    else:
                        stats["other_err"] += 1
                        errors.append(f"[ERROR] {file_path} first line should be '+++'")

    return errors, stats

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    print(f"Checking md files in: {CHECK_DIR}")
    issues, stats = check_md_files(CHECK_DIR)

    if issues:
        print("Problems found:")
        for issue in issues:
            print(issue)
    else:
        print("All md files are correctly formatted [OK]")

    print("\n--- Summary ---")
    print(f"Total md files: {stats['total']}")
    print(f"  _index.md: {stats['index_total']} ([OK] {stats['index_ok']}, [FAIL] {stats['index_err']})")
    print(f"  other md:  {stats['other_total']} ([OK] {stats['other_ok']}, [FAIL] {stats['other_err']})")
