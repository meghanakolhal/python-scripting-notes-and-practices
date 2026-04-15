# Session 1 — Part 4: Functions

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Parts 2–3

---

## Why functions?

Functions bundle reusable logic with a **name**, **inputs (parameters)**, and often a **return value**. Same idea as reusable shell functions or Ansible tasks — one definition, many calls.

---

## Basic function

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

message = greet("DevOps")
```

- **`def`** — start a function definition.  
- **`name: str`** — type hint (documentation + tooling; not enforced at runtime by default).  
- **`-> str`** — return type hint.  
- **`return`** — sends a value back; without it, the function returns `None`.

---

## Default arguments

```python
def connect(host: str, port: int = 22, timeout: int = 30) -> None:
    print(f"{host}:{port} timeout={timeout}")
```

Callers can omit `port` and `timeout` when defaults given above are okay to them.

---

## `*args` — extra positional arguments

```python
def summarize(*items: str) -> None:
    for item in items:
        print(item)

summarize("a", "b", "c")
```

Inside the function, `items` is a **tuple** of all extra positional arguments.

## Main difference:

List: mutable (can change)
Tuple: immutable (cannot change after creation)

Syntax
List uses []
Tuple uses ()

```my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
Mutability example
my_list[0] = 99      # works
my_tuple[0] = 99     # TypeError
```
When to use what
Use list when data may change (add/remove/update items).
Use tuple when data should stay fixed (like coordinates, config constants, returned fixed groups of values).

Extra points
Tuples are slightly more memory-efficient.
Tuples can be used as dictionary keys (if all elements hashable); lists cannot.

<!-- extra info can ignore -->
Hashable means: a value can be converted to a fixed hash number (via hash(...)) that does not change during its lifetime.

Why it matters:

Dictionary keys and set elements must be hashable.
Python uses the hash value to store/find them quickly.

Examples:

Hashable: int, float, str, bool, tuple (only if all elements inside are hashable)
Not hashable: list, dict, set (because they are mutable)
```
hash("hello")      # works
hash((1, 2, 3))    # works
hash([1, 2, 3])    # TypeError: unhashable type: 'list'
```
Quick rule:

Usually immutable => hashable (with some exceptions)
Usually mutable => not hashable

Important exceptions
tuple is immutable, but may be unhashable
If it contains any unhashable element, whole tuple becomes unhashable.

hash((1, 2, 3))        # works
hash((1, [2, 3]))      # TypeError (list inside is unhashable)
frozenset is immutable, but may be unhashable in practice if contents aren't hashable

hash(frozenset({1, 2}))      # works
frozenset([ [1,2] ])       # fails earlier because list can't be set element

User-defined classes can be immutable-looking but unhashable
If class defines equality (__eq__) but no proper __hash__, Python may set hash to None, making instances unhashable.

Why hashing exists?
Without hashing, to find a key in a dictionary, Python would scan items one by one (slow).
With hashing, Python computes a number from the key and jumps near the right place (very fast average O(1)).
<!-- extra info ends  -->


**DevOps:** Pass through an unknown number of hostnames or tags.

---

## `**kwargs` — extra keyword arguments

```python
def run(**options: str) -> None:
    for key, value in options.items():
        print(f"{key}={value}")

run(env="prod", region="us-east-1")
```

Inside the function, `options` is a **dict**.

**DevOps:** Forward optional flags to APIs or CLI wrappers.

---

## Docstrings

A **docstring** is a string right after `def` that explains what the function does.

```python
def health_url(host: str, use_https: bool = True) -> str:
    """Return a health-check URL for the given host."""
    scheme = "https" if use_https else "http"
    return f"{scheme}://{host}/health"
```

Tools and humans read this; aim for one clear sentence, then details if needed.

---

## Practice

1. Write a function `port_string(port: int) -> str` that returns `"port is 443"` (use an f-string).
2. Write a function `max_retry(default: int = 3) -> int` that returns the default — call it with no args and print the result.
3. Add a one-line docstring to one of your functions.

---

## Test questions — Part 4

1. **Concept:** What is the difference between a **parameter** and an **argument** in everyday terms?
2. **Recall:** What does a function return if it has no `return` statement?
3. **Code read:** What type is `args` inside `def f(*args):` when you call `f(1, 2, 3)`?
4. **Scenario:** You want callers to pass arbitrary key=value settings into a wrapper. Do you use `*args` or `**kwargs`?
5. **True/False:** Type hints like `name: str` stop the program if you pass an integer at runtime.

**Answer key:**  
1. Parameter is the name in the definition; argument is the actual value passed in the call.  
2. `None`.  
3. A tuple `(1, 2, 3)`.  
4. `**kwargs`.  
5. False — hints are not enforced by the interpreter by default (tools like mypy can check them).

---

## Next part

**Part 5: Error handling** (`part05_error_handling.md`).
