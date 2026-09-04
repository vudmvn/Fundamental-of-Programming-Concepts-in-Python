# Bài 1. Giới thiệu về lập trình và Python

**Cập nhật lần cuối:** 4 tháng 9 năm 2026

> **Nguồn biên soạn:** Chương 1 – *Introduction*, trong *Python for Everyone, 3rd Edition* của Cay Horstmann và Rance Necaise.
>
> Bài giảng này giữ cấu trúc và trọng tâm của Chương 1, nhưng được diễn giải lại bằng tiếng Việt theo hướng dùng trực tiếp cho giảng dạy.

---

## Giới thiệu bài học

Trước khi học biến, biểu thức, câu lệnh điều kiện hay vòng lặp, người học cần hiểu ba vấn đề nền tảng:

1. **Máy tính là gì và thực hiện chương trình như thế nào?**
2. **Python được dùng để viết và chạy chương trình ra sao?**
3. **Làm thế nào để mô tả một lời giải trước khi bắt đầu viết mã?**

Chương này bắt đầu từ khái niệm **computer program**, giới thiệu các thành phần chính của máy tính, sau đó hướng dẫn viết và chạy chương trình Python đầu tiên. Phần cuối tập trung vào hai kỹ năng quan trọng đối với người mới học lập trình:

- nhận biết và sửa lỗi;
- thiết kế thuật toán bằng **pseudocode** trước khi chuyển sang mã Python.

---

## Kiến thức và kỹ năng đạt được

Sau khi hoàn thành bài học, người học có thể:

- Giải thích khái niệm **computer program** và **programming**.
- Phân biệt **hardware** và **software**.
- Mô tả vai trò của **CPU**, **memory**, **secondary storage** và các thiết bị vào/ra.
- Giải thích vì sao cần sử dụng **high-level programming language**.
- Nêu được một số ưu điểm cơ bản của Python.
- Tạo, lưu và chạy một chương trình Python đơn giản.
- Sử dụng **interactive mode** để thử nhanh các câu lệnh Python.
- Giải thích ở mức khái niệm quá trình:
  **source code → byte code → virtual machine → running program**.
- Phân tích cấu trúc của chương trình `Hello, World!`.
- Phân biệt **compile-time error**, **exception** và **run-time/logic error**.
- Giải thích khái niệm **algorithm** và **pseudocode**.
- Mô tả một thuật toán theo các bước rõ ràng, thực thi được và kết thúc được.

---

## Cấu trúc bài học

1. Computer Programs
2. The Anatomy of a Computer
3. Computers Are Everywhere
4. The Python Programming Language
5. Becoming Familiar with Your Programming Environment
6. Interactive Mode và Backup Copies
7. The Python Interpreter
8. Analyzing Your First Program
9. Errors
10. Problem Solving: Algorithm Design
11. Data Is Everywhere
12. How To: Describing an Algorithm with Pseudocode
13. Worked Example: Tiling a Floor
14. Tổng kết và bài tập

---

# 1.1 Computer Programs

## 1.1.1 Máy tính có thể làm nhiều công việc khác nhau

Máy tính có thể được dùng cho rất nhiều mục đích:

- soạn thảo văn bản;
- tính toán;
- ngân hàng điện tử;
- chơi trò chơi;
- xử lý ảnh;
- điều khiển thiết bị;
- phân tích dữ liệu.

Điểm đáng chú ý là **cùng một máy tính vật lý** có thể thực hiện rất nhiều nhiệm vụ khác nhau.

Nguyên nhân là máy tính không bị giới hạn vào một công việc duy nhất. Nó có thể thực thi các **program** khác nhau.

### Computer program là gì?

**Computer program** là một chuỗi các chỉ dẫn và quyết định yêu cầu máy tính thực hiện một nhiệm vụ cụ thể.

Có thể hình dung:

```text
Bài toán
   ↓
Chương trình
   ↓
Các chỉ dẫn rất cơ bản
   ↓
Máy tính thực hiện với tốc độ cao
   ↓
Kết quả
```

Một lệnh máy tính ở mức rất thấp có thể đơn giản như:

- vẽ một điểm tại một vị trí trên màn hình;
- cộng hai số;
- kiểm tra một giá trị;
- chuyển sang một chỉ dẫn khác nếu điều kiện đúng.

Một ứng dụng hiện đại có thể gồm hàng triệu chỉ dẫn nhỏ như vậy.

---

## 1.1.2 Hardware và Software

### Hardware

**Hardware** là toàn bộ các thành phần vật lý của máy tính và thiết bị ngoại vi.

Ví dụ:

- CPU;
- bộ nhớ;
- ổ đĩa;
- màn hình;
- bàn phím;
- chuột;
- máy in.

### Software

**Software** là các chương trình mà máy tính thực thi.

Ví dụ:

- hệ điều hành;
- trình duyệt;
- phần mềm văn phòng;
- Python;
- các chương trình do chúng ta tự viết.

### Programming là gì?

**Programming** là quá trình:

> thiết kế và hiện thực các chương trình máy tính.

Lập trình không chỉ là gõ mã. Nó còn bao gồm:

- hiểu bài toán;
- thiết kế lời giải;
- viết chương trình;
- kiểm tra;
- sửa lỗi;
- cải tiến chương trình.

---

## Self Check 1.1

### Câu 1

Computer program là gì?

A. Một thiết bị vật lý trong máy tính  
B. Một chuỗi chỉ dẫn và quyết định để máy tính thực hiện nhiệm vụ  
C. Một loại dữ liệu  
D. Một thiết bị nhập

<details>
<summary>Đáp án</summary>

**B.** Chương trình máy tính là một chuỗi các chỉ dẫn và quyết định được thực thi để hoàn thành một nhiệm vụ.

</details>

### Câu 2

Phân biệt hardware và software.

<details>
<summary>Đáp án</summary>

- **Hardware:** các thành phần vật lý.
- **Software:** các chương trình điều khiển và sử dụng phần cứng.

</details>

### Câu 3

Đúng hay sai: Programming chỉ đơn giản là gõ các câu lệnh Python vào máy tính.

<details>
<summary>Đáp án</summary>

**Sai.** Programming còn bao gồm phân tích bài toán, thiết kế thuật toán, kiểm thử và sửa lỗi.

</details>

---

# 1.2 The Anatomy of a Computer

Để hiểu việc lập trình, chúng ta cần biết chương trình được thực thi ở đâu và dữ liệu được lưu trữ như thế nào.

## 1.2.1 Central Processing Unit – CPU

**CPU (Central Processing Unit)** là thành phần trung tâm chịu trách nhiệm:

- tìm và thực hiện các chỉ dẫn của chương trình;
- thực hiện phép toán số học;
- xử lý dữ liệu;
- đọc dữ liệu từ bộ nhớ hoặc thiết bị;
- ghi kết quả trở lại bộ nhớ hoặc thiết bị lưu trữ.

Có thể xem CPU là thành phần trực tiếp thực hiện các bước mà chương trình yêu cầu.

<p align="center">
  <img src="images/image-2.png" alt="Central Processing Unit - CPU" width="700" />
</p>

---

## 1.2.2 Primary Storage – bộ nhớ chính

**Primary storage**, hay memory, dùng để lưu:

- chương trình đang chạy;
- dữ liệu đang được chương trình xử lý.

Đặc điểm:

- nhanh;
- truy cập trực tiếp bởi CPU;
- thường cần điện để duy trì dữ liệu.

Trong máy tính cá nhân, primary storage thường chính là **RAM**.

<p align="center">
  <img src="images/image-1.png" alt="Primary Storage - RAM" width="700" />
</p>

---

## 1.2.3 Secondary Storage – bộ nhớ thứ cấp

**Secondary storage** dùng để lưu dữ liệu lâu dài.

Ví dụ:

- HDD;
- SSD;
- USB;
- các thiết bị lưu trữ khác.

So với memory:

| Đặc điểm | Primary storage | Secondary storage |
|---|---|---|
| Tốc độ | Nhanh hơn | Chậm hơn |
| Chi phí / dung lượng | Cao hơn | Thấp hơn |
| Lưu khi mất điện | Thường không | Có |
| Vai trò | Dữ liệu đang xử lý | Lưu trữ dài hạn |

---

## 1.2.4 Input và Output

### Input

Dữ liệu được đưa vào máy tính qua:

- bàn phím;
- chuột/trackpad;
- microphone;
- camera;
- mạng.

### Output

Máy tính gửi kết quả ra qua:

- màn hình;
- loa;
- máy in;
- mạng.

---

## 1.2.5 Mối quan hệ giữa các thành phần

Một mô hình đơn giản:

<p align="center">
  <img src="images/image-3.png" alt="Mối quan hệ giữa các thành phần phần cứng máy tính" width="700" />
</p>

### Khi chạy một chương trình

1. Program được lưu trong secondary storage.
2. Khi chạy, program được nạp vào memory.
3. CPU đọc từng chỉ dẫn.
4. CPU xử lý dữ liệu.
5. Kết quả có thể:
   - lưu vào memory;
   - ghi xuống secondary storage;
   - gửi ra thiết bị output.

---

## Self Check 1.2

### Câu 1

CPU có vai trò chính nào?

<details>
<summary>Đáp án</summary>

CPU thực hiện điều khiển chương trình và xử lý dữ liệu: tìm, đọc và thực thi các chỉ dẫn; thực hiện phép tính; trao đổi dữ liệu với bộ nhớ và thiết bị.

</details>

### Câu 2

Phân biệt primary storage và secondary storage.

<details>
<summary>Đáp án</summary>

Primary storage nhanh và dùng cho chương trình/dữ liệu đang xử lý. Secondary storage chậm hơn nhưng dùng để lưu dữ liệu lâu dài.

</details>

### Câu 3

Khi một chương trình bắt đầu chạy, nó thường được nạp từ đâu vào đâu?

<details>
<summary>Đáp án</summary>

Từ **secondary storage** vào **memory**.

</details>

---

# Computing & Society 1.1 – Computers Are Everywhere

Máy tính ban đầu rất lớn. Các hệ thống như ENIAC chiếm cả một căn phòng.

Ngày nay, máy tính xuất hiện ở nhiều quy mô:

- data center;
- laptop;
- smartphone;
- thẻ giao thông;
- ô tô;
- máy móc công nghiệp;
- thiết bị y tế;
- thiết bị gia dụng.

Một chiếc xe hiện đại có thể chứa nhiều máy tính nhỏ để điều khiển:

- động cơ;
- hệ thống phanh;
- đèn;
- giải trí;
- cảm biến.

<p align="center">
  <img src="images/image-4.png" alt="Máy tính nhúng trong các thiết bị hiện đại" width="700" />
</p>

### Ý nghĩa

Kiến thức về máy tính và lập trình không còn chỉ dành cho chuyên gia CNTT.

Nó ngày càng quan trọng trong:

- kỹ thuật;
- kinh tế;
- quản trị;
- khoa học;
- y tế;
- phân tích dữ liệu.

---

# 1.3 The Python Programming Language

## 1.3.1 Vì sao cần ngôn ngữ lập trình bậc cao?

CPU chỉ thực thi các chỉ dẫn rất cơ bản.

Việc yêu cầu lập trình viên viết trực tiếp hàng nghìn hoặc hàng triệu lệnh mức thấp là:

- khó;
- mất thời gian;
- dễ sai.

Do đó, **high-level programming languages** được phát triển.

Người lập trình viết các chỉ dẫn ở mức trừu tượng cao hơn. Sau đó hệ thống tự động chuyển chúng thành dạng mà máy tính có thể thực thi.

---

## 1.3.2 Python

Python là một ngôn ngữ lập trình bậc cao.

Python được phát triển bởi **Guido van Rossum** từ đầu thập niên 1990.

<p align="center">
  <img src="images/image-5.png" alt="Guido van Rossum - Tác giả ngôn ngữ Python" width="500" />
</p>

Một số mục tiêu thiết kế quan trọng của Python:

- dễ viết chương trình;
- dễ sửa đổi;
- cú pháp đơn giản;
- thuận tiện khi làm việc với dữ liệu phức tạp.

---

## 1.3.3 Vì sao Python phổ biến?

### 1. Cú pháp đơn giản

So với nhiều ngôn ngữ khác, Python có cú pháp tương đối gọn và dễ đọc.

### 2. Phù hợp cho người mới

Người học có thể tập trung nhiều hơn vào tư duy giải quyết bài toán.

### 3. Interactive programming

Python hỗ trợ môi trường tương tác, giúp người học thử từng lệnh và nhận kết quả ngay.

### 4. Portable

Một chương trình Python thường có thể chạy trên nhiều hệ điều hành như:

- Windows;
- Linux;
- macOS.

### 5. Nhiều packages

**Package** là một tập hợp mã nguồn hỗ trợ giải quyết một nhóm bài toán.

Ví dụ package cho:

- machine learning;
- statistics;
- data visualization;
- computational biology;
- xử lý dữ liệu.

---

## Self Check 1.3

### Câu 1

Vì sao chúng ta sử dụng high-level programming language?

<details>
<summary>Đáp án</summary>

Vì việc viết trực tiếp các chỉ dẫn CPU ở mức thấp rất phức tạp và dễ sai. Ngôn ngữ bậc cao giúp mô tả lời giải thuận tiện hơn.

</details>

### Câu 2

Nêu ba ưu điểm của Python.

<details>
<summary>Đáp án</summary>

Ví dụ:

- cú pháp đơn giản;
- dễ học;
- hỗ trợ interactive programming;
- portable;
- nhiều packages.

</details>

### Câu 3

Package là gì?

<details>
<summary>Đáp án</summary>

Package là một tập hợp mã được xây dựng để hỗ trợ một lĩnh vực hoặc nhóm bài toán cụ thể, giúp lập trình viên tái sử dụng giải pháp có sẵn.

</details>

---

# 1.4 Becoming Familiar with Your Programming Environment

Để lập trình, bạn cần một **programming environment**.

Tùy môi trường học tập, bạn có thể sử dụng:

- IDE;
- text editor + terminal;
- Python shell;
- notebook environment.

## Bước 1. Cài đặt môi trường Python

Cần cài:

- Python;
- trình soạn thảo hoặc IDE phù hợp.

## Bước 2. Khởi động môi trường

Ví dụ:

- VS Code;
- PyCharm;
- IDLE;
- terminal;
- môi trường được giảng viên cung cấp.

## Bước 3. Viết chương trình đầu tiên

Tạo file:

```text
hello.py
```

Nội dung:

```python
# My first Python program.
print("Hello, World!")
```

## Bước 4. Chạy chương trình

Kết quả:

```text
Hello, World!
```

## Bước 5. Tổ chức file

Nên tổ chức bài tập theo thư mục.

Ví dụ:

```text
PythonCourse/
│
├── Chapter01/
│   ├── hello.py
│   └── exercises/
│
├── Chapter02/
│
└── Chapter03/
```

### Lưu ý: Python is case sensitive

Python phân biệt chữ hoa và chữ thường.

```python
print("Hello")
```

khác với:

```python
Print("Hello")
```

`Print` không phải là `print`.

---

## Self Check 1.4

### Câu 1

Phần mở rộng thông thường của file chương trình Python là gì?

<details>
<summary>Đáp án</summary>

`.py`

</details>

### Câu 2

Đúng hay sai: `print` và `Print` là cùng một tên trong Python.

<details>
<summary>Đáp án</summary>

**Sai.** Python phân biệt chữ hoa và chữ thường.

</details>

### Câu 3

Vì sao nên tổ chức các bài tập Python trong các thư mục riêng?

<details>
<summary>Đáp án</summary>

Để dễ quản lý, tìm kiếm, sao lưu và nộp bài.

</details>

---

# Programming Tip 1.1 – Interactive Mode

Python có thể được sử dụng theo hai cách phổ biến:

## Script mode

Viết chương trình trong file:

```text
hello.py
```

sau đó chạy toàn bộ file.

## Interactive mode

Nhập từng lệnh và nhận kết quả ngay.

Ví dụ:

```python
>>> print("Hello, World!")
Hello, World!
```

hoặc:

```python
>>> 7035 * 0.15
1055.25
```

### Khi nào nên dùng interactive mode?

- thử một biểu thức;
- kiểm tra cú pháp;
- học một hàm mới;
- kiểm tra nhanh một ý tưởng;
- dùng Python như máy tính cầm tay.

---

## Self Check – Interactive Mode

Interactive mode thích hợp nhất cho trường hợp nào?

A. Viết một hệ thống phần mềm lớn  
B. Thử nhanh một biểu thức Python  
C. Lưu trữ dữ liệu lâu dài  
D. Thay thế CPU

<details>
<summary>Đáp án</summary>

**B.**

</details>

---

# Programming Tip 1.2 – Backup Copies

Việc mất file có thể xảy ra do:

- xóa nhầm;
- hỏng thiết bị;
- ghi đè file;
- lỗi hệ thống.

Do đó cần tạo **backup copies**.

## Nguyên tắc cơ bản

### 1. Backup thường xuyên

Không nên đợi đến cuối ngày mới sao lưu.

### 2. Có nhiều bản backup

Có thể lưu nhiều phiên bản khác nhau.

### 3. Kiểm tra chiều sao chép

Cần chắc chắn rằng bạn đang:

```text
work folder → backup folder
```

chứ không phải ngược lại.

### 4. Thỉnh thoảng kiểm tra backup

Backup chỉ có giá trị nếu có thể phục hồi được.

---

# Special Topic 1.1 – The Python Interpreter

Ta thường nói:

> Python interpreter đọc chương trình và thực thi từng bước.

Nhưng bên trong, quá trình có thể hiểu chi tiết hơn.

```text
Source code (.py)
      ↓
   Compiler
      ↓
   Byte code
      ↓
Virtual Machine
      ↓
Running Program
```

<p align="center">
  <img src="images/image-6.png" alt="Quy trình thực thi của Python Interpreter: Source code -> Byte code -> Virtual Machine" width="700" />
</p>

## Source code

Là mã Python do người lập trình viết.

Ví dụ:

```python
print("Hello")
```

## Compiler

Compiler chuyển source code thành **byte code**.

## Byte code

Là dạng chỉ dẫn đơn giản hơn, dùng bởi Python Virtual Machine.

## Virtual Machine

Virtual machine thực thi byte code.

## Standard Library

Các chức năng có sẵn như `print()` được cung cấp bởi Python Standard Library.

## Additional packages

Với các nhiệm vụ đặc biệt, có thể cần cài thêm package.

---

## Self Check – Python Interpreter

### Câu 1

Sắp xếp đúng thứ tự:

- byte code
- source code
- virtual machine
- compiler

<details>
<summary>Đáp án</summary>

```text
source code
→ compiler
→ byte code
→ virtual machine
```

</details>

### Câu 2

`print()` có cần tự lập trình lại từ đầu không?

<details>
<summary>Đáp án</summary>

Không. `print()` là chức năng có sẵn trong môi trường Python.

</details>

---

# 1.5 Analyzing Your First Program

Xét chương trình:

```python
# My first Python program.
print("Hello, World!")
```

## 1.5.1 Comment

Dòng:

```python
# My first Python program.
```

là một **comment**.

Comment:

- bắt đầu bằng `#`;
- dành cho người đọc mã;
- không được thực thi như một statement.

---

## 1.5.2 Statement

Dòng:

```python
print("Hello, World!")
```

là một Python statement.

Nó yêu cầu Python thực hiện một hành động.

---

## 1.5.3 Function

`print` là một **function**.

Function là:

> một tập hợp các chỉ dẫn thực hiện một nhiệm vụ cụ thể.

---

## 1.5.4 Function call

Khi viết:

```python
print("Hello, World!")
```

ta **call** function `print`.

Cấu trúc:

```text
function_name(arguments)
```

---

## 1.5.5 Argument

Trong:

```python
print("Hello, World!")
```

giá trị:

```python
"Hello, World!"
```

là một **argument**.

Argument cung cấp dữ liệu cho function.

---

## 1.5.6 String

Một dãy ký tự nằm trong dấu nháy được gọi là **string**.

```python
"Hello, World!"
```

hoặc:

```python
'Hello, World!'
```

đều là string.

---

## 1.5.7 `print()` với nhiều arguments

Ví dụ:

```python
print("The answer is", 6 * 7)
```

Output:

```text
The answer is 42
```

Các giá trị được in theo thứ tự và mặc định cách nhau bởi khoảng trắng.

---

## 1.5.8 `print()` không có argument

```python
print("Hello")
print()
print("World")
```

Output:

```text
Hello

World
```

`print()` tạo ra một dòng trống.

---

## Syntax – print Statement

```python
print()
print(value1, value2, ..., valuen)
```

Ví dụ:

```python
print("The answer is", 6 + 7, "!")
```

<p align="center">
  <img src="images/image-7.png" alt="Kết quả thực thi lệnh print trong Python" width="700" />
</p>

---

## Self Check 1.5

### Câu 1

Trong lệnh:

```python
print("Python")
```

hãy xác định:

- function name;
- argument;
- data type của argument.

<details>
<summary>Đáp án</summary>

- Function name: `print`
- Argument: `"Python"`
- Data type: string

</details>

### Câu 2

Dòng sau có được Python thực thi không?

```python
# Calculate the total cost.
```

<details>
<summary>Đáp án</summary>

Không. Đây là comment.

</details>

### Câu 3

Output của:

```python
print("The answer is", 6 + 7, "!")
```

là gì?

<details>
<summary>Đáp án</summary>

```text
The answer is 13 !
```

</details>

---

# 1.6 Errors

Lỗi là điều bình thường trong quá trình phát triển chương trình.

Người lập trình cần học cách:

- đọc thông báo lỗi;
- xác định loại lỗi;
- tìm vị trí lỗi;
- sửa lỗi;
- kiểm thử lại.

---

## 1.6.1 Compile-Time Error / Syntax Error

Ví dụ:

```python
print("Hello, World!)
```

Khi chạy câu lệnh trên, ta thiếu dấu đóng ngoặc kép `"`. Python sẽ dừng ngay trong quá trình phân tích cú pháp và hiển thị thông báo lỗi:

```text
SyntaxError: EOL while scanning string literal
```

*(Lưu ý: Trong các phiên bản Python mới từ 3.10 trở lên, lỗi này có thể được hiển thị rõ hơn dưới dạng `SyntaxError: unterminated string literal (detected at line 1)`).*

**Giải thích thông báo lỗi:**
- **`SyntaxError`:** Lỗi cú pháp (mã nguồn vi phạm quy tắc ngữ pháp của ngôn ngữ Python).
- **`EOL` (End Of Line):** Kết thúc dòng.
- **`string literal`:** Hằng chuỗi ký tự (chuỗi văn bản nằm trong cặp dấu nháy kép `"` hoặc nháy đơn `'`).
- **Bản chất lỗi:** Trình thông dịch Python đang quét một hằng chuỗi (bắt đầu bằng dấu `"`) nhưng lại gặp ký tự kết thúc dòng (xuống dòng) trước khi tìm thấy dấu đóng ngoặc kép tương ứng để khép lại chuỗi.

Lỗi này vi phạm cú pháp Python và được phát hiện ở giai đoạn biên dịch mã nguồn sang byte code (trước khi chương trình thực thi bình thường). Vì vậy, đây là một **compile-time error** hay **syntax error**.

### Ví dụ khác

```python
print(Hello, World!)
```

Python không hiểu `Hello` và `World` theo cách người viết mong muốn. Do thiếu dấu ngoặc kép, Python coi `Hello` và `World` là các biến/định danh (identifiers), và dấu phẩy ngăn cách khiến cú pháp câu lệnh không hợp lệ (báo lỗi `SyntaxError: invalid syntax`).

---

## 1.6.2 Exception

Ví dụ:

```python
print(1 / 0)
```

Cú pháp hợp lệ, nhưng phép chia cho 0 không thể thực hiện.

Python phát sinh:

```text
ZeroDivisionError
```

Đây là một **exception** xảy ra trong quá trình chạy.

---

## 1.6.3 Logic / Run-Time Error

Ví dụ:

```python
print("Hello, Word!")
```

Chương trình:

- hợp lệ về cú pháp;
- chạy được;
- không phát sinh exception;

nhưng output không đúng mong muốn.

Đây là lỗi logic.

---

## So sánh các loại lỗi

| Loại lỗi | Thời điểm phát hiện | Ví dụ |
|---|---|---|
| Syntax / compile-time | Trước khi chạy đúng | thiếu dấu nháy |
| Exception | Trong khi chạy | chia cho 0 |
| Logic error | Chương trình chạy nhưng kết quả sai | in `"Word"` thay vì `"World"` |

---

# Common Error 1.1 – Misspelling Words

Python phân biệt chữ hoa và chữ thường.

Sai:

```python
Print("Hello")
```

Đúng:

```python
print("Hello")
```

Một lỗi chính tả nhỏ có thể tạo ra thông báo lỗi khó hiểu.

Khi nhận lỗi liên quan đến:

- undefined name;
- function không tồn tại;

hãy kiểm tra:

- chính tả;
- chữ hoa/chữ thường;
- dấu câu.

---

## Self Check 1.6

### Câu 1

Lỗi trong:

```python
print("Hello)
```

thuộc loại nào?

<details>
<summary>Đáp án</summary>

Syntax / compile-time error.

</details>

### Câu 2

Lỗi trong:

```python
print(10 / 0)
```

thuộc loại nào?

<details>
<summary>Đáp án</summary>

Exception xảy ra lúc chạy, cụ thể là `ZeroDivisionError`.

</details>

### Câu 3

Chương trình chạy được nhưng kết quả sai thuộc loại lỗi nào?

<details>
<summary>Đáp án</summary>

Logic error / run-time error theo cách phân loại của chương.

</details>

---

# 1.7 Problem Solving: Algorithm Design

Trước khi viết mã, cần xác định:

> Máy tính phải thực hiện các bước nào?

Máy tính không thể tự hiểu một yêu cầu mơ hồ.

Ví dụ:

> “Hãy tìm người phù hợp nhất với tôi.”

Yêu cầu này không đủ chính xác vì “phù hợp nhất” có thể phụ thuộc vào ý kiến cá nhân.

Ngược lại, bài toán:

> Có $10,000 trong tài khoản, lãi suất 5% mỗi năm. Sau bao nhiêu năm số dư ít nhất đạt $20,000?

có thể mô tả bằng các bước rõ ràng.

---

## 1.7.1 Pseudocode

**Pseudocode** là mô tả không chính thức của các bước giải bài toán.

Ví dụ:

```text
Set year to 0.
Set balance to 10000.

While balance is less than 20000:
    Add 1 to year.
    Set interest to balance × 0.05.
    Add interest to balance.

Report year.
```

Pseudocode:

- không cần đúng cú pháp Python;
- dành cho con người;
- tập trung vào logic lời giải.

---

## 1.7.2 Algorithm

Một **algorithm** là một chuỗi bước giải quyết bài toán.

Theo chương, một thuật toán tốt phải có ba đặc điểm:

### 1. Unambiguous

Mỗi bước phải rõ ràng, không mơ hồ.

### 2. Executable

Mỗi bước phải thực hiện được trong thực tế.

### 3. Terminating

Thuật toán phải kết thúc sau hữu hạn bước.

---

## 1.7.3 Software Development Process

Có thể tóm tắt quá trình phát triển:

```text
Understand the problem
        ↓
Develop and describe an algorithm
        ↓
Test the algorithm with simple inputs
        ↓
Translate the algorithm into Python
        ↓
Compile / run / test the program
```

Điểm quan trọng:

> Không nên bắt đầu bằng việc gõ Python ngay lập tức.

---

## Self Check 1.7

### Câu 1

Pseudocode là gì?

<details>
<summary>Đáp án</summary>

Pseudocode là mô tả không chính thức nhưng rõ ràng về chuỗi các bước dùng để giải một bài toán.

</details>

### Câu 2

Ba đặc điểm quan trọng của một algorithm là gì?

<details>
<summary>Đáp án</summary>

- unambiguous;
- executable;
- terminating.

</details>

### Câu 3

Thứ tự hợp lý hơn là:

A. Code → hiểu bài toán → thuật toán  
B. Hiểu bài toán → thuật toán → code  
C. Code → test → hiểu bài toán

<details>
<summary>Đáp án</summary>

**B.**

</details>

---

# Computing & Society 1.2 – Data Is Everywhere

Ngày nay, dữ liệu được thu thập ở quy mô rất lớn.

Ví dụ:

- giao dịch;
- ảnh;
- video;
- cảm biến;
- hành vi người dùng;
- dữ liệu y tế;
- dữ liệu giao thông.

Sự gia tăng năng lực tính toán tạo điều kiện cho **data science**.

## Data mining

Mục tiêu:

- tìm pattern;
- tìm nhóm dữ liệu tương tự;
- phát hiện hành vi bất thường;
- hỗ trợ dự đoán.

## Machine learning

Machine learning xây dựng hệ thống có khả năng học từ dữ liệu.

Ví dụ:

```text
Training data
     ↓
Machine-learning model
     ↓
Model đã học
     ↓
Dữ liệu mới
     ↓
Prediction
```

Một mô hình có thể học từ rất nhiều ảnh chó/mèo và sau đó dự đoán ảnh mới thuộc lớp nào.

Python rất phù hợp với data science vì:

- interactive;
- dễ thử nghiệm;
- có nhiều packages;
- hỗ trợ xử lý dữ liệu và machine learning.

---

# HOW TO 1.1 – Describing an Algorithm with Pseudocode

## Bài toán

Bạn cần lựa chọn giữa hai chiếc xe:

- xe 1 tiết kiệm nhiên liệu hơn nhưng giá mua cao;
- xe 2 rẻ hơn nhưng tốn nhiên liệu hơn.

Biết:

- purchase price;
- fuel efficiency;
- giá xăng;
- số km/mile đi mỗi năm;
- thời gian sử dụng.

Hãy xác định chiếc xe có tổng chi phí thấp hơn.

---

## Bước 1. Xác định input và output

### Input

Với mỗi xe:

- purchase price;
- fuel efficiency.

Thông tin chung:

- annual miles driven;
- gas price;
- number of years.

### Output

Chiếc xe có total cost thấp hơn.

---

## Bước 2. Chia bài toán thành các bài toán nhỏ

Với mỗi xe:

```text
annual fuel consumed
annual fuel cost
operating cost
total cost
```

---

## Bước 3. Viết pseudocode

```text
For each car:
    annual fuel consumed =
        annual miles driven / fuel efficiency

    annual fuel cost =
        price per gallon × annual fuel consumed

    operating cost =
        10 × annual fuel cost

    total cost =
        purchase price + operating cost

If total cost of car 1 < total cost of car 2:
    Choose car 1.
Else:
    Choose car 2.
```

---

## Bước 4. Test pseudocode bằng một ví dụ cụ thể

Giả sử:

### Car 1

- price = 25,000
- fuel efficiency = 50 mpg

### Car 2

- price = 20,000
- fuel efficiency = 30 mpg

Với Car 1:

```text
annual fuel consumed = 15000 / 50 = 300
annual fuel cost = 4 × 300 = 1200
operating cost = 10 × 1200 = 12000
total cost = 25000 + 12000 = 37000
```

Nếu Car 2 có total cost = 40,000 thì chọn Car 1.

---

## Self Check – Pseudocode Design

Tại sao nên test pseudocode bằng một ví dụ đơn giản trước khi viết Python?

<details>
<summary>Đáp án</summary>

Vì việc kiểm tra bằng tay giúp phát hiện sớm lỗi trong logic của thuật toán trước khi thêm độ phức tạp của cú pháp lập trình.

</details>

---

# WORKED EXAMPLE 1.1 – Writing an Algorithm for Tiling a Floor

## Bài toán

Lát một sàn hình chữ nhật bằng gạch đen và trắng xen kẽ.

Mỗi viên:

```text
4 × 4 inches
```

Kích thước sàn là bội số của 4.

---

## Bước 1. Input và Output

### Input

- length;
- width.

### Output

Một cách bố trí các viên gạch đen/trắng phủ kín sàn.

---

## Bước 2. Chia bài toán

Một bài toán con tự nhiên:

> Lát một hàng gạch.

Nếu lát được một hàng, có thể lặp lại theo từng hàng cho đến khi phủ kín sàn.

Trong một hàng:

- bắt đầu bằng một màu;
- viên tiếp theo dùng màu đối lập;
- tiếp tục cho đến hết hàng.

---

## Bước 3. Pseudocode

```text
Place a black tile in the northwest corner.

While the floor is not yet filled:

    Repeat until the current row is filled:
        If the previously placed tile was white:
            Pick a black tile.
        Else:
            Pick a white tile.

        Place the picked tile east of the previous tile.

    Locate the first tile of the completed row.

    If there is space to the south:
        Place a tile of the opposite color below it.
```

---

## Bước 4. Test bằng ví dụ

Giả sử sàn:

```text
20 × 12 inches
```

Mỗi viên:

```text
4 × 4 inches
```

Số cột:

```text
20 / 4 = 5
```

Số hàng:

```text
12 / 4 = 3
```

Một cách bố trí:

```text
B W B W B
W B W B W
B W B W B
```

Trong đó:

- `B` = Black
- `W` = White

---

# Tổng kết Chương 1

## Computer Programs

- Máy tính thực hiện các chỉ dẫn cơ bản với tốc độ rất cao.
- Computer program là chuỗi chỉ dẫn và quyết định.
- Programming là quá trình thiết kế và hiện thực chương trình.

## Computer Architecture

- CPU thực hiện điều khiển và xử lý.
- Memory lưu chương trình/dữ liệu đang hoạt động.
- Secondary storage lưu dữ liệu lâu dài.
- Peripheral devices cung cấp input/output.

## Python

- Python là high-level programming language.
- Python dễ học, portable và có nhiều packages.
- Python hỗ trợ interactive programming.

## Programming Environment

- Program thường được lưu trong file `.py`.
- Python phân biệt chữ hoa/chữ thường.
- Nên tổ chức file và backup thường xuyên.

## First Program

```python
print("Hello, World!")
```

Giới thiệu:

- comment;
- statement;
- function;
- function call;
- argument;
- string.

## Errors

- syntax / compile-time error;
- exception;
- logic / run-time error.

## Algorithm Design

Một algorithm cần:

- unambiguous;
- executable;
- terminating.

Quy trình khuyến nghị:

```text
Problem
↓
Algorithm
↓
Test by hand
↓
Python code
↓
Run and test
```

---

# Quiz tổng hợp

## Câu 1

Programming là:

A. Chỉ sử dụng phần mềm  
B. Thiết kế và hiện thực chương trình máy tính  
C. Chỉ viết comment  
D. Chỉ sửa lỗi

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 2

Thành phần nào trực tiếp thực thi các chỉ dẫn của chương trình?

A. CPU  
B. Printer  
C. Keyboard  
D. Hard disk

<details>
<summary>Đáp án</summary>

**A**

</details>

## Câu 3

Chương trình Python thường có phần mở rộng:

A. `.java`  
B. `.cpp`  
C. `.py`  
D. `.txt`

<details>
<summary>Đáp án</summary>

**C**

</details>

## Câu 4

Dòng nào là comment?

A. `print("Hello")`  
B. `# print a greeting`  
C. `"Hello"`  
D. `print()`

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 5

Trong:

```python
print("Hello")
```

`"Hello"` là:

A. function  
B. comment  
C. argument và string  
D. syntax error

<details>
<summary>Đáp án</summary>

**C**

</details>

## Câu 6

Đoạn mã:

```python
print(1 / 0)
```

gây ra:

A. syntax error  
B. exception  
C. không có lỗi  
D. comment

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 7

Pseudocode chủ yếu dùng để:

A. thay thế CPU  
B. mô tả logic thuật toán trước khi code  
C. tạo file backup  
D. cài Python

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 8

Một thuật toán hợp lệ cần:

A. unambiguous  
B. executable  
C. terminating  
D. cả ba

<details>
<summary>Đáp án</summary>

**D**

</details>

---

# Bài tập thực hành

## Bài 1. Hello Python

Viết chương trình in ra:

```text
Hello, Python!
I am learning programming.
```

---

## Bài 2. Phân tích chương trình

Cho:

```python
# Calculate an answer.
print("The answer is", 8 + 5)
```

Hãy chỉ ra:

- comment;
- function;
- function call;
- arguments;
- string;
- expression.

---

## Bài 3. Phân loại lỗi

Cho từng đoạn mã sau, hãy xác định loại lỗi.

### a.

```python
print("Hello)
```

### b.

```python
print(10 / 0)
```

### c.

```python
print("Goodbye")
```

trong khi yêu cầu là in `"Hello"`.

<details>
<summary>Gợi ý / Đáp án</summary>

- a: syntax error.
- b: exception.
- c: logic error.

</details>

---

## Bài 4. Interactive Mode

Trong Python interactive mode, thử:

```python
10 + 20
8 * 7
100 / 4
2 ** 10
```

Ghi lại kết quả.

---

## Bài 5. Algorithm Design

Một tài khoản có:

```text
balance = 10,000
```

Mỗi tháng:

- nhận lãi 0.5%;
- rút 500.

Viết pseudocode xác định sau bao nhiêu tháng tài khoản hết tiền.

---

## Bài 6. Chi phí đi lại

Bạn có thể:

- lái xe;
- đi tàu.

Biết:

- khoảng cách;
- mức tiêu thụ nhiên liệu;
- giá xăng;
- giá vé tàu.

Hãy mô tả thuật toán để xác định phương án rẻ hơn.

---

# Bài tập mở

## Bài 1

Một smartphone là thiết bị đơn chức năng hay máy tính lập trình được? Giải thích.

## Bài 2

Nêu ba ví dụ về máy tính được nhúng trong các thiết bị không giống máy tính truyền thống.

## Bài 3

Giải thích vì sao bài toán:

> “Hãy tìm người bạn đời phù hợp nhất.”

khó chuyển trực tiếp thành một algorithm.

## Bài 4

Tự chọn một công việc hàng ngày và mô tả bằng pseudocode.

Ví dụ:

- pha cà phê;
- đăng nhập vào hệ thống;
- tính tiền mua hàng;
- gửi email.

Yêu cầu pseudocode phải:

- rõ ràng;
- thực hiện được;
- kết thúc được.

---

# Thuật ngữ quan trọng

| Thuật ngữ | Ý nghĩa |
|---|---|
| Computer program | Chuỗi chỉ dẫn và quyết định cho máy tính |
| Programming | Thiết kế và hiện thực chương trình |
| Hardware | Thành phần vật lý của máy tính |
| Software | Các chương trình máy tính |
| CPU | Bộ xử lý trung tâm |
| Memory | Bộ nhớ chính |
| Secondary storage | Bộ nhớ lưu trữ dài hạn |
| Input | Dữ liệu đưa vào hệ thống |
| Output | Thông tin hệ thống tạo ra |
| High-level language | Ngôn ngữ lập trình bậc cao |
| Python | Ngôn ngữ lập trình bậc cao |
| Package | Tập mã hỗ trợ một lĩnh vực/bài toán |
| Interpreter | Thành phần thực thi chương trình Python |
| Source code | Mã do lập trình viên viết |
| Byte code | Mã trung gian cho virtual machine |
| Comment | Ghi chú cho người đọc mã |
| Function | Nhóm chỉ dẫn thực hiện một nhiệm vụ |
| Argument | Giá trị truyền cho function |
| String | Chuỗi ký tự |
| Syntax error | Lỗi cú pháp |
| Exception | Lỗi phát sinh khi thực thi một thao tác |
| Logic error | Chương trình chạy nhưng cho kết quả sai |
| Pseudocode | Mô tả không chính thức của thuật toán |
| Algorithm | Chuỗi bước rõ ràng để giải bài toán |

---

# Gợi ý học tập

Sau khi học xong Chương 1, người học chưa cần cố viết các chương trình phức tạp. Quan trọng nhất là hình thành quy trình:

```text
Hiểu bài toán
→ nghĩ cách giải bằng tay
→ mô tả thành algorithm/pseudocode
→ chuyển sang Python
→ chạy
→ đọc lỗi
→ sửa
→ kiểm thử lại
```

Đây là quy trình sẽ được sử dụng xuyên suốt các chương tiếp theo.
