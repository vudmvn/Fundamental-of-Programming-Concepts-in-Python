# Lecture: Basic Input/Output in Python

## 1. Lesson Introduction

In most programs, data is received, processed, and then returned to the user. Two fundamental operations used in this process are:

- **Input:** receiving data from the user.
- **Output:** displaying results on the screen.

For example, a program that calculates the area of a rectangle needs to:

1. Input the length.
2. Input the width.
3. Calculate the area.
4. Display the result on the screen.

In Python, the two most basic functions for input and output are:

```python
input()
print()
```

---

## 2. Learning Objectives

After completing this lesson, students will be able to:

1. Use `print()` to display data on the screen.
2. Print multiple values in a single `print()` statement.
3. Use the basic parameters `sep` and `end`.
4. Use `input()` to receive data from the keyboard.
5. Understand that `input()` returns data of type `str`.
6. Convert input data to `int` or `float` when calculations are required.
7. Combine input, processing, and output in a program.
8. Use f-strings for basic output formatting.
9. Identify several common errors when working with input and output.

> **Lesson scope:** The exercises in this lesson are written directly using basic statements; user-defined functions (`def`) are not used yet.

---

## 3. Displaying Data with `print()`

### 3.1. Basic Syntax

```python
print(value)
```

Example:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

Numeric values can be displayed directly:

```python
print(100)
print(3.14)
```

You can also display values stored in variables:

```python
name = "An"
age = 18

print(name)
print(age)
```

---

### 3.2. Printing Multiple Values in One Statement

`print()` can receive multiple values at the same time.

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

By default, `print()` inserts a space between the values passed to it.

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

### 3.3. The `sep` Parameter — Controlling the Separator

```python
print("2026", "09", "06", sep="-")
```

Output:

```text
2026-09-06
```

Another example:

```python
print("Python", "Java", "C++", sep=" | ")
```

Output:

```text
Python | Java | C++
```

---

### 3.4. The `end` Parameter — Controlling the Line Ending

By default, Python moves to a new line after each `print()` statement.

```python
print("Hello")
print("Python")
```

Output:

```text
Hello
Python
```

This behavior can be changed with `end`:

```python
print("Hello", end=" ")
print("Python")
```

Output:

```text
Hello Python
```

---

### Self-Check Questions 1

### Question 1

What is the output of the following program?

```python
print("A", "B", "C", sep="-")
```

<details>
<summary>Answer</summary>

```text
A-B-C
```

</details>

### Question 2

What is the output of the following program?

```python
print("Hello", end=" ")
print("World")
```

<details>
<summary>Answer</summary>

```text
Hello World
```

</details>

---

## 4. Displaying Variable Values

Programs usually display not only fixed values but also data stored in variables.

```python
product = "Laptop"
price = 1500

print(product)
print(price)
```

Text and variables can be combined:

```python
print("Product:", product)
print("Price:", price)
```

---

## 5. Receiving Input with `input()`

### 5.1. Syntax

```python
variable = input("Prompt")
```

Example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

`input()` performs four steps:

1. displays a prompt;
2. waits for the user to enter data;
3. receives the data when the user presses Enter;
4. returns the entered data.

---

### 5.2. Data Type Returned by `input()`

```python
age = input("Enter your age: ")
print(type(age))
```

If the user enters `18`, the result is still:

```text
<class 'str'>
```

Even when the input looks like a number, `input()` still returns a string.

---

## 6. Converting Input Data Types

When input data is used in arithmetic calculations, the string returned by `input()` must be converted to an appropriate numeric type.

### 6.1. Converting to an Integer with `int()`

```python
age = int(input("Enter your age: "))
print(age + 1)
```

If the user enters `18`, the output is:

```text
19
```

### 6.2. Converting to a Floating-Point Number with `float()`

```python
price = float(input("Enter price: "))
print(price)
```

---

### 6.3. Comparing Input With and Without Type Conversion

#### Case 1 — Without Type Conversion

```python
x = input("Enter x: ")
y = input("Enter y: ")
print(x + y)
```

If the user enters `10` and `20`, the output is:

```text
1020
```

#### Case 2 — With Type Conversion

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

### Self-Check Questions 2

### Question 1

What does the following code print if the user enters `5`?

```python
x = input("x = ")
print(x * 3)
```

<details>
<summary>Answer</summary>

```text
555
```

Because `x` is the string `"5"`; multiplying a string by `3` repeats the string three times.

</details>

### Question 2

How can the code be modified so that the result is `15`?

<details>
<summary>Answer</summary>

```python
x = int(input("x = "))
print(x * 3)
```

</details>

---

## 7. The Input → Process → Output Model

The structure of a basic input/output program can be described in three steps:

```text
Input
  ↓
Process
  ↓
Output
```

Example: calculating the area of a rectangle.

```python
length = float(input("Length: "))
width = float(input("Width: "))

area = length * width

print("Area:", area)
```

In this example:

- `length`, `width`: input;
- `length * width`: process;
- `print(...)`: output.

---

## 8. Formatting Output with f-Strings

F-strings provide a clear and convenient way to combine text with variable values.

```python
name = "An"
age = 18

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

Expressions can also be placed inside `{}`:

```python
x = 10
y = 5
print(f"{x} + {y} = {x + y}")
```

Output:

```text
10 + 5 = 15
```

### 8.1. Formatting Floating-Point Numbers

```python
price = 19.5678
print(f"Price: {price:.2f}")
```

Output:

```text
Price: 19.57
```

`.2f` means that the floating-point number is displayed with 2 digits after the decimal point.

---

## 9. Common Errors and How to Identify Them

### 9.1. Forgetting to Convert the Data Type

Incorrect:

```python
age = input("Age: ")
next_age = age + 1
```

Reason:

- `age` is a `str`;
- `1` is an `int`;
- `str` and `int` cannot be added directly.

Corrected version:

```python
age = int(input("Age: "))
next_age = age + 1
```

### 9.2. Input Data Does Not Match the Required Type

```python
age = int(input("Age: "))
```

If the user enters `eighteen`, Python cannot convert that string into an integer.

Within the scope of this lesson, assume that the user enters data in the required format. Techniques for validating and handling invalid input will be introduced in later lessons.

### 9.3. Confusing a Variable with a String Literal

```python
x = 10
print("x")
```

Output:

```text
x
```

Whereas:

```python
print(x)
```

Output:

```text
10
```

---

## 10. Integrated Examples

### Example 1 — Personal Information

```python
name = input("Name: ")
age = int(input("Age: "))

print(f"Hello {name}!")
print(f"Next year you will be {age + 1}.")
```

### Example 2 — Calculating the Total Cost

```python
price = float(input("Product price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print(f"Total: {total:.2f}")
```

### Example 3 — Converting Celsius to Fahrenheit

Formula:

$$
F = \frac{9}{5}C + 32
$$

```python
celsius = float(input("Celsius: "))
fahrenheit = 9 / 5 * celsius + 32
print(f"Fahrenheit: {fahrenheit:.2f}")
```

---

## 11. Predict the Output Exercises

### Exercise 1

```python
x = "10"
y = "5"
print(x + y)
```

<details>
<summary>Answer</summary>

```text
105
```

</details>

### Exercise 2

```python
x = 10
y = 5
print("Result:", x + y)
```

<details>
<summary>Answer</summary>

```text
Result: 15
```

</details>

### Exercise 3

```python
print("A", "B", sep=":", end=" ")
print("C")
```

<details>
<summary>Answer</summary>

```text
A:B C
```

</details>

### Exercise 4

```python
x = 7
print(f"x = {x}, x^2 = {x * x}")
```

<details>
<summary>Answer</summary>

```text
x = 7, x^2 = 49
```

</details>

---

## 12. Practice Exercises

> **General requirement:** Write statements directly according to the **Input → Process → Output** model; user-defined functions (`def`) are not used yet.

### Exercise 1 — Greeting

Input the user's name and display:

```text
Hello, <name>!
```

### Exercise 2 — Age Next Year

Input the current age and display the user's age next year.

### Exercise 3 — Sum and Product

Input two integers `a` and `b`. Display their sum and product.

### Exercise 4 — Rectangle

Input the length and width. Calculate and display the area and perimeter.

### Exercise 5 — Calculating the Total Purchase Cost

Input the product name, unit price, and quantity. Display an invoice in the following format:

```text
Product: Notebook
Unit price: 15.50
Quantity: 3
Total: 46.50
```

### Exercise 6 — Temperature Conversion

Input a temperature in Celsius and convert it to Fahrenheit:

$$
F = \frac{9}{5}C + 32
$$

Display the result with 2 digits after the decimal point.

### Exercise 7 — Calculating the Average Score

Input three floating-point scores. Calculate and display the average with 2 digits after the decimal point.

### Exercise 8 — Converting Seconds

Input a number of seconds. Calculate the total number of full minutes and the remaining seconds.

Example:

```text
Seconds: 135
Minutes: 2
Remaining seconds: 15
```

Hint:

```python
//   # integer division
%    # remainder
```

---

## 13. Integrated Practice — Calculating Trip Cost

Input:

- distance traveled (km);
- fuel consumption (liters/100 km);
- fuel price (currency units/liter).

Calculate:

$$
\text{fuel\_used} = \frac{\text{distance} \times \text{consumption}}{100}
$$

$$
\text{cost} = \text{fuel\_used} \times \text{fuel\_price}
$$

Sample output:

```text
Distance: 250
Consumption (L/100km): 7.5
Fuel price: 23000

Fuel used: 18.75 L
Estimated cost: 431250.00
```

---

## 14. Self-Assessment After the Lesson

- [ ] I know how to use `print()`.
- [ ] I know how to print multiple values in one statement.
- [ ] I understand `sep` and `end`.
- [ ] I know how to use `input()`.
- [ ] I remember that `input()` returns `str`.
- [ ] I know when to use `int()` or `float()`.
- [ ] I can write a program using the Input → Process → Output model.
- [ ] I know how to use basic f-strings.
- [ ] I can format floating-point values using `.2f`.
- [ ] I can explain an error caused by adding `str` and `int`.
- [ ] I can independently write simple programs without using `def`.

---

## 15. Knowledge Summary

Important tools:

```python
print(...)
input(...)
int(...)
float(...)
type(...)
```

Common patterns:

```python
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))
print("Result:", result)
print(f"Result: {result}")
print(f"Result: {result:.2f}")
```

Remember:

```text
Input → Process → Output
```

and the learning process:

> **Predict → Run → Explain → Modify → Practice**
