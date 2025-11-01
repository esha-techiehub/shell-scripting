# Advanced Shell Scripting — README

*A concise, practical guide to regular expressions, grep, sed, awk, and file handling — with examples and mini exercises.*

---

## Table of Contents

1. Overview
2. Regular Expressions (Quick Recap)
3. `grep` — Searching Text

   * Common flags
   * Examples
   * Combining flags
4. `sed` — Stream Editing

   * Basic substitution
   * Deleting lines and ranges
   * In-place edits
   * Examples with sample file
5. `awk` — Field Processing and Reporting

   * Basics
   * Examples
6. File & Directory Handling

   * Create / Read / Modify / Delete
   * Directory operations
7. Pipelines: `grep` + `sed` (and `awk`)

   * Examples and patterns
8. Example Scripts

   * Log processing script
   * Small automation examples
9. Cheat Sheet (commands & one-liners)
10. Practice Exercises
11. Notes, Tips & Safety

---

## 1. Overview

This README gathers the essential advanced shell scripting concepts: how to search and transform text using regular expressions, `grep`, `sed`, and `awk`; plus file and directory handling. It includes ready-to-run examples and sample input files so you can practice immediately.

## 2. Regular Expressions (Quick Recap)

* `.` : any single character
* `*` : zero or more of previous token
* `+` : one or more (extended regex)
* `?` : zero or one (extended regex)
* `[]` : character class, e.g. `[0-9]`
* `()` : grouping (extended regex)
* `|` : alternation (OR, extended regex)
* `^` and `$` : start and end of line

> Use extended regex with `grep -E` or `egrep` and `sed -E` when you need `+`, `?`, `()` or `|` without escaping.

## 3. `grep` — Searching Text

**Basic syntax:**

```bash
grep [options] 'pattern' filename
```

**Common flags:**

* `-i` : case-insensitive
* `-n` : show line numbers
* `-v` : invert match (show non-matching lines)
* `-E` : extended regex
* `-r` : recursive (search files in directories)
* `-c` : count matching lines

**Examples:**

```bash
grep "error" logfile.txt        # lines with "error"
grep -i "error" logfile.txt     # case-insensitive
grep -n "error" logfile.txt     # include line numbers
grep -v "error" logfile.txt     # lines that DO NOT contain 'error'
grep -E "cat|dog" animals.txt   # match 'cat' OR 'dog'
```

**Combining flags (yes you can):**

```bash
# All equivalent:
grep -i -n -E "error|fail" logfile.txt
grep -inE "error|fail" logfile.txt
grep -Ein "error|fail" logfile.txt
```

These search for `error` or `fail`, case-insensitively, using extended regex, and print line numbers.

## 4. `sed` — Stream Editing

**Basic substitution syntax:**

```bash
sed 's/pattern/replacement/' file     # replace first occurrence on each line
sed 's/pattern/replacement/g' file    # replace all occurrences on each line
```

**Delete lines by pattern or range:**

```bash
sed '/banana/d' fruits.txt    # delete lines containing 'banana'
sed '2,4d' fruits.txt         # delete lines 2 through 4
```

**In-place editing:**

```bash
sed -i 's/foo/bar/g' file.txt   # Modify file directly (no output)
```

**Sample file ********`fruits.txt`******** (use this to test):**

```
apple banana mango
banana apple grape
apple apple cherry
orange banana apple
grape mango banana
```

**`sed`**** examples & their outputs:**

* `sed 's/apple/orange/' fruits.txt` — replace first `apple` per line.
* `sed 's/apple/orange/g' fruits.txt` — replace all occurrences.
* `sed '/banana/d' fruits.txt` — keep only lines without `banana`.
* `sed '2,4d' fruits.txt` — remove lines 2 through 4.
* `sed -i 's/apple/orange/g' fruits.txt` — permanently replace inside file.

**Advanced ********`sed`******** one-liner (select + substitute + print):**

```bash
sed -n '/ERROR/s/ERROR/ALERT/p' logfile.txt
```

This selects lines that match `/ERROR/`, substitutes `ERROR` with `ALERT`, and prints them.

## 5. `awk` — Field Processing and Reporting

**Basic usage:**

```bash
awk 'pattern { action }' file
```

Fields are `$1`, `$2`, ... and `$0` is the whole line. Default field separator is whitespace; use `-F` to change it.

**Examples:**

```bash
awk '{ print $1 }' file.txt                     # print first column
awk '/error/ { print $2, $3 }' logfile.txt      # print fields 2 and 3 for matched lines
awk -F, '{ print $1, $3 }' data.csv             # CSV with comma separator
awk '{ sum += $2 } END { print sum }' data.txt # sum of column 2
```

## 6. File & Directory Handling

**Create files:**

```bash
touch filename.txt
echo "Hello" > file.txt   # overwrite
echo "More" >> file.txt   # append
cat > newfile.txt           # type input then Ctrl+D to finish
```

**Read files:**

```bash
cat file.txt
head -n 5 file.txt
tail -n 5 file.txt
less file.txt
```

**Delete files:**

```bash
rm file.txt
rm -f file.txt      # force
rm *.log
```

**Directories:**

```bash
mkdir newfolder
mkdir -p path/to/newfolder  # nested
rmdir emptydir
rm -r dir_name              # remove recursively
cd /path/to/dir
pwd
```

## 7. Pipelines: `grep` + `sed` (+ `awk`)

**Patterns:** filter → transform → format → save

**Examples:**

```bash
# Replace 'ERROR' with 'ALERT' in lines that contain 'ERROR'
grep "ERROR" logfile.txt | sed 's/ERROR/ALERT/'

# Use sed alone to do the same (select & replace & print)
sed -n '/ERROR/s/ERROR/ALERT/p' logfile.txt

# Filter errors, replace and save to new file
grep "ERROR" logfile.txt | sed 's/ERROR/FIXED/' > fixed_errors.txt

# Exclude lines containing 'successful', then replace INFO with NOTICE
grep -v "successful" logfile.txt | sed 's/INFO/NOTICE/'

# Extract ERROR or WARNING and strip the uppercase prefix
grep -E "ERROR|WARNING" logfile.txt | sed 's/^[A-Z]*: //'

# Example pipeline using awk for columns
grep -E "ERROR|WARNING" logfile.txt | sed 's/^[A-Z]*: //' | awk '{ print NR, $0 }'
```

## 8. Example Scripts

**Log processing script (********`process_logs.sh`********)**

```bash
#!/bin/bash
# Extract errors, convert ERROR -> ALERT, and create a summary
LOGFILE=${1:-server.log}
OUTDIR=${2:-./out}
mkdir -p "$OUTDIR"

# extract and transform
grep -E "ERROR|FAIL|FATAL" "$LOGFILE" | sed -E 's/ERROR|FAIL|FATAL/ALERT/g' > "$OUTDIR/alerts.txt"

# create a summary with line numbers and timestamp
nl -ba "$OUTDIR/alerts.txt" > "$OUTDIR/alerts_numbered.txt"

echo "Processed $LOGFILE -> $OUTDIR/alerts.txt"
```

**Small automation: Replace in-place in many files**

```bash
# replace 'foo' with 'bar' in all .txt files
for f in *.txt; do
  sed -i 's/foo/bar/g' "$f"
done
```

## 9. Cheat Sheet (quick reference)

* `grep -inE "pattern1|pattern2" file` — case-insensitive, line numbers, extended regex
* `sed -n '/PATTERN/s/A/B/p' file` — operate only on lines matching PATTERN
* `sed -i 's/A/B/g' file` — edit file in place
* `awk -F"," '{print $1, $3}' data.csv` — print columns 1 and 3 from CSV
* `rm -r somedir` — delete directory recursively

## 10. Practice Exercises

1. Create `fruits.txt` with the sample contents shown above. Try the `sed` commands and confirm outputs.
2. Create `logfile.txt` with the sample logs and run `grep -inE "error|fail" logfile.txt`.
3. Use `awk` to compute the sum of the second column in a whitespace-delimited data file.
4. Write a script that finds `.conf` files in `/etc` containing the word `deprecated` and outputs filenames and line numbers.

## 11. Notes, Tips & Safety

* Test commands without `-i` first to ensure the transformation is correct before modifying files in-place.
* Use `grep -n` or `nl` to get line numbers when you need to reference or edit specific lines.
* `sed` uses basic regex by default; prefer `-E` for extended syntax or escape special chars.
* When working with user-supplied filenames, always quote variables in scripts: `"$file"` to avoid word-splitting or globbing problems.

---
