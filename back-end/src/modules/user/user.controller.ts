import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}
  @Post()
  createUser(@Body() data: CreateUserDto){
    return this.userService.createUser(data)
  }
  @Get()
  getAllUser(){
    return this.userService.getAllUser();
  }
}
