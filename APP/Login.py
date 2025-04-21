import requests
import tkinter as tk
from tkinter import messagebox,ttk
import bcrypt

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

            if is_correct and id == data.get("id"):
                messagebox.showinfo("Login Success", "Welcome")
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

        tk.Label(self, text="ID:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
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

        self.roles_display = {
            "Người dùng": "user",
            "Shipper": "shipper"
        }

        row += 1
        tk.Label(self, text="Vai trò:").grid(row=row, column=0, sticky="e", padx=10, pady=5)
        self.role_combo = ttk.Combobox(self, values=list(self.roles_display.keys()), state="readonly")
        self.role_combo.current(0)
        self.role_combo.grid(row=row, column=1, columnspan=2)

        row += 1
        self.register_button = tk.Button(self, text="Đăng ký", command=self.register)
        self.register_button.grid(row=row, column=0, columnspan=3, pady=10)

        row += 1
        tk.Button(self, text="Quay lại", command=lambda: self.controller.show_frame("OpenWindow")).grid(row=row, column=0, columnspan=3)

    def register(self):
        id = self.id_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        role_label = self.role_combo.get()
        name = self.name_entry.get()

        if not id or not password or not phone or not name:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ các trường.")
            return

        role_value = self.roles_display.get(role_label)
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


class OpenWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        tk.Label(self, text="Chào bạn!").pack(pady=20)
        tk.Button(self, text="Đăng Nhập", command=lambda: controller.show_frame("LoginWinDow")).pack(pady=10)
        tk.Button(self, text="Đăng Ký", command=lambda: controller.show_frame("RegisterWindow")).pack(pady=10)

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Tkinter Login/Register")
        self.frames = {}

        for F in (OpenWindow, LoginWinDow, RegisterWindow):
            frame = F(root, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("OpenWindow")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()

