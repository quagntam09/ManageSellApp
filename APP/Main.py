import tkinter as tk
from Login_Register import LoginWinDow, RegisterWindow

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
        self.root.title("Ứng dụng Mua Bán Hàng Online")
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

