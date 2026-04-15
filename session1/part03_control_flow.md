# Session 1 — Part 3: Control Flow

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Part 2 (data types)

---

## `if` / `elif` / `else`

Run different code based on conditions.

```python
exit_code = 0

if exit_code == 0:
    print("Success")
elif exit_code == 1:
    print("General error")
else:
    print("Other failure")
```

**DevOps:** Branch on environment name, HTTP status, or command exit codes.

**Indentation matters:** Python uses spaces (usually 4) to define blocks — no `{ }` like some languages.

---

## `for` loops — iterate over sequences

```python
hosts = ["web-01", "web-02", "db-01"]

for host in hosts:
    print(f"Checking {host}")
```

**DevOps:** “For each server in the inventory, run a check.”

### `range`

```python
for i in range(3):      # 0, 1, 2
    print(i)

for attempt in range(1, 4):  # 1, 2, 3
    print(f"retry {attempt}")
```

---

## `while` loops — repeat while condition is true

```python
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    attempt += 1
    print(f"Attempt {attempt}")
    # In real scripts: call API, check result, break on success
```

**DevOps:** Retry logic — try up to N times with sleep between attempts (you may use `time.sleep` later).

### `break` and `continue`

- **`break`** — exit the loop immediately.  
- **`continue`** — skip to the next iteration.

```python
for host in hosts:
    if host.startswith("skip-"):
        continue
    print(host)
```

---

## Practice

1. Write a `for` loop that prints each host in `["a", "b", "c"]` prefixed with `HOST: `.
2. Write an `if` that prints `"prod"` only if variable `env` equals `"production"` (case-sensitive).
3. Write a `while` loop that counts from 1 to 3 and prints each number.

---

## Test questions — Part 3

1. **Concept:** When is `while` more appropriate than `for` for a DevOps retry script?
2. **Recall:** What Python keyword skips the rest of the current loop iteration and goes to the next item?
3. **Code read:** What does this print?

```python
for x in [10, 20, 30]:
    if x == 20:
        continue
    print(x)
```

4. **Scenario:** You have 200 hosts. You want to stop the loop as soon as one host fails a check. Which keyword do you use after detecting failure?
5. **True/False:** `if env = "prod":` is valid Python for comparing `env` to `"prod"`.

**Answer key:**  
1. When you do not know how many tries until success/failure (bounded by max retries).  
2. `continue`.  
3. `10` and `30` only (20 is skipped).  
4. `break`.  
5. False — comparison uses `==`, not `=`.

---

## Next part

**Part 4: Functions** (`part04_functions.md`).
