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
        label_options = {"bg": "#f0f2f5", "fg": "#333", "font": ("Times", 11)}
        entry_options = {"width": 30, "bg": "white", "bd": 1, "relief": "solid", "font": ("Times", 11)}
        
        row = 0
        self.id_error = tk.Label(self, text="", fg="red", bg="#f0f2f5", font=("Times", 8))
        self.id_error.grid(row=row, column=1, columnspan=2, sticky="w", padx=(0, 20))
        row += 1
        tk.Label(self, text="Tài Khoản:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        self.id_entry = tk.Entry(self, **entry_options)
        self.id_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        row += 1
        self.pass_error = tk.Label(self, text="", fg="red", bg="#f0f2f5", font=("Times", 8))
        self.pass_error.grid(row=row, column=1, columnspan=2, sticky="w", padx=(0, 20))
        row += 1
        tk.Label(self, text="Mật khẩu:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        self.password_entry = tk.Entry(self, show="*", **entry_options)
        self.password_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        # row += 1
        # tk.Label(self, text="Số điện thoại:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        # self.phone_entry = tk.Entry(self, **entry_options)
        # self.phone_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        # row += 1
        # tk.Label(self, text="Tên người dùng:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        # self.name_entry = tk.Entry(self, **entry_options)
        # self.name_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        # row += 1
        # tk.Label(self, text="Email:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        # self.email_entry = tk.Entry(self, **entry_options)
        # self.email_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        row += 1
        self.register_button = tk.Button(self, text="Đăng ký", command=self.register,
                                         bg="#4CAF50", fg="white", font=("Times", 11, "bold"), bd=0, padx=10, pady=5)
        self.register_button.grid(row=row, column=0, columnspan=3, pady=(15,5))
        

        row += 1
        tk.Button(self, text="Quay lại", command=lambda: self.controller.show_frame("OpenWindow"),
                  bg="#2196F3", fg="white", font=("Times", 11, "bold"), bd=0, padx=10, pady=5).grid(row=row, column=0, columnspan=3, pady=(0,15))

    def register(self):
        has_error = False
        id = self.id_entry.get()
        if not id:
            self.id_error.config(text="Vui lòng nhập tài khoản")
            has_error = True
        else:
            self.id_error.config(text="")
        password = self.password_entry.get()
        if not password:
            self.pass_error.config(text="Vui lòng điền mật khẩu")
            has_error = True
        else:
            self.pass_error.config(text="")

        account = {
            "id": id,
            "password": password,
            "role_id": "1001"
        }
        res = requests.post("http://localhost:3000/account", json= account)
        data = res.json()
        print(data)
        if not has_error:
            messagebox.showwarning("Thông báo", "Đăng kí thành công!")
            return
        # phone = self.phone_entry.get()
        # name = self.name_entry.get()
        # email = self.email_entry.get()
        # if not id or not password or not phone or not name:
        #     messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ các trường.")
        #     return
        # if not IsEmail(email):
        #     messagebox.showwarning("Sai định dạng", "Email không đúng!")
        # if not IsPhone(phone):
        #     messagebox.showwarning("Sai định dạng", "Số điện thoại không đúng!")

        # try:
        #     res = requests.post("http://localhost:3000/account", json={
        #         "id": id,
        #         "password": password,
        #         "phone": phone,
        #         "name": name,
        #         "role_id": "1001"
        #         ""
        #     })

        #     if res.status_code == 201:
        #         messagebox.showinfo("Thành công", "Đăng ký thành công!")
        #     else:
        #         messagebox.showerror("Thất bại", f"Lỗi: {res.json().get('message')}")
        # except Exception as e:
        #     messagebox.showerror("Lỗi kết nối", str(e))

