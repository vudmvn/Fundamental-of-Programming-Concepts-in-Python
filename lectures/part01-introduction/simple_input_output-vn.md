# Bài giảng: Nhập/Xuất cơ bản trong Python

## 1. Giới thiệu bài học

Trong hầu hết các chương trình, dữ liệu được tiếp nhận, xử lý và sau đó trả kết quả cho người dùng. Hai thao tác nền tảng để thực hiện quá trình này là:

- **Nhập dữ liệu (Input):** nhận dữ liệu từ người dùng.
- **Xuất dữ liệu (Output):** hiển thị kết quả ra màn hình.

Ví dụ, một chương trình tính diện tích hình chữ nhật cần:

1. Nhập chiều dài.
2. Nhập chiều rộng.
3. Tính diện tích.
4. In kết quả ra màn hình.

Trong Python, hai hàm cơ bản nhất để thực hiện nhập và xuất dữ liệu là:

```python
input()
print()
```

---

## 2. Mục tiêu học tập

Sau bài học này, sinh viên có thể:

1. Sử dụng `print()` để xuất dữ liệu ra màn hình.
2. In nhiều giá trị trong cùng một lệnh `print()`.
3. Sử dụng các tham số cơ bản `sep` và `end`.
4. Sử dụng `input()` để nhận dữ liệu từ bàn phím.
5. Hiểu rằng `input()` trả về dữ liệu kiểu `str`.
6. Chuyển dữ liệu nhập sang `int` hoặc `float` khi cần tính toán.
7. Kết hợp nhập dữ liệu, tính toán và xuất kết quả.
8. Sử dụng f-string để định dạng output đơn giản.
9. Phân biệt một số lỗi thường gặp khi làm việc với nhập/xuất.

> **Phạm vi bài học:** Các bài tập trong bài này được viết trực tiếp bằng các câu lệnh cơ bản; chưa sử dụng hàm tự định nghĩa (`def`).

---

## 3. Xuất dữ liệu với `print()`

### 3.1. Cú pháp cơ bản

```python
print(value)
```

Ví dụ:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

Có thể xuất trực tiếp các giá trị số:

```python
print(100)
print(3.14)
```

Hoặc xuất giá trị đang được lưu trong biến:

```python
name = "An"
age = 18

print(name)
print(age)
```

---

### 3.2. In nhiều giá trị trong một lệnh

`print()` có thể nhận nhiều giá trị cùng lúc.

```python
name = "An"
age = 18

print("Name:", name)
print("Age:", age)
```

Output:

```text
Name: An
Age: 18
```

Theo mặc định, `print()` chèn một dấu cách giữa các giá trị được truyền vào.

```python
x = 10
y = 20
print(x, y)
```

Output:

```text
10 20
```

---

### 3.3. Tham số `sep` — điều khiển ký tự phân cách

```python
print("2026", "09", "06", sep="-")
```

Output:

```text
2026-09-06
```

Ví dụ khác:

```python
print("Python", "Java", "C++", sep=" | ")
```

Output:

```text
Python | Java | C++
```

---

### 3.4. Tham số `end` — điều khiển ký tự kết thúc

Mặc định, sau mỗi `print()`, Python xuống dòng.

```python
print("Hello")
print("Python")
```

Output:

```text
Hello
Python
```

Có thể thay đổi bằng `end`:

```python
print("Hello", end=" ")
print("Python")
```

Output:

```text
Hello Python
```

---

### Câu hỏi tự kiểm tra 1

### Câu 1

Output của chương trình sau là gì?

```python
print("A", "B", "C", sep="-")
```

<details>
<summary>Đáp án</summary>

```text
A-B-C
```

</details>

### Câu 2

Output của chương trình sau là gì?

```python
print("Hello", end=" ")
print("World")
```

<details>
<summary>Đáp án</summary>

```text
Hello World
```

</details>

---

## 4. Xuất giá trị của biến

Thông thường chúng ta không chỉ in giá trị cố định mà còn in dữ liệu được lưu trong biến.

```python
product = "Laptop"
price = 1500

print(product)
print(price)
```

Có thể kết hợp text và biến:

```python
print("Product:", product)
print("Price:", price)
```

---

## 5. Nhập dữ liệu với `input()`

### 5.1. Cú pháp

```python
variable = input("Prompt")
```

Ví dụ:

```python
name = input("Enter your name: ")
print("Hello", name)
```

`input()` thực hiện bốn bước:

1. hiển thị lời nhắc;
2. chờ người dùng nhập dữ liệu;
3. nhận dữ liệu khi người dùng nhấn Enter;
4. trả về dữ liệu vừa nhập.

---

### 5.2. Kiểu dữ liệu trả về của `input()`

```python
age = input("Enter your age: ")
print(type(age))
```

Nếu nhập `18`, kết quả vẫn là:

```text
<class 'str'>
```

Dù dữ liệu trông giống một số, `input()` vẫn trả về chuỗi.

---

## 6. Chuyển đổi kiểu dữ liệu đầu vào

Khi dữ liệu nhập được sử dụng trong các phép tính số học, cần chuyển chuỗi nhận được từ `input()` sang kiểu số phù hợp.

### 6.1. Chuyển sang số nguyên với `int()`

```python
age = int(input("Enter your age: "))
print(age + 1)
```

Nếu nhập `18`, output là:

```text
19
```

### 6.2. Chuyển sang số thực với `float()`

```python
price = float(input("Enter price: "))
print(price)
```

---

### 6.3. So sánh khi có và không có chuyển kiểu

#### Trường hợp 1 — Không chuyển kiểu

```python
x = input("Enter x: ")
y = input("Enter y: ")
print(x + y)
```

Nếu nhập `10` và `20`, output là:

```text
1020
```

#### Trường hợp 2 — Có chuyển kiểu

```python
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(x + y)
```

Output:

```text
30
```

---

### Câu hỏi tự kiểm tra 2

### Câu 1

Đoạn code sau in gì nếu người dùng nhập `5`?

```python
x = input("x = ")
print(x * 3)
```

<details>
<summary>Đáp án</summary>

```text
555
```

Vì `x` là chuỗi `"5"`; nhân chuỗi với `3` lặp lại chuỗi ba lần.

</details>

### Câu 2

Muốn kết quả là `15` thì sửa thế nào?

<details>
<summary>Đáp án</summary>

```python
x = int(input("x = "))
print(x * 3)
```

</details>

---

## 7. Mô hình Input → Process → Output

Có thể mô tả cấu trúc của một chương trình nhập/xuất cơ bản bằng ba bước:

```text
Input
  ↓
Process
  ↓
Output
```

Ví dụ: tính diện tích hình chữ nhật.

```python
length = float(input("Length: "))
width = float(input("Width: "))

area = length * width

print("Area:", area)
```

Trong đó:

- `length`, `width`: input;
- `length * width`: process;
- `print(...)`: output.

---

## 8. Định dạng dữ liệu xuất với f-string

F-string cung cấp cách trình bày chuỗi kết hợp với giá trị của biến rõ ràng và thuận tiện.

```python
name = "An"
age = 18

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

Có thể đặt biểu thức bên trong `{}`:

```python
x = 10
y = 5
print(f"{x} + {y} = {x + y}")
```

Output:

```text
10 + 5 = 15
```

### 8.1. Định dạng số thực

```python
price = 19.5678
print(f"Price: {price:.2f}")
```

Output:

```text
Price: 19.57
```

`.2f` nghĩa là hiển thị số thực với 2 chữ số sau dấu thập phân.

---

## 9. Các lỗi thường gặp và cách nhận biết

### 9.1. Quên chuyển kiểu dữ liệu

Sai:

```python
age = input("Age: ")
next_age = age + 1
```

Nguyên nhân:

- `age` là `str`;
- `1` là `int`;
- không thể cộng trực tiếp `str` và `int`.

Sửa:

```python
age = int(input("Age: "))
next_age = age + 1
```

### 9.2. Dữ liệu nhập không phù hợp với kiểu cần chuyển

```python
age = int(input("Age: "))
```

Nếu người dùng nhập `eighteen`, Python không thể chuyển chuỗi đó thành số nguyên.

Trong phạm vi bài học này, giả sử người dùng nhập dữ liệu đúng định dạng được yêu cầu. Kỹ thuật kiểm tra và xử lý dữ liệu nhập không hợp lệ sẽ được giới thiệu ở các bài sau.

### 9.3. Nhầm lẫn giữa biến và chuỗi ký tự

```python
x = 10
print("x")
```

Output:

```text
x
```

Trong khi:

```python
print(x)
```

Output:

```text
10
```

---

## 10. Ví dụ tổng hợp

### Ví dụ 1 — Thông tin cá nhân

```python
name = input("Name: ")
age = int(input("Age: "))

print(f"Hello {name}!")
print(f"Next year you will be {age + 1}.")
```

### Ví dụ 2 — Tính tổng tiền

```python
price = float(input("Product price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print(f"Total: {total:.2f}")
```

### Ví dụ 3 — Chuyển đổi Celsius sang Fahrenheit

Công thức:

$$
F = \frac{9}{5}C + 32
$$

```python
celsius = float(input("Celsius: "))
fahrenheit = 9 / 5 * celsius + 32
print(f"Fahrenheit: {fahrenheit:.2f}")
```

---

## 11. Bài tập dự đoán kết quả (Predict the Output)

### Bài 1

```python
x = "10"
y = "5"
print(x + y)
```

<details>
<summary>Đáp án</summary>

```text
105
```

</details>

### Bài 2

```python
x = 10
y = 5
print("Result:", x + y)
```

<details>
<summary>Đáp án</summary>

```text
Result: 15
```

</details>

### Bài 3

```python
print("A", "B", sep=":", end=" ")
print("C")
```

<details>
<summary>Đáp án</summary>

```text
A:B C
```

</details>

### Bài 4

```python
x = 7
print(f"x = {x}, x^2 = {x * x}")
```

<details>
<summary>Đáp án</summary>

```text
x = 7, x^2 = 49
```

</details>

---

## 12. Bài tập thực hành

> **Yêu cầu chung:** Viết các câu lệnh trực tiếp theo mô hình **Input → Process → Output**; chưa sử dụng hàm tự định nghĩa (`def`).

### Bài 1 — Lời chào

Nhập tên của người dùng và in:

```text
Hello, <name>!
```

### Bài 2 — Tuổi năm sau

Nhập tuổi hiện tại và in tuổi của người dùng vào năm sau.

### Bài 3 — Tổng và tích

Nhập hai số nguyên `a` và `b`. In tổng và tích.

### Bài 4 — Hình chữ nhật

Nhập chiều dài và chiều rộng. Tính và in diện tích và chu vi.

### Bài 5 — Tính tổng tiền mua hàng

Nhập tên sản phẩm, đơn giá và số lượng. In hóa đơn dạng:

```text
Product: Notebook
Unit price: 15.50
Quantity: 3
Total: 46.50
```

### Bài 6 — Chuyển đổi nhiệt độ

Nhập nhiệt độ Celsius và đổi sang Fahrenheit:

$$
F = \frac{9}{5}C + 32
$$

Hiển thị kết quả với 2 chữ số sau dấu thập phân.

### Bài 7 — Tính điểm trung bình

Nhập ba điểm số thực. Tính và in điểm trung bình với 2 chữ số sau dấu thập phân.

### Bài 8 — Chuyển đổi số giây

Nhập một số giây. Tính tổng số phút và số giây còn lại.

Ví dụ:

```text
Seconds: 135
Minutes: 2
Remaining seconds: 15
```

Gợi ý:

```python
//   # chia lấy phần nguyên
%    # chia lấy phần dư
```

---

## 13. Bài thực hành tổng hợp — Tính chi phí chuyến đi

Input:

- quãng đường đi được (km);
- mức tiêu hao nhiên liệu (lít/100 km);
- giá nhiên liệu (đồng/lít).

Tính:

$$
\text{fuel\_used} = \frac{\text{distance} \times \text{consumption}}{100}
$$

$$
\text{cost} = \text{fuel\_used} \times \text{fuel\_price}
$$

Output mẫu:

```text
Distance: 250
Consumption (L/100km): 7.5
Fuel price: 23000

Fuel used: 18.75 L
Estimated cost: 431250.00
```

---

## 14. Tự đánh giá sau bài học

- [ ] Tôi biết sử dụng `print()`.
- [ ] Tôi biết in nhiều giá trị trong một lệnh.
- [ ] Tôi hiểu `sep` và `end`.
- [ ] Tôi biết sử dụng `input()`.
- [ ] Tôi nhớ rằng `input()` trả về `str`.
- [ ] Tôi biết khi nào cần `int()` hoặc `float()`.
- [ ] Tôi có thể viết chương trình Input → Process → Output.
- [ ] Tôi biết sử dụng f-string cơ bản.
- [ ] Tôi có thể định dạng số thực bằng `.2f`.
- [ ] Tôi có thể giải thích lỗi do cộng `str` và `int`.
- [ ] Tôi có thể tự viết các chương trình đơn giản mà không cần `def`.

---

## 15. Tổng kết kiến thức

Các công cụ quan trọng:

```python
print(...)
input(...)
int(...)
float(...)
type(...)
```

Các mẫu thường gặp:

```python
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))
print("Result:", result)
print(f"Result: {result}")
print(f"Result: {result:.2f}")
```

Hãy nhớ:

```text
Input → Process → Output
```

và quy trình học:

> **Predict → Run → Explain → Modify → Practice**
