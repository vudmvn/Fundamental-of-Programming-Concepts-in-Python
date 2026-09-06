# Tutorial/Lab: Using ChatGPT to Learn and Self-Study Python Effectively

## 1. Introduction

Generative AI tools such as **ChatGPT** can be very useful for learning Python. However, their educational value depends heavily on **how learners use them**.

If a student only asks:

```text
Solve this problem for me.
```

they may quickly receive a complete program, but still fail to understand:

- How was the problem analyzed?
- Why was a particular statement used?
- Why does the program work?
- What should be changed if the problem changes?
- How can the student solve a similar problem independently?

In this tutorial/lab, ChatGPT is used as a **personal AI tutor** to:

- explain concepts;
- create or reorganize lecture notes;
- generate quizzes and self-check questions;
- provide examples;
- ask diagnostic questions;
- give hints when the learner is stuck;
- support debugging;
- review solutions;
- generate additional practice exercises.

> **Key principle:**  
> Use AI to **learn how to solve a problem**, not merely to **obtain the solution**.

---

## 2. Learning Objectives

After completing this lab, students should be able to:

1. Use ChatGPT to explain a Python concept they do not understand.
2. Write prompts with sufficient context.
3. Ask AI for **hints instead of complete solutions**.
4. Use AI to check their own understanding.
5. Use AI to support Python debugging.
6. Verify and evaluate AI-generated answers.
7. Use AI to create additional practice exercises.
8. Use AI to generate self-assessment quizzes.
9. Use AI to create or reorganize lecture notes.
10. Build an effective AI-assisted Python self-study workflow.

---

## 3. Preparation

Students need:

- a web browser;
- a ChatGPT account;
- Google Colab or another Python environment;
- lecture materials, if available;
- basic Python knowledge.

The first examples mainly use:

- variables;
- data types;
- operators;
- `print()`;
- `input()`;
- Python expressions.

Students are not required to know how to define functions.

---

## 4. What Role Should AI Play When Learning Python?

A useful way to work with ChatGPT is to treat it as a **personal tutor**.

Instead of:

```text
I do not know how to solve this. Write the code for me.
```

try:

```text
I am learning basic Python.

I do not want to see the complete solution yet.

Please:
1. Explain the problem.
2. Give me the first hint.
3. Let me try before giving more help.
```

A recommended workflow is:

```text
Read the material
      ↓
Explain it in your own words
      ↓
Ask AI about unclear points
      ↓
Write the program yourself
      ↓
Run the program
      ↓
Ask for a hint if necessary
      ↓
Revise the program
      ↓
Ask AI to review it
      ↓
Take a quiz
      ↓
Practice with a similar problem
```

---

## 5. What Makes a Good Prompt?

A useful learning prompt usually contains four parts:

```text
[Context]

[What I do not understand]

[What I want the AI to do]

[How I want the AI to respond]
```

Example:

```text
I am a beginner learning Python.

I am studying variables, but I do not understand the difference
between a variable and the value assigned to it.

Explain the idea using a simple example.

After the explanation, give me 3 short questions to check
whether I understand it.

Do not show the answers immediately.
```

Compared with:

```text
What is a Python variable?
```

the detailed prompt gives the AI information about:

- the learner's level;
- the topic being studied;
- the specific difficulty;
- the desired explanation style;
- how understanding should be checked.

---

## 6. Technique 1 — Ask AI to Explain a Concept

Suppose a student does not understand:

```python
x = 10
```

They can ask:

```text
I am new to Python.

Please explain:

x = 10

Explain:
- What is x?
- What is 10?
- What does = mean?
- What happens when Python executes this statement?

Use simple language and one real-life analogy.
```

Then continue:

```text
Now ask me 3 questions to check whether I really understand x = 10.

Do not give me the answers yet.
```

### Practice 1

Use ChatGPT to learn one of the following concepts:

- variables;
- data types;
- operators;
- `print()`;
- `input()`.

Your prompt must include:

- your current level;
- the concept you want to learn;
- a request for an example;
- a request for a knowledge check.

---

## 7. Technique 2 — Use AI to Check Your Own Explanation

A useful learning strategy is:

> **Explain first — ask AI to check later.**

Example:

```text
My understanding is that input() reads data entered by the user
and always returns a string.

Please check my explanation.

If anything is incorrect:
- point out the incorrect part;
- explain why;
- give a small example.
```

### Practice 2

Explain this statement in your own words:

```python
age = input("Enter your age: ")
```

Then ask ChatGPT to check your explanation.

---

## 8. Technique 3 — Predict the Output Before Running the Code

AI can generate **Predict the Output** exercises.

Example prompt:

```text
I am learning basic Python variables, operators, and print().

Give me 5 short Python programs whose outputs I must predict.

Requirements:
- at most 5 lines each;
- no loops;
- no user-defined functions;
- do not show answers immediately;
- increase the difficulty gradually.
```

Example:

```python
x = 5
y = 3
x = x + y
print(x)
```

Recommended process:

1. Predict the output.
2. Write down your answer.
3. Run the program.
4. Compare the result.
5. Explain why your prediction was wrong, if necessary.

---

## 9. Technique 4 — Ask for Hints Instead of Solutions

Problem:

> Read the length and width of a rectangle.  
> Print its area and perimeter.

Instead of:

```text
Write Python code to solve this problem.
```

ask:

```text
I need to solve this Python exercise by myself:

"Read the length and width of a rectangle.
Print its area and perimeter."

I am learning input, variables, operators, and print.

Do not write the complete solution.

Ask me questions that help me identify:
1. the required inputs;
2. the variables I need;
3. the formulas I need;
4. the required outputs.
```

---

## 10. A Three-Level Hint System

### Hint 1 — Idea Hint

No code.

### Hint 2 — Structure Hint

Suggests the concept or statement to use.

### Hint 3 — Near-Solution Hint

May include part of the code, but not the full solution.

Example:

```text
I am still stuck.

Give me Hint 2.

Do not provide the complete solution.
```

---

## 11. Technique 5 — Debug with AI

Example:

```python
age = input("Enter age: ")
next_age = age + 1
print(next_age)
```

A useful prompt:

```text
I am new to Python.

Here is my program:

age = input("Enter age: ")
next_age = age + 1
print(next_age)

The program produces an error.

Do not fix everything immediately.

Please:
1. explain the cause of the error;
2. identify the line that causes it;
3. ask me one guiding question so I can fix it myself.
```

---

## 12. Reading Error Messages with ChatGPT

When asking AI about an error, provide:

```text
1. Code
2. Error message
3. Expected result
4. Actual result
```

Template:

```text
I am learning basic Python.

Code:

[CODE]

Error:

[ERROR MESSAGE]

I want the program to:

[DESCRIPTION]

Explain the error for a beginner.

Do not give the complete corrected solution immediately.
```

---

## 13. Technique 6 — Ask AI to Review Your Code

Example:

```text
Here is the program I wrote:

length = float(input("Length: "))
width = float(input("Width: "))

area = length * width
perimeter = 2 * (length + width)

print(area)
print(perimeter)

Please review my code.

Tell me:
1. whether the program is correct;
2. whether the variable names are clear;
3. whether any lines are unnecessary;
4. how the code could be easier to read.

Do not use advanced Python techniques.
```

---

## 14. Technique 7 — Ask AI to Act as a Teacher

Prompt:

```text
Act as my Python teacher.

Topic: variables and data types.

Process:

1. Ask me one question.
2. Wait for my answer.
3. Comment on my answer.
4. If I am wrong, explain briefly.
5. Then ask the next question.

Start easy and gradually increase the difficulty.

Do not ask multiple questions at once.
```

This turns ChatGPT into an **interactive AI tutor**.

---

## 15. Technique 8 — Use AI to Generate Practice Exercises

Prompt:

```text
I have just completed this exercise:

"Read the radius and calculate the area of a circle."

Create 5 similar exercises for me to practice:
- input();
- variables;
- arithmetic;
- print().

Do not use:
- if;
- loops;
- lists;
- functions.

Do not provide solutions.
```

---

## 16. Technique 9 — Use AI to Generate Quizzes

ChatGPT can generate quizzes for immediate self-assessment.

Avoid a vague request such as:

```text
Create a Python quiz.
```

A better prompt specifies:

- topic;
- learner level;
- question type;
- number of questions;
- allowed knowledge;
- when answers should be shown.

### 16.1. Multiple-Choice Quiz

```text
I am a beginner learning Python.

Create 10 multiple-choice questions about:
- variables;
- data types;
- print();
- input();
- arithmetic operators.

Requirements:
- 4 choices A, B, C, D for each question;
- exactly one correct answer;
- no if statements, loops, lists, or functions;
- do not show the answers yet;
- gradually increase the difficulty.
```

After completing the quiz:

```text
Here are my answers:

1A
2C
3B
...

Please:
1. score my answers;
2. identify the incorrect answers;
3. explain them briefly;
4. identify the topics I still need to review.
```

### 16.2. Predict-the-Output Quiz

```text
Create 5 Python Predict the Output questions.

Topics:
- variables;
- assignment;
- arithmetic operators;
- print().

Each code snippet should contain 2 to 5 lines.

Do not show the answers first.
```

### 16.3. Find-the-Bug Quiz

```text
Create 5 "Find the Bug" questions for a Python beginner.

Each question should contain one short code snippet with exactly one error.

Topics:
- input;
- type conversion;
- variables;
- arithmetic;
- print.

Do not provide the answers yet.
```

### 16.4. Concept-Explanation Quiz

```text
Test me with 5 short Python questions.

Do not use multiple-choice questions.

I must explain the answer in my own words.

Ask one question at a time.
After each answer:
- evaluate my answer;
- add anything important that I missed;
- then ask the next question.
```

### 16.5. Generate a Quiz from Your Own Mistakes

```text
In my recent exercises, I made these mistakes:

1. I forgot to convert input() to int.
2. I confused = with comparison.
3. I did not understand x = x + 1.

Create 6 quiz questions that focus on exactly these mistakes.

Do not show the answers first.
```

### Practice 3 — Create a Personal Quiz

Choose one Python topic you have already studied.

Ask ChatGPT to create:

- 3 Multiple Choice questions;
- 2 Predict the Output questions;
- 2 Find the Bug questions;
- 1 Explain in Your Own Words question.

Complete the entire quiz before asking AI for the answers.

---

## 17. Technique 10 — Use AI to Create Lecture Notes

AI can help transform:

- lecture slides;
- textbooks;
- classroom notes;
- code examples;
- Markdown documents;

into a more readable **self-study lecture note**.

Whenever possible, provide a **specific source** instead of asking AI to create an entire lecture from scratch.

### 17.1. Create a Lecture Note from Lecture Content

```text
Below is the content of my Python lecture:

[CONTENT]

Turn this into a lecture note for beginner students.

Use the following structure:

1. Lesson introduction
2. Learning objectives
3. Key concepts
4. Detailed explanations
5. Python examples
6. Common mistakes
7. Self-check questions
8. Practice exercises
9. Lesson summary

Do not add material beyond the source unless you clearly label it as additional content.
```

### 17.2. Expand a Short Slide into a Detailed Lecture Note

Example slide:

```text
Variables
- Store values
- Assignment operator =
- Dynamic typing
```

Prompt:

```text
This is content from a Python slide:

Variables
- Store values
- Assignment operator =
- Dynamic typing

Rewrite it as a lecture note for beginners.

For each concept:
- explain it in words;
- provide at least one example;
- include one common mistake;
- include one self-check question.

Do not use advanced Python concepts.
```

### 17.3. Create Lecture Notes at Different Levels

```text
Explain Python variables at three levels:

Level 1:
For someone who has never programmed before.

Level 2:
For a student who already knows input/output.

Level 3:
Give a more detailed explanation involving variables, objects, and references.

Keep the three levels clearly separated.
```

### 17.4. Create Lecture Notes with Example Code

```text
Create a lecture note on Python input/output for beginners.

Each section should include:

- concept;
- syntax;
- short code example;
- corresponding output;
- line-by-line explanation;
- common mistake;
- mini exercise.

Do not use:
- if;
- loops;
- functions;
- lists.
```

### 17.5. Add Self-Check Questions to Lecture Notes

```text
After every lecture-note section, add:

### Self-check

Include:
- 2 conceptual questions;
- 1 Predict the Output question;
- 1 Find the Bug question.

Do not show the answers immediately.

Place the answers at the end of each section.
```

For Markdown:

```text
Put the self-check answers inside:

<details>
<summary>Answer</summary>

...

</details>
```

### 17.6. Create Lecture Notes from Your Own Questions

```text
These are questions I asked while studying Python:

- What type does input() return?
- How does int(input()) work?
- Why does string + int cause an error?
- What is a variable in Python?

Organize them into a short lecture note.

Put the concepts in a logical order.

Each section should contain:
- explanation;
- example;
- self-check question.
```

---

## 18. Verify AI-Generated Lecture Notes

An AI-generated lecture note is **not automatically correct**.

Check:

- [ ] Does the content match the original lecture?
- [ ] Did AI add content that was not in the source?
- [ ] Does all example code run correctly?
- [ ] Are the shown outputs correct?
- [ ] Are the technical terms accurate?
- [ ] Is any content too advanced for the current lesson?
- [ ] Do the examples actually illustrate the intended concept?

A useful verification prompt:

```text
Review the lecture note you just created.

For each technical claim:
- check its correctness;
- check the code;
- identify content that is inferred or added;
- do not introduce new material.
```

Whenever possible, compare AI-generated notes with:

- instructor slides;
- textbooks;
- Python documentation;
- actual program execution.

---

## 19. Technique 11 — Ask AI to Increase Difficulty Gradually

```text
Create a 5-level Python learning ladder.

Topics:
- input;
- output;
- variables;
- arithmetic operators.

Level 1: very basic
Level 2: basic
Level 3: combines several calculations
Level 4: real-world problem
Level 5: integrated problem

Do not use if statements, loops, or functions.

Do not provide solutions.
```

---

## 20. Technique 12 — Learn with the Socratic Method

```text
I am solving this problem:

"Read a Celsius temperature and convert it to Fahrenheit."

I do not know how to start.

Do not give me the formula or code immediately.

Guide me using questions.

Ask only one question at a time.
```

In this mode, AI does not solve the problem for the learner. It **guides the reasoning process**.

---

## 21. Workflow: Build a Complete Learning Package with AI

A useful use of AI is to create a **learning package** for one topic.

```text
I am self-studying Python input and output.

Help me create a learning package containing:

1. A short lecture note
2. 3 examples
3. 5 self-check questions
4. 5 quiz questions
5. 3 practice exercises
6. One integrated exercise
7. A knowledge checklist

Requirements:
- suitable for beginners;
- no if statements;
- no loops;
- no functions;
- do not show quiz answers immediately.
```

Recommended sequence:

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

## 22. Integrated Lab — Learn One Python Topic with ChatGPT

Choose one topic:

- Variables
- Data Types
- Input/Output
- Arithmetic Operators

### Step 1 — Self-Assessment

```text
What do I already know about this topic?
What do I still not understand?
```

### Step 2 — Create a Mini Lecture Note

```text
Create a mini lecture note on [TOPIC].

Include:
- concepts;
- syntax;
- examples;
- common mistakes;
- self-check questions.

Make it suitable for a Python beginner.
```

### Step 3 — Verify the Lecture Note

Run every code example.

Record anything that is:

- incorrect;
- unclear;
- too advanced.

### Step 4 — Explain Back

Write:

```text
My understanding is:
...
```

Then ask AI to check your explanation.

### Step 5 — Generate a Quiz

```text
Create 8 quiz questions based on the lecture note above.

Include:
- Multiple Choice;
- Predict the Output;
- Find the Bug;
- Explain.

Do not show the answers.
```

### Step 6 — Take the Quiz

Answer every question before asking AI to grade it.

### Step 7 — Practice

```text
Give me 3 short exercises on the topic I just learned.

Do not provide solutions.
```

### Step 8 — Debug or Review

If the code is wrong:

```text
Give me Hint 1.
```

If the code is correct:

```text
Review my code and ask me one question to check
whether I truly understand my solution.
```

### Step 9 — Generate the Next Exercise

Ask AI for a similar exercise that is slightly more difficult.

---

## 23. Recommended AI-Assisted Python Self-Study Workflow

```text
1. READ
   Read the lecture
      ↓
2. BUILD NOTES
   Create or organize lecture notes
      ↓
3. EXPLAIN
   Explain the concept yourself
      ↓
4. ASK
   Ask AI about unclear points
      ↓
5. PREDICT
   Predict program output
      ↓
6. QUIZ
   Self-assess
      ↓
7. CODE
   Write your own program
      ↓
8. TEST
   Run and test
      ↓
9. DEBUG
   Ask for hints if needed
      ↓
10. REVIEW
    Ask AI to review
      ↓
11. PRACTICE
    Solve a new problem
      ↓
12. REFLECT
    Summarize knowledge and mistakes
```

---

## 24. AI Use Patterns That Are Not Recommended

### Copy the Entire Problem

```text
Solve this.
```

### Copy Code Without Understanding It

A program that runs is not necessarily a program you understand.

### Ask for Quiz Answers Immediately

Looking at the answers before attempting the quiz removes much of its learning value.

### Ask AI to Create an Entire Lecture Without a Source

AI may:

- add material not yet taught;
- omit important material;
- use terminology different from the instructor;
- produce examples that are too advanced.

### Assume AI Is Always Correct

Every AI output should go through:

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

## 25. Prompt Toolkit for Python Students

### Learn a Concept

```text
I am new to Python.

Explain [CONCEPT].

Include:
1. a definition;
2. one example;
3. one common beginner mistake;
4. one self-check question.

Do not use advanced concepts.
```

### Ask for a Hint

```text
I am working on this exercise:

[PROBLEM]

This is what I have tried:

[CODE/IDEA]

Give me Hint 1 only.

Do not provide the solution.
```

### Debug

```text
Code:

[CODE]

Error:

[ERROR]

Expected:

[EXPECTED RESULT]

Explain the cause and help me find the fix myself.
```

### Review Code

```text
Here is the code I wrote:

[CODE]

Please review:
1. correctness;
2. readability;
3. logic errors;
4. edge cases.

Do not rewrite the whole program unless necessary.
```

### Generate a Quiz

```text
Create 10 quiz questions on [TOPIC].

Include:
- 4 Multiple Choice;
- 3 Predict the Output;
- 2 Find the Bug;
- 1 Explain.

Do not show the answers first.
```

### Create a Lecture Note

```text
Based on the following material:

[LECTURE CONTENT]

Create a lecture note containing:

1. Learning objectives
2. Concepts
3. Explanations
4. Examples
5. Common mistakes
6. Self-check
7. Exercises
8. Summary

Do not add material beyond the source unless clearly labeled.
```

### Create a Review Package

```text
Based on this lecture note, create:

- one summary;
- 10 flashcards;
- 10 quiz questions;
- 5 Predict the Output questions;
- 3 Find the Bug questions;
- 5 exercises.

Do not provide the answers immediately.
```

---

## 26. Lab Report

Students submit:

### 1. Topic Studied

```text
...
```

### 2. Prompt Used to Create the Lecture Note

```text
...
```

### 3. Lecture Note After Student Verification/Revision

```text
...
```

### 4. One AI Explanation That Was Unclear or Incorrect

```text
...
```

### 5. Quiz-Generation Prompt

```text
...
```

### 6. Quiz Result

```text
Score:
...

Incorrect questions:
...
```

### 7. Knowledge Gaps Identified by the Quiz

```text
...
```

### 8. One Python Error That AI Helped Diagnose

```text
...
```

### 9. Final Code Written by the Student

```python
...
```

### 10. One New Exercise Generated by AI

```text
...
```

### 11. Reflection

```text
What I learned:

...

What I still do not understand:

...

Mistakes I often make:

...
```

---

## 27. Self-Assessment

| Skill | Not Yet | With Help | Independently |
|---|:---:|:---:|:---:|
| Write a clear prompt | ☐ | ☐ | ☐ |
| Ask AI for explanations | ☐ | ☐ | ☐ |
| Create lecture notes | ☐ | ☐ | ☐ |
| Verify lecture notes | ☐ | ☐ | ☐ |
| Generate quizzes | ☐ | ☐ | ☐ |
| Use quizzes to identify learning gaps | ☐ | ☐ | ☐ |
| Ask for hints instead of solutions | ☐ | ☐ | ☐ |
| Debug with AI | ☐ | ☐ | ☐ |
| Review code | ☐ | ☐ | ☐ |
| Verify AI output | ☐ | ☐ | ☐ |
| Generate additional practice | ☐ | ☐ | ☐ |

---

## 28. The 5T Principle for Learning Python with AI

### 1. Think

Think before asking AI.

### 2. Try

Attempt the problem yourself.

### 3. Talk

Ask AI specifically about what is difficult.

### 4. Test

Do not assume the AI answer is correct.

### 5. Teach-back

Explain the concept or solution again in your own words.

---

## 29. The Most Important Rule

> **Never submit code that you cannot explain.**

Similarly:

> **Never study an AI-generated lecture note without checking it.**

and:

> **Do the quiz before looking at the answers.**

A lesson is truly complete when you can:

1. explain the concept;
2. predict program behavior;
3. write your own code;
4. test the code;
5. identify and fix errors;
6. answer quiz questions;
7. explain the material again without relying on AI.

---

## 30. Conclusion

ChatGPT can play several roles:

```text
ChatGPT
   │
   ├── Tutor
   │     └── Explain concepts
   │
   ├── Lecture-note Assistant
   │     └── Organize learning materials
   │
   ├── Quiz Generator
   │     └── Check understanding
   │
   ├── Questioner
   │     └── Ask diagnostic questions
   │
   ├── Coach
   │     └── Provide hints
   │
   ├── Debugging Assistant
   │     └── Support debugging
   │
   ├── Reviewer
   │     └── Review code
   │
   └── Practice Generator
         └── Create new exercises
```

Use this role sparingly:

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

Prefer this workflow:

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

The final goal is not:

> **How much code can AI write for you?**

The better question is:

> **After using AI, can you explain, write, test, and fix more Python programs by yourself?**
