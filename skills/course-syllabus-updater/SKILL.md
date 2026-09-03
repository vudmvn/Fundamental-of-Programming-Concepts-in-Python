---
name: course-syllabus-updater
description: Skill chuyên tự động tổng hợp, cập nhật và đồng bộ file README.md (Tiếng Việt có dấu chuẩn) và README-en.md (Phiên bản Tiếng Anh song ngữ) cho môn Lập trình Python. Tự động tạo bảng ma trận liên kết động tới các bài giảng, slide, lab, đáp án, tệp dữ liệu và hình ảnh (hiển thị dấu gạch ngang '-' đối với các mục chưa có hoặc chưa được biên soạn thực tế). Kích hoạt khi người dùng yêu cầu cập nhật trang chủ, cập nhật syllabus, đồng bộ bảng bài giảng hoặc tạo/cập nhật phiên bản song ngữ.
---

# Skill: Cập nhật File Markdown Giới thiệu Môn học & Cổng thông tin Song ngữ (Bilingual Course Portal Updater)

Skill này hỗ trợ tự động duy trì và cập nhật tệp **`README.md`** (Trang chủ Tiếng Việt có dấu chuẩn) và **`README-en.md`** (Phiên bản Tiếng Anh Song ngữ) cho môn **Lập trình Python** - Giảng viên: TS. Vũ Đức Minh (ĐH Kinh tế Quốc dân).

---

## 🎯 1. Nhiệm vụ chính của Skill

1. **Hiển thị Tiêu đề Tiếng Việt có dấu chuẩn**: Đảm bảo tất cả tiêu đề bài học, tên chủ đề tuần học, danh mục tài liệu đều viết bằng Tiếng Việt chuẩn có đầy đủ dấu thanh, ngữ pháp chính xác.
2. **Hỗ trợ Phiên bản Song ngữ (Bilingual Support)**: Tự động khởi tạo và cập nhật song song 2 phiên bản trang chủ:
   - **`README.md`**: Trang chủ Tiếng Việt (có nút chuyển ngữ 🌐 sang English).
   - **`README-en.md`**: Trang chủ Tiếng Anh (có nút chuyển ngữ 🌐 về Tiếng Việt).
3. **Quy tắc Hiển thị Dấu Gạch Ngang `-` cho Mục chưa Biên soạn**:
   - Đối với các tài nguyên **chưa được tạo** hoặc **mới chỉ có tệp template khung rỗng** (chưa có nội dung thực tế như `slides.md`, `lab_exercise.ipynb`, `lab_solution.ipynb`, `data/` rỗng), bảng ma trận bắt buộc hiển thị **dấu gạch ngang `-`**.
   - Chỉ hiển thị đường liên kết icon (VD: `[📊 Slides]`, `[💻 Lab]`, `[🔑 Đáp án]`) khi tệp đã chứa nội dung bài giảng/thực hành đầy đủ và hoàn chỉnh.
4. **Xây dựng Bảng Ma trận Liên kết Động (Dynamic Course Matrix)**: Quét tự động thư mục `lectures/` và xây dựng bảng liên kết trực tiếp cho toàn bộ các bài học trong học phần.

---

## 📑 2. Quy chuẩn Ngôn ngữ & Tiêu đề trong Trang chủ

### 1. Quy chuẩn Tiếng Việt có dấu (`README.md`)
- Tất cả tiêu đề tuần học, tài liệu đọc và phần mô tả phải chuẩn hóa Tiếng Việt có dấu (VD: `"Tuần 01: Cài đặt môi trường & Cú pháp cơ bản"`, `"Cấu trúc điều khiển và Vòng lặp"`).
- Không viết tắt hoặc bỏ dấu trong các bảng ma trận.

### 2. Quy chuẩn Dấu Gạch Ngang (`-`)
- Cột nào của tuần học chưa có tài nguyên hoàn chỉnh (Ví dụ: chưa soạn Slide, chưa có file Lab, đáp án, hoặc thư mục `data/` đang rỗng) thì đặt giá trị `-`.

### 3. Quy chuẩn Song ngữ & Quy tắc Nghiêm ngặt cho `README-en.md` (Strict No-Vietnamese in `README-en.md` Rule)
- Cung cấp tiêu đề và mô tả chuẩn bằng Tiếng Anh (VD: `"Week 01: Python Setup & Basic Syntax"`, `"Control Flow & Loops"`).
- Đặt nút chuyển đổi ngôn ngữ nổi bật ở đầu trang: `🌐 Language: [🇻🇳 Vietnamese Version (README.md)](README.md) | 🇬🇧 English`.
- **TUYỆT ĐỐI KHÔNG ĐƯA NỘI DUNG TIẾNG VIỆT VÀO `README-en.md`**:
  - Tệp `README-en.md` là giao diện Tiếng Anh 100%. **Không bao giờ** chèn các bài đọc Tiếng Việt (`-vn.md`), tiêu đề Tiếng Việt hoặc mô tả Tiếng Việt vào tệp `README-en.md`.
  - Nếu bài đọc/bài giảng chưa có bản dịch Tiếng Anh (`-en.md`), tại ô Bài đọc trong `README-en.md` **bắt buộc hiển thị dấu gạch ngang `-`** (không tự động lấy link bài đọc Tiếng Việt làm fallback).
  - **Quy tắc Chiều ngược lại (Reverse Rule)**: Trong tệp Tiếng Việt `README.md`, có thể dẫn liên kết tham chiếu tài liệu Tiếng Anh nếu cần thiết hoặc thích hợp, nhưng chiều ngược lại (đưa nội dung Tiếng Việt sang `README-en.md`) là **HOÀN TOÀN BỊ CẤM**.

---

## ⚡ 3. Quy trình Cập nhật & Tự động hóa

Khi người dùng ra lệnh:
> *"Cập nhật file README/Syllabus môn học"*  
> hoặc  
> *"Đồng bộ lại danh sách bài giảng Tiếng Việt có dấu và tạo phiên bản song ngữ"*

Agent sẽ thực hiện:
1. Đọc nội dung từ `syllabus-vn.md` và thông tin các file bài đọc trong `lectures/`.
2. Kiểm tra tính thực tế của các tệp `slides.md`, `lab_exercise.ipynb`, `lab_solution.ipynb` (gán `-` nếu chưa hoàn thiện).
3. Thực thi script `python scripts/publish_lecture.py` để sinh đồng thời cả 2 tệp `README.md` (Tiếng Việt) và `README-en.md` (Tiếng Anh).
4. Đẩy bản cập nhật mới nhất lên GitHub bằng lệnh:
   ```bash
   python scripts/publish_lecture.py -m "docs(readme): Cập nhật cổng thông tin môn học với quy định dấu gạch ngang '-' cho mục chưa có"
   ```
