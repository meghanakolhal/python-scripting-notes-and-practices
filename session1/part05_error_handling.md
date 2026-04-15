# Session 1 — Part 5: Error Handling (try / except / finally)

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Parts 3–4

---

## Why this is critical in DevOps

Scripts talk to networks, files, and APIs. **Failures are normal** (timeouts, permission denied, HTTP 500). You must:

1. **Catch** expected failures and react (retry, log, skip host).  
2. **Log** useful context — not silence errors.  
3. **Clean up** when needed — `finally` runs whether success or failure.

**Rule:** Never **silently** swallow exceptions (empty `except:` with no log) in production scripts.

---

## try / except

```python
try:
    value = int("not_a_number")
except ValueError as e:
    print(f"Conversion failed: {e}")
```

- **`ValueError`** — a **type** of error (exception).  
- **`as e`** — bind the exception object to `e` for logging.

---

## Multiple except blocks

```python
try:
    risky_operation()
except FileNotFoundError:
    print("Missing file")
except PermissionError:
    print("No permission")
except OSError as e:
    print(f"Other OS error: {e}")
```

Catch **specific** exceptions first; broad `Exception` last if you use it at all.

---

## finally

Runs **always** after `try` (and `except`), even if you `return` or error.

```python
def read_config(path: str) -> None:
    f = None
    try:
        f = open(path, encoding="utf-8")
        data = f.read()
        print(data)
    except OSError as e:
        print(f"Could not read {path}: {e}")
    finally:
        if f is not None:
            f.close()
```

**DevOps:** Close files, release locks, reset terminal state.

---

## Raising errors

When something is wrong and callers should handle it:

```python
if port < 1 or port > 65535:
    raise ValueError(f"Invalid port: {port}")
```

---

## Practice

1. Wrap `int("42")` in try/except and print a message on `ValueError` (try with `"xx"` to trigger it).
2. Write a function that takes a filename, tries to open it, on `FileNotFoundError` returns the string `"missing"` instead of crashing.
3. Explain in one sentence why `except:` with no type is discouraged.

---

## Test questions — Part 5

1. **Concept:** Why is bare `except:` without logging dangerous in a deployment script?
2. **Recall:** When does `finally` run — only on success, only on error, or always?
3. **Code read:** If `int("x")` runs inside `try` and raises `ValueError`, and you have `except TypeError`, what happens?
4. **Scenario:** HTTP request fails with timeout. Which is better: catch a broad `Exception` everywhere, or catch the library’s specific timeout exception type?
5. **True/False:** It is good practice to use `except: pass` so the script always exits with code 0.

**Answer key:**  
1. You hide bugs and real failures; debugging becomes impossible.  
2. Always (after try/except completes).  
3. The exception is **not** caught; it propagates (wrong type).  
4. Prefer the **specific** exception when you know it — clearer intent and fewer surprises.  
5. False — silent failures hide production issues.

---

## Next part

**Part 6: f-strings, comprehensions & script skeleton** (`part06_fstrings_comprehensions_and_skeleton.md`).
