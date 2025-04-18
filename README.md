# 🧪 String Calculator - TDD Kata in Python

This project is an implementation of the classic **String Calculator** TDD Kata using Python and the built-in `unittest` module. The goal is to develop the `add_strings()` function step by step through test-driven development (TDD), writing tests before writing code.

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.6+
- No external libraries required (uses built-in `unittest` and `re` modules)

---

## 🧰 Folder Structure

. ├── calculator.py # Main logic - contains the add_strings() function ├── test.py # Unit tests for add_strings() ├──


---

## ✅ Features Implemented

### 🔹 Basic Functionality
- ✅ Return `0` for an empty string
- ✅ Return the number itself for a single number (e.g., `"5"` → `5`)
- ✅ Add two comma-separated numbers (e.g., `"1,2"` → `3`)
- ✅ Add any number of comma-separated values

### 🔹 Support for Newlines
- ✅ Handle newline (`\n`) as an additional delimiter  
  Example: `"1\n2,3"` → `6`

### 🔹 Custom Delimiters
- ✅ Use custom delimiter from the string:  
  Format: `"//[delimiter]\n[numbers...]"`  
  Example: `"//;\n1;2"` → `3`

- ✅ Delimiters of any length:  
  Example: `"//[***]\n1***2***3"` → `6`

- ✅ Multiple delimiters:  
  Example: `"//[*][%]\n1*2%3"` → `6`

- ✅ Multiple delimiters with longer length:  
  Example: `"//[***][##]\n1***2##3"` → `6`

### 🔹 Edge Cases
- ✅ Ignore numbers bigger than 1000  
  Example: `"2,1001"` → `2`

- ✅ Throw exception for negative numbers:  
  Example: `"-1,2,-5"` → ❌ `"negative numbers not allowed: -1, -5"`

---

## 🧪 Running the Tests

Run all test cases:

```bash
python -m unittest test.py


---

## ✅ Features Implemented

### 🔹 Basic Functionality
- ✅ Return `0` for an empty string
- ✅ Return the number itself for a single number (e.g., `"5"` → `5`)
- ✅ Add two comma-separated numbers (e.g., `"1,2"` → `3`)
- ✅ Add any number of comma-separated values

### 🔹 Support for Newlines
- ✅ Handle newline (`\n`) as an additional delimiter  
  Example: `"1\n2,3"` → `6`

### 🔹 Custom Delimiters
- ✅ Use custom delimiter from the string:  
  Format: `"//[delimiter]\n[numbers...]"`  
  Example: `"//;\n1;2"` → `3`

- ✅ Delimiters of any length:  
  Example: `"//[***]\n1***2***3"` → `6`

- ✅ Multiple delimiters:  
  Example: `"//[*][%]\n1*2%3"` → `6`

- ✅ Multiple delimiters with longer length:  
  Example: `"//[***][##]\n1***2##3"` → `6`

### 🔹 Edge Cases
- ✅ Ignore numbers bigger than 1000  
  Example: `"2,1001"` → `2`

- ✅ Throw exception for negative numbers:  
  Example: `"-1,2,-5"` → ❌ `"negative numbers not allowed: -1, -5"`

---

## 🧪 Running the Tests

Run all test cases:

```bash
python -m unittest test.py


python -m unittest test.py TestStringCalculator.test_add_single_number
```
