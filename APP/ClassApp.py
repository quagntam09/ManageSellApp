import requests
import json
class User:
    def __init__(self, id, user_name, phone, vip, accountId):
        self.id = id
        self.user_name = user_name
        self.phone = phone
        self.vip = vip
    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "phone": self.phone,
            "vip": self.vip
        }
    def to_dict_update(self):
        return {
            "user_name": self.user_name,
            "phone": self.phone,
            "vip": self.vip
        }
    def update(self):
        response = requests.patch(f"http://localhost:3000/user/{self.id}", json= self.to_dict_update())
        if response.status_code == 200:
            print("Update User Thành Công!")
        else:
            print("Update User Gặp Lỗi!")



# class Shipper:
#     def __init__(self, id, shipper_name, phone, password):
#         self.id = id
#         self.shipper_name = shipper_name
#         self.phone = phone
#         self.password = password
#         self.apiShipper = "http://localhost:3000/shipper"
#         self.deliveredOrders = 0
#         self.totalEarnings = 0
#     def to_dict_creat(self):
#         return {
#             "id": self.id,
#             "shipper_name": self.shipper_name,
#             "phone": self.phone,
#             "password": self.password
#         }
#     def to_dict_update(self):
#         return {
#             "shipper_name": self.shipper_name,
#             "phone": self.phone,
#             "deliveredOrders": self.deliveredOrders,
#             "totalEarnings": self.totalEarnings
#         }
#     def GetShipperById(self):
#         request = requests.get(self.apiShipper + f"/{self.id}")
#         return request.json()
#     def CreateShipper(self):   
#         request = requests.post(self.apiShipper,json= self.to_dict_creat())
#         return request.json()
#     def UpdateShipper(self, newdata = {}):
#         self.shipper_name= newdata.get("shipper_name", self.shipper_name)
#         self.phone = newdata.get("phone", self.phone)
#         self.deliveredOrders = newdata.get("deliveredOrders", self.deliveredOrders)
#         self.totalEarnings = newdata.get("totalEarnings", self.totalEarnings)


#         request = requests.patch(self.apiShipper + f"/{self.id}", json= self.to_dict_update())
#         return request.json()
#     def DeleteShipper(self):
#         request = requests.delete(self.apiShipper + f"/{self.id}")
#         return request.json()



class Product:
    def __init__(self, id, name, description, price, stock, category):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category": self.category
        }
    
class Order:
    def __init__(self, id, createdAt, address, status, totalPrice, shippingFee, paymentStatus, userId, shipperId):
        self.id = id
        self.userId = userId
        self.ShipperId = shipperId
        self.address = address
        self.totalPrice = totalPrice
        self.shippingFee = shippingFee
        self.creatAt = createdAt
        self.status = status
        self.paymentStatus = paymentStatus

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "shipperId": self.ShipperId,
            "address": self.address,
            "totalPrice": self.totalPrice,
            "shippingFee": self.shippingFee,
            "creatAt": self.creatAt,
            "status": self.status,
            "paymentStatus": self.paymentStatus
        }
    
    # def updateStatus(self, id):
    #     response = requests.patch(f"http://localhost:3000/order/Status/{id}")
    #     if response.status_code == 200:
    #         print("Cập nhật trạng thái thành công!")

class DanhSach:
    def __init__(self, name):
        self.danhsach = []
        self.name = name

    def GhiDanhSachVaoJson(self):
        with open(f"{self.name}.json", "w", encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self.danhsach], f, indent=4, ensure_ascii=False)

    def LayDanhSachProDuctTuDB(self):
        response = requests.get(f"http://localhost:3000/{self.name}")
        if response.status_code == 200:
            data = response.json()
            self.danhsach = [Product(**item) for item in data]
            self.GhiDanhSachVaoJson()
        else:
            print("Lỗi khi lấy dữ liệu từ DB:", response.status_code)
    def LayDanhSachUserTuDB(self):
        response = requests.get(f"http://localhost:3000/{self.name}")
        if response.status_code == 200:
            data = response.json()
            self.danhsach = [User(**item) for item in data]
            self.GhiDanhSachVaoJson()
        else:
            print("Lỗi khi lấy dữ liệu từ DB:", response.status_code)

    def LayDanhSachOrderTuDB(self):
        response = requests.get(f"http://localhost:3000/{self.name}")
        if response.status_code == 200:
            data = response.json()
            print(data)
            self.danhsach = [Order(**item) for item in data]
            self.GhiDanhSachVaoJson()
        else:
            print("Lỗi khi lấy dữ liệu từ DB:", response.status_code)
    def UpdateDuLieuProductVaoDB(self):
        with open(f"{self.name}.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            self.danhsach = [Product(**product) for product in data]
        dataDict = [x.to_dict() for x in self.danhsach]
        requests.patch(f"http://localhost:3000/{self.name}", json= dataDict)
        


