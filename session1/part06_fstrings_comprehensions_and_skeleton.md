# Session 1 — Part 6: f-strings, List Comprehensions & DevOps Script Skeleton

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Parts 2–5

---

## f-strings — formatted strings (Python 3.6+)

Prefix a string with `f` and embed expressions in `{ }`:

```python
host = "db-01"
port = 5432
line = f"Connecting to {host}:{port}"
status = 200
log_line = f"GET /health -> {status}"
```

**DevOps:** Log lines, URLs, paths, CLI output — readable and fast.

### Formatting numbers

```python
cpu = 0.8123
print(f"CPU: {cpu:.1%}")   # CPU: 81.2%
```

---

## List comprehensions — build lists in one expression

Instead of:

```python
names = ["web-01", "web-02"]
upper = []
for n in names:
    upper.append(n.upper())
```

Use:

```python
upper = [n.upper() for n in names]
```

**With filter:**

```python
hosts = ["web-01", "skip-me", "web-02"]
active = [h for h in hosts if not h.startswith("skip-")]
```

**DevOps:** Filter host lists, normalize tags, map config keys — keep scripts short and readable.

---

## Canonical DevOps script skeleton

This pattern appears everywhere: logging, a main function, CLI args, `if __name__ == "__main__":`.

```python
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)


def check_services(hosts: list[str], port: int = 80) -> dict[str, str]:
    """Run a trivial check per host (placeholder for real HTTP/TCP checks)."""
    results: dict[str, str] = {}
    for host in hosts:
        try:
            # Placeholder: real code would connect or HTTP GET
            if not host:
                raise ValueError("empty host")
            results[host] = "ok"
        except Exception as e:
            log.error("Failed %s: %s", host, e) 
            # Think of it like blanks:
            # "Failed %s: %s" = "Failed ___: ___"
            # first %s gets host
            # second %s gets e (error)
            # Output becomes: Failed web-01: timeout
            results[host] = "error"
    return results


if __name__ == "__main__":
    hosts = sys.argv[1:]
    if not hosts:
        log.error("Usage: python script.py <host> [host ...]")
        sys.exit(1)
    print(check_services(hosts))
```

- **`if __name__ == "__main__"`** — code runs only when the file is executed directly, not when imported as a module.  
- **`sys.argv`** — list of command-line arguments; `[0]` is script name, `[1:]` are hosts here.

Visualize command line input as a list:

If you run:

python script.py host1 host2 host3
Then:

sys.argv == ["script.py", "host1", "host2", "host3"]
sys.argv[0] → script name ("script.py")
sys.argv[1] → first real argument ("host1")
So:

sys.argv[1:] means: start from index 1 to the end
It skips the script name and gives only user inputs: ["host1", "host2", "host3"]

- **`sys.exit(1)`** — non-zero exit code signals failure to CI/CD or shell.

---

## Practice

1. Build an f-string that prints `retry 2/5` using variables `attempt` and `total`.
2. From `ports = [80, 443, 8080]`, create a new list of strings like `"port_80"` using a comprehension.
3. Copy the skeleton above into a file, run it with: `python yourfile.py host1 host2` and observe logs.

---

## Test questions — Part 6

1. **Concept:** Why use `if __name__ == "__main__":` instead of putting all code at the top level of the file?
2. **Recall:** What is `sys.argv[0]` typically?
3. **Code read:** What does `[x * 2 for x in [1, 2, 3] if x > 1]` evaluate to?
4. **Scenario:** You need a multiline log message with variables. Is f-string inside triple-quoted `"""` valid in Python?
5. **True/False:** List comprehensions can always be replaced by a for-loop; comprehensions are mainly for readability and sometimes speed.

**Answer key:**  
1. So the file can be **imported** (tests, modules) without running CLI side effects.  
2. The script’s path/name as invoked.  
3. `[4, 6]` (only 2 and 3 pass the filter, doubled).  
4. Yes — f-strings work in triple-quoted strings.  
5. True — comprehensions are optional syntax sugar when the logic fits.

---

## Session 1 checklist (you are ready when…)

- [ ] You can create a venv and explain why not to use system Python for projects.  
- [ ] You can use `list`, `dict`, and `set` in simple DevOps-shaped examples.  
- [ ] You can write `if`/`for`/`while` with correct indentation.  
- [ ] You can define functions with defaults and optional `*args`/`**kwargs`.  
- [ ] You use `try`/`except`/`finally` without silencing errors blindly.  
- [ ] You can format output with f-strings and filter lists with comprehensions.  
- [ ] You recognize the logging + `main` + `sys.argv` script layout.

---

## Next session (preview)

Deeper scripting: `pathlib`, `subprocess`, reading YAML/JSON config, `argparse`, and small automation tasks — still with a DevOps lens.
