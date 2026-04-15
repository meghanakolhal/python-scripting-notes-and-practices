# Session 1 — Part 2: Data Types & Variables

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Part 1 (venv optional for running examples)

---

## Variables

A **variable** is a name that refers to a value. You do not declare a type in advance (Python figures it out).

```python
hostname = "web-01.prod"
port = 443
healthy = True
```

Convention: `snake_case` for variable and function names.

---

## Core types you will use daily (DevOps)

| Type   | Meaning              | Example DevOps use                          |
|--------|----------------------|---------------------------------------------|
| `str`  | Text                 | Hostnames, paths, log lines                 |
| `int`  | Whole numbers        | Ports, exit codes, counts                   |
| `bool` | True / False         | Feature flags, health checks                |
| `list` | Ordered sequence     | List of hosts, ordered steps                |
| `dict` | Key → value map      | Config: name → value, tags                  |
| `set`  | Unique unordered items | Unique hostnames, tag keys (no duplicates) |

---

## Strings (`str`)

```python
region = "us-east-1"
message = "Deploy " + region
```

Strings are **immutable** (you build new strings; you do not “edit” one in place in beginner scripts).

If you print earlier, you get earlier values:

```s = "hello"
print(s)   # hello
s = "hello!"
print(s)   # hello!
s = s + " world"
print(s)   # hello! world
```
So Python always uses the latest assigned value for that variable at that point in the code.

---

## Lists — ordered, allow duplicates

```python
hosts = ["web-01", "web-02", "db-01"]
hosts.append("cache-01")
first = hosts[0]      # index 0 = first
last = hosts[-1]      # last item
```

**DevOps:** Loop over `hosts` to run checks (Part 3).

---

## Dicts — fast lookup by key

```python
config = {
    "env": "production",
    "replicas": 3,
    "region": "us-east-1",
}
env = config["env"]
replicas = config.get("replicas", 1)  # default if key missing
```

**DevOps:** Represent JSON-like config, API responses, or merged variables.

---

## Sets — unique items, unordered

```python
tags = {"prod", "web", "critical"}
tags.add("web")  # still one "web"
```

**DevOps:** Deduplicate host lists, or model “which regions are in use.”

---

## Type checking (optional at first)

You can annotate for clarity (more in Part 4):

```python
hosts: list[str] = ["a", "b"]
port: int = 443
```

---

## Practice

1. Create a `list` of three fake server names. Print the second server.
2. Create a `dict` with keys `environment`, `version` and values you choose. Print `environment`.
3. Given `hosts = ["a", "a", "b"]`, convert to a `set` and print it — how many items?

---

## Test questions — Part 2

1. **Concept:** What is the difference between a `list` and a `set` when you care about order and duplicates?
2. **Recall:** How do you safely read a key from a dict that might be missing, without crashing?
3. **Code read:** What does `hosts[-1]` return if `hosts = ["x", "y", "z"]`?
4. **Scenario:** API returns JSON with server metadata. Which Python type is usually the closest match for one server’s key-value fields?
5. **True/False:** `port = "443"` and `port = 443` behave the same in numeric addition with `80`.

**Answer key:**  
1. List keeps order and duplicates; set is unordered and stores unique values only.  
2. Use `.get("key", default)` or check `"key" in d` before `d["key"]`.  
3. `"z"` (last element).  
4. `dict` (often nested dicts/lists in real APIs).  
5. False — string `"443"` does not add numerically like an int without converting.

---

## Next part

**Part 3: Control flow** (`part03_control_flow.md`).
