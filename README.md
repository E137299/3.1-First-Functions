# 3.1-First-Functions

### **Challenge 1: Sum of Two Numbers**
**Task:**
Write a function called sum_two_numbers(a, b) that takes two numbers as parameters and returns their sum.

```python
def sum_two_numbers(a, b):
    # your code
```
**Example Usage:**

```python
#Example 1
result = sum_two_numbers(5, 10)
print(result)  # Output should be 15

#Example 2
print(sum_two_numbers(100,1)) # Output should be 101

```

<br></br>
---
### **Challenge 2: Check Even or Odd**
**Task:**

Write a function called is_even(number) that takes a single integer as a parameter. The function should return True if the number is even, and False if the number is odd.

```python
def is_even(number):
    # your code
```
**Example Usage:**
```python
#Example 1
value = is_even(4))  
print(value)# Output: True

#Example 2
print(is_even(7))  # Output: False
```

<br></br>
---
### **Challenge 3: Absolute Difference**
**Task:**  
Write a function `absolute_difference(a, b)` that takes two numbers and returns the absolute difference between them (the difference without regard to negative values).

```python
def absolute_difference(a, b):
    # your code
```

**Example Usage:**

```python
#Example 1
difference = absolute_difference(10, 4)
print(difference)  # Output: 6

#Example 2
print(absolute_difference(4, 10))  # Output: 6
```

<br></br>
---
### **Challenge 4: Determine Largest of Three Numbers**

**Task:**  
Write a function `largest_of_three(x, y, z)` that takes three numbers as input and returns the largest of the three. You are not allowed to use loops or any built-in functions like `max()`.

```python
def largest_of_three(x, y, z):
    # your code
```

**Example Usage:**

```python
#Example 1
largest = largest_of_three(3, 7, 5)
print(largest)  # Output: 7

#Example 2
print(largest_of_three(10, 10, 9))  # Output: 10
```
<br></br>
---

### **Challenge 5: Is It a Vowel?**

**Task:**  
Write a function `is_vowel(c)` that takes a single character `c` as a parameter and returns `True` if it is a vowel (a, e, i, o, u, lowercase or uppercase), and `False` otherwise. You cannot use loops.

```python
def is_vowel(c):
    # your code
```

**Example Usage:**

```python
#Example 1
letter = is_vowel('A')
print(letter)  # Output: True

#Example 2
print(is_vowel('b'))  # Output: False
```
<br></br>
---

### **Challenge 6: Convert Temperature (Celsius to Fahrenheit)**

**Task:**  
Write a function `celsius_to_fahrenheit(c)` that takes a temperature in Celsius and converts it to Fahrenheit using the formula:  
°F = (°C × 9/5) + 32

```python
def celsius_to_fahrenheit(c):
    # your code
```

**Example Usage:**

```python
print(celsius_to_fahrenheit(0))  # Output: 32.0
print(celsius_to_fahrenheit(100))  # Output: 212.0
```
<br></br>
---

### **Challenge 7: Is It a Leap Year?**

**Task:**  
Write a function `is_leap_year(year)` that takes a year as a parameter and returns `True` if the year is a leap year, and `False` otherwise. A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

```python
def is_leap_year(year):
    # your code
```

**Example Usage:**

```python
#Example 1
leap = is_leap_year(2024)
print(leap)  # Output: True

#Example 2
print(is_leap_year(1900))  # Output: False
```

