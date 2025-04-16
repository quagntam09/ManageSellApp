import { Module } from '@nestjs/common';
import { OrderDetailService } from './order-detail.service';
import { OrderDetailController } from './order-detail.controller';
import { PrismaService } from '../prisma/prisma.service';

@Module({
  controllers: [OrderDetailController],
  providers: [OrderDetailService, PrismaService],
})
export class OrderDetailModule {}
