# Session 2 — Part 2: YAML for Configuration Files

**Audience:** Absolute beginners  
**Time:** ~15–20 minutes  
**Prerequisite:** Part 1 (JSON basics)

---

## Why YAML in DevOps

YAML is used in Kubernetes, CI pipelines, Helm values, and deployment configs.
It is human-readable, but indentation-sensitive.

---

## Read YAML with PyYAML

Install once in your venv:

```bash
pip install pyyaml
```

Read file:

```python
import yaml

with open("deployment.yaml", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

replicas = manifest["spec"]["replicas"]
image = manifest["spec"]["template"]["spec"]["containers"][0]["image"]
print(f"Image: {image} Replicas: {replicas}")
```

Use `safe_load()` for trusted parsing behavior.

---

## Write YAML

```python
out = {
    "name": "billing",
    "replicas": 3,
    "port": 8080,
}

with open("service.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(out, f, sort_keys=False)
```

---

## Common YAML mistakes

- Wrong indentation depth
- Tabs instead of spaces
- Treating numbers as strings accidentally

---

## Practice

1. Create `service.yaml` with `name`, `port`, `healthcheck_path`, then read and print values.
2. Load a YAML dict and print all keys.
3. Change replicas from 2 to 4 and write back to a new file.

---

## Test questions — Part 2

1. **Concept:** Why is YAML popular in DevOps tooling?
2. **Recall:** Which function is recommended for reading YAML safely?
3. **Code read:** What type do you usually get after `yaml.safe_load(...)` for a mapping document?
4. **Scenario:** YAML parse fails with indentation error. What is first thing to inspect?
5. **True/False:** Tabs and spaces are interchangeable in YAML indentation.

**Answer key:**  
1. Human-readable config format used widely by infra tools.  
2. `yaml.safe_load`.  
3. Usually `dict` (or list depending on document).  
4. Indentation consistency and nesting levels.  
5. False (tabs are problematic; use spaces).

---

## Next part

Continue to `part03_environment_variables_and_dotenv.md`.
