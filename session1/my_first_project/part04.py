def greet(name: str)-> str:
    return f"My first project {name}"

message = greet("Hello world!")
print(message)

# 1. Write a function `port_string(port: int) -> str` that returns `"port is 443"` (use an f-string).
def port_string(port: int) -> str:
    return f"port is {port}"

print(port_string(443))

# 2. Write a function `max_retry(default: int = 3) -> int` that returns the default — call it with no args and print the result.
def max_retry(default: int = 3) -> int:
    return default

print(max_retry())

# 3. Add a one-line docstring to one of your functions.
def port_string(port: int) -> str:
    """Returns the port number as a string"""
    return f"port is {port}"

print(port_string(443))

# 4. Write a function `health_url(host: str, use_https: bool = True) -> str` that returns a health-check URL for the given host.
def health_url(host: str, use_https: bool = True) -> str:
    """Returns a health-check URL for the given host"""
    return f"https://{host}/health"

print(health_url("localhost"))