
# 🐚 Shell Scripting Fundamentals  
## Variables: System-Defined, User-Defined & Special Variables

---

## 🧠 What is a Variable?

A **variable** in shell scripting is like a **container or storage box** that holds data temporarily while your script runs.  

You can store values like text, numbers, file paths, or command outputs in variables and reuse them throughout your script.

---

### 💬 In Simple Terms:

Think of it like **naming a cup** — instead of pouring water directly every time, you name the cup and use it whenever needed.  

Example:
```bash
name="Eshwari"
echo "Hello, $name"
```
Output:
```
Hello, Eshwari
```

Here:
- `name` → is the **variable name**
- `"Eshwari"` → is the **value stored**
- `$name` → is how you **access** the value stored in the variable.

---

## 🧩 Rules for Defining Variables

| Rule | Description |
|------|--------------|
| 1️⃣ | No spaces on either side of `=` (e.g., ✅ `x=10`, ❌ `x = 10`) |
| 2️⃣ | Variable names are **case-sensitive** (`Name` ≠ `name`) |
| 3️⃣ | Use only letters, digits, and underscores (`_`) |
| 4️⃣ | By convention, system variables use **uppercase**, user variables use **lowercase** |
| 5️⃣ | Access variable values using `$` before the name (e.g., `$USER`, `$name`) |

---

## 🧱 Types of Variables in Shell

There are **three major types of variables**:

| Type | Who Defines It | Example |
|------|----------------|----------|
| **1. System-defined variables** | Defined automatically by the shell | `$HOME`, `$USER`, `$PWD` |
| **2. User-defined variables** | Defined manually by the user | `name="Esha"`, `count=5` |
| **3. Special variables** | Automatically set when you run a script | `$0`, `$1`, `$#`, `$?`, `$$` |

---

## 🖥️ 1️⃣ System-Defined Variables (Environment Variables)

These are built-in variables that the **operating system or shell** creates automatically.  
They store useful system information such as username, home directory, shell type, etc.

### 📋 Common System Variables

| Variable | Description | Example Output |
|-----------|--------------|----------------|
| `$HOME` | Path of your home directory | `/home/eshwari` |
| `$USER` | Current logged-in user | `eshwari` |
| `$PWD` | Present working directory | `/home/eshwari/projects` |
| `$SHELL` | Default shell type | `/bin/bash` |
| `$PATH` | Directories to search for executable files | `/usr/local/bin:/usr/bin:/bin` |
| `$HOSTNAME` | Name of your computer | `ubuntu-server` |

---

### 🧪 Example — Viewing System Variables
```bash
#!/bin/bash
echo "User Name: $USER"
echo "Home Directory: $HOME"
echo "Current Working Directory: $PWD"
echo "Shell Type: $SHELL"
echo "System Hostname: $HOSTNAME"
```

✅ **Output:**
```
User Name: eshwari
Home Directory: /home/eshwari
Current Working Directory: /home/eshwari/scripts
Shell Type: /bin/bash
System Hostname: ubuntu-server
```

---

## 👩‍💻 2️⃣ User-Defined Variables

These are variables **you** create in your script to store and reuse data.

### 🧾 Example 1 — Simple User Variable
```bash
#!/bin/bash
name="Eshwari"
course="Linux Shell Scripting"
echo "Hi $name, welcome to the $course course!"
```
✅ **Output:**
```
Hi Eshwari, welcome to the Linux Shell Scripting course!
```

---

### 🧾 Example 2 — Numeric Variables and Arithmetic
```bash
#!/bin/bash
x=10
y=5
sum=$((x + y))
echo "The sum of $x and $y is $sum"
```
✅ **Output:**
```
The sum of 10 and 5 is 15
```

---

### 🧾 Example 3 — Storing Command Outputs in Variables
```bash
#!/bin/bash
current_date=$(date)
echo "Today's date and time: $current_date"
```
✅ **Output:**
```
Today's date and time: Fri Oct 24 18:50:32 IST 2025
```

---

## ⚙️ 3️⃣ Special Variables

These are **automatically created by the shell** when you **execute a script**.  
They hold information about the **script name, arguments, process ID, exit status, etc.**

### 🧩 Common Special Variables

| Variable | Meaning | Example |
|-----------|----------|----------|
| `$0` | The name of the current script | `./test.sh` |
| `$1, $2, $3...` | Command-line arguments passed to the script | `./script.sh arg1 arg2` |
| `$#` | Number of arguments passed | `2` |
| `$@` | All arguments as a list | `arg1 arg2` |
| `$?` | Exit status of last command (0 = success, non-zero = failure) | `0` |
| `$$` | Process ID (PID) of the current script | `12345` |
| `$!` | PID of last background command | `6789` |

---

### 🧪 Example — Using Command Line Arguments
```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total arguments: $#"
echo "All arguments: $@"
```
Run as:
```bash
./info.sh DevOps Linux
```
✅ **Output:**
```
Script name: ./info.sh
First argument: DevOps
Second argument: Linux
Total arguments: 2
All arguments: DevOps Linux
```

---

### 🧪 Example — Exit Status `$?`
```bash
#!/bin/bash
ping -c 1 google.com
if [ $? -eq 0 ]; then
    echo "Internet is working!"
else
    echo "Internet is down!"
fi
```
✅ **Output:**
```
Internet is working!
```

---

### 🧪 Example — Process ID `$$`
```bash
#!/bin/bash
echo "The current script process ID is $$"
```
✅ **Output:**
```
The current script process ID is 24567
```

---

## 🧰 Summary Table

| Type | Defined By | Examples | Use Case |
|------|-------------|----------|----------|
| **System-defined** | Shell or OS | `$USER`, `$HOME`, `$PWD`, `$SHELL`, `$PATH` | Access system details |
| **User-defined** | You | `name="Esha"`, `x=10` | Store reusable data |
| **Special variables** | Shell (auto) | `$0`, `$1`, `$#`, `$?`, `$$` | Get script arguments, status, PID |

---

## 🌟 Why Variables Are Important in Shell Scripts

| Benefit | Explanation |
|----------|--------------|
| **Reusability** | Store data once and reuse it anywhere in the script. |
| **Flexibility** | Adapt scripts easily by changing variable values. |
| **Automation** | Pass arguments dynamically to scripts. |
| **Dynamic Scripting** | Capture command outputs for real-time tasks (like date, logs). |
| **Error Handling** | Use `$?` to check success or failure of commands. |

---

## 💼 Real-Time Example: User Backup Script Using Variables
```bash
#!/bin/bash
# Backup Script using variables

USER_NAME=$USER
DATE=$(date +%F)
SRC="/home/$USER_NAME/Documents"
DEST="/home/$USER_NAME/backup_$DATE"

echo "Starting backup for user: $USER_NAME"
mkdir -p $DEST
cp -r $SRC $DEST

if [ $? -eq 0 ]; then
    echo "Backup completed successfully at $DEST"
else
    echo "Backup failed. Please check!"
fi
```
✅ **Output:**
```
Starting backup for user: eshwari
Backup completed successfully at /home/eshwari/backup_2025-10-24
```

---

## 🧠 Summary

| Concept | Description |
|----------|--------------|
| **Variable** | A container that holds data temporarily in a script. |
| **System Variables** | Predefined by OS (e.g., `$USER`, `$HOME`, `$PATH`). |
| **User Variables** | Created by user (`name="Esha"`). |
| **Special Variables** | Auto-assigned by shell (`$0`, `$1`, `$#`, `$?`, `$$`). |
| **Purpose** | Used for dynamic automation, data storage, error handling, and parameter passing. |

---
