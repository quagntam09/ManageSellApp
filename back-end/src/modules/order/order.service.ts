import { Injectable } from '@nestjs/common';
import { CreateOrderDto } from './dto/create-order.dto';
import { UpdateOrderDto } from './dto/update-order.dto';
import { PrismaService } from '../prisma/prisma.service';
@Injectable()
export class OrderService {
  constructor(private readonly prisma: PrismaService) {}
  async creatOrder(data: CreateOrderDto){
    const {userId, address, shippingFee, totalPrice, products} = data;
    
    return this.prisma.order.create({
      data: {
        user: {connect: {id: userId}},
        address,
        shippingFee: +shippingFee,
        totalPrice: +totalPrice,
        orderDetails:{
          create: products.map(p => (
            {
              quantity: p.quantity,
              product: {connect: {id: p.productId}}
            }))
        }
      },
      include:{
        orderDetails:{
          include: {
            product: true
          }
        }
      }
    })

  }

  async getAllOrder(){
    return this.prisma.order.findMany();
  }

  async getOrderById(id: string){
    return this.prisma.order.findUnique({where: {id}});
  }
}
