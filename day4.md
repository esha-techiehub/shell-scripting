
# 🐚 Creating and Executing Shell Scripts  
### (Including Shebang Line `#!/bin/bash` and File Permissions using `chmod`)

---

## 🧠 What is a Shell Script?

A **Shell Script** is a **text file** that contains a **set of Linux commands** that you want the computer to execute automatically — one after another.

👉 Instead of typing each command manually in the terminal every time,  
you can **save all commands in one file** and **run that file** whenever needed.

---

### 💡 Example in Real Life:
Imagine you need to:
1. Create a backup folder,  
2. Copy files, and  
3. Show a success message.

You could type all three commands one by one every day —  
**OR** you could put them all in one file (a shell script) and just run it once.

That’s the power of Shell Scripting. 💪

---

## 🧩 Step 1: Create a New Shell Script File

You can create a new file using any text editor such as **nano** or **vi**.

```bash
nano my_first_script.sh
```

This opens a text editor in the terminal.

---

## 🧭 Step 2: The Shebang Line — `#!/bin/bash`

The **first line** of every shell script usually starts with this line:

```bash
#!/bin/bash
```

### 🔍 What is the Shebang Line?

- `#!` → is called a **Shebang** or **Hashbang**.  
- `/bin/bash` → tells the system **which shell interpreter** should run the commands inside your script.

So the full line means:
> “Hey system, please use the **Bash shell** to execute everything in this script.”

---

### 💬 Why the Shebang Line is Important

| Purpose | Explanation |
|----------|--------------|
| **Interpreter Specification** | Tells the OS which shell to use (bash, zsh, python, etc.) |
| **Portability** | Ensures your script runs correctly even if different shells exist on a system |
| **Automation** | Allows scripts to run from anywhere without manually specifying the shell each time |

---

### 🧪 Example:

**File: `greet.sh`**

```bash
#!/bin/bash
echo "Hello, welcome to Shell Scripting!"
echo "Today is: $(date)"
```

---

## 🧩 Step 3: Save and Exit

- In **nano**, press:
  ```
  CTRL + O → Enter → CTRL + X
  ```
  (This saves the file and exits the editor)

---

## 🧩 Step 4: Make the Script Executable — Using `chmod`

After creating your script, it’s **just a text file**.  
To make it **executable** (runnable like a program), you must change its **permissions**.

That’s where `chmod` comes in.

---

### 🔐 What is `chmod`?

`chmod` stands for **Change Mode** — it changes the **permissions** of a file.

Every file in Linux has three sets of permissions:
1. **Owner (user who created it)**
2. **Group (users in same group)**
3. **Others (everyone else)**

Each can have:
- `r` → read  
- `w` → write  
- `x` → execute

---

### 🧮 File Permission Example

To **allow execution**, you use:

```bash
chmod +x greet.sh
```

✅ This means:  
> “Add execute permission (`x`) to the file greet.sh.”

---

### 🧾 Verify the Permissions

Run:
```bash
ls -l greet.sh
```

Output:
```
-rwxr-xr-- 1 eshwari staff 123 Oct 24 18:22 greet.sh
```

Explanation:
- `rwx` → owner can read, write, execute  
- `r-x` → group can read and execute  
- `r--` → others can only read  

Now your script can be executed!

---

## 🧩 Step 5: Execute (Run) the Script

You can run it in two ways:

### ✅ Option 1 — Directly run from current directory:
```bash
./greet.sh
```

🔹 `./` means “current directory” (where the file is located).

### ✅ Option 2 — Run using Bash explicitly:
```bash
bash greet.sh
```

Both methods will display:
```
Hello, welcome to Shell Scripting!
Today is: Fri Oct 24 18:25:10 IST 2025
```

---

## 🧠 Why We Need `chmod` Before Running

| Purpose | Description |
|----------|--------------|
| **Security** | Prevents accidental execution of unwanted scripts. |
| **Control** | Only authorized users can run or modify the script. |
| **System Protection** | Linux doesn’t run unknown files unless you grant permission. |

Without `chmod +x`, if you try to run the script, you’ll get:
```
bash: ./greet.sh: Permission denied
```

---

## ⚙️ Example 2 — Script with Logic & Variables

```bash
#!/bin/bash
# This script checks if a folder exists

FOLDER="/home/student/project"

if [ -d "$FOLDER" ]; then
    echo "✅ The folder exists: $FOLDER"
else
    echo "❌ The folder does not exist. Creating now..."
    mkdir "$FOLDER"
    echo "Folder created successfully!"
fi
```

### 🧩 Explanation:
- `if [ -d "$FOLDER" ]` → Checks if directory exists.  
- `mkdir` → Creates a new directory if not found.  
- `$FOLDER` → Variable that stores the folder path.  
- `echo` → Prints output messages.  

---

## 🕰️ When We Use Shell Scripts in Real Time

| Use Case | Description |
|-----------|--------------|
| **Automation** | Daily backups, log cleanup, server monitoring |
| **DevOps Pipelines** | Used in Jenkins, GitHub Actions, or Azure DevOps steps |
| **System Maintenance** | Checking memory, CPU, disk usage automatically |
| **Software Installation** | Automating setup (Apache, Nginx, Docker, etc.) |
| **File Operations** | Compressing, moving, renaming, or deleting files on schedule |

---

## 📦 Example 3 — Automated Backup Script

```bash
#!/bin/bash
# Automated Backup Script

SRC="/home/student/docs"
DEST="/home/student/backup"
DATE=$(date +%F_%H-%M-%S)
FILENAME="backup_$DATE.tar.gz"

mkdir -p $DEST
tar -czf $DEST/$FILENAME $SRC

echo "Backup created successfully at $DEST/$FILENAME"
```

✅ **Output:**
```
Backup created successfully at /home/student/backup/backup_2025-10-24_18-30-20.tar.gz
```

---

## 🧰 Quick Reference Table

| Step | Command | Description |
|------|----------|--------------|
| 1️⃣ | `nano script.sh` | Create script file |
| 2️⃣ | `#!/bin/bash` | Shebang line to define shell |
| 3️⃣ | `chmod +x script.sh` | Give execute permission |
| 4️⃣ | `./script.sh` | Run script |
| 5️⃣ | `ls -l` | Check file permissions |
| 6️⃣ | `echo`, `mkdir`, `tar` | Common commands used inside scripts |

---

## 🌟 Summary

| Concept | Description |
|----------|--------------|
| **Shell Script** | A file containing multiple Linux commands to automate tasks |
| **Shebang (`#!/bin/bash`)** | Tells system which shell to use |
| **chmod +x** | Grants execute permission to run the script |
| **Execution Methods** | `./script.sh` or `bash script.sh` |
| **Use Cases** | Automation, system monitoring, backups, DevOps tasks |
| **Benefit** | Saves time, reduces human error, increases efficiency |

---
