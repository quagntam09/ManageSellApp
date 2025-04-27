import requests
import tkinter as tk
from tkinter import messagebox,ttk
import bcrypt
from UserWindow import UserWindow
class LoginWinDow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Id:").pack(pady=(20, 5))
        self.Id_entry = tk.Entry(self)
        self.Id_entry.pack()

        tk.Label(self, text="Password:").pack(pady=(10, 5))
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=15)
        tk.Button(self, text="Quay lại", command=lambda: self.controller.show_frame("OpenWindow")).pack()


    def login(self):
        id = self.Id_entry.get()
        password = self.password_entry.get()

        try:
            res = requests.get(f"http://localhost:3000/account/{id}")
            data = res.json()

            hashed_password = data.get("password").encode('utf-8')
            is_correct = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
            accountId = data.get("id")
            if is_correct and id == accountId:
                messagebox.showinfo("Login Success", "Welcome")
                res = requests.get(f"http://localhost:3000/user/{accountId}")
                user = res.json()
                print(user)
                if(data.get("roleId") == "1001"):
                    frame = UserWindow(self.master, self.controller, user)
                    self.controller.frames["UserWindow"] = frame
                    frame.grid(row=0, column=0, sticky="nsew") 
                    self.controller.show_frame("UserWindow")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Không thể kết nối đến server: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi xảy ra: {e}")

class RegisterWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.build_ui()

    def build_ui(self):
        row = 0 

        tk.Label(self, text="Tài Khoản:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        tk.Label(self, text="Mật khẩu:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        tk.Label(self, text="Số điện thoại:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        tk.Label(self, text="Tên người dùng:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=row, column=1, columnspan=2)


        row += 1
        self.register_button = tk.Button(self, text="Đăng ký", command=self.register)
        self.register_button.grid(row=row, column=0, columnspan=3, pady=10)

        row += 1
        tk.Button(self, text="Quay lại", command=lambda: self.controller.show_frame("OpenWindow")).grid(row=row, column=0, columnspan=3)

    def register(self):
        id = self.id_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        name = self.name_entry.get()

        if not id or not password or not phone or not name:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ các trường.")
            return
        try:
            res = requests.post("http://localhost:3000/account", json={
                "id": id,
                "password": password,
                "phone": phone,
                "name": name,
                "role_id": "1001"
            })

            if res.status_code == 201:
                messagebox.showinfo("Thành công", "Đăng ký thành công!")
            else:
                messagebox.showerror("Thất bại", f"Lỗi: {res.json().get('message')}")
        except Exception as e:
            messagebox.showerror("Lỗi kết nối", str(e))

