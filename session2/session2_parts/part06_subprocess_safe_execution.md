# Session 2 — Part 6: subprocess and Safe Shell Command Execution

**Audience:** Absolute beginners  
**Time:** ~20 minutes  
**Prerequisite:** Part 5

---

## Why `subprocess` in DevOps scripts

Sometimes Python must call system commands (`git`, `kubectl`, `df`, `docker`).
Use `subprocess.run` safely and predictably.

---

## Safe one-shot command helper

```python
import subprocess

def run(cmd: list[str], timeout: int = 30) -> str:
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
        timeout=timeout,
    )
    return result.stdout.strip()
```

Usage:

```python
output = run(["python", "--version"])
print(output)
```

---

## Key safety rules

- Prefer list args like `["git", "status"]`.
- Avoid `shell=True` when command contains user input.
- Use `check=True` to fail on non-zero exit.
- Use `timeout=` to avoid hung commands.

---

## Parsing command output

```python
df = run(["df", "-h", "--output=target,pcent"])
for line in df.splitlines()[1:]:
    mount, pct = line.split()
    if int(pct.rstrip("%")) > 80:
        print(f"WARNING: {mount} is {pct} full")
```

---

## Practice

1. Write `run(["python", "--version"])` and print output.
2. Add timeout and test with a short command.
3. Try a failing command and catch `subprocess.CalledProcessError`.

---

## Test questions — Part 6

1. **Concept:** Why is `shell=True` risky with untrusted input?
2. **Recall:** Which flag raises exception on non-zero command exit?
3. **Code read:** What does `capture_output=True, text=True` provide?
4. **Scenario:** Command hangs in CI. Which parameter helps protect pipeline time?
5. **True/False:** `subprocess.run` always returns only stdout and never stderr.

**Answer key:**  
1. Shell injection risk.  
2. `check=True`.  
3. Captured stdout/stderr as strings.  
4. `timeout=`.  
5. False (stderr available too).

---

## Session 2 checklist (you are ready when…)

- [ ] You can parse JSON and safely access nested fields.  
- [ ] You can read/write YAML with `safe_load`/`safe_dump`.  
- [ ] You understand env vars and local `.env` loading.  
- [ ] You can build CLI flags with `argparse`.  
- [ ] You can use correct exit codes for CI compatibility.  
- [ ] You can automate file operations using `pathlib` and `shutil`.  
- [ ] You can run shell commands safely with `subprocess.run`.

---

## Next session (preview)

Small real-world automation projects: API polling, config linting, retries/backoff, and structured logging.
