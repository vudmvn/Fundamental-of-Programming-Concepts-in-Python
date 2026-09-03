import os
import re
from datetime import datetime

def update_lecture_dates():
    lectures_dir = "lectures"
    now = datetime.now()
    vn_date_str = f"**Cập nhật lần cuối:** {now.day} tháng {now.month} năm {now.year}"
    en_month_str = now.strftime("%B")
    en_date_str = f"**Last updated:** {en_month_str} {now.day}, {now.year}"

    count = 0
    if not os.path.exists(lectures_dir):
        print("Thư mục lectures/ chưa tồn tại.")
        return

    for root, dirs, files in os.walk(lectures_dir):
        for file in files:
            if file.endswith(".md") and file not in ["slides.md"]:
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                if file.endswith("-en.md"):
                    if "**Last updated:**" in content:
                        new_content = re.sub(r"\*\*Last updated:\*\*.*", en_date_str, content)
                    else:
                        new_content = content
                else:
                    if "**Cập nhật lần cuối:**" in content:
                        new_content = re.sub(r"\*\*Cập nhật lần cuối:\*\*.*", vn_date_str, content)
                    else:
                        new_content = content

                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated date in: {filepath}")
                    count += 1

    print(f"Finished updating {count} lecture files.")

if __name__ == "__main__":
    update_lecture_dates()
