import { Injectable } from '@nestjs/common';
import { CreateOrderDto } from './dto/create-order.dto';
import { UpdateOrderDto } from './dto/update-order.dto';
import { PrismaService } from '../prisma/prisma.service';
@Injectable()
export class OrderService {
  constructor(private readonly prisma: PrismaService) {}
  createOrder(createOrderDto: CreateOrderDto) {
    return this.prisma.order.create({
      data: createOrderDto,
    });
  }
  findAllOrder() {
    return this.prisma.order.findMany({
      include: { orderItems: true },
    });
  }
  findOneOrder(id: number) {
    return this.prisma.order.findUnique({
      where: { id },
      include: { orderItems: true },
    });
  }
  findOrderByUserId(userId: number) {
    return this.prisma.order.findMany({
      where: { userId },
      include: { orderItems: true },
    });
  }
}
