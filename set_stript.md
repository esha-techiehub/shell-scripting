
# Bash `set` Safety Flags — DevOps Cheat‑Sheet (with demos)

This README gives you **production‑safe defaults** and a **hands‑on demo** you can run on any Linux/EC2 box to teach students how `set` flags change script behavior.

---

## ⚙️ The `set` Command in Shell Scripts

`set` changes how Bash handles **errors**, **variables**, and **pipelines**.

### The most useful flags

| Flag | Meaning | Why/When |
| --- | --- | --- |
| `-e` | Exit on first error (non‑zero status) | **Fail fast**; essential for deploy/backup/DB scripts |
| `-u` | Treat **unset** variables as errors | Catch typos & missing env (e.g., `$DEPLOY_PATH`) |
| `-o pipefail` | Pipelines fail if **any** command fails | Detect hidden failures in `cmd1 \| cmd2 \| cmd3` |
| `-x` | Print each command before executing | Debugging / trace logs |
| `-v` | Print script lines as read (before expansion) | Teaching / step‑through reading |
| `-n` | **Syntax check only** (don’t execute) | Pre‑deployment validation |
| `-f` | Disable globbing (`* ? []`) | Work with literal filenames |

**Turn flags off** with `set +e`, `set +u`, etc.

---

## ✅ Recommended production header

Put this at the **top** of deployment/ops scripts:

```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
trap 'echo "❌ Error on line $LINENO (exit=$?)" >&2' ERR
```

- `-e` → stop on error  
- `-u` → error on undefined variables  
- `-o pipefail` → fail on any pipeline error  
- `IFS` tweak avoids word‑splitting surprises  
- `trap` annotates the failing line for quick diagnosis

> For temporary exceptions, wrap sections with `set +e` … `set -e` or use `|| true` on known benign failures.

---

## 🧪 Hands‑on demo script

Use `demo_set_flags.sh` (included next section) to **show each flag live**.

### How to run

```bash
chmod +x demo_set_flags.sh

# 1) Baseline (no flags)
./demo_set_flags.sh baseline

# 2) Exit on error
./demo_set_flags.sh -e

# 3) Unset vars are errors
./demo_set_flags.sh -u

# 4) Pipefail
./demo_set_flags.sh pipefail

# 5) Debug trace (-x)
./demo_set_flags.sh -x

# 6) Verbose read (-v)
./demo_set_flags.sh -v

# 7) Syntax check only (-n) - nothing executes
bash -n demo_set_flags.sh && echo "Syntax OK"
```

**Tip for class:** run each mode in a fresh shell so previous flags don’t persist.

---

## 📜 `demo_set_flags.sh` (copy/paste)

```bash
#!/usr/bin/env bash

mode="$1"

# helper that deliberately fails
will_fail() { echo "About to fail..."; ls /definitely/missing/path; echo "This will not print if -e"; }

# helper for pipelines
pipe_test() { echo "ok"; false | cat >/dev/null; echo "after pipeline"; }

# show unset variable behavior
unset_var_test() { echo "DEPLOY_PATH is: $DEPLOY_PATH"; }

# common demo body
run_body() {
  echo "== part A: simple command =="
  echo "hello"

  echo "== part B: failing command =="
  will_fail    # ls on a missing path returns non-zero

  echo "== part C: pipeline test =="
  false | grep . >/dev/null
  echo "pipeline done"

  echo "== part D: unset var read =="
  unset DEPLOY_PATH
  unset_var_test

  echo "== part E: pipeline with redirection =="
  cat /no/such/file | sort >/tmp/out.txt
  echo "end"
}

case "$mode" in
  -e|--errexit)
    set -e
    run_body
    ;;
  -u|--nounset)
    set -u
    run_body
    ;;
  pipefail)
    set -o pipefail
    run_body
    ;;
  -x|--xtrace)
    set -x
    run_body
    ;;
  -v|--verbose)
    set -v
    run_body
    ;;
  baseline|"")
    echo "(baseline: no safety flags)"
    run_body
    ;;
  *)
    echo "Usage: $0 [baseline|-e|-u|pipefail|-x|-v]" >&2
    exit 2
    ;;
esac
```

### What you’ll observe

- **Baseline**: the script keeps going even after errors.
- **`-e`**: stops at the first failing command (after “About to fail…”).
- **`-u`**: exits when reading `$DEPLOY_PATH` (since it’s unset).
- **`pipefail`**: the `false | grep` pipeline causes failure.
- **`-x`**: every command is printed with a `+` prefix.
- **`-v`**: each script line is echoed as Bash reads it.

---

## 🧪 Pipefail with real‑world line

**Without** pipefail (bad – only `sort` status is checked):
```bash
docker exec -i mongodb mongodump --archive --gzip > backup.gz
```

**Safer** with pipefail:
```bash
set -o pipefail
docker exec -i mongodb mongodump --archive --gzip > backup.gz
```

If `mongodump` fails, the pipeline status is non‑zero and your script stops (with `-e`).

---

## 🧰 Pattern for controlled exceptions

Sometimes you expect a non‑critical failure (e.g., stopping an old container).

```bash
set -euo pipefail

docker stop old_service || true    # ignore error if already stopped
docker rm old_service   || true

set +e                               # temporarily allow failures
some_noncritical_task || echo "continuing despite failure"
set -e                               # re‑enable fail‑fast
```

---

## 🧠 Quick reference

| Flag | Meaning | When to use |
| --- | --- | --- |
| `-e` | Exit on error | **Always** in prod scripts |
| `-u` | Unset variable is error | **Always** |
| `-o pipefail` | Fail on any pipeline error | **Always** |
| `-x` | Print commands before run | Testing / Debug logs |
| `-v` | Print lines as read | Teaching / tracing |
| `-n` | Parse only | Validation / CI lint |
| `-f` | Disable globbing | Literal filenames |

---

Happy shipping! Ship **safe** and **observable** 🚀
