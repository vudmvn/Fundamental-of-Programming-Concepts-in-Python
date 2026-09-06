# Tutorial/Lab: Sử dụng ChatGPT để học và tự học Python hiệu quả

## 1. Giới thiệu

Các công cụ AI tạo sinh như **ChatGPT** có thể hỗ trợ rất tốt trong quá trình học lập trình Python. Tuy nhiên, hiệu quả học tập phụ thuộc rất lớn vào **cách người học sử dụng AI**.

Nếu chỉ yêu cầu:

```text
Giải bài này cho tôi.
```

người học có thể nhanh chóng nhận được một đoạn chương trình hoàn chỉnh, nhưng lại không hiểu:

- Bài toán được phân tích như thế nào?
- Vì sao sử dụng câu lệnh đó?
- Tại sao chương trình đúng?
- Khi bài toán thay đổi thì cần sửa chương trình ở đâu?
- Làm thế nào để tự viết một chương trình tương tự?

Trong tutorial/lab này, ChatGPT được sử dụng như một **trợ giảng cá nhân (AI tutor)** để:

- giải thích kiến thức;
- tạo hoặc tái cấu trúc lecture note;
- tạo quiz và self-check;
- cung cấp ví dụ;
- đặt câu hỏi kiểm tra;
- đưa ra gợi ý khi gặp khó khăn;
- hỗ trợ tìm lỗi;
- đánh giá lời giải;
- tạo thêm bài tập tự luyện.

> **Nguyên tắc quan trọng:**  
> Hãy sử dụng AI để **học cách giải bài toán**, không chỉ để **lấy lời giải của bài toán**.

---

## 2. Mục tiêu học tập

Sau khi hoàn thành bài lab, sinh viên có thể:

1. Sử dụng ChatGPT để giải thích một khái niệm Python chưa hiểu.
2. Viết prompt cung cấp đủ ngữ cảnh cho AI.
3. Yêu cầu AI đưa ra **gợi ý thay vì lời giải hoàn chỉnh**.
4. Sử dụng AI để kiểm tra cách hiểu của bản thân.
5. Sử dụng AI để hỗ trợ tìm lỗi trong chương trình Python.
6. Kiểm tra và đánh giá câu trả lời do AI cung cấp.
7. Sử dụng AI để tạo bài tập tự luyện.
8. Sử dụng AI để tạo quiz tự kiểm tra.
9. Sử dụng AI để tạo hoặc tái cấu trúc lecture note.
10. Xây dựng một quy trình tự học Python với sự hỗ trợ của AI.

---

## 3. Chuẩn bị

Sinh viên cần:

- trình duyệt web;
- tài khoản ChatGPT;
- Google Colab hoặc môi trường chạy Python;
- tài liệu bài giảng nếu có;
- kiến thức Python cơ bản.

Trong các ví dụ đầu tiên, chúng ta chủ yếu sử dụng:

- biến;
- kiểu dữ liệu;
- toán tử;
- `print()`;
- `input()`;
- biểu thức Python.

Không yêu cầu sinh viên phải biết viết hàm.

---

## 4. AI nên đóng vai trò gì trong quá trình học Python?

Một cách sử dụng ChatGPT hiệu quả là xem AI như một **gia sư cá nhân**.

Thay vì:

```text
Tôi không biết làm bài này. Hãy viết code cho tôi.
```

hãy thử:

```text
Tôi đang học Python cơ bản.

Tôi chưa muốn xem lời giải hoàn chỉnh.

Hãy:
1. Giải thích bài toán.
2. Cho tôi một gợi ý đầu tiên.
3. Đợi tôi thử làm.
```

Một quy trình học phù hợp là:

```text
Đọc kiến thức
      ↓
Tự giải thích lại
      ↓
Hỏi AI những phần chưa hiểu
      ↓
Tự viết chương trình
      ↓
Chạy thử chương trình
      ↓
Nhờ AI gợi ý nếu gặp khó khăn
      ↓
Sửa chương trình
      ↓
Nhờ AI review
      ↓
Làm quiz
      ↓
Làm bài tương tự
```

---

## 5. Một prompt tốt cần có gì?

Một prompt học lập trình tốt thường gồm bốn thành phần:

```text
[Ngữ cảnh]

[Điều tôi chưa hiểu]

[AI cần làm gì]

[Cách tôi muốn AI trả lời]
```

Ví dụ:

```text
Tôi là sinh viên mới bắt đầu học Python.

Tôi đang học về biến nhưng chưa hiểu sự khác nhau giữa
biến và giá trị được gán cho biến.

Hãy giải thích cho tôi bằng một ví dụ đơn giản.

Sau phần giải thích, hãy cho tôi 3 câu hỏi nhỏ để kiểm tra
xem tôi đã hiểu chưa.

Không đưa đáp án ngay.
```

So với:

```text
Biến Python là gì?
```

prompt trên giúp AI biết:

- trình độ người học;
- nội dung đang học;
- phần chưa hiểu;
- cách giải thích mong muốn;
- cách kiểm tra sau khi học.

---

## 6. Kỹ thuật 1 — Nhờ AI giải thích kiến thức

Giả sử sinh viên chưa hiểu:

```python
x = 10
```

Có thể hỏi:

```text
Tôi mới học Python.

Hãy giải thích câu lệnh:

x = 10

Giải thích:
- x là gì?
- 10 là gì?
- dấu = có nghĩa gì?
- máy tính thực hiện câu lệnh này như thế nào?

Sử dụng ngôn ngữ đơn giản và một phép so sánh trong đời sống.
```

Sau khi đọc, tiếp tục:

```text
Bây giờ hãy đặt cho tôi 3 câu hỏi để kiểm tra xem tôi
thực sự hiểu x = 10 hay chưa.

Không cho đáp án trước.
```

### Thực hành 1

Sử dụng ChatGPT để tìm hiểu một trong các khái niệm:

- biến;
- kiểu dữ liệu;
- toán tử;
- `print()`;
- `input()`.

Prompt phải có:

- trình độ hiện tại;
- khái niệm cần học;
- yêu cầu ví dụ;
- yêu cầu kiểm tra lại kiến thức.

---

## 7. Kỹ thuật 2 — Sử dụng AI để kiểm tra cách hiểu

Một phương pháp học hiệu quả là:

> **Tự giải thích trước — nhờ AI kiểm tra sau.**

Ví dụ:

```text
Theo tôi hiểu, input() lấy dữ liệu người dùng nhập từ bàn phím
và luôn trả về dữ liệu kiểu chuỗi.

Hãy kiểm tra cách hiểu của tôi.

Nếu có điểm nào sai:
- chỉ ra điểm sai;
- giải thích tại sao;
- cho một ví dụ nhỏ.
```

### Thực hành 2

Tự giải thích:

```python
age = input("Enter your age: ")
```

Sau đó yêu cầu ChatGPT kiểm tra cách hiểu của bạn.

---

## 8. Kỹ thuật 3 — Dự đoán kết quả trước khi chạy chương trình

Có thể yêu cầu AI tạo bài tập **Predict the Output**:

```text
Tôi đang học Python cơ bản về biến, toán tử và print().

Hãy cho tôi 5 đoạn chương trình ngắn để tôi dự đoán kết quả.

Yêu cầu:
- mỗi đoạn tối đa 5 dòng;
- chưa sử dụng vòng lặp;
- chưa sử dụng hàm tự định nghĩa;
- không cho đáp án ngay;
- độ khó tăng dần.
```

Ví dụ:

```python
x = 5
y = 3
x = x + y
print(x)
```

Quy trình:

1. Tự dự đoán.
2. Ghi lại đáp án.
3. Chạy code.
4. So sánh.
5. Giải thích nguyên nhân nếu dự đoán sai.

---

## 9. Kỹ thuật 4 — Xin gợi ý thay vì xin lời giải

Bài toán:

> Nhập chiều dài và chiều rộng hình chữ nhật.  
> In diện tích và chu vi.

Thay vì:

```text
Viết code Python giải bài này.
```

hãy hỏi:

```text
Tôi cần tự giải bài tập Python sau:

"Nhập chiều dài và chiều rộng của hình chữ nhật.
In diện tích và chu vi."

Tôi đang học input, biến, toán tử và print.

Không viết lời giải hoàn chỉnh.

Hãy đặt cho tôi các câu hỏi để tôi tự xác định:
1. cần nhập những dữ liệu nào;
2. cần những biến nào;
3. cần những công thức nào;
4. cần in những kết quả nào.
```

---

## 10. Hệ thống gợi ý 3 cấp độ

### Hint 1 — Gợi ý ý tưởng

Không chứa code.

### Hint 2 — Gợi ý cấu trúc

Cho biết nên dùng kiến thức hoặc câu lệnh nào.

### Hint 3 — Gợi ý gần lời giải

Có thể chứa một phần code nhưng chưa đưa toàn bộ lời giải.

Ví dụ:

```text
Tôi vẫn chưa làm được.

Hãy cho tôi Hint 2.

Không đưa lời giải hoàn chỉnh.
```

---

## 11. Kỹ thuật 5 — Debug chương trình cùng AI

Ví dụ:

```python
age = input("Enter age: ")
next_age = age + 1
print(next_age)
```

Prompt tốt:

```text
Tôi mới học Python.

Đây là chương trình của tôi:

age = input("Enter age: ")
next_age = age + 1
print(next_age)

Chương trình báo lỗi.

Không sửa toàn bộ ngay.

Hãy:
1. giải thích nguyên nhân lỗi;
2. chỉ ra dòng gây lỗi;
3. đặt một câu hỏi gợi ý để tôi tự sửa.
```

---

## 12. Đọc thông báo lỗi với ChatGPT

Khi hỏi AI về lỗi, nên cung cấp:

```text
1. Code
2. Error message
3. Kết quả mong đợi
4. Kết quả thực tế
```

Template:

```text
Tôi đang học Python cơ bản.

Code:

[CODE]

Error:

[ERROR MESSAGE]

Tôi muốn chương trình:

[MÔ TẢ]

Hãy giải thích lỗi cho người mới học.

Không đưa lời giải hoàn chỉnh ngay.
```

---

## 13. Kỹ thuật 6 — Nhờ AI review code

Ví dụ:

```text
Đây là chương trình tôi tự viết:

length = float(input("Length: "))
width = float(input("Width: "))

area = length * width
perimeter = 2 * (length + width)

print(area)
print(perimeter)

Hãy review code của tôi.

Cho biết:
1. chương trình có đúng không;
2. tên biến có dễ hiểu không;
3. có dòng nào dư thừa không;
4. có thể làm code dễ đọc hơn như thế nào.

Không sử dụng kiến thức Python nâng cao.
```

---

## 14. Kỹ thuật 7 — Nhờ AI đóng vai giáo viên

Prompt:

```text
Hãy đóng vai giáo viên Python của tôi.

Chủ đề: biến và kiểu dữ liệu.

Quy trình:

1. Hỏi tôi một câu.
2. Đợi tôi trả lời.
3. Nhận xét câu trả lời.
4. Nếu tôi sai, giải thích ngắn gọn.
5. Sau đó hỏi câu tiếp theo.

Bắt đầu từ dễ và tăng dần độ khó.

Không cho nhiều câu cùng lúc.
```

Đây là cách biến ChatGPT thành một **AI tutor tương tác**.

---

## 15. Kỹ thuật 8 — Sử dụng AI để tạo bài tập tự luyện

Prompt:

```text
Tôi vừa hoàn thành bài:

"Nhập bán kính và tính diện tích hình tròn."

Hãy tạo cho tôi 5 bài tập tương tự để luyện:
- input();
- biến;
- phép toán;
- print().

Không sử dụng:
- if;
- loop;
- list;
- function.

Không đưa lời giải.
```

---

## 16. Kỹ thuật 9 — Sử dụng AI để tạo Quiz

ChatGPT có thể được sử dụng để tạo quiz giúp kiểm tra kiến thức ngay sau khi học.

Không nên chỉ yêu cầu:

```text
Tạo quiz Python.
```

Prompt nên chỉ rõ:

- chủ đề;
- trình độ;
- loại câu hỏi;
- số lượng;
- kiến thức được phép sử dụng;
- cách cung cấp đáp án.

### 16.1. Tạo quiz trắc nghiệm

```text
Tôi là sinh viên mới bắt đầu học Python.

Hãy tạo 10 câu hỏi trắc nghiệm về:
- biến;
- kiểu dữ liệu;
- print();
- input();
- toán tử số học.

Yêu cầu:
- mỗi câu có 4 lựa chọn A, B, C, D;
- chỉ có một đáp án đúng;
- chưa sử dụng if, loop, list hoặc function;
- không hiển thị đáp án ngay;
- độ khó tăng dần.
```

Sau khi hoàn thành:

```text
Đây là đáp án của tôi:

1A
2C
3B
...

Hãy:
1. chấm điểm;
2. chỉ ra câu sai;
3. giải thích ngắn gọn;
4. xác định chủ đề tôi còn yếu.
```

### 16.2. Quiz dạng Predict the Output

```text
Hãy tạo 5 câu quiz Python dạng Predict the Output.

Chủ đề:
- variables;
- assignment;
- arithmetic operators;
- print().

Mỗi đoạn code từ 2 đến 5 dòng.

Không hiển thị đáp án trước.
```

### 16.3. Quiz dạng Find the Bug

```text
Tạo 5 câu quiz "Find the Bug" dành cho sinh viên mới học Python.

Mỗi câu gồm một đoạn code ngắn có đúng một lỗi.

Chủ đề:
- input;
- type conversion;
- variable;
- arithmetic;
- print.

Không cung cấp đáp án ngay.
```

### 16.4. Quiz dạng giải thích khái niệm

```text
Hãy kiểm tra tôi bằng 5 câu hỏi ngắn về Python.

Không dùng trắc nghiệm.

Tôi phải tự giải thích bằng lời.

Mỗi lần chỉ hỏi một câu.
Sau mỗi câu trả lời:
- đánh giá câu trả lời;
- bổ sung phần tôi còn thiếu;
- sau đó hỏi câu tiếp theo.
```

### 16.5. Tạo quiz dựa trên lỗi của chính người học

```text
Trong các bài vừa làm, tôi đã mắc các lỗi sau:

1. Quên chuyển kết quả input() sang int.
2. Nhầm giữa = và phép so sánh.
3. Không hiểu x = x + 1.

Hãy tạo cho tôi 6 câu quiz tập trung vào đúng các lỗi này.

Không cung cấp đáp án trước.
```

### Thực hành 3 — Tạo quiz cá nhân

Chọn một chủ đề Python đã học.

Yêu cầu ChatGPT tạo:

- 3 câu Multiple Choice;
- 2 câu Predict the Output;
- 2 câu Find the Bug;
- 1 câu Explain in Your Own Words.

Làm toàn bộ quiz trước khi yêu cầu AI cung cấp đáp án.

---

## 17. Kỹ thuật 10 — Sử dụng AI để tạo Lecture Note

AI có thể hỗ trợ biến:

- slide bài giảng;
- textbook;
- ghi chú trên lớp;
- đoạn code;
- tài liệu Markdown;

thành một **lecture note dễ tự học hơn**.

Nên cung cấp cho AI **nguồn nội dung cụ thể** thay vì yêu cầu AI tự tạo toàn bộ kiến thức từ đầu.

### 17.1. Tạo lecture note từ nội dung bài giảng

```text
Dưới đây là nội dung bài giảng Python của tôi:

[NỘI DUNG]

Hãy chuyển nội dung này thành lecture note dành cho
sinh viên mới bắt đầu.

Cấu trúc:

1. Giới thiệu bài học
2. Mục tiêu học tập
3. Khái niệm chính
4. Giải thích chi tiết
5. Ví dụ Python
6. Các lỗi thường gặp
7. Self-check questions
8. Bài tập tự luyện
9. Tóm tắt cuối bài

Không bổ sung kiến thức vượt quá nội dung gốc
nếu không ghi rõ đó là phần bổ sung.
```

### 17.2. Biến slide ngắn thành lecture note chi tiết

Ví dụ slide:

```text
Variables
- Store values
- Assignment operator =
- Dynamic typing
```

Prompt:

```text
Đây là nội dung từ một slide Python:

Variables
- Store values
- Assignment operator =
- Dynamic typing

Hãy viết lại thành lecture note dành cho người mới học.

Mỗi khái niệm cần:
- giải thích bằng lời;
- ít nhất một ví dụ;
- một lỗi phổ biến;
- một self-check question.

Không sử dụng kiến thức Python nâng cao.
```

### 17.3. Tạo lecture note ở nhiều mức độ

```text
Giải thích Python variable ở ba mức:

Level 1:
Cho người chưa từng lập trình.

Level 2:
Cho sinh viên đã học input/output.

Level 3:
Giải thích kỹ hơn về biến, object và reference.

Giữ các mức tách biệt rõ ràng.
```

### 17.4. Tạo lecture note kèm code minh họa

```text
Tạo lecture note về Python input/output cho người mới học.

Mỗi mục cần có:

- khái niệm;
- cú pháp;
- ví dụ code ngắn;
- output tương ứng;
- giải thích từng dòng;
- lỗi thường gặp;
- mini exercise.

Chưa sử dụng:
- if;
- loop;
- function;
- list.
```

### 17.5. Tạo Self-check trong lecture note

```text
Bổ sung sau mỗi phần của lecture note:

### Self-check

Gồm:
- 2 câu hỏi khái niệm;
- 1 Predict the Output;
- 1 câu hỏi tìm lỗi.

Không hiển thị đáp án ngay.

Đưa đáp án ở cuối từng phần.
```

Nếu sử dụng Markdown:

```text
Đưa đáp án Self-check vào thẻ:

<details>
<summary>Answer</summary>

...

</details>
```

### 17.6. Tạo lecture note từ chính câu hỏi của sinh viên

```text
Đây là những câu hỏi tôi đã hỏi khi học Python:

- input() trả về kiểu gì?
- int(input()) hoạt động như thế nào?
- tại sao string + int gây lỗi?
- biến trong Python là gì?

Hãy tổ chức chúng thành một lecture note ngắn.

Sắp xếp kiến thức theo thứ tự hợp lý.

Mỗi phần gồm:
- giải thích;
- ví dụ;
- self-check question.
```

---

## 18. Kiểm chứng Lecture Note do AI tạo

Một lecture note do AI tạo **không tự động trở thành tài liệu đúng**.

Sinh viên cần kiểm tra:

- [ ] Nội dung có phù hợp với bài giảng gốc không?
- [ ] AI có thêm kiến thức không có trong nguồn không?
- [ ] Code có chạy được không?
- [ ] Output có đúng không?
- [ ] Thuật ngữ có được sử dụng chính xác không?
- [ ] Có nội dung nào quá nâng cao so với bài học không?
- [ ] Ví dụ có thực sự minh họa đúng khái niệm không?

Một prompt hữu ích:

```text
Hãy review lại lecture note vừa tạo.

Với từng khẳng định kỹ thuật:
- kiểm tra tính chính xác;
- kiểm tra code;
- chỉ ra nội dung nào là suy diễn hoặc bổ sung;
- không tự thêm nội dung mới.
```

Tốt hơn nữa, hãy so sánh lecture note AI tạo với:

- slide của giảng viên;
- giáo trình;
- Python documentation;
- chương trình chạy thực tế.

---

## 19. Kỹ thuật 11 — Yêu cầu AI tăng dần độ khó

```text
Tạo cho tôi một learning ladder gồm 5 bài tập Python.

Chủ đề:
- input;
- output;
- variables;
- arithmetic operators.

Level 1: rất cơ bản
Level 2: cơ bản
Level 3: kết hợp nhiều phép tính
Level 4: bài toán thực tế
Level 5: bài tổng hợp

Không sử dụng if, loop hoặc function.

Không cho lời giải.
```

---

## 20. Kỹ thuật 12 — Học theo phương pháp Socratic

```text
Tôi đang giải bài:

"Nhập nhiệt độ Celsius và đổi sang Fahrenheit."

Tôi chưa biết bắt đầu từ đâu.

Không đưa công thức hoặc code ngay.

Hãy hướng dẫn tôi bằng các câu hỏi.

Mỗi lần chỉ hỏi một câu.
```

AI lúc này không giải bài mà **dẫn dắt quá trình suy luận**.

---

## 21. Workflow: Tạo một bài học hoàn chỉnh bằng AI

Một cách sử dụng AI hữu ích là tạo một **learning package** cho một chủ đề.

```text
Tôi đang tự học Python về input và output.

Hãy giúp tôi tạo một learning package gồm:

1. Lecture note ngắn
2. 3 ví dụ minh họa
3. 5 self-check questions
4. 5 câu quiz
5. 3 bài tập tự luyện
6. Một bài tổng hợp
7. Checklist kiến thức cần đạt

Yêu cầu:
- dành cho người mới bắt đầu;
- không sử dụng if;
- không sử dụng loop;
- không sử dụng function;
- đáp án quiz không hiển thị ngay.
```

Quy trình nên là:

```text
Lecture Note
     ↓
Example
     ↓
Self-check
     ↓
Quiz
     ↓
Exercise
     ↓
AI Review
     ↓
Additional Practice
```

---

## 22. Lab tổng hợp — Học một chủ đề Python với ChatGPT

Chọn một chủ đề:

- Variables
- Data Types
- Input/Output
- Arithmetic Operators

### Bước 1 — Tự đánh giá

```text
Tôi đã biết gì về chủ đề này?
Tôi chưa hiểu điều gì?
```

### Bước 2 — Tạo mini lecture note

```text
Tạo cho tôi một mini lecture note về [CHỦ ĐỀ].

Bao gồm:
- khái niệm;
- cú pháp;
- ví dụ;
- lỗi thường gặp;
- self-check.

Phù hợp với người mới học Python.
```

### Bước 3 — Kiểm tra lecture note

Chạy toàn bộ các đoạn code mẫu.

Ghi lại nếu có nội dung:

- sai;
- chưa rõ;
- quá nâng cao.

### Bước 4 — Explain-back

Tự viết:

```text
Theo cách hiểu của tôi:
...
```

Sau đó yêu cầu AI kiểm tra.

### Bước 5 — Tạo quiz

```text
Hãy tạo 8 câu quiz dựa trên lecture note trên.

Gồm:
- Multiple Choice;
- Predict the Output;
- Find the Bug;
- Explain.

Không hiển thị đáp án.
```

### Bước 6 — Làm quiz

Tự trả lời trước khi yêu cầu AI chấm.

### Bước 7 — Làm bài tập

```text
Cho tôi 3 bài tập nhỏ về nội dung vừa học.

Không có lời giải.
```

### Bước 8 — Debug hoặc review

Nếu sai:

```text
Cho tôi Hint 1.
```

Nếu đúng:

```text
Review code của tôi và đặt một câu hỏi để kiểm tra
xem tôi có thực sự hiểu lời giải hay không.
```

### Bước 9 — Tạo bài tập tiếp theo

Yêu cầu AI tạo một bài tương tự nhưng khó hơn một chút.

---

## 23. Quy trình tự học Python với AI được khuyến nghị

```text
1. READ
   Đọc bài giảng
      ↓
2. BUILD NOTES
   Tạo/tổ chức lecture note
      ↓
3. EXPLAIN
   Tự giải thích
      ↓
4. ASK
   Hỏi AI phần chưa hiểu
      ↓
5. PREDICT
   Dự đoán output
      ↓
6. QUIZ
   Tự kiểm tra
      ↓
7. CODE
   Tự viết chương trình
      ↓
8. TEST
   Chạy và kiểm thử
      ↓
9. DEBUG
   Xin hint nếu cần
      ↓
10. REVIEW
    Nhờ AI review
      ↓
11. PRACTICE
    Làm bài mới
      ↓
12. REFLECT
    Tổng kết kiến thức và lỗi
```

---

## 24. Những cách sử dụng AI không được khuyến nghị

### Copy toàn bộ đề bài

```text
Solve this.
```

### Copy code nhưng không hiểu

Chạy được không có nghĩa là hiểu.

### Xin đáp án quiz ngay lập tức

Nếu xem đáp án trước, quiz mất phần lớn giá trị học tập.

### Yêu cầu AI tự viết toàn bộ lecture note mà không có nguồn

AI có thể:

- thêm nội dung chưa học;
- bỏ nội dung quan trọng;
- sử dụng thuật ngữ khác với giảng viên;
- đưa ra ví dụ quá phức tạp.

### Tin rằng AI luôn đúng

Mọi output của AI đều cần:

```text
Read
  ↓
Understand
  ↓
Run
  ↓
Verify
```

---

## 25. Prompt Toolkit dành cho sinh viên Python

### Học khái niệm

```text
Tôi mới học Python.

Hãy giải thích [KHÁI NIỆM].

Cho:
1. định nghĩa;
2. một ví dụ;
3. một lỗi phổ biến;
4. một self-check question.

Không sử dụng kiến thức nâng cao.
```

### Xin gợi ý

```text
Tôi đang làm bài:

[ĐỀ]

Đây là những gì tôi đã thử:

[CODE/Ý TƯỞNG]

Chỉ cho tôi Hint 1.

Không đưa lời giải.
```

### Debug

```text
Code:

[CODE]

Error:

[ERROR]

Expected:

[KẾT QUẢ MONG MUỐN]

Giải thích nguyên nhân và giúp tôi tự tìm cách sửa.
```

### Review code

```text
Đây là code tôi tự viết:

[CODE]

Hãy review:
1. tính đúng;
2. tính dễ đọc;
3. lỗi logic;
4. trường hợp đặc biệt.

Không viết lại toàn bộ nếu không cần.
```

### Tạo quiz

```text
Tạo 10 câu quiz về [CHỦ ĐỀ].

Gồm:
- 4 Multiple Choice;
- 3 Predict the Output;
- 2 Find the Bug;
- 1 Explain.

Không hiển thị đáp án trước.
```

### Tạo lecture note

```text
Dựa trên nội dung sau:

[NỘI DUNG BÀI GIẢNG]

Hãy tạo lecture note gồm:

1. Learning objectives
2. Concepts
3. Explanations
4. Examples
5. Common mistakes
6. Self-check
7. Exercises
8. Summary

Không bổ sung nội dung vượt quá nguồn nếu không ghi rõ.
```

### Tạo bộ tài liệu ôn tập

```text
Dựa trên lecture note này, hãy tạo:

- một bản tóm tắt;
- 10 flashcards;
- 10 quiz questions;
- 5 Predict the Output;
- 3 Find the Bug;
- 5 exercises.

Không đưa lời giải ngay.
```

---

## 26. Báo cáo Lab

Sinh viên nộp:

### 1. Chủ đề đã học

```text
...
```

### 2. Prompt dùng để tạo lecture note

```text
...
```

### 3. Lecture note sau khi sinh viên kiểm tra/chỉnh sửa

```text
...
```

### 4. Một nội dung AI giải thích chưa tốt hoặc chưa chính xác

```text
...
```

### 5. Prompt tạo quiz

```text
...
```

### 6. Kết quả quiz

```text
Score:
...

Các câu sai:
...
```

### 7. Kiến thức còn yếu được phát hiện qua quiz

```text
...
```

### 8. Một lỗi Python AI đã giúp tìm

```text
...
```

### 9. Code cuối cùng do sinh viên tự viết

```python
...
```

### 10. Một bài tập mới do AI tạo

```text
...
```

### 11. Reflection

```text
Điều tôi học được:

...

Điều tôi vẫn chưa hiểu:

...

Lỗi tôi thường mắc:

...
```

---

## 27. Tự đánh giá

| Kỹ năng | Chưa làm được | Có thể làm với hỗ trợ | Có thể tự làm |
|---|:---:|:---:|:---:|
| Viết prompt rõ ràng | ☐ | ☐ | ☐ |
| Nhờ AI giải thích | ☐ | ☐ | ☐ |
| Tạo lecture note | ☐ | ☐ | ☐ |
| Kiểm chứng lecture note | ☐ | ☐ | ☐ |
| Tạo quiz | ☐ | ☐ | ☐ |
| Dùng quiz để tìm learning gap | ☐ | ☐ | ☐ |
| Xin Hint thay vì lời giải | ☐ | ☐ | ☐ |
| Debug cùng AI | ☐ | ☐ | ☐ |
| Review code | ☐ | ☐ | ☐ |
| Kiểm tra output của AI | ☐ | ☐ | ☐ |
| Tạo bài tập tự luyện | ☐ | ☐ | ☐ |

---

## 28. Nguyên tắc 5T khi học Python với AI

### 1. Think — Tự nghĩ trước

Đừng hỏi AI ngay lập tức.

### 2. Try — Tự thử

Viết ý tưởng hoặc code của mình.

### 3. Talk — Trao đổi với AI

Chỉ hỏi đúng phần đang khó.

### 4. Test — Kiểm thử

Không mặc định AI đúng.

### 5. Teach-back — Giải thích lại

Hãy tự giải thích kiến thức hoặc lời giải bằng ngôn ngữ của mình.

---

## 29. Quy tắc quan trọng nhất

> **Never submit code that you cannot explain.**

Không nộp một chương trình mà bạn không thể tự giải thích.

Tương tự:

> **Never study an AI-generated lecture note without checking it.**

và:

> **Do the quiz before looking at the answers.**

Một bài học chỉ thực sự hoàn thành khi bạn có thể:

1. giải thích khái niệm;
2. dự đoán chương trình;
3. tự viết code;
4. kiểm thử code;
5. phát hiện và sửa lỗi;
6. trả lời quiz;
7. giải thích lại nội dung mà không cần nhìn AI.

---

## 30. Kết luận

ChatGPT có thể đảm nhiệm nhiều vai trò:

```text
ChatGPT
   │
   ├── Tutor
   │     └── Giải thích kiến thức
   │
   ├── Lecture-note Assistant
   │     └── Tổ chức tài liệu học
   │
   ├── Quiz Generator
   │     └── Kiểm tra kiến thức
   │
   ├── Questioner
   │     └── Đặt câu hỏi
   │
   ├── Coach
   │     └── Cung cấp Hint
   │
   ├── Debugging Assistant
   │     └── Hỗ trợ tìm lỗi
   │
   ├── Reviewer
   │     └── Nhận xét code
   │
   └── Practice Generator
         └── Tạo bài tập mới
```

Vai trò nên hạn chế:

```text
Problem
   ↓
ChatGPT
   ↓
Complete Solution
   ↓
Copy
   ↓
Submit
```

Vai trò nên ưu tiên:

```text
Lecture
   ↓
Build Notes
   ↓
Understand
   ↓
Quiz
   ↓
Think
   ↓
Try
   ↓
Ask for Hint
   ↓
Revise
   ↓
Test
   ↓
Explain
   ↓
Practice Again
```

Mục tiêu cuối cùng không phải là:

> **AI có thể viết được bao nhiêu code cho bạn?**

mà là:

> **Sau khi sử dụng AI, bạn có thể tự giải thích, tự viết và tự sửa được nhiều chương trình Python hơn hay không?**
