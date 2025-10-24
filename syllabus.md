# Shell Scripting - Complete Overview

## I. Introduction to Shell Scripting

### What is a Shell?

A **Shell** is a command-line interface that allows users to interact
with the operating system. It interprets user commands and executes
them.\
Common types of shells include: - **Bash (Bourne Again Shell)** --- most
widely used in Linux systems. - **Zsh (Z Shell)** --- advanced shell
with auto-completion and customization. - **Ksh (Korn Shell)** --- used
in enterprise UNIX systems. - **Fish (Friendly Interactive Shell)** ---
user-friendly and interactive.

### What is Shell Scripting?

**Shell Scripting** refers to writing a sequence of commands in a text
file that can be executed by the shell. It automates tasks, reduces
manual effort, and enhances system efficiency.

#### Importance and Benefits:

-   Automation of repetitive tasks
-   Improved system administration
-   Simplified configuration management
-   Efficient error handling and monitoring

### Basic Command Line Interface (CLI) Concepts:

-   **Navigation:** `cd`, `pwd`, `ls`
-   **File Management:** `cp`, `mv`, `rm`, `mkdir`, `rmdir`
-   **Basic Commands:** `cat`, `echo`, `touch`, `man`, `clear`

### Creating and Executing Shell Scripts:

-   **Shebang Line:** `#!/bin/bash` --- defines the interpreter.
-   **Permissions:** Use `chmod +x script.sh` to make a script
    executable.
-   Execute using `./script.sh`.

------------------------------------------------------------------------

## II. Shell Scripting Fundamentals

### Variables

-   **System-defined variables:** e.g., `$HOME`, `$USER`, `$PATH`
-   **User-defined variables:** `name="Eshwari"`
-   **Special variables:** `$0`, `$1`, `$#`, `$@`, `$?`, `$$`

### Input and Output

-   **echo / print:** Display output to the terminal.
-   **read:** Accept user input.
-   **I/O Redirection:**
    -   `<` --- Input redirection
    -   `>` --- Output redirection
    -   `>>` --- Append output
    -   `2>` --- Redirect errors

### Operators

-   **Arithmetic:** `+`, `-`, `*`, `/`, `%`
-   **Relational:** `-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`
-   **Logical:** `&&`, `||`, `!`
-   **Assignment:** `=`, `+=`, `-=`, etc.

### Quoting Mechanisms

-   **Single quotes ('')** --- prevent variable expansion.
-   **Double quotes ("")** --- allow variable expansion.
-   **Backticks (\`\`)** --- used for command substitution.

### Command & Variable Substitution

-   `$(command)` or `command` for command substitution.
-   `${variable}` for variable substitution.

------------------------------------------------------------------------

## III. Control Flow Statements

### Conditional Statements

-   **if** --- basic condition
-   **if-else** --- binary decision
-   **if-elif-else** --- multiple conditions
-   **case** --- multi-branch selection

### Loops

-   **for loop:** Iterate over lists or ranges.
-   **while loop:** Repeat while condition is true.
-   **until loop:** Repeat until condition becomes true.

### Loop Control

-   **break** --- exit loop.
-   **continue** --- skip iteration.

------------------------------------------------------------------------

## IV. Functions and Arrays

### Shell Functions

-   **Defining Functions:**

    ``` bash
    my_function() {
        echo "Hello World"
    }
    ```

-   **Calling Functions:** `my_function`

-   **Passing Arguments:** `$1`, `$2`, etc.

### Arrays

-   **Declaring:** `arr=(1 2 3)`
-   **Accessing:** `${arr[0]}`
-   **Length:** `${#arr[@]}`
-   **All Elements:** `${arr[@]}`

------------------------------------------------------------------------

## V. Advanced Shell Scripting Concepts

### Regular Expressions

-   **grep:** Search text patterns.
-   **sed:** Stream editor for substitutions.
-   **awk:** Pattern scanning and processing.

### File Handling

-   Create files: `touch`
-   Delete files: `rm`
-   Modify: `echo "text" >> file.txt`
-   Directory operations: `mkdir`, `rmdir`, `mv`

### Process Management

-   **ps:** Display running processes.
-   **kill:** Terminate a process by PID.
-   **nohup:** Run processes immune to hangups.

### Environment Variables

-   View: `printenv` or `env`
-   Set: `export VAR=value`

### Scheduling Tasks

-   **cron jobs:** Schedule tasks using `crontab -e`.

### Debugging Shell Scripts

-   Use `bash -x script.sh` for step-by-step execution tracing.

------------------------------------------------------------------------

## VI. Practical Applications

### Automating Routine Tasks

-   Backups, updates, user management, and deployment tasks.

### Data Processing and Manipulation

-   Extracting and transforming large log or CSV files.

### System Monitoring and Reporting

-   Generate reports for CPU, memory, and disk usage.

### Customizing User Experience

-   Personalize shell environments with aliases and startup scripts.

------------------------------------------------------------------------

**© Binnbash Academy \| Trainers: Vishwanath Sir & Eshwari Mam**
