
# 💻 Basic Command Line Interface (CLI) Concepts  
## Navigation, File Management & Basic Commands

---

## 🧠 What is CLI (Command Line Interface)?

A **Command Line Interface (CLI)** is a **text-based interface** that allows users to **interact with the operating system directly by typing commands**.  
It’s different from GUI (Graphical User Interface), where you use a mouse and icons.

When you open a **terminal** (in Linux, macOS) or **PowerShell/CMD** (in Windows), you’re working inside a CLI environment.

---

## ⚙️ Why CLI is Important

| Reason | Description |
|--------|--------------|
| **Speed & Efficiency** | Typing commands is often faster than using GUI, especially for repetitive tasks. |
| **Automation** | CLI commands can be combined into scripts for automatic execution. |
| **Remote Access** | You can manage remote servers using tools like SSH. |
| **Fine Control** | CLI gives you low-level control over files, processes, and configurations. |
| **DevOps Requirement** | Tools like Docker, Kubernetes, Git, and AWS rely on CLI-based commands. |

---

## 🕰️ When Do We Use CLI?

| Scenario | Example |
|-----------|----------|
| **Server Management** | Connecting to cloud servers (AWS EC2, Azure VM) using SSH. |
| **System Configuration** | Changing permissions, editing files, managing services. |
| **Automation** | Writing shell scripts to automate backups, deployments, etc. |
| **Learning DevOps/Cloud** | Every tool (Docker, Terraform, Kubernetes) uses CLI commands. |

---

## 🧩 CLI Layout (Prompt Structure)

A typical Linux shell prompt looks like:
```bash
user@hostname:~$
```

| Symbol | Meaning |
|---------|----------|
| `user` | Current logged-in username |
| `hostname` | System/computer name |
| `~` | Current directory (home directory) |
| `$` | Normal user prompt (if root, it’s `#`) |

---

## 🧭 Navigation Commands — Moving Around the Filesystem

| Command | Description | Example | Output/Notes |
|----------|--------------|----------|---------------|
| `pwd` | Prints the current working directory | `pwd` | `/home/eshwari` |
| `ls` | Lists files and directories | `ls -l` | Detailed list view |
| `cd` | Change directory | `cd /etc` | Moves to `/etc` folder |
| `cd ..` | Go back one directory | `cd ..` | From `/home/user/docs` → `/home/user` |
| `cd ~` | Go to home directory | `cd ~` | Returns to `/home/username` |
| `cd /` | Go to root directory | `cd /` | Root of the entire filesystem |

🔹 **Tip**: Use **Tab key** for auto-completion of paths and file names.

---

## 📁 File Management Commands — Creating, Viewing, Deleting, Copying, Moving

| Command | Description | Example | Notes |
|----------|--------------|----------|-------|
| `touch` | Create an empty file | `touch notes.txt` | Creates file instantly |
| `cat` | View file content | `cat notes.txt` | Displays entire content |
| `less` / `more` | View long files page by page | `less log.txt` | Use arrows to scroll |
| `mkdir` | Create a directory | `mkdir project` | Creates new folder |
| `rmdir` | Remove an empty directory | `rmdir old_folder` | Works only if empty |
| `rm` | Remove files | `rm notes.txt` | Permanently deletes |
| `rm -r` | Remove directory recursively | `rm -r project/` | Deletes folder + contents |
| `cp` | Copy files | `cp file1.txt file2.txt` | Makes a duplicate |
| `cp -r` | Copy directories recursively | `cp -r source/ destination/` | Copies entire folders |
| `mv` | Move or rename files | `mv old.txt new.txt` | Moves or renames file |
| `nano` / `vi` | Open text editor | `nano script.sh` | Edits files in terminal |

---

## 🔍 Viewing and Searching

| Command | Description | Example |
|----------|--------------|----------|
| `head` | Show first 10 lines | `head log.txt` |
| `tail` | Show last 10 lines | `tail log.txt` |
| `tail -f` | Monitor file live (useful for logs) | `tail -f /var/log/syslog` |
| `grep` | Search for text pattern | `grep "error" log.txt` |
| `find` | Locate files by name | `find /home -name "*.py"` |

💡 **Use Case Example**:  
When monitoring logs in real time, DevOps engineers use:
```bash
tail -f /var/log/nginx/access.log | grep "404"
```
→ This shows only failed web requests (status 404).

---

## 🧮 System and Utility Commands

| Command | Description | Example |
|----------|--------------|----------|
| `date` | Show current date and time | `date` |
| `whoami` | Display current user | `whoami` |
| `clear` | Clears the terminal screen | `clear` |
| `history` | Shows list of previous commands | `history` |
| `echo` | Displays a message or variable | `echo "Hello Eshwari"` |
| `man` | Manual pages for any command | `man ls` |
| `uname -a` | Shows system information | `uname -a` |
| `df -h` | Disk usage info | `df -h` |
| `free -h` | Memory usage info | `free -h` |

---

## 🔐 File Permissions (Basic)

| Command | Description | Example |
|----------|--------------|----------|
| `chmod` | Change file permissions | `chmod 755 script.sh` |
| `chown` | Change file owner | `chown user:user file.txt` |
| `ls -l` | Check permissions | Shows rwx details |

Example output:
```
-rwxr-xr-- 1 eshwari staff 1234 Oct 24 script.sh
```
Here:
- `r` = read  
- `w` = write  
- `x` = execute  

---

## 🧰 File Compression & Archiving

| Command | Description | Example |
|----------|--------------|----------|
| `tar -cvf` | Create tar archive | `tar -cvf backup.tar /home/user` |
| `tar -xvf` | Extract tar archive | `tar -xvf backup.tar` |
| `gzip` | Compress file | `gzip file.txt` |
| `gunzip` | Decompress file | `gunzip file.txt.gz` |

---

## 🧑‍💻 Example Practical Workflow

**Scenario:** A DevOps engineer needs to organize and back up project logs.  
Steps:
```bash
cd /var/log/nginx             # Navigate to log directory
ls -lh                        # List logs with details
mkdir /backup_logs            # Create backup folder
cp *.log /backup_logs/        # Copy all log files
tar -cvf logs_backup.tar /backup_logs  # Archive them
mv logs_backup.tar /home/eshwari/      # Move archive to home
```

✅ **Result:** All logs are archived, safely backed up, and easy to retrieve.

---

## 🌟 Advantages of Mastering CLI

| Benefit | Explanation |
|----------|--------------|
| **Efficiency** | Work faster with fewer clicks. |
| **Automation** | Easily combine commands into scripts. |
| **Remote Control** | Manage servers without GUI (via SSH). |
| **Troubleshooting** | Access logs, processes, and system details directly. |
| **Lightweight** | No need for graphical resources. |
| **Universal Skill** | Same commands work on most Linux systems (AWS, Azure, GCP). |

---

## 🧠 Summary

| Concept | Description |
|----------|--------------|
| **CLI** | A text-based interface for communicating with the OS. |
| **Navigation** | Moving between directories (`cd`, `pwd`, `ls`). |
| **File Management** | Creating, editing, copying, moving, and deleting files. |
| **Utilities** | Viewing system info (`df`, `free`, `date`, `uname`). |
| **Importance** | Essential for automation, DevOps, and cloud system management. |

---
