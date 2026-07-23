import requests

payload = {
    "model": "llama3:8b",
    "prompt": "Say Hello",
    "stream": False
}

response = requests.post(
    "http://localhost:11434/api/generate",
    json=payload
)

print(response.status_code)
print(response.json())