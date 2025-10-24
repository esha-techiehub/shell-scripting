
# 🐚 Shell Scripting Fundamentals  
## Operators: Arithmetic, Relational, Logical & Assignment

---

## 🧠 What are Operators?

In shell scripting, **operators** are special symbols or keywords that instruct the shell to perform operations on **variables and values**.  
They help in performing **calculations**, **comparisons**, and **logical decisions** within a script.

Think of them as tools that allow you to manipulate data and control the program’s logic.

---

## 🧩 Types of Operators

| Category | Purpose | Examples |
|-----------|----------|-----------|
| **1. Arithmetic Operators** | Perform mathematical calculations | `+ - * / % **` |
| **2. Relational Operators** | Compare two numbers or strings | `-eq -ne -gt -lt -ge -le` |
| **3. Logical Operators** | Combine multiple conditions | `&& || !` |
| **4. Assignment Operators** | Assign or modify variable values | `= += -= *= /=` |

---

## ⚙️ 1️⃣ Arithmetic Operators

Arithmetic operators are used for **mathematical calculations** such as addition, subtraction, multiplication, etc.

### 🔹 Common Arithmetic Operators

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `+` | Addition | `$((a + b))` | Sum of a and b |
| `-` | Subtraction | `$((a - b))` | Difference |
| `*` | Multiplication | `$((a * b))` | Product |
| `/` | Division | `$((a / b))` | Quotient |
| `%` | Modulus (remainder) | `$((a % b))` | Remainder |
| `**` | Exponentiation | `$((a ** b))` | a raised to b |

---

### 🧪 Example — Arithmetic
```bash
#!/bin/bash
a=10
b=5

echo "Addition: $((a + b))"
echo "Subtraction: $((a - b))"
echo "Multiplication: $((a * b))"
echo "Division: $((a / b))"
echo "Remainder: $((a % b))"
```

✅ Output:
```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2
Remainder: 0
```

💡 **Tip:** Use `$(( ))` for cleaner and modern arithmetic expressions.

---

## ⚖️ 2️⃣ Relational Operators

Relational operators compare **two numeric values** and return **true (0)** or **false (non-zero)**.  
They are mainly used inside **if conditions** for decision-making.

### 🔹 Common Relational Operators

| Operator | Meaning | Example | True When |
|-----------|----------|----------|------------|
| `-eq` | Equal to | `[ $a -eq $b ]` | a = b |
| `-ne` | Not equal to | `[ $a -ne $b ]` | a ≠ b |
| `-gt` | Greater than | `[ $a -gt $b ]` | a > b |
| `-lt` | Less than | `[ $a -lt $b ]` | a < b |
| `-ge` | Greater than or equal | `[ $a -ge $b ]` | a ≥ b |
| `-le` | Less than or equal | `[ $a -le $b ]` | a ≤ b |

---

### 🧪 Example — Relational Comparison
```bash
#!/bin/bash
a=8
b=12

if [ $a -lt $b ]
then
  echo "$a is less than $b"
else
  echo "$a is greater than or equal to $b"
fi
```
✅ Output:
```
8 is less than 12
```

---

### 🔹 String Comparisons (Bonus)

| Operator | Description | Example | True When |
|-----------|--------------|----------|------------|
| `=` | Strings are equal | `[ "$a" = "$b" ]` | Same content |
| `!=` | Strings are not equal | `[ "$a" != "$b" ]` | Different |
| `-z` | String is empty | `[ -z "$a" ]` | a is empty |
| `-n` | String is not empty | `[ -n "$a" ]` | a has value |

---

## 🔀 3️⃣ Logical Operators

Logical operators combine **multiple conditions** to build complex logic.

| Operator | Meaning | Example | True When |
|-----------|----------|----------|------------|
| `&&` | Logical AND | `[ $a -gt 5 ] && [ $b -lt 10 ]` | Both true |
| `||` | Logical OR | `[ $a -eq 10 ] || [ $b -eq 20 ]` | At least one true |
| `!` | Logical NOT | `[ ! $a -eq $b ]` | Condition false |

---

### 🧪 Example — Logical AND (&&)
```bash
#!/bin/bash
a=15
b=20

if [ $a -gt 10 ] && [ $b -lt 25 ]
then
  echo "Both conditions are true"
else
  echo "One or both are false"
fi
```
✅ Output:
```
Both conditions are true
```

---

### 🧪 Example — Logical OR (||)
```bash
#!/bin/bash
a=5
b=50

if [ $a -lt 10 ] || [ $b -lt 20 ]
then
  echo "At least one condition is true"
else
  echo "Both conditions are false"
fi
```
✅ Output:
```
At least one condition is true
```

---

### 🧪 Example — Logical NOT (!)
```bash
#!/bin/bash
a=10
b=20

if [ ! $a -eq $b ]
then
  echo "a and b are not equal"
else
  echo "a and b are equal"
fi
```
✅ Output:
```
a and b are not equal
```

---

## 🧮 4️⃣ Assignment Operators

Assignment operators are used to **assign** or **update** values of variables.

### 🔹 Common Assignment Operators

| Operator | Description | Example | Equivalent To |
|-----------|--------------|----------|----------------|
| `=` | Assign value | `a=10` | a = 10 |
| `+=` | Add and assign | `((a += 2))` | a = a + 2 |
| `-=` | Subtract and assign | `((a -= 2))` | a = a - 2 |
| `*=` | Multiply and assign | `((a *= 2))` | a = a * 2 |
| `/=` | Divide and assign | `((a /= 2))` | a = a / 2 |
| `%=` | Modulus and assign | `((a %= 3))` | a = a % 3 |

---

### 🧪 Example — Assignment in Action
```bash
#!/bin/bash
a=10

((a += 5))
echo "After addition: $a"

((a -= 3))
echo "After subtraction: $a"

((a *= 2))
echo "After multiplication: $a"

((a /= 3))
echo "After division: $a"
```
✅ Output:
```
After addition: 15
After subtraction: 12
After multiplication: 24
After division: 8
```

---

## 🧰 Combined Example — All Operators Together
```bash
#!/bin/bash
a=10
b=20

echo "Arithmetic:"
echo "Sum: $((a + b))"
echo "Product: $((a * b))"

if [ $a -lt $b ] && [ $b -ge 20 ]; then
    echo "Relational & Logical check: True"
fi

((a += 5))
echo "After assignment, a = $a"
```

✅ Output:
```
Arithmetic:
Sum: 30
Product: 200
Relational & Logical check: True
After assignment, a = 15
```

---

## 🧠 Summary

| Operator Type | Purpose | Example | Description |
|----------------|----------|----------|--------------|
| **Arithmetic** | Perform math operations | `$((a + b))` | Add, subtract, multiply, divide |
| **Relational** | Compare values | `[ $a -gt $b ]` | Greater, equal, less |
| **Logical** | Combine conditions | `[ $a -gt 5 ] && [ $b -lt 10 ]` | AND, OR, NOT |
| **Assignment** | Assign or modify variables | `((a += 2))` | Updates variable values |

---

## 🌟 Real-Time DevOps Example — Disk Monitoring Script
```bash
#!/bin/bash
THRESHOLD=80
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//')

if [ $USAGE -ge $THRESHOLD ]; then
    echo "⚠️  Disk usage high: $USAGE%"
else
    echo "✅ Disk usage normal: $USAGE%"
fi
```
✅ **Operators used:**
- `=` → assignment  
- `-ge` → relational (greater or equal)  
- `if` → logical control

---
