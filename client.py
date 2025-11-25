import requests

BASE_URL = "http://localhost:8000"

# 1. Testar /status
response_status = requests.get(f"{BASE_URL}/status")
print("Resposta do /status:")
print(response_status.json())

# 2. Enviar dados ao /eco
payload = {
    "message": "Olá servidor!",
    "value": 123
}

response_eco = requests.post(f"{BASE_URL}/eco", json=payload)
print("\nResposta do /eco:")
print(response_eco.json())
