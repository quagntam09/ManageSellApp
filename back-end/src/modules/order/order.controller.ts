import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { OrderService } from './order.service';
import { CreateOrderDto } from './dto/create-order.dto';
import { get } from 'http';

@Controller('order')
export class OrderController {
  constructor(private readonly orderService: OrderService) {}
  @Post()
  createOrder(@Body() data: CreateOrderDto){
    return this.orderService.creatOrder(data);
  }
  @Get(":id")
  getOrderById(@Param("id") id: string){
    return this.orderService.getOrderById(id);
  }
  @Get()
  getAllOrder(){
    return this.orderService.getAllOrder();
  }
}
