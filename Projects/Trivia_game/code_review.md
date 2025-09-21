# Quiz App - Code Review & Improvement Guide

This document provides a detailed code review of the Quiz App project, highlighting strengths, issues, and suggestions for improvement.

---

## 1. Project Structure

### Current Structure
```
Trivia_game/
├── Questions/
│   ├── question_display.py
│   └── Question_list.json
└── quiz/
    └── quiz.py
```

### Recommendations
- Rename `question_display.py` → `questions.py` for clarity
- Move JSON files into a dedicated `data/` folder
- Separate **data loading**, **question logic**, and **game loop** for better modularity

### Improved Structure
```
Trivia_game/
├── data/
│   └── questions.json
├── questions/
│   └── questions.py
└── quiz/
    └── main.py
```

---

## 2. `question_display.py` Review

### Strengths
- Correctly reads JSON files using `os.path.join`
- Functions exist to print and retrieve question data
- Random question selection logic is present

### Issues & Suggestions

#### 1. Global Variable Usage
**Current Issue:**
```python
data = read_question_from_file()
```
⚠️ Makes code less flexible and harder to test.

**Suggestion:** Pass data explicitly to functions or encapsulate in a class.

#### 2. `print_question()` Function
**Current Issue:**
```python
for key, value in question.items():
    print(f"ID: {key}")
    print(f"Question: {value['question']}")
    print(f"Options: {', '.join(value['options'])}")
```
Assumes each question dict has only one key.

**Better Approach:**
```python
def print_question(question):
    print(f"ID: {question['id']}")
    print(f"Question: {question['question']}")
    print(f"Options: {', '.join(question['options'])}")
```

#### 3. `question_engine()` Function
**Issues:**
- Only returns the first key/value; assumes one question per dict
- Unclear function name

**Suggestion:** Rename to `get_question_by_index()` for clarity.

**Example:**
```python
def get_question_by_index(data, index):
    q = data[index]
    key = list(q.keys())[0]
    val = q[key]
    return {
        "id": key,
        "question": val["question"],
        "options": val["options"],
        "answer": val["answer"]
    }
```

#### 4. Random Question Selection
**Current Issue:** `randrange(10)` assumes exactly 10 questions.

**Better Approach:**
```python
from random import choice
question = choice(data)
```

---

## 3. `quiz.py` Review

### Strengths
- Main game loop is simple and readable
- `update_score()` function returns updated score and correctness flag

### Issues & Suggestions

#### 1. Repeated String Literals
**Current:**
```python
user_input = input("Do you wish to keep the quiz running: (Yes/No) Or Enter:  ")
```

**Better:** Normalize input:
```python
user_input = input("Do you want to continue? (yes/no): ").strip().lower()
```

#### 2. Variable Issues
**Problems:**
```python
curent_score, Flag = update_score(user_answer, actual_anwer, total_score)
```
- Typo: `curent_score` → `current_score`
- Use snake_case: `Flag` → `flag`

#### 3. Score Logic
Returning `current_score` is unnecessary; consider returning only correctness flag and updating score in main loop.

#### 4. Inappropriate Messages
**Current:**
```python
print("You fucked up !!!!! ", total_score)
```
⚠️ Avoid profanity.

**Replace with:**
```python
print("Incorrect! Your score:", total_score)
```

#### 5. Modularization
The game loop does too much. Suggested structure:
```python
def play_round(question_data):
    # Handle one round of quiz
    return correct  # or updated score
```

#### 6. Input Handling
Currently requires exact string match for answers.
**Suggestion:** Allow selecting by option number and ignore case.

#### 7. Remove Unused Code
Commented functions like `while_loops_practise()` should be removed or moved to separate practice files.

---

## 4. Suggested Improvements & Best Practices

### Code Quality
- **Avoid globals** – pass data as parameters
- **Use dataclasses** for questions:
```python
from dataclasses import dataclass
from typing import List

@dataclass
class Question:
    id: str
    question: str
    options: List[str]
    answer: str
```

### Testing & Maintenance
- **Unit tests** – test JSON loading, score updating, and random selection
- **Separate logic & I/O** – makes testing and maintenance easier

### User Experience
- **Random question selection** – use `choice(data)` instead of hard-coded ranges
- **Normalize input** – `strip()` and `lower()` to avoid case mismatch
- **Improve messages** – user-friendly and professional

### Project Organization
- **Folder & file naming** – clear and consistent for maintainability

---

## 5. Summary

The project is a solid starting point for a quiz app. Key areas for improvement:

1. **Reduce reliance on globals**
2. **Modularize game logic and question handling**
3. **Normalize user input and improve feedback messages**
4. **Use dataclasses and better naming for readability**
5. **Make project folder structure cleaner and scalable**

Applying these suggestions will make the code more maintainable, testable, and easier to extend in the future.