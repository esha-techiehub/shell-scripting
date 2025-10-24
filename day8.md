
# 🐚 Shell Scripting Fundamentals  
## Quoting Mechanisms: Single Quotes, Double Quotes, Backticks  
### Plus: Command Substitution & Variable Substitution

---

## 🧠 Why Quoting Matters in Shell Scripting

In Linux shell, **quotes** tell the shell **how to interpret special characters, variables, and commands** inside a string.  

Without proper quoting, your script may:
- Misinterpret spaces
- Expand variables unintentionally
- Fail to run embedded commands properly

So, understanding **quoting rules** helps you write clean, predictable, and bug-free scripts.

---

## 🧩 Three Main Quoting Mechanisms

| Type | Symbol | Purpose |
|------|---------|----------|
| **Single Quotes** | `' '` | Protect everything inside; no variable or command expansion |
| **Double Quotes** | `" "` | Allow variable and command expansion but prevent word splitting |
| **Backticks** | `` ` ` `` | Used for command substitution (old syntax) |

---

## 🔸 1️⃣ Single Quotes `' '`

### 💬 Definition:
Anything inside **single quotes** is treated **literally** by the shell —  
**no variable expansion, no command substitution, no escape characters** work inside.

### 🔹 Syntax:
```bash
echo 'This is a single-quoted string'
```

### 🧪 Example 1 — Literal String
```bash
name="Eshwari"
echo 'Hello $name, welcome!'
```
✅ Output:
```
Hello $name, welcome!
```

💡 **Explanation:**  
The `$name` is **not replaced** because single quotes tell the shell:  
> “Treat everything between quotes as plain text.”

---

### 🧪 Example 2 — Protect Special Characters
```bash
echo 'Price is $100 & offer ends soon!'
```
✅ Output:
```
Price is $100 & offer ends soon!
```

### ✅ When to Use Single Quotes
- When you want to **print exact text** without interpreting `$`, `*`, or `` ` ` ``.
- When handling **regular expressions** or **special characters**.
- When writing **static text** in scripts.

---

## 🔸 2️⃣ Double Quotes `" "`

### 💬 Definition:
Double quotes **protect text partially**:
- They **preserve spaces and special characters**,  
- But **allow variables and command substitution** (`$variable`, `$(command)`).

---

### 🔹 Syntax:
```bash
echo "Welcome $USER, today is $(date)"
```

### 🧪 Example 1 — Variable Expansion
```bash
name="Eshwari"
echo "Hello $name, welcome to Shell Scripting!"
```
✅ Output:
```
Hello Eshwari, welcome to Shell Scripting!
```

### 🧪 Example 2 — Command Substitution Inside Double Quotes
```bash
echo "Current directory is $(pwd)"
```
✅ Output:
```
Current directory is /home/student
```

### ✅ When to Use Double Quotes
- When using **variables or commands** inside strings.
- When text contains **spaces** but still needs expansion.
- When writing **dynamic messages or logs**.

---

## 🔸 3️⃣ Backticks `` ` ` ``

### 💬 Definition:
Backticks (also called **grave accents**) are used for **command substitution**,  
meaning the **output of a command** replaces the command itself.

Example:
```bash
echo "Today is: `date`"
```
✅ Output:
```
Today is: Fri Oct 25 10:30:45 IST 2025
```

---

### ⚙️ How Command Substitution Works
- The shell executes the command inside backticks.
- It captures the **output** of that command.
- Then it replaces the backtick expression with that output.

### ⚠️ Limitation of Backticks
- Difficult to **nest** (use one command inside another).  
- Hard to **read** in complex scripts.

Hence, the modern syntax `$(command)` is **preferred**.

---

## 🔹 Modern Command Substitution — `$(command)`

This is the **new and recommended syntax** to perform command substitution.  
It’s easier to read and supports nesting.

### 🧪 Example — Using `$(command)`
```bash
current_date=$(date)
echo "Current date and time: $current_date"
```
✅ Output:
```
Current date and time: Fri Oct 25 10:35:15 IST 2025
```

### 🧪 Example — Nested Command Substitution
```bash
echo "Today is $(date +%A), and you are in $(pwd)"
```
✅ Output:
```
Today is Friday, and you are in /home/student
```

---

## 💡 Difference Between Backticks and $( )

| Feature | Backticks (`` `command` ``) | `$(command)` |
|----------|----------------------------|---------------|
| Readability | Hard to read | Easy to read |
| Nesting | Difficult | Easy |
| Modern Standard | Deprecated | Recommended |
| Example | ``echo `date` `` | `echo $(date)` |

---

## 🧩 Variable Substitution

Variable substitution means **replacing a variable name with its actual value** when the script runs.  

Whenever the shell sees `$variable`, it replaces it with the **stored value**.

### 🧪 Example — Basic Variable Substitution
```bash
name="Eshwari"
echo "Hello $name"
```
✅ Output:
```
Hello Eshwari
```

### 🧪 Example — Using Curly Braces `{ }` for Clarity
```bash
course="DevOps"
echo "You are learning ${course}Engineering"
```
✅ Output:
```
You are learning DevOpsEngineering
```

💡 Curly braces `{}` help **separate variable names** from surrounding text.

### 🧪 Example — Default or Fallback Value
```bash
echo "User: ${USER:-Unknown}"
```
✅ Output:
```
User: eshwari
```

### 🧪 Example — Variable Substitution with Command Substitution
```bash
files=$(ls)
echo "Files in current directory: $files"
```
✅ Output:
```
Files in current directory: script.sh notes.txt image.png
```

---

## 🔁 Combining Quoting + Substitution

### 🧪 Example — Single Quotes (No Expansion)
```bash
name="Esha"
echo 'Hello $name, today is $(date)'
```
✅ Output:
```
Hello $name, today is $(date)
```

### 🧪 Example — Double Quotes (With Expansion)
```bash
name="Esha"
echo "Hello $name, today is $(date)"
```
✅ Output:
```
Hello Esha, today is Fri Oct 25 10:40:52 IST 2025
```

---

## 🧠 Summary Table

| Concept | Syntax | Expands Variables | Expands Commands | Preserves Spaces |
|----------|---------|------------------|------------------|------------------|
| **Single Quotes** | `'text'` | ❌ | ❌ | ✅ |
| **Double Quotes** | `"text"` | ✅ | ✅ | ✅ |
| **Backticks** | `` `command` `` | N/A | ✅ | ✅ |
| **$(command)** | `$(command)` | N/A | ✅ | ✅ |
| **Variable Substitution** | `$variable`, `${variable}` | ✅ | ❌ | ✅ |

---

## 🌟 Real-Time DevOps Example — Auto Log Generator
```bash
#!/bin/bash
USER_NAME=$USER
DATE=$(date +%F_%H-%M-%S)
HOST=$(hostname)
LOG_FILE="/var/log/${HOST}_${USER_NAME}_${DATE}.log"

echo "Log generated by $USER_NAME on $HOST at $(date)" > $LOG_FILE
echo "System uptime:" >> $LOG_FILE
uptime >> $LOG_FILE

echo "✅ Log file created: $LOG_FILE"
```
✅ **Uses:**
- **Double Quotes** → variable & command expansion  
- **$(command)** → command substitution  
- **${variable}** → variable substitution inside filenames  

---
