
from ClassApp import User, Shipper

user =Shipper("001", "Hua quang tam", "0865324192", "password123")
respoint = user.UpdateShipper({"shipper_name": "HHH", "deliveredOrders": 10})
print(user.shipper_name, user.deliveredOrders)

print(respoint)


