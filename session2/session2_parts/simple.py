# 1. Create a Python dict with keys `app`, `version`, `replicas` and print it as pretty JSON.
# answer: 
app = {
    "app" : "myapp",
    "version" : "v1",
    "replicas" : "2"
}
import json
print(type(app))
print(app)
print(json.dumps(app, indent=2))
# Output:
# {
#   "app": "myapp",
#   "version": "v1",
#   "replicas": "2"
# }

# 2. Load this JSON string and print `port`: `'{"port": 443, "env": "prod"}'`.

raw = '{"port": 443, "env": "prod"}'
data = json.loads(raw)
print(type(data))
print(data)
print(data["port"])

# 3. From `{"service": {}}`, safely read missing key `service.name` with fallback `"unknown"`.
# raw = '{"service": {}}'
raw = '{"service": {"port": 443, "name": "api"}}'
data = json.loads(raw)
print(type(data))
print(data)
# print(data["service"]["name"])
# need to handle safely 
print(data.get("service", {}).get("name", "unknown"))

# 1. **Concept:** What two common Python types represent JSON objects and arrays?
# answer: dict and list

# 2. **Recall:** What is the difference between `json.load()` and `json.loads()`?
# answer: json.load() reads from a file and json.loads() reads from a string

# 3. **Code read:** Why can `payload["a"]["b"]` crash?
# answer: because the key "a" is not in the dictionary and the key "b" is not in the dictionary

# 4. **Scenario:** API occasionally omits `region`. Which method helps avoid `KeyError`?
# answer: .get("region", "unknown")

# 5. **True/False:** `json.dumps()` converts JSON text to dict.
# answer: false
# json.dumps() converts dict to JSON text
# json.dump() writes to a file
# json.loads() converts JSON text to dict
# json.load() reads from a file

# ------------------------------------------------------------part02_yaml_for_configs.md--------------------------------------------------------

# 1. Create `service.yaml` with `name`, `port`, `healthcheck_path`, then read and print values.
import yaml
service = {
    "name": "myapp",
    "port": 8080,
    "healthcheck_path": "/health"
}
with open("service.yaml", "w") as f:
    yaml.safe_dump(service, f)
print(service)

# 2. Load a YAML dict and print all keys.
Loaded_service = {}
with open("service.yaml", "r") as f:
    Loaded_service = yaml.safe_load(f)

print(Loaded_service.keys())


# 3. Change replicas from 2 to 4 and write back to a new file

Loaded_service["replicas"] = 4
with open("service_new.yaml", "w") as f:
    yaml.safe_dump(Loaded_service, f)

with open("service_new.yaml", "r") as f:
    new_service = yaml.safe_load(f)

print(new_service)

# 1. **Concept:** Why is YAML popular in DevOps tooling?
# answer: YAML is a human-readable data serialization language that is commonly used in configuration files and deployment manifests. It is popular in DevOps tooling because it is easy to read and write, and it is a good format for configuration files.

# 2. **Recall:** Which function is recommended for reading YAML safely?
# answer: yaml.safe_load()

# 3. **Code read:** What type do you usually get after `yaml.safe_load(...)` for a mapping document?
# answer: dict 

# 4. **Scenario:** YAML parse fails with indentation error. What is first thing to inspect?
# answer: the indentation of the YAML file

# 5. **True/False:** Tabs and spaces are interchangeable in YAML indentation.
# answer: false
# Tabs and spaces are not interchangeable in YAML indentation. Tabs are not allowed in YAML indentation.

# ------------------------------------------------------------part03_environment_variables_and_dotenv.md--------------------------------------------------------
# 1. Create `.env` with `API_KEY=demo123` and `ENV=dev`.
# API_KEY = "demo123"
# with open(".env", "w") as f:
#     f.write(f"API_KEY={API_KEY}")


# with open(".env", "r") as f:
#     print(f.read())

# 3. Remove `API_KEY` and observe fail-fast error with `os.environ["API_KEY"]`.
# comment API_KEY creation 
from dotenv import load_dotenv
import os
load_dotenv()

print(os.environ["API_KEY"])

# --------------------------------------------------------------- part04_argparse_and_exit_codes.md ---------------------------------------------------------------

# 1. Build `cli_demo.py` with `--host`, `--port`, `--env`.
from argparse import ArgumentParser
parser = ArgumentParser( description="Health check tool")
parser.add_argument("--host", required=True)
parser.add_argument("--port", type=int, default=80)
parser.add_argument("--env", choices=["dev", "staging", "prod"], default="dev")
args = parser.parse_args()
print(args.host, args.port, args.env)

# ------------------------------
# Notes
# sys is a built-in Python module for interpreter/system-level things.

# Common use:

# sys.argv -> command-line arguments
# sys.exit(code) -> end program with an exit code
# sys.path -> import search paths
# For your CLI assignment, sys.exit(...) is important for CI/scripts.

# sys.exit(0) = success
# sys.exit(1) (or non-zero) = failure
# Why needed:

# Humans can read printed messages, but CI/CD tools check exit code.
# If validation fails and you still exit 0, CI thinks everything passed.
# -----------------------------
import sys
# 2. Add validation for port range 1..65535.
if args.port < 1 or args.port > 65535:
    print(f"Invalid port: {args.port}")
    sys.exit(1)
else:
    print(f"Valid port: {args.port}")
    sys.exit(0)

# 3. Run with valid and invalid values, check exit code in shell

# python3 simple.py --host localhost --port 8080 --env dev
# echo $?

# --------------------------------------------------------------- part05_pathlib_os_shutil.md ---------------------------------------------------------------
# 1. Create a script that lists all `.yaml` files in a folder.
from pathlib import Path 
base = Path(__file__).resolve().parent  # folder of simple.py
for file in base.glob("*.yaml"):
    print(file.name)

#  OR

base1 = Path("./").glob("*.yaml")
for file in base1 :
    print(file)

# 2. Copy one file to a backup folder with `copy2`.
import shutil
from shutil import copy2
Path("backup").mkdir(exist_ok=True)
copy2("service.yaml",  "backup/service.yaml")


# 3. Archive the folder and print archive path.
from shutil import make_archive
shutil.make_archive("archive", "zip", "backup")
archive_path = Path("archive.zip")
print(f"Archive path: {archive_path}")

# --------------------------------------------------------------- part06_subprocess_safe_execution.md ---------------------------------------------------------------


# 1. Write `run(["python", "--version"])` and print output.
from subprocess import run
result = run(["python3", "--version"], capture_output=True, text=True)
print(f"Python version: {result.stdout.strip()}")

print("stdout:", result.stdout.strip())
print("stderr:", result.stderr.strip())

# 2. Add timeout and test with a short command.
result2 = run(["python3", "--version"], capture_output=True, text=True, timeout=1)
print(f"Python version: {result2.stdout.strip()}")
print("stdout:", result2.stdout.strip())
print("stderr:", result2.stderr.strip())

# 3. Try a failing command and catch `subprocess.CalledProcessError`.
result3 = run(["python", "--version"], capture_output=True, text=True, timeout=1)
print(f"Python version: {result3.stdout.strip()}")
print("stdout:", result3.stdout.strip())
print("stderr:", result3.stderr.strip())


# 1. **Concept:** Why is `shell=True` risky with untrusted input?
# answer: It allows for shell injection, where an attacker can inject commands into the shell.
# 2. **Recall:** Which flag raises exception on non-zero command exit?
# answer: `check=True`
# 3. **Code read:** What does `capture_output=True, text=True` provide?
# answer: It captures the stdout and stderr of the command and returns them as strings.
# 4. **Scenario:** Command hangs in CI. Which parameter helps protect pipeline time?
# answer: `timeout=`
# 5. **True/False:** `subprocess.run` always returns only stdout and never stderr.
# answer: False

























# import yaml

# required_keys = ["name", "replicas", "port", "labels"]

# def validate(val):
#     errors = []

#     if not isinstance(val, dict):
#         return ["Config must be a YAML mapping/object"]

#     # required keys
#     for key in required_keys:
#         if key not in val:
#             errors.append(f"Missing key: {key}")

#     # replicas
#     if "replicas" in val:
#         if not isinstance(val["replicas"], int):
#             errors.append("replicas must be an integer")
#         elif val["replicas"] <= 0:
#             errors.append("replicas must be greater than 0")

#     # port
#     if "port" in val:
#         if not isinstance(val["port"], int):
#             errors.append("port must be an integer")
#         elif not (1 <= val["port"] <= 65535):
#             errors.append("port must be between 1 and 65535")

#     return errors


# file_name = "/mnt/c/Learn_Python/session2/session2_parts/config.yaml"

# try:
#     with open(file_name, "r", encoding="utf-8") as f:
#         config = yaml.safe_load(f)

#     errors = validate(config)

#     if errors:
#         print("Errors found:")
#         for e in errors:
#             print("-", e)
#     else:
#         print("Config is valid")

# except FileNotFoundError:
#     print(f"File not found: {file_name}")
# except yaml.YAMLError as e:
#     print(f"Invalid YAML: {e}")