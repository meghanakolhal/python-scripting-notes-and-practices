# 1. Write a `for` loop that prints each host in `["a", "b", "c"]` prefixed with `HOST: `.
hosts = ["a", "b", "c"]
for host in hosts:
    print(f"HOST: {host}")  

# 2. Write an `if` that prints `"prod"` only if variable `env` equals `"production"` (case-sensitive).
env = "dev"
if env == "production":
    print("prod")
else:
    print("not prod")

# 3. Write a `while` loop that counts from 1 to 3 and prints each number.
count = 1
while count <= 3:
    print(count)
    count += 1



# When is `while` more appropriate than `for` for a DevOps retry script?
#Answer: When you do not know how many tries until success/failure (bounded by max retries).

# What Python keyword skips the rest of the current loop iteration and goes to the next item?
#Answer: `continue`.

# What does this print?

```python
for x in [10, 20, 30]:
    if x == 20:
        continue
    print(x)
```
#Answer: 10 and 30 only (20 is skipped).

# You have 200 hosts. You want to stop the loop as soon as one host fails a check. Which keyword do you use after detecting failure?
#Answer: `break`.   

# True/False: `if env = "prod":` is valid Python for comparing `env` to `"prod"`.
#Answer: False. Comparison uses `==`, not `=`.

# 
