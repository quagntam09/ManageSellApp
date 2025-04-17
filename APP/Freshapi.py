import requests
import json

# Định nghĩa URL cho GET và POST
urlUser = 'http://localhost:3000/user/100'
urlShipper = 'http://localhost:3000/shipper/002'

dataUse = {
    "user_name": "Nguyen Kien 1",
    "vip": 3
}
request = requests.delete(url=urlUser)

print(request.json())


