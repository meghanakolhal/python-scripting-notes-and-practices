# Session 2 — Part 4: argparse and Exit Codes

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Part 3

---

## Why `argparse`

Real automation scripts need clean command-line interfaces.
`argparse` gives help text, validation, and standard flag handling.

---

## Basic CLI

```python
import argparse

parser = argparse.ArgumentParser(description="Health check tool")
parser.add_argument("--host", required=True)
parser.add_argument("--port", type=int, default=80)
parser.add_argument("--env", choices=["dev", "staging", "prod"], default="dev")
args = parser.parse_args()

print(args.host, args.port, args.env)
```

---

## Exit codes matter

- `0` -> success
- non-zero (`1`, `2`, etc.) -> failure for shell/CI pipelines

```python
import sys

if args.port < 1 or args.port > 65535:
    print("Invalid port")
    sys.exit(1)

sys.exit(0)
```

---

## Practice

1. Build `cli_demo.py` with `--host`, `--port`, `--env`.
2. Add validation for port range 1..65535.
3. Run with valid and invalid values, check exit code in shell.

---

## Test questions — Part 4

1. **Concept:** Why is argparse better than manually reading `sys.argv` for production tools?
2. **Recall:** What exit code should indicate success?
3. **Code read:** What does `type=int` do in an argument definition?
4. **Scenario:** CI should fail if config is invalid. Which exit code should your script return?
5. **True/False:** `argparse` can automatically generate help output.

**Answer key:**  
1. Built-in parsing, validation, help, and clearer interfaces.  
2. `0`.  
3. Converts input string to integer (or errors).  
4. Non-zero, usually `1`.  
5. True.

---

## Next part

Continue to `part05_pathlib_os_shutil.md`.
