"""
Part 06 practice: logging placeholders, argv slicing, *args, **kwargs.

How to run:
1) python part06.py
2) python part06.py web-01 web-02 db-01
"""

from __future__ import annotations

import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)


def demo_logging_placeholders() -> None:
    """Show what '%s: %s' means in logging."""
    host = "web-01"
    error = "timeout"

    # Visualize this as: "Failed ___: ___"
    # 1st %s -> host, 2nd %s -> error
    log.error("Failed %s: %s", host, error)

    # Try changing values above and run again.


def demo_argv_slice() -> list[str]:
    """Return user arguments only (skip script name)."""
    print("\n--- argv visualization ---")
    print("sys.argv full list: ", sys.argv)
    print("sys.argv[0] (script):", sys.argv[0])
    print("sys.argv[1:] (inputs):", sys.argv[1:])
    return sys.argv[1:]


def sum_numbers(*args: int) -> int:
    """Accept any count of positional numbers and return total."""
    print("\n--- *args visualization ---")
    print("args value:", args)  # tuple
    return sum(args)


def deploy_service(service: str, **kwargs: str) -> None:
    """Accept fixed service name + flexible named options."""
    print("\n--- **kwargs visualization ---")
    print("service:", service)
    print("kwargs value:", kwargs)  # dict
    for key, value in kwargs.items():
        print(f"{key} = {value}")


def run_exercises() -> None:
    """Run tiny exercises with expected behavior."""
    print("Practice file for: %s, argv[1:], *args, **kwargs")
    print("-------------------------------------------------")

    # Exercise 1: logging placeholders
    print("\nExercise 1: logging placeholder '%s: %s'")
    demo_logging_placeholders()

    # Exercise 2: argv slicing
    print("\nExercise 2: sys.argv[1:]")
    hosts = demo_argv_slice()
    print("Host count from argv[1:]:", len(hosts))

    # Exercise 3: *args
    print("\nExercise 3: *args")
    total = sum_numbers(10, 20, 30)
    print("sum_numbers(10, 20, 30) =", total)  # expected: 60

    # Exercise 4: **kwargs
    print("\nExercise 4: **kwargs")
    deploy_service(
        "billing-api",
        env="prod",
        region="us-east-1",
        retries="3",
        timeout="30s",
    )

    # Exercise 5: combine fixed + *args + **kwargs
    print("\nExercise 5: think task")
    print("Q: Why is 'service' a normal parameter, but options are **kwargs?")
    print("A: service is mandatory and fixed; options are flexible and optional.")


if __name__ == "__main__":
    run_exercises()
# 1. Build an f-string that prints `retry 2/5` using variables `attempt` and `total`.
attempt = 2
total = 5
print(f"retry {attempt}/{total}")

# 2. Write a function that takes a list of hosts and returns a list of hosts that are active.
def get_active_hosts(hosts: list[str]) -> list[str]:
    return [host for host in hosts if host.startswith("active-")]

# 3. Write a function that takes a list of hosts and returns a list of hosts that are inactive.
def get_inactive_hosts(hosts: list[str]) -> list[str]:
    return [host for host in hosts if not host.startswith("active-")]

get_active_hosts(["active-web-01", "inactive-web-02", "active-web-03"]) # Output: ["active-web-01", "active-web-03"]
get_inactive_hosts(["active-web-01", "inactive-web-02", "active-web-03"]) # Output: ["inactive-web-02"]


# 4. From `ports = [80, 443, 8080]`, create a new list of strings like `"port_80"` using a comprehension.
ports = [80, 443, 8080]
port_strings = [f"port_{port}" for port in ports]
print(port_strings) # Output: ["port_80", "port_443", "port_8080"]

## Test questions — Part 6

# 1. **Concept:** Why use `if __name__ == "__main__":` instead of putting all code at the top level of the file?
#Answer: To prevent the code from being run when the file is imported as a module.
#Example:
#if __name__ == "__main__":
#    print("This will only run when the file is run directly.")
#else:
#    print("This will run when the file is imported as a module.")

# 2. **Recall:** What is `sys.argv[0]` typically?
#Answer: The path to the script that is being run.
#Example:
#print(sys.argv[0]) # Output: /path/to/script.py    

# 3. **Code read:** What does `[x * 2 for x in [1, 2, 3] if x > 1]` evaluate to?
#Answer: [4, 6]
#Example:
#print([x * 2 for x in [1, 2, 3] if x > 1]) # Output: [4, 6]

# 4. **Scenario:** You need a multiline log message with variables. Is f-string inside triple-quoted `"""` valid in Python?
#Answer: Yes, f-string inside triple-quoted `"""` is valid in Python.
#Example:
#print(f"""This is a multiline log message with variables: {var1} and {var2}""") # Output: This is a multiline log message with variables: var1 and var2

# 5. **True/False:** List comprehensions can always be replaced by a for-loop; comprehensions are mainly for readability and sometimes speed.
#Answer: True
#Example:
#print([x * 2 for x in [1, 2, 3] if x > 1]) # Output: [4, 6]

