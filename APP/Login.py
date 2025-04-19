import requests
import tkinter as tk
from tkinter import messagebox,ttk
import bcrypt
from PIL import Image, ImageTk  # Cần cài pillow nếu chưa có
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        tk.Label(root, text="Id:").pack(pady=(20, 5))
        self.Id_entry = tk.Entry(root)
        self.Id_entry.pack()

        tk.Label(root, text="Password:").pack(pady=(10, 5))
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Login", command=self.login).pack(pady=15)

    def login(self):
        id = self.Id_entry.get()
        password = self.password_entry.get()

        try:
            res = requests.get(f"http://localhost:3000/account/{id}")
            data = res.json()

            hashed_password = data.get("password").encode('utf-8')
            is_correct = bcrypt.checkpw(password.encode('utf-8'), hashed_password)

            if is_correct and id == data.get("id"):
                messagebox.showinfo("Login Success", "Welcome")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Không thể kết nối đến server: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi xảy ra: {e}")

class RegisterWindow:
    def __init__(self, master):
        self.master = master
        master.title("Đăng ký tài khoản")
        row = 0
        tk.Label(master, text="ID:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.id_entry = tk.Entry(master)
        self.id_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        tk.Label(master, text="Mật khẩu:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        tk.Label(master, text="Số điện thoại:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        tk.Label(master, text="Tên người dùng:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=row, column=1, columnspan=2)

        self.roles_display = {
            "Người dùng": "user",
            "Shipper": "shipper"
        }

        row += 1
        tk.Label(master, text="Vai trò:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.role_combo = ttk.Combobox(master, values=list(self.roles_display.keys()), state="readonly")
        self.role_combo.current(0)
        self.role_combo.grid(row=row, column=1, columnspan=2)

        row += 1
        self.register_button = tk.Button(master, text="Đăng ký", command=self.register)
        self.register_button.grid(row=row, column=0, columnspan=3, pady=10)
    def register(self):
        id = self.id_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        role_label = self.role_combo.get()  # Ví dụ: "Người dùng"
        name = self.name_entry.get()

        if not id or not password or not phone or not name:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ các trường.")
            return

        # Mapping hiển thị → backend value
        role_value = self.roles_display.get(role_label)  # "user" hoặc "shipper"

        # Mapping role → id
        role_id_map = {"user": "1001", "shipper": "1002"}
        role_id = role_id_map.get(role_value)

        if not role_id:
            messagebox.showerror("Lỗi vai trò", "Vai trò không hợp lệ.")
            return

        try:
            res = requests.post("http://localhost:3000/account", json={
                "id": id,
                "password": password,
                "phone": phone,
                "name": name,
                "role_id": role_id
            })

            if res.status_code == 201:
                messagebox.showinfo("Thành công", "Đăng ký thành công!")
            else:
                messagebox.showerror("Thất bại", f"Lỗi: {res.json().get('message')}")
        except Exception as e:
            messagebox.showerror("Lỗi kết nối", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterWindow(root)
    root.mainloop()
