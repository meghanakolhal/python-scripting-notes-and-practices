# Session 2 � Part 1: JSON for API/Data Handling

**Audience:** Absolute beginners in Python, DevOps background  
**Time:** ~15�20 minutes  
**Prerequisite:** Session 1 complete

---

## Why JSON matters in DevOps

Most APIs (cloud, CI/CD, monitoring, secrets managers) send and receive JSON.
In Python, JSON maps naturally to `dict` and `list`.

---

## Load JSON safely

```python
import json

raw = '{"service": "api", "port": 8080, "healthy": true}'
data = json.loads(raw) # converts the raw string into a dictionary
print(raw) # Output: {"service": "api", "port": 8080, "healthy": true}
print(type(data))      # dict
print(data) # Output: {'service': 'api', 'port': 8080, 'healthy': True}
print(data["service"]) # api
```

Read from file:

```python
with open("response.json", encoding="utf-8") as f:  #encoding is the “decoder language” to turn bytes -> readable text as files stores raw bytes
    payload = json.load(f)
```

---

## Access nested fields without crashes

Direct indexing fails if key is missing:

```python
image = payload["spec"]["template"]["image"]
```

Safer beginner approach with `.get()`:

```python
spec = payload.get("spec", {})
template = spec.get("template", {})
image = template.get("image", "unknown")
```

---

## Convert Python to JSON

```python
report = {"host": "web-01", "status": "ok"}
text = json.dumps(report, indent=2)# converts the dictionary into a string
print(text) # Output:
# {
#   "host": "web-01",
#   "status": "ok"
# }
```

Quick memory:

json.dumps(...) -> to string
json.dump(...) -> to file
json.loads(...) -> string to Python object
json.load(...) -> file to Python object
Useful options:


json.dumps(data, indent=2)      # pretty format
json.dumps(data, sort_keys=True)

---

## Practice

1. Create a Python dict with keys `app`, `version`, `replicas` and print it as pretty JSON.
2. Load this JSON string and print `port`: `'{"port": 443, "env": "prod"}'`.
3. From `{"service": {}}`, safely read missing key `service.name` with fallback `"unknown"`.

---

## Test questions � Part 1

1. **Concept:** What two common Python types represent JSON objects and arrays?
2. **Recall:** What is the difference between `json.load()` and `json.loads()`?
3. **Code read:** Why can `payload["a"]["b"]` crash?
4. **Scenario:** API occasionally omits `region`. Which method helps avoid `KeyError`?
5. **True/False:** `json.dumps()` converts JSON text to dict.

**Answer key:**  
1. Object -> `dict`, Array -> `list`.  
2. `load()` reads from file object; `loads()` reads from string.  
3. Missing keys at any level raise `KeyError`.  
4. `.get("region", default)`.  
5. False (`dumps` makes dict -> JSON string).

---

## Next part

Continue to `part02_yaml_for_configs.md`.
