# Day 1 — Python Fundamentals for DevOps Engineers

**[THEORY] Session 1: Environment Setup & Python Syntax (90 min)**

This session treats you as an **absolute beginner** in Python while respecting that you already think like an engineer (systems, automation, failure modes). Work through the parts **in order** — each file builds on the previous one.

---

## Session 1 — structured lesson parts (basic → advanced)

| Part | Topic | File |
|------|--------|------|
| 1 | Environment setup (pyenv, venv, why isolation matters) | [part01_environment_setup.md](part01_environment_setup.md) |
| 2 | Data types: `str`, `int`, `bool`, `list`, `dict`, `set` + DevOps examples | [part02_data_types_and_variables.md](part02_data_types_and_variables.md) |
| 3 | Control flow: `if`/`elif`/`else`, `for`, `while`, retry-style loops | [part03_control_flow.md](part03_control_flow.md) |
| 4 | Functions: definitions, type hints, `*args`/`**kwargs`, docstrings | [part04_functions.md](part04_functions.md) |
| 5 | Error handling: `try`/`except`/`finally` (no silent failures) | [part05_error_handling.md](part05_error_handling.md) |
| 6 | f-strings, list comprehensions, logging + script skeleton | [part06_fstrings_comprehensions_and_skeleton.md](part06_fstrings_comprehensions_and_skeleton.md) |

**Each part includes:** short theory, DevOps-flavored examples, hands-on practice, and a **Test questions** section with an answer key so you can self-check before writing scripts on your own.

---

## Original outline (reference)

- **pyenv & venv** — Install Python 3.11 via pyenv. Always use virtual environments — never pollute the system Python.
- **Data types** — `str`, `int`, `bool`, `list`, `dict`, `set` — with real DevOps examples: host lists, config dicts, tag sets.
- **Control flow** — `if`/`elif`/`else`, `for` loops over server lists, `while` with retry logic.
- **Functions** — Define reusable functions with type hints, `*args`/`**kwargs`, and docstrings.
- **Error handling** — `try`/`except`/`finally` — the most important construct in ops scripting. Never silently swallow exceptions.
- **f-strings** — Dynamic log messages, path construction, CLI output formatting.
- **List comprehensions** — Filter host lists, transform config values in one readable line.

### Code pattern

```python
# Canonical DevOps script skeleton
import sys, logging
logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

def check_services(hosts: list[str], port: int = 80) -> dict:
    results = {}
    for host in hosts:
        try:
            results[host] = "ok"
        except Exception as e:
            log.error(f"Failed {host}: {e}")
            results[host] = "error"
    return results

if __name__ == "__main__":
    print(check_services(sys.argv[1:]))
```

---

## How to use this session

1. Read **Part 1**, do the practice, complete the test questions, then move on.
2. Repeat for Parts 2–6 in one sitting or split across two days if needed.
3. When all checkboxes in Part 6 are comfortable, you are ready to write small scripts from scratch with the same structure you will use in pipelines and jump boxes.
