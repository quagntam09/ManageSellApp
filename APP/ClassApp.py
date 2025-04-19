import requests
class User:
    def __init__(self, id, user_name, email, phone, password):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.vip = 0
        self.password = password
        self.apiUser = "http://localhost:3000/user"
    def to_dict_creat(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password
        }
    def to_dict_update(self):
        return {
            "user_name": self.user_name,
            "email": self.email,
            "phone": self.phone,
            "vip": self.vip
        }
    def GetUserById(self):
        request = requests.get(self.apiUser + f"/{self.id}")
        return request.json()
    def CreateUser(self):   
        request = requests.post(self.apiUser,json= self.to_dict_creat())
        return request.json()
    def UpdateUser(self, newdata = {}):
        self.user_name = newdata.get("user_name", self.user_name)
        self.email = newdata.get("email", self.email)
        self.phone = newdata.get("phone", self.phone)
        self.vip = newdata.get("vip", self.phone)

        request = requests.patch(self.apiUser + f"/{self.id}", json= self.to_dict_update())
        return request.json()
    def DeleteUser(self):
        request = requests.delete(self.apiUser + f"/{self.id}")
        return request.json()

class Shipper:
    def __init__(self, id, shipper_name, phone, password):
        self.id = id
        self.shipper_name = shipper_name
        self.phone = phone
        self.password = password
        self.apiShipper = "http://localhost:3000/shipper"
        self.deliveredOrders = 0
        self.totalEarnings = 0
    def to_dict_creat(self):
        return {
            "id": self.id,
            "shipper_name": self.shipper_name,
            "phone": self.phone,
            "password": self.password
        }
    def to_dict_update(self):
        return {
            "shipper_name": self.shipper_name,
            "phone": self.phone,
            "deliveredOrders": self.deliveredOrders,
            "totalEarnings": self.totalEarnings
        }
    def GetShipperById(self):
        request = requests.get(self.apiShipper + f"/{self.id}")
        return request.json()
    def CreateShipper(self):   
        request = requests.post(self.apiShipper,json= self.to_dict_creat())
        return request.json()
    def UpdateShipper(self, newdata = {}):
        self.shipper_name= newdata.get("shipper_name", self.shipper_name)
        self.phone = newdata.get("phone", self.phone)
        self.deliveredOrders = newdata.get("deliveredOrders", self.deliveredOrders)
        self.totalEarnings = newdata.get("totalEarnings", self.totalEarnings)


        request = requests.patch(self.apiShipper + f"/{self.id}", json= self.to_dict_update())
        return request.json()
    def DeleteShipper(self):
        request = requests.delete(self.apiShipper + f"/{self.id}")
        return request.json()

