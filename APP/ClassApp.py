import requests
import json
class User:
    def __init__(self, id, user_name, phone, vip, email, accountId):
        self.id = id
        self.user_name = user_name
        self.phone = phone
        self.vip = vip
        self.email = email
        self.accountId = accountId
    
    
    # def to_dict_update(self):
    #     return {
    #         "user_name": self.user_name,
    #         "phone": self.phone,
    #         "vip": self.vip
    #     }
    # def update(self):
    #     response = requests.patch(f"http://localhost:3000/user/{self.id}", json= self.to_dict_update())
    #     if response.status_code == 200:
    #         print("Update User Thành Công!")
    #     else:
    #         print("Update User Gặp Lỗi!")

class DanhSachUser:
    def __init__(self):
        self.Users = []
        self.LayDBTuServer()
        self.ghiJsonUser()
    def ghiJsonUser(self):
        with open("users.json","w", encoding= 'utf-8') as f:
            data = [user.__dict__ for user in self.Users]
            json.dump(data, f, indent= 4, ensure_ascii= False)
    def LayDBTuServer(self):
        res = requests.get(f"http://localhost:3000/user")
        if res.status_code == 200:
            print("Get User Thành Công!")
            data = res.json()
            # print(res.json())
            self.Users = [User(**us) for us in data]
        else:
            print("Get User Gặp Lỗi!")

class Account:
    def __init__(self, id, password, roleId):
        self.id = id
        self.password = password
        self.roleId = roleId
class DanhSachAccount:
    def __init__(self):
        self.Accounts = []
        self.LayDBTuServer()
        self.ghiJsonAccount()
    def ghiJsonAccount(self):
        with open("accounts.json","w", encoding= 'utf-8') as f:
            data = [account.__dict__ for account in self.Accounts]
            json.dump(data, f, indent= 4, ensure_ascii= False)
    # def docJsonAccount(self):
    #     with open("accounts.json", "r", encoding= 'utf-8') as f:
    #         data = json.load(f)
    #         self.Accounts = [Account(**ac) for ac in data]
    def LayDBTuServer(self):
        res = requests.get(f"http://localhost:3000/account")
        if res.status_code == 200:
            print("Get Accounts Thành Công!")
            data = res.json()
            # print(res.json())
            self.Accounts = [Account(**ac) for ac in data]
        else:
            print("Get Accounts Gặp Lỗi!")



class Product:
    def __init__(self, id, name, description, price, stock, categoryId, img, rate):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.categoryId = categoryId
        self.img = img
        self.rate = rate
    def to_dict(self):
        return {
            "name": self.name,
            "img": self.img
        }
class DanhSachProduct:
    def __init__(self):
        self.ProDucts = []
        self.layDBTuServer()
        self.ghiJsonProduct()
    def ghiJsonProduct(self):
        with open("products.json","w", encoding= 'utf-8') as f:
            data = [p.__dict__ for p in self.ProDucts]
            json.dump(data, f, indent= 4, ensure_ascii= False)
    def layDBTuServer(self):
        res = requests.get("http://localhost:3000/product")
        if res.status_code == 200:
            print("Lấy products thành công!")
            data = res.json()
            self.ProDucts = [Product(**p) for p in data]
        else:
            print("Lỗi get product!")
    def get_all(self):
        return [p.to_dict() for p in self.ProDucts]
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
        


