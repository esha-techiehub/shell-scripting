
# 🐚 Shell Scripting Fundamentals  
## Input and Output: echo, print, read, and I/O Redirection (<, >, >>, 2>)

---

## 🧠 What is Input and Output (I/O)?

In Shell scripting, **Input** and **Output** are two basic forms of communication between the **user** and the **system**.

| Concept | Description |
|----------|--------------|
| **Input (I)** | Data given **to** the script or command (from keyboard, file, or another command). |
| **Output (O)** | Information produced **by** the script (displayed on screen, stored in files, or passed to another command). |

In simple words:
- **Input** → data enters the program  
- **Output** → data leaves the program  

---

## 🧩 1️⃣ Displaying Output — `echo` and `printf`

These commands help you **display text or values** on the screen.

---

### 🗣️ `echo` Command

The **`echo`** command prints messages, variable values, or results on the terminal.

#### 🔹 Syntax:
```bash
echo [options] [string]
```

#### 🔹 Example:
```bash
echo "Welcome to Shell Scripting"
```
Output:
```
Welcome to Shell Scripting
```

---

### 🧪 Example — Printing Variable Values
```bash
name="Eshwari"
course="DevOps"
echo "Hello $name, you are learning $course"
```
Output:
```
Hello Eshwari, you are learning DevOps
```

---

### 🔹 Common `echo` Options

| Option | Meaning | Example | Output |
|---------|----------|----------|----------|
| `-n` | Don’t print new line | `echo -n "Hello "` | `Hello` (no new line) |
| `-e` | Enable escape characters | `echo -e "Line1\nLine2"` | Prints two lines |
| `\t` | Tab space | `echo -e "A\tB\tC"` | Columns separated by tabs |
| `\n` | New line | `echo -e "First Line\nSecond Line"` | Two separate lines |

---

### 🧪 Example with Escape Sequences
```bash
echo -e "Name:\tEshwari\nCourse:\tShell Scripting"
```
Output:
```
Name:    Eshwari
Course:  Shell Scripting
```

---

## 🖨️ `printf` Command

The **`printf`** command works like `echo` but offers **more formatting control**, similar to C programming.

#### 🔹 Syntax:
```bash
printf "format string" arguments
```

#### 🔹 Example:
```bash
printf "Name: %s\nAge: %d\n" "Eshwari" 25
```
Output:
```
Name: Eshwari
Age: 25
```

✅ `%s` → string, `%d` → number  
✅ `\n` → new line  

---

## 🧭 2️⃣ Taking Input from User — `read` Command

The **`read`** command allows the user to **enter data** during script execution.

#### 🔹 Syntax:
```bash
read [options] variable_name
```

---

### 🧪 Example 1 — Basic User Input
```bash
#!/bin/bash
echo "Enter your name: "
read name
echo "Welcome, $name!"
```
✅ Output:
```
Enter your name:
Eshwari
Welcome, Eshwari!
```

---

### 🧪 Example 2 — Multiple Inputs
```bash
read first last
echo "Hello $first $last"
```
✅ Input:
```
Esha S
```
✅ Output:
```
Hello Esha S
```

---

### 🧪 Example 3 — Input with Prompt in Same Line
Use `-p` option:
```bash
read -p "Enter your course name: " course
echo "You are learning $course"
```
✅ Output:
```
Enter your course name: Linux
You are learning Linux
```

---

### 🧪 Example 4 — Hide Password Input
Use `-s` (silent) option:
```bash
read -sp "Enter your password: " pass
echo
echo "Password entered successfully!"
```
✅ Output:
```
Enter your password:
Password entered successfully!
```
(The input is hidden while typing.)

---

## 🔁 3️⃣ Input and Output Redirection

By default:
- **Input** comes from the **keyboard** (`stdin`)
- **Output** goes to the **screen** (`stdout`)
- **Errors** are shown on the **screen** (`stderr`)

Redirection allows you to **change** these destinations:
- Send output to a **file**
- Take input from a **file**
- Redirect errors separately

---

### 🔹 3.1 Output Redirection — `>` and `>>`

#### 📤 Using `>` — Redirect and Overwrite
Redirects standard output to a file.  
If the file exists, it is **overwritten**.

Example:
```bash
echo "Hello, Shell!" > output.txt
```
✅ Creates `output.txt` with content:
```
Hello, Shell!
```

---

#### 📤 Using `>>` — Redirect and Append
Appends output to an existing file.  
If file doesn’t exist, creates one.

Example:
```bash
echo "This is the second line" >> output.txt
```
✅ Adds a new line **without erasing** previous content.

---

### 🔹 3.2 Input Redirection — `<`

Take input **from a file** instead of typing manually.

Example:
```bash
#!/bin/bash
while read line
do
  echo "Line from file: $line"
done < sample.txt
```

✅ Reads each line from `sample.txt` and prints it.

---

### 🔹 3.3 Error Redirection — `2>` and `2>>`

Redirect **error messages** into a file.

Example:
```bash
ls /no/such/file 2> error.log
```
✅ Saves the error message in `error.log`.

Append errors instead of overwriting:
```bash
ls /no/such/file 2>> error.log
```

---

### 🔹 3.4 Combine Output and Errors Together

Merge normal output and errors into one file:
```bash
command > output.log 2>&1
```

✅ `>` redirects normal output; `2>&1` sends errors to same place.

Example:
```bash
ls /etc /no/such/file > result.log 2>&1
```

✅ Both valid and error outputs are written into `result.log`.

---

### 🔹 3.5 Example — Combined Use Case
```bash
#!/bin/bash
echo "Starting backup process..."
tar -czf backup.tar /home/student > backup.log 2> error.log
echo "Backup complete. Check backup.log and error.log for details."
```

✅ Output:
- Normal messages → `backup.log`
- Errors → `error.log`

---

## 🧰 4️⃣ File Descriptors — Quick Theory

| Descriptor | Name | Meaning | Default |
|-------------|------|----------|----------|
| `0` | `stdin` | Standard Input | Keyboard |
| `1` | `stdout` | Standard Output | Screen |
| `2` | `stderr` | Standard Error | Screen |

So when you do:
- `> file` → redirects `stdout`
- `2> file` → redirects `stderr`
- `< file` → redirects `stdin`

---

## 🧠 Example Summary of Redirection Operators

| Operator | Function | Example | Description |
|-----------|-----------|----------|--------------|
| `>` | Redirect output (overwrite) | `echo "Hi" > file.txt` | Creates or replaces file |
| `>>` | Redirect output (append) | `echo "Hi" >> file.txt` | Adds to file end |
| `<` | Redirect input | `command < file.txt` | Reads input from file |
| `2>` | Redirect error (overwrite) | `ls /no/file 2> error.log` | Saves only errors |
| `2>>` | Redirect error (append) | `ls /no/file 2>> error.log` | Appends errors |
| `>&` | Combine streams | `command > all.log 2>&1` | Merges output + errors |

---

## 💼 Real-Life DevOps Example — Log and Error Handling
```bash
#!/bin/bash
LOG_FILE="/var/log/deploy.log"
ERROR_FILE="/var/log/deploy_error.log"

echo "Starting deployment..." > $LOG_FILE
kubectl apply -f app-deployment.yaml >> $LOG_FILE 2>> $ERROR_FILE

if [ $? -eq 0 ]; then
    echo "Deployment successful!" >> $LOG_FILE
else
    echo "Deployment failed. Check $ERROR_FILE for details." >> $LOG_FILE
fi
```

✅ **Explanation:**
- Normal output → `deploy.log`
- Errors → `deploy_error.log`
- `$?` checks command success or failure.

---

## 🧾 Summary

| Concept | Description | Example |
|----------|--------------|----------|
| **echo** | Prints simple text or variables | `echo "Hello"` |
| **printf** | Prints formatted output | `printf "Name: %s\n" "Esha"` |
| **read** | Takes input from user | `read name` |
| **>** | Redirects output (overwrite) | `echo "Hi" > file.txt` |
| **>>** | Redirects output (append) | `echo "Hi" >> file.txt` |
| **<** | Takes input from file | `command < file.txt` |
| **2>** | Redirects errors | `ls /no/file 2> error.log` |

---
