# Bài 2. Lập trình với số và chuỗi

**Cập nhật lần cuối:** 11 tháng 9, 2026

> **Nguồn:** Chương 2 – *Programming with Numbers and Strings*, trong *Python for Everyone, 3rd Edition* của Cay Horstmann và Rance Necaise.
>
> Bài giảng này giữ nguyên cấu trúc, thuật ngữ, ví dụ và trọng tâm giảng dạy của Chương 2, đồng thời tổ chức lại nội dung để có thể sử dụng trực tiếp trên lớp. Các ví dụ chủ ý tuân theo quy ước của giáo trình, bao gồm cách đặt tên biến và toán tử định dạng chuỗi `%`.

---

## Giới thiệu bài học

Chương 1 giới thiệu khái niệm chương trình máy tính, tổ chức cơ bản của máy tính, môi trường lập trình Python và vai trò của thuật toán. Chương 2 bắt đầu chuyển từ **hiểu chương trình là gì** sang **viết các chương trình có thể thực hiện những phép tính hữu ích**.

Các khối kiến thức chính của chương gồm:

1. **Biến (variables)** để lưu trữ giá trị.
2. **Kiểu dữ liệu số (numeric types)** để biểu diễn số nguyên và số thực.
3. **Biểu thức số học (arithmetic expressions)** để tính toán giá trị mới.
4. **Chuỗi (strings)** để biểu diễn và xử lý văn bản.
5. **Nhập và xuất dữ liệu (input and output)** để giao tiếp với người dùng.
6. **Đồ họa đơn giản (simple graphics)** để tạo các hình vẽ từ các đối tượng hình học và văn bản.

Một tư tưởng xuyên suốt chương là: không nên bắt đầu giải bài toán bằng cách gõ ngay các câu lệnh Python. Quy trình tốt hơn là:

```text
Hiểu bài toán
      ↓
Tính thử một ví dụ cụ thể bằng tay
      ↓
Xác định biến và hằng số
      ↓
Xây dựng phép tính / pseudocode
      ↓
Chuyển lời giải sang Python
      ↓
Chạy, quan sát và cải thiện kết quả
```

---

## Kiến thức và kỹ năng cần đạt

Sau bài học này, sinh viên có thể:

- Định nghĩa và sử dụng **biến** và **hằng số**.
- Giải thích sự khác nhau giữa giá trị kiểu `int` và `float`.
- Sử dụng đúng toán tử gán `=`.
- Chọn tên biến hợp lệ và có ý nghĩa.
- Sử dụng comment để giải thích mục đích của chương trình.
- Viết biểu thức số học với `+`, `-`, `*`, `/`, `//`, `%`, và `**`.
- Giải thích thứ tự ưu tiên toán tử và vai trò của dấu ngoặc.
- Gọi các hàm dựng sẵn như `abs()`, `round()`, `min()`, và `max()`.
- Import và sử dụng các hàm từ module `math`.
- Nhận biết **sai số làm tròn (roundoff errors)** của số thực dấu phẩy động.
- Thực hiện phép tính bằng tay trước khi lập trình.
- Tạo và thao tác với **chuỗi**.
- Sử dụng phép nối chuỗi, lặp chuỗi, chỉ số và các phương thức chuỗi.
- Chuyển đổi giữa chuỗi và số bằng `str()`, `int()`, và `float()`.
- Sử dụng `input()` để nhận dữ liệu từ người dùng.
- Định dạng dữ liệu số và chuỗi bằng toán tử định dạng `%` được sử dụng trong giáo trình.
- Viết các chương trình nhỏ theo cấu trúc **Input → Process → Output**.
- Tạo các hình vẽ đơn giản bằng cửa sổ đồ họa và canvas.
- Phân rã một hình vẽ thành đường thẳng, hình chữ nhật, hình oval và văn bản.

---

## Cấu trúc bài học

1. Biến
2. Số học
3. Giải quyết vấn đề: Trước tiên hãy tính bằng tay
4. Chuỗi
5. Nhập và xuất dữ liệu
6. Đồ họa: Hình vẽ đơn giản
7. Công cụ tùy chọn: Xử lý ký hiệu với SymPy
8. Tổng kết và bài tập

---

# 2.1 Biến

Một chương trình trở nên hữu ích khi nó có thể lưu trữ giá trị, thay đổi các giá trị đó và sử dụng chúng trong các phép tính tiếp theo.

Một **biến (variable)** là một vị trí lưu trữ trong chương trình máy tính. Mỗi biến có:

- một **tên**;
- một **giá trị** hiện đang được lưu tại vị trí đó.

Có thể hình dung biến giống như một chỗ đỗ xe có nhãn:

![Tên biến và giá trị được lưu](image.png)

Tên biến dùng để xác định vị trí lưu trữ; giá trị là nội dung hiện tại của vị trí đó.

---

## 2.1.1 Định nghĩa biến

Một giá trị được lưu vào biến bằng **câu lệnh gán (assignment statement)**.

```python
cansPerPack = 6
```

Dạng tổng quát:

```text
variableName = value
```

Lần đầu tiên một biến được gán giá trị, biến đó được **tạo và khởi tạo**.

```python
cansPerPack = 6
print(cansPerPack)
```

Output:

```text
6
```

Nếu sau đó biến được gán một giá trị khác, giá trị trước sẽ bị thay thế.

```python
cansPerPack = 6
cansPerPack = 8
print(cansPerPack)
```

Output:

```text
8
```

### Phép gán không phải là phép bằng trong toán học

Ký hiệu `=` trong Python là **toán tử gán (assignment operator)**. Nó không mang nghĩa “bằng nhau” như trong toán học.

Xét:

```python
cansPerPack = cansPerPack + 2
```

Nếu `cansPerPack` hiện đang chứa `8`, Python thực hiện:

```text
1. Đọc giá trị hiện tại: 8
2. Tính 8 + 2 = 10
3. Lưu 10 trở lại cansPerPack
```

Sau khi câu lệnh thực thi, về mặt ý nghĩa:

```python
cansPerPack == 10
```

tức là biến hiện chứa giá trị `10`.

Điều này hoàn toàn hợp lý trong lập trình, mặc dù phương trình đại số `x = x + 2` là vô lý nếu hiểu `=` là dấu bằng.

---

## 2.1.2 Kiểu dữ liệu số

Mọi giá trị trong Python đều có một **kiểu dữ liệu (data type)**. Kiểu dữ liệu quyết định:

- cách biểu diễn giá trị;
- các phép toán có thể thực hiện trên giá trị đó.

Hai kiểu số quan trọng:

| Kiểu Python | Ý nghĩa | Ví dụ |
|---|---|---|
| `int` | số nguyên | `6`, `0`, `-25` |
| `float` | số thực dấu phẩy động | `0.355`, `1.0`, `-3.5` |

Ví dụ:

```python
count = 6
price = 2.95
```

Một giá trị số được viết trực tiếp trong chương trình được gọi là **number literal**.

```python
6
0.5
1.0
1E6
2.96E-2
```

Một số điểm cần lưu ý:

- `6` có kiểu `int`.
- `6.0` có kiểu `float`.
- Các số viết bằng ký pháp khoa học như `1E6` là giá trị dấu phẩy động.

Kiểu dữ liệu gắn với **giá trị**, chứ không gắn cố định với tên biến.

```python
taxRate = 5
taxRate = 5.5
```

Python cho phép điều này. Tuy nhiên, giáo trình khuyến nghị giữ kiểu dữ liệu của biến nhất quán về mặt ý nghĩa. Nếu biến biểu diễn thuế suất và có thể nhận giá trị thập phân, nên khởi tạo dưới dạng số thực:

```python
taxRate = 5.0
```

---

## 2.1.3 Tên biến

Tên biến phải tuân theo quy tắc đặt tên của Python.

### Quy tắc

1. Tên phải bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`.
2. Các ký tự tiếp theo có thể là chữ cái, chữ số hoặc dấu gạch dưới.
3. Không được chứa khoảng trắng hoặc ký hiệu như `?`, `%`, `.`, `/`.
4. Tên biến **phân biệt chữ hoa và chữ thường**.
5. Không được dùng các từ khóa dành riêng như `if`, `class`.

Ví dụ:

| Tên | Hợp lệ? | Nhận xét |
|---|---:|---|
| `canVolume1` | Có | Cho phép chữ cái và chữ số |
| `x` | Có | Hợp lệ nhưng thường chưa đủ mô tả |
| `CanVolume` | Có | Khác `canVolume`; không theo quy ước biến viết thường của sách |
| `6pack` | Không | Không được bắt đầu bằng chữ số |
| `can volume` | Không | Không được có khoảng trắng |
| `class` | Không | Từ khóa dành riêng |
| `ltr/fl.oz` | Không | Chứa `/` và `.` |

### Tên có ý nghĩa

So sánh:

```python
cv = 0.355
```

với:

```python
canVolume = 0.355
```

Tên thứ hai giúp người đọc hiểu ngay ý nghĩa của biến.

---

## 2.1.4 Hằng số

Một **hằng số (constant)** là giá trị được dự kiến sẽ không thay đổi trong suốt chương trình.

Python không thực sự ngăn lập trình viên thay đổi hằng số. Thay vào đó, chương này dùng quy ước viết tên hằng bằng chữ in hoa.

```python
BOTTLE_VOLUME = 2.0
MAX_SIZE = 100
```

Hằng có tên giúp chương trình dễ hiểu hơn.

Ít rõ ràng:

```python
totalVolume = bottles * 2
```

Rõ ràng hơn:

```python
BOTTLE_VOLUME = 2.0
totalVolume = bottles * BOTTLE_VOLUME
```

Tên hằng giải thích **vì sao** giá trị `2.0` xuất hiện trong phép tính.

---

## 2.1.5 Comment

**Comment** là phần giải thích dành cho người đọc chương trình.

```python
CAN_VOLUME = 0.355  # Liters in a 12-ounce can
```

Python bỏ qua mọi nội dung từ `#` đến cuối dòng.

Comment ở đầu file có thể giải thích mục đích chương trình:

```python
##
# This program computes the volume, in liters, of a six-pack of soda cans.
#
```

Comment đặc biệt hữu ích để giải thích:

- mục đích của chương trình;
- các hằng số khó hiểu;
- các giả định quan trọng;
- các bước chính của phép tính.

---

## Ví dụ – Tính thể tích nước ngọt

```python
##
# This program computes the volume of a six-pack of soda cans
# and the total volume when a two-liter bottle is added.
#

CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0

cansPerPack = 6
totalVolume = cansPerPack * CAN_VOLUME

print("A six-pack of 12-ounce cans contains", totalVolume, "liters.")

totalVolume = totalVolume + BOTTLE_VOLUME

print("A six-pack and a two-liter bottle contain", totalVolume, "liters.")
```

Về mặt ý nghĩa:

```text
6 lon × 0.355 L/lon = 2.13 L

2.13 L + 2.00 L      = 4.13 L
```

---

# Common Error 2.1 – Sử dụng biến chưa được định nghĩa

Một biến phải được tạo trước khi được sử dụng.

Sai:

```python
canVolume = 12 * literPerOunce
literPerOunce = 0.0296
```

Khi Python thực thi câu lệnh đầu tiên, `literPerOunce` chưa tồn tại.

Do đó Python phát sinh **`NameError`**:

```text
NameError: name 'literPerOunce' is not defined
```

## Vì sao lỗi xảy ra?

Python thực thi câu lệnh **từ trên xuống dưới**.

Tại câu lệnh:

```python
canVolume = 12 * literPerOunce
```

Python cố tìm giá trị hiện tại của `literPerOunce`, nhưng biến này chưa được gán giá trị.

Vì vậy, tên biến đang ở trạng thái **chưa được định nghĩa**.

Đúng:

```python
literPerOunce = 0.0296
canVolume = 12 * literPerOunce
```

Các câu lệnh được thực thi theo thứ tự, vì vậy biến phải được định nghĩa trước khi sử dụng.

---

# Programming Tip 2.1 – Chọn tên biến có ý nghĩa

Nên dùng:

```python
canVolume = 0.355
```

thay vì:

```python
cv = 0.355
```

Tên biến có ý nghĩa giúp giảm công sức suy luận khi đọc chương trình và làm cho code dễ bảo trì hơn.

---

# Programming Tip 2.2 – Không sử dụng magic number

**Magic number** là một số xuất hiện trong code mà không có giải thích rõ ràng.

Ít rõ ràng:

```python
totalVolume = bottles * 2
```

Tốt hơn:

```python
BOTTLE_VOLUME = 2.0
totalVolume = bottles * BOTTLE_VOLUME
```

Sử dụng hằng có tên giúp thay đổi chương trình an toàn hơn. Nếu kích thước chai thay đổi, chỉ cần sửa định nghĩa hằng.

---

## Self Check 2.1

### Câu 1

Điều gì xảy ra khi câu lệnh sau được thực thi lần đầu?

```python
count = 10
```

<details>
<summary>Đáp án</summary>

Một biến tên `count` được tạo và khởi tạo với giá trị nguyên `10`.

</details>

### Câu 2

Giả sử:

```python
x = 7
x = x + 3
```

Sau đó `x` chứa giá trị bao nhiêu?

<details>
<summary>Đáp án</summary>

`10`.

Python trước tiên tính `x + 3`, sau đó lưu kết quả trở lại `x`.

</details>

### Câu 3

Sự khác nhau giữa `6` và `6.0` là gì?

<details>
<summary>Đáp án</summary>

`6` có kiểu `int`; `6.0` có kiểu `float`.

</details>

### Câu 4

Tên nào phù hợp nhất cho một hằng số?

A. `bottleVolume`  
B. `BOTTLE_VOLUME`  
C. `bottle volume`  
D. `2liters`

<details>
<summary>Đáp án</summary>

**B. `BOTTLE_VOLUME`**

Chương này dùng quy ước tên hằng viết bằng chữ in hoa.

</details>

### Câu 5

Vì sao đoạn code sau sai?

```python
result = price * quantity
quantity = 4
```

<details>
<summary>Đáp án</summary>

`quantity` được sử dụng trước khi được tạo và khởi tạo.

</details>

---

# 2.2 Số học

Python có thể được dùng như một máy tính, nhưng các biểu thức số học phải được viết bằng toán tử và cú pháp Python.

---

## 2.2.1 Các phép toán số học cơ bản

Các toán tử cơ bản:

| Phép toán | Toán tử Python | Ví dụ |
|---|---:|---|
| Cộng | `+` | `a + b` |
| Trừ | `-` | `a - b` |
| Nhân | `*` | `a * b` |
| Chia | `/` | `a / b` |

Ví dụ, biểu thức toán học:

$$
\frac{a+b}{2}
$$

được viết trong Python:

```python
(a + b) / 2
```

Sự kết hợp của literal, biến, toán tử và dấu ngoặc được gọi là **biểu thức (expression)**.

### Thứ tự ưu tiên toán tử

Python sử dụng thứ tự ưu tiên gần giống đại số:

1. Dấu ngoặc
2. Lũy thừa
3. Nhân và chia
4. Cộng và trừ

Ví dụ:

```python
a + b / 2
```

Python tính `b / 2` trước.

Để tính trung bình của `a` và `b`:

```python
(a + b) / 2
```

Các toán tử cùng mức ưu tiên thường được thực hiện từ trái sang phải.

```python
10 - 2 - 3
```

được tính như:

```text
(10 - 2) - 3 = 5
```

### Kết hợp `int` và `float`

Nếu một biểu thức chứa cả số nguyên và số thực, kết quả sẽ là số thực.

```python
7 + 4.0
```

Kết quả:

```text
11.0
```

---

## 2.2.2 Lũy thừa

Python sử dụng `**` cho phép lũy thừa.

```python
2 ** 3
```

nghĩa là:

$$
2^3 = 8
$$

Ví dụ:

```python
10 * 2 ** 3
```

Kết quả:

```text
80
```

Lũy thừa có ưu tiên cao hơn phép nhân.

Các phép lũy thừa được tính từ phải sang trái:

```python
10 ** 2 ** 3
```

được hiểu là:

```text
10 ** (2 ** 3)
```

không phải:

```text
(10 ** 2) ** 3
```

Biểu thức toán học:

$$
b\left(1 + \frac{r}{100}\right)^n
$$

được viết:

```python
b * (1 + r / 100) ** n
```

---

## 2.2.3 Chia lấy phần nguyên và phần dư

Phép chia thông thường `/` cho kết quả kiểu số thực.

```python
7 / 4
```

Kết quả:

```text
1.75
```

### Floor division `//`

Với các số nguyên dương, `//` lấy phần nguyên của thương.

```python
7 // 4
```

Kết quả:

```text
1
```

### Phần dư `%`

Toán tử `%` tính phần dư.

```python
7 % 4
```

Kết quả:

```text
3
```

### Ví dụ – Đổi pennies thành dollars và cents

```python
pennies = 1729

dollars = pennies // 100
cents = pennies % 100

print(dollars)
print(cents)
```

Output:

```text
17
29
```

Một số mẫu hữu ích với số nguyên dương `n`:

```python
n % 10       # chữ số cuối
n // 10      # tất cả chữ số trừ chữ số cuối
n % 100      # hai chữ số cuối
n % 2        # 0 nếu chẵn, 1 nếu lẻ
```

---

## 2.2.4 Gọi hàm

Một hàm có thể **trả về giá trị** để sử dụng trong biểu thức, in ra hoặc lưu vào biến.

Ví dụ:

```python
distance = abs(-173)
```

`abs()` trả về giá trị tuyệt đối.

Một số hàm số học dựng sẵn:

| Hàm | Mục đích |
|---|---|
| `abs(x)` | Giá trị tuyệt đối của `x` |
| `round(x)` | Làm tròn `x` về số nguyên |
| `round(x, n)` | Làm tròn `x` đến `n` chữ số thập phân |
| `max(x1, ..., xn)` | Giá trị lớn nhất |
| `min(x1, ..., xn)` | Giá trị nhỏ nhất |

Ví dụ:

```python
print(abs(-10))
print(round(7.627, 2))
print(min(7.25, 10.95, 5.95, 6.05))
```

Hàm phải được gọi với số lượng đối số phù hợp.

Sai:

```python
abs()
abs(-10, 2)
```

Hàm `abs()` yêu cầu đúng một đối số.

---

## 2.2.5 Hàm toán học và module `math`

Thư viện chuẩn của Python chứa nhiều module tái sử dụng.

Module `math` cung cấp nhiều hàm toán học.

Để sử dụng `sqrt()`:

```python
from math import sqrt

y = sqrt(25)
print(y)
```

Output:

```text
5.0
```

Một số hàm thường dùng:

| Hàm | Ý nghĩa |
|---|---|
| `sqrt(x)` | Căn bậc hai |
| `trunc(x)` | Cắt phần thập phân |
| `sin(x)` | Sin của `x`, đơn vị radian |
| `cos(x)` | Cos của `x`, đơn vị radian |
| `tan(x)` | Tan của `x`, đơn vị radian |
| `exp(x)` | $e^x$ |
| `degrees(x)` | Radian → độ |
| `radians(x)` | Độ → radian |
| `log(x)` | Logarithm tự nhiên |
| `log(x, base)` | Logarithm theo cơ số chỉ định |

Module cũng cung cấp các hằng như `pi`.

```python
from math import pi

area = pi * radius ** 2
```

---

# Common Error 2.2 – Sai số làm tròn

Số thực dấu phẩy động không phải lúc nào cũng biểu diễn chính xác giá trị thập phân.

Ví dụ:

```python
price = 4.35
quantity = 100

total = price * quantity
print(total)
```

Máy tính có thể hiển thị giá trị rất gần nhưng không hoàn toàn bằng `435`.

Đây không nhất thiết là lỗi lập trình. Nguyên nhân là nhiều số thập phân không thể biểu diễn chính xác bằng một số hữu hạn chữ số nhị phân.

Khi hiển thị cho người dùng, nên làm tròn hoặc định dạng với số chữ số thập phân cố định.

---

# Common Error 2.3 – Dấu ngoặc không cân bằng

Xét:

```python
((a + b) * t / 2 * (1 - t)
```

Có nhiều dấu ngoặc mở hơn dấu ngoặc đóng.

Quy tắc kiểm tra hữu ích:

- khi đọc từ trái sang phải, số dấu ngoặc đóng không bao giờ được lớn hơn số dấu ngoặc mở;
- khi kết thúc biểu thức, số dấu ngoặc mở và đóng phải bằng nhau.

---

# Programming Tip 2.3 – Sử dụng khoảng trắng trong biểu thức

Nên viết:

```python
x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
```

thay vì:

```python
x1=(-b+sqrt(b**2-4*a*c))/(2*a)
```

Khoảng trắng giúp cấu trúc biểu thức dễ đọc hơn.

---

# Special Topic 2.1 – Các cách import module khác

Import một số hàm:

```python
from math import sqrt, sin, cos
```

Import toàn bộ tên trong module:

```python
from math import *
```

Import module:

```python
import math

y = math.sqrt(x)
```

Cách cuối làm rõ hàm đến từ module nào.

---

# Special Topic 2.2 – Kết hợp phép gán và phép toán

Python cung cấp các toán tử gán kết hợp.

```python
total += cans
```

tương đương:

```python
total = total + cans
```

Tương tự:

```python
total *= 2
count += 1
```

---

# Special Topic 2.3 – Nối dòng

Biểu thức dài có thể tách thành nhiều dòng nếu việc xuống dòng xảy ra bên trong dấu ngoặc.

```python
x1 = ((-b + sqrt(b ** 2 - 4 * a * c))
      / (2 * a))
```

Cách này tốt hơn việc ngắt một biểu thức hoàn chỉnh tại vị trí tùy ý.

---

## Self Check 2.2

### Câu 1

Giá trị của:

```python
10 + 6 / 2
```

là bao nhiêu?

<details>
<summary>Đáp án</summary>

`13.0`

Phép chia được thực hiện trước phép cộng.

</details>

### Câu 2

Kết quả:

```python
17 // 5
17 % 5
```

là gì?

<details>
<summary>Đáp án</summary>

```text
3
2
```

</details>

### Câu 3

Làm thế nào lấy chữ số cuối của số nguyên dương `n`?

<details>
<summary>Đáp án</summary>

```python
n % 10
```

</details>

### Câu 4

Vì sao biểu thức sau khác `(a + b) / 2`?

```python
a + b / 2
```

<details>
<summary>Đáp án</summary>

Vì phép chia có ưu tiên cao hơn phép cộng. Python tính `b / 2` trước rồi mới cộng `a`.

</details>

### Câu 5

Cần import gì trước khi sử dụng `sqrt(x)` theo phong cách giáo trình?

<details>
<summary>Đáp án</summary>

```python
from math import sqrt
```

</details>

---

# 2.3 Giải quyết vấn đề: Trước tiên hãy tính bằng tay

Trước khi chuyển một bài toán thành Python, hãy giải ít nhất một ví dụ cụ thể bằng tay.

Nguyên tắc:

> Nếu bạn không thể tự tính lời giải, rất khó để viết một chương trình đáng tin cậy tự động hóa phép tính đó.

---

## Ví dụ – Xếp gạch xen kẽ dọc theo tường

Giả sử các viên gạch đen và trắng được đặt dọc theo tường với các yêu cầu:

- viên đầu tiên màu đen;
- màu sắc xen kẽ;
- viên cuối cùng cũng phải màu đen.

Giả sử:

```text
Tổng chiều rộng = 100 inch

Chiều rộng gạch = 5 inch
```

Nếu sử dụng 20 viên, viên cuối sẽ màu trắng. Thay vào đó, có thể xem mẫu như:

```text
B | WB | WB | WB | ... | WB
```

Có một viên đen đầu tiên, sau đó là các cặp trắng/đen.

Viên đầu tiên chiếm `5` inch, còn lại `95` inch.

Mỗi cặp chiếm:

```text
2 × 5 = 10 inch
```

Số cặp hoàn chỉnh:

```text
95 // 10 = 9
```

Số viên gạch:

```text
1 + 2 × 9 = 19
```

Gạch chiếm:

```text
19 × 5 = 95 inch
```

Tổng khoảng trống:

```text
100 - 95 = 5 inch
```

Khoảng trống ở mỗi đầu:

```text
5 / 2 = 2.5 inch
```

### Thuật toán tổng quát

```text
số cặp = phần nguyên của
         (tổng chiều rộng - chiều rộng gạch) / (2 × chiều rộng gạch)

số viên = 1 + 2 × số cặp

khoảng trống mỗi đầu =
    (tổng chiều rộng - số viên × chiều rộng gạch) / 2
```

Tính bằng tay giúp làm lộ rõ cấu trúc cần thiết cho thuật toán.

---

# Worked Example 2.1 – Tính thời gian di chuyển

Một robot di chuyển đến một vật thể. Robot có thể đi nhanh hơn trên đường và chậm hơn trên địa hình đá.

Input:

- khoảng cách ngang đến vật thể;
- khoảng cách dọc đến vật thể;
- tốc độ trên đường;
- tốc độ trên địa hình đá;
- chiều dài đoạn đường đầu tiên.

Tổng thời gian gồm hai phần.

### Đoạn 1

```text
time1 = length1 / speed1
```

### Đoạn 2

Đoạn thứ hai là cạnh huyền của tam giác vuông.

$$
\text{segment2Length}
=
\sqrt{(\text{xDistance}-\text{segment1Length})^2 + \text{yDistance}^2}
$$

Sau đó:

```text
time2 = segment2Length / speed2
```

Tổng:

```text
totalTime = time1 + time2
```

Phiên bản Python:

```python
from math import sqrt

segment1Time = segment1Length / segment1Speed

segment2Length = sqrt((xDistance - segment1Length) ** 2 + yDistance ** 2)

segment2Time = segment2Length / segment2Speed

totalTime = segment1Time + segment2Time
```

Ví dụ này đồng thời củng cố việc sử dụng tên biến có ý nghĩa.

---

## Self Check 2.3

### Câu 1

Vì sao lập trình viên nên tính thử một ví dụ cụ thể bằng tay trước khi viết code?

<details>
<summary>Đáp án</summary>

Vì tính bằng tay giúp nhận diện các bước cần thiết và phát hiện lỗi logic trước khi phải xử lý thêm cú pháp Python.

</details>

### Câu 2

Trong ví dụ lát gạch, vì sao floor division hữu ích?

<details>
<summary>Đáp án</summary>

Vì chỉ có thể đặt các cặp gạch hoàn chỉnh. Một phần lẻ của cặp gạch không có ý nghĩa.

</details>

### Câu 3

Thứ tự nào phù hợp hơn?

A. Viết code → đoán thuật toán → kiểm thử  
B. Tính ví dụ → suy ra thuật toán → viết code  
C. Viết code → chọn tên biến → hiểu bài toán

<details>
<summary>Đáp án</summary>

**B.**

</details>

---

# 2.4 Chuỗi

Nhiều chương trình xử lý văn bản thay vì chỉ xử lý số.

Một **chuỗi (string)** là một dãy ký tự.

Ví dụ:

```python
"Hello"
"Python"
"123 Main Street"
```

Ký tự có thể gồm:

- chữ cái;
- chữ số;
- dấu câu;
- khoảng trắng;
- ký hiệu Unicode.

---

## 2.4.1 Kiểu chuỗi

Chuỗi có thể được lưu trong biến.

```python
greeting = "Hello"
print(greeting)
```

**String literal** là chuỗi được viết trực tiếp trong source code.

Python hỗ trợ cả dấu nháy đơn và nháy kép:

```python
"This is a string."
'So is this.'
```

Điều này cho phép dùng một loại dấu nháy bên trong loại còn lại:

```python
message = 'He said "Hello"'
```

### Độ dài chuỗi

Sử dụng `len()` để lấy số ký tự.

```python
length = len("World!")
```

`length` nhận giá trị `6`.

Khoảng trắng cũng được tính là ký tự.

**Chuỗi rỗng (empty string)** chứa 0 ký tự:

```python
""
''
```

---

## 2.4.2 Nối chuỗi và lặp chuỗi

### Nối chuỗi `+`

Toán tử `+` nối các chuỗi.

```python
firstName = "Harry"
lastName = "Morgan"

name = firstName + " " + lastName
```

Kết quả:

```text
Harry Morgan
```

Cả hai toán hạng phải là chuỗi.

Sai:

```python
"Agent " + 1729
```

### Lặp chuỗi `*`

Chuỗi có thể được lặp bằng một số nguyên.

```python
dashes = "-" * 50
```

Ví dụ khác:

```python
message = "Echo. "
print(message * 5)
```

---

## 2.4.3 Chuyển đổi giữa số và chuỗi

### Số → chuỗi

Dùng `str()`.

```python
id = 1729
name = "Agent " + str(id)
```

Kết quả:

```text
Agent 1729
```

### Chuỗi → số nguyên

Dùng `int()`.

```python
id = int("1729")
```

### Chuỗi → số thực

Dùng `float()`.

```python
price = float("17.29")
```

Chuỗi phải có dạng hợp lệ của kiểu số cần chuyển đổi.

---

## 2.4.4 Chuỗi và ký tự

Chuỗi là một dãy ký tự. Mỗi ký tự có một **chỉ số (index)**.

Python bắt đầu đếm từ `0`.

```text
Chuỗi:  H  a  r  r  y
Index:  0  1  2  3  4
```

Với:

```python
name = "Harry"
```

ta có thể truy cập từng ký tự:

```python
first = name[0]
last = name[4]
```

Kết quả:

```text
first = "H"
last  = "y"
```

Chỉ số hợp lệ cuối cùng:

```python
len(name) - 1
```

Cách tổng quát để lấy ký tự cuối:

```python
last = name[len(name) - 1]
```

Dùng chỉ số ngoài phạm vi hợp lệ sẽ gây exception khi chạy.

### Ví dụ – Tạo initials

```python
first = "Rodolfo"
second = "Sally"

initials = first[0] + "&" + second[0]

print(initials)
```

Output:

```text
R&S
```

---

## 2.4.5 Phương thức chuỗi

**Method** là một thao tác gắn với một object.

Với:

```python
name = "John Smith"
```

ta có thể gọi:

```python
uppercaseName = name.upper()
lowercaseName = name.lower()
```

Một số method hữu ích:

| Method | Kết quả |
|---|---|
| `s.lower()` | Phiên bản chữ thường của `s` |
| `s.upper()` | Phiên bản chữ hoa của `s` |
| `s.replace(old, new)` | Chuỗi mới sau khi thay thế |

Ví dụ:

```python
name2 = name.replace("John", "Jane")
```

Kết quả:

```text
Jane Smith
```

Các method này trả về chuỗi mới. Chúng không thay đổi trực tiếp chuỗi ban đầu.

---

# Special Topic 2.4 – Giá trị ký tự

Ký tự được biểu diễn nội bộ bằng các mã số nguyên.

Dùng `ord()` để lấy mã của ký tự:

```python
ord("H")
```

Dùng `chr()` để chuyển mã số về ký tự:

```python
chr(97)
```

Ví dụ:

```python
print("The letter H has code", ord("H"))
print("Code 97 represents", chr(97))
```

---

# Special Topic 2.5 – Escape sequence

**Escape sequence** bắt đầu bằng dấu gạch chéo ngược và biểu diễn một ký tự đặc biệt trong chuỗi.

Ví dụ:

```python
"You're \"Welcome\""
```

```python
"C:\\Temp\\Secret.txt"
```

```python
print("*\n**\n***")
```

Output:

```text
*
**
***
```

Một số escape sequence:

| Escape sequence | Ý nghĩa |
|---|---|
| `\"` | Dấu nháy kép bên trong chuỗi nháy kép |
| `\\` | Dấu gạch chéo ngược |
| `\n` | Xuống dòng |

---

# Computing & Society 2.1 – Bảng chữ cái quốc tế và Unicode

Xử lý văn bản không chỉ giới hạn ở bảng chữ cái tiếng Anh.

Các hệ chữ viết khác nhau gồm:

- bảng chữ cái châu Âu có dấu;
- Hy Lạp;
- Cyrillic;
- Hebrew;
- Arabic;
- chữ Hán;
- hệ chữ viết Nhật Bản và Hàn Quốc;
- biểu tượng và emoji.

**Unicode** cung cấp một hệ mã chung có thể biểu diễn ký tự của các hệ chữ viết trên toàn thế giới.

Chuỗi trong Python 3 hỗ trợ Unicode.

Ví dụ:

```python
text = "£100"
print(text[0])
```

Mỗi vị trí trong chuỗi tương ứng với một ký tự Unicode, không chỉ là một byte ASCII.

---

## Self Check 2.4

### Câu 1

Giá trị của:

```python
len("Hello")
```

là gì?

<details>
<summary>Đáp án</summary>

`5`

</details>

### Câu 2

Giá trị của:

```python
"Py" + "thon"
```

là gì?

<details>
<summary>Đáp án</summary>

```text
Python
```

</details>

### Câu 3

Đoạn sau tạo ra gì?

```python
"-" * 5
```

<details>
<summary>Đáp án</summary>

```text
-----
```

</details>

### Câu 4

Với:

```python
s = "Python"
```

`s[0]` và `s[len(s) - 1]` là gì?

<details>
<summary>Đáp án</summary>

```text
s[0]           → "P"
s[len(s) - 1]  → "n"
```

</details>

### Câu 5

Vì sao đoạn sau thất bại?

```python
"Agent " + 1729
```

<details>
<summary>Đáp án</summary>

Phép nối chuỗi yêu cầu cả hai phía đều là chuỗi. Cần chuyển số nguyên trước:

```python
"Agent " + str(1729)
```

</details>

---

# 2.5 Nhập và xuất dữ liệu

Hầu hết chương trình hữu ích đều nhận dữ liệu từ người dùng và tạo kết quả dựa trên các dữ liệu đó.

Cấu trúc phổ biến:

```text
Input
  ↓
Process
  ↓
Output
```

---

## 2.5.1 Nhập dữ liệu từ người dùng

Dùng `input()` để đọc văn bản từ bàn phím.

```python
first = input("Enter your first name: ")
```

Chuỗi truyền vào `input()` được gọi là **prompt**.

Về mặt ý nghĩa, `input()` thực hiện:

```text
Hiển thị prompt
     ↓
Chờ người dùng nhập
     ↓
Người dùng nhấn Enter
     ↓
Trả về các ký tự đã nhập dưới dạng chuỗi
```

Ví dụ:

```python
first = input("Enter your first name: ")
second = input("Enter your significant other's first name: ")

initials = first[0] + "&" + second[0]

print(initials)
```

---

## 2.5.2 Nhập dữ liệu số

`input()` luôn trả về chuỗi.

Để đọc số nguyên:

```python
userInput = input("Please enter the number of bottles: ")
bottles = int(userInput)
```

Để đọc số thực:

```python
userInput = input("Enter price per bottle: ")
price = float(userInput)
```

Có thể kết hợp:

```python
bottles = int(input("Please enter the number of bottles: "))
price = float(input("Enter price per bottle: "))
```

---

## 2.5.3 Định dạng output

Chương này sử dụng **toán tử định dạng chuỗi `%`** của Python để điều khiển cách hiển thị giá trị.

### Số thực

```python
price = 1.215962441314554

print("%.2f" % price)
```

Output:

```text
1.22
```

### Độ rộng trường

```python
print("%10.2f" % price)
```

Giá trị chiếm trường có độ rộng `10` và được căn phải.

### Một số format specifier

| Specifier | Ý nghĩa |
|---|---|
| `%d` | Số nguyên |
| `%f` | Số thực |
| `%.2f` | Số thực với 2 chữ số sau dấu thập phân |
| `%7.2f` | Độ rộng 7, 2 chữ số thập phân |
| `%s` | Chuỗi |
| `%9s` | Chuỗi căn phải trong trường rộng 9 |
| `%-9s` | Chuỗi căn trái trong trường rộng 9 |
| `%%` | Dấu phần trăm `%` |
| `%+5d` | Hiển thị dấu cho số nguyên dương/âm |

### Định dạng nhiều giá trị

```python
quantity = 24
total = 17.29

print("Quantity: %d Total: %10.2f" % (quantity, total))
```

Các giá trị được ghép với format specifier theo thứ tự từ trái sang phải.

---

## Ví dụ – Giá trên mỗi ounce

```python
##
# This program prints the price per ounce for a six-pack of cans.
#

CANS_PER_PACK = 6

packPrice = float(input("Please enter the price for a six-pack: "))
canVolume = float(input("Please enter the volume for each can (in ounces): "))

packVolume = canVolume * CANS_PER_PACK
pricePerOunce = packPrice / packVolume

print("Price per ounce: %8.2f" % pricePerOunce)
```

Chương trình minh họa đầy đủ mô hình **Input → Process → Output**.

---

# Programming Tip 2.4 – Không trì hoãn việc chuyển kiểu

Khi đọc dữ liệu số, nên chuyển kiểu ngay.

Ít nên dùng:

```python
unitPrice = input("Enter the unit price: ")

price1 = float(unitPrice)
price2 = 12 * float(unitPrice)
```

Tốt hơn:

```python
unitPriceInput = input("Enter the unit price: ")
unitPrice = float(unitPriceInput)

price1 = unitPrice
price2 = 12 * unitPrice
```

Hoặc kết hợp:

```python
unitPrice = float(input("Enter the unit price: "))
```

Chuyển kiểu sớm giúp giảm lặp lại và giảm nguy cơ vô tình dùng chuỗi trong phép tính số học.

---

# HOW TO 2.1 – Viết chương trình đơn giản

Chương này đưa ra phương pháp có hệ thống để chuyển một đề bài thành chương trình Python.

## Bài toán – Máy bán hàng tự động trả tiền thừa

Khách hàng:

- chọn sản phẩm;
- đưa vào một tờ tiền;
- nhận sản phẩm;
- nhận tiền thừa bằng đồng 1 đô-la và quarter.

Giả sử giá sản phẩm là bội số của 25 cent.

---

## Bước 1. Xác định input và output

### Input

- mệnh giá tờ tiền;
- giá sản phẩm tính bằng penny.

### Output

- số đồng 1 đô-la;
- số quarter.

---

## Bước 2. Tính một ví dụ bằng tay

Giả sử:

```text
Tiền đưa vào = $5.00

Giá sản phẩm = $2.25
```

Tiền thừa:

```text
$5.00 - $2.25 = $2.75 = 275 pennies
```

Máy trả:

```text
2 đồng 1 đô-la

3 quarter
```

---

## Bước 3. Viết pseudocode

```text
change due = 100 × bill value - item price

dollar coins = change due // 100

change due = change due % 100

quarters = change due // 25
```

---

## Bước 4. Xác định biến và hằng

Biến:

```text
billValue
itemPrice
changeDue
dollarCoins
quarters
```

Hằng:

```python
PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25
```

Tất cả đều dùng số nguyên vì phép tính sử dụng floor division và remainder.

---

## Bước 5. Chuyển phép tính sang Python

```python
changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice

dollarCoins = changeDue // PENNIES_PER_DOLLAR

changeDue = changeDue % PENNIES_PER_DOLLAR

quarters = changeDue // PENNIES_PER_QUARTER
```

---

## Bước 6. Thêm input và output

```python
billValue = int(input("Enter bill value: "))
itemPrice = int(input("Enter item price in pennies: "))

print("Dollar coins: %6d" % dollarCoins)
print("Quarters:     %6d" % quarters)
```

---

## Bước 7. Ghép thành chương trình hoàn chỉnh

```python
##
# This program simulates a vending machine that gives change.
#

PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

billValue = int(input("Enter bill value: "))
itemPrice = int(input("Enter item price in pennies: "))

changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice

dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue % PENNIES_PER_DOLLAR

quarters = changeDue // PENNIES_PER_QUARTER

print("Dollar coins: %6d" % dollarCoins)
print("Quarters:     %6d" % quarters)
```

Phương pháp tổng quát:

```text
Hiểu bài toán

→ Tính bằng tay

→ Pseudocode

→ Biến / hằng

→ Phép tính Python

→ Input / output

→ Chương trình hoàn chỉnh
```

---

# Worked Example 2.2 – Tính chi phí tem

Một máy bán tem nhận tiền giấy và trả:

- tem thư hạng nhất;
- tem 1 cent làm tiền thừa.

Giả sử giá tem hạng nhất là `49` cent như trong ví dụ của sách.

### Input

- số đô-la đưa vào.

### Output

- số tem hạng nhất;
- số tem 1 cent.

### Tính bằng tay với $1

```text
100 // 49 = 2 tem hạng nhất

100 - 2 × 49 = 2 cent tiền thừa
```

### Phép tính tổng quát

```python
FIRST_CLASS_STAMP_PRICE = 49

firstClassStamps = 100 * dollars // FIRST_CLASS_STAMP_PRICE

change = 100 * dollars - firstClassStamps * FIRST_CLASS_STAMP_PRICE
```

Ví dụ hoàn chỉnh:

```python
FIRST_CLASS_STAMP_PRICE = 49

dollars = int(input("Enter number of dollars: "))

firstClassStamps = 100 * dollars // FIRST_CLASS_STAMP_PRICE

change = 100 * dollars - firstClassStamps * FIRST_CLASS_STAMP_PRICE

print("First class stamps: %6d" % firstClassStamps)
print("Penny stamps:       %6d" % change)
```

Ví dụ này củng cố:

- hằng có tên;
- số học số nguyên;
- floor division;
- chuyển đổi input;
- định dạng output.

---

# Computing & Society 2.2 – Lỗi trong phần cứng silicon

Không phải mọi kết quả số sai đều do lập trình viên ứng dụng gây ra.

Chương này thảo luận về **lỗi chia dấu phẩy động Pentium (Pentium floating-point division bug)**. Một khiếm khuyết trong phần cứng CPU khiến một số rất ít phép chia số thực cho kết quả không chính xác.

Bài học tổng quát:

- phần mềm phụ thuộc vào phần cứng;
- phần cứng cũng có thể chứa lỗi;
- tính toán số phụ thuộc vào các chuẩn và cách triển khai được thiết kế cẩn thận;
- kiểm thử có thể phát hiện vấn đề ở nhiều lớp khác nhau của hệ thống tính toán.

Chương này cũng nhắc đến các vấn đề bảo mật CPU về sau liên quan đến speculative execution, cho thấy các tối ưu hóa phức tạp có thể tạo ra rủi ro không mong muốn.

---

## Self Check 2.5

### Câu 1

`input()` trả về kiểu dữ liệu nào?

<details>
<summary>Đáp án</summary>

Chuỗi (`str`).

</details>

### Câu 2

Làm thế nào đọc trực tiếp một số nguyên từ input của người dùng?

<details>
<summary>Đáp án</summary>

```python
value = int(input("Enter a value: "))
```

</details>

### Câu 3

`%.2f` có ý nghĩa gì trong cú pháp định dạng của chương?

<details>
<summary>Đáp án</summary>

Hiển thị một giá trị số thực với hai chữ số sau dấu thập phân.

</details>

### Câu 4

Vì sao nên chuyển kiểu dữ liệu số ngay sau khi đọc input?

<details>
<summary>Đáp án</summary>

Để tránh chuyển đổi lặp lại và giảm khả năng vô tình sử dụng chuỗi trong phép tính số học.

</details>

### Câu 5

Những toán tử nào đặc biệt hữu ích khi tính tiền thừa bằng các đơn vị tiền nguyên?

<details>
<summary>Đáp án</summary>

Floor division `//` và remainder `%`.

</details>

---

# TOOLBOX 2.1 – Xử lý ký hiệu với SymPy

Phần tùy chọn này minh họa hệ sinh thái Python rộng lớn hơn.

**SymPy** là package dùng cho toán học ký hiệu. Thay vì chỉ tính giá trị số, SymPy có thể thao tác trực tiếp trên biểu thức toán học.

Thiết lập thường dùng:

```python
from sympy import *
```

Tạo biểu thức ký hiệu:

```python
f = sympify("x ** 2 * sin(x)")
```

SymPy có thể thực hiện:

### Khai triển biểu thức

```python
expand((x - 1) * (x + 1))
```

### Giải phương trình

```python
solve(x ** 2 + 2 * x - 8)
```

### Đạo hàm

```python
diff(f)
```

### Tích phân

```python
g = integrate(f)
```

### Thay thế và tính giá trị số

```python
result = g.subs(x, 0).evalf()
```

### Vẽ đồ thị

```python
plot(x ** 2)
```

Mục tiêu chính không phải ghi nhớ mọi lệnh SymPy, mà là nhận ra rằng các package Python cung cấp những chức năng chuyên biệt có thể tái sử dụng trong chương trình.

---

# Tổng kết Chương 2

## Biến

- Biến là một vị trí lưu trữ có tên.
- Phép gán lưu giá trị vào biến.
- Biến được tạo khi được gán lần đầu.
- Gán lại sẽ thay thế giá trị cũ.
- `=` là phép gán, không phải dấu bằng toán học.
- Các kiểu số quan trọng gồm `int` và `float`.
- Nên dùng tên biến có ý nghĩa.
- Theo quy ước của chương, dùng chữ in hoa cho hằng.
- Dùng comment để giải thích ý định của chương trình.

## Số học

Các toán tử quan trọng:

```python
+  -  *  /  //  %  **
```

Ghi nhớ:

```text
/   → chia thông thường

//  → chia lấy phần nguyên

%   → phần dư

**  → lũy thừa
```

Các hàm hữu ích:

```python
abs()
round()
min()
max()
```

Module `math` cung cấp:

```python
sqrt()
sin()
cos()
log()
```

## Giải quyết vấn đề

Trước khi viết code:

```text
Chọn giá trị cụ thể

→ giải bằng tay

→ xác định mẫu tổng quát

→ viết thuật toán

→ chuyển sang Python
```

## Chuỗi

- Chuỗi là dãy ký tự.
- `len()` trả về độ dài chuỗi.
- `+` nối chuỗi.
- `*` lặp chuỗi.
- `str()`, `int()`, `float()` thực hiện chuyển đổi.
- Chỉ số chuỗi bắt đầu từ `0`.
- Các method như `upper()`, `lower()`, `replace()` trả về chuỗi mới.

## Input và Output

- `input()` trả về chuỗi.
- Chuyển input số bằng `int()` hoặc `float()`.
- Nên chuyển kiểu càng sớm càng tốt sau khi đọc input.
- Chương này dùng toán tử định dạng `%` để điều khiển cách trình bày output.

## Đồ họa

- Tạo cửa sổ đồ họa.
- Lấy canvas.
- Vẽ hình và văn bản lên canvas.
- Gốc tọa độ nằm ở góc trên bên trái.
- Màu có thể đặt bằng tên hoặc thành phần RGB.

---

# Quiz tổng hợp

## Câu 1

Câu lệnh gán làm gì?

A. Kiểm tra bằng nhau  
B. Lưu một giá trị vào biến  
C. In một giá trị  
D. Tạo comment

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 2

Giá trị nào có kiểu `float`?

A. `6`  
B. `0`  
C. `6.0`  
D. `-4`

<details>
<summary>Đáp án</summary>

**C**

</details>

## Câu 3

Kết quả của:

```python
17 // 5
```

là:

A. `2`  
B. `3`  
C. `3.4`  
D. `5`

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 4

Kết quả của:

```python
17 % 5
```

là:

A. `2`  
B. `3`  
C. `5`  
D. `17`

<details>
<summary>Đáp án</summary>

**A**

</details>

## Câu 5

Biểu thức sau tạo ra gì?

```python
"Py" + "thon"
```

<details>
<summary>Đáp án</summary>

```text
Python
```

</details>

## Câu 6

Với:

```python
s = "Hello"
```

`s[1]` là:

A. `"H"`  
B. `"e"`  
C. `"l"`  
D. Lỗi

<details>
<summary>Đáp án</summary>

**B. `"e"`**

</details>

## Câu 7

`input()` trả về kiểu nào?

A. Luôn là `int`  
B. Luôn là `float`  
C. `str`  
D. Phụ thuộc nội dung người dùng nhập

<details>
<summary>Đáp án</summary>

**C. `str`**

</details>

## Câu 8

Câu lệnh nào đọc một số thực từ người dùng?

A. `price = input()`  
B. `price = float(input("Price: "))`  
C. `price = str(input())`  
D. `price = print(input())`

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 9

Lý do tốt nhất để dùng hằng có tên là gì?

A. Luôn làm chương trình chạy nhanh hơn  
B. Giúp giá trị số dễ hiểu và dễ thay đổi hơn  
C. Ngăn Python thay đổi giá trị  
D. Thay thế hoàn toàn comment

<details>
<summary>Đáp án</summary>

**B**

</details>

## Câu 10

Trước khi chuyển một phép tính không đơn giản sang Python, nên làm gì?

A. Chọn cú pháp ngẫu nhiên  
B. Tính thử ít nhất một ví dụ bằng tay  
C. Cài package đồ họa  
D. Chuyển mọi giá trị thành chuỗi

<details>
<summary>Đáp án</summary>

**B**

</details>

---

# Bài tập ôn tập

## Bài 1. Theo dõi phép gán

Xác định giá trị cuối cùng của `mystery`:

```python
mystery = 1
mystery = 1 - 2 * mystery
mystery = mystery + 1
```

<details>
<summary>Đáp án</summary>

```text
Ban đầu: mystery = 1

Câu lệnh 2: mystery = 1 - 2 × 1 = -1

Câu lệnh 3: mystery = -1 + 1 = 0
```

Giá trị cuối: `0`.

</details>

---

## Bài 2. Chuyển biểu thức toán học sang Python

Viết biểu thức Python cho:

1. Trung bình của `a` và `b`.
2. $a^2+b^2$.
3. $\sqrt{x^2+y^2}$.
4. $PV(1+r/100)^n$.

<details>
<summary>Đáp án tham khảo</summary>

```python
(a + b) / 2

a ** 2 + b ** 2

sqrt(x ** 2 + y ** 2)

PV * (1 + r / 100) ** n
```

</details>

---

## Bài 3. Floor division và remainder

Cho:

```python
n = 1729
```

Dự đoán:

```python
n % 10
n // 10
n % 100
n % 2
```

<details>
<summary>Đáp án</summary>

```text
9
172
29
1
```

</details>

---

## Bài 4. Biểu thức chuỗi

Cho:

```python
s = "Hello"
t = "World"
```

Tìm giá trị:

```python
len(s) + len(t)

s[1] + s[2]

s[len(s) // 2]

s + t

t + s

s * 2
```

<details>
<summary>Đáp án</summary>

```text
10
el
l
HelloWorld
WorldHello
HelloHello
```

</details>

---

## Bài 5. Giải thích sự khác nhau

Giải thích sự khác nhau giữa:

```text
2
2.0
'2'
"2"
"2.0"
```

<details>
<summary>Đáp án</summary>

- `2` là số nguyên.
- `2.0` là số thực.
- `'2'` và `"2"` là chuỗi chứa một ký tự.
- `"2.0"` là chuỗi chứa ba ký tự.

</details>

---

## Bài 6. Sai số làm tròn

Xét:

```python
purchase = 19.93
payment = 20.00

change = payment - purchase

print(change)
```

Giải thích vì sao có thể nhận được kết quả như:

```text
0.07000000000000028
```

<details>
<summary>Đáp án</summary>

Nhiều số thập phân không thể biểu diễn chính xác bằng dạng nhị phân dấu phẩy động. Các giá trị gần đúng bên trong máy tính có thể tạo ra sai khác số rất nhỏ. Khi hiển thị tiền, nên định dạng hoặc làm tròn kết quả.

</details>

---

# Bài tập thực hành

## Bài 1. Kích thước giấy

Một tờ giấy letter-size có kích thước `8.5 × 11` inch. Có `25.4` millimeter trong một inch.

Viết chương trình hiển thị kích thước theo millimeter. Sử dụng hằng có tên và comment.

---

## Bài 2. Lũy thừa của một số

Đọc một số và hiển thị:

- bình phương;
- lập phương;
- lũy thừa bậc bốn.

Chỉ dùng `**` cho lũy thừa bậc bốn.

---

## Bài 3. Hai số nguyên

Đọc hai số nguyên và in:

- tổng;
- hiệu;
- tích;
- trung bình;
- trị tuyệt đối của hiệu;
- giá trị lớn nhất;
- giá trị nhỏ nhất.

---

## Bài 4. Tách số nguyên năm chữ số

Đọc một số nguyên dương có năm chữ số và hiển thị từng chữ số riêng.

Ví dụ:

```text
Input: 16384

Output: 1 6 3 8 4
```

Sử dụng floor division và remainder.

---

## Bài 5. Ký tự đầu, giữa và cuối

Đọc một từ và in:

- ký tự đầu;
- ký tự cuối;
- ký tự ở giữa.

Nếu từ có độ dài chẵn, dùng ký tự ngay trước vị trí giữa.

---

## Bài 6. Monogram

Đọc tên ba phần, ví dụ:

```text
Harold James Morgan
```

và hiển thị:

```text
HJM
```

Hãy viết pseudocode trước khi viết Python.

---

## Bài 7. Máy bán hàng tự động

Điều chỉnh thuật toán máy bán hàng để trả tiền thừa bằng:

- quarter;
- dime;
- nickel.

Giả sử giá sản phẩm là bội số của `5` cent.

---

## Bài 8. Nhiệt độ và điểm sương

Sử dụng công thức và các hằng do giảng viên hoặc giáo trình cung cấp, viết chương trình đọc nhiệt độ và độ ẩm tương đối rồi tính gần đúng điểm sương.

Tập trung vào:

- import `log` từ `math`;
- chuyển công thức toán học sang Python chính xác;
- sử dụng dấu ngoặc đúng.

---

# Bài tập mở

## Bài 1

Đưa ra ba ví dụ về **magic number** có thể xuất hiện trong một chương trình kinh doanh thực tế. Thay mỗi giá trị bằng một hằng có tên phù hợp.

## Bài 2

Giải thích vì sao `=` trong Python nên được đọc là “gán” thay vì “bằng”. Đưa ra một ví dụ hợp lệ trong Python nhưng vô lý nếu hiểu như phương trình đại số.

## Bài 3

Chọn một đại lượng trong đời sống phù hợp với:

- floor division;
- remainder.

Mô tả một chương trình sử dụng cả hai toán tử.

Ví dụ:

- đổi giây thành phút và giây;
- đổi cent thành đô-la và cent;
- đóng gói vật phẩm vào các hộp đầy.

## Bài 4

Chọn một chuỗi ngắn và liệt kê từng ký tự cùng chỉ số của nó.

---

# Thuật ngữ chính

| Thuật ngữ | Ý nghĩa |
|---|---|
| Variable | Vị trí lưu trữ có tên |
| Assignment | Lưu giá trị vào biến |
| Assignment operator | Toán tử `=` |
| Initialization | Gán giá trị đầu tiên cho biến |
| Data type | Quyết định cách biểu diễn và các phép toán hợp lệ |
| `int` | Kiểu số nguyên |
| `float` | Kiểu số thực |
| Literal | Giá trị viết trực tiếp trong source code |
| Variable name | Tên dùng để tham chiếu đến biến |
| Constant | Giá trị dự kiến không thay đổi |
| Magic number | Giá trị số không được giải thích trong code |
| Comment | Giải thích dành cho người đọc, Python bỏ qua |
| Operator | Ký hiệu thực hiện phép toán |
| Expression | Kết hợp của giá trị, biến, toán tử và lời gọi hàm |
| Precedence | Quy tắc quyết định thứ tự tính |
| Exponentiation | Phép lũy thừa `**` |
| Floor division | Phép chia với `//` |
| Modulus / remainder | Phép `%` |
| Function | Thao tác tái sử dụng có thể nhận đối số và trả về giá trị |
| Standard library | Tập hợp module chuẩn có sẵn |
| Module | Nhóm hàm và định nghĩa dữ liệu liên quan |
| Roundoff error | Sai số nhỏ do biểu diễn dấu phẩy động hữu hạn |
| String | Dãy ký tự |
| String literal | Chuỗi viết trực tiếp trong source code |
| Concatenation | Nối chuỗi bằng `+` |
| Repetition | Lặp chuỗi bằng `*` |
| Index | Vị trí của ký tự trong chuỗi |
| Method | Thao tác gắn với object |
| Escape sequence | Chuỗi bắt đầu bằng backslash biểu diễn ký tự đặc biệt |
| Unicode | Chuẩn mã hóa ký tự cho các hệ chữ viết toàn cầu |
| Prompt | Lời nhắc cho biết dữ liệu cần nhập |
| Input | Dữ liệu đưa vào chương trình |
| Output | Kết quả do chương trình tạo ra |
| Format specifier | Mẫu điều khiển cách biểu diễn output |
| Canvas | Vùng vẽ bên trong cửa sổ đồ họa |
| RGB | Biểu diễn màu đỏ-lục-lam |
| Bounding box | Hình chữ nhật dùng để định vị oval hoặc đối tượng khác |

---

# Hướng dẫn học tập

Sau Chương 2, sinh viên cần có khả năng viết các chương trình nhỏ để xử lý dữ liệu số và văn bản. Điều quan trọng nhất không phải là ghi nhớ cú pháp rời rạc, mà là tuân theo một quy trình có kỷ luật:

```text
Hiểu nhiệm vụ

→ chọn biến và hằng có ý nghĩa

→ tính một ví dụ bằng tay

→ viết phép tính rõ ràng

→ nhận input

→ chuyển về đúng kiểu dữ liệu

→ xử lý dữ liệu

→ định dạng và hiển thị output

→ kiểm thử bằng giá trị đơn giản

→ quan sát kết quả bất thường

→ cải thiện chương trình
```

Một chu trình luyện tập hữu ích:

> **Dự đoán → Tính bằng tay → Viết → Chạy → Giải thích → Điều chỉnh → Thực hành**
