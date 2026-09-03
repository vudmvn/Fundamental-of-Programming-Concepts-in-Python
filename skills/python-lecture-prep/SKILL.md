---
name: python-lecture-prep
description: Quy trình và công cụ hỗ trợ chuẩn bị bài giảng, tài liệu thực hành, Jupyter Notebooks, Slide LaTeX Beamer / PDF, dữ liệu mẫu, hình ảnh minh họa (căn giữa ảnh, tự động đổi tên ảnh trùng không ghi đè, kiểm tra đường dẫn ảnh .tex, dọn dẹp file tạm .aux/.log sau khi biên dịch PDF, cập nhật link PDF vào README.md/README-en.md dạng target=_blank) và tự động xuất bản (publish) lên GitHub cho môn Lập trình Python. Kích hoạt khi người dùng yêu cầu soạn bài giảng, tạo notebook, thiết kế slide TeX/PDF, quản lý hình ảnh hoặc đẩy bài giảng mới lên GitHub.
---

# Skill: Hỗ trợ Soạn Bài giảng, Quản lý Slide TeX/PDF, Hình ảnh & Xuất bản GitHub - Lập trình Python

Skill này được thiết kế riêng cho học phần **Lập trình Python** (Giảng viên: TS. Vũ Đức Minh, ĐH Kinh tế Quốc dân).

---

## 🏛️ 1. Cấu trúc Tài liệu Bài giảng Chuẩn

Mỗi bài giảng theo từng phần/tuần (hoặc chủ đề) trong repository sẽ tuân theo cấu trúc thư mục tiêu chuẩn sau:

```text
lectures/
└── partXX-<ten-chu-de>/
    ├── README.md                  # Tóm tắt lý thuyết, mục tiêu bài học & chỉ dẫn (dùng link images/ + căn giữa ảnh)
    ├── ten_bai_doc.md             # Tệp bài đọc chi tiết (.md tiếng Việt)
    ├── ten_bai_doc-en.md          # Tệp bài đọc chi tiết (.md tiếng Anh)
    ├── partXX_lecture_1.tex       # Tệp nguồn Slide LaTeX Beamer (hỗ trợ phông chữ Việt DejaVu)
    ├── partXX_lecture_1.pdf       # Tệp Slide PDF đã biên dịch hoàn chỉnh
    ├── slides.md                  # Slide Marp định dạng Markdown (nếu áp dụng)
    ├── data/                      # Dữ liệu mẫu phục vụ bài giảng (nếu có)
    │   └── dataset.csv
    └── images/                    # THƯ MỤC CHỨA HÌNH ẢNH MINH HỌA CỦA BÀI GIẢNG
        ├── architecture.png
        └── diagram_example.png
```

> ⚠️ **Quy tắc Nghiêm ngặt về Notebook (`.ipynb`):**  
> **TUYỆT ĐỐI KHÔNG TỰ ĐỘNG TẠO CÁC FILE NOTEBOOK RỖNG/TEMPLATE DUMMY (`lecture.ipynb`, `lab_exercise.ipynb`, `lab_solution.ipynb`).** Chỉ khởi tạo tệp Notebook khi có nội dung mã nguồn thực tế và được yêu cầu cụ thể.

---

## 🖼️ 2. Quy chuẩn Quản lý Hình ảnh, Slide TeX/PDF & Tự động Cập nhật README

Khi tạo, nhúng hoặc biên dịch tài liệu, Agent **BẮT BUỘC** thực hiện theo các nguyên tắc sau:

### 1. Vị trí lưu trữ hình ảnh
- Tất cả các tệp hình ảnh (sơ đồ, minh họa, ảnh chụp màn hình, biểu đồ, ảnh sinh tự động từ `generate_image`, v.v.) dành cho bài học nào **phải được đặt vào thư mục `images/`** của bài học đó (`lectures/partXX-<slug>/images/`).
- Tuyệt đối **không** đặt ảnh ở thư mục gốc, thư mục tạm, hay lưu URL bên ngoài không ổn định.

### 2. Định dạng & Đặt tên tệp hình ảnh
- Đặt tên tệp ảnh bằng chữ cái thường, không dấu, nối bằng dấu gạch ngang `-` (VD: `python-flowchart.png`, `oop-inheritance-diagram.png`).

### 3. Quy tắc Không Ghi đè & Tự động Đổi tên Ảnh Trùng (No-Overwrite & Auto-Rename Rule)
- **TUYỆT ĐỐI KHÔNG XÓA HOẶC GHI ĐÈ** lên các tệp hình ảnh đã tồn tại trong thư mục `images/`.
- Khi chèn hoặc sinh một hình ảnh mới, Agent phải kiểm tra xem tên tệp đã tồn tại trong thư mục `images/` hay chưa.
- **Tự động đổi tên ảnh trùng (Auto-rename on collision):** Nếu tên tệp dự định lưu đã tồn tại (ví dụ `flow-diagram.png`), Agent sẽ tự động bổ sung số thứ tự tăng dần thành `flow-diagram-1.png`, `flow-diagram-2.png`, ... hoặc gán nhãn mô tả phân biệt.

### 4. Quy chuẩn Căn giữa Hình ảnh (Image Centering Mandatory Rule)
- **TẤT CẢ HÌNH ẢNH** xuất hiện trong các tệp Markdown (`README.md`, `slides.md`, các bài đọc `.md`) và cell Markdown của Jupyter Notebook (`.ipynb`) **PHẢI ĐƯỢC CĂN GIỮA (CENTERED)** để tạo giao diện bài giảng chuyên nghiệp.
- Cú pháp HTML Căn giữa Chuẩn:
  ```html
  <p align="center">
    <img src="images/ten-anh.png" alt="Mô tả hình ảnh" width="800" />
  </p>
  ```

### 5. Quy chuẩn Biên dịch Slide LaTeX Beamer (.tex ➔ .pdf) & Kiểm tra Đường dẫn Ảnh
- **Kiểm tra đường dẫn ảnh trong tệp `.tex`:** Mọi hình ảnh chèn vào Slide LaTeX Beamer phải được kiểm tra tồn tại thực tế tại thư mục `images/`. Macro `\imageplaceholder{#1}{#2}` phải được cấu hình tự động hiển thị hình ảnh thật qua `\IfFileExists{#1}{\includegraphics[...]{#1}}{...}`.
- **Lệnh biên dịch chuẩn:** Sử dụng `xelatex -interaction=nonstopmode <filename>.tex` (chạy 2 lượt biên dịch để cập nhật đầy đủ chỉ mục, bookmark và số trang).
- **Quy tắc Dọn dẹp Tệp Tạm (Temp Build Files Cleanup):** Ngay sau khi biên dịch hoàn tất tệp `.pdf`, Agent **BẮT BUỘC** phải xóa tất cả các tệp phụ trợ sinh ra trong quá trình biên dịch (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc`, `.vrb`, `.fls`, `.fdb_latexmk`, `.synctex.gz`) để giữ cho repository luôn sạch sẽ.

### 6. Quy tắc Cập nhật Liên kết Slide PDF vào `README.md` & `README-en.md` (Anti-404 Docsify Link)
- Ngay sau khi tệp PDF slide được tạo hoặc biên dịch lại, Agent **BẮT BUỘC** phải cập nhật liên kết tệp PDF vào cột Slide/Slides thuộc bảng Ma trận học phần ở cả 2 tệp **`README.md`** và **`README-en.md`**.
- **Cú pháp thẻ mở PDF bắt buộc:** Do trang web Docsify là ứng dụng Single Page (SPA), liên kết tệp PDF **bắt buộc** phải dùng cú pháp thẻ HTML có `target="_blank"` để mở trực tiếp tệp PDF trên tab mới của trình duyệt, tránh bị Docsify SPA Router chặn trả về lỗi 404 Not Found:
  ```html
  <a href="lectures/partXX-<slug>/<filename>.pdf" target="_blank">PDF</a>
  ```

### 7. Quy tắc Tự động Cập nhật Ngày chỉnh sửa (Auto Last-Updated Date Rule)
- **BẮT BUỘC:** Mỗi tệp bài giảng Markdown (`.md`) phải có dòng thông tin ngày cập nhật ngay dưới tiêu đề bài học (dòng `#`):
  - Tệp tiếng Việt: `**Cập nhật lần cuối:** <ngày> tháng <tháng> năm <năm>` (VD: `**Cập nhật lần cuối:** 3 tháng 9 năm 2026`)
  - Tệp tiếng Anh: `**Last updated:** <Month> <Day>, <Year>` (VD: `**Last updated:** September 3, 2026`)
- Khi tạo mới bài giảng hoặc bất kỳ khi nào chỉnh sửa, cập nhật nội dung của tệp bài giảng `.md`, Agent **BẮT BUỘC** phải tự động cập nhật dòng này về **ngày hiện tại**.

### 8. Quy tắc Phân định Ngôn ngữ Nghiêm ngặt cho `README-en.md` (Strict No-Vietnamese in `README-en.md` Rule)
- **TUYỆT ĐỐI KHÔNG ĐƯA NỘI DUNG TIẾNG VIỆT VÀO `README-en.md`**: Tệp `README-en.md` là giao diện Tiếng Anh 100%. Không bao giờ chèn các bài đọc Tiếng Việt (`-vn.md`), tiêu đề Tiếng Việt hoặc mô tả Tiếng Việt vào tệp `README-en.md`.
- Nếu bài đọc/bài giảng chưa có bản dịch Tiếng Anh (`-en.md`), tại ô Bài đọc trong `README-en.md` **bắt buộc hiển thị dấu gạch ngang `-`** (không tự động lấy link bài đọc Tiếng Việt làm fallback).
- **Quy tắc Chiều ngược lại (Reverse Rule)**: Trong tệp Tiếng Việt `README.md`, có thể dẫn liên kết tham chiếu tài liệu Tiếng Anh nếu cần thiết hoặc thích hợp, nhưng chiều ngược lại (đưa nội dung Tiếng Việt sang `README-en.md`) là **HOÀN TOÀN BỊ CẤM**.

---

## 🔄 3. Quy trình Soạn & Cập nhật Bài giảng (5 Bước)

1. **Bước 1: Xác định Yêu cầu & Chuẩn đầu ra (CLOs)** theo `syllabus-vn.md` / `syllabus-en.md`.
2. **Bước 2: Tạo Nội dung Bài đọc, Slide TeX & Hình ảnh** (`README.md`, `.md`, `.tex` & `images/`).
3. **Bước 3: Biên dịch PDF & Xóa Tệp Tạm** (`xelatex` 2 pass + cleanup).
4. **Bước 4: Cập nhật Liên kết Slide PDF vào `README.md` & `README-en.md`** (`target="_blank"`).
5. **Bước 5: Kiểm tra & Đồng bộ lên GitHub (`git add`, `git commit`, `git push`)**.
