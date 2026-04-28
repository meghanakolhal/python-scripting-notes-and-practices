# Session 2 — Part 3: Environment Variables and python-dotenv

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Part 2

---

## Why env vars for DevOps

Secrets should not be hardcoded in scripts or committed in Git.
Use environment variables for API keys, tokens, endpoints, and runtime settings.

---

## Read env variables with `os.environ`

```python
import os

api_key = os.environ["API_KEY"]  # fail fast if missing
region = os.environ.get("REGION", "us-east-1")
```

- `os.environ["KEY"]` -> raises `KeyError` if missing.
- `os.environ.get("KEY", default)` -> safe fallback.

---

## Use `.env` during local development

Install:

```bash
pip install python-dotenv
```

Usage:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ["API_KEY"]
print("Loaded key length:", len(api_key))
```

Add `.env` to `.gitignore`.

---

## Practice

1. Create `.env` with `API_KEY=demo123` and `ENV=dev`.
2. Write script that loads and prints `ENV`.
3. Remove `API_KEY` and observe fail-fast error with `os.environ["API_KEY"]`.

---

## Test questions — Part 3

1. **Concept:** Why should secrets be stored in env vars instead of source code?
2. **Recall:** Which call fails fast when variable is missing: `os.environ[...]` or `.get()`?
3. **Code read:** What default is used in `os.environ.get("REGION", "us-east-1")` when `REGION` is unset?
4. **Scenario:** You want required credentials to stop execution if absent. Which style should you choose?
5. **True/False:** `.env` files should usually be committed to public repos if they include real credentials.

**Answer key:**  
1. Better security, environment-specific values, safer deployments.  
2. `os.environ[...]`.  
3. `"us-east-1"`.  
4. Use `os.environ["KEY"]` to fail fast.  
5. False.

---

## Next part

Continue to `part04_argparse_and_exit_codes.md`.
