import { Injectable } from '@nestjs/common';
import { CreateOrderDetailDto } from './dto/create-order-detail.dto';
import { UpdateOrderDetailDto } from './dto/update-order-detail.dto';
import { PrismaService } from '../prisma/prisma.service';
@Injectable()
export class OrderDetailService {
  constructor(private readonly prisma: PrismaService) {}
 
}
