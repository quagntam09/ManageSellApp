import tkinter as tk
from PIL import Image, ImageTk
from ClassApp import DanhSachProduct
from ttkbootstrap.scrolled import ScrolledFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ứng dụng mua bán hàng online")
        self.geometry("1800x800")
        self.DanhSachSanPham = DanhSachProduct()

        # Thanh điều hướng trên cùng
        nav_bar = tk.Frame(self, bg="#cccccc")
        nav_bar.pack(side="top", fill="x")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (ProductFrame, AccountFrame, ProductDetailFrame):
            frame = F(self.container, self)
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.frames[F] = frame

        # Navigation buttons
        btn_product = tk.Button(nav_bar, text="Sản phẩm", command=lambda: self.show_frame(ProductFrame))
        btn_account = tk.Button(nav_bar, text="Tài khoản", command=lambda: self.show_frame(AccountFrame))
        for btn in (btn_product, btn_account):
            btn.pack(side="left", padx=5, pady=5)

        self.show_frame(ProductFrame)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class ProductDetailFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.img_label = tk.Label(self)
        self.img_label.pack(pady=10)

        self.name_label = tk.Label(self, font=("Arial", 16))
        self.name_label.pack(pady=10)

        self.price_label = tk.Label(self, font=("Arial", 14))
        self.price_label.pack(pady=10)

        self.btn_back = tk.Button(self, text="Quay lại", command=lambda: controller.show_frame(ProductFrame))
        self.btn_back.pack(pady=20)

    def update_product(self, product):
        self.name_label.config(text=f"Tên sản phẩm: {product['name']}")
        self.price_label.config(text=f"Giá: {product['price']}")
        try:
            img = Image.open(product['img']).resize((200, 200))
            self.photo = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.photo)
            self.img_label.image = self.photo
        except:
            self.img_label.config(image="", text="Không có ảnh")

class ProductFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        category_bar = tk.Frame(self, bg="#cccccc")
        category_bar.pack(side="top", fill="x")
        btn_thietbidientu = tk.Button(category_bar, text="Thiết bị điện tử", command=self.showThietBiDienTu)
        btn_thoitrang = tk.Button(category_bar, text="Thời trang", command=self.showThoiTrang)
        btn_all = tk.Button(category_bar, text="Hiện toàn bộ", command=self.showAll)
        for btn in (btn_thietbidientu, btn_thoitrang, btn_all):
            btn.pack(side="left", padx=5, pady=5)

        self.DanhSachSanPham = controller.DanhSachSanPham
        self.images = []

        self.scrollframe = ScrolledFrame(self, autohide=True)
        self.scrollframe.pack(fill="both", expand=True, padx=20, pady=10)

        self.container = self.scrollframe
        self.render_products(self.DanhSachSanPham.get_all())

    def render_products(self, product_list):
        for widget in self.container.winfo_children():
            widget.destroy()

        for product in product_list:
            item_frame = tk.Frame(self.container, bd=1, relief="solid", padx=10, pady=10)
            item_frame.pack(fill="x", pady=5)

            try:
                img = Image.open(product['img']).resize((80, 80))
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)
                img_label = tk.Label(item_frame, image=photo)
                img_label.grid(row=0, column=0, rowspan=2, padx=5, sticky="nw")
            except:
                tk.Label(item_frame, text="Không có ảnh").grid(row=0, column=0)

            name_label = tk.Label(item_frame, text=product['name'], font=("Arial", 12, "bold"),
                                  wraplength=400, justify="left")
            name_label.grid(row=0, column=1, sticky="w", padx=10)

            # Nhấn vào frame là mở chi tiết
            img_label.bind("<Button-1>", lambda e, p=product: self.open_product_detail(p))
            item_frame.bind("<Button-1>", lambda e, p=product: self.open_product_detail(p))
            name_label.bind("<Button-1>", lambda e, p=product: self.open_product_detail(p))

    def open_product_detail(self, product):
        detail_frame = self.controller.frames[ProductDetailFrame]
        detail_frame.update_product(product)
        self.controller.show_frame(ProductDetailFrame)

    def showThietBiDienTu(self):
        filtered = [p for p in self.DanhSachSanPham.get_all() if p["categoryId"] == "001"]
        self.render_products(filtered)

    def showThoiTrang(self):
        filtered = [p for p in self.DanhSachSanPham.get_all() if p["categoryId"] == "002"]
        self.render_products(filtered)
    def showAll(self):
        filtered = [p for p in self.DanhSachSanPham.get_all()]
        self.render_products(filtered)
class AccountFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Tài khoản", font=("Arial", 24)).pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
