# Quy trình Soạn bài giảng, Quản lý Hình ảnh & Xuất bản lên GitHub (Lập trình Python)

Tài liệu này hướng dẫn chi tiết quy trình chuẩn bị bài giảng, tạo tài liệu thực hành (Jupyter Notebooks, Slides), sinh/quản lý dữ liệu và hình ảnh minh họa trong thư mục `images/`, đồng thời tự động xuất bản lên GitHub bằng công cụ **Antigravity Skill** và các bộ script hỗ trợ.

---

## 🏗️ 1. Cấu trúc Quản lý Bài giảng trong Repository

Mỗi tuần học sẽ nằm trong một thư mục riêng biệt tại đường dẫn `lectures/partXX-<ten-chu-de>`:

```text
Python/
├── .gemini/skills/                 # AI Agent custom skills
│   ├── python-lecture-prep/
│   └── course-syllabus-updater/
├── skills/                         # Thư mục quản lý skills
├── lectures/
│   ├── part01-tong-quan-va-cai-dat/
│   │   ├── README.md               # Tóm tắt lý thuyết & chỉ dẫn tuần 1
│   │   ├── ten_bai_doc.md          # Bài đọc lý thuyết chi tiết (Tiếng Việt)
│   │   ├── ten_bai_doc-en.md       # Bài đọc lý thuyết chi tiết (Tiếng Anh)
│   │   ├── part01_lecture_1.tex    # Nguồn Slide LaTeX Beamer
│   │   ├── part01_lecture_1.pdf    # Slide PDF đã biên dịch
│   │   ├── slides.md               # Slide Marp định dạng Markdown
│   │   ├── data/                   # Bộ dữ liệu dùng trong tuần (nếu có)
│   │   └── images/                 # THƯ MỤC LƯU HÌNH ẢNH MINH HỌA
│   │       ├── overview.png
│   │       └── diagram.png
│   └── part02-toan-tu-re-nhanh/
├── scripts/
│   ├── create_lecture.py           # Script khởi tạo khung bài giảng mới
│   ├── publish_lecture.py          # Script tự động cập nhật README & push GitHub
│   └── update_lecture_dates.py     # Script đồng bộ ngày cập nhật trong file .md
├── assets/                         # Ảnh bìa sách tham khảo & tài nguyên dùng chung
├── syllabus-vn.md                  # Đề cương chi tiết học phần (Tiếng Việt)
├── syllabus-en.md                  # Đề cương chi tiết học phần (Tiếng Anh)
├── index.md                        # Trang chủ repo + Mục lục bài giảng (Tiếng Việt)
└── index-en.md                     # Trang chủ repo + Mục lục bài giảng (Tiếng Anh 100%)
```

---

## 🖼️ 2. Quy chuẩn Quản lý, Căn giữa & Bảo vệ Hình ảnh

1. **Vị trí lưu trữ**: Tất cả ảnh minh họa, sơ đồ, infographic hoặc biểu đồ được tạo/export cho tuần học nào sẽ nằm trong thư mục `lectures/partXX-<slug>/images/`.
2. **Quy tắc Không Ghi đè & Tự động Đổi tên (No-Overwrite & Auto-Rename Rule)**:
   - **Tuyệt đối không xóa hoặc ghi đè** lên các tệp ảnh đã tồn tại trong thư mục `images/`.
   - Nếu tên tệp ảnh mới định lưu bị trùng tên với tệp ảnh đã có sẵn, Antigravity Skill sẽ tự động thêm số thứ tự phân biệt (ví dụ `image-1.png`, `image-2.png`).
3. **Quy tắc Bắt buộc Căn giữa (Image Centering Rule)**:
   - **TẤT CẢ HÌNH ẢNH** trong các tệp Markdown (`README.md`, `slides.md`, các bài đọc `.md`) và Notebook (`.ipynb`) **PHẢI ĐƯỢC CĂN GIỮA (CENTERED)**:
     ```html
     <p align="center">
       <img src="images/ten-anh.png" alt="Mô tả hình ảnh" width="800" />
     </p>
     ```
4. **Quy tắc Cập nhật Ngày chỉnh sửa (Auto Last-Updated Date Rule)**:
   - Mỗi tệp bài giảng Markdown (`.md`) bắt buộc phải có dòng thông tin ngày cập nhật ngay dưới tiêu đề bài học:
     - Tiếng Việt: `**Cập nhật lần cuối:** <ngày> tháng <tháng> năm <năm>`
     - Tiếng Anh: `**Last updated:** <Month> <Day>, <Year>`
5. **Quy chuẩn Slide TeX/PDF (.tex ➔ .pdf)**:
   - Biên dịch bằng `xelatex -interaction=nonstopmode <filename>.tex` (2 lượt).
   - Ngay sau khi xuất xong tệp PDF, Agent **bắt buộc dọn dẹp xóa các tệp tạm** (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc`, `.vrb`, `.fls`, `.synctex.gz`).
6. **Quy tắc Cập nhật Link Slide PDF vào `index.md` & `index-en.md`**:
   - Bắt buộc dùng thẻ HTML `target="_blank"`: `<a href="lectures/.../partXX_lecture_X.pdf" target="_blank">PDF</a>` để mở trực tiếp tab mới.
7. **Quy tắc Phân định Ngôn ngữ Nghiêm ngặt cho `index-en.md`**:
   - Tệp `index-en.md` là giao diện Tiếng Anh 100%. Không bao giờ chèn các bài đọc hoặc mô tả Tiếng Việt vào `index-en.md`.

---

## ⚡ 3. Quy trình Soạn Bài giảng Chi tiết

### Bước 1: Khởi tạo khung bài giảng mới
Chạy script Python để sinh nhanh bộ file mẫu:
```bash
python scripts/create_lecture.py --week <Số_thứ_tự> --title "<Tên_chủ_đề>"
```

*Ví dụ:*
```bash
python scripts/create_lecture.py --week 1 --title "Cài đặt môi trường và Cú pháp cơ bản"
```

### Bước 2: Nhờ AI Assistant (Antigravity Agent) biên soạn nội dung
Chỉ cần ra lệnh cho AI bằng tiếng Việt:
> *"Soạn bài giảng Tuần 1 về Cài đặt môi trường và Cú pháp cơ bản theo đề cương syllabus-vn.md. Tạo sơ đồ luồng biên dịch Python đặt vào images/ và nhúng vào slides.md."*

Agent sẽ áp dụng skill `python-lecture-prep` để:
1. Đọc chuẩn đầu ra từ `syllabus-vn.md`.
2. Tạo các bài đọc `.md` song ngữ (có gắn ngày cập nhật).
3. Biên soạn slide LaTeX Beamer hoặc Marp `slides.md`.
4. Căn giữa toàn bộ hình ảnh trong `images/`.
5. Tạo mã nguồn thực hành và bộ dữ liệu mẫu trong `data/` nếu cần.

### Bước 3: Xuất bản tự động lên GitHub
Sau khi biên soạn xong, chạy:
```bash
python scripts/publish_lecture.py -m "feat(lecture): Hoàn thành bài giảng Tuần 01"
```

---

## 🌐 4. Thông tin Repository & Giảng viên
- **Giảng viên:** TS. Vũ Đức Minh
- **Khoa:** Khoa học dữ liệu & Trí tuệ nhân tạo (NEU)
- **Học phần:** Lập trình Python (DSAI1003)
- **GitHub Repository:** [https://github.com/vudmvn/Fundamental-of-Programming-Concepts-in-Python](https://github.com/vudmvn/Fundamental-of-Programming-Concepts-in-Python)
- **Website:** [https://vudmvn.github.io/Fundamental-of-Programming-Concepts-in-Python/](https://vudmvn.github.io/Fundamental-of-Programming-Concepts-in-Python/)
