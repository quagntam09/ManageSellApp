import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { OrderService } from './order.service';
import { CreateOrderDto } from './dto/create-order.dto';
import { UpdateOrderDto } from './dto/update-order.dto';

@Controller('order')
export class OrderController {
  constructor(private readonly orderService: OrderService) {}
  @Post()
  createOrder(@Body() createOrderDto: CreateOrderDto) {
    return this.orderService.createOrder(createOrderDto);
  }
  @Get()
  findAllOrder() {
    return this.orderService.findAllOrder();
  }
  @Get(':id')
  findOneOrder(@Param('id') id: string) {
    return this.orderService.findOneOrder(+id);
  }
  @Get('user/:userId')
  findOrderByUserId(@Param('userId') userId: string) {
    return this.orderService.findOrderByUserId(+userId);
  }
}
