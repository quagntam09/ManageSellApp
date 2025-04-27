import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service'; // Đảm bảo bạn có PrismaService trong project
import { CreateOrderDto } from './dto/create-order.dto';  // Import DTO của bạn ở đây

@Injectable()
export class OrderService {
  constructor(private readonly prisma: PrismaService) {}

  async creatOrder(data: CreateOrderDto) {
    const { userId, address, shippingFee, totalPrice, products } = data;

    // Kiểm tra dữ liệu trước khi tạo đơn hàng
    if (!Array.isArray(products) || products.length === 0) {
      throw new Error('Products array cannot be empty.');
    }

    // Tạo đơn hàng
    return this.prisma.order.create({
      data: {
        user: {
          connect: {
            id: userId,  // Kết nối với người dùng qua userId
          },
        },
        address,
        shippingFee: Number(shippingFee),  // Chuyển đổi sang số nếu cần
        totalPrice: Number(totalPrice),  // Chuyển đổi sang số nếu cần
        orderDetails: {
          create: products.map((p) => ({
            quantity: p.quantity,  // Sử dụng số lượng của sản phẩm
            product: {
              connect: {
                id: p.productId,  // Kết nối với sản phẩm qua productId
              },
            },
          })),
        },
      },
      include: {
        orderDetails: {
          include: {
            product: true,  // Bao gồm thông tin sản phẩm liên kết với chi tiết đơn hàng
          },
        },
      },
    });
  }
  async getAllOrder(){
    return this.prisma.order.findMany();
  }
}
