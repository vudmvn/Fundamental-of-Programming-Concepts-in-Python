# Lesson 5. Functions

**Last updated:** October 4, 2026

> **Source:** Chapter 5 – *Functions*, in the uploaded *Python for Everyone* textbook by Cay Horstmann and Rance Necaise (2/e).
>
> This lecture follows the chapter's structure, terminology, examples, and instructional focus while reorganizing the material for direct classroom use. The main emphasis is on function design, implementation, testing, parameter passing, return values, decomposition, reuse, stepwise refinement, and variable scope. Graphics material is treated as optional, and recursion is retained as an optional advanced topic.

---

## Lesson Introduction

Up to this point, programs have been built mainly from expressions, decisions, and loops. As programs become larger, however, simply placing more statements into one long script makes the code difficult to understand, test, and reuse.

A **function** packages a computation or action under a name.

Instead of repeatedly writing the same steps, we can define those steps once and call the function whenever they are needed.

Conceptually:

```text
Arguments
   ↓
+-------------------+
|      Function     |
|  named sequence   |
|  of instructions  |
+-------------------+
   ↓
Return value
```

The key idea is to think of a function as a **black box**:

- the caller knows what inputs the function needs;
- the caller knows what result the function provides;
- the caller does not need to know every internal implementation detail.

Functions are important not only because they reduce duplicated code. They also make it possible to break a complex task into smaller, understandable, testable parts.

---

## Knowledge and Skills to Be Achieved

After completing this lesson, students will be able to:

- Explain the ideas of **function**, **function call**, **argument**, **parameter variable**, and **return value**.
- Treat a function as a black box with a clearly specified interface.
- Define a function with `def`.
- Call a user-defined function.
- Use `return` to send a result to the caller.
- Distinguish **returning a value** from **printing output**.
- Test a function with representative inputs.
- Organize a program around a `main()` function.
- Explain how arguments are transferred to parameter variables.
- Explain why assigning to a parameter variable does not normally change the caller's variable.
- Design functions that do not return a useful value.
- Recognize that such functions return `None`.
- Identify repeated computations that should be extracted into reusable functions.
- Use parameter variables to make functions more general and reusable.
- Apply **stepwise refinement** to decompose a complex problem.
- Use small helper functions to support a larger computation.
- Explain the purpose of **function comments**, **tracing**, and **stubs**.
- Distinguish **local**, **parameter**, and **global** variables.
- Explain **scope** and why unnecessary global variables should be avoided.
- Understand the purpose of a toolkit of related functions.
- Explain the basic idea of recursion and identify a base case and a recursive reduction.

---

## Lesson Structure

1. Functions as Black Boxes
2. Implementing and Testing Functions
3. Parameter Passing
4. Return Values
5. Functions Without Return Values
6. Problem Solving: Reusable Functions
7. Problem Solving: Stepwise Refinement
8. Variable Scope
9. Optional Topic: Building a Toolkit
10. Recursive Functions (Optional)
11. Chapter Summary, Quiz, and Practice

---

# 5.1 Functions as Black Boxes

A **function** is a named sequence of instructions.

Python already provides many functions. Earlier lessons used functions such as:

```python
print()
input()
len()
round()
int()
float()
```

The important point is that we can use these functions without knowing how every internal instruction is implemented.

For example:

```python
price = round(6.8275, 2)
```

The call:

```python
round(6.8275, 2)
```

supplies two values to the function.

These values are called **arguments**.

The result:

```text
6.83
```

is the **return value**.

The caller then stores that value in:

```python
price
```

---

## 5.1.1 Function Call: Input, Computation, Result

A useful mental model is:

```text
Caller

round(6.8275, 2)
        |
        | arguments
        v
+----------------------+
|        round         |
|                      |
| perform computation  |
+----------------------+
        |
        | return value
        v
       6.83

Caller continues
```

The function temporarily takes control, performs its task, returns a result, and then the calling program continues.

---

## 5.1.2 Arguments

Arguments are the values supplied in a function call.

Example:

```python
round(6.8275, 2)
```

Arguments:

```text
6.8275
2
```

The function can receive one argument, multiple arguments, or no arguments. For example:

```python
random()
```

requires no argument.

---

## 5.1.3 Return Value

A function may compute a value and return it to the caller.

```python
length = len("Python")
```

The call returns `6`, so `length` becomes `6`.

---

## 5.1.4 Returning Is Not the Same as Printing

Printing:

```python
print(6.83)
```

produces visible output.

Returning:

```python
return 6.83
```

passes a value back to the caller.

A returned value can be stored, used in an expression, passed to another function, or tested in a condition.

---

## Example: Nested Function Calls

```python
result = round(abs(-6.8275), 2)
```

Conceptually:

```text
abs(-6.8275)
      ↓
   6.8275
      ↓
round(6.8275, 2)
      ↓
    6.83
```

The inner call is evaluated first.

---

## Self Check 5.1

### Question 1

In:

```python
len("black boxes")
```

how many arguments are supplied?

<details><summary>Answer</summary>

One argument: the string `"black boxes"`.

</details>

### Question 2

What is a return value?

<details><summary>Answer</summary>

It is the result computed by a function and transferred back to the point where the function was called.

</details>

### Question 3

Does every function require an argument?

<details><summary>Answer</summary>

No. A function may require zero, one, or multiple arguments.

</details>

### Question 4

Is returning a value equivalent to printing it?

<details><summary>Answer</summary>

No. `return` gives a value to the caller, while `print` displays output.

</details>

---

# 5.2 Implementing and Testing Functions

The previous section treated functions as black boxes. Now we construct our own functions.

The textbook begins with a simple task: compute the volume of a cube from its side length.

For a cube with side length $s$:

$$
V = s^3
$$

---

## 5.2.1 Implementing a Function

A function definition begins with `def`.

```python
def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume
```

The first line is the **function header**. It specifies the function name and the parameter variable.

The indented statements form the **function body**.

---

## Syntax 5.1 – Function Definition

```python
def functionName(parameter1, parameter2, ...) :
    statements
```

A function that computes a result normally contains:

```python
return result
```

---

## 5.2.2 Parameter Variables

A **parameter variable** represents an argument received when the function is called.

In:

```python
def cubeVolume(sideLength) :
```

`sideLength` is a parameter variable.

When the program calls:

```python
cubeVolume(2)
```

the parameter receives:

```text
sideLength = 2
```

---

## 5.2.3 Calling the Function

```python
result1 = cubeVolume(2)
result2 = cubeVolume(10)

print(result1)
print(result2)
```

Output:

```text
8
1000
```

---

## 5.2.4 Definition vs. Call

Defining:

```python
def cubeVolume(sideLength) :
    return sideLength ** 3
```

does not yet compute a volume.

The body executes only when the function is called:

```python
cubeVolume(2)
```

So remember:

```text
definition → tells Python what the function is
call       → asks Python to execute it
```

---

## 5.2.5 Testing a Function

A function should be tested independently.

```python
def cubeVolume(sideLength) :
    return sideLength ** 3

print(cubeVolume(2))
print(cubeVolume(10))
```

Expected:

```text
8
1000
```

Testing is easier when a function performs one clear task.

---

## 5.2.6 Programs with `main()`

The textbook recommends placing the overall program logic in `main()`.

```python
def main() :
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)

    print("A cube with side length 2 has volume", result1)
    print("A cube with side length 10 has volume", result2)

def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume

main()
```

---

## Syntax 5.2 – Program with Functions

```python
def main() :
    statements

def helperFunction(...) :
    statements

def anotherFunction(...) :
    statements

main()
```

The definitions are processed before `main()` is called.

---

## Why Can `main()` Call a Function Defined Later?

```python
def main() :
    result = cubeVolume(2)
    print(result)

def cubeVolume(sideLength) :
    return sideLength ** 3

main()
```

Execution order:

```text
1. Define main
2. Define cubeVolume
3. Execute main()
4. main calls cubeVolume
```

By the time `main` runs, `cubeVolume` has been defined.

---

## Programming Tip 5.1 – Function Comments

The textbook style documents purpose, parameters, and return value:

```python
## Computes the volume of a cube.
#  @param sideLength the length of a side of the cube
#  @return the volume of the cube
#
def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume
```

---

## Example: Area of a Square

```python
## Computes the area of a square.
#  @param sideLength the side length of the square
#  @return the area of the square
#
def squareArea(sideLength) :
    return sideLength * sideLength
```

---

## Self Check 5.2

### Question 1

What is:

```python
cubeVolume(3)
```

<details><summary>Answer</summary>

`27`.

</details>

### Question 2

What is:

```python
cubeVolume(cubeVolume(2))
```

<details><summary>Answer</summary>

`cubeVolume(2)` returns `8`, then `cubeVolume(8)` returns `512`.

</details>

### Question 3

Why can a file containing only function definitions appear to do nothing?

<details><summary>Answer</summary>

Because a definition does not execute the body. The function must be called.

</details>

---

# 5.3 Parameter Passing

When a function is called, each argument supplies an initial value for a corresponding parameter variable.

```python
def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume

result1 = cubeVolume(2)
```

Conceptually:

```text
Caller:
result1 = cubeVolume(2)

         argument 2
             |
             v

Function call:
sideLength = 2
volume = 8
return 8

             |
             v

Caller:
result1 = 8
```

---

## 5.3.1 Parameters Belong to a Function Call

For:

```python
cubeVolume(2)
```

a parameter variable exists for that call:

```text
sideLength = 2
```

A later call:

```python
cubeVolume(10)
```

has a new parameter value.

---

## 5.3.2 Arguments Can Be Expressions

All of these are valid:

```python
cubeVolume(3)
cubeVolume(length)
cubeVolume(length + 1)
cubeVolume(2 * width)
```

The argument expression is evaluated first.

---

## Example: Two Parameters

```python
def average(x, y) :
    result = (x + y) / 2
    return result
```

Call:

```python
value = average(5, 7)
```

Result:

```text
6.0
```

---

## Programming Tip 5.2 – Do Not Modify Parameter Variables

Python allows:

```python
def totalCents(dollars, cents) :
    cents = dollars * 100 + cents
    return cents
```

but the textbook recommends clearer code:

```python
def totalCents(dollars, cents) :
    result = dollars * 100 + cents
    return result
```

The parameters continue to represent the original inputs.

---

## Common Error 5.1 – Trying to Modify Arguments

```python
def addTax(price, rate) :
    tax = price * rate / 100
    price = price + tax
    return tax
```

Now:

```python
total = 10
addTax(total, 7.5)
```

does **not** change `total` to `10.75`.

Inside the function, `price` changes, but `total` in the caller does not.

If the caller needs the new value:

```python
def addTax(price, rate) :
    tax = price * rate / 100
    return price + tax

total = 10
total = addTax(total, 7.5)
```

Now `total` becomes `10.75`.

---

## Self Check 5.3

### Question 1

```python
def mystery(x, y) :
    z = x + y
    z = z / 2.0
    return z

print(mystery(5, 7))
```

<details><summary>Answer</summary>

`6.0`.

</details>

### Question 2

```python
def mystery(n) :
    n = n + 1
    n = n + 1
    return n

a = 5
print(mystery(a))
print(a)
```

<details><summary>Answer</summary>

The first output is `7`; the second is `5`.

</details>

---

# 5.4 Return Values

The `return` statement terminates the current function call and sends a result back to the caller.

```python
def cubeVolume(sideLength) :
    return sideLength ** 3
```

---

## 5.4.1 `return` Ends the Function Call

```python
def sign(number) :
    if number > 0 :
        return 1

    if number < 0 :
        return -1

    return 0
```

Once `return` executes, later statements in that call are skipped.

---

## 5.4.2 Functions in Expressions

A returned value can be used directly:

```python
volume = cubeVolume(4)

print(cubeVolume(4))

total = cubeVolume(2) + cubeVolume(3)

if cubeVolume(2) > 5 :
    print("Large enough")
```

---

## 5.4.3 Boolean Return Values

```python
def isEven(number) :
    return number % 2 == 0
```

Use:

```python
if isEven(12) :
    print("Even")
```

---

## 5.4.4 String Return Values

```python
def signName(number) :
    if number > 0 :
        return "positive"
    elif number < 0 :
        return "negative"
    else :
        return "zero"
```

---

## Special Topic 5.1 – Single-Line Compound Statements

The textbook sometimes writes:

```python
if n == 0 : return 0
```

The equivalent expanded version is:

```python
if n == 0 :
    return 0
```

---

# HOW TO 5.1 – Implementing a Function

The textbook presents a systematic design process.

## Step 1. Describe what the function should do

State the task precisely.

## Step 2. Determine the inputs

Ask what information the caller must supply.

## Step 3. Determine parameter and return-value types

For example:

```text
parameter: length → integer
return value: password → string
```

## Step 4. Write pseudocode

Describe the algorithm independently of Python syntax.

## Step 5. Implement the body

Translate the pseudocode into Python.

## Step 6. Test the function

Use normal and boundary cases.

---

# Worked Example 5.1 – Generating Random Passwords

The textbook generates a password of a specified length containing lowercase letters, one digit, and one special character.

The special-character set used is:

```text
+-*/?!@#$%&
```

A useful decomposition is:

```text
makePassword(length)
    |
    +-- randomCharacter(characters)
    |
    +-- insertAtRandom(string, toInsert)
```

Pseudocode:

```text
password = empty string

Repeat length - 2 times
    Append a random lowercase letter

Generate a random digit
Insert it at a random position

Generate a random special symbol
Insert it at a random position

Return password
```

The key lesson is decomposition into helper functions.

---

# 5.5 Functions Without Return Values

Not every function needs to compute a value.

The textbook example prints a string in a box.

```text
-------
!Hello!
-------
```

Implementation:

```python
## Prints a string in a box.
#  @param contents the string to enclose in a box
#
def boxString(contents) :
    n = len(contents)
    print("-" * (n + 2))
    print("!" + contents + "!")
    print("-" * (n + 2))
```

Call:

```python
boxString("Hello")
```

---

## 5.5.1 `None`

A function without an explicit useful return value returns:

```python
None
```

Therefore:

```python
result = boxString("Hello")
```

prints the box and then stores `None` in `result`.

---

## 5.5.2 Do Not Confuse Output with Return Values

This is appropriate:

```python
boxString("Hello")
```

This is usually not useful:

```python
print(boxString("Hello"))
```

because the box is printed and then `None` is printed.

---

## 5.5.3 Early Return Without a Value

```python
def boxString(contents) :
    n = len(contents)

    if n == 0 :
        return

    print("-" * (n + 2))
    print("!" + contents + "!")
    print("-" * (n + 2))
```

---

## Self Check 5.5

### Question 1

What does `boxString("World")` return?

<details><summary>Answer</summary>

`None`.

</details>

### Question 2

Write `shout(text)` so that `shout("Hello")` prints `Hello!!!`.

<details><summary>Answer</summary>

```python
def shout(text) :
    print(text + "!!!")
```

</details>

---

# 5.6 Problem Solving: Reusable Functions

If the same computation appears repeatedly, put it into a function.

Instead of:

```python
result1 = value1 * 2.54
result2 = value2 * 2.54
result3 = value3 * 2.54
```

use:

```python
def inchesToCentimeters(inches) :
    return inches * 2.54
```

Then:

```python
result1 = inchesToCentimeters(value1)
result2 = inchesToCentimeters(value2)
result3 = inchesToCentimeters(value3)
```

---

## 5.6.1 Parameterize What Changes

Less reusable:

```python
def printHello() :
    print("Hello, Minh")
```

More reusable:

```python
def printGreeting(name) :
    print("Hello,", name)
```

---

## 5.6.2 Clear Interfaces

```python
## Computes the total number of cents.
#  @param dollars the whole-dollar amount
#  @param cents the remaining cents
#  @return the total amount in cents
#
def totalCents(dollars, cents) :
    return dollars * 100 + cents
```

The interface tells the caller what to supply and what to expect.

---

## 5.6.3 Prefer Returning Data When Reuse Matters

Less reusable:

```python
def printArea(width, height) :
    print(width * height)
```

More reusable:

```python
def rectangleArea(width, height) :
    return width * height
```

The second can be used in assignments, expressions, and conditions.

---

# 5.7 Problem Solving: Stepwise Refinement

**Stepwise refinement** means breaking a difficult task into simpler tasks and continuing until each task is manageable.

```text
Solve large problem
      |
      +-- Subtask A
      |
      +-- Subtask B
      |      |
      |      +-- B1
      |      +-- B2
      |
      +-- Subtask C
```

Each meaningful subtask may become a function.

---

## 5.7.1 Example: Integer Names

The textbook asks for an integer below 1,000 to be converted to English.

Example:

```text
274
```

becomes:

```text
two hundred seventy four
```

Helpers include:

```python
digitName(digit)
teenName(number)
tensName(number)
```

---

## 5.7.2 Specify Helpers Before Implementing

```python
## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digitName(digit) :
    ...
```

This is a key design habit: first define the interface.

---

## 5.7.3 High-Level Pseudocode for `intName`

```text
part = number
name = empty string

If part has a hundreds digit
    append the hundreds name
    remove the hundreds part

If part is at least 20
    append the tens name
    remove the tens part
Else if part is between 10 and 19
    append the teen name
    set part to 0

If part is still greater than 0
    append the digit name

Return name
```

---

## Programming Tip 5.3 – Keep Functions Short

A function should carry out one well-defined task.

Short functions are easier to understand, test, reuse, debug, and modify.

---

## Programming Tip 5.4 – Tracing Functions

For `416`, an important trace is:

| Stage | `part` | `name` |
|---|---:|---|
| Start | 416 | `""` |
| Hundreds processed | 16 | `"four hundred"` |
| Teen processed | 0 | `"four hundred sixteen"` |

Tracing reveals why `part` must become `0` after the teen part is processed.

---

## Programming Tip 5.5 – Stubs

A **stub** is a temporary incomplete function used while developing or testing other code.

```python
def digitName(digit) :
    return "mumble"
```

```python
def tensName(number) :
    return "mumblety"
```

An intermediate result such as:

```text
mumble hundred mumblety mumble
```

can show that the high-level control logic works before every helper is complete.

---

# Worked Example 5.2 – Calculating a Course Grade

A student has four letter grades.

The lowest grade is dropped.

The remaining three are averaged after conversion to numeric grade points.

Examples:

```text
A+ = 4.3
A  = 4.0
A- = 3.7
B+ = 3.3
...
D- = 0.7
F  = 0
```

A high-level decomposition is:

```text
Process one set of grades
      |
      +-- Convert letter grade to number
      |
      +-- Find lowest of four numbers
      |
      +-- Compute average of remaining three
      |
      +-- Convert number grade to letter
      |
      +-- Print result
```

---

## 5.7.4 Convert Letter Grade to Number

```python
def gradeToNumber(grade) :
    result = 0

    first = grade[0]
    first = first.upper()

    if first == "A" :
        result = 4
    elif first == "B" :
        result = 3
    elif first == "C" :
        result = 2
    elif first == "D" :
        result = 1

    if len(grade) > 1 :
        second = grade[1]

        if second == "+" :
            result = result + 0.3
        elif second == "-" :
            result = result - 0.3

    return result
```

---

## 5.7.5 Process One Set of Grades

The first input can serve as a sentinel: `Q` means stop.

High-level logic:

```text
Read first grade.
If first grade is Q
    signal that processing is finished.

Read next three grades.
Convert all grades to numbers.
Find the lowest.
Average the other three.
Convert average back to a letter.
Print result.
```

A complex program can therefore have a simple `main()` loop.

---

# Worked Example 5.3 – Using a Debugger

A debugger helps locate bugs by allowing controlled program execution.

Useful operations include:

- pausing at a breakpoint;
- inspecting variable values;
- stepping through statements;
- stepping into a function call;
- continuing execution.

When debugging function-based programs, ask:

```text
Which function is executing?
What arguments did it receive?
What are the parameter values?
What local variables exist?
What value is about to be returned?
Where does execution continue after return?
```

A disciplined approach is:

```text
1. Choose a small test case.
2. Predict the correct result.
3. Trace the call.
4. Inspect parameters and local variables.
5. Find the first state that differs from expectation.
```

---

# 5.8 Variable Scope

The **scope** of a variable is the part of the program in which the variable is visible.

---

## 5.8.1 Local Variables

```python
def calculateTax(price, rate) :
    tax = price * rate / 100
    return tax
```

`tax` is local to `calculateTax`.

---

## 5.8.2 Parameter Variables

In:

```python
def calculateTax(price, rate) :
```

`price` and `rate` are parameter variables.

---

## 5.8.3 Global Variables

```python
TAX_RATE = 7.5

def calculateTax(price) :
    return price * TAX_RATE / 100
```

`TAX_RATE` is global.

---

## 5.8.4 Same Local Name in Different Functions

```python
def first() :
    result = 10
    return result

def second() :
    result = 20
    return result
```

The two variables named `result` are separate.

---

## Programming Tip 5.6 – Avoid Global Variables

Unnecessary global variables make it harder to determine which function depends on or changes shared state.

Prefer explicit inputs:

```python
def calculateTax(price, rate) :
    return price * rate / 100
```

instead of relying on changing global state.

---

## Global Constants

A fixed global constant is often more reasonable:

```python
PENNIES_PER_DOLLAR = 100
```

The important distinction is:

```text
global constant → shared fixed configuration
global variable → shared changing state
```

---

## Self Check 5.8

### Question 1

```python
def f(x) :
    y = x + 1
    return y
```

Which variables belong to `f`?

<details><summary>Answer</summary>

`x` is a parameter variable and `y` is a local variable.

</details>

### Question 2

Why can global variables make debugging difficult?

<details><summary>Answer</summary>

Because several parts of the program may depend on or modify shared state.

</details>

---

# 5.9 Optional Topic: Building a Toolkit

Section 5.9 uses graphics and image processing to illustrate the design of a **toolkit**: a collection of related reusable functions.

The original section includes comparing images, adjusting brightness, rotating images, and using the toolkit from another program.

For courses that skip the graphics library, the software-design idea remains important.

Example numeric toolkit:

```python
def isEven(number) :
    return number % 2 == 0

def cube(number) :
    return number ** 3

def clamp(value, low, high) :
    if value < low :
        return low
    if value > high :
        return high
    return value
```

A toolkit centralizes tested, reusable operations.

---

# 5.10 Recursive Functions (Optional)

A function is **recursive** when it calls itself.

A recursive solution has two essential parts:

```text
Base case
    Solve the simplest case directly.

Recursive case
    Reduce the problem to a smaller version of the same problem.
```

---

## 5.10.1 Digit Sum

For:

```text
1729
```

we can write:

```text
digitSum(1729)
=
digitSum(172) + 9
```

because:

```python
1729 // 10
```

is `172` and:

```python
1729 % 10
```

is `9`.

---

## 5.10.2 Base Case

```python
if n == 0 :
    return 0
```

Without a base case, recursion would not terminate.

---

## 5.10.3 Recursive Implementation

```python
def digitSum(n) :
    if n == 0 :
        return 0

    return digitSum(n // 10) + n % 10
```

For `1729`:

```text
digitSum(1729)
= digitSum(172) + 9
= digitSum(17) + 2 + 9
= digitSum(1) + 7 + 2 + 9
= digitSum(0) + 1 + 7 + 2 + 9
= 19
```

---

# HOW TO 5.2 – Thinking Recursively

A useful design process is:

## Step 1. Find a simpler input for the same problem

For digit sum:

```python
n // 10
```

## Step 2. Determine the work that remains

```python
n % 10
```

## Step 3. Identify the simplest input

```text
n = 0
```

## Step 4. Combine the cases

```python
def digitSum(n) :
    if n == 0 :
        return 0
    return digitSum(n // 10) + n % 10
```

The central recursive idea is:

```text
same problem + simpler input + base case
```

---

# Chapter 5 Summary

## Functions and Black Boxes

A function is a named sequence of instructions. The caller supplies arguments, and the function may return a result.

## Function Definition and Testing

Functions are defined with `def` and executed through function calls. Functions should be tested independently.

## Parameter Passing

Arguments provide the initial values of parameter variables.

## Return Values

`return` terminates the current function call and transfers a result to the caller.

## Functions Without Useful Return Values

Some functions perform actions such as producing output and return `None`.

## Reusability

Repeated computations should be packaged into parameterized functions.

## Stepwise Refinement

Complex tasks should be decomposed into simpler tasks and helper functions.

## Variable Scope

Local and parameter variables belong to functions; global variables are defined outside functions. Unnecessary global state should be avoided.

## Toolkits

Related reusable functions can be collected into a toolkit.

## Recursion

A recursive function solves a problem through a simpler input of the same problem and requires a terminating base case.

---

# Summary Quiz

## Question 1

Which keyword begins a function definition?

A. `function`  
B. `define`  
C. `def`  
D. `func`

<details><summary>Answer</summary>

C. `def`

</details>

## Question 2

In `cubeVolume(5)`, what is `5`?

<details><summary>Answer</summary>

An argument.

</details>

## Question 3

In `def cubeVolume(sideLength) :`, what is `sideLength`?

<details><summary>Answer</summary>

A parameter variable.

</details>

## Question 4

What does `return` do?

<details><summary>Answer</summary>

It terminates the function call and passes a result back to the caller.

</details>

## Question 5

Why does changing a parameter variable not automatically change the caller's variable?

<details><summary>Answer</summary>

The parameter variable belongs to the function call; assigning to it does not assign to the caller's variable.

</details>

## Question 6

What value is returned when a function reaches the end without returning another value?

<details><summary>Answer</summary>

`None`.

</details>

## Question 7

What is a stub?

<details><summary>Answer</summary>

A temporary incomplete function used to support testing while another part of the program is being developed.

</details>

## Question 8

What is scope?

<details><summary>Answer</summary>

The part of a program in which a variable is visible.

</details>

## Question 9

What is stepwise refinement?

<details><summary>Answer</summary>

Breaking a complex task into simpler tasks until the subtasks are manageable.

</details>

## Question 10

What is necessary for recursion to terminate?

<details><summary>Answer</summary>

A base case and a recursive step that moves toward that base case.

</details>

---

# Short Programming Practice

## Exercise 1 – Square

Write:

```python
square(number)
```

that returns the square of `number`.

## Exercise 2 – Maximum of Two Values

Write:

```python
larger(a, b)
```

that returns the larger value.

## Exercise 3 – Is Positive

Write:

```python
isPositive(number)
```

that returns a Boolean value.

## Exercise 4 – Total Cents

Write:

```python
totalCents(dollars, cents)
```

that returns the total number of cents.

## Exercise 5 – Print a Separator

Write:

```python
printSeparator(length)
```

that prints a line of `length` hyphens and does not return a useful value.

## Exercise 6 – Function Composition

Given:

```python
def square(x) :
    return x * x

def addOne(x) :
    return x + 1
```

predict:

```python
square(addOne(3))
addOne(square(3))
square(square(2))
```

before running the code.

---

# Applied Practice

## Applied Exercise 1 – Business: Revenue

Write:

```python
revenue(price, quantity)
```

that returns:

$$
\text{revenue} = \text{price} \times \text{quantity}
$$

## Applied Exercise 2 – Finance: Compound Balance

Write:

```python
futureBalance(initialBalance, annualRate, years)
```

that computes a balance after a fixed number of years using a loop.

## Applied Exercise 3 – Supply Chain: Transportation Cost

Write:

```python
transportCost(distance, costPerKm)
```

and then:

```python
totalDeliveryCost(distance, costPerKm, handlingCost)
```

where the second function reuses the first.

## Applied Exercise 4 – Economics: Price after Tax

Write:

```python
priceAfterTax(price, taxRate)
```

that returns the final price without modifying the parameter variable `price`.

---

# Practice: Stepwise Refinement

Consider:

> Read several sales values, compute total sales, average sales, and the largest sale, then print a formatted report.

Design possible functions such as:

```text
readSalesData
computeAverage
findLargest
printReport
main
```

For each proposed function, specify:

```text
purpose
parameters
return value
```

The goal is not to maximize the number of functions. The goal is a clear decomposition.

---

# Practice: Scope Analysis

Consider:

```python
RATE = 5

def main() :
    balance = 1000
    result = grow(balance, RATE)
    print(result)

def grow(amount, rate) :
    interest = amount * rate / 100
    result = amount + interest
    return result

main()
```

Classify:

```text
RATE
balance
result in main
amount
rate
interest
result in grow
```

as global, parameter, or local variables.

Then explain why the two names `result` refer to different variables.

---

# Optional Recursive Practice

## Exercise R1 – Countdown

Write:

```python
countdown(n)
```

recursively.

## Exercise R2 – Sum from 1 to n

Use:

$$
S(n) = n + S(n-1)
$$

with:

$$
S(0) = 0
$$

and implement:

```python
sumTo(n)
```

## Exercise R3 – Digit Sum

Implement:

```python
digitSum(n)
```

recursively and test:

```python
digitSum(1729)   # 19
digitSum(1000)   # 1
digitSum(9)      # 9
digitSum(0)      # 0
```

---

# Key Terms

- argument
- base case
- black box
- caller
- function
- function body
- function call
- function header
- global variable
- helper function
- local variable
- `main`
- parameter passing
- parameter variable
- recursion
- recursive case
- return value
- scope
- stepwise refinement
- stub
- toolkit

---

# Final Checklist

Be able to distinguish:

```text
function definition     vs. function call
argument                vs. parameter variable
print                   vs. return
local variable          vs. global variable
computation function    vs. action/output function
large task              vs. refined subtasks
complete helper         vs. stub
iteration               vs. recursion
base case               vs. recursive case
```

The central design principle of the chapter is:

> **Break a complex computation into small, well-specified functions, and make the transfer of information between them explicit through parameters and return values.**
