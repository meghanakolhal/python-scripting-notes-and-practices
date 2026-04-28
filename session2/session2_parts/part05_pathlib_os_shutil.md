# Session 2 � Part 5: Filesystem Automation with pathlib, os, shutil

**Audience:** Absolute beginners  
**Time:** ~20 minutes  
**Prerequisite:** Part 4

---

## Why this matters in DevOps

Automation scripts often scan directories, move artifacts, archive logs, and clean old files.
`pathlib` gives readable file path operations.

---

## `pathlib.Path` basics

```python
from pathlib import Path

p = Path("logs/app.log")
print(p.exists())
print(p.name)        # app.log
print(p.suffix)      # .log
```

Read/write text:

```python
cfg = Path("config.txt")
cfg.write_text("enabled=true\n", encoding="utf-8")
print(cfg.read_text(encoding="utf-8"))
```

---

## Globbing and traversal

```python
log_dir = Path("logs")
for f in log_dir.glob("*.log"):
    print(f)
```

`os.walk()` is useful for deep recursive audits across large trees.

---

## `shutil` operations

```python
import shutil

shutil.copy2("app.log", "backup/app.log")
archive_path = shutil.make_archive("logs_backup", "zip", "logs")
print(archive_path)
```

---

## Practice

1. Create a script that lists all `.log` files in a folder.
2. Copy one file to a backup folder with `copy2`.
3. Archive the folder and print archive path.

---

## Test questions � Part 5

1. **Concept:** Why prefer `pathlib` over string-concatenated paths?
2. **Recall:** Which method reads full file text from a `Path` object?
3. **Code read:** What does `Path("/tmp").glob("*.log")` return conceptually?
4. **Scenario:** You need to zip a directory for artifact upload. Which stdlib helper is convenient?
5. **True/False:** `shutil.copy2` attempts to preserve metadata better than basic copy.

**Answer key:**  
1. More readable, cross-platform path handling, safer operations.  
2. `.read_text()`.  
3. Iterator of matching log file paths.  
4. `shutil.make_archive`.  
5. True.
It means shutil.copy2() copies file content and also tries to preserve metadata (like modified time, access time, permission bits) more than shutil.copy().

Quick difference:

shutil.copy(src, dst) -> content + permission mode
shutil.copy2(src, dst) -> content + mode + timestamps (+ extra metadata when platform supports it)
So if you care about “keeping file details same as original,” prefer copy2.
---

## Next part

Continue to `part06_subprocess_safe_execution.md`.
