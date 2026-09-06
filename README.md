# 🐍 DSAI1003 – Các nguyên lý lập trình cơ bản với Python

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docsify](https://img.shields.io/badge/Website-Docsify-informational.svg)](https://vudmvn.github.io/Fundamental-of-Programming-Concepts-in-Python/)
[![Institution](https://img.shields.io/badge/NEU-School%20of%20Technology-red.svg)](https://neu.edu.vn/)

🌐 **Ngôn ngữ:** 🇻🇳 **Tiếng Việt** | [🇬🇧 English Version (README-en.md)](README-en.md)

> **Giảng viên:** TS. Vũ Đức Minh  
> **Đơn vị phụ trách:** Khoa Khoa học Dữ liệu & Trí tuệ Nhân tạo, Trường Công nghệ, Trường Đại học Kinh tế Quốc dân (NEU)  
> **Chương trình đào tạo:** Cử nhân Khoa học Dữ liệu trong Tài chính & Thương mại điện tử (DSFE)  
> **Số tín chỉ:** 3 Tín chỉ (45h Lý thuyết + 22.5h Thực hành/Lab, 90h Tự học)  
> **Quyết định ban hành:** 975/QĐ-ĐHKTQD (30/03/2024)  
> **Website bài giảng:** [https://vudmvn.github.io/Fundamental-of-Programming-Concepts-in-Python/](https://vudmvn.github.io/Fundamental-of-Programming-Concepts-in-Python/)  
> **Đề cương chi tiết:** [syllabus-vn.md](syllabus-vn.md) | [syllabus-en.md](syllabus-en.md)

---

## 🚀 1. Chuyên đề Phương pháp Học tập

Học phần cung cấp bộ cẩm nang, tài liệu slide và chuyên đề hướng dẫn phương pháp học tập chuẩn mực:

| Tài liệu / Chuyên đề | Định dạng / Liên kết |
| :--- | :---: |
| 📘 **Cẩm nang Học phần & Phương pháp Tự học** (Handbook A4, 11 trang) | [**Tải PDF**](python_course_guide.pdf) |
| 🖥️ **Slide Giới thiệu & Định hướng Môn học** (Beamer 16:9, 26 slides) | [**Tải Slide PDF**](python_course_guide_slides.pdf) |
| 📖 **Phương pháp Tự học Lập trình Python Hiệu quả** (Tutorial/Lab) | [**Xem tài liệu**](tutorial-effective-python-self-study-vn.md) |
| 🤖 **Chiến lược Sử dụng Trí tuệ Nhân tạo (ChatGPT/AI) Hỗ trợ Học tập** (Tutorial/Lab) | [**Xem tài liệu**](learning-python-with-AI-tool-vn.md) |

---

## 📌 2. Giới thiệu Học phần & Mục tiêu (Course Objectives)

Học phần **Các nguyên lý lập trình cơ bản với Python (DSAI1003)** là học phần bắt buộc thuộc khối kiến thức cơ sở ngành, trang bị cho sinh viên tư duy thuật toán, kỹ thuật tổ chức chương trình và năng lực giải quyết bài toán thông qua ngôn ngữ Python.

### 🎯 Chuẩn đầu ra môn học:
- **G1 (Tư duy thuật toán):** Biểu diễn thuật toán bằng mã giả và lưu đồ; cài đặt chương trình console và giao diện cơ bản giải quyết bài toán kinh doanh.
- **G2 (Cấu trúc điều khiển):** Vận dụng thành thạo cấu trúc rẽ nhánh (`if-elif-else`) và vòng lặp (`while`, `for`) cho các tác vụ lặp.
- **G3 (Thiết kế hàm):** Thiết kế và cài đặt hàm module hóa, hàm đệ quy để phân rã bài toán phức tạp.
- **G4 (Cấu trúc dữ liệu):** Khai thác thành thạo các kiểu dữ liệu tập hợp tích hợp (List, Tuple, Set, Dictionary).
- **G5 (Tệp tin & Ngoại lệ):** Đọc/ghi tệp tin văn bản, tệp nhị phân và thiết lập cơ chế xử lý ngoại lệ an toàn (`try-except`).
- **G6 (Lập trình Hướng đối tượng):** Nắm vững và vận dụng các nguyên lý OOP (Lớp, Đối tượng, Đóng gói, Kế thừa, Đa hình).
- **G7 (Năng lực tự học & Làm việc nhóm):** Phát triển tư duy phản biện, khả năng tự học suốt đời, kỹ năng làm việc nhóm và tinh thần trách nhiệm.

---

## 📚 3. Ma trận Kế hoạch Giảng dạy & Học liệu 15 Tuần

| Tuần | Bài học / Chủ đề | Bài giảng & Tài liệu đọc | Slide bài giảng | Thực hành / Bài tập | Trạng thái |
|:---:|:---|:---|:---:|:---:|:---:|
| **Tuần 01** | **Bài 1: Giới thiệu chung & Thiết kế giải thuật** | [Bài đọc 1: Giới thiệu lập trình & Python](lectures/part01-introduction/introduction-vn.md) | [Slide Bài 1 (PDF)](python_course_guide_slides.pdf) | Cài đặt môi trường (Python 3.11+, VS Code, Colab) | ✅ *Đã sẵn sàng* |
| **Tuần 02** | **Bài 2: Quy trình phát triển phần mềm & Kiểu dữ liệu** | Biểu thức số học, chuỗi, lệnh gán, biến, toán tử, module | - | Giao **Bài tập về nhà #1** | ⏳ *Đang biên soạn* |
| **Tuần 03** | **Bài 3: Cấu trúc ra quyết định (Decision Making)** | Nhánh `if`, `if-else`, `if-elif-else`, logic Boolean | - | Nộp BT #1 | ⏳ *Đang biên soạn* |
| **Tuần 04** | **Bài 4: Cấu trúc vòng lặp (Loops)** | Vòng lặp `while`, `for`, lặp lồng nhau, duyệt chuỗi | - | Giao **Bài tập về nhà #2** | ⏳ *Đang biên soạn* |
| **Tuần 05** | **Bài 5: Thiết kế hàm & Phạm vi biến** | Cú pháp `def`, tham số, giá trị trả về, đệ quy | - | Nộp BT #2 | ⏳ *Đang biên soạn* |
| **Tuần 06** | **Bài 6: Cấu trúc List và Tuple** | Mảng tuần tự 1D, 2D, slicing, các hàm tích hợp | - | Giao **Bài tập về nhà #3** | ⏳ *Đang biên soạn* |
| **Tuần 07** | **Thi giữa kỳ (Midterm Exam)** | Ôn tập tổng hợp kiến thức từ Bài 1 đến Bài 6 | - | **Thi Giữa kỳ (Trọng số 30%)** | ⏳ *Đang biên soạn* |
| **Tuần 08** | **Bài 7: Thao tác Tệp và Xử lý Ngoại lệ (Phần 1)** | Đọc/ghi tệp text, `sys.argv`, an toàn ngoại lệ `try-except` | - | Giao **Bài tập về nhà #4** | ⏳ *Đang biên soạn* |
| **Tuần 09** | **Bài 7: Thao tác Tệp và Xử lý Ngoại lệ (Phần 2)** | Xử lý tệp nhị phân, cấu trúc dữ liệu lưu trữ bền vững | - | Nộp BT #4 | ⏳ *Đang biên soạn* |
| **Tuần 10** | **Bài 8: Tập hợp (Set) và Từ điển (Dictionary)** | Bảng băm, tra cứu key-value, phân tích giao dịch | - | Case study TMĐT | ⏳ *Đang biên soạn* |
| **Tuần 11** | **Bài 9: Đối tượng và Lớp (OOP - Phần 1)** | Khái niệm Class, Object, constructor `__init__`, method | - | Mini-lab OOP | ⏳ *Đang biên soạn* |
| **Tuần 12** | **Bài 9: Đối tượng và Lớp (OOP - Phần 2)** | Đóng gói (encapsulation), thiết kế mô hình thực thể | - | Luyện tập OOP | ⏳ *Đang biên soạn* |
| **Tuần 13** | **Bài 10: Kế thừa và Đa hình (Phần 1)** | Cây kế thừa, lớp con, hàm `super()`, ghi đè method | - | Đề cương ôn tập | ⏳ *Đang biên soạn* |
| **Tuần 14** | **Bài 10: Kế thừa và Đa hình (Phần 2)** | Tính đa hình (polymorphism), thiết kế hệ thống | - | Tổng hợp kiến thức | ⏳ *Đang biên soạn* |
| **Tuần 15** | **Tổng kết và Ôn tập cuối kỳ** | Hệ thống hóa toàn bộ kiến thức học phần DSAI1003 | - | **Mock test phòng máy** | ⏳ *Đang biên soạn* |

---

## 📖 4. Giáo trình Chuẩn Quốc tế (Textbooks)

| Bìa sách | Tên tài liệu | Tác giả | Nhà xuất bản & Năm | Vai trò |
|:---:|:---|:---|:---:|:---:|
| <img src="assets/images/python-for-everyone-3rd-cover.jpg" alt="Python for Everyone" width="80" /> | **[1] Python for Everyone**, 3rd Edition | Cay Horstmann, Rance Necaise | Wiley (2019) | **Giáo trình chính** (Cú pháp & Giải thuật) |
| <img src="assets/images/intro-to-python-deitel-cover.jpg" alt="Intro to Python for Computer Science and Data Science" width="80" /> | **[2] Intro to Python for Computer Science and Data Science: Learning to Program with AI, Big Data and The Cloud** | Paul Deitel, Harvey Deitel | Pearson (2020) | **Giáo trình chính** (Xử lý dữ liệu & AI) |
| <img src="assets/images/the-python-workbook-cover.jpg" alt="The Python Workbook" width="80" /> | **[3] The Python Workbook: A Brief Introduction with Exercises and Solutions**, 2nd Edition | Ben Stephenson | Springer (2019) | Sách bài tập tự luyện kèm lời giải |

---

## ⚖️ 5. Phương thức Đánh giá Kết quả

* **Bài tập về nhà (HW - 30%):** Tối thiểu 4 bài tập thực hành lập trình và lý thuyết nộp qua hệ thống LMS/Moodle (2 tuần/bài).
* **Thi giữa kỳ (Midterm - 30%):** Bài kiểm tra đánh giá kiến thức từ Bài 1 đến Bài 6 (Tự luận trên giấy hoặc máy tính phòng Lab vào Tuần 7).
* **Thi cuối kỳ (Final - 40%):** Bài thi thực hành lập trình tổng hợp trực tiếp trên máy tính tại phòng Lab vào Tuần 15.
* **Quy định đạt môn:** Điểm tổng kết $\ge$ **5.0 / 10.0**; chuyên cần tham dự tối thiểu **80%** số buổi trên lớp.

---

> © 2026 TS. Vũ Đức Minh – Trường Đại học Kinh tế Quốc dân (NEU). Bản quyền tài liệu thuộc về tác giả.
