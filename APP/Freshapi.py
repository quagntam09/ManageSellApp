import requests
import json
from DataApi import apiApp

url = apiApp()
data =         {
            "userId": "004",
            "address": "tphcm",
            "totalPrice": 50000,
            "shippingFee": 5500,
            "products": [
                {   
                    "productId": "cm9n09kpe0000vcn827z7fm9v",
                    "quantity": 10
                }
            ]
        }
request = requests.get(url=url.apiOrder, json= data)

print(request.json())


