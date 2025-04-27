import tkinter as tk
from tkinter import ttk
from ClassApp import DanhSach, Order
import requests
import json

class UserWindow(tk.Frame):
    def __init__(self, master, controller, user):
        super().__init__(master)
        self.controller = controller
        self.DanhSachHangHoa = DanhSach("product")
        self.DanhSachHangHoa.LayDanhSachProDuctTuDB()
        self.user = user
        self.gio_hang = []  # [(hang, so_luong)]
        self.widgets_hang = {}  # Lưu lại widget theo từng hàng hóa
        self.DanhSachOrder = DanhSach("order")
        self.BangHangHoa()
        self.BangGioHang()

    def BangHangHoa(self):
        self.frameHangHoa = ttk.LabelFrame(self, text="Danh sách hàng hóa")
        self.frameHangHoa.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for hang in self.DanhSachHangHoa.danhsach:
            self.TaoDongHangHoa(hang)

    def TaoDongHangHoa(self, hang):
        frame_row = ttk.Frame(self.frameHangHoa)
        frame_row.pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(frame_row, text=hang.name, width=20).pack(side=tk.LEFT)
        ttk.Label(frame_row, text=hang.description, width=30).pack(side=tk.LEFT)
        stock_label = ttk.Label(frame_row, text=f"{hang.stock}", width=10)
        stock_label.pack(side=tk.LEFT)
        ttk.Label(frame_row, text=f"{hang.price}đ", width=10).pack(side=tk.LEFT)

        spin = tk.Spinbox(frame_row, from_=0, to=hang.stock, width=5)
        spin.pack(side=tk.LEFT)

        def them_vao_gio():
            sl = int(spin.get())
            if 0 < sl <= hang.stock:
                self.gio_hang.append((hang, sl))
                hang.stock -= sl
                spin.config(to=hang.stock)
                stock_label.config(text=str(hang.stock))
                spin.delete(0, tk.END)
                spin.insert(0, 0)
                self.CapNhatGioHang()

        ttk.Button(frame_row, text="Xác nhận", command=them_vao_gio).pack(side=tk.LEFT, padx=5)
        self.widgets_hang[hang] = {
            "spin": spin,
            "stock_label": stock_label
        }


    def BangGioHang(self):
        self.frameGio = ttk.LabelFrame(self, text="Giỏ hàng")
        self.frameGio.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        cols = ("Tên hàng", "Mô Tả", "Số lượng mua", "Giá")
        self.treeGioHang = ttk.Treeview(self.frameGio, columns=cols, show="headings", selectmode="browse")
        for col in cols:
            self.treeGioHang.heading(col, text=col)
            self.treeGioHang.column(col, width=120)

        self.treeGioHang.pack(fill=tk.BOTH, expand=True)

        btn_xoa = ttk.Button(self.frameGio, text="Xóa khỏi giỏ hàng", command=self.XoaKhoiGio)
        btn_xoa.pack(pady=5)
        btn_dathang = ttk.Button(self.frameGio, text="Xác nhận đặt hàng", command=self.DatHang)
        btn_dathang.pack(pady=5)

    def CapNhatGioHang(self):
        for row in self.treeGioHang.get_children():
            self.treeGioHang.delete(row)

        for hang, sl in self.gio_hang:
            self.treeGioHang.insert("", "end", values=(hang.name, hang.description, sl, hang.price))
    def DatHang(self):
        if(len(self.gio_hang) > 0):
            products = []
            totalprice = 0
            for hang  in self.gio_hang:
                print(hang[0].to_dict())
                totalprice += hang[0].price * hang[1]
                products.append({"productId": hang[0].id , "quantity": hang[1]})
            shippingfee = totalprice * 0.1
            hoadon = {
                "userId": self.user.get("id"),
                "address": "none",
                "totalPrice": totalprice,
                "shippingFee": shippingfee,
                "products": products
            }
            res = requests.post(f"http://localhost:3000/order", json= hoadon)
            self.DanhSachOrder.LayDanhSachOrderTuDB()
            # print(tmp.__dict__)
            # with open("order.json", "w", encoding= 'utf-8') as f:
            #     json.dump(hoadon, f, indent= 4, ensure_ascii= False)
            # print("Xuất hóa đơn thành công!")
            
            # print(tmp.__dict__)
            # print(hoadon)
            print(self.user)
            self.DanhSachHangHoa.GhiDanhSachVaoJson()
            self.gio_hang.clear()
            self.CapNhatGioHang()
            self.DanhSachHangHoa.UpdateDuLieuProductVaoDB()
            print("Update thành công!")
            print("Đặt hàng thành công!")
        else:
            print("không có hàng trong giỏ hàng!")

    def XoaKhoiGio(self):
        if(len(self.gio_hang) > 0):
            selected = self.treeGioHang.selection()
            if not selected:
                print("Vui lòng chọn hàng muốn xóa khỏi giỏ!")
                return 

            item = self.treeGioHang.item(selected[0])
            ten_hang = item["values"][0]
            so_luong = item["values"][2]

            for i, (hang, sl) in enumerate(self.gio_hang):
                if hang.name == ten_hang and sl == so_luong:
                    hang.stock += sl
                    del self.gio_hang[i]
                    widgets = self.widgets_hang.get(hang)
                    if widgets:
                        widgets["stock_label"].config(text=str(hang.stock))
                        widgets["spin"].config(to=hang.stock)
                    break
            self.CapNhatGioHang()
            print("Xóa hàng thành công")
        else:
            print("Giỏ hàng trống!")
