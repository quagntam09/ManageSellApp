import requests
import json

# Định nghĩa URL cho GET và POST
urlUser = 'http://localhost:3000/user/100'
urlShipper = 'http://localhost:3000/shipper'

data = {
    "id": "003",
    "shipper_name": "Nguyen Phuc Kien",
    "phone": "0909091",
    "password": "password123"
}
request = requests.post(url=urlShipper, json= data)

print(request.json())


