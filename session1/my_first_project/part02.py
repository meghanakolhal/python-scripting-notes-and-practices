# 1. Create a `list` of three fake server names. Print the second server.
servers = ["server1", "server2", "server3" ]
print(servers[1])

# 2. Create a `dict` with keys `environment`, `version` and values you choose. Print `environment`.
config = { "environment": "production", "version": "1.0.0" }
print(config["environment"])

# 3. Given `hosts = ["a", "a", "b"]`, convert to a `set` and print it — how many items?
hosts = ["a", "a", "b"]
hosts_set = set(hosts)
print(hosts_set)
print(len(hosts_set))

# 4. Write a `for` loop that prints each host in `["a", "b", "c"]` prefixed with `HOST: `.
hosts = ["a", "b", "c"]
for host in hosts:
    print(f"HOST: {host}")

# 5. Write an `if` that prints `"prod"` only if variable `env` equals `"production"` (case-sensitive).
env = "dev"
if env == "production":
    print("prod")
else:
    print("not prod")