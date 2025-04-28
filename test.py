import requests

data = {
    "id": "999",
    "password": "0123",
    "role_id": "1001"
}
res = requests.post("http://localhost:3000/account", json= data)

data = res.json()
print(data)