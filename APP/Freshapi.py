import requests
import json

# Định nghĩa URL cho GET và POST
urlgetUser = 'http://localhost:3000/user'
urlpostUser = 'http://localhost:3000/user'

# Dữ liệu gửi lên khi tạo người dùng
data = {
    "id": "003",
    "username": "Nguyen Van D",  # không phải "username"
    "vip": 2,
    "email": "333@gmail.com",
    "password": "password123"
}


# Gửi yêu cầu POST để tạo người dùng mới
response = requests.post(urlpostUser, json= data)  # Gửi dưới dạng JSON
if response.status_code == 201:  # Kiểm tra xem người dùng đã được tạo thành công hay chưa
    print("Người dùng đã được tạo thành công.")
else:
    print(f"Yêu cầu POST không thành công. Mã lỗi: {response.status_code}")

# Gửi yêu cầu GET để lấy danh sách người dùng
response = requests.get(urlgetUser)

# Kiểm tra mã trạng thái trả về
if response.status_code == 200:
    data = response.json()  # Chuyển dữ liệu JSON nhận được thành dictionary
    print(data)
else:
    print(f"Yêu cầu GET không thành công. Mã lỗi: {response.status_code}")
