import json

raw = '{"service": "api", "port": 8080, "healthy": true}'
data = json.loads(raw)  # converts the raw string into a dictionary
print(raw) # Output: {"service": "api", "port": 8080, "healthy": true}
print(type(data))      # dict
print(data) # Output: {'service': 'api', 'port': 8080, 'healthy': True}
print(data["service"]) # api

# 1. Create a Python dict with keys `app`, `version`, `replicas` and print it as pretty JSON.
dict = {
    "app" : "myapp",
    "version" : "v1",
    "replicas" : "2"
}
