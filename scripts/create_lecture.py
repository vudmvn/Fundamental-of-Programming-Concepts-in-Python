#!/usr/bin/env python3
"""
Script tự động khởi tạo cấu trúc bài giảng theo tuần/phần cho môn Lập trình Python.
Cách dùng:
    python scripts/create_lecture.py --week 1 --title "Cài đặt môi trường và Cú pháp cơ bản"
"""

import os
import sys
import argparse
import re

def slugify(text):
    text = text.lower().strip()
    vietnamese_map = {
        'à':'a', 'á':'a', 'ả':'a', 'ã':'a', 'ạ':'a', 'ă':'a', 'ằ':'a', 'ắ':'a', 'ẳ':'a', 'ẵ':'a', 'ặ':'a',
        'â':'a', 'ầ':'a', 'ấ':'a', 'ẩ':'a', 'ẫ':'a', 'ậ':'a', 'đ':'d', 'è':'e', 'é':'e', 'ẻ':'e', 'ẽ':'e', 'ẹ':'e',
        'ê':'e', 'ề':'e', 'ế':'e', 'ể':'e', 'ễ':'e', 'ệ':'e', 'ì':'i', 'í':'i', 'ỉ':'i', 'ĩ':'i', 'ị':'i',
        'ò':'o', 'ó':'o', 'ỏ':'o', 'õ':'o', 'ọ':'o', 'ô':'o', 'ồ':'o', 'ố':'o', 'ổ':'o', 'ỗ':'o', 'ộ':'o',
        'ơ':'o', 'ờ':'o', 'ớ':'o', 'ở':'o', 'ỡ':'o', 'ợ':'o', 'ù':'u', 'ú':'u', 'ủ':'u', 'ũ':'u', 'ụ':'u',
        'ư':'u', 'ừ':'u', 'ứ':'u', 'ử':'u', 'ữ':'u', 'ự':'u', 'ỳ':'y', 'ý':'y', 'ỷ':'y', 'ỹ':'y', 'ỵ':'y'
    }
    for char, replacement in vietnamese_map.items():
        text = text.replace(char, replacement)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def create_lecture(week, title):
    week_num = int(week)
    week_str = f"{week_num:02d}"
    folder_slug = f"part{week_str}-{slugify(title)}"
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lectures", folder_slug))
    data_dir = os.path.join(base_dir, "data")
    images_dir = os.path.join(base_dir, "images")

    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    # 1. Tạo README.md trong thư mục tuần
    readme_content = f"""# Bài học {week_str}: {title}

**Cập nhật lần cuối:** 3 tháng 9 năm 2026

## 🎯 Mục tiêu bài học
- Nắm vững các khái niệm lý thuyết nền tảng về **{title}**.
- Áp dụng cú pháp Python chuẩn PEP8 để giải quyết bài toán thực tế.
- Thực hành xây dựng và chạy chương trình minh họa.

## 📁 Cấu trúc bài học
- `README.md`: Hướng dẫn học tập và tóm tắt kiến thức.
- `slides.md` / Slide PDF: Tài liệu trình chiếu bài giảng.
- `data/`: Bộ dữ liệu thực tế phục vụ bài học (nếu có).
- `images/`: Lưu trữ toàn bộ sơ đồ minh họa, đồ thị và hình vẽ.

## 🚀 Hướng dẫn học tập
1. Theo dõi bài giảng lý thuyết qua Slide và các bài đọc `.md`.
2. Chạy thử các ví dụ mã nguồn và quan sát kết quả thực thi.
3. Hoàn thành các bài tập thực hành được giao.
"""
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 2. Tạo slides.md (Marp Format)
    slides_content = f"""---
marp: true
theme: default
paginate: true
header: 'Lập trình Python | TS. Vũ Đức Minh'
footer: 'Bài học {week_str}: {title}'
---

# Bài học {week_str}: {title}

**Học phần:** Lập trình Python  
**Giảng viên:** TS. Vũ Đức Minh  
**Khoa:** Khoa học dữ liệu & Trí tuệ nhân tạo (NEU)

---

## 📌 Nội dung chính

1. Giới thiệu tổng quan & Đặt vấn đề
2. Các khái niệm & Cú pháp cốt lõi
3. Ví dụ minh họa & Thực thi mã nguồn
4. Tổng kết & Bài tập áp dụng

---

## 1. Giới thiệu tổng quan

- Đặt vấn đề trong lập trình ứng dụng thực tế.
- Vai trò của chủ đề **{title}** trong lập trình Python hiện đại.

---

## 2. Bài tập thực hành

- Sinh viên thực hành viết mã nguồn và nộp bài theo hướng dẫn.
"""
    slides_path = os.path.join(base_dir, "slides.md")
    with open(slides_path, "w", encoding="utf-8") as f:
        f.write(slides_content)

    print(f"✅ Đã khởi tạo thành công bài học: lectures/{folder_slug}")

if __name__ == "__main__":
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="Khởi tạo thư mục bài giảng mới.")
    parser.add_argument("--week", required=True, help="Số thứ tự tuần/bài (vd: 1, 2, 3...)")
    parser.add_argument("--title", required=True, help="Tên chủ đề bài giảng")
    args = parser.parse_args()

    create_lecture(args.week, args.title)
