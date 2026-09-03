#!/usr/bin/env python3
"""
Script tự động quét các bài giảng trong `lectures/`, đối chiếu với đề cương `syllabus-vn.md`,
tạo/cập nhật Cổng thông tin môn học Song ngữ (Tiếng Việt `README.md` và Tiếng Anh `README-en.md`),
và thực hiện commit + push lên GitHub.
"""

import os
import sys
import re
import argparse
import subprocess

# 15 Tuần chuẩn theo đề cương chính thức DSAI1003
SYLLABUS_WEEKS = [
    {
        "week": "01",
        "topic_vn": "Bài 1: Giới thiệu chung & Thiết kế giải thuật",
        "topic_en": "Lecture 1: Introduction & Algorithm Design",
        "desc_vn": "Chương trình máy tính, giải phẫu máy tính, ngôn ngữ Python, lỗi biên dịch/runtime, thiết kế giải thuật và mã giả.",
        "desc_en": "Computer programs, anatomy of a computer, Python language, compile/runtime errors, algorithm design and pseudocode."
    },
    {
        "week": "02",
        "topic_vn": "Bài 2: Quy trình phát triển phần mềm & Kiểu dữ liệu",
        "topic_en": "Lecture 2: Software Development & Data Types",
        "desc_vn": "Quy trình phát triển phần mềm, kiểu dữ liệu số/ký tự/chuỗi, biểu thức, câu lệnh gán, biến số, hàm và module.",
        "desc_en": "Software development process, numeric/character/string data types, expressions, assignments, variables, functions and modules."
    },
    {
        "week": "03",
        "topic_vn": "Bài 3: Cấu trúc ra quyết định (Decision Making)",
        "topic_en": "Lecture 3: Decision Making",
        "desc_vn": "Câu lệnh if, toán tử so sánh quan hệ, rẽ nhánh lồng nhau, cấu trúc if-elif-else, biến logic và toán tử Boolean.",
        "desc_en": "The if statement, relational operations, nested branches, multiple alternatives (if-elif-else), Boolean variables and operators."
    },
    {
        "week": "04",
        "topic_vn": "Bài 4: Cấu trúc vòng lặp (Loops)",
        "topic_en": "Lecture 4: Loops",
        "desc_vn": "Vòng lặp while, vòng lặp for, vòng lặp lồng nhau, kỹ thuật xử lý chuỗi ký tự bằng vòng lặp.",
        "desc_en": "While loops, for loops, nested loops, string processing patterns using loops."
    },
    {
        "week": "05",
        "topic_vn": "Bài 5: Thiết kế hàm & Phạm vi biến",
        "topic_en": "Lecture 5: Functions & Variable Scope",
        "desc_vn": "Khai báo hàm (def), kiểm thử hàm, truyền tham số và giá trị trả về, biến cục bộ/toàn cục, nhập môn hàm đệ quy.",
        "desc_en": "Function declaration (def), testing functions, parameter passing and return values, variable scope, introduction to recursion."
    },
    {
        "week": "06",
        "topic_vn": "Bài 6: Cấu trúc List và Tuple",
        "topic_en": "Lecture 6: Lists and Tuples",
        "desc_vn": "Đặc tính của List, thao tác và phương thức trên List, sử dụng List với hàm, biểu diễn ma trận và bảng dữ liệu 2 chiều.",
        "desc_en": "Basic properties of lists, list operations and methods, using lists with functions, creating matrices and 2D tables."
    },
    {
        "week": "07",
        "topic_vn": "Thi giữa kỳ (Midterm Exam)",
        "topic_en": "Midterm Examination",
        "desc_vn": "Ôn tập tổng hợp kiến thức từ Bài 1 đến Bài 6 và thực hiện bài kiểm tra giữa kỳ.",
        "desc_en": "Review of core concepts from Lectures 1 to 6 and administration of midterm examination."
    },
    {
        "week": "08",
        "topic_vn": "Bài 7: Thao tác Tệp và Xử lý Ngoại lệ (Phần 1)",
        "topic_en": "Lecture 7: Files and Exceptions (Part 1)",
        "desc_vn": "Thao tác tệp văn bản (đọc, ghi, ghi nối tiếp), thao tác tệp nhị phân và xử lý tham số dòng lệnh sys.argv.",
        "desc_en": "Text file operations (read, write, append), binary file operations, and command line arguments (sys.argv)."
    },
    {
        "week": "09",
        "topic_vn": "Bài 7: Thao tác Tệp và Xử lý Ngoại lệ (Phần 2)",
        "topic_en": "Lecture 7: Files and Exceptions (Part 2)",
        "desc_vn": "Cơ chế bắt lỗi và xử lý ngoại lệ (try-except-finally), định nghĩa custom exceptions và an toàn thao tác dữ liệu.",
        "desc_en": "Exception handling schemes (try-except-finally), custom exceptions, and exception safety in data handling."
    },
    {
        "week": "10",
        "topic_vn": "Bài 8: Tập hợp (Set) và Từ điển (Dictionary)",
        "topic_en": "Lecture 8: Sets and Dictionaries",
        "desc_vn": "Cấu trúc Set và phép toán tập hợp, cấu trúc Dictionary tra cứu key-value, cấu trúc dữ liệu lồng nhau phức hợp.",
        "desc_en": "Set data structure and set operations, Dictionary structure and key-value lookups, complex and nested structures."
    },
    {
        "week": "11",
        "topic_vn": "Bài 9: Đối tượng và Lớp (OOP - Phần 1)",
        "topic_en": "Lecture 9: Objects and Classes (OOP - Part 1)",
        "desc_vn": "Hệ tư tưởng OOP, cài đặt lớp đơn giản, xác định giao diện công khai, thiết kế biểu diễn dữ liệu và đóng gói.",
        "desc_en": "OOP paradigm, implementing simple classes, public interface specification, data representation design and encapsulation."
    },
    {
        "week": "12",
        "topic_vn": "Bài 9: Đối tượng và Lớp (OOP - Phần 2)",
        "topic_en": "Lecture 9: Objects and Classes (OOP - Part 2)",
        "desc_vn": "Hàm khởi tạo (__init__), cài đặt các phương thức đối tượng, kiểm thử và gỡ lỗi lớp đối tượng.",
        "desc_en": "Constructors (__init__), implementing instance methods, unit testing and debugging class implementations."
    },
    {
        "week": "13",
        "topic_vn": "Bài 10: Kế thừa và Đa hình (Phần 1)",
        "topic_en": "Lecture 10: Inheritance and Polymorphism (Part 1)",
        "desc_vn": "Cây phân cấp kế thừa, cài đặt các lớp con (subclasses), tái sử dụng mã nguồn và gọi constructor super().",
        "desc_en": "Inheritance hierarchies, implementing subclasses, code reuse, and calling superclass constructor super()."
    },
    {
        "week": "14",
        "topic_vn": "Bài 10: Kế thừa và Đa hình (Phần 2)",
        "topic_en": "Lecture 10: Inheritance and Polymorphism (Part 2)",
        "desc_vn": "Ghi đè phương thức (method overriding), tính đa hình (polymorphism), dynamic method dispatch và bài toán thực tế.",
        "desc_en": "Method overriding, polymorphism, dynamic method dispatch, and practical domain problem solving."
    },
    {
        "week": "15",
        "topic_vn": "Tổng kết và Ôn tập cuối kỳ",
        "topic_en": "Course Summary & Final Review",
        "desc_vn": "Hệ thống hóa toàn bộ kiến thức học phần DSAI1003, giải đáp thắc mắc và chuẩn bị thi kết thúc học phần.",
        "desc_en": "Systematizing full course knowledge (DSAI1003), Q&A session, and comprehensive final examination preparation."
    }
]

def is_valid_content_file(file_path, min_bytes=300):
    if not os.path.exists(file_path):
        return False
    return os.path.getsize(file_path) >= min_bytes

def scan_lectures_dir(lectures_dir):
    lecture_map = {}
    if not os.path.exists(lectures_dir):
        return lecture_map

    for folder in os.listdir(lectures_dir):
        folder_path = os.path.join(lectures_dir, folder)
        if os.path.isdir(folder_path):
            part_key = None
            if folder.startswith("part"):
                num_match = re.search(r'part(\d+)', folder)
                if num_match:
                    part_key = f"{int(num_match.group(1)):02d}"
            elif folder.startswith("week-"):
                num_match = re.search(r'week-(\d+)', folder)
                if num_match:
                    part_key = f"{int(num_match.group(1)):02d}"

            if not part_key:
                continue

            files = os.listdir(folder_path)

            notebook_links_vn = []
            notebook_links_en = []
            lab_links_vn = []
            lab_links_en = []
            solution_links_vn = []
            solution_links_en = []

            for f in sorted(files):
                if f.endswith(".ipynb"):
                    full_p = os.path.join(folder_path, f)
                    if is_valid_content_file(full_p, 1000):
                        clean_name = f.replace(".ipynb", "")
                        link_html = f'<a href="lectures/{folder}/{f}" target="_blank">{clean_name}</a>'
                        is_vn_file = f.endswith("-vn.ipynb") or "_vn" in f
                        is_en_file = f.endswith("-en.ipynb") or "_en" in f

                        if "solution" in f or "dap_an" in f:
                            if not is_en_file: solution_links_vn.append(f'🔑 {link_html}')
                            if not is_vn_file: solution_links_en.append(f'🔑 {link_html}')
                        elif "practice" in f or "exercise" in f or "lab" in f:
                            if not is_en_file: lab_links_vn.append(f'💻 {link_html}')
                            if not is_vn_file: lab_links_en.append(f'💻 {link_html}')
                        else:
                            if not is_en_file: notebook_links_vn.append(f'📘 {link_html}')
                            if not is_vn_file: notebook_links_en.append(f'📘 {link_html}')

            # Slide PDFs
            slide_links_vn = []
            slide_links_en = []
            for f in sorted(files):
                if f.endswith(".pdf"):
                    link_html = f'<a href="lectures/{folder}/{f}" target="_blank">PDF ({f.replace(".pdf", "")})</a>'
                    is_vn_file = f.endswith("-vn.pdf") or "_vn" in f
                    is_en_file = f.endswith("-en.pdf") or "_en" in f
                    if not is_en_file: slide_links_vn.append(link_html)
                    if not is_vn_file: slide_links_en.append(link_html)

            extra_mds_vn = []
            extra_mds_en = []

            md_files = [f for f in files if f.endswith(".md") and f not in ["README.md", "README-en.md", "slides.md", "slides-en.md"]]

            for f in sorted(md_files):
                file_full_path = os.path.join(folder_path, f)
                doc_title = f.replace(".md", "").replace("_", " ").replace("-", " ").title()
                try:
                    with open(file_full_path, "r", encoding="utf-8") as mdf:
                        for line in mdf:
                            line_str = line.strip()
                            if line_str.startswith("# "):
                                doc_title = line_str.replace("# ", "").strip()
                                break
                except Exception:
                    pass

                clean_name = f.replace(".md", "")
                is_en_file = f.endswith("-en.md") or "_en." in f
                is_vn_file = not is_en_file

                if any(k in f for k in ["practice", "exercise", "lab"]):
                    link_html = f'💻 <a href="lectures/{folder}/{f}" target="_blank">{clean_name}</a>'
                    if is_vn_file: lab_links_vn.append(link_html)
                    if is_en_file: lab_links_en.append(link_html)
                else:
                    link_str = f"• [{doc_title}](lectures/{folder}/{f})"
                    if is_vn_file: extra_mds_vn.append(link_str)
                    if is_en_file: extra_mds_en.append(link_str)

            lecture_map[part_key] = {
                "folder": folder,
                "notebook_vn": "<br>".join(notebook_links_vn) if notebook_links_vn else "-",
                "notebook_en": "<br>".join(notebook_links_en) if notebook_links_en else "-",
                "slides_vn": "<br>".join(slide_links_vn) if slide_links_vn else "-",
                "slides_en": "<br>".join(slide_links_en) if slide_links_en else "-",
                "lab_vn": "<br>".join(lab_links_vn) if lab_links_vn else "-",
                "lab_en": "<br>".join(lab_links_en) if lab_links_en else "-",
                "solution_vn": "<br>".join(solution_links_vn) if solution_links_vn else "-",
                "solution_en": "<br>".join(solution_links_en) if solution_links_en else "-",
                "extra_docs_vn": "<br>".join(extra_mds_vn) if extra_mds_vn else "",
                "extra_docs_en": "<br>".join(extra_mds_en) if extra_mds_en else ""
            }
    return lecture_map

def generate_matrices():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lectures_dir = os.path.join(root_dir, "lectures")
    lecture_map = scan_lectures_dir(lectures_dir)

    # 1. Bảng tiếng Việt cho README.md
    vn_rows = []
    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic = item["topic_vn"]
        data = lecture_map.get(w)
        if data:
            docs = []
            if data["notebook_vn"] != "-": docs.append(data["notebook_vn"])
            if data["extra_docs_vn"]: docs.append(data["extra_docs_vn"])
            docs_cell = "<br>".join(docs) if docs else "-"
            slide_cell = data["slides_vn"]
            lab_cell = data["lab_vn"]
            sol_cell = data["solution_vn"]
            status = "✅ *Đã sẵn sàng*"
        else:
            docs_cell = "-"
            slide_cell = "-"
            lab_cell = "-"
            sol_cell = "-"
            status = "⏳ *Đang biên soạn*"

        vn_rows.append(f"| **Tuần {w}** | **{topic}** | {docs_cell} | {slide_cell} | {lab_cell} | {sol_cell} | {status} |")

    # 2. Bảng tiếng Anh cho README-en.md
    en_rows = []
    for item in SYLLABUS_WEEKS:
        w = item["week"]
        topic = item["topic_en"]
        data = lecture_map.get(w)
        if data:
            docs = []
            if data["notebook_en"] != "-": docs.append(data["notebook_en"])
            if data["extra_docs_en"]: docs.append(data["extra_docs_en"])
            docs_cell = "<br>".join(docs) if docs else "-"
            slide_cell = data["slides_en"]
            lab_cell = data["lab_en"]
            sol_cell = data["solution_en"]
            status = "✅ *Ready*"
        else:
            docs_cell = "-"
            slide_cell = "-"
            lab_cell = "-"
            sol_cell = "-"
            status = "⏳ *In Preparation*"

        en_rows.append(f"| **Week {w}** | **{topic}** | {docs_cell} | {slide_cell} | {lab_cell} | {sol_cell} | {status} |")

    return "\n".join(vn_rows), "\n".join(en_rows), lecture_map

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Quản lý và xuất bản bài giảng Lập trình Python.")
    parser.add_argument("-m", "--message", help="Commit message cho Git và thực hiện git push")
    parser.add_argument("--skip-git", action="store_true", help="Chỉ cập nhật ma trận README, không commit/push git")
    args = parser.parse_args()

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    vn_table, en_table, lecture_map = generate_matrices()
    print(f"🔍 Đã quét thấy {len(lecture_map)} thư mục bài giảng trong lectures/")

    if args.message and not args.skip_git:
        try:
            print("🚀 Đang đồng bộ lên GitHub...")
            subprocess.run(["git", "add", "."], cwd=root_dir, check=True)
            subprocess.run(["git", "commit", "-m", args.message], cwd=root_dir, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=root_dir, check=False)
            print("✅ Đã xuất bản thành công!")
        except Exception as e:
            print(f"⚠️ Lỗi trong quá trình git commit/push: {e}")

if __name__ == "__main__":
    main()
