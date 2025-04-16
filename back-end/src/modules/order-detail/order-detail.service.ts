import { Injectable } from '@nestjs/common';
import { CreateOrderDetailDto } from './dto/create-order-detail.dto';
import { UpdateOrderDetailDto } from './dto/update-order-detail.dto';
import { PrismaService } from '../prisma/prisma.service';
@Injectable()
export class OrderDetailService {
  constructor(private readonly prisma: PrismaService) {}
  createOrderDetail(createOrderDetailDto: CreateOrderDetailDto) {
    return this.prisma.orderDetail.create({
      data: createOrderDetailDto,
    });
  }
  findAllOrderDetail() {
    return this.prisma.orderDetail.findMany({
      include: { order: true, product: true },
    });
  }
  findOneOrderDetail(id: number) {
    return this.prisma.orderDetail.findUnique({
      where: { id },
      include: { order: true, product: true },
    });
  }
  updateOrderDetail(id: number, updateOrderDetailDto: UpdateOrderDetailDto) {
    return this.prisma.orderDetail.update({
      where: { id },
      data: updateOrderDetailDto,
    });
  }
}
