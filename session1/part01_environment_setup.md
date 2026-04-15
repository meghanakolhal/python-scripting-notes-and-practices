# Session 1 — Part 1: Environment Setup (pyenv & venv)

**Audience:** Absolute beginners in Python, DevOps background  
**Time:** ~15 minutes reading + practice  
**Prerequisite:** None

---

## Why this matters for DevOps

- **System Python** is what your OS or tools may rely on. Installing packages globally can break those tools.
- **pyenv** lets you install and switch **multiple Python versions** on one machine (e.g. 3.11 for new scripts, 3.9 for legacy).
- **venv** (virtual environment) is an **isolated folder** where each project gets its own packages. This matches how you isolate dependencies per service or repo.

**Rule:** Never pollute system Python with `pip install` for project work. Always use a venv.

---

## 1. Install Python 3.11 with pyenv (overview)

Commands depend on your OS. On Windows, people often use **pyenv-win** or the official **python.org** installer; on Linux/macOS, **pyenv** is common.

Typical flow (Linux/macOS style):

```bash
pyenv install 3.11.9
pyenv global 3.11.9   # or pyenv local 3.11.9 inside a project folder
python --version
```

Verify you see Python 3.11.x.

---

## 2. Create and use a virtual environment

From your project folder (e.g. `Learn_Python`):

```bash
python -m venv .venv
```

- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **macOS/Linux:** `source .venv/bin/activate`

After activation, `python` and `pip` point **inside** `.venv`. Install packages here only:

```bash
pip install requests
```

Deactivate when done:

```bash
deactivate
```

---

## 3. What to put in `.gitignore`

Add `.venv/` so the virtual environment is not committed (teammates recreate it with `python -m venv .venv` and `pip install -r requirements.txt`).

---

## Practice (hands-on)

1. Create a folder `my_first_script` and a venv inside it.
2. Activate the venv and run `python -c "print('venv works')"` .
3. Write down one sentence: why venv is better than `pip install` to system Python.

---

## Test questions — Part 1

Answer without running code first, then check with notes above.

1. **Concept:** What is the main risk of installing many Python packages with `pip` into the system Python on a shared laptop used for DevOps work?
2. **Concept:** What does `python -m venv .venv` create, in plain language?
3. **Recall:** After activating a venv, which `python` runs when you type `python` in that terminal — system or venv?
4. **Scenario:** You clone a repo that has `requirements.txt` but no `.venv`. What two-step process do you use before running the project’s scripts?
5. **True/False:** You should commit the entire `.venv` folder to Git so teammates get the same packages automatically.

**Answer key (for self-check):**  
1. Breaking OS tools or other projects that expect different package versions.  
2. A private copy of Python + pip isolated in a folder (usually `.venv`).  
3. The venv’s Python.  
4. Create/activate venv, then `pip install -r requirements.txt`.  
5. False — commit `requirements.txt`, not `.venv`.

---

## Next part

Continue to **Part 2: Data types & variables** (`part02_data_types_and_variables.md`).
