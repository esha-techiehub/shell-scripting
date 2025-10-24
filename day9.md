
# 🐚 Shell Scripting Fundamentals  
## III. Control Flow Statements  
### Conditional Statements (`if`, `if-else`, `if-elif-else`, `case`)  
### Loops (`for`, `while`, `until`)  
### Loop Control (`break`, `continue`)

---

## 🧠 What are Control Flow Statements?

Control flow statements determine **which part of a script executes**, **how often**, and **under what conditions**.  
They allow your shell scripts to make **decisions** and **repeat tasks** automatically.

Example:
> If it’s raining, take an umbrella. Else, go outside freely.  

This everyday logic is implemented using control flow in shell scripting.

---

## 🧩 1️⃣ Conditional Statements

Conditional statements check **conditions** (true or false) and execute commands based on the result.

### Types
1. `if` statement  
2. `if-else` statement  
3. `if-elif-else` ladder  
4. `case` statement  

---

### 🔹 1.1 `if` Statement

**Syntax:**
```bash
if [ condition ]
then
   commands
fi
```

**Example:**
```bash
#!/bin/bash
age=20

if [ $age -ge 18 ]
then
  echo "You are eligible to vote."
fi
```
✅ Output:
```
You are eligible to vote.
```

**Explanation:**
- `[ $age -ge 18 ]` checks if age ≥ 18.  
- If true, code inside `then` runs.

---

### 🔹 1.2 `if-else` Statement

**Syntax:**
```bash
if [ condition ]
then
   commands_if_true
else
   commands_if_false
fi
```

**Example:**
```bash
#!/bin/bash
marks=45

if [ $marks -ge 50 ]
then
  echo "You passed!"
else
  echo "You failed. Try again!"
fi
```
✅ Output:
```
You failed. Try again!
```

---

### 🔹 1.3 `if-elif-else` Ladder

**Syntax:**
```bash
if [ condition1 ]
then
   commands1
elif [ condition2 ]
then
   commands2
else
   commands3
fi
```

**Example:**
```bash
#!/bin/bash
marks=82

if [ $marks -ge 90 ]
then
  echo "Grade: A"
elif [ $marks -ge 75 ]
then
  echo "Grade: B"
elif [ $marks -ge 50 ]
then
  echo "Grade: C"
else
  echo "Grade: F"
fi
```
✅ Output:
```
Grade: B
```

**Explanation:**  
Conditions are checked **top to bottom**; first match executes.

---

### 🔹 1.4 `case` Statement

Used when one variable has **multiple possible values**.

**Syntax:**
```bash
case $variable in
  pattern1)
     commands ;;
  pattern2)
     commands ;;
  *)
     default_commands ;;
esac
```

**Example:**
```bash
#!/bin/bash
echo "Enter a number between 1 and 3:"
read num

case $num in
  1)
    echo "You selected ONE" ;;
  2)
    echo "You selected TWO" ;;
  3)
    echo "You selected THREE" ;;
  *)
    echo "Invalid choice!" ;;
esac
```
✅ Output:
```
Enter a number between 1 and 3:
2
You selected TWO
```

---

## 🔁 2️⃣ Loops

Loops allow repetitive tasks without writing the same code multiple times.

### Types
1. `for` loop  
2. `while` loop  
3. `until` loop  

---

### 🔹 2.1 `for` Loop

Executes commands **for each value** in a list or range.

**Syntax:**
```bash
for variable in list
do
   commands
done
```

**Example 1 — Basic Loop**
```bash
for fruit in apple banana mango
do
  echo "I like $fruit"
done
```
✅ Output:
```
I like apple
I like banana
I like mango
```

**Example 2 — Range Loop**
```bash
for i in {1..5}
do
  echo "Number: $i"
done
```
✅ Output:
```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

---

### 🔹 2.2 `while` Loop

Repeats **as long as** a condition is true.

**Syntax:**
```bash
while [ condition ]
do
   commands
done
```

**Example:**
```bash
count=1
while [ $count -le 5 ]
do
  echo "Loop iteration: $count"
  ((count++))
done
```
✅ Output:
```
Loop iteration: 1
Loop iteration: 2
Loop iteration: 3
Loop iteration: 4
Loop iteration: 5
```

---

### 🔹 2.3 `until` Loop

Opposite of `while` — runs **until** a condition becomes true.

**Syntax:**
```bash
until [ condition ]
do
   commands
done
```

**Example:**
```bash
count=1
until [ $count -gt 5 ]
do
  echo "Count is $count"
  ((count++))
done
```
✅ Output:
```
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
```

---

## 🔂 3️⃣ Loop Control Statements

Used to **control or alter** loop execution.

### 🔸 `break` — Exit Loop Early

**Example:**
```bash
for i in {1..10}
do
  if [ $i -eq 5 ]
  then
    echo "Breaking at $i"
    break
  fi
  echo "Iteration $i"
done
```
✅ Output:
```
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Breaking at 5
```

💡 `break` stops the loop immediately when `$i = 5`.

---

### 🔸 `continue` — Skip Current Iteration

**Example:**
```bash
for i in {1..5}
do
  if [ $i -eq 3 ]
  then
    echo "Skipping $i"
    continue
  fi
  echo "Iteration $i"
done
```
✅ Output:
```
Iteration 1
Iteration 2
Skipping 3
Iteration 4
Iteration 5
```

💡 `continue` skips iteration 3 and moves to the next.

---

## 💼 Real-Time DevOps Example — Server Monitor
```bash
#!/bin/bash
SERVERS=("server1" "server2" "server3")

for s in "${SERVERS[@]}"
do
  echo "Pinging $s..."
  ping -c 1 $s > /dev/null 2>&1

  if [ $? -ne 0 ]; then
    echo "❌ $s is down!"
  else
    echo "✅ $s is up!"
  fi
done
```

✅ **Uses:**
- `for` loop — iterate servers  
- `if-else` — condition check  
- `break/continue` can be added for logic control

---

## 🧠 Summary Table

| Category | Type | Purpose | Example |
|-----------|------|----------|----------|
| **Conditional** | `if` | Single condition | `if [ $x -gt 10 ]; then echo "ok"; fi` |
|  | `if-else` | Two conditions | `if [ ]; then ... else ... fi` |
|  | `if-elif-else` | Multiple conditions | `if [ ]; then ... elif [ ]; fi` |
|  | `case` | Multiple options | `case $var in 1) ... ;; esac` |
| **Loops** | `for` | Repeat for list/range | `for i in {1..5}; do echo $i; done` |
|  | `while` | Repeat while true | `while [ $x -lt 5 ]; do ...; done` |
|  | `until` | Repeat until true | `until [ $x -gt 5 ]; do ...; done` |
| **Loop Control** | `break` | Exit loop early | `if [ $x -eq 5 ]; then break; fi` |
|  | `continue` | Skip iteration | `if [ $x -eq 3 ]; then continue; fi` |

---
