# 🧪 String Calculator - TDD Kata in Python

This repository contains an implementation of the classic **String Calculator** Kata using **Test-Driven Development (TDD)** in Python. Each feature is built incrementally using tests first, followed by code and refactoring.

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.6+
- `unittest` (comes built-in with Python)

---

## 🧰 Project Structure


---

## ✅ Features (TDD Steps)

### Step-by-step functionality added:

1. ✅ Return `0` for an empty string
2. ✅ Return the number itself for a single number (e.g., `"5"` → `5`)
3. ✅ Add two comma-separated numbers (e.g., `"1,2"` → `3`)
4. ✅ Handle an unknown amount of comma-separated numbers
5. ✅ Support newline (`\n`) as a valid separator along with commas
6. ✅ Support custom delimiter in the format:  
   `//[delimiter]\n[numbers…]`  
   Example: `"//;\n1;2"` → `3`
7. ✅ Throw an exception for negative numbers with the message:  
   `"negative numbers not allowed: -1, -5"`
8. ✅ Show **all** negative numbers in the exception message

---

## 🧪 Running the Tests

Run all test cases:

```bash
python -m unittest discover
